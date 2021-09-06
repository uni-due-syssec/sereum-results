// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
uint256 collect; // 0x0

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  MEM[0x40] = 0x60;
  if (msg.data.length()) {
    if ((0x41c0e1b5 == function_selector)) kill()();
    if ((0xe5225381 == function_selector)) collect()();
    if ((0xef89aff3 == function_selector)) 0xef89aff3(function_selector);
  }
  if ((BALANCE(address((collect / 0x1))) >= msg.value)) {
    v00xdc = MEM[0x40];
    MEM[v00xdc] = 0x6d4ce63c00000000000000000000000000000000000000000000000000000000;
    require(isContract(address((collect / 0x1))));
    require(address((collect / 0x1)).call(MEM[MEM[0x40] : MEM[0x40] + (v00xdc + 4 - MEM[0x40])]).gas(msg.gas - 50));
  }
  exit();
}

function kill() public {
  require(!msg.value);
  selfdestruct(address(msg.sender));
}

function collect() public {
  v13f0x1f5 = MEM[0x40];
  MEM[v13f0x1f5] = 0x549262ba00000000000000000000000000000000000000000000000000000000;
  require(isContract(address((collect / 0x1))));
  require(address((collect / 0x1)).call(MEM[MEM[0x40] : MEM[0x40] + (v13f0x1f5 + 4 - MEM[0x40])]).value(msg.value).gas(msg.gas - 9050));
  v13f0x285 = MEM[0x40];
  MEM[v13f0x285] = 0x6d4ce63c00000000000000000000000000000000000000000000000000000000;
  require(isContract(address((collect / 0x1))));
  require(address((collect / 0x1)).call(MEM[MEM[0x40] : MEM[0x40] + (v13f0x285 + 4 - MEM[0x40])]).gas(msg.gas - 50));
  exit();
}

function 0xef89aff3() public {
  require(!msg.value);
  v1490x2f9 = address((collect / 0x1));
  v1490x159 = MEM[0x40];
  MEM[v1490x159] = address(v1490x2f9);
  return(MEM[MEM[0x40]:MEM[0x40] + (v1490x159 + 32 - MEM[0x40])]);
}

