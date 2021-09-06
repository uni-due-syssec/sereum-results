// Decompiled at www.contract-library.com
// 2019.11.29 19:56 UTC

// Data structures and variables inferred from the use of storage instructions
uint256 _owner; // STORAGE[0x0]

// Events

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  freeMemPtr = 0x60;
  if (msg.data.length() >= 0x4) {
    if (function_selector == 0x87f14e6f) 0x87f14e6f; // stack operands: ()
    if (0x8da5cb5b == function_selector) owner(); // stack operands: ()
    if (0xacec338a == function_selector) setActive(bool); // stack operands: ()
    if (0xd0e30db0 == function_selector) deposit(); // stack operands: ()
    if (0xf2fde38b == function_selector) transferOwnership(address); // stack operands: ()
  }
  va6_0x0 = v8b = !(0xff & _owner >> 160);
  if (v8b) {
    va6_0x0 = va5 = address(_owner) != address(tx.origin);
  }
  require(!va6_0x0);
  exit();
}

function deposit() public {
  exit();
}

function transferOwnership(address varg0) public {
  require(!msg.value);
  require(address(_owner) == address(msg.sender));
  require(address(varg0));
  _owner = address(varg0) | (~0xffffffffffffffffffffffffffffffffffffffff & _owner);
  exit();
}

function 0x87f14e6f() public {
  require(!msg.value);
  require(address(_owner) == address(msg.sender));
  /*call status*/v17b = address(msg.sender).call().value(address(this).balance).gas((!address(this).balance * 0x8fc));
  exit();
}

function owner() public {
  require(!msg.value);
  v18e = address(_owner);
  return address(v18e);
}

function setActive(bool varg0) public {
  require(!msg.value);
  require(address(_owner) == address(msg.sender));
  _owner = (_owner & ~0xff0000000000000000000000000000000000000000) | varg0 << 160;
  exit();
}

