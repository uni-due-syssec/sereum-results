true_positive: yes  
fp_type: None  
source: yes

# Notes

This is a clear unconditional re-entrancy attack. The contract is pretty
clearly vulnerable. However, this seems to be another test contract. The
vulnerabe contract has source and contains two implementations of basically the
same functionality.  One is vulnerable to re-entrancy attacks, while the other
is not.

In the transaction that we observed, the attacker seems to try to hide her
attack by wrapping it inside a constructor of another contract and immediately
selfdestructing the attack contracts after the attack was successful.


This function is vulnerable and actually exploited.

```solidity
function get() public payable
{
    bool success;
    bytes memory data;
/// external call
    (success, data) = msg.sender.call.value(_balances[msg.sender])("");

    if (!success) 
    {
        revert("withdrawal failed");
    }

/// state update
    _balances[msg.sender] = 0;
}
```


This function is not vulnerable (but also broken).

```solidity
function withdraw() public payable
{
    bool success;
    bytes memory data;

/// state update
    _balances[msg.sender] = 0;

/// then the external call
    (success, data) = msg.sender.call.value(_balances[msg.sender])("");

    if (!success) 
    {
        revert("withdrawal failed");
    }
}
```

