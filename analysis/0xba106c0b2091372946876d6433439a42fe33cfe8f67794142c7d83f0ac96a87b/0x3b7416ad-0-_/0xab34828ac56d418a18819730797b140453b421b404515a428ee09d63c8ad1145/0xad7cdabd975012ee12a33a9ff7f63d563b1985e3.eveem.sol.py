# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xAd7Cdabd975012ee12A33A9ff7f63D563B1985e3 
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
def unknown031f9c80(array m_param1, array m_param2) payable: 
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if m_param1.length:
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 192] = m_param1.length
      [94ms = 0
      [94midx = 0
      [94ms = call.value
      mwhile [94midx < m_param1.lengthm:
          require [94midx < m_param1.length
          [94m_84 = mem[(32 * [94midx) + 128]
          require [94midx < mem[(32 * m_param1.length) + 128]
          [94m_103 = mem[(32 * [94midx) + (32 * m_param1.length) + 160]
          mem[(64 * m_param1.length) + (32 * m_param2.length) + 256] = 0
          mem[(64 * m_param1.length) + (32 * m_param2.length) + 228] = caller
          require ext_code.size(addr([94m_84))
          call addr([94m_84).0xd9214ed5 with:
             value [94m_103 wei
               gas gas_remaining - 9710 wei
              args caller
          mem[(64 * m_param1.length) + (32 * m_param2.length) + 224] = ext_call.return_data[0]
          require ext_call.success
          require [94midx < mem[(32 * m_param1.length) + (32 * m_param2.length) + 192]
          mem[(32 * m_param1.length) + (32 * m_param2.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
          require [94midx < mem[(32 * m_param1.length) + (32 * m_param2.length) + 192]
          if not ext_call.return_data[0]:
              [94ms = [94m_84
              [94midx = [94midx + 1
              [94ms = [94ms
              mcontinue 
          require [94midx < mem[(32 * m_param1.length) + 128]
          [94ms = [94m_84
          [94midx = [94midx + 1
          [94ms = [94ms - mem[(32 * [94midx) + (32 * m_param1.length) + 160]
          mcontinue 
      if [94ms > 0:
          call caller with:
             value [94ms wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 224] = 0x1974884f00000000000000000000000000000000000000000000000000000000
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 228] = caller
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 260] = 1
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 292] = 128
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 356] = m_param1.length
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 388 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 324] = (32 * m_param1.length) + 160
      mem[(98 * m_param1.length) + (32 * m_param2.length) + 388] = mem[(32 * m_param1.length) + (32 * m_param2.length) + 192]
      mem[(98 * m_param1.length) + (32 * m_param2.length) + 420 len floor32(mem[(32 * m_param1.length) + (32 * m_param2.length) + 192])] = mem[(32 * m_param1.length) + (32 * m_param2.length) + 224 len floor32(mem[(32 * m_param1.length) + (32 * m_param2.length) + 192])]
      require ext_code.size(mmarketAddress)
      call mmarketAddress.0x1974884f with:
           gas gas_remaining - 710 wei
          args mem[(64 * m_param1.length) + (32 * m_param2.length) + 228 len (32 * mem[(32 * m_param1.length) + (32 * m_param2.length) + 192]) + (32 * m_param1.length) + 192]
      require ext_call.success


# hash = 0x25a0b2e1
# getter = None
# const = None
# payable = False
def unknown25a0b2e1(array m_param1): # not payable
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      [94m_9 = mem[(32 * [94midx) + 128]
      mem[(32 * m_param1.length) + 128] = 0x3b7416ad00000000000000000000000000000000000000000000000000000000
      mem[(32 * m_param1.length) + 132] = caller
      mem[(32 * m_param1.length) + 164] = addr([94m_9)
      require ext_code.size(mmarketAddress)
      call mmarketAddress.0x3b7416ad with:
           gas gas_remaining - 710 wei
          args caller, addr([94m_9)
      require ext_call.success
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x3a256949
# getter = None
# const = None
# payable = False
def unknown3a256949(array m_param1, array m_param2, array m_param3): # not payable
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = m_param3.length
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 192 len 32 * m_param3.length] = call.data[m_param3 + 36 len 32 * m_param3.length]
  require m_param1.length == m_param2.length
  require m_param1.length == m_param3.length
  [94ms = 0
  [94ms = 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      [94m_21 = mem[(32 * [94midx) + 128]
      require [94midx < m_param2.length
      [94m_23 = mem[(32 * [94midx) + (32 * m_param1.length) + 160]
      require [94midx < m_param3.length
      [94m_25 = mem[(32 * [94midx) + (32 * m_param1.length) + (32 * m_param2.length) + 192]
      if not mem[(32 * [94midx) + (32 * m_param1.length) + 160]:
          mem[(32 * m_param1.length) + (32 * m_param2.length) + (32 * m_param3.length) + 192] = 0xb82a097800000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param1.length) + (32 * m_param2.length) + (32 * m_param3.length) + 196] = caller
          mem[(32 * m_param1.length) + (32 * m_param2.length) + (32 * m_param3.length) + 228] = [94m_25
          require ext_code.size(addr([94m_21))
          call addr([94m_21).0xb82a0978 with:
               gas gas_remaining - 710 wei
              args caller, [94m_25
      else:
          mem[(32 * m_param1.length) + (32 * m_param2.length) + (32 * m_param3.length) + 192] = 0xdf9b8fff00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param1.length) + (32 * m_param2.length) + (32 * m_param3.length) + 196] = caller
          mem[(32 * m_param1.length) + (32 * m_param2.length) + (32 * m_param3.length) + 228] = [94m_25
          require ext_code.size(addr([94m_21))
          call addr([94m_21).0xdf9b8fff with:
               gas gas_remaining - 710 wei
              args caller, [94m_25
      require ext_call.success
      [94ms = [94m_25
      [94ms = [94m_23
      [94ms = [94m_21
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = False
def withdraw(): # not payable
  require mstor0 == caller
  call mstor0 with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  require ext_call.success


# hash = 0x47cf775d
# getter = None
# const = None
# payable = False
def unknown47cf775d(addr m_param1, uint256 m_param2, uint8 m_param3, uint32 m_param4, uint8 m_param5, bool m_param6): # not payable
  [94midx = 0
  mwhile uint8([94midx) < m_param3m:
      require m_param3
      mem[96] = 0xf401e49a00000000000000000000000000000000000000000000000000000000
      mem[100] = m_param1
      mem[132] = m_param4
      mem[164] = m_param5
      mem[196] = m_param6
      require ext_code.size(mmarketAddress)
      call mmarketAddress.0xf401e49a with:
         value m_param2 / m_param3 wei
           gas gas_remaining - 9710 wei
          args addr(m_param1), m_param4 << 224, m_param5 << 248, m_param6
      require ext_call.success
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x5dcc68de
# getter = None
# const = None
# payable = True
def unknown5dcc68de(array m_param1, array m_param2) payable: 
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if m_param1.length:
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 192] = m_param1.length
      [94ms = 0
      [94midx = 0
      [94ms = call.value
      mwhile [94midx < m_param1.lengthm:
          require [94midx < m_param1.length
          [94m_84 = mem[(32 * [94midx) + 128]
          require [94midx < mem[(32 * m_param1.length) + 128]
          [94m_103 = mem[(32 * [94midx) + (32 * m_param1.length) + 160]
          mem[(64 * m_param1.length) + (32 * m_param2.length) + 256] = 0
          mem[(64 * m_param1.length) + (32 * m_param2.length) + 228] = caller
          require ext_code.size(addr([94m_84))
          call addr([94m_84).0x5a0cf9f3 with:
             value [94m_103 wei
               gas gas_remaining - 9710 wei
              args caller
          mem[(64 * m_param1.length) + (32 * m_param2.length) + 224] = ext_call.return_data[0]
          require ext_call.success
          require [94midx < mem[(32 * m_param1.length) + (32 * m_param2.length) + 192]
          mem[(32 * m_param1.length) + (32 * m_param2.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
          require [94midx < mem[(32 * m_param1.length) + (32 * m_param2.length) + 192]
          if not ext_call.return_data[0]:
              [94ms = [94m_84
              [94midx = [94midx + 1
              [94ms = [94ms
              mcontinue 
          require [94midx < mem[(32 * m_param1.length) + 128]
          [94ms = [94m_84
          [94midx = [94midx + 1
          [94ms = [94ms - mem[(32 * [94midx) + (32 * m_param1.length) + 160]
          mcontinue 
      if [94ms > 0:
          call caller with:
             value [94ms wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 224] = 0x1974884f00000000000000000000000000000000000000000000000000000000
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 228] = caller
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 260] = 0
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 292] = 128
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 356] = m_param1.length
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 388 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
      mem[(64 * m_param1.length) + (32 * m_param2.length) + 324] = (32 * m_param1.length) + 160
      mem[(98 * m_param1.length) + (32 * m_param2.length) + 388] = mem[(32 * m_param1.length) + (32 * m_param2.length) + 192]
      mem[(98 * m_param1.length) + (32 * m_param2.length) + 420 len floor32(mem[(32 * m_param1.length) + (32 * m_param2.length) + 192])] = mem[(32 * m_param1.length) + (32 * m_param2.length) + 224 len floor32(mem[(32 * m_param1.length) + (32 * m_param2.length) + 192])]
      require ext_code.size(mmarketAddress)
      call mmarketAddress.0x1974884f with:
           gas gas_remaining - 710 wei
          args mem[(64 * m_param1.length) + (32 * m_param2.length) + 228 len (32 * mem[(32 * m_param1.length) + (32 * m_param2.length) + 192]) + (32 * m_param1.length) + 192]
      require ext_call.success


# hash = 0x69a82efc
# getter = None
# const = None
# payable = True
def unknown69a82efc(bool m_param1, array m_param2, array m_param3) payable: 
  mem[128 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param2.length) + 128] = m_param3.length
  mem[(32 * m_param2.length) + 160 len 32 * m_param3.length] = call.data[m_param3 + 36 len 32 * m_param3.length]
  mem[(32 * m_param2.length) + (32 * m_param3.length) + 160] = 0
  if m_param2.length:
      mem[(32 * m_param2.length) + (32 * m_param3.length) + 192] = m_param2.length
      [94ms = 0
      [94midx = 0
      [94ms = call.value
      mwhile [94midx < m_param2.lengthm:
          require [94midx < m_param2.length
          [94m_108 = mem[(32 * [94midx) + 128]
          if not m_param1:
              if [94midx < mem[(32 * m_param2.length) + 128]:
                  [94m_133 = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
                  mem[(64 * m_param2.length) + (32 * m_param3.length) + 256] = 0
                  mem[(64 * m_param2.length) + (32 * m_param3.length) + 228] = caller
                  require ext_code.size(addr([94m_108))
                  call addr([94m_108).0x5a0cf9f3 with:
                     value [94m_133 wei
                       gas gas_remaining - 9710 wei
                      args caller
                  mem[(64 * m_param2.length) + (32 * m_param3.length) + 224] = ext_call.return_data[0]
                  require ext_call.success
                  if [94midx < mem[(32 * m_param2.length) + (32 * m_param3.length) + 192]:
                      mem[(32 * m_param2.length) + (32 * m_param3.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
                      if [94midx < mem[(32 * m_param2.length) + (32 * m_param3.length) + 192]:
                          if not ext_call.return_data[0]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              mcontinue 
                          if [94midx < mem[(32 * m_param2.length) + 128]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms - mem[(32 * [94midx) + (32 * m_param2.length) + 160]
                              mcontinue 
          else:
              if [94midx < mem[(32 * m_param2.length) + 128]:
                  [94m_137 = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
                  mem[(64 * m_param2.length) + (32 * m_param3.length) + 256] = 0
                  mem[(64 * m_param2.length) + (32 * m_param3.length) + 228] = caller
                  require ext_code.size(addr([94m_108))
                  call addr([94m_108).0xd9214ed5 with:
                     value [94m_137 wei
                       gas gas_remaining - 9710 wei
                      args caller
                  mem[(64 * m_param2.length) + (32 * m_param3.length) + 224] = ext_call.return_data[0]
                  require ext_call.success
                  if [94midx < mem[(32 * m_param2.length) + (32 * m_param3.length) + 192]:
                      mem[(32 * m_param2.length) + (32 * m_param3.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
                      if [94midx < mem[(32 * m_param2.length) + (32 * m_param3.length) + 192]:
                          if not ext_call.return_data[0]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              mcontinue 
                          if [94midx < mem[(32 * m_param2.length) + 128]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms - mem[(32 * [94midx) + (32 * m_param2.length) + 160]
                              mcontinue 
          revert
      if [94ms > 0:
          call caller with:
             value [94ms wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
      mem[(64 * m_param2.length) + (32 * m_param3.length) + 224] = 0x1974884f00000000000000000000000000000000000000000000000000000000
      mem[(64 * m_param2.length) + (32 * m_param3.length) + 228] = caller
      mem[(64 * m_param2.length) + (32 * m_param3.length) + 260] = m_param1
      mem[(64 * m_param2.length) + (32 * m_param3.length) + 292] = 128
      mem[(64 * m_param2.length) + (32 * m_param3.length) + 356] = m_param2.length
      mem[(64 * m_param2.length) + (32 * m_param3.length) + 388 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
      mem[(64 * m_param2.length) + (32 * m_param3.length) + 324] = (32 * m_param2.length) + 160
      mem[(98 * m_param2.length) + (32 * m_param3.length) + 388] = mem[(32 * m_param2.length) + (32 * m_param3.length) + 192]
      mem[(98 * m_param2.length) + (32 * m_param3.length) + 420 len floor32(mem[(32 * m_param2.length) + (32 * m_param3.length) + 192])] = mem[(32 * m_param2.length) + (32 * m_param3.length) + 224 len floor32(mem[(32 * m_param2.length) + (32 * m_param3.length) + 192])]
      require ext_code.size(mmarketAddress)
      call mmarketAddress.0x1974884f with:
           gas gas_remaining - 710 wei
          args mem[(64 * m_param2.length) + (32 * m_param3.length) + 228 len (32 * mem[(32 * m_param2.length) + (32 * m_param3.length) + 192]) + (32 * m_param2.length) + 192]
      require ext_call.success


# hash = 0x6dcea85f
# getter = None
# const = None
# payable = False
def setMarket(address m_add): # not payable
  require mstor0 == caller
  mmarketAddress = m_add


# hash = 0x7141f423
# getter = None
# const = None
# payable = True
def unknown7141f423(uint8 m_param1, uint32 m_param2, uint8 m_param3, array m_param4, array m_param5, bool m_param6) payable: 
  mem[96] = m_param4.length
  mem[128 len 32 * m_param4.length] = call.data[m_param4 + 36 len 32 * m_param4.length]
  mem[(32 * m_param4.length) + 128] = m_param5.length
  mem[(32 * m_param4.length) + 160 len 32 * m_param5.length] = call.data[m_param5 + 36 len 32 * m_param5.length]
  if not m_param6:
      require m_param3 - 1
      [94midx = 0
      mwhile uint8([94midx) < m_param1m:
          require m_param1
          [94m_199 = (32 * m_param4.length) + (32 * m_param5.length) + 160
          mem[(32 * m_param4.length) + (32 * m_param5.length) + 160] = 0xf401e49a00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param5.length) + 164] = caller
          mem[(32 * m_param4.length) + (32 * m_param5.length) + 196] = m_param2
          mem[(32 * m_param4.length) + (32 * m_param5.length) + 228] = m_param3
          mem[(32 * m_param4.length) + (32 * m_param5.length) + 260] = m_param6
          require ext_code.size(mmarketAddress)
          call mmarketAddress.0xf401e49a with:
             value m_param1 * 10 * 10^18 / m_param3 - 1 / m_param1 wei
               gas gas_remaining - 9710 wei
              args caller, m_param2 << 224, m_param3 << 248, m_param6
          require ext_call.success
          [94midx = [94midx + 1
          mcontinue 
      mem[(32 * m_param4.length) + (32 * m_param5.length) + 160] = 0
      if m_param4.length:
          [94m_msize = max((32 * m_param4.length) + (32 * m_param5.length) + 60, (32 * m_param4.length) + (32 * m_param5.length) + 96, [94m_199)
          mem[[94m_msize + 132] = m_param4.length
          mem[64] = ([94m_msize + 132) + (32 * m_param4.length) + 32
          [94ms = 0
          [94midx = 0
          [94ms = call.value - (m_param1 * 10 * 10^18 / m_param3 - 1)
          mwhile [94midx < m_param4.lengthm:
              require [94midx < m_param4.length
              [94m_408 = mem[(32 * [94midx) + 128]
              if not m_param6:
                  if [94midx < m_param5.length:
                      [94m_449 = mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 64] = 0
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 36] = caller
                      require ext_code.size(addr([94m_408))
                      call addr([94m_408).0x5a0cf9f3 with:
                         value [94m_449 wei
                           gas gas_remaining - 9710 wei
                          args caller
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 32] = ext_call.return_data[0]
                      require ext_call.success
                      if [94midx < mem[[94m_msize + 132]:
                          mem[([94m_msize + 132) + (32 * [94midx) + 32] = bool(ext_call.return_data[0])
                          if [94midx < mem[[94m_msize + 132]:
                              if not ext_call.return_data[0]:
                                  [94ms = [94m_408
                                  [94midx = [94midx + 1
                                  [94ms = [94ms
                                  mcontinue 
                              if [94midx < m_param5.length:
                                  [94ms = [94m_408
                                  [94midx = [94midx + 1
                                  [94ms = [94ms - mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                                  mcontinue 
              else:
                  if [94midx < m_param5.length:
                      [94m_453 = mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 64] = 0
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 36] = caller
                      require ext_code.size(addr([94m_408))
                      call addr([94m_408).0xd9214ed5 with:
                         value [94m_453 wei
                           gas gas_remaining - 9710 wei
                          args caller
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 32] = ext_call.return_data[0]
                      require ext_call.success
                      if [94midx < mem[[94m_msize + 132]:
                          mem[([94m_msize + 132) + (32 * [94midx) + 32] = bool(ext_call.return_data[0])
                          if [94midx < mem[[94m_msize + 132]:
                              if not ext_call.return_data[0]:
                                  [94ms = [94m_408
                                  [94midx = [94midx + 1
                                  [94ms = [94ms
                                  mcontinue 
                              if [94midx < m_param5.length:
                                  [94ms = [94m_408
                                  [94midx = [94midx + 1
                                  [94ms = [94ms - mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                                  mcontinue 
              revert
          if [94ms > 0:
              call caller with:
                 value [94ms wei
                   gas 2300 * is_zero(value) wei
              require ext_call.success
          mem[([94m_msize + 132) + (32 * m_param4.length) + 32] = 0x1974884f00000000000000000000000000000000000000000000000000000000
          mem[([94m_msize + 132) + (32 * m_param4.length) + 36] = caller
          mem[([94m_msize + 132) + (32 * m_param4.length) + 68] = m_param6
          mem[([94m_msize + 132) + (32 * m_param4.length) + 100] = 128
          mem[([94m_msize + 132) + (32 * m_param4.length) + 164] = m_param4.length
          mem[([94m_msize + 132) + (32 * m_param4.length) + 196 len floor32(m_param4.length)] = call.data[m_param4 + 36 len floor32(m_param4.length)]
          mem[([94m_msize + 132) + (32 * m_param4.length) + 132] = (32 * m_param4.length) + 160
          mem[(64 * m_param4.length) + ([94m_msize + 132) + 196] = mem[[94m_msize + 132]
          mem[(64 * m_param4.length) + ([94m_msize + 132) + 228 len floor32(mem[[94m_msize + 132])] = mem[([94m_msize + 132) + 32 len floor32(mem[[94m_msize + 132])]
          require ext_code.size(mmarketAddress)
          call mmarketAddress.0x1974884f with:
               gas gas_remaining - 710 wei
              args caller, m_param6, Array(len=m_param4.length, data=mem[([94m_msize + 132) + (32 * m_param4.length) + 196 len (32 * mem[[94m_msize + 132]) + (32 * m_param4.length) + 32]), (32 * m_param4.length) + 160
          require ext_call.success
  else:
      require m_param3 + 1
      [94midx = 0
      mwhile uint8([94midx) < m_param1m:
          require m_param1
          [94m_201 = (32 * m_param4.length) + (32 * m_param5.length) + 160
          mem[(32 * m_param4.length) + (32 * m_param5.length) + 160] = 0xf401e49a00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param5.length) + 164] = caller
          mem[(32 * m_param4.length) + (32 * m_param5.length) + 196] = m_param2
          mem[(32 * m_param4.length) + (32 * m_param5.length) + 228] = m_param3
          mem[(32 * m_param4.length) + (32 * m_param5.length) + 260] = m_param6
          require ext_code.size(mmarketAddress)
          call mmarketAddress.0xf401e49a with:
             value m_param1 * 10 * 10^18 / m_param3 + 1 / m_param1 wei
               gas gas_remaining - 9710 wei
              args caller, m_param2 << 224, m_param3 << 248, m_param6
          require ext_call.success
          [94midx = [94midx + 1
          mcontinue 
      mem[(32 * m_param4.length) + (32 * m_param5.length) + 160] = 0
      if m_param4.length:
          [94m_msize = max((32 * m_param4.length) + (32 * m_param5.length) + 60, (32 * m_param4.length) + (32 * m_param5.length) + 96, [94m_201)
          mem[[94m_msize + 132] = m_param4.length
          mem[64] = ([94m_msize + 132) + (32 * m_param4.length) + 32
          [94ms = 0
          [94midx = 0
          [94ms = call.value - (m_param1 * 10 * 10^18 / m_param3 + 1)
          mwhile [94midx < m_param4.lengthm:
              require [94midx < m_param4.length
              [94m_414 = mem[(32 * [94midx) + 128]
              if not m_param6:
                  if [94midx < m_param5.length:
                      [94m_471 = mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 64] = 0
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 36] = caller
                      require ext_code.size(addr([94m_414))
                      call addr([94m_414).0x5a0cf9f3 with:
                         value [94m_471 wei
                           gas gas_remaining - 9710 wei
                          args caller
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 32] = ext_call.return_data[0]
                      require ext_call.success
                      if [94midx < mem[[94m_msize + 132]:
                          mem[([94m_msize + 132) + (32 * [94midx) + 32] = bool(ext_call.return_data[0])
                          if [94midx < mem[[94m_msize + 132]:
                              if not ext_call.return_data[0]:
                                  [94ms = [94m_414
                                  [94midx = [94midx + 1
                                  [94ms = [94ms
                                  mcontinue 
                              if [94midx < m_param5.length:
                                  [94ms = [94m_414
                                  [94midx = [94midx + 1
                                  [94ms = [94ms - mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                                  mcontinue 
              else:
                  if [94midx < m_param5.length:
                      [94m_475 = mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 64] = 0
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 36] = caller
                      require ext_code.size(addr([94m_414))
                      call addr([94m_414).0xd9214ed5 with:
                         value [94m_475 wei
                           gas gas_remaining - 9710 wei
                          args caller
                      mem[([94m_msize + 132) + (32 * m_param4.length) + 32] = ext_call.return_data[0]
                      require ext_call.success
                      if [94midx < mem[[94m_msize + 132]:
                          mem[([94m_msize + 132) + (32 * [94midx) + 32] = bool(ext_call.return_data[0])
                          if [94midx < mem[[94m_msize + 132]:
                              if not ext_call.return_data[0]:
                                  [94ms = [94m_414
                                  [94midx = [94midx + 1
                                  [94ms = [94ms
                                  mcontinue 
                              if [94midx < m_param5.length:
                                  [94ms = [94m_414
                                  [94midx = [94midx + 1
                                  [94ms = [94ms - mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                                  mcontinue 
              revert
          if [94ms > 0:
              call caller with:
                 value [94ms wei
                   gas 2300 * is_zero(value) wei
              require ext_call.success
          mem[([94m_msize + 132) + (32 * m_param4.length) + 32] = 0x1974884f00000000000000000000000000000000000000000000000000000000
          mem[([94m_msize + 132) + (32 * m_param4.length) + 36] = caller
          mem[([94m_msize + 132) + (32 * m_param4.length) + 68] = m_param6
          mem[([94m_msize + 132) + (32 * m_param4.length) + 100] = 128
          mem[([94m_msize + 132) + (32 * m_param4.length) + 164] = m_param4.length
          mem[([94m_msize + 132) + (32 * m_param4.length) + 196 len floor32(m_param4.length)] = call.data[m_param4 + 36 len floor32(m_param4.length)]
          mem[([94m_msize + 132) + (32 * m_param4.length) + 132] = (32 * m_param4.length) + 160
          mem[(64 * m_param4.length) + ([94m_msize + 132) + 196] = mem[[94m_msize + 132]
          mem[(64 * m_param4.length) + ([94m_msize + 132) + 228 len floor32(mem[[94m_msize + 132])] = mem[([94m_msize + 132) + 32 len floor32(mem[[94m_msize + 132])]
          require ext_code.size(mmarketAddress)
          call mmarketAddress.0x1974884f with:
               gas gas_remaining - 710 wei
              args caller, m_param6, Array(len=m_param4.length, data=mem[([94m_msize + 132) + (32 * m_param4.length) + 196 len (32 * mem[[94m_msize + 132]) + (32 * m_param4.length) + 32]), (32 * m_param4.length) + 160
          require ext_call.success


# hash = 0x80f55605
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def market(): # not payable
  return mmarketAddress


# hash = 0xacbbf3ac
# getter = None
# const = None
# payable = False
def unknownacbbf3ac(uint256 m_param1): # not payable
  require m_param1 + 1
  return (10 * 10^18 / m_param1 + 1)


# hash = 0xd87789e0
# getter = None
# const = None
# payable = False
def unknownd87789e0(uint256 m_param1): # not payable
  require m_param1 - 1
  return (10 * 10^18 / m_param1 - 1)


# hash = 0xdcd78126
# getter = None
# const = None
# payable = True
def unknowndcd78126(uint8 m_param1, uint32 m_param2, uint8 m_param3, bool m_param4) payable: 
  [94midx = 0
  mwhile uint8([94midx) < m_param1m:
      require m_param1
      mem[96] = 0xf401e49a00000000000000000000000000000000000000000000000000000000
      mem[100] = caller
      mem[132] = m_param2
      mem[164] = m_param3
      mem[196] = m_param4
      require ext_code.size(mmarketAddress)
      call mmarketAddress.0xf401e49a with:
         value call.value / m_param1 wei
           gas gas_remaining - 9710 wei
          args caller, m_param2 << 224, m_param3 << 248, m_param4
      require ext_call.success
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xfd29e664
# getter = None
# const = None
# payable = False
def unknownfd29e664(addr m_param1, uint256 m_param2, bool m_param3, array m_param4, array m_param5): # not payable
  mem[128 len 32 * m_param4.length] = call.data[m_param4 + 36 len 32 * m_param4.length]
  mem[(32 * m_param4.length) + 128] = m_param5.length
  mem[(32 * m_param4.length) + 160 len 32 * m_param5.length] = call.data[m_param5 + 36 len 32 * m_param5.length]
  mem[(32 * m_param4.length) + (32 * m_param5.length) + 160] = 0
  if m_param4.length:
      mem[(32 * m_param4.length) + (32 * m_param5.length) + 192] = m_param4.length
      [94ms = 0
      [94midx = 0
      [94ms = m_param2
      mwhile [94midx < m_param4.lengthm:
          require [94midx < m_param4.length
          [94m_108 = mem[(32 * [94midx) + 128]
          if not m_param3:
              if [94midx < mem[(32 * m_param4.length) + 128]:
                  [94m_133 = mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                  mem[(64 * m_param4.length) + (32 * m_param5.length) + 256] = 0
                  mem[(64 * m_param4.length) + (32 * m_param5.length) + 228] = m_param1
                  require ext_code.size(addr([94m_108))
                  call addr([94m_108).0x5a0cf9f3 with:
                     value [94m_133 wei
                       gas gas_remaining - 9710 wei
                      args m_param1
                  mem[(64 * m_param4.length) + (32 * m_param5.length) + 224] = ext_call.return_data[0]
                  require ext_call.success
                  if [94midx < mem[(32 * m_param4.length) + (32 * m_param5.length) + 192]:
                      mem[(32 * m_param4.length) + (32 * m_param5.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
                      if [94midx < mem[(32 * m_param4.length) + (32 * m_param5.length) + 192]:
                          if not ext_call.return_data[0]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              mcontinue 
                          if [94midx < mem[(32 * m_param4.length) + 128]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms - mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                              mcontinue 
          else:
              if [94midx < mem[(32 * m_param4.length) + 128]:
                  [94m_137 = mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                  mem[(64 * m_param4.length) + (32 * m_param5.length) + 256] = 0
                  mem[(64 * m_param4.length) + (32 * m_param5.length) + 228] = m_param1
                  require ext_code.size(addr([94m_108))
                  call addr([94m_108).0xd9214ed5 with:
                     value [94m_137 wei
                       gas gas_remaining - 9710 wei
                      args m_param1
                  mem[(64 * m_param4.length) + (32 * m_param5.length) + 224] = ext_call.return_data[0]
                  require ext_call.success
                  if [94midx < mem[(32 * m_param4.length) + (32 * m_param5.length) + 192]:
                      mem[(32 * m_param4.length) + (32 * m_param5.length) + (32 * [94midx) + 224] = bool(ext_call.return_data[0])
                      if [94midx < mem[(32 * m_param4.length) + (32 * m_param5.length) + 192]:
                          if not ext_call.return_data[0]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms
                              mcontinue 
                          if [94midx < mem[(32 * m_param4.length) + 128]:
                              [94ms = [94m_108
                              [94midx = [94midx + 1
                              [94ms = [94ms - mem[(32 * [94midx) + (32 * m_param4.length) + 160]
                              mcontinue 
          revert
      if [94ms > 0:
          call m_param1 with:
             value [94ms wei
               gas 2300 * is_zero(value) wei
          require ext_call.success
      mem[(64 * m_param4.length) + (32 * m_param5.length) + 224] = 0x1974884f00000000000000000000000000000000000000000000000000000000
      mem[(64 * m_param4.length) + (32 * m_param5.length) + 228] = m_param1
      mem[(64 * m_param4.length) + (32 * m_param5.length) + 260] = m_param3
      mem[(64 * m_param4.length) + (32 * m_param5.length) + 292] = 128
      mem[(64 * m_param4.length) + (32 * m_param5.length) + 356] = m_param4.length
      mem[(64 * m_param4.length) + (32 * m_param5.length) + 388 len floor32(m_param4.length)] = call.data[m_param4 + 36 len floor32(m_param4.length)]
      mem[(64 * m_param4.length) + (32 * m_param5.length) + 324] = (32 * m_param4.length) + 160
      mem[(98 * m_param4.length) + (32 * m_param5.length) + 388] = mem[(32 * m_param4.length) + (32 * m_param5.length) + 192]
      mem[(98 * m_param4.length) + (32 * m_param5.length) + 420 len floor32(mem[(32 * m_param4.length) + (32 * m_param5.length) + 192])] = mem[(32 * m_param4.length) + (32 * m_param5.length) + 224 len floor32(mem[(32 * m_param4.length) + (32 * m_param5.length) + 192])]
      require ext_code.size(mmarketAddress)
      call mmarketAddress.0x1974884f with:
           gas gas_remaining - 710 wei
          args mem[(64 * m_param4.length) + (32 * m_param5.length) + 228 len (32 * mem[(32 * m_param4.length) + (32 * m_param5.length) + 192]) + (32 * m_param4.length) + 192]
      require ext_call.success


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


