# transaction 0x0b291275b76f78223094ff8f8a986f6ec03f2719b04e1b3df58134464a49d888

[etherscan.io/tx](https://etherscan.io/tx/0x0b291275b76f78223094ff8f8a986f6ec03f2719b04e1b3df58134464a49d888)


### Contract at 0xf79bcc67b915ba1fa11c77670ed6f2b5ae1297a2

* [etherscan](https://etherscan.io/address/0xf79bcc67b915ba1fa11c77670ed6f2b5ae1297a2)
* [contract-library](https://contract-library.com/contracts/Ethereum/f79bcc67b915ba1fa11c77670ed6f2b5ae1297a2)
* sent 0.048125 ether (48125000000000000 wei)
    * to 0x5ebe013e380aa3ca8b56cb60d26e969be516129d; 48125000000000000 wei
    * to 0x4eb6a19ffb643df5cae036735c325f1a81aec8b6; 0 wei
    * to 0xf88a8c89a3ae936a36b426983abdda1f99a4bf18; 0 wei
* received 0.05 ether (50000000000000000 wei)
    * from 0xf88a8c89a3ae936a36b426983abdda1f99a4bf18; 50000000000000000 wei
* called functions:
    * `getCurrentPrice(uint256)`, fsig: c55d0f56, ether: 0 wei, count: 1
    * `bid(uint256,address)`, fsig: 9f04996d, ether: 50000000000000000 wei, count: 1


### Contract at 0x4eb6a19ffb643df5cae036735c325f1a81aec8b6

* [etherscan](https://etherscan.io/address/0x4eb6a19ffb643df5cae036735c325f1a81aec8b6)
* [contract-library](https://contract-library.com/contracts/Ethereum/4eb6a19ffb643df5cae036735c325f1a81aec8b6)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * `fallback`, fsig: , ether: 0 wei, count: 1


### Contract at 0xf88a8c89a3ae936a36b426983abdda1f99a4bf18

**flagged vulnerable**

* [etherscan](https://etherscan.io/address/0xf88a8c89a3ae936a36b426983abdda1f99a4bf18)
* [contract-library](https://contract-library.com/contracts/Ethereum/f88a8c89a3ae936a36b426983abdda1f99a4bf18)
* sent 0.05 ether (50000000000000000 wei)
    * to 0xf79bcc67b915ba1fa11c77670ed6f2b5ae1297a2; 50000000000000000 wei
* didn't receive any ether
* called functions:
    * fsig: a9059cbb, ether: 0 wei, count: 1
        * `many_msg_babbage(bytes1)`
        * `transfer(bytes4[9],bytes5[6],int48[11])`
        * `transfer(address,uint256)`


### Contract at 0x5ebe013e380aa3ca8b56cb60d26e969be516129d

* [etherscan](https://etherscan.io/address/0x5ebe013e380aa3ca8b56cb60d26e969be516129d)
* [contract-library](https://contract-library.com/contracts/Ethereum/5ebe013e380aa3ca8b56cb60d26e969be516129d)
* contract didn't send ether
* received 0.048125 ether (48125000000000000 wei)
    * from 0xf79bcc67b915ba1fa11c77670ed6f2b5ae1297a2; 48125000000000000 wei
* called functions:
    * `fallback`, fsig: , ether: 48125000000000000 wei, count: 1

# Notes

