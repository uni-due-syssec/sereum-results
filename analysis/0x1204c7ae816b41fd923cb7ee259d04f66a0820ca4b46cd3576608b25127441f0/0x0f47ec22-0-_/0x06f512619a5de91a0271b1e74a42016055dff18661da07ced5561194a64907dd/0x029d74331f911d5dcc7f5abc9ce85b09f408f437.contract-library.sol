// Decompiled at www.contract-library.com

// Data structures and variables inferred from the use of storage instructions
uint256 paused; // 0x0
uint256 nonFungibleContract; // 0x1
uint256 ownerCut; // 0x2
uint256 storage_3; // 0x3
mapping (uint256 => [uint256]) cancelAuction;
uint256 isSiringClockAuction; // 0x5

// Note: The function selector is not present in the original solidity code.
// However, we display it for the sake of completeness.
function __function_selector__(uint32 function_selector) public {
  MEM[0x40] = 0x80;
  if ((msg.data.length() >= 0x4)) {
    if ((function_selector == 0xa912873)) 0x0a912873();
    if ((0x3f4ba83a == function_selector)) unpause()(function_selector);
    if ((0x598647f8 == function_selector)) bid(uint256,uint256)(function_selector);
    if ((0x5c975abb == function_selector)) paused()(function_selector);
    if ((0x76190f8f == function_selector)) isSiringClockAuction()(function_selector);
    if ((0x78bd7935 == function_selector)) getAuction(uint256)(function_selector);
    if ((0x83b5ff8b == function_selector)) ownerCut()(function_selector);
    if ((0x8456cb59 == function_selector)) pause()(function_selector);
    if ((0x878eb368 == function_selector)) cancelAuctionWhenPaused(uint256)(function_selector);
    if ((0x8da5cb5b == function_selector)) owner()(function_selector);
    if ((0x96b5a755 == function_selector)) cancelAuction(uint256)(function_selector);
    if ((0xc55d0f56 == function_selector)) getCurrentPrice(uint256)(function_selector);
    if ((0xd4e119cf == function_selector)) 0xd4e119cf(function_selector);
    if ((0xdd1b7a0f == function_selector)) nonFungibleContract()(function_selector);
  }
  throw();
}

function unpause() public {
  require(!msg.value);
  require((msg.sender == address(paused)));
  require((0xff & paused/1461501637330902918203684832716283019655932542976));
  paused = (-0xff0000000000000000000000000000000000000001 & paused);
  v1080x3d9 = 0x1;
  v1080x121 = MEM[0x40];
  MEM[v1080x121] = v1080x3d9;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v1080x121 - MEM[0x40]))]);
}

function bid(uint256 varg0, uint256 varg1) public {
  require(!msg.value);
  require((msg.sender == address(nonFungibleContract)));
  v8af_0 = getCurrentPrice_impl(keccak256(MEM[0x0 : 0x40]), 0x8b0);
  require(v8af_0);
  0xbb1(keccak256(MEM[0x0 : 0x40]), 0x8c4, 0x0, 0x0);
}

function paused() public {
  require(!msg.value);
  v14c0x439 = (0xff & paused/1461501637330902918203684832716283019655932542976);
  v14c0x121 = MEM[0x40];
  MEM[v14c0x121] = v14c0x439;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v14c0x121 - MEM[0x40]))]);
}

function isSiringClockAuction() public {
  require(!msg.value);
  v1610x442 = (0xff & isSiringClockAuction);
  v1610x121 = MEM[0x40];
  MEM[v1610x121] = v1610x442;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v1610x121 - MEM[0x40]))]);
}

function getAuction(uint256 varg0) public {
  require(!msg.value);
  v465_0 = getCurrentPrice_impl(keccak256(MEM[0x0 : 0x40]), 0x466);
  v1760x467 = !v1760x465_0;
  require(v1760x465_0);
  v1760x473 = STORAGE[v1760x453];
  v1760x477 = v1760x453 + 1;
  v1760x47d = v1760x453 + 2;
  v1760x489 = address(v1760x473);
  v1760x495 = uint128(STORAGE[v1760x477]);
  v1760x4ae = uint128((STORAGE[v1760x477] / 0x100000000000000000000000000000000));
  v1760x4bc = uint64(STORAGE[v1760x47d]);
  v1760x4cb = uint64((STORAGE[v1760x47d] / 0x10000000000000000));
  v1760x4d3 = (0xff & (STORAGE[v1760x47d] / 0x100000000000000000000000000000000));
  v1760x192 = MEM[0x40];
  MEM[v1760x192] = address(v1760x489);
  MEM[v1760x192 + 32] = v1760x495;
  MEM[v1760x192 + 64] = v1760x4ae;
  MEM[v1760x192 + 96] = v1760x4bc;
  MEM[v1760x192 + 128] = v1760x4cb;
  MEM[v1760x192 + 160] = v1760x4d3;
  return(MEM[MEM[0x40]:MEM[0x40] + (0xc0 + (v1760x192 - MEM[0x40]))]);
}

