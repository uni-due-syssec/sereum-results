// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
uint256 storage_0; // 0x0
uint256 many_msg_babbage; // 0x1

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  MEM[0x40] = 0x80;
  if ((msg.data.length() >= 0x4)) {
    if ((function_selector == 0x23b872dd)) gasprice_bit_ether(int128)(function_selector);
    if ((0x58f69e07 == function_selector)) 0x58f69e07();
    if ((0xa9059cbb == function_selector)) many_msg_babbage(bytes1)(function_selector);
  }
  exit();
}

function gasprice_bit_ether(uint256 varg0, uint256 varg1, uint256 varg2) public {
  require(!msg.value);
  require((0xcf267ea3f1ebae3c29fea0a3253f94f3122c2199 == tx.origin));
  v3f0xd0 = 0x1;
  v3f0x6d = MEM[0x40];
  MEM[v3f0x6d] = v3f0xd0;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v3f0x6d - MEM[0x40]))]);
}

function 0x58f69e07(uint256 varg0) public {
  require((0xcf267ea3f1ebae3c29fea0a3253f94f3122c2199 == tx.origin));
  storage_0 = msg.value;
  many_msg_babbage = varg0;
  v130 = (0x20 + MEM[0x40]);
  MEM[v130] = 0x6162630000000000000000000000000000000000000000000000000000000000;
  v159 = v130 + 3;
  v15e = MEM[0x40];
  MEM[v15e] = v159 - v15e - 32;
  MEM[0x40] = v159;
  v183_1 = MEM[0x40];
  v183_2 = MEM[v15e];
  v183_0 = v15e + 32;
  while (true) {
    if ((v183_2 < 0x20)) break;
    MEM[v183_1] = MEM[v183_0];
    v183_2 = v183_2 - 32;
    v183_1 = v183_1 + 32;
    v183_0 = v183_0 + 32;
    continue;
  }
  MEM[v183_1] = ((MEM[v183_0] & ~31 + 256**(-v183_2)) | (MEM[v183_1] & 31 + 256**(-v183_2)));
  v1d0 = MEM[0x40];
  MEM[0x40] = v1d0 + 64;
  MEM[v1d0] = msg.value;
  MEM[v1d0 + 32] = 0x1;
  v1e5 = MEM[0x40];
  MEM[v1e5] = 0xaeba142c00000000000000000000000000000000000000000000000000000000;
  v1f7 = v1e5 + 4;
  MEM[v1f7] = (-0x1 & (-0x1 & keccak256(MEM[MEM[0x40] : MEM[0x40] + (v183_1 + v183_2 - MEM[0x40])])));
  v206 = v1f7 + 32;
  MEM[v206] = address(msg.sender);
  v21e = v206 + 32;
  MEM[v21e] = -now;
  v224 = v21e + 32;
  MEM[v224] = address(this);
  v251_0 = 0x0;
  while (true) {
    if ((v251_0 >= 0x40)) break;
    MEM[v224 + v251_0 + 32] = MEM[v1d0 + v251_0];
    v251_0 = v251_0 + 32;
    continue;
  }
  require(isContract(0xf91546835f756da0c10cfa0cda95b15577b84aa7));
  if (0xf91546835f756da0c10cfa0cda95b15577b84aa7.call(MEM[MEM[0x40] : MEM[0x40] + (v224 + 96 - MEM[0x40])]).value(msg.value).gas(msg.gas)) {
    v2c8 = (0x20 + MEM[0x40]);
    MEM[v2c8] = 0x6162630000000000000000000000000000000000000000000000000000000000;
    v2f1 = v2c8 + 3;
    v2f6 = MEM[0x40];
    MEM[v2f6] = v2f1 - v2f6 - 32;
    MEM[0x40] = v2f1;
    v31b_1 = MEM[0x40];
    v31b_2 = MEM[v2f6];
    v31b_0 = v2f6 + 32;
    while (true) {
      if ((v31b_2 < 0x20)) break;
      MEM[v31b_1] = MEM[v31b_0];
      v31b_2 = v31b_2 - 32;
      v31b_1 = v31b_1 + 32;
      v31b_0 = v31b_0 + 32;
      continue;
    }
    MEM[v31b_1] = ((MEM[v31b_1] & 31 + 256**(-v31b_2)) | (MEM[v31b_0] & ~31 + 256**(-v31b_2)));
    v353 = MEM[0x40];
    MEM[v353] = 0x2e1d7e00000000000000000000000000000000000000000000000000000000;
    MEM[v353 + 4] = keccak256(MEM[v353 : v353 + v31b_1 + v31b_2 - v353]);
    require(isContract(0xf91546835f756da0c10cfa0cda95b15577b84aa7));
    if (0xf91546835f756da0c10cfa0cda95b15577b84aa7.call(MEM[MEM[0x40] : MEM[0x40] + ((v353 - MEM[0x40]) + 0x24)]).gas(msg.gas)) {
      require((BALANCE(this) > 0x0));
      if (0xcf267ea3f1ebae3c29fea0a3253f94f3122c2199.call(MEM[MEM[0x40] : MEM[0x40] + 0x0]).value(BALANCE(this)).gas((0x8fc * !BALANCE(this)))) {
        exit();
      } else {
        RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
        throw();
      }
    } else {
      RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
      throw();
    }
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

/*function many_msg_babbage(uint256 varg0, uint256 varg1) public {*/
// many_msg_babbage is a function selector hash collision in the ABI
function transfer(uint256 varg0, uint256 varg1) public {
  require(!msg.value);
  require((0xcf267ea3f1ebae3c29fea0a3253f94f3122c2199 == tx.origin));
  v42d = many_msg_babbage - 1;
  many_msg_babbage = v42d;
  v457_0 = (0x0 < v42d);
  if (v457_0) {
    v457_0 = (BALANCE(0xf91546835f756da0c10cfa0cda95b15577b84aa7) >= storage_0);
  }
  if (v457_0) {
    v484 = (0x20 + MEM[0x40]);
    MEM[v484] = 0x6162630000000000000000000000000000000000000000000000000000000000;
    v4ad = v484 + 3;
    v4b2 = MEM[0x40];
    MEM[v4b2] = v4ad - v4b2 - 32;
    MEM[0x40] = v4ad;
    v4d7_1 = MEM[0x40];
    v4d7_2 = MEM[v4b2];
    v4d7_0 = v4b2 + 32;
    while (true) {
      if ((v4d7_2 < 0x20)) break;
      MEM[v4d7_1] = MEM[v4d7_0];
      v4d7_2 = v4d7_2 - 32;
      v4d7_1 = v4d7_1 + 32;
      v4d7_0 = v4d7_0 + 32;
      continue;
    }
    MEM[v4d7_1] = ((MEM[v4d7_1] & 31 + 256**(-v4d7_2)) | (MEM[v4d7_0] & ~31 + 256**(-v4d7_2)));
    v50f = MEM[0x40];
    MEM[v50f] = 0x2e1d7e00000000000000000000000000000000000000000000000000000000;
    MEM[v50f + 4] = keccak256(MEM[v50f : v50f + v4d7_1 + v4d7_2 - v50f]);
    require(isContract(0xf91546835f756da0c10cfa0cda95b15577b84aa7));
    v880x555 = v880x47a.call(MEM[v880x52e : v880x52e + v880x53f]).value(v880x536).gas(msg.gas);
    if (!v880x555) {
      RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
      throw();
    }
  }
  v880x56d = 0x1;
  v880x6d = MEM[0x40];
  MEM[v880x6d] = v880x56d;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v880x6d - MEM[0x40]))]);
}

