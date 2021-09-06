true_positive: yes  
fp_type: None  
source: yes

# Notes

Apparently TheDAO was also exploited with a different re-entrancy vulnerability
in the `getMyReward` function. First `splitDAO` is called, but then the
`getMyReward` function is called recursively instead (the other attack called
`splitDAO`).


```solidity

    function getMyReward() noEther returns (bool _success) {
        return withdrawRewardFor(msg.sender);
    }

    function withdrawRewardFor(address _account) noEther internal returns (bool _success) {
        if ((balanceOf(_account) * rewardAccount.accumulatedInput()) / totalSupply < paidOut[_account])
            throw;

        uint reward =
            (balanceOf(_account) * rewardAccount.accumulatedInput()) / totalSupply - paidOut[_account];
/// the payOut function performs an external call
        if (!rewardAccount.payOut(_account, reward))
            throw;
/// state is updated afterwards
        paidOut[_account] += reward;
        return true;
    }
```

