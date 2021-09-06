# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x461CF4FCa42E12D95DEF43EC0f14512B34498E00 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x1e270dc6': 'unknown1e270dc6(?)', '0x27dc297e': '__callback(bytes32 _myid, string _result)', '0x442a13a5': 'unknown442a13a5(?)', '0x67988182': 'unknown67988182(?)', '0x8a6b114b': 'getBet(address _player, uint256 _game)', '0xc92025f5': 'unknownc92025f5(?)', '0xee6892ed': 'unknownee6892ed(?)'} 

# storage definitions
def storage:
    # storage address 5
    ROUND_TIME # mask: a s
    # storage address 6
    unknownbefec197 # mask: a s
    # storage address 7
    unknown434e2897 # mask: a s
    # storage address 8
    unknown326c25ad # mask: a s
    # storage address 9
    HOUSE_EDGE # mask: a s
    # storage address 10
    MIN_BET # mask: a s
    # storage address 11
    MAX_BET # mask: a s
    # storage address 12
    unknowndb85e2a0 # mask: a s
    # storage address 13
    unknownea6700e2 # mask: a s
    # storage address 14
    stor14 # mask: a s
    # storage address 14
    unknown6d1a4496 # mask: a s
    # storage address 14
    unknown0f055139 # mask: a s
    # storage address 15
    unknownec11c49e # mask: a s
    # storage address 16
    unknown178f9ebd # mask: a s
    # storage address 17
    settingsAddress # mask: a s
    # storage address 21
    unknown236e5e4c # mask: a s
    # storage address 22
    unknown0aefecb5 # mask: a s
    # storage address 23
    unknown7952ea9d # mask: a s
    # storage address 24
    unknownbd874dff # mask: a s
    # storage address 25
    unknowne7ef3eb6 # mask: a s
    # storage address 26
    unknownc4ea0bcd
    # storage address 27
    unknown264be753
    # storage address 28
    rounds
    # storage address 29
    casinoAddress # mask: a s
    # storage address 30
    distributorAddress # mask: a s
# hash = 0x0aefecb5
# getter = ['storage', 256, 0, 22]
# const = None
# payable = False
def unknown0aefecb5(): # not payable
  return unknown0aefecb5


# hash = 0x0f055139
# getter = ['bool', ['storage', 8, 8, 14]]
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
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknown178f9ebd(): # not payable
  return unknown178f9ebd


# hash = 0x1a7965d1
# getter = None
# const = None
# payable = False
def unknown1a7965d1(uint8 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param1 <= 4
  if _param1 == 1:
      if _param2 <= 4:
          return (_param2 > 4)
      return (_param2 < 96)
  require _param1 <= 4
  if not _param1:
      if _param2 <= 3:
          return (_param2 > 3)
      return (_param2 < 95)
  require _param1 <= 4
  if _param1 == 2:
      return (_param2 < 100)
  require _param1 <= 4
  if _param1 == 3:
      return (_param2 < 2)
  require _param1 <= 4
  if _param1 != 4:
      return 0
  return (_param2 < 3)


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


# hash = 0x236e5e4c
# getter = ['storage', 256, 0, 21]
# const = None
# payable = False
def unknown236e5e4c(): # not payable
  return unknown236e5e4c


# hash = 0x264be753
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 27]]]
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
  stor14 = Mask(248, 0, _param1)
  log 0x77db83c1: not _param1


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


# hash = 0x326c25ad
# getter = ['storage', 256, 0, 8]
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
# getter = ['storage', 256, 0, 7]
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


