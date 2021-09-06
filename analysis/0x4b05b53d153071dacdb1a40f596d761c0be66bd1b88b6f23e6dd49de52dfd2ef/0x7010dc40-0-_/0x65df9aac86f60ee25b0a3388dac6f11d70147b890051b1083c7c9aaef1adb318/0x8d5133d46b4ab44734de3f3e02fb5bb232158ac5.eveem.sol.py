# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x8d5133D46B4aB44734de3F3E02FB5bb232158AC5 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    exchangeAddress # mask: a s
    # storage address 2
    unknown97d6958d
    # storage address 3
    unknown47b922db # mask: a s
    # storage address 4
    unknowne5091753
    # storage address 5
    unknown2b742f50 # mask: a s
    # storage address 6
    stor6
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    unknown65139292 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 10
    stor10 # mask: a s
    # storage address 11
    stor11 # mask: a s
    # storage address 12
    stor12 # mask: a s
    # storage address 13
    unknown7d704810 # mask: a s
# hash = 0x11317681
# getter = ['storage', 256, 0, ['add', ['sha3', 4], ['cd', 4]]]
# const = None
# payable = False
def unknown11317681(uint256 m_param1): # not payable
  require m_param1 < munknowne5091753m.length
  return munknowne5091753m[m_param1m]


# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address m_newOwner): # not payable
  if mowner != caller:
      revert with 0, '1'
  mowner = m_newOwner


# hash = 0x2b742f50
# getter = ['storage', 8, 0, 5]
# const = None
# payable = False
def unknown2b742f50(): # not payable
  require munknown2b742f50 <= 4
  return munknown2b742f50


# hash = 0x4051ddac
# getter = None
# const = None
# payable = False
def getSummary(): # not payable
  return eth.balance(mowner), mstor9, mstor10, mstor11, mstor7, munknown65139292, munknown7d704810


# hash = 0x47b922db
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknown47b922db(): # not payable
  return munknown47b922db


# hash = 0x4988b70e
# getter = None
# const = None
# payable = True
def unknown4988b70e() payable: 
  stop


# hash = 0x4a797a55
# getter = None
# const = None
# payable = False
def unknown4a797a55(uint256 m_param1): # not payable
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(mexchangeAddress)
          call mexchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, '13'
  if m_param1 <= eth.balance(this.address):
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x2fe6a1e6 with:
         value m_param1 wei
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      munknown7d704810 -= m_param1
  else:
      log 0x1d37a599: ext_call.return_data[0], _param1 - eth.balance(this.address), 14, 'los in fixLoss'
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x2fe6a1e6 with:
         value eth.balance(this.address) wei
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      munknown7d704810 -= eth.balance(this.address)


