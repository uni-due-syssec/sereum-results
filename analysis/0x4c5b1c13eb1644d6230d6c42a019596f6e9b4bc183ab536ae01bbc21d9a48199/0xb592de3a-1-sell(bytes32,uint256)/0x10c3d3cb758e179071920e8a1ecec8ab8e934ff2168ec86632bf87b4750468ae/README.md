# transaction 0x10c3d3cb758e179071920e8a1ecec8ab8e934ff2168ec86632bf87b4750468ae

[etherscan.io/tx](https://etherscan.io/tx/0x10c3d3cb758e179071920e8a1ecec8ab8e934ff2168ec86632bf87b4750468ae)


### Contract at 0x7bf9a7eeccf2d1de1833b20b6ce9bdddcef58722

* [etherscan](https://etherscan.io/address/0x7bf9a7eeccf2d1de1833b20b6ce9bdddcef58722)
* [contract-library](https://contract-library.com/contracts/Ethereum/7bf9a7eeccf2d1de1833b20b6ce9bdddcef58722)
* contract didn't send ether
* contract wasn't called


### Contract at 0xd3021787f73b0c33ec5ac048c96622bbea6f91a9

* [etherscan](https://etherscan.io/address/0xd3021787f73b0c33ec5ac048c96622bbea6f91a9)
* [contract-library](https://contract-library.com/contracts/Ethereum/d3021787f73b0c33ec5ac048c96622bbea6f91a9)
* sent 0.25 ether (250000000000000000 wei)
    * to 0xd4cd7c881f5ceece4917d856ce73f510d7d0769e; 250000000000000000 wei
    * to 0xf215edc10d93c9e9ed5ae39ea1152cb68631a313; 0 wei
* contract wasn't called


### Contract at 0x0000000000000000000000000000000000000002

* [etherscan](https://etherscan.io/address/0x0000000000000000000000000000000000000002)
* [contract-library](https://contract-library.com/contracts/Ethereum/0000000000000000000000000000000000000002)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * fsig: d4cd7c88, ether: 0 wei, count: 1


### Contract at 0xf215edc10d93c9e9ed5ae39ea1152cb68631a313

* [etherscan](https://etherscan.io/address/0xf215edc10d93c9e9ed5ae39ea1152cb68631a313)
* [contract-library](https://contract-library.com/contracts/Ethereum/f215edc10d93c9e9ed5ae39ea1152cb68631a313)
* contract didn't send ether
* received 1.25 ether (1250000000000000000 wei)
    * from 0xd3021787f73b0c33ec5ac048c96622bbea6f91a9; 0 wei
    * from 0xd4cd7c881f5ceece4917d856ce73f510d7d0769e; 1250000000000000000 wei
* called functions:
    * fsig: 34196683, ether: 0 wei, count: 1
    * fsig: 23b872dd, ether: 0 wei, count: 5
        * `gasprice_bit_ether(int128)`
        * `transferFrom(address,address,uint256)`
    * `fallback`, fsig: , ether: 1250000000000000000 wei, count: 5
    * fsig: a9059cbb, ether: 0 wei, count: 5
        * `many_msg_babbage(bytes1)`
        * `transfer(bytes4[9],bytes5[6],int48[11])`
        * `transfer(address,uint256)`


### Contract at 0xd4cd7c881f5ceece4917d856ce73f510d7d0769e

**flagged vulnerable**

* [etherscan](https://etherscan.io/address/0xd4cd7c881f5ceece4917d856ce73f510d7d0769e)
* [contract-library](https://contract-library.com/contracts/Ethereum/d4cd7c881f5ceece4917d856ce73f510d7d0769e)
* sent 1.25 ether (1250000000000000000 wei)
    * to 0xf215edc10d93c9e9ed5ae39ea1152cb68631a313; 1250000000000000000 wei
* received 0.25 ether (250000000000000000 wei)
    * from 0xd3021787f73b0c33ec5ac048c96622bbea6f91a9; 250000000000000000 wei
    * from 0xf215edc10d93c9e9ed5ae39ea1152cb68631a313; 0 wei
* called functions:
    * fsig: 58045026, ether: 250000000000000000 wei, count: 1
    * fsig: 856652e9, ether: 0 wei, count: 1
    * `sell(bytes32,uint256)`, fsig: b592de3a, ether: 0 wei, count: 5

# Notes

