true_positive: yes  
fp_type: None  
source: yes

# Notes

Source code of both the vulnerable `HODLwallet` and the attacker contract are
available. Interestingly, the re-entrancy vulnerable does not bypass the check
for enough balances, but a check on the number of withdrawals.

All the withdraw function use the following internal withdrawal function, which
implements certain artifical restrictions:

1. Only a certain amount of withdrawal possible per withdraw call
2. Enough ether in balances
3. In total only 3 withdrawals possible

```solidity
function doWithdraw(address from, address to, uint256 amount) internal {
    // only use in emergencies!
    // you can only get a little at a time.
    // we will hodl the rest for you.

/// (1)
    require(amount <= MAX_WITHDRAWAL);
/// (2)
    require(balances[from] >= amount);
/// (3) - bypassable with re-entrancy
    require(withdrawalCount[from] < 3);

    balances[from] = balances[from].sub(amount);

/// external call
    to.call.value(amount)();

/// state update
    withdrawalCount[from] = withdrawalCount[from].add(1);
}
```

It is possible to bypass the check at (3) using the re-entrancy attack.
However, this seems to basically only bypass the restrictions of the
`HODLwallet` withdrawal and it does not actually allow the attacker to steal
ether from others using the wallet.


The `HODLwallet` seems to be somewhat of a prank contract, as there are some
not so serious comments in the source code submitted to etherscan, e.g.,

```solidity
// HODL YOUR COINS HERE!! THE SAFEST WALLET!!

[...]

    function addBalances(address[] addrs, uint256[] _balances) public payable onlyOwner {
        // in case more idio^H^H^H^HHODLers want to join

[...]
```

