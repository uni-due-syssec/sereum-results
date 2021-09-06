true_positive: yes  
fp_type: None  
source: yes

# Notes

The vulnerability is in the `cancelEscrow` function. The problem is that an
escrow is deleted only after the `buyer` and `arbitrator` are sent their money.
A malicious buyer (or arbitrator for that matter) can re-enter `cancelEscrow`
and the escrow is still valid in this case: the contract will send ether again.

```solidity
function cancelEscrow(
  /**
   * Cancel escrow. Return money to buyer
   */
  bytes16 _tradeID, // The unique ID of the trade
  address _seller, // The selling party of the trade
  address _buyer, // The buying party of the trade
  uint256 _value // 
)  external {
    
    bytes32 _tradeHash = keccak256(_tradeID, _seller, _buyer, _value);
    require(escrows[_tradeHash].exists);
    require(escrows[_tradeHash].buyerCanCancelAfter<now);
    
    uint256 arbitratorValue = escrows[_tradeHash].summ*ARBITRATOR_PERCENT/100;
    uint256 buyerValue =  escrows[_tradeHash].summ - arbitratorValue;
    
/// EXTERNAL CALL
    bool buyerReceivedMoney = escrows[_tradeHash].buyer.call.value(buyerValue)();
    bool arbitratorReceivedMoney = arbitrator.call.value(arbitratorValue)();
    
    if ( buyerReceivedMoney && arbitratorReceivedMoney )
    {    
/// STATE UPDATE
        delete escrows[_tradeHash];
    } else {
        throw;
    }

}
```

