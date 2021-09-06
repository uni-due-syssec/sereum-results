true_positive: no  
fp_type: unknown

# Notes

It's hard to tell whether and why this is a false positive, because no source
code is available and the available decompiler don't seem to be able to cope
with a contract of that size.

We can analyze this transaction according to a little public information.
According to the [0xUniverse](https://0xuniverse.com/presskit/) homepage, there
are a couple of contracts involved in this game:

* 0x06a6a7af298129e3a2ab396c9c06f91d3c54aba8 is the "Planets" contract
* 0xe658e6eb4b478da2cf36d9e3712ba0c1b33786a1 is the "Planet Auction v2" contract
* ... (some more, not relevant for this transaction analysis)

In the transaction we flagged, we have a call chain 

```
0x06a6a7af298129e3a2ab396c9c06f91d3c54aba8  (Planets)
 | --> 0xe658e6eb4b478da2cf36d9e3712ba0c1b33786a1 (Planets Auction v2)
        | --> 0x06a6a7af298129e3a2ab396c9c06f91d3c54aba8 (Planets)
```

As both contracts are by the same developers, it is fair to assume that they
don't try to attack each other.

Here is a summary of relevant parts of the execution trace. As we can see the
storage address, which is write-locked by Sereum seems rather arbitrary, which
suggests this is part of a mapping variable. The locked variable stores the
address of the "Planet Auction v2" contract.


```
[...]

CALL(0xe658e6eb4b478da2cf36d9e3712ba0c1b33786a1 (@ 0x0b7edea3)
 | ether=0
 | input=mem[128:196]{0b7edea3000000000000000000000000e50368f101bad9016b62fc61ac520c5c
 | 25a124f300000000000000000000000000000000000000000000000000000000
 | 000086d2}
 | ...)                                                                                                                                                        | 0x06a6a7aF298129E3a2AB396c9C06F91D3C54aBA8 @ 0x12ef == 4847

[...]

    CALL(0x6a6a7af298129e3a2ab396c9c06f91d3c54aba8 (@ transferFrom(address,address,uint256) [0x23b872dd])
     | ether=0
     | input=mem[128:228]{23b872dd000000000000000000000000e658e6eb4b478da2cf36d9e3712ba0c1
     | b33786a1000000000000000000000000e50368f101bad9016b62fc61ac520c5c
     | 25a124f300000000000000000000000000000000000000000000000000000000
     | 000086d2}
     | ...)                                                                                                                                                | 0xe658E6Eb4B478da2Cf36d9e3712ba0c1b33786A1 @ 0x1392 == 5010

[...]
        
        SLOAD(addr=a4c98efb1ba4d1bb1ae9aa108b1694897cda049d1fde034aeb06a942ddc43bfe) => value=0000000000000000000000000000000000000000000000000000000000000000 | 0x06a6a7aF298129E3a2AB396c9C06F91D3C54aBA8 @ 0x3501 == 13569
        POP                                                                                                                                                    | 0x06a6a7aF298129E3a2AB396c9C06F91D3C54aBA8 @ 0x1baf == 7087
         |-> WRITELOCK to ≥2:JUMPI storage 0xa4c98efb1ba4d1bb1ae9aa108b1694897cda049d1fde034aeb06a942ddc43bfe contract 0x06a6a7aF298129E3a2AB396c9C06F91D3C54aBA8

[...]

SSTORE(addr=a4c98efb1ba4d1bb1ae9aa108b1694897cda049d1fde034aeb06a942ddc43bfe,   value=000000000000000000000000e658e6eb4b478da2cf36d9e3712ba0c1b33786a1)          | 0x06a6a7aF298129E3a2AB396c9C06F91D3C54aBA8 @ 0xd38 == 3384
```

