# transaction 0x6d3e792830c9561cd26672d7c038b984ec41402ecdb0f7ee80569bb12be2d386

[etherscan.io/tx](https://etherscan.io/tx/0x6d3e792830c9561cd26672d7c038b984ec41402ecdb0f7ee80569bb12be2d386)


### Contract at 0x47fb0c659835085e1d3e29ce2a3f8bac6a058077

* [etherscan](https://etherscan.io/address/0x47fb0c659835085e1d3e29ce2a3f8bac6a058077)
* [contract-library](https://contract-library.com/contracts/Ethereum/47fb0c659835085e1d3e29ce2a3f8bac6a058077)
* sent 0.0746114061454419 ether (74611406145441909 wei)
    * to 0xbb9bc244d798123fde783fcc1c72d3bb8c189413; 0 wei
    * to 0xd2e16a20dd7b1ae54fb0312209784478d069c7b0; 74611406145441909 wei
    * to 0xd6266bfe94742c361683969e802c895ababdb4f9; 0 wei
* contract wasn't called


### Contract at 0xbb9bc244d798123fde783fcc1c72d3bb8c189413

**flagged vulnerable**

* [etherscan](https://etherscan.io/address/0xbb9bc244d798123fde783fcc1c72d3bb8c189413)
* [contract-library](https://contract-library.com/contracts/Ethereum/bb9bc244d798123fde783fcc1c72d3bb8c189413)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * `closingTime()`, fsig: 4b6753bc, ether: 0 wei, count: 1
    * fsig: 18160ddd, ether: 0 wei, count: 2
        * `totalSupply()`
        * `voting_var(address,uint256,int128,int128)`
    * fsig: 70a08231, ether: 0 wei, count: 4
        * `branch_passphrase_public(uint256,bytes8)`
        * `passphrase_calculate_transfer(uint64,address)`
        * `balanceOf(address)`
    * `paidOut(address)`, fsig: 81f03fcb, ether: 0 wei, count: 2
    * fsig: a9059cbb, ether: 0 wei, count: 2
        * `many_msg_babbage(bytes1)`
        * `transfer(address,uint256)`
        * `transfer(bytes4[9],bytes5[6],int48[11])`
    * `getMyReward()`, fsig: cc9ae3f6, ether: 0 wei, count: 49


### Contract at 0x79f09717c5b352078234832e5737651ddb333548

* [etherscan](https://etherscan.io/address/0x79f09717c5b352078234832e5737651ddb333548)
* [contract-library](https://contract-library.com/contracts/Ethereum/79f09717c5b352078234832e5737651ddb333548)
* contract didn't send ether
* contract wasn't called


### Contract at 0xd6266bfe94742c361683969e802c895ababdb4f9

* [etherscan](https://etherscan.io/address/0xd6266bfe94742c361683969e802c895ababdb4f9)
* [contract-library](https://contract-library.com/contracts/Ethereum/d6266bfe94742c361683969e802c895ababdb4f9)
* contract didn't send ether
* received 0.07466307887962666 ether (74663078879626650 wei)
    * from 0x47fb0c659835085e1d3e29ce2a3f8bac6a058077; 0 wei
    * from 0xd2e16a20dd7b1ae54fb0312209784478d069c7b0; 74663078879626650 wei
* called functions:
    * fsig: 42966c68, ether: 0 wei, count: 1
        * `collate_propagate_storage(bytes16)`
        * `burn(uint256)`
    * `fallback`, fsig: , ether: 74663078879626650 wei, count: 49


### Contract at 0xd2e16a20dd7b1ae54fb0312209784478d069c7b0

* [etherscan](https://etherscan.io/address/0xd2e16a20dd7b1ae54fb0312209784478d069c7b0)
* [contract-library](https://contract-library.com/contracts/Ethereum/d2e16a20dd7b1ae54fb0312209784478d069c7b0)
* sent 0.07466307887962666 ether (74663078879626650 wei)
    * to 0xd6266bfe94742c361683969e802c895ababdb4f9; 74663078879626650 wei
* received 0.0746114061454419 ether (74611406145441909 wei)
    * from 0x47fb0c659835085e1d3e29ce2a3f8bac6a058077; 74611406145441909 wei
    * from 0xbb9bc244d798123fde783fcc1c72d3bb8c189413; 0 wei
* called functions:
    * `accumulatedInput()`, fsig: d2cc718f, ether: 0 wei, count: 100
    * `fallback`, fsig: , ether: 74611406145441909 wei, count: 1
    * `payOut(address,uint256)`, fsig: 0221038a, ether: 0 wei, count: 49

# Notes

