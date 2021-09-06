true_positive: no  
fp_type: 4  
source: yes

# Notes

It seems there are two major contracts involved. First the `payService`
contract is called. This then calls into the `paymentContract`. Depending on
some conditions, this contract will then issue a token transfer by calling the
`EtheremonToken` contract (re-entered).

Transferring tokens twice doesn't work with Sereum. The `require` statements
lock the variables to the nested invocation by the `paymentContract`. 

In this case, there is no problem, because before transferring Tokens the
second time (in the top-level invocation) all the checks are performed again.
If the user wouldn't have enough tokens due to the re-entered invocation of
`transfer`, then the checks would revert the transaction instead of
transferring Tokens again.


```solidity
/// from contract EtheremonToken
function payService(uint _tokens, uint32 _type, string _text, uint64 _param1, uint64 _param2, uint64 _param3, uint64 _param4, uint64 _param5, uint64 _param6) isActive requirePaymentContract external {
    if (_tokens > balanceOf[msg.sender])
        revert();
/// this is the contract at 0xcdf...
    PaymentInterface payment = PaymentInterface(paymentContract);
/// external call, which re-enters the 
    uint deductedTokens = payment.payService(msg.sender, _tokens, _type, _text, _param1, _param2, _param3, _param4, _param5, _param6);
    if (deductedTokens == 0 || deductedTokens > _tokens)
        revert();
/// Safe, because the checks are performed again when the internal function
/// _transfer is called.
    _transfer(msg.sender, inGameRewardAddress, deductedTokens);
}
```


```solidity
/// from contract TokenERC20
function transfer(address _to, uint256 _value) public {
    _transfer(msg.sender, _to, _value);
}
/// from contract EtheremonToken
function _transfer(address _from, address _to, uint _value) internal {
    require (_to != 0x0);
    require (balanceOf[_from] >= _value);
    require (balanceOf[_to] + _value > balanceOf[_to]);
    require(!frozenAccount[_from]);
    require(!frozenAccount[_to]);
    balanceOf[_from] -= _value;
    balanceOf[_to] += _value;
    Transfer(_from, _to, _value);
}
```
