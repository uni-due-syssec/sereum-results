# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x9235F45DCBC87a8aacD687aE0D6641F672A808A8 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x9dddd51d': 'unknown9dddd51d(?)'} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    unknown1f11cb48
    # storage address 2
    unknown60bb4cbf
    # storage address 3
    stor3
    # storage address 4
    unknowndb5a4e99
    # storage address 5
    unknownc519b54b # mask: a s
    # storage address 5
    unknowne3b1e2fe # mask: a s
    # storage address 5
    unknownf887b097 # mask: a s
    # storage address 99
    stor99
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037084
    stor87903029871075914254377627908054574944891091886930582284385770809450030037084
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037085
    stor87903029871075914254377627908054574944891091886930582284385770809450030037085
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037086
    stor87903029871075914254377627908054574944891091886930582284385770809450030037086
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037087
    stor87903029871075914254377627908054574944891091886930582284385770809450030037087
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037088
    stor87903029871075914254377627908054574944891091886930582284385770809450030037088
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037089
    stor87903029871075914254377627908054574944891091886930582284385770809450030037089
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037090
    stor87903029871075914254377627908054574944891091886930582284385770809450030037090
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037091
    stor87903029871075914254377627908054574944891091886930582284385770809450030037091
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037092
    stor87903029871075914254377627908054574944891091886930582284385770809450030037092
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037093
    stor87903029871075914254377627908054574944891091886930582284385770809450030037093
# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address _newOwner): # not payable
  if owner != caller:
      revert with 0, '1'
  owner = _newOwner


