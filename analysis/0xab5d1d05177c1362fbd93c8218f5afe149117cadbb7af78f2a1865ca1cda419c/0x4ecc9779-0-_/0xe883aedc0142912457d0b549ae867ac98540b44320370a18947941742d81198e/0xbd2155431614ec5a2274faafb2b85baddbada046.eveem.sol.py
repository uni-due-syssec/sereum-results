# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xbD2155431614eC5a2274FaaFB2b85bAdDbADA046 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x13de5b49': 'unknown13de5b49(?)'} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    backupOwner # mask: a s
    # storage address 2
    unknown88b45046 # mask: a s
    # storage address 3
    unknownef95b90e # mask: a s
    # storage address 4
    unknownf51efd7a
    # storage address 5
    unknown585c5b83
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 10
    stor10 # mask: a s
    # storage address 11
    stor11 # mask: a s
    # storage address 12
    stor12 # mask: a s
    # storage address 13
    stor13 # mask: a s
    # storage address 14
    stor14 # mask: a s
    # storage address 15
    stor15 # mask: a s
    # storage address 16
    stor16 # mask: a s
    # storage address 17
    stor17 # mask: a s
    # storage address 18
    stor18 # mask: a s
    # storage address 19
    stor19 # mask: a s
    # storage address 20
    stor20 # mask: a s
    # storage address 21
    stor21 # mask: a s
    # storage address 22
    stor22 # mask: a s
    # storage address 23
    stor23 # mask: a s
    # storage address 24
    stor24 # mask: a s
    # storage address 25
    stor25 # mask: a s
    # storage address 26
    stor26 # mask: a s
    # storage address 27
    stor27 # mask: a s
    # storage address 28
    stor28 # mask: a s
    # storage address 29
    stor29 # mask: a s
    # storage address 30
    stor30 # mask: a s
    # storage address 31
    stor31 # mask: a s
    # storage address 32
    stor32 # mask: a s
    # storage address 33
    stor33 # mask: a s
    # storage address 34
    stor34 # mask: a s
    # storage address 35
    unknown3c2848ea
# hash = 0x030b7d87
# getter = None
# const = None
# payable = False
def unknown030b7d87(uint256 _param1, uint256 _param2): # not payable
  mem[208 len 0] = None
  mem[208] = mem[224 len 16]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[208 len 16]]:
      revert with 0, 'permission deny'
  stor31 = _param1
  stor32 = _param2


# hash = 0x06b9d635
# getter = None
# const = None
# payable = False
def unknown06b9d635(addr _param1, addr _param2, uint256 _param3): # not payable
  require ext_code.size(stor7)
  call stor7.0x4c577b95 with:
       gas gas_remaining wei
      args addr(_param1), _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if block.timestamp - ext_call.return_data[0] < stor32:
      revert with 0, 'can not less than 24 hours'
  require ext_code.size(stor7)
  call stor7.0xe4fed460 with:
       gas gas_remaining wei
      args addr(_param1), _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(stor7)
  call stor7.0x17ff16e2 with:
       gas gas_remaining wei
      args addr(_param1), _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _param3 > 0:
      revert with 0, 'draw excceed invest'
  return 1


# hash = 0x12065fe0
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const getBalance = eth.balance(this.address)


# hash = 0x1268b86e
# getter = None
# const = None
# payable = False
def unknown1268b86e(addr _param1, uint256 _param2): # not payable
  if _param2 > stor33:
      revert with 0, 'amt illgel'
  require ext_code.size(stor7)
  call stor7.0xefde7d9b with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if block.timestamp <= ext_call.return_data[0]:
      revert with 0, 'time limited'
  require ext_code.size(stor7)
  call stor7.0xefde7d9b with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if block.timestamp - ext_call.return_data[0] < 3600 * stor34:
      revert with 0, 'time limited'
  return 1


# hash = 0x169d8b77
# getter = None
# const = None
# payable = False
def unknown169d8b77(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5, uint256 _param6, uint256 _param7, uint256 _param8, uint256 _param9, uint256 _param10): # not payable
  mem[200 len 0] = None
  mem[200] = mem[208 len 8], uint64('setRatio'), mem[224 len 8]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[200 len 8]]:
      revert with 0, 'permission deny'
  stor10 = _param1
  stor11 = _param2
  stor12 = _param3
  stor13 = _param4
  stor14 = _param5
  stor15 = _param6
  stor16 = _param7
  stor17 = _param8
  stor18 = _param9
  stor19 = _param10


# hash = 0x1933c4f0
# getter = None
# const = None
# payable = False
def unknown1933c4f0(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4): # not payable
  mem[204 len 0] = None
  mem[204] = uint64('setWeekRatio'), mem[224 len 12]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[204 len 12]]:
      revert with 0, 'permission deny'
  stor27 = _param1
  stor28 = _param2
  stor29 = _param3
  stor30 = _param4


