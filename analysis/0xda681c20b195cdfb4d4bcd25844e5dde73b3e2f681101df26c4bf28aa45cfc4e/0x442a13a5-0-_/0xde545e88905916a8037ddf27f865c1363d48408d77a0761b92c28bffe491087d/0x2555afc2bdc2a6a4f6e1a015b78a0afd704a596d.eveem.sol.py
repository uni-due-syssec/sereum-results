# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x2555aFC2BDc2a6A4f6E1a015B78a0AfD704A596D 
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
    unknown6d1a4496 # mask: a s
    # storage address 14
    stor14 # mask: a s
    # storage address 14
    unknown0f055139 # mask: a s
    # storage address 15
    unknownec11c49e # mask: a s
    # storage address 16
    unknown178f9ebd # mask: a s
    # storage address 17
    settingsAddress # mask: a s
    # storage address 20
    unknown0aefecb5 # mask: a s
    # storage address 21
    unknown7952ea9d # mask: a s
    # storage address 22
    unknownbd874dff # mask: a s
    # storage address 23
    unknownc4ea0bcd
    # storage address 24
    unknown264be753
    # storage address 25
    rounds
    # storage address 26
    casinoAddress # mask: a s
    # storage address 27
    distributorAddress # mask: a s
# hash = 0x0aefecb5
# getter = ['storage', 256, 0, 20]
# const = None
# payable = False
def unknown0aefecb5(): # not payable
  return munknown0aefecb5


# hash = 0x0f055139
# getter = ['bool', ['storage', 8, 8, 14]]
# const = None
# payable = False
def unknown0f055139(): # not payable
  return bool(munknown0f055139)


