# transaction 0xc382ccc5895df4fbcd3548c7d8892cb4ed397a43092a23235c0f01dad839aa5c

[etherscan.io/tx](https://etherscan.io/tx/0xc382ccc5895df4fbcd3548c7d8892cb4ed397a43092a23235c0f01dad839aa5c)


### Contract at 0x3fce483a0236ba36869e4e82151006045e7d3331

* [etherscan](https://etherscan.io/address/0x3fce483a0236ba36869e4e82151006045e7d3331)
* [contract-library](https://contract-library.com/contracts/Ethereum/3fce483a0236ba36869e4e82151006045e7d3331)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * `proxyApprove(address,uint256,bytes32)`, fsig: 4f09eba7, ether: 0 wei, count: 1


### Contract at 0x606ddac6f2928369e8515340f8de97fe2d166777

* [etherscan](https://etherscan.io/address/0x606ddac6f2928369e8515340f8de97fe2d166777)
* [contract-library](https://contract-library.com/contracts/Ethereum/606ddac6f2928369e8515340f8de97fe2d166777)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * fsig: 00000000, ether: 0 wei, count: 1
        * `blockHashAmarilloNonspontaneously(uint256)`
        * `blockHashAmphithyronVersify(uint256)`
        * `blockHashAddendsInexpansible(uint256)`
        * `left_branch_block(uint32)`
        * `get_block_hash_257335279069929(uint256)`
        * `blockHashAskewLimitary(uint256)`
        * `overdiffusingness(bytes,uint256,uint256,uint256,uint256)`
    * `__dig(uint256)`, fsig: 21835af6, ether: 0 wei, count: 1


### Contract at 0x4e8703a59fec01a97d4d2d76271e4f086dbb52fc

* [etherscan](https://etherscan.io/address/0x4e8703a59fec01a97d4d2d76271e4f086dbb52fc)
* [contract-library](https://contract-library.com/contracts/Ethereum/4e8703a59fec01a97d4d2d76271e4f086dbb52fc)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * fsig: 00000000, ether: 0 wei, count: 1
        * `blockHashAmarilloNonspontaneously(uint256)`
        * `blockHashAmphithyronVersify(uint256)`
        * `blockHashAddendsInexpansible(uint256)`
        * `left_branch_block(uint32)`
        * `get_block_hash_257335279069929(uint256)`
        * `blockHashAskewLimitary(uint256)`
        * `overdiffusingness(bytes,uint256,uint256,uint256,uint256)`


### Contract at 0x414fbf684a6426cf6012623f51170a5a86161d52

* [etherscan](https://etherscan.io/address/0x414fbf684a6426cf6012623f51170a5a86161d52)
* [contract-library](https://contract-library.com/contracts/Ethereum/414fbf684a6426cf6012623f51170a5a86161d52)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * `emitApprove(address,address,bytes32,uint256)`, fsig: d54c8c87, ether: 0 wei, count: 1
    * `versions(address)`, fsig: 488725a0, ether: 0 wei, count: 1


### Contract at 0x238f99a33f6a1c78187b5b0d645cb4606aebf9e3

**flagged vulnerable**

* [etherscan](https://etherscan.io/address/0x238f99a33f6a1c78187b5b0d645cb4606aebf9e3)
* [contract-library](https://contract-library.com/contracts/Ethereum/238f99a33f6a1c78187b5b0d645cb4606aebf9e3)
* [eevm](https://eveem.org/code/0x238f99A33f6A1c78187b5B0D645CB4606aEBF9E3)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * `emitApprove(address,address,uint256)`, fsig: 23385089, ether: 0 wei, count: 1


### Contract at 0x1ff21eca1c3ba96ed53783ab9c92ffbf77862584

* [etherscan](https://etherscan.io/address/0x1ff21eca1c3ba96ed53783ab9c92ffbf77862584)
* [contract-library](https://contract-library.com/contracts/Ethereum/1ff21eca1c3ba96ed53783ab9c92ffbf77862584)
* contract didn't send ether
* contract wasn't called

# Notes


Unlikely to be a re-entrancy attack, since

1. The write-lock was triggered at calldepth 0 (i.e., there seems to be no attacker contract)
2. eveem.org decompiler says that the variable is called `forwardCallGas` ("is uint256 at storage 16")