# hash = 0x4a39ec90
# getter = ['struct', ['loc', 27]]
# const = None
# payable = False
def bets(address _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < unknown264be753[_param1].field_0
  require uint8(unknown264be753[_param1][_param2].field_8) <= 4
  return uint8(unknown264be753[_param1][_param2].field_0), 
         uint8(unknown264be753[_param1][_param2].field_0),
         uint128(unknown264be753[_param1][_param2].field_0),
         uint64(unknown264be753[_param1][_param2].field_0),
         bool(uint8(unknown264be753[_param1][_param2].field_208)),
         bool(uint8(unknown264be753[_param1][_param2].field_216)),
         bool(uint8(unknown264be753[_param1][_param2].field_224))


# hash = 0x57e1a954
# getter = None
# const = None
# payable = False
def unknown57e1a954(uint8 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param1 <= 4
  if _param1 == 1:
      return _param2
  require _param1 <= 4
  if not _param1:
      return (-_param2 + 99)
  require _param1 <= 4
  if _param1 == 2:
      return 1
  require _param1 <= 4
  if _param1 == 3:
      if _param2:
          return 50
      return 49
  require _param1 <= 4
  if _param1 != 4:
      return 0
  if _param2 != 2:
      return 45
  return 10


# hash = 0x5e51db47
# getter = None
# const = None
# payable = False
def unknown5e51db47(addr _param1): # not payable
  require calldata.size - 4 >= 32
  mem[0] = _param1
  mem[32] = 27
  if unknown264be753[addr(_param1)].field_0 <= 0:
      return 0
  [94midx = stor[sha3(mem[0 len 64])]
  [94ms = 0
  while [94midx >= 0:
      mem[32] = 27
      require [94midx - 1 < unknown264be753[addr(_param1)].field_0
      mem[0] = sha3(addr(_param1), 27)
      if not uint8(unknown264be753[addr(_param1)][[94midx].field_0):
          if [94midx - 1:
              if (10 * [94ms) + 1 <= 10000:
                  [94midx = [94midx - 1
                  [94ms = (10 * [94ms) + 1
                  continue 
          return ((10 * [94ms) + 1)
      if [94midx - 1:
          if (10 * [94ms) + 2 <= 10000:
              [94midx = [94midx - 1
              [94ms = (10 * [94ms) + 2
              continue 
      return ((10 * [94ms) + 2)
  return [94ms


# hash = 0x6540742f
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def MIN_BET(): # not payable
  return MIN_BET


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


# hash = 0x6b5878c0
# getter = None
# const = None
# payable = False
def unknown6b5878c0(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require unknown264be753[addr(_param1)].field_0 - 1 < unknown264be753[addr(_param1)].field_0
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 4
  require uint64(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) < rounds.length
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 4
  if uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) == 1:
      return rounds[2 * uint64(uint64(stor27[addr(_param1)][stor27[addr(_param1)].field_0].field_0))].field_256, 
             uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             bool(uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0))
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 4
  if not uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0):
      return rounds[2 * uint64(uint64(stor27[addr(_param1)][stor27[addr(_param1)].field_0].field_0))].field_256, 
             uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             -uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) + 99,
             bool(uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0))
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 4
  if uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) == 2:
      return rounds[2 * uint64(uint64(stor27[addr(_param1)][stor27[addr(_param1)].field_0].field_0))].field_256, 
             uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             1,
             bool(uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0))
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 4
  if uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) == 3:
      if uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0):
          return rounds[2 * uint64(uint64(stor27[addr(_param1)][stor27[addr(_param1)].field_0].field_0))].field_256, 
                 uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
                 50,
                 bool(uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0))
      return rounds[2 * uint64(uint64(stor27[addr(_param1)][stor27[addr(_param1)].field_0].field_0))].field_256, 
             uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             49,
             bool(uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0))
  require uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) <= 4
  if uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) != 4:
      return rounds[2 * uint64(uint64(stor27[addr(_param1)][stor27[addr(_param1)].field_0].field_0))].field_256, 
             uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             0,
             bool(uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0))
  if uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0) != 2:
      return rounds[2 * uint64(uint64(stor27[addr(_param1)][stor27[addr(_param1)].field_0].field_0))].field_256, 
             uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
             45,
             bool(uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0))
  return rounds[2 * uint64(uint64(stor27[addr(_param1)][stor27[addr(_param1)].field_0].field_0))].field_256, 
         uint128(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0),
         10,
         bool(uint8(unknown264be753[addr(_param1)][unknown264be753[addr(_param1)].field_0].field_0))


# hash = 0x6cd0f102
# getter = None
# const = None
# payable = False
def setHouseEdge(uint256 _value): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require _value < 100000
  HOUSE_EDGE = _value
  log 0x88a54f8c: _value


# hash = 0x6d1a4496
# getter = ['bool', ['storage', 8, 0, 14]]
# const = None
# payable = False
def unknown6d1a4496(): # not payable
  return bool(unknown6d1a4496)


# hash = 0x7250e224
# getter = None
# const = None
# payable = False
def addDistributor(address _new): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  distributorAddress = _new


# hash = 0x7892fd29
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def ROUND_TIME(): # not payable
  return ROUND_TIME


# hash = 0x7952ea9d
# getter = ['storage', 256, 0, 23]
# const = None
# payable = False
def unknown7952ea9d(): # not payable
  return unknown7952ea9d


# hash = 0x7e95b523
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def MAX_BET(): # not payable
  return MAX_BET


# hash = 0x82bc07e6
# getter = None
# const = None
# payable = False
def lastRound(): # not payable
  return (rounds.length - 1)


# hash = 0x881eff1e
# getter = None
# const = None
# payable = False
def setMaxBet(uint256 _newMaxBet): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  MAX_BET = _newMaxBet
  log 0xaa2f425a: _newMaxBet


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
  if not unknown6d1a4496:
      return MIN_BET, MAX_BET, unknownea6700e2, unknowndb85e2a0
  if _param1 < 13:
      if _param1 > 4:
          require ext_code.size(settingsAddress)
          static call settingsAddress.ETH_TO_WEI() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not (3 * _param1) - 5:
              return MIN_BET, 0, unknownea6700e2, unknowndb85e2a0
          require (-5 * unknown326c25ad * ext_call.return_data[0]) + (3 * _param1 * unknown326c25ad * ext_call.return_data[0]) / (3 * _param1) - 5 == unknown326c25ad * ext_call.return_data[0]
          return MIN_BET, 
                 (-5 * unknown326c25ad * ext_call.return_data[0]) + (3 * _param1 * unknown326c25ad * ext_call.return_data[0]) / 100,
                 unknownea6700e2,
                 unknowndb85e2a0
  require ext_code.size(settingsAddress)
  static call settingsAddress.ETH_TO_WEI() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _param1 < 46:
      if not (2 * _param1) + 8:
          return MIN_BET, 0, unknownea6700e2, unknowndb85e2a0
      require (8 * unknown326c25ad * ext_call.return_data[0]) + (2 * _param1 * unknown326c25ad * ext_call.return_data[0]) / (2 * _param1) + 8 == unknown326c25ad * ext_call.return_data[0]
      return MIN_BET, 
             (8 * unknown326c25ad * ext_call.return_data[0]) + (2 * _param1 * unknown326c25ad * ext_call.return_data[0]) / 100,
             unknownea6700e2,
             unknowndb85e2a0
  if _param1 < 56:
      return MIN_BET, unknown326c25ad * ext_call.return_data[0], unknownea6700e2, unknowndb85e2a0
  if not _param1 - 55:
      require 100 * unknown326c25ad * ext_call.return_data[0] / 100 == unknown326c25ad * ext_call.return_data[0]
      return MIN_BET, 100 * unknown326c25ad * ext_call.return_data[0] / 100, unknownea6700e2, unknowndb85e2a0
  require (5 * _param1) - 275 / _param1 - 55 == 5
  if not (5 * _param1) - 175:
      return MIN_BET, 0, unknownea6700e2, unknowndb85e2a0
  require (-175 * unknown326c25ad * ext_call.return_data[0]) + (5 * _param1 * unknown326c25ad * ext_call.return_data[0]) / (5 * _param1) - 175 == unknown326c25ad * ext_call.return_data[0]
  return MIN_BET, 
         (-175 * unknown326c25ad * ext_call.return_data[0]) + (5 * _param1 * unknown326c25ad * ext_call.return_data[0]) / 100,
         unknownea6700e2,
         unknowndb85e2a0


# hash = 0x8b706799
# getter = None
# const = None
# payable = False
def unknown8b706799(uint256 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param1 <= 100
  if not HOUSE_EDGE:
      require -_param1 + 100 > 0
      require -_param1 + 100
      if not _param2:
          require _param1 > 0
          require _param1
          if not 0 / _param1:
              return 0
          require (100000 * 0 / _param1) - (0 / -_param1 + 100 * 0 / _param1) / 0 / _param1 == -(0 / -_param1 + 100) + 100000
          return ((100000 * 0 / _param1) - (0 / -_param1 + 100 * 0 / _param1) / 100000)
      require (100 * _param2) - (_param1 * _param2) / _param2 == -_param1 + 100
      require _param1 > 0
      require _param1
      if not (100 * _param2) - (_param1 * _param2) / _param1:
          return 0
      require (100000 * (100 * _param2) - (_param1 * _param2) / _param1) - (0 / -_param1 + 100 * (100 * _param2) - (_param1 * _param2) / _param1) / (100 * _param2) - (_param1 * _param2) / _param1 == -(0 / -_param1 + 100) + 100000
      return ((100000 * (100 * _param2) - (_param1 * _param2) / _param1) - (0 / -_param1 + 100 * (100 * _param2) - (_param1 * _param2) / _param1) / 100000)
  require 100 * HOUSE_EDGE / HOUSE_EDGE == 100
  require -_param1 + 100 > 0
  require -_param1 + 100
  if not _param2:
      require _param1 > 0
      require _param1
      if not 0 / _param1:
          return 0
      require (100000 * 0 / _param1) - (100 * HOUSE_EDGE / -_param1 + 100 * 0 / _param1) / 0 / _param1 == -(100 * HOUSE_EDGE / -_param1 + 100) + 100000
      return ((100000 * 0 / _param1) - (100 * HOUSE_EDGE / -_param1 + 100 * 0 / _param1) / 100000)
  require (100 * _param2) - (_param1 * _param2) / _param2 == -_param1 + 100
  require _param1 > 0
  require _param1
  if not (100 * _param2) - (_param1 * _param2) / _param1:
      return 0
  require (100000 * (100 * _param2) - (_param1 * _param2) / _param1) - (100 * HOUSE_EDGE / -_param1 + 100 * (100 * _param2) - (_param1 * _param2) / _param1) / (100 * _param2) - (_param1 * _param2) / _param1 == -(100 * HOUSE_EDGE / -_param1 + 100) + 100000
  return ((100000 * (100 * _param2) - (_param1 * _param2) / _param1) - (100 * HOUSE_EDGE / -_param1 + 100 * (100 * _param2) - (_param1 * _param2) / _param1) / 100000)


# hash = 0x8c65c81f
# getter = ['struct', ['loc', 28]]
# const = None
# payable = False
def rounds(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < rounds.length
  require uint8(rounds[_param1].field_224) <= 2
  return Mask(224, 0, rounds[_param1].field_0), uint8(rounds[_param1].field_0), rounds[_param1].field_256


# hash = 0x8daaaa2f
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def HOUSE_EDGE(): # not payable
  return HOUSE_EDGE


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
# getter = ['storage', 160, 0, 29]
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


# hash = 0xa7e32ee5
# getter = None
# const = None
# payable = False
def unknowna7e32ee5(addr _param1): # not payable
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


# hash = 0xa8e14f65
# getter = None
# const = None
# payable = False
def unknowna8e14f65(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < unknown264be753[addr(_param1)].field_0
  require uint64(unknown264be753[addr(_param1)][_param2].field_144) < rounds.length
  require uint8(rounds[uint64(stor27[addr(_param1)][_param2].field_144)].field_224) <= 2
  if uint8(rounds[uint64(stor27[addr(_param1)][_param2].field_144)].field_224) != 2:
      return 0
  return 1


# hash = 0xb1fc8ad4
# getter = None
# const = None
# payable = False
def unknownb1fc8ad4(uint256 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param1 <= 100
  if not HOUSE_EDGE:
      require -_param1 + 100 > 0
      require -_param1 + 100
      if not _param2:
          require _param1 > 0
          require _param1
          if not 0 / _param1:
              return 0
          require 0 / -_param1 + 100 * 0 / _param1 / 0 / _param1 == 0 / -_param1 + 100
          return (0 / -_param1 + 100 * 0 / _param1 / 100000)
      require (100 * _param2) - (_param1 * _param2) / _param2 == -_param1 + 100
      require _param1 > 0
      require _param1
      if not (100 * _param2) - (_param1 * _param2) / _param1:
          return 0
      require 0 / -_param1 + 100 * (100 * _param2) - (_param1 * _param2) / _param1 / (100 * _param2) - (_param1 * _param2) / _param1 == 0 / -_param1 + 100
      return (0 / -_param1 + 100 * (100 * _param2) - (_param1 * _param2) / _param1 / 100000)
  require 100 * HOUSE_EDGE / HOUSE_EDGE == 100
  require -_param1 + 100 > 0
  require -_param1 + 100
  if not _param2:
      require _param1 > 0
      require _param1
      if not 0 / _param1:
          return 0
      require 100 * HOUSE_EDGE / -_param1 + 100 * 0 / _param1 / 0 / _param1 == 100 * HOUSE_EDGE / -_param1 + 100
      return (100 * HOUSE_EDGE / -_param1 + 100 * 0 / _param1 / 100000)
  require (100 * _param2) - (_param1 * _param2) / _param2 == -_param1 + 100
  require _param1 > 0
  require _param1
  if not (100 * _param2) - (_param1 * _param2) / _param1:
      return 0
  require 100 * HOUSE_EDGE / -_param1 + 100 * (100 * _param2) - (_param1 * _param2) / _param1 / (100 * _param2) - (_param1 * _param2) / _param1 == 100 * HOUSE_EDGE / -_param1 + 100
  return (100 * HOUSE_EDGE / -_param1 + 100 * (100 * _param2) - (_param1 * _param2) / _param1 / 100000)


# hash = 0xbd874dff
# getter = ['storage', 256, 0, 24]
# const = None
# payable = False
def unknownbd874dff(): # not payable
  return unknownbd874dff


# hash = 0xbefec197
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknownbefec197(): # not payable
  return unknownbefec197


# hash = 0xbfe10928
# getter = ['storage', 160, 0, 30]
# const = None
# payable = False
def distributor(): # not payable
  return distributorAddress


# hash = 0xc4ea0bcd
# getter = ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 26]]]
# const = None
# payable = False
def unknownc4ea0bcd(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require unknownc4ea0bcd[_param1] <= 2
  return unknownc4ea0bcd[_param1]


# hash = 0xdb85e2a0
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknowndb85e2a0(): # not payable
  return unknowndb85e2a0


# hash = 0xe06174e4
# getter = ['storage', 160, 0, 17]
# const = None
# payable = False
def settings(): # not payable
  return settingsAddress


# hash = 0xe165c274
# getter = None
# const = None
# payable = False
def unknowne165c274(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if not unknown6d1a4496:
      return MAX_BET
  if _param1 < 13:
      if _param1 > 4:
          require ext_code.size(settingsAddress)
          static call settingsAddress.ETH_TO_WEI() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not (3 * _param1) - 5:
              return 0
          require (-5 * unknown326c25ad * ext_call.return_data[0]) + (3 * _param1 * unknown326c25ad * ext_call.return_data[0]) / (3 * _param1) - 5 == unknown326c25ad * ext_call.return_data[0]
          return ((-5 * unknown326c25ad * ext_call.return_data[0]) + (3 * _param1 * unknown326c25ad * ext_call.return_data[0]) / 100)
  require ext_code.size(settingsAddress)
  static call settingsAddress.ETH_TO_WEI() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _param1 < 46:
      if not (2 * _param1) + 8:
          return 0
      require (8 * unknown326c25ad * ext_call.return_data[0]) + (2 * _param1 * unknown326c25ad * ext_call.return_data[0]) / (2 * _param1) + 8 == unknown326c25ad * ext_call.return_data[0]
      return ((8 * unknown326c25ad * ext_call.return_data[0]) + (2 * _param1 * unknown326c25ad * ext_call.return_data[0]) / 100)
  if _param1 < 56:
      return (unknown326c25ad * ext_call.return_data[0])
  if not _param1 - 55:
      require 100 * unknown326c25ad * ext_call.return_data[0] / 100 == unknown326c25ad * ext_call.return_data[0]
      return (100 * unknown326c25ad * ext_call.return_data[0] / 100)
  require (5 * _param1) - 275 / _param1 - 55 == 5
  if not (5 * _param1) - 175:
      return 0
  require (-175 * unknown326c25ad * ext_call.return_data[0]) + (5 * _param1 * unknown326c25ad * ext_call.return_data[0]) / (5 * _param1) - 175 == unknown326c25ad * ext_call.return_data[0]
  return ((-175 * unknown326c25ad * ext_call.return_data[0]) + (5 * _param1 * unknown326c25ad * ext_call.return_data[0]) / 100)


# hash = 0xe7ef3eb6
# getter = ['storage', 256, 0, 25]
# const = None
# payable = False
def unknowne7ef3eb6(): # not payable
  return unknowne7ef3eb6


# hash = 0xe8967dbb
# getter = ['struct', ['loc', 27]]
# const = None
# payable = False
def unknowne8967dbb(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < unknown264be753[addr(_param1)].field_0
  require uint8(unknown264be753[addr(_param1)][_param2].field_8) <= 4
  return uint128(unknown264be753[addr(_param1)][_param2].field_0), 
         bool(uint8(unknown264be753[addr(_param1)][_param2].field_216)),
         bool(uint8(unknown264be753[addr(_param1)][_param2].field_208)),
         bool(uint8(unknown264be753[addr(_param1)][_param2].field_224))


# hash = 0xea6700e2
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknownea6700e2(): # not payable
  return unknownea6700e2


# hash = 0xec11c49e
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknownec11c49e(): # not payable
  return unknownec11c49e


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


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


