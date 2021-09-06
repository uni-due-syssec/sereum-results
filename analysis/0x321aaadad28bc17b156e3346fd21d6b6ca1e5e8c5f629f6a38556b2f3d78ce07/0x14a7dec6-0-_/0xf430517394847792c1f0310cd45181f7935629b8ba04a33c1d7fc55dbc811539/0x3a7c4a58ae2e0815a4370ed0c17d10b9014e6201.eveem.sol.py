# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x3a7c4a58Ae2E0815a4370Ed0c17d10B9014e6201 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0xff534a34': 'unknownff534a34(?)'} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    unknown1065cf73
    # storage address 2
    unknown5e8b360e
    # storage address 3
    stor3
    # storage address 4
    stor4
# hash = 0x010cd68b
# getter = None
# const = None
# payable = False
def unknown010cd68b(): # not payable
  if mstor4m.length:
      mem[160] = uint256(mstor4m.field_0)
      [94midx = 160
      [94ms = 0
      mwhile (32 * mstor4m.length) + 128 > [94midxm:
          mem[[94midx + 32] = mstor4m[[94msm]m.field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
  return Array(len=mstor4m.length, data=mem[160 len 32 * mstor4m.length])


# hash = 0x0bc689ef
# getter = None
# const = None
# payable = False
def unknown0bc689ef(uint256 m_param1): # not payable
  [94midx = 0
  mwhile [94midx < munknown5e8b360em[m_param1m]m.field_0m:
      mem[0] = munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0
      mem[32] = 1
      if munknown1065cf73m[munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0m]m.field_1024:
          if munknown1065cf73m[munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0m]m.field_1808:
              [94midx = [94midx + 1
              mcontinue 
          else:
              if munknown1065cf73m[munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0m]m.field_1792:
                  [94midx = [94midx + 1
                  mcontinue 
              else:
                  if munknown1065cf73m[munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0m]m.field_1536 < block.timestamp:
                      [94midx = [94midx + 1
                      mcontinue 
                  else:
                      if munknown1065cf73m[munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0m]m.field_768 >= 1:
                          [94midx = [94midx + 1
                          mcontinue 
                      else:
                          [94midx = [94midx + 1
                          mcontinue 
      else:
          [94midx = [94midx + 1
          mcontinue 
  return 0


# hash = 0x0dd4b27e
# getter = None
# const = None
# payable = False
def unknown0dd4b27e(uint256 m_param1, addr m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5, uint256 m_param6, addr m_param7, uint8 m_param8, uint8 m_param9): # not payable
  require ext_code.size(addr(code.data[11615 len 32]))
  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if ext_call.return_data[12 len 20] == caller:
      require ext_code.size(addr(code.data[11615 len 32]))
      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 0x637573746f6469616e0000000000000000000000000000000000000000000000
      require ext_call.success
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0xb1eb7998 with:
           gas gas_remaining - 50 wei
          args m_param1, tx.origin
      require ext_call.success
      if ext_call.return_data[0] < m_param3:
          log 0x565a29bc: _param1, 6, 3, tx.origin
      else:
          munknown1065cf73m[mstor4m.length + 1m]m.field_0 = mstor4m.length + 1
          munknown1065cf73m[mstor4m.length + 1m]m.field_256 = m_param1
          munknown1065cf73m[mstor4m.length + 1m]m.field_512 = m_param4
          munknown1065cf73m[mstor4m.length + 1m]m.field_768 = m_param3
          munknown1065cf73m[mstor4m.length + 1m]m.field_1024 = tx.origin
          munknown1065cf73m[mstor4m.length + 1m]m.field_1280 = m_param2
          munknown1065cf73m[mstor4m.length + 1m]m.field_1536 = m_param5
          munknown1065cf73m[mstor4m.length + 1m]m.field_1792 = 0
          munknown1065cf73m[mstor4m.length + 1m]m.field_1800 = 0
          munknown1065cf73m[mstor4m.length + 1m]m.field_2048 = m_param6
          munknown1065cf73m[mstor4m.length + 1m]m.field_2304 = m_param7
          munknown1065cf73m[mstor4m.length + 1m]m.field_2464 = m_param8
          munknown1065cf73m[mstor4m.length + 1m]m.field_2472 = m_param9
          mstor4m.length++
          if not mstor4m.length <= mstor4m.length + 1:
              [94midx = mstor4m.length + 1
              mwhile mstor4m.length > [94midxm:
                  mstor4m[[94midxm]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
          mstor4m[mstor4m.lengthm]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
          munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0++
          munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m[munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
          mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0++
          mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m[mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
          log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param3, 5, tx.origin, _param2
          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0
  else:
      if mstor0 == caller:
          require ext_code.size(addr(code.data[11615 len 32]))
          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
          require ext_call.success
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0xb1eb7998 with:
               gas gas_remaining - 50 wei
              args m_param1, tx.origin
          require ext_call.success
          if ext_call.return_data[0] < m_param3:
              log 0x565a29bc: _param1, 6, 3, tx.origin
          else:
              munknown1065cf73m[mstor4m.length + 1m]m.field_0 = mstor4m.length + 1
              munknown1065cf73m[mstor4m.length + 1m]m.field_256 = m_param1
              munknown1065cf73m[mstor4m.length + 1m]m.field_512 = m_param4
              munknown1065cf73m[mstor4m.length + 1m]m.field_768 = m_param3
              munknown1065cf73m[mstor4m.length + 1m]m.field_1024 = tx.origin
              munknown1065cf73m[mstor4m.length + 1m]m.field_1280 = m_param2
              munknown1065cf73m[mstor4m.length + 1m]m.field_1536 = m_param5
              munknown1065cf73m[mstor4m.length + 1m]m.field_1792 = 0
              munknown1065cf73m[mstor4m.length + 1m]m.field_1800 = 0
              munknown1065cf73m[mstor4m.length + 1m]m.field_2048 = m_param6
              munknown1065cf73m[mstor4m.length + 1m]m.field_2304 = m_param7
              munknown1065cf73m[mstor4m.length + 1m]m.field_2464 = m_param8
              munknown1065cf73m[mstor4m.length + 1m]m.field_2472 = m_param9
              mstor4m.length++
              if not mstor4m.length <= mstor4m.length + 1:
                  [94midx = mstor4m.length + 1
                  mwhile mstor4m.length > [94midxm:
                      mstor4m[[94midxm]m.field_0 = 0
                      [94midx = [94midx + 1
                      mcontinue 
              mstor4m[mstor4m.lengthm]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
              munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0++
              munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m[munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
              mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0++
              mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m[mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
              log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param3, 5, tx.origin, _param2
              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0


# hash = 0x1065cf73
# getter = ['storage', 256, 0, ['add', 8, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown1065cf73(uint256 m_param1): # not payable
  return munknown1065cf73m[m_param1m]m.field_2048


# hash = 0x14a7dec6
# getter = None
# const = None
# payable = False
def unknown14a7dec6(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5, addr m_param6, uint8 m_param7, uint8 m_param8): # not payable
  require ext_code.size(addr(code.data[11615 len 32]))
  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xb1eb7998 with:
       gas gas_remaining - 50 wei
      args m_param1, tx.origin
  require ext_call.success
  if ext_call.return_data[0] < m_param2:
      log 0x565a29bc: _param1, 6, 3, tx.origin
  else:
      munknown1065cf73m[mstor4m.length + 1m]m.field_0 = mstor4m.length + 1
      munknown1065cf73m[mstor4m.length + 1m]m.field_256 = m_param1
      munknown1065cf73m[mstor4m.length + 1m]m.field_512 = m_param3
      munknown1065cf73m[mstor4m.length + 1m]m.field_768 = m_param2
      munknown1065cf73m[mstor4m.length + 1m]m.field_1024 = tx.origin
      munknown1065cf73m[mstor4m.length + 1m]m.field_1280 = 0
      munknown1065cf73m[mstor4m.length + 1m]m.field_1536 = m_param4
      munknown1065cf73m[mstor4m.length + 1m]m.field_1792 = 0
      munknown1065cf73m[mstor4m.length + 1m]m.field_1800 = 0
      munknown1065cf73m[mstor4m.length + 1m]m.field_2048 = m_param5
      munknown1065cf73m[mstor4m.length + 1m]m.field_2304 = m_param6
      munknown1065cf73m[mstor4m.length + 1m]m.field_2464 = m_param7
      munknown1065cf73m[mstor4m.length + 1m]m.field_2472 = m_param8
      mstor4m.length++
      if not mstor4m.length <= mstor4m.length + 1:
          [94midx = mstor4m.length + 1
          mwhile mstor4m.length > [94midxm:
              mstor4m[[94midxm]m.field_0 = 0
              [94midx = [94midx + 1
              mcontinue 
      mstor4m[mstor4m.lengthm]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
      munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0++
      munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m[munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
      mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0++
      mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m[mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
      log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param2, 5, tx.origin, 0
      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0


# hash = 0x1aa3a008
# getter = None
# const = None
# payable = False
def register(): # not payable
  if mstor0 == caller:
      require ext_code.size(code.data[11615 len 32])
      call code.data[11615 len 32].register(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 'offerbook'
      require ext_call.success


# hash = 0x24f10dfc
# getter = None
# const = None
# payable = False
def unknown24f10dfc(uint256 m_param1, uint8 m_param2): # not payable
  if munknown1065cf73m[m_param1m]m.field_1024:
      if munknown1065cf73m[m_param1m]m.field_1024 == caller:
          if not munknown1065cf73m[m_param1m]m.field_1808:
              if not munknown1065cf73m[m_param1m]m.field_1792:
                  if munknown1065cf73m[m_param1m]m.field_1536 >= block.timestamp:
                      munknown1065cf73m[m_param1m]m.field_2472 = m_param2
                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if mstor0 == caller:
              if not munknown1065cf73m[m_param1m]m.field_1808:
                  if not munknown1065cf73m[m_param1m]m.field_1792:
                      if munknown1065cf73m[m_param1m]m.field_1536 >= block.timestamp:
                          munknown1065cf73m[m_param1m]m.field_2472 = m_param2
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0x26a49e37
# getter = ['storage', 256, 0, ['add', 2, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def price(uint256 m_value): # not payable
  return munknown1065cf73m[m_valuem]m.field_512


# hash = 0x364a314e
# getter = ['bool', ['storage', 8, 160, ['add', 9, ['sha3', ['data', ['cd', 4], 1]]]]]
# const = None
# payable = False
def unknown364a314e(uint256 m_param1): # not payable
  return bool(munknown1065cf73m[m_param1m]m.field_2464)


# hash = 0x3a7f8dc7
# getter = None
# const = None
# payable = False
def unknown3a7f8dc7(uint256 m_param1, addr m_param2): # not payable
  if mstor3m[m_param1m]m[addr(m_param2)m]m.field_0:
      mem[160] = mstor3m[m_param1m]m[addr(m_param2)m]m.field_0
      [94midx = 160
      [94ms = 0
      mwhile (32 * mstor3m[m_param1m]m[addr(m_param2)m]m.field_0) + 128 > [94midxm:
          mem[[94midx + 32] = mstor3m[m_param1m]m[addr(m_param2)m]m[[94msm]m.field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
  return Array(len=mstor3m[m_param1m]m[addr(m_param2)m]m.field_0, data=mem[160 len 32 * mstor3m[m_param1m]m[addr(m_param2)m]m.field_0])


# hash = 0x3bec747f
# getter = None
# const = None
# payable = False
def unknown3bec747f(uint256 m_param1): # not payable
  if munknown1065cf73m[m_param1m]m.field_1024:
      if munknown1065cf73m[m_param1m]m.field_1808:
          return 0
      else:
          if munknown1065cf73m[m_param1m]m.field_1792:
              return 0
          else:
              if munknown1065cf73m[m_param1m]m.field_1536 < block.timestamp:
                  return 0
              else:
                  if munknown1065cf73m[m_param1m]m.field_768 >= 1:
                      return 0
                  else:
                      return 0
  else:
      return 0


# hash = 0x3c481549
# getter = None
# const = None
# payable = False
def unknown3c481549(uint256 m_param1, addr m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5, uint256 m_param6, addr m_param7, uint8 m_param8, uint8 m_param9): # not payable
  require ext_code.size(addr(code.data[11615 len 32]))
  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xb1eb7998 with:
       gas gas_remaining - 50 wei
      args m_param1, tx.origin
  require ext_call.success
  if ext_call.return_data[0] < m_param3:
      log 0x565a29bc: _param1, 6, 3, tx.origin
  else:
      munknown1065cf73m[mstor4m.length + 1m]m.field_0 = mstor4m.length + 1
      munknown1065cf73m[mstor4m.length + 1m]m.field_256 = m_param1
      munknown1065cf73m[mstor4m.length + 1m]m.field_512 = m_param4
      munknown1065cf73m[mstor4m.length + 1m]m.field_768 = m_param3
      munknown1065cf73m[mstor4m.length + 1m]m.field_1024 = tx.origin
      munknown1065cf73m[mstor4m.length + 1m]m.field_1280 = m_param2
      munknown1065cf73m[mstor4m.length + 1m]m.field_1536 = m_param5
      munknown1065cf73m[mstor4m.length + 1m]m.field_1792 = 0
      munknown1065cf73m[mstor4m.length + 1m]m.field_1800 = 0
      munknown1065cf73m[mstor4m.length + 1m]m.field_2048 = m_param6
      munknown1065cf73m[mstor4m.length + 1m]m.field_2304 = m_param7
      munknown1065cf73m[mstor4m.length + 1m]m.field_2464 = m_param8
      munknown1065cf73m[mstor4m.length + 1m]m.field_2472 = m_param9
      mstor4m.length++
      if not mstor4m.length <= mstor4m.length + 1:
          [94midx = mstor4m.length + 1
          mwhile mstor4m.length > [94midxm:
              mstor4m[[94midxm]m.field_0 = 0
              [94midx = [94midx + 1
              mcontinue 
      mstor4m[mstor4m.lengthm]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
      munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0++
      munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m[munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
      mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0++
      mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m[mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
      log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param3, 5, tx.origin, _param2
      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0


# hash = 0x40e58ee5
# getter = None
# const = None
# payable = False
def cancel(uint256 m_proposalId): # not payable
  if munknown1065cf73m[m_proposalIdm]m.field_1024:
      if munknown1065cf73m[m_proposalIdm]m.field_1024 == caller:
          if not munknown1065cf73m[m_proposalIdm]m.field_1808:
              if not munknown1065cf73m[m_proposalIdm]m.field_1792:
                  if munknown1065cf73m[m_proposalIdm]m.field_1536 >= block.timestamp:
                      munknown1065cf73m[m_proposalIdm]m.field_1808 = 1
                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_256, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_512, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_768, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1024, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1280, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_0
      else:
          if mstor0 == caller:
              if not munknown1065cf73m[m_proposalIdm]m.field_1808:
                  if not munknown1065cf73m[m_proposalIdm]m.field_1792:
                      if munknown1065cf73m[m_proposalIdm]m.field_1536 >= block.timestamp:
                          munknown1065cf73m[m_proposalIdm]m.field_1808 = 1
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_256, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_512, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_768, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1024, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1280, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_0


# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  if mstor0 == caller:
      [93mselfdestruct([91mstor0[93m)


# hash = 0x4579268a
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def getOffer(uint256 m_id): # not payable
  return munknown1065cf73m[m_idm]m.field_0, 
         munknown1065cf73m[m_idm]m.field_256,
         munknown1065cf73m[m_idm]m.field_512,
         munknown1065cf73m[m_idm]m.field_768,
         munknown1065cf73m[m_idm]m.field_1024,
         munknown1065cf73m[m_idm]m.field_1280,
         munknown1065cf73m[m_idm]m.field_1536,
         bool(munknown1065cf73m[m_idm]m.field_1792),
         bool(munknown1065cf73m[m_idm]m.field_1800),
         bool(munknown1065cf73m[m_idm]m.field_1808),
         munknown1065cf73m[m_idm]m.field_2048,
         munknown1065cf73m[m_idm]m.field_2304


# hash = 0x5d8cb9fa
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def unknown5d8cb9fa(uint256 m_param1): # not payable
  [94midx = 0
  mwhile [94midx < munknown5e8b360em[m_param1m]m.field_0m:
      mem[0] = munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0
      mem[32] = 1
      if munknown1065cf73m[munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0m]m.field_1024:
          if munknown1065cf73m[munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0m]m.field_1808:
              [94midx = [94midx + 1
              mcontinue 
          else:
              if munknown1065cf73m[munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0m]m.field_1792:
                  [94midx = [94midx + 1
                  mcontinue 
              else:
                  if munknown1065cf73m[munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0m]m.field_1536 < block.timestamp:
                      [94midx = [94midx + 1
                      mcontinue 
                  else:
                      if munknown1065cf73m[munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_0m]m.field_768 >= 1:
                          [94midx = [94midx + 1
                          mcontinue 
                      else:
                          [94midx = [94midx + 1
                          mcontinue 
      else:
          [94midx = [94midx + 1
          mcontinue 
  return munknown1065cf73m[0m]m.field_0, 
         munknown1065cf73m[0m]m.field_256,
         munknown1065cf73m[0m]m.field_512,
         munknown1065cf73m[0m]m.field_768,
         munknown1065cf73m[0m]m.field_1024,
         munknown1065cf73m[0m]m.field_1280,
         munknown1065cf73m[0m]m.field_1536,
         bool(munknown1065cf73m[0m]m.field_1792),
         bool(munknown1065cf73m[0m]m.field_1800),
         bool(munknown1065cf73m[0m]m.field_1808)


# hash = 0x5e8b360e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def unknown5e8b360e(uint256 m_param1): # not payable
  return munknown5e8b360em[m_param1m]m.field_0


# hash = 0x6b16815f
# getter = None
# const = None
# payable = False
def unknown6b16815f(uint256 m_param1, uint8 m_param2): # not payable
  if munknown1065cf73m[m_param1m]m.field_1024:
      if munknown1065cf73m[m_param1m]m.field_1024 == caller:
          if not munknown1065cf73m[m_param1m]m.field_1808:
              if not munknown1065cf73m[m_param1m]m.field_1792:
                  if munknown1065cf73m[m_param1m]m.field_1536 >= block.timestamp:
                      munknown1065cf73m[m_param1m]m.field_2464 = m_param2
                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if mstor0 == caller:
              if not munknown1065cf73m[m_param1m]m.field_1808:
                  if not munknown1065cf73m[m_param1m]m.field_1792:
                      if munknown1065cf73m[m_param1m]m.field_1536 >= block.timestamp:
                          munknown1065cf73m[m_param1m]m.field_2464 = m_param2
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0x6e9960c3
# getter = None
# const = ['return', 0]
# payable = False
const getAdmin = 0


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address m_newAdmin): # not payable
  if mstor0 == caller:
      mstor0 = m_newAdmin


# hash = 0x78eec5d9
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown78eec5d9(uint256 m_param1): # not payable
  return munknown1065cf73m[m_param1m]m.field_768


# hash = 0x7fcdc744
# getter = ['bool', ['storage', 8, 168, ['add', 9, ['sha3', ['data', ['cd', 4], 1]]]]]
# const = None
# payable = False
def unknown7fcdc744(uint256 m_param1): # not payable
  return bool(munknown1065cf73m[m_param1m]m.field_2472)


# hash = 0x8052f837
# getter = None
# const = None
# payable = False
def unknown8052f837(uint256 m_param1, uint256 m_param2, addr m_param3): # not payable
  if munknown1065cf73m[m_param1m]m.field_1024:
      if munknown1065cf73m[m_param1m]m.field_1024 == caller:
          if not munknown1065cf73m[m_param1m]m.field_1808:
              if not munknown1065cf73m[m_param1m]m.field_1792:
                  if munknown1065cf73m[m_param1m]m.field_1536 >= block.timestamp:
                      if m_param2 >= 0:
                          if m_param3:
                              munknown1065cf73m[m_param1m]m.field_2048 = m_param2
                              munknown1065cf73m[m_param1m]m.field_2304 = m_param3
                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if mstor0 == caller:
              if not munknown1065cf73m[m_param1m]m.field_1808:
                  if not munknown1065cf73m[m_param1m]m.field_1792:
                      if munknown1065cf73m[m_param1m]m.field_1536 >= block.timestamp:
                          if m_param2 >= 0:
                              if m_param3:
                                  munknown1065cf73m[m_param1m]m.field_2048 = m_param2
                                  munknown1065cf73m[m_param1m]m.field_2304 = m_param3
                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0x83b9d911
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown83b9d911(uint256 m_param1): # not payable
  return munknown1065cf73m[m_param1m]m.field_256


# hash = 0x8b68b88c
# getter = None
# const = None
# payable = False
def unknown8b68b88c(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5, addr m_param6, uint8 m_param7, uint8 m_param8): # not payable
  require ext_code.size(addr(code.data[11615 len 32]))
  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if ext_call.return_data[12 len 20] == caller:
      require ext_code.size(addr(code.data[11615 len 32]))
      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 0x637573746f6469616e0000000000000000000000000000000000000000000000
      require ext_call.success
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0xb1eb7998 with:
           gas gas_remaining - 50 wei
          args m_param1, tx.origin
      require ext_call.success
      if ext_call.return_data[0] < m_param2:
          log 0x565a29bc: _param1, 6, 3, tx.origin
      else:
          munknown1065cf73m[mstor4m.length + 1m]m.field_0 = mstor4m.length + 1
          munknown1065cf73m[mstor4m.length + 1m]m.field_256 = m_param1
          munknown1065cf73m[mstor4m.length + 1m]m.field_512 = m_param3
          munknown1065cf73m[mstor4m.length + 1m]m.field_768 = m_param2
          munknown1065cf73m[mstor4m.length + 1m]m.field_1024 = tx.origin
          munknown1065cf73m[mstor4m.length + 1m]m.field_1280 = 0
          munknown1065cf73m[mstor4m.length + 1m]m.field_1536 = m_param4
          munknown1065cf73m[mstor4m.length + 1m]m.field_1792 = 0
          munknown1065cf73m[mstor4m.length + 1m]m.field_1800 = 0
          munknown1065cf73m[mstor4m.length + 1m]m.field_2048 = m_param5
          munknown1065cf73m[mstor4m.length + 1m]m.field_2304 = m_param6
          munknown1065cf73m[mstor4m.length + 1m]m.field_2464 = m_param7
          munknown1065cf73m[mstor4m.length + 1m]m.field_2472 = m_param8
          mstor4m.length++
          if not mstor4m.length <= mstor4m.length + 1:
              [94midx = mstor4m.length + 1
              mwhile mstor4m.length > [94midxm:
                  mstor4m[[94midxm]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
          mstor4m[mstor4m.lengthm]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
          munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0++
          munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m[munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
          mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0++
          mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m[mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
          log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param2, 5, tx.origin, 0
          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0
  else:
      if mstor0 == caller:
          require ext_code.size(addr(code.data[11615 len 32]))
          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
          require ext_call.success
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0xb1eb7998 with:
               gas gas_remaining - 50 wei
              args m_param1, tx.origin
          require ext_call.success
          if ext_call.return_data[0] < m_param2:
              log 0x565a29bc: _param1, 6, 3, tx.origin
          else:
              munknown1065cf73m[mstor4m.length + 1m]m.field_0 = mstor4m.length + 1
              munknown1065cf73m[mstor4m.length + 1m]m.field_256 = m_param1
              munknown1065cf73m[mstor4m.length + 1m]m.field_512 = m_param3
              munknown1065cf73m[mstor4m.length + 1m]m.field_768 = m_param2
              munknown1065cf73m[mstor4m.length + 1m]m.field_1024 = tx.origin
              munknown1065cf73m[mstor4m.length + 1m]m.field_1280 = 0
              munknown1065cf73m[mstor4m.length + 1m]m.field_1536 = m_param4
              munknown1065cf73m[mstor4m.length + 1m]m.field_1792 = 0
              munknown1065cf73m[mstor4m.length + 1m]m.field_1800 = 0
              munknown1065cf73m[mstor4m.length + 1m]m.field_2048 = m_param5
              munknown1065cf73m[mstor4m.length + 1m]m.field_2304 = m_param6
              munknown1065cf73m[mstor4m.length + 1m]m.field_2464 = m_param7
              munknown1065cf73m[mstor4m.length + 1m]m.field_2472 = m_param8
              mstor4m.length++
              if not mstor4m.length <= mstor4m.length + 1:
                  [94midx = mstor4m.length + 1
                  mwhile mstor4m.length > [94midxm:
                      mstor4m[[94midxm]m.field_0 = 0
                      [94midx = [94midx + 1
                      mcontinue 
              mstor4m[mstor4m.lengthm]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
              munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0++
              munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m[munknown5e8b360em[mstor1m[mstor4m.length + 1m]m.field_256m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
              mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0++
              mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m[mstor3m[mstor1m[mstor4m.length + 1m]m.field_256m]m[mstor1m[mstor4m.length + 1m]m.field_1024m]m.field_0m]m.field_0 = munknown1065cf73m[mstor4m.length + 1m]m.field_0
              log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param2, 5, tx.origin, 0
              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0


# hash = 0x9097548d
# getter = None
# const = None
# payable = False
def unknown9097548d(uint256 m_param1): # not payable
  return ((munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_2048) + (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512))


# hash = 0xab4797cd
# getter = None
# const = None
# payable = False
def unknownab4797cd(uint256 m_param1): # not payable
  [94ms = 0
  [94midx = 0
  [94ms = 0
  mwhile [94midx < munknown5e8b360em[m_param1m]m.field_0m:
      mem[0] = munknown5e8b360em[m_param1m]m[[94midxm]m.field_0
      mem[32] = 1
      if munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_1280:
          if munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_1280 != caller:
              [94ms = sha3(munknown5e8b360em[m_param1m]m[[94midxm]m.field_0, 1)
              [94midx = [94midx + 1
              [94ms = [94ms
              mcontinue 
      [94ms = sha3(munknown5e8b360em[m_param1m]m[[94midxm]m.field_0, 1)
      [94midx = [94midx + 1
      [94ms = [94ms + munknown1065cf73m[mstor2m[m_param1m]m[[94midxm]m.field_0m]m.field_768
      mcontinue 
  return [94ms


# hash = 0xb741e9c7
# getter = None
# const = None
# payable = False
def unknownb741e9c7(uint256 m_param1, uint256 m_param2): # not payable
  if munknown1065cf73m[m_param1m]m.field_1024:
      if munknown1065cf73m[m_param1m]m.field_1024 == caller:
          if not munknown1065cf73m[m_param1m]m.field_1808:
              if not munknown1065cf73m[m_param1m]m.field_1792:
                  if munknown1065cf73m[m_param1m]m.field_1536 >= block.timestamp:
                      if m_param2 >= 0:
                          if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                              munknown1065cf73m[m_param1m]m.field_768 = m_param2
                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                          else:
                              require ext_code.size(addr(code.data[11615 len 32]))
                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                   gas gas_remaining - 50 wei
                                  args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                              require ext_call.success
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).0xb1eb7998 with:
                                   gas gas_remaining - 50 wei
                                  args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                              require ext_call.success
                              if ext_call.return_data[0] >= m_param2 - munknown1065cf73m[m_param1m]m.field_768:
                                  munknown1065cf73m[m_param1m]m.field_768 = m_param2
                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if mstor0 == caller:
              if not munknown1065cf73m[m_param1m]m.field_1808:
                  if not munknown1065cf73m[m_param1m]m.field_1792:
                      if munknown1065cf73m[m_param1m]m.field_1536 >= block.timestamp:
                          if m_param2 >= 0:
                              if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                  munknown1065cf73m[m_param1m]m.field_768 = m_param2
                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                              else:
                                  require ext_code.size(addr(code.data[11615 len 32]))
                                  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).0xb1eb7998 with:
                                       gas gas_remaining - 50 wei
                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                  require ext_call.success
                                  if ext_call.return_data[0] >= m_param2 - munknown1065cf73m[m_param1m]m.field_768:
                                      munknown1065cf73m[m_param1m]m.field_768 = m_param2
                                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0xb8adaa11
# getter = None
# const = None
# payable = False
def reject(uint256 m_idx): # not payable
  if munknown1065cf73m[m_idxm]m.field_1280:
      if munknown1065cf73m[m_idxm]m.field_1280 == caller:
          munknown1065cf73m[m_idxm]m.field_1800 = 1
          log 0x129066a9: _idx, unknown1065cf73[_idx].field_768, 7, unknown1065cf73[_idx].field_1280, unknown1065cf73[_idx].field_1024


# hash = 0xbd98583a
# getter = None
# const = None
# payable = False
def unknownbd98583a(uint256 m_param1, addr m_param2): # not payable
  [94midx = 0
  mwhile [94midx < mstor3m[m_param1m]m[addr(m_param2)m]m.field_0m:
      mem[0] = mstor3m[m_param1m]m[addr(m_param2)m]m[[94midxm]m.field_0
      mem[32] = 1
      if munknown1065cf73m[mstor3m[m_param1m]m[addr(m_param2)m]m[[94midxm]m.field_0m]m.field_1024:
          if munknown1065cf73m[mstor3m[m_param1m]m[addr(m_param2)m]m[[94midxm]m.field_0m]m.field_1808:
              [94midx = [94midx + 1
              mcontinue 
          else:
              if munknown1065cf73m[mstor3m[m_param1m]m[addr(m_param2)m]m[[94midxm]m.field_0m]m.field_1792:
                  [94midx = [94midx + 1
                  mcontinue 
              else:
                  if munknown1065cf73m[mstor3m[m_param1m]m[addr(m_param2)m]m[[94midxm]m.field_0m]m.field_1536 < block.timestamp:
                      [94midx = [94midx + 1
                      mcontinue 
                  else:
                      if munknown1065cf73m[mstor3m[m_param1m]m[addr(m_param2)m]m[[94midxm]m.field_0m]m.field_768 >= 1:
                          [94midx = [94midx + 1
                          mcontinue 
                      else:
                          [94midx = [94midx + 1
                          mcontinue 
      else:
          [94midx = [94midx + 1
          mcontinue 
  return 0


# hash = 0xbf8712c5
# getter = None
# const = None
# payable = False
def unknownbf8712c5(uint256 m_param1): # not payable
  if munknown1065cf73m[m_param1m]m.field_1024:
      if munknown1065cf73m[m_param1m]m.field_1808:
          return 0
      else:
          if munknown1065cf73m[m_param1m]m.field_1792:
              return 0
          else:
              if munknown1065cf73m[m_param1m]m.field_1536 < block.timestamp:
                  return 0
              else:
                  if munknown1065cf73m[m_param1m]m.field_768 >= 1:
                      return 0
                  else:
                      return 0
  else:
      return 0


# hash = 0xc72196b9
# getter = None
# const = None
# payable = False
def unknownc72196b9(uint256 m_param1): # not payable
  if munknown5e8b360em[m_param1m]m.field_0:
      mem[160] = munknown5e8b360em[m_param1m]m.field_0
      [94midx = 160
      [94ms = 0
      mwhile (32 * munknown5e8b360em[m_param1m]m.field_0) + 128 > [94midxm:
          mem[[94midx + 32] = munknown5e8b360em[m_param1m]m[[94msm]m.field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
  return Array(len=munknown5e8b360em[m_param1m]m.field_0, data=mem[160 len 32 * munknown5e8b360em[m_param1m]m.field_0])


# hash = 0xc815729d
# getter = None
# const = None
# payable = True
def unknownc815729d(uint256 m_param1) payable: 
  if caller != caller:
      if mstor0 != caller:
          require ext_code.size(addr(code.data[11615 len 32]))
          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
          require ext_call.success
          if ext_call.return_data[12 len 20] != caller:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 14, caller
              return 0
  if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536:
      log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 3, caller
      return 0
  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1280:
      if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1280 != caller:
          log 0x565a29bc: unknown1065cf73[_param1].field_0, 7, 3, caller
          if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
          else:
              if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
          if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
          if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
              require ext_code.size(addr(code.data[11615 len 32]))
              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                   gas gas_remaining - 50 wei
                  args 'stabletoken'
              require ext_call.success
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                   gas gas_remaining - 50 wei
                  args caller
              require ext_call.success
              if ext_call.return_data[0] < 0:
                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                  return 0
              else:
                  return 0
          else:
              return 0
  if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
      log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
      if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
      if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
          require ext_code.size(addr(code.data[11615 len 32]))
          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 'stabletoken'
          require ext_call.success
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
               gas gas_remaining - 50 wei
              args caller
          require ext_call.success
          if ext_call.return_data[0] < 0:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
              return 0
          else:
              return 0
      else:
          return 0
  if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
      log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
      if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
      if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
          require ext_code.size(addr(code.data[11615 len 32]))
          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 'stabletoken'
          require ext_call.success
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
               gas gas_remaining - 50 wei
              args caller
          require ext_call.success
          if ext_call.return_data[0] < 0:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
              return 0
          else:
              return 0
      else:
          return 0
  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
      if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
          require ext_code.size(addr(code.data[11615 len 32]))
          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 'stabletoken'
          require ext_call.success
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
               gas gas_remaining - 50 wei
              args caller
          require ext_call.success
          if ext_call.return_data[0] < 0:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
              return 0
          else:
              return 0
      else:
          return 0
  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
      if call.value < 0:
          return 0
  else:
      require ext_code.size(addr(code.data[11615 len 32]))
      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 'stabletoken'
      require ext_call.success
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
           gas gas_remaining - 50 wei
          args caller
      require ext_call.success
      if ext_call.return_data[0] < 0:
          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
          return 0
  require ext_code.size(addr(code.data[11615 len 32]))
  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  require ext_code.size(code.data[11615 len 32])
  call code.data[11615 len 32].addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
  require ext_call.success
  if 0 > munknown1065cf73m[m_param1m]m.field_768:
      return 0
  if not munknown1065cf73m[m_param1m]m.field_2472:
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x308f16da with:
           gas gas_remaining - 50 wei
          args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, 0, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
      require ext_call.success
  else:
      if not munknown1065cf73m[m_param1m]m.field_2304:
          call munknown1065cf73m[m_param1m]m.field_1024 with:
               gas 2300 wei
          require ext_call.success
      else:
          call munknown1065cf73m[m_param1m]m.field_2304 with:
               gas 2300 wei
          require ext_call.success
          call munknown1065cf73m[m_param1m]m.field_1024 with:
               gas 2300 wei
      if call.value > munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512:
          call caller with:
             value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
               gas 2300 * is_zero(value) wei
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xedc43db5 with:
       gas gas_remaining - 50 wei
      args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, 0, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
  require ext_call.success
  require ext_call.return_data[0]
  if munknown1065cf73m[m_param1m]m.field_2464:
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x391465cb with:
           gas gas_remaining - 50 wei
          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
      require ext_call.success
      if ext_call.return_data[0]:
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x7954e911 with:
               gas gas_remaining - 50 wei
              args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, 0
          require ext_call.success
  if not munknown1065cf73m[m_param1m]m.field_768:
      munknown1065cf73m[m_param1m]m.field_1792 = 1
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x5168fe58 with:
       gas gas_remaining - 50 wei
      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
  require ext_call.success
  log 0x129066a9: unknown1065cf73[_param1].field_0, 0, 6, unknown1065cf73[_param1].field_1024, caller
  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
  return bool(ext_call.return_data[0])


# hash = 0xcc6bee54
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def unknowncc6bee54(): # not payable
  return mstor4m.length


# hash = 0xda54fcc4
# getter = None
# const = None
# payable = True
def unknownda54fcc4(uint256 m_param1, uint256 m_param2) payable: 
  if caller == caller:
      if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536:
          log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 3, caller
      else:
          if m_param2 >= 0:
              if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1280:
                  if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                      if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                      if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                          require ext_code.size(addr(code.data[11615 len 32]))
                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                               gas gas_remaining - 50 wei
                              args 'stabletoken'
                          require ext_call.success
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                               gas gas_remaining - 50 wei
                              args caller
                          require ext_call.success
                          if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                  else:
                      if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                          if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                          if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                              require ext_code.size(addr(code.data[11615 len 32]))
                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                   gas gas_remaining - 50 wei
                                  args 'stabletoken'
                              require ext_call.success
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                   gas gas_remaining - 50 wei
                                  args caller
                              require ext_call.success
                              if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                      else:
                          if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                  require ext_code.size(addr(code.data[11615 len 32]))
                                  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                  if call.value >= (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                      require ext_code.size(addr(code.data[11615 len 32]))
                                      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                      require ext_call.success
                                      require ext_code.size(code.data[11615 len 32])
                                      call code.data[11615 len 32].addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                      require ext_call.success
                                      if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                          if not munknown1065cf73m[m_param1m]m.field_2472:
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x308f16da with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                              require ext_call.success
                                          else:
                                              if not munknown1065cf73m[m_param1m]m.field_2304:
                                                  call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                     value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                       gas 2300 * is_zero(value) wei
                                                  require ext_call.success
                                              else:
                                                  call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                     value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                       gas 2300 * is_zero(value) wei
                                                  require ext_call.success
                                                  call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                     value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                       gas 2300 * is_zero(value) wei
                                              if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                  call caller with:
                                                     value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                       gas 2300 * is_zero(value) wei
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0xedc43db5 with:
                                               gas gas_remaining - 50 wei
                                              args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                          require ext_call.success
                                          require ext_call.return_data[0]
                                          if not munknown1065cf73m[m_param1m]m.field_2464:
                                              munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                          else:
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x391465cb with:
                                                   gas gas_remaining - 50 wei
                                                  args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                              require ext_call.success
                                              if not ext_call.return_data[0]:
                                                  munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x7954e911 with:
                                                       gas gas_remaining - 50 wei
                                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                  require ext_call.success
                                          if not munknown1065cf73m[m_param1m]m.field_768:
                                              munknown1065cf73m[m_param1m]m.field_1792 = 1
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0x5168fe58 with:
                                               gas gas_remaining - 50 wei
                                              args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                          require ext_call.success
                                          log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                              else:
                                  require ext_code.size(addr(code.data[11615 len 32]))
                                  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                  else:
                                      require ext_code.size(addr(code.data[11615 len 32]))
                                      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                      require ext_call.success
                                      require ext_code.size(code.data[11615 len 32])
                                      call code.data[11615 len 32].addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                      require ext_call.success
                                      if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                          if not munknown1065cf73m[m_param1m]m.field_2472:
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x308f16da with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                              require ext_call.success
                                          else:
                                              if not munknown1065cf73m[m_param1m]m.field_2304:
                                                  call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                     value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                       gas 2300 * is_zero(value) wei
                                                  require ext_call.success
                                              else:
                                                  call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                     value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                       gas 2300 * is_zero(value) wei
                                                  require ext_call.success
                                                  call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                     value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                       gas 2300 * is_zero(value) wei
                                              if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                  call caller with:
                                                     value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                       gas 2300 * is_zero(value) wei
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0xedc43db5 with:
                                               gas gas_remaining - 50 wei
                                              args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                          require ext_call.success
                                          require ext_call.return_data[0]
                                          if not munknown1065cf73m[m_param1m]m.field_2464:
                                              munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                          else:
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x391465cb with:
                                                   gas gas_remaining - 50 wei
                                                  args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                              require ext_call.success
                                              if not ext_call.return_data[0]:
                                                  munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x7954e911 with:
                                                       gas gas_remaining - 50 wei
                                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                  require ext_call.success
                                          if not munknown1065cf73m[m_param1m]m.field_768:
                                              munknown1065cf73m[m_param1m]m.field_1792 = 1
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0x5168fe58 with:
                                               gas gas_remaining - 50 wei
                                              args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                          require ext_call.success
                                          log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
              else:
                  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1280 != caller:
                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 7, 3, caller
                      if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                      else:
                          if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                      if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                      if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                          require ext_code.size(addr(code.data[11615 len 32]))
                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                               gas gas_remaining - 50 wei
                              args 'stabletoken'
                          require ext_call.success
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                               gas gas_remaining - 50 wei
                              args caller
                          require ext_call.success
                          if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                  else:
                      if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                          if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                          if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                              require ext_code.size(addr(code.data[11615 len 32]))
                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                   gas gas_remaining - 50 wei
                                  args 'stabletoken'
                              require ext_call.success
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                   gas gas_remaining - 50 wei
                                  args caller
                              require ext_call.success
                              if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                      else:
                          if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                  require ext_code.size(addr(code.data[11615 len 32]))
                                  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                  if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                      require ext_code.size(addr(code.data[11615 len 32]))
                                      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                              else:
                                  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                      if call.value >= (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                          require ext_code.size(addr(code.data[11615 len 32]))
                                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          require ext_code.size(code.data[11615 len 32])
                                          call code.data[11615 len 32].addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                              if not munknown1065cf73m[m_param1m]m.field_2472:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x308f16da with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                  require ext_call.success
                                              else:
                                                  if not munknown1065cf73m[m_param1m]m.field_2304:
                                                      call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                  else:
                                                      call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                      call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                  if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                      call caller with:
                                                         value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                           gas 2300 * is_zero(value) wei
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                              require ext_call.success
                                              require ext_call.return_data[0]
                                              if not munknown1065cf73m[m_param1m]m.field_2464:
                                                  munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x391465cb with:
                                                       gas gas_remaining - 50 wei
                                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                                  require ext_call.success
                                                  if not ext_call.return_data[0]:
                                                      munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x7954e911 with:
                                                           gas gas_remaining - 50 wei
                                                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                      require ext_call.success
                                              if not munknown1065cf73m[m_param1m]m.field_768:
                                                  munknown1065cf73m[m_param1m]m.field_1792 = 1
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                   gas gas_remaining - 50 wei
                                                  args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                              require ext_call.success
                                              log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                                  else:
                                      require ext_code.size(addr(code.data[11615 len 32]))
                                      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                      else:
                                          require ext_code.size(addr(code.data[11615 len 32]))
                                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          require ext_code.size(code.data[11615 len 32])
                                          call code.data[11615 len 32].addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                              if not munknown1065cf73m[m_param1m]m.field_2472:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x308f16da with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                  require ext_call.success
                                              else:
                                                  if not munknown1065cf73m[m_param1m]m.field_2304:
                                                      call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                  else:
                                                      call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                      call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                  if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                      call caller with:
                                                         value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                           gas 2300 * is_zero(value) wei
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                              require ext_call.success
                                              require ext_call.return_data[0]
                                              if not munknown1065cf73m[m_param1m]m.field_2464:
                                                  munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x391465cb with:
                                                       gas gas_remaining - 50 wei
                                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                                  require ext_call.success
                                                  if not ext_call.return_data[0]:
                                                      munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x7954e911 with:
                                                           gas gas_remaining - 50 wei
                                                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                      require ext_call.success
                                              if not munknown1065cf73m[m_param1m]m.field_768:
                                                  munknown1065cf73m[m_param1m]m.field_1792 = 1
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                   gas gas_remaining - 50 wei
                                                  args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                              require ext_call.success
                                              log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
  else:
      if mstor0 == caller:
          if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 3, caller
          else:
              if m_param2 >= 0:
                  if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1280:
                      if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                          if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                          if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                              require ext_code.size(addr(code.data[11615 len 32]))
                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                   gas gas_remaining - 50 wei
                                  args 'stabletoken'
                              require ext_call.success
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                   gas gas_remaining - 50 wei
                                  args caller
                              require ext_call.success
                              if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                      else:
                          if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                  require ext_code.size(addr(code.data[11615 len 32]))
                                  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                  if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                      require ext_code.size(addr(code.data[11615 len 32]))
                                      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                              else:
                                  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                      if call.value >= (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                          require ext_code.size(addr(code.data[11615 len 32]))
                                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          require ext_code.size(code.data[11615 len 32])
                                          call code.data[11615 len 32].addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                              if not munknown1065cf73m[m_param1m]m.field_2472:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x308f16da with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                  require ext_call.success
                                              else:
                                                  if not munknown1065cf73m[m_param1m]m.field_2304:
                                                      call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                  else:
                                                      call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                      call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                  if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                      call caller with:
                                                         value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                           gas 2300 * is_zero(value) wei
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                              require ext_call.success
                                              require ext_call.return_data[0]
                                              if not munknown1065cf73m[m_param1m]m.field_2464:
                                                  munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x391465cb with:
                                                       gas gas_remaining - 50 wei
                                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                                  require ext_call.success
                                                  if not ext_call.return_data[0]:
                                                      munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x7954e911 with:
                                                           gas gas_remaining - 50 wei
                                                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                      require ext_call.success
                                              if not munknown1065cf73m[m_param1m]m.field_768:
                                                  munknown1065cf73m[m_param1m]m.field_1792 = 1
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                   gas gas_remaining - 50 wei
                                                  args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                              require ext_call.success
                                              log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                                  else:
                                      require ext_code.size(addr(code.data[11615 len 32]))
                                      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                      else:
                                          require ext_code.size(addr(code.data[11615 len 32]))
                                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          require ext_code.size(code.data[11615 len 32])
                                          call code.data[11615 len 32].addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                              if not munknown1065cf73m[m_param1m]m.field_2472:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x308f16da with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                  require ext_call.success
                                              else:
                                                  if not munknown1065cf73m[m_param1m]m.field_2304:
                                                      call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                  else:
                                                      call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                      call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                         value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                  if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                      call caller with:
                                                         value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                           gas 2300 * is_zero(value) wei
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                              require ext_call.success
                                              require ext_call.return_data[0]
                                              if not munknown1065cf73m[m_param1m]m.field_2464:
                                                  munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x391465cb with:
                                                       gas gas_remaining - 50 wei
                                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                                  require ext_call.success
                                                  if not ext_call.return_data[0]:
                                                      munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x7954e911 with:
                                                           gas gas_remaining - 50 wei
                                                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                      require ext_call.success
                                              if not munknown1065cf73m[m_param1m]m.field_768:
                                                  munknown1065cf73m[m_param1m]m.field_1792 = 1
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                   gas gas_remaining - 50 wei
                                                  args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                              require ext_call.success
                                              log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                  else:
                      if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1280 != caller:
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 7, 3, caller
                          if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                          else:
                              if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                          if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                          if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                              require ext_code.size(addr(code.data[11615 len 32]))
                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                   gas gas_remaining - 50 wei
                                  args 'stabletoken'
                              require ext_call.success
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                   gas gas_remaining - 50 wei
                                  args caller
                              require ext_call.success
                              if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                      else:
                          if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                  require ext_code.size(addr(code.data[11615 len 32]))
                                  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                                  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                  if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                      require ext_code.size(addr(code.data[11615 len 32]))
                                      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                              else:
                                  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                      if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                          require ext_code.size(addr(code.data[11615 len 32]))
                                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'stabletoken'
                                          require ext_call.success
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                               gas gas_remaining - 50 wei
                                              args caller
                                          require ext_call.success
                                          if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                  else:
                                      if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                          if call.value >= (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                              require ext_code.size(addr(code.data[11615 len 32]))
                                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              require ext_code.size(code.data[11615 len 32])
                                              call code.data[11615 len 32].addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                                  if not munknown1065cf73m[m_param1m]m.field_2472:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x308f16da with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                      require ext_call.success
                                                  else:
                                                      if not munknown1065cf73m[m_param1m]m.field_2304:
                                                          call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                      else:
                                                          call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                          call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                      if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                          call caller with:
                                                             value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                               gas 2300 * is_zero(value) wei
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                  require ext_call.success
                                                  require ext_call.return_data[0]
                                                  if not munknown1065cf73m[m_param1m]m.field_2464:
                                                      munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x391465cb with:
                                                           gas gas_remaining - 50 wei
                                                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                                      require ext_call.success
                                                      if not ext_call.return_data[0]:
                                                          munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x7954e911 with:
                                                               gas gas_remaining - 50 wei
                                                              args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                          require ext_call.success
                                                  if not munknown1065cf73m[m_param1m]m.field_768:
                                                      munknown1065cf73m[m_param1m]m.field_1792 = 1
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                       gas gas_remaining - 50 wei
                                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                                  require ext_call.success
                                                  log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                                      else:
                                          require ext_code.size(addr(code.data[11615 len 32]))
                                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'stabletoken'
                                          require ext_call.success
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                               gas gas_remaining - 50 wei
                                              args caller
                                          require ext_call.success
                                          if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                          else:
                                              require ext_code.size(addr(code.data[11615 len 32]))
                                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              require ext_code.size(code.data[11615 len 32])
                                              call code.data[11615 len 32].addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                                  if not munknown1065cf73m[m_param1m]m.field_2472:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x308f16da with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                      require ext_call.success
                                                  else:
                                                      if not munknown1065cf73m[m_param1m]m.field_2304:
                                                          call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                      else:
                                                          call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                          call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                      if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                          call caller with:
                                                             value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                               gas 2300 * is_zero(value) wei
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                  require ext_call.success
                                                  require ext_call.return_data[0]
                                                  if not munknown1065cf73m[m_param1m]m.field_2464:
                                                      munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x391465cb with:
                                                           gas gas_remaining - 50 wei
                                                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                                      require ext_call.success
                                                      if not ext_call.return_data[0]:
                                                          munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x7954e911 with:
                                                               gas gas_remaining - 50 wei
                                                              args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                          require ext_call.success
                                                  if not munknown1065cf73m[m_param1m]m.field_768:
                                                      munknown1065cf73m[m_param1m]m.field_1792 = 1
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                       gas gas_remaining - 50 wei
                                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                                  require ext_call.success
                                                  log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          require ext_code.size(addr(code.data[11615 len 32]))
          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
          require ext_call.success
          if ext_call.return_data[12 len 20] != caller:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 14, caller
          else:
              if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536:
                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 3, caller
              else:
                  if m_param2 >= 0:
                      if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1280:
                          if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                  require ext_code.size(addr(code.data[11615 len 32]))
                                  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                                  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                  if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                      require ext_code.size(addr(code.data[11615 len 32]))
                                      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                              else:
                                  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                      if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                          require ext_code.size(addr(code.data[11615 len 32]))
                                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'stabletoken'
                                          require ext_call.success
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                               gas gas_remaining - 50 wei
                                              args caller
                                          require ext_call.success
                                          if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                  else:
                                      if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                          if call.value >= (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                              require ext_code.size(addr(code.data[11615 len 32]))
                                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              require ext_code.size(code.data[11615 len 32])
                                              call code.data[11615 len 32].addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                                  if not munknown1065cf73m[m_param1m]m.field_2472:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x308f16da with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                      require ext_call.success
                                                  else:
                                                      if not munknown1065cf73m[m_param1m]m.field_2304:
                                                          call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                      else:
                                                          call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                          call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                      if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                          call caller with:
                                                             value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                               gas 2300 * is_zero(value) wei
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                  require ext_call.success
                                                  require ext_call.return_data[0]
                                                  if not munknown1065cf73m[m_param1m]m.field_2464:
                                                      munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x391465cb with:
                                                           gas gas_remaining - 50 wei
                                                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                                      require ext_call.success
                                                      if not ext_call.return_data[0]:
                                                          munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x7954e911 with:
                                                               gas gas_remaining - 50 wei
                                                              args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                          require ext_call.success
                                                  if not munknown1065cf73m[m_param1m]m.field_768:
                                                      munknown1065cf73m[m_param1m]m.field_1792 = 1
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                       gas gas_remaining - 50 wei
                                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                                  require ext_call.success
                                                  log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                                      else:
                                          require ext_code.size(addr(code.data[11615 len 32]))
                                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'stabletoken'
                                          require ext_call.success
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                               gas gas_remaining - 50 wei
                                              args caller
                                          require ext_call.success
                                          if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                          else:
                                              require ext_code.size(addr(code.data[11615 len 32]))
                                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              require ext_code.size(code.data[11615 len 32])
                                              call code.data[11615 len 32].addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                                  if not munknown1065cf73m[m_param1m]m.field_2472:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x308f16da with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                      require ext_call.success
                                                  else:
                                                      if not munknown1065cf73m[m_param1m]m.field_2304:
                                                          call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                      else:
                                                          call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                          call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                             value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                      if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                          call caller with:
                                                             value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                               gas 2300 * is_zero(value) wei
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                  require ext_call.success
                                                  require ext_call.return_data[0]
                                                  if not munknown1065cf73m[m_param1m]m.field_2464:
                                                      munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x391465cb with:
                                                           gas gas_remaining - 50 wei
                                                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                                      require ext_call.success
                                                      if not ext_call.return_data[0]:
                                                          munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x7954e911 with:
                                                               gas gas_remaining - 50 wei
                                                              args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                          require ext_call.success
                                                  if not munknown1065cf73m[m_param1m]m.field_768:
                                                      munknown1065cf73m[m_param1m]m.field_1792 = 1
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                       gas gas_remaining - 50 wei
                                                      args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                                  require ext_call.success
                                                  log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                      else:
                          if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1280 != caller:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 7, 3, caller
                              if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              else:
                                  if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                  require ext_code.size(addr(code.data[11615 len 32]))
                                  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1792):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                                  if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                  if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                      require ext_code.size(addr(code.data[11615 len 32]))
                                      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                              else:
                                  if 1 == bool(munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1800):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                                      if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                      if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                          require ext_code.size(addr(code.data[11615 len 32]))
                                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'stabletoken'
                                          require ext_call.success
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                               gas gas_remaining - 50 wei
                                              args caller
                                          require ext_call.success
                                          if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                  else:
                                      if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_1536 < block.timestamp:
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                          if not munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                              require ext_code.size(addr(code.data[11615 len 32]))
                                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 'stabletoken'
                                              require ext_call.success
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                                   gas gas_remaining - 50 wei
                                                  args caller
                                              require ext_call.success
                                              if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                      else:
                                          if munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2472:
                                              if call.value >= (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                                  require ext_code.size(addr(code.data[11615 len 32]))
                                                  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                                       gas gas_remaining - 50 wei
                                                      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                                  require ext_call.success
                                                  require ext_code.size(code.data[11615 len 32])
                                                  call code.data[11615 len 32].addressOf(bytes32 name) with:
                                                       gas gas_remaining - 50 wei
                                                      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                                  require ext_call.success
                                                  if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                                      if not munknown1065cf73m[m_param1m]m.field_2472:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x308f16da with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                          require ext_call.success
                                                      else:
                                                          if not munknown1065cf73m[m_param1m]m.field_2304:
                                                              call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                                 value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                                   gas 2300 * is_zero(value) wei
                                                              require ext_call.success
                                                          else:
                                                              call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                                 value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                                   gas 2300 * is_zero(value) wei
                                                              require ext_call.success
                                                              call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                                 value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                                   gas 2300 * is_zero(value) wei
                                                          if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                              call caller with:
                                                                 value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                                   gas 2300 * is_zero(value) wei
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                      require ext_call.success
                                                      require ext_call.return_data[0]
                                                      if not munknown1065cf73m[m_param1m]m.field_2464:
                                                          munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x391465cb with:
                                                               gas gas_remaining - 50 wei
                                                              args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                                          require ext_call.success
                                                          if not ext_call.return_data[0]:
                                                              munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                          else:
                                                              require ext_code.size(addr(ext_call.return_data[0]))
                                                              call addr(ext_call.return_data[0]).0x7954e911 with:
                                                                   gas gas_remaining - 50 wei
                                                                  args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                              require ext_call.success
                                                      if not munknown1065cf73m[m_param1m]m.field_768:
                                                          munknown1065cf73m[m_param1m]m.field_1792 = 1
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                           gas gas_remaining - 50 wei
                                                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                                      require ext_call.success
                                                      log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                                          else:
                                              require ext_code.size(addr(code.data[11615 len 32]))
                                              call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 'stabletoken'
                                              require ext_call.success
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                                   gas gas_remaining - 50 wei
                                                  args caller
                                              require ext_call.success
                                              if ext_call.return_data[0] < (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_512) + (m_param2 * munknown1065cf73m[munknown1065cf73m[m_param1m]m.field_0m]m.field_2048):
                                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                              else:
                                                  require ext_code.size(addr(code.data[11615 len 32]))
                                                  call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                                                       gas gas_remaining - 50 wei
                                                      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                                  require ext_call.success
                                                  require ext_code.size(code.data[11615 len 32])
                                                  call code.data[11615 len 32].addressOf(bytes32 name) with:
                                                       gas gas_remaining - 50 wei
                                                      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                                  require ext_call.success
                                                  if m_param2 <= munknown1065cf73m[m_param1m]m.field_768:
                                                      if not munknown1065cf73m[m_param1m]m.field_2472:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x308f16da with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, 0, munknown1065cf73m[m_param1m]m.field_2304, caller, m_param2, munknown1065cf73m[m_param1m]m.field_2048, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                          require ext_call.success
                                                      else:
                                                          if not munknown1065cf73m[m_param1m]m.field_2304:
                                                              call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                                 value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                                   gas 2300 * is_zero(value) wei
                                                              require ext_call.success
                                                          else:
                                                              call munknown1065cf73m[m_param1m]m.field_2304 with:
                                                                 value m_param2 * munknown1065cf73m[m_param1m]m.field_2048 wei
                                                                   gas 2300 * is_zero(value) wei
                                                              require ext_call.success
                                                              call munknown1065cf73m[m_param1m]m.field_1024 with:
                                                                 value m_param2 * munknown1065cf73m[m_param1m]m.field_512 wei
                                                                   gas 2300 * is_zero(value) wei
                                                          if call.value > (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) + (m_param2 * munknown1065cf73m[m_param1m]m.field_2048):
                                                              call caller with:
                                                                 value call.value - (munknown1065cf73m[m_param1m]m.field_2048 * munknown1065cf73m[m_param1m]m.field_768) - (munknown1065cf73m[m_param1m]m.field_768 * munknown1065cf73m[m_param1m]m.field_512) wei
                                                                   gas 2300 * is_zero(value) wei
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, munknown1065cf73m[m_param1m]m.field_1024, caller, m_param2, munknown1065cf73m[m_param1m]m.field_512, bool(munknown1065cf73m[m_param1m]m.field_2472)
                                                      require ext_call.success
                                                      require ext_call.return_data[0]
                                                      if not munknown1065cf73m[m_param1m]m.field_2464:
                                                          munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x391465cb with:
                                                               gas gas_remaining - 50 wei
                                                              args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                                                          require ext_call.success
                                                          if not ext_call.return_data[0]:
                                                              munknown1065cf73m[m_param1m]m.field_768 -= m_param2
                                                          else:
                                                              require ext_code.size(addr(ext_call.return_data[0]))
                                                              call addr(ext_call.return_data[0]).0x7954e911 with:
                                                                   gas gas_remaining - 50 wei
                                                                  args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024, m_param2
                                                              require ext_call.success
                                                      if not munknown1065cf73m[m_param1m]m.field_768:
                                                          munknown1065cf73m[m_param1m]m.field_1792 = 1
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                           gas gas_remaining - 50 wei
                                                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_512
                                                      require ext_call.success
                                                      log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0xdbe867f8
# getter = None
# const = None
# payable = False
def unknowndbe867f8(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  if munknown1065cf73m[m_param1m]m.field_1024:
      if munknown1065cf73m[m_param1m]m.field_1024 == caller:
          if not munknown1065cf73m[m_param1m]m.field_1808:
              if not munknown1065cf73m[m_param1m]m.field_1792:
                  if munknown1065cf73m[m_param1m]m.field_1536 >= block.timestamp:
                      if m_param2 >= 0:
                          if m_param3 >= 0:
                              munknown1065cf73m[m_param1m]m.field_512 = m_param2
                              munknown1065cf73m[m_param1m]m.field_2048 = m_param3
                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if mstor0 == caller:
              if not munknown1065cf73m[m_param1m]m.field_1808:
                  if not munknown1065cf73m[m_param1m]m.field_1792:
                      if munknown1065cf73m[m_param1m]m.field_1536 >= block.timestamp:
                          if m_param2 >= 0:
                              if m_param3 >= 0:
                                  munknown1065cf73m[m_param1m]m.field_512 = m_param2
                                  munknown1065cf73m[m_param1m]m.field_2048 = m_param3
                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0xe1b56a7d
# getter = None
# const = None
# payable = False
def unknowne1b56a7d(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4): # not payable
  if munknown1065cf73m[m_param1m]m.field_1024:
      if munknown1065cf73m[m_param1m]m.field_1024 == caller:
          if not munknown1065cf73m[m_param1m]m.field_1808:
              if not munknown1065cf73m[m_param1m]m.field_1792:
                  if m_param3 <= munknown1065cf73m[m_param1m]m.field_768:
                      munknown1065cf73m[m_param1m]m.field_768 = m_param3
                      munknown1065cf73m[m_param1m]m.field_512 = m_param2
                      munknown1065cf73m[m_param1m]m.field_1536 = m_param4
                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                  else:
                      require ext_code.size(addr(code.data[11615 len 32]))
                      call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                           gas gas_remaining - 50 wei
                          args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                      require ext_call.success
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).0xb1eb7998 with:
                           gas gas_remaining - 50 wei
                          args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                      require ext_call.success
                      if ext_call.return_data[0] >= m_param3 - munknown1065cf73m[m_param1m]m.field_768:
                          munknown1065cf73m[m_param1m]m.field_768 = m_param3
                          munknown1065cf73m[m_param1m]m.field_512 = m_param2
                          munknown1065cf73m[m_param1m]m.field_1536 = m_param4
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if mstor0 == caller:
              if not munknown1065cf73m[m_param1m]m.field_1808:
                  if not munknown1065cf73m[m_param1m]m.field_1792:
                      if m_param3 <= munknown1065cf73m[m_param1m]m.field_768:
                          munknown1065cf73m[m_param1m]m.field_768 = m_param3
                          munknown1065cf73m[m_param1m]m.field_512 = m_param2
                          munknown1065cf73m[m_param1m]m.field_1536 = m_param4
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                      else:
                          require ext_code.size(addr(code.data[11615 len 32]))
                          call addr(code.data[11615 len 32]).addressOf(bytes32 name) with:
                               gas gas_remaining - 50 wei
                              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                          require ext_call.success
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).0xb1eb7998 with:
                               gas gas_remaining - 50 wei
                              args munknown1065cf73m[m_param1m]m.field_256, munknown1065cf73m[m_param1m]m.field_1024
                          require ext_call.success
                          if ext_call.return_data[0] >= m_param3 - munknown1065cf73m[m_param1m]m.field_768:
                              munknown1065cf73m[m_param1m]m.field_768 = m_param3
                              munknown1065cf73m[m_param1m]m.field_512 = m_param2
                              munknown1065cf73m[m_param1m]m.field_1536 = m_param4
                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0xf19b8273
# getter = ['bool', ['storage', 8, 0, ['add', 7, ['sha3', ['data', ['cd', 4], 1]]]]]
# const = None
# payable = False
def unknownf19b8273(uint256 m_param1): # not payable
  return bool(munknown1065cf73m[m_param1m]m.field_1792)


# hash = 0xf7d97577
# getter = None
# const = None
# payable = False
def setPrice(uint256 m_date, uint256 m_priceAtDate): # not payable
  if munknown1065cf73m[m_datem]m.field_1024:
      if munknown1065cf73m[m_datem]m.field_1024 == caller:
          if not munknown1065cf73m[m_datem]m.field_1808:
              if not munknown1065cf73m[m_datem]m.field_1792:
                  if munknown1065cf73m[m_datem]m.field_1536 >= block.timestamp:
                      if m_priceAtDate >= 0:
                          munknown1065cf73m[m_datem]m.field_512 = m_priceAtDate
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_date].field_0].field_256, unknown1065cf73[unknown1065cf73[_date].field_0].field_512, unknown1065cf73[unknown1065cf73[_date].field_0].field_768, unknown1065cf73[unknown1065cf73[_date].field_0].field_1024, unknown1065cf73[unknown1065cf73[_date].field_0].field_1280, unknown1065cf73[unknown1065cf73[_date].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_date].field_0].field_0
      else:
          if mstor0 == caller:
              if not munknown1065cf73m[m_datem]m.field_1808:
                  if not munknown1065cf73m[m_datem]m.field_1792:
                      if munknown1065cf73m[m_datem]m.field_1536 >= block.timestamp:
                          if m_priceAtDate >= 0:
                              munknown1065cf73m[m_datem]m.field_512 = m_priceAtDate
                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_date].field_0].field_256, unknown1065cf73[unknown1065cf73[_date].field_0].field_512, unknown1065cf73[unknown1065cf73[_date].field_0].field_768, unknown1065cf73[unknown1065cf73[_date].field_0].field_1024, unknown1065cf73[unknown1065cf73[_date].field_0].field_1280, unknown1065cf73[unknown1065cf73[_date].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_date].field_0].field_0


# hash = 0xffcf88fd
# getter = ['storage', 256, 0, ['add', ['cd', 36], ['sha3', ['sha3', ['data', ['cd', 4], 2]]]]]
# const = None
# payable = False
def unknownffcf88fd(uint256 m_param1, uint256 m_param2): # not payable
  require m_param2 < munknown5e8b360em[m_param1m]m.field_0
  return munknown5e8b360em[m_param1m]m[m_param2m]m.field_0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


