// Decompiled at www.contract-library.com
// 2019.11.28 20:18 UTC

// Data structures and variables inferred from the use of storage instructions
uint256 stor_0; // STORAGE[0x0]
uint256 _money; // STORAGE[0x1]
uint256 ___function_selector__; // STORAGE[0x2]
uint256 stor_3; // STORAGE[0x3]
uint256 stor_4; // STORAGE[0x4]

// Events

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  if (msg.data.length() >= 0x4) {
    if (0x4ddd108a == function_selector) money(); // stack operands: ()
    if (0xb74387fc == function_selector) 0xb74387fc; // stack operands: ()
    if (0xe3295ec2 == function_selector) 0xe3295ec2; // stack operands: ()
  }
  ___function_selector__ = .function_selector__ + 1;
  if (msg.gas > .function_selector__*stor_3 + stor_4) {
    require(extcodesize(address(stor_0 >> 0)));
    /*call status*/v103, /*rets*/v130 = address(stor_0 >> 0).call(0x3892be14 << 224).gas(msg.gas);
    require(v103);
    require(RETURNDATASIZE >= 0x20);
  }
  exit();
}

function money() public {
  require(!msg.value);
  require(address(msg.sender) == address(_money >> 0));
  /*call status*/v23c = address(_money >> 0).call().value(address(this).balance).gas((!address(this).balance * 0x8fc));
  require(v23c);
  exit();
}

function 0xb74387fc() public {
  require(!msg.value);
  require(address(msg.sender) == address(_money >> 0));
  ___function_selector__ = 0x0;
  require(extcodesize(address(stor_0 >> 0)));
  /*call status*/v341, /*rets*/v36e = address(stor_0 >> 0).call(0x3892be14 << 224).gas(msg.gas);
  require(v341);
  require(RETURNDATASIZE >= 0x20);
  exit();
}

function 0xe3295ec2() public {
  require(address(msg.sender) == address(_money >> 0));
  require(extcodesize(address(stor_0 >> 0)));
  /*call status*/v46f, /*rets*/v49d = address(stor_0 >> 0).call(0x6bf0f4a1 << 224, 0x62).value(msg.value).gas(msg.gas);
  require(v46f);
  require(RETURNDATASIZE >= 0x20);
  exit();
}

