# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x6a801fF842E03cDA992034642df3C242fDA5CC8A 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x27dc297e': '__callback(bytes32 _myid, string _result)', '0x58d33e6d': 'unknown58d33e6d(?)', '0x780b9dca': 'unknown780b9dca(?)', '0xa75c2603': 'unknowna75c2603(?)'} 

# storage definitions
def storage:
    # storage address 5
    unknownbefec197 # mask: a s
    # storage address 6
    unknown434e2897 # mask: a s
    # storage address 7
    unknown326c25ad # mask: a s
    # storage address 8
    MIN_BET # mask: a s
    # storage address 9
    unknown46228a93
    # storage address 10
    ROUND_TIME # mask: a s
    # storage address 11
    unknowndb85e2a0 # mask: a s
    # storage address 12
    unknownea6700e2 # mask: a s
    # storage address 13
    unknownf91ea562 # mask: a s
    # storage address 14
    unknown7142451c # mask: a s
    # storage address 15
    unknown4907a660 # mask: a s
    # storage address 16
    unknown2e4bda25 # mask: a s
    # storage address 17
    unknown307320b5 # mask: a s
    # storage address 18
    unknown0f055139 # mask: a s
    # storage address 18
    stor18 # mask: a s
    # storage address 18
    unknown6d1a4496 # mask: a s
    # storage address 19
    unknownec11c49e # mask: a s
    # storage address 20
    unknown178f9ebd # mask: a s
    # storage address 21
    settingsAddress # mask: a s
    # storage address 24
    lastRound # mask: a s
    # storage address 25
    unknown0aefecb5 # mask: a s
    # storage address 26
    unknown7952ea9d # mask: a s
    # storage address 27
    unknownbd874dff # mask: a s
    # storage address 28
    unknownc4ea0bcd
    # storage address 29
    unknown264be753
    # storage address 30
    rounds
    # storage address 31
    casinoAddress # mask: a s
    # storage address 32
    distributorAddress # mask: a s
# hash = 0x0aefecb5
# getter = ['storage', 256, 0, 25]
# const = None
# payable = False
def unknown0aefecb5(): # not payable
  return unknown0aefecb5


# hash = 0x0f055139
# getter = ['bool', ['storage', 8, 8, 18]]
# const = None
# payable = False
def unknown0f055139(): # not payable
  return bool(unknown0f055139)


