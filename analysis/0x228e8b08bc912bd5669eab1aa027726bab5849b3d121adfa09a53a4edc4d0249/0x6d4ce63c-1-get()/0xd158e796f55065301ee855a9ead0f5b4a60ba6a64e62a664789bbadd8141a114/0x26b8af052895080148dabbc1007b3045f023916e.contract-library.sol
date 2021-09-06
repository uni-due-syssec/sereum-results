// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
mapping (uint256 => [uint256]) put;

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  MEM[0x40] = 0x60;
  if (msg.data.length()) {
    if ((0x27e235e3 == function_selector)) balances(address)(function_selector);
    if ((0x46d6c084 == function_selector)) 0x46d6c084();
    if ((0x549262ba == function_selector)) put()();
    if ((0x6d4ce63c == function_selector)) get()();
  }
  require(!msg.value);
  throw();
}

function balances(address varg0) public {
  require(!msg.value);
  v720xf1 = put[varg0][0];
  v720xa6 = MEM[0x40];
  MEM[v720xa6] = v720xf1;
  return(MEM[MEM[0x40]:MEM[0x40] + (v720xa6 + 32 - MEM[0x40])]);
}

function 0x46d6c084() public {
  exit();
}

function put() public {
  vc30x129 = address(msg.sender);
  vc30x12e = 0x20;
  put[vc30x129] = msg.value;
  exit();
}

function get() public {
  require(!msg.value);
  vcd0x186 = address(msg.sender);
  vcd0x18b = 0x20;
  require(address(msg.sender).call(MEM[MEM[0x40] : MEM[0x40] + (MEM[0x40] - MEM[0x40])]).value(put[vcd0x186][0]).gas(msg.gas - 34050));
  vcd0x1ee = address(msg.sender);
  vcd0x1f3 = 0x20;
  put[vcd0x1ee] = 0x0;
  exit();
}

