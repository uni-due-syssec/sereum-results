true_positive: no  
fp_type: unknown

# Notes

The problem is that a integer overflow check introduced by the `SafeMath`
library also introduces a conditional branch. This conditional branch makes
Sereum issue a write-lock, which is then violated later on.

The TX starts with a call to `tokenReinvest`, which calls another contract,
which re-enters the flagged contract in the `pushToBank` function, which
executes the following solidity code.

```solidity
uint256 _amount = msg.value;
lastClaim[_player] = block.timestamp;
/// SafeMath call here, which introduces a branch due to overflow check
balance[_player] = _amount.add(balance[_player]);
```

This code doesn't have any branch, but on the EVM level the SafeMath library
introduces one with the integer overflow check. Since `balances[_player]` then
influences a control-flow decision, Sereum will issue a write-lock.


Here are the relevant parts of the transaction trace:


```
SLOAD(addr=26a87bc6ad51a48019fe441a2998cebb2d098b65341ddf0d8ec81a5e0e0c0d4f) => value=0000000000000000000000000000000000000000000000000000000000000000         | 0xDF18880A02C7F3EB4f40FdF515fce31C1CB7EF66 @ 0xce5 == 3301

[...]

CALL(0x8888882056160e5ff4a0f26607d4a05bc506ca8c (@ withdrawFor(address))
 | ether=0
 | input=mem[128:164]{9eca672c0000000000000000000000007c9eab55d5085cfe605c8a8569594037
 | 4163ce83}
 | ...)                                                                                                                                                        | 0xDF18880A02C7F3EB4f40FdF515fce31C1CB7EF66 @ 0x179e == 6046

[...]

    CALL(0xdf18880a02c7f3eb4f40fdf515fce31c1cb7ef66 (@ pushToBank(address))
     | ether=0
     | input=mem[128:164]{e9288d720000000000000000000000007c9eab55d5085cfe605c8a8569594037
     | 4163ce83}
     | ...)                                                                                                                                                | 0x8888887c5eDE327aFbeb15019598aAa3b4FaE759 @ 0x30ef == 12527
        SLOAD(addr=26a87bc6ad51a48019fe441a2998cebb2d098b65341ddf0d8ec81a5e0e0c0d4f) => value=0000000000000000000000000000000000000000000000000000000000000000 | 0xDF18880A02C7F3EB4f40FdF515fce31C1CB7EF66 @ 0x27f1 == 10225
        DUP1                                                                                                                                                   | 0xDF18880A02C7F3EB4f40FdF515fce31C1CB7EF66 @ 0x29ce == 10702
         |-> WRITELOCK 
         [...]
         | to ≥2:JUMPI storage 0x26a87bc6ad51a48019fe441a2998cebb2d098b65341ddf0d8ec81a5e0e0c0d4f contract 0xDF18880A02C7F3EB4f40FdF515fce31C1CB7EF66
         [...]
        SSTORE(addr=26a87bc6ad51a48019fe441a2998cebb2d098b65341ddf0d8ec81a5e0e0c0d4f, value=0000000000000000000000000000000000000000000000000000000000000000)  | 0xDF18880A02C7F3EB4f40FdF515fce31C1CB7EF66 @ 0x2841 == 10305

[...]

SSTORE(addr=26a87bc6ad51a48019fe441a2998cebb2d098b65341ddf0d8ec81a5e0e0c0d4f, value=0000000000000000000000000000000000000000000000000000000000000000)          | 0xDF18880A02C7F3EB4f40FdF515fce31C1CB7EF66 @ 0xe63 == 3683
```


And here the relevant solidity code from the contract:

```solidity
    function tokenReinvest(uint256 _amount) 
        public
        payable
    {
        address _sender = msg.sender;
        uint256 _deposit = msg.value;
/// read from mapping (first SLOAD in TX)
        uint256 _curBalance = balance[_sender];
        uint256 investAmount;
        uint256 collected = 0;
        if (_deposit == 0) {
            if (_amount > balance[_sender]) 
                collected = collectIncome(_sender);
            require(_amount <= _curBalance + collected, "balance not enough");
            investAmount = _amount;//_curBalance + collected;
        } else {
            collected = collectIncome(_sender);
            investAmount = _deposit.add(_curBalance).add(collected);
        }
/// write to mapping (Sereum detects re-entrancy)
        balance[_sender] = _curBalance.add(collected + _deposit).sub(investAmount);
        lastClaim [_sender] = block.timestamp;
        f2mContract.buyFor.value(investAmount)(_sender);
    }


/// ...


    function collectIncome(address _member)
        public
        returns(uint256)
    {
        require(_member != address(devTeamContract), "no right");
        //lastClaim[_member] = block.timestamp;
        uint256 collected = collectDividends(_member) + collectRef(_member) + collectReward(_member);
        return collected;
    }

/// ...

    function collectDividends(address _member)
        public
        returns(uint256)
    {
        require(_member != address(devTeamContract), "no right");
/// external call observed in the trace
        uint256 collected = f2mContract.withdrawFor(_member);
        claimedSum[_member] += collected;
        return collected;
    }

/// withdrawFor triggers callback to pushToBank

/// ... 

    function pushToBank(address _player)
        public
        payable
    {
        uint256 _amount = msg.value;
        lastClaim[_player] = block.timestamp;
        balance[_player] = _amount.add(balance[_player]);
    }
```
