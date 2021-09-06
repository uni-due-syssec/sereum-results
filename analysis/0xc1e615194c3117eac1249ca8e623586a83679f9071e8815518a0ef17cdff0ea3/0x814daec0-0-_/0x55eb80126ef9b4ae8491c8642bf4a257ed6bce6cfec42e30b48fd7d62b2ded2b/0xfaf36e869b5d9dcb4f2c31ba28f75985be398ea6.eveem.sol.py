# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xFAF36E869b5D9DCB4F2C31BA28f75985Be398ea6 
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
def unknown11317681(uint256 _param1): # not payable
  require _param1 < unknowne5091753.length
  return unknowne5091753[_param1]


# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address _newOwner): # not payable
  if owner != caller:
      revert with 0, '1'
  owner = _newOwner


# hash = 0x2645dd61
# getter = None
# const = None
# payable = False
def unknown2645dd61(uint256 _param1): # not payable
  mem[64] = 416
  [94ms = 96
  [94midx = 0
  [94ms = 0
  while [94midx < unknowne5091753.length:
      mem[0] = unknowne5091753[[94midx]
      mem[32] = 2
      [94m_17 = mem[64]
      mem[64] = mem[64] + 320
      mem[[94m_17] = unknown97d6958d[stor4[[94midx]].field_0
      mem[[94m_17 + 32] = unknown97d6958d[stor4[[94midx]].field_256
      mem[[94m_17 + 64] = unknown97d6958d[stor4[[94midx]].field_512
      mem[[94m_17 + 96] = unknown97d6958d[stor4[[94midx]].field_768
      mem[[94m_17 + 128] = unknown97d6958d[stor4[[94midx]].field_1024
      require uint8(unknown97d6958d[stor4[[94midx]].field_1280) <= 4
      mem[[94m_17 + 160] = uint8(unknown97d6958d[stor4[[94midx]].field_1280)
      mem[[94m_17 + 192] = unknown97d6958d[stor4[[94midx]].field_1536
      mem[[94m_17 + 224] = unknown97d6958d[stor4[[94midx]].field_1792
      mem[[94m_17 + 256] = unknown97d6958d[stor4[[94midx]].field_2048
      mem[[94m_17 + 288] = unknown97d6958d[stor4[[94midx]].field_2304
      if _param1 != unknown97d6958d[stor4[[94midx]].field_0:
          [94ms = [94m_17
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      mem[mem[64] + 4] = unknown97d6958d[stor4[[94midx]].field_256
      require ext_code.size(0x1fc04ee645b616a1641ea13fa5360cfa1e043367)
      [93mdelegate 0x1fc04ee645b616a1641ea13fa5360cfa1e043367.abs(int256 val) with:
           gas gas_remaining wei
          args unknown97d6958d[stor4[[94midx]].field_256
      mem[mem[64]] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94ms = [94m_17
      [94midx = [94midx + 1
      [94ms = delegate.return_data[0] + [94ms
      continue 
  return [94ms


# hash = 0x2b742f50
# getter = ['storage', 8, 0, 5]
# const = None
# payable = False
def unknown2b742f50(): # not payable
  require unknown2b742f50 <= 4
  return unknown2b742f50


# hash = 0x4051ddac
# getter = None
# const = None
# payable = False
def getSummary(): # not payable
  return eth.balance(owner), stor9, stor10, stor11, stor7, unknown65139292, unknown7d704810


# hash = 0x47b922db
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknown47b922db(): # not payable
  return unknown47b922db


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
def unknown4a797a55(uint256 _param1): # not payable
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(exchangeAddress)
          call exchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, '13'
  if _param1 <= eth.balance(this.address):
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x2fe6a1e6 with:
         value _param1 wei
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      unknown7d704810 -= _param1
  else:
      log 0x1d37a599: ext_call.return_data[0], _param1 - eth.balance(this.address), 14, 'los in fixLoss'
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x2fe6a1e6 with:
         value eth.balance(this.address) wei
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      unknown7d704810 -= eth.balance(this.address)


# hash = 0x4b15908c
# getter = None
# const = None
# payable = False
def unknown4b15908c(uint8 _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5): # not payable
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(exchangeAddress)
          call exchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, '13'
  require _param1 <= 4
  uint8(unknown97d6958d[_param2].field_1280) = _param1
  unknown97d6958d[_param2].field_768 = _param3
  unknown97d6958d[_param2].field_2048 = block.timestamp
  unknown97d6958d[_param2].field_1024 = _param5
  [94midx = 0
  while [94midx < unknowne5091753.length:
      mem[0] = 4
      if unknowne5091753[[94midx] != _param2:
          [94midx = [94midx + 1
          continue 
      if [94midx == unknowne5091753.length - 1:
          require [94midx < unknowne5091753.length
          unknowne5091753[[94midx] = 0
      else:
          require unknowne5091753.length - 1 < unknowne5091753.length
          require [94midx < unknowne5091753.length
          unknowne5091753[[94midx] = unknowne5091753[unknowne5091753.length]
          require unknowne5091753.length - 1 < unknowne5091753.length
          unknowne5091753[unknowne5091753.length] = 0
      unknowne5091753.length--
      if unknowne5091753.length > unknowne5091753.length - 1:
          [94midx = unknowne5091753.length + sha3(4) - 1
          while sha3(4) + unknowne5091753.length > [94midx:
              stor[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x2d8815c8 with:
         value _param4 wei
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      stor9 += _param4
      stop
  require ext_code.size(exchangeAddress)
  call exchangeAddress.0x2d8815c8 with:
     value _param4 wei
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  stor9 += _param4


# hash = 0x4d12f044
# getter = ['struct', ['loc', 2]]
# const = None
# payable = False
def unknown4d12f044(uint256 _param1): # not payable
  require uint8(unknown97d6958d[_param1].field_1280) <= 4
  return unknown97d6958d[_param1].field_1536, 
         unknown97d6958d[_param1].field_1792,
         unknown97d6958d[_param1].field_2048,
         unknown97d6958d[_param1].field_2304


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


# hash = 0x5b7ce8c9
# getter = None
# const = None
# payable = True
def unknown5b7ce8c9() payable: 
  if exchangeAddress != caller:
      revert with 0, '14'
  unknown7d704810 += call.value


# hash = 0x5ee74564
# getter = None
# const = None
# payable = False
def unknown5ee74564(): # not payable
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      return 1
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 2:
      return 2
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 3:
      return 3
  require unknown2b742f50 <= 4
  if unknown2b742f50 != 4:
      revert with 0, '4'
  return 4


# hash = 0x62e039f0
# getter = None
# const = None
# payable = True
def unknown62e039f0() payable: 
  if exchangeAddress != caller:
      revert with 0, '14'


# hash = 0x65139292
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def unknown65139292(): # not payable
  return unknown65139292


# hash = 0x740a2ab3
# getter = ['struct', ['loc', 2]]
# const = None
# payable = False
def unknown740a2ab3(uint256 _param1): # not payable
  require uint8(unknown97d6958d[_param1].field_1280) <= 4
  require uint8(unknown97d6958d[_param1].field_1280) <= 4
  return unknown97d6958d[_param1].field_0, 
         unknown97d6958d[_param1].field_256,
         unknown97d6958d[_param1].field_512,
         unknown97d6958d[_param1].field_768,
         uint8(unknown97d6958d[_param1].field_1280),
         unknown97d6958d[_param1].field_1024


# hash = 0x76ea9b4e
# getter = None
# const = None
# payable = False
def unknown76ea9b4e(uint256 _param1): # not payable
  if owner != caller:
      revert with 0, '1'
  require uint8(unknown97d6958d[_param1].field_1280) <= 4
  if uint8(unknown97d6958d[_param1].field_1280) != 2:
      revert with 0, '21'
  uint8(unknown97d6958d[_param1].field_1280) = 3


# hash = 0x7c5d4050
# getter = None
# const = None
# payable = False
def unknown7c5d4050(uint256 _param1): # not payable
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(exchangeAddress)
          call exchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, '13'
  if _param1 > eth.balance(this.address):
      revert with 0, '17'
  if _param1 != unknown65139292:
      revert with 0, '17'
  stor11 += _param1
  unknown65139292 = 0
  call owner with:
     value _param1 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x1639a0b3: _param1


# hash = 0x7d704810
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknown7d704810(): # not payable
  return unknown7d704810


# hash = 0x7d8aac96
# getter = None
# const = None
# payable = False
def unknown7d8aac96(uint256 _param1): # not payable
  if owner != caller:
      revert with 0, '1'
  if _param1 + unknown65139292 >= eth.balance(this.address):
      revert with 0, '16'
  unknown65139292 += _param1
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(exchangeAddress)
          call exchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
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
      stor6[stor7] = _param1
      log 0x46349e9c: stor7, _param1
  else:
      unknown65139292 = 0
      call owner with:
         value _param1 wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log 0x1639a0b3: _param1
  stor7++


# hash = 0x80d23170
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def unknown80d23170(): # not payable
  return unknowne5091753.length


# hash = 0x814daec0
# getter = None
# const = None
# payable = False
def unknown814daec0(uint256 _param1, uint256 _param2): # not payable
  if owner != caller:
      revert with 0, '1'
  if not _param2:
      revert with 0, '18'
  if not _param1:
      revert with 0, '19'
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(exchangeAddress)
          call exchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xc738ce0b with:
       gas gas_remaining wei
      args this.address, _param1, _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not ext_call.return_data[0]:
      log 0xc39f0786: ext_call.return_data[32]
      return 0
  unknown97d6958d[stor3].field_0 = _param1
  uint8(unknown97d6958d[stor3].field_1280) = 0
  unknown97d6958d[stor3].field_256 = _param2
  unknown97d6958d[stor3].field_1536 = block.timestamp
  unknowne5091753.length++
  unknowne5091753[unknowne5091753.length] = unknown47b922db
  unknown47b922db++
  return unknowne5091753.length


# hash = 0x893d20e8
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def getOwner(): # not payable
  return owner


# hash = 0x896796ef
# getter = None
# const = None
# payable = False
def unknown896796ef(uint256 _param1): # not payable
  if _param1 <= eth.balance(this.address):
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x5fecf62c with:
         value _param1 wei
           gas gas_remaining wei
  else:
      log 0x1d37a599: Array(len=17, data='los in revert gas'), _param1 - eth.balance(this.address)
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x5fecf62c with:
         value eth.balance(this.address) wei
           gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x8b2dbfab
# getter = None
# const = None
# payable = False
def unknown8b2dbfab(array _param1, array _param2, uint256 _param3): # not payable
  mem[128 len _param1.length] = _param1[all]
  mem[ceil32(_param1.length) + 128] = _param2.length
  mem[ceil32(_param1.length) + 160 len _param2.length] = _param2[all]
  if owner != caller:
      revert with 0, '1'
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(exchangeAddress)
          call exchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 160] = 0x60bb4cbf00000000000000000000000000000000000000000000000000000000
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 260 len ceil32(_param1.length)] = _param1[all], mem[_param1.length + 128 len ceil32(_param1.length) - _param1.length]
  mem[_param1.length + ceil32(_param1.length) + ceil32(_param2.length) + 260] = _param2.length
  mem[_param1.length + ceil32(_param1.length) + ceil32(_param2.length) + 292 len ceil32(_param2.length)] = _param2[all], mem[ceil32(_param1.length) + _param2.length + 160 len ceil32(_param2.length) - _param2.length]
  if not _param2.length % 32:
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x60bb4cbf with:
           gas gas_remaining wei
          args Array(len=_param1.length, data=Mask(8 * ceil32(_param1.length), -(8 * ceil32(_param1.length)) + 256, _param1[all], mem[_param1.length + 128 len ceil32(_param1.length) - _param1.length]) << (8 * ceil32(_param1.length)) - 256, mem[(2 * ceil32(_param1.length)) + ceil32(_param2.length) + 260 len _param2.length + _param1.length + -ceil32(_param1.length) + 32]), _param1.length + 96
  else:
      mem[floor32(_param2.length) + _param1.length + ceil32(_param1.length) + ceil32(_param2.length) + 292] = mem[floor32(_param2.length) + _param1.length + ceil32(_param1.length) + ceil32(_param2.length) + -(_param2.length % 32) + 324 len _param2.length % 32]
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x60bb4cbf with:
           gas gas_remaining wei
          args Array(len=_param1.length, data=Mask(8 * ceil32(_param1.length), -(8 * ceil32(_param1.length)) + 256, _param1[all], mem[_param1.length + 128 len ceil32(_param1.length) - _param1.length]) << (8 * ceil32(_param1.length)) - 256, mem[(2 * ceil32(_param1.length)) + ceil32(_param2.length) + 260 len floor32(_param2.length) + _param1.length + -ceil32(_param1.length) + 64]), _param1.length + 96
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if owner != caller:
      revert with 0, '1'
  if not _param3:
      revert with 0, '18'
  if not ext_call.return_data[0]:
      revert with 0, '19'
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(exchangeAddress)
          call exchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xc738ce0b with:
       gas gas_remaining wei
      args this.address, ext_call.return_data[0], _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not ext_call.return_data[0]:
      log 0xc39f0786: ext_call.return_data[32]
      return 0
  unknown97d6958d[stor3].field_0 = ext_call.return_data[0]
  uint8(unknown97d6958d[stor3].field_1280) = 0
  unknown97d6958d[stor3].field_256 = _param3
  unknown97d6958d[stor3].field_1536 = block.timestamp
  unknowne5091753.length++
  unknowne5091753[unknowne5091753.length] = unknown47b922db
  unknown47b922db++
  return unknowne5091753.length


# hash = 0x935c9ad2
# getter = None
# const = None
# payable = False
def CancelOrder(uint256 _id): # not payable
  if owner != caller:
      revert with 0, '1'
  require uint8(unknown97d6958d[_id].field_1280) <= 4
  if uint8(unknown97d6958d[_id].field_1280):
      revert with 0, '20'
  uint8(unknown97d6958d[_id].field_1280) = 1
  unknown97d6958d[_id].field_768 = 0
  unknown97d6958d[_id].field_2048 = block.timestamp
  unknown97d6958d[_id].field_1024 = 0
  [94midx = 0
  while [94midx < unknowne5091753.length:
      mem[0] = 4
      if unknowne5091753[[94midx] != _id:
          [94midx = [94midx + 1
          continue 
      if [94midx == unknowne5091753.length - 1:
          require [94midx < unknowne5091753.length
          unknowne5091753[[94midx] = 0
      else:
          require unknowne5091753.length - 1 < unknowne5091753.length
          require [94midx < unknowne5091753.length
          unknowne5091753[[94midx] = unknowne5091753[unknowne5091753.length]
          require unknowne5091753.length - 1 < unknowne5091753.length
          unknowne5091753[unknowne5091753.length] = 0
      unknowne5091753.length--
      if unknowne5091753.length > unknowne5091753.length - 1:
          [94midx = unknowne5091753.length + sha3(4) - 1
          while sha3(4) + unknowne5091753.length > [94midx:
              stor[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      stop


# hash = 0x97d6958d
# getter = ['struct', ['loc', 2]]
# const = None
# payable = False
def unknown97d6958d(uint256 _param1): # not payable
  require uint8(unknown97d6958d[_param1].field_1280) <= 4
  return unknown97d6958d[_param1].field_0, 
         unknown97d6958d[_param1].field_256,
         unknown97d6958d[_param1].field_512,
         unknown97d6958d[_param1].field_768,
         unknown97d6958d[_param1].field_1024,
         uint8(unknown97d6958d[_param1].field_1280),
         unknown97d6958d[_param1].field_1536,
         unknown97d6958d[_param1].field_1792,
         unknown97d6958d[_param1].field_2048,
         unknown97d6958d[_param1].field_2304


# hash = 0xb60d4288
# getter = None
# const = None
# payable = True
def fund() payable: 
  stor10 += call.value


# hash = 0xca6eb973
# getter = None
# const = None
# payable = False
def unknownca6eb973(): # not payable
  if exchangeAddress != caller:
      revert with 0, '14'
  [94ms = 0
  [94midx = 0
  while [94midx < ('cd', 36).length:
      mem[0] = cd[((32 * [94midx) + cd[36] + 36)]
      mem[32] = 2
      require [94midx < ('cd', 68).length
      unknown97d6958d[cd[((32 * [94midx) + cd[36] + 36)]].field_2304 = cd[((32 * [94midx) + cd[68] + 36)]
      [94ms = sha3(cd[((32 * [94midx) + cd[36] + 36)], 2)
      [94midx = [94midx + 1
      continue 
  stor12 += cd[4]


# hash = 0xd2f7265a
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def exchange(): # not payable
  return exchangeAddress


# hash = 0xdd4da280
# getter = None
# const = None
# payable = False
def unknowndd4da280(): # not payable
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(exchangeAddress)
          call exchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, '13'
  unknown65139292 = 0
  log 0x5c6d04d1 


# hash = 0xe5091753
# getter = ['storage', 256, 0, ['add', ['sha3', 4], ['cd', 4]]]
# const = None
# payable = False
def unknowne5091753(uint256 _param1): # not payable
  require _param1 < unknowne5091753.length
  return unknowne5091753[_param1]


# hash = 0xedc29637
# getter = None
# const = None
# payable = False
def unknownedc29637(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  require unknown2b742f50 <= 4
  if not unknown2b742f50:
      revert with 0, '3'
  require unknown2b742f50 <= 4
  if unknown2b742f50 == 1:
      require ext_code.size(exchangeAddress)
      call exchangeAddress.0x7db65b17 with:
           gas gas_remaining wei
          args 1
  else:
      require unknown2b742f50 <= 4
      if unknown2b742f50 == 2:
          require ext_code.size(exchangeAddress)
          call exchangeAddress.0x7db65b17 with:
               gas gas_remaining wei
              args 2
      else:
          require unknown2b742f50 <= 4
          if unknown2b742f50 == 3:
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 3
          else:
              require unknown2b742f50 <= 4
              if unknown2b742f50 != 4:
                  revert with 0, '4'
              require ext_code.size(exchangeAddress)
              call exchangeAddress.0x7db65b17 with:
                   gas gas_remaining wei
                  args 4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, '13'
  uint8(unknown97d6958d[_param1].field_1280) = 2
  unknown97d6958d[_param1].field_512 = _param2
  unknown97d6958d[_param1].field_1792 = block.timestamp
  unknown97d6958d[_param1].field_2304 = block.timestamp
  require ext_code.size(exchangeAddress)
  call exchangeAddress.0x2d8815c8 with:
     value _param3 wei
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  stor9 += _param3


# hash = 0xfce2ab2d
# getter = None
# const = None
# payable = False
def unknownfce2ab2d(addr _param1): # not payable
  require ext_code.size(exchangeAddress)
  call exchangeAddress.0x798cc26a with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != tx.origin:
      revert with 0, '15'
  exchangeAddress = _param1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