# hash = 0x4b15908c
# getter = None
# const = None
# payable = False
def unknown4b15908c(uint8 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5): # not payable
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(mexchangeAddress)
          call mexchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, '13'
  require m_param1 <= 4
  uint8(munknown97d6958dm[m_param2m]m.field_296) = m_param1
  uint32(munknown97d6958dm[m_param2m]m.field_32) = uint32(block.timestamp)
  Mask(192, 0, munknown97d6958dm[m_param2m]m.field_64) = Mask(144, 0, munknown97d6958dm[m_param2m]m.field_64)
  munknown97d6958dm[m_param2m]m.field_208 % 1099511627776 = ('signextend', 4, ('sdiv', ('param', '_param3'), 1000000000000)) % 1099511627776
  munknown97d6958dm[m_param2m]m.field_256 % 1099511627776 = ('signextend', 4, ('sdiv', ('param', '_param5'), 1000000000000)) % 1099511627776
  [94midx = 0
  mwhile [94midx < munknowne5091753m.lengthm:
      mem[0] = 4
      if munknowne5091753m[[94midxm] != m_param2:
          [94midx = [94midx + 1
          mcontinue 
      if [94midx == munknowne5091753m.length - 1:
          require [94midx < munknowne5091753m.length
          munknowne5091753m[[94midxm] = 0
      else:
          require munknowne5091753m.length - 1 < munknowne5091753m.length
          require [94midx < munknowne5091753m.length
          munknowne5091753m[[94midxm] = munknowne5091753m[munknowne5091753m.lengthm]
          require munknowne5091753m.length - 1 < munknowne5091753m.length
          munknowne5091753m[munknowne5091753m.lengthm] = 0
      munknowne5091753m.length--
      if munknowne5091753m.length > munknowne5091753m.length - 1:
          [94midx = munknowne5091753m.length + sha3(4) - 1
          mwhile sha3(4) + munknowne5091753m.length > [94midxm:
              mstor[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x2d8815c8 with:
         value m_param4 wei
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      mstor9 += m_param4
      stop
  require ext_code.size(mexchangeAddress)
  call mexchangeAddress.0x2d8815c8 with:
     value m_param4 wei
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mstor9 += m_param4


# hash = 0x4d12f044
# getter = ['struct', ['loc', 2]]
# const = None
# payable = False
def unknown4d12f044(uint256 m_param1): # not payable
  require uint8(munknown97d6958dm[m_param1m]m.field_296) <= 4
  return uint32(munknown97d6958dm[m_param1m]m.field_0), 
         uint32(munknown97d6958dm[m_param1m]m.field_0),
         uint32(munknown97d6958dm[m_param1m]m.field_32)


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


# hash = 0x5b7ce8c9
# getter = None
# const = None
# payable = True
def unknown5b7ce8c9() payable: 
  if mexchangeAddress != caller:
      revert with 0, '14'
  munknown7d704810 += call.value


# hash = 0x5ee74564
# getter = None
# const = None
# payable = False
def unknown5ee74564(): # not payable
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      return 1
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 2:
      return 2
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 3:
      return 3
  require munknown2b742f50 <= 4
  if munknown2b742f50 != 4:
      revert with 0, '4'
  return 4


# hash = 0x62e039f0
# getter = None
# const = None
# payable = True
def unknown62e039f0() payable: 
  if mexchangeAddress != caller:
      revert with 0, '14'


# hash = 0x65139292
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def unknown65139292(): # not payable
  return munknown65139292


# hash = 0x7010dc40
# getter = None
# const = None
# payable = False
def unknown7010dc40(uint32 m_param1, uint256 m_param2): # not payable
  if mowner != caller:
      revert with 0, '1'
  if not m_param2:
      revert with 0, '18'
  if not m_param1:
      revert with 0, '19'
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(mexchangeAddress)
          call mexchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x8ba002fc with:
       gas gas_remaining wei
      args this.address, m_param1 << 224, m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not ext_call.return_data[0]:
      log 0xc39f0786: ext_call.return_data[32]
      return 0
  uint32(munknown97d6958dm[mstor3m]m.field_0) = m_param1
  uint8(munknown97d6958dm[mstor3m]m.field_296) = 0
  uint32(munknown97d6958dm[mstor3m]m.field_64) = uint32(block.timestamp)
  addr(munknown97d6958dm[mstor3m]m.field_96) = uint32(munknown97d6958dm[mstor3m]m.field_96)
  munknown97d6958dm[mstor3m]m.field_128 % 1099511627776 = ('signextend', 4, ('sdiv', ('param', '_param2'), 1000000000000)) % 1099511627776
  munknowne5091753m.length++
  munknowne5091753m[munknowne5091753m.lengthm] = munknown47b922db
  munknown47b922db++
  return munknowne5091753m.length


# hash = 0x740a2ab3
# getter = ['struct', ['loc', 2]]
# const = None
# payable = False
def unknown740a2ab3(uint256 m_param1): # not payable
  require uint8(munknown97d6958dm[m_param1m]m.field_296) <= 4
  require uint8(munknown97d6958dm[m_param1m]m.field_296) <= 4
  return uint32(munknown97d6958dm[m_param1m]m.field_0), 
         10^12 * ('signextend', 4, ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 128, ('field', 128, ('stor', ('map', ('param', '_param1'), ('name', 'unknown97d6958d', 2))))))))),
         10^12 * ('signextend', 4, ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 88, ('field', 168, ('stor', ('map', ('param', '_param1'), ('name', 'unknown97d6958d', 2))))))))),
         10^12 * ('signextend', 4, ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 48, ('field', 208, ('stor', ('map', ('param', '_param1'), ('name', 'unknown97d6958d', 2))))))))),
         uint8(munknown97d6958dm[m_param1m]m.field_256),
         10^12 * ('signextend', 4, ('signextend', 4, ('signextend', 4, ('signextend', 4, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'unknown97d6958d', 2))))))))


