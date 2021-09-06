// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
uint256 b; // 0x0
uint256 __function_selector__; // 0x1
uint256 storage_2; // 0x2

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint256 function_selector) public {
  MEM[0x40] = 0x60;
  if (msg.data.length()) {
    if ((function_selector == 0x20740e9a)) 0x20740e9a();
    if ((0xa1c51915 == function_selector)) getB()(function_selector);
  }
  v430x0_0 = (__function_selector__ <= 0x5);
  if ((__function_selector__ <= 0x5)) {
    v430x0_0 = (0xff & storage_2);
  }
  if (!v430x0_0) {
    __function_selector__ = 0x0;
  } else {
    __function_selector__ = __function_selector__ + 1;
    MEM[0x60] = 0x5fd8c71000000000000000000000000000000000000000000000000000000000;
    require((b & 0xffffffffffffffffffffffffffffffffffffffff).call(MEM[0x60 : 0x64]).gas(msg.gas - 25050));
  }
  exit();
}

function getB() public {
  MEM[0x60] = 0xf8b2cb4f00000000000000000000000000000000000000000000000000000000;
  MEM[0x64] = address(this);
  require((b & 0xffffffffffffffffffffffffffffffffffffffff).call(MEM[0x60 : 0x84]).gas(msg.gas - 25050));
  return(MEM[MEM[0x40]:MEM[0x40] + 0x20]);
}

function 0x20740e9a() public {
  MEM[0x60] = 0xd0e30db000000000000000000000000000000000000000000000000000000000;
  require((0xffffffffffffffffffffffffffffffffffffffff & b).call(MEM[0x60 : 0x64]).gas(msg.gas - 25050));
  exit();
}

