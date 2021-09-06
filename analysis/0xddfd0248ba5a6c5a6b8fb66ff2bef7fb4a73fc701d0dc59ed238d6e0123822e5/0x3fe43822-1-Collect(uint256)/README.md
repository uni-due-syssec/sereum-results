true_positive: yes  
fp_type: None  
source: yes

# Notes

Re-entrancy in the `Collect` function. It is a typical check, call, state
update pattern as seen in many re-entrancy vulnerabilities.

```solidity
/// CHECK
if(balances[msg.sender]>=MinSum && balances[msg.sender]>=_am)
{
/// CALL
    if(msg.sender.call.value(_am)())
    {
/// STATE UPDATE
        balances[msg.sender]-=_am;
        Log.AddMessage(msg.sender,_am,"Collect");
    }
}
```