# hash = 0x76ea9b4e
# getter = None
# const = None
# payable = False
def unknown76ea9b4e(uint256 m_param1): # not payable
  if mowner != caller:
      revert with 0, '1'
  require uint8(munknown97d6958dm[m_param1m]m.field_296) <= 4
  if uint8(munknown97d6958dm[m_param1m]m.field_296) != 2:
      revert with 0, '21'
  uint8(munknown97d6958dm[m_param1m]m.field_296) = 3


# hash = 0x7c5d4050
# getter = None
# const = None
# payable = False
def unknown7c5d4050(uint256 m_param1): # not payable
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(mexchangeAddress)
          call mexchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, '13'
  if m_param1 > eth.balance(this.address):
      revert with 0, '17'
  if m_param1 != munknown65139292:
      revert with 0, '17'
  mstor11 += m_param1
  munknown65139292 = 0
  call mowner with:
     value m_param1 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x1639a0b3: _param1


# hash = 0x7d704810
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknown7d704810(): # not payable
  return munknown7d704810


# hash = 0x7d8aac96
# getter = None
# const = None
# payable = False
def unknown7d8aac96(uint256 m_param1): # not payable
  if mowner != caller:
      revert with 0, '1'
  if m_param1 + munknown65139292 >= eth.balance(this.address):
      revert with 0, '16'
  munknown65139292 += m_param1
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(mexchangeAddress)
          call mexchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xae375d05 with:
       gas gas_remaining wei
      args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != 1:
      mstor6m[mstor7m] = m_param1
      log 0x46349e9c: stor7, _param1
  else:
      munknown65139292 = 0
      call mowner with:
         value m_param1 wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log 0x1639a0b3: _param1
  mstor7++


# hash = 0x80d23170
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def unknown80d23170(): # not payable
  return munknowne5091753m.length


# hash = 0x893d20e8
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def getOwner(): # not payable
  return mowner


# hash = 0x896796ef
# getter = None
# const = None
# payable = False
def unknown896796ef(uint256 m_param1): # not payable
  if m_param1 <= eth.balance(this.address):
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x5fecf62c with:
         value m_param1 wei
           gas gas_remaining wei
  else:
      log 0x1d37a599: Array(len=17, data='los in revert gas'), _param1 - eth.balance(this.address)
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x5fecf62c with:
         value eth.balance(this.address) wei
           gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x8b2dbfab
