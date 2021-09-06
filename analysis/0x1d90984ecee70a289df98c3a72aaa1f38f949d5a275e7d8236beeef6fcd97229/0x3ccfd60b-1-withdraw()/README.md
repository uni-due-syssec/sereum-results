true_positive: yes  
fp_type: None

# Notes

Pretty clear re-entrancy attack. The pattern is exactly what we are searching
for.


```solidity
function withdraw() {
    msg.sender.call(balances[msg.sender])("")
    balances[msg.sender] = 0
}
```
