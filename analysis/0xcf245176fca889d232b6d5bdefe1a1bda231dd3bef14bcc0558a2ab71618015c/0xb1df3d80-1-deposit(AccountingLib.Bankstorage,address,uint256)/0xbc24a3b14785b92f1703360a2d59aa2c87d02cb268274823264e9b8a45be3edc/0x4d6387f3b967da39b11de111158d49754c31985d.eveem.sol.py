# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x4d6387f3B967dA39B11DE111158D49754C31985d 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    unknown86086ba8 # mask: a s
    # storage address 3
    unknownc31bfcbb # mask: a s
    # storage address 4
    stor4
# hash = 0x02dc2e1d
# getter = None
# const = None
# payable = True
def queuePayment(bytes _bitcoinAddress) payable: 
  mem[128 len _bitcoinAddress.length] = _bitcoinAddress[all]
  if call.value < 10^17:
      call caller with:
         value call.value wei
           gas 0 wei
      return 0
  stor4[stor3].field_0 = _bitcoinAddress.length
  if not _bitcoinAddress.length:
      [94midx = 0
      while stor4[stor3].field_0 + 31 / 32 > [94midx:
          stor4[stor3][[94midx].field_0 = 0
          [94midx = [94midx + 1
          continue 
  else:
      [94ms = 0
      [94midx = 128
      while _bitcoinAddress.length + 128 > [94midx:
          stor4[stor3][[94ms].field_0 = mem[[94midx]
          [94ms = [94ms + 1
          [94midx = [94midx + 32
          continue 
      [94midx = Mask(251, 0, _bitcoinAddress.length + 31) >> 5
      while stor4[stor3].field_0 + 31 / 32 > [94midx:
          stor4[stor3][[94midx].field_0 = 0
          [94midx = [94midx + 1
          continue 
  stor4[stor3].field_256 = call.value
  addr(stor4[stor3].field_512) = caller
  log 0x2dba1d9e: unknownc31bfcbb
  unknownc31bfcbb++
  return 1


# hash = 0x26a18375
# getter = None
# const = None
# payable = True
def setAvailability(bool _available) payable: 
  if caller == stor0:
      if not _available:
          stor1 = 0
      else:
          stor1 = block.timestamp


# hash = 0x3ecbc1b7
# getter = None
# const = None
# payable = True
def unknown3ecbc1b7() payable: 
  return (block.timestamp - stor1 > 23 * 3600)


# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = True
def kill() payable: 
  if stor0 != caller:
      stop
  [93mselfdestruct([91mstor0[93m)


# hash = 0x856c71dd
# getter = None
# const = None
# payable = True
def isAvailable() payable: 
  return (block.timestamp - stor1 < 24 * 3600)


# hash = 0x86086ba8
# getter = ['storage', 256, 0, 2]
# const = None
# payable = True
def unknown86086ba8() payable: 
  return unknown86086ba8


# hash = 0x87d81789
# getter = None
# const = None
# payable = True
def payments(uint256 _param1) payable: 
  if not stor4[_param1].field_0:
      return 96, stor4[_param1].field_256, addr(stor4[_param1].field_512), stor4[_param1].field_0
  mem[224] = stor4[_param1].field_0
  [94midx = 224
  [94ms = 0
  while stor4[_param1].field_0 + 224 > [94midx + 32:
      mem[[94midx + 32] = stor4[_param1][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return Array(len=stor4[_param1].field_0, data=mem[224 len stor4[_param1].field_0 + (floor32(stor4[_param1].field_0 - 1) + -stor4[_param1].field_0 + 32 % 32)]), 
         stor4[_param1].field_256,
         addr(stor4[_param1].field_512)


# hash = 0xc31bfcbb
# getter = ['storage', 256, 0, 3]
# const = None
# payable = True
def unknownc31bfcbb() payable: 
  return unknownc31bfcbb


# hash = 0xf010264a
# getter = None
# const = None
# payable = True
def unknownf010264a(uint256 _param1, array _param2, uint256 _param3, addr _param4, addr _param5) payable: 
  mem[96] = _param2.length
  mem[128 len _param2.length] = _param2[all]
  if stor0 != caller:
      return 0
  if unknown86086ba8 >= unknownc31bfcbb:
      return 0
  if _param1 != unknown86086ba8:
      return 0
  if _param3 != stor4[_param1].field_256:
      return 0
  if stor4[_param1].field_0 != _param2.length:
      return 0
  mem[0] = _param1
  mem[32] = 4
  [94midx = 0
  while uint8([94midx) < stor4[_param1].field_0:
      require [94midx < _param2.length
      require [94midx < stor[sha3(mem[0 len 64])].field_0
      if Mask(8, -(('field', 3, ('stor', ('add', ('div', 0.03125, ('var', 0)), ('sha3', ('sha3', ('mem', ('range', 0, 64))))))), 0) + 256, [94midx % 32) << (('field', 3, ('stor', ('add', ('div', 0.03125, ('var', 0)), ('sha3', ('sha3', ('mem', ('range', 0, 64))))))), 0) - 8 != Mask(8, 248, mem[[94midx + 128]):
          return 0
      mem[0] = _param1
      mem[32] = 4
      [94midx = [94midx + 1
      continue 
  call _param4 with:
     value 5 * 10^15 wei
       gas 0 wei
  call _param5 with:
     value _param3 - 5 * 10^15 wei
       gas 0 wei
  unknown86086ba8++
  stor4[_param1].field_0 = 0
  [94ms = 0
  while sha3(sha3(_param1, 4)) + (stor4[_param1].field_0 + 31 / 32) > None:
      stor[None].field_0 = 0
      [94ms = None + 1
      continue 
  stor4[_param1].field_256 = 0
  addr(stor4[_param1].field_512) = 0
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


