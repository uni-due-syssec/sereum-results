# False Positive Types and Root Causes

In [our paper on Sereum](https://arxiv.org/abs/1812.05934) we classified the false positives according to 5 primary root-causes. 


## 1. Lack of Field Sensitivity on the EVM Level

This is a classic over-tainting issue. We assign taints to 32-byte integers
(i.e., the native word size of the EVM) on the stack and the storage area.  Two
unrelated variables of smaller data types (e.g., `uint32`), can be stored at
the same storage address, which can hold 256 bit / 32 bytes.

Sereum will assign taints to both variables, which leads to over-tainting. At
the EVM bytecode level it is hard to distinguish between fields and infer the
right data type. 


```solidity
// This will be stored at one storage address, because one storage address
// holds a full 256 bit integer (32 bytes).
struct S {
    uint128 a;
    uint128 b;
}

// Will be stored in storage in the contract
S s;

function foo() {
    if (s.a) {  // write-lock s (not only s.a)
        return something;
    }
}

function bar() {
    external_call();// trigger re-entrancy at foo() -> s locked
    s.b = something; // trigger alert due to write to s (not s.b)
}

```


## 2. Storage Deallocation

A solidity statment of the type

```solidity
mapping (uint => uint) M;
delete M[id];
```

is equivalent to a `SSTORE` instruction with value 0. This can cause false
positives, since deallocations are typically at the end of functions of
contracts. 

Most contracts we identified resulted in false positives (all cases in the original Sereum paper). 
Note that the *Spankchain* incident is actually a true positive, where the attacker exploited the fact, that the `delete` was executed at the very end of the function (see [detailed analysis in this repository](./analysis/0x46a8b25053a9cf565e3032a4e9348281eda7cc5f3837a3613aea7a3dd9b9d3c2/0x002e1d7e-1-LCOpenTimeout(bytes32))).


## 3. Constructor Callbacks

Here a constructor calls back into the calling contract to retrieve information. 
This can lead to false positives, when the callback performs a conditional jump and the same variable is legitmately modified after the constructor finished.


Here is an example for a bad pattern, that can easily lead to a false positive.

```solidity
// Bad pattern, possibly leading to false positives:

contract Child {
    constructor() public {
        Parent p = msg.sender;
        // unnecessary callback to parent
        x = p.getX();
    }
}

contract Parent {
    uint x;
    function getX() public view returns(uint) { return x; }

    function foo() public {
        // ...
        new Child();
        // ...
    }
}
```


The following code pattern is functionally equivalent, but is much safer. 
Sereum is less likely to report a false positive. 
Furthermore it's also less likely to accidentally introduce a real re-entrancy bug.

```solidity
// good pattern, pass all information to child contract in constructor arguments

contract Child {
    uint x;
    constructor(uint _x) public {
        x = _x;
    }
}

contract Parent {
    uint x;
    
    function foo() public {
        // ...
        new Child(x);
        // ...
    }
}
```


## 4. Tight Contract Coupling

Functionality is sometimes split between various contracts, which repeatedly call each other in nested invocations.
Those contracts might trust each other (e.g., owned/developed by the same entity), but Sereum cannot be aware of such relationships between contracts and must assume the contract are adversarial.
If the contracts perform repeated callbacks to each other, then Sereum is very likely to write-lock some variable, even though in reality control never passes to the attacker.


## 5. Manual Re-Entrancy Locking

Some contracts contain locking variables, which act as guards for certain
functions. This can be used to prevent re-entrancy attacks.

**Example** here the `withdrawBalance` employs a "lock variable"
`disableWithdraw[msg.sender]` to prevent the sender from re-entering the
`withdrawBalance` function. So even though the state is updated after the
external call.


```solidity
function withdrawBalance() public {
    require(disableWithdraw[msg.sender] == false);
    uint amountToWithdraw = ;
    
    disableWithdraw[msg.sender] = true;
    msg.sender.call.value(userBalances[msg.sender])("");
    disableWithdraw[msg.sender] = false;

    userBalances[msg.sender] = 0;
}
```

More information on this can be found in our repository on re-entrancy attack
patterns:

* [Information and Evaluation of Tools](https://github.com/uni-due-syssec/eth-reentrancy-attack-patterns#testcase-manual-lock)
* [Vulnerable and Attack Contracts](https://github.com/uni-due-syssec/eth-reentrancy-attack-patterns/blob/master/manual-lock.sol)


## 6. Bounds-Checking of Dynamic Arrays

Bounds-checking of dynamic arrays (e.g., [the BlockChaincuties contract](analysis/0x9d9df1dc920c01efbd3ce3c17f6b1e8ee0185675511af5b5231ed5476eb4d7c3/0x1bbfce0e-1-bidOnBreedingAuctionTutorial(uint40))

## New patterns