# hash = 0x1635717c
# getter = None
# const = None
# payable = False
def unknown1635717c(): # not payable
  if not unknowndb5a4e99.length:
      mem[(32 * unknowndb5a4e99.length) + 128] = unknowndb5a4e99.length
  else:
      mem[128 len 32 * unknowndb5a4e99.length] = code.data[9315 len 32 * unknowndb5a4e99.length]
      mem[(32 * unknowndb5a4e99.length) + 128] = unknowndb5a4e99.length
      mem[(32 * unknowndb5a4e99.length) + 160 len 32 * unknowndb5a4e99.length] = code.data[9315 len 32 * unknowndb5a4e99.length]
  [94midx = 0
  while [94midx < unknowndb5a4e99.length:
      require [94midx < unknowndb5a4e99.length
      mem[(32 * [94midx) + 128] = unknowndb5a4e99[[94midx]
      require [94midx < unknowndb5a4e99.length
      if 0 >= unknown1f11cb48[stor4[[94midx]].field_2304:
          revert with 0, '25'
      mem[0] = unknowndb5a4e99[[94midx]
      mem[32] = 1
      require [94midx < mem[(32 * unknowndb5a4e99.length) + 128]
      mem[(32 * unknowndb5a4e99.length) + (32 * [94midx) + 160] = unknown1f11cb48[stor4[[94midx]].field_2560
      [94midx = [94midx + 1
      continue 
  mem[(64 * unknowndb5a4e99.length) + 160] = 64
  mem[(64 * unknowndb5a4e99.length) + 224] = unknowndb5a4e99.length
  mem[(64 * unknowndb5a4e99.length) + 256 len floor32(unknowndb5a4e99.length)] = mem[128 len floor32(unknowndb5a4e99.length)]
  mem[(64 * unknowndb5a4e99.length) + 192] = (32 * unknowndb5a4e99.length) + 96
  mem[(98 * unknowndb5a4e99.length) + 256] = mem[(32 * unknowndb5a4e99.length) + 128]
  [94ms = 0
  while unknowndb5a4e99.length < 32 * mem[(32 * unknowndb5a4e99.length) + 128]:
      mem[(99 * unknowndb5a4e99.length) + 288] = mem[(34 * unknowndb5a4e99.length) + 160]
      [94ms = unknowndb5a4e99.length + 32
      continue 
  return memory
    from (64 * unknowndb5a4e99.length) + 160
     [93mlen (32 * mem[(32 * unknowndb5a4e99.length) + 128]) + (161 * unknowndb5a4e99.length) + 128


# hash = 0x1a3cd59a
# getter = None
# const = None
# payable = False
def getInfo(uint256 _castleid): # not payable
  mem[96] = 96
  mem[128] = 96
  mem[160] = 0
  mem[192] = 0
  mem[224] = 0
  mem[256] = 0
  mem[288] = 0
  mem[320] = 0
  mem[352] = 0
  mem[384] = 0
  mem[416] = 0
  mem[448] = 0
  mem[32] = 1
  mem[864] = unknown1f11cb48[_castleid].length
  mem[896] = unknown1f11cb48[_castleid].field_0
  [94midx = 896
  [94ms = 0
  while unknown1f11cb48[_castleid].length + 896 > [94midx + 32:
      mem[[94midx + 32] = unknown1f11cb48[_castleid][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[480] = 864
  mem[64] = ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 928
  mem[ceil32(unknown1f11cb48[_castleid].length) + 896] = unknown1f11cb48[_castleid][1].length
  mem[0] = sha3(_castleid, 1) + 1
  mem[ceil32(unknown1f11cb48[_castleid].length) + 928] = unknown1f11cb48[_castleid][1].field_0
  [94midx = ceil32(unknown1f11cb48[_castleid].length) + 928
  [94ms = 0
  while ceil32(unknown1f11cb48[_castleid].length) + unknown1f11cb48[_castleid][1].length + 896 > [94midx:
      mem[[94midx + 32] = unknown1f11cb48[_castleid][[94ms + 1].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[512] = ceil32(unknown1f11cb48[_castleid].length) + 896
  mem[544] = unknown1f11cb48[_castleid].field_512
  mem[576] = unknown1f11cb48[_castleid].field_768
  mem[608] = unknown1f11cb48[_castleid].field_1024
  mem[640] = unknown1f11cb48[_castleid].field_1280
  mem[672] = unknown1f11cb48[_castleid].field_1536
  mem[704] = unknown1f11cb48[_castleid].field_1792
  mem[736] = bool(uint8(unknown1f11cb48[_castleid].field_2048))
  mem[768] = bool(uint8(unknown1f11cb48[_castleid].field_2056))
  mem[800] = unknown1f11cb48[_castleid].field_2304
  mem[832] = unknown1f11cb48[_castleid].field_2560
  mem[ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 992] = unknown1f11cb48[_castleid].field_512
  mem[ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 1024] = unknown1f11cb48[_castleid].field_768
  mem[ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 1056] = unknown1f11cb48[_castleid].field_1024
  mem[ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 1088] = unknown1f11cb48[_castleid].field_2560
  mem[ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 928] = 192
  mem[ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 1120] = unknown1f11cb48[_castleid].length
  mem[ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 1152 len ceil32(unknown1f11cb48[_castleid].length)] = mem[896 len ceil32(unknown1f11cb48[_castleid].length)]
  mem[ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 960] = unknown1f11cb48[_castleid].length + 224
  mem[unknown1f11cb48[_castleid].length + ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 1152] = unknown1f11cb48[_castleid][1].length
  mem[unknown1f11cb48[_castleid].length + ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 1184 len ceil32(unknown1f11cb48[_castleid][1].length)] = mem[ceil32(unknown1f11cb48[_castleid].length) + 928 len ceil32(unknown1f11cb48[_castleid][1].length)]
  if not unknown1f11cb48[_castleid][1].length % 32:
      return Array(len=unknown1f11cb48[_castleid].length, data=mem[896 len ceil32(unknown1f11cb48[_castleid].length)], mem[(2 * ceil32(unknown1f11cb48[_castleid].length)) + ceil32(unknown1f11cb48[_castleid][1].length) + 1152 len unknown1f11cb48[_castleid][1].length + unknown1f11cb48[_castleid].length + -ceil32(unknown1f11cb48[_castleid].length) + 32]), 
             unknown1f11cb48[_castleid].length + 224,
             unknown1f11cb48[_castleid].field_512,
             unknown1f11cb48[_castleid].field_768,
             unknown1f11cb48[_castleid].field_1024,
             unknown1f11cb48[_castleid].field_2560
  mem[floor32(unknown1f11cb48[_castleid][1].length) + unknown1f11cb48[_castleid].length + ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + 1184] = mem[floor32(unknown1f11cb48[_castleid][1].length) + unknown1f11cb48[_castleid].length + ceil32(unknown1f11cb48[_castleid].length) + ceil32(unknown1f11cb48[_castleid][1].length) + -unknown1f11cb48[_castleid][1].length % 32 + 1216 len unknown1f11cb48[_castleid][1].length % 32]
  return Array(len=unknown1f11cb48[_castleid].length, data=mem[896 len ceil32(unknown1f11cb48[_castleid].length)], mem[(2 * ceil32(unknown1f11cb48[_castleid].length)) + ceil32(unknown1f11cb48[_castleid][1].length) + 1152 len floor32(unknown1f11cb48[_castleid][1].length) + unknown1f11cb48[_castleid].length + -ceil32(unknown1f11cb48[_castleid].length) + 64]), 
         unknown1f11cb48[_castleid].length + 224,
         unknown1f11cb48[_castleid].field_512,
         unknown1f11cb48[_castleid].field_768,
         unknown1f11cb48[_castleid].field_1024,
         unknown1f11cb48[_castleid].field_2560


# hash = 0x1f11cb48
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def unknown1f11cb48(uint256 _param1): # not payable
  [94midx = 896
  [94ms = 0
  while unknown1f11cb48[_param1].length + 896 > [94midx + 32:
      mem[[94midx + 32] = unknown1f11cb48[_param1][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  [94midx = ceil32(unknown1f11cb48[_param1].length) + 928
  [94ms = 0
  while ceil32(unknown1f11cb48[_param1].length) + unknown1f11cb48[_param1][1].length + 896 > [94midx:
      mem[[94midx + 32] = unknown1f11cb48[_param1][[94ms + 1].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return unknown1f11cb48[_param1].field_1280, 
         unknown1f11cb48[_param1].field_1536,
         unknown1f11cb48[_param1].field_1792,
         bool(uint8(unknown1f11cb48[_param1].field_2048)),
         bool(uint8(unknown1f11cb48[_param1].field_2056)),
         unknown1f11cb48[_param1].field_2304


# hash = 0x370760ed
# getter = None
# const = None
# payable = False
def unknown370760ed(uint256 _param1): # not payable
  require _param1 < stor3.length
  mem[96] = stor3[_param1].length
  mem[0] = (11 * _param1) + sha3(3)
  mem[128] = stor3[_param1].field_0
  [94midx = 128
  [94ms = 0
  while stor3[_param1].length + 96 > [94midx:
      mem[[94midx + 32] = stor3[(11 * _param1) + [94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[64] = ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 160
  mem[ceil32(stor3[_param1].length) + 128] = stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length
  mem[ceil32(stor3[_param1].length) + 160] = stor[sha3((11 * _param1) + ('name', 'stor3', 3) + 1)].field_0
  [94midx = ceil32(stor3[_param1].length) + 160
  [94ms = 0
  while ceil32(stor3[_param1].length) + stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length + 128 > [94midx:
      mem[[94midx + 32] = stor[[94ms + sha3((11 * _param1) + ('name', 'stor3', 3) + 1)].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 224] = stor3[_param1].field_512
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 256] = stor3[_param1].field_768
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 288] = stor3[_param1].field_1024
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 320] = stor3[_param1].field_1280
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 352] = stor3[_param1].field_1536
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 384] = stor3[_param1].field_1792
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 416] = bool(uint8(stor3[_param1].field_2048))
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 448] = bool(uint8(stor3[_param1].field_2056))
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 480] = stor3[_param1].field_2304
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 512] = stor3[_param1].field_2560
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 160] = 384
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 544] = stor3[_param1].length
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 576 len ceil32(stor3[_param1].length)] = mem[128 len ceil32(stor3[_param1].length)]
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 192] = stor3[_param1].length + 416
  mem[stor3[_param1].length + ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 576] = stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length
  mem[stor3[_param1].length + ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 608 len ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length)] = mem[ceil32(stor3[_param1].length) + 160 len ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length)]
  if not stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length % 32:
      return Array(len=stor3[_param1].length, data=mem[128 len ceil32(stor3[_param1].length)], mem[(2 * ceil32(stor3[_param1].length)) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 576 len stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length + stor3[_param1].length + -ceil32(stor3[_param1].length) + 32]), 
             stor3[_param1].length + 416,
             stor3[_param1].field_512,
             stor3[_param1].field_768,
             stor3[_param1].field_1024,
             stor3[_param1].field_1280,
             stor3[_param1].field_1536,
             stor3[_param1].field_1792,
             bool(uint8(stor3[_param1].field_2048)),
             bool(uint8(stor3[_param1].field_2056)),
             stor3[_param1].field_2304,
             stor3[_param1].field_2560
  mem[floor32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + stor3[_param1].length + ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 608] = mem[floor32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + stor3[_param1].length + ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + -stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length % 32 + 640 len stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length % 32]
  return Array(len=stor3[_param1].length, data=mem[128 len ceil32(stor3[_param1].length)], mem[(2 * ceil32(stor3[_param1].length)) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 576 len floor32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + stor3[_param1].length + -ceil32(stor3[_param1].length) + 64]), 
         stor3[_param1].length + 416,
         stor3[_param1].field_512,
         stor3[_param1].field_768,
         stor3[_param1].field_1024,
         stor3[_param1].field_1280,
         stor3[_param1].field_1536,
         stor3[_param1].field_1792,
         bool(uint8(stor3[_param1].field_2048)),
         bool(uint8(stor3[_param1].field_2056)),
         stor3[_param1].field_2304,
         stor3[_param1].field_2560


# hash = 0x40490a90
# getter = None
# const = ['return', 100000]
# payable = False
const getMultiplier = 100000


# hash = 0x5678fa73
# getter = None
# const = None
# payable = False
def unknown5678fa73(): # not payable
  return unknownf887b097, unknownf887b097, unknowne3b1e2fe


# hash = 0x60bb4cbf
# getter = ['storage', 256, 0, ['sha3', ['data', ['call.data', ['add', 36, ['cd', 36]], ['cd', ['add', 4, ['cd', 36]]]], ['sha3', ['data', ['call.data', ['add', 36, ['cd', 4]], ['cd', ['add', 4, ['cd', 4]]]], 2]]]]]
# const = None
# payable = False
def unknown60bb4cbf(array _param1, array _param2): # not payable
  return unknown60bb4cbf[_param1[all]][_param2[all]]


# hash = 0x68361d71
# getter = None
# const = None
# payable = False
def unknown68361d71(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4, bool _param5, bool _param6, uint256 _param7): # not payable
  if owner != caller:
      revert with 0, '1'
  require 0 < unknown1f11cb48[_param1].field_2560
  unknown1f11cb48[_param1].field_1280 = _param2
  unknown1f11cb48[_param1].field_1536 = _param3
  unknown1f11cb48[_param1].field_1792 = _param4
  uint8(unknown1f11cb48[_param1].field_2048) = uint8(_param5)
  Mask(248, 0, unknown1f11cb48[_param1].field_2056) = Mask(248, 0, _param6)
  Mask(240, 0, unknown1f11cb48[_param1].field_2064) = Mask(240, 16, _param5) >> 16
  unknown1f11cb48[_param1].field_2304 = _param7
  return 0


# hash = 0x721e6584
# getter = ['bool', ['storage', 8, 8, ['add', 8, ['sha3', ['data', ['cd', 4], 1]]]]]
# const = None
# payable = False
def unknown721e6584(uint256 _param1): # not payable
  if 0 >= unknown1f11cb48[_param1].field_2304:
      revert with 0, '25'
  return bool(uint8(unknown1f11cb48[_param1].field_2056))


# hash = 0x7c6ab85b
# getter = ['bool', ['storage', 8, 0, ['add', 8, ['sha3', ['data', ['cd', 4], 1]]]]]
# const = None
# payable = False
def unknown7c6ab85b(uint256 _param1): # not payable
  if 0 >= unknown1f11cb48[_param1].field_2304:
      revert with 0, '25'
  return bool(uint8(unknown1f11cb48[_param1].field_2048))


# hash = 0x893d20e8
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def getOwner(): # not payable
  return owner


# hash = 0x89590641
# getter = None
# const = None
# payable = False
def unknown89590641(uint256 _param1, array _param2, array _param3, uint256 _param4, uint256 _param5, uint256 _param6, uint256 _param7): # not payable
  mem[128 len _param2.length] = _param2[all]
  mem[ceil32(_param2.length) + 128] = _param3.length
  mem[ceil32(_param2.length) + 160 len _param3.length] = _param3[all]
  if owner != caller:
      revert with 0, '1'
  unknown1f11cb48[_param1][].field_0 = Array(len=_param2.length, data=_param2[all])
  unknown1f11cb48[_param1][1][].field_0 = Array(len=_param3.length, data=_param3[all])
  unknown1f11cb48[_param1].field_512 = _param4
  unknown1f11cb48[_param1].field_768 = _param5
  unknown1f11cb48[_param1].field_1024 = _param6
  unknown1f11cb48[_param1].field_2560 = _param7
  unknown1f11cb48[_param1].field_1280 = 0
  unknown1f11cb48[_param1].field_1536 = 0
  unknown1f11cb48[_param1].field_1792 = 0
  uint16(unknown1f11cb48[_param1].field_2048) = 0
  unknown1f11cb48[_param1].field_2304 = 100
  mem[ceil32(_param2.length) + ceil32(_param3.length) + 160 len floor32(_param3.length)] = call.data[_param3 + 36 len floor32(_param3.length)]
  mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param3.length) + 160] = 256^(-(_param3.length % 32) + 32) - 1 and mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param3.length) + 160] or call.data[_param3 + floor32(_param3.length) + 36 len _param3.length % 32], mem[ceil32(_param2.length) + _param3.length + 160 len -(_param3.length % 32) + 32] and !(256^(-(_param3.length % 32) + 32) - 1)
  mem[ceil32(_param2.length) + ceil32(_param3.length) + _param3.length + 160] = 2
  [94m_1762 = sha3(call.data[_param3 + 36 len floor32(_param3.length)], mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param3.length) + 160 len (_param3.length % 32) + 32])
  mem[ceil32(_param2.length) + ceil32(_param3.length) + 160 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
  mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param2.length) + 160] = !(256^(-(_param2.length % 32) + 32) - 1) and call.data[_param2 + floor32(_param2.length) + 36 len _param2.length % 32], mem[_param2.length + 128 len -(_param2.length % 32) + 32] or 256^(-(_param2.length % 32) + 32) - 1 and mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param2.length) + 160]
  mem[_param2.length + ceil32(_param2.length) + ceil32(_param3.length) + 160] = [94m_1762
  stor[mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param2.length) + 160 len (_param2.length % 32) + 32]][call.data[_param2 + 36 len floor32(_param2.length)]] = _param1
  stor3.length++
  if 31 >= unknown1f11cb48[_param1].length:
      stor3[stor3.length].field_0 = unknown1f11cb48[_param1].field_0
      [94midx = 0
      while stor3[stor3.length].length + 31 / 32 > [94midx:
          stor3[(11 * stor3.length) + [94midx].field_0 = 0
          [94midx = [94midx + 1
          continue 
      if 31 >= unknown1f11cb48[_param1][1].length:
          storC257[stor3.length] = unknown1f11cb48[_param1].field_256
          [94midx = 0
          while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
              stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)] = 0
              [94midx = [94midx + 1
              continue 
      else:
          storC257[stor3.length] = Mask(255, 1, (256 * not bool(unknown1f11cb48[_param1].field_256)) - 1 and unknown1f11cb48[_param1].field_256) + 1
          if not Mask(255, 1, (256 * not bool(unknown1f11cb48[_param1].field_256)) - 1 and unknown1f11cb48[_param1].field_256):
              [94midx = 0
              while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
                  stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)] = 0
                  [94midx = [94midx + 1
                  continue 
          else:
              [94ms = 0
              [94midx = 0
              while unknown1f11cb48[_param1][1].length + 31 / 32 > [94midx:
                  stor[[94ms + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)] = unknown1f11cb48[_param1][[94midx + 1].field_0
                  [94ms = [94ms + 1
                  [94midx = [94midx + 1
                  continue 
              [94midx = unknown1f11cb48[_param1][1].length + 31 / 32
              while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
                  stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)] = 0
                  [94midx = [94midx + 1
                  continue 
  else:
      stor3[stor3.length].field_0 = Mask(255, 1, unknown1f11cb48[_param1].field_0 and (256 * not bool(unknown1f11cb48[_param1].field_0)) - 1) + 1
      if not Mask(255, 1, unknown1f11cb48[_param1].field_0 and (256 * not bool(unknown1f11cb48[_param1].field_0)) - 1):
          [94midx = 0
          while stor3[stor3.length].length + 31 / 32 > [94midx:
              stor3[(11 * stor3.length) + [94midx].field_0 = 0
              [94midx = [94midx + 1
              continue 
      else:
          [94ms = 0
          [94midx = 0
          while unknown1f11cb48[_param1].length + 31 / 32 > [94midx:
              stor3[(11 * stor3.length) + [94ms].field_0 = unknown1f11cb48[_param1][[94midx].field_0
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              continue 
          [94midx = unknown1f11cb48[_param1].length + 31 / 32
          while stor3[stor3.length].length + 31 / 32 > [94midx:
              stor3[(11 * stor3.length) + [94midx].field_0 = 0
              [94midx = [94midx + 1
              continue 
      if 31 >= unknown1f11cb48[_param1][1].length:
          storC257[stor3.length] = unknown1f11cb48[_param1].field_256
          [94midx = 0
          while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
              stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)] = 0
              [94midx = [94midx + 1
              continue 
      else:
          storC257[stor3.length] = Mask(255, 1, (256 * not bool(unknown1f11cb48[_param1].field_256)) - 1 and unknown1f11cb48[_param1].field_256) + 1
          if not Mask(255, 1, (256 * not bool(unknown1f11cb48[_param1].field_256)) - 1 and unknown1f11cb48[_param1].field_256):
              [94midx = 0
              while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
                  stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)] = 0
                  [94midx = [94midx + 1
                  continue 
          else:
              [94ms = 0
              [94midx = 0
              while unknown1f11cb48[_param1][1].length + 31 / 32 > [94midx:
                  stor[[94ms + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)] = unknown1f11cb48[_param1][[94midx + 1].field_0
                  [94ms = [94ms + 1
                  [94midx = [94midx + 1
                  continue 
              [94midx = unknown1f11cb48[_param1][1].length + 31 / 32
              while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
                  stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)] = 0
                  [94midx = [94midx + 1
                  continue 
  storC257[stor3.length] = unknown1f11cb48[_param1].field_512
  storC257[stor3.length] = unknown1f11cb48[_param1].field_768
  storC257[stor3.length] = unknown1f11cb48[_param1].field_1024
  storC257[stor3.length] = unknown1f11cb48[_param1].field_1280
  storC257[stor3.length] = unknown1f11cb48[_param1].field_1536
  storC257[stor3.length] = unknown1f11cb48[_param1].field_1792
  uint8(storC257[stor3.length].field_0) = uint8(bool(uint8(unknown1f11cb48[_param1].field_2048)))
  uint8(storC257[stor3.length].field_0) = uint8(bool(uint8(unknown1f11cb48[_param1].field_2048)))
  Mask(248, 0, storC257[stor3.length].field_8) = Mask(248, 0, bool(uint8(unknown1f11cb48[_param1].field_2056)))
  Mask(240, 0, storC257[stor3.length].field_16) = Mask(240, 16, bool(uint8(unknown1f11cb48[_param1].field_2048))) >> 16
  storC257[stor3.length] = unknown1f11cb48[_param1].field_2304
  storC257[stor3.length] = unknown1f11cb48[_param1].field_2560
  unknowndb5a4e99.length++
  unknowndb5a4e99[unknowndb5a4e99.length] = _param1
  return 0


# hash = 0x98f6735a
# getter = None
# const = None
# payable = False
def unknown98f6735a(uint256 _param1): # not payable
  mem[32] = 1
  mem[96] = unknown1f11cb48[_param1].length
  mem[0] = sha3(_param1, 1)
  mem[128] = unknown1f11cb48[_param1].field_0
  [94midx = 128
  [94ms = 0
  while unknown1f11cb48[_param1].length + 96 > [94midx:
      mem[[94midx + 32] = unknown1f11cb48[_param1][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[64] = ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 160
  mem[ceil32(unknown1f11cb48[_param1].length) + 128] = unknown1f11cb48[_param1][1].length
  mem[ceil32(unknown1f11cb48[_param1].length) + 160] = unknown1f11cb48[_param1][1].field_0
  [94midx = ceil32(unknown1f11cb48[_param1].length) + 160
  [94ms = 0
  while ceil32(unknown1f11cb48[_param1].length) + unknown1f11cb48[_param1][1].length + 128 > [94midx:
      mem[[94midx + 32] = unknown1f11cb48[_param1][[94ms + 1].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 224] = unknown1f11cb48[_param1].field_512
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 256] = unknown1f11cb48[_param1].field_768
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 288] = unknown1f11cb48[_param1].field_1024
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 320] = unknown1f11cb48[_param1].field_1280
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 352] = unknown1f11cb48[_param1].field_1536
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 384] = unknown1f11cb48[_param1].field_1792
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 416] = bool(uint8(unknown1f11cb48[_param1].field_2048))
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 448] = bool(uint8(unknown1f11cb48[_param1].field_2056))
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 480] = unknown1f11cb48[_param1].field_2304
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 512] = unknown1f11cb48[_param1].field_2560
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 160] = 384
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 544] = unknown1f11cb48[_param1].length
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 576 len ceil32(unknown1f11cb48[_param1].length)] = mem[128 len ceil32(unknown1f11cb48[_param1].length)]
  mem[ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 192] = unknown1f11cb48[_param1].length + 416
  mem[unknown1f11cb48[_param1].length + ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 576] = unknown1f11cb48[_param1][1].length
  mem[unknown1f11cb48[_param1].length + ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 608 len ceil32(unknown1f11cb48[_param1][1].length)] = mem[ceil32(unknown1f11cb48[_param1].length) + 160 len ceil32(unknown1f11cb48[_param1][1].length)]
  if not unknown1f11cb48[_param1][1].length % 32:
      return Array(len=unknown1f11cb48[_param1].length, data=mem[128 len ceil32(unknown1f11cb48[_param1].length)], mem[(2 * ceil32(unknown1f11cb48[_param1].length)) + ceil32(unknown1f11cb48[_param1][1].length) + 576 len unknown1f11cb48[_param1][1].length + unknown1f11cb48[_param1].length + -ceil32(unknown1f11cb48[_param1].length) + 32]), 
             unknown1f11cb48[_param1].length + 416,
             unknown1f11cb48[_param1].field_512,
             unknown1f11cb48[_param1].field_768,
             unknown1f11cb48[_param1].field_1024,
             unknown1f11cb48[_param1].field_1280,
             unknown1f11cb48[_param1].field_1536,
             unknown1f11cb48[_param1].field_1792,
             bool(uint8(unknown1f11cb48[_param1].field_2048)),
             bool(uint8(unknown1f11cb48[_param1].field_2056)),
             unknown1f11cb48[_param1].field_2304,
             unknown1f11cb48[_param1].field_2560
  mem[floor32(unknown1f11cb48[_param1][1].length) + unknown1f11cb48[_param1].length + ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + 608] = mem[floor32(unknown1f11cb48[_param1][1].length) + unknown1f11cb48[_param1].length + ceil32(unknown1f11cb48[_param1].length) + ceil32(unknown1f11cb48[_param1][1].length) + -unknown1f11cb48[_param1][1].length % 32 + 640 len unknown1f11cb48[_param1][1].length % 32]
  return Array(len=unknown1f11cb48[_param1].length, data=mem[128 len ceil32(unknown1f11cb48[_param1].length)], mem[(2 * ceil32(unknown1f11cb48[_param1].length)) + ceil32(unknown1f11cb48[_param1][1].length) + 576 len floor32(unknown1f11cb48[_param1][1].length) + unknown1f11cb48[_param1].length + -ceil32(unknown1f11cb48[_param1].length) + 64]), 
         unknown1f11cb48[_param1].length + 416,
         unknown1f11cb48[_param1].field_512,
         unknown1f11cb48[_param1].field_768,
         unknown1f11cb48[_param1].field_1024,
         unknown1f11cb48[_param1].field_1280,
         unknown1f11cb48[_param1].field_1536,
         unknown1f11cb48[_param1].field_1792,
         bool(uint8(unknown1f11cb48[_param1].field_2048)),
         bool(uint8(unknown1f11cb48[_param1].field_2056)),
         unknown1f11cb48[_param1].field_2304,
         unknown1f11cb48[_param1].field_2560


# hash = 0x9ba1a7d5
# getter = None
# const = None
# payable = False
def unknown9ba1a7d5(uint256 _param1): # not payable
  return (unknown1f11cb48[_param1].field_2304 > 0)


# hash = 0x9e66d12d
# getter = ['storage', 256, 0, ['add', 2, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown9e66d12d(uint256 _param1): # not payable
  if 0 >= unknown1f11cb48[_param1].field_2304:
      revert with 0, '25'
  return unknown1f11cb48[_param1].field_512


# hash = 0x9fb59daf
# getter = ['storage', 256, 0, ['add', 9, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown9fb59daf(uint256 _param1): # not payable
  if 0 >= unknown1f11cb48[_param1].field_2304:
      revert with 0, '25'
  return unknown1f11cb48[_param1].field_2304


# hash = 0xb00a6eef
# getter = None
# const = None
# payable = False
def unknownb00a6eef(uint256 _param1): # not payable
  return (unknown1f11cb48[_param1].field_2304 > 0)


# hash = 0xc519b54b
# getter = ['storage', 8, 8, 5]
# const = None
# payable = False
def unknownc519b54b(): # not payable
  return unknownc519b54b


# hash = 0xcba181e8
# getter = None
# const = None
# payable = False
def unknowncba181e8(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  if unknown1f11cb48[_param1].field_2304 <= 0:
      return 0, 'Ticker not found'
  if 0 >= unknown1f11cb48[_param1].field_2304:
      revert with 0, '25'
  if not uint8(unknown1f11cb48[_param1].field_2048):
      return 0, 'Trade for instrument is forbided'
  if 0 >= unknown1f11cb48[_param1].field_2304:
      revert with 0, '25'
  if _param3 <′ 0:
      if not uint8(unknown1f11cb48[_param1].field_2056):
          return 0, 'Short for instrument is forbided'
  require ext_code.size(0x1fc04ee645b616a1641ea13fa5360cfa1e043367)
  [93mdelegate 0x1fc04ee645b616a1641ea13fa5360cfa1e043367.abs(int256 val) with:
       gas gas_remaining wei
      args _param3
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if delegate.return_data[0] < unknown1f11cb48[_param1].field_512:
      return 0, 'Volume too low'
  if 0 >= unknown1f11cb48[_param1].field_2304:
      revert with 0, '25'
  require ext_code.size(0x1fc04ee645b616a1641ea13fa5360cfa1e043367)
  [93mdelegate 0x1fc04ee645b616a1641ea13fa5360cfa1e043367.abs(int256 val) with:
       gas gas_remaining wei
      args _param3
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require unknown1f11cb48[_param1].field_1024
  if delegate.return_data[0] % unknown1f11cb48[_param1].field_1024:
      return 0, 'VolStep is not correct'
  if 0 >= unknown1f11cb48[_param1].field_2304:
      revert with 0, '25'
  if _param2 <= unknown1f11cb48[_param1].field_768:
      return 1, 0
  return 0, 'Aim volume too huge'


# hash = 0xcd1ba783
# getter = ['storage', 256, 0, ['add', 4, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknowncd1ba783(uint256 _param1): # not payable
  if 0 >= unknown1f11cb48[_param1].field_2304:
      revert with 0, '25'
  return unknown1f11cb48[_param1].field_1024


# hash = 0xcdf9b77e
# getter = ['storage', 256, 0, ['add', 10, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def getCurrency(uint256 _index): # not payable
  if 0 >= unknown1f11cb48[_index].field_2304:
      revert with 0, '25'
  return unknown1f11cb48[_index].field_2560


# hash = 0xdb5a4e99
# getter = ['storage', 256, 0, ['add', ['sha3', 4], ['cd', 4]]]
# const = None
# payable = False
def unknowndb5a4e99(uint256 _param1): # not payable
  require _param1 < unknowndb5a4e99.length
  return unknowndb5a4e99[_param1]


# hash = 0xdf7c6650
# getter = None
# const = None
# payable = False
def unknowndf7c6650(uint8 _param1, uint8 _param2, uint8 _param3): # not payable
  if owner != caller:
      revert with 0, '1'
  unknownf887b097 = _param1
  unknownc519b54b = _param2
  unknowne3b1e2fe = _param3


# hash = 0xe3b1e2fe
# getter = ['storage', 8, 16, 5]
# const = None
# payable = False
def unknowne3b1e2fe(): # not payable
  return unknowne3b1e2fe


# hash = 0xeacfff63
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknowneacfff63(uint256 _param1): # not payable
  if 0 >= unknown1f11cb48[_param1].field_2304:
      revert with 0, '25'
  return unknown1f11cb48[_param1].field_768


# hash = 0xef0b2368
# getter = None
# const = None
# payable = False
def unknownef0b2368(uint256 _param1): # not payable
  mem[128 len 1024] = code.data[9315 len 1024]
  [94midx = 0
  while [94midx < 32:
      require [94midx < 32
      mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, ('add', 256, ('mul', -1, (('mask_shl', 256, 0, -3, ('param', '_param1')), 0))), ('add', -11, (('mask_shl', 256, 0, -3, ('param', '_param1')), 0)), ('var', 0)), 0) + 256, 0) << (('mask_shl', 8, ('add', 256, ('mul', -1, (('mask_shl', 256, 0, -3, ('param', '_param1')), 0))), ('add', -11, (('mask_shl', 256, 0, -3, ('param', '_param1')), 0)), ('var', 0)), 0) - 256
      [94midx = [94midx + 1
      continue 
  return 32, 32, mem[128]


# hash = 0xf887b097
# getter = ['storage', 8, 0, 5]
# const = None
# payable = False
def unknownf887b097(): # not payable
  return unknownf887b097


# hash = 0xfcee45f4
# getter = ['storage', 256, 0, ['add', 7, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def getFee(uint256 _value): # not payable
  if 0 >= unknown1f11cb48[_value].field_2304:
      revert with 0, '25'
  return unknown1f11cb48[_value].field_1792


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


