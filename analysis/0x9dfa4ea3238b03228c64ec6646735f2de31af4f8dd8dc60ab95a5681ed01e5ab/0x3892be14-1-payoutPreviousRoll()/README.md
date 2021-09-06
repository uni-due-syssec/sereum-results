true_positive: yes  
fp_type: None  
source: yes

# Notes

The contract has a re-entrancy vulnerability in the `payoutPreviousRoll`
function, which let's a user that has previously won in a "diceroll" to
withdraw their price-money multiple times with an re-entrancy attack. The
re-entrancy is somewhat hidden in the original contract, because the external
call is within an internal function called `_finalizePreviousRoll` and the
following state update is in the public `payoutPreviousRoll` function.


```solidity
// Finalizes the previous roll and pays out user if they won.
// Gas: 45k
//   21k: tx overhead
//    1k: SLOADs
//    2k: execution
//    8k: send winnings
//    5k: update user
//    5k: update stats
//    3k: RollFinalized event
function payoutPreviousRoll()
    public
    returns (bool _success)
{
    // Load last roll in one SLOAD.
    User storage _user = users[msg.sender];
    // Error if on same block.
    if (_user.r_block == uint32(block.number)){
        emit PayoutError(now, "Cannot payout roll on the same block");
        return false;
    }
    // Error if nothing to payout.
    if (_user.r_block == 0){
        emit PayoutError(now, "No roll to pay out.");
        return false;
    }

    // Finalize previous roll (this may update stats)
    Stats memory _stats = stats;
/// inlined the following call
    //_finalizePreviousRoll(_user, _stats);
/// start of inlined internal call to _finalizePreviousRoll
    // Finalizes the previous roll for the _user.
    // There must be a previous roll, or this throws.
    // Returns true, unless user wins and we couldn't pay.
    //function _finalizePreviousRoll(User memory _user, Stats memory _stats)
    //    private
    //{
    assert(_user.r_block != uint32(block.number));
    assert(_user.r_block != 0);
    
    // compute result and isWinner
    uint8 _result = computeResult(_user.r_block, _user.r_id);
    bool _isWinner = _result <= _user.r_number;
    if (_isWinner) {
/// EXTERNAL CALL
        require(msg.sender.call.value(_user.r_payout)());
        _stats.totalWon += _user.r_payout;
    }
    // they won and we paid, or they lost. roll is finalized.
    emit RollFinalized(now, _user.r_id, msg.sender, _result, _isWinner ? _user.r_payout : 0);
//}
/// end of inlined internal call to _finalizePreviousRoll

/// STATE UPDATE
    // Clear last roll, update stats
    _user.r_id = 0;
    _user.r_block = 0;
    _user.r_number = 0;
    _user.r_payout = 0;
    stats.totalWon = _stats.totalWon;
    return true;
}

```
