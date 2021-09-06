// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
uint256 ceoAddress; // 0x0
uint256 autoBirthFee; // 0x1
uint256 autoBirthFee; // 0x10
uint256 storage_11; // 0x11
uint256 geneScience; // 0x12
uint256 promoCreatedCount; // 0x13
uint256 gen0CreatedCount; // 0x14
uint256 paused; // 0x2
uint256 storage_3; // 0x3
uint256 secondsPerBlock; // 0x5
uint256[] canBreedWith;
mapping (uint256 => [uint256]) ownerOf;
mapping (uint256 => [uint256]) owner_8;
mapping (uint256 => [uint256]) owner_9;
mapping (uint256 => [uint256]) sireAllowedToAddress;
uint256 saleAuction; // 0xb
uint256 siringAuction; // 0xc
uint256 owner_d; // 0xd
uint256 tokenContract; // 0xe
mapping (uint256 => [uint256]) tokenBalanceOf;

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  MEM[0x40] = 0x80;
  if ((msg.data.length() >= 0x4)) {
    if ((function_selector == 0x1ffc9a7)) supportsInterface(bytes4)(function_selector);
    if ((0x5e45546 == function_selector)) promoCreatedCount()(function_selector);
    if ((0x6fdde03 == function_selector)) name()(function_selector);
    if ((0x95ea7b3 == function_selector)) approve(address,uint256)();
    if ((0xa0f8168 == function_selector)) ceoAddress()(function_selector);
    if ((0xe583df0 == function_selector)) GEN0_STARTING_PRICE()(function_selector);
    if ((0xf47ec22 == function_selector)) 0x0f47ec22(function_selector);
    if ((0x14001f4c == function_selector)) setSiringAuctionAddress(address)();
    if ((0x18160ddd == function_selector)) totalSupply()(function_selector);
    if ((0x1940a936 == function_selector)) isPregnant(uint256)(function_selector);
    if ((0x19c2f201 == function_selector)) GEN0_AUCTION_DURATION()(function_selector);
    if ((0x1a266a69 == function_selector)) 0x1a266a69();
    if ((0x21717ebf == function_selector)) siringAuction()(function_selector);
    if ((0x23b872dd == function_selector)) gasprice_bit_ether(int128)(function_selector);
    if ((0x23e505d7 == function_selector)) 0x23e505d7();
    if ((0x24e7a38a == function_selector)) setGeneScienceAddress(address)();
    if ((0x26a4e8d2 == function_selector)) setTokenAddress(address)();
    if ((0x278ecde1 == function_selector)) refund(uint256)();
    if ((0x2a0ef02e == function_selector)) 0x2a0ef02e();
    if ((0x2ba73c15 == function_selector)) setCOO(address)();
    if ((0x2bbfd941 == function_selector)) 0x2bbfd941();
    if ((0x3d7d3f5a == function_selector)) createSaleAuction(uint256,uint256,uint256,uint256)();
    if ((0x3f4ba83a == function_selector)) unpause()();
    if ((0x46116e6f == function_selector)) sireAllowedToAddress(uint256)(function_selector);
    if ((0x46d22c70 == function_selector)) canBreedWith(uint256,uint256)(function_selector);
    if ((0x4ad8c938 == function_selector)) createSiringAuction(uint256,uint256,uint256,uint256)(function_selector);
    if ((0x4b136782 == function_selector)) 0x4b136782(function_selector);
    if ((0x4b85fd55 == function_selector)) setAutoBirthFee(uint256)();
    if ((0x4dfff04f == function_selector)) approveSiring(address,uint256)();
    if ((0x55a373d6 == function_selector)) tokenContract()(function_selector);
    if ((0x5663896e == function_selector)) setSecondsPerBlock(uint256)();
    if ((0x5c975abb == function_selector)) paused()(function_selector);
    if ((0x5de973a5 == function_selector)) 0x5de973a5(function_selector);
    if ((0x6352211e == function_selector)) ownerOf(uint256)();
    if ((0x680eba27 == function_selector)) GEN0_CREATION_LIMIT()(function_selector);
    if ((0x6e037679 == function_selector)) 0x6e037679(function_selector);
    if ((0x6fbde40d == function_selector)) setSaleAuctionAddress(address)();
    if ((0x70a08231 == function_selector)) balanceOf(address)(function_selector);
    if ((0x79a9232f == function_selector)) 0x79a9232f(function_selector);
    if ((0x7a7d4937 == function_selector)) secondsPerBlock()(function_selector);
    if ((0x8456cb59 == function_selector)) pause()();
    if ((0x8462151c == function_selector)) tokensOfOwner(address)(function_selector);
    if ((0x88c2a0bf == function_selector)) giveBirth(uint256)(function_selector);
    if ((0x92f64cce == function_selector)) 0x92f64cce(function_selector);
    if ((0x95d89b41 == function_selector)) symbol()(function_selector);
    if ((0x9d6fac6f == function_selector)) cooldowns(uint256)(function_selector);
    if ((0xa1045d73 == function_selector)) 0xa1045d73(function_selector);
    if ((0xa9059cbb == function_selector)) many_msg_babbage(bytes1)(function_selector);
    if ((0xad221195 == function_selector)) transferTokenFrom(address,address,uint256)();
    if ((0xb047fb50 == function_selector)) cooAddress()(function_selector);
    if ((0xb0c35c05 == function_selector)) autoBirthFee()(function_selector);
    if ((0xb9b8ea8e == function_selector)) 0xb9b8ea8e(function_selector);
    if ((0xc3bea9af == function_selector)) createGen0Auction(uint256)();
    if ((0xc754a0a3 == function_selector)) 0xc754a0a3(function_selector);
    if ((0xd3e6f49f == function_selector)) isReadyToBreed(uint256)(function_selector);
    if ((0xdefb9584 == function_selector)) GEN0_CREATION_LIMIT()(function_selector);
    if ((0xe42c08f2 == function_selector)) tokenBalanceOf(address)(function_selector);
    if ((0xe6cbe351 == function_selector)) saleAuction()(function_selector);
    if ((0xe86d5083 == function_selector)) 0xe86d5083(function_selector);
    if ((0xef299b0b == function_selector)) 0xef299b0b();
    if ((0xf1ca9410 == function_selector)) gen0CreatedCount()(function_selector);
    if ((0xf2b47d52 == function_selector)) geneScience()(function_selector);
  }
  throw();
}

function totalSupply_impl(uint256 vg0) private {
  return(canBreedWith.length - 1) // to vg0;
}

function isPregnant_impl(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2, uint256 vg4) private {
  v109c = (vg0 > 0x0);
  require(v109c);
  v10ad = (vg0 < canBreedWith.length);
  require(v10ad);
  v10c2 = 2*vg0;
  return(uint32((STORAGE[(0x1 + (v10c2 + keccak256(MEM[0x0 : 0x20])))] / 0x1000000000000000000000000000000000000000000000000))) // to vg2;
}

function 0x191e(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2) private {
  require(vg0);
  throw();
  0x29dc(uint32(vg2));
  while (true) {
    0xe67(vg0);
  }
  v191e0x306 = MEM[0x40];
  MEM[v191e0x306] = v191e0x2e36;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v191e0x306 - MEM[0x40]))]);
  v191e0x32f = MEM[0x40];
  MEM[v191e0x32f] = v191e0x2e36;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v191e0x32f - MEM[0x40]))]);
  exit();
  require(vg0);
  throw();
  0x298d(v?, v?, 0xe67);
  require(vg0);
  throw();
  0x295f(address(siringAuction), v?, 0x197e);
  v1985 = MEM[0x40];
  MEM[v1985] = 0xa91287300000000000000000000000000000000000000000000000000000000;
  MEM[v1985 + 132] = msg.sender;
  MEM[v1985 + 164] = 0x0;
  require(isContract(address(siringAuction)));
  if (!v1c570x12d2) {
  }
  if (!v191e0x12d2) {
  }
  vfd40x12d2 = vfd40x19ca.call(MEM[vfd40x19bf : vfd40x19bf + vfd40x19de]).value(vfd40x19b5).gas(msg.gas);
  if (vfd40x12d2) {
    GOTO ;
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
  if (!v2deb0x12d2) {
  }
  throw();
  0x29dc(vg2);
  while (true) {
    0x2091(vg0);
  }
  if (!vg0) {
  }
}

function balanceOf_impl(uint256 vg0, uint256 vg2) private {
  v1c39 = address(vg0);
  return(owner_8[v29ff][0]) // to vg2;
}

function 0x1c57(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2) private {
  require(vg0);
  throw();
  0x29dc(uint32(vg2));
  while (true) {
    0xe67(vg0);
  }
  v1c570x306 = MEM[0x40];
  MEM[v1c570x306] = v1c570x2e36;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v1c570x306 - MEM[0x40]))]);
  v1c570x32f = MEM[0x40];
  MEM[v1c570x32f] = v1c570x2e36;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v1c570x32f - MEM[0x40]))]);
  exit();
  require(vg0);
  throw();
  0x298d(v?, v?, 0xe67);
  require(vg0);
  throw();
  0x295f(address(siringAuction), v?, 0x197e);
  v1985 = MEM[0x40];
  MEM[v1985] = 0xa91287300000000000000000000000000000000000000000000000000000000;
  MEM[v1985 + 132] = msg.sender;
  MEM[v1985 + 164] = 0x0;
  require(isContract(address(siringAuction)));
  if (!v1c570x12d2) {
  }
  if (!v191e0x12d2) {
  }
  vfd40x12d2 = vfd40x19ca.call(MEM[vfd40x19bf : vfd40x19bf + vfd40x19de]).value(vfd40x19b5).gas(msg.gas);
  if (vfd40x12d2) {
    GOTO ;
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
  if (!v2deb0x12d2) {
  }
  throw();
}