function ownerCut() public {
  require(!msg.value);
  v1cd0x4dd = ownerCut;
  v1cd0x1e6 = MEM[0x40];
  MEM[v1cd0x1e6] = v1cd0x4dd;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v1cd0x1e6 - MEM[0x40]))]);
}

function pause() public {
  require(!msg.value);
  require((msg.sender == address(paused)));
  require(!(0xff & paused/1461501637330902918203684832716283019655932542976));
  paused = (0x10000000000000000000000000000000000000000 | (-0xff0000000000000000000000000000000000000001 & paused));
  v1f40x535 = 0x1;
  v1f40x121 = MEM[0x40];
  MEM[v1f40x121] = v1f40x535;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v1f40x121 - MEM[0x40]))]);
}

function cancelAuctionWhenPaused(uint256 varg0) public {
  require(!msg.value);
  require((0xff & paused/1461501637330902918203684832716283019655932542976));
  require((msg.sender == address(paused)));
  v580_0 = getCurrentPrice_impl(keccak256(MEM[0x0 : 0x40]), 0x581);
  require(v580_0);
  0xb34(address(cancelAuction[varg0][0]), varg0, 0x5a2);
}

function owner() public {
  require(!msg.value);
  v2210x5b2 = address(paused);
  v2210x23a = MEM[0x40];
  MEM[v2210x23a] = address(v2210x5b2);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v2210x23a - MEM[0x40]))]);
}

function cancelAuction(uint256 varg0) public {
  require(!msg.value);
  v5cc_0 = getCurrentPrice_impl(keccak256(MEM[0x0 : 0x40]), 0x5cd);
  require(v5cc_0);
  require((address(cancelAuction[varg0][0]) == msg.sender));
  0xb34(address(cancelAuction[varg0][0]), varg0, 0x427);
}

function getCurrentPrice(uint256 varg0) public {
  require(!msg.value);
  v610_0 = getCurrentPrice_impl(keccak256(MEM[0x0 : 0x40]), 0x611);
  require(v610_0);
  0xbb1(keccak256(MEM[0x0 : 0x40]), 0x625, keccak256(MEM[0x0 : 0x40]));
}

function 0xd4e119cf() public {
  require(!msg.value);
  v2820x62f = storage_3;
  v2820x1e6 = MEM[0x40];
  MEM[v2820x1e6] = v2820x62f;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v2820x1e6 - MEM[0x40]))]);
}

function nonFungibleContract() public {
  require(!msg.value);
  v2970x63e = address(nonFungibleContract);
  v2970x23a = MEM[0x40];
  MEM[v2970x23a] = address(v2970x63e);
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (v2970x23a - MEM[0x40]))]);
}

