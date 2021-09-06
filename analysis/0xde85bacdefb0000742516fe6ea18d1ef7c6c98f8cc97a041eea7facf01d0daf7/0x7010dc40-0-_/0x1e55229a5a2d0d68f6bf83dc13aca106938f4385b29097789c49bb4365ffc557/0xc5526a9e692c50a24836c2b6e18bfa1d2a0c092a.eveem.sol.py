# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xC5526a9e692C50a24836C2B6e18Bfa1D2a0c092A 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x5923aa0a': 'unknown5923aa0a(?)'} 

# storage definitions
def storage:
# hash = 0x0977eb77
# getter = ['bool', ['storage', 8, 8, ['add', 8, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]]
# const = None
# payable = False
def unknown0977eb77(uint32 _param1): # not payable
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  return bool(uint8(unknown0f543432[_param1 << 224].field_2056))


# hash = 0x0f543432
# getter = ['storage', 32, 0, ['add', 10, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknown0f543432(uint32 _param1): # not payable
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  return uint32(unknown0f543432[_param1 << 224].field_2560)


# hash = 0x12081ef5
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def unknown12081ef5(uint32 _param1): # not payable
  [94midx = 896
  [94ms = 0
  while unknown0f543432[_param1 << 224].length + 896 > [94midx + 32:
      mem[[94midx + 32] = uint256(unknown0f543432[_param1 << 224][[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  [94midx = ceil32(unknown0f543432[_param1 << 224].length) + 928
  [94ms = 0
  while ceil32(unknown0f543432[_param1 << 224].length) + unknown0f543432[_param1 << 224][1].length + 896 > [94midx:
      mem[[94midx + 32] = uint256(unknown0f543432[_param1 << 224][[94ms + 1].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return uint256(unknown0f543432[_param1 << 224].field_1280), 
         uint256(unknown0f543432[_param1 << 224].field_1536),
         uint256(unknown0f543432[_param1 << 224].field_1792),
         bool(uint8(unknown0f543432[_param1 << 224].field_2048)),
         bool(uint8(unknown0f543432[_param1 << 224].field_2056)),
         uint256(unknown0f543432[_param1 << 224].field_2304)


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
  if not stor4.length:
      mem[(32 * stor4.length) + 128] = stor4.length
  else:
      mem[128 len 32 * stor4.length] = code.data[9903 len 32 * stor4.length]
      mem[(32 * stor4.length) + 128] = stor4.length
      mem[(32 * stor4.length) + 160 len 32 * stor4.length] = code.data[9903 len 32 * stor4.length]
  [94midx = 0
  while [94midx < stor4.length:
      require [94midx < stor4.length
      mem[(32 * [94midx) + 128] = stor('array', ('div', 0.125, ('var', 0)), ('name', 'stor4', 4))[uint8([94midx)]
      require [94midx < stor4.length
      if 0 >= uint256(unknown0f543432[uint32(stor4[0.125 / [94midx].field_(32 * idx % 8) - 224)].field_2304):
          revert with 0, '25'
      mem[0] = stor('array', ('div', 0.125, ('var', 0)), ('name', 'stor4', 4))[uint8([94midx)]
      mem[32] = 1
      require [94midx < mem[(32 * stor4.length) + 128]
      mem[(32 * stor4.length) + (32 * [94midx) + 160] = uint32(unknown0f543432[uint32(stor4[0.125 / [94midx].field_(32 * idx % 8) - 224)].field_2560)
      [94midx = [94midx + 1
      continue 
  mem[(64 * stor4.length) + 160] = 64
  mem[(64 * stor4.length) + 224] = stor4.length
  mem[(64 * stor4.length) + 256 len floor32(stor4.length)] = mem[128 len floor32(stor4.length)]
  mem[(64 * stor4.length) + 192] = (32 * stor4.length) + 96
  mem[(98 * stor4.length) + 256] = mem[(32 * stor4.length) + 128]
  [94ms = 0
  while stor4.length < 32 * mem[(32 * stor4.length) + 128]:
      mem[(99 * stor4.length) + 288] = mem[(34 * stor4.length) + 160]
      [94ms = stor4.length + 32
      continue 
  return memory
    from (64 * stor4.length) + 160
     [93mlen (32 * mem[(32 * stor4.length) + 128]) + (161 * stor4.length) + 128


# hash = 0x1719b3d5
# getter = None
# const = None
# payable = False
def unknown1719b3d5(uint32 _param1): # not payable
  mem[32] = 1
  mem[96] = unknown0f543432[_param1].length
  mem[0] = sha3(_param1, 1)
  mem[128] = uint256(unknown0f543432[_param1].field_0)
  [94midx = 128
  [94ms = 0
  while unknown0f543432[_param1].length + 96 > [94midx:
      mem[[94midx + 32] = uint256(unknown0f543432[_param1][[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[64] = ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 160
  mem[ceil32(unknown0f543432[_param1].length) + 128] = unknown0f543432[_param1][1].length
  mem[ceil32(unknown0f543432[_param1].length) + 160] = uint256(unknown0f543432[_param1][1].field_0)
  [94midx = ceil32(unknown0f543432[_param1].length) + 160
  [94ms = 0
  while ceil32(unknown0f543432[_param1].length) + unknown0f543432[_param1][1].length + 128 > [94midx:
      mem[[94midx + 32] = uint256(unknown0f543432[_param1][[94ms + 1].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 224] = uint256(unknown0f543432[_param1].field_512)
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 256] = uint256(unknown0f543432[_param1].field_768)
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 288] = uint256(unknown0f543432[_param1].field_1024)
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 320] = uint256(unknown0f543432[_param1].field_1280)
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 352] = uint256(unknown0f543432[_param1].field_1536)
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 384] = uint256(unknown0f543432[_param1].field_1792)
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 416] = bool(uint8(unknown0f543432[_param1].field_2048))
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 448] = bool(uint8(unknown0f543432[_param1].field_2056))
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 480] = uint256(unknown0f543432[_param1].field_2304)
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 512] = uint32(unknown0f543432[_param1].field_2560)
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 160] = 384
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 544] = unknown0f543432[_param1].length
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 576 len ceil32(unknown0f543432[_param1].length)] = mem[128 len ceil32(unknown0f543432[_param1].length)]
  mem[ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 192] = unknown0f543432[_param1].length + 416
  mem[unknown0f543432[_param1].length + ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 576] = unknown0f543432[_param1][1].length
  mem[unknown0f543432[_param1].length + ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 608 len ceil32(unknown0f543432[_param1][1].length)] = mem[ceil32(unknown0f543432[_param1].length) + 160 len ceil32(unknown0f543432[_param1][1].length)]
  if not unknown0f543432[_param1][1].length % 32:
      return Array(len=unknown0f543432[_param1].length, data=mem[128 len ceil32(unknown0f543432[_param1].length)], mem[(2 * ceil32(unknown0f543432[_param1].length)) + ceil32(unknown0f543432[_param1][1].length) + 576 len unknown0f543432[_param1][1].length + unknown0f543432[_param1].length + -ceil32(unknown0f543432[_param1].length) + 32]), 
             unknown0f543432[_param1].length + 416,
             uint256(unknown0f543432[_param1].field_512),
             uint256(unknown0f543432[_param1].field_768),
             uint256(unknown0f543432[_param1].field_1024),
             uint256(unknown0f543432[_param1].field_1280),
             uint256(unknown0f543432[_param1].field_1536),
             uint256(unknown0f543432[_param1].field_1792),
             bool(uint8(unknown0f543432[_param1].field_2048)),
             bool(uint8(unknown0f543432[_param1].field_2056)),
             uint256(unknown0f543432[_param1].field_2304),
             uint32(unknown0f543432[_param1].field_2560)
  mem[floor32(unknown0f543432[_param1][1].length) + unknown0f543432[_param1].length + ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + 608] = mem[floor32(unknown0f543432[_param1][1].length) + unknown0f543432[_param1].length + ceil32(unknown0f543432[_param1].length) + ceil32(unknown0f543432[_param1][1].length) + -unknown0f543432[_param1][1].length % 32 + 640 len unknown0f543432[_param1][1].length % 32]
  return Array(len=unknown0f543432[_param1].length, data=mem[128 len ceil32(unknown0f543432[_param1].length)], mem[(2 * ceil32(unknown0f543432[_param1].length)) + ceil32(unknown0f543432[_param1][1].length) + 576 len floor32(unknown0f543432[_param1][1].length) + unknown0f543432[_param1].length + -ceil32(unknown0f543432[_param1].length) + 64]), 
         unknown0f543432[_param1].length + 416,
         uint256(unknown0f543432[_param1].field_512),
         uint256(unknown0f543432[_param1].field_768),
         uint256(unknown0f543432[_param1].field_1024),
         uint256(unknown0f543432[_param1].field_1280),
         uint256(unknown0f543432[_param1].field_1536),
         uint256(unknown0f543432[_param1].field_1792),
         bool(uint8(unknown0f543432[_param1].field_2048)),
         bool(uint8(unknown0f543432[_param1].field_2056)),
         uint256(unknown0f543432[_param1].field_2304),
         uint32(unknown0f543432[_param1].field_2560)


# hash = 0x1ada4339
# getter = None
# const = None
# payable = False
def unknown1ada4339(uint32 _param1): # not payable
  return (uint256(unknown0f543432[_param1 << 224].field_2304) > 0)


# hash = 0x307e47cb
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknown307e47cb(uint32 _param1): # not payable
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  return uint256(unknown0f543432[_param1 << 224].field_768)


# hash = 0x370760ed
# getter = None
# const = None
# payable = False
def unknown370760ed(uint256 _param1): # not payable
  require _param1 < stor3.length
  mem[96] = stor3[_param1].length
  mem[0] = (11 * _param1) + sha3(3)
  mem[128] = uint256(stor3[_param1].field_0)
  [94midx = 128
  [94ms = 0
  while stor3[_param1].length + 96 > [94midx:
      mem[[94midx + 32] = uint256(stor3[(11 * _param1) + [94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[64] = ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 160
  mem[ceil32(stor3[_param1].length) + 128] = stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length
  mem[ceil32(stor3[_param1].length) + 160] = uint256(stor[sha3((11 * _param1) + ('name', 'stor3', 3) + 1)].field_0)
  [94midx = ceil32(stor3[_param1].length) + 160
  [94ms = 0
  while ceil32(stor3[_param1].length) + stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length + 128 > [94midx:
      mem[[94midx + 32] = uint256(stor[[94ms + sha3((11 * _param1) + ('name', 'stor3', 3) + 1)].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 224] = uint256(stor3[_param1].field_512)
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 256] = uint256(stor3[_param1].field_768)
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 288] = uint256(stor3[_param1].field_1024)
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 320] = uint256(stor3[_param1].field_1280)
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 352] = uint256(stor3[_param1].field_1536)
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 384] = uint256(stor3[_param1].field_1792)
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 416] = bool(uint8(stor3[_param1].field_2048))
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 448] = bool(uint8(stor3[_param1].field_2056))
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 480] = uint256(stor3[_param1].field_2304)
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 512] = uint32(stor3[_param1].field_2560)
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 160] = 384
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 544] = stor3[_param1].length
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 576 len ceil32(stor3[_param1].length)] = mem[128 len ceil32(stor3[_param1].length)]
  mem[ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 192] = stor3[_param1].length + 416
  mem[stor3[_param1].length + ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 576] = stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length
  mem[stor3[_param1].length + ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 608 len ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length)] = mem[ceil32(stor3[_param1].length) + 160 len ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length)]
  if not stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length % 32:
      return Array(len=stor3[_param1].length, data=mem[128 len ceil32(stor3[_param1].length)], mem[(2 * ceil32(stor3[_param1].length)) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 576 len stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length + stor3[_param1].length + -ceil32(stor3[_param1].length) + 32]), 
             stor3[_param1].length + 416,
             uint256(stor3[_param1].field_512),
             uint256(stor3[_param1].field_768),
             uint256(stor3[_param1].field_1024),
             uint256(stor3[_param1].field_1280),
             uint256(stor3[_param1].field_1536),
             uint256(stor3[_param1].field_1792),
             bool(uint8(stor3[_param1].field_2048)),
             bool(uint8(stor3[_param1].field_2056)),
             uint256(stor3[_param1].field_2304),
             uint32(stor3[_param1].field_2560)
  mem[floor32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + stor3[_param1].length + ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 608] = mem[floor32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + stor3[_param1].length + ceil32(stor3[_param1].length) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + -stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length % 32 + 640 len stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length % 32]
  return Array(len=stor3[_param1].length, data=mem[128 len ceil32(stor3[_param1].length)], mem[(2 * ceil32(stor3[_param1].length)) + ceil32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + 576 len floor32(stor[(11 * _param1) + ('name', 'stor3', 3) + 1].length) + stor3[_param1].length + -ceil32(stor3[_param1].length) + 64]), 
         stor3[_param1].length + 416,
         uint256(stor3[_param1].field_512),
         uint256(stor3[_param1].field_768),
         uint256(stor3[_param1].field_1024),
         uint256(stor3[_param1].field_1280),
         uint256(stor3[_param1].field_1536),
         uint256(stor3[_param1].field_1792),
         bool(uint8(stor3[_param1].field_2048)),
         bool(uint8(stor3[_param1].field_2056)),
         uint256(stor3[_param1].field_2304),
         uint32(stor3[_param1].field_2560)


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
# getter = ['storage', 32, 0, ['sha3', ['data', ['call.data', ['add', 36, ['cd', 36]], ['cd', ['add', 4, ['cd', 36]]]], ['sha3', ['data', ['call.data', ['add', 36, ['cd', 4]], ['cd', ['add', 4, ['cd', 4]]]], 2]]]]]
# const = None
# payable = False
def unknown60bb4cbf(array _param1, array _param2): # not payable
  return unknown60bb4cbf[_param1[all]][_param2[all]]


# hash = 0x63276d6e
# getter = None
# const = None
# payable = False
def unknown63276d6e(uint32 _param1): # not payable
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
  mem[864] = unknown0f543432[_param1 << 224].length
  mem[896] = uint256(unknown0f543432[_param1 << 224].field_0)
  [94midx = 896
  [94ms = 0
  while unknown0f543432[_param1 << 224].length + 896 > [94midx + 32:
      mem[[94midx + 32] = uint256(unknown0f543432[_param1 << 224][[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[480] = 864
  mem[64] = ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 928
  mem[ceil32(unknown0f543432[_param1 << 224].length) + 896] = unknown0f543432[_param1 << 224][1].length
  mem[0] = sha3(_param1 << 224, 1) + 1
  mem[ceil32(unknown0f543432[_param1 << 224].length) + 928] = uint256(unknown0f543432[_param1 << 224][1].field_0)
  [94midx = ceil32(unknown0f543432[_param1 << 224].length) + 928
  [94ms = 0
  while ceil32(unknown0f543432[_param1 << 224].length) + unknown0f543432[_param1 << 224][1].length + 896 > [94midx:
      mem[[94midx + 32] = uint256(unknown0f543432[_param1 << 224][[94ms + 1].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[512] = ceil32(unknown0f543432[_param1 << 224].length) + 896
  mem[544] = uint256(unknown0f543432[_param1 << 224].field_512)
  mem[576] = uint256(unknown0f543432[_param1 << 224].field_768)
  mem[608] = uint256(unknown0f543432[_param1 << 224].field_1024)
  mem[640] = uint256(unknown0f543432[_param1 << 224].field_1280)
  mem[672] = uint256(unknown0f543432[_param1 << 224].field_1536)
  mem[704] = uint256(unknown0f543432[_param1 << 224].field_1792)
  mem[736] = bool(uint8(unknown0f543432[_param1 << 224].field_2048))
  mem[768] = bool(uint8(unknown0f543432[_param1 << 224].field_2056))
  mem[800] = uint256(unknown0f543432[_param1 << 224].field_2304)
  mem[832] = uint32(unknown0f543432[_param1 << 224].field_2560)
  mem[ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 992] = uint256(unknown0f543432[_param1 << 224].field_512)
  mem[ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 1024] = uint256(unknown0f543432[_param1 << 224].field_768)
  mem[ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 1056] = uint256(unknown0f543432[_param1 << 224].field_1024)
  mem[ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 1088] = uint32(unknown0f543432[_param1 << 224].field_2560)
  mem[ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 928] = 192
  mem[ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 1120] = unknown0f543432[_param1 << 224].length
  mem[ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 1152 len ceil32(unknown0f543432[_param1 << 224].length)] = mem[896 len ceil32(unknown0f543432[_param1 << 224].length)]
  mem[ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 960] = unknown0f543432[_param1 << 224].length + 224
  mem[unknown0f543432[_param1 << 224].length + ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 1152] = unknown0f543432[_param1 << 224][1].length
  mem[unknown0f543432[_param1 << 224].length + ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 1184 len ceil32(unknown0f543432[_param1 << 224][1].length)] = mem[ceil32(unknown0f543432[_param1 << 224].length) + 928 len ceil32(unknown0f543432[_param1 << 224][1].length)]
  if not unknown0f543432[_param1 << 224][1].length % 32:
      return Array(len=unknown0f543432[_param1 << 224].length, data=mem[896 len ceil32(unknown0f543432[_param1 << 224].length)], mem[(2 * ceil32(unknown0f543432[_param1 << 224].length)) + ceil32(unknown0f543432[_param1 << 224][1].length) + 1152 len unknown0f543432[_param1 << 224][1].length + unknown0f543432[_param1 << 224].length + -ceil32(unknown0f543432[_param1 << 224].length) + 32]), 
             unknown0f543432[_param1 << 224].length + 224,
             uint256(unknown0f543432[_param1 << 224].field_512),
             uint256(unknown0f543432[_param1 << 224].field_768),
             uint256(unknown0f543432[_param1 << 224].field_1024),
             uint32(unknown0f543432[_param1 << 224].field_2560)
  mem[floor32(unknown0f543432[_param1 << 224][1].length) + unknown0f543432[_param1 << 224].length + ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + 1184] = mem[floor32(unknown0f543432[_param1 << 224][1].length) + unknown0f543432[_param1 << 224].length + ceil32(unknown0f543432[_param1 << 224].length) + ceil32(unknown0f543432[_param1 << 224][1].length) + -unknown0f543432[_param1 << 224][1].length % 32 + 1216 len unknown0f543432[_param1 << 224][1].length % 32]
  return Array(len=unknown0f543432[_param1 << 224].length, data=mem[896 len ceil32(unknown0f543432[_param1 << 224].length)], mem[(2 * ceil32(unknown0f543432[_param1 << 224].length)) + ceil32(unknown0f543432[_param1 << 224][1].length) + 1152 len floor32(unknown0f543432[_param1 << 224][1].length) + unknown0f543432[_param1 << 224].length + -ceil32(unknown0f543432[_param1 << 224].length) + 64]), 
         unknown0f543432[_param1 << 224].length + 224,
         uint256(unknown0f543432[_param1 << 224].field_512),
         uint256(unknown0f543432[_param1 << 224].field_768),
         uint256(unknown0f543432[_param1 << 224].field_1024),
         uint32(unknown0f543432[_param1 << 224].field_2560)


# hash = 0x893d20e8
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def getOwner(): # not payable
  return owner


# hash = 0xbcda2a76
# getter = ['storage', 256, 0, ['add', 7, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknownbcda2a76(uint32 _param1): # not payable
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  return uint256(unknown0f543432[_param1 << 224].field_1792)


# hash = 0xc38cc8ff
# getter = None
# const = None
# payable = False
def unknownc38cc8ff(uint32 _param1): # not payable
  return (uint256(unknown0f543432[_param1 << 224].field_2304) > 0)


# hash = 0xc519b54b
# getter = ['storage', 8, 8, 5]
# const = None
# payable = False
def unknownc519b54b(): # not payable
  return unknownc519b54b


# hash = 0xc7fe2366
# getter = ['storage', 256, 0, ['add', 9, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknownc7fe2366(uint32 _param1): # not payable
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  return uint256(unknown0f543432[_param1 << 224].field_2304)


# hash = 0xcb50aa78
# getter = ['bool', ['storage', 8, 0, ['add', 8, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]]
# const = None
# payable = False
def unknowncb50aa78(uint32 _param1): # not payable
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  return bool(uint8(unknown0f543432[_param1 << 224].field_2048))


# hash = 0xcf1999da
# getter = ['storage', 256, 0, ['add', 4, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknowncf1999da(uint32 _param1): # not payable
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  return uint256(unknown0f543432[_param1 << 224].field_1024)


# hash = 0xd4e66db7
# getter = ['storage', 256, 0, ['add', 2, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknownd4e66db7(uint32 _param1): # not payable
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  return uint256(unknown0f543432[_param1 << 224].field_512)


# hash = 0xdb5a4e99
# getter = ['storage', 32, ['mask_shl', 3, 0, 5, ['cd', 4]], ['add', ['mask_shl', 253, 3, -3, ['cd', 4]], ['sha3', 4]]]
# const = None
# payable = False
def unknowndb5a4e99(uint256 _param1): # not payable
  require _param1 < stor4.length
  return unknowndb5a4e99[uint8(_param1)]


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


# hash = 0xe2491a34
# getter = None
# const = None
# payable = False
def unknowne2491a34(uint32 _param1, uint256 _param2, uint256 _param3): # not payable
  if uint256(unknown0f543432[_param1 << 224].field_2304) <= 0:
      return 0, 'Ticker not found'
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  if not uint8(unknown0f543432[_param1 << 224].field_2048):
      return 0, 'Trade for instrument is forbided'
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  if _param3 <′ 0:
      if not uint8(unknown0f543432[_param1 << 224].field_2056):
          return 0, 'Short for instrument is forbided'
  require ext_code.size(0xfe6134fa39466e8788ec310c2c1f3c2128c988be)
  [93mdelegate 0xfe6134fa39466e8788ec310c2c1f3c2128c988be.abs(int256 val) with:
       gas gas_remaining wei
      args _param3
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if delegate.return_data[0] < uint256(unknown0f543432[_param1 << 224].field_512):
      return 0, 'Volume too low'
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  require ext_code.size(0xfe6134fa39466e8788ec310c2c1f3c2128c988be)
  [93mdelegate 0xfe6134fa39466e8788ec310c2c1f3c2128c988be.abs(int256 val) with:
       gas gas_remaining wei
      args _param3
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require uint256(unknown0f543432[_param1 << 224].field_1024)
  if delegate.return_data[0] % uint256(unknown0f543432[_param1 << 224].field_1024):
      return 0, 'VolStep is not correct'
  if 0 >= uint256(unknown0f543432[_param1 << 224].field_2304):
      revert with 0, '25'
  if _param2 <= uint256(unknown0f543432[_param1 << 224].field_768):
      return 1, 0
  return 0, 'Aim volume too huge'


# hash = 0xe3b1e2fe
# getter = ['storage', 8, 16, 5]
# const = None
# payable = False
def unknowne3b1e2fe(): # not payable
  return unknowne3b1e2fe


# hash = 0xe530cb17
# getter = None
# const = None
# payable = False
def unknowne530cb17(uint32 _param1, uint256 _param2, uint256 _param3, uint256 _param4, bool _param5, bool _param6, uint256 _param7): # not payable
  if owner != caller:
      revert with 0, '1'
  require uint32(unknown0f543432[_param1 << 224].field_2560) > 0
  uint256(unknown0f543432[_param1 << 224].field_1280) = _param2
  uint256(unknown0f543432[_param1 << 224].field_1536) = _param3
  uint256(unknown0f543432[_param1 << 224].field_1792) = _param4
  uint8(unknown0f543432[_param1 << 224].field_2048) = uint8(_param5)
  Mask(248, 0, unknown0f543432[_param1 << 224].field_2056) = Mask(248, 0, _param6)
  Mask(240, 0, unknown0f543432[_param1 << 224].field_2064) = Mask(240, 16, _param5) >> 16
  uint256(unknown0f543432[_param1 << 224].field_2304) = _param7
  return 0


# hash = 0xe6dbd5f2
# getter = None
# const = None
# payable = False
def unknowne6dbd5f2(uint32 _param1, array _param2, array _param3, uint256 _param4, uint256 _param5, uint256 _param6, uint32 _param7): # not payable
  mem[128 len _param2.length] = _param2[all]
  mem[ceil32(_param2.length) + 128] = _param3.length
  mem[ceil32(_param2.length) + 160 len _param3.length] = _param3[all]
  if owner != caller:
      revert with 0, '1'
  uint256(unknown0f543432[_param1 << 224][].field_0) = Array(len=_param2.length, data=_param2[all])
  uint256(unknown0f543432[_param1 << 224][1][].field_0) = Array(len=_param3.length, data=_param3[all])
  uint256(unknown0f543432[_param1 << 224].field_512) = _param4
  uint256(unknown0f543432[_param1 << 224].field_768) = _param5
  uint256(unknown0f543432[_param1 << 224].field_1024) = _param6
  uint32(unknown0f543432[_param1 << 224].field_2560) = _param7
  uint256(unknown0f543432[_param1 << 224].field_1280) = 0
  uint256(unknown0f543432[_param1 << 224].field_1536) = 0
  uint256(unknown0f543432[_param1 << 224].field_1792) = 0
  uint16(unknown0f543432[_param1 << 224].field_2048) = 0
  uint256(unknown0f543432[_param1 << 224].field_2304) = 100
  mem[ceil32(_param2.length) + ceil32(_param3.length) + 160 len floor32(_param3.length)] = call.data[_param3 + 36 len floor32(_param3.length)]
  mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param3.length) + 160] = 256^(-(_param3.length % 32) + 32) - 1 and mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param3.length) + 160] or call.data[_param3 + floor32(_param3.length) + 36 len _param3.length % 32], mem[ceil32(_param2.length) + _param3.length + 160 len -(_param3.length % 32) + 32] and !(256^(-(_param3.length % 32) + 32) - 1)
  mem[ceil32(_param2.length) + ceil32(_param3.length) + _param3.length + 160] = 2
  [94m_1762 = sha3(call.data[_param3 + 36 len floor32(_param3.length)], mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param3.length) + 160 len (_param3.length % 32) + 32])
  mem[ceil32(_param2.length) + ceil32(_param3.length) + 160 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
  mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param2.length) + 160] = !(256^(-(_param2.length % 32) + 32) - 1) and call.data[_param2 + floor32(_param2.length) + 36 len _param2.length % 32], mem[_param2.length + 128 len -(_param2.length % 32) + 32] or 256^(-(_param2.length % 32) + 32) - 1 and mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param2.length) + 160]
  mem[_param2.length + ceil32(_param2.length) + ceil32(_param3.length) + 160] = [94m_1762
  uint32(stor[mem[ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param2.length) + 160 len (_param2.length % 32) + 32]][call.data[_param2 + 36 len floor32(_param2.length)]]) = _param1
  stor3.length++
  if 31 >= unknown0f543432[_param1 << 224].length:
      uint256(stor3[stor3.length].field_0) = uint256(unknown0f543432[_param1 << 224].field_0)
      [94midx = 0
      while stor3[stor3.length].length + 31 / 32 > [94midx:
          uint256(stor3[(11 * stor3.length) + [94midx].field_0) = 0
          [94midx = [94midx + 1
          continue 
      if 31 >= unknown0f543432[_param1 << 224][1].length:
          storC257[stor3.length] = uint256(unknown0f543432[_param1 << 224].field_256)
          [94midx = 0
          while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
              uint256(stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)]) = 0
              [94midx = [94midx + 1
              continue 
      else:
          storC257[stor3.length] = Mask(255, 1, (256 * not bool(unknown0f543432[_param1 << 224].field_256)) - 1 and uint256(unknown0f543432[_param1 << 224].field_256)) + 1
          if not Mask(255, 1, (256 * not bool(unknown0f543432[_param1 << 224].field_256)) - 1 and uint256(unknown0f543432[_param1 << 224].field_256)):
              [94midx = 0
              while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
                  uint256(stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)]) = 0
                  [94midx = [94midx + 1
                  continue 
          else:
              [94ms = 0
              [94midx = 0
              while unknown0f543432[_param1 << 224][1].length + 31 / 32 > [94midx:
                  uint256(stor[[94ms + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)]) = uint256(unknown0f543432[_param1 << 224][[94midx + 1].field_0)
                  [94ms = [94ms + 1
                  [94midx = [94midx + 1
                  continue 
              [94midx = unknown0f543432[_param1 << 224][1].length + 31 / 32
              while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
                  uint256(stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)]) = 0
                  [94midx = [94midx + 1
                  continue 
  else:
      uint256(stor3[stor3.length].field_0) = Mask(255, 1, uint256(unknown0f543432[_param1 << 224].field_0) and (256 * not bool(unknown0f543432[_param1 << 224].field_0)) - 1) + 1
      if not Mask(255, 1, uint256(unknown0f543432[_param1 << 224].field_0) and (256 * not bool(unknown0f543432[_param1 << 224].field_0)) - 1):
          [94midx = 0
          while stor3[stor3.length].length + 31 / 32 > [94midx:
              uint256(stor3[(11 * stor3.length) + [94midx].field_0) = 0
              [94midx = [94midx + 1
              continue 
      else:
          [94ms = 0
          [94midx = 0
          while unknown0f543432[_param1 << 224].length + 31 / 32 > [94midx:
              uint256(stor3[(11 * stor3.length) + [94ms].field_0) = uint256(unknown0f543432[_param1 << 224][[94midx].field_0)
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              continue 
          [94midx = unknown0f543432[_param1 << 224].length + 31 / 32
          while stor3[stor3.length].length + 31 / 32 > [94midx:
              uint256(stor3[(11 * stor3.length) + [94midx].field_0) = 0
              [94midx = [94midx + 1
              continue 
      if 31 >= unknown0f543432[_param1 << 224][1].length:
          storC257[stor3.length] = uint256(unknown0f543432[_param1 << 224].field_256)
          [94midx = 0
          while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
              uint256(stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)]) = 0
              [94midx = [94midx + 1
              continue 
      else:
          storC257[stor3.length] = Mask(255, 1, (256 * not bool(unknown0f543432[_param1 << 224].field_256)) - 1 and uint256(unknown0f543432[_param1 << 224].field_256)) + 1
          if not Mask(255, 1, (256 * not bool(unknown0f543432[_param1 << 224].field_256)) - 1 and uint256(unknown0f543432[_param1 << 224].field_256)):
              [94midx = 0
              while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
                  uint256(stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)]) = 0
                  [94midx = [94midx + 1
                  continue 
          else:
              [94ms = 0
              [94midx = 0
              while unknown0f543432[_param1 << 224][1].length + 31 / 32 > [94midx:
                  uint256(stor[[94ms + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)]) = uint256(unknown0f543432[_param1 << 224][[94midx + 1].field_0)
                  [94ms = [94ms + 1
                  [94midx = [94midx + 1
                  continue 
              [94midx = unknown0f543432[_param1 << 224][1].length + 31 / 32
              while stor[(11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4].length + 31 / 32 > [94midx:
                  uint256(stor[[94midx + sha3((11 * stor3.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)]) = 0
                  [94midx = [94midx + 1
                  continue 
  storC257[stor3.length] = uint256(unknown0f543432[_param1 << 224].field_512)
  storC257[stor3.length] = uint256(unknown0f543432[_param1 << 224].field_768)
  storC257[stor3.length] = uint256(unknown0f543432[_param1 << 224].field_1024)
  storC257[stor3.length] = uint256(unknown0f543432[_param1 << 224].field_1280)
  storC257[stor3.length] = uint256(unknown0f543432[_param1 << 224].field_1536)
  storC257[stor3.length] = uint256(unknown0f543432[_param1 << 224].field_1792)
  uint8(storC257[stor3.length].field_0) = uint8(bool(uint8(unknown0f543432[_param1 << 224].field_2048)))
  uint8(storC257[stor3.length].field_0) = uint8(bool(uint8(unknown0f543432[_param1 << 224].field_2048)))
  Mask(248, 0, storC257[stor3.length].field_8) = Mask(248, 0, bool(uint8(unknown0f543432[_param1 << 224].field_2056)))
  Mask(240, 0, storC257[stor3.length].field_16) = Mask(240, 16, bool(uint8(unknown0f543432[_param1 << 224].field_2048))) >> 16
  storC257[stor3.length] = uint256(unknown0f543432[_param1 << 224].field_2304)
  storC257[stor3.length] = uint32(unknown0f543432[_param1 << 224].field_2560)
  stor4.length++
  uint256(stor4[Mask(253, 0, stor4.length.field_3)].field_0) = uint256(stor4[Mask(253, 0, stor4.length.field_3)].field_0) and !(4294967295 * 256^(4 * stor4.length % 8)) or 256^(4 * stor4.length % 8) * _param1
  return 0


# hash = 0xef0b2368
# getter = None
# const = None
# payable = False
def unknownef0b2368(uint256 _param1): # not payable
  mem[128 len 1024] = code.data[9903 len 1024]
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


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