function 0x2091(uint256 vg0, uint256 vg2, uint256 vg2) private {
  0x29dc(vg2);
  if (vg0) GOTO 0x209c;
  if (!vg0) {
  }
  throw();
  v20a4 = (v? < canBreedWith.length);
  require(v20a4);
  throw();
  v20b9 = MEM[0x40];
  MEM[0x40] = v20b9 + 256;
  v20c5 = (v? * 0x2);
  vg2 = (keccak256(MEM[0x0 : 0x20]) + v20c5);
  MEM[v20b9] = canBreedWith[v20c5][0];
  MEM[v20b9 + 32] = uint64(STORAGE[vg2 + 1]);
  MEM[v20b9 + 64] = uint64((STORAGE[vg2 + 1] / 0x10000000000000000));
  MEM[v20b9 + 96] = uint32((STORAGE[vg2 + 1] / 0x100000000000000000000000000000000));
  MEM[v20b9 + 128] = uint32((STORAGE[vg2 + 1] / 0x10000000000000000000000000000000000000000));
  MEM[v20b9 + 160] = uint32((STORAGE[vg2 + 1] / 0x1000000000000000000000000000000000000000000000000));
  MEM[v20b9 + 192] = uint16((STORAGE[vg2 + 1] / 0x100000000000000000000000000000000000000000000000000000000));
  MEM[v20b9 + 224] = uint16((STORAGE[vg2 + 1] / 0x1000000000000000000000000000000000000000000000000000000000000));
  vg2, v2154_1, vg2, vg2, vg2 = 0x3154(v20b9, 0x2155, vg2);
  require(vg2);
  throw();
  require((vg2 < canBreedWith.length));
  throw();
  v217d = MEM[0x40];
  MEM[0x40] = v217d + 256;
  MEM[v217d] = canBreedWith[2*vg2][0];
  MEM[v217d + 32] = uint64(STORAGE[((keccak256(MEM[0x0 : 0x20]) + 2*vg2) + 0x1)]);
  MEM[v217d + 64] = uint64((STORAGE[((keccak256(MEM[0x0 : 0x20]) + 2*vg2) + 0x1)] / 0x10000000000000000));
  MEM[v217d + 96] = uint32((STORAGE[((keccak256(MEM[0x0 : 0x20]) + 2*vg2) + 0x1)] / 0x100000000000000000000000000000000));
  MEM[v217d + 128] = uint32((STORAGE[((keccak256(MEM[0x0 : 0x20]) + 2*vg2) + 0x1)] / 0x10000000000000000000000000000000000000000));
  MEM[v217d + 160] = uint32((STORAGE[((keccak256(MEM[0x0 : 0x20]) + 2*vg2) + 0x1)] / 0x1000000000000000000000000000000000000000000000000));
  MEM[v217d + 192] = uint16((STORAGE[((keccak256(MEM[0x0 : 0x20]) + 2*vg2) + 0x1)] / 0x100000000000000000000000000000000000000000000000000000000));
  MEM[v217d + 224] = uint16((STORAGE[((keccak256(MEM[0x0 : 0x20]) + 2*vg2) + 0x1)] / 0x1000000000000000000000000000000000000000000000000000000000000));
  vg2, vg2, vg2, vg2, vg2 = 0x3154(v217d, 0x2219, (keccak256(MEM[0x0 : 0x20]) + 2*vg2));
  require(vg2);
  throw();
  v222f_0 = canBreedWith_impl(vg2, vg2, vg2, vg2, 0x2230);
  require(v222f_0);
  throw();
  v2245_0 = transferTokenFrom_impl(vg2, this, msg.sender, 0x2246, vg2);
}

function 0x2246(uint256 vg0, uint256 vg2, uint256 vg2) private {
  0x29dc(vg2);
}

function transferTokenFrom_impl(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2, uint256 vg4) private {
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  v239d = !vg0;
  if (vg0) {
    v23b2 = address(vg2);
    v23f2_0 = (v23b2 == msg.sender);
    if ((v23b2 != msg.sender)) {
      v23f2_0 = (msg.sender == address(saleAuction));
    }
    if (!v23f2_0) {
      v23f2_0 = (msg.sender == address(siringAuction));
    }
    if (!v23f2_0) {
      v23f2_0 = (msg.sender == address(owner_d));
    }
    require(v23f2_0);
    v2407 = address(vg2);
    require(v2407);
    v241c = address(vg2);
    v242d = (vg0 > tokenBalanceOf[v29ff][0]);
    require((vg0 <= tokenBalanceOf[v29ff][0]));
    v2441 = address(vg2);
    v2453 = (tokenBalanceOf[v29ff][0] + vg0);
    require((v2453 > tokenBalanceOf[v29ff][0]));
    v2469 = address(vg2);
    v247d = address(vg2);
    v2486 = (tokenBalanceOf[v29ff][0] - vg0);
    tokenBalanceOf[v29ff] = v2486;
    v248c = (vg0 + tokenBalanceOf[v29ff][0]);
    tokenBalanceOf[v29ff] = v248c;
    require(((tokenBalanceOf[v29ff][0] + tokenBalanceOf[v29ff][0]) == (tokenBalanceOf[v29ff][0] + v248c)));
    v24a2 = MEM[0x40];
    v24ad = address(vg2);
    MEM[v24a2] = v24ad;
    v24b1 = address(vg2);
    MEM[v24a2 + 32] = v24b1;
    MEM[v24a2 + 64] = vg0;
    log(MEM[0x40], (0x60 + (v24a2 - MEM[0x40])), 0x3844b7075ed6e7d4b61342769cb2b1b325cba410a62932affaa90aee247dadf5);
    return() // to vg2;
  } else {
    0xfd4();
  }
}

function isReadyToBreed_impl(uint256 vg0, uint256 vg2, uint256 vg2) private {
  v275c = (vg0 > 0x0);
  require(v275c);
  v276d = (vg0 < canBreedWith.length);
  require(v276d);
  v2782 = MEM[0x40];
  MEM[0x40] = v2782 + 256;
  v278e = 2*vg0;
  MEM[v2782] = canBreedWith[v278e][0];
  MEM[v2782 + 32] = uint64(STORAGE[((keccak256(MEM[0x0 : 0x20]) + v278e) + 0x1)]);
  MEM[v2782 + 64] = uint64((STORAGE[((keccak256(MEM[0x0 : 0x20]) + v278e) + 0x1)] / 0x10000000000000000));
  MEM[v2782 + 96] = uint32((STORAGE[((keccak256(MEM[0x0 : 0x20]) + v278e) + 0x1)] / 0x100000000000000000000000000000000));
  MEM[v2782 + 128] = uint32((STORAGE[((keccak256(MEM[0x0 : 0x20]) + v278e) + 0x1)] / 0x10000000000000000000000000000000000000000));
  MEM[v2782 + 160] = uint32((STORAGE[((keccak256(MEM[0x0 : 0x20]) + v278e) + 0x1)] / 0x1000000000000000000000000000000000000000000000000));
  MEM[v2782 + 192] = uint16((STORAGE[((keccak256(MEM[0x0 : 0x20]) + v278e) + 0x1)] / 0x100000000000000000000000000000000000000000000000000000000));
  MEM[v2782 + 224] = uint16((STORAGE[((keccak256(MEM[0x0 : 0x20]) + v278e) + 0x1)] / 0x1000000000000000000000000000000000000000000000000000000000000));
  v281d_0, v281d_1, v281d_2, v281d_3, v281d_4 = 0x3154(v2782, 0x1c57, (keccak256(MEM[0x0 : 0x20]) + v278e));
}

/*function isOwner(uint256 vg0, uint256 vg2, uint256 vg2) private {*/
/// probably something like isOwner(f, a)
function isOwner(uint256 vg0, uint256 vg2, uint256 vg2) private {
  v294e = ownerOf[vg0][0];
  v2959 = address(vg2);
  return((address(v294e) == v2959)) // to vg2;
}

function 0x295f(uint256 vg0, uint256 vg2, uint256 vg2) private {
  v2970 = owner_9[vg2][0];
  v2985 = address(vg0);
  owner_9[vg2] = (v2985 | (-0x10000000000000000000000000000000000000000 & v2970));
  return() // to vg2;
}

function 0x298d(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2, uint256 vg4, uint256 vg5, uint256 vg6) private {
  v2999 = (vg2 < canBreedWith.length);
  require(v2999);
  v29ae = 2*vg2;
  v29b8 = (vg0 < canBreedWith.length);
  require(v29b8);
  v29cd = 2*vg0;
  v29db_0 = canBreedWith_impl(vg0, (v29cd + keccak256(MEM[0x0 : 0x20])), vg2, (v29ae + keccak256(MEM[0x0 : 0x20])), 0x191e);
}

