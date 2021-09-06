# transaction 0x3ad6b1c362da9513700af6a6a124e2243453709963b12c9448eef24ea6069ef9

[etherscan.io/tx](https://etherscan.io/tx/0x3ad6b1c362da9513700af6a6a124e2243453709963b12c9448eef24ea6069ef9)


### Contract at 0x0dabb315fc7b2995185885b3d1058e5c0ebd0943

* [etherscan](https://etherscan.io/address/0x0dabb315fc7b2995185885b3d1058e5c0ebd0943)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x0dabb315fc7b2995185885b3d1058e5c0ebd0943)
* contract didn't send ether
* contract wasn't called


### Contract at 0x0fc53f7c2659a708f46d0c4336eb8c1e0f551307

**flagged vulnerable**

* [etherscan](https://etherscan.io/address/0x0fc53f7c2659a708f46d0c4336eb8c1e0f551307)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x0fc53f7c2659a708f46d0c4336eb8c1e0f551307)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * `receivePlayerInfo(uint256,address,bytes32,uint256)`, fsig: 49cc635d, ether: 0 wei, count: 1


### Contract at 0xf0bb66dcde19eb86dcb8eddf857c10b137b6dbbb

* [etherscan](https://etherscan.io/address/0xf0bb66dcde19eb86dcb8eddf857c10b137b6dbbb)
* [contract-library](https://contract-library.com/contracts/Ethereum/0xf0bb66dcde19eb86dcb8eddf857c10b137b6dbbb)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * `getPlayerID(address)`, fsig: e56556a9, ether: 0 wei, count: 1
    * `getPlayerName(uint256)`, fsig: 82e37b2c, ether: 0 wei, count: 1
    * `getPlayerLAff(uint256)`, fsig: e3c08adf, ether: 0 wei, count: 1

# Notes

Relevant parts of the transaction:

The transaction starts with a call to `buyXid(uint256,uint256)` (0x8f38f309)
with the arguments:
* function_sig `8f38f309`
* uint256 `0000000000000000000000000000000000000000000000000000000000000008`
* uint256 `0000000000000000000000000000000000000000000000000000000000000002`

```
[...]

CALL(0xf0bb66dcde19eb86dcb8eddf857c10b137b6dbbb (@ getPlayerID(address))
 | ether=0
 | input=mem[704:740]{e56556a90000000000000000000000000dabb315fc7b2995185885b3d1058e5c
 | 0ebd0943}
 | ...)                                                                                                                                                        | 0x0fC53f7c2659a708F46D0c4336eb8C1E0f551307 @ 0xa4e == 2638

[...]

    CALL(0xfc53f7c2659a708f46d0c4336eb8c1e0f551307 (@ receivePlayerInfo(uint256,address,bytes32,uint256))
     | ether=0
     | input=mem[128:260]{49cc635d00000000000000000000000000000000000000000000000000000000
     | 000000090000000000000000000000000dabb315fc7b2995185885b3d1058e5c
     | 0ebd094300000000000000000000000000000000000000000000000000000000
     | 0000000000000000000000000000000000000000000000000000000000000000
     | 00000000}
     | ...)                                                                                                                                                | 0xF0bb66DcDe19eb86dCb8eDdf857C10B137B6dBbb @ 0x135d == 4957

[...]

        SLOAD(addr=dcdb48aeab0a526088abf89eddb1a3941b6a115664c6e50f52e8260bded51def) => value=0000000000000000000000000000000000000000000000000000000000000000 | 0x0fC53f7c2659a708F46D0c4336eb8C1E0f551307 @ 0x1af7 == 6903
        PUSH1                                                                                                                                                  | 0x0fC53f7c2659a708F46D0c4336eb8C1E0f551307 @ 0x1b00 == 6912
         |-> WRITELOCK to ≥2:JUMPI storage 0xdcdb48aeab0a526088abf89eddb1a3941b6a115664c6e50f52e8260bded51def contract 0x0fC53f7c2659a708F46D0c4336eb8C1E0f551307
        SSTORE(addr=dcdb48aeab0a526088abf89eddb1a3941b6a115664c6e50f52e8260bded51def, value=0000000000000000000000000000000000000000000000000000000000000009)  | 0x0fC53f7c2659a708F46D0c4336eb8C1E0f551307 @ 0x1b18 == 6936

[...]

SSTORE(addr=dcdb48aeab0a526088abf89eddb1a3941b6a115664c6e50f52e8260bded51def, value=0000000000000000000000000000000000000000000000000000000000000009)          | 0x0fC53f7c2659a708F46D0c4336eb8C1E0f551307 @ 0xbdf == 3039

```


The flagged contract `0x0fc5` calls the `getPlayerID` function of the `0xf0bb`
contract. Then this contract, calls back into the flagged contract `0x0fc5` at
function `receivePlayerInfo(uint256,address,bytes32,uint256)`. 

It seems somehow the `receivePlayerInfo` loads from the storage address
`0xdcb48a...`, which currently contains 0, but also write to the same address
the value 9. This might be related to the value 8, which was passed as argument
to the `buyXid` function call. However, this might be coincidence.

Later the value 9 is again stored into the variable in the `buyXid` call, which
triggers Sereum.
