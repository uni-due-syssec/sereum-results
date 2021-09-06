# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x047B05647249A576a1E44216B4747b9D327dC4f7 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x0c69794e': 'unknown0c69794e(?)', '0x254acc24': 'unknown254acc24(?)', '0x27dc297e': '__callback(bytes32 _myid, string _result)', '0xa8e0cd1c': 'unknowna8e0cd1c(?)', '0xac7a83de': 'unknownac7a83de(?)', '0xafa268c1': 'unknownafa268c1(?)', '0xafab5dd5': 'unknownafab5dd5(?)'} 

# storage definitions
def storage:
    # storage address 6
    userBalances
    # storage address 7
    unknown009c0198
    # storage address 8
    unknown46d1e91b
    # storage address 9
    unknown7d6bf618 # mask: a s
    # storage address 11
    settingsAddress # mask: a s
    # storage address 12
    distributorAddress # mask: a s
    # storage address 13
    unknown236e5e4c # mask: a s
    # storage address 14
    unknown0aefecb5 # mask: a s
    # storage address 15
    unknown610fe551 # mask: a s
    # storage address 16
    unknown7952ea9d # mask: a s
    # storage address 17
    unknownbd874dff # mask: a s
    # storage address 18
    unknown397425fb # mask: a s
    # storage address 19
    unknowne7ef3eb6 # mask: a s
    # storage address 20
    unknown8f722042
    # storage address 21
    unknown14c84f3a
    # storage address 22
    unknown224d2ede
    # storage address 23
    unknown97bbb5bc
    # storage address 24
    unknownc2853b66
    # storage address 25
    unknown264be753
    # storage address 26
    unknown0bc99288
    # storage address 27
    users
    # storage address 28
    unknown68e22c58
    # storage address 29
    unknown3685083d
    # storage address 30
    unknown55064bd3 # mask: a s