# hash = 0x163e7285
# getter = None
# const = None
# payable = False
def unknown163e7285(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown434e2897 = _param1


# hash = 0x164ad4e9
# getter = None
# const = None
# payable = False
def unknown164ad4e9(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown326c25ad = _param1
  log 0xf47b735d: _param1


# hash = 0x178f9ebd
# getter = ['storage', 256, 0, 20]
# const = None
# payable = False
def unknown178f9ebd(): # not payable
  return unknown178f9ebd


# hash = 0x1ce314cd
# getter = None
# const = None
# payable = False
def unknown1ce314cd(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown46228a93[2] = _param1
  unknown4907a660 = _param1
  log 0xfec588ee: 2, _param1


# hash = 0x1f8be1cb
# getter = None
# const = None
# payable = False
def unknown1f8be1cb(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknownea6700e2 = _param1


# hash = 0x264be753
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 29]]]
# const = None
# payable = False
def unknown264be753(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown264be753[addr(_param1)].field_0


# hash = 0x2a3ec233
# getter = None
# const = None
# payable = False
def unknown2a3ec233(bool _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  stor18 = Mask(248, 0, _param1)
  log 0x77db83c1: not _param1


# hash = 0x2e4bda25
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknown2e4bda25(): # not payable
  return unknown2e4bda25


# hash = 0x2f4ae2d6
# getter = None
# const = None
# payable = False
def unknown2f4ae2d6(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknownbefec197 = _param1


# hash = 0x307320b5
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknown307320b5(): # not payable
  return unknown307320b5


# hash = 0x326c25ad
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def unknown326c25ad(): # not payable
  return unknown326c25ad


# hash = 0x38bbfa50
# getter = None
# const = None
# payable = False
def __callback(bytes32 _myid, string _result, bytes _proof): # not payable
  require calldata.size - 4 >= 96
  require _result <= 4294967296
  require _result + 36 <= calldata.size
  require _result.length <= 4294967296 and _result + _result.length + 36 <= calldata.size
  require _proof <= 4294967296
  require _proof + 36 <= calldata.size
  require _proof.length <= 4294967296 and _proof + _proof.length + 36 <= calldata.size


# hash = 0x434e2897
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknown434e2897(): # not payable
  return unknown434e2897


# hash = 0x440277e8
# getter = None
# const = None
# payable = False
def unknown440277e8(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(casinoAddress)
  static call casinoAddress.0x440277e8 with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x46228a93
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = False
def unknown46228a93(uint8 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown46228a93[_param1]


# hash = 0x4907a660
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknown4907a660(): # not payable
  return unknown4907a660


# hash = 0x4a39ec90
# getter = ['struct', ['loc', 29]]
# const = None
# payable = False
def bets(address _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < unknown264be753[_param1].field_0
  require uint8(unknown264be753[_param1][_param2].field_0) <= 5
  return uint8(unknown264be753[_param1][_param2].field_0), 
         uint128(unknown264be753[_param1][_param2].field_0),
         uint64(unknown264be753[_param1][_param2].field_0),
         bool(uint8(unknown264be753[_param1][_param2].field_200)),
         bool(uint8(unknown264be753[_param1][_param2].field_208)),
         bool(uint8(unknown264be753[_param1][_param2].field_216))


# hash = 0x63c587ba
# getter = None
# const = None
# payable = False
def unknown63c587ba(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknownf91ea562 = _param1


# hash = 0x6540742f
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def MIN_BET(): # not payable
  return MIN_BET


# hash = 0x67988182
# getter = None
# const = None
# payable = False
def unknown67988182(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require caller == casinoAddress
  require _param2 < unknown264be753[addr(_param1)].field_0
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
  require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
  if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) == 5:
      require ext_code.size(distributorAddress)
      static call distributorAddress.0x65e86f0c with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(distributorAddress)
      call distributorAddress.sendTokens(address to, uint256 amount) with:
           gas gas_remaining wei
          args addr(_param1), ext_call.return_data[0] * unknownf91ea562 / 100
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) != 1:
      require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
      if uint8(unknown264be753[addr(_param1)][_param2].field_0) != 2:
          require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
          if uint8(unknown264be753[addr(_param1)][_param2].field_0) != 3:
              require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
  mem[836 len 0] = None
  mem[900 len 0] = None
  require ext_code.size(distributorAddress)
  static call distributorAddress.0x1cdb3a4e with:
          gas gas_remaining wei
         args addr(this.address), rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_256, addr(_param1), 192, 256, 1, 1, mem[836], 1, mem[900]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      require ext_code.size(distributorAddress)
      call distributorAddress.0x289ef3 with:
           gas gas_remaining wei
          args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  require _param2 < unknown264be753[addr(_param1)].field_0
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) == 1:
      require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) <= 2
      if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) != 2:
          require _param2 < unknown264be753[addr(_param1)].field_0
          if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
              require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
              unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
          unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
          return 0
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
      require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
      require _param2 < unknown264be753[addr(_param1)].field_0
      if uint8(unknown264be753[addr(_param1)][_param2].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0):
          if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
              require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
              unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
          unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
          return 0
      if uint128(unknown264be753[addr(_param1)][_param2].field_8) > 0:
          require _param2 < unknown264be753[addr(_param1)].field_0
          unknown264be753[addr(_param1)][_param2].field_200 % 72057594037927936 = 1
          require _param2 < unknown264be753[addr(_param1)].field_0
          unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
          return uint128(unknown264be753[addr(_param1)][_param2].field_0), 2 * uint128(unknown264be753[addr(_param1)][_param2].field_8)
      if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
          require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
          unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
      unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
      return uint128(unknown264be753[addr(_param1)][_param2].field_0), 0
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) == 2:
      require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) <= 2
      if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) != 2:
          require _param2 < unknown264be753[addr(_param1)].field_0
          if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
              require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
              unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
          unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
          return 0
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
      require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
      require _param2 < unknown264be753[addr(_param1)].field_0
      if uint8(unknown264be753[addr(_param1)][_param2].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0):
          if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
              require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
              unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
          unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
          return 0
      if 3 * uint128(unknown264be753[addr(_param1)][_param2].field_8) > 0:
          require _param2 < unknown264be753[addr(_param1)].field_0
          unknown264be753[addr(_param1)][_param2].field_200 % 72057594037927936 = 1
          require _param2 < unknown264be753[addr(_param1)].field_0
          unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
          return 3 * uint128(unknown264be753[addr(_param1)][_param2].field_8), 
                 4 * uint128(unknown264be753[addr(_param1)][_param2].field_8)
      if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
          require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
          unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
      unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
      return 3 * uint128(unknown264be753[addr(_param1)][_param2].field_8), 0
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) == 3:
      require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) <= 2
      if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) != 2:
          require _param2 < unknown264be753[addr(_param1)].field_0
          if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
              require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
              unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
          unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
          return 0
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
      require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
      require _param2 < unknown264be753[addr(_param1)].field_0
      if uint8(unknown264be753[addr(_param1)][_param2].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0):
          if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
              require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
              unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
          unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
          return 0
      if 4 * uint128(uint128(unknown264be753[addr(_param1)][_param2].field_8)) > 0:
          require _param2 < unknown264be753[addr(_param1)].field_0
          unknown264be753[addr(_param1)][_param2].field_200 % 72057594037927936 = 1
          require _param2 < unknown264be753[addr(_param1)].field_0
          unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
          return uint128(unknown264be753[addr(_param1)][_param2].field_8) << 128, 
                 uint128(unknown264be753[addr(_param1)][_param2].field_8) + (4 * uint128(uint128(unknown264be753[addr(_param1)][_param2].field_8)))
      if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
          require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
          unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
      unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
      return uint128(unknown264be753[addr(_param1)][_param2].field_8) << 128, 0
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
  require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) <= 2
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) != 4:
      if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) == 2:
          require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
          require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
      require _param2 < unknown264be753[addr(_param1)].field_0
      if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
          require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
          unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
      unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
      return 0
  if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) != 2:
      require _param2 < unknown264be753[addr(_param1)].field_0
      if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
          require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
          unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
      unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
      return 0
  require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  require _param2 < unknown264be753[addr(_param1)].field_0
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0):
      if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
          require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
          unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
      unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
      return 0
  if 19 * uint128(unknown264be753[addr(_param1)][_param2].field_8) > 0:
      require _param2 < unknown264be753[addr(_param1)].field_0
      unknown264be753[addr(_param1)][_param2].field_200 % 72057594037927936 = 1
      require _param2 < unknown264be753[addr(_param1)].field_0
      unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
      return 19 * uint128(unknown264be753[addr(_param1)][_param2].field_8), 
             20 * uint128(unknown264be753[addr(_param1)][_param2].field_8)
  if not uint8(unknown264be753[addr(_param1)][_param2].field_216):
      require uint128(unknown264be753[addr(_param1)][_param2].field_8) + unknown7952ea9d >= unknown7952ea9d
      unknown7952ea9d += uint128(unknown264be753[addr(_param1)][_param2].field_8)
  unknown264be753[addr(_param1)][_param2].field_208 % 281474976710656 = 1
  return 19 * uint128(unknown264be753[addr(_param1)][_param2].field_8), 0