function 0x29dc(uint256 vg0) private {
  v29e6 = (vg0 < canBreedWith.length);
  require(v29e6);
  v29fb = 2*vg0;
  v29ff = 0x6;
  v2a05 = (v? < canBreedWith.length);
  require(v2a05);
  v2a1c = (v? * 0x2);
  v2a21 = ((v2a1c + keccak256(MEM[0x0 : 0x20])) + 0x1);
  v2a4e = uint32(vg0);
  STORAGE[v2a21] = (6277101735386680763835789423207666416102355444464034512896*v2a4e | (-0xffffffff000000000000000000000000000000000000000000000001 & STORAGE[v2a21]));
  0x3183((v29fb + keccak256(MEM[0x0 : 0x20])), 0x2a5d);
  0x3183((v2a1c + keccak256(MEM[0x0 : 0x20])), 0x2a66);
}

function 0x2b3a(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2, uint256 vg4, uint256 vg5, uint256 vg6, uint256 vg7, uint256 vg8, uint256 vg9, uint256 vga, uint256 vgb, uint256 vgc, uint256 vgd) private {
  v2b45 = address(vg2);
  owner_8[v29ff] = (0x1 + owner_8[v29ff][0]);
  v2b69 = ownerOf[vg0][0];
  ownerOf[vg0] = (v2b45 | (-0x10000000000000000000000000000000000000000 & v2b69));
  v2b7a = address(vg2);
  if (v2b7a) {
    v2b89 = address(vg2);
    owner_8[v29ff] = (-0x1 + owner_8[v29ff][0]);
    v2bae = sireAllowedToAddress[vg0][0];
    sireAllowedToAddress[vg0] = (-0x10000000000000000000000000000000000000000 & v2bae);
    v2bc7 = owner_9[vg0][0];
    owner_9[vg0] = (-0x10000000000000000000000000000000000000000 & v2bc7);
  }
  v2bd1 = MEM[0x40];
  v2bdc = address(vg2);
  MEM[v2bd1] = v2bdc;
  v2be0 = address(vg2);
  MEM[v2bd1 + 32] = v2be0;
  MEM[v2bd1 + 64] = vg0;
  log(MEM[0x40], (0x60 + (v2bd1 - MEM[0x40])), 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef);
  GOTO vg2;
  exit();
  GOTO v2b3aarg6;
  return(vg4) // to vgd;
}

function canBreedWith_impl(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2, uint256 vg4) private {
  v2c70 = (vg2 == vg0);
  if ((vg2 != vg0)) {
    v2c81 = vg2 + 1;
    v2cac_0 = (vg0 == uint32((STORAGE[v2c81] / 0x100000000000000000000000000000000)));
    if ((vg0 != uint32((STORAGE[v2c81] / 0x100000000000000000000000000000000)))) {
      v2c9b = vg2 + 1;
      v2cac_0 = (vg0 == uint32((STORAGE[v2c9b] / 0x10000000000000000000000000000000000000000)));
    }
    if (!v2cac_0) {
      v2cbd = vg2 + 1;
      v2ce8_0 = (vg2 == uint32((STORAGE[v2cbd] / 0x100000000000000000000000000000000)));
      if ((vg2 != uint32((STORAGE[v2cbd] / 0x100000000000000000000000000000000)))) {
        v2cd7 = vg2 + 1;
        v2ce8_0 = (vg2 == uint32((STORAGE[v2cd7] / 0x10000000000000000000000000000000000000000)));
      }
      if (!v2ce8_0) {
        v2cf9 = vg2 + 1;
        v2d22_0 = !uint32((STORAGE[v2cf9] / 0x100000000000000000000000000000000));
        if (uint32((STORAGE[v2cf9] / 0x100000000000000000000000000000000))) {
          v2d12 = vg2 + 1;
          v2d22_0 = !uint32((STORAGE[v2d12] / 0x100000000000000000000000000000000));
        }
        if (!v2d22_0) {
          v2d34 = vg2 + 1;
          v2d38 = vg2 + 1;
          v2d7a_0 = (uint32((STORAGE[v2d38] / 0x100000000000000000000000000000000)) == uint32((STORAGE[v2d34] / 0x100000000000000000000000000000000)));
          if ((uint32((STORAGE[v2d38] / 0x100000000000000000000000000000000)) != uint32((STORAGE[v2d34] / 0x100000000000000000000000000000000)))) {
            v2d5b = vg2 + 1;
            v2d5f = vg2 + 1;
            v2d7a_0 = (uint32((STORAGE[v2d5b] / 0x10000000000000000000000000000000000000000)) == uint32((STORAGE[v2d5f] / 0x100000000000000000000000000000000)));
          }
          if (!v2d7a_0) {
            v2d8c = vg2 + 1;
            v2d90 = vg2 + 1;
            v2dd2_0 = (uint32((STORAGE[v2d8c] / 0x100000000000000000000000000000000)) == uint32((STORAGE[v2d90] / 0x10000000000000000000000000000000000000000)));
            if ((uint32((STORAGE[v2d8c] / 0x100000000000000000000000000000000)) != uint32((STORAGE[v2d90] / 0x10000000000000000000000000000000000000000)))) {
              v2db5 = vg2 + 1;
              v2db9 = vg2 + 1;
              v2dd2_0 = (uint32((STORAGE[v2db9] / 0x10000000000000000000000000000000000000000)) == uint32((STORAGE[v2db5] / 0x10000000000000000000000000000000000000000)));
            }
            if (!v2dd2_0) {
              v2de3_0 = 0x1;
            } else {
              v2de3_0 = 0x0;
              GOTO 0x2de3;
            }
          } else {
            v2de3_0 = 0x0;
            GOTO 0x2de3;
          }
        } else {
          v2de3_0 = 0x1;
          GOTO 0x2de3;
        }
      } else {
        v2de3_0 = 0x0;
        GOTO 0x2de3;
      }
    } else {
      v2de3_0 = 0x0;
      GOTO 0x2de3;
    }
  } else {
    v2de3_0 = 0x0;
  }
  return(v2de3_0) // to vg4;
}

function supportsInterface(bytes4 varg0) public {
  require(!msg.value);
  vg2 = 0x302;
  vab8 = MEM[0x40];
  MEM[vab8] = 0x737570706f727473496e74657266616365286279746573342900000000000000;
  if (((keccak256(MEM[MEM[0x40] : MEM[0x40] + (0x19 + (vab8 - MEM[0x40]))]) & -0x100000000000000000000000000000000000000000000000000000000) == (-0x100000000000000000000000000000000000000000000000000000000 & (varg0 & -0x100000000000000000000000000000000000000000000000000000000)))) supportsInterface_impl(((keccak256(MEM[MEM[0x40] : MEM[0x40] + (0x19 + (vab8 - MEM[0x40]))]) & -0x100000000000000000000000000000000000000000000000000000000) == (-0x100000000000000000000000000000000000000000000000000000000 & (varg0 & -0x100000000000000000000000000000000000000000000000000000000))), 0x0, (varg0 & -0x100000000000000000000000000000000000000000000000000000000));
  vb17 = MEM[0x40];
  MEM[vb17] = 0x746f6b656e4d657461646174612875696e743235362c737472696e6729000000;
  vb3c = MEM[0x40];
  MEM[vb3c] = 0x746f6b656e734f664f776e657228616464726573732900000000000000000000;
  vb6a = MEM[0x40];
  MEM[vb6a] = 0x7472616e7366657246726f6d28616464726573732c616464726573732c75696e;
  MEM[vb6a + 32] = 0x7432353629000000000000000000000000000000000000000000000000000000;
  vbbe = MEM[0x40];
  MEM[vbbe] = 0x7472616e7366657228616464726573732c75696e743235362900000000000000;
  vbec = MEM[0x40];
  MEM[vbec] = 0x617070726f766528616464726573732c75696e74323536290000000000000000;
  vc1a = MEM[0x40];
  MEM[vc1a] = 0x6f776e65724f662875696e743235362900000000000000000000000000000000;
  vc48 = MEM[0x40];
  MEM[vc48] = 0x62616c616e63654f662861646472657373290000000000000000000000000000;
  vc76 = MEM[0x40];
  MEM[vc76] = 0x746f74616c537570706c79282900000000000000000000000000000000000000;
  vca4 = MEM[0x40];
  MEM[vca4] = 0x73796d626f6c2829000000000000000000000000000000000000000000000000;
  vcd2 = MEM[0x40];
  MEM[vcd2] = 0x6e616d6528290000000000000000000000000000000000000000000000000000;
  vd38 = (((((((keccak256(MEM[vca4 : vca4 + vc76 - vca4 + 13]) ^ (keccak256(MEM[vcd2 : vcd2 + vca4 - vcd2 + 8]) ^ keccak256(MEM[MEM[0x40] : MEM[0x40] + (0x6 + (vcd2 - MEM[0x40]))]))) ^ keccak256(MEM[vc76 : vc76 + vc48 - vc76 + 18])) ^ keccak256(MEM[vc48 : vc48 + vc1a - vc48 + 16])) ^ keccak256(MEM[vc1a : vc1a + vbec - vc1a + 24])) ^ keccak256(MEM[vbec : vbec + vbbe - vbec + 25])) ^ keccak256(MEM[vbbe : vbbe + vb6a - vbbe + 37])) ^ keccak256(MEM[vb6a : vb6a + vb3c - vb6a + 22]));
  vg0 = (((vd38 ^ keccak256(MEM[vb3c : vb3c + vb17 - vb3c + 29])) & -0x100000000000000000000000000000000000000000000000000000000) == (-0x100000000000000000000000000000000000000000000000000000000 & (varg0 & -0x100000000000000000000000000000000000000000000000000000000)));
  return(vg0) // to vg2;
}

