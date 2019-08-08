# reentrancy_*.csv

These files are lists of transactions, where sereum flagged a reentrancy
attack. The csv files contain the following columns:

* `blocknum` - the Etherum blockchain block number
* `txhash` - the transaction hash
* `gas` - gas supplied to the transaction
* `caller` - address of the caller to the vulnerable contract 
* `contract` - the address of the contract which Sereum flagged as vulnerable/attacked
* `codehash` - this is the codehash of the flagged contract (i.e., the one which is considered vulnerable)
* `calldata` - this is the calldata supplied to the vulnerable contract (this is not the same as the calldata supplied to the transaction)
* `functionsig` - the first 4 bytes of the calldata, useful to lookup the solidity function signature
* `returnvalue` - unused
* `calldepth` - the call stack depth, at which the re-entrancy attack was detected
* `externalcalldepth` - this is similar to the calldepth, but does ignore calls that do not change storage context (e.g., `DELEGATECALL`) it is also off-by-one to the calldepth
* `pc` - the EVM program counter at which the re-entrancy attack was detected
* `storageaddress` - the write-locked storage address to which the contract wrote
* `writelockdepth` - this is the externalcalldepth to which the storageaddress was write-locked
* `reason` - the reson for issuing the write-lock, can be 
    * `JUMPI` - data-flow from storage to conditional jump (as described in our original NDSS paper)
    * `CALL_VALUE` - data-flow from storage to the amount of ether passed to a call instruction (for detecting unconditional re-entrancy)
    * `CALL_DATA` - data-flow from storage to the data passed to a call instruction (for detecting unconditional re-entrancy)
    * `CREATE_DATA` - data-flow from storage to the data passed to a create instruction (for detecting unconditional re-entrancy)
* `ts` - mostly unused; timestamp when the transaction was replayed by Sereum
