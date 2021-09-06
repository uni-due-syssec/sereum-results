# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xD7Dc910ac32c6eD4E00c2181391500a2e2B5a867 
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
    unknownd266770c
# hash = 0x042cefc1
# getter = None
# const = None
# payable = False
def unknown042cefc1(uint8 m_param1, addr m_param2): # not payable
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mstor12m.lengthm:
      mem[0] = 12
      if mstor12m[[94midxm] != caller:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = 1
      mcontinue 
  if 0 >= mstor12m.length:
      revert with 0, '8'
  if bool([94ms) != 1:
      revert with 0, '8'
  mstor11m[m_param1 + 255m]m[callerm] = m_param2
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mstor12m.lengthm:
      mem[0] = mstor12m[[94midxm]
      mem[32] = sha3(m_param1 + 255, 11)
      if mstor11m[m_param1 + 255m]m[mstor12m[[94midxm]m] != m_param2:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  if [94ms >=′ 3:
      munknown0b0db12dm[mstor3m[m_param1 << 248m]m] = 0
      munknown7db65b17m[m_param1 << 248m] = m_param2
      munknown0b0db12dm[m_param2m] = m_param1


# hash = 0x07f67dbd
# getter = None
# const = None
# payable = False
def unknown07f67dbd(uint8 m_param1, addr m_param2): # not payable
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mstor12m.lengthm:
      mem[0] = 12
      if mstor12m[[94midxm] != caller:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = 1
      mcontinue 
  if 0 >= mstor12m.length:
      revert with 0, '8'
  if bool([94ms) != 1:
      revert with 0, '8'
  mstor11m[m_param1 + 510m]m[callerm] = m_param2
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mstor12m.lengthm:
      mem[0] = mstor12m[[94midxm]
      mem[32] = sha3(m_param1 + 510, 11)
      if mstor11m[m_param1 + 510m]m[mstor12m[[94midxm]m] != m_param2:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  if [94ms >=′ 3:
      munknownd974081fm[m_param1 << 248m] = m_param2


# hash = 0x0b0db12d
# getter = ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = False
def unknown0b0db12d(addr m_param1): # not payable
  return munknown0b0db12dm[m_param1m]


# hash = 0x10fe6584
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown10fe6584(): # not payable
  return munknown10fe6584Address


# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address m_newOwner): # not payable
  if mowner != caller:
      revert with 0, '1'
  mowner = m_newOwner


# hash = 0x2881178b
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknown2881178b(): # not payable
  return munknown2881178b


# hash = 0x2d8815c8
# getter = None
# const = None
# payable = True
def unknown2d8815c8() payable: 
  call munknownd1bd1d6eAddress with:
     value call.value / 2 wei
       gas gas_remaining wei
  munknownb00a6d92 += call.value / 2
  munknown2881178b += call.value / 2


# hash = 0x2fe6a1e6
# getter = None
# const = None
# payable = True
def unknown2fe6a1e6() payable: 
  stop


# hash = 0x33d45905
# getter = None
# const = None
# payable = False
def unknown33d45905(array m_param1, array m_param2): # not payable
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  if mowner != caller:
      revert with 0, '1'
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param2.length
      require [94midx < m_param1.length
      mem[0] = mem[(32 * [94midx) + 156 len 4]
      mem[32] = 13
      munknownd266770cm[mem[(32 * [94midx) + 156 len 4]m] = mem[(32 * [94midx) + (32 * m_param1.length) + 160]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x4cf667d9
# getter = ['storage', 160, 0, ['add', ['sha3', 8], ['cd', 4]]]
# const = None
# payable = False
def unknown4cf667d9(uint256 m_param1): # not payable
  require m_param1 < munknown4cf667d9m.length
  return munknown4cf667d9m[m_param1m]


# hash = 0x5fecf62c
# getter = None
# const = None
# payable = True
def unknown5fecf62c() payable: 
  stop


# hash = 0x78914887
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def unknown78914887(addr m_param1): # not payable
  return munknown78914887m[m_param1m]


# hash = 0x798cc26a
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknown798cc26a(): # not payable
  return mowner


# hash = 0x7db65b17
# getter = ['storage', 160, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 3]]]
# const = None
# payable = False
def unknown7db65b17(uint8 m_param1): # not payable
  return munknown7db65b17m[m_param1 << 248m]


# hash = 0x841586e0
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def unknown841586e0(): # not payable
  return munknown4cf667d9m.length


# hash = 0x893d20e8
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def getOwner(): # not payable
  return mowner


# hash = 0x929dd1e0
# getter = None
# const = None
# payable = True
def unknown929dd1e0() payable: 
  if munknown78914887m[callerm]:
      log 0x72365943: caller, unknown78914887[caller], 0
      return munknown78914887m[callerm]
  require ext_code.size(munknown10fe6584Address)
  call munknown10fe6584Address.0x8f0196d6 with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  munknown78914887m[callerm] = addr(ext_call.return_data[0])
  munknown9801354fm[addr(ext_call.return_data[0])m] = caller
  munknown4cf667d9m.length++
  munknown4cf667d9m[munknown4cf667d9m.lengthm] = addr(ext_call.return_data[0])
  log 0x72365943: caller, addr(ext_call.return_data[0]), 1
  return addr(ext_call.return_data[0])


# hash = 0x9801354f
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def unknown9801354f(addr m_param1): # not payable
  return munknown9801354fm[m_param1m]


# hash = 0xb00a6d92
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknownb00a6d92(): # not payable
  return munknownb00a6d92


# hash = 0xb92e7207
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 3]]]
# const = None
# payable = False
def unknownb92e7207(uint8 m_param1): # not payable
  return munknown7db65b17m[m_param1m]


# hash = 0xd1bd1d6e
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknownd1bd1d6e(): # not payable
  return munknownd1bd1d6eAddress


# hash = 0xd266770c
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 32, 0, 224, ['cd', 4]], 13]]]
# const = None
# payable = False
def unknownd266770c(uint32 m_param1): # not payable
  return munknownd266770cm[m_param1 << 224m]


# hash = 0xd974081f
# getter = ['storage', 160, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 5]]]
# const = None
# payable = False
def unknownd974081f(uint8 m_param1): # not payable
  return munknownd974081fm[m_param1 << 248m]


# hash = 0xdf41b67c
# getter = None
# const = None
# payable = False
def unknowndf41b67c(addr m_param1, uint256 m_param2): # not payable
  if munknown0b0db12dm[callerm] <= 0:
      revert with 0, '9'
  if m_param2:
      require ext_code.size(m_param1)
      call m_param1.0x5b7ce8c9 with:
         value m_param2 wei
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0xe1d1cb13
# getter = None
# const = None
# payable = False
def unknowne1d1cb13(addr m_param1, uint32 m_param2, array m_param3, array m_param4): # not payable
  if mowner != caller:
      revert with 0, '1'
  require ext_code.size(m_param1)
  call m_param1.0xca6eb973 with:
       gas gas_remaining wei
      args 0, m_param2, 96, (32 * m_param3.length) + 128, m_param3.length, call.data[m_param3 + 36 len 32 * m_param3.length], m_param4.length, call.data[m_param4 + 36 len 32 * m_param4.length]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if m_param2 <′ 0:
      munknown2881178b -= m_param2


# hash = 0xea2143c2
# getter = None
# const = None
# payable = False
def unknownea2143c2(addr m_param1): # not payable
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mstor12m.lengthm:
      mem[0] = 12
      if mstor12m[[94midxm] != caller:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = 1
      mcontinue 
  if 0 >= mstor12m.length:
      revert with 0, '8'
  if bool([94ms) != 1:
      revert with 0, '8'
  mstor11m[0m]m[callerm] = m_param1
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mstor12m.lengthm:
      mem[0] = mstor12m[[94midxm]
      mem[32] = sha3(0, 11)
      if mstor11m[0m]m[mstor12m[[94midxm]m] != m_param1:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  if [94ms >=′ 3:
      munknown10fe6584Address = m_param1


# hash = 0xedba7f8f
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 5]]]
# const = None
# payable = False
def unknownedba7f8f(uint8 m_param1): # not payable
  return munknownd974081fm[m_param1m]


# hash = 0xf7e17fe9
# getter = None
# const = None
# payable = True
def unknownf7e17fe9() payable: 
  munknown2881178b += call.value


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