# hash = 0x009c0198
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def unknown009c0198(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown009c0198[_param1]


# hash = 0x00ce8e3e
# getter = None
# const = None
# payable = False
def getUsers(): # not payable
  if not users.length:
      mem[(32 * users.length) + 128] = 32
      mem[(32 * users.length) + 160] = users.length
      mem[(32 * users.length) + 192 len floor32(users.length)] = mem[128 len floor32(users.length)]
      return memory
        from (32 * users.length) + 128
         [93mlen (96 * users.length) + 64
  mem[128] = addr(users.field_0)
  [94midx = 128
  [94ms = 0
  while (32 * users.length) + 96 > [94midx:
      mem[[94midx + 32] = addr(users[[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * users.length) + 192 len floor32(users.length)] = mem[128 len floor32(users.length)]
  return Array(len=users.length, data=mem[128 len floor32(users.length)], mem[(32 * users.length) + floor32(users.length) + 192 len (32 * users.length) - floor32(users.length)]), 


# hash = 0x05815caa
# getter = None
# const = None
# payable = False
def unknown05815caa(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require caller == distributorAddress
  if _param2:
      require _param2 + userBalances[addr(_param1)] >= userBalances[addr(_param1)]
      userBalances[addr(_param1)] += _param2
      require _param2 + unknown7d6bf618 >= unknown7d6bf618
      unknown7d6bf618 += _param2
      require eth.balance(this.address) >= _param2 + unknown7d6bf618


# hash = 0x0aefecb5
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def unknown0aefecb5(): # not payable
  return unknown0aefecb5


# hash = 0x0bc99288
# getter = ['struct', ['loc', 26]]
# const = None
# payable = False
def unknown0bc99288(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return addr(unknown0bc99288[_param1].field_0), 
         addr(unknown0bc99288[_param1].field_256),
         unknown0bc99288[_param1].field_512,
         bool(uint8(unknown0bc99288[_param1].field_768)),
         bool(uint8(unknown0bc99288[_param1].field_776))


# hash = 0x14c84f3a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 21]]]
# const = None
# payable = False
def unknown14c84f3a(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown14c84f3a[_param1]


# hash = 0x19a3d89c
# getter = None
# const = None
# payable = False
def unknown19a3d89c(): # not payable
  mem[96] = 0
  mem[128] = 3 * 10^18
  mem[160] = 25 * 10^14 * 3600
  mem[192] = 5 * 10^15 * 3600
  mem[224] = 30 * 10^18
  mem[256] = 125 * 10^14 * 3600
  mem[288] = 175 * 10^14 * 3600
  mem[320] = 84 * 10^18
  mem[352] = 3 * 10^16 * 24 * 3600
  mem[384] = 375 * 10^14 * 24 * 3600
  mem[416] = 165 * 10^18
  mem[448] = 55 * 10^15 * 3600
  mem[480] = 65 * 10^15 * 3600
  mem[512] = 273 * 10^18
  mem[544] = 875 * 10^14 * 3600
  mem[576] = 10^17 * 3600
  mem[608] = 408 * 10^18
  mem[640] = 1275 * 10^14 * 24 * 3600
  mem[672] = 1425 * 10^14 * 24 * 3600
  mem[704] = 570 * 10^18
  mem[736] = 175 * 10^15 * 3600
  mem[768] = 1925 * 10^14 * 3600
  mem[800] = 759 * 10^18
  mem[832] = 23 * 10^16 * 3600
  mem[864] = 25 * 10^16 * 3600
  mem[896] = 975 * 10^18
  mem[928] = 8125 * 10^10 * 3600 * 24 * 3600
  mem[960] = 875 * 10^11 * 3600 * 24 * 3600
  mem[992] = 1218 * 10^18
  mem[1024] = 3625 * 10^14 * 3600
  mem[1056] = 3875 * 10^14 * 3600
  mem[1088] = 1488 * 10^18
  mem[1120] = 44 * 10^16 * 3600
  mem[1152] = 4675 * 10^14 * 3600
  mem[1184] = 1785 * 10^18
  mem[1216] = 525 * 10^15 * 24 * 3600
  mem[1248] = 555 * 10^15 * 24 * 3600
  mem[1280] = 2109 * 10^18
  mem[1312] = 6175 * 10^14 * 3600
  mem[1344] = 65 * 10^16 * 3600
  mem[1376] = 2460 * 10^18
  mem[1408] = 7175 * 10^14 * 3600
  mem[1440] = 7525 * 10^14 * 3600
  mem[1472] = 2838 * 10^18
  mem[1504] = 825 * 10^15 * 24 * 3600
  mem[1536] = 8625 * 10^14 * 24 * 3600
  mem[1568] = 3243 * 10^18
  mem[1600] = 94 * 10^16 * 3600
  mem[1632] = 98 * 10^16 * 3600
  mem[1664] = 3675 * 10^18
  mem[1696] = 10625 * 10^14 * 3600
  mem[1728] = 1105 * 10^15 * 3600
  mem[1760] = 4134 * 10^18
  mem[1792] = 33125 * 10^10 * 3600 * 24 * 3600
  mem[1824] = 34375 * 10^10 * 3600 * 24 * 3600
  mem[1856] = 4620 * 10^18
  mem[1888] = 133 * 10^16 * 3600
  mem[1920] = 13775 * 10^14 * 3600
  mem[1952] = 5133 * 10^18
  mem[1984] = 1475 * 10^15 * 3600
  mem[2016] = 1525 * 10^15 * 3600
  mem[2048] = 5673 * 10^18
  mem[2080] = 16275 * 10^14 * 24 * 3600
  mem[2112] = 168 * 10^16 * 24 * 3600
  mem[2144] = 6240 * 10^18
  mem[2176] = 17875 * 10^14 * 3600
  mem[2208] = 18425 * 10^14 * 3600
  mem[2240] = 6834 * 10^18
  mem[2272] = 1955 * 10^15 * 3600
  mem[2304] = 20125 * 10^14 * 3600
  mem[2336] = 7455 * 10^18
  mem[2368] = 213 * 10^16 * 24 * 3600
  mem[2400] = 219 * 10^16 * 24 * 3600
  mem[2432] = 8103 * 10^18
  mem[2464] = 23125 * 10^14 * 3600
  mem[2496] = 2375 * 10^15 * 3600
  mem[2528] = 8778 * 10^18
  mem[2560] = 25025 * 10^14 * 3600
  mem[2592] = 25675 * 10^14 * 3600
  mem[2624] = 9480 * 10^18
  mem[2656] = 75 * 10^13 * 24 * 3600 * 24 * 3600
  mem[2688] = 76875 * 10^10 * 24 * 3600 * 24 * 3600
  mem[2720] = 10209 * 10^18
  mem[2752] = 2905 * 10^15 * 3600
  mem[2784] = 2975 * 10^15 * 3600
  mem[2816] = 10965 * 10^18
  mem[2848] = 31175 * 10^14 * 3600
  mem[2880] = 319 * 10^16 * 3600
  mem[2912] = 11748 * 10^18
  mem[2944] = 33375 * 10^14 * 24 * 3600
  mem[2976] = 34125 * 10^14 * 24 * 3600
  mem[3008] = 12558 * 10^18
  mem[3040] = 3565 * 10^15 * 3600
  mem[3072] = 36425 * 10^14 * 3600
  mem[3104] = 13395 * 10^18
  mem[3136] = 38 * 10^17 * 3600
  mem[3168] = 388 * 10^16 * 3600
  mem[3200] = 14259 * 10^18
  mem[3232] = 40425 * 10^14 * 24 * 3600
  mem[3264] = 4125 * 10^15 * 24 * 3600
  mem[3296] = 15150 * 10^18
  unknown224d2ede.length = 101
  [94ms = 0
  [94midx = 96
  while 3328 > [94midx:
      Mask(80, 0, unknown224d2ede[[94ms].field_0) = mem[[94midx + 22 len 10]
      Mask(176, 0, unknown224d2ede[[94ms].field_80) = 0
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 101
  while unknown224d2ede.length > [94midx:
      unknown224d2ede[[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 


# hash = 0x1d0c9d61
# getter = None
# const = None
# payable = False
def unknown1d0c9d61(): # not payable
  mem[96] = 0
  mem[128] = 0
  mem[160] = 0
  mem[192] = 0
  mem[224] = 40
  mem[256] = 0
  mem[288] = 0
  mem[320] = 0
  mem[352] = 40
  mem[384] = 0
  mem[416] = 0
  mem[448] = 0
  mem[480] = 40
  mem[512] = 0
  mem[544] = 0
  mem[576] = 0
  mem[608] = 40
  mem[640] = 0
  mem[672] = 0
  mem[704] = 0
  mem[736] = 40
  mem[768] = 0
  mem[800] = 0
  mem[832] = 0
  mem[864] = 50
  mem[896] = 0
  mem[928] = 0
  mem[960] = 0
  mem[992] = 50
  mem[1024] = 0
  mem[1056] = 0
  mem[1088] = 0
  mem[1120] = 50
  mem[1152] = 0
  mem[1184] = 0
  mem[1216] = 0
  mem[1248] = 50
  mem[1280] = 0
  mem[1312] = 0
  mem[1344] = 0
  mem[1376] = 50
  mem[1408] = 0
  mem[1440] = 0
  mem[1472] = 0
  mem[1504] = 60
  mem[1536] = 0
  mem[1568] = 0
  mem[1600] = 0
  mem[1632] = 60
  mem[1664] = 0
  mem[1696] = 0
  mem[1728] = 0
  mem[1760] = 60
  mem[1792] = 0
  mem[1824] = 0
  mem[1856] = 0
  mem[1888] = 60
  mem[1920] = 0
  mem[1952] = 0
  mem[1984] = 0
  mem[2016] = 60
  mem[2048] = 0
  mem[2080] = 0
  mem[2112] = 0
  mem[2144] = 70
  mem[2176] = 0
  mem[2208] = 0
  mem[2240] = 0
  mem[2272] = 70
  mem[2304] = 0
  mem[2336] = 0
  mem[2368] = 0
  mem[2400] = 70
  mem[2432] = 0
  mem[2464] = 0
  mem[2496] = 0
  mem[2528] = 70
  mem[2560] = 0
  mem[2592] = 0
  mem[2624] = 0
  mem[2656] = 70
  mem[2688] = 0
  mem[2720] = 0
  mem[2752] = 0
  mem[2784] = 80
  mem[2816] = 0
  mem[2848] = 0
  mem[2880] = 0
  mem[2912] = 80
  mem[2944] = 0
  mem[2976] = 0
  mem[3008] = 0
  mem[3040] = 80
  mem[3072] = 0
  mem[3104] = 0
  mem[3136] = 0
  mem[3168] = 80
  mem[3200] = 0
  mem[3232] = 0
  mem[3264] = 0
  mem[3296] = 80
  unknownc2853b66.length = 101
  [94ms = 0
  [94midx = 96
  while 3328 > [94midx:
      uint8(unknownc2853b66[[94ms].field_0) = mem[[94midx + 31 len 1]
      Mask(248, 0, unknownc2853b66[[94ms].field_8) = 0
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 101
  while unknownc2853b66.length > [94midx:
      unknownc2853b66[[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 


# hash = 0x224d2ede
# getter = ['storage', 256, 0, ['add', ['sha3', 22], ['cd', 4]]]
# const = None
# payable = False
def unknown224d2ede(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < unknown224d2ede.length
  return unknown224d2ede[_param1].field_0


# hash = 0x236e5e4c
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknown236e5e4c(): # not payable
  return unknown236e5e4c


# hash = 0x26224c64
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def userBalances(address _param1): # not payable
  require calldata.size - 4 >= 32
  return userBalances[_param1]


# hash = 0x264be753
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 25]]]
# const = None
# payable = False
def unknown264be753(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown264be753[addr(_param1)].field_0


# hash = 0x33f707d1
# getter = None
# const = None
# payable = False
def ownerWithdraw(uint256 _amount): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require _amount <= eth.balance(this.address) - unknown7d6bf618
  require ext_code.size(this.address)
  static call this.address.0x55064bd3 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  call caller with:
     value _amount wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x365b98b2
# getter = ['storage', 160, 0, ['add', ['sha3', 27], ['cd', 4]]]
# const = None
# payable = False
def users(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < users.length
  return addr(users[_param1].field_0)


# hash = 0x3685083d
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 29]]]]]
# const = None
# payable = False
def unknown3685083d(addr _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  return unknown3685083d[_param1][_param2]


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


# hash = 0x397425fb
# getter = ['storage', 256, 0, 18]
# const = None
# payable = False
def unknown397425fb(): # not payable
  return unknown397425fb


# hash = 0x3c8bccd9
# getter = None
# const = None
# payable = False
def unknown3c8bccd9(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.HOUSE_EDGE() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      if _param1:
          require 50 * _param1 / _param1 == 50
          if 50 * _param1 / 50:
              require not 0 / 50 * _param1 / 50
              return 0
          else:
              return 0
      else:
          return 0
  require 100 * ext_call.return_data[0] / ext_call.return_data[0] == 100
  if not _param1:
      return 0
  require 50 * _param1 / _param1 == 50
  if not 50 * _param1 / 50:
      return 0
  require 100 * ext_call.return_data[0] / 50 * 50 * _param1 / 50 / 50 * _param1 / 50 == 100 * ext_call.return_data[0] / 50
  return (100 * ext_call.return_data[0] / 50 * 50 * _param1 / 50 / 100000)


# hash = 0x440277e8
# getter = None
# const = None
# payable = False
def unknown440277e8(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if not unknown264be753[addr(_param1)].field_0:
      return userBalances[addr(_param1)]
  require unknown68e22c58[addr(_param1)] < unknown264be753[addr(_param1)].field_0
  mem[64] = 224
  require ext_code.size(addr(unknown264be753[addr(_param1)][stor28[addr(_param1)]].field_0))
  static call addr(unknown264be753[addr(_param1)][stor28[addr(_param1)]].field_0).0xe8967dbb with:
          gas gas_remaining wei
         args addr(_param1), unknown264be753[addr(_param1)][stor28[addr(_param1)]].field_256
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 128
  if ext_call.return_data[32]:
      return userBalances[addr(_param1)]
  mem[0] = _param1
  mem[32] = 28
  [94midx = stor[sha3(mem[0 len 64])]
  [94ms = userBalances[addr(_param1)]
  while [94midx < unknown264be753[addr(_param1)].field_0:
      [94m_43 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_43] = 0
      mem[[94m_43 + 32] = 0
      mem[32] = 25
      require [94midx < unknown264be753[addr(_param1)].field_0
      mem[0] = sha3(addr(_param1), 25)
      [94m_48 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_48] = addr(unknown264be753[addr(_param1)][[94midx].field_0)
      mem[[94m_48 + 32] = unknown264be753[addr(_param1)][[94midx].field_256
      require ext_code.size(addr(unknown264be753[addr(_param1)][[94midx].field_0))
      static call addr(unknown264be753[addr(_param1)][[94midx].field_0).0xe8967dbb with:
              gas gas_remaining wei
             args addr(_param1), unknown264be753[addr(_param1)][[94midx].field_256
      mem[mem[64] len 128] = ext_call.return_data[0 len 128]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 128
      if ext_call.return_data[32]:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      mem[mem[64] + 4] = _param1
      mem[mem[64] + 36] = unknown264be753[addr(_param1)][[94midx].field_256
      require ext_code.size(addr(unknown264be753[addr(_param1)][[94midx].field_0))
      static call addr(unknown264be753[addr(_param1)][[94midx].field_0).0xee6892ed with:
              gas gas_remaining wei
             args addr(_param1), unknown264be753[addr(_param1)][[94midx].field_256
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = (2 * ext_call.return_data[0]) + [94ms
      continue 
  return [94ms


# hash = 0x46d1e91b
# getter = ['struct', ['loc', 8]]
# const = None
# payable = False
def unknown46d1e91b(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < unknown46d1e91b[_param1].field_0
  return unknown46d1e91b[_param1][_param2].field_0, unknown46d1e91b[_param1][_param2].field_256


# hash = 0x4a39ec90
# getter = ['struct', ['loc', 25]]
# const = None
# payable = False
def bets(address _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < unknown264be753[_param1].field_0
  return addr(unknown264be753[_param1][_param2].field_0), unknown264be753[_param1][_param2].field_256


# hash = 0x4fa8235b
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 8]]]
# const = None
# payable = False
def unknown4fa8235b(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown46d1e91b[addr(_param1)].field_0


# hash = 0x55064bd3
# getter = ['storage', 256, 0, 30]
# const = None
# payable = False
def unknown55064bd3(): # not payable
  return unknown55064bd3


# hash = 0x5a93cc8f
# getter = None
# const = None
# payable = True
def unknown5a93cc8f(addr _param1, uint256 _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(settingsAddress)
  static call settingsAddress.0x2a1e747e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if not _param2:
      return 0
  require _param2 + unknown009c0198[addr(_param1)] >= unknown009c0198[addr(_param1)]
  unknown009c0198[addr(_param1)] += _param2
  return 1


# hash = 0x610fe551
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknown610fe551(): # not payable
  return unknown610fe551


# hash = 0x68c6b11a
# getter = None
# const = None
# payable = False
def unknown68c6b11a(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xeeee2023 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require _param1 == tx.origin
  if userBalances[addr(_param1)] < _param2:
      return 0
  require _param2 <= userBalances[addr(_param1)]
  userBalances[addr(_param1)] -= _param2
  require _param2 <= unknown7d6bf618
  unknown7d6bf618 -= _param2
  return 1


# hash = 0x68e22c58
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 28]]]
# const = None
# payable = False
def unknown68e22c58(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown68e22c58[_param1]


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
  require not distributorAddress
  distributorAddress = _new


# hash = 0x7952ea9d
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknown7952ea9d(): # not payable
  return unknown7952ea9d


# hash = 0x7d6bf618
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknown7d6bf618(): # not payable
  return unknown7d6bf618


# hash = 0x888575d3
# getter = None
# const = None
# payable = False
def unknown888575d3(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xeeee2023 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown236e5e4c += _param1
  call caller with:
     value _param1 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x8f722042
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 20]]]
# const = None
# payable = False
def unknown8f722042(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown8f722042[_param1]


# hash = 0x97bbb5bc
# getter = ['storage', 256, 0, ['add', ['sha3', 23], ['cd', 4]]]
# const = None
# payable = False
def unknown97bbb5bc(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < unknown97bbb5bc.length
  return unknown97bbb5bc[_param1].field_0


# hash = 0xa51af4c5
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def distributorAddress(): # not payable
  return distributorAddress


# hash = 0xac53df0b
# getter = None
# const = None
# payable = False
def unknownac53df0b(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(settingsAddress)
  static call settingsAddress.HOUSE_EDGE() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      if not _param1:
          return 0
      require 50 * _param1 / _param1 == 50
      if not 50 * _param1 / 50:
          return 0
      require 100000 * 50 * _param1 / 50 / 50 * _param1 / 50 == 100000
      return (100000 * 50 * _param1 / 50 / 100000)
  require 100 * ext_call.return_data[0] / ext_call.return_data[0] == 100
  if not _param1:
      return 0
  require 50 * _param1 / _param1 == 50
  if not 50 * _param1 / 50:
      return 0
  require (100000 * 50 * _param1 / 50) - (100 * ext_call.return_data[0] / 50 * 50 * _param1 / 50) / 50 * _param1 / 50 == -(100 * ext_call.return_data[0] / 50) + 100000
  return ((100000 * 50 * _param1 / 50) - (100 * ext_call.return_data[0] / 50 * 50 * _param1 / 50) / 100000)


# hash = 0xb13f5bc3
# getter = None
# const = None
# payable = False
def unknownb13f5bc3(): # not payable
  mem[96] = 0
  mem[128] = 0
  mem[160] = 10^16
  mem[192] = 2 * 10^16
  mem[224] = 0
  mem[256] = 3 * 10^16
  mem[288] = 4 * 10^16
  mem[320] = 5 * 10^16
  mem[352] = 0
  mem[384] = 6 * 10^16
  mem[416] = 7 * 10^16
  mem[448] = 8 * 10^16
  mem[480] = 0
  mem[512] = 25 * 10^12 * 3600
  mem[544] = 10^17
  mem[576] = 11 * 10^16
  mem[608] = 0
  mem[640] = 12 * 10^16
  mem[672] = 13 * 10^16
  mem[704] = 14 * 10^16
  mem[736] = 0
  mem[768] = 15 * 10^16
  mem[800] = 16 * 10^16
  mem[832] = 17 * 10^16
  mem[864] = 0
  mem[896] = 5 * 10^13 * 3600
  mem[928] = 19 * 10^16
  mem[960] = 2 * 10^17
  mem[992] = 0
  mem[1024] = 21 * 10^16
  mem[1056] = 22 * 10^16
  mem[1088] = 23 * 10^16
  mem[1120] = 0
  mem[1152] = 24 * 10^16
  mem[1184] = 25 * 10^16
  mem[1216] = 26 * 10^16
  mem[1248] = 0
  mem[1280] = 75 * 10^12 * 24 * 3600
  mem[1312] = 28 * 10^16
  mem[1344] = 29 * 10^16
  mem[1376] = 0
  mem[1408] = 3 * 10^17
  mem[1440] = 31 * 10^16
  mem[1472] = 32 * 10^16
  mem[1504] = 0
  mem[1536] = 33 * 10^16
  mem[1568] = 34 * 10^16
  mem[1600] = 35 * 10^16
  mem[1632] = 0
  mem[1664] = 10^14 * 3600
  mem[1696] = 37 * 10^16
  mem[1728] = 38 * 10^16
  mem[1760] = 0
  mem[1792] = 39 * 10^16
  mem[1824] = 4 * 10^17
  mem[1856] = 41 * 10^16
  mem[1888] = 0
  mem[1920] = 42 * 10^16
  mem[1952] = 43 * 10^16
  mem[1984] = 44 * 10^16
  mem[2016] = 0
  mem[2048] = 125 * 10^12 * 3600
  mem[2080] = 46 * 10^16
  mem[2112] = 47 * 10^16
  mem[2144] = 0
  mem[2176] = 48 * 10^16
  mem[2208] = 49 * 10^16
  mem[2240] = 5 * 10^17
  mem[2272] = 0
  mem[2304] = 51 * 10^16
  mem[2336] = 52 * 10^16
  mem[2368] = 53 * 10^16
  mem[2400] = 0
  mem[2432] = 15 * 10^13 * 24 * 3600
  mem[2464] = 55 * 10^16
  mem[2496] = 56 * 10^16
  mem[2528] = 0
  mem[2560] = 57 * 10^16
  mem[2592] = 58 * 10^16
  mem[2624] = 59 * 10^16
  mem[2656] = 0
  mem[2688] = 6 * 10^17
  mem[2720] = 61 * 10^16
  mem[2752] = 62 * 10^16
  mem[2784] = 0
  mem[2816] = 175 * 10^12 * 3600
  mem[2848] = 64 * 10^16
  mem[2880] = 65 * 10^16
  mem[2912] = 0
  mem[2944] = 66 * 10^16
  mem[2976] = 67 * 10^16
  mem[3008] = 68 * 10^16
  mem[3040] = 0
  mem[3072] = 69 * 10^16
  mem[3104] = 7 * 10^17
  mem[3136] = 71 * 10^16
  mem[3168] = 0
  mem[3200] = 2 * 10^14 * 3600
  mem[3232] = 73 * 10^16
  mem[3264] = 74 * 10^16
  mem[3296] = 0
  unknown97bbb5bc.length = 101
  [94ms = 0
  [94midx = 96
  while 3328 > [94midx:
      uint64(unknown97bbb5bc[[94ms].field_0) = mem[[94midx + 24 len 8]
      Mask(192, 0, unknown97bbb5bc[[94ms].field_64) = 0
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 101
  while unknown97bbb5bc.length > [94midx:
      unknown97bbb5bc[[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 


# hash = 0xb7055719
# getter = None
# const = None
# payable = False
def unknownb7055719(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require unknown68e22c58[addr(_param1)] < unknown264be753[addr(_param1)].field_0
  require ext_code.size(addr(unknown264be753[addr(_param1)][stor28[addr(_param1)]].field_0))
  static call addr(unknown264be753[addr(_param1)][stor28[addr(_param1)]].field_0).0xe8967dbb with:
          gas gas_remaining wei
         args addr(_param1), unknown264be753[addr(_param1)][stor28[addr(_param1)]].field_256
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 128
  return not bool(ext_call.return_data[32])


# hash = 0xbd874dff
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknownbd874dff(): # not payable
  return unknownbd874dff


# hash = 0xc2853b66
# getter = ['storage', 256, 0, ['add', ['sha3', 24], ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 21]]]]]
# const = None
# payable = False
def unknownc2853b66(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require unknown14c84f3a[addr(_param1)] < unknownc2853b66.length
  return unknownc2853b66[stor21[addr(_param1)]].field_0


# hash = 0xc63e0c05
# getter = None
# const = None
# payable = False
def unknownc63e0c05(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require caller == distributorAddress
  unknown397425fb = _param1


# hash = 0xdc29f1de
# getter = None
# const = None
# payable = True
def topUp() payable: 
  require call.value + userBalances[caller] >= userBalances[caller]
  userBalances[caller] += call.value
  require call.value + unknown7d6bf618 >= unknown7d6bf618
  unknown7d6bf618 += call.value


# hash = 0xe06174e4
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def settings(): # not payable
  return settingsAddress


# hash = 0xe2c2f4ac
# getter = ['storage', 256, 0, ['add', ['sha3', 24], ['cd', 4]]]
# const = None
# payable = False
def unknowne2c2f4ac(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < unknownc2853b66.length
  return unknownc2853b66[_param1].field_0


# hash = 0xe7ef3eb6
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def unknowne7ef3eb6(): # not payable
  return unknowne7ef3eb6


# hash = 0xf3fef3a3
# getter = None
# const = None
# payable = False
def withdraw(address _to, uint256 _value): # not payable
  require calldata.size - 4 >= 64
  if _to != caller:
      require ext_code.size(settingsAddress)
      static call settingsAddress.0xeeee2023 with:
              gas gas_remaining wei
             args caller
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
  require ext_code.size(this.address)
  call this.address.0xa8e0cd1c with:
       gas gas_remaining wei
      args _to
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require _value <= userBalances[addr(_to)]
  userBalances[addr(_to)] -= _value
  require _value <= unknown7d6bf618
  unknown7d6bf618 -= _value
  unknown46d1e91b[addr(_to)].field_0++
  unknown46d1e91b[addr(_to)][unknown46d1e91b[addr(_to)].field_0].field_0 = block.timestamp
  unknown46d1e91b[addr(_to)][unknown46d1e91b[addr(_to)].field_0].field_256 = _value
  call _to with:
     value _value wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0xc7c8ab30: _to, block.timestamp


# hash = 0xf5d82b6b
# getter = None
# const = None
# payable = True
def add(address _receiver, uint256 _equivalentEthAmount) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xeeee2023 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if not _equivalentEthAmount:
      return 0
  require _equivalentEthAmount + userBalances[addr(_receiver)] >= userBalances[addr(_receiver)]
  userBalances[addr(_receiver)] += _equivalentEthAmount
  require _equivalentEthAmount + unknown7d6bf618 >= unknown7d6bf618
  unknown7d6bf618 += _equivalentEthAmount
  require eth.balance(this.address) >= _equivalentEthAmount + unknown7d6bf618
  return 1


# hash = 0xfb624554
# getter = None
# const = None
# payable = False
def unknownfb624554(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(settingsAddress)
  static call settingsAddress.0xeeee2023 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require _param1 == tx.origin
  if unknown009c0198[addr(_param1)] < _param2:
      return 0
  require _param2 <= unknown009c0198[addr(_param1)]
  unknown009c0198[addr(_param1)] -= _param2
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require not unknown397425fb
  unknownbd874dff += call.value