# hash = 0x6b0f9b09
# getter = None
# const = None
# payable = False
def unknown6b0f9b09(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknowndb85e2a0 = _param1


# hash = 0x6d1a4496
# getter = ['bool', ['storage', 8, 0, 18]]
# const = None
# payable = False
def unknown6d1a4496(): # not payable
  return bool(unknown6d1a4496)


# hash = 0x6ff1c9bc
# getter = None
# const = None
# payable = False
def unknown6ff1c9bc(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require caller == casinoAddress
  call _param1 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x7142451c
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def unknown7142451c(): # not payable
  return unknown7142451c


# hash = 0x75619ab5
# getter = None
# const = None
# payable = False
def setDistributor(address _distributor): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  distributorAddress = _distributor


# hash = 0x7892fd29
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def ROUND_TIME(): # not payable
  return ROUND_TIME


# hash = 0x7952ea9d
# getter = ['storage', 256, 0, 26]
# const = None
# payable = False
def unknown7952ea9d(): # not payable
  return unknown7952ea9d


# hash = 0x79c4d445
# getter = None
# const = None
# payable = False
def unknown79c4d445(uint8 _param1): # not payable
  require calldata.size - 4 >= 32
  if not unknown6d1a4496:
      require _param1 <= 5
      return unknown46228a93[_param1 << 248]
  require _param1 <= 5
  if _param1 == 1:
      require ext_code.size(settingsAddress)
      static call settingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return (unknown326c25ad * ext_call.return_data[0])
  require _param1 <= 5
  if _param1 == 2:
      require ext_code.size(settingsAddress)
      static call settingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return (50 * unknown326c25ad * ext_call.return_data[0] / 100)
  require _param1 <= 5
  if _param1 == 3:
      require ext_code.size(settingsAddress)
      static call settingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return (40 * unknown326c25ad * ext_call.return_data[0] / 100)
  require _param1 <= 5
  if _param1 != 4:
      return 0
  require ext_code.size(settingsAddress)
  static call settingsAddress.ETH_TO_WEI() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return (10 * unknown326c25ad * ext_call.return_data[0] / 100)


# hash = 0x80057b9a
# getter = None
# const = None
# payable = False
def getColor(uint256 _id): # not payable
  require calldata.size - 4 >= 32
  if _id < 20:
      return 1
  if _id < 30:
      return 2
  if _id < 38:
      return 3
  if _id < 40:
      return 4
  if _id >= 42:
      return 0
  return 5


# hash = 0x82bc07e6
# getter = ['storage', 64, 0, 24]
# const = None
# payable = False
def lastRound(): # not payable
  return lastRound


# hash = 0x88ea41b9
# getter = None
# const = None
# payable = False
def setMinBet(uint256 _eth): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  MIN_BET = _eth
  log 0x2668101b: _eth


# hash = 0x8984e2b4
# getter = None
# const = None
# payable = False
def unknown8984e2b4(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if 4760 == _param1:
      if not unknown6d1a4496:
          return MIN_BET, unknown46228a93[1], unknownea6700e2, unknowndb85e2a0
      require ext_code.size(settingsAddress)
      static call settingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return MIN_BET, unknown326c25ad * ext_call.return_data[0], unknownea6700e2, unknowndb85e2a0
  if 2380 == _param1:
      if not unknown6d1a4496:
          return MIN_BET, unknown46228a93[2], unknownea6700e2, unknowndb85e2a0
      require ext_code.size(settingsAddress)
      static call settingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return MIN_BET, 50 * unknown326c25ad * ext_call.return_data[0] / 100, unknownea6700e2, unknowndb85e2a0
  if 1904 == _param1:
      if not unknown6d1a4496:
          return MIN_BET, unknown46228a93[3], unknownea6700e2, unknowndb85e2a0
      require ext_code.size(settingsAddress)
      static call settingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return MIN_BET, 40 * unknown326c25ad * ext_call.return_data[0] / 100, unknownea6700e2, unknowndb85e2a0
  if _param1 != 476:
      if not unknown6d1a4496:
          return MIN_BET, unknown46228a93[5], unknownea6700e2, unknowndb85e2a0
      return MIN_BET, 0, unknownea6700e2, unknowndb85e2a0
  if not unknown6d1a4496:
      return MIN_BET, unknown46228a93[4], unknownea6700e2, unknowndb85e2a0
  require ext_code.size(settingsAddress)
  static call settingsAddress.ETH_TO_WEI() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return MIN_BET, 10 * unknown326c25ad * ext_call.return_data[0] / 100, unknownea6700e2, unknowndb85e2a0


# hash = 0x8a6b114b
# getter = None
# const = None
# payable = False
def getBet(address _player, uint256 _game): # not payable
  require calldata.size - 4 >= 64
  require _game < unknown264be753[addr(_player)].field_0
  require uint8(unknown264be753[addr(_player)][_game].field_0) <= 5
  require uint64(unknown264be753[addr(_player)][_game].field_136) < rounds.length
  require _game < unknown264be753[addr(_player)].field_0
  require uint8(unknown264be753[addr(_player)][_game].field_0) <= 5
  require uint64(unknown264be753[addr(_player)][_game].field_136) < rounds.length
  require uint8(unknown264be753[addr(_player)][_game].field_0) <= 5
  if uint8(unknown264be753[addr(_player)][_game].field_0) == 1:
      if uint64(unknown264be753[addr(_player)][_game].field_136) < rounds.length:
          if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_8) <= 2:
              if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_8) != 2:
                  if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                      if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                          return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                 uint8(unknown264be753[addr(_player)][_game].field_0),
                                 uint128(unknown264be753[addr(_player)][_game].field_0),
                                 uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                 0
              else:
                  if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                      if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                          if uint8(unknown264be753[addr(_player)][_game].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0):
                              if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                  if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                      return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                             uint8(unknown264be753[addr(_player)][_game].field_0),
                                             uint128(unknown264be753[addr(_player)][_game].field_0),
                                             uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                             0
                          else:
                              if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                  if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                      return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                             uint8(unknown264be753[addr(_player)][_game].field_0),
                                             uint128(unknown264be753[addr(_player)][_game].field_0),
                                             uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                             uint128(unknown264be753[addr(_player)][_game].field_8) > 0
  else:
      if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
          if uint8(unknown264be753[addr(_player)][_game].field_0) == 2:
              if uint64(unknown264be753[addr(_player)][_game].field_136) < rounds.length:
                  if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_8) <= 2:
                      if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_8) != 2:
                          if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                              if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                  return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                         uint8(unknown264be753[addr(_player)][_game].field_0),
                                         uint128(unknown264be753[addr(_player)][_game].field_0),
                                         uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                         0
                      else:
                          if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                              if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                  if uint8(unknown264be753[addr(_player)][_game].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0):
                                      if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                          if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                              return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                                     uint8(unknown264be753[addr(_player)][_game].field_0),
                                                     uint128(unknown264be753[addr(_player)][_game].field_0),
                                                     uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                                     0
                                  else:
                                      if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                          if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                              return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                                     uint8(unknown264be753[addr(_player)][_game].field_0),
                                                     uint128(unknown264be753[addr(_player)][_game].field_0),
                                                     uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                                     3 * uint128(unknown264be753[addr(_player)][_game].field_8) > 0
          else:
              if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                  if uint8(unknown264be753[addr(_player)][_game].field_0) == 3:
                      if uint64(unknown264be753[addr(_player)][_game].field_136) < rounds.length:
                          if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_8) <= 2:
                              if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_8) != 2:
                                  if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                      if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                          return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                                 uint8(unknown264be753[addr(_player)][_game].field_0),
                                                 uint128(unknown264be753[addr(_player)][_game].field_0),
                                                 uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                                 0
                              else:
                                  if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                      if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                          if uint8(unknown264be753[addr(_player)][_game].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0):
                                              if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                                  if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                                      return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                                             uint8(unknown264be753[addr(_player)][_game].field_0),
                                                             uint128(unknown264be753[addr(_player)][_game].field_0),
                                                             uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                                             0
                                          else:
                                              if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                                  if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                                      return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                                             uint8(unknown264be753[addr(_player)][_game].field_0),
                                                             uint128(unknown264be753[addr(_player)][_game].field_0),
                                                             uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                                             4 * uint128(uint128(unknown264be753[addr(_player)][_game].field_8)) > 0
                  else:
                      if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                          if uint8(unknown264be753[addr(_player)][_game].field_0) != 4:
                              if uint64(unknown264be753[addr(_player)][_game].field_136) < rounds.length:
                                  if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_8) <= 2:
                                      if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_8) != 2:
                                          if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                              if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                                  return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                                         uint8(unknown264be753[addr(_player)][_game].field_0),
                                                         uint128(unknown264be753[addr(_player)][_game].field_0),
                                                         uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                                         0
                                      else:
                                          if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                              if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                                  if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                                      if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                                          return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                                                 uint8(unknown264be753[addr(_player)][_game].field_0),
                                                                 uint128(unknown264be753[addr(_player)][_game].field_0),
                                                                 uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                                                 0
                          else:
                              if uint64(unknown264be753[addr(_player)][_game].field_136) < rounds.length:
                                  if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_8) <= 2:
                                      if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_8) != 2:
                                          if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                              if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                                  return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                                         uint8(unknown264be753[addr(_player)][_game].field_0),
                                                         uint128(unknown264be753[addr(_player)][_game].field_0),
                                                         uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                                         0
                                      else:
                                          if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                              if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                                  if uint8(unknown264be753[addr(_player)][_game].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0):
                                                      if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                                          if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                                              return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                                                     uint8(unknown264be753[addr(_player)][_game].field_0),
                                                                     uint128(unknown264be753[addr(_player)][_game].field_0),
                                                                     uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                                                     0
                                                  else:
                                                      if uint8(unknown264be753[addr(_player)][_game].field_0) <= 5:
                                                          if uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0) <= 5:
                                                              return uint64(unknown264be753[addr(_player)][_game].field_0), 
                                                                     uint8(unknown264be753[addr(_player)][_game].field_0),
                                                                     uint128(unknown264be753[addr(_player)][_game].field_0),
                                                                     uint8(rounds[2 * uint64(uint64(stor29[addr(_player)][_game].field_136))].field_0),
                                                                     19 * uint128(unknown264be753[addr(_player)][_game].field_8) > 0
  revert