# getter = None
# const = None
# payable = False
def unknown8b2dbfab(array m_param1, array m_param2, uint256 m_param3): # not payable
  mem[128 len m_param1.length] = m_param1[allm]
  mem[ceil32(m_param1.length) + 128] = m_param2.length
  mem[ceil32(m_param1.length) + 160 len m_param2.length] = m_param2[allm]
  if mowner != caller:
      revert with 0, '1'
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(mexchangeAddress)
          call mexchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160] = 0x60bb4cbf00000000000000000000000000000000000000000000000000000000
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 260 len ceil32(m_param1.length)] = m_param1[allm], mem[m_param1.length + 128 len ceil32(m_param1.length) - m_param1.length]
  mem[m_param1.length + ceil32(m_param1.length) + ceil32(m_param2.length) + 260] = m_param2.length
  mem[m_param1.length + ceil32(m_param1.length) + ceil32(m_param2.length) + 292 len ceil32(m_param2.length)] = m_param2[allm], mem[ceil32(m_param1.length) + m_param2.length + 160 len ceil32(m_param2.length) - m_param2.length]
  if not m_param2.length % 32:
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x60bb4cbf with:
           gas gas_remaining wei
          args Array(len=m_param1.length, data=Mask(8 * ceil32(m_param1.length), -(8 * ceil32(m_param1.length)) + 256, m_param1[allm], mem[m_param1.length + 128 len ceil32(m_param1.length) - m_param1.length]) << (8 * ceil32(m_param1.length)) - 256, mem[(2 * ceil32(m_param1.length)) + ceil32(m_param2.length) + 260 len m_param2.length + m_param1.length + -ceil32(m_param1.length) + 32]), m_param1.length + 96
  else:
      mem[floor32(m_param2.length) + m_param1.length + ceil32(m_param1.length) + ceil32(m_param2.length) + 292] = mem[floor32(m_param2.length) + m_param1.length + ceil32(m_param1.length) + ceil32(m_param2.length) + -(m_param2.length % 32) + 324 len m_param2.length % 32]
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x60bb4cbf with:
           gas gas_remaining wei
          args Array(len=m_param1.length, data=Mask(8 * ceil32(m_param1.length), -(8 * ceil32(m_param1.length)) + 256, m_param1[allm], mem[m_param1.length + 128 len ceil32(m_param1.length) - m_param1.length]) << (8 * ceil32(m_param1.length)) - 256, mem[(2 * ceil32(m_param1.length)) + ceil32(m_param2.length) + 260 len floor32(m_param2.length) + m_param1.length + -ceil32(m_param1.length) + 64]), m_param1.length + 96
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mowner != caller:
      revert with 0, '1'
  if not m_param3:
      revert with 0, '18'
  if not ext_call.return_data[28 len 4]:
      revert with 0, '19'
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(mexchangeAddress)
          call mexchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x8ba002fc with:
       gas gas_remaining wei
      args this.address, ext_call.return_data[0] << 224, m_param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not ext_call.return_data[0]:
      log 0xc39f0786: ext_call.return_data[32]
      return 0
  uint32(munknown97d6958dm[mstor3m]m.field_0) = uint32(ext_call.return_data[0])
  uint8(munknown97d6958dm[mstor3m]m.field_296) = 0
  uint32(munknown97d6958dm[mstor3m]m.field_64) = uint32(block.timestamp)
  addr(munknown97d6958dm[mstor3m]m.field_96) = uint32(munknown97d6958dm[mstor3m]m.field_96)
  munknown97d6958dm[mstor3m]m.field_128 % 1099511627776 = ('signextend', 4, ('sdiv', ('param', '_param3'), 1000000000000)) % 1099511627776
  munknowne5091753m.length++
  munknowne5091753m[munknowne5091753m.lengthm] = munknown47b922db
  munknown47b922db++
  return munknowne5091753m.length