# hash = 0x163e7285
# getter = None
# const = None
# payable = False
def unknown163e7285(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown434e2897 = m_param1


# hash = 0x164ad4e9
# getter = None
# const = None
# payable = False
def unknown164ad4e9(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown326c25ad = m_param1
  log 0xf47b735d: _param1


# hash = 0x178f9ebd
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknown178f9ebd(): # not payable
  return munknown178f9ebd


# hash = 0x1a7965d1
# getter = None
# const = None
# payable = False
def unknown1a7965d1(uint8 m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param1 <= 4
  if m_param1 == 1:
      if m_param2 <= 4:
          return (m_param2 > 4)
      return (m_param2 < 96)
  require m_param1 <= 4
  if not m_param1:
      if m_param2 <= 3:
          return (m_param2 > 3)
      return (m_param2 < 95)
  require m_param1 <= 4
  if m_param1 == 2:
      return (m_param2 < 100)
  require m_param1 <= 4
  if m_param1 == 3:
      return (m_param2 < 2)
  require m_param1 <= 4
  if m_param1 != 4:
      return 0
  return (m_param2 < 3)


# hash = 0x1f8be1cb
# getter = None
# const = None
# payable = False
def unknown1f8be1cb(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknownea6700e2 = m_param1


# hash = 0x264be753
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 24]]]
# const = None
# payable = False
def unknown264be753(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown264be753m[addr(m_param1)m]m.field_0


# hash = 0x2a3ec233
# getter = None
# const = None
# payable = False
def unknown2a3ec233(bool m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mstor14 = Mask(248, 0, m_param1)
  log 0x77db83c1: not _param1


# hash = 0x2f4ae2d6
# getter = None
# const = None
# payable = False
def unknown2f4ae2d6(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknownbefec197 = m_param1


# hash = 0x326c25ad
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def unknown326c25ad(): # not payable
  return munknown326c25ad


# hash = 0x38bbfa50
# getter = None
# const = None
# payable = False
def __callback(bytes32 m_myid, string m_result, bytes m_proof): # not payable
  require calldata.size - 4 >= 96
  require m_result <= 4294967296
  require m_result + 36 <= calldata.size
  require m_result.length <= 4294967296 and m_result + m_result.length + 36 <= calldata.size
  require m_proof <= 4294967296
  require m_proof + 36 <= calldata.size
  require m_proof.length <= 4294967296 and m_proof + m_proof.length + 36 <= calldata.size


# hash = 0x434e2897
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def unknown434e2897(): # not payable
  return munknown434e2897


# hash = 0x440277e8
# getter = None
# const = None
# payable = False
def unknown440277e8(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(mcasinoAddress)
  static call mcasinoAddress.0x440277e8 with:
          gas gas_remaining wei
         args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x4a39ec90
# getter = ['struct', ['loc', 24]]
# const = None
# payable = False
def bets(address m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 < munknown264be753m[m_param1m]m.field_0
  require uint8(munknown264be753m[m_param1m]m[m_param2m]m.field_8) <= 4
  return uint8(munknown264be753m[m_param1m]m[m_param2m]m.field_0), 
         uint8(munknown264be753m[m_param1m]m[m_param2m]m.field_0),
         uint128(munknown264be753m[m_param1m]m[m_param2m]m.field_0),
         uint64(munknown264be753m[m_param1m]m[m_param2m]m.field_0),
         bool(uint8(munknown264be753m[m_param1m]m[m_param2m]m.field_208)),
         bool(uint8(munknown264be753m[m_param1m]m[m_param2m]m.field_216)),
         bool(uint8(munknown264be753m[m_param1m]m[m_param2m]m.field_224))


# hash = 0x57e1a954
# getter = None
# const = None
# payable = False
def unknown57e1a954(uint8 m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param1 <= 4
  if m_param1 == 1:
      return m_param2
  require m_param1 <= 4
  if not m_param1:
      return (-m_param2 + 99)
  require m_param1 <= 4
  if m_param1 == 2:
      return 1
  require m_param1 <= 4
  if m_param1 == 3:
      if m_param2:
          return 50
      return 49
  require m_param1 <= 4
  if m_param1 != 4:
      return 0
  if m_param2 != 2:
      return 45
  return 10


# hash = 0x5e51db47
# getter = None
# const = None
# payable = False
def unknown5e51db47(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  mem[0] = m_param1
  mem[32] = 24
  if munknown264be753m[addr(m_param1)m]m.field_0 <= 0:
      return 0
  [94midx = mstor[sha3(mem[0 len 64])m]
  [94ms = 0
  mwhile [94midx >= 0m:
      mem[32] = 24
      require [94midx - 1 < munknown264be753m[addr(m_param1)m]m.field_0
      mem[0] = sha3(addr(m_param1), 24)
      if not uint8(munknown264be753m[addr(m_param1)m]m[[94midxm]m.field_0):
          if [94midx - 1:
              if (10 * [94ms) + 1 <= 10000:
                  [94midx = [94midx - 1
                  [94ms = (10 * [94ms) + 1
                  mcontinue 
          return ((10 * [94ms) + 1)
      if [94midx - 1:
          if (10 * [94ms) + 2 <= 10000:
              [94midx = [94midx - 1
              [94ms = (10 * [94ms) + 2
              mcontinue 
      return ((10 * [94ms) + 2)
  return [94ms


# hash = 0x6540742f
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def MIN_BET(): # not payable
  return mMIN_BET


# hash = 0x6b0f9b09
# getter = None
# const = None
# payable = False
def unknown6b0f9b09(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknowndb85e2a0 = m_param1


# hash = 0x6cd0f102
# getter = None
# const = None
# payable = False
def setHouseEdge(uint256 m_value): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require m_value < 100000
  mHOUSE_EDGE = m_value
  log 0x88a54f8c: _value


# hash = 0x6d1a4496
# getter = ['bool', ['storage', 8, 0, 14]]
# const = None
# payable = False
def unknown6d1a4496(): # not payable
  return bool(munknown6d1a4496)


# hash = 0x6ff1c9bc
# getter = None
# const = None
# payable = False
def unknown6ff1c9bc(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require caller == mcasinoAddress
  call m_param1 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x75619ab5
# getter = None
# const = None
# payable = False
def setDistributor(address m_distributor): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mdistributorAddress = m_distributor


# hash = 0x7892fd29
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def ROUND_TIME(): # not payable
  return mROUND_TIME


# hash = 0x7952ea9d
# getter = ['storage', 256, 0, 21]
# const = None
# payable = False
def unknown7952ea9d(): # not payable
  return munknown7952ea9d


# hash = 0x7e95b523
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def MAX_BET(): # not payable
  return mMAX_BET


# hash = 0x82bc07e6
# getter = None
# const = None
# payable = False
def lastRound(): # not payable
  return (mroundsm.length - 1)


# hash = 0x881eff1e
# getter = None
# const = None
# payable = False
def setMaxBet(uint256 m_newMaxBet): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mMAX_BET = m_newMaxBet
  log 0xaa2f425a: _newMaxBet


# hash = 0x88ea41b9
# getter = None
# const = None
# payable = False
def setMinBet(uint256 m_eth): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mMIN_BET = m_eth
  log 0x2668101b: _eth


# hash = 0x8984e2b4
# getter = None
# const = None
# payable = False
def unknown8984e2b4(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if not munknown6d1a4496:
      return mMIN_BET, mMAX_BET, munknownea6700e2, munknowndb85e2a0
  if m_param1 < 13:
      if m_param1 > 4:
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.ETH_TO_WEI() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not (3 * m_param1) - 5:
              return mMIN_BET, 0, munknownea6700e2, munknowndb85e2a0
          require (-5 * munknown326c25ad * ext_call.return_data[0]) + (3 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / (3 * m_param1) - 5 == munknown326c25ad * ext_call.return_data[0]
          return mMIN_BET, 
                 (-5 * munknown326c25ad * ext_call.return_data[0]) + (3 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / 100,
                 munknownea6700e2,
                 munknowndb85e2a0
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.ETH_TO_WEI() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if m_param1 < 46:
      if not (2 * m_param1) + 8:
          return mMIN_BET, 0, munknownea6700e2, munknowndb85e2a0
      require (8 * munknown326c25ad * ext_call.return_data[0]) + (2 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / (2 * m_param1) + 8 == munknown326c25ad * ext_call.return_data[0]
      return mMIN_BET, 
             (8 * munknown326c25ad * ext_call.return_data[0]) + (2 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / 100,
             munknownea6700e2,
             munknowndb85e2a0
  if m_param1 < 56:
      return mMIN_BET, munknown326c25ad * ext_call.return_data[0], munknownea6700e2, munknowndb85e2a0
  if not m_param1 - 55:
      require 100 * munknown326c25ad * ext_call.return_data[0] / 100 == munknown326c25ad * ext_call.return_data[0]
      return mMIN_BET, 100 * munknown326c25ad * ext_call.return_data[0] / 100, munknownea6700e2, munknowndb85e2a0
  require (5 * m_param1) - 275 / m_param1 - 55 == 5
  if not (5 * m_param1) - 175:
      return mMIN_BET, 0, munknownea6700e2, munknowndb85e2a0
  require (-175 * munknown326c25ad * ext_call.return_data[0]) + (5 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / (5 * m_param1) - 175 == munknown326c25ad * ext_call.return_data[0]
  return mMIN_BET, 
         (-175 * munknown326c25ad * ext_call.return_data[0]) + (5 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / 100,
         munknownea6700e2,
         munknowndb85e2a0


# hash = 0x8b706799
# getter = None
# const = None
# payable = False
def unknown8b706799(uint256 m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param1 <= 100
  if not mHOUSE_EDGE:
      require -m_param1 + 100 > 0
      require -m_param1 + 100
      if not m_param2:
          require m_param1 > 0
          require m_param1
          if not 0 / m_param1:
              return 0
          require (100000 * 0 / m_param1) - (0 / -m_param1 + 100 * 0 / m_param1) / 0 / m_param1 == -(0 / -m_param1 + 100) + 100000
          return ((100000 * 0 / m_param1) - (0 / -m_param1 + 100 * 0 / m_param1) / 100000)
      require (100 * m_param2) - (m_param1 * m_param2) / m_param2 == -m_param1 + 100
      require m_param1 > 0
      require m_param1
      if not (100 * m_param2) - (m_param1 * m_param2) / m_param1:
          return 0
      require (100000 * (100 * m_param2) - (m_param1 * m_param2) / m_param1) - (0 / -m_param1 + 100 * (100 * m_param2) - (m_param1 * m_param2) / m_param1) / (100 * m_param2) - (m_param1 * m_param2) / m_param1 == -(0 / -m_param1 + 100) + 100000
      return ((100000 * (100 * m_param2) - (m_param1 * m_param2) / m_param1) - (0 / -m_param1 + 100 * (100 * m_param2) - (m_param1 * m_param2) / m_param1) / 100000)
  require 100 * mHOUSE_EDGE / mHOUSE_EDGE == 100
  require -m_param1 + 100 > 0
  require -m_param1 + 100
  if not m_param2:
      require m_param1 > 0
      require m_param1
      if not 0 / m_param1:
          return 0
      require (100000 * 0 / m_param1) - (100 * mHOUSE_EDGE / -m_param1 + 100 * 0 / m_param1) / 0 / m_param1 == -(100 * mHOUSE_EDGE / -m_param1 + 100) + 100000
      return ((100000 * 0 / m_param1) - (100 * mHOUSE_EDGE / -m_param1 + 100 * 0 / m_param1) / 100000)
  require (100 * m_param2) - (m_param1 * m_param2) / m_param2 == -m_param1 + 100
  require m_param1 > 0
  require m_param1
  if not (100 * m_param2) - (m_param1 * m_param2) / m_param1:
      return 0
  require (100000 * (100 * m_param2) - (m_param1 * m_param2) / m_param1) - (100 * mHOUSE_EDGE / -m_param1 + 100 * (100 * m_param2) - (m_param1 * m_param2) / m_param1) / (100 * m_param2) - (m_param1 * m_param2) / m_param1 == -(100 * mHOUSE_EDGE / -m_param1 + 100) + 100000
  return ((100000 * (100 * m_param2) - (m_param1 * m_param2) / m_param1) - (100 * mHOUSE_EDGE / -m_param1 + 100 * (100 * m_param2) - (m_param1 * m_param2) / m_param1) / 100000)


# hash = 0x8c65c81f
# getter = ['struct', ['loc', 25]]
# const = None
# payable = False
def rounds(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < mroundsm.length
  require uint8(mroundsm[m_param1m]m.field_224) <= 2
  return Mask(224, 0, mroundsm[m_param1m]m.field_0), uint8(mroundsm[m_param1m]m.field_0), mroundsm[m_param1m]m.field_256


# hash = 0x8daaaa2f
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def HOUSE_EDGE(): # not payable
  return mHOUSE_EDGE


# hash = 0x93d1259f
# getter = None
# const = None
# payable = False
def unknown93d1259f(bool m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown6d1a4496 = uint8(m_param1)
  log 0xfd21a702: _param1


# hash = 0x9403e8dd
# getter = ['storage', 160, 0, 26]
# const = None
# payable = False
def casino(): # not payable
  return mcasinoAddress


# hash = 0x95b0f404
# getter = None
# const = None
# payable = False
def unknown95b0f404(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknownec11c49e = m_param1


# hash = 0x95e4d2ed
# getter = None
# const = None
# payable = False
def unknown95e4d2ed(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown178f9ebd = m_param1


# hash = 0xa8e14f65
# getter = None
# const = None
# payable = False
def unknowna8e14f65(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
  require uint64(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_144) < mroundsm.length
  require uint8(mroundsm[uint64(mstor24m[addr(m_param1)m]m[m_param2m]m.field_144)m]m.field_224) <= 2
  if uint8(mroundsm[uint64(mstor24m[addr(m_param1)m]m[m_param2m]m.field_144)m]m.field_224) != 2:
      return 0
  return 1


# hash = 0xb1fc8ad4
# getter = None
# const = None
# payable = False
def unknownb1fc8ad4(uint256 m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param1 <= 100
  if not mHOUSE_EDGE:
      require -m_param1 + 100 > 0
      require -m_param1 + 100
      if not m_param2:
          require m_param1 > 0
          require m_param1
          if not 0 / m_param1:
              return 0
          require 0 / -m_param1 + 100 * 0 / m_param1 / 0 / m_param1 == 0 / -m_param1 + 100
          return (0 / -m_param1 + 100 * 0 / m_param1 / 100000)
      require (100 * m_param2) - (m_param1 * m_param2) / m_param2 == -m_param1 + 100
      require m_param1 > 0
      require m_param1
      if not (100 * m_param2) - (m_param1 * m_param2) / m_param1:
          return 0
      require 0 / -m_param1 + 100 * (100 * m_param2) - (m_param1 * m_param2) / m_param1 / (100 * m_param2) - (m_param1 * m_param2) / m_param1 == 0 / -m_param1 + 100
      return (0 / -m_param1 + 100 * (100 * m_param2) - (m_param1 * m_param2) / m_param1 / 100000)
  require 100 * mHOUSE_EDGE / mHOUSE_EDGE == 100
  require -m_param1 + 100 > 0
  require -m_param1 + 100
  if not m_param2:
      require m_param1 > 0
      require m_param1
      if not 0 / m_param1:
          return 0
      require 100 * mHOUSE_EDGE / -m_param1 + 100 * 0 / m_param1 / 0 / m_param1 == 100 * mHOUSE_EDGE / -m_param1 + 100
      return (100 * mHOUSE_EDGE / -m_param1 + 100 * 0 / m_param1 / 100000)
  require (100 * m_param2) - (m_param1 * m_param2) / m_param2 == -m_param1 + 100
  require m_param1 > 0
  require m_param1
  if not (100 * m_param2) - (m_param1 * m_param2) / m_param1:
      return 0
  require 100 * mHOUSE_EDGE / -m_param1 + 100 * (100 * m_param2) - (m_param1 * m_param2) / m_param1 / (100 * m_param2) - (m_param1 * m_param2) / m_param1 == 100 * mHOUSE_EDGE / -m_param1 + 100
  return (100 * mHOUSE_EDGE / -m_param1 + 100 * (100 * m_param2) - (m_param1 * m_param2) / m_param1 / 100000)


# hash = 0xbd874dff
# getter = ['storage', 256, 0, 22]
# const = None
# payable = False
def unknownbd874dff(): # not payable
  return munknownbd874dff


# hash = 0xbefec197
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknownbefec197(): # not payable
  return munknownbefec197


# hash = 0xbfe10928
# getter = ['storage', 160, 0, 27]
# const = None
# payable = False
def distributor(): # not payable
  return mdistributorAddress


# hash = 0xc4ea0bcd
# getter = ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 23]]]
# const = None
# payable = False
def unknownc4ea0bcd(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require munknownc4ea0bcdm[m_param1m] <= 2
  return munknownc4ea0bcdm[m_param1m]


# hash = 0xdb85e2a0
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknowndb85e2a0(): # not payable
  return munknowndb85e2a0


# hash = 0xe06174e4
# getter = ['storage', 160, 0, 17]
# const = None
# payable = False
def settings(): # not payable
  return msettingsAddress


# hash = 0xe165c274
# getter = None
# const = None
# payable = False
def unknowne165c274(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if not munknown6d1a4496:
      return mMAX_BET
  if m_param1 < 13:
      if m_param1 > 4:
          require ext_code.size(msettingsAddress)
          static call msettingsAddress.ETH_TO_WEI() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not (3 * m_param1) - 5:
              return 0
          require (-5 * munknown326c25ad * ext_call.return_data[0]) + (3 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / (3 * m_param1) - 5 == munknown326c25ad * ext_call.return_data[0]
          return ((-5 * munknown326c25ad * ext_call.return_data[0]) + (3 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / 100)
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.ETH_TO_WEI() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if m_param1 < 46:
      if not (2 * m_param1) + 8:
          return 0
      require (8 * munknown326c25ad * ext_call.return_data[0]) + (2 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / (2 * m_param1) + 8 == munknown326c25ad * ext_call.return_data[0]
      return ((8 * munknown326c25ad * ext_call.return_data[0]) + (2 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / 100)
  if m_param1 < 56:
      return (munknown326c25ad * ext_call.return_data[0])
  if not m_param1 - 55:
      require 100 * munknown326c25ad * ext_call.return_data[0] / 100 == munknown326c25ad * ext_call.return_data[0]
      return (100 * munknown326c25ad * ext_call.return_data[0] / 100)
  require (5 * m_param1) - 275 / m_param1 - 55 == 5
  if not (5 * m_param1) - 175:
      return 0
  require (-175 * munknown326c25ad * ext_call.return_data[0]) + (5 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / (5 * m_param1) - 175 == munknown326c25ad * ext_call.return_data[0]
  return ((-175 * munknown326c25ad * ext_call.return_data[0]) + (5 * m_param1 * munknown326c25ad * ext_call.return_data[0]) / 100)


# hash = 0xe8967dbb
# getter = ['struct', ['loc', 24]]
# const = None
# payable = False
def unknowne8967dbb(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
  require uint8(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8) <= 4
  return uint128(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0), 
         bool(uint8(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216)),
         bool(uint8(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208)),
         bool(uint8(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_224))


# hash = 0xea6700e2
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknownea6700e2(): # not payable
  return munknownea6700e2


# hash = 0xec11c49e
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknownec11c49e(): # not payable
  return munknownec11c49e


# hash = 0xf25b7675
# getter = None
# const = None
# payable = False
def unknownf25b7675(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require munknown264be753m[addr(m_param1)m]m.field_0 - 1 < munknown264be753m[addr(m_param1)m]m.field_0
  require uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) <= 4
  require uint64(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) < mroundsm.length
  require uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) <= 4
  if uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) == 1:
      return mroundsm[2 * uint64(uint64(mstor24m[addr(m_param1)m]m[mstor24m[addr(m_param1)m]m.field_0m]m.field_0))m]m.field_256, 
             uint128(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0),
             uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0)
  require uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) <= 4
  if not uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0):
      return mroundsm[2 * uint64(uint64(mstor24m[addr(m_param1)m]m[mstor24m[addr(m_param1)m]m.field_0m]m.field_0))m]m.field_256, 
             uint128(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0),
             -uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) + 99
  require uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) <= 4
  if uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) == 2:
      return mroundsm[2 * uint64(uint64(mstor24m[addr(m_param1)m]m[mstor24m[addr(m_param1)m]m.field_0m]m.field_0))m]m.field_256, 
             uint128(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0),
             1
  require uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) <= 4
  if uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) == 3:
      if uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0):
          return mroundsm[2 * uint64(uint64(mstor24m[addr(m_param1)m]m[mstor24m[addr(m_param1)m]m.field_0m]m.field_0))m]m.field_256, 
                 uint128(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0),
                 50
      return mroundsm[2 * uint64(uint64(mstor24m[addr(m_param1)m]m[mstor24m[addr(m_param1)m]m.field_0m]m.field_0))m]m.field_256, 
             uint128(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0),
             49
  require uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) <= 4
  if uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) != 4:
      return mroundsm[2 * uint64(uint64(mstor24m[addr(m_param1)m]m[mstor24m[addr(m_param1)m]m.field_0m]m.field_0))m]m.field_256, 
             uint128(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0),
             0
  if uint8(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0) != 2:
      return mroundsm[2 * uint64(uint64(mstor24m[addr(m_param1)m]m[mstor24m[addr(m_param1)m]m.field_0m]m.field_0))m]m.field_256, 
             uint128(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0),
             45
  return mroundsm[2 * uint64(uint64(mstor24m[addr(m_param1)m]m[mstor24m[addr(m_param1)m]m.field_0m]m.field_0))m]m.field_256, 
         uint128(munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0),
         10


# hash = 0xfa65cb04
# getter = None
# const = None
# payable = False
def unknownfa65cb04(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mROUND_TIME = m_param1
  log 0x2a9e9292: _param1


# hash = 0xfd874762
# getter = None
# const = None
# payable = False
def unknownfd874762(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mcasinoAddress = m_param1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


