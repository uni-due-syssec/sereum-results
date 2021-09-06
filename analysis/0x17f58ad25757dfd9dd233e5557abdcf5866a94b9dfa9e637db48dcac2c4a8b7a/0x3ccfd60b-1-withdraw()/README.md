true_positive: no  
fp_type: 4  
source: yes

# Notes


Does seem to be a false positive. The analyzed transaction has a rather
simple callchain:

```
-> OlympusIndex.withdraw()
    -> AsyncWithdraw[0x53400..].freeze()
        -> OlympusIndex.getPrice()
          | write-lock(_total_supply)
[...]
   | write(_total_supply)
```

Both the `AsyncWithdraw` and `OlympusIndex` were created by the same address.
This looks like a simple innocent callback (`getPrice` is a `view` function).
