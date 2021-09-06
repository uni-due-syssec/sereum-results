// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
uint256 money; // 0x0
uint256 __function_selector__; // 0x1

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  MEM[0x40] = 0x80;
  if ((msg.data.length() >= 0x4)) {
    if ((0x3c183c10 == function_selector)) 0x3c183c10();
    if ((0x98e1b410 == function_selector)) getMoney()();
  }
  if ((BALANCE(address(__function_selector__)) > 0x0)) {
    vcf = MEM[0x40];
    MEM[vcf] = 0x3ccfd60b00000000000000000000000000000000000000000000000000000000;
    require(isContract(address(__function_selector__)));
    v00x117 = v00xc7.call(MEM[v00xff : v00xff + v00x102]).value(v00x104).gas(msg.gas);
    if (!v00x117) {
      RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
      throw();
    }
  }
  exit();
}

function 0x3c183c10() public {
  v1fd = MEM[0x40];
  MEM[v1fd] = 0x3ccfd60b00000000000000000000000000000000000000000000000000000000;
  require(isContract(address(__function_selector__)));
  if (address(__function_selector__).call(MEM[MEM[0x40] : MEM[0x40] + (v1fd + 4 - MEM[0x40])]).gas(msg.gas)) {
    v12f0x277 = (BALANCE(address(this)) > v12f0x16b);
    require(v12f0x277);
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function getMoney() public {
  require(!msg.value);
  require((address(msg.sender) == address(money)));
  selfdestruct(address(money));
}

