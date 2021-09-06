# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xb7f6afa1fc197dDA2935E6d9088636D466673aCd 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x23210ea4': 'unknown23210ea4(?)', '0x41ee0fc7': 'unknown41ee0fc7(?)', '0x71a91f69': 'unknown71a91f69(?)', '0x977136b0': 'unknown977136b0(?)', '0xaf8d8e11': 'unknownaf8d8e11(?)', '0xe92c5b98': 'unknowne92c5b98(?)', '0xf82a728a': 'unknownf82a728a(?)'} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    unknown2b742f50 # mask: a s
    # storage address 2
    unknownd943c6fdAddress # mask: a s
# hash = 0x06024aa4
# getter = None
# const = None
# payable = False
def unknown06024aa4(addr _param1): # not payable
  if owner != caller:
      revert with 0, '1'
  unknownd943c6fdAddress = _param1


# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address _newOwner): # not payable
  if owner != caller:
      revert with 0, '1'
  owner = _newOwner


# hash = 0x1dbe9759
# getter = None
# const = None
# payable = False
def unknown1dbe9759(uint32 _param1, array _param2, array _param3): # not payable
  mem[128 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  mem[(32 * _param2.length) + 128] = _param3.length
  mem[(32 * _param2.length) + 160 len 32 * _param3.length] = call.data[_param3 + 36 len 32 * _param3.length]
  [94midx = 0
  while [94midx < _param2.length:
      require [94midx < _param2.length
      if mem[(32 * [94midx) + 156 len 4] != _param1:
          [94midx = [94midx + 1
          continue 
      require [94midx < _param3.length
      mem[(32 * _param3.length) + (32 * _param2.length) + 160] = mem[(32 * [94midx) + (32 * _param2.length) + 160]
      return memory
        from (32 * _param3.length) + (32 * _param2.length) + 160
         [93mlen 32
  require ext_code.size(stor1)
  call stor1.0xd266770c with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x2b742f50
# getter = ['storage', 8, 160, 2]
# const = None
# payable = False
def unknown2b742f50(): # not payable
  require unknown2b742f50 <= 4
  return unknown2b742f50


# hash = 0x57e1000a
# getter = None
# const = None
# payable = False
def unknown57e1000a(uint8 _param1): # not payable
  require _param1 <= 4
  if not _param1:
      revert with 0, '3'
  require _param1 <= 4
  if _param1 == 1:
      return 1
  require _param1 <= 4
  if _param1 == 2:
      return 2
  require _param1 <= 4
  if _param1 == 3:
      return 3
  require _param1 <= 4
  if _param1 != 4:
      revert with 0, '4'
  return 4


# hash = 0x5962b4a0
# getter = None
# const = None
# payable = False
def unknown5962b4a0(uint256 _param1, uint256 _param2): # not payable
  if eth.balance(_param1):
      return ((100 * eth.balance(_param1)) + (100 * _param2) /′ eth.balance(_param1))
  else:
      return 0


# hash = 0x5c2758d3
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknown5c2758d3(): # not payable
  return unknownd943c6fdAddress


# hash = 0x60bb4cbf
# getter = None
# const = None
# payable = False
def unknown60bb4cbf(array _param1, array _param2): # not payable
  require ext_code.size(unknownd943c6fdAddress)
  call unknownd943c6fdAddress.0x60bb4cbf with:
       gas gas_remaining wei
      args 0, 64, _param1.length + 96, _param1.length, _param1[all], _param2.length, _param2[all]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[28 len 4]


# hash = 0x7feb6e85
# getter = None
# const = None
# payable = False
def unknown7feb6e85(uint32 _param1, uint256 _param2): # not payable
  require ext_code.size(unknownd943c6fdAddress)
  call unknownd943c6fdAddress.0x12081ef5 with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 192
  require ext_code.size(unknownd943c6fdAddress)
  call unknownd943c6fdAddress.getMultiplier() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(0xfe6134fa39466e8788ec310c2c1f3c2128c988be)
  [93mdelegate 0xfe6134fa39466e8788ec310c2c1f3c2128c988be.abs(int256 val) with:
       gas gas_remaining wei
      args _param2
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  return (ext_call.return_data[64] * delegate.return_data[0] / ext_call.return_data[0])


# hash = 0x893d20e8
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def getOwner(): # not payable
  return owner


# hash = 0x8ba002fc
# getter = None
# const = None
# payable = False
def unknown8ba002fc(addr _param1, uint32 _param2, uint256 _param3): # not payable
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(_param1)
      call _param1.0x5ee74564 with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[31 len 1] != 1:
          revert with 0, '2'
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(_param1)
          call _param1.0x5ee74564 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[31 len 1] != 2:
              revert with 0, '2'
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(_param1)
              call _param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 3:
                  revert with 0, '2'
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(_param1)
              call _param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 4:
                  revert with 0, '2'
  require ext_code.size(0xfe6134fa39466e8788ec310c2c1f3c2128c988be)
  [93mdelegate 0xfe6134fa39466e8788ec310c2c1f3c2128c988be.abs(int256 val) with:
       gas gas_remaining wei
      args _param3
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(_param1)
  call _param1.0xb8310f49 with:
       gas gas_remaining wei
      args _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknownd943c6fdAddress)
  call unknownd943c6fdAddress.0xe2491a34 with:
       gas gas_remaining wei
      args _param2 << 224, delegate.return_data[0] + ext_call.return_data[0], _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return bool(ext_call.return_data[0]), ext_call.return_data[32]


# hash = 0xae375d05
# getter = None
# const = None
# payable = False
def unknownae375d05(addr _param1): # not payable
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(_param1)
      call _param1.0x5ee74564 with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[31 len 1] != 1:
          revert with 0, '2'
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(_param1)
          call _param1.0x5ee74564 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[31 len 1] != 2:
              revert with 0, '2'
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(_param1)
              call _param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 3:
                  revert with 0, '2'
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(_param1)
              call _param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 4:
                  revert with 0, '2'
  require ext_code.size(_param1)
  call _param1.0x80d23170 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return not bool(ext_call.return_data[0])


# hash = 0xc2637c7e
# getter = None
# const = None
# payable = False
def unknownc2637c7e(addr _param1, uint256 _param2): # not payable
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(_param1)
      call _param1.0x5ee74564 with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[31 len 1] != 1:
          revert with 0, '2'
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(_param1)
          call _param1.0x5ee74564 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[31 len 1] != 2:
              revert with 0, '2'
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(_param1)
              call _param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 3:
                  revert with 0, '2'
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(_param1)
              call _param1.0x5ee74564 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[31 len 1] != 4:
                  revert with 0, '2'
  require ext_code.size(unknownd943c6fdAddress)
  call unknownd943c6fdAddress.0x5678fa73 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 96
  if eth.balance(_param1):
      return (ext_call.return_data[31 len 1] >′ (100 * eth.balance(_param1)) + (100 * _param2) /′ eth.balance(_param1))
  return (ext_call.return_data[31 len 1] >′ 0)


# hash = 0xd082ea8c
# getter = None
# const = None
# payable = False
def setExchangeAddress(address _exchangeAddress): # not payable
  if owner != caller:
      revert with 0, '1'
  stor1 = _exchangeAddress


# hash = 0xd7facd9b
# getter = None
# const = None
# payable = False
def unknownd7facd9b(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4): # not payable
  return (_param1 + _param3 - _param2 - _param4)


# hash = 0xd943c6fd
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknownd943c6fd(): # not payable
  return unknownd943c6fdAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


