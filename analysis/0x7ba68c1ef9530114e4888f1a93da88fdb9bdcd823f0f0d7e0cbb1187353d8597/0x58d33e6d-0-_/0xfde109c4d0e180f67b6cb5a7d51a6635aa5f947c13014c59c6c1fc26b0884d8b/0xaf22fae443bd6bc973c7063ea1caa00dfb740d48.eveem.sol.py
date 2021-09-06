# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xAf22fae443bd6BC973c7063EA1Caa00Dfb740D48 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x27dc297e': '__callback(bytes32 _myid, string _result)', '0x58d33e6d': 'unknown58d33e6d(?)', '0x780b9dca': 'unknown780b9dca(?)', '0xa75c2603': 'unknowna75c2603(?)', '0xe105e7eb': 'unknowne105e7eb(?)'} 

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
    stor18 # mask: a s
    # storage address 18
    unknown6d1a4496 # mask: a s
    # storage address 18
    unknown0f055139 # mask: a s
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
  return munknown0aefecb5


# hash = 0x0f055139
# getter = ['bool', ['storage', 8, 8, 18]]
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
# getter = ['storage', 256, 0, 20]
# const = None
# payable = False
def unknown178f9ebd(): # not payable
  return munknown178f9ebd


# hash = 0x1ce314cd
# getter = None
# const = None
# payable = False
def unknown1ce314cd(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown46228a93m[2m] = m_param1
  munknown4907a660 = m_param1
  log 0xfec588ee: 2, _param1


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
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 29]]]
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
  mstor18 = Mask(248, 0, m_param1)
  log 0x77db83c1: not _param1


# hash = 0x2e4bda25
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknown2e4bda25(): # not payable
  return munknown2e4bda25


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


# hash = 0x307320b5
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknown307320b5(): # not payable
  return munknown307320b5


# hash = 0x326c25ad
# getter = ['storage', 256, 0, 7]
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
# getter = ['storage', 256, 0, 6]
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


