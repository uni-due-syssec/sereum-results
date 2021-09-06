# transaction 0xe0ff4c18eb1a2431eaa4ad6968c3c91ace0aabee931ede7b0caa81744ab5d1b6

[etherscan.io/tx](https://etherscan.io/tx/0xe0ff4c18eb1a2431eaa4ad6968c3c91ace0aabee931ede7b0caa81744ab5d1b6)


### Contract at 0x66c6ad83b4d732cead084355fa029ce637409bac

* [etherscan](https://etherscan.io/address/0x66c6ad83b4d732cead084355fa029ce637409bac)
* [contract-library](https://contract-library.com/contracts/Ethereum/66c6ad83b4d732cead084355fa029ce637409bac)
* sent 0.2 ether (200000000000000000 wei)
    * to 0x72f60eca0db6811274215694129661151f97982e; 200000000000000000 wei
    * to 0xee695cd3f2f04c04978efae258c8e0b87d19f6ba; 0 wei
* contract wasn't called


### Contract at 0x7bf9a7eeccf2d1de1833b20b6ce9bdddcef58722

* [etherscan](https://etherscan.io/address/0x7bf9a7eeccf2d1de1833b20b6ce9bdddcef58722)
* [contract-library](https://contract-library.com/contracts/Ethereum/7bf9a7eeccf2d1de1833b20b6ce9bdddcef58722)
* contract didn't send ether
* contract wasn't called


### Contract at 0x72f60eca0db6811274215694129661151f97982e

**flagged vulnerable**

* [etherscan](https://etherscan.io/address/0x72f60eca0db6811274215694129661151f97982e)
* [contract-library](https://contract-library.com/contracts/Ethereum/72f60eca0db6811274215694129661151f97982e)
* sent 0.4 ether (400000000000000000 wei)
    * to 0xee695cd3f2f04c04978efae258c8e0b87d19f6ba; 400000000000000000 wei
* received 0.2 ether (200000000000000000 wei)
    * from 0x66c6ad83b4d732cead084355fa029ce637409bac; 200000000000000000 wei
    * from 0xee695cd3f2f04c04978efae258c8e0b87d19f6ba; 0 wei
* called functions:
    * fsig: 58045026, ether: 200000000000000000 wei, count: 1
    * fsig: 856652e9, ether: 0 wei, count: 1
    * `sell(bytes32,uint256)`, fsig: b592de3a, ether: 0 wei, count: 2


### Contract at 0xee695cd3f2f04c04978efae258c8e0b87d19f6ba

* [etherscan](https://etherscan.io/address/0xee695cd3f2f04c04978efae258c8e0b87d19f6ba)
* [contract-library](https://contract-library.com/contracts/Ethereum/ee695cd3f2f04c04978efae258c8e0b87d19f6ba)
* contract didn't send ether
* received 0.4 ether (400000000000000000 wei)
    * from 0x66c6ad83b4d732cead084355fa029ce637409bac; 0 wei
    * from 0x72f60eca0db6811274215694129661151f97982e; 400000000000000000 wei
* called functions:
    * fsig: 34196683, ether: 0 wei, count: 1
    * fsig: 23b872dd, ether: 0 wei, count: 2
        * `gasprice_bit_ether(int128)`
        * `transferFrom(address,address,uint256)`
    * `fallback`, fsig: , ether: 400000000000000000 wei, count: 2
    * fsig: a9059cbb, ether: 0 wei, count: 2
        * `many_msg_babbage(bytes1)`
        * `transfer(bytes4[9],bytes5[6],int48[11])`
        * `transfer(address,uint256)`


### Contract at 0x0000000000000000000000000000000000000002

* [etherscan](https://etherscan.io/address/0x0000000000000000000000000000000000000002)
* [contract-library](https://contract-library.com/contracts/Ethereum/0000000000000000000000000000000000000002)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * fsig: 72f60eca, ether: 0 wei, count: 1

# Notes

