# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xC46e8D1A4675f39f1d043EBDa328FADF92115496 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x54c8cc78': 'unknown54c8cc78(?)', '0xedc43db5': 'unknownedc43db5(?)'} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    holding
    # storage address 2
    stor2
    # storage address 3
    unknownd759e241
    # storage address 4
    stor4
    # storage address 5
    stor5
# hash = 0x0c5e11e2
# getter = None
# const = None
# payable = False
def unknown0c5e11e2(uint256 _param1, addr _param2, uint256 _param3, uint256 _param4, uint256 _param5): # not payable
  require ext_code.size(addr(code.data[10837 len 32]))
  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if ext_call.return_data[12 len 20] != caller:
      if stor0 != caller:
          return 0
  holding[stor5.length + 1].field_0 = stor5.length + 1
  holding[stor5.length + 1].field_256 = _param1
  addr(holding[stor5.length + 1].field_512) = _param2
  holding[stor5.length + 1].field_768 = _param3
  holding[stor5.length + 1].field_1024 = _param4
  holding[stor5.length + 1].field_1280 = _param5
  unknownd759e241[_param1][addr(_param2)] = stor5.length + 1
  stor4[_param1].field_0++
  if not stor4[_param1].field_0 <= stor4[_param1].field_0 + 1:
      [94midx = stor4[_param1].field_0 + 1
      while stor4[_param1].field_0 > [94midx:
          stor4[_param1][[94midx].field_0 = 0
          [94midx = [94midx + 1
          continue 
  stor4[_param1][stor4[_param1].field_0].field_0 = holding[stor5.length + 1].field_0
  stor2[addr(_param2)].field_0++
  stor2[addr(_param2)][stor2[addr(_param2)].field_0].field_0 = holding[stor5.length + 1].field_0
  stor5.length++
  stor5[stor5.length].field_0 = holding[stor5.length + 1].field_0
  log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
  return holding[stor5.length + 1].field_0


# hash = 0x0fb0a3b2
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def unknown0fb0a3b2(uint256 _param1, addr _param2): # not payable
  return holding[stor3[_param1][addr(_param2)]].field_0, 
         holding[stor3[_param1][addr(_param2)]].field_256,
         addr(holding[stor3[_param1][addr(_param2)]].field_512),
         holding[stor3[_param1][addr(_param2)]].field_768,
         holding[stor3[_param1][addr(_param2)]].field_1024,
         holding[stor3[_param1][addr(_param2)]].field_1280


# hash = 0x1aa3a008
# getter = None
# const = None
# payable = False
def register(): # not payable
  if stor0 == caller:
      require ext_code.size(code.data[10837 len 32])
      call code.data[10837 len 32].register(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 'custodian'
      require ext_call.success


# hash = 0x1cb78281
# getter = None
# const = None
# payable = False
def unknown1cb78281(uint256 _param1, uint256 _param2): # not payable
  mem[96] = 0
  mem[128] = 0
  mem[160] = 0
  mem[192] = 0
  mem[64] = 416
  mem[224] = 0
  mem[256] = 0
  mem[288] = 0
  mem[320] = 0
  mem[352] = 0
  mem[384] = 0
  if _param2:
      [94ms = 224
      [94midx = _param1
      while [94midx < _param2:
          require [94midx < stor5.length
          mem[0] = stor5[[94midx].field_0
          mem[32] = 1
          [94m_59 = mem[64]
          mem[64] = mem[64] + 192
          mem[[94m_59] = holding[stor5[[94midx].field_0].field_0
          mem[[94m_59 + 32] = holding[stor5[[94midx].field_0].field_256
          mem[[94m_59 + 64] = addr(holding[stor5[[94midx].field_0].field_512)
          mem[[94m_59 + 96] = holding[stor5[[94midx].field_0].field_768
          mem[[94m_59 + 128] = holding[stor5[[94midx].field_0].field_1024
          mem[[94m_59 + 160] = holding[stor5[[94midx].field_0].field_1280
          require [94midx < mem[96]
          mem[(32 * [94midx) + 128] = holding[stor5[[94midx].field_0].field_0
          require [94midx < mem[128]
          mem[(32 * [94midx) + 160] = addr(holding[stor5[[94midx].field_0].field_512)
          require [94midx < mem[160]
          mem[(32 * [94midx) + 192] = holding[stor5[[94midx].field_0].field_256
          require [94midx < mem[192]
          mem[(32 * [94midx) + 224] = holding[stor5[[94midx].field_0].field_768
          [94ms = [94m_59
          [94midx = [94midx + 1
          continue 
      [94m_48 = mem[64]
      mem[mem[64]] = 128
      mem[mem[64] + 128] = mem[96]
      [94m_50 = mem[96]
      mem[mem[64] + 160 len 32 * mem[96]] = mem[128 len 32 * mem[96]]
      mem[mem[64] + 32] = (32 * mem[96]) + 160
      mem[(32 * mem[96]) + mem[64] + 160] = mem[128]
      [94m_52 = mem[128]
      mem[(32 * mem[96]) + mem[64] + 192 len 32 * mem[128]] = mem[160 len 32 * mem[128]]
      mem[mem[64] + 64] = (32 * mem[128]) + (32 * mem[96]) + 192
      mem[(32 * [94m_52) + (32 * [94m_50) + [94m_48 + 192] = mem[160]
      [94m_54 = mem[160]
      mem[(32 * [94m_52) + (32 * [94m_50) + [94m_48 + 224 len 32 * mem[160]] = mem[192 len 32 * mem[160]]
      mem[[94m_48 + 96] = (32 * mem[160]) + (32 * [94m_52) + (32 * [94m_50) + 224
      mem[(32 * [94m_54) + (32 * [94m_52) + (32 * [94m_50) + [94m_48 + 224] = mem[192]
      mem[(32 * [94m_54) + (32 * [94m_52) + (32 * [94m_50) + [94m_48 + 256 len 32 * mem[192]] = mem[224 len 32 * mem[192]]
      return memory
        from mem[64]
         [93mlen (32 * mem[192]) + (32 * [94m_54) + (32 * [94m_52) + (32 * [94m_50) + [94m_48 + -mem[64] + 256
  [94ms = 224
  [94midx = _param1
  while [94midx < stor5.length:
      mem[0] = stor5[[94midx].field_0
      mem[32] = 1
      [94m_72 = mem[64]
      mem[64] = mem[64] + 192
      mem[[94m_72] = holding[stor5[[94midx].field_0].field_0
      mem[[94m_72 + 32] = holding[stor5[[94midx].field_0].field_256
      mem[[94m_72 + 64] = addr(holding[stor5[[94midx].field_0].field_512)
      mem[[94m_72 + 96] = holding[stor5[[94midx].field_0].field_768
      mem[[94m_72 + 128] = holding[stor5[[94midx].field_0].field_1024
      mem[[94m_72 + 160] = holding[stor5[[94midx].field_0].field_1280
      require [94midx < mem[96]
      mem[(32 * [94midx) + 128] = holding[stor5[[94midx].field_0].field_0
      require [94midx < mem[128]
      mem[(32 * [94midx) + 160] = addr(holding[stor5[[94midx].field_0].field_512)
      require [94midx < mem[160]
      mem[(32 * [94midx) + 192] = holding[stor5[[94midx].field_0].field_256
      require [94midx < mem[192]
      mem[(32 * [94midx) + 224] = holding[stor5[[94midx].field_0].field_768
      [94ms = [94m_72
      [94midx = [94midx + 1
      continue 
  [94m_61 = mem[64]
  mem[mem[64]] = 128
  mem[mem[64] + 128] = mem[96]
  [94m_63 = mem[96]
  mem[mem[64] + 160 len 32 * mem[96]] = mem[128 len 32 * mem[96]]
  mem[mem[64] + 32] = (32 * mem[96]) + 160
  mem[(32 * mem[96]) + mem[64] + 160] = mem[128]
  [94m_65 = mem[128]
  mem[(32 * mem[96]) + mem[64] + 192 len 32 * mem[128]] = mem[160 len 32 * mem[128]]
  mem[mem[64] + 64] = (32 * mem[128]) + (32 * mem[96]) + 192
  mem[(32 * [94m_65) + (32 * [94m_63) + [94m_61 + 192] = mem[160]
  [94m_67 = mem[160]
  mem[(32 * [94m_65) + (32 * [94m_63) + [94m_61 + 224 len 32 * mem[160]] = mem[192 len 32 * mem[160]]
  mem[[94m_61 + 96] = (32 * mem[160]) + (32 * [94m_65) + (32 * [94m_63) + 224
  mem[(32 * [94m_67) + (32 * [94m_65) + (32 * [94m_63) + [94m_61 + 224] = mem[192]
  mem[(32 * [94m_67) + (32 * [94m_65) + (32 * [94m_63) + [94m_61 + 256 len 32 * mem[192]] = mem[224 len 32 * mem[192]]
  return memory
    from mem[64]
     [93mlen (32 * mem[192]) + (32 * [94m_67) + (32 * [94m_65) + (32 * [94m_63) + [94m_61 + -mem[64] + 256


# hash = 0x2d0b104c
# getter = None
# const = None
# payable = False
def unknown2d0b104c(uint256 _param1, addr _param2, addr _param3, uint256 _param4): # not payable
  require ext_code.size(addr(code.data[10837 len 32]))
  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if stor0 != caller:
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x391465cb with:
           gas gas_remaining - 50 wei
          args _param1, caller
      require ext_call.success
      if not ext_call.return_data[0]:
          return 0
  if addr(holding[stor3[_param1][addr(_param3)]].field_512):
      holding[stor3[_param1][addr(_param3)]].field_768 += _param4
      if holding[stor3[_param1][addr(_param2)]].field_1024 > 0:
          if holding[stor3[_param1][addr(_param3)]].field_1024 > 0:
              return 0
          holding[stor3[_param1][addr(_param3)]].field_1024 = holding[stor3[_param1][addr(_param2)]].field_1024
          holding[stor3[_param1][addr(_param3)]].field_1280 = holding[stor3[_param1][addr(_param2)]].field_1280
          holding[stor3[_param1][addr(_param3)]].field_1024 = 0
          if 1 == holding[stor3[_param1][addr(_param2)]].field_1280:
              require ext_code.size(addr(code.data[10837 len 32]))
              call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                   gas gas_remaining - 50 wei
                  args 'cashsettled'
              require ext_call.success
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x43fb2310 with:
                   gas gas_remaining - 50 wei
                  args holding[stor3[_param1][addr(_param3)]].field_1024, unknownd759e241[_param1][addr(_param3)]
              require ext_call.success
          else:
              if 2 == holding[stor3[_param1][addr(_param3)]].field_1280:
                  require ext_code.size(addr(code.data[10837 len 32]))
                  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                       gas gas_remaining - 50 wei
                      args 'cashsettled'
                  require ext_call.success
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x173396bb with:
                       gas gas_remaining - 50 wei
                      args holding[stor3[_param1][addr(_param3)]].field_1024, unknownd759e241[_param1][addr(_param3)]
                  require ext_call.success
      holding[stor3[_param1][addr(_param2)]].field_768 -= _param4
      log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, 0, holding[stor3[_param1][addr(_param2)]].field_768 - _param4, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 6, holding[stor3[_param1][addr(_param2)]].field_0
      log 0x563ecb3e: holding[stor3[_param1][addr(_param3)]].field_256, 0, holding[stor3[_param1][addr(_param3)]].field_768, holding[stor3[_param1][addr(_param3)]].field_1024, holding[stor3[_param1][addr(_param3)]].field_1280, 6, unknownd759e241[_param1][addr(_param3)]
  else:
      holding[stor5.length + 1].field_0 = stor5.length + 1
      holding[stor5.length + 1].field_256 = _param1
      addr(holding[stor5.length + 1].field_512) = _param3
      holding[stor5.length + 1].field_768 = _param4
      holding[stor5.length + 1].field_1280 = 1
      unknownd759e241[_param1][addr(_param3)] = stor5.length + 1
      stor4[_param1].field_0++
      stor4[_param1][stor4[_param1].field_0].field_0 = stor5.length + 1
      stor2[addr(_param3)].field_0++
      stor2[addr(_param3)][stor2[addr(_param3)].field_0].field_0 = stor5.length + 1
      stor5.length++
      stor5[stor5.length].field_0 = stor5.length + 1
      if holding[stor3[_param1][addr(_param2)]].field_1024 > 0:
          if holding[stor5.length + 1].field_1024 > 0:
              return 0
          holding[stor5.length + 1].field_1024 = holding[stor3[_param1][addr(_param2)]].field_1024
          holding[stor5.length + 1].field_1280 = holding[stor3[_param1][addr(_param2)]].field_1280
          holding[stor5.length + 1].field_1024 = 0
          if 1 == holding[stor3[_param1][addr(_param2)]].field_1280:
              require ext_code.size(addr(code.data[10837 len 32]))
              call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                   gas gas_remaining - 50 wei
                  args 'cashsettled'
              require ext_call.success
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x43fb2310 with:
                   gas gas_remaining - 50 wei
                  args holding[stor5.length + 1].field_1024, stor5.length + 1
              require ext_call.success
          else:
              if 2 == holding[stor5.length + 1].field_1280:
                  require ext_code.size(addr(code.data[10837 len 32]))
                  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                       gas gas_remaining - 50 wei
                      args 'cashsettled'
                  require ext_call.success
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x173396bb with:
                       gas gas_remaining - 50 wei
                      args holding[stor5.length + 1].field_1024, stor5.length + 1
                  require ext_call.success
      holding[stor3[_param1][addr(_param2)]].field_768 -= _param4
      log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, 0, holding[stor3[_param1][addr(_param2)]].field_768 - _param4, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 6, holding[stor3[_param1][addr(_param2)]].field_0
      log 0x563ecb3e: holding[stor5.length + 1].field_256, 0, holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 6, stor5.length + 1
  return 1


# hash = 0x308f16da
# getter = None
# const = None
# payable = False
def unknown308f16da(uint256 _param1, addr _param2, addr _param3, uint256 _param4, uint256 _param5, bool _param6): # not payable
  require ext_code.size(addr(code.data[10837 len 32]))
  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args ('offerbook' << 184)
  require ext_call.success
  require ext_code.size(code.data[10837 len 32])
  call code.data[10837 len 32].addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if addr(ext_call.return_data[0]) != caller:
      if stor0 != caller:
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x391465cb with:
               gas gas_remaining - 50 wei
              args _param1, caller
          require ext_call.success
          if not ext_call.return_data[0]:
              return 0
  if _param5 <= 0:
      return 1
  if _param6:
      return 1
  require ext_code.size(addr(code.data[10837 len 32]))
  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 'stabletoken'
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).adminTransfer(address from, address to, uint256 value) with:
       gas gas_remaining - 50 wei
      args addr(_param2), addr(_param3), _param4 * _param5
  require ext_call.success
  if not ext_call.return_data[0]:
      log 0x5a29bc1d: _param1, 5, 3, _param2
  return bool(ext_call.return_data[0])


# hash = 0x30ac2e7f
# getter = None
# const = None
# payable = False
def unknown30ac2e7f(addr _param1): # not payable
  if stor2[addr(_param1)].field_0:
      mem[160] = stor2[addr(_param1)].field_0
      [94midx = 160
      [94ms = 0
      while (32 * stor2[addr(_param1)].field_0) + 128 > [94midx:
          mem[[94midx + 32] = stor2[addr(_param1)][[94ms].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
  return Array(len=stor2[addr(_param1)].field_0, data=mem[160 len 32 * stor2[addr(_param1)].field_0])


# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  if stor0 == caller:
      [93mselfdestruct([91mstor0[93m)


# hash = 0x56457b00
# getter = None
# const = None
# payable = False
def unknown56457b00(): # not payable
  if stor5.length:
      mem[160] = uint256(stor5.field_0)
      [94midx = 160
      [94ms = 0
      while (32 * stor5.length) + 128 > [94midx:
          mem[[94midx + 32] = stor5[[94ms].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
  return Array(len=stor5.length, data=mem[160 len 32 * stor5.length])


# hash = 0x6ef22110
# getter = None
# const = None
# payable = False
def unknown6ef22110(uint256 _param1): # not payable
  if stor4[_param1].field_0:
      mem[160] = stor4[_param1].field_0
      if (32 * stor4[_param1].field_0) + 32 > 64:
          mem[192] = stor4[_param1].field_256
          [94midx = 192
          [94ms = 1
          while (32 * stor4[_param1].field_0) + 128 > [94midx:
              mem[[94midx + 32] = stor4[_param1][[94ms].field_256
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              continue 
  return Array(len=stor4[_param1].field_0, data=mem[160 len 32 * stor4[_param1].field_0])


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address _newAdmin): # not payable
  if stor0 == caller:
      stor0 = _newAdmin


# hash = 0x7954e911
# getter = None
# const = None
# payable = False
def unknown7954e911(uint256 _param1, addr _param2, uint256 _param3): # not payable
  require ext_code.size(addr(code.data[10837 len 32]))
  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  require ext_code.size(code.data[10837 len 32])
  call code.data[10837 len 32].addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args ('offerbook' << 184)
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).exists(uint256 tokenId) with:
       gas gas_remaining - 50 wei
      args _param1
  require ext_call.success
  if ext_call.return_data[0]:
      require ext_code.size(addr(ext_call.return_data[0]))
      if caller == addr(ext_call.return_data[0]):
          call addr(ext_call.return_data[0]).0x92089c46 with:
               gas gas_remaining - 50 wei
              args _param1
          require ext_call.success
          if addr(ext_call.return_data[0]) != caller:
              if addr(holding[stor3[_param1][addr(_param2)]].field_512):
                  holding[stor3[_param1][addr(_param2)]].field_768 += _param3
                  log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
              else:
                  holding[stor5.length + 1].field_0 = stor5.length + 1
                  holding[stor5.length + 1].field_256 = _param1
                  addr(holding[stor5.length + 1].field_512) = _param2
                  holding[stor5.length + 1].field_768 = _param3
                  holding[stor5.length + 1].field_1024 = 0
                  holding[stor5.length + 1].field_1280 = 1
                  unknownd759e241[_param1][addr(_param2)] = stor5.length + 1
                  stor4[_param1].field_0++
                  if not stor4[_param1].field_0 <= stor4[_param1].field_0 + 1:
                      [94midx = stor4[_param1].field_0 + 1
                      while stor4[_param1].field_0 > [94midx:
                          stor4[_param1][[94midx].field_0 = 0
                          [94midx = [94midx + 1
                          continue 
                  stor4[_param1][stor4[_param1].field_0].field_0 = holding[stor5.length + 1].field_0
                  stor2[addr(_param2)].field_0++
                  stor2[addr(_param2)][stor2[addr(_param2)].field_0].field_0 = holding[stor5.length + 1].field_0
                  stor5.length++
                  stor5[stor5.length].field_0 = holding[stor5.length + 1].field_0
                  log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x940589d6 with:
                   gas gas_remaining - 50 wei
                  args _param1, _param3
              require ext_call.success
          else:
              if ext_call.return_data[12 len 20] == _param2:
                  if addr(holding[stor3[_param1][addr(_param2)]].field_512):
                      holding[stor3[_param1][addr(_param2)]].field_768 += _param3
                      log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
                  else:
                      holding[stor5.length + 1].field_0 = stor5.length + 1
                      holding[stor5.length + 1].field_256 = _param1
                      addr(holding[stor5.length + 1].field_512) = _param2
                      holding[stor5.length + 1].field_768 = _param3
                      holding[stor5.length + 1].field_1024 = 0
                      holding[stor5.length + 1].field_1280 = 1
                      unknownd759e241[_param1][addr(_param2)] = stor5.length + 1
                      stor4[_param1].field_0++
                      if not stor4[_param1].field_0 <= stor4[_param1].field_0 + 1:
                          [94midx = stor4[_param1].field_0 + 1
                          while stor4[_param1].field_0 > [94midx:
                              stor4[_param1][[94midx].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                      stor4[_param1][stor4[_param1].field_0].field_0 = holding[stor5.length + 1].field_0
                      stor2[addr(_param2)].field_0++
                      stor2[addr(_param2)][stor2[addr(_param2)].field_0].field_0 = holding[stor5.length + 1].field_0
                      stor5.length++
                      stor5[stor5.length].field_0 = holding[stor5.length + 1].field_0
                      log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x940589d6 with:
                       gas gas_remaining - 50 wei
                      args _param1, _param3
                  require ext_call.success
      else:
          if stor0 == caller:
              call addr(ext_call.return_data[0]).0x92089c46 with:
                   gas gas_remaining - 50 wei
                  args _param1
              require ext_call.success
              if addr(ext_call.return_data[0]) != caller:
                  if addr(holding[stor3[_param1][addr(_param2)]].field_512):
                      holding[stor3[_param1][addr(_param2)]].field_768 += _param3
                      log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
                  else:
                      holding[stor5.length + 1].field_0 = stor5.length + 1
                      holding[stor5.length + 1].field_256 = _param1
                      addr(holding[stor5.length + 1].field_512) = _param2
                      holding[stor5.length + 1].field_768 = _param3
                      holding[stor5.length + 1].field_1024 = 0
                      holding[stor5.length + 1].field_1280 = 1
                      unknownd759e241[_param1][addr(_param2)] = stor5.length + 1
                      stor4[_param1].field_0++
                      if not stor4[_param1].field_0 <= stor4[_param1].field_0 + 1:
                          [94midx = stor4[_param1].field_0 + 1
                          while stor4[_param1].field_0 > [94midx:
                              stor4[_param1][[94midx].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                      stor4[_param1][stor4[_param1].field_0].field_0 = holding[stor5.length + 1].field_0
                      stor2[addr(_param2)].field_0++
                      stor2[addr(_param2)][stor2[addr(_param2)].field_0].field_0 = holding[stor5.length + 1].field_0
                      stor5.length++
                      stor5[stor5.length].field_0 = holding[stor5.length + 1].field_0
                      log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x940589d6 with:
                       gas gas_remaining - 50 wei
                      args _param1, _param3
                  require ext_call.success
              else:
                  if ext_call.return_data[12 len 20] == _param2:
                      if addr(holding[stor3[_param1][addr(_param2)]].field_512):
                          holding[stor3[_param1][addr(_param2)]].field_768 += _param3
                          log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
                      else:
                          holding[stor5.length + 1].field_0 = stor5.length + 1
                          holding[stor5.length + 1].field_256 = _param1
                          addr(holding[stor5.length + 1].field_512) = _param2
                          holding[stor5.length + 1].field_768 = _param3
                          holding[stor5.length + 1].field_1024 = 0
                          holding[stor5.length + 1].field_1280 = 1
                          unknownd759e241[_param1][addr(_param2)] = stor5.length + 1
                          stor4[_param1].field_0++
                          if not stor4[_param1].field_0 <= stor4[_param1].field_0 + 1:
                              [94midx = stor4[_param1].field_0 + 1
                              while stor4[_param1].field_0 > [94midx:
                                  stor4[_param1][[94midx].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                          stor4[_param1][stor4[_param1].field_0].field_0 = holding[stor5.length + 1].field_0
                          stor2[addr(_param2)].field_0++
                          stor2[addr(_param2)][stor2[addr(_param2)].field_0].field_0 = holding[stor5.length + 1].field_0
                          stor5.length++
                          stor5[stor5.length].field_0 = holding[stor5.length + 1].field_0
                          log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).0x940589d6 with:
                           gas gas_remaining - 50 wei
                          args _param1, _param3
                      require ext_call.success
          else:
              call addr(ext_call.return_data[0]).0x391465cb with:
                   gas gas_remaining - 50 wei
                  args _param1, caller
              require ext_call.success
              if ext_call.return_data[0]:
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x92089c46 with:
                       gas gas_remaining - 50 wei
                      args _param1
                  require ext_call.success
                  if addr(ext_call.return_data[0]) != caller:
                      if addr(holding[stor3[_param1][addr(_param2)]].field_512):
                          holding[stor3[_param1][addr(_param2)]].field_768 += _param3
                          log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
                      else:
                          holding[stor5.length + 1].field_0 = stor5.length + 1
                          holding[stor5.length + 1].field_256 = _param1
                          addr(holding[stor5.length + 1].field_512) = _param2
                          holding[stor5.length + 1].field_768 = _param3
                          holding[stor5.length + 1].field_1024 = 0
                          holding[stor5.length + 1].field_1280 = 1
                          unknownd759e241[_param1][addr(_param2)] = stor5.length + 1
                          stor4[_param1].field_0++
                          if not stor4[_param1].field_0 <= stor4[_param1].field_0 + 1:
                              [94midx = stor4[_param1].field_0 + 1
                              while stor4[_param1].field_0 > [94midx:
                                  stor4[_param1][[94midx].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                          stor4[_param1][stor4[_param1].field_0].field_0 = holding[stor5.length + 1].field_0
                          stor2[addr(_param2)].field_0++
                          stor2[addr(_param2)][stor2[addr(_param2)].field_0].field_0 = holding[stor5.length + 1].field_0
                          stor5.length++
                          stor5[stor5.length].field_0 = holding[stor5.length + 1].field_0
                          log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).0x940589d6 with:
                           gas gas_remaining - 50 wei
                          args _param1, _param3
                      require ext_call.success
                  else:
                      if ext_call.return_data[12 len 20] == _param2:
                          if addr(holding[stor3[_param1][addr(_param2)]].field_512):
                              holding[stor3[_param1][addr(_param2)]].field_768 += _param3
                              log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
                          else:
                              holding[stor5.length + 1].field_0 = stor5.length + 1
                              holding[stor5.length + 1].field_256 = _param1
                              addr(holding[stor5.length + 1].field_512) = _param2
                              holding[stor5.length + 1].field_768 = _param3
                              holding[stor5.length + 1].field_1024 = 0
                              holding[stor5.length + 1].field_1280 = 1
                              unknownd759e241[_param1][addr(_param2)] = stor5.length + 1
                              stor4[_param1].field_0++
                              if not stor4[_param1].field_0 <= stor4[_param1].field_0 + 1:
                                  [94midx = stor4[_param1].field_0 + 1
                                  while stor4[_param1].field_0 > [94midx:
                                      stor4[_param1][[94midx].field_0 = 0
                                      [94midx = [94midx + 1
                                      continue 
                              stor4[_param1][stor4[_param1].field_0].field_0 = holding[stor5.length + 1].field_0
                              stor2[addr(_param2)].field_0++
                              stor2[addr(_param2)][stor2[addr(_param2)].field_0].field_0 = holding[stor5.length + 1].field_0
                              stor5.length++
                              stor5[stor5.length].field_0 = holding[stor5.length + 1].field_0
                              log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).0x940589d6 with:
                               gas gas_remaining - 50 wei
                              args _param1, _param3
                          require ext_call.success


# hash = 0x7acd04e9
# getter = None
# const = None
# payable = False
def unknown7acd04e9(array _param1, addr _param2, array _param3, array _param4): # not payable
  mem[96] = _param1.length
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = _param3.length
  mem[(32 * _param1.length) + 160 len 32 * _param3.length] = call.data[_param3 + 36 len 32 * _param3.length]
  mem[64] = (32 * _param4.length) + (32 * _param3.length) + (32 * _param1.length) + 192
  mem[(32 * _param3.length) + (32 * _param1.length) + 160] = _param4.length
  mem[(32 * _param3.length) + (32 * _param1.length) + 192 len 32 * _param4.length] = call.data[_param4 + 36 len 32 * _param4.length]
  if _param1.length == _param3.length:
      if _param1.length == _param4.length:
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param1.length) + 224] = 0
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param1.length) + 196] = 0x626f6e6400000000000000000000000000000000000000000000000000000000
          require ext_code.size(addr(code.data[10837 len 32]))
          call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param1.length) + 192] = ext_call.return_data[0]
          require ext_call.success
          [94midx = 0
          while [94midx < _param1.length:
              require [94midx < mem[96]
              if stor0 == caller:
                  require [94midx < mem[(32 * _param1.length) + 128]
                  require [94midx < mem[(32 * _param3.length) + (32 * _param1.length) + 160]
                  [94m_3370 = mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                  mem[0] = mem[(32 * [94midx) + 128]
                  [94m_3373 = sha3(unknownd759e241[mem[(32 * [94midx) + 128]][addr(_param2)], 1)
                  [94m_3374 = sha3(addr(mem[(32 * [94midx) + (32 * _param1.length) + 160]), sha3(mem[(32 * [94midx) + 128], 3))
                  if addr(holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_512):
                      mem[32] = 1
                      holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_768 += mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                      if holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1024 <= 0:
                          holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                          mem[mem[64]] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_256
                          mem[mem[64] + 32] = addr(holding[stor3[mem[0]][addr(_param2)]].field_512)
                          mem[mem[64] + 64] = holding[stor3[mem[0]][addr(_param2)]].field_768 - [94m_3370
                          mem[mem[64] + 96] = holding[stor3[mem[0]][addr(_param2)]].field_1024
                          log 0x563ecb3e: mem[mem[64] len 64], holding[stor3[mem[0]][addr(_param2)]].field_768 - _3370, holding[stor3[mem[0]][addr(_param2)]].field_1024, holding[stor3[mem[0]][addr(_param2)]].field_1280, 6, holding[stor3[mem[0]][addr(_param2)]].field_0
                          mem[32] = 1
                          mem[mem[64]] = holding[stor[[94m_3374]].field_256
                          mem[mem[64] + 32] = addr(holding[stor[[94m_3374]].field_512)
                          mem[mem[64] + 64] = holding[stor[[94m_3374]].field_768
                          mem[mem[64] + 96] = holding[stor[[94m_3374]].field_1024
                          mem[mem[64] + 128] = holding[stor[[94m_3374]].field_1280
                          mem[0] = stor[[94m_3374]
                          log 0x563ecb3e: holding[stor[_3374]].field_256, addr(holding[stor[_3374]].field_512), holding[stor[_3374]].field_768, holding[stor[_3374]].field_1024, holding[stor[_3374]].field_1280, 6, stor[_3374]
                      else:
                          mem[0] = unknownd759e241[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]
                          mem[32] = 1
                          if holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1024 <= 0:
                              holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1024 = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1024
                              holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1280 = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1280
                              holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1024 = 0
                              if 1 == holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1280:
                                  require ext_code.size(addr(code.data[10837 len 32]))
                                  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'cashsettled'
                                  require ext_call.success
                                  mem[0] = unknownd759e241[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]
                                  mem[32] = 1
                                  mem[mem[64] + 4] = holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1024
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).0x43fb2310 with:
                                       gas gas_remaining - 50 wei
                                      args mem[mem[64] + 4], stor[[94m_3374]
                                  require ext_call.success
                                  unknownd759e241[[94m_3373] -= [94m_3370
                                  mem[mem[64] + 64] = unknownd759e241[[94m_3373] - [94m_3370
                                  log 0x563ecb3e: holding[_3373].field_0, addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                              else:
                                  mem[32] = 1
                                  if holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1280 != 2:
                                      holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                      mem[mem[64]] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_256
                                      mem[mem[64] + 64] = unknownd759e241[[94m_3373] - [94m_3370
                                      mem[mem[64] + 96] = stor4[[94m_3373].field_0
                                      log 0x563ecb3e: mem[mem[64]], addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                                  else:
                                      require ext_code.size(addr(code.data[10837 len 32]))
                                      call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'cashsettled'
                                      require ext_call.success
                                      mem[0] = unknownd759e241[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]
                                      mem[32] = 1
                                      mem[mem[64] + 4] = holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1024
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).0x173396bb with:
                                           gas gas_remaining - 50 wei
                                          args mem[mem[64] + 4], stor[[94m_3374]
                                      require ext_call.success
                                      unknownd759e241[[94m_3373] -= [94m_3370
                                      mem[mem[64] + 64] = unknownd759e241[[94m_3373] - [94m_3370
                                      log 0x563ecb3e: holding[_3373].field_0, addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                              mem[32] = 1
                              mem[mem[64]] = holding[stor[[94m_3374]].field_256
                              mem[mem[64] + 32] = addr(holding[stor[[94m_3374]].field_512)
                              mem[mem[64] + 64] = holding[stor[[94m_3374]].field_768
                              mem[mem[64] + 96] = holding[stor[[94m_3374]].field_1024
                              mem[mem[64] + 128] = holding[stor[[94m_3374]].field_1280
                              mem[0] = stor[[94m_3374]
                              log 0x563ecb3e: holding[stor[_3374]].field_256, addr(holding[stor[_3374]].field_512), holding[stor[_3374]].field_768, holding[stor[_3374]].field_1024, holding[stor[_3374]].field_1280, 6, stor[_3374]
                  else:
                      holding[stor5.length + 1].field_0 = stor5.length + 1
                      holding[stor5.length + 1].field_256 = mem[(32 * [94midx) + 128]
                      addr(holding[stor5.length + 1].field_512) = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                      holding[stor5.length + 1].field_768 = mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                      holding[stor5.length + 1].field_1280 = 1
                      unknownd759e241[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])] = stor5.length + 1
                      stor4[mem[(32 * [94midx) + 128]].field_0++
                      stor4[mem[(32 * [94midx) + 128]][stor4[mem[(32 * [94midx) + 128]].field_0].field_0 = stor5.length + 1
                      mem[32] = 2
                      stor2[addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])].field_0++
                      stor2[addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])][stor2[addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])].field_0].field_0 = stor5.length + 1
                      stor5.length++
                      stor5[stor5.length].field_0 = stor5.length + 1
                      if holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1024 <= 0:
                          holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                          mem[mem[64]] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_256
                          mem[mem[64] + 32] = addr(holding[stor3[mem[0]][addr(_param2)]].field_512)
                          mem[mem[64] + 64] = holding[stor3[mem[0]][addr(_param2)]].field_768 - [94m_3370
                          mem[mem[64] + 96] = holding[stor3[mem[0]][addr(_param2)]].field_1024
                          log 0x563ecb3e: mem[mem[64] len 64], holding[stor3[mem[0]][addr(_param2)]].field_768 - _3370, holding[stor3[mem[0]][addr(_param2)]].field_1024, holding[stor3[mem[0]][addr(_param2)]].field_1280, 6, holding[stor3[mem[0]][addr(_param2)]].field_0
                          mem[32] = 1
                          mem[mem[64]] = holding[stor5.length + 1].field_256
                          mem[mem[64] + 32] = addr(holding[stor5.length + 1].field_512)
                          mem[mem[64] + 64] = holding[stor5.length + 1].field_768
                          mem[mem[64] + 96] = holding[stor5.length + 1].field_1024
                          mem[mem[64] + 128] = holding[stor5.length + 1].field_1280
                          mem[0] = stor5.length + 1
                          log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 6, stor5.length + 1
                      else:
                          mem[0] = stor5.length + 1
                          mem[32] = 1
                          if holding[stor5.length + 1].field_1024 <= 0:
                              holding[stor5.length + 1].field_1024 = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1024
                              holding[stor5.length + 1].field_1280 = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1280
                              holding[stor5.length + 1].field_1024 = 0
                              if 1 == holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1280:
                                  require ext_code.size(addr(code.data[10837 len 32]))
                                  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'cashsettled'
                                  require ext_call.success
                                  mem[0] = stor5.length + 1
                                  mem[32] = 1
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).0x43fb2310 with:
                                       gas gas_remaining - 50 wei
                                      args holding[stor5.length + 1].field_1024, stor5.length + 1
                                  require ext_call.success
                                  holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                  mem[mem[64] + 64] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 - mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                  log 0x563ecb3e: holding[_3373].field_0, addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                              else:
                                  mem[32] = 1
                                  if holding[stor5.length + 1].field_1280 != 2:
                                      holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                      mem[mem[64]] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_256
                                      mem[mem[64] + 64] = unknownd759e241[[94m_3373] - [94m_3370
                                      mem[mem[64] + 96] = stor4[[94m_3373].field_0
                                      log 0x563ecb3e: mem[mem[64]], addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                                  else:
                                      require ext_code.size(addr(code.data[10837 len 32]))
                                      call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'cashsettled'
                                      require ext_call.success
                                      mem[0] = stor5.length + 1
                                      mem[32] = 1
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).0x173396bb with:
                                           gas gas_remaining - 50 wei
                                          args holding[stor5.length + 1].field_1024, stor5.length + 1
                                      require ext_call.success
                                      holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                      mem[mem[64] + 64] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 - mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                      log 0x563ecb3e: holding[_3373].field_0, addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                              mem[32] = 1
                              mem[mem[64]] = holding[stor5.length + 1].field_256
                              mem[mem[64] + 32] = addr(holding[stor5.length + 1].field_512)
                              mem[mem[64] + 64] = holding[stor5.length + 1].field_768
                              mem[mem[64] + 96] = holding[stor5.length + 1].field_1024
                              mem[mem[64] + 128] = holding[stor5.length + 1].field_1280
                              mem[0] = stor5.length + 1
                              log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 6, stor5.length + 1
              else:
                  mem[mem[64] + 4] = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 36] = caller
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x391465cb with:
                       gas gas_remaining - 50 wei
                      args mem[mem[64] + 4], caller
                  mem[mem[64]] = ext_call.return_data[0]
                  require ext_call.success
                  if ext_call.return_data[0]:
                      require [94midx < mem[96]
                      require [94midx < mem[(32 * _param1.length) + 128]
                      require [94midx < mem[(32 * _param3.length) + (32 * _param1.length) + 160]
                      [94m_3389 = mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                      mem[0] = mem[(32 * [94midx) + 128]
                      [94m_3394 = sha3(unknownd759e241[mem[(32 * [94midx) + 128]][addr(_param2)], 1)
                      [94m_3395 = sha3(addr(mem[(32 * [94midx) + (32 * _param1.length) + 160]), sha3(mem[(32 * [94midx) + 128], 3))
                      if addr(holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_512):
                          mem[32] = 1
                          holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_768 += mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                          if holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1024 <= 0:
                              holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                              mem[mem[64]] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_256
                              mem[mem[64] + 32] = addr(holding[stor3[mem[0]][addr(_param2)]].field_512)
                              mem[mem[64] + 64] = holding[stor3[mem[0]][addr(_param2)]].field_768 - [94m_3389
                              mem[mem[64] + 96] = holding[stor3[mem[0]][addr(_param2)]].field_1024
                              log 0x563ecb3e: mem[mem[64] len 64], holding[stor3[mem[0]][addr(_param2)]].field_768 - _3389, holding[stor3[mem[0]][addr(_param2)]].field_1024, holding[stor3[mem[0]][addr(_param2)]].field_1280, 6, holding[stor3[mem[0]][addr(_param2)]].field_0
                              mem[32] = 1
                              mem[mem[64]] = holding[stor[[94m_3395]].field_256
                              mem[mem[64] + 32] = addr(holding[stor[[94m_3395]].field_512)
                              mem[mem[64] + 64] = holding[stor[[94m_3395]].field_768
                              mem[mem[64] + 96] = holding[stor[[94m_3395]].field_1024
                              mem[mem[64] + 128] = holding[stor[[94m_3395]].field_1280
                              mem[0] = stor[[94m_3395]
                              log 0x563ecb3e: holding[stor[_3395]].field_256, addr(holding[stor[_3395]].field_512), holding[stor[_3395]].field_768, holding[stor[_3395]].field_1024, holding[stor[_3395]].field_1280, 6, stor[_3395]
                          else:
                              mem[0] = unknownd759e241[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]
                              mem[32] = 1
                              if holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1024 <= 0:
                                  holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1024 = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1024
                                  holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1280 = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1280
                                  holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1024 = 0
                                  if 1 == holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1280:
                                      require ext_code.size(addr(code.data[10837 len 32]))
                                      call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'cashsettled'
                                      require ext_call.success
                                      mem[0] = unknownd759e241[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]
                                      mem[32] = 1
                                      mem[mem[64] + 4] = holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1024
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).0x43fb2310 with:
                                           gas gas_remaining - 50 wei
                                          args mem[mem[64] + 4], stor[[94m_3395]
                                      require ext_call.success
                                      unknownd759e241[[94m_3394] -= [94m_3389
                                      mem[mem[64] + 64] = unknownd759e241[[94m_3394] - [94m_3389
                                      log 0x563ecb3e: holding[_3394].field_0, addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                  else:
                                      mem[32] = 1
                                      if holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1280 != 2:
                                          holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                          mem[mem[64]] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_256
                                          mem[mem[64] + 64] = unknownd759e241[[94m_3394] - [94m_3389
                                          mem[mem[64] + 96] = stor4[[94m_3394].field_0
                                          log 0x563ecb3e: mem[mem[64]], addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                      else:
                                          require ext_code.size(addr(code.data[10837 len 32]))
                                          call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'cashsettled'
                                          require ext_call.success
                                          mem[0] = unknownd759e241[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]
                                          mem[32] = 1
                                          mem[mem[64] + 4] = holding[stor3[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])]].field_1024
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0x173396bb with:
                                               gas gas_remaining - 50 wei
                                              args mem[mem[64] + 4], stor[[94m_3395]
                                          require ext_call.success
                                          unknownd759e241[[94m_3394] -= [94m_3389
                                          mem[mem[64] + 64] = unknownd759e241[[94m_3394] - [94m_3389
                                          log 0x563ecb3e: holding[_3394].field_0, addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                  mem[32] = 1
                                  mem[mem[64]] = holding[stor[[94m_3395]].field_256
                                  mem[mem[64] + 32] = addr(holding[stor[[94m_3395]].field_512)
                                  mem[mem[64] + 64] = holding[stor[[94m_3395]].field_768
                                  mem[mem[64] + 96] = holding[stor[[94m_3395]].field_1024
                                  mem[mem[64] + 128] = holding[stor[[94m_3395]].field_1280
                                  mem[0] = stor[[94m_3395]
                                  log 0x563ecb3e: holding[stor[_3395]].field_256, addr(holding[stor[_3395]].field_512), holding[stor[_3395]].field_768, holding[stor[_3395]].field_1024, holding[stor[_3395]].field_1280, 6, stor[_3395]
                      else:
                          holding[stor5.length + 1].field_0 = stor5.length + 1
                          holding[stor5.length + 1].field_256 = mem[(32 * [94midx) + 128]
                          addr(holding[stor5.length + 1].field_512) = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
                          holding[stor5.length + 1].field_768 = mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                          holding[stor5.length + 1].field_1280 = 1
                          unknownd759e241[mem[(32 * [94midx) + 128]][addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])] = stor5.length + 1
                          stor4[mem[(32 * [94midx) + 128]].field_0++
                          stor4[mem[(32 * [94midx) + 128]][stor4[mem[(32 * [94midx) + 128]].field_0].field_0 = stor5.length + 1
                          mem[32] = 2
                          stor2[addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])].field_0++
                          stor2[addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])][stor2[addr(mem[(32 * [94midx) + (32 * _param1.length) + 160])].field_0].field_0 = stor5.length + 1
                          stor5.length++
                          stor5[stor5.length].field_0 = stor5.length + 1
                          if holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1024 <= 0:
                              holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                              mem[mem[64]] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_256
                              mem[mem[64] + 32] = addr(holding[stor3[mem[0]][addr(_param2)]].field_512)
                              mem[mem[64] + 64] = holding[stor3[mem[0]][addr(_param2)]].field_768 - [94m_3389
                              mem[mem[64] + 96] = holding[stor3[mem[0]][addr(_param2)]].field_1024
                              log 0x563ecb3e: mem[mem[64] len 64], holding[stor3[mem[0]][addr(_param2)]].field_768 - _3389, holding[stor3[mem[0]][addr(_param2)]].field_1024, holding[stor3[mem[0]][addr(_param2)]].field_1280, 6, holding[stor3[mem[0]][addr(_param2)]].field_0
                              mem[32] = 1
                              mem[mem[64]] = holding[stor5.length + 1].field_256
                              mem[mem[64] + 32] = addr(holding[stor5.length + 1].field_512)
                              mem[mem[64] + 64] = holding[stor5.length + 1].field_768
                              mem[mem[64] + 96] = holding[stor5.length + 1].field_1024
                              mem[mem[64] + 128] = holding[stor5.length + 1].field_1280
                              mem[0] = stor5.length + 1
                              log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 6, stor5.length + 1
                          else:
                              mem[0] = stor5.length + 1
                              mem[32] = 1
                              if holding[stor5.length + 1].field_1024 <= 0:
                                  holding[stor5.length + 1].field_1024 = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1024
                                  holding[stor5.length + 1].field_1280 = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1280
                                  holding[stor5.length + 1].field_1024 = 0
                                  if 1 == holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_1280:
                                      require ext_code.size(addr(code.data[10837 len 32]))
                                      call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'cashsettled'
                                      require ext_call.success
                                      mem[0] = stor5.length + 1
                                      mem[32] = 1
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).0x43fb2310 with:
                                           gas gas_remaining - 50 wei
                                          args holding[stor5.length + 1].field_1024, stor5.length + 1
                                      require ext_call.success
                                      holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                      mem[mem[64] + 64] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 - mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                      log 0x563ecb3e: holding[_3394].field_0, addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                  else:
                                      mem[32] = 1
                                      if holding[stor5.length + 1].field_1280 != 2:
                                          holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                          mem[mem[64]] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_256
                                          mem[mem[64] + 64] = unknownd759e241[[94m_3394] - [94m_3389
                                          mem[mem[64] + 96] = stor4[[94m_3394].field_0
                                          log 0x563ecb3e: mem[mem[64]], addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                      else:
                                          require ext_code.size(addr(code.data[10837 len 32]))
                                          call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'cashsettled'
                                          require ext_call.success
                                          mem[0] = stor5.length + 1
                                          mem[32] = 1
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0x173396bb with:
                                               gas gas_remaining - 50 wei
                                              args holding[stor5.length + 1].field_1024, stor5.length + 1
                                          require ext_call.success
                                          holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 -= mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                          mem[mem[64] + 64] = holding[stor3[mem[(32 * [94midx) + 128]][addr(_param2)]].field_768 - mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param1.length) + 192]
                                          log 0x563ecb3e: holding[_3394].field_0, addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                  mem[32] = 1
                                  mem[mem[64]] = holding[stor5.length + 1].field_256
                                  mem[mem[64] + 32] = addr(holding[stor5.length + 1].field_512)
                                  mem[mem[64] + 64] = holding[stor5.length + 1].field_768
                                  mem[mem[64] + 96] = holding[stor5.length + 1].field_1024
                                  mem[mem[64] + 128] = holding[stor5.length + 1].field_1280
                                  mem[0] = stor5.length + 1
                                  log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 6, stor5.length + 1
              [94midx = [94midx + 1
              continue 


# hash = 0x8b69450d
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknown8b69450d(): # not payable
  return stor5.length


# hash = 0xb1eb7998
# getter = None
# const = None
# payable = False
def unknownb1eb7998(uint256 _param1, addr _param2): # not payable
  require ext_code.size(addr(code.data[10837 len 32]))
  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args ('offerbook' << 184)
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xbd98583a with:
       gas gas_remaining - 50 wei
      args _param1, _param2
  require ext_call.success
  return (holding[stor3[_param1][addr(_param2)]].field_768 - ext_call.return_data[0])


# hash = 0xbae930cb
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def holding(uint256 _blockNumber): # not payable
  return holding[_blockNumber].field_0, 
         holding[_blockNumber].field_256,
         addr(holding[_blockNumber].field_512),
         holding[_blockNumber].field_768,
         holding[_blockNumber].field_1024,
         holding[_blockNumber].field_1280


# hash = 0xcd22bee5
# getter = None
# const = None
# payable = False
def unknowncd22bee5(uint256 _param1, addr _param2, uint256 _param3, uint8 _param4, bool _param5): # not payable
  require ext_code.size(addr(code.data[10837 len 32]))
  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if ext_call.return_data[12 len 20] == caller:
      [94ms = 0
      [94midx = 0
      while [94midx < stor5.length:
          mem[0] = stor5[[94midx].field_0
          mem[32] = 1
          if holding[stor5[[94midx].field_0].field_256 == _param1:
              if not _param5:
                  mem[0] = stor5[[94midx].field_0
                  require ext_code.size(addr(code.data[10837 len 32]))
                  call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                       gas gas_remaining - 50 wei
                      args 'stabletoken'
                  require ext_call.success
                  mem[100] = addr(holding[stor5[[94midx].field_0].field_512)
                  mem[132] = _param2
                  mem[164] = _param3 * holding[stor5[[94midx].field_0].field_768
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).adminTransfer(address from, address to, uint256 value) with:
                       gas gas_remaining - 50 wei
                      args addr(holding[stor5[[94midx].field_0].field_512), addr(_param2), _param3 * holding[stor5[[94midx].field_0].field_768
                  mem[96] = ext_call.return_data[0]
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      mem[96] = _param1
                      mem[128] = 5
                      log 0x5a29bc1d: _param1, 5, 3, addr(holding[stor5[idx].field_0].field_512)
              if 2 == _param4:
                  mem[96] = _param1
                  mem[128] = _param3 * holding[stor5[[94midx].field_0].field_768
                  log 0x8b36b54e: _param1, _param3 * holding[stor5[idx].field_0].field_768, 4, _param2, addr(holding[stor5[idx].field_0].field_512)
          [94ms = sha3(stor5[[94midx].field_0, 1)
          [94midx = [94midx + 1
          continue 
  else:
      if stor0 == caller:
          [94ms = 0
          [94midx = 0
          while [94midx < stor5.length:
              mem[0] = stor5[[94midx].field_0
              mem[32] = 1
              if holding[stor5[[94midx].field_0].field_256 == _param1:
                  if not _param5:
                      mem[0] = stor5[[94midx].field_0
                      require ext_code.size(addr(code.data[10837 len 32]))
                      call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                           gas gas_remaining - 50 wei
                          args 'stabletoken'
                      require ext_call.success
                      mem[100] = addr(holding[stor5[[94midx].field_0].field_512)
                      mem[132] = _param2
                      mem[164] = _param3 * holding[stor5[[94midx].field_0].field_768
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).adminTransfer(address from, address to, uint256 value) with:
                           gas gas_remaining - 50 wei
                          args addr(holding[stor5[[94midx].field_0].field_512), addr(_param2), _param3 * holding[stor5[[94midx].field_0].field_768
                      mem[96] = ext_call.return_data[0]
                      require ext_call.success
                      if not ext_call.return_data[0]:
                          mem[96] = _param1
                          mem[128] = 5
                          log 0x5a29bc1d: _param1, 5, 3, addr(holding[stor5[idx].field_0].field_512)
                  if 2 == _param4:
                      mem[96] = _param1
                      mem[128] = _param3 * holding[stor5[[94midx].field_0].field_768
                      log 0x8b36b54e: _param1, _param3 * holding[stor5[idx].field_0].field_768, 4, _param2, addr(holding[stor5[idx].field_0].field_512)
              [94ms = sha3(stor5[[94midx].field_0, 1)
              [94midx = [94midx + 1
              continue 
      else:
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x391465cb with:
               gas gas_remaining - 50 wei
              args _param1, caller
          require ext_call.success
          if ext_call.return_data[0]:
              [94ms = 0
              [94midx = 0
              while [94midx < stor5.length:
                  mem[0] = stor5[[94midx].field_0
                  mem[32] = 1
                  if holding[stor5[[94midx].field_0].field_256 == _param1:
                      if not _param5:
                          mem[0] = stor5[[94midx].field_0
                          require ext_code.size(addr(code.data[10837 len 32]))
                          call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
                               gas gas_remaining - 50 wei
                              args 'stabletoken'
                          require ext_call.success
                          mem[100] = addr(holding[stor5[[94midx].field_0].field_512)
                          mem[132] = _param2
                          mem[164] = _param3 * holding[stor5[[94midx].field_0].field_768
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).adminTransfer(address from, address to, uint256 value) with:
                               gas gas_remaining - 50 wei
                              args addr(holding[stor5[[94midx].field_0].field_512), addr(_param2), _param3 * holding[stor5[[94midx].field_0].field_768
                          mem[96] = ext_call.return_data[0]
                          require ext_call.success
                          if not ext_call.return_data[0]:
                              mem[96] = _param1
                              mem[128] = 5
                              log 0x5a29bc1d: _param1, 5, 3, addr(holding[stor5[idx].field_0].field_512)
                      if 2 == _param4:
                          mem[96] = _param1
                          mem[128] = _param3 * holding[stor5[[94midx].field_0].field_768
                          log 0x8b36b54e: _param1, _param3 * holding[stor5[idx].field_0].field_768, 4, _param2, addr(holding[stor5[idx].field_0].field_512)
                  [94ms = sha3(stor5[[94midx].field_0, 1)
                  [94midx = [94midx + 1
                  continue 
  return 0


# hash = 0xd295c57a
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknownd295c57a(uint256 _param1): # not payable
  return holding[_param1].field_256


# hash = 0xd759e241
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['cd', 4], 3]]]]]
# const = None
# payable = False
def unknownd759e241(uint256 _param1, addr _param2): # not payable
  return unknownd759e241[_param1][addr(_param2)]


# hash = 0xe57d6f52
# getter = None
# const = None
# payable = False
def unknowne57d6f52(uint256 _param1, uint256 _param2): # not payable
  if addr(holding[_param1].field_512):
      require ext_code.size(addr(code.data[10837 len 32]))
      call addr(code.data[10837 len 32]).addressOf(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 0x626f6e6400000000000000000000000000000000000000000000000000000000
      require ext_call.success
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x391465cb with:
           gas gas_remaining - 50 wei
          args holding[_param1].field_256, caller
      require ext_call.success
      if ext_call.return_data[0]:
          if _param2 >= 1:
              holding[_param1].field_768 += _param2
              log 0x563ecb3e: holding[_param1].field_256, 0, _param2 + holding[_param1].field_768, holding[_param1].field_1024, holding[_param1].field_1280, 7, holding[_param1].field_0
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x940589d6 with:
                   gas gas_remaining - 50 wei
                  args holding[_param1].field_256, _param2
              require ext_call.success
      else:
          if stor0 == caller:
              if _param2 >= 1:
                  holding[_param1].field_768 += _param2
                  log 0x563ecb3e: holding[_param1].field_256, 0, _param2 + holding[_param1].field_768, holding[_param1].field_1024, holding[_param1].field_1280, 7, holding[_param1].field_0
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x940589d6 with:
                       gas gas_remaining - 50 wei
                      args holding[_param1].field_256, _param2
                  require ext_call.success


# hash = 0xe849d4ef
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['cd', 4], 3]]]]], 1]]]]
# const = None
# payable = False
def unknowne849d4ef(uint256 _param1, addr _param2): # not payable
  return holding[stor3[_param1][addr(_param2)]].field_768


# hash = 0xe8a96b46
# getter = ['storage', 160, 0, ['add', 2, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def getHolder(uint256 _number): # not payable
  return addr(holding[_number].field_512)


# hash = 0xec375953
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknownec375953(uint256 _param1): # not payable
  return holding[_param1].field_768


# hash = 0xf49c505f
# getter = None
# const = None
# payable = False
def unknownf49c505f(uint256 _param1): # not payable
  mem[64] = 288
  [94ms = 96
  [94midx = 0
  [94ms = 0
  while [94midx < stor4[_param1].field_0:
      require [94midx < stor4[_param1].field_0
      mem[0] = stor4[_param1][[94midx].field_0
      mem[32] = 1
      [94m_14 = sha3(stor4[_param1][[94midx].field_0, 1)
      [94m_15 = mem[64]
      mem[64] = mem[64] + 192
      mem[[94m_15] = holding[stor4[_param1][[94midx].field_0].field_0
      mem[[94m_15 + 32] = holding[stor4[_param1][[94midx].field_0].field_256
      mem[[94m_15 + 64] = addr(holding[stor4[_param1][[94midx].field_0].field_512)
      mem[[94m_15 + 96] = holding[stor4[_param1][[94midx].field_0].field_768
      mem[[94m_15 + 128] = holding[stor4[_param1][[94midx].field_0].field_1024
      mem[[94m_15 + 160] = holding[stor4[_param1][[94midx].field_0].field_1280
      mem[0] = _param1
      mem[32] = 4
      [94ms = [94m_15
      [94midx = [94midx + 1
      [94ms = holding[stor4[_param1][[94midx].field_0].field_768 + [94ms
      continue 
  return (unknownd759e241[[94m_14] * stor4[_param1].field_0)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


