// Decompiled at www.contract-library.com
// 2019.11.30 08:52 UTC

// Data structures and variables inferred from the use of storage instructions
uint256 _getBalance; // STORAGE[0x0]

// Events
event Transfer(string, address, address, uint256)
event Deposit(address, uint256)

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  freeMemPtr = 0x60;
  if (0x26224c64 == function_selector) 0x26224c64; // stack operands: ()
  if (0xccd6e5b6 == function_selector) 0xccd6e5b6; // stack operands: ()
  if (0xd0e30db0 == function_selector) deposit(); // stack operands: ()
  if (0xf8b2cb4f == function_selector) getBalance(address); // stack operands: ()
  throw();
}

function 0x26224c64(address varg0) public {
  require(!msg.value);
  return _getBalance[varg0][0];
}

function 0xccd6e5b6(uint256 varg0, address varg1) public {
  if (varg0 <= _getBalance[address(msg.sender)][0]) {
    /*call status*/v29e = address(varg1).call().value(varg0).gas(msg.gas - 34050);
    if (v29e) {
      _getBalance[address(msg.sender)] = (_getBalance[address(msg.sender)][0] - varg0);
      v468 =  new array[](0x11);
      emit Transfer(v468, address(msg.sender), address(varg1), varg0, v?, 0x5061796d656e742065786563757465642e000000000000000000000000000000);
    } else {
      v33e =  new array[](0x18);
      emit Transfer(v33e, address(msg.sender), address(varg1), varg0, v?, 0x43616c6c2e76616c75652077656e742077726f6e672e2e2e0000000000000000);
    }
  } else {
    v228 =  new array[](0x1e);
    emit Transfer(v228, address(msg.sender), address(varg1), varg0, v?, 'Amount greater than balance...\x00\x00');
  }
  exit();
}

function deposit() public {
  emit Deposit(address(msg.sender), msg.value);
  _getBalance[address(msg.sender)] = (_getBalance[address(msg.sender)][0] + msg.value);
  exit();
}

function getBalance(address varg0) public {
  require(!msg.value);
  return _getBalance[address(varg0)][0];
}