function 0x2deb(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2) private {
  require(vg0);
  throw();
  0x29dc(uint32(vg2));
  while (true) {
    0xe67(vg0);
  }
  v2deb0x306 = MEM[0x40];
  MEM[v2deb0x306] = v2deb0x2e36;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v2deb0x306 - MEM[0x40]))]);
  v2deb0x32f = MEM[0x40];
  MEM[v2deb0x32f] = v2deb0x2e36;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v2deb0x32f - MEM[0x40]))]);
  exit();
  require(vg0);
  throw();
  0x298d(v?, v?, 0xe67);
  require(vg0);
  throw();
  0x295f(address(siringAuction), v?, 0x197e);
  v1985 = MEM[0x40];
  MEM[v1985] = 0xa91287300000000000000000000000000000000000000000000000000000000;
  MEM[v1985 + 132] = msg.sender;
  MEM[v1985 + 164] = 0x0;
  require(isContract(address(siringAuction)));
  if (!v1c570x12d2) {
  }
  if (!v191e0x12d2) {
  }
  vfd40x12d2 = vfd40x19ca.call(MEM[vfd40x19bf : vfd40x19bf + vfd40x19de]).value(vfd40x19b5).gas(msg.gas);
  if (vfd40x12d2) {
    GOTO ;
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
  if (!v2deb0x12d2) {
  }
  throw();
  0x29dc(vg2);
  while (true) {
    0x2091(vg0);
  }
  if (!vg0) {
  }
  v2dfb = ownerOf[vg0][0];
  v2e02 = ownerOf[vg2][0];
  if ((address(v2dfb) == address(v2e02))) 0x191e((address(v2dfb) == address(v2e02)), address(v2e02), address(v2dfb), 0x0);
  v2e27 = sireAllowedToAddress[vg2][0];
  vg0 = (address(v2dfb) == address(v2e27));
  0x2091(vg0);
}

function createGen0Auction_impl(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2, uint256 vg4, uint256 vg5, uint256 vg6, uint256 vg7, uint256 vg8, uint256 vg9, uint256 vga, uint256 vgb, uint256 vgc, uint256 vgd) private {
  v3270 = MEM[0x40];
  MEM[0x40] = v3270 + 256;
  MEM[v3270] = 0x0;
  MEM[v3270 + 32] = 0x0;
  MEM[v3270 + 64] = 0x0;
  MEM[v3270 + 96] = 0x0;
  MEM[v3270 + 128] = 0x0;
  MEM[v3270 + 160] = 0x0;
  MEM[v3270 + 192] = 0x0;
  MEM[v3270 + 224] = 0x0;
  v2e54 = uint32(vg4);
  v2e56 = (vg4 == v2e54);
  require(v2e56);
  v2e66 = uint32(vg2);
  v2e68 = (vg2 == v2e66);
  require(v2e68);
  v2e76 = uint16(vg2);
  v2e78 = (vg2 == v2e76);
  require(v2e78);
  v3097_2 = vg2/2;
  if ((uint16(v3097_2) > 0xd)) {
    v3097_2 = 0xd;
  }
  v2e9f = MEM[0x40];
  MEM[0x40] = v2e9f + 256;
  MEM[v2e9f] = vg2;
  v2eba = v2e9f + 32;
  MEM[v2eba] = uint64(now);
  v2ec2 = v2e9f + 64;
  MEM[v2ec2] = 0x0;
  v2ecd = uint32(vg4);
  v2ed1 = v2e9f + 96;
  MEM[v2ed1] = v2ecd;
  v2ed7 = uint32(vg2);
  v2edb = v2e9f + 128;
  MEM[v2edb] = v2ed7;
  v2ee2 = v2e9f + 160;
  MEM[v2ee2] = 0x0;
  v2eef = v2e9f + 192;
  MEM[v2eef] = uint16(v3097_2);
  v2ef5 = uint16(vg2);
  v2ef9 = v2e9f + 224;
  MEM[v2ef9] = v2ef5;
  v2f00 = canBreedWith.length;
  canBreedWith.length = v2f00 + 1;
  MEM[0x0] = 0x6;
  STORAGE[2*v2f00 + 111414077815863400510004064629973595961579173665589224203503662149373724986687] = MEM[v2e9f];
  v2f5c = 2*v2f00 + 111414077815863400510004064629973595961579173665589224203503662149373724986688;
  v3085 = ((uint16(MEM[v2ef9]) * 0x1000000000000000000000000000000000000000000000000000000000000) | (0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff & ((uint16(MEM[v2eef]) * 0x100000000000000000000000000000000000000000000000000000000) | (0xffff0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff & ((uint32(MEM[v2ee2]) * 0x1000000000000000000000000000000000000000000000000) | (-0xffffffff000000000000000000000000000000000000000000000001 & ((uint32(MEM[v2edb]) * 0x10000000000000000000000000000000000000000) | (-0xffffffff0000000000000000000000000000000000000001 & ((uint32(MEM[v2ed1]) * 0x100000000000000000000000000000000) | (-0xffffffff00000000000000000000000000000001 & ((uint64(MEM[v2ec2]) * 0x10000000000000000) | (-0xffffffffffffffff0000000000000001 & (uint64(MEM[v2eba]) | (STORAGE[v2f5c] & -0x10000000000000000))))))))))))));
  STORAGE[v2f5c] = v3085;
  require((v2f00 == uint32(v2f00)));
  v30a9 = MEM[0x40];
  v30b3 = address(vg0);
  MEM[v30a9] = v30b3;
  MEM[v30a9 + 32] = v2f00;
  MEM[v30a9 + 64] = uint32(MEM[v2e9f + 96]);
  MEM[v30a9 + 96] = uint32(MEM[v2e9f + 128]);
  MEM[v30a9 + 128] = vg2;
  MEM[v30a9 + 160] = MEM[v2e9f];
  log(MEM[0x40], (0xc0 + (v30a9 - MEM[0x40])), 0xa2950fd8c03e7518275ee57e05ca76c671969b5445b12b1aeea4b0b30195e5df);
  0x2b3a(v2f00, vg0, 0x0, 0x3118, v2f00, v2e9f, v3097_2, 0x0, vg0, vg2, vg2);
}

function 0x3154(uint256 vg0, uint256 vg2, uint256 vg2) private {
  v315a = vg0 + 160;
  if ((0x0 != uint32(MEM[v315a]))) supportsInterface_impl((0x0 == uint32(MEM[v315a])), 0x0, vg0);
  v316f = vg0 + 64;
  return((uint64(MEM[v316f]) <= uint64(block.number))) // to vg2;
}

function promoCreatedCount() public {
  require(!msg.value);
  v3160xd4a = promoCreatedCount;
  v3160x32f = MEM[0x40];
  MEM[v3160x32f] = v3160xd4a;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v3160x32f - MEM[0x40]))]);
}

function 0x3183(uint256 vg0, uint256 vg2) private {
  v318a = vg0 + 1;
  require((uint16((STORAGE[v318a] / 0x100000000000000000000000000000000000000000000000000000000)) < 0xe));
  require(secondsPerBlock);
  v31d5 = vg0 + 1;
  v320b = ((uint64(((uint32((STORAGE[((uint16((STORAGE[v318a] / 0x100000000000000000000000000000000000000000000000000000000)) / 0x8) + 0x3)] / (0x100 ** (0x4 * (uint16((STORAGE[v318a] / 0x100000000000000000000000000000000000000000000000000000000)) % 0x8))))) / secondsPerBlock) + block.number)) * 0x10000000000000000) | (-0xffffffffffffffff0000000000000001 & STORAGE[v31d5]));
  STORAGE[v31d5] = v320b;
  if ((uint16(v320b/26959946667150639794667015087019630673637144422540572481103610249216) < 0xd)) {
    v3228 = vg0 + 1;
    STORAGE[v3228] = ((STORAGE[v3228] & 0xffff0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff) | (0x100000000000000000000000000000000000000000000000000000000 * uint16((0x1 + uint16((STORAGE[v3228] / 0x100000000000000000000000000000000000000000000000000000000))))));
  }
  return() // to vg2;
}

function name() public {
  require(!msg.value);
  v33d0xd51 = MEM[0x40];
  MEM[0x40] = v33d0xd51 + 64;
  MEM[v33d0xd51] = 0xb;
  MEM[v33d0xd51 + 32] = 0x43727970746f466f786573000000000000000000000000000000000000000000;
  v33d0x356 = MEM[0x40];
  MEM[v33d0x356] = 0x20;
  MEM[v33d0x356 + 32] = MEM[v33d0xd51];
  v37d0x33d_0 = 0x0;
  while (true) {
    if ((v37d0x33d_0 >= MEM[v33d0xd51])) break;
    MEM[v33d0x356 + v37d0x33d_0 + 64] = MEM[v33d0xd51 + v37d0x33d_0 + 32];
    v37d0x33d_0 = v37d0x33d_0 + 32;
    GOTO 0x374;
  }
  v3b90x33d_1 = (MEM[v33d0xd51] + v33d0x356 + 64);
  if ((0x1f & MEM[v33d0xd51])) {
    v33d0x3a2 = (v3b90x33d_1 - (0x1f & MEM[v33d0xd51]));
    MEM[v33d0x3a2] = (~((0x100 ** (0x20 - (0x1f & MEM[v33d0xd51]))) - 0x1) & MEM[v33d0x3a2]);
    v3b90x33d_1 = v33d0x3a2 + 32;
  }
  return(MEM[MEM[0x40]:MEM[0x40] + (v3b90x33d_1 - MEM[0x40])]);
}