function 0x6b5(uint256 vg0, uint256 vg1, uint256 vg2, uint256 vg3, uint256 vg4, uint256 vg5, uint256 vg6, uint256 vg7, uint256 vg8, uint256 vg9) private {
  v6b8 = vg1.call(MEM[vg3 : vg3 + vg4]).value(vg2).gas(msg.gas);
  if (v6b8) {
    GOTO ;
    v31a = MEM[0x40];
    MEM[0x40] = v31a + 192;
    MEM[v31a] = 0xffffffffffffffffffffffffffffffffffffffff;
    v330 = v31a + 32;
    MEM[v330] = 0xffffffffffffffffffffffffffffffff;
    v33f = v330 + 32;
    MEM[v33f] = 0xffffffffffffffffffffffffffffffff;
    v34e = v33f + 32;
    MEM[v34e] = 0xffffffffffffffff;
    v35e = v34e + 32;
    MEM[v35e] = uint64(now);
    MEM[v35e + 32] = ;
    require((uint64(MEM[v31a + 96]) >= 0x3c));
    require((uint128(MEM[v31a + 64]) >= storage_3));
    v6b50x70f = v6b50x31a + 64;
    v6b50x71d = v6b50x31a + 32;
    require((uint128(MEM[v6b50x71d]) >= uint128(MEM[v6b50x70f])));
    MEM[0x20] = 0x4;
    v6b50x746 = keccak256(MEM[0x0 : 0x40]);
    v6b50x748 = MEM[v6b50x31a];
    v6b50x755 = address(v6b50x748);
    STORAGE[v6b50x746] = (v6b50x755 | (STORAGE[v6b50x746] & -0x10000000000000000000000000000000000000000));
    v6b50x775 = v6b50x31a + 32;
    v6b50x77a = v6b50x746 + 1;
    v6b50x77f = v6b50x31a + 64;
    v6b50x78b = uint128(MEM[v6b50x77f]);
    v6b50x7a3 = uint128(MEM[v6b50x775]);
    STORAGE[v6b50x77a] = (uint128((v6b50x7a3 | (STORAGE[v6b50x77a] & -0x100000000000000000000000000000000))) | 340282366920938463463374607431768211456*v6b50x78b);
    v6b50x7c9 = v6b50x31a + 96;
    v6b50x7cf = v6b50x746 + 2;
    v6b50x7d6 = v6b50x31a + 128;
    v6b50x7dc = v6b50x31a + 160;
    v6b50x7df = MEM[v6b50x7dc];
    v6b50x822 = uint64(MEM[v6b50x7c9]);
    STORAGE[v6b50x7cf] = (((((v6b50x822 | (STORAGE[v6b50x7cf] & -0x10000000000000000)) & -0xffffffffffffffff0000000000000001) | (0x10000000000000000 * uint64(MEM[v6b50x7d6]))) & -0xff00000000000000000000000000000001) | 340282366920938463463374607431768211456*v6b50x7df);
    v6b50x846 = MEM[0x40];
    MEM[v6b50x846 + 32] = v6b50x7a3;
    MEM[v6b50x846 + 64] = v6b50x78b;
    MEM[v6b50x846 + 96] = v6b50x822;
    MEM[v6b50x846 + 128] = v6b50x755;
    MEM[v6b50x846 + 160] = v6b50x7df;
    log(MEM[0x40], (0xc0 + (v6b50x846 - MEM[0x40])), 0x47c084ad6c4ba8273c62a3a8f81410f52cd39c9edef32e99b0d20520b9dc401d);
    GOTO ;
    exit();
    v6b50xb74 = MEM[0x40];
    MEM[v6b50xb74 + 32] = ;
    log(MEM[0x40], (0x40 + (v6b50xb74 - MEM[0x40])), 0x9b78714c624a264673f0e2244bc8a1121ed50c982ffd7c7d5a65286701e7c009);
    GOTO ;
    GOTO ;
  } else {
    RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
    throw();
  }
}

function 0xaa5() private {
  vaac = MEM[0x40];
  MEM[vaac] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000;
  MEM[vaac + 4] = 0xffffffffffffffffffffffffffffffffffffffff;
  if (isContract(address(nonFungibleContract))) 0x6b5(!isContract(address(nonFungibleContract)), address(nonFungibleContract), 0x0, MEM[0x40], ((vaac - MEM[0x40]) + 0x44), MEM[0x40], 0x0, vaac + 68, 0xa9059cbb, address(nonFungibleContract));
  throw();
}

function getCurrentPrice_impl(uint256 vg0, uint256 vg1) private {
  vb16 = vg0 + 2;
  return((uint64((STORAGE[vb16] / 0x10000000000000000)) > 0x0)) // to vg1;
}

function 0xb34(uint256 vg0, uint256 vg1, uint256 vg2) private {
  vb46 = cancelAuction[vg1][0x2];
  0xc38(vg1, 0xb66);
  0xaa5();
}

