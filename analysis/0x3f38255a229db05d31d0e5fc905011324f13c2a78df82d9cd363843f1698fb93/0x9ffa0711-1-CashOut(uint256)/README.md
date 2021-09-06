true_positive: yes  
fp_type: None  
source: yes

# Notes

Re-entrancy in the `Cashout` function of the contract. Attacker can re-enter the function to bypass the check on `balances[msg.sender]`.

```Solidity
/// CHECK
if(_am<=balances[msg.sender])
{            
/// CALL
    if(msg.sender.call.value(_am)())  
    {
/// STATE UPDATE
        balances[msg.sender]-=_am;
        TransferLog.AddMessage(msg.sender,_am,"CashOut");
    }
}
```

## Honeypot

Likely a honeypot contract. See the [paper by Torres et al.](https://arxiv.org/abs/1902.06976) for an analysis.

