true_positive: no  
fp_type: unknown

# Notes

The entrypoint to the transaction is the function
`bidOnBreedingAuctionTutorial(uint40)` in the `BlockchainCutiesCore` contract.
On line 1559 the function `getBreedingFee` is called, which is just a wrapper
to a call to the `config` contract, which in turn recursively calls into the
`BlockchainCutiesCore` at function `getGeneration`.

In the `getGeneration` function there is no obvious control-flow. However,
solidity will add a bounds check on the array. The length of the array is
stored at address 0. Sereum then detects the length of the array as a critical
variable and issues a write-lock.

Then a lot of other things happen. Finally, a new Cutie is created, which is
then pushed to the end of the global cuties array. First, the length of the
array is incremented by one. However, Sereum write-locked the length variable
to the callback from the `config` contract. Sereum will then issue an alert.

```solidity
// first defined in the solidity contract, which means it ends up at storage address 0
    Cutie[] public cuties;
    // ...


// called from within bidOnBreedingAuctionTutorial on line 1559
        uint256 fee = getBreedingFee(0, _dadId);
// ...

// taking a closer look at this function, this just forwards to the config contract
    function getBreedingFee(uint40 _momId, uint40 _dadId)
        public
        view
        returns (uint256)
    {
        return config.getBreedingFee(_momId, _dadId);
    }

// config.getBreedingFee then calls back into the getGeneration function of the BlockchainCutiesCore contract

// ...

    function getGeneration(uint40 _id)
        public
        view
        returns (uint16 generation)
    {
        Cutie storage cutie = cuties[_id]; // bounds-check here! -> write-lock
        generation = cutie.generation;
    }

// ...

// a new Cutie is created in bidOnBreedingAuctionTutorial on line 1580
        uint40 cutieId = _createCutie(0, _dadId, babyGen, getCooldownIndexFromGeneration(babyGen), childGenes, msg.sender, 12);

// ...

// which will push the new cutie into the array:

        uint256 newCutieId256 = cuties.push(_cutie) - 1;

// ...


```



