# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xFE09d42A447D4295FD108D8A666e9cD3FEb43307 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    marketAddress # mask: a s
# hash = 0x031f9c80
# getter = None
# const = None
# payable = True
def unknown031f9c80(array _param1, array _param2) payable: 
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = _param2.length
  mem[(32 * _param1.length) + 160 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  mem[(32 * _param1.length) + (32 * _param2.length) + 160] = 0
  if _param1.length:
      mem[(32 * _param1.length) + (32 * _param2.length) + 192] = _param1.length
      [94ms = 0
      [94midx = 0
      [94ms = call.value
      while [94midx < _param1.length:
          require [94midx < _param1.length
          [94m_84 = mem[(32 * [94midx) + 128]
          require [94midx < mem[(32 * _param1.length) + 128]
          [94m_103 = mem[(32 * [94midx) + (32 * _param1.length) + 160]
          mem[(64 * _param1.length) + (32 * _param2.length) + 256] = 0
          mem[(64 * _param1.length) + (32 * _param2.length) + 228] = caller
          require ext_code.size(addr([94m_84))
          call addr([94m_84).0xd9214ed5 with:
             value [94m_103 wei
               gas gas_remaining - 9710 wei
              args caller
          mem[(64 * _param1.length) + (32 * _param2.length) + 224] = ext_call.return_data[0]
          require ext_call.success
          require [94midx < mem[(32 * _param1.length) + (32 * _param2.length) + 192]
          mem[(32 * _param1.length) + (32 * _param2.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
          require [94midx < mem[(32 * _param1.length) + (32 * _param2.length) + 192]
          if not ext_call.return_data[0]:
              [94ms = [94m_84
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
          require [94midx < mem[(32 * _param1.length) + 128]
          [94ms = [94m_84
          [94midx = [94midx + 1
          [94ms = [94ms - mem[(32 * [94midx) + (32 * _param1.length) + 160]
          continue 
      if [94ms > 0:
          call caller with:
             value [94ms wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
      mem[(64 * _param1.length) + (32 * _param2.length) + 224] = 0x1974884f00000000000000000000000000000000000000000000000000000000
      mem[(64 * _param1.length) + (32 * _param2.length) + 228] = caller
      mem[(64 * _param1.length) + (32 * _param2.length) + 260] = 1
      mem[(64 * _param1.length) + (32 * _param2.length) + 292] = 128
      mem[(64 * _param1.length) + (32 * _param2.length) + 356] = _param1.length
      mem[(64 * _param1.length) + (32 * _param2.length) + 388 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
      mem[(64 * _param1.length) + (32 * _param2.length) + 324] = (32 * _param1.length) + 160
      mem[(98 * _param1.length) + (32 * _param2.length) + 388] = mem[(32 * _param1.length) + (32 * _param2.length) + 192]
      mem[(98 * _param1.length) + (32 * _param2.length) + 420 len floor32(mem[(32 * _param1.length) + (32 * _param2.length) + 192])] = mem[(32 * _param1.length) + (32 * _param2.length) + 224 len floor32(mem[(32 * _param1.length) + (32 * _param2.length) + 192])]
      require ext_code.size(marketAddress)
      call marketAddress.0x1974884f with:
           gas gas_remaining - 710 wei
          args mem[(64 * _param1.length) + (32 * _param2.length) + 228 len (32 * mem[(32 * _param1.length) + (32 * _param2.length) + 192]) + (32 * _param1.length) + 192]
      require ext_call.success


# hash = 0x25a0b2e1
# getter = None
# const = None
# payable = False
def unknown25a0b2e1(array _param1): # not payable
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      [94m_9 = mem[(32 * [94midx) + 128]
      mem[(32 * _param1.length) + 128] = 0x3b7416ad00000000000000000000000000000000000000000000000000000000
      mem[(32 * _param1.length) + 132] = caller
      mem[(32 * _param1.length) + 164] = addr([94m_9)
      require ext_code.size(marketAddress)
      call marketAddress.0x3b7416ad with:
           gas gas_remaining - 710 wei
          args caller, addr([94m_9)
      require ext_call.success
      [94midx = [94midx + 1
      continue 


# hash = 0x3a256949
# getter = None
# const = None
# payable = False
def unknown3a256949(array _param1, array _param2, array _param3): # not payable
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = _param2.length
  mem[(32 * _param1.length) + 160 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  mem[(32 * _param1.length) + (32 * _param2.length) + 160] = _param3.length
  mem[(32 * _param1.length) + (32 * _param2.length) + 192 len 32 * _param3.length] = call.data[_param3 + 36 len 32 * _param3.length]
  require _param1.length == _param2.length
  require _param1.length == _param3.length
  [94ms = 0
  [94ms = 0
  [94ms = 0
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      [94m_21 = mem[(32 * [94midx) + 128]
      require [94midx < _param2.length
      [94m_23 = mem[(32 * [94midx) + (32 * _param1.length) + 160]
      require [94midx < _param3.length
      [94m_25 = mem[(32 * [94midx) + (32 * _param1.length) + (32 * _param2.length) + 192]
      if not mem[(32 * [94midx) + (32 * _param1.length) + 160]:
          mem[(32 * _param1.length) + (32 * _param2.length) + (32 * _param3.length) + 192] = 0xb82a097800000000000000000000000000000000000000000000000000000000
          mem[(32 * _param1.length) + (32 * _param2.length) + (32 * _param3.length) + 196] = caller
          mem[(32 * _param1.length) + (32 * _param2.length) + (32 * _param3.length) + 228] = [94m_25
          require ext_code.size(addr([94m_21))
          call addr([94m_21).0xb82a0978 with:
               gas gas_remaining - 710 wei
              args caller, [94m_25
      else:
          mem[(32 * _param1.length) + (32 * _param2.length) + (32 * _param3.length) + 192] = 0xdf9b8fff00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param1.length) + (32 * _param2.length) + (32 * _param3.length) + 196] = caller
          mem[(32 * _param1.length) + (32 * _param2.length) + (32 * _param3.length) + 228] = [94m_25
          require ext_code.size(addr([94m_21))
          call addr([94m_21).0xdf9b8fff with:
               gas gas_remaining - 710 wei
              args caller, [94m_25
      require ext_call.success
      [94ms = [94m_25
      [94ms = [94m_23
      [94ms = [94m_21
      [94midx = [94midx + 1
      continue 


# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = False
def withdraw(): # not payable
  require stor0 == caller
  call stor0 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0x47cf775d
# getter = None
# const = None
# payable = False
def unknown47cf775d(addr _param1, uint256 _param2, uint8 _param3, uint32 _param4, uint8 _param5, bool _param6): # not payable
  [94midx = 0
  while uint8([94midx) < _param3:
      require _param3
      mem[96] = 0xf401e49a00000000000000000000000000000000000000000000000000000000
      mem[100] = _param1
      mem[132] = _param4
      mem[164] = _param5
      mem[196] = _param6
      require ext_code.size(marketAddress)
      call marketAddress.0xf401e49a with:
         value _param2 / _param3 wei
           gas gas_remaining - 9710 wei
          args addr(_param1), _param4 << 224, _param5 << 248, _param6
      require ext_call.success
      [94midx = [94midx + 1
      continue 


# hash = 0x5dcc68de
# getter = None
# const = None
# payable = True
def unknown5dcc68de(array _param1, array _param2) payable: 
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = _param2.length
  mem[(32 * _param1.length) + 160 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  mem[(32 * _param1.length) + (32 * _param2.length) + 160] = 0
  if _param1.length:
      mem[(32 * _param1.length) + (32 * _param2.length) + 192] = _param1.length
      [94ms = 0
      [94midx = 0
      [94ms = call.value
      while [94midx < _param1.length:
          require [94midx < _param1.length
          [94m_84 = mem[(32 * [94midx) + 128]
          require [94midx < mem[(32 * _param1.length) + 128]
          [94m_103 = mem[(32 * [94midx) + (32 * _param1.length) + 160]
          mem[(64 * _param1.length) + (32 * _param2.length) + 256] = 0
          mem[(64 * _param1.length) + (32 * _param2.length) + 228] = caller
          require ext_code.size(addr([94m_84))
          call addr([94m_84).0x5a0cf9f3 with:
             value [94m_103 wei
               gas gas_remaining - 9710 wei
              args caller
          mem[(64 * _param1.length) + (32 * _param2.length) + 224] = ext_call.return_data[0]
          require ext_call.success
          require [94midx < mem[(32 * _param1.length) + (32 * _param2.length) + 192]
          mem[(32 * _param1.length) + (32 * _param2.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
          require [94midx < mem[(32 * _param1.length) + (32 * _param2.length) + 192]
          if not ext_call.return_data[0]:
              [94ms = [94m_84
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
          require [94midx < mem[(32 * _param1.length) + 128]
          [94ms = [94m_84
          [94midx = [94midx + 1
          [94ms = [94ms - mem[(32 * [94midx) + (32 * _param1.length) + 160]
          continue 
      if [94ms > 0:
          call caller with:
             value [94ms wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
      mem[(64 * _param1.length) + (32 * _param2.length) + 224] = 0x1974884f00000000000000000000000000000000000000000000000000000000
      mem[(64 * _param1.length) + (32 * _param2.length) + 228] = caller
      mem[(64 * _param1.length) + (32 * _param2.length) + 260] = 0
      mem[(64 * _param1.length) + (32 * _param2.length) + 292] = 128
      mem[(64 * _param1.length) + (32 * _param2.length) + 356] = _param1.length
      mem[(64 * _param1.length) + (32 * _param2.length) + 388 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
      mem[(64 * _param1.length) + (32 * _param2.length) + 324] = (32 * _param1.length) + 160
      mem[(98 * _param1.length) + (32 * _param2.length) + 388] = mem[(32 * _param1.length) + (32 * _param2.length) + 192]
      mem[(98 * _param1.length) + (32 * _param2.length) + 420 len floor32(mem[(32 * _param1.length) + (32 * _param2.length) + 192])] = mem[(32 * _param1.length) + (32 * _param2.length) + 224 len floor32(mem[(32 * _param1.length) + (32 * _param2.length) + 192])]
      require ext_code.size(marketAddress)
      call marketAddress.0x1974884f with:
           gas gas_remaining - 710 wei
          args mem[(64 * _param1.length) + (32 * _param2.length) + 228 len (32 * mem[(32 * _param1.length) + (32 * _param2.length) + 192]) + (32 * _param1.length) + 192]
      require ext_call.success


# hash = 0x69a82efc
# getter = None
# const = None
# payable = True
def unknown69a82efc(bool _param1, array _param2, array _param3) payable: 
  mem[128 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  mem[(32 * _param2.length) + 128] = _param3.length
  mem[(32 * _param2.length) + 160 len 32 * _param3.length] = call.data[_param3 + 36 len 32 * _param3.length]
  mem[(32 * _param2.length) + (32 * _param3.length) + 160] = 0
  if _param2.length:
      mem[(32 * _param2.length) + (32 * _param3.length) + 192] = _param2.length
      [94ms = 0
      [94midx = 0
      [94ms = call.value
      while [94midx < _param2.length:
          require [94midx < _param2.length
          [94m_108 = mem[(32 * [94midx) + 128]
          if not _param1:
              if [94midx < mem[(32 * _param2.length) + 128]:
                  [94m_133 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
                  mem[(64 * _param2.length) + (32 * _param3.length) + 256] = 0
                  mem[(64 * _param2.length) + (32 * _param3.length) + 228] = caller
                  require ext_code.size(addr([94m_108))
                  call addr([94m_108).0x5a0cf9f3 with:
                     value [94m_133 wei
                       gas gas_remaining - 9710 wei
                      args caller
                  mem[(64 * _param2.length) + (32 * _param3.length) + 224] = ext_call.return_data[0]
                  require ext_call.success
                  if [94midx < mem[(32 * _param2.length) + (32 * _param3.length) + 192]:
                      mem[(32 * _param2.length) + (32 * _param3.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
                      if [94midx < mem[(32 * _param2.length) + (32 * _param3.length) + 192]:
                          if not ext_call.return_data[0]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
                          if [94midx < mem[(32 * _param2.length) + 128]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms - mem[(32 * [94midx) + (32 * _param2.length) + 160]
                              continue 
          else:
              if [94midx < mem[(32 * _param2.length) + 128]:
                  [94m_137 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
                  mem[(64 * _param2.length) + (32 * _param3.length) + 256] = 0
                  mem[(64 * _param2.length) + (32 * _param3.length) + 228] = caller
                  require ext_code.size(addr([94m_108))
                  call addr([94m_108).0xd9214ed5 with:
                     value [94m_137 wei
                       gas gas_remaining - 9710 wei
                      args caller
                  mem[(64 * _param2.length) + (32 * _param3.length) + 224] = ext_call.return_data[0]
                  require ext_call.success
                  if [94midx < mem[(32 * _param2.length) + (32 * _param3.length) + 192]:
                      mem[(32 * _param2.length) + (32 * _param3.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
                      if [94midx < mem[(32 * _param2.length) + (32 * _param3.length) + 192]:
                          if not ext_call.return_data[0]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
                          if [94midx < mem[(32 * _param2.length) + 128]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms - mem[(32 * [94midx) + (32 * _param2.length) + 160]
                              continue 
          revert
      if [94ms > 0:
          call caller with:
             value [94ms wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
      mem[(64 * _param2.length) + (32 * _param3.length) + 224] = 0x1974884f00000000000000000000000000000000000000000000000000000000
      mem[(64 * _param2.length) + (32 * _param3.length) + 228] = caller
      mem[(64 * _param2.length) + (32 * _param3.length) + 260] = _param1
      mem[(64 * _param2.length) + (32 * _param3.length) + 292] = 128
      mem[(64 * _param2.length) + (32 * _param3.length) + 356] = _param2.length
      mem[(64 * _param2.length) + (32 * _param3.length) + 388 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
      mem[(64 * _param2.length) + (32 * _param3.length) + 324] = (32 * _param2.length) + 160
      mem[(98 * _param2.length) + (32 * _param3.length) + 388] = mem[(32 * _param2.length) + (32 * _param3.length) + 192]
      mem[(98 * _param2.length) + (32 * _param3.length) + 420 len floor32(mem[(32 * _param2.length) + (32 * _param3.length) + 192])] = mem[(32 * _param2.length) + (32 * _param3.length) + 224 len floor32(mem[(32 * _param2.length) + (32 * _param3.length) + 192])]
      require ext_code.size(marketAddress)
      call marketAddress.0x1974884f with:
           gas gas_remaining - 710 wei
          args mem[(64 * _param2.length) + (32 * _param3.length) + 228 len (32 * mem[(32 * _param2.length) + (32 * _param3.length) + 192]) + (32 * _param2.length) + 192]
      require ext_call.success


# hash = 0x6dcea85f
# getter = None
# const = None
# payable = False
def setMarket(address _add): # not payable
  require stor0 == caller
  marketAddress = _add


# hash = 0x7141f423
# getter = None
# const = None
# payable = True
def unknown7141f423(uint8 _param1, uint32 _param2, uint8 _param3, array _param4, array _param5, bool _param6) payable: 
  mem[96] = _param4.length
  mem[128 len 32 * _param4.length] = call.data[_param4 + 36 len 32 * _param4.length]
  mem[(32 * _param4.length) + 128] = _param5.length
  mem[(32 * _param4.length) + 160 len 32 * _param5.length] = call.data[_param5 + 36 len 32 * _param5.length]
  if not _param6:
      require _param3 - 1
      [94midx = 0
      while uint8([94midx) < _param1:
          require _param1
          [94m_199 = (32 * _param4.length) + (32 * _param5.length) + 160
          mem[(32 * _param4.length) + (32 * _param5.length) + 160] = 0xf401e49a00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param5.length) + 164] = caller
          mem[(32 * _param4.length) + (32 * _param5.length) + 196] = _param2
          mem[(32 * _param4.length) + (32 * _param5.length) + 228] = _param3
          mem[(32 * _param4.length) + (32 * _param5.length) + 260] = _param6
          require ext_code.size(marketAddress)
          call marketAddress.0xf401e49a with:
             value _param1 * 10 * 10^18 / _param3 - 1 / _param1 wei
               gas gas_remaining - 9710 wei
              args caller, _param2 << 224, _param3 << 248, _param6
          require ext_call.success
          [94midx = [94midx + 1
          continue 
      mem[(32 * _param4.length) + (32 * _param5.length) + 160] = 0
      if _param4.length:
          [94m_msize = max((32 * _param4.length) + (32 * _param5.length) + 60, (32 * _param4.length) + (32 * _param5.length) + 96, [94m_199)
          mem[[94m_msize + 132] = _param4.length
          mem[64] = ([94m_msize + 132) + (32 * _param4.length) + 32
          [94ms = 0
          [94midx = 0
          [94ms = call.value - (_param1 * 10 * 10^18 / _param3 - 1)
          while [94midx < _param4.length:
              require [94midx < _param4.length
              [94m_408 = mem[(32 * [94midx) + 128]
              if not _param6:
                  if [94midx < _param5.length:
                      [94m_449 = mem[(32 * [94midx) + (32 * _param4.length) + 160]
                      mem[([94m_msize + 132) + (32 * _param4.length) + 64] = 0
                      mem[([94m_msize + 132) + (32 * _param4.length) + 36] = caller
                      require ext_code.size(addr([94m_408))
                      call addr([94m_408).0x5a0cf9f3 with:
                         value [94m_449 wei
                           gas gas_remaining - 9710 wei
                          args caller
                      mem[([94m_msize + 132) + (32 * _param4.length) + 32] = ext_call.return_data[0]
                      require ext_call.success
                      if [94midx < mem[[94m_msize + 132]:
                          mem[([94m_msize + 132) + (32 * [94midx) + 32] = bool(ext_call.return_data[0])
                          if [94midx < mem[[94m_msize + 132]:
                              if not ext_call.return_data[0]:
                                  [94ms = [94m_408
                                  [94midx = [94midx + 1
                                  [94ms = [94ms
                                  continue 
                              if [94midx < _param5.length:
                                  [94ms = [94m_408
                                  [94midx = [94midx + 1
                                  [94ms = [94ms - mem[(32 * [94midx) + (32 * _param4.length) + 160]
                                  continue 
              else:
                  if [94midx < _param5.length:
                      [94m_453 = mem[(32 * [94midx) + (32 * _param4.length) + 160]
                      mem[([94m_msize + 132) + (32 * _param4.length) + 64] = 0
                      mem[([94m_msize + 132) + (32 * _param4.length) + 36] = caller
                      require ext_code.size(addr([94m_408))
                      call addr([94m_408).0xd9214ed5 with:
                         value [94m_453 wei
                           gas gas_remaining - 9710 wei
                          args caller
                      mem[([94m_msize + 132) + (32 * _param4.length) + 32] = ext_call.return_data[0]
                      require ext_call.success
                      if [94midx < mem[[94m_msize + 132]:
                          mem[([94m_msize + 132) + (32 * [94midx) + 32] = bool(ext_call.return_data[0])
                          if [94midx < mem[[94m_msize + 132]:
                              if not ext_call.return_data[0]:
                                  [94ms = [94m_408
                                  [94midx = [94midx + 1
                                  [94ms = [94ms
                                  continue 
                              if [94midx < _param5.length:
                                  [94ms = [94m_408
                                  [94midx = [94midx + 1
                                  [94ms = [94ms - mem[(32 * [94midx) + (32 * _param4.length) + 160]
                                  continue 
              revert
          if [94ms > 0:
              call caller with:
                 value [94ms wei
                   gas 2300 * is_zero(value) wei
              require ext_call.success
          mem[([94m_msize + 132) + (32 * _param4.length) + 32] = 0x1974884f00000000000000000000000000000000000000000000000000000000
          mem[([94m_msize + 132) + (32 * _param4.length) + 36] = caller
          mem[([94m_msize + 132) + (32 * _param4.length) + 68] = _param6
          mem[([94m_msize + 132) + (32 * _param4.length) + 100] = 128
          mem[([94m_msize + 132) + (32 * _param4.length) + 164] = _param4.length
          mem[([94m_msize + 132) + (32 * _param4.length) + 196 len floor32(_param4.length)] = call.data[_param4 + 36 len floor32(_param4.length)]
          mem[([94m_msize + 132) + (32 * _param4.length) + 132] = (32 * _param4.length) + 160
          mem[(64 * _param4.length) + ([94m_msize + 132) + 196] = mem[[94m_msize + 132]
          mem[(64 * _param4.length) + ([94m_msize + 132) + 228 len floor32(mem[[94m_msize + 132])] = mem[([94m_msize + 132) + 32 len floor32(mem[[94m_msize + 132])]
          require ext_code.size(marketAddress)
          call marketAddress.0x1974884f with:
               gas gas_remaining - 710 wei
              args caller, _param6, Array(len=_param4.length, data=call.data[_param4 + 36 len floor32(_param4.length)], mem[([94m_msize + 132) + (32 * _param4.length) + floor32(_param4.length) + 196 len (32 * _param4.length) + (32 * mem[[94m_msize + 132]) + -floor32(_param4.length) + 32]), (32 * _param4.length) + 160
          require ext_call.success
  else:
      require _param3 + 1
      [94midx = 0
      while uint8([94midx) < _param1:
          require _param1
          [94m_201 = (32 * _param4.length) + (32 * _param5.length) + 160
          mem[(32 * _param4.length) + (32 * _param5.length) + 160] = 0xf401e49a00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param5.length) + 164] = caller
          mem[(32 * _param4.length) + (32 * _param5.length) + 196] = _param2
          mem[(32 * _param4.length) + (32 * _param5.length) + 228] = _param3
          mem[(32 * _param4.length) + (32 * _param5.length) + 260] = _param6
          require ext_code.size(marketAddress)
          call marketAddress.0xf401e49a with:
             value _param1 * 10 * 10^18 / _param3 + 1 / _param1 wei
               gas gas_remaining - 9710 wei
              args caller, _param2 << 224, _param3 << 248, _param6
          require ext_call.success
          [94midx = [94midx + 1
          continue 
      mem[(32 * _param4.length) + (32 * _param5.length) + 160] = 0
      if _param4.length:
          [94m_msize = max((32 * _param4.length) + (32 * _param5.length) + 60, (32 * _param4.length) + (32 * _param5.length) + 96, [94m_201)
          mem[[94m_msize + 132] = _param4.length
          mem[64] = ([94m_msize + 132) + (32 * _param4.length) + 32
          [94ms = 0
          [94midx = 0
          [94ms = call.value - (_param1 * 10 * 10^18 / _param3 + 1)
          while [94midx < _param4.length:
              require [94midx < _param4.length
              [94m_414 = mem[(32 * [94midx) + 128]
              if not _param6:
                  if [94midx < _param5.length:
                      [94m_471 = mem[(32 * [94midx) + (32 * _param4.length) + 160]
                      mem[([94m_msize + 132) + (32 * _param4.length) + 64] = 0
                      mem[([94m_msize + 132) + (32 * _param4.length) + 36] = caller
                      require ext_code.size(addr([94m_414))
                      call addr([94m_414).0x5a0cf9f3 with:
                         value [94m_471 wei
                           gas gas_remaining - 9710 wei
                          args caller
                      mem[([94m_msize + 132) + (32 * _param4.length) + 32] = ext_call.return_data[0]
                      require ext_call.success
                      if [94midx < mem[[94m_msize + 132]:
                          mem[([94m_msize + 132) + (32 * [94midx) + 32] = bool(ext_call.return_data[0])
                          if [94midx < mem[[94m_msize + 132]:
                              if not ext_call.return_data[0]:
                                  [94ms = [94m_414
                                  [94midx = [94midx + 1
                                  [94ms = [94ms
                                  continue 
                              if [94midx < _param5.length:
                                  [94ms = [94m_414
                                  [94midx = [94midx + 1
                                  [94ms = [94ms - mem[(32 * [94midx) + (32 * _param4.length) + 160]
                                  continue 
              else:
                  if [94midx < _param5.length:
                      [94m_475 = mem[(32 * [94midx) + (32 * _param4.length) + 160]
                      mem[([94m_msize + 132) + (32 * _param4.length) + 64] = 0
                      mem[([94m_msize + 132) + (32 * _param4.length) + 36] = caller
                      require ext_code.size(addr([94m_414))
                      call addr([94m_414).0xd9214ed5 with:
                         value [94m_475 wei
                           gas gas_remaining - 9710 wei
                          args caller
                      mem[([94m_msize + 132) + (32 * _param4.length) + 32] = ext_call.return_data[0]
                      require ext_call.success
                      if [94midx < mem[[94m_msize + 132]:
                          mem[([94m_msize + 132) + (32 * [94midx) + 32] = bool(ext_call.return_data[0])
                          if [94midx < mem[[94m_msize + 132]:
                              if not ext_call.return_data[0]:
                                  [94ms = [94m_414
                                  [94midx = [94midx + 1
                                  [94ms = [94ms
                                  continue 
                              if [94midx < _param5.length:
                                  [94ms = [94m_414
                                  [94midx = [94midx + 1
                                  [94ms = [94ms - mem[(32 * [94midx) + (32 * _param4.length) + 160]
                                  continue 
              revert
          if [94ms > 0:
              call caller with:
                 value [94ms wei
                   gas 2300 * is_zero(value) wei
              require ext_call.success
          mem[([94m_msize + 132) + (32 * _param4.length) + 32] = 0x1974884f00000000000000000000000000000000000000000000000000000000
          mem[([94m_msize + 132) + (32 * _param4.length) + 36] = caller
          mem[([94m_msize + 132) + (32 * _param4.length) + 68] = _param6
          mem[([94m_msize + 132) + (32 * _param4.length) + 100] = 128
          mem[([94m_msize + 132) + (32 * _param4.length) + 164] = _param4.length
          mem[([94m_msize + 132) + (32 * _param4.length) + 196 len floor32(_param4.length)] = call.data[_param4 + 36 len floor32(_param4.length)]
          mem[([94m_msize + 132) + (32 * _param4.length) + 132] = (32 * _param4.length) + 160
          mem[(64 * _param4.length) + ([94m_msize + 132) + 196] = mem[[94m_msize + 132]
          mem[(64 * _param4.length) + ([94m_msize + 132) + 228 len floor32(mem[[94m_msize + 132])] = mem[([94m_msize + 132) + 32 len floor32(mem[[94m_msize + 132])]
          require ext_code.size(marketAddress)
          call marketAddress.0x1974884f with:
               gas gas_remaining - 710 wei
              args caller, _param6, Array(len=_param4.length, data=mem[([94m_msize + 132) + (32 * _param4.length) + 196 len (32 * mem[[94m_msize + 132]) + (32 * _param4.length) + 32]), (32 * _param4.length) + 160
          require ext_call.success


# hash = 0x80f55605
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def market(): # not payable
  return marketAddress


# hash = 0xacbbf3ac
# getter = None
# const = None
# payable = False
def unknownacbbf3ac(uint256 _param1): # not payable
  require _param1 + 1
  return (10 * 10^18 / _param1 + 1)


# hash = 0xd87789e0
# getter = None
# const = None
# payable = False
def unknownd87789e0(uint256 _param1): # not payable
  require _param1 - 1
  return (10 * 10^18 / _param1 - 1)


# hash = 0xdcd78126
# getter = None
# const = None
# payable = True
def unknowndcd78126(uint8 _param1, uint32 _param2, uint8 _param3, bool _param4) payable: 
  [94midx = 0
  while uint8([94midx) < _param1:
      require _param1
      mem[96] = 0xf401e49a00000000000000000000000000000000000000000000000000000000
      mem[100] = caller
      mem[132] = _param2
      mem[164] = _param3
      mem[196] = _param4
      require ext_code.size(marketAddress)
      call marketAddress.0xf401e49a with:
         value call.value / _param1 wei
           gas gas_remaining - 9710 wei
          args caller, _param2 << 224, _param3 << 248, _param4
      require ext_call.success
      [94midx = [94midx + 1
      continue 


# hash = 0xfd29e664
# getter = None
# const = None
# payable = False
def unknownfd29e664(addr _param1, uint256 _param2, bool _param3, array _param4, array _param5): # not payable
  mem[128 len 32 * _param4.length] = call.data[_param4 + 36 len 32 * _param4.length]
  mem[(32 * _param4.length) + 128] = _param5.length
  mem[(32 * _param4.length) + 160 len 32 * _param5.length] = call.data[_param5 + 36 len 32 * _param5.length]
  mem[(32 * _param4.length) + (32 * _param5.length) + 160] = 0
  if _param4.length:
      mem[(32 * _param4.length) + (32 * _param5.length) + 192] = _param4.length
      [94ms = 0
      [94midx = 0
      [94ms = _param2
      while [94midx < _param4.length:
          require [94midx < _param4.length
          [94m_108 = mem[(32 * [94midx) + 128]
          if not _param3:
              if [94midx < mem[(32 * _param4.length) + 128]:
                  [94m_133 = mem[(32 * [94midx) + (32 * _param4.length) + 160]
                  mem[(64 * _param4.length) + (32 * _param5.length) + 256] = 0
                  mem[(64 * _param4.length) + (32 * _param5.length) + 228] = _param1
                  require ext_code.size(addr([94m_108))
                  call addr([94m_108).0x5a0cf9f3 with:
                     value [94m_133 wei
                       gas gas_remaining - 9710 wei
                      args _param1
                  mem[(64 * _param4.length) + (32 * _param5.length) + 224] = ext_call.return_data[0]
                  require ext_call.success
                  if [94midx < mem[(32 * _param4.length) + (32 * _param5.length) + 192]:
                      mem[(32 * _param4.length) + (32 * _param5.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
                      if [94midx < mem[(32 * _param4.length) + (32 * _param5.length) + 192]:
                          if not ext_call.return_data[0]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
                          if [94midx < mem[(32 * _param4.length) + 128]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms - mem[(32 * [94midx) + (32 * _param4.length) + 160]
                              continue 
          else:
              if [94midx < mem[(32 * _param4.length) + 128]:
                  [94m_137 = mem[(32 * [94midx) + (32 * _param4.length) + 160]
                  mem[(64 * _param4.length) + (32 * _param5.length) + 256] = 0
                  mem[(64 * _param4.length) + (32 * _param5.length) + 228] = _param1
                  require ext_code.size(addr([94m_108))
                  call addr([94m_108).0xd9214ed5 with:
                     value [94m_137 wei
                       gas gas_remaining - 9710 wei
                      args _param1
                  mem[(64 * _param4.length) + (32 * _param5.length) + 224] = ext_call.return_data[0]
                  require ext_call.success
                  if [94midx < mem[(32 * _param4.length) + (32 * _param5.length) + 192]:
                      mem[(32 * _param4.length) + (32 * _param5.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
                      if [94midx < mem[(32 * _param4.length) + (32 * _param5.length) + 192]:
                          if not ext_call.return_data[0]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              continue 
                          if [94midx < mem[(32 * _param4.length) + 128]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms - mem[(32 * [94midx) + (32 * _param4.length) + 160]
                              continue 
          revert
      if [94ms > 0:
          call _param1 with:
             value [94ms wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
      mem[(64 * _param4.length) + (32 * _param5.length) + 224] = 0x1974884f00000000000000000000000000000000000000000000000000000000
      mem[(64 * _param4.length) + (32 * _param5.length) + 228] = _param1
      mem[(64 * _param4.length) + (32 * _param5.length) + 260] = _param3
      mem[(64 * _param4.length) + (32 * _param5.length) + 292] = 128
      mem[(64 * _param4.length) + (32 * _param5.length) + 356] = _param4.length
      mem[(64 * _param4.length) + (32 * _param5.length) + 388 len floor32(_param4.length)] = call.data[_param4 + 36 len floor32(_param4.length)]
      mem[(64 * _param4.length) + (32 * _param5.length) + 324] = (32 * _param4.length) + 160
      mem[(98 * _param4.length) + (32 * _param5.length) + 388] = mem[(32 * _param4.length) + (32 * _param5.length) + 192]
      mem[(98 * _param4.length) + (32 * _param5.length) + 420 len floor32(mem[(32 * _param4.length) + (32 * _param5.length) + 192])] = mem[(32 * _param4.length) + (32 * _param5.length) + 224 len floor32(mem[(32 * _param4.length) + (32 * _param5.length) + 192])]
      require ext_code.size(marketAddress)
      call marketAddress.0x1974884f with:
           gas gas_remaining - 710 wei
          args mem[(64 * _param4.length) + (32 * _param5.length) + 228 len (32 * mem[(32 * _param4.length) + (32 * _param5.length) + 192]) + (32 * _param4.length) + 192]
      require ext_call.success


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


