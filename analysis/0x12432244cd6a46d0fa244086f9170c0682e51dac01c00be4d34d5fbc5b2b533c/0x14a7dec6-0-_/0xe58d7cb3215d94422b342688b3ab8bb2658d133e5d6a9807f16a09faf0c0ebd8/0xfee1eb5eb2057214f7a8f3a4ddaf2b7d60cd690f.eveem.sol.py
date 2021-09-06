# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xFEE1eB5eb2057214f7A8F3a4dDaf2B7d60cD690f 
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
def unknown0c5e11e2(uint256 m_param1, addr m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5): # not payable
  require ext_code.size(addr(code.data[11131 len 32]))
  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if ext_call.return_data[12 len 20] != caller:
      if mstor0 != caller:
          return 0
  if munknownd759e241m[m_param1m]m[addr(m_param2)m]:
      return mholdingm[0m]m.field_0
  mholdingm[mstor5m.length + 1m]m.field_0 = mstor5m.length + 1
  mholdingm[mstor5m.length + 1m]m.field_256 = m_param1
  addr(mholdingm[mstor5m.length + 1m]m.field_512) = m_param2
  mholdingm[mstor5m.length + 1m]m.field_768 = m_param3
  mholdingm[mstor5m.length + 1m]m.field_1024 = m_param4
  mholdingm[mstor5m.length + 1m]m.field_1280 = m_param5
  munknownd759e241m[m_param1m]m[addr(m_param2)m] = mstor5m.length + 1
  mstor4m[m_param1m]m.field_0++
  if not mstor4m[m_param1m]m.field_0 <= mstor4m[m_param1m]m.field_0 + 1:
      [94midx = mstor4m[m_param1m]m.field_0 + 1
      mwhile mstor4m[m_param1m]m.field_0 > [94midxm:
          mstor4m[m_param1m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  mstor4m[m_param1m]m[mstor4m[m_param1m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
  mstor2m[addr(m_param2)m]m.field_0++
  mstor2m[addr(m_param2)m]m[mstor2m[addr(m_param2)m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
  mstor5m.length++
  mstor5m[mstor5m.lengthm]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
  log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
  return mholdingm[mstor5m.length + 1m]m.field_0


# hash = 0x0fb0a3b2
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def unknown0fb0a3b2(uint256 m_param1, addr m_param2): # not payable
  return mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_0, 
         mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_256,
         addr(mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_512),
         mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768,
         mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_1024,
         mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_1280


# hash = 0x1aa3a008
# getter = None
# const = None
# payable = False
def register(): # not payable
  if mstor0 == caller:
      require ext_code.size(code.data[11131 len 32])
      call code.data[11131 len 32].register(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 'custodian'
      require ext_call.success


# hash = 0x1cb78281
# getter = None
# const = None
# payable = False
def unknown1cb78281(uint256 m_param1, uint256 m_param2): # not payable
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
  if m_param2:
      [94ms = 224
      [94midx = m_param1
      mwhile [94midx < m_param2m:
          require [94midx < mstor5m.length
          mem[0] = mstor5m[[94midxm]m.field_0
          mem[32] = 1
          [94m_59 = mem[64]
          mem[64] = mem[64] + 192
          mem[[94m_59] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_0
          mem[[94m_59 + 32] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_256
          mem[[94m_59 + 64] = addr(mholdingm[mstor5m[[94midxm]m.field_0m]m.field_512)
          mem[[94m_59 + 96] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
          mem[[94m_59 + 128] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_1024
          mem[[94m_59 + 160] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_1280
          require [94midx < mem[96]
          mem[(32 * [94midx) + 128] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_0
          require [94midx < mem[128]
          mem[(32 * [94midx) + 160] = addr(mholdingm[mstor5m[[94midxm]m.field_0m]m.field_512)
          require [94midx < mem[160]
          mem[(32 * [94midx) + 192] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_256
          require [94midx < mem[192]
          mem[(32 * [94midx) + 224] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
          [94ms = [94m_59
          [94midx = [94midx + 1
          mcontinue 
  else:
      [94ms = 224
      [94midx = m_param1
      mwhile [94midx < mstor5m.lengthm:
          mem[0] = mstor5m[[94midxm]m.field_0
          mem[32] = 1
          [94m_72 = mem[64]
          mem[64] = mem[64] + 192
          mem[[94m_72] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_0
          mem[[94m_72 + 32] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_256
          mem[[94m_72 + 64] = addr(mholdingm[mstor5m[[94midxm]m.field_0m]m.field_512)
          mem[[94m_72 + 96] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
          mem[[94m_72 + 128] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_1024
          mem[[94m_72 + 160] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_1280
          require [94midx < mem[96]
          mem[(32 * [94midx) + 128] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_0
          require [94midx < mem[128]
          mem[(32 * [94midx) + 160] = addr(mholdingm[mstor5m[[94midxm]m.field_0m]m.field_512)
          require [94midx < mem[160]
          mem[(32 * [94midx) + 192] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_256
          require [94midx < mem[192]
          mem[(32 * [94midx) + 224] = mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
          [94ms = [94m_72
          [94midx = [94midx + 1
          mcontinue 
  mem[mem[64]] = 128
  mem[mem[64] + 128] = mem[96]
  mem[mem[64] + 160 len 32 * mem[96]] = mem[128 len 32 * mem[96]]
  mem[mem[64] + 32] = (32 * mem[96]) + 160
  mem[(32 * mem[96]) + mem[64] + 160] = mem[128]
  mem[(32 * mem[96]) + mem[64] + 192 len 32 * mem[128]] = mem[160 len 32 * mem[128]]
  mem[mem[64] + 64] = (32 * mem[128]) + (32 * mem[96]) + 192
  mem[(32 * mem[128]) + (32 * mem[96]) + mem[64] + 192] = mem[160]
  mem[(32 * mem[128]) + (32 * mem[96]) + mem[64] + 224 len 32 * mem[160]] = mem[192 len 32 * mem[160]]
  mem[mem[64] + 96] = (32 * mem[160]) + (32 * mem[128]) + (32 * mem[96]) + 224
  mem[(32 * mem[160]) + (32 * mem[128]) + (32 * mem[96]) + mem[64] + 224] = mem[192]
  mem[(32 * mem[160]) + (32 * mem[128]) + (32 * mem[96]) + mem[64] + 256 len 32 * mem[192]] = mem[224 len 32 * mem[192]]
  return Array(len=mem[mem[64] + 128 len (32 * mem[96]) + 32], data=mem[128], mem[mem[64] + (32 * mem[96]) + 192 len (32 * mem[192]) + (32 * mem[160]) + (32 * mem[128]) + 64]), 
         (32 * mem[96]) + 160,
         (32 * mem[128]) + (32 * mem[96]) + 192,
         (32 * mem[160]) + (32 * mem[128]) + (32 * mem[96]) + 224


# hash = 0x2d0b104c
# getter = None
# const = None
# payable = False
def unknown2d0b104c(uint256 m_param1, addr m_param2, addr m_param3, uint256 m_param4): # not payable
  require ext_code.size(addr(code.data[11131 len 32]))
  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if mstor0 != caller:
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x391465cb with:
           gas gas_remaining - 50 wei
          args m_param1, caller
      require ext_call.success
      if not ext_call.return_data[0]:
          return 0
  if addr(mholdingm[mstor3m[m_param1m]m[addr(m_param3)m]m]m.field_512):
      mholdingm[mstor3m[m_param1m]m[addr(m_param3)m]m]m.field_768 += m_param4
      if mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_1024 > 0:
          if mholdingm[mstor3m[m_param1m]m[addr(m_param3)m]m]m.field_1024 > 0:
              return 0
          mholdingm[mstor3m[m_param1m]m[addr(m_param3)m]m]m.field_1024 = mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_1024
          mholdingm[mstor3m[m_param1m]m[addr(m_param3)m]m]m.field_1280 = mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_1280
          mholdingm[mstor3m[m_param1m]m[addr(m_param3)m]m]m.field_1024 = 0
          if 1 == mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
              require ext_code.size(addr(code.data[11131 len 32]))
              call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                   gas gas_remaining - 50 wei
                  args 'cashsettled'
              require ext_call.success
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x43fb2310 with:
                   gas gas_remaining - 50 wei
                  args mholdingm[mstor3m[m_param1m]m[addr(m_param3)m]m]m.field_1024, munknownd759e241m[m_param1m]m[addr(m_param3)m]
              require ext_call.success
          else:
              if 2 == mholdingm[mstor3m[m_param1m]m[addr(m_param3)m]m]m.field_1280:
                  require ext_code.size(addr(code.data[11131 len 32]))
                  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                       gas gas_remaining - 50 wei
                      args 'cashsettled'
                  require ext_call.success
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x173396bb with:
                       gas gas_remaining - 50 wei
                      args mholdingm[mstor3m[m_param1m]m[addr(m_param3)m]m]m.field_1024, munknownd759e241m[m_param1m]m[addr(m_param3)m]
                  require ext_call.success
      mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768 -= m_param4
      log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, 0, holding[stor3[_param1][addr(_param2)]].field_768 - _param4, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 6, holding[stor3[_param1][addr(_param2)]].field_0
      log 0x563ecb3e: holding[stor3[_param1][addr(_param3)]].field_256, 0, holding[stor3[_param1][addr(_param3)]].field_768, holding[stor3[_param1][addr(_param3)]].field_1024, holding[stor3[_param1][addr(_param3)]].field_1280, 6, unknownd759e241[_param1][addr(_param3)]
  else:
      mholdingm[mstor5m.length + 1m]m.field_0 = mstor5m.length + 1
      mholdingm[mstor5m.length + 1m]m.field_256 = m_param1
      addr(mholdingm[mstor5m.length + 1m]m.field_512) = m_param3
      mholdingm[mstor5m.length + 1m]m.field_768 = m_param4
      mholdingm[mstor5m.length + 1m]m.field_1280 = 1
      munknownd759e241m[m_param1m]m[addr(m_param3)m] = mstor5m.length + 1
      mstor4m[m_param1m]m.field_0++
      mstor4m[m_param1m]m[mstor4m[m_param1m]m.field_0m]m.field_0 = mstor5m.length + 1
      mstor2m[addr(m_param3)m]m.field_0++
      mstor2m[addr(m_param3)m]m[mstor2m[addr(m_param3)m]m.field_0m]m.field_0 = mstor5m.length + 1
      mstor5m.length++
      mstor5m[mstor5m.lengthm]m.field_0 = mstor5m.length + 1
      if mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_1024 > 0:
          if mholdingm[mstor5m.length + 1m]m.field_1024 > 0:
              return 0
          mholdingm[mstor5m.length + 1m]m.field_1024 = mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_1024
          mholdingm[mstor5m.length + 1m]m.field_1280 = mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_1280
          mholdingm[mstor5m.length + 1m]m.field_1024 = 0
          if 1 == mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
              require ext_code.size(addr(code.data[11131 len 32]))
              call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                   gas gas_remaining - 50 wei
                  args 'cashsettled'
              require ext_call.success
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x43fb2310 with:
                   gas gas_remaining - 50 wei
                  args mholdingm[mstor5m.length + 1m]m.field_1024, mstor5m.length + 1
              require ext_call.success
          else:
              if 2 == mholdingm[mstor5m.length + 1m]m.field_1280:
                  require ext_code.size(addr(code.data[11131 len 32]))
                  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                       gas gas_remaining - 50 wei
                      args 'cashsettled'
                  require ext_call.success
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x173396bb with:
                       gas gas_remaining - 50 wei
                      args mholdingm[mstor5m.length + 1m]m.field_1024, mstor5m.length + 1
                  require ext_call.success
      mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768 -= m_param4
      log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, 0, holding[stor3[_param1][addr(_param2)]].field_768 - _param4, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 6, holding[stor3[_param1][addr(_param2)]].field_0
      log 0x563ecb3e: holding[stor5.length + 1].field_256, 0, holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 6, stor5.length + 1
  return 1


# hash = 0x308f16da
# getter = None
# const = None
# payable = False
def unknown308f16da(uint256 m_param1, addr m_param2, addr m_param3, uint256 m_param4, uint256 m_param5, bool m_param6): # not payable
  require ext_code.size(addr(code.data[11131 len 32]))
  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args ('offerbook' << 184)
  require ext_call.success
  require ext_code.size(code.data[11131 len 32])
  call code.data[11131 len 32].addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if addr(ext_call.return_data[0]) != caller:
      if mstor0 != caller:
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x391465cb with:
               gas gas_remaining - 50 wei
              args m_param1, caller
          require ext_call.success
          if not ext_call.return_data[0]:
              return 0
  if m_param5 <= 0:
      return 1
  if m_param6:
      return 1
  require ext_code.size(addr(code.data[11131 len 32]))
  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 'stabletoken'
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).adminTransfer(address from, address to, uint256 value) with:
       gas gas_remaining - 50 wei
      args addr(m_param2), addr(m_param3), m_param4 * m_param5
  require ext_call.success
  if not ext_call.return_data[0]:
      log 0x5a29bc1d: _param1, 5, 3, _param2
  return bool(ext_call.return_data[0])


# hash = 0x30ac2e7f
# getter = None
# const = None
# payable = False
def unknown30ac2e7f(addr m_param1): # not payable
  if mstor2m[addr(m_param1)m]m.field_0:
      mem[160] = mstor2m[addr(m_param1)m]m.field_0
      [94midx = 160
      [94ms = 0
      mwhile (32 * mstor2m[addr(m_param1)m]m.field_0) + 128 > [94midxm:
          mem[[94midx + 32] = mstor2m[addr(m_param1)m]m[[94msm]m.field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
  return Array(len=mstor2m[addr(m_param1)m]m.field_0, data=mem[160 len 32 * mstor2m[addr(m_param1)m]m.field_0])


# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  if mstor0 == caller:
      [93mselfdestruct([91mstor0[93m)


# hash = 0x56457b00
# getter = None
# const = None
# payable = False
def unknown56457b00(): # not payable
  if mstor5m.length:
      mem[160] = uint256(mstor5m.field_0)
      [94midx = 160
      [94ms = 0
      mwhile (32 * mstor5m.length) + 128 > [94midxm:
          mem[[94midx + 32] = mstor5m[[94msm]m.field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
  return Array(len=mstor5m.length, data=mem[160 len 32 * mstor5m.length])


# hash = 0x6ef22110
# getter = None
# const = None
# payable = False
def unknown6ef22110(uint256 m_param1): # not payable
  if mstor4m[m_param1m]m.field_0:
      mem[160] = mstor4m[m_param1m]m.field_0
      if (32 * mstor4m[m_param1m]m.field_0) + 32 > 64:
          mem[192] = mstor4m[m_param1m]m.field_256
          [94midx = 192
          [94ms = 1
          mwhile (32 * mstor4m[m_param1m]m.field_0) + 128 > [94midxm:
              mem[[94midx + 32] = mstor4m[m_param1m]m[[94msm]m.field_256
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
  return Array(len=mstor4m[m_param1m]m.field_0, data=mem[160 len 32 * mstor4m[m_param1m]m.field_0])


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address m_newAdmin): # not payable
  if mstor0 == caller:
      mstor0 = m_newAdmin


# hash = 0x7954e911
# getter = None
# const = None
# payable = False
def unknown7954e911(uint256 m_param1, addr m_param2, uint256 m_param3): # not payable
  require ext_code.size(addr(code.data[11131 len 32]))
  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  require ext_code.size(code.data[11131 len 32])
  call code.data[11131 len 32].addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args ('offerbook' << 184)
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).exists(uint256 tokenId) with:
       gas gas_remaining - 50 wei
      args m_param1
  require ext_call.success
  if ext_call.return_data[0]:
      require ext_code.size(addr(ext_call.return_data[0]))
      if caller == addr(ext_call.return_data[0]):
          call addr(ext_call.return_data[0]).0x92089c46 with:
               gas gas_remaining - 50 wei
              args m_param1
          require ext_call.success
          if addr(ext_call.return_data[0]) != caller:
              if addr(mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_512):
                  mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768 += m_param3
                  log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
              else:
                  if not munknownd759e241m[m_param1m]m[addr(m_param2)m]:
                      mholdingm[mstor5m.length + 1m]m.field_0 = mstor5m.length + 1
                      mholdingm[mstor5m.length + 1m]m.field_256 = m_param1
                      addr(mholdingm[mstor5m.length + 1m]m.field_512) = m_param2
                      mholdingm[mstor5m.length + 1m]m.field_768 = m_param3
                      mholdingm[mstor5m.length + 1m]m.field_1024 = 0
                      mholdingm[mstor5m.length + 1m]m.field_1280 = 1
                      munknownd759e241m[m_param1m]m[addr(m_param2)m] = mstor5m.length + 1
                      mstor4m[m_param1m]m.field_0++
                      if not mstor4m[m_param1m]m.field_0 <= mstor4m[m_param1m]m.field_0 + 1:
                          [94midx = mstor4m[m_param1m]m.field_0 + 1
                          mwhile mstor4m[m_param1m]m.field_0 > [94midxm:
                              mstor4m[m_param1m]m[[94midxm]m.field_0 = 0
                              [94midx = [94midx + 1
                              mcontinue 
                      mstor4m[m_param1m]m[mstor4m[m_param1m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                      mstor2m[addr(m_param2)m]m.field_0++
                      mstor2m[addr(m_param2)m]m[mstor2m[addr(m_param2)m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                      mstor5m.length++
                      mstor5m[mstor5m.lengthm]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                      log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x940589d6 with:
                   gas gas_remaining - 50 wei
                  args m_param1, m_param3
              require ext_call.success
          else:
              if ext_call.return_data[12 len 20] == m_param2:
                  if addr(mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_512):
                      mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768 += m_param3
                      log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
                  else:
                      if not munknownd759e241m[m_param1m]m[addr(m_param2)m]:
                          mholdingm[mstor5m.length + 1m]m.field_0 = mstor5m.length + 1
                          mholdingm[mstor5m.length + 1m]m.field_256 = m_param1
                          addr(mholdingm[mstor5m.length + 1m]m.field_512) = m_param2
                          mholdingm[mstor5m.length + 1m]m.field_768 = m_param3
                          mholdingm[mstor5m.length + 1m]m.field_1024 = 0
                          mholdingm[mstor5m.length + 1m]m.field_1280 = 1
                          munknownd759e241m[m_param1m]m[addr(m_param2)m] = mstor5m.length + 1
                          mstor4m[m_param1m]m.field_0++
                          if not mstor4m[m_param1m]m.field_0 <= mstor4m[m_param1m]m.field_0 + 1:
                              [94midx = mstor4m[m_param1m]m.field_0 + 1
                              mwhile mstor4m[m_param1m]m.field_0 > [94midxm:
                                  mstor4m[m_param1m]m[[94midxm]m.field_0 = 0
                                  [94midx = [94midx + 1
                                  mcontinue 
                          mstor4m[m_param1m]m[mstor4m[m_param1m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                          mstor2m[addr(m_param2)m]m.field_0++
                          mstor2m[addr(m_param2)m]m[mstor2m[addr(m_param2)m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                          mstor5m.length++
                          mstor5m[mstor5m.lengthm]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                          log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x940589d6 with:
                       gas gas_remaining - 50 wei
                      args m_param1, m_param3
                  require ext_call.success
      else:
          if mstor0 == caller:
              call addr(ext_call.return_data[0]).0x92089c46 with:
                   gas gas_remaining - 50 wei
                  args m_param1
              require ext_call.success
              if addr(ext_call.return_data[0]) != caller:
                  if addr(mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_512):
                      mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768 += m_param3
                      log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
                  else:
                      if not munknownd759e241m[m_param1m]m[addr(m_param2)m]:
                          mholdingm[mstor5m.length + 1m]m.field_0 = mstor5m.length + 1
                          mholdingm[mstor5m.length + 1m]m.field_256 = m_param1
                          addr(mholdingm[mstor5m.length + 1m]m.field_512) = m_param2
                          mholdingm[mstor5m.length + 1m]m.field_768 = m_param3
                          mholdingm[mstor5m.length + 1m]m.field_1024 = 0
                          mholdingm[mstor5m.length + 1m]m.field_1280 = 1
                          munknownd759e241m[m_param1m]m[addr(m_param2)m] = mstor5m.length + 1
                          mstor4m[m_param1m]m.field_0++
                          if not mstor4m[m_param1m]m.field_0 <= mstor4m[m_param1m]m.field_0 + 1:
                              [94midx = mstor4m[m_param1m]m.field_0 + 1
                              mwhile mstor4m[m_param1m]m.field_0 > [94midxm:
                                  mstor4m[m_param1m]m[[94midxm]m.field_0 = 0
                                  [94midx = [94midx + 1
                                  mcontinue 
                          mstor4m[m_param1m]m[mstor4m[m_param1m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                          mstor2m[addr(m_param2)m]m.field_0++
                          mstor2m[addr(m_param2)m]m[mstor2m[addr(m_param2)m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                          mstor5m.length++
                          mstor5m[mstor5m.lengthm]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                          log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x940589d6 with:
                       gas gas_remaining - 50 wei
                      args m_param1, m_param3
                  require ext_call.success
              else:
                  if ext_call.return_data[12 len 20] == m_param2:
                      if addr(mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_512):
                          mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768 += m_param3
                          log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
                      else:
                          if not munknownd759e241m[m_param1m]m[addr(m_param2)m]:
                              mholdingm[mstor5m.length + 1m]m.field_0 = mstor5m.length + 1
                              mholdingm[mstor5m.length + 1m]m.field_256 = m_param1
                              addr(mholdingm[mstor5m.length + 1m]m.field_512) = m_param2
                              mholdingm[mstor5m.length + 1m]m.field_768 = m_param3
                              mholdingm[mstor5m.length + 1m]m.field_1024 = 0
                              mholdingm[mstor5m.length + 1m]m.field_1280 = 1
                              munknownd759e241m[m_param1m]m[addr(m_param2)m] = mstor5m.length + 1
                              mstor4m[m_param1m]m.field_0++
                              if not mstor4m[m_param1m]m.field_0 <= mstor4m[m_param1m]m.field_0 + 1:
                                  [94midx = mstor4m[m_param1m]m.field_0 + 1
                                  mwhile mstor4m[m_param1m]m.field_0 > [94midxm:
                                      mstor4m[m_param1m]m[[94midxm]m.field_0 = 0
                                      [94midx = [94midx + 1
                                      mcontinue 
                              mstor4m[m_param1m]m[mstor4m[m_param1m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                              mstor2m[addr(m_param2)m]m.field_0++
                              mstor2m[addr(m_param2)m]m[mstor2m[addr(m_param2)m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                              mstor5m.length++
                              mstor5m[mstor5m.lengthm]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                              log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).0x940589d6 with:
                           gas gas_remaining - 50 wei
                          args m_param1, m_param3
                      require ext_call.success
          else:
              call addr(ext_call.return_data[0]).0x391465cb with:
                   gas gas_remaining - 50 wei
                  args m_param1, caller
              require ext_call.success
              if ext_call.return_data[0]:
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x92089c46 with:
                       gas gas_remaining - 50 wei
                      args m_param1
                  require ext_call.success
                  if addr(ext_call.return_data[0]) != caller:
                      if addr(mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_512):
                          mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768 += m_param3
                          log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
                      else:
                          if not munknownd759e241m[m_param1m]m[addr(m_param2)m]:
                              mholdingm[mstor5m.length + 1m]m.field_0 = mstor5m.length + 1
                              mholdingm[mstor5m.length + 1m]m.field_256 = m_param1
                              addr(mholdingm[mstor5m.length + 1m]m.field_512) = m_param2
                              mholdingm[mstor5m.length + 1m]m.field_768 = m_param3
                              mholdingm[mstor5m.length + 1m]m.field_1024 = 0
                              mholdingm[mstor5m.length + 1m]m.field_1280 = 1
                              munknownd759e241m[m_param1m]m[addr(m_param2)m] = mstor5m.length + 1
                              mstor4m[m_param1m]m.field_0++
                              if not mstor4m[m_param1m]m.field_0 <= mstor4m[m_param1m]m.field_0 + 1:
                                  [94midx = mstor4m[m_param1m]m.field_0 + 1
                                  mwhile mstor4m[m_param1m]m.field_0 > [94midxm:
                                      mstor4m[m_param1m]m[[94midxm]m.field_0 = 0
                                      [94midx = [94midx + 1
                                      mcontinue 
                              mstor4m[m_param1m]m[mstor4m[m_param1m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                              mstor2m[addr(m_param2)m]m.field_0++
                              mstor2m[addr(m_param2)m]m[mstor2m[addr(m_param2)m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                              mstor5m.length++
                              mstor5m[mstor5m.lengthm]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                              log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).0x940589d6 with:
                           gas gas_remaining - 50 wei
                          args m_param1, m_param3
                      require ext_call.success
                  else:
                      if ext_call.return_data[12 len 20] == m_param2:
                          if addr(mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_512):
                              mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768 += m_param3
                              log 0x563ecb3e: holding[stor3[_param1][addr(_param2)]].field_256, addr(holding[stor3[_param1][addr(_param2)]].field_512), _param3 + holding[stor3[_param1][addr(_param2)]].field_768, holding[stor3[_param1][addr(_param2)]].field_1024, holding[stor3[_param1][addr(_param2)]].field_1280, 7, holding[stor3[_param1][addr(_param2)]].field_0
                          else:
                              if not munknownd759e241m[m_param1m]m[addr(m_param2)m]:
                                  mholdingm[mstor5m.length + 1m]m.field_0 = mstor5m.length + 1
                                  mholdingm[mstor5m.length + 1m]m.field_256 = m_param1
                                  addr(mholdingm[mstor5m.length + 1m]m.field_512) = m_param2
                                  mholdingm[mstor5m.length + 1m]m.field_768 = m_param3
                                  mholdingm[mstor5m.length + 1m]m.field_1024 = 0
                                  mholdingm[mstor5m.length + 1m]m.field_1280 = 1
                                  munknownd759e241m[m_param1m]m[addr(m_param2)m] = mstor5m.length + 1
                                  mstor4m[m_param1m]m.field_0++
                                  if not mstor4m[m_param1m]m.field_0 <= mstor4m[m_param1m]m.field_0 + 1:
                                      [94midx = mstor4m[m_param1m]m.field_0 + 1
                                      mwhile mstor4m[m_param1m]m.field_0 > [94midxm:
                                          mstor4m[m_param1m]m[[94midxm]m.field_0 = 0
                                          [94midx = [94midx + 1
                                          mcontinue 
                                  mstor4m[m_param1m]m[mstor4m[m_param1m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                                  mstor2m[addr(m_param2)m]m.field_0++
                                  mstor2m[addr(m_param2)m]m[mstor2m[addr(m_param2)m]m.field_0m]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                                  mstor5m.length++
                                  mstor5m[mstor5m.lengthm]m.field_0 = mholdingm[mstor5m.length + 1m]m.field_0
                                  log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 5, holding[stor5.length + 1].field_0
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).0x940589d6 with:
                               gas gas_remaining - 50 wei
                              args m_param1, m_param3
                          require ext_call.success


# hash = 0x7acd04e9
# getter = None
# const = None
# payable = False
def unknown7acd04e9(array m_param1, addr m_param2, array m_param3, array m_param4): # not payable
  mem[96] = m_param1.length
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  mem[(32 * m_param1.length) + 128] = m_param3.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param3.length] = call.data[m_param3 + 36 len 32 * m_param3.length]
  mem[64] = (32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param1.length) + 192
  mem[(32 * m_param3.length) + (32 * m_param1.length) + 160] = m_param4.length
  mem[(32 * m_param3.length) + (32 * m_param1.length) + 192 len 32 * m_param4.length] = call.data[m_param4 + 36 len 32 * m_param4.length]
  if m_param1.length == m_param3.length:
      if m_param1.length == m_param4.length:
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param1.length) + 224] = 0
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param1.length) + 196] = 0x626f6e6400000000000000000000000000000000000000000000000000000000
          require ext_code.size(addr(code.data[11131 len 32]))
          call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param1.length) + 192] = ext_call.return_data[0]
          require ext_call.success
          [94midx = 0
          mwhile [94midx < m_param1.lengthm:
              require [94midx < mem[96]
              if mstor0 == caller:
                  require [94midx < mem[(32 * m_param1.length) + 128]
                  require [94midx < mem[(32 * m_param3.length) + (32 * m_param1.length) + 160]
                  [94m_3370 = mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                  mem[0] = mem[(32 * [94midx) + 128]
                  [94m_3373 = sha3(munknownd759e241m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m], 1)
                  [94m_3374 = sha3(addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160]), sha3(mem[(32 * [94midx) + 128], 3))
                  if addr(mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_512):
                      mem[32] = 1
                      mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_768 += mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                      if mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1024 <= 0:
                          mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                          mem[mem[64]] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_256
                          mem[mem[64] + 32] = addr(mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_512)
                          mem[mem[64] + 64] = mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_768 - [94m_3370
                          mem[mem[64] + 96] = mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_1024
                          log 0x563ecb3e: mem[mem[64] len 64], holding[stor3[mem[0]][addr(_param2)]].field_768 - _3370, holding[stor3[mem[0]][addr(_param2)]].field_1024, holding[stor3[mem[0]][addr(_param2)]].field_1280, 6, holding[stor3[mem[0]][addr(_param2)]].field_0
                          mem[32] = 1
                          mem[mem[64]] = mholdingm[mstor[[94m_3374m]m]m.field_256
                          mem[mem[64] + 32] = addr(mholdingm[mstor[[94m_3374m]m]m.field_512)
                          mem[mem[64] + 64] = mholdingm[mstor[[94m_3374m]m]m.field_768
                          mem[mem[64] + 96] = mholdingm[mstor[[94m_3374m]m]m.field_1024
                          mem[mem[64] + 128] = mholdingm[mstor[[94m_3374m]m]m.field_1280
                          mem[0] = mstor[[94m_3374m]
                          log 0x563ecb3e: holding[stor[_3374]].field_256, addr(holding[stor[_3374]].field_512), holding[stor[_3374]].field_768, holding[stor[_3374]].field_1024, holding[stor[_3374]].field_1280, 6, stor[_3374]
                      else:
                          mem[0] = munknownd759e241m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]
                          mem[32] = 1
                          if mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1024 <= 0:
                              mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1024 = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1024
                              mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1280 = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1280
                              mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1024 = 0
                              if 1 == mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1280:
                                  require ext_code.size(addr(code.data[11131 len 32]))
                                  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'cashsettled'
                                  require ext_call.success
                                  mem[0] = munknownd759e241m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]
                                  mem[32] = 1
                                  mem[mem[64] + 4] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1024
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).0x43fb2310 with:
                                       gas gas_remaining - 50 wei
                                      args mem[mem[64] + 4], mstor[[94m_3374m]
                                  require ext_call.success
                                  munknownd759e241m[[94m_3373m] -= [94m_3370
                                  mem[mem[64] + 64] = munknownd759e241m[[94m_3373m] - [94m_3370
                                  log 0x563ecb3e: holding[_3373].field_0, addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                              else:
                                  mem[32] = 1
                                  if mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1280 != 2:
                                      mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                      mem[mem[64]] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_256
                                      mem[mem[64] + 64] = munknownd759e241m[[94m_3373m] - [94m_3370
                                      mem[mem[64] + 96] = mstor4m[[94m_3373m]m.field_0
                                      log 0x563ecb3e: mem[mem[64]], addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                                  else:
                                      require ext_code.size(addr(code.data[11131 len 32]))
                                      call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'cashsettled'
                                      require ext_call.success
                                      mem[0] = munknownd759e241m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]
                                      mem[32] = 1
                                      mem[mem[64] + 4] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1024
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).0x173396bb with:
                                           gas gas_remaining - 50 wei
                                          args mem[mem[64] + 4], mstor[[94m_3374m]
                                      require ext_call.success
                                      munknownd759e241m[[94m_3373m] -= [94m_3370
                                      mem[mem[64] + 64] = munknownd759e241m[[94m_3373m] - [94m_3370
                                      log 0x563ecb3e: holding[_3373].field_0, addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                              mem[32] = 1
                              mem[mem[64]] = mholdingm[mstor[[94m_3374m]m]m.field_256
                              mem[mem[64] + 32] = addr(mholdingm[mstor[[94m_3374m]m]m.field_512)
                              mem[mem[64] + 64] = mholdingm[mstor[[94m_3374m]m]m.field_768
                              mem[mem[64] + 96] = mholdingm[mstor[[94m_3374m]m]m.field_1024
                              mem[mem[64] + 128] = mholdingm[mstor[[94m_3374m]m]m.field_1280
                              mem[0] = mstor[[94m_3374m]
                              log 0x563ecb3e: holding[stor[_3374]].field_256, addr(holding[stor[_3374]].field_512), holding[stor[_3374]].field_768, holding[stor[_3374]].field_1024, holding[stor[_3374]].field_1280, 6, stor[_3374]
                  else:
                      mholdingm[mstor5m.length + 1m]m.field_0 = mstor5m.length + 1
                      mholdingm[mstor5m.length + 1m]m.field_256 = mem[(32 * [94midx) + 128]
                      addr(mholdingm[mstor5m.length + 1m]m.field_512) = mem[(32 * [94midx) + (32 * m_param1.length) + 172 len 20]
                      mholdingm[mstor5m.length + 1m]m.field_768 = mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                      mholdingm[mstor5m.length + 1m]m.field_1280 = 1
                      munknownd759e241m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m] = mstor5m.length + 1
                      mstor4m[mem[(32 * [94midx) + 128]m]m.field_0++
                      mstor4m[mem[(32 * [94midx) + 128]m]m[mstor4m[mem[(32 * [94midx) + 128]m]m.field_0m]m.field_0 = mstor5m.length + 1
                      mem[32] = 2
                      mstor2m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m.field_0++
                      mstor2m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m[mstor2m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m.field_0m]m.field_0 = mstor5m.length + 1
                      mstor5m.length++
                      mstor5m[mstor5m.lengthm]m.field_0 = mstor5m.length + 1
                      if mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1024 <= 0:
                          mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                          mem[mem[64]] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_256
                          mem[mem[64] + 32] = addr(mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_512)
                          mem[mem[64] + 64] = mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_768 - [94m_3370
                          mem[mem[64] + 96] = mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_1024
                          log 0x563ecb3e: mem[mem[64] len 64], holding[stor3[mem[0]][addr(_param2)]].field_768 - _3370, holding[stor3[mem[0]][addr(_param2)]].field_1024, holding[stor3[mem[0]][addr(_param2)]].field_1280, 6, holding[stor3[mem[0]][addr(_param2)]].field_0
                          mem[32] = 1
                          mem[mem[64]] = mholdingm[mstor5m.length + 1m]m.field_256
                          mem[mem[64] + 32] = addr(mholdingm[mstor5m.length + 1m]m.field_512)
                          mem[mem[64] + 64] = mholdingm[mstor5m.length + 1m]m.field_768
                          mem[mem[64] + 96] = mholdingm[mstor5m.length + 1m]m.field_1024
                          mem[mem[64] + 128] = mholdingm[mstor5m.length + 1m]m.field_1280
                          mem[0] = mstor5m.length + 1
                          log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 6, stor5.length + 1
                      else:
                          mem[0] = mstor5m.length + 1
                          mem[32] = 1
                          if mholdingm[mstor5m.length + 1m]m.field_1024 <= 0:
                              mholdingm[mstor5m.length + 1m]m.field_1024 = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1024
                              mholdingm[mstor5m.length + 1m]m.field_1280 = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1280
                              mholdingm[mstor5m.length + 1m]m.field_1024 = 0
                              if 1 == mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1280:
                                  require ext_code.size(addr(code.data[11131 len 32]))
                                  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'cashsettled'
                                  require ext_call.success
                                  mem[0] = mstor5m.length + 1
                                  mem[32] = 1
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).0x43fb2310 with:
                                       gas gas_remaining - 50 wei
                                      args mholdingm[mstor5m.length + 1m]m.field_1024, mstor5m.length + 1
                                  require ext_call.success
                                  mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                  mem[mem[64] + 64] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 - mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                  log 0x563ecb3e: holding[_3373].field_0, addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                              else:
                                  mem[32] = 1
                                  if mholdingm[mstor5m.length + 1m]m.field_1280 != 2:
                                      mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                      mem[mem[64]] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_256
                                      mem[mem[64] + 64] = munknownd759e241m[[94m_3373m] - [94m_3370
                                      mem[mem[64] + 96] = mstor4m[[94m_3373m]m.field_0
                                      log 0x563ecb3e: mem[mem[64]], addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                                  else:
                                      require ext_code.size(addr(code.data[11131 len 32]))
                                      call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'cashsettled'
                                      require ext_call.success
                                      mem[0] = mstor5m.length + 1
                                      mem[32] = 1
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).0x173396bb with:
                                           gas gas_remaining - 50 wei
                                          args mholdingm[mstor5m.length + 1m]m.field_1024, mstor5m.length + 1
                                      require ext_call.success
                                      mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                      mem[mem[64] + 64] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 - mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                      log 0x563ecb3e: holding[_3373].field_0, addr(stor2[_3373].field_0), unknownd759e241[_3373] - _3370, stor4[_3373].field_0, stor5[_3373].field_0, 6, stor[_3373]
                              mem[32] = 1
                              mem[mem[64]] = mholdingm[mstor5m.length + 1m]m.field_256
                              mem[mem[64] + 32] = addr(mholdingm[mstor5m.length + 1m]m.field_512)
                              mem[mem[64] + 64] = mholdingm[mstor5m.length + 1m]m.field_768
                              mem[mem[64] + 96] = mholdingm[mstor5m.length + 1m]m.field_1024
                              mem[mem[64] + 128] = mholdingm[mstor5m.length + 1m]m.field_1280
                              mem[0] = mstor5m.length + 1
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
                      require [94midx < mem[(32 * m_param1.length) + 128]
                      require [94midx < mem[(32 * m_param3.length) + (32 * m_param1.length) + 160]
                      [94m_3389 = mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                      mem[0] = mem[(32 * [94midx) + 128]
                      [94m_3394 = sha3(munknownd759e241m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m], 1)
                      [94m_3395 = sha3(addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160]), sha3(mem[(32 * [94midx) + 128], 3))
                      if addr(mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_512):
                          mem[32] = 1
                          mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_768 += mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                          if mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1024 <= 0:
                              mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                              mem[mem[64]] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_256
                              mem[mem[64] + 32] = addr(mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_512)
                              mem[mem[64] + 64] = mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_768 - [94m_3389
                              mem[mem[64] + 96] = mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_1024
                              log 0x563ecb3e: mem[mem[64] len 64], holding[stor3[mem[0]][addr(_param2)]].field_768 - _3389, holding[stor3[mem[0]][addr(_param2)]].field_1024, holding[stor3[mem[0]][addr(_param2)]].field_1280, 6, holding[stor3[mem[0]][addr(_param2)]].field_0
                              mem[32] = 1
                              mem[mem[64]] = mholdingm[mstor[[94m_3395m]m]m.field_256
                              mem[mem[64] + 32] = addr(mholdingm[mstor[[94m_3395m]m]m.field_512)
                              mem[mem[64] + 64] = mholdingm[mstor[[94m_3395m]m]m.field_768
                              mem[mem[64] + 96] = mholdingm[mstor[[94m_3395m]m]m.field_1024
                              mem[mem[64] + 128] = mholdingm[mstor[[94m_3395m]m]m.field_1280
                              mem[0] = mstor[[94m_3395m]
                              log 0x563ecb3e: holding[stor[_3395]].field_256, addr(holding[stor[_3395]].field_512), holding[stor[_3395]].field_768, holding[stor[_3395]].field_1024, holding[stor[_3395]].field_1280, 6, stor[_3395]
                          else:
                              mem[0] = munknownd759e241m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]
                              mem[32] = 1
                              if mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1024 <= 0:
                                  mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1024 = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1024
                                  mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1280 = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1280
                                  mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1024 = 0
                                  if 1 == mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1280:
                                      require ext_code.size(addr(code.data[11131 len 32]))
                                      call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'cashsettled'
                                      require ext_call.success
                                      mem[0] = munknownd759e241m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]
                                      mem[32] = 1
                                      mem[mem[64] + 4] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1024
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).0x43fb2310 with:
                                           gas gas_remaining - 50 wei
                                          args mem[mem[64] + 4], mstor[[94m_3395m]
                                      require ext_call.success
                                      munknownd759e241m[[94m_3394m] -= [94m_3389
                                      mem[mem[64] + 64] = munknownd759e241m[[94m_3394m] - [94m_3389
                                      log 0x563ecb3e: holding[_3394].field_0, addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                  else:
                                      mem[32] = 1
                                      if mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1280 != 2:
                                          mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                          mem[mem[64]] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_256
                                          mem[mem[64] + 64] = munknownd759e241m[[94m_3394m] - [94m_3389
                                          mem[mem[64] + 96] = mstor4m[[94m_3394m]m.field_0
                                          log 0x563ecb3e: mem[mem[64]], addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                      else:
                                          require ext_code.size(addr(code.data[11131 len 32]))
                                          call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'cashsettled'
                                          require ext_call.success
                                          mem[0] = munknownd759e241m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]
                                          mem[32] = 1
                                          mem[mem[64] + 4] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m]m.field_1024
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0x173396bb with:
                                               gas gas_remaining - 50 wei
                                              args mem[mem[64] + 4], mstor[[94m_3395m]
                                          require ext_call.success
                                          munknownd759e241m[[94m_3394m] -= [94m_3389
                                          mem[mem[64] + 64] = munknownd759e241m[[94m_3394m] - [94m_3389
                                          log 0x563ecb3e: holding[_3394].field_0, addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                  mem[32] = 1
                                  mem[mem[64]] = mholdingm[mstor[[94m_3395m]m]m.field_256
                                  mem[mem[64] + 32] = addr(mholdingm[mstor[[94m_3395m]m]m.field_512)
                                  mem[mem[64] + 64] = mholdingm[mstor[[94m_3395m]m]m.field_768
                                  mem[mem[64] + 96] = mholdingm[mstor[[94m_3395m]m]m.field_1024
                                  mem[mem[64] + 128] = mholdingm[mstor[[94m_3395m]m]m.field_1280
                                  mem[0] = mstor[[94m_3395m]
                                  log 0x563ecb3e: holding[stor[_3395]].field_256, addr(holding[stor[_3395]].field_512), holding[stor[_3395]].field_768, holding[stor[_3395]].field_1024, holding[stor[_3395]].field_1280, 6, stor[_3395]
                      else:
                          mholdingm[mstor5m.length + 1m]m.field_0 = mstor5m.length + 1
                          mholdingm[mstor5m.length + 1m]m.field_256 = mem[(32 * [94midx) + 128]
                          addr(mholdingm[mstor5m.length + 1m]m.field_512) = mem[(32 * [94midx) + (32 * m_param1.length) + 172 len 20]
                          mholdingm[mstor5m.length + 1m]m.field_768 = mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                          mholdingm[mstor5m.length + 1m]m.field_1280 = 1
                          munknownd759e241m[mem[(32 * [94midx) + 128]m]m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m] = mstor5m.length + 1
                          mstor4m[mem[(32 * [94midx) + 128]m]m.field_0++
                          mstor4m[mem[(32 * [94midx) + 128]m]m[mstor4m[mem[(32 * [94midx) + 128]m]m.field_0m]m.field_0 = mstor5m.length + 1
                          mem[32] = 2
                          mstor2m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m.field_0++
                          mstor2m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m[mstor2m[addr(mem[(32 * [94midx) + (32 * m_param1.length) + 160])m]m.field_0m]m.field_0 = mstor5m.length + 1
                          mstor5m.length++
                          mstor5m[mstor5m.lengthm]m.field_0 = mstor5m.length + 1
                          if mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1024 <= 0:
                              mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                              mem[mem[64]] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_256
                              mem[mem[64] + 32] = addr(mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_512)
                              mem[mem[64] + 64] = mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_768 - [94m_3389
                              mem[mem[64] + 96] = mholdingm[mstor3m[mem[0]m]m[addr(m_param2)m]m]m.field_1024
                              log 0x563ecb3e: mem[mem[64] len 64], holding[stor3[mem[0]][addr(_param2)]].field_768 - _3389, holding[stor3[mem[0]][addr(_param2)]].field_1024, holding[stor3[mem[0]][addr(_param2)]].field_1280, 6, holding[stor3[mem[0]][addr(_param2)]].field_0
                              mem[32] = 1
                              mem[mem[64]] = mholdingm[mstor5m.length + 1m]m.field_256
                              mem[mem[64] + 32] = addr(mholdingm[mstor5m.length + 1m]m.field_512)
                              mem[mem[64] + 64] = mholdingm[mstor5m.length + 1m]m.field_768
                              mem[mem[64] + 96] = mholdingm[mstor5m.length + 1m]m.field_1024
                              mem[mem[64] + 128] = mholdingm[mstor5m.length + 1m]m.field_1280
                              mem[0] = mstor5m.length + 1
                              log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 6, stor5.length + 1
                          else:
                              mem[0] = mstor5m.length + 1
                              mem[32] = 1
                              if mholdingm[mstor5m.length + 1m]m.field_1024 <= 0:
                                  mholdingm[mstor5m.length + 1m]m.field_1024 = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1024
                                  mholdingm[mstor5m.length + 1m]m.field_1280 = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1280
                                  mholdingm[mstor5m.length + 1m]m.field_1024 = 0
                                  if 1 == mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_1280:
                                      require ext_code.size(addr(code.data[11131 len 32]))
                                      call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'cashsettled'
                                      require ext_call.success
                                      mem[0] = mstor5m.length + 1
                                      mem[32] = 1
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).0x43fb2310 with:
                                           gas gas_remaining - 50 wei
                                          args mholdingm[mstor5m.length + 1m]m.field_1024, mstor5m.length + 1
                                      require ext_call.success
                                      mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                      mem[mem[64] + 64] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 - mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                      log 0x563ecb3e: holding[_3394].field_0, addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                  else:
                                      mem[32] = 1
                                      if mholdingm[mstor5m.length + 1m]m.field_1280 != 2:
                                          mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                          mem[mem[64]] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_256
                                          mem[mem[64] + 64] = munknownd759e241m[[94m_3394m] - [94m_3389
                                          mem[mem[64] + 96] = mstor4m[[94m_3394m]m.field_0
                                          log 0x563ecb3e: mem[mem[64]], addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                      else:
                                          require ext_code.size(addr(code.data[11131 len 32]))
                                          call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'cashsettled'
                                          require ext_call.success
                                          mem[0] = mstor5m.length + 1
                                          mem[32] = 1
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0x173396bb with:
                                               gas gas_remaining - 50 wei
                                              args mholdingm[mstor5m.length + 1m]m.field_1024, mstor5m.length + 1
                                          require ext_call.success
                                          mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 -= mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                          mem[mem[64] + 64] = mholdingm[mstor3m[mem[(32 * [94midx) + 128]m]m[addr(m_param2)m]m]m.field_768 - mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param1.length) + 192]
                                          log 0x563ecb3e: holding[_3394].field_0, addr(stor2[_3394].field_0), unknownd759e241[_3394] - _3389, stor4[_3394].field_0, stor5[_3394].field_0, 6, stor[_3394]
                                  mem[32] = 1
                                  mem[mem[64]] = mholdingm[mstor5m.length + 1m]m.field_256
                                  mem[mem[64] + 32] = addr(mholdingm[mstor5m.length + 1m]m.field_512)
                                  mem[mem[64] + 64] = mholdingm[mstor5m.length + 1m]m.field_768
                                  mem[mem[64] + 96] = mholdingm[mstor5m.length + 1m]m.field_1024
                                  mem[mem[64] + 128] = mholdingm[mstor5m.length + 1m]m.field_1280
                                  mem[0] = mstor5m.length + 1
                                  log 0x563ecb3e: holding[stor5.length + 1].field_256, addr(holding[stor5.length + 1].field_512), holding[stor5.length + 1].field_768, holding[stor5.length + 1].field_1024, holding[stor5.length + 1].field_1280, 6, stor5.length + 1
              [94midx = [94midx + 1
              mcontinue 


# hash = 0x8b69450d
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknown8b69450d(): # not payable
  return mstor5m.length


# hash = 0xb1eb7998
# getter = None
# const = None
# payable = False
def unknownb1eb7998(uint256 m_param1, addr m_param2): # not payable
  require ext_code.size(addr(code.data[11131 len 32]))
  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args ('offerbook' << 184)
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xbd98583a with:
       gas gas_remaining - 50 wei
      args m_param1, m_param2
  require ext_call.success
  return (mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768 - ext_call.return_data[0])


# hash = 0xbae930cb
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def holding(uint256 m_blockNumber): # not payable
  return mholdingm[m_blockNumberm]m.field_0, 
         mholdingm[m_blockNumberm]m.field_256,
         addr(mholdingm[m_blockNumberm]m.field_512),
         mholdingm[m_blockNumberm]m.field_768,
         mholdingm[m_blockNumberm]m.field_1024,
         mholdingm[m_blockNumberm]m.field_1280


# hash = 0xcd22bee5
# getter = None
# const = None
# payable = False
def unknowncd22bee5(uint256 m_param1, addr m_param2, uint256 m_param3, uint8 m_param4, bool m_param5): # not payable
  require ext_code.size(addr(code.data[11131 len 32]))
  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if ext_call.return_data[12 len 20] == caller:
      [94ms = 0
      [94midx = 0
      mwhile [94midx < mstor5m.lengthm:
          mem[0] = mstor5m[[94midxm]m.field_0
          mem[32] = 1
          if mholdingm[mstor5m[[94midxm]m.field_0m]m.field_256 == m_param1:
              if not m_param5:
                  mem[0] = mstor5m[[94midxm]m.field_0
                  require ext_code.size(addr(code.data[11131 len 32]))
                  call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                       gas gas_remaining - 50 wei
                      args 'stabletoken'
                  require ext_call.success
                  mem[100] = addr(mholdingm[mstor5m[[94midxm]m.field_0m]m.field_512)
                  mem[132] = m_param2
                  mem[164] = m_param3 * mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).adminTransfer(address from, address to, uint256 value) with:
                       gas gas_remaining - 50 wei
                      args addr(mholdingm[mstor5m[[94midxm]m.field_0m]m.field_512), addr(m_param2), m_param3 * mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
                  mem[96] = ext_call.return_data[0]
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      mem[96] = m_param1
                      mem[128] = 5
                      log 0x5a29bc1d: _param1, 5, 3, addr(holding[stor5[idx].field_0].field_512)
              if 2 == m_param4:
                  mem[96] = m_param1
                  mem[128] = m_param3 * mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
                  log 0x8b36b54e: _param1, _param3 * holding[stor5[idx].field_0].field_768, 4, _param2, addr(holding[stor5[idx].field_0].field_512)
          [94ms = sha3(mstor5m[[94midxm]m.field_0, 1)
          [94midx = [94midx + 1
          mcontinue 
  else:
      if mstor0 == caller:
          [94ms = 0
          [94midx = 0
          mwhile [94midx < mstor5m.lengthm:
              mem[0] = mstor5m[[94midxm]m.field_0
              mem[32] = 1
              if mholdingm[mstor5m[[94midxm]m.field_0m]m.field_256 == m_param1:
                  if not m_param5:
                      mem[0] = mstor5m[[94midxm]m.field_0
                      require ext_code.size(addr(code.data[11131 len 32]))
                      call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                           gas gas_remaining - 50 wei
                          args 'stabletoken'
                      require ext_call.success
                      mem[100] = addr(mholdingm[mstor5m[[94midxm]m.field_0m]m.field_512)
                      mem[132] = m_param2
                      mem[164] = m_param3 * mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).adminTransfer(address from, address to, uint256 value) with:
                           gas gas_remaining - 50 wei
                          args addr(mholdingm[mstor5m[[94midxm]m.field_0m]m.field_512), addr(m_param2), m_param3 * mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
                      mem[96] = ext_call.return_data[0]
                      require ext_call.success
                      if not ext_call.return_data[0]:
                          mem[96] = m_param1
                          mem[128] = 5
                          log 0x5a29bc1d: _param1, 5, 3, addr(holding[stor5[idx].field_0].field_512)
                  if 2 == m_param4:
                      mem[96] = m_param1
                      mem[128] = m_param3 * mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
                      log 0x8b36b54e: _param1, _param3 * holding[stor5[idx].field_0].field_768, 4, _param2, addr(holding[stor5[idx].field_0].field_512)
              [94ms = sha3(mstor5m[[94midxm]m.field_0, 1)
              [94midx = [94midx + 1
              mcontinue 
      else:
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x391465cb with:
               gas gas_remaining - 50 wei
              args m_param1, caller
          require ext_call.success
          if ext_call.return_data[0]:
              [94ms = 0
              [94midx = 0
              mwhile [94midx < mstor5m.lengthm:
                  mem[0] = mstor5m[[94midxm]m.field_0
                  mem[32] = 1
                  if mholdingm[mstor5m[[94midxm]m.field_0m]m.field_256 == m_param1:
                      if not m_param5:
                          mem[0] = mstor5m[[94midxm]m.field_0
                          require ext_code.size(addr(code.data[11131 len 32]))
                          call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
                               gas gas_remaining - 50 wei
                              args 'stabletoken'
                          require ext_call.success
                          mem[100] = addr(mholdingm[mstor5m[[94midxm]m.field_0m]m.field_512)
                          mem[132] = m_param2
                          mem[164] = m_param3 * mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).adminTransfer(address from, address to, uint256 value) with:
                               gas gas_remaining - 50 wei
                              args addr(mholdingm[mstor5m[[94midxm]m.field_0m]m.field_512), addr(m_param2), m_param3 * mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
                          mem[96] = ext_call.return_data[0]
                          require ext_call.success
                          if not ext_call.return_data[0]:
                              mem[96] = m_param1
                              mem[128] = 5
                              log 0x5a29bc1d: _param1, 5, 3, addr(holding[stor5[idx].field_0].field_512)
                      if 2 == m_param4:
                          mem[96] = m_param1
                          mem[128] = m_param3 * mholdingm[mstor5m[[94midxm]m.field_0m]m.field_768
                          log 0x8b36b54e: _param1, _param3 * holding[stor5[idx].field_0].field_768, 4, _param2, addr(holding[stor5[idx].field_0].field_512)
                  [94ms = sha3(mstor5m[[94midxm]m.field_0, 1)
                  [94midx = [94midx + 1
                  mcontinue 
  return 0


# hash = 0xd295c57a
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknownd295c57a(uint256 m_param1): # not payable
  return mholdingm[m_param1m]m.field_256


# hash = 0xd759e241
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['cd', 4], 3]]]]]
# const = None
# payable = False
def unknownd759e241(uint256 m_param1, addr m_param2): # not payable
  return munknownd759e241m[m_param1m]m[addr(m_param2)m]


# hash = 0xe57d6f52
# getter = None
# const = None
# payable = False
def unknowne57d6f52(uint256 m_param1, uint256 m_param2): # not payable
  if addr(mholdingm[m_param1m]m.field_512):
      require ext_code.size(addr(code.data[11131 len 32]))
      call addr(code.data[11131 len 32]).addressOf(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 0x626f6e6400000000000000000000000000000000000000000000000000000000
      require ext_call.success
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x391465cb with:
           gas gas_remaining - 50 wei
          args mholdingm[m_param1m]m.field_256, caller
      require ext_call.success
      if ext_call.return_data[0]:
          if m_param2 >= 1:
              mholdingm[m_param1m]m.field_768 += m_param2
              log 0x563ecb3e: holding[_param1].field_256, 0, _param2 + holding[_param1].field_768, holding[_param1].field_1024, holding[_param1].field_1280, 7, holding[_param1].field_0
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).0x940589d6 with:
                   gas gas_remaining - 50 wei
                  args mholdingm[m_param1m]m.field_256, m_param2
              require ext_call.success
      else:
          if mstor0 == caller:
              if m_param2 >= 1:
                  mholdingm[m_param1m]m.field_768 += m_param2
                  log 0x563ecb3e: holding[_param1].field_256, 0, _param2 + holding[_param1].field_768, holding[_param1].field_1024, holding[_param1].field_1280, 7, holding[_param1].field_0
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x940589d6 with:
                       gas gas_remaining - 50 wei
                      args mholdingm[m_param1m]m.field_256, m_param2
                  require ext_call.success


# hash = 0xe849d4ef
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['cd', 4], 3]]]]], 1]]]]
# const = None
# payable = False
def unknowne849d4ef(uint256 m_param1, addr m_param2): # not payable
  return mholdingm[mstor3m[m_param1m]m[addr(m_param2)m]m]m.field_768


# hash = 0xe8a96b46
# getter = ['storage', 160, 0, ['add', 2, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def getHolder(uint256 m_number): # not payable
  return addr(mholdingm[m_numberm]m.field_512)


# hash = 0xec375953
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknownec375953(uint256 m_param1): # not payable
  return mholdingm[m_param1m]m.field_768


# hash = 0xf49c505f
# getter = None
# const = None
# payable = False
def unknownf49c505f(uint256 m_param1): # not payable
  mem[64] = 288
  [94ms = 96
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mstor4m[m_param1m]m.field_0m:
      require [94midx < mstor4m[m_param1m]m.field_0
      mem[0] = mstor4m[m_param1m]m[[94midxm]m.field_0
      mem[32] = 1
      [94m_14 = sha3(mstor4m[m_param1m]m[[94midxm]m.field_0, 1)
      [94m_15 = mem[64]
      mem[64] = mem[64] + 192
      mem[[94m_15] = mholdingm[mstor4m[m_param1m]m[[94midxm]m.field_0m]m.field_0
      mem[[94m_15 + 32] = mholdingm[mstor4m[m_param1m]m[[94midxm]m.field_0m]m.field_256
      mem[[94m_15 + 64] = addr(mholdingm[mstor4m[m_param1m]m[[94midxm]m.field_0m]m.field_512)
      mem[[94m_15 + 96] = mholdingm[mstor4m[m_param1m]m[[94midxm]m.field_0m]m.field_768
      mem[[94m_15 + 128] = mholdingm[mstor4m[m_param1m]m[[94midxm]m.field_0m]m.field_1024
      mem[[94m_15 + 160] = mholdingm[mstor4m[m_param1m]m[[94midxm]m.field_0m]m.field_1280
      mem[0] = m_param1
      mem[32] = 4
      [94ms = [94m_15
      [94midx = [94midx + 1
      [94ms = mholdingm[mstor4m[m_param1m]m[[94midxm]m.field_0m]m.field_768 + [94ms
      mcontinue 
  return (munknownd759e241m[[94m_14m] * mstor4m[m_param1m]m.field_0)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


