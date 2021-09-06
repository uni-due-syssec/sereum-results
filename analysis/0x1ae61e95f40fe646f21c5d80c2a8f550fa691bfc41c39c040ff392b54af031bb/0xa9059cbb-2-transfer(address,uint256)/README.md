true_positive: no  
fp_type: 5

# Notes

This looks like a manual locking issue with a boolean, which is somwhat
obfuscated, by an address being at the same storage address.

First we can observe the following pattern:

```
SLOAD(addr=0000000000000000000000000000000000000000000000000000000000000016) => value=000000000000000000000000 69975e4c4835e70c16b1a8f0b06ba82182e72791                 | 0xE4c94d45f7Aef7018a5D66f44aF780ec6023378e @ 0x827 == 2087
SSTORE(addr=0000000000000000000000000000000000000000000000000000000000000016,   value=000000000000000000000001 69975e4c4835e70c16b1a8f0b06ba82182e72791)                  | 0xE4c94d45f7Aef7018a5D66f44aF780ec6023378e @ 0x839 == 2105
```

As you can see the latter 20 bytes do not change at all, while the other one
changes from 0 to 1.

In the middle there is a re-entering call (to the `emitTransfer` function),
which checks either this boolean flag or loads the address.

```
SLOAD(addr=0000000000000000000000000000000000000000000000000000000000000016) => value=000000000000000000000001 69975e4c4835e70c16b1a8f0b06ba82182e72791         | 0xE4c94d45f7Aef7018a5D66f44aF780ec6023378e @ 0x8ad == 2221
JUMP                                                                                                                                                           | 0xE4c94d45f7Aef7018a5D66f44aF780ec6023378e @ 0x8c0 == 2240
 |-> WRITELOCK to ≥2:JUMPI storage 0x0000000000000000000000000000000000000000000000000000000000000016 contract 0xE4c94d45f7Aef7018a5D66f44aF780ec6023378e
```


At the end of the transaction, we can see that the change is reverted and the
boolean is set back to 0.

```
SLOAD(addr=0000000000000000000000000000000000000000000000000000000000000016) => value=000000000000000000000001 69975e4c4835e70c16b1a8f0b06ba82182e72791                 | 0xE4c94d45f7Aef7018a5D66f44aF780ec6023378e @ 0x205e == 8286
SSTORE(addr=0000000000000000000000000000000000000000000000000000000000000016,   value=000000000000000000000000 69975e4c4835e70c16b1a8f0b06ba82182e72791)                  | 0xE4c94d45f7Aef7018a5D66f44aF780ec6023378e @ 0x206a == 8298
```


The relevant code is in the `_transfer` function (which is wrapped by the
`transfer` ABI-callable function).


```solidity
/// ...
    function _allow() internal {
        __isAllowed = true;
    }

    function _disallow() internal {
        __isAllowed = false;
    }
/// ...

    function _transfer(address _to, uint _value) internal returns(bool, bool) {
        uint startGas = msg.gas + transferCallGas;
        uint fee = calculateFee(_value);
        if (!_transferFee(msg.sender, fee, "Transfer fee")) {
            return (false, false);
        }
        /// call to _allow();
        __isAllowed = true;
        /// return from _allow

        /// triggers external call, which re-enters at emitTransfer
        bool success = super.transfer(_to, _value);
        /// call to _disallow();
        __isAllowed = false;
        /// return from _disallow
        if (!success) {
            return _returnFee(msg.sender, fee);
        }
        return (true, _applyRefund(startGas));
    }
```

and the `emitTransfer` function, where the check for `__isAllowed` makes Sereum
trigger a writelock on the address.

```solidity
    // ...
    modifier onlyMultiAsset() {
        if (msg.sender == address(multiAsset)) {
            _
        }
    }
    // ...
    function emitTransfer(address _from, address _to, uint _value) onlyMultiAsset() {
        Transfer(_from, _to, _value);
        if (__isAllowed) {
            return;
        }
        if (feeAddress == 0x0 || _to == feeAddress || _from == feeAddress) {
            return;
        }
        if (_transferFee(_from, calculateFee(_value), "Transfer fee")) {
            return;
        }
        throw;
    }
```
