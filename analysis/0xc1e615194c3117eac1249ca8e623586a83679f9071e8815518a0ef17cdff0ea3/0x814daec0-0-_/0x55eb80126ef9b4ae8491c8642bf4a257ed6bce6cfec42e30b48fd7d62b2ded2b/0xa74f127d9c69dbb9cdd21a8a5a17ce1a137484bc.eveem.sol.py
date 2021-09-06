# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xa74f127D9C69dbB9CDD21a8A5a17CE1a137484bC 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x384ab546': 'unknown384ab546(?)', '0x85a69651': 'unknown85a69651(?)', '0x8aee0683': 'unknown8aee0683(?)', '0xc672c4af': 'unknownc672c4af(?)', '0xc8c32c63': 'unknownc8c32c63(?)', '0xed3b1dcd': 'unknowned3b1dcd(?)', '0xffdd2888': 'unknownffdd2888(?)'} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    unknownd943c6fdAddress # mask: a s
    # storage address 2
    unknown2b742f50 # mask: a s
# hash = 0x06024aa4
# getter = None
# const = None
# payable = False
def unknown06024aa4(addr m_param1): # not payable
  if mowner != caller:
      revert with 0, '1'
  munknownd943c6fdAddress = m_param1


# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address m_newOwner): # not payable
  if mowner != caller:
      revert with 0, '1'
  mowner = m_newOwner


# hash = 0x2b742f50
# getter = ['storage', 8, 160, 2]
# const = None
# payable = False
def unknown2b742f50(): # not payable
  require munknown2b742f50 <= 4
  return munknown2b742f50


# hash = 0x57e1000a
# getter = None
# const = None
# payable = False
def unknown57e1000a(uint8 m_param1): # not payable
  require m_param1 <= 4
  if not m_param1:
      revert with 0, '3'
  require m_param1 <= 4
  if m_param1 == 1:
      return 1
  require m_param1 <= 4
  if m_param1 == 2:
      return 2
  require m_param1 <= 4
  if m_param1 == 3:
      return 3
  require m_param1 <= 4
  if m_param1 != 4:
      revert with 0, '4'
  return 4


# hash = 0x5962b4a0
# getter = None
# const = None
# payable = False
def unknown5962b4a0(uint256 m_param1, uint256 m_param2): # not payable
  if eth.balance(m_param1):
      return ((100 * eth.balance(m_param1)) + (100 * m_param2) /′ eth.balance(m_param1))
  else:
      return 0


# hash = 0x5c2758d3
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknown5c2758d3(): # not payable
  return munknownd943c6fdAddress


