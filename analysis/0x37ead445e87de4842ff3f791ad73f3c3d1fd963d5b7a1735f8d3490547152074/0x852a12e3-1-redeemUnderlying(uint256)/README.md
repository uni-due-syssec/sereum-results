true_positive: (unknown|yes|no)  
fp_type: (None,unknown,1-5)  
source: (yes|no)

# Notes

Not sure whether this is a false positive or not? It is certainly pretty
complicated...


```solidity
/**
 * @notice Sender redeems cTokens in exchange for a specified amount of underlying asset
 * @dev Accrues interest whether or not the operation succeeds, unless reverted
 * @param redeemAmount The amount of underlying to redeem
 * @return uint 0=success, otherwise a failure (see ErrorReporter.sol for details)
 */
function redeemUnderlying(uint redeemAmount) external returns (uint) {
    return redeemUnderlyingInternal(redeemAmount);
}


/**
 * @notice Sender redeems cTokens in exchange for a specified amount of underlying asset
 * @dev Accrues interest whether or not the operation succeeds, unless reverted
 * @param redeemAmount The amount of underlying to redeem
 * @return uint 0=success, otherwise a failure (see ErrorReporter.sol for details)
 */
function redeemUnderlyingInternal(uint redeemAmount) internal nonReentrant returns (uint) {
    uint error = accrueInterest();
    if (error != uint(Error.NO_ERROR)) {
        // accrueInterest emits logs on errors, but we still want to log the fact that an attempted redeem failed
        return fail(Error(error), FailureInfo.REDEEM_ACCRUE_INTEREST_FAILED);
    }
    // redeemFresh emits redeem-specific logs on errors, so we don't need to
    return redeemFresh(msg.sender, 0, redeemAmount);
}

/**
 * @notice User redeems cTokens in exchange for the underlying asset
 * @dev Assumes interest has already been accrued up to the current block
 * @param redeemer The address of the account which is redeeming the tokens
 * @param redeemTokensIn The number of cTokens to redeem into underlying (only one of redeemTokensIn or redeemAmountIn may be zero)
 * @param redeemAmountIn The number of cTokens to redeem into underlying (only one of redeemTokensIn or redeemAmountIn may be zero)
 * @return uint 0=success, otherwise a failure (see ErrorReporter.sol for details)
 */
function redeemFresh(address payable redeemer, uint redeemTokensIn, uint redeemAmountIn) internal returns (uint) {
    require(redeemTokensIn == 0 || redeemAmountIn == 0, "one of redeemTokensIn or redeemAmountIn must be zero");

    RedeemLocalVars memory vars;

/// [...] 

    /////////////////////////
    // EFFECTS & INTERACTIONS
    // (No safe failures beyond this point)

    /*
     * We invoke doTransferOut for the redeemer and the redeemAmount.
     *  Note: The cToken must handle variations between ERC-20 and ETH underlying.
     *  On success, the cToken has redeemAmount less of cash.
     *  If doTransferOut fails despite the fact we checked pre-conditions,
     *   we revert because we can't be sure if side effects occurred.
     */
/// EXTERNAL CALL
    vars.err = doTransferOut(redeemer, vars.redeemAmount);
    require(vars.err == Error.NO_ERROR, "redeem transfer out failed");

    /* We write previously calculated values into storage */

/// STATE UPDATE
/// Here we write to the (locked) totalSupply variable
    totalSupply = vars.totalSupplyNew;
    accountTokens[redeemer] = vars.accountTokensNew;

    /* We emit a Transfer event, and a Redeem event */
    emit Transfer(redeemer, address(this), vars.redeemTokens);
    emit Redeem(redeemer, vars.redeemAmount, vars.redeemTokens);

    /* We call the defense hook */
    comptroller.redeemVerify(address(this), redeemer, vars.redeemAmount, vars.redeemTokens);

    return uint(Error.NO_ERROR);
}
```
