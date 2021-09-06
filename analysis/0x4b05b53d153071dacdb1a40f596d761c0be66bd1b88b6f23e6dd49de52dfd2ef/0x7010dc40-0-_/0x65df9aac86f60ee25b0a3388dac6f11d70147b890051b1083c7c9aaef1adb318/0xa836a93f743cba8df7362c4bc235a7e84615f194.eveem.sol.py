# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xa836A93F743CBa8df7362c4bC235A7E84615f194 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x5923aa0a': 'unknown5923aa0a(?)'} 

# storage definitions
def storage:
    # storage address 1
    unknown0f543432
    # storage address 3
    stor3
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037085
    stor87903029871075914254377627908054574944891091886930582284385770809450030037085
    # storage address 99
    stor99
    # storage address 2
    unknown60bb4cbf
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037084
    stor87903029871075914254377627908054574944891091886930582284385770809450030037084
    # storage address 4
    stor4
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037087
    stor87903029871075914254377627908054574944891091886930582284385770809450030037087
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037093
    stor87903029871075914254377627908054574944891091886930582284385770809450030037093
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037091
    stor87903029871075914254377627908054574944891091886930582284385770809450030037091
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037088
    stor87903029871075914254377627908054574944891091886930582284385770809450030037088
    # storage address 5
    unknownc519b54b # mask: a s
    # storage address 5
    unknowne3b1e2fe # mask: a s
    # storage address 5
    unknownf887b097 # mask: a s
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037090
    stor87903029871075914254377627908054574944891091886930582284385770809450030037090
    # storage address 0
    owner # mask: a s
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037086
    stor87903029871075914254377627908054574944891091886930582284385770809450030037086
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037089
    stor87903029871075914254377627908054574944891091886930582284385770809450030037089
    # storage address 87903029871075914254377627908054574944891091886930582284385770809450030037092
    stor87903029871075914254377627908054574944891091886930582284385770809450030037092
# hash = 0x0977eb77
# getter = ['bool', ['storage', 8, 8, ['add', 8, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]]
# const = None
# payable = False
def unknown0977eb77(uint32 m_param1): # not payable
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  return bool(uint8(munknown0f543432m[m_param1 << 224m]m.field_2056))


# hash = 0x0f543432
# getter = ['storage', 32, 0, ['add', 10, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknown0f543432(uint32 m_param1): # not payable
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  return uint32(munknown0f543432m[m_param1 << 224m]m.field_2560)