# hash = 0x1b71d0f2
# getter = None
# const = None
# payable = False
def unknown1b71d0f2(addr _param1, uint256 _param2): # not payable
  if owner != caller:
      revert with 0, 'you are not the owner'
  unknownf51efd7a[addr(_param1)] = _param2


# hash = 0x3291fa5f
# getter = None
# const = None
# payable = False
def unknown3291fa5f(array _param1, uint256 _param2): # not payable
  mem[128 len _param1.length] = _param1[all]
  if owner != caller:
      revert with 0, 'you are not the owner'
  mem[ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[ceil32(_param1.length) + floor32(_param1.length) + -(_param1.length % 32) + 192 len _param1.length % 32] = mem[floor32(_param1.length) + -(_param1.length % 32) + 160 len _param1.length % 32]
  mem[_param1.length + ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] = 256^(-(_param1.length % 32) + 32) - 1 and mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] or mem[ceil32(_param1.length) + floor32(_param1.length) + 160] and !(256^(-(_param1.length % 32) + 32) - 1)
  unknown585c5b83[call.data[_param1 + 36 len floor32(_param1.length)]][mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160 len _param1.length % 32]] = _param2


# hash = 0x3af8e4ab
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def backupOwner(): # not payable
  return backupOwner


# hash = 0x3c2848ea
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 35]]]]]
# const = None
# payable = False
def unknown3c2848ea(addr _param1, addr _param2): # not payable
  return unknown3c2848ea[_param1][_param2]


# hash = 0x3e74d449
# getter = None
# const = None
# payable = False
def unknown3e74d449(addr _param1, uint256 _param2): # not payable
  mem[202 len 0] = None
  mem[202] = mem[212 len 2], Mask(80, 0, 'tansferETH'), mem[224 len 10]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[202 len 10]]:
      revert with 0, 'permission deny'
  if _param2 > unknownef95b90e:
      revert with 0, 'single excceed'
  call _param1 with:
     value _param2 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x49464afe
# getter = None
# const = None
# payable = False
def unknown49464afe(uint256 _param1, addr _param2, addr _param3): # not payable
  mem[207 len 0] = None
  mem[207] = uint16('setInvestConfig'), mem[224 len 15]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[207 len 15]]:
      revert with 0, 'permission deny'
  stor6 = _param1
  stor7 = _param2
  stor9 = _param2
  stor8 = _param3


# hash = 0x56029aea
# getter = None
# const = None
# payable = False
def unknown56029aea(uint256 _param1): # not payable
  mem[212 len 0] = None
  mem[212] = mem[232 len 12]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[212 len 20]]:
      revert with 0, 'permission deny'
  unknownef95b90e = _param1


# hash = 0x585c5b83
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 5]]]
# const = None
# payable = False
def unknown585c5b83(uint256 _param1): # not payable
  return unknown585c5b83[_param1]


# hash = 0x64020558
# getter = None
# const = None
# payable = False
def unknown64020558(uint256 _param1, addr _param2): # not payable
  if owner != caller:
      revert with 0, 'you are not the owner'
  if _param1 != 201901261442:
      revert with 0, 'password is not right'
  [93mselfdestruct([91m_param2[93m)


# hash = 0x6e5de674
# getter = None
# const = None
# payable = False
def unknown6e5de674(addr _param1): # not payable
  if owner != caller:
      revert with 0, 'you are not the owner'
  owner = _param1


# hash = 0x78a1bf05
# getter = None
# const = None
# payable = False
def unknown78a1bf05(): # not payable
  return stor32, stor27, stor28, stor29, stor30, stor31


# hash = 0x85ab0dd7
# getter = None
# const = None
# payable = False
def unknown85ab0dd7(uint256 _param1): # not payable
  require ext_code.size(stor8)
  call stor8.0x85ab0dd7 with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[0], ext_call.return_data[32]


# hash = 0x88b45046
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def unknown88b45046(): # not payable
  return unknown88b45046


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8dbc5813
# getter = None
# const = None
# payable = False
def unknown8dbc5813(array _param1): # not payable
  mem[128 len _param1.length] = _param1[all]
  mem[ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[ceil32(_param1.length) + floor32(_param1.length) + -(_param1.length % 32) + 192 len _param1.length % 32] = mem[floor32(_param1.length) + -(_param1.length % 32) + 160 len _param1.length % 32]
  mem[_param1.length + ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] = 256^(-(_param1.length % 32) + 32) - 1 and mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] or mem[ceil32(_param1.length) + floor32(_param1.length) + 160] and !(256^(-(_param1.length % 32) + 32) - 1)
  mem[_param1.length + ceil32(_param1.length) + 160] = unknown585c5b83[call.data[_param1 + 36 len floor32(_param1.length)]][mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160 len _param1.length % 32]]
  return memory
    from _param1.length + ceil32(_param1.length) + 160
     [93mlen 32


# hash = 0x954785a5
# getter = None
# const = None
# payable = False
def unknown954785a5(uint256 _param1, uint256 _param2): # not payable
  mem[204 len 0] = None
  mem[204] = uint64('setContrDraw'), mem[224 len 12]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[204 len 12]]:
      revert with 0, 'permission deny'
  stor33 = _param1
  stor34 = _param2


# hash = 0xaa8ee3ae
# getter = None
# const = None
# payable = False
def unknownaa8ee3ae(addr _param1): # not payable
  if backupOwner != caller:
      revert with 0, 'you are not backupOwner'
  owner = _param1


# hash = 0xab4258e8
# getter = None
# const = None
# payable = False
def unknownab4258e8(bool _param1, uint256 _param2): # not payable
  mem[205 len 0] = None
  mem[205] = 'setReferLevel' % 281474976710656, mem[224 len 13]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[205 len 13]]:
      revert with 0, 'permission deny'
  stor25 = uint8(_param1)
  stor26 = _param2


# hash = 0xb1b57156
# getter = None
# const = None
# payable = False
def unknownb1b57156(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5): # not payable
  mem[201 len 0] = None
  mem[201] = mem[210 len 5], Mask(72, 0, 'setRatio2'), mem[224 len 9]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[201 len 9]]:
      revert with 0, 'permission deny'
  stor20 = _param1
  stor21 = _param2
  stor22 = _param3
  stor23 = _param4
  stor24 = _param5