function approve(address varg0, uint256 varg1) public {
  require(!msg.value);
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  vda4_0 = isOwner(varg1, msg.sender, 0xda5);
  require(vda4_0);
  0x295f(varg0, varg1, 0xdba);
  v3c70xdbe = MEM[0x40];
  MEM[v3c70xdbe] = msg.sender;
  v3c70xdcb = address(v3c70x3e3);
  MEM[v3c70xdbe + 32] = v3c70xdcb;
  MEM[v3c70xdbe + 64] = v3c70x3e6;
  log(MEM[0x40], (0x60 + (v3c70xdbe - MEM[0x40])), 0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925);
  exit();
}

function ceoAddress() public {
  require(!msg.value);
  v3ed0xe12 = address(ceoAddress);
  v3ed0x406 = MEM[0x40];
  MEM[v3ed0x406] = address(v3ed0xe12);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v3ed0x406 - MEM[0x40]))]);
}

function GEN0_STARTING_PRICE() public {
  require(!msg.value);
  v41e0xe16 = 0x64;
  v41e0x32f = MEM[0x40];
  MEM[v41e0x32f] = v41e0xe16;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v41e0x32f - MEM[0x40]))]);
}

function 0x0f47ec22(uint256 varg0, uint256 varg1, uint256 varg2) public {
  require(!msg.value);
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  require(isOwner(varg1, msg.sender, 0xe3e));
  isReadyToBreed_impl(varg1, 0xe52, 0x0);
}

function setSiringAuctionAddress(address varg0) public {
  require(!msg.value);
  require((msg.sender == address(ceoAddress)));
  v1007 = MEM[0x40];
  MEM[v1007] = 0x76190f8f00000000000000000000000000000000000000000000000000000000;
  require(isContract(address(varg0)));
  if (address(varg0).call(MEM[MEM[0x40] : MEM[0x40] + (v1007 + 4 - MEM[0x40])]).gas(msg.gas)) {
    require((RETURNDATASIZE >= 0x20));
    v4510x105f = MEM[v4510x104e];
    require(v4510x105f);
    v4510x1084 = address(v4510x46d);
    siringAuction = (v4510x1084 | (-0x10000000000000000000000000000000000000000 & siringAuction));
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function totalSupply() public {
  require(!msg.value);
  v486_0 = totalSupply_impl(0x32b);
  v4720x32f = MEM[0x40];
  MEM[v4720x32f] = v4720x486_0;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v4720x32f - MEM[0x40]))]);
}

function isPregnant(uint256 varg0) public {
  require(!msg.value);
  v49e_0, v49e_1, v49e_2, v49e_3 = isPregnant_impl(varg0, 0x302);
  v4870x306 = MEM[0x40];
  v4870x308 = !v4870x49e_0;
  MEM[v4870x306] = v4870x49e_0;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v4870x306 - MEM[0x40]))]);
}

function GEN0_AUCTION_DURATION() public {
  require(!msg.value);
  v49f0x10dd = 0xd2f00;
  v49f0x32f = MEM[0x40];
  MEM[v49f0x32f] = v49f0x10dd;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v49f0x32f - MEM[0x40]))]);
}

function 0x1a266a69(uint256 varg0) public {
  require(!msg.value);
  require((msg.sender == address(ceoAddress)));
  v4b40x1104 = address(v4b40x4d0);
  require(v4b40x1104);
  v4b40x1129 = address(v4b40x4d0);
  paused = (v4b40x1129 | (-0x10000000000000000000000000000000000000000 & paused));
  exit();
}

function siringAuction() public {
  require(!msg.value);
  v4d50x113d = address(siringAuction);
  v4d50x406 = MEM[0x40];
  MEM[v4d50x406] = address(v4d50x113d);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v4d50x406 - MEM[0x40]))]);
}

function gasprice_bit_ether(address varg0, address varg1, uint256 varg2) public {
  require(!msg.value);
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  require(address(varg1));
  require((this != address(varg1)));
  v2b37 = (address(owner_9[varg2][0]) == address(msg.sender));
  require(v2b37);
  v11a0_0 = isOwner(varg2, varg0, 0x11a1);
  require(v11a0_0);
  0x2b3a(varg2, varg1, varg0, 0x11b7, varg2, varg1, varg0);
}

