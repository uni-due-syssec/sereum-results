true_positive: yes  
fp_type: 2  
source: yes

# Notes

This is the Spankchain incident. See the [writeup](https://medium.com/spankchain/we-got-spanked-what-we-know-so-far-d5ed3a0f38fe) of the Spankchain project for more details about the incident.

The variable `Channels[_lcID]` is a *struct* of type `Channel`, which due to size occupies various storage slots. 
Sereum will lock the part of the struct, which are used in conditional checks.
The first `require` statement will lock the first storage address occupied by the `Channels[_lcID]` variable.
The last statement in `LCOpenTimeout` is a `delete` statement, which is implemented on the EVM level as `SSTORE` instructions with value 0. 
Storage slots with value 0 are not explicitely stored on the blockchain (as all storage is implicitely initialized with 0).


```solidity
function LCOpenTimeout(bytes32 _lcID) public {
/// Sereum: write-lock first storage word of Channels[_lcID]
    require(msg.sender == Channels[_lcID].partyAddresses[0] && Channels[_lcID].isOpen == false);
    require(now > Channels[_lcID].LCopenTimeout);

    if(Channels[_lcID].initialDeposit[0] != 0) {
        Channels[_lcID].partyAddresses[0].transfer(Channels[_lcID].ethBalances[0]);
    } 
    if(Channels[_lcID].initialDeposit[1] != 0) {
/// Sereum: external call here
/// Note: Channels[_lcID].token is a potentially attacker controlled contract.
/// and transfer here is not the solidity method, but the transfer method of
/// the target contract.
        require(Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], Channels[_lcID].erc20Balances[0]),"CreateChannel: token transfer failure");
    }

    emit DidLCClose(_lcID, 0, Channels[_lcID].ethBalances[0], Channels[_lcID].erc20Balances[0], 0, 0);

    // only safe to delete since no action was taken on this channel
/// Sereum: write to locked variable (Channels[_lcID]) with SSTORE(Channels[_lcID],0)
    delete Channels[_lcID];
}
```