# hash = 0x935c9ad2
# getter = None
# const = None
# payable = False
def CancelOrder(uint256 m_id): # not payable
  if mowner != caller:
      revert with 0, '1'
  require uint8(munknown97d6958dm[m_idm]m.field_296) <= 4
  if uint8(munknown97d6958dm[m_idm]m.field_296):
      revert with 0, '20'
  uint8(munknown97d6958dm[m_idm]m.field_296) = 1
  uint32(munknown97d6958dm[m_idm]m.field_32) = uint32(block.timestamp)
  Mask(192, 0, munknown97d6958dm[m_idm]m.field_64) = Mask(144, 0, munknown97d6958dm[m_idm]m.field_64)
  munknown97d6958dm[m_idm]m.field_256 % 1099511627776 = 0
  [94midx = 0
  mwhile [94midx < munknowne5091753m.lengthm:
      mem[0] = 4
      if munknowne5091753m[[94midxm] != m_id:
          [94midx = [94midx + 1
          mcontinue 
      if [94midx == munknowne5091753m.length - 1:
          require [94midx < munknowne5091753m.length
          munknowne5091753m[[94midxm] = 0
      else:
          require munknowne5091753m.length - 1 < munknowne5091753m.length
          require [94midx < munknowne5091753m.length
          munknowne5091753m[[94midxm] = munknowne5091753m[munknowne5091753m.lengthm]
          require munknowne5091753m.length - 1 < munknowne5091753m.length
          munknowne5091753m[munknowne5091753m.lengthm] = 0
      munknowne5091753m.length--
      if munknowne5091753m.length > munknowne5091753m.length - 1:
          [94midx = munknowne5091753m.length + sha3(4) - 1
          mwhile sha3(4) + munknowne5091753m.length > [94midxm:
              mstor[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      stop


# hash = 0x97d6958d
# getter = ['struct', ['loc', 2]]
# const = None
# payable = False
def unknown97d6958d(uint256 m_param1): # not payable
  require uint8(munknown97d6958dm[m_param1m]m.field_296) <= 4
  return uint32(munknown97d6958dm[m_param1m]m.field_0), 
         uint32(munknown97d6958dm[m_param1m]m.field_0),
         uint32(munknown97d6958dm[m_param1m]m.field_0),
         uint32(munknown97d6958dm[m_param1m]m.field_0),
         ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 128, ('field', 128, ('stor', ('map', ('param', '_param1'), ('name', 'unknown97d6958d', 2)))))))),
         ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 88, ('field', 168, ('stor', ('map', ('param', '_param1'), ('name', 'unknown97d6958d', 2)))))))),
         ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 48, ('field', 208, ('stor', ('map', ('param', '_param1'), ('name', 'unknown97d6958d', 2)))))))),
         ('signextend', 4, ('signextend', 4, ('signextend', 4, ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'unknown97d6958d', 2))))))),
         uint8(munknown97d6958dm[m_param1m]m.field_296)


# hash = 0xb60d4288
# getter = None
# const = None
# payable = True
def fund() payable: 
  mstor10 += call.value


