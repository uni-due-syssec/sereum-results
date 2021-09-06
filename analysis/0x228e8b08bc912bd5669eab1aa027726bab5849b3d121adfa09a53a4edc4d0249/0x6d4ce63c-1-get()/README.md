true_positive: yes  
fp_type: None

# Notes

Pretty clear re-entrancy attack, due to a withdrawAll pattern (first send
ether, then set balances to 0)