function 0xbb1(uint256 vg0, uint256 vg1, uint256 vg2, uint256 vg3) private {
  vbb5 = vg0 + 2;
  vca5_4 = 0x0;
  if ((now > uint64((STORAGE[vbb5] / 0x10000000000000000)))) {
    vbdd = vg0 + 2;
    vca5_4 = (now - uint64((STORAGE[vbdd] / 0x10000000000000000)));
  }
  vbfb = vg0 + 1;
  vc00 = vg0 + 2;
  vc86_0 = uint128((STORAGE[vbfb] / 0x100000000000000000000000000000000));
  if ((vca5_4 < uint64(STORAGE[vc00]))) {
    require(uint64(STORAGE[vc00]));
    vc86_0 = (uint128(STORAGE[vbfb]) + (((vc86_0 - uint128(STORAGE[vbfb])) * vca5_4) / uint64(STORAGE[vc00])));
  }
  while (true) {
    GOTO vg1;
  }
  vbb10x1e6 = MEM[0x40];
  MEM[vbb10x1e6] = vbb10xc27;
  return(MEM[MEM[0x40]:MEM[0x40] + (0x20 + (vbb10x1e6 - MEM[0x40]))]);
  v8c9 = (v? < vc86_0);
  require((v? >= vc86_0));
  v8e7 = uint16(v?);
  if ((v8e7 != 0x3)) {
    0xc38(v?, 0x8f5);
  }
  if ((vc86_0 > 0x0)) {
    v902 = (v? + 0x2);
    if ((0x1 != (0xff & (STORAGE[v902] / 0x100000000000000000000000000000000)))) {
      vc8e = ownerCut*vc86_0/100;
      v939 = MEM[0x40];
      MEM[v939] = 0xad22119500000000000000000000000000000000000000000000000000000000;
      MEM[v939 + 4] = msg.sender;
      MEM[v939 + 36] = address(STORAGE[]);
      MEM[v939 + 68] = vc86_0 - vc8e;
      require(isContract(address(nonFungibleContract)));
      if (address(nonFungibleContract).call(MEM[MEM[0x40] : MEM[0x40] + ((v939 - MEM[0x40]) + 0x64)]).gas(msg.gas)) {
        v9cb = MEM[0x40];
        MEM[v9cb] = 0xad22119500000000000000000000000000000000000000000000000000000000;
        MEM[v9cb + 4] = msg.sender;
        v9ff = address(nonFungibleContract);
        MEM[v9cb + 36] = v9ff;
        MEM[v9cb + 68] = vc8e;
        require(isContract(v9ff));
        if (!v9ff.call(MEM[MEM[0x40] : MEM[0x40] + ((v9cb - MEM[0x40]) + 0x64)]).gas(msg.gas)) {
          RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
          throw();
        }
      } else {
        RETURNDATACOPY(0x0, 0x0, RETURNDATASIZE);
        throw();
      }
    } else {
      GOTO 0xa52;
    }
  }
  va56 = MEM[0x40];
  MEM[va56 + 32] = vc86_0;
  MEM[va56 + 64] = msg.sender;
  MEM[va56 + 96] = 0x0;
  log(MEM[0x40], (0x80 + (va56 - MEM[0x40])), 0x2446614a82134413a15e9542b6f529ea9425ee7fda9d1b894dfd29cc7a20bcf1);
  0xaa5();
}

function 0xc38(uint256 vg0, uint256 vg1) private {
  vc48 = cancelAuction[vg0][0];
  cancelAuction[vg0] = (-0x10000000000000000000000000000000000000000 & vc48);
  cancelAuction[vg0][0x1] = 0x0;
  vc6e = cancelAuction[vg0][0x2];
  cancelAuction[vg0][0x2] = (-0x10000000000000000000000000000000000 & vc6e);
  return() // to vg1;
}

function 0x0a912873(uint256 varg0, uint128 varg1, uint128 varg2, uint64 varg3, address varg4, uint256 varg5) public {
  require(!msg.value);
  vcd2 = MEM[0x40];
  MEM[0x40] = vcd2 + 192;
  MEM[vcd2] = 0x0;
  MEM[vcd2 + 32] = 0x0;
  MEM[vcd2 + 64] = 0x0;
  MEM[vcd2 + 96] = 0x0;
  MEM[vcd2 + 128] = 0x0;
  MEM[vcd2 + 160] = 0x0;
  require((varg1 == varg1));
  require((varg2 == varg2));
  require((varg3 == varg3));
  require((msg.sender == address(nonFungibleContract)));
  v648 = MEM[0x40];
  MEM[v648] = 0x23b872dd00000000000000000000000000000000000000000000000000000000;
  MEM[v648 + 4] = address(varg4);
  MEM[v648 + 36] = this;
  MEM[v648 + 68] = varg0;
  if (isContract(address(nonFungibleContract))) 0x6b5(!isContract(address(nonFungibleContract)), address(nonFungibleContract), 0x0, MEM[0x40], ((v648 - MEM[0x40]) + 0x64), MEM[0x40], 0x0, v648 + 100, 0x23b872dd, address(nonFungibleContract));
  throw();
}

