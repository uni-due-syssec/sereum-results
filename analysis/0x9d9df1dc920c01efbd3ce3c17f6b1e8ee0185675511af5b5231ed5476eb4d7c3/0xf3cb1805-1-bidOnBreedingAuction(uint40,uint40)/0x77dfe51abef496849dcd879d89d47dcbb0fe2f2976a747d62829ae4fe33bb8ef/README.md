# transaction 0x77dfe51abef496849dcd879d89d47dcbb0fe2f2976a747d62829ae4fe33bb8ef

[etherscan.io/tx](https://etherscan.io/tx/0x77dfe51abef496849dcd879d89d47dcbb0fe2f2976a747d62829ae4fe33bb8ef)


### Contract at 0x20c81ae5a7cf1c5a3f8293313692474f8d6b808b

* [etherscan](https://etherscan.io/address/0x20c81ae5a7cf1c5a3f8293313692474f8d6b808b)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x20c81ae5a7cf1c5a3f8293313692474f8d6b808b)
* contract didn't send ether
* received 3000000000000000 wei
    from 0xd73be539d6b2076bab83ca6ba62dfe189abc6bbe; 3000000000000000 wei
* called functions:
    * bid(uint40), fsig: c170fd54, ether: 3000000000000000, count: 1


### Contract at 0x685b9cfb5e5de7ac73c152b2bc72ff9238f6f005

* [etherscan](https://etherscan.io/address/0x685b9cfb5e5de7ac73c152b2bc72ff9238f6f005)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x685b9cfb5e5de7ac73c152b2bc72ff9238f6f005)
* contract didn't send ether
* didn't receive any ether
* called functions:
    * canBreed(uint40,uint256,uint40,uint256), fsig: c868a569, ether: 0, count: 1
    * mixGenes(uint256,uint256), fsig: 8d8b1b88, ether: 0, count: 1


### Contract at 0x87fc0cdb581f84456c02f20ec1a844d95803c437

* [etherscan](https://etherscan.io/address/0x87fc0cdb581f84456c02f20ec1a844d95803c437)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x87fc0cdb581f84456c02f20ec1a844d95803c437)
* contract didn't send ether
* contract wasn't called


### Contract at 0x7d3e5eff86d25e9618512d871f4533c277361cc1

* [etherscan](https://etherscan.io/address/0x7d3e5eff86d25e9618512d871f4533c277361cc1)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x7d3e5eff86d25e9618512d871f4533c277361cc1)
* sent 2880000000000000 wei
    * to 0xd73be539d6b2076bab83ca6ba62dfe189abc6bbe; 0 wei
    * to 0x7e9bd33576356b15d8e1756257436437b7fc914b; 2880000000000000 wei
* didn't receive any ether
* called functions:
    * getBreedingFee(uint40,uint40), fsig: 66dc860a, ether: 0, count: 1
    * getCooldownEndTimeFromIndex(uint16), fsig: 06347def, ether: 0, count: 2
    * getCooldownIndexCount(), fsig: 732606fc, ether: 0, count: 2
    * getBabyGen(uint16,uint16), fsig: 1af97fb7, ether: 0, count: 1
    * getCooldownIndexFromGeneration(uint16), fsig: 5757dcdf, ether: 0, count: 1


### Contract at 0x7e9bd33576356b15d8e1756257436437b7fc914b

* [etherscan](https://etherscan.io/address/0x7e9bd33576356b15d8e1756257436437b7fc914b)
* [contract-library](https://contract-library.com/contracts/Ethereum/0x7e9bd33576356b15d8e1756257436437b7fc914b)
* contract didn't send ether
* received 2880000000000000 wei
    from 0x7d3e5eff86d25e9618512d871f4533c277361cc1; 2880000000000000 wei
* called functions:
    * fsig: None, ether: 2880000000000000, count: 1


### Contract at 0xd73be539d6b2076bab83ca6ba62dfe189abc6bbe

**flagged vulnerable**

* [etherscan](https://etherscan.io/address/0xd73be539d6b2076bab83ca6ba62dfe189abc6bbe)
* [contract-library](https://contract-library.com/contracts/Ethereum/0xd73be539d6b2076bab83ca6ba62dfe189abc6bbe)
* sent 3000000000000000 wei
    * to 0x685b9cfb5e5de7ac73c152b2bc72ff9238f6f005; 0 wei
    * to 0x7d3e5eff86d25e9618512d871f4533c277361cc1; 0 wei
    * to 0x20c81ae5a7cf1c5a3f8293313692474f8d6b808b; 3000000000000000 wei
* didn't receive any ether
* called functions:
    * getGeneration(uint40), fsig: 9c91ae20, ether: 0, count: 2
    * getCooldownIndex(uint40), fsig: 2917f162, ether: 0, count: 2
    * fsig: a9059cbb, ether: 0, count: 1
        * many_msg_babbage(bytes1)
        * transfer(address,uint256)

# Notes