# hash = 0x46228a93
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = False
def unknown46228a93(uint8 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown46228a93m[m_param1m]


# hash = 0x4907a660
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknown4907a660(): # not payable
  return munknown4907a660


# hash = 0x4a39ec90
# getter = ['struct', ['loc', 29]]
# const = None
# payable = False
def bets(address m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 < munknown264be753m[m_param1m]m.field_0
  require munknown264be753m[m_param1m]m[m_param2m]m.field_0 <= 5
  return munknown264be753m[m_param1m]m[m_param2m]m.field_0, 
         munknown264be753m[m_param1m]m[m_param2m]m.field_0,
         munknown264be753m[m_param1m]m[m_param2m]m.field_0,
         bool(munknown264be753m[m_param1m]m[m_param2m]m.field_200),
         bool(munknown264be753m[m_param1m]m[m_param2m]m.field_208),
         bool(munknown264be753m[m_param1m]m[m_param2m]m.field_216)


# hash = 0x63c587ba
# getter = None
# const = None
# payable = False
def unknown63c587ba(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknownf91ea562 = m_param1


# hash = 0x6540742f
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def MIN_BET(): # not payable
  return mMIN_BET


# hash = 0x67988182
# getter = None
# const = None
# payable = False
def unknown67988182(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require caller == mcasinoAddress
  require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
  require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
  if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 == 5:
      require ext_code.size(mdistributorAddress)
      static call mdistributorAddress.0x65e86f0c with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(mdistributorAddress)
      call mdistributorAddress.sendTokens(address to, uint256 amount) with:
           gas gas_remaining wei
          args addr(m_param1), ext_call.return_data[0] * munknownf91ea562 / 100
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != 1:
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
      if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != 2:
          require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
          if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != 3:
              require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
  mem[836 len 0] = None
  mem[900 len 0] = None
  require ext_code.size(mdistributorAddress)
  static call mdistributorAddress.0x1cdb3a4e with:
          gas gas_remaining wei
         args addr(this.address), mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_256, addr(m_param1), 192, 256, 1, 1, mem[836], 1, mem[900]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      require ext_code.size(mdistributorAddress)
      call mdistributorAddress.0x289ef3 with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 == 1:
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 <= 2
      if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 != 2:
          require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
          if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
              require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
              munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
          return 0
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
      require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
      if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0:
          if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
              require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
              munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
          return 0
      if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8:
          require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_200 = 1
          require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
          return munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0, 2 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
      if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
          require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
          munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
      munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
      return munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0, 0
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 == 2:
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 <= 2
      if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 != 2:
          require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
          if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
              require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
              munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
          return 0
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
      require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
      if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0:
          if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
              require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
              munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
          return 0
      if 3 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8:
          require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_200 = 1
          require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
          return 3 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8, 4 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
      if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
          require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
          munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
      munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
      return 3 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8, 0
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 == 3:
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 <= 2
      if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 != 2:
          require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
          if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
              require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
              munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
          return 0
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
      require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
      if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0:
          if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
              require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
              munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
          return 0
      if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8:
          require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_200 = 1
          require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
          munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
          return munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 << 128, 
                 munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + (4 * uint128(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8))
      if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
          require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
          munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
      munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
      return munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 << 128, 0
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
  require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 <= 2
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != 4:
      if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 == 2:
          require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
          require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
      require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
      if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
          require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
          munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
      munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
      return 0
  if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 != 2:
      require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
      if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
          require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
          munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
      munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
      return 0
  require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0:
      if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
          require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
          munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
      munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
      return 0
  if 19 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8:
      require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
      munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_200 = 1
      require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
      munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
      return 19 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8, 20 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
  if not munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216:
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8 + munknown7952ea9d >= munknown7952ea9d
      munknown7952ea9d += munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8
  munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208 = 1
  return 19 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8, 0


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


# hash = 0x6d1a4496
# getter = ['bool', ['storage', 8, 0, 18]]
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


# hash = 0x7142451c
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def unknown7142451c(): # not payable
  return munknown7142451c


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
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def ROUND_TIME(): # not payable
  return mROUND_TIME


# hash = 0x7952ea9d
# getter = ['storage', 256, 0, 26]
# const = None
# payable = False
def unknown7952ea9d(): # not payable
  return munknown7952ea9d


# hash = 0x79c4d445
# getter = None
# const = None
# payable = False
def unknown79c4d445(uint8 m_param1): # not payable
  require calldata.size - 4 >= 32
  if not munknown6d1a4496:
      require m_param1 <= 5
      return munknown46228a93m[m_param1 << 248m]
  require m_param1 <= 5
  if m_param1 == 1:
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return (munknown326c25ad * ext_call.return_data[0])
  require m_param1 <= 5
  if m_param1 == 2:
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return (50 * munknown326c25ad * ext_call.return_data[0] / 100)
  require m_param1 <= 5
  if m_param1 == 3:
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return (40 * munknown326c25ad * ext_call.return_data[0] / 100)
  require m_param1 <= 5
  if m_param1 != 4:
      return 0
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.ETH_TO_WEI() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return (10 * munknown326c25ad * ext_call.return_data[0] / 100)


# hash = 0x80057b9a
# getter = None
# const = None
# payable = False
def getColor(uint256 m_id): # not payable
  require calldata.size - 4 >= 32
  if m_id < 20:
      return 1
  if m_id < 30:
      return 2
  if m_id < 38:
      return 3
  if m_id < 40:
      return 4
  if m_id >= 42:
      return 0
  return 5


# hash = 0x82bc07e6
# getter = ['storage', 64, 0, 24]
# const = None
# payable = False
def lastRound(): # not payable
  return mlastRound


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
  if 4760 == m_param1:
      if not munknown6d1a4496:
          return mMIN_BET, munknown46228a93m[1m], munknownea6700e2, munknowndb85e2a0
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return mMIN_BET, munknown326c25ad * ext_call.return_data[0], munknownea6700e2, munknowndb85e2a0
  if 2380 == m_param1:
      if not munknown6d1a4496:
          return mMIN_BET, munknown46228a93m[2m], munknownea6700e2, munknowndb85e2a0
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return mMIN_BET, 50 * munknown326c25ad * ext_call.return_data[0] / 100, munknownea6700e2, munknowndb85e2a0
  if 1904 == m_param1:
      if not munknown6d1a4496:
          return mMIN_BET, munknown46228a93m[3m], munknownea6700e2, munknowndb85e2a0
      require ext_code.size(msettingsAddress)
      static call msettingsAddress.ETH_TO_WEI() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return mMIN_BET, 40 * munknown326c25ad * ext_call.return_data[0] / 100, munknownea6700e2, munknowndb85e2a0
  if m_param1 != 476:
      if not munknown6d1a4496:
          return mMIN_BET, munknown46228a93m[5m], munknownea6700e2, munknowndb85e2a0
      return mMIN_BET, 0, munknownea6700e2, munknowndb85e2a0
  if not munknown6d1a4496:
      return mMIN_BET, munknown46228a93m[4m], munknownea6700e2, munknowndb85e2a0
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.ETH_TO_WEI() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return mMIN_BET, 10 * munknown326c25ad * ext_call.return_data[0] / 100, munknownea6700e2, munknowndb85e2a0


# hash = 0x8a6b114b
# getter = None
# const = None
# payable = False
def getBet(address m_player, uint256 m_game): # not payable
  require calldata.size - 4 >= 64
  require m_game < munknown264be753m[addr(m_player)m]m.field_0
  require munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5
  require munknown264be753m[addr(m_player)m]m[m_gamem]m.field_136 < mroundsm.length
  require m_game < munknown264be753m[addr(m_player)m]m.field_0
  require munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5
  require munknown264be753m[addr(m_player)m]m[m_gamem]m.field_136 < mroundsm.length
  require munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5
  if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 == 1:
      if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_136 < mroundsm.length:
          if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_8 <= 2:
              if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_8 != 2:
                  if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                      if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                          return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                 munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                 munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                 mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                 0
              else:
                  if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                      if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                          if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0:
                              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                  if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                      return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                             munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                             munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                             mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                             0
                          else:
                              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                  if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                      return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                             munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                             munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                             mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                             munknown264be753m[addr(m_player)m]m[m_gamem]m.field_8 > 0
  else:
      if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
          if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 == 2:
              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_136 < mroundsm.length:
                  if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_8 <= 2:
                      if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_8 != 2:
                          if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                              if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                  return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                         munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                         munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                         mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                         0
                      else:
                          if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                  if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0:
                                      if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                          if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                              return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                                     munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                     munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                     mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                                     0
                                  else:
                                      if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                          if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                              return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                                     munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                     munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                     mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                                     3 * munknown264be753m[addr(m_player)m]m[m_gamem]m.field_8 > 0
          else:
              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                  if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 == 3:
                      if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_136 < mroundsm.length:
                          if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_8 <= 2:
                              if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_8 != 2:
                                  if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                      if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                          return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                                 munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                 munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                 mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                                 0
                              else:
                                  if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                      if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                          if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0:
                                              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                                  if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                                      return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                                             munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                             munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                             mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                                             0
                                          else:
                                              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                                  if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                                      return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                                             munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                             munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                             mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                                             4 * uint128(munknown264be753m[addr(m_player)m]m[m_gamem]m.field_8) > 0
                  else:
                      if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                          if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 != 4:
                              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_136 < mroundsm.length:
                                  if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_8 <= 2:
                                      if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_8 != 2:
                                          if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                              if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                                  return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                                         munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                         munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                         mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                                         0
                                      else:
                                          if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                                  if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                                      if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                                          return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                                                 munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                                 munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                                 mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                                                 0
                          else:
                              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_136 < mroundsm.length:
                                  if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_8 <= 2:
                                      if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_8 != 2:
                                          if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                              if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                                  return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                                         munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                         munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                         mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                                         0
                                      else:
                                          if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                              if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                                  if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0:
                                                      if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                                          if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                                              return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                                                     munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                                     munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                                     mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                                                     0
                                                  else:
                                                      if munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0 <= 5:
                                                          if mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0 <= 5:
                                                              return munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0, 
                                                                     munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                                     munknown264be753m[addr(m_player)m]m[m_gamem]m.field_0,
                                                                     mroundsm[2 * uint64(mstor29m[addr(m_player)m]m[m_gamem]m.field_136)m]m.field_0,
                                                                     19 * munknown264be753m[addr(m_player)m]m[m_gamem]m.field_8 > 0
  revert


# hash = 0x8b706799
# getter = None
# const = None
# payable = False
def unknown8b706799(uint256 m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  if 50 == m_param1:
      return m_param2
  if 4760 == m_param1:
      return m_param2
  if 2380 == m_param1:
      return (3 * m_param2)
  if 1904 == m_param1:
      return (4 * m_param2)
  if m_param1 != 476:
      return 0
  return (19 * m_param2)


# hash = 0x8c65c81f
# getter = ['struct', ['loc', 30]]
# const = None
# payable = False
def rounds(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < mroundsm.length
  require mroundsm[m_param1m]m.field_0 <= 5
  require mroundsm[m_param1m]m.field_8 <= 2
  return mroundsm[m_param1m]m.field_0, mroundsm[m_param1m]m.field_0, mroundsm[m_param1m]m.field_256


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
# getter = ['storage', 160, 0, 31]
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


# hash = 0x986ad946
# getter = None
# const = None
# payable = False
def unknown986ad946(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if 4760 == m_param1:
      return 1
  if 2380 == m_param1:
      return 2
  if 1904 == m_param1:
      return 3
  if m_param1 != 476:
      return 5
  return 4


# hash = 0xa80c74bf
# getter = None
# const = None
# payable = False
def unknowna80c74bf(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown46228a93m[4m] = m_param1
  munknown307320b5 = m_param1
  log 0xfec588ee: 4, _param1


# hash = 0xa8e14f65
# getter = None
# const = None
# payable = False
def unknowna8e14f65(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
  require mroundsm[mstor29m[addr(m_param1)m]m[m_param2m]m.field_136m]m.field_8 <= 2
  if mroundsm[mstor29m[addr(m_param1)m]m[m_param2m]m.field_136m]m.field_8 != 2:
      return 0
  return 1


# hash = 0xb2a8325e
# getter = None
# const = None
# payable = False
def unknownb2a8325e(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown46228a93m[3m] = m_param1
  munknown2e4bda25 = m_param1
  log 0xfec588ee: 3, _param1


# hash = 0xbd874dff
# getter = ['storage', 256, 0, 27]
# const = None
# payable = False
def unknownbd874dff(): # not payable
  return munknownbd874dff


# hash = 0xbefec197
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknownbefec197(): # not payable
  return munknownbefec197


# hash = 0xbfe10928
# getter = ['storage', 160, 0, 32]
# const = None
# payable = False
def distributor(): # not payable
  return mdistributorAddress


# hash = 0xc4ea0bcd
# getter = ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 28]]]
# const = None
# payable = False
def unknownc4ea0bcd(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require munknownc4ea0bcdm[m_param1m] <= 2
  return munknownc4ea0bcdm[m_param1m]


# hash = 0xc9f60c62
# getter = None
# const = None
# payable = False
def unknownc9f60c62(uint8 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 <= 5
  if m_param1 == 1:
      return 4760
  require m_param1 <= 5
  if m_param1 == 2:
      return 2380
  require m_param1 <= 5
  if m_param1 == 3:
      return 1904
  require m_param1 <= 5
  if m_param1 != 4:
      return 0
  return 476


# hash = 0xdb85e2a0
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def unknowndb85e2a0(): # not payable
  return munknowndb85e2a0


# hash = 0xe06174e4
# getter = ['storage', 160, 0, 21]
# const = None
# payable = False
def settings(): # not payable
  return msettingsAddress


# hash = 0xe8967dbb
# getter = ['struct', ['loc', 29]]
# const = None
# payable = False
def unknowne8967dbb(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  return munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0, 
         bool(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_208),
         bool(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_200),
         bool(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_216)


# hash = 0xe929a58b
# getter = None
# const = None
# payable = False
def unknowne929a58b(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(msettingsAddress)
  static call msettingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown46228a93m[1m] = m_param1
  munknown7142451c = m_param1
  log 0xfec588ee: 1, _param1


# hash = 0xea6700e2
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknownea6700e2(): # not payable
  return munknownea6700e2


# hash = 0xec11c49e
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def unknownec11c49e(): # not payable
  return munknownec11c49e


# hash = 0xee6892ed
# getter = None
# const = None
# payable = False
def unknownee6892ed(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 < munknown264be753m[addr(m_param1)m]m.field_0
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 == 1:
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 <= 2
      if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 != 2:
          return 0
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
      if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0:
          return 0
      return munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 == 2:
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 <= 2
      if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 != 2:
          return 0
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
      if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0:
          return 0
      return (3 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0)
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 == 3:
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 <= 2
      if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 != 2:
          return 0
      require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
      require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
      if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0:
          return 0
      return (4 * uint128(munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_8))
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_136 < mroundsm.length
  require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 <= 2
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != 4:
      if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 == 2:
          require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
          require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
          return 0
      else:
          return 0
  if mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_8 != 2:
      return 0
  require mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0 <= 5
  require munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0 != mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[m_param2m]m.field_136)m]m.field_0:
      return 0
  return (19 * munknown264be753m[addr(m_param1)m]m[m_param2m]m.field_0)


# hash = 0xf25b7675
# getter = None
# const = None
# payable = False
def unknownf25b7675(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require munknown264be753m[addr(m_param1)m]m.field_0 - 1 < munknown264be753m[addr(m_param1)m]m.field_0
  require munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0 <= 5
  require munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0 < mroundsm.length
  require munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0 == 1:
      return mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[mstor29m[addr(m_param1)m]m.field_0m]m.field_0)m]m.field_256, 
             munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0,
             4760
  require munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0 == 2:
      return mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[mstor29m[addr(m_param1)m]m.field_0m]m.field_0)m]m.field_256, 
             munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0,
             2380
  require munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0 == 3:
      return mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[mstor29m[addr(m_param1)m]m.field_0m]m.field_0)m]m.field_256, 
             munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0,
             1904
  require munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0 <= 5
  if munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0 != 4:
      return mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[mstor29m[addr(m_param1)m]m.field_0m]m.field_0)m]m.field_256, 
             munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0,
             0
  return mroundsm[2 * uint64(mstor29m[addr(m_param1)m]m[mstor29m[addr(m_param1)m]m.field_0m]m.field_0)m]m.field_256, 
         munknown264be753m[addr(m_param1)m]m[munknown264be753m[addr(m_param1)m]m.field_0m]m.field_0,
         476


# hash = 0xf91ea562
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknownf91ea562(): # not payable
  return munknownf91ea562


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


