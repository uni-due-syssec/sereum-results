# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xFC4f24fBedBdFff1eEaA3C279c72355f36D2f4F2 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    unknown10fe6584Address # mask: a s
    # storage address 2
    unknownd1bd1d6eAddress # mask: a s
    # storage address 3
    unknown7db65b17
    # storage address 4
    unknown0b0db12d
    # storage address 5
    unknownd974081f
    # storage address 6
    unknown78914887
    # storage address 7
    unknown9801354f
    # storage address 8
    unknown4cf667d9
    # storage address 9
    unknownb00a6d92 # mask: a s
    # storage address 10
    unknown2881178b # mask: a s
    # storage address 11
    stor11
    # storage address 12
    stor12
    # storage address 13
    unknowncf39918e
# hash = 0x042cefc1
# getter = None
# const = None
# payable = False
def unknown042cefc1(uint8 _param1, addr _param2): # not payable
  [94midx = 0
  [94ms = 0
  while [94midx < stor12.length:
      mem[0] = 12
      if stor12[[94midx] != caller:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = 1
      continue 
  if 0 >= stor12.length:
      revert with 0, '8'
  if bool([94ms) != 1:
      revert with 0, '8'
  stor11[_param1 + 255][caller] = _param2
  [94midx = 0
  [94ms = 0
  while [94midx < stor12.length:
      mem[0] = stor12[[94midx]
      mem[32] = sha3(_param1 + 255, 11)
      if stor11[_param1 + 255][stor12[[94midx]] != _param2:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  if [94ms >=′ 3:
      unknown0b0db12d[stor3[_param1 << 248]] = 0
      unknown7db65b17[_param1 << 248] = _param2
      unknown0b0db12d[_param2] = _param1


# hash = 0x07f67dbd
# getter = None
# const = None
# payable = False
def unknown07f67dbd(uint8 _param1, addr _param2): # not payable
  [94midx = 0
  [94ms = 0
  while [94midx < stor12.length:
      mem[0] = 12
      if stor12[[94midx] != caller:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = 1
      continue 
  if 0 >= stor12.length:
      revert with 0, '8'
  if bool([94ms) != 1:
      revert with 0, '8'
  stor11[_param1 + 510][caller] = _param2
  [94midx = 0
  [94ms = 0
  while [94midx < stor12.length:
      mem[0] = stor12[[94midx]
      mem[32] = sha3(_param1 + 510, 11)
      if stor11[_param1 + 510][stor12[[94midx]] != _param2:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  if [94ms >=′ 3:
      unknownd974081f[_param1 << 248] = _param2


# hash = 0x0b0db12d
# getter = ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = False
def unknown0b0db12d(addr _param1): # not payable
  return unknown0b0db12d[_param1]


# hash = 0x10fe6584
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown10fe6584(): # not payable
  return unknown10fe6584Address


# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address _newOwner): # not payable
  if owner != caller:
      revert with 0, '1'
  owner = _newOwner


# hash = 0x2881178b
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknown2881178b(): # not payable
  return unknown2881178b


# hash = 0x2d8815c8
# getter = None
# const = None
# payable = True
def unknown2d8815c8() payable: 
  call unknownd1bd1d6eAddress with:
     value call.value / 2 wei
       gas gas_remaining wei
  unknownb00a6d92 += call.value / 2
  unknown2881178b += call.value / 2


# hash = 0x2fe6a1e6
# getter = None
# const = None
# payable = True
def unknown2fe6a1e6() payable: 
  stop


# hash = 0x4cf667d9
# getter = ['storage', 160, 0, ['add', ['sha3', 8], ['cd', 4]]]
# const = None
# payable = False
def unknown4cf667d9(uint256 _param1): # not payable
  require _param1 < unknown4cf667d9.length
  return unknown4cf667d9[_param1]


# hash = 0x5fecf62c
# getter = None
# const = None
# payable = True
def unknown5fecf62c() payable: 
  stop


# hash = 0x781851a7
# getter = None
# const = None
# payable = False
def unknown781851a7(array _param1, array _param2): # not payable
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = _param2.length
  mem[(32 * _param1.length) + 160 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  if owner != caller:
      revert with 0, '1'
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param2.length
      require [94midx < _param1.length
      mem[0] = mem[(32 * [94midx) + 128]
      mem[32] = 13
      unknowncf39918e[mem[(32 * [94midx) + 128]] = mem[(32 * [94midx) + (32 * _param1.length) + 160]
      [94midx = [94midx + 1
      continue 


# hash = 0x78914887
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def unknown78914887(addr _param1): # not payable
  return unknown78914887[_param1]


# hash = 0x798cc26a
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknown798cc26a(): # not payable
  return owner


# hash = 0x7db65b17
# getter = ['storage', 160, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 3]]]
# const = None
# payable = False
def unknown7db65b17(uint8 _param1): # not payable
  return unknown7db65b17[_param1 << 248]


# hash = 0x841586e0
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def unknown841586e0(): # not payable
  return unknown4cf667d9.length


# hash = 0x893d20e8
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def getOwner(): # not payable
  return owner


# hash = 0x929dd1e0
# getter = None
# const = None
# payable = True
def unknown929dd1e0() payable: 
  if unknown78914887[caller]:
      log 0x72365943: caller, unknown78914887[caller], 0
      return unknown78914887[caller]
  require ext_code.size(unknown10fe6584Address)
  call unknown10fe6584Address.0x8f0196d6 with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  unknown78914887[caller] = addr(ext_call.return_data[0])
  unknown9801354f[addr(ext_call.return_data[0])] = caller
  unknown4cf667d9.length++
  unknown4cf667d9[unknown4cf667d9.length] = addr(ext_call.return_data[0])
  log 0x72365943: caller, addr(ext_call.return_data[0]), 1
  return addr(ext_call.return_data[0])


# hash = 0x9801354f
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def unknown9801354f(addr _param1): # not payable
  return unknown9801354f[_param1]


# hash = 0xb00a6d92
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknownb00a6d92(): # not payable
  return unknownb00a6d92


# hash = 0xb92e7207
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 3]]]
# const = None
# payable = False
def unknownb92e7207(uint8 _param1): # not payable
  return unknown7db65b17[_param1]


# hash = 0xcf39918e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 13]]]
# const = None
# payable = False
def unknowncf39918e(uint256 _param1): # not payable
  return unknowncf39918e[_param1]


# hash = 0xd1bd1d6e
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknownd1bd1d6e(): # not payable
  return unknownd1bd1d6eAddress


# hash = 0xd974081f
# getter = ['storage', 160, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 5]]]
# const = None
# payable = False
def unknownd974081f(uint8 _param1): # not payable
  return unknownd974081f[_param1 << 248]


# hash = 0xdf41b67c
# getter = None
# const = None
# payable = False
def unknowndf41b67c(addr _param1, uint256 _param2): # not payable
  if unknown0b0db12d[caller] <= 0:
      revert with 0, '9'
  if _param2:
      require ext_code.size(_param1)
      call _param1.0x5b7ce8c9 with:
         value _param2 wei
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0xe1d1cb13
# getter = None
# const = None
# payable = False
def unknowne1d1cb13(addr _param1, uint32 _param2, array _param3, array _param4): # not payable
  if owner != caller:
      revert with 0, '1'
  require ext_code.size(_param1)
  call _param1.0xca6eb973 with:
       gas gas_remaining wei
      args 0, _param2, 96, (32 * _param3.length) + 128, _param3.length, call.data[_param3 + 36 len 32 * _param3.length], _param4.length, call.data[_param4 + 36 len 32 * _param4.length]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if _param2 <′ 0:
      unknown2881178b -= _param2


# hash = 0xea2143c2
# getter = None
# const = None
# payable = False
def unknownea2143c2(addr _param1): # not payable
  [94midx = 0
  [94ms = 0
  while [94midx < stor12.length:
      mem[0] = 12
      if stor12[[94midx] != caller:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = 1
      continue 
  if 0 >= stor12.length:
      revert with 0, '8'
  if bool([94ms) != 1:
      revert with 0, '8'
  stor11[0][caller] = _param1
  [94midx = 0
  [94ms = 0
  while [94midx < stor12.length:
      mem[0] = stor12[[94midx]
      mem[32] = sha3(0, 11)
      if stor11[0][stor12[[94midx]] != _param1:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  if [94ms >=′ 3:
      unknown10fe6584Address = _param1


# hash = 0xedba7f8f
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 5]]]
# const = None
# payable = False
def unknownedba7f8f(uint8 _param1): # not payable
  return unknownd974081f[_param1]


# hash = 0xf7e17fe9
# getter = None
# const = None
# payable = True
def unknownf7e17fe9() payable: 
  unknown2881178b += call.value


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