# hash = 0x5cafc695
# getter = None
# const = None
# payable = False
def unknown5cafc695(uint256 m_param1, uint256 m_param2): # not payable
  require ext_code.size(munknownd943c6fdAddress)
  call munknownd943c6fdAddress.0x1f11cb48 with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 192
  require ext_code.size(munknownd943c6fdAddress)
  call munknownd943c6fdAddress.getMultiplier() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(0x1fc04ee645b616a1641ea13fa5360cfa1e043367)
  [93mdelegate 0x1fc04ee645b616a1641ea13fa5360cfa1e043367.abs(int256 val) with:
       gas gas_remaining wei
      args m_param2
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  return (ext_call.return_data[64] * delegate.return_data[0] / ext_call.return_data[0])


# hash = 0x5e0b79d0
# getter = None
# const = None
# payable = False
def unknown5e0b79d0(uint256 m_param1, array m_param2, array m_param3): # not payable
  mem[128 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param2.length) + 128] = m_param3.length
  mem[(32 * m_param2.length) + 160 len 32 * m_param3.length] = call.data[m_param3 + 36 len 32 * m_param3.length]
  [94midx = 0
  mwhile [94midx < m_param2.lengthm:
      require [94midx < m_param2.length
      if mem[(32 * [94midx) + 128] != m_param1:
          [94midx = [94midx + 1
          mcontinue 
      require [94midx < m_param3.length
      mem[(32 * m_param3.length) + (32 * m_param2.length) + 160] = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
      return memory
        from (32 * m_param3.length) + (32 * m_param2.length) + 160
         [93mlen 32
  require ext_code.size(mstor1)
  call mstor1.0xcf39918e with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x60bb4cbf
# getter = None
# const = None
# payable = False
def unknown60bb4cbf(array m_param1, array m_param2): # not payable
  require ext_code.size(munknownd943c6fdAddress)
  call munknownd943c6fdAddress.0x60bb4cbf with:
       gas gas_remaining wei
      args 0, 64, m_param1.length + 96, m_param1.length, m_param1[allm], m_param2.length, m_param2[allm]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x893d20e8
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def getOwner(): # not payable
  return mowner


# hash = 0xae375d05
# getter = None
# const = None
# payable = False
def unknownae375d05(addr m_param1): # not payable
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(m_param1)
      call m_param1.0x5ee74564 with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[31 len 1] != 1:
          revert with 0, '2'
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(m_param1)
          call m_param1.0x5ee74564 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[31 len 1] != 2:
              revert with 0, '2'
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(m_param1)
              call m_param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 3:
                  revert with 0, '2'
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(m_param1)
              call m_param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 4:
                  revert with 0, '2'
  require ext_code.size(m_param1)
  call m_param1.0x80d23170 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return not bool(ext_call.return_data[0])


# hash = 0xc2637c7e
# getter = None
# const = None
# payable = False
def unknownc2637c7e(addr m_param1, uint256 m_param2): # not payable
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(m_param1)
      call m_param1.0x5ee74564 with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[31 len 1] != 1:
          revert with 0, '2'
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(m_param1)
          call m_param1.0x5ee74564 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[31 len 1] != 2:
              revert with 0, '2'
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(m_param1)
              call m_param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 3:
                  revert with 0, '2'
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(m_param1)
              call m_param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 4:
                  revert with 0, '2'
  require ext_code.size(munknownd943c6fdAddress)
  call munknownd943c6fdAddress.0x5678fa73 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 96
  if eth.balance(m_param1):
      return (ext_call.return_data[31 len 1] >′ (100 * eth.balance(m_param1)) + (100 * m_param2) /′ eth.balance(m_param1))
  return (ext_call.return_data[31 len 1] >′ 0)


# hash = 0xc738ce0b
# getter = None
# const = None
# payable = False
def unknownc738ce0b(addr m_param1, uint256 m_param2, uint256 m_param3): # not payable
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(m_param1)
      call m_param1.0x5ee74564 with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[31 len 1] != 1:
          revert with 0, '2'
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(m_param1)
          call m_param1.0x5ee74564 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[31 len 1] != 2:
              revert with 0, '2'
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(m_param1)
              call m_param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 3:
                  revert with 0, '2'
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(m_param1)
              call m_param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 4:
                  revert with 0, '2'
  require ext_code.size(0x1fc04ee645b616a1641ea13fa5360cfa1e043367)
  [93mdelegate 0x1fc04ee645b616a1641ea13fa5360cfa1e043367.abs(int256 val) with:
       gas gas_remaining wei
      args m_param3
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_param1)
  call m_param1.0x2645dd61 with:
       gas gas_remaining wei
      args m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(munknownd943c6fdAddress)
  call munknownd943c6fdAddress.0xcba181e8 with:
       gas gas_remaining wei
      args m_param2, delegate.return_data[0] + ext_call.return_data[0], m_param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return bool(ext_call.return_data[0]), ext_call.return_data[32]


# hash = 0xd082ea8c
# getter = None
# const = None
# payable = False
def setExchangeAddress(address m_exchangeAddress): # not payable
  if mowner != caller:
      revert with 0, '1'
  mstor1 = m_exchangeAddress


# hash = 0xd7facd9b
# getter = None
# const = None
# payable = False
def unknownd7facd9b(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4): # not payable
  return (m_param1 + m_param3 - m_param2 - m_param4)


# hash = 0xd943c6fd
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknownd943c6fd(): # not payable
  return munknownd943c6fdAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


