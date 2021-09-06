// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
uint256 addr; // 0x0

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  MEM[0x40] = 0x60;
  if (msg.data.length()) {
    if ((0x1b9265b8 == function_selector)) pay()();
    if ((0x40c82671 == function_selector)) 0x40c82671();
    if ((0x63bd1d4a == function_selector)) payout()();
    if ((0xd1d80fdf == function_selector)) setAddr(address)();
  }
  va5 = MEM[0x40];
  MEM[va5] = 0xdb88031a00000000000000000000000000000000000000000000000000000000;
  require(isContract(address(addr)));
  v00xef = v00x9d.call(MEM[v00xd8 : v00xd8 + v00xdb]).value(v00xdd).gas(msg.gas - 710);
  require(v00xef);
  exit();
}

function 0x40c82671(uint256 varg0) public {
  require(!msg.value);
  v20b = MEM[0x40];
  MEM[v20b] = 0xdb88031a00000000000000000000000000000000000000000000000000000000;
  require(isContract(address(addr)));
  v1090x255 = v1090x203.call(MEM[v1090x23e : v1090x23e + v1090x241]).value(v1090x243).gas(msg.gas - 710);
  require(v1090x255);
  exit();
}

function payout() public {
  require(!msg.value);
  exit();
}

function setAddr(address varg0) public {
  require(!msg.value);
  addr = (address(varg0) | (-0x10000000000000000000000000000000000000000 & addr));
  exit();
}

function pay() public {
  exit();
}

