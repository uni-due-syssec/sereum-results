# transaction 0xfd00ed2dfa30be48547fe1294d5363a36e1aa23335a2bee0fd0073279b6f02f4

[etherscan.io/tx](https://etherscan.io/tx/0xfd00ed2dfa30be48547fe1294d5363a36e1aa23335a2bee0fd0073279b6f02f4)


### Contract at 2399c2c86fbf159d81b7cb90014038f31080b4fc

* [etherscan](https://etherscan.io/address/0x2399c2c86fbf159d81b7cb90014038f31080b4fc)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x2399c2c86fbf159d81b7cb90014038f31080b4fc)
* contract didn't send ether
* received 3.1328346e-10 ether (313283460 wei)
    * from 0x3f4a95380874eb1b1e878b1571209e656c4a227c; 0 wei
    * from 0xd2e16a20dd7b1ae54fb0312209784478d069c7b0; 313283460 wei
* called functions:
    * `getTotalSupply()`, fsig: c4e41b22, ether: 0 wei, count: 1
    * fsig: 3a1f074f, ether: 0 wei, count: 1
    * `split(uint256)`, fsig: dbceb005, ether: 0 wei, count: 1
    * `fallback`, fsig: , ether: 313283460 wei, count: 21


### Contract at 3f4a95380874eb1b1e878b1571209e656c4a227c

* [etherscan](https://etherscan.io/address/0x3f4a95380874eb1b1e878b1571209e656c4a227c)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x3f4a95380874eb1b1e878b1571209e656c4a227c)
* sent 1.157920892373162e+59 ether (115792089237316195423570985008687907853269984665640564039457583949386783850274 wei)
    * to 0xbb9bc244d798123fde783fcc1c72d3bb8c189413; 0 wei
    * to 0xd2e16a20dd7b1ae54fb0312209784478d069c7b0; 115792089237316195423570985008687907853269984665640564039457583949386783850274 wei
    * to 0x2399c2c86fbf159d81b7cb90014038f31080b4fc; 0 wei
* contract wasn't called


### Contract at 0f112f6698b23dd44060eca9c09f4b3463feb07f

* [etherscan](https://etherscan.io/address/0x0f112f6698b23dd44060eca9c09f4b3463feb07f)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x0f112f6698b23dd44060eca9c09f4b3463feb07f)
* contract didn't send ether
* received 0.021698768590141 ether (21698768590140999 wei)
    * from 0xd2e16a20dd7b1ae54fb0312209784478d069c7b0; 21698768590140999 wei
* called functions:
    * `fallback`, fsig: , ether: 21698768590140999 wei, count: 21


### Contract at 39771e2d34eda36a49ff4fa4194d7fcb839165da

* [etherscan](https://etherscan.io/address/0x39771e2d34eda36a49ff4fa4194d7fcb839165da)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x39771e2d34eda36a49ff4fa4194d7fcb839165da)
* contract didn't send ether
* received 0.10849384295070492 ether (108493842950704932 wei)
    * from 0xbb9bc244d798123fde783fcc1c72d3bb8c189413; 108493842950704932 wei
* called functions:
    * `createTokenProxy(address)`, fsig: baac5300, ether: 108493842950704932 wei, count: 21


### Contract at d2e16a20dd7b1ae54fb0312209784478d069c7b0

* [etherscan](https://etherscan.io/address/0xd2e16a20dd7b1ae54fb0312209784478d069c7b0)
* [contract-library](https://contract-library.com/contracts/Ethereum/0xd2e16a20dd7b1ae54fb0312209784478d069c7b0)
* sent 0.02169876890342446 ether (21698768903424459 wei)
    * to 0x2399c2c86fbf159d81b7cb90014038f31080b4fc; 313283460 wei
    * to 0x0f112f6698b23dd44060eca9c09f4b3463feb07f; 21698768590140999 wei
* received 1.157920892373162e+59 ether (115792089237316195423570985008687907853269984665640564039457583949386783850274 wei)
    * from 0x3f4a95380874eb1b1e878b1571209e656c4a227c; 115792089237316195423570985008687907853269984665640564039457583949386783850274 wei
    * from 0xbb9bc244d798123fde783fcc1c72d3bb8c189413; 0 wei
* called functions:
    * `accumulatedInput()`, fsig: d2cc718f, ether: 0 wei, count: 45
    * `fallback`, fsig: , ether: 115792089237316195423570985008687907853269984665640564039457583949386783850274 wei, count: 1
    * `payOut(address,uint256)`, fsig: 0221038a, ether: 0 wei, count: 21


### Contract at bb9bc244d798123fde783fcc1c72d3bb8c189413

**flagged vulnerable**

* [etherscan](https://etherscan.io/address/0xbb9bc244d798123fde783fcc1c72d3bb8c189413)
* [contract-library](https://contract-library.com/contracts/Ethereum/0xbb9bc244d798123fde783fcc1c72d3bb8c189413)
* sent 0.10849384295070492 ether (108493842950704932 wei)
    * to 0xd2e16a20dd7b1ae54fb0312209784478d069c7b0; 0 wei
    * to 0x39771e2d34eda36a49ff4fa4194d7fcb839165da; 108493842950704932 wei
* didn't receive any ether
* called functions:
    * `proposals(uint256)`, fsig: 013cf08b, ether: 0 wei, count: 2
    * `balanceOf(address)`, fsig: 70a08231, ether: 0 wei, count: 8
    * `totalSupply()`, fsig: 18160ddd, ether: 0 wei, count: 4
    * `paidOut(address)`, fsig: 81f03fcb, ether: 0 wei, count: 6
    * `getNewDAOAddress(uint256)`, fsig: be7c29c1, ether: 0 wei, count: 4
    * fsig: a9059cbb, ether: 0 wei, count: 2
        * `many_msg_babbage(bytes1)`
        * `transfer(address,uint256)`
    * `rewardAccount()`, fsig: 0e708203, ether: 0 wei, count: 1
    * `splitDAO(uint256,address)`, fsig: 82661dc4, ether: 0 wei, count: 21


### Contract at 79f09717c5b352078234832e5737651ddb333548

* [etherscan](https://etherscan.io/address/0x79f09717c5b352078234832e5737651ddb333548)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x79f09717c5b352078234832e5737651ddb333548)
* contract didn't send ether
* contract wasn't called

# Notes


```

    CALL(0xbb9bc244d798123fde783fcc1c72d3bb8c189413 (@ splitDAO(uint256,address))
     | ether=0
     | input=mem[96:164]{82661dc400000000000000000000000000000000000000000000000000000000
     | 0000011100000000000000000000000079f09717c5b352078234832e5737651d
     | db333548}
     | ...) | 0x2399c2C86FBF159d81b7cb90014038f31080B4FC @ 0xa12 == 2578

[...]

        SLOAD(addr=203b745457dddbb5160b857d091601c44e8520f7b33d2e4bf1a9f0c135c38b31) => value=0000000000000000000000000000000000000000000002864c4dc489cc45cbc1                     | 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413 @ 0x605 == 1541
        PUSH1                                                                                                                                                                      | 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413 @ 0x2828 == 10280
         |-> WRITELOCK 
         | to ≥2:JUMPI storage 0xd9e27dc2d71d1e06cbbad89a5e25c1cc7977b84abf2a31414d95f284fe792bc0 contract 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
         | to ≥2:JUMPI storage 0xecaa4a597dd5995be76dd75525926def3c1ec44bed28b7ad06fd0887980948c6 contract 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
         | to ≥2:JUMPI storage 0x0000000000000000000000000000000000000000000000000000000000000016 contract 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
[this is the first write-lock of the later offending variable]
         | to ≥2:JUMPI storage 0x44eeadcf26734914699b0fe44d9d2e12bd9af3403c6666b13eccc9f7b87e7a03 contract 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413

[...]

                CALL(0xbb9bc244d798123fde783fcc1c72d3bb8c189413 (@ splitDAO(uint256,address))
                 | ether=0
                 | input=mem[96:164]{82661dc400000000000000000000000000000000000000000000000000000000
                 | 0000011100000000000000000000000079f09717c5b352078234832e5737651d
                 | db333548}
                 | ...) | 0x2399c2C86FBF159d81b7cb90014038f31080B4FC @ 0x11e == 286


[...]

[deep in the recursive call chain:]
...  SLOAD(addr=203b745457dddbb5160b857d091601c44e8520f7b33d2e4bf1a9f0c135c38b31) => value=0000000000000000000000000000000000000000000002864c4dc489cc45cbc1 | 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413 @ 0x605 == 1541
...  SLOAD(addr=44eeadcf26734914699b0fe44d9d2e12bd9af3403c6666b13eccc9f7b87e7a03) => value=00000000000000000000000000000000000000000000008b89b6aeeb7da4e922 | 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413 @ 0x2953 == 10579
...  PUSH1 | 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413 @ 0x2969 == 10601
...  |-> WRITELOCK 
...  | to ≥65:JUMPI storage 0x203b745457dddbb5160b857d091601c44e8520f7b33d2e4bf1a9f0c135c38b31 contract 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
...  | to ≥65:JUMPI storage 0xecaa4a597dd5995be76dd75525926def3c1ec44bed28b7ad06fd0887980948c6 contract 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
[this is the offending variable]
...  | to ≥65:JUMPI storage 0x44eeadcf26734914699b0fe44d9d2e12bd9af3403c6666b13eccc9f7b87e7a03 contract 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
...  | to ≥65:JUMPI storage 0xd9e27dc2d71d1e06cbbad89a5e25c1cc7977b84abf2a31414d95f284fe792bc0 contract 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413

[...]

[deep in the recursive call chain:]
...   SLOAD(addr=44eeadcf26734914699b0fe44d9d2e12bd9af3403c6666b13eccc9f7b87e7a03) => value=0000000000000000000000000000000000000000000000000000000000000000 | 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413 @ 0x292d == 10541
...   SSTORE(addr=44eeadcf26734914699b0fe44d9d2e12bd9af3403c6666b13eccc9f7b87e7a03, value=0000000000000000000000000000000000000000000000000000000000e3a274) | 0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413 @ 0x2931 == 10545

```
