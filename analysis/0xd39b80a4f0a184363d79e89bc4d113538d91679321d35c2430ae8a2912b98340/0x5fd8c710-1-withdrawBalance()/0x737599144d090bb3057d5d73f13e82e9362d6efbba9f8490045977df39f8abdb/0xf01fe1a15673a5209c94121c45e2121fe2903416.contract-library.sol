// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
mapping (uint256 => [uint256]) balances;

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint256 function_selector) public {
  MEM[0x40] = 0x60;
  if ((function_selector == 0x27e235e3)) balances(address)(function_selector);
  if ((0x5fd8c710 == function_selector)) withdrawBalance()();
  v00x2a = (0xd0e30db0 == v00xd);
  if (v00x2a) deposit()();
  v00x35 = (0xf8b2cb4f == v00xd);
  if (v00x35) getBalance(address)(v00xd);
  exit();
}

function balances(address varg0) public {
  MEM[0x60] = balances[varg0][0];
  return(MEM[0x60:0x80]);
}

function withdrawBalance() public {
  v540x61 = address(msg.sender);
  require(v540x61.call(MEM[0x60 : 0x60]).value(balances[v540x61][0]).gas(msg.gas - 34050));
  v540xf5 = address(msg.sender);
  v540xfa = 0x20;
  balances[v540xf5] = 0x0;
  exit();
}

function deposit() public {
  v910x9e = address(msg.sender);
  balances[v910x9e] = (0x16345785d8a0000 + balances[v910x9e][0]);
  exit();
}

function getBalance(address varg0) public {
  MEM[0x60] = balances[varg0][0];
  return(MEM[0x60:0x80]);
}