function 0x23e505d7(uint256 varg0, uint256 varg1, uint256 varg2, uint256 varg3) public {
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  require((msg.value >= varg1));
  v11ec_0 = isOwner(varg0, msg.sender, 0x11ed);
  require(v11ec_0);
  v1200_0, v1200_1, v1200_2, v1200_3 = isPregnant_impl(varg0, 0x1201, varg3, varg2, varg1);
  require(!v1200_0);
  if (address(ceoAddress).call(MEM[MEM[0x40] : MEM[0x40] + 0x0]).value(msg.value).gas((0x8fc * !msg.value))) {
    0x295f(address(saleAuction), varg0, 0x125d);
    v1264 = MEM[0x40];
    MEM[v1264] = 0xa91287300000000000000000000000000000000000000000000000000000000;
    MEM[v1264 + 4] = varg0;
    MEM[v1264 + 36] = v1200_3;
    MEM[v1264 + 68] = v1200_2;
    MEM[v1264 + 100] = v1200_1;
    MEM[v1264 + 132] = msg.sender;
    MEM[v1264 + 164] = 0x1;
    require(isContract(address(saleAuction)));
    v5140x12d2 = v5140x12a7.call(MEM[v5140x129c : v5140x129c + v5140x12be]).value(v5140x12b5).gas(msg.gas);
    if (v5140x12d2) {
      exit();
    } else {
      RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
      throw();
    }
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function setGeneScienceAddress(address varg0) public {
  require(!msg.value);
  require((msg.sender == address(ceoAddress)));
  v131a = MEM[0x40];
  MEM[v131a] = 0x54c15b8200000000000000000000000000000000000000000000000000000000;
  require(isContract(address(varg0)));
  if (address(varg0).call(MEM[MEM[0x40] : MEM[0x40] + (v131a + 4 - MEM[0x40])]).gas(msg.gas)) {
    require((RETURNDATASIZE >= 0x20));
    v5280x1372 = MEM[v5280x1361];
    require(v5280x1372);
    v5280x1397 = address(v5280x544);
    geneScience = (v5280x1397 | (-0x10000000000000000000000000000000000000000 & geneScience));
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function setTokenAddress(address varg0) public {
  require(!msg.value);
  require((msg.sender == address(ceoAddress)));
  v13bd = MEM[0x40];
  MEM[v13bd] = 0x1ffc9a700000000000000000000000000000000000000000000000000000000;
  MEM[v13bd + 4] = 0xa5126e4500000000000000000000000000000000000000000000000000000000;
  require(isContract(address(varg0)));
  if (address(varg0).call(MEM[MEM[0x40] : MEM[0x40] + ((v13bd - MEM[0x40]) + 0x24)]).gas(msg.gas)) {
    require((RETURNDATASIZE >= 0x20));
    v5490x1469 = MEM[v5490x1458];
    require(v5490x1469);
    v5490x148e = address(v5490x565);
    tokenContract = (v5490x148e | (-0x10000000000000000000000000000000000000000 & tokenContract));
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function refund(uint256 varg0) public {
  require(!msg.value);
  v1498 = msg.sender;
  require((varg0 <= tokenBalanceOf[v1498][0]));
  v14ba = MEM[0x40];
  MEM[v14ba] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000;
  MEM[v14ba + 4] = msg.sender;
  MEM[v14ba + 36] = varg0;
  require(isContract(address(tokenContract)));
  v56a0x1522 = v56a0x14f7.call(MEM[v56a0x14ec : v56a0x14ec + v56a0x150e]).value(v56a0x1505).gas(msg.gas);
  if (v56a0x1522) {
    v56a0x1536 = msg.sender;
    v56a0x154a = (tokenBalanceOf[v56a0x1536][0] - v56a0x57d);
    tokenBalanceOf[v56a0x1536] = v56a0x154a;
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function 0x2a0ef02e(address varg0) public {
  require(!msg.value);
  require((msg.sender == address(ceoAddress)));
  v157e = MEM[0x40];
  MEM[v157e] = 0xc7b8351900000000000000000000000000000000000000000000000000000000;
  require(isContract(address(varg0)));
  if (address(varg0).call(MEM[MEM[0x40] : MEM[0x40] + (v157e + 4 - MEM[0x40])]).gas(msg.gas)) {
    require((RETURNDATASIZE >= 0x20));
    v5820x15d6 = MEM[v5820x15c5];
    require(v5820x15d6);
    v5820x15fb = address(v5820x59e);
    owner_d = (v5820x15fb | (-0x10000000000000000000000000000000000000000 & owner_d));
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function setCOO(address varg0) public {
  require(!msg.value);
  require((msg.sender == address(ceoAddress)));
  v5a30x1625 = address(v5a30x5bf);
  require(v5a30x1625);
  v5a30x164a = address(v5a30x5bf);
  autoBirthFee = (v5a30x164a | (-0x10000000000000000000000000000000000000000 & autoBirthFee));
  exit();
}

function 0x2bbfd941(uint256 varg0, uint256 varg1, uint256 varg2, uint256 varg3) public {
  require(!msg.value);
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  v1672_0 = isOwner(varg0, msg.sender, 0x1673);
  require(v1672_0);
  v1686_0, v1686_1, v1686_2, v1686_3 = isPregnant_impl(varg0, 0x1687, varg3, varg2, varg1);
  require(!v1686_0);
  0x295f(address(owner_d), varg0, 0x16a8);
  v16af = MEM[0x40];
  MEM[v16af] = 0xa91287300000000000000000000000000000000000000000000000000000000;
  MEM[v16af + 4] = varg0;
  MEM[v16af + 36] = v1686_3;
  MEM[v16af + 68] = v1686_2;
  MEM[v16af + 100] = v1686_1;
  MEM[v16af + 132] = msg.sender;
  MEM[v16af + 164] = 0x0;
  require(isContract(address(owner_d)));
  v5c40x12d2 = v5c40x16f4.call(MEM[v5c40x16e9 : v5c40x16e9 + v5c40x1708]).value(v5c40x16df).gas(msg.gas);
  if (v5c40x12d2) {
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function createSaleAuction(uint256 varg0, uint256 varg1, uint256 varg2, uint256 varg3) public {
  require(!msg.value);
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  v1739_0 = isOwner(varg0, msg.sender, 0x173a);
  require(v1739_0);
  v174d_0, v174d_1, v174d_2, v174d_3 = isPregnant_impl(varg0, 0x174e, varg3, varg2, varg1);
  require(!v174d_0);
  0x295f(address(saleAuction), varg0, 0x176f);
  v1776 = MEM[0x40];
  MEM[v1776] = 0xa91287300000000000000000000000000000000000000000000000000000000;
  MEM[v1776 + 4] = varg0;
  MEM[v1776 + 36] = v174d_3;
  MEM[v1776 + 68] = v174d_2;
  MEM[v1776 + 100] = v174d_1;
  MEM[v1776 + 132] = msg.sender;
  MEM[v1776 + 164] = 0x0;
  require(isContract(address(saleAuction)));
  v5e50x12d2 = v5e50x17bb.call(MEM[v5e50x17b0 : v5e50x17b0 + v5e50x17cf]).value(v5e50x17a6).gas(msg.gas);
  if (v5e50x12d2) {
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function unpause() public {
  require(!msg.value);
  require((msg.sender == address(ceoAddress)));
  require((0xff & paused/1461501637330902918203684832716283019655932542976));
  require(address(saleAuction));
  require(address(siringAuction));
  require(address(owner_d));
  require(address(tokenContract));
  require(address(geneScience));
  require((msg.sender == address(ceoAddress)));
  require((0xff & paused/1461501637330902918203684832716283019655932542976));
  paused = (-0xff0000000000000000000000000000000000000001 & paused);
  exit();
}

function sireAllowedToAddress(uint256 varg0) public {
  require(!msg.value);
  v61b0x18a4 = address(sireAllowedToAddress[varg0][0]);
  v61b0x406 = MEM[0x40];
  MEM[v61b0x406] = address(v61b0x18a4);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v61b0x406 - MEM[0x40]))]);
}

function canBreedWith(uint256 varg0, uint256 varg1) public {
  require(!msg.value);
  require((varg0 > 0x0));
  require((varg1 > 0x0));
  require((varg0 < canBreedWith.length));
  require((varg1 < canBreedWith.length));
  v190c_0 = canBreedWith_impl(varg1, (2*varg1 + keccak256(MEM[0x0 : 0x20])), varg0, (2*varg0 + keccak256(MEM[0x0 : 0x20])), 0x190d);
  if (!v190c_0) 0x191e(v190c_0);
  0x2deb(varg0, varg1, 0x191e, (2*varg1 + keccak256(MEM[0x0 : 0x20])));
}

function createSiringAuction(uint256 varg0, uint256 varg1, uint256 varg2, uint256 varg3) public {
  require(!msg.value);
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  v1947_0 = isOwner(varg0, msg.sender, 0x1948);
  require(v1947_0);
  isReadyToBreed_impl(varg0, 0x195c, varg3);
}

function 0x4b136782(uint256 varg0, uint256 varg1, uint256 varg2, uint256 varg3, address varg4) public {
  require(!msg.value);
  require((msg.sender == address(paused)));
  if (!address(varg4)) {
    v1a39_0 = address(autoBirthFee);
  }
  require((0xc350 > promoCreatedCount));
  promoCreatedCount = promoCreatedCount + 1;
  v1a4e_0 = createGen0Auction_impl(v1a39_0, varg3, varg2, varg1, varg0, 0x1a4f, v1a39_0, varg4, varg3, varg2, varg1, varg0);
}

function setAutoBirthFee(uint256 varg0) public {
  require(!msg.value);
  require((msg.sender == address(autoBirthFee)));
  autoBirthFee = varg0;
  exit();
}

function approveSiring(address varg0, uint256 varg1) public {
  require(!msg.value);
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  v1a94_0 = isOwner(varg1, msg.sender, 0x1a95);
  v6b40x1a96 = !v6b40x1a94_0;
  require(v6b40x1a94_0);
  v6b40x1ab0 = sireAllowedToAddress[v6b40x6d3][0];
  v6b40x1ac6 = address(v6b40x6d0);
  sireAllowedToAddress[v6b40x6d3] = (v6b40x1ac6 | (-0x10000000000000000000000000000000000000000 & v6b40x1ab0));
  exit();
}

function tokenContract() public {
  require(!msg.value);
  v6d80x1ada = address(tokenContract);
  v6d80x406 = MEM[0x40];
  MEM[v6d80x406] = address(v6d80x1ada);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v6d80x406 - MEM[0x40]))]);
}

function setSecondsPerBlock(uint256 varg0) public {
  require(!msg.value);
  require((msg.sender == address(ceoAddress)));
  v6ed0x1aff = (v6ed0x700 < uint32(storage_3));
  require(v6ed0x1aff);
  secondsPerBlock = v6ed0x700;
  exit();
}

function paused() public {
  require(!msg.value);
  v7050x1b1a = (0xff & paused/1461501637330902918203684832716283019655932542976);
  v7050x306 = MEM[0x40];
  MEM[v7050x306] = v7050x1b1a;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v7050x306 - MEM[0x40]))]);
}

function 0x5de973a5(uint256 varg0) public {
  require(!msg.value);
  v71a0x1b35 = address(owner_9[varg0][0]);
  v71a0x406 = MEM[0x40];
  MEM[v71a0x406] = address(v71a0x1b35);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v71a0x406 - MEM[0x40]))]);
}

function ownerOf(uint256 varg0) public {
  require(!msg.value);
  if (address(ownerOf[varg0][0])) ownerOf_impl(address(ownerOf[varg0][0]), varg0);
  throw();
}

function GEN0_CREATION_LIMIT() public {
  require(!msg.value);
  v74a0x1b5d = 0xc350;
  v74a0x32f = MEM[0x40];
  MEM[v74a0x32f] = v74a0x1b5d;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v74a0x32f - MEM[0x40]))]);
}

function 0x6e037679(uint256 varg0) public {
  require(!msg.value);
  v75f0x1b7a = address(ownerOf[varg0][0]);
  v75f0x406 = MEM[0x40];
  MEM[v75f0x406] = address(v75f0x1b7a);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v75f0x406 - MEM[0x40]))]);
}

function setSaleAuctionAddress(address varg0) public {
  require(!msg.value);
  require((msg.sender == address(ceoAddress)));
  v1baa = MEM[0x40];
  MEM[v1baa] = 0x85b8618800000000000000000000000000000000000000000000000000000000;
  require(isContract(address(varg0)));
  if (address(varg0).call(MEM[MEM[0x40] : MEM[0x40] + (v1baa + 4 - MEM[0x40])]).gas(msg.gas)) {
    require((RETURNDATASIZE >= 0x20));
    v7770x1c02 = MEM[v7770x1bf1];
    require(v7770x1c02);
    v7770x1c27 = address(v7770x793);
    saleAuction = (v7770x1c27 | (-0x10000000000000000000000000000000000000000 & saleAuction));
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function balanceOf(address varg0) public {
  require(!msg.value);
  v7b8_0 = balanceOf_impl(varg0, 0x32b);
  v7980x32f = MEM[0x40];
  MEM[v7980x32f] = v7980x7b8_0;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v7980x32f - MEM[0x40]))]);
}

function 0x79a9232f(uint256 varg0, uint256 varg1) public {
  require(!msg.value);
  0x298d(varg1, varg0, 0x1c57, 0x0, varg1, varg0);
}

function secondsPerBlock() public {
  require(!msg.value);
  v7d40x1c61 = secondsPerBlock;
  v7d40x32f = MEM[0x40];
  MEM[v7d40x32f] = v7d40x1c61;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v7d40x32f - MEM[0x40]))]);
}

function pause() public {
  require(!msg.value);
  require((msg.sender == address(ceoAddress)));
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  paused = (0x10000000000000000000000000000000000000000 | (-0xff0000000000000000000000000000000000000001 & paused));
  exit();
}

