// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
mapping (uint256 => [uint256]) balances;

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  MEM[0x40] = 0x80;
  if ((msg.data.length() >= 0x4)) {
    if ((0x27e235e3 == function_selector)) balances(address)(function_selector);
    if ((0x3ccfd60b == function_selector)) withdraw()();
  }
  v00x7d = address(msg.sender);
  v00x82 = 0x20;
  balances[v00x7d] = (balances[v00x7d][0] + msg.value);
  exit();
}

function balances(address varg0) public {
  require(!msg.value);
  v9a0x11d = balances[varg0][0];
  v9a0xde = MEM[0x40];
  MEM[v9a0xde] = v9a0x11d;
  return(MEM[MEM[0x40]:MEM[0x40] + (v9a0xde + 32 - MEM[0x40])]);
}

function withdraw() public {
  require(!msg.value);
  vf10x167 = address(msg.sender);
  vf10x16c = 0x20;

  // NOTE: the decompiler somehow missed a CALL instruction here
  msg.sender.call.value(balances[msg.sender])("")
  //

  vf10x1bd = address(msg.sender);
  vf10x1c2 = 0x20;
  balances[vf10x1bd] = 0x0;
  exit();
}