# hash = 0x8b706799
# getter = None
# const = None
# payable = False
def unknown8b706799(uint256 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  if 50 == _param1:
      return _param2
  if 4760 == _param1:
      return _param2
  if 2380 == _param1:
      return (3 * _param2)
  if 1904 == _param1:
      return (4 * _param2)
  if _param1 != 476:
      return 0
  return (19 * _param2)


# hash = 0x8c65c81f
# getter = ['struct', ['loc', 30]]
# const = None
# payable = False
def rounds(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < rounds.length
  require uint8(rounds[_param1].field_0) <= 5
  require uint8(rounds[_param1].field_8) <= 2
  return uint8(rounds[_param1].field_0), uint8(rounds[_param1].field_0), rounds[_param1].field_256


# hash = 0x93d1259f
# getter = None
# const = None
# payable = False
def unknown93d1259f(bool _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown6d1a4496 = uint8(_param1)
  log 0xfd21a702: _param1


# hash = 0x9403e8dd
# getter = ['storage', 160, 0, 31]
# const = None
# payable = False
def casino(): # not payable
  return casinoAddress


# hash = 0x95b0f404
# getter = None
# const = None
# payable = False
def unknown95b0f404(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknownec11c49e = _param1


# hash = 0x95e4d2ed
# getter = None
# const = None
# payable = False
def unknown95e4d2ed(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown178f9ebd = _param1


# hash = 0x986ad946
# getter = None
# const = None
# payable = False
def unknown986ad946(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if 4760 == _param1:
      return 1
  if 2380 == _param1:
      return 2
  if 1904 == _param1:
      return 3
  if _param1 != 476:
      return 5
  return 4


# hash = 0xa80c74bf
# getter = None
# const = None
# payable = False
def unknowna80c74bf(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown46228a93[4] = _param1
  unknown307320b5 = _param1
  log 0xfec588ee: 4, _param1


# hash = 0xa8e14f65
# getter = None
# const = None
# payable = False
def unknowna8e14f65(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < unknown264be753[addr(_param1)].field_0
  require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
  require uint8(rounds[uint64(stor29[addr(_param1)][_param2].field_136)].field_8) <= 2
  if uint8(rounds[uint64(stor29[addr(_param1)][_param2].field_136)].field_8) != 2:
      return 0
  return 1


# hash = 0xb2a8325e
# getter = None
# const = None
# payable = False
def unknownb2a8325e(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown46228a93[3] = _param1
  unknown2e4bda25 = _param1
  log 0xfec588ee: 3, _param1


# hash = 0xbd874dff
# getter = ['storage', 256, 0, 27]
# const = None
# payable = False
def unknownbd874dff(): # not payable
  return unknownbd874dff


# hash = 0xbefec197
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknownbefec197(): # not payable
  return unknownbefec197


# hash = 0xbfe10928
# getter = ['storage', 160, 0, 32]
# const = None
# payable = False
def distributor(): # not payable
  return distributorAddress


# hash = 0xc4ea0bcd
# getter = ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 28]]]
# const = None
# payable = False
def unknownc4ea0bcd(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require unknownc4ea0bcd[_param1] <= 2
  return unknownc4ea0bcd[_param1]


# hash = 0xc9f60c62
# getter = None
# const = None
# payable = False
def unknownc9f60c62(uint8 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 <= 5
  if _param1 == 1:
      return 4760
  require _param1 <= 5
  if _param1 == 2:
      return 2380
  require _param1 <= 5
  if _param1 == 3:
      return 1904
  require _param1 <= 5
  if _param1 != 4:
      return 0
  return 476


# hash = 0xdb85e2a0
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def unknowndb85e2a0(): # not payable
  return unknowndb85e2a0


# hash = 0xe06174e4
# getter = ['storage', 160, 0, 21]
# const = None
# payable = False
def settings(): # not payable
  return settingsAddress


# hash = 0xe105e7eb
# getter = None
# const = None
# payable = False
def unknowne105e7eb(addr _param1): # not payable
  require calldata.size - 4 >= 32
  mem[0] = _param1
  mem[32] = 29
  if unknown264be753[addr(_param1)].field_0 <= 0:
      return 0
  [94midx = stor[sha3(mem[0 len 64])]
  [94ms = 0
  [94mt = 0
  while [94midx >= 0:
      require [94midx - 1 < unknown264be753[addr(_param1)].field_0
      mem[32] = 29
      require [94midx - 1 < unknown264be753[addr(_param1)].field_0
      mem[0] = sha3(addr(_param1), 29)
      require uint8(unknown264be753[addr(_param1)][[94midx].field_0) <= 5
      if not uint8(unknown264be753[addr(_param1)][[94midx].field_0):
          if [94midx - 1 != 0:
              if (10 * [94mt) + 1 <= 10000:
                  [94midx = [94midx - 1
                  [94ms = (10 * [94ms) + uint8(unknown264be753[addr(_param1)][[94midx].field_0)
                  [94mt = (10 * [94mt) + 1
                  continue 
          return (10 * [94mt) + 1, (10 * [94ms) + uint8(unknown264be753[addr(_param1)][[94midx].field_0)
      if [94midx - 1 != 0:
          if (10 * [94mt) + 2 <= 10000:
              [94midx = [94midx - 1
              [94ms = (10 * [94ms) + uint8(unknown264be753[addr(_param1)][[94midx].field_0)
              [94mt = (10 * [94mt) + 2
              continue 
      return (10 * [94mt) + 2, (10 * [94ms) + uint8(unknown264be753[addr(_param1)][[94midx].field_0)
  return [94mt, [94ms


# hash = 0xe8967dbb
# getter = ['struct', ['loc', 29]]
# const = None
# payable = False
def unknowne8967dbb(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < unknown264be753[addr(_param1)].field_0
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  return uint128(unknown264be753[addr(_param1)][_param2].field_0), 
         bool(uint8(unknown264be753[addr(_param1)][_param2].field_208)),
         bool(uint8(unknown264be753[addr(_param1)][_param2].field_200)),
         bool(uint8(unknown264be753[addr(_param1)][_param2].field_216))


# hash = 0xe929a58b
# getter = None
# const = None
# payable = False
def unknowne929a58b(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown46228a93[1] = _param1
  unknown7142451c = _param1
  log 0xfec588ee: 1, _param1


# hash = 0xea6700e2
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknownea6700e2(): # not payable
  return unknownea6700e2


# hash = 0xec11c49e
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def unknownec11c49e(): # not payable
  return unknownec11c49e


# hash = 0xee6892ed
# getter = None
# const = None
# payable = False
def unknownee6892ed(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < unknown264be753[addr(_param1)].field_0
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) == 1:
      require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) <= 2
      if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) != 2:
          return 0
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
      require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
      if uint8(unknown264be753[addr(_param1)][_param2].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0):
          return 0
      return uint128(unknown264be753[addr(_param1)][_param2].field_0)
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) == 2:
      require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) <= 2
      if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) != 2:
          return 0
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
      require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
      if uint8(unknown264be753[addr(_param1)][_param2].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0):
          return 0
      return (3 * uint128(unknown264be753[addr(_param1)][_param2].field_0))
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) == 3:
      require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) <= 2
      if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) != 2:
          return 0
      require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
      require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
      if uint8(unknown264be753[addr(_param1)][_param2].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0):
          return 0
      return (4 * uint128(uint128(unknown264be753[addr(_param1)][_param2].field_8)))
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  require uint64(unknown264be753[addr(_param1)][_param2].field_136) < rounds.length
  require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) <= 2
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) != 4:
      if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) == 2:
          require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
          require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
          return 0
      else:
          return 0
  if uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_8) != 2:
      return 0
  require uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0) <= 5
  require uint8(unknown264be753[addr(_param1)][_param2].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][_param2].field_0) != uint8(rounds[2 * uint64(uint64(stor29[addr(_param1)][_param2].field_136))].field_0):
      return 0
  return (19 * uint128(unknown264be753[addr(_param1)][_param2].field_0))


# hash = 0xf25b7675
# getter = None
# const = None
# payable = False
def unknownf25b7675(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require unknown264be753[addr(_param1)].field_0 - 1 < unknown264be753[addr(_param1)].field_0
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 5
  require uint64(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) < rounds.length
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) == 1:
      return rounds[2 * uint64(uint64(stor29[addr(_param1)][stor29[addr(_param1)].field_0].field_0))].field_256, 
             uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             4760
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) == 2:
      return rounds[2 * uint64(uint64(stor29[addr(_param1)][stor29[addr(_param1)].field_0].field_0))].field_256, 
             uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             2380
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) == 3:
      return rounds[2 * uint64(uint64(stor29[addr(_param1)][stor29[addr(_param1)].field_0].field_0))].field_256, 
             uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             1904
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 5
  if uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) != 4:
      return rounds[2 * uint64(uint64(stor29[addr(_param1)][stor29[addr(_param1)].field_0].field_0))].field_256, 
             uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             0
  return rounds[2 * uint64(uint64(stor29[addr(_param1)][stor29[addr(_param1)].field_0].field_0))].field_256, 
         uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
         476


# hash = 0xf91ea562
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknownf91ea562(): # not payable
  return unknownf91ea562


# hash = 0xfa65cb04
# getter = None
# const = None
# payable = False
def unknownfa65cb04(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  ROUND_TIME = _param1
  log 0x2a9e9292: _param1


# hash = 0xfd874762
# getter = None
# const = None
# payable = False
def unknownfd874762(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  casinoAddress = _param1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