function tokensOfOwner(address varg0) public {
  require(!msg.value);
  v1ccb_0 = balanceOf_impl(varg0, 0x1ccc);
  if (v1ccb_0) {
    v1cef = MEM[0x40];
    MEM[v1cef] = v1ccb_0;
    MEM[0x40] = 32*v1ccb_0 + v1cef + 32;
    if (v1ccb_0) {
      CODECOPY(v1cef + 32, CODESIZE, 32*v1ccb_0);
    }
    v1d1f_0 = totalSupply_impl(0x1d20);
    v1d55_1 = 0x0;
    v1d33_0 = 0x1;
    while (true) {
      if ((v1d33_0 > v1d1f_0)) break;
      if ((address(ownerOf[v1d33_0][0]) == address(varg0))) {
        require((v1d55_1 < MEM[v1cef]));
        MEM[v1cef + 32*v1d55_1 + 32] = v1d33_0;
        v1d55_1 = v1d55_1 + 1;
      }
      v1d33_0 = v1d33_0 + 1;
      continue;
    }
  } else {
    v7fe0x1cef = MEM[0x40];
    MEM[v7fe0x1cef] = 0x0;
    MEM[0x40] = v7fe0x1cef + 32;
  }
  v7fe0x823 = MEM[0x40];
  MEM[v7fe0x823] = 0x20;
  MEM[v7fe0x823 + 32] = MEM[v7fe0x1cef];
  v84c0x7fe_0 = 0x0;
  while (true) {
    if ((v84c0x7fe_0 >= (MEM[v7fe0x1cef] * 0x20))) break;
    MEM[v7fe0x823 + v84c0x7fe_0 + 64] = MEM[v7fe0x1cef + v84c0x7fe_0 + 32];
    v84c0x7fe_0 = v84c0x7fe_0 + 32;
    GOTO 0x843;
  }
  return(MEM[MEM[0x40]:MEM[0x40] + (((MEM[v7fe0x1cef] * 0x20) + v7fe0x823 + 64) - MEM[0x40])]);
}

function giveBirth(uint256 varg0) public {
  require(!msg.value);
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  require((varg0 < canBreedWith.length));
  require(uint64(STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)]));
  v1df1 = MEM[0x40];
  MEM[0x40] = v1df1 + 256;
  MEM[v1df1] = canBreedWith[2*varg0][0];
  MEM[v1df1 + 32] = uint64(STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)]);
  MEM[v1df1 + 64] = uint64((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x10000000000000000));
  MEM[v1df1 + 96] = uint32((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x100000000000000000000000000000000));
  MEM[v1df1 + 128] = uint32((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x10000000000000000000000000000000000000000));
  MEM[v1df1 + 160] = uint32((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x1000000000000000000000000000000000000000000000000));
  MEM[v1df1 + 192] = uint16((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x100000000000000000000000000000000000000000000000000000000));
  MEM[v1df1 + 224] = uint16((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x1000000000000000000000000000000000000000000000000000000000000));
  if ((0x0 == uint32(MEM[v1df1 + 160]))) supportsInterface_impl((0x0 != uint32(MEM[v1df1 + 160])), 0x0, v1df1);
  v3151 = (uint64(MEM[v1df1 + 64]) <= uint64(block.number));
  require(v3151);
  require((uint32((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x1000000000000000000000000000000000000000000000000)) < canBreedWith.length));
  v1fbe_5 = uint16((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x1000000000000000000000000000000000000000000000000000000000000));
  if ((v1fbe_5 < uint16((STORAGE[((keccak256(MEM[0x0 : 0x20]) + (uint32((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x1000000000000000000000000000000000000000000000000)) * 0x2)) + 0x1)] / 0x1000000000000000000000000000000000000000000000000000000000000)))) {
    v1fbe_5 = uint16((STORAGE[((keccak256(MEM[0x0 : 0x20]) + (uint32((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x1000000000000000000000000000000000000000000000000)) * 0x2)) + 0x1)] / 0x1000000000000000000000000000000000000000000000000000000000000));
  }
  v1f0a = MEM[0x40];
  MEM[v1f0a] = 0xd9f5aed00000000000000000000000000000000000000000000000000000000;
  MEM[v1f0a + 4] = canBreedWith[2*varg0][0];
  MEM[v1f0a + 36] = canBreedWith[(uint32((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x1000000000000000000000000000000000000000000000000)) * 0x2)][0];
  MEM[v1f0a + 68] = uint64((uint64((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x10000000000000000)) + -0x1));
  require(isContract(address(geneScience)));
  if (address(geneScience).call(MEM[MEM[0x40] : MEM[0x40] + ((v1f0a - MEM[0x40]) + 0x64)]).gas(msg.gas)) {
    require((RETURNDATASIZE >= 0x20));
    v2006_0 = createGen0Auction_impl(address(ownerOf[varg0][0]), MEM[MEM[0x40]], uint16(v1fbe_5 + 1), uint32((STORAGE[(0x1 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))] / 0x1000000000000000000000000000000000000000000000000)), varg0, 0x2007, 0x0, address(ownerOf[varg0][0]), MEM[MEM[0x40]], v1fbe_5, (keccak256(MEM[0x0 : 0x20]) + (uint32((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x1000000000000000000000000000000000000000000000000)) * 0x2)), uint32((STORAGE[((2*varg0 + keccak256(MEM[0x0 : 0x20])) + 0x1)] / 0x1000000000000000000000000000000000000000000000000)), (2*varg0 + keccak256(MEM[0x0 : 0x20])), 0x0);
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function 0x92f64cce(uint256 varg0, uint256 varg1, uint256 varg2) public {
  require(!msg.value);
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  require((varg2 >= autoBirthFee));
  v207b_0 = isOwner(varg0, msg.sender, 0x207c);
  require(v207b_0);
  0x2deb(varg0, varg1, 0x2091, 0x0);
}

function symbol() public {
  require(!msg.value);
  v8a50x225b = MEM[0x40];
  MEM[0x40] = v8a50x225b + 64;
  MEM[v8a50x225b] = 0x2;
  MEM[v8a50x225b + 32] = 0x4346000000000000000000000000000000000000000000000000000000000000;
  v8a50x356 = MEM[0x40];
  MEM[v8a50x356] = 0x20;
  MEM[v8a50x356 + 32] = MEM[v8a50x225b];
  v37d0x8a5_0 = 0x0;
  while (true) {
    if ((v37d0x8a5_0 >= MEM[v8a50x225b])) break;
    MEM[v37d0x8a5_0 + v8a50x356 + 64] = MEM[v37d0x8a5_0 + v8a50x225b + 32];
    v37d0x8a5_0 = v37d0x8a5_0 + 32;
    GOTO 0x374;
  }
  v3b90x8a5_1 = (MEM[v8a50x225b] + v8a50x356 + 64);
  if ((0x1f & MEM[v8a50x225b])) {
    v8a50x3a2 = (v3b90x8a5_1 - (0x1f & MEM[v8a50x225b]));
    MEM[v8a50x3a2] = (~((0x100 ** (0x20 - (0x1f & MEM[v8a50x225b]))) - 0x1) & MEM[v8a50x3a2]);
    v3b90x8a5_1 = v8a50x3a2 + 32;
  }
  return(MEM[MEM[0x40]:MEM[0x40] + (v3b90x8a5_1 - MEM[0x40])]);
}

function cooldowns(uint256 varg0) public {
  require(!msg.value);
  require((varg0 < 0xe));
  v8ba0x22b8 = uint32((STORAGE[varg0 + 3] / (0x100 ** (0x4 * (varg0 % 0x8)))));
  v8ba0x8d6 = MEM[0x40];
  MEM[v8ba0x8d6] = uint32(v8ba0x22b8);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v8ba0x8d6 - MEM[0x40]))]);
}

function 0xa1045d73() public {
  require(!msg.value);
  v8eb0x22c7 = address(paused);
  v8eb0x406 = MEM[0x40];
  MEM[v8eb0x406] = address(v8eb0x22c7);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v8eb0x406 - MEM[0x40]))]);
}

/*function many_msg_babbage(address varg0, uint256 varg1) public {*/
/// very likely ERC function transfer
function transfer(address varg0, uint256 varg1) public {
  require(!msg.value);
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  require(address(varg0));
  require((this != address(varg0)));
  require((address(saleAuction) != address(varg0)));
  require((address(siringAuction) != address(varg0)));
  require((address(owner_d) != address(varg0)));
  v2366_0 = isOwner(varg1, msg.sender, 0x2367);
  require(v2366_0);
  0x2b3a(varg1, varg0, msg.sender, 0x237d, varg1, varg0);
}

function transferTokenFrom(address varg0, address varg1, uint256 varg2) public {
  require(!msg.value);
  v94d_0 = transferTokenFrom_impl(varg2, varg1, varg0, 0x3eb);
  exit();
}

function cooAddress() public {
  require(!msg.value);
  v94e0x24fa = address(autoBirthFee);
  v94e0x406 = MEM[0x40];
  MEM[v94e0x406] = address(v94e0x24fa);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v94e0x406 - MEM[0x40]))]);
}

function autoBirthFee() public {
  require(!msg.value);
  v9630x2500 = autoBirthFee;
  v9630x32f = MEM[0x40];
  MEM[v9630x32f] = v9630x2500;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v9630x32f - MEM[0x40]))]);
}