# hash = 0xb8310f49
# getter = None
# const = None
# payable = False
def unknownb8310f49(uint32 m_param1): # not payable
  mem[64] = 384
  [94ms = 96
  [94midx = 0
  [94ms = 0
  mwhile [94midx < munknowne5091753m.lengthm:
      mem[0] = munknowne5091753m[[94midxm]
      mem[32] = 2
      [94m_17 = mem[64]
      mem[64] = mem[64] + 288
      mem[[94m_17] = uint32(munknown97d6958dm[mstor4m[[94midxm]m]m.field_0)
      mem[[94m_17 + 32] = uint32(munknown97d6958dm[mstor4m[[94midxm]m]m.field_32)
      mem[[94m_17 + 64] = uint32(munknown97d6958dm[mstor4m[[94midxm]m]m.field_64)
      mem[[94m_17 + 96] = uint32(munknown97d6958dm[mstor4m[[94midxm]m]m.field_96)
      mem[[94m_17 + 128] = ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 128, ('field', 128, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor4', 4))), ('name', 'unknown97d6958d', 2))))))))
      mem[[94m_17 + 160] = ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 88, ('field', 168, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor4', 4))), ('name', 'unknown97d6958d', 2))))))))
      mem[[94m_17 + 192] = ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 48, ('field', 208, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor4', 4))), ('name', 'unknown97d6958d', 2))))))))
      mem[[94m_17 + 224] = ('signextend', 4, ('signextend', 4, ('signextend', 4, ('field', 256, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor4', 4))), ('name', 'unknown97d6958d', 2)))))))
      require uint8(munknown97d6958dm[mstor4m[[94midxm]m]m.field_296) <= 4
      mem[[94m_17 + 256] = uint8(munknown97d6958dm[mstor4m[[94midxm]m]m.field_296)
      if uint32(munknown97d6958dm[mstor4m[[94midxm]m]m.field_0) != m_param1:
          [94ms = [94m_17
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      mem[mem[64] + 4] = ('signextend', 4, ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 128, ('field', 128, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor4', 4))), ('name', 'unknown97d6958d', 2)))))))))
      require ext_code.size(0x4454205ecd208cc580643bcd6bf710c9009b5a34)
      [93mdelegate 0x4454205ecd208cc580643bcd6bf710c9009b5a34.abs(int256 val) with:
           gas gas_remaining wei
          args ('signextend', 4, ('signextend', 4, ('signextend', 4, ('signextend', 4, ('type', 128, ('field', 128, ('stor', ('map', ('stor', ('array', ('var', 0), ('name', 'stor4', 4))), ('name', 'unknown97d6958d', 2)))))))))
      mem[mem[64]] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94ms = [94m_17
      [94midx = [94midx + 1
      [94ms = delegate.return_data[0] + [94ms
      mcontinue 
  return [94ms


# hash = 0xca6eb973
# getter = None
# const = None
# payable = False
def unknownca6eb973(): # not payable
  if mexchangeAddress != caller:
      revert with 0, '14'
  [94ms = 0
  [94midx = 0
  mwhile [94midx < m('cd', 36).lengthm:
      mem[0] = cd[((32 * [94midx) + cd[36] + 36)]
      mem[32] = 2
      [94ms = sha3(cd[((32 * [94midx) + cd[36] + 36)], 2)
      [94midx = [94midx + 1
      mcontinue 
  mstor12 += cd[4]


# hash = 0xd2f7265a
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def exchange(): # not payable
  return mexchangeAddress


# hash = 0xdd4da280
# getter = None
# const = None
# payable = False
def unknowndd4da280(): # not payable
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(mexchangeAddress)
          call mexchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, '13'
  munknown65139292 = 0
  log 0x5c6d04d1 


# hash = 0xe5091753
# getter = ['storage', 256, 0, ['add', ['sha3', 4], ['cd', 4]]]
# const = None
# payable = False
def unknowne5091753(uint256 m_param1): # not payable
  require m_param1 < munknowne5091753m.length
  return munknowne5091753m[m_param1m]


# hash = 0xedc29637
# getter = None
# const = None
# payable = False
def unknownedc29637(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  require munknown2b742f50 <= 4
  if not munknown2b742f50:
      revert with 0, '3'
  require munknown2b742f50 <= 4
  if munknown2b742f50 == 1:
      require ext_code.size(mexchangeAddress)
      call mexchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require munknown2b742f50 <= 4
      if munknown2b742f50 == 2:
          require ext_code.size(mexchangeAddress)
          call mexchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require munknown2b742f50 <= 4
          if munknown2b742f50 == 3:
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require munknown2b742f50 <= 4
              if munknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(mexchangeAddress)
              call mexchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, '13'
  uint8(munknown97d6958dm[m_param1m]m.field_296) = 2
  uint32(munknown97d6958dm[m_param1m]m.field_96) = uint32(block.timestamp)
  uint128(munknown97d6958dm[m_param1m]m.field_128) = munknown97d6958dm[m_param1m]m.field_128 % 1099511627776
  munknown97d6958dm[m_param1m]m.field_168 % 1099511627776 = ('signextend', 4, ('sdiv', ('param', '_param2'), 1000000000000)) % 1099511627776
  require ext_code.size(mexchangeAddress)
  call mexchangeAddress.0x2d8815c8 with:
     value m_param3 wei
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mstor9 += m_param3


# hash = 0xfce2ab2d
# getter = None
# const = None
# payable = False
def unknownfce2ab2d(addr m_param1): # not payable
  require ext_code.size(mexchangeAddress)
  call mexchangeAddress.0x798cc26a with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != tx.origin:
      revert with 0, '15'
  mexchangeAddress = m_param1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


