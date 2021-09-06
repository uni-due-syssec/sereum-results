// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
mapping (uint256 => [uint256]) balances;

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  MEM[0x40] = 0x60;
  if (msg.data.length()) {
    if ((0x12b58349 == function_selector)) getTotalBalance()(function_selector);
    if ((0x27e235e3 == function_selector)) balances(address)(function_selector);
    if ((0x9a166299 == function_selector)) getMyAddress()(function_selector);
    if ((0xdb88031a == function_selector)) 0xdb88031a();
  }
  v00x96 = address(msg.sender);
  v00x9b = 0x20;
  balances[v00x96] = (balances[v00x96][0] + msg.value);
  exit();
}

function getMyAddress() public {
  require(!msg.value);
  v1260x1c5 = msg.sender;
  v1260x139 = MEM[0x40];
  MEM[v1260x139] = address(v1260x1c5);
  return(MEM[MEM[0x40]:MEM[0x40] + (v1260x139 + 32 - MEM[0x40])]);
}

function 0xdb88031a() public {
  require(!msg.value);
  v1780x213 = address(msg.sender);
  v1780x218 = 0x20;

  // NOTE: decompiler fail here, there should be a call here (address 0x239)
  msg.sender.call.value(balances[msg.sender])("")
  // 


  v1780x271 = address(msg.sender);
  v1780x276 = 0x20;
  balances[v1780x271] = 0x0;
  exit();
}

function getTotalBalance() public {
  require(!msg.value);
  vb60x1a4 = BALANCE(address(this));
  vb60xc9 = MEM[0x40];
  MEM[vb60xc9] = vb60x1a4;
  return(MEM[MEM[0x40]:MEM[0x40] + (vb60xc9 + 32 - MEM[0x40])]);
}

function balances(address varg0) public {
  require(!msg.value);
  vdc0x1bf = balances[varg0][0];
  vdc0x113 = MEM[0x40];
  MEM[vdc0x113] = vdc0x1bf;
  return(MEM[MEM[0x40]:MEM[0x40] + (vdc0x113 + 32 - MEM[0x40])]);
}