function 0xb9b8ea8e() public {
  require(!msg.value);
  v9780x2506 = storage_11;
  v9780x32f = MEM[0x40];
  MEM[v9780x32f] = v9780x2506;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v9780x32f - MEM[0x40]))]);
}

function createGen0Auction(uint256 varg0) public {
  require(!msg.value);
  require((msg.sender == address(autoBirthFee)));
  require((0xc350 > gen0CreatedCount));
  v2541_0 = createGen0Auction_impl(this, varg0, 0x0, 0x0, 0x0, 0x2542, 0x0, varg0);
  0x295f(address(saleAuction), v2541_0, 0x255c);
  v2563 = MEM[0x40];
  MEM[v2563] = 0xa91287300000000000000000000000000000000000000000000000000000000;
  MEM[v2563 + 4] = v2541_0;
  MEM[v2563 + 36] = 0x1f4;
  MEM[v2563 + 68] = 0x1f4;
  MEM[v2563 + 100] = 0xd2f00;
  MEM[v2563 + 132] = this;
  MEM[v2563 + 164] = 0x0;
  require(isContract(address(saleAuction)));
  v98d0x25d3 = v98d0x25ab.call(MEM[v98d0x25a0 : v98d0x25a0 + v98d0x25bf]).value(v98d0x2596).gas(msg.gas);
  if (v98d0x25d3) {
    gen0CreatedCount = gen0CreatedCount + 1;
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function 0xc754a0a3(uint256 varg0) public {
  require(!msg.value);
  require((varg0 < canBreedWith.length));
  v9a50x2644 = (0x0 != uint32((STORAGE[(0x1 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))] / 0x1000000000000000000000000000000000000000000000000)));
  v9a50x266c = (uint64((STORAGE[(0x1 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))] / 0x10000000000000000)) <= block.number);
  v9a50x2685 = uint16((STORAGE[(0x1 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))] / 0x100000000000000000000000000000000000000000000000000000000));
  v9a50x26aa = uint64((STORAGE[(0x1 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))] / 0x10000000000000000));
  v9a50x26c7 = uint32((STORAGE[(0x1 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))] / 0x1000000000000000000000000000000000000000000000000));
  v9a50x26ec = uint64((STORAGE[(0x1 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))] / 0x1));
  v9a50x2709 = uint32((STORAGE[(0x1 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))] / 0x100000000000000000000000000000000));
  v9a50x2726 = uint32((STORAGE[(0x1 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))] / 0x10000000000000000000000000000000000000000));
  v9a50x273f = uint16((STORAGE[(0x1 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))] / 0x1000000000000000000000000000000000000000000000000000000000000));
  v9a50x2746 = STORAGE[(0x0 + (2*varg0 + keccak256(MEM[0x0 : 0x20])))];
  v9a50x9c1 = MEM[0x40];
  MEM[v9a50x9c1] = v9a50x2644;
  MEM[v9a50x9c1 + 32] = v9a50x266c;
  MEM[v9a50x9c1 + 64] = v9a50x2685;
  MEM[v9a50x9c1 + 96] = v9a50x26aa;
  MEM[v9a50x9c1 + 128] = v9a50x26c7;
  MEM[v9a50x9c1 + 160] = v9a50x26ec;
  MEM[v9a50x9c1 + 192] = v9a50x2709;
  MEM[v9a50x9c1 + 224] = v9a50x2726;
  MEM[v9a50x9c1 + 256] = v9a50x273f;
  MEM[v9a50x9c1 + 288] = v9a50x2746;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x140 + (v9a50x9c1 - MEM[0x40]))]);
}

function isReadyToBreed(uint256 varg0) public {
  require(!msg.value);
  isReadyToBreed_impl(varg0, 0x302);
}

function tokenBalanceOf(address varg0) public {
  require(!msg.value);
  va270x282d = tokenBalanceOf[varg0][0];
  va270x32f = MEM[0x40];
  MEM[va270x32f] = va270x282d;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (va270x32f - MEM[0x40]))]);
}

function saleAuction() public {
  require(!msg.value);
  va480x283c = address(saleAuction);
  va480x406 = MEM[0x40];
  MEM[va480x406] = address(va480x283c);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (va480x406 - MEM[0x40]))]);
}

function 0xe86d5083() public {
  require(!msg.value);
  va5d0x284b = address(owner_d);
  va5d0x406 = MEM[0x40];
  MEM[va5d0x406] = address(va5d0x284b);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (va5d0x406 - MEM[0x40]))]);
}

function 0xef299b0b(uint256 varg0) public {
  require(!msg.value);
  v284f = msg.sender;
  require(((tokenBalanceOf[v284f][0] + varg0) > tokenBalanceOf[v284f][0]));
  v2872 = MEM[0x40];
  MEM[v2872] = 0x23b872dd00000000000000000000000000000000000000000000000000000000;
  MEM[v2872 + 4] = msg.sender;
  MEM[v2872 + 36] = this;
  MEM[v2872 + 68] = varg0;
  require(isContract(address(tokenContract)));
  if (address(tokenContract).call(MEM[MEM[0x40] : MEM[0x40] + ((v2872 - MEM[0x40]) + 0x64)]).gas(msg.gas)) {
    require((RETURNDATASIZE >= 0x20));
    va720x290a = MEM[va720x28f9];
    require(va720x290a);
    va720x2913 = msg.sender;
    va720x2926 = (va720xa85 + tokenBalanceOf[va720x2913][0]);
    tokenBalanceOf[va720x2913] = va720x2926;
    exit();
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function gen0CreatedCount() public {
  require(!msg.value);
  va8a0x292d = gen0CreatedCount;
  va8a0x32f = MEM[0x40];
  MEM[va8a0x32f] = va8a0x292d;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (va8a0x32f - MEM[0x40]))]);
}

function geneScience() public {
  require(!msg.value);
  va9f0x293c = address(geneScience);
  va9f0x406 = MEM[0x40];
  MEM[va9f0x406] = address(va9f0x293c);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (va9f0x406 - MEM[0x40]))]);
}

function supportsInterface_impl(uint256 vg0, uint256 vg2, uint256 vg2) private {
  return(vg0) // to vg2;
}

function ownerOf_impl(uint256 vg0, uint256 vg2, uint256 vg2) private {
  return(vg0) // to vg2;
}

function 0xe67(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2) private {
  if (vg0) GOTO 0xe72;
  require(vg0);
  throw();
  throw();
  ve79 = MEM[0x40];
  MEM[ve79] = 0xc55d0f5600000000000000000000000000000000000000000000000000000000;
  if (isContract(address(siringAuction))) GOTO 0xed9;
  if (!isContract(address(siringAuction))) {
  }
  throw();
  if (address(siringAuction).call(MEM[MEM[0x40] : MEM[0x40] + ((ve79 - MEM[0x40]) + 0x24)]).gas(msg.gas)) GOTO 0xeed;
  if (!address(siringAuction).call(MEM[MEM[0x40] : MEM[0x40] + ((ve79 - MEM[0x40]) + 0x24)]).gas(msg.gas)) {
  }
  RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
  throw();
  require((RETURNDATASIZE >= 0x20));
  throw();
  require((MEM[MEM[0x40]] < (MEM[MEM[0x40]] + autoBirthFee)));
  throw();
  require((vg2 >= (MEM[MEM[0x40]] + autoBirthFee)));
  throw();
  vf33 = MEM[0x40];
  MEM[vf33] = 0x598647f800000000000000000000000000000000000000000000000000000000;
  MEM[vf33 + 36] = -autoBirthFee + vg2;
  require(isContract(address(siringAuction)));
  throw();
  if (address(siringAuction).call(MEM[MEM[0x40] : MEM[0x40] + ((vf33 - MEM[0x40]) + 0x44)]).gas(msg.gas)) {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
    vfbd_0 = transferTokenFrom_impl(autoBirthFee, this, msg.sender, 0xfbe);
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
  0x29dc(uint32(vg2));
}

function 0xfbe(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2) private {
  0x29dc(uint32(vg2));
}

function 0xfd4(uint256 vg0, uint256 vg2, uint256 vg2, uint256 vg2) private {
  require(vg0);
  throw();
  0x29dc(uint32(vg2));
  0xe67();
  vfd40x306 = MEM[0x40];
  MEM[vfd40x306] = vfd40x2e36;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (vfd40x306 - MEM[0x40]))]);
  vfd40x32f = MEM[0x40];
  MEM[vfd40x32f] = vfd40x2e36;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (vfd40x32f - MEM[0x40]))]);
  exit();
  while (true) {
    0xe67(vg0);
  }
  require(vg0);
  throw();
  0x298d(v?, v?, 0xe67);
  require(vg0);
  throw();
  0x295f(address(siringAuction), v?, 0x197e);
  v1985 = MEM[0x40];
  MEM[v1985] = 0xa91287300000000000000000000000000000000000000000000000000000000;
  MEM[v1985 + 132] = msg.sender;
  MEM[v1985 + 164] = 0x0;
  require(isContract(address(siringAuction)));
  if (!v1c570x12d2) {
  }
  if (!v191e0x12d2) {
  }
  vfd40x12d2 = vfd40x19ca.call(MEM[vfd40x19bf : vfd40x19bf + vfd40x19de]).value(vfd40x19b5).gas(msg.gas);
  if (vfd40x12d2) {
    GOTO ;
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
  if (!v2deb0x12d2) {
  }
  throw();
  0x29dc(vg2);
}