# hash = 0x12081ef5
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def unknown12081ef5(uint32 m_param1): # not payable
  [94midx = 896
  [94ms = 0
  mwhile munknown0f543432m[m_param1 << 224m]m.length + 896 > [94midx + 32m:
      mem[[94midx + 32] = uint256(munknown0f543432m[m_param1 << 224m]m[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  [94midx = ceil32(munknown0f543432m[m_param1 << 224m]m.length) + 928
  [94ms = 0
  mwhile ceil32(munknown0f543432m[m_param1 << 224m]m.length) + munknown0f543432m[m_param1 << 224m]m[1m]m.length + 896 > [94midxm:
      mem[[94midx + 32] = uint256(munknown0f543432m[m_param1 << 224m]m[[94ms + 1m]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return uint256(munknown0f543432m[m_param1 << 224m]m.field_1280), 
         uint256(munknown0f543432m[m_param1 << 224m]m.field_1536),
         uint256(munknown0f543432m[m_param1 << 224m]m.field_1792),
         bool(uint8(munknown0f543432m[m_param1 << 224m]m.field_2048)),
         bool(uint8(munknown0f543432m[m_param1 << 224m]m.field_2056)),
         uint256(munknown0f543432m[m_param1 << 224m]m.field_2304)


# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address m_newOwner): # not payable
  if mowner != caller:
      revert with 0, '1'
  mowner = m_newOwner


# hash = 0x1635717c
# getter = None
# const = None
# payable = False
def unknown1635717c(): # not payable
  if not mstor4m.length:
      mem[(32 * mstor4m.length) + 128] = mstor4m.length
  else:
      mem[128 len 32 * mstor4m.length] = code.data[9903 len 32 * mstor4m.length]
      mem[(32 * mstor4m.length) + 128] = mstor4m.length
      mem[(32 * mstor4m.length) + 160 len 32 * mstor4m.length] = code.data[9903 len 32 * mstor4m.length]
  [94midx = 0
  mwhile [94midx < mstor4m.lengthm:
      require [94midx < mstor4m.length
      mem[(32 * [94midx) + 128] = mstor('array', ('div', 0.125, ('var', 0)), ('name', 'stor4', 4))m[uint8([94midx)m]
      require [94midx < mstor4m.length
      if 0 >= uint256(munknown0f543432m[uint32(mstor4m[0.125 / [94midxm]m.field_(32 * idx % 8) - 224)m]m.field_2304):
          revert with 0, '25'
      mem[0] = mstor('array', ('div', 0.125, ('var', 0)), ('name', 'stor4', 4))m[uint8([94midx)m]
      mem[32] = 1
      require [94midx < mem[(32 * mstor4m.length) + 128]
      mem[(32 * mstor4m.length) + (32 * [94midx) + 160] = uint32(munknown0f543432m[uint32(mstor4m[0.125 / [94midxm]m.field_(32 * idx % 8) - 224)m]m.field_2560)
      [94midx = [94midx + 1
      mcontinue 
  mem[(64 * mstor4m.length) + 160] = 64
  mem[(64 * mstor4m.length) + 224] = mstor4m.length
  mem[(64 * mstor4m.length) + 256 len floor32(mstor4m.length)] = mem[128 len floor32(mstor4m.length)]
  mem[(64 * mstor4m.length) + 192] = (32 * mstor4m.length) + 96
  mem[(98 * mstor4m.length) + 256] = mem[(32 * mstor4m.length) + 128]
  [94ms = 0
  mwhile mstor4m.length < 32 * mem[(32 * mstor4m.length) + 128]m:
      mem[(99 * mstor4m.length) + 288] = mem[(34 * mstor4m.length) + 160]
      [94ms = mstor4m.length + 32
      mcontinue 
  return memory
    from (64 * mstor4m.length) + 160
     [93mlen (32 * mem[(32 * mstor4m.length) + 128]) + (161 * mstor4m.length) + 128


# hash = 0x1719b3d5
# getter = None
# const = None
# payable = False
def unknown1719b3d5(uint32 m_param1): # not payable
  mem[32] = 1
  mem[96] = munknown0f543432m[m_param1m]m.length
  mem[0] = sha3(m_param1, 1)
  mem[128] = uint256(munknown0f543432m[m_param1m]m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile munknown0f543432m[m_param1m]m.length + 96 > [94midxm:
      mem[[94midx + 32] = uint256(munknown0f543432m[m_param1m]m[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[64] = ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 160
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + 128] = munknown0f543432m[m_param1m]m[1m]m.length
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + 160] = uint256(munknown0f543432m[m_param1m]m[1m]m.field_0)
  [94midx = ceil32(munknown0f543432m[m_param1m]m.length) + 160
  [94ms = 0
  mwhile ceil32(munknown0f543432m[m_param1m]m.length) + munknown0f543432m[m_param1m]m[1m]m.length + 128 > [94midxm:
      mem[[94midx + 32] = uint256(munknown0f543432m[m_param1m]m[[94ms + 1m]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 224] = uint256(munknown0f543432m[m_param1m]m.field_512)
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 256] = uint256(munknown0f543432m[m_param1m]m.field_768)
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 288] = uint256(munknown0f543432m[m_param1m]m.field_1024)
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 320] = uint256(munknown0f543432m[m_param1m]m.field_1280)
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 352] = uint256(munknown0f543432m[m_param1m]m.field_1536)
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 384] = uint256(munknown0f543432m[m_param1m]m.field_1792)
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 416] = bool(uint8(munknown0f543432m[m_param1m]m.field_2048))
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 448] = bool(uint8(munknown0f543432m[m_param1m]m.field_2056))
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 480] = uint256(munknown0f543432m[m_param1m]m.field_2304)
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 512] = uint32(munknown0f543432m[m_param1m]m.field_2560)
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 160] = 384
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 544] = munknown0f543432m[m_param1m]m.length
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 576 len ceil32(munknown0f543432m[m_param1m]m.length)] = mem[128 len ceil32(munknown0f543432m[m_param1m]m.length)]
  mem[ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 192] = munknown0f543432m[m_param1m]m.length + 416
  mem[munknown0f543432m[m_param1m]m.length + ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 576] = munknown0f543432m[m_param1m]m[1m]m.length
  mem[munknown0f543432m[m_param1m]m.length + ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 608 len ceil32(munknown0f543432m[m_param1m]m[1m]m.length)] = mem[ceil32(munknown0f543432m[m_param1m]m.length) + 160 len ceil32(munknown0f543432m[m_param1m]m[1m]m.length)]
  if not munknown0f543432m[m_param1m]m[1m]m.length % 32:
      return Array(len=munknown0f543432m[m_param1m]m.length, data=mem[128 len ceil32(munknown0f543432m[m_param1m]m.length)], mem[(2 * ceil32(munknown0f543432m[m_param1m]m.length)) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 576 len munknown0f543432m[m_param1m]m[1m]m.length + munknown0f543432m[m_param1m]m.length + -ceil32(munknown0f543432m[m_param1m]m.length) + 32]), 
             munknown0f543432m[m_param1m]m.length + 416,
             uint256(munknown0f543432m[m_param1m]m.field_512),
             uint256(munknown0f543432m[m_param1m]m.field_768),
             uint256(munknown0f543432m[m_param1m]m.field_1024),
             uint256(munknown0f543432m[m_param1m]m.field_1280),
             uint256(munknown0f543432m[m_param1m]m.field_1536),
             uint256(munknown0f543432m[m_param1m]m.field_1792),
             bool(uint8(munknown0f543432m[m_param1m]m.field_2048)),
             bool(uint8(munknown0f543432m[m_param1m]m.field_2056)),
             uint256(munknown0f543432m[m_param1m]m.field_2304),
             uint32(munknown0f543432m[m_param1m]m.field_2560)
  mem[floor32(munknown0f543432m[m_param1m]m[1m]m.length) + munknown0f543432m[m_param1m]m.length + ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 608] = mem[floor32(munknown0f543432m[m_param1m]m[1m]m.length) + munknown0f543432m[m_param1m]m.length + ceil32(munknown0f543432m[m_param1m]m.length) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + -munknown0f543432m[m_param1m]m[1m]m.length % 32 + 640 len munknown0f543432m[m_param1m]m[1m]m.length % 32]
  return Array(len=munknown0f543432m[m_param1m]m.length, data=mem[128 len ceil32(munknown0f543432m[m_param1m]m.length)], mem[(2 * ceil32(munknown0f543432m[m_param1m]m.length)) + ceil32(munknown0f543432m[m_param1m]m[1m]m.length) + 576 len floor32(munknown0f543432m[m_param1m]m[1m]m.length) + munknown0f543432m[m_param1m]m.length + -ceil32(munknown0f543432m[m_param1m]m.length) + 64]), 
         munknown0f543432m[m_param1m]m.length + 416,
         uint256(munknown0f543432m[m_param1m]m.field_512),
         uint256(munknown0f543432m[m_param1m]m.field_768),
         uint256(munknown0f543432m[m_param1m]m.field_1024),
         uint256(munknown0f543432m[m_param1m]m.field_1280),
         uint256(munknown0f543432m[m_param1m]m.field_1536),
         uint256(munknown0f543432m[m_param1m]m.field_1792),
         bool(uint8(munknown0f543432m[m_param1m]m.field_2048)),
         bool(uint8(munknown0f543432m[m_param1m]m.field_2056)),
         uint256(munknown0f543432m[m_param1m]m.field_2304),
         uint32(munknown0f543432m[m_param1m]m.field_2560)


# hash = 0x1ada4339
# getter = None
# const = None
# payable = False
def unknown1ada4339(uint32 m_param1): # not payable
  return (uint256(munknown0f543432m[m_param1 << 224m]m.field_2304) > 0)


# hash = 0x307e47cb
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknown307e47cb(uint32 m_param1): # not payable
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  return uint256(munknown0f543432m[m_param1 << 224m]m.field_768)


# hash = 0x370760ed
# getter = None
# const = None
# payable = False
def unknown370760ed(uint256 m_param1): # not payable
  require m_param1 < mstor3m.length
  mem[96] = mstor3m[m_param1m]m.length
  mem[0] = (11 * m_param1) + sha3(3)
  mem[128] = uint256(mstor3m[m_param1m]m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile mstor3m[m_param1m]m.length + 96 > [94midxm:
      mem[[94midx + 32] = uint256(mstor3m[(11 * m_param1) + [94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[64] = ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 160
  mem[ceil32(mstor3m[m_param1m]m.length) + 128] = mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length
  mem[ceil32(mstor3m[m_param1m]m.length) + 160] = uint256(mstor[sha3((11 * m_param1) + ('name', 'stor3', 3) + 1)m]m.field_0)
  [94midx = ceil32(mstor3m[m_param1m]m.length) + 160
  [94ms = 0
  mwhile ceil32(mstor3m[m_param1m]m.length) + mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length + 128 > [94midxm:
      mem[[94midx + 32] = uint256(mstor[[94ms + sha3((11 * m_param1) + ('name', 'stor3', 3) + 1)m]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 224] = uint256(mstor3m[m_param1m]m.field_512)
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 256] = uint256(mstor3m[m_param1m]m.field_768)
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 288] = uint256(mstor3m[m_param1m]m.field_1024)
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 320] = uint256(mstor3m[m_param1m]m.field_1280)
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 352] = uint256(mstor3m[m_param1m]m.field_1536)
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 384] = uint256(mstor3m[m_param1m]m.field_1792)
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 416] = bool(uint8(mstor3m[m_param1m]m.field_2048))
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 448] = bool(uint8(mstor3m[m_param1m]m.field_2056))
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 480] = uint256(mstor3m[m_param1m]m.field_2304)
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 512] = uint32(mstor3m[m_param1m]m.field_2560)
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 160] = 384
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 544] = mstor3m[m_param1m]m.length
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 576 len ceil32(mstor3m[m_param1m]m.length)] = mem[128 len ceil32(mstor3m[m_param1m]m.length)]
  mem[ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 192] = mstor3m[m_param1m]m.length + 416
  mem[mstor3m[m_param1m]m.length + ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 576] = mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length
  mem[mstor3m[m_param1m]m.length + ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 608 len ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length)] = mem[ceil32(mstor3m[m_param1m]m.length) + 160 len ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length)]
  if not mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length % 32:
      return Array(len=mstor3m[m_param1m]m.length, data=mem[128 len ceil32(mstor3m[m_param1m]m.length)], mem[(2 * ceil32(mstor3m[m_param1m]m.length)) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 576 len mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length + mstor3m[m_param1m]m.length + -ceil32(mstor3m[m_param1m]m.length) + 32]), 
             mstor3m[m_param1m]m.length + 416,
             uint256(mstor3m[m_param1m]m.field_512),
             uint256(mstor3m[m_param1m]m.field_768),
             uint256(mstor3m[m_param1m]m.field_1024),
             uint256(mstor3m[m_param1m]m.field_1280),
             uint256(mstor3m[m_param1m]m.field_1536),
             uint256(mstor3m[m_param1m]m.field_1792),
             bool(uint8(mstor3m[m_param1m]m.field_2048)),
             bool(uint8(mstor3m[m_param1m]m.field_2056)),
             uint256(mstor3m[m_param1m]m.field_2304),
             uint32(mstor3m[m_param1m]m.field_2560)
  mem[floor32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + mstor3m[m_param1m]m.length + ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 608] = mem[floor32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + mstor3m[m_param1m]m.length + ceil32(mstor3m[m_param1m]m.length) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + -mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length % 32 + 640 len mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length % 32]
  return Array(len=mstor3m[m_param1m]m.length, data=mem[128 len ceil32(mstor3m[m_param1m]m.length)], mem[(2 * ceil32(mstor3m[m_param1m]m.length)) + ceil32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + 576 len floor32(mstor[(11 * m_param1) + ('name', 'stor3', 3) + 1m]m.length) + mstor3m[m_param1m]m.length + -ceil32(mstor3m[m_param1m]m.length) + 64]), 
         mstor3m[m_param1m]m.length + 416,
         uint256(mstor3m[m_param1m]m.field_512),
         uint256(mstor3m[m_param1m]m.field_768),
         uint256(mstor3m[m_param1m]m.field_1024),
         uint256(mstor3m[m_param1m]m.field_1280),
         uint256(mstor3m[m_param1m]m.field_1536),
         uint256(mstor3m[m_param1m]m.field_1792),
         bool(uint8(mstor3m[m_param1m]m.field_2048)),
         bool(uint8(mstor3m[m_param1m]m.field_2056)),
         uint256(mstor3m[m_param1m]m.field_2304),
         uint32(mstor3m[m_param1m]m.field_2560)


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
  return munknownf887b097, munknownf887b097, munknowne3b1e2fe


# hash = 0x60bb4cbf
# getter = ['storage', 32, 0, ['sha3', ['data', ['call.data', ['add', 36, ['cd', 36]], ['cd', ['add', 4, ['cd', 36]]]], ['sha3', ['data', ['call.data', ['add', 36, ['cd', 4]], ['cd', ['add', 4, ['cd', 4]]]], 2]]]]]
# const = None
# payable = False
def unknown60bb4cbf(array m_param1, array m_param2): # not payable
  return munknown60bb4cbfm[m_param1[allm]m]m[m_param2[allm]m]


# hash = 0x63276d6e
# getter = None
# const = None
# payable = False
def unknown63276d6e(uint32 m_param1): # not payable
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
  mem[864] = munknown0f543432m[m_param1 << 224m]m.length
  mem[896] = uint256(munknown0f543432m[m_param1 << 224m]m.field_0)
  [94midx = 896
  [94ms = 0
  mwhile munknown0f543432m[m_param1 << 224m]m.length + 896 > [94midx + 32m:
      mem[[94midx + 32] = uint256(munknown0f543432m[m_param1 << 224m]m[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[480] = 864
  mem[64] = ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 928
  mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + 896] = munknown0f543432m[m_param1 << 224m]m[1m]m.length
  mem[0] = sha3(m_param1 << 224, 1) + 1
  mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + 928] = uint256(munknown0f543432m[m_param1 << 224m]m[1m]m.field_0)
  [94midx = ceil32(munknown0f543432m[m_param1 << 224m]m.length) + 928
  [94ms = 0
  mwhile ceil32(munknown0f543432m[m_param1 << 224m]m.length) + munknown0f543432m[m_param1 << 224m]m[1m]m.length + 896 > [94midxm:
      mem[[94midx + 32] = uint256(munknown0f543432m[m_param1 << 224m]m[[94ms + 1m]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[512] = ceil32(munknown0f543432m[m_param1 << 224m]m.length) + 896
  mem[544] = uint256(munknown0f543432m[m_param1 << 224m]m.field_512)
  mem[576] = uint256(munknown0f543432m[m_param1 << 224m]m.field_768)
  mem[608] = uint256(munknown0f543432m[m_param1 << 224m]m.field_1024)
  mem[640] = uint256(munknown0f543432m[m_param1 << 224m]m.field_1280)
  mem[672] = uint256(munknown0f543432m[m_param1 << 224m]m.field_1536)
  mem[704] = uint256(munknown0f543432m[m_param1 << 224m]m.field_1792)
  mem[736] = bool(uint8(munknown0f543432m[m_param1 << 224m]m.field_2048))
  mem[768] = bool(uint8(munknown0f543432m[m_param1 << 224m]m.field_2056))
  mem[800] = uint256(munknown0f543432m[m_param1 << 224m]m.field_2304)
  mem[832] = uint32(munknown0f543432m[m_param1 << 224m]m.field_2560)
  mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 992] = uint256(munknown0f543432m[m_param1 << 224m]m.field_512)
  mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 1024] = uint256(munknown0f543432m[m_param1 << 224m]m.field_768)
  mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 1056] = uint256(munknown0f543432m[m_param1 << 224m]m.field_1024)
  mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 1088] = uint32(munknown0f543432m[m_param1 << 224m]m.field_2560)
  mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 928] = 192
  mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 1120] = munknown0f543432m[m_param1 << 224m]m.length
  mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 1152 len ceil32(munknown0f543432m[m_param1 << 224m]m.length)] = mem[896 len ceil32(munknown0f543432m[m_param1 << 224m]m.length)]
  mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 960] = munknown0f543432m[m_param1 << 224m]m.length + 224
  mem[munknown0f543432m[m_param1 << 224m]m.length + ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 1152] = munknown0f543432m[m_param1 << 224m]m[1m]m.length
  mem[munknown0f543432m[m_param1 << 224m]m.length + ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 1184 len ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length)] = mem[ceil32(munknown0f543432m[m_param1 << 224m]m.length) + 928 len ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length)]
  if not munknown0f543432m[m_param1 << 224m]m[1m]m.length % 32:
      return Array(len=munknown0f543432m[m_param1 << 224m]m.length, data=mem[896 len ceil32(munknown0f543432m[m_param1 << 224m]m.length)], mem[(2 * ceil32(munknown0f543432m[m_param1 << 224m]m.length)) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 1152 len munknown0f543432m[m_param1 << 224m]m[1m]m.length + munknown0f543432m[m_param1 << 224m]m.length + -ceil32(munknown0f543432m[m_param1 << 224m]m.length) + 32]), 
             munknown0f543432m[m_param1 << 224m]m.length + 224,
             uint256(munknown0f543432m[m_param1 << 224m]m.field_512),
             uint256(munknown0f543432m[m_param1 << 224m]m.field_768),
             uint256(munknown0f543432m[m_param1 << 224m]m.field_1024),
             uint32(munknown0f543432m[m_param1 << 224m]m.field_2560)
  mem[floor32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + munknown0f543432m[m_param1 << 224m]m.length + ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 1184] = mem[floor32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + munknown0f543432m[m_param1 << 224m]m.length + ceil32(munknown0f543432m[m_param1 << 224m]m.length) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + -munknown0f543432m[m_param1 << 224m]m[1m]m.length % 32 + 1216 len munknown0f543432m[m_param1 << 224m]m[1m]m.length % 32]
  return Array(len=munknown0f543432m[m_param1 << 224m]m.length, data=mem[896 len ceil32(munknown0f543432m[m_param1 << 224m]m.length)], mem[(2 * ceil32(munknown0f543432m[m_param1 << 224m]m.length)) + ceil32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + 1152 len floor32(munknown0f543432m[m_param1 << 224m]m[1m]m.length) + munknown0f543432m[m_param1 << 224m]m.length + -ceil32(munknown0f543432m[m_param1 << 224m]m.length) + 64]), 
         munknown0f543432m[m_param1 << 224m]m.length + 224,
         uint256(munknown0f543432m[m_param1 << 224m]m.field_512),
         uint256(munknown0f543432m[m_param1 << 224m]m.field_768),
         uint256(munknown0f543432m[m_param1 << 224m]m.field_1024),
         uint32(munknown0f543432m[m_param1 << 224m]m.field_2560)


# hash = 0x893d20e8
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def getOwner(): # not payable
  return mowner


# hash = 0xbcda2a76
# getter = ['storage', 256, 0, ['add', 7, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknownbcda2a76(uint32 m_param1): # not payable
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  return uint256(munknown0f543432m[m_param1 << 224m]m.field_1792)


# hash = 0xc38cc8ff
# getter = None
# const = None
# payable = False
def unknownc38cc8ff(uint32 m_param1): # not payable
  return (uint256(munknown0f543432m[m_param1 << 224m]m.field_2304) > 0)


# hash = 0xc519b54b
# getter = ['storage', 8, 8, 5]
# const = None
# payable = False
def unknownc519b54b(): # not payable
  return munknownc519b54b


# hash = 0xc7fe2366
# getter = ['storage', 256, 0, ['add', 9, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknownc7fe2366(uint32 m_param1): # not payable
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  return uint256(munknown0f543432m[m_param1 << 224m]m.field_2304)


# hash = 0xcb50aa78
# getter = ['bool', ['storage', 8, 0, ['add', 8, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]]
# const = None
# payable = False
def unknowncb50aa78(uint32 m_param1): # not payable
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  return bool(uint8(munknown0f543432m[m_param1 << 224m]m.field_2048))


# hash = 0xcf1999da
# getter = ['storage', 256, 0, ['add', 4, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknowncf1999da(uint32 m_param1): # not payable
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  return uint256(munknown0f543432m[m_param1 << 224m]m.field_1024)


# hash = 0xd4e66db7
# getter = ['storage', 256, 0, ['add', 2, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 1]]]]
# const = None
# payable = False
def unknownd4e66db7(uint32 m_param1): # not payable
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  return uint256(munknown0f543432m[m_param1 << 224m]m.field_512)


# hash = 0xdb5a4e99
# getter = ['storage', 32, ['mask_shl', 3, 0, 5, ['cd', 4]], ['add', ['mask_shl', 253, 3, -3, ['cd', 4]], ['sha3', 4]]]
# const = None
# payable = False
def unknowndb5a4e99(uint256 m_param1): # not payable
  require m_param1 < mstor4m.length
  return munknowndb5a4e99m[uint8(m_param1)m]


# hash = 0xdf7c6650
# getter = None
# const = None
# payable = False
def unknowndf7c6650(uint8 m_param1, uint8 m_param2, uint8 m_param3): # not payable
  if mowner != caller:
      revert with 0, '1'
  munknownf887b097 = m_param1
  munknownc519b54b = m_param2
  munknowne3b1e2fe = m_param3


# hash = 0xe2491a34
# getter = None
# const = None
# payable = False
def unknowne2491a34(uint32 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  if uint256(munknown0f543432m[m_param1 << 224m]m.field_2304) <= 0:
      return 0, 'Ticker not found'
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  if not uint8(munknown0f543432m[m_param1 << 224m]m.field_2048):
      return 0, 'Trade for instrument is forbided'
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  if m_param3 <′ 0:
      if not uint8(munknown0f543432m[m_param1 << 224m]m.field_2056):
          return 0, 'Short for instrument is forbided'
  require ext_code.size(0x4454205ecd208cc580643bcd6bf710c9009b5a34)
  [93mdelegate 0x4454205ecd208cc580643bcd6bf710c9009b5a34.abs(int256 val) with:
       gas gas_remaining wei
      args m_param3
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if delegate.return_data[0] < uint256(munknown0f543432m[m_param1 << 224m]m.field_512):
      return 0, 'Volume too low'
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  require ext_code.size(0x4454205ecd208cc580643bcd6bf710c9009b5a34)
  [93mdelegate 0x4454205ecd208cc580643bcd6bf710c9009b5a34.abs(int256 val) with:
       gas gas_remaining wei
      args m_param3
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require uint256(munknown0f543432m[m_param1 << 224m]m.field_1024)
  if delegate.return_data[0] % uint256(munknown0f543432m[m_param1 << 224m]m.field_1024):
      return 0, 'VolStep is not correct'
  if 0 >= uint256(munknown0f543432m[m_param1 << 224m]m.field_2304):
      revert with 0, '25'
  if m_param2 <= uint256(munknown0f543432m[m_param1 << 224m]m.field_768):
      return 1, 0
  return 0, 'Aim volume too huge'


# hash = 0xe3b1e2fe
# getter = ['storage', 8, 16, 5]
# const = None
# payable = False
def unknowne3b1e2fe(): # not payable
  return munknowne3b1e2fe


# hash = 0xe530cb17
# getter = None
# const = None
# payable = False
def unknowne530cb17(uint32 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, bool m_param5, bool m_param6, uint256 m_param7): # not payable
  if mowner != caller:
      revert with 0, '1'
  require uint32(munknown0f543432m[m_param1 << 224m]m.field_2560) > 0
  uint256(munknown0f543432m[m_param1 << 224m]m.field_1280) = m_param2
  uint256(munknown0f543432m[m_param1 << 224m]m.field_1536) = m_param3
  uint256(munknown0f543432m[m_param1 << 224m]m.field_1792) = m_param4
  uint8(munknown0f543432m[m_param1 << 224m]m.field_2048) = uint8(m_param5)
  Mask(248, 0, munknown0f543432m[m_param1 << 224m]m.field_2056) = Mask(248, 0, m_param6)
  Mask(240, 0, munknown0f543432m[m_param1 << 224m]m.field_2064) = Mask(240, 16, m_param5) >> 16
  uint256(munknown0f543432m[m_param1 << 224m]m.field_2304) = m_param7
  return 0


# hash = 0xe6dbd5f2
# getter = None
# const = None
# payable = False
def unknowne6dbd5f2(uint32 m_param1, array m_param2, array m_param3, uint256 m_param4, uint256 m_param5, uint256 m_param6, uint32 m_param7): # not payable
  mem[128 len m_param2.length] = m_param2[allm]
  mem[ceil32(m_param2.length) + 128] = m_param3.length
  mem[ceil32(m_param2.length) + 160 len m_param3.length] = m_param3[allm]
  if mowner != caller:
      revert with 0, '1'
  uint256(munknown0f543432m[m_param1 << 224m]m[m]m.field_0) = Array(len=m_param2.length, data=m_param2[allm])
  uint256(munknown0f543432m[m_param1 << 224m]m[1m]m[m]m.field_0) = Array(len=m_param3.length, data=m_param3[allm])
  uint256(munknown0f543432m[m_param1 << 224m]m.field_512) = m_param4
  uint256(munknown0f543432m[m_param1 << 224m]m.field_768) = m_param5
  uint256(munknown0f543432m[m_param1 << 224m]m.field_1024) = m_param6
  uint32(munknown0f543432m[m_param1 << 224m]m.field_2560) = m_param7
  uint256(munknown0f543432m[m_param1 << 224m]m.field_1280) = 0
  uint256(munknown0f543432m[m_param1 << 224m]m.field_1536) = 0
  uint256(munknown0f543432m[m_param1 << 224m]m.field_1792) = 0
  uint16(munknown0f543432m[m_param1 << 224m]m.field_2048) = 0
  uint256(munknown0f543432m[m_param1 << 224m]m.field_2304) = 100
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 160 len floor32(m_param3.length)] = call.data[m_param3 + 36 len floor32(m_param3.length)]
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + floor32(m_param3.length) + 160] = 256^(-(m_param3.length % 32) + 32) - 1 and mem[ceil32(m_param2.length) + ceil32(m_param3.length) + floor32(m_param3.length) + 160] or call.data[m_param3 + floor32(m_param3.length) + 36 len m_param3.length % 32], mem[ceil32(m_param2.length) + m_param3.length + 160 len -(m_param3.length % 32) + 32] and !(256^(-(m_param3.length % 32) + 32) - 1)
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + m_param3.length + 160] = 2
  [94m_1762 = sha3(call.data[m_param3 + 36 len floor32(m_param3.length)], mem[ceil32(m_param2.length) + ceil32(m_param3.length) + floor32(m_param3.length) + 160 len (m_param3.length % 32) + 32])
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 160 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + floor32(m_param2.length) + 160] = !(256^(-(m_param2.length % 32) + 32) - 1) and call.data[m_param2 + floor32(m_param2.length) + 36 len m_param2.length % 32], mem[m_param2.length + 128 len -(m_param2.length % 32) + 32] or 256^(-(m_param2.length % 32) + 32) - 1 and mem[ceil32(m_param2.length) + ceil32(m_param3.length) + floor32(m_param2.length) + 160]
  mem[m_param2.length + ceil32(m_param2.length) + ceil32(m_param3.length) + 160] = [94m_1762
  uint32(mstor[mem[ceil32(m_param2.length) + ceil32(m_param3.length) + floor32(m_param2.length) + 160 len (m_param2.length % 32) + 32]m]m[call.data[m_param2 + 36 len floor32(m_param2.length)]m]) = m_param1
  mstor3m.length++
  if 31 >= munknown0f543432m[m_param1 << 224m]m.length:
      uint256(mstor3m[mstor3m.lengthm]m.field_0) = uint256(munknown0f543432m[m_param1 << 224m]m.field_0)
      [94midx = 0
      mwhile mstor3m[mstor3m.lengthm]m.length + 31 / 32 > [94midxm:
          uint256(mstor3m[(11 * mstor3m.length) + [94midxm]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 
      if 31 >= munknown0f543432m[m_param1 << 224m]m[1m]m.length:
          mstorC257m[mstor3m.lengthm] = uint256(munknown0f543432m[m_param1 << 224m]m.field_256)
          [94midx = 0
          mwhile mstor[(11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4m]m.length + 31 / 32 > [94midxm:
              uint256(mstor[[94midx + sha3((11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)m]) = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          mstorC257m[mstor3m.lengthm] = Mask(255, 1, (256 * not bool(munknown0f543432m[m_param1 << 224m]m.field_256)) - 1 and uint256(munknown0f543432m[m_param1 << 224m]m.field_256)) + 1
          if not Mask(255, 1, (256 * not bool(munknown0f543432m[m_param1 << 224m]m.field_256)) - 1 and uint256(munknown0f543432m[m_param1 << 224m]m.field_256)):
              [94midx = 0
              mwhile mstor[(11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4m]m.length + 31 / 32 > [94midxm:
                  uint256(mstor[[94midx + sha3((11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)m]) = 0
                  [94midx = [94midx + 1
                  mcontinue 
          else:
              [94ms = 0
              [94midx = 0
              mwhile munknown0f543432m[m_param1 << 224m]m[1m]m.length + 31 / 32 > [94midxm:
                  uint256(mstor[[94ms + sha3((11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)m]) = uint256(munknown0f543432m[m_param1 << 224m]m[[94midx + 1m]m.field_0)
                  [94ms = [94ms + 1
                  [94midx = [94midx + 1
                  mcontinue 
              [94midx = munknown0f543432m[m_param1 << 224m]m[1m]m.length + 31 / 32
              mwhile mstor[(11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4m]m.length + 31 / 32 > [94midxm:
                  uint256(mstor[[94midx + sha3((11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)m]) = 0
                  [94midx = [94midx + 1
                  mcontinue 
  else:
      uint256(mstor3m[mstor3m.lengthm]m.field_0) = Mask(255, 1, uint256(munknown0f543432m[m_param1 << 224m]m.field_0) and (256 * not bool(munknown0f543432m[m_param1 << 224m]m.field_0)) - 1) + 1
      if not Mask(255, 1, uint256(munknown0f543432m[m_param1 << 224m]m.field_0) and (256 * not bool(munknown0f543432m[m_param1 << 224m]m.field_0)) - 1):
          [94midx = 0
          mwhile mstor3m[mstor3m.lengthm]m.length + 31 / 32 > [94midxm:
              uint256(mstor3m[(11 * mstor3m.length) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          [94ms = 0
          [94midx = 0
          mwhile munknown0f543432m[m_param1 << 224m]m.length + 31 / 32 > [94midxm:
              uint256(mstor3m[(11 * mstor3m.length) + [94msm]m.field_0) = uint256(munknown0f543432m[m_param1 << 224m]m[[94midxm]m.field_0)
              [94ms = [94ms + 1
              [94midx = [94midx + 1
              mcontinue 
          [94midx = munknown0f543432m[m_param1 << 224m]m.length + 31 / 32
          mwhile mstor3m[mstor3m.lengthm]m.length + 31 / 32 > [94midxm:
              uint256(mstor3m[(11 * mstor3m.length) + [94midxm]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
      if 31 >= munknown0f543432m[m_param1 << 224m]m[1m]m.length:
          mstorC257m[mstor3m.lengthm] = uint256(munknown0f543432m[m_param1 << 224m]m.field_256)
          [94midx = 0
          mwhile mstor[(11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4m]m.length + 31 / 32 > [94midxm:
              uint256(mstor[[94midx + sha3((11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)m]) = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          mstorC257m[mstor3m.lengthm] = Mask(255, 1, (256 * not bool(munknown0f543432m[m_param1 << 224m]m.field_256)) - 1 and uint256(munknown0f543432m[m_param1 << 224m]m.field_256)) + 1
          if not Mask(255, 1, (256 * not bool(munknown0f543432m[m_param1 << 224m]m.field_256)) - 1 and uint256(munknown0f543432m[m_param1 << 224m]m.field_256)):
              [94midx = 0
              mwhile mstor[(11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4m]m.length + 31 / 32 > [94midxm:
                  uint256(mstor[[94midx + sha3((11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)m]) = 0
                  [94midx = [94midx + 1
                  mcontinue 
          else:
              [94ms = 0
              [94midx = 0
              mwhile munknown0f543432m[m_param1 << 224m]m[1m]m.length + 31 / 32 > [94midxm:
                  uint256(mstor[[94ms + sha3((11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)m]) = uint256(munknown0f543432m[m_param1 << 224m]m[[94midx + 1m]m.field_0)
                  [94ms = [94ms + 1
                  [94midx = [94midx + 1
                  mcontinue 
              [94midx = munknown0f543432m[m_param1 << 224m]m[1m]m.length + 31 / 32
              mwhile mstor[(11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4m]m.length + 31 / 32 > [94midxm:
                  uint256(mstor[[94midx + sha3((11 * mstor3m.length) - 0x3da8a5f161a6c3ff06a60736d0ed24d7963cc6a5c4fafd2fa1dae9bb908e07a4)m]) = 0
                  [94midx = [94midx + 1
                  mcontinue 
  mstorC257m[mstor3m.lengthm] = uint256(munknown0f543432m[m_param1 << 224m]m.field_512)
  mstorC257m[mstor3m.lengthm] = uint256(munknown0f543432m[m_param1 << 224m]m.field_768)
  mstorC257m[mstor3m.lengthm] = uint256(munknown0f543432m[m_param1 << 224m]m.field_1024)
  mstorC257m[mstor3m.lengthm] = uint256(munknown0f543432m[m_param1 << 224m]m.field_1280)
  mstorC257m[mstor3m.lengthm] = uint256(munknown0f543432m[m_param1 << 224m]m.field_1536)
  mstorC257m[mstor3m.lengthm] = uint256(munknown0f543432m[m_param1 << 224m]m.field_1792)
  uint8(mstorC257m[mstor3m.lengthm]m.field_0) = uint8(bool(uint8(munknown0f543432m[m_param1 << 224m]m.field_2048)))
  uint8(mstorC257m[mstor3m.lengthm]m.field_0) = uint8(bool(uint8(munknown0f543432m[m_param1 << 224m]m.field_2048)))
  Mask(248, 0, mstorC257m[mstor3m.lengthm]m.field_8) = Mask(248, 0, bool(uint8(munknown0f543432m[m_param1 << 224m]m.field_2056)))
  Mask(240, 0, mstorC257m[mstor3m.lengthm]m.field_16) = Mask(240, 16, bool(uint8(munknown0f543432m[m_param1 << 224m]m.field_2048))) >> 16
  mstorC257m[mstor3m.lengthm] = uint256(munknown0f543432m[m_param1 << 224m]m.field_2304)
  mstorC257m[mstor3m.lengthm] = uint32(munknown0f543432m[m_param1 << 224m]m.field_2560)
  mstor4m.length++
  uint256(mstor4m[Mask(253, 0, mstor4m.lengthm.field_3)m]m.field_0) = uint256(mstor4m[Mask(253, 0, mstor4m.lengthm.field_3)m]m.field_0) and !(4294967295 * 256^(4 * mstor4m.length % 8)) or 256^(4 * mstor4m.length % 8) * m_param1
  return 0


# hash = 0xef0b2368
# getter = None
# const = None
# payable = False
def unknownef0b2368(uint256 m_param1): # not payable
  mem[128 len 1024] = code.data[9903 len 1024]
  [94midx = 0
  mwhile [94midx < 32m:
      require [94midx < 32
      mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, ('add', 256, ('mul', -1, (('mask_shl', 256, 0, -3, ('param', '_param1')), 0))), ('add', -11, (('mask_shl', 256, 0, -3, ('param', '_param1')), 0)), ('var', 0)), 0) + 256, 0) << (('mask_shl', 8, ('add', 256, ('mul', -1, (('mask_shl', 256, 0, -3, ('param', '_param1')), 0))), ('add', -11, (('mask_shl', 256, 0, -3, ('param', '_param1')), 0)), ('var', 0)), 0) - 256
      [94midx = [94midx + 1
      mcontinue 
  return 32, 32, mem[128]


# hash = 0xf887b097
# getter = ['storage', 8, 0, 5]
# const = None
# payable = False
def unknownf887b097(): # not payable
  return munknownf887b097


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