# hash = 0xe67b6444
# getter = None
# const = None
# payable = False
def unknowne67b6444(addr _param1, addr _param2, uint256 _param3): # not payable
  mem[204 len 0] = None
  mem[204] = uint64('tansferERC20'), mem[224 len 12]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[204 len 12]]:
      revert with 0, 'permission deny'
  require ext_code.size(_param1)
  call _param1.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(_param2), _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0xef95b90e
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknownef95b90e(): # not payable
  return unknownef95b90e


# hash = 0xef98ffb5
# getter = None
# const = None
# payable = False
def unknownef98ffb5(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  require ext_code.size(stor9)
  call stor9.0x4bf5cb14 with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 96
  if _param2 > (2 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) + (7 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100 * stor30 / 10000) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100):
      revert with 0, 'amt is not right'
  require stor31
  if block.timestamp - ext_call.return_data[32] / stor31 < 7:
      revert with 0, 'nowday < 7'
  if block.timestamp - ext_call.return_data[32] / stor31 < 14:
      if ((-7 * stor28 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / stor31 * stor28 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) / 10000) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) < ext_call.return_data[64]:
          revert with 0, 'w2 safe check'
      if ((-7 * stor28 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / stor31 * stor28 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) / 10000) + ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) - ext_call.return_data[64] < _param2:
          revert with 0, 'w2 excceed'
      return _param2, 1, 0
  if block.timestamp - ext_call.return_data[32] / stor31 < 21:
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + ((-14 * stor29 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / stor31 * stor29 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) / 10000) < ext_call.return_data[64]:
          revert with 0, 'w3 safe check'
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + ((-14 * stor29 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / stor31 * stor29 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) / 10000) - ext_call.return_data[64] < _param2:
          revert with 0, 'w3 excceed'
      return _param2, 1, 0
  if block.timestamp - ext_call.return_data[32] / stor31 < 28:
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + ((50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) + ((-21 * stor30 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / stor31 * stor30 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) / 10000) < ext_call.return_data[64]:
          revert with 0, 'w4 safe check'
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + ((50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) + ((-21 * stor30 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) + (block.timestamp - ext_call.return_data[32] / stor31 * stor30 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) / 10000) - ext_call.return_data[64] < _param2:
          revert with 0, 'w4 excceed'
      return _param2, 1, 0
  if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + ((50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) + (7 * stor30 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100 / 10000) >= ext_call.return_data[64]:
      if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + ((50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) + (7 * stor30 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100 / 10000) - ext_call.return_data[64] >= _param2:
          return _param2, 1, 0
  if _param3 < ext_call.return_data[0]:
      revert with 0, 're-take amt wrong'
  if _param3 > stor6:
      revert with 0, 'maxPerInvest excceed'
  if ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (2 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) + (7 * stor30 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100 / 10000) < ext_call.return_data[64]:
      revert with 0, 'wo cao ,dont say impossible'
  return ((50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + ((50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (2 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100) + (7 * stor30 * (50 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100) + (50 * 7 * (50 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100) + (50 * 7 * (50 * ext_call.return_data[0]) + (50 * 7 * ext_call.return_data[0] * stor27 / 10000) / 100 * stor28 / 10000) / 100 * stor29 / 10000) / 100 / 10000) - ext_call.return_data[64], 
         0,
         1


# hash = 0xf51efd7a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = False
def unknownf51efd7a(addr _param1): # not payable
  return unknownf51efd7a[_param1]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


