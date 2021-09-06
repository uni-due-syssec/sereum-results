# Analysis of Flagged Contracts

Contracts are organized according to their `codehash`. To minimize manual
analysis effort, we save and analyze one transaction for each unique
combination out of:

* code hash (top level directory)
* function signature (second level directory)
* program counter (`PC`) of the flagged contract, when the vulnerability is reported

The directory is formatted according to this format:  
`{hex_signature}-{known_count}-{first_text_signaure}`  
We retrieve the `hex_signature` from the calldata or transaction input. 
We then perform a lookup of the hex signature at [4byte.directory](https://www.4byte.directory), which gives us a set of known text signatures.
It is rather common for multiple text signatures to map to the same the hex signature.
As such, the `known_count` reflects how many text signatures are known to the 4byte service.
We then simply append the first text signature to increase human readability.

For example, for TheDAO incident we have one directory for code hash of the DAO contract:

[0x6a5d24750f78441e56fec050dc52fe8e911976485b7472faac7464a176a67caa/](0x6a5d24750f78441e56fec050dc52fe8e911976485b7472faac7464a176a67caa/)  

For TheDAO we have two functions, where we saw (potential) re-entrancy attacks:

* [0x82661dc4-1-splitDAO(uint256,address)](0x6a5d24750f78441e56fec050dc52fe8e911976485b7472faac7464a176a67caa/0x82661dc4-1-splitDAO(uint256,address))
* [0xcc9ae3f6-1-getMyReward()](0x6a5d24750f78441e56fec050dc52fe8e911976485b7472faac7464a176a67caa/0xcc9ae3f6-1-getMyReward())
 
And for each function we save one transaction for every distinct program counter (`PC`). In this case it is one transaction for each called function.  

* [0x82661dc4-1-splitDAO(uint256,address)/0xfd00ed2dfa30be48547fe1294d5363a36e1aa23335a2bee0fd0073279b6f02f4](0x6a5d24750f78441e56fec050dc52fe8e911976485b7472faac7464a176a67caa/0x82661dc4-1-splitDAO(uint256,address)/0xfd00ed2dfa30be48547fe1294d5363a36e1aa23335a2bee0fd0073279b6f02f4)
* [0xcc9ae3f6-1-getMyReward()/0x1d228adeb31531fff63eb57731df221a4a4ec300b3649ff5c9a99ed7e1349666](0x6a5d24750f78441e56fec050dc52fe8e911976485b7472faac7464a176a67caa/0xcc9ae3f6-1-getMyReward()/0x1d228adeb31531fff63eb57731df221a4a4ec300b3649ff5c9a99ed7e1349666)
