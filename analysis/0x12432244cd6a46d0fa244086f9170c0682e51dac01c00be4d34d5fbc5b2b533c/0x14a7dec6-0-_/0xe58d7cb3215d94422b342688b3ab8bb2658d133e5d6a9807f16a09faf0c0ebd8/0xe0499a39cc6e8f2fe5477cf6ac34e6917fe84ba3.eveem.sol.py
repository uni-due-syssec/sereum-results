# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xE0499a39Cc6e8f2fe5477cF6aC34E6917FE84Ba3 
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
  if stor4.length:
      mem[160] = uint256(stor4.field_0)
      [94midx = 160
      [94ms = 0
      while (32 * stor4.length) + 128 > [94midx:
          mem[[94midx + 32] = stor4[[94ms].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
  return Array(len=stor4.length, data=mem[160 len 32 * stor4.length])


# hash = 0x0bc689ef
# getter = None
# const = None
# payable = False
def unknown0bc689ef(uint256 _param1): # not payable
  mem[64] = 544
  mem[96] = 0
  mem[128] = 0
  mem[160] = 0
  mem[192] = 0
  mem[224] = 0
  mem[256] = 0
  mem[288] = 0
  mem[320] = 0
  mem[352] = 0
  mem[384] = 0
  mem[416] = 0
  mem[448] = 0
  mem[480] = 0
  mem[512] = 0
  [94midx = 0
  while [94midx < unknown5e8b360e[_param1].field_0:
      mem[0] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_0
      mem[32] = 1
      if unknown1065cf73[unknown1065cf73[stor2[_param1][[94midx].field_0].field_0].field_1024:
          if not unknown1065cf73[unknown1065cf73[stor2[_param1][[94midx].field_0].field_0].field_1808:
              if not unknown1065cf73[unknown1065cf73[stor2[_param1][[94midx].field_0].field_0].field_1792:
                  if unknown1065cf73[unknown1065cf73[stor2[_param1][[94midx].field_0].field_0].field_1536 >= block.timestamp:
                      if unknown1065cf73[unknown1065cf73[stor2[_param1][[94midx].field_0].field_0].field_768 >= 1:
                          require [94midx < unknown5e8b360e[_param1].field_0
                          mem[0] = unknown5e8b360e[_param1][[94midx].field_0
                          mem[32] = 1
                          if not mem[236 len 20]:
                              [94m_31 = mem[64]
                              mem[64] = mem[64] + 448
                              mem[[94m_31] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_0
                              mem[[94m_31 + 32] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_256
                              mem[[94m_31 + 64] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_512
                              mem[[94m_31 + 96] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_768
                              mem[[94m_31 + 128] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1024
                              mem[[94m_31 + 160] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1280
                              mem[[94m_31 + 192] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1536
                              mem[[94m_31 + 224] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1792)
                              mem[[94m_31 + 256] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1800)
                              mem[[94m_31 + 288] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1808)
                              mem[[94m_31 + 320] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_2048
                              mem[[94m_31 + 352] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_2304
                              mem[[94m_31 + 384] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_2464)
                              mem[[94m_31 + 416] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_2472)
                          else:
                              if unknown1065cf73[stor2[_param1][[94midx].field_0].field_512 < mem[160]:
                                  require [94midx < unknown5e8b360e[_param1].field_0
                                  mem[0] = unknown5e8b360e[_param1][[94midx].field_0
                                  mem[32] = 1
                                  [94m_34 = mem[64]
                                  mem[64] = mem[64] + 448
                                  mem[[94m_34] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_0
                                  mem[[94m_34 + 32] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_256
                                  mem[[94m_34 + 64] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_512
                                  mem[[94m_34 + 96] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_768
                                  mem[[94m_34 + 128] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1024
                                  mem[[94m_34 + 160] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1280
                                  mem[[94m_34 + 192] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1536
                                  mem[[94m_34 + 224] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1792)
                                  mem[[94m_34 + 256] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1800)
                                  mem[[94m_34 + 288] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1808)
                                  mem[[94m_34 + 320] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_2048
                                  mem[[94m_34 + 352] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_2304
                                  mem[[94m_34 + 384] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_2464)
                                  mem[[94m_34 + 416] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_2472)
      [94midx = [94midx + 1
      continue 
  mem[mem[64]] = mem[96]
  return memory
    from mem[64]
     [93mlen 32


# hash = 0x0dd4b27e
# getter = None
# const = None
# payable = False
def unknown0dd4b27e(uint256 _param1, addr _param2, uint256 _param3, uint256 _param4, uint256 _param5, uint256 _param6, addr _param7, uint8 _param8, uint8 _param9): # not payable
  require ext_code.size(addr(code.data[11619 len 32]))
  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if ext_call.return_data[12 len 20] == caller:
      require ext_code.size(addr(code.data[11619 len 32]))
      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 0x637573746f6469616e0000000000000000000000000000000000000000000000
      require ext_call.success
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0xb1eb7998 with:
           gas gas_remaining - 50 wei
          args _param1, tx.origin
      require ext_call.success
      if ext_call.return_data[0] < _param3:
          log 0x565a29bc: _param1, 6, 3, tx.origin
      else:
          unknown1065cf73[stor4.length + 1].field_0 = stor4.length + 1
          unknown1065cf73[stor4.length + 1].field_256 = _param1
          unknown1065cf73[stor4.length + 1].field_512 = _param4
          unknown1065cf73[stor4.length + 1].field_768 = _param3
          unknown1065cf73[stor4.length + 1].field_1024 = tx.origin
          unknown1065cf73[stor4.length + 1].field_1280 = _param2
          unknown1065cf73[stor4.length + 1].field_1536 = _param5
          unknown1065cf73[stor4.length + 1].field_1792 = 0
          unknown1065cf73[stor4.length + 1].field_1800 = 0
          unknown1065cf73[stor4.length + 1].field_2048 = _param6
          unknown1065cf73[stor4.length + 1].field_2304 = _param7
          unknown1065cf73[stor4.length + 1].field_2464 = _param8
          unknown1065cf73[stor4.length + 1].field_2472 = _param9
          stor4.length++
          if not stor4.length <= stor4.length + 1:
              [94midx = stor4.length + 1
              while stor4.length > [94midx:
                  stor4[[94midx].field_0 = 0
                  [94midx = [94midx + 1
                  continue 
          stor4[stor4.length].field_0 = unknown1065cf73[stor4.length + 1].field_0
          unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0++
          unknown5e8b360e[stor1[stor4.length + 1].field_256][unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
          stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0++
          stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024][stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
          log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param3, 5, tx.origin, _param2
          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0
  else:
      if stor0 == caller:
          require ext_code.size(addr(code.data[11619 len 32]))
          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
          require ext_call.success
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0xb1eb7998 with:
               gas gas_remaining - 50 wei
              args _param1, tx.origin
          require ext_call.success
          if ext_call.return_data[0] < _param3:
              log 0x565a29bc: _param1, 6, 3, tx.origin
          else:
              unknown1065cf73[stor4.length + 1].field_0 = stor4.length + 1
              unknown1065cf73[stor4.length + 1].field_256 = _param1
              unknown1065cf73[stor4.length + 1].field_512 = _param4
              unknown1065cf73[stor4.length + 1].field_768 = _param3
              unknown1065cf73[stor4.length + 1].field_1024 = tx.origin
              unknown1065cf73[stor4.length + 1].field_1280 = _param2
              unknown1065cf73[stor4.length + 1].field_1536 = _param5
              unknown1065cf73[stor4.length + 1].field_1792 = 0
              unknown1065cf73[stor4.length + 1].field_1800 = 0
              unknown1065cf73[stor4.length + 1].field_2048 = _param6
              unknown1065cf73[stor4.length + 1].field_2304 = _param7
              unknown1065cf73[stor4.length + 1].field_2464 = _param8
              unknown1065cf73[stor4.length + 1].field_2472 = _param9
              stor4.length++
              if not stor4.length <= stor4.length + 1:
                  [94midx = stor4.length + 1
                  while stor4.length > [94midx:
                      stor4[[94midx].field_0 = 0
                      [94midx = [94midx + 1
                      continue 
              stor4[stor4.length].field_0 = unknown1065cf73[stor4.length + 1].field_0
              unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0++
              unknown5e8b360e[stor1[stor4.length + 1].field_256][unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
              stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0++
              stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024][stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
              log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param3, 5, tx.origin, _param2
              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0


# hash = 0x1065cf73
# getter = ['storage', 256, 0, ['add', 8, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown1065cf73(uint256 _param1): # not payable
  return unknown1065cf73[_param1].field_2048


# hash = 0x14a7dec6
# getter = None
# const = None
# payable = False
def unknown14a7dec6(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5, addr _param6, uint8 _param7, uint8 _param8): # not payable
  require ext_code.size(addr(code.data[11619 len 32]))
  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xb1eb7998 with:
       gas gas_remaining - 50 wei
      args _param1, tx.origin
  require ext_call.success
  if ext_call.return_data[0] < _param2:
      log 0x565a29bc: _param1, 6, 3, tx.origin
  else:
      unknown1065cf73[stor4.length + 1].field_0 = stor4.length + 1
      unknown1065cf73[stor4.length + 1].field_256 = _param1
      unknown1065cf73[stor4.length + 1].field_512 = _param3
      unknown1065cf73[stor4.length + 1].field_768 = _param2
      unknown1065cf73[stor4.length + 1].field_1024 = tx.origin
      unknown1065cf73[stor4.length + 1].field_1280 = 0
      unknown1065cf73[stor4.length + 1].field_1536 = _param4
      unknown1065cf73[stor4.length + 1].field_1792 = 0
      unknown1065cf73[stor4.length + 1].field_1800 = 0
      unknown1065cf73[stor4.length + 1].field_2048 = _param5
      unknown1065cf73[stor4.length + 1].field_2304 = _param6
      unknown1065cf73[stor4.length + 1].field_2464 = _param7
      unknown1065cf73[stor4.length + 1].field_2472 = _param8
      stor4.length++
      if not stor4.length <= stor4.length + 1:
          [94midx = stor4.length + 1
          while stor4.length > [94midx:
              stor4[[94midx].field_0 = 0
              [94midx = [94midx + 1
              continue 
      stor4[stor4.length].field_0 = unknown1065cf73[stor4.length + 1].field_0
      unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0++
      unknown5e8b360e[stor1[stor4.length + 1].field_256][unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
      stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0++
      stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024][stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
      log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param2, 5, tx.origin, 0
      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0


# hash = 0x1aa3a008
# getter = None
# const = None
# payable = False
def register(): # not payable
  if stor0 == caller:
      require ext_code.size(code.data[11619 len 32])
      call code.data[11619 len 32].register(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 'offerbook'
      require ext_call.success


# hash = 0x24f10dfc
# getter = None
# const = None
# payable = False
def unknown24f10dfc(uint256 _param1, uint8 _param2): # not payable
  if unknown1065cf73[_param1].field_1024:
      if unknown1065cf73[_param1].field_1024 == caller:
          if not unknown1065cf73[_param1].field_1808:
              if not unknown1065cf73[_param1].field_1792:
                  if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                      unknown1065cf73[_param1].field_2472 = _param2
                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if stor0 == caller:
              if not unknown1065cf73[_param1].field_1808:
                  if not unknown1065cf73[_param1].field_1792:
                      if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                          unknown1065cf73[_param1].field_2472 = _param2
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0x26a49e37
# getter = ['storage', 256, 0, ['add', 2, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def price(uint256 _value): # not payable
  return unknown1065cf73[_value].field_512


# hash = 0x364a314e
# getter = ['bool', ['storage', 8, 160, ['add', 9, ['sha3', ['data', ['cd', 4], 1]]]]]
# const = None
# payable = False
def unknown364a314e(uint256 _param1): # not payable
  return bool(unknown1065cf73[_param1].field_2464)


# hash = 0x3a7f8dc7
# getter = None
# const = None
# payable = False
def unknown3a7f8dc7(uint256 _param1, addr _param2): # not payable
  if stor3[_param1][addr(_param2)].field_0:
      mem[160] = stor3[_param1][addr(_param2)].field_0
      [94midx = 160
      [94ms = 0
      while (32 * stor3[_param1][addr(_param2)].field_0) + 128 > [94midx:
          mem[[94midx + 32] = stor3[_param1][addr(_param2)][[94ms].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
  return Array(len=stor3[_param1][addr(_param2)].field_0, data=mem[160 len 32 * stor3[_param1][addr(_param2)].field_0])


# hash = 0x3bec747f
# getter = None
# const = None
# payable = False
def unknown3bec747f(uint256 _param1): # not payable
  if unknown1065cf73[_param1].field_1024:
      if not unknown1065cf73[_param1].field_1808:
          if not unknown1065cf73[_param1].field_1792:
              if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                  if unknown1065cf73[_param1].field_768 >= 1:
                      return unknown1065cf73[_param1].field_768
                  else:
                      return 0
              else:
                  return 0
          else:
              return 0
      else:
          return 0
  else:
      return 0


# hash = 0x3c481549
# getter = None
# const = None
# payable = False
def unknown3c481549(uint256 _param1, addr _param2, uint256 _param3, uint256 _param4, uint256 _param5, uint256 _param6, addr _param7, uint8 _param8, uint8 _param9): # not payable
  require ext_code.size(addr(code.data[11619 len 32]))
  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xb1eb7998 with:
       gas gas_remaining - 50 wei
      args _param1, tx.origin
  require ext_call.success
  if ext_call.return_data[0] < _param3:
      log 0x565a29bc: _param1, 6, 3, tx.origin
  else:
      unknown1065cf73[stor4.length + 1].field_0 = stor4.length + 1
      unknown1065cf73[stor4.length + 1].field_256 = _param1
      unknown1065cf73[stor4.length + 1].field_512 = _param4
      unknown1065cf73[stor4.length + 1].field_768 = _param3
      unknown1065cf73[stor4.length + 1].field_1024 = tx.origin
      unknown1065cf73[stor4.length + 1].field_1280 = _param2
      unknown1065cf73[stor4.length + 1].field_1536 = _param5
      unknown1065cf73[stor4.length + 1].field_1792 = 0
      unknown1065cf73[stor4.length + 1].field_1800 = 0
      unknown1065cf73[stor4.length + 1].field_2048 = _param6
      unknown1065cf73[stor4.length + 1].field_2304 = _param7
      unknown1065cf73[stor4.length + 1].field_2464 = _param8
      unknown1065cf73[stor4.length + 1].field_2472 = _param9
      stor4.length++
      if not stor4.length <= stor4.length + 1:
          [94midx = stor4.length + 1
          while stor4.length > [94midx:
              stor4[[94midx].field_0 = 0
              [94midx = [94midx + 1
              continue 
      stor4[stor4.length].field_0 = unknown1065cf73[stor4.length + 1].field_0
      unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0++
      unknown5e8b360e[stor1[stor4.length + 1].field_256][unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
      stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0++
      stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024][stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
      log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param3, 5, tx.origin, _param2
      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0


# hash = 0x40e58ee5
# getter = None
# const = None
# payable = False
def cancel(uint256 _proposalId): # not payable
  if unknown1065cf73[_proposalId].field_1024:
      if unknown1065cf73[_proposalId].field_1024 == caller:
          if not unknown1065cf73[_proposalId].field_1808:
              if not unknown1065cf73[_proposalId].field_1792:
                  if unknown1065cf73[_proposalId].field_1536 >= block.timestamp:
                      unknown1065cf73[_proposalId].field_1808 = 1
                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_256, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_512, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_768, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1024, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1280, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_0
      else:
          if stor0 == caller:
              if not unknown1065cf73[_proposalId].field_1808:
                  if not unknown1065cf73[_proposalId].field_1792:
                      if unknown1065cf73[_proposalId].field_1536 >= block.timestamp:
                          unknown1065cf73[_proposalId].field_1808 = 1
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_256, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_512, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_768, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1024, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1280, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_proposalId].field_0].field_0


# hash = 0x41c0e1b5
# getter = None
# const = None
# payable = False
def kill(): # not payable
  if stor0 == caller:
      [93mselfdestruct([91mstor0[93m)


# hash = 0x4579268a
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def getOffer(uint256 _id): # not payable
  return unknown1065cf73[_id].field_0, 
         unknown1065cf73[_id].field_256,
         unknown1065cf73[_id].field_512,
         unknown1065cf73[_id].field_768,
         unknown1065cf73[_id].field_1024,
         unknown1065cf73[_id].field_1280,
         unknown1065cf73[_id].field_1536,
         bool(unknown1065cf73[_id].field_1792),
         bool(unknown1065cf73[_id].field_1800),
         bool(unknown1065cf73[_id].field_1808),
         unknown1065cf73[_id].field_2048,
         unknown1065cf73[_id].field_2304


# hash = 0x5d8cb9fa
# getter = None
# const = None
# payable = False
def unknown5d8cb9fa(uint256 _param1): # not payable
  mem[64] = 544
  mem[96] = 0
  mem[128] = 0
  mem[160] = 0
  mem[192] = 0
  mem[224] = 0
  mem[256] = 0
  mem[288] = 0
  mem[320] = 0
  mem[352] = 0
  mem[384] = 0
  mem[416] = 0
  mem[448] = 0
  mem[480] = 0
  mem[512] = 0
  [94midx = 0
  while [94midx < unknown5e8b360e[_param1].field_0:
      mem[0] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_0
      mem[32] = 1
      if unknown1065cf73[unknown1065cf73[stor2[_param1][[94midx].field_0].field_0].field_1024:
          if not unknown1065cf73[unknown1065cf73[stor2[_param1][[94midx].field_0].field_0].field_1808:
              if not unknown1065cf73[unknown1065cf73[stor2[_param1][[94midx].field_0].field_0].field_1792:
                  if unknown1065cf73[unknown1065cf73[stor2[_param1][[94midx].field_0].field_0].field_1536 >= block.timestamp:
                      if unknown1065cf73[unknown1065cf73[stor2[_param1][[94midx].field_0].field_0].field_768 >= 1:
                          require [94midx < unknown5e8b360e[_param1].field_0
                          mem[0] = unknown5e8b360e[_param1][[94midx].field_0
                          mem[32] = 1
                          if not mem[236 len 20]:
                              [94m_33 = mem[64]
                              mem[64] = mem[64] + 448
                              mem[[94m_33] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_0
                              mem[[94m_33 + 32] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_256
                              mem[[94m_33 + 64] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_512
                              mem[[94m_33 + 96] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_768
                              mem[[94m_33 + 128] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1024
                              mem[[94m_33 + 160] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1280
                              mem[[94m_33 + 192] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1536
                              mem[[94m_33 + 224] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1792)
                              mem[[94m_33 + 256] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1800)
                              mem[[94m_33 + 288] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1808)
                              mem[[94m_33 + 320] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_2048
                              mem[[94m_33 + 352] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_2304
                              mem[[94m_33 + 384] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_2464)
                              mem[[94m_33 + 416] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_2472)
                          else:
                              if unknown1065cf73[stor2[_param1][[94midx].field_0].field_512 < mem[160]:
                                  require [94midx < unknown5e8b360e[_param1].field_0
                                  mem[0] = unknown5e8b360e[_param1][[94midx].field_0
                                  mem[32] = 1
                                  [94m_36 = mem[64]
                                  mem[64] = mem[64] + 448
                                  mem[[94m_36] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_0
                                  mem[[94m_36 + 32] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_256
                                  mem[[94m_36 + 64] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_512
                                  mem[[94m_36 + 96] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_768
                                  mem[[94m_36 + 128] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1024
                                  mem[[94m_36 + 160] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1280
                                  mem[[94m_36 + 192] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_1536
                                  mem[[94m_36 + 224] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1792)
                                  mem[[94m_36 + 256] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1800)
                                  mem[[94m_36 + 288] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_1808)
                                  mem[[94m_36 + 320] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_2048
                                  mem[[94m_36 + 352] = unknown1065cf73[stor2[_param1][[94midx].field_0].field_2304
                                  mem[[94m_36 + 384] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_2464)
                                  mem[[94m_36 + 416] = bool(unknown1065cf73[stor2[_param1][[94midx].field_0].field_2472)
      [94midx = [94midx + 1
      continue 
  mem[0] = mem[96]
  mem[32] = 1
  mem[mem[64]] = unknown1065cf73[mem[96]].field_0
  mem[mem[64] + 32] = unknown1065cf73[mem[0]].field_256
  mem[mem[64] + 64] = unknown1065cf73[mem[0]].field_512
  mem[mem[64] + 96] = unknown1065cf73[mem[0]].field_768
  return mem[mem[64] len 64], 
         unknown1065cf73[mem[0]].field_512,
         unknown1065cf73[mem[0]].field_768,
         unknown1065cf73[mem[0]].field_1024,
         unknown1065cf73[mem[0]].field_1280,
         unknown1065cf73[mem[0]].field_1536,
         bool(unknown1065cf73[mem[0]].field_1792),
         bool(unknown1065cf73[mem[0]].field_1800),
         bool(unknown1065cf73[mem[0]].field_1808)


# hash = 0x5e8b360e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def unknown5e8b360e(uint256 _param1): # not payable
  return unknown5e8b360e[_param1].field_0


# hash = 0x6b16815f
# getter = None
# const = None
# payable = False
def unknown6b16815f(uint256 _param1, uint8 _param2): # not payable
  if unknown1065cf73[_param1].field_1024:
      if unknown1065cf73[_param1].field_1024 == caller:
          if not unknown1065cf73[_param1].field_1808:
              if not unknown1065cf73[_param1].field_1792:
                  if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                      unknown1065cf73[_param1].field_2464 = _param2
                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if stor0 == caller:
              if not unknown1065cf73[_param1].field_1808:
                  if not unknown1065cf73[_param1].field_1792:
                      if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                          unknown1065cf73[_param1].field_2464 = _param2
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
def setAdmin(address _newAdmin): # not payable
  if stor0 == caller:
      stor0 = _newAdmin


# hash = 0x78eec5d9
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown78eec5d9(uint256 _param1): # not payable
  return unknown1065cf73[_param1].field_768


# hash = 0x7fcdc744
# getter = ['bool', ['storage', 8, 168, ['add', 9, ['sha3', ['data', ['cd', 4], 1]]]]]
# const = None
# payable = False
def unknown7fcdc744(uint256 _param1): # not payable
  return bool(unknown1065cf73[_param1].field_2472)


# hash = 0x8052f837
# getter = None
# const = None
# payable = False
def unknown8052f837(uint256 _param1, uint256 _param2, addr _param3): # not payable
  if unknown1065cf73[_param1].field_1024:
      if unknown1065cf73[_param1].field_1024 == caller:
          if not unknown1065cf73[_param1].field_1808:
              if not unknown1065cf73[_param1].field_1792:
                  if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                      if _param2 >= 0:
                          if _param3:
                              unknown1065cf73[_param1].field_2048 = _param2
                              unknown1065cf73[_param1].field_2304 = _param3
                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if stor0 == caller:
              if not unknown1065cf73[_param1].field_1808:
                  if not unknown1065cf73[_param1].field_1792:
                      if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                          if _param2 >= 0:
                              if _param3:
                                  unknown1065cf73[_param1].field_2048 = _param2
                                  unknown1065cf73[_param1].field_2304 = _param3
                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0x83b9d911
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown83b9d911(uint256 _param1): # not payable
  return unknown1065cf73[_param1].field_256


# hash = 0x8b68b88c
# getter = None
# const = None
# payable = False
def unknown8b68b88c(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5, addr _param6, uint8 _param7, uint8 _param8): # not payable
  require ext_code.size(addr(code.data[11619 len 32]))
  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  if ext_call.return_data[12 len 20] == caller:
      require ext_code.size(addr(code.data[11619 len 32]))
      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
           gas gas_remaining - 50 wei
          args 0x637573746f6469616e0000000000000000000000000000000000000000000000
      require ext_call.success
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0xb1eb7998 with:
           gas gas_remaining - 50 wei
          args _param1, tx.origin
      require ext_call.success
      if ext_call.return_data[0] < _param2:
          log 0x565a29bc: _param1, 6, 3, tx.origin
      else:
          unknown1065cf73[stor4.length + 1].field_0 = stor4.length + 1
          unknown1065cf73[stor4.length + 1].field_256 = _param1
          unknown1065cf73[stor4.length + 1].field_512 = _param3
          unknown1065cf73[stor4.length + 1].field_768 = _param2
          unknown1065cf73[stor4.length + 1].field_1024 = tx.origin
          unknown1065cf73[stor4.length + 1].field_1280 = 0
          unknown1065cf73[stor4.length + 1].field_1536 = _param4
          unknown1065cf73[stor4.length + 1].field_1792 = 0
          unknown1065cf73[stor4.length + 1].field_1800 = 0
          unknown1065cf73[stor4.length + 1].field_2048 = _param5
          unknown1065cf73[stor4.length + 1].field_2304 = _param6
          unknown1065cf73[stor4.length + 1].field_2464 = _param7
          unknown1065cf73[stor4.length + 1].field_2472 = _param8
          stor4.length++
          if not stor4.length <= stor4.length + 1:
              [94midx = stor4.length + 1
              while stor4.length > [94midx:
                  stor4[[94midx].field_0 = 0
                  [94midx = [94midx + 1
                  continue 
          stor4[stor4.length].field_0 = unknown1065cf73[stor4.length + 1].field_0
          unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0++
          unknown5e8b360e[stor1[stor4.length + 1].field_256][unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
          stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0++
          stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024][stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
          log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param2, 5, tx.origin, 0
          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0
  else:
      if stor0 == caller:
          require ext_code.size(addr(code.data[11619 len 32]))
          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
          require ext_call.success
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0xb1eb7998 with:
               gas gas_remaining - 50 wei
              args _param1, tx.origin
          require ext_call.success
          if ext_call.return_data[0] < _param2:
              log 0x565a29bc: _param1, 6, 3, tx.origin
          else:
              unknown1065cf73[stor4.length + 1].field_0 = stor4.length + 1
              unknown1065cf73[stor4.length + 1].field_256 = _param1
              unknown1065cf73[stor4.length + 1].field_512 = _param3
              unknown1065cf73[stor4.length + 1].field_768 = _param2
              unknown1065cf73[stor4.length + 1].field_1024 = tx.origin
              unknown1065cf73[stor4.length + 1].field_1280 = 0
              unknown1065cf73[stor4.length + 1].field_1536 = _param4
              unknown1065cf73[stor4.length + 1].field_1792 = 0
              unknown1065cf73[stor4.length + 1].field_1800 = 0
              unknown1065cf73[stor4.length + 1].field_2048 = _param5
              unknown1065cf73[stor4.length + 1].field_2304 = _param6
              unknown1065cf73[stor4.length + 1].field_2464 = _param7
              unknown1065cf73[stor4.length + 1].field_2472 = _param8
              stor4.length++
              if not stor4.length <= stor4.length + 1:
                  [94midx = stor4.length + 1
                  while stor4.length > [94midx:
                      stor4[[94midx].field_0 = 0
                      [94midx = [94midx + 1
                      continue 
              stor4[stor4.length].field_0 = unknown1065cf73[stor4.length + 1].field_0
              unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0++
              unknown5e8b360e[stor1[stor4.length + 1].field_256][unknown5e8b360e[stor1[stor4.length + 1].field_256].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
              stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0++
              stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024][stor3[stor1[stor4.length + 1].field_256][stor1[stor4.length + 1].field_1024].field_0].field_0 = unknown1065cf73[stor4.length + 1].field_0
              log 0x129066a9: unknown1065cf73[stor4.length + 1].field_0, _param2, 5, tx.origin, 0
              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_768, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1024, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1280, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_1808), 12, unknown1065cf73[unknown1065cf73[stor4.length + 1].field_0].field_0


# hash = 0x9097548d
# getter = None
# const = None
# payable = False
def unknown9097548d(uint256 _param1): # not payable
  return ((unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_2048) + (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512))


# hash = 0xab4797cd
# getter = None
# const = None
# payable = False
def unknownab4797cd(uint256 _param1): # not payable
  [94ms = 0
  [94midx = 0
  [94ms = 0
  while [94midx < unknown5e8b360e[_param1].field_0:
      mem[0] = unknown5e8b360e[_param1][[94midx].field_0
      mem[32] = 1
      if unknown1065cf73[stor2[_param1][[94midx].field_0].field_1280:
          if unknown1065cf73[stor2[_param1][[94midx].field_0].field_1280 != caller:
              [94ms = sha3(unknown5e8b360e[_param1][[94midx].field_0, 1)
              [94midx = [94midx + 1
              [94ms = [94ms
              continue 
      [94ms = sha3(unknown5e8b360e[_param1][[94midx].field_0, 1)
      [94midx = [94midx + 1
      [94ms = [94ms + unknown1065cf73[stor2[_param1][[94midx].field_0].field_768
      continue 
  return [94ms


# hash = 0xb741e9c7
# getter = None
# const = None
# payable = False
def unknownb741e9c7(uint256 _param1, uint256 _param2): # not payable
  if unknown1065cf73[_param1].field_1024:
      if unknown1065cf73[_param1].field_1024 == caller:
          if not unknown1065cf73[_param1].field_1808:
              if not unknown1065cf73[_param1].field_1792:
                  if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                      if _param2 >= 0:
                          if _param2 <= unknown1065cf73[_param1].field_768:
                              unknown1065cf73[_param1].field_768 = _param2
                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                          else:
                              require ext_code.size(addr(code.data[11619 len 32]))
                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                   gas gas_remaining - 50 wei
                                  args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                              require ext_call.success
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).0xb1eb7998 with:
                                   gas gas_remaining - 50 wei
                                  args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                              require ext_call.success
                              if ext_call.return_data[0] >= _param2 - unknown1065cf73[_param1].field_768:
                                  unknown1065cf73[_param1].field_768 = _param2
                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if stor0 == caller:
              if not unknown1065cf73[_param1].field_1808:
                  if not unknown1065cf73[_param1].field_1792:
                      if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                          if _param2 >= 0:
                              if _param2 <= unknown1065cf73[_param1].field_768:
                                  unknown1065cf73[_param1].field_768 = _param2
                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                              else:
                                  require ext_code.size(addr(code.data[11619 len 32]))
                                  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).0xb1eb7998 with:
                                       gas gas_remaining - 50 wei
                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                  require ext_call.success
                                  if ext_call.return_data[0] >= _param2 - unknown1065cf73[_param1].field_768:
                                      unknown1065cf73[_param1].field_768 = _param2
                                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0xb8adaa11
# getter = None
# const = None
# payable = False
def reject(uint256 _idx): # not payable
  if unknown1065cf73[_idx].field_1280:
      if unknown1065cf73[_idx].field_1280 == caller:
          unknown1065cf73[_idx].field_1800 = 1
          log 0x129066a9: _idx, unknown1065cf73[_idx].field_768, 7, unknown1065cf73[_idx].field_1280, unknown1065cf73[_idx].field_1024


# hash = 0xbd98583a
# getter = None
# const = None
# payable = False
def unknownbd98583a(uint256 _param1, addr _param2): # not payable
  [94midx = 0
  while [94midx < stor3[_param1][addr(_param2)].field_0:
      mem[0] = stor3[_param1][addr(_param2)][[94midx].field_0
      mem[32] = 1
      if unknown1065cf73[stor3[_param1][addr(_param2)][[94midx].field_0].field_1024:
          if not unknown1065cf73[stor3[_param1][addr(_param2)][[94midx].field_0].field_1808:
              if not unknown1065cf73[stor3[_param1][addr(_param2)][[94midx].field_0].field_1792:
                  if unknown1065cf73[stor3[_param1][addr(_param2)][[94midx].field_0].field_1536 >= block.timestamp:
                      if unknown1065cf73[stor3[_param1][addr(_param2)][[94midx].field_0].field_768 >= 1:
                          require [94midx < stor3[_param1][addr(_param2)].field_0
                          mem[0] = stor3[_param1][addr(_param2)][[94midx].field_0
                          mem[32] = 1
      [94midx = [94midx + 1
      continue 
  return 0


# hash = 0xbf8712c5
# getter = None
# const = None
# payable = False
def unknownbf8712c5(uint256 _param1): # not payable
  if unknown1065cf73[_param1].field_1024:
      if not unknown1065cf73[_param1].field_1808:
          if not unknown1065cf73[_param1].field_1792:
              if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                  if unknown1065cf73[_param1].field_768 >= 1:
                      return 1
                  else:
                      return 0
              else:
                  return 0
          else:
              return 0
      else:
          return 0
  else:
      return 0


# hash = 0xc72196b9
# getter = None
# const = None
# payable = False
def unknownc72196b9(uint256 _param1): # not payable
  if unknown5e8b360e[_param1].field_0:
      mem[160] = unknown5e8b360e[_param1].field_0
      [94midx = 160
      [94ms = 0
      while (32 * unknown5e8b360e[_param1].field_0) + 128 > [94midx:
          mem[[94midx + 32] = unknown5e8b360e[_param1][[94ms].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
  return Array(len=unknown5e8b360e[_param1].field_0, data=mem[160 len 32 * unknown5e8b360e[_param1].field_0])


# hash = 0xc815729d
# getter = None
# const = None
# payable = True
def unknownc815729d(uint256 _param1) payable: 
  if caller != caller:
      if stor0 != caller:
          require ext_code.size(addr(code.data[11619 len 32]))
          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
          require ext_call.success
          if ext_call.return_data[12 len 20] != caller:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 14, caller
              return 0
  if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536:
      log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 3, caller
      return 0
  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280:
      if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280 != caller:
          log 0x565a29bc: unknown1065cf73[_param1].field_0, 7, 3, caller
          if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
          else:
              if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
          if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
          if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
              require ext_code.size(addr(code.data[11619 len 32]))
              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
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
  if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
      log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
      if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
      if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
          require ext_code.size(addr(code.data[11619 len 32]))
          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
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
  if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
      log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
      if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
      if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
          require ext_code.size(addr(code.data[11619 len 32]))
          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
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
  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
      if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
          require ext_code.size(addr(code.data[11619 len 32]))
          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
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
  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
      if call.value < 0:
          return 0
  else:
      require ext_code.size(addr(code.data[11619 len 32]))
      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
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
  require ext_code.size(addr(code.data[11619 len 32]))
  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
  require ext_call.success
  require ext_code.size(code.data[11619 len 32])
  call code.data[11619 len 32].addressOf(bytes32 name) with:
       gas gas_remaining - 50 wei
      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
  require ext_call.success
  if 0 > unknown1065cf73[_param1].field_768:
      return 0
  if not unknown1065cf73[_param1].field_2472:
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x308f16da with:
           gas gas_remaining - 50 wei
          args 0, 0, unknown1065cf73[_param1].field_2304, caller, 0, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
      require ext_call.success
  else:
      if not unknown1065cf73[_param1].field_2304:
          call unknown1065cf73[_param1].field_1024 with:
               gas 2300 wei
          require ext_call.success
      else:
          call unknown1065cf73[_param1].field_2304 with:
               gas 2300 wei
          require ext_call.success
          call unknown1065cf73[_param1].field_1024 with:
               gas 2300 wei
      if call.value > unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512:
          call caller with:
             value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
               gas 2300 * is_zero(value) wei
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0xedc43db5 with:
       gas gas_remaining - 50 wei
      args 0, 0, unknown1065cf73[_param1].field_1024, caller, 0, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
  require ext_call.success
  require ext_call.return_data[0]
  if unknown1065cf73[_param1].field_2464:
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).0x391465cb with:
           gas gas_remaining - 50 wei
          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
      require ext_call.success
      if ext_call.return_data[0]:
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x7954e911 with:
               gas gas_remaining - 50 wei
              args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, 0
          require ext_call.success
  if not unknown1065cf73[_param1].field_768:
      unknown1065cf73[_param1].field_1792 = 1
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x5168fe58 with:
       gas gas_remaining - 50 wei
      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
  require ext_call.success
  log 0x129066a9: unknown1065cf73[_param1].field_0, 0, 6, unknown1065cf73[_param1].field_1024, caller
  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
  return bool(ext_call.return_data[0])


# hash = 0xcc6bee54
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def unknowncc6bee54(): # not payable
  return stor4.length


# hash = 0xda54fcc4
# getter = None
# const = None
# payable = True
def unknownda54fcc4(uint256 _param1, uint256 _param2) payable: 
  if caller == caller:
      if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536:
          log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 3, caller
      else:
          if _param2 >= 0:
              if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280:
                  if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                      if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                      if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                          require ext_code.size(addr(code.data[11619 len 32]))
                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                               gas gas_remaining - 50 wei
                              args 'stabletoken'
                          require ext_call.success
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                               gas gas_remaining - 50 wei
                              args caller
                          require ext_call.success
                          if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                  else:
                      if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                          if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                          if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                              require ext_code.size(addr(code.data[11619 len 32]))
                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                   gas gas_remaining - 50 wei
                                  args 'stabletoken'
                              require ext_call.success
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                   gas gas_remaining - 50 wei
                                  args caller
                              require ext_call.success
                              if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                      else:
                          if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                  require ext_code.size(addr(code.data[11619 len 32]))
                                  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                  if call.value >= (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                      require ext_code.size(addr(code.data[11619 len 32]))
                                      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                      require ext_call.success
                                      require ext_code.size(code.data[11619 len 32])
                                      call code.data[11619 len 32].addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                      require ext_call.success
                                      if _param2 <= unknown1065cf73[_param1].field_768:
                                          if not unknown1065cf73[_param1].field_2472:
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x308f16da with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                              require ext_call.success
                                          else:
                                              if not unknown1065cf73[_param1].field_2304:
                                                  call unknown1065cf73[_param1].field_1024 with:
                                                     value _param2 * unknown1065cf73[_param1].field_512 wei
                                                       gas 2300 * is_zero(value) wei
                                                  require ext_call.success
                                              else:
                                                  call unknown1065cf73[_param1].field_2304 with:
                                                     value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                       gas 2300 * is_zero(value) wei
                                                  require ext_call.success
                                                  call unknown1065cf73[_param1].field_1024 with:
                                                     value _param2 * unknown1065cf73[_param1].field_512 wei
                                                       gas 2300 * is_zero(value) wei
                                              if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                  call caller with:
                                                     value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                       gas 2300 * is_zero(value) wei
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0xedc43db5 with:
                                               gas gas_remaining - 50 wei
                                              args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                          require ext_call.success
                                          require ext_call.return_data[0]
                                          if not unknown1065cf73[_param1].field_2464:
                                              unknown1065cf73[_param1].field_768 -= _param2
                                          else:
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x391465cb with:
                                                   gas gas_remaining - 50 wei
                                                  args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                              require ext_call.success
                                              if not ext_call.return_data[0]:
                                                  unknown1065cf73[_param1].field_768 -= _param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x7954e911 with:
                                                       gas gas_remaining - 50 wei
                                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                  require ext_call.success
                                          if not unknown1065cf73[_param1].field_768:
                                              unknown1065cf73[_param1].field_1792 = 1
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0x5168fe58 with:
                                               gas gas_remaining - 50 wei
                                              args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                          require ext_call.success
                                          log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                              else:
                                  require ext_code.size(addr(code.data[11619 len 32]))
                                  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                  else:
                                      require ext_code.size(addr(code.data[11619 len 32]))
                                      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                      require ext_call.success
                                      require ext_code.size(code.data[11619 len 32])
                                      call code.data[11619 len 32].addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                      require ext_call.success
                                      if _param2 <= unknown1065cf73[_param1].field_768:
                                          if not unknown1065cf73[_param1].field_2472:
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x308f16da with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                              require ext_call.success
                                          else:
                                              if not unknown1065cf73[_param1].field_2304:
                                                  call unknown1065cf73[_param1].field_1024 with:
                                                     value _param2 * unknown1065cf73[_param1].field_512 wei
                                                       gas 2300 * is_zero(value) wei
                                                  require ext_call.success
                                              else:
                                                  call unknown1065cf73[_param1].field_2304 with:
                                                     value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                       gas 2300 * is_zero(value) wei
                                                  require ext_call.success
                                                  call unknown1065cf73[_param1].field_1024 with:
                                                     value _param2 * unknown1065cf73[_param1].field_512 wei
                                                       gas 2300 * is_zero(value) wei
                                              if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                  call caller with:
                                                     value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                       gas 2300 * is_zero(value) wei
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0xedc43db5 with:
                                               gas gas_remaining - 50 wei
                                              args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                          require ext_call.success
                                          require ext_call.return_data[0]
                                          if not unknown1065cf73[_param1].field_2464:
                                              unknown1065cf73[_param1].field_768 -= _param2
                                          else:
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x391465cb with:
                                                   gas gas_remaining - 50 wei
                                                  args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                              require ext_call.success
                                              if not ext_call.return_data[0]:
                                                  unknown1065cf73[_param1].field_768 -= _param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x7954e911 with:
                                                       gas gas_remaining - 50 wei
                                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                  require ext_call.success
                                          if not unknown1065cf73[_param1].field_768:
                                              unknown1065cf73[_param1].field_1792 = 1
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).0x5168fe58 with:
                                               gas gas_remaining - 50 wei
                                              args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                          require ext_call.success
                                          log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
              else:
                  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280 != caller:
                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 7, 3, caller
                      if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                      else:
                          if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                      if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                      if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                          require ext_code.size(addr(code.data[11619 len 32]))
                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                               gas gas_remaining - 50 wei
                              args 'stabletoken'
                          require ext_call.success
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                               gas gas_remaining - 50 wei
                              args caller
                          require ext_call.success
                          if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                  else:
                      if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                          if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                          if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                              require ext_code.size(addr(code.data[11619 len 32]))
                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                   gas gas_remaining - 50 wei
                                  args 'stabletoken'
                              require ext_call.success
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                   gas gas_remaining - 50 wei
                                  args caller
                              require ext_call.success
                              if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                      else:
                          if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                  require ext_code.size(addr(code.data[11619 len 32]))
                                  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                  if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                      require ext_code.size(addr(code.data[11619 len 32]))
                                      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                              else:
                                  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                      if call.value >= (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                          require ext_code.size(addr(code.data[11619 len 32]))
                                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          require ext_code.size(code.data[11619 len 32])
                                          call code.data[11619 len 32].addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          if _param2 <= unknown1065cf73[_param1].field_768:
                                              if not unknown1065cf73[_param1].field_2472:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x308f16da with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                                  require ext_call.success
                                              else:
                                                  if not unknown1065cf73[_param1].field_2304:
                                                      call unknown1065cf73[_param1].field_1024 with:
                                                         value _param2 * unknown1065cf73[_param1].field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                  else:
                                                      call unknown1065cf73[_param1].field_2304 with:
                                                         value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                      call unknown1065cf73[_param1].field_1024 with:
                                                         value _param2 * unknown1065cf73[_param1].field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                  if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                      call caller with:
                                                         value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                           gas 2300 * is_zero(value) wei
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                              require ext_call.success
                                              require ext_call.return_data[0]
                                              if not unknown1065cf73[_param1].field_2464:
                                                  unknown1065cf73[_param1].field_768 -= _param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x391465cb with:
                                                       gas gas_remaining - 50 wei
                                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                                  require ext_call.success
                                                  if not ext_call.return_data[0]:
                                                      unknown1065cf73[_param1].field_768 -= _param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x7954e911 with:
                                                           gas gas_remaining - 50 wei
                                                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                      require ext_call.success
                                              if not unknown1065cf73[_param1].field_768:
                                                  unknown1065cf73[_param1].field_1792 = 1
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                   gas gas_remaining - 50 wei
                                                  args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                              require ext_call.success
                                              log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                                  else:
                                      require ext_code.size(addr(code.data[11619 len 32]))
                                      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                      else:
                                          require ext_code.size(addr(code.data[11619 len 32]))
                                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          require ext_code.size(code.data[11619 len 32])
                                          call code.data[11619 len 32].addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          if _param2 <= unknown1065cf73[_param1].field_768:
                                              if not unknown1065cf73[_param1].field_2472:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x308f16da with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                                  require ext_call.success
                                              else:
                                                  if not unknown1065cf73[_param1].field_2304:
                                                      call unknown1065cf73[_param1].field_1024 with:
                                                         value _param2 * unknown1065cf73[_param1].field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                  else:
                                                      call unknown1065cf73[_param1].field_2304 with:
                                                         value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                      call unknown1065cf73[_param1].field_1024 with:
                                                         value _param2 * unknown1065cf73[_param1].field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                  if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                      call caller with:
                                                         value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                           gas 2300 * is_zero(value) wei
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                              require ext_call.success
                                              require ext_call.return_data[0]
                                              if not unknown1065cf73[_param1].field_2464:
                                                  unknown1065cf73[_param1].field_768 -= _param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x391465cb with:
                                                       gas gas_remaining - 50 wei
                                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                                  require ext_call.success
                                                  if not ext_call.return_data[0]:
                                                      unknown1065cf73[_param1].field_768 -= _param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x7954e911 with:
                                                           gas gas_remaining - 50 wei
                                                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                      require ext_call.success
                                              if not unknown1065cf73[_param1].field_768:
                                                  unknown1065cf73[_param1].field_1792 = 1
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                   gas gas_remaining - 50 wei
                                                  args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                              require ext_call.success
                                              log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
  else:
      if stor0 == caller:
          if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 3, caller
          else:
              if _param2 >= 0:
                  if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280:
                      if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                          if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                          if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                              require ext_code.size(addr(code.data[11619 len 32]))
                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                   gas gas_remaining - 50 wei
                                  args 'stabletoken'
                              require ext_call.success
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                   gas gas_remaining - 50 wei
                                  args caller
                              require ext_call.success
                              if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                      else:
                          if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                  require ext_code.size(addr(code.data[11619 len 32]))
                                  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                  if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                      require ext_code.size(addr(code.data[11619 len 32]))
                                      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                              else:
                                  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                      if call.value >= (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                          require ext_code.size(addr(code.data[11619 len 32]))
                                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          require ext_code.size(code.data[11619 len 32])
                                          call code.data[11619 len 32].addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          if _param2 <= unknown1065cf73[_param1].field_768:
                                              if not unknown1065cf73[_param1].field_2472:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x308f16da with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                                  require ext_call.success
                                              else:
                                                  if not unknown1065cf73[_param1].field_2304:
                                                      call unknown1065cf73[_param1].field_1024 with:
                                                         value _param2 * unknown1065cf73[_param1].field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                  else:
                                                      call unknown1065cf73[_param1].field_2304 with:
                                                         value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                      call unknown1065cf73[_param1].field_1024 with:
                                                         value _param2 * unknown1065cf73[_param1].field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                  if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                      call caller with:
                                                         value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                           gas 2300 * is_zero(value) wei
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                              require ext_call.success
                                              require ext_call.return_data[0]
                                              if not unknown1065cf73[_param1].field_2464:
                                                  unknown1065cf73[_param1].field_768 -= _param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x391465cb with:
                                                       gas gas_remaining - 50 wei
                                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                                  require ext_call.success
                                                  if not ext_call.return_data[0]:
                                                      unknown1065cf73[_param1].field_768 -= _param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x7954e911 with:
                                                           gas gas_remaining - 50 wei
                                                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                      require ext_call.success
                                              if not unknown1065cf73[_param1].field_768:
                                                  unknown1065cf73[_param1].field_1792 = 1
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                   gas gas_remaining - 50 wei
                                                  args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                              require ext_call.success
                                              log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                                  else:
                                      require ext_code.size(addr(code.data[11619 len 32]))
                                      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                      else:
                                          require ext_code.size(addr(code.data[11619 len 32]))
                                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          require ext_code.size(code.data[11619 len 32])
                                          call code.data[11619 len 32].addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                          require ext_call.success
                                          if _param2 <= unknown1065cf73[_param1].field_768:
                                              if not unknown1065cf73[_param1].field_2472:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x308f16da with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                                  require ext_call.success
                                              else:
                                                  if not unknown1065cf73[_param1].field_2304:
                                                      call unknown1065cf73[_param1].field_1024 with:
                                                         value _param2 * unknown1065cf73[_param1].field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                  else:
                                                      call unknown1065cf73[_param1].field_2304 with:
                                                         value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                           gas 2300 * is_zero(value) wei
                                                      require ext_call.success
                                                      call unknown1065cf73[_param1].field_1024 with:
                                                         value _param2 * unknown1065cf73[_param1].field_512 wei
                                                           gas 2300 * is_zero(value) wei
                                                  if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                      call caller with:
                                                         value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                           gas 2300 * is_zero(value) wei
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                              require ext_call.success
                                              require ext_call.return_data[0]
                                              if not unknown1065cf73[_param1].field_2464:
                                                  unknown1065cf73[_param1].field_768 -= _param2
                                              else:
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x391465cb with:
                                                       gas gas_remaining - 50 wei
                                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                                  require ext_call.success
                                                  if not ext_call.return_data[0]:
                                                      unknown1065cf73[_param1].field_768 -= _param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x7954e911 with:
                                                           gas gas_remaining - 50 wei
                                                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                      require ext_call.success
                                              if not unknown1065cf73[_param1].field_768:
                                                  unknown1065cf73[_param1].field_1792 = 1
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                   gas gas_remaining - 50 wei
                                                  args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                              require ext_call.success
                                              log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                  else:
                      if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280 != caller:
                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 7, 3, caller
                          if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                          else:
                              if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                          if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                          if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                              require ext_code.size(addr(code.data[11619 len 32]))
                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                   gas gas_remaining - 50 wei
                                  args 'stabletoken'
                              require ext_call.success
                              require ext_code.size(addr(ext_call.return_data[0]))
                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                   gas gas_remaining - 50 wei
                                  args caller
                              require ext_call.success
                              if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                      else:
                          if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                  require ext_code.size(addr(code.data[11619 len 32]))
                                  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                                  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                  if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                      require ext_code.size(addr(code.data[11619 len 32]))
                                      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                              else:
                                  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                      if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                          require ext_code.size(addr(code.data[11619 len 32]))
                                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'stabletoken'
                                          require ext_call.success
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                               gas gas_remaining - 50 wei
                                              args caller
                                          require ext_call.success
                                          if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                  else:
                                      if unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                          if call.value >= (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                              require ext_code.size(addr(code.data[11619 len 32]))
                                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              require ext_code.size(code.data[11619 len 32])
                                              call code.data[11619 len 32].addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              if _param2 <= unknown1065cf73[_param1].field_768:
                                                  if not unknown1065cf73[_param1].field_2472:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x308f16da with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                                      require ext_call.success
                                                  else:
                                                      if not unknown1065cf73[_param1].field_2304:
                                                          call unknown1065cf73[_param1].field_1024 with:
                                                             value _param2 * unknown1065cf73[_param1].field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                      else:
                                                          call unknown1065cf73[_param1].field_2304 with:
                                                             value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                          call unknown1065cf73[_param1].field_1024 with:
                                                             value _param2 * unknown1065cf73[_param1].field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                      if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                          call caller with:
                                                             value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                               gas 2300 * is_zero(value) wei
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                                  require ext_call.success
                                                  require ext_call.return_data[0]
                                                  if not unknown1065cf73[_param1].field_2464:
                                                      unknown1065cf73[_param1].field_768 -= _param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x391465cb with:
                                                           gas gas_remaining - 50 wei
                                                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                                      require ext_call.success
                                                      if not ext_call.return_data[0]:
                                                          unknown1065cf73[_param1].field_768 -= _param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x7954e911 with:
                                                               gas gas_remaining - 50 wei
                                                              args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                          require ext_call.success
                                                  if not unknown1065cf73[_param1].field_768:
                                                      unknown1065cf73[_param1].field_1792 = 1
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                       gas gas_remaining - 50 wei
                                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                                  require ext_call.success
                                                  log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                                      else:
                                          require ext_code.size(addr(code.data[11619 len 32]))
                                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'stabletoken'
                                          require ext_call.success
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                               gas gas_remaining - 50 wei
                                              args caller
                                          require ext_call.success
                                          if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                          else:
                                              require ext_code.size(addr(code.data[11619 len 32]))
                                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              require ext_code.size(code.data[11619 len 32])
                                              call code.data[11619 len 32].addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              if _param2 <= unknown1065cf73[_param1].field_768:
                                                  if not unknown1065cf73[_param1].field_2472:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x308f16da with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                                      require ext_call.success
                                                  else:
                                                      if not unknown1065cf73[_param1].field_2304:
                                                          call unknown1065cf73[_param1].field_1024 with:
                                                             value _param2 * unknown1065cf73[_param1].field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                      else:
                                                          call unknown1065cf73[_param1].field_2304 with:
                                                             value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                          call unknown1065cf73[_param1].field_1024 with:
                                                             value _param2 * unknown1065cf73[_param1].field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                      if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                          call caller with:
                                                             value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                               gas 2300 * is_zero(value) wei
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                                  require ext_call.success
                                                  require ext_call.return_data[0]
                                                  if not unknown1065cf73[_param1].field_2464:
                                                      unknown1065cf73[_param1].field_768 -= _param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x391465cb with:
                                                           gas gas_remaining - 50 wei
                                                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                                      require ext_call.success
                                                      if not ext_call.return_data[0]:
                                                          unknown1065cf73[_param1].field_768 -= _param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x7954e911 with:
                                                               gas gas_remaining - 50 wei
                                                              args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                          require ext_call.success
                                                  if not unknown1065cf73[_param1].field_768:
                                                      unknown1065cf73[_param1].field_1792 = 1
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                       gas gas_remaining - 50 wei
                                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                                  require ext_call.success
                                                  log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          require ext_code.size(addr(code.data[11619 len 32]))
          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
               gas gas_remaining - 50 wei
              args 0x626f6e6400000000000000000000000000000000000000000000000000000000
          require ext_call.success
          if ext_call.return_data[12 len 20] != caller:
              log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 14, caller
          else:
              if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536:
                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 11, 3, caller
              else:
                  if _param2 >= 0:
                      if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280:
                          if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                  require ext_code.size(addr(code.data[11619 len 32]))
                                  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                                  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                  if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                      require ext_code.size(addr(code.data[11619 len 32]))
                                      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                              else:
                                  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                      if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                          require ext_code.size(addr(code.data[11619 len 32]))
                                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'stabletoken'
                                          require ext_call.success
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                               gas gas_remaining - 50 wei
                                              args caller
                                          require ext_call.success
                                          if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                  else:
                                      if unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                          if call.value >= (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                              require ext_code.size(addr(code.data[11619 len 32]))
                                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              require ext_code.size(code.data[11619 len 32])
                                              call code.data[11619 len 32].addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              if _param2 <= unknown1065cf73[_param1].field_768:
                                                  if not unknown1065cf73[_param1].field_2472:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x308f16da with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                                      require ext_call.success
                                                  else:
                                                      if not unknown1065cf73[_param1].field_2304:
                                                          call unknown1065cf73[_param1].field_1024 with:
                                                             value _param2 * unknown1065cf73[_param1].field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                      else:
                                                          call unknown1065cf73[_param1].field_2304 with:
                                                             value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                          call unknown1065cf73[_param1].field_1024 with:
                                                             value _param2 * unknown1065cf73[_param1].field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                      if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                          call caller with:
                                                             value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                               gas 2300 * is_zero(value) wei
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                                  require ext_call.success
                                                  require ext_call.return_data[0]
                                                  if not unknown1065cf73[_param1].field_2464:
                                                      unknown1065cf73[_param1].field_768 -= _param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x391465cb with:
                                                           gas gas_remaining - 50 wei
                                                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                                      require ext_call.success
                                                      if not ext_call.return_data[0]:
                                                          unknown1065cf73[_param1].field_768 -= _param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x7954e911 with:
                                                               gas gas_remaining - 50 wei
                                                              args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                          require ext_call.success
                                                  if not unknown1065cf73[_param1].field_768:
                                                      unknown1065cf73[_param1].field_1792 = 1
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                       gas gas_remaining - 50 wei
                                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                                  require ext_call.success
                                                  log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                                      else:
                                          require ext_code.size(addr(code.data[11619 len 32]))
                                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'stabletoken'
                                          require ext_call.success
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                               gas gas_remaining - 50 wei
                                              args caller
                                          require ext_call.success
                                          if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                          else:
                                              require ext_code.size(addr(code.data[11619 len 32]))
                                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              require ext_code.size(code.data[11619 len 32])
                                              call code.data[11619 len 32].addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                              require ext_call.success
                                              if _param2 <= unknown1065cf73[_param1].field_768:
                                                  if not unknown1065cf73[_param1].field_2472:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x308f16da with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                                      require ext_call.success
                                                  else:
                                                      if not unknown1065cf73[_param1].field_2304:
                                                          call unknown1065cf73[_param1].field_1024 with:
                                                             value _param2 * unknown1065cf73[_param1].field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                      else:
                                                          call unknown1065cf73[_param1].field_2304 with:
                                                             value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                               gas 2300 * is_zero(value) wei
                                                          require ext_call.success
                                                          call unknown1065cf73[_param1].field_1024 with:
                                                             value _param2 * unknown1065cf73[_param1].field_512 wei
                                                               gas 2300 * is_zero(value) wei
                                                      if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                          call caller with:
                                                             value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                               gas 2300 * is_zero(value) wei
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                                  require ext_call.success
                                                  require ext_call.return_data[0]
                                                  if not unknown1065cf73[_param1].field_2464:
                                                      unknown1065cf73[_param1].field_768 -= _param2
                                                  else:
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x391465cb with:
                                                           gas gas_remaining - 50 wei
                                                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                                      require ext_call.success
                                                      if not ext_call.return_data[0]:
                                                          unknown1065cf73[_param1].field_768 -= _param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x7954e911 with:
                                                               gas gas_remaining - 50 wei
                                                              args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                          require ext_call.success
                                                  if not unknown1065cf73[_param1].field_768:
                                                      unknown1065cf73[_param1].field_1792 = 1
                                                  require ext_code.size(addr(ext_call.return_data[0]))
                                                  call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                       gas gas_remaining - 50 wei
                                                      args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                                  require ext_call.success
                                                  log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                      else:
                          if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280 != caller:
                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 7, 3, caller
                              if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              else:
                                  if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                              if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                              if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                  require ext_code.size(addr(code.data[11619 len 32]))
                                  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                       gas gas_remaining - 50 wei
                                      args 'stabletoken'
                                  require ext_call.success
                                  require ext_code.size(addr(ext_call.return_data[0]))
                                  call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                       gas gas_remaining - 50 wei
                                      args caller
                                  require ext_call.success
                                  if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                          else:
                              if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792):
                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                                  if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                  if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                      require ext_code.size(addr(code.data[11619 len 32]))
                                      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                           gas gas_remaining - 50 wei
                                          args 'stabletoken'
                                      require ext_call.success
                                      require ext_code.size(addr(ext_call.return_data[0]))
                                      call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                           gas gas_remaining - 50 wei
                                          args caller
                                      require ext_call.success
                                      if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                              else:
                                  if 1 == bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800):
                                      log 0x565a29bc: unknown1065cf73[_param1].field_0, 8, 3, caller
                                      if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                      if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                          require ext_code.size(addr(code.data[11619 len 32]))
                                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                               gas gas_remaining - 50 wei
                                              args 'stabletoken'
                                          require ext_call.success
                                          require ext_code.size(addr(ext_call.return_data[0]))
                                          call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                               gas gas_remaining - 50 wei
                                              args caller
                                          require ext_call.success
                                          if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                              log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                  else:
                                      if unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536 < block.timestamp:
                                          log 0x565a29bc: unknown1065cf73[_param1].field_0, 9, 3, caller
                                          if not unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                              require ext_code.size(addr(code.data[11619 len 32]))
                                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 'stabletoken'
                                              require ext_call.success
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                                   gas gas_remaining - 50 wei
                                                  args caller
                                              require ext_call.success
                                              if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                      else:
                                          if unknown1065cf73[unknown1065cf73[_param1].field_0].field_2472:
                                              if call.value >= (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                                  require ext_code.size(addr(code.data[11619 len 32]))
                                                  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                                       gas gas_remaining - 50 wei
                                                      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                                  require ext_call.success
                                                  require ext_code.size(code.data[11619 len 32])
                                                  call code.data[11619 len 32].addressOf(bytes32 name) with:
                                                       gas gas_remaining - 50 wei
                                                      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                                  require ext_call.success
                                                  if _param2 <= unknown1065cf73[_param1].field_768:
                                                      if not unknown1065cf73[_param1].field_2472:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x308f16da with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                                          require ext_call.success
                                                      else:
                                                          if not unknown1065cf73[_param1].field_2304:
                                                              call unknown1065cf73[_param1].field_1024 with:
                                                                 value _param2 * unknown1065cf73[_param1].field_512 wei
                                                                   gas 2300 * is_zero(value) wei
                                                              require ext_call.success
                                                          else:
                                                              call unknown1065cf73[_param1].field_2304 with:
                                                                 value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                                   gas 2300 * is_zero(value) wei
                                                              require ext_call.success
                                                              call unknown1065cf73[_param1].field_1024 with:
                                                                 value _param2 * unknown1065cf73[_param1].field_512 wei
                                                                   gas 2300 * is_zero(value) wei
                                                          if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                              call caller with:
                                                                 value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                                   gas 2300 * is_zero(value) wei
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                                      require ext_call.success
                                                      require ext_call.return_data[0]
                                                      if not unknown1065cf73[_param1].field_2464:
                                                          unknown1065cf73[_param1].field_768 -= _param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x391465cb with:
                                                               gas gas_remaining - 50 wei
                                                              args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                                          require ext_call.success
                                                          if not ext_call.return_data[0]:
                                                              unknown1065cf73[_param1].field_768 -= _param2
                                                          else:
                                                              require ext_code.size(addr(ext_call.return_data[0]))
                                                              call addr(ext_call.return_data[0]).0x7954e911 with:
                                                                   gas gas_remaining - 50 wei
                                                                  args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                              require ext_call.success
                                                      if not unknown1065cf73[_param1].field_768:
                                                          unknown1065cf73[_param1].field_1792 = 1
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                           gas gas_remaining - 50 wei
                                                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                                      require ext_call.success
                                                      log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                                          else:
                                              require ext_code.size(addr(code.data[11619 len 32]))
                                              call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                                   gas gas_remaining - 50 wei
                                                  args 'stabletoken'
                                              require ext_call.success
                                              require ext_code.size(addr(ext_call.return_data[0]))
                                              call addr(ext_call.return_data[0]).getBalance(address addressToCheck) with:
                                                   gas gas_remaining - 50 wei
                                                  args caller
                                              require ext_call.success
                                              if ext_call.return_data[0] < (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_512) + (_param2 * unknown1065cf73[unknown1065cf73[_param1].field_0].field_2048):
                                                  log 0x565a29bc: unknown1065cf73[_param1].field_0, 4, 3, caller
                                              else:
                                                  require ext_code.size(addr(code.data[11619 len 32]))
                                                  call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                                                       gas gas_remaining - 50 wei
                                                      args 0x626f6e6400000000000000000000000000000000000000000000000000000000
                                                  require ext_call.success
                                                  require ext_code.size(code.data[11619 len 32])
                                                  call code.data[11619 len 32].addressOf(bytes32 name) with:
                                                       gas gas_remaining - 50 wei
                                                      args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                                                  require ext_call.success
                                                  if _param2 <= unknown1065cf73[_param1].field_768:
                                                      if not unknown1065cf73[_param1].field_2472:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x308f16da with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, 0, unknown1065cf73[_param1].field_2304, caller, _param2, unknown1065cf73[_param1].field_2048, bool(unknown1065cf73[_param1].field_2472)
                                                          require ext_call.success
                                                      else:
                                                          if not unknown1065cf73[_param1].field_2304:
                                                              call unknown1065cf73[_param1].field_1024 with:
                                                                 value _param2 * unknown1065cf73[_param1].field_512 wei
                                                                   gas 2300 * is_zero(value) wei
                                                              require ext_call.success
                                                          else:
                                                              call unknown1065cf73[_param1].field_2304 with:
                                                                 value _param2 * unknown1065cf73[_param1].field_2048 wei
                                                                   gas 2300 * is_zero(value) wei
                                                              require ext_call.success
                                                              call unknown1065cf73[_param1].field_1024 with:
                                                                 value _param2 * unknown1065cf73[_param1].field_512 wei
                                                                   gas 2300 * is_zero(value) wei
                                                          if call.value > (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) + (_param2 * unknown1065cf73[_param1].field_2048):
                                                              call caller with:
                                                                 value call.value - (unknown1065cf73[_param1].field_2048 * unknown1065cf73[_param1].field_768) - (unknown1065cf73[_param1].field_768 * unknown1065cf73[_param1].field_512) wei
                                                                   gas 2300 * is_zero(value) wei
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0xedc43db5 with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, unknown1065cf73[_param1].field_1024, caller, _param2, unknown1065cf73[_param1].field_512, bool(unknown1065cf73[_param1].field_2472)
                                                      require ext_call.success
                                                      require ext_call.return_data[0]
                                                      if not unknown1065cf73[_param1].field_2464:
                                                          unknown1065cf73[_param1].field_768 -= _param2
                                                      else:
                                                          require ext_code.size(addr(ext_call.return_data[0]))
                                                          call addr(ext_call.return_data[0]).0x391465cb with:
                                                               gas gas_remaining - 50 wei
                                                              args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                                                          require ext_call.success
                                                          if not ext_call.return_data[0]:
                                                              unknown1065cf73[_param1].field_768 -= _param2
                                                          else:
                                                              require ext_code.size(addr(ext_call.return_data[0]))
                                                              call addr(ext_call.return_data[0]).0x7954e911 with:
                                                                   gas gas_remaining - 50 wei
                                                                  args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024, _param2
                                                              require ext_call.success
                                                      if not unknown1065cf73[_param1].field_768:
                                                          unknown1065cf73[_param1].field_1792 = 1
                                                      require ext_code.size(addr(ext_call.return_data[0]))
                                                      call addr(ext_call.return_data[0]).0x5168fe58 with:
                                                           gas gas_remaining - 50 wei
                                                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_512
                                                      require ext_call.success
                                                      log 0x129066a9: unknown1065cf73[_param1].field_0, _param2, 6, unknown1065cf73[_param1].field_1024, caller
                                                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0xdbe867f8
# getter = None
# const = None
# payable = False
def unknowndbe867f8(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  if unknown1065cf73[_param1].field_1024:
      if unknown1065cf73[_param1].field_1024 == caller:
          if not unknown1065cf73[_param1].field_1808:
              if not unknown1065cf73[_param1].field_1792:
                  if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                      if _param2 >= 0:
                          if _param3 >= 0:
                              unknown1065cf73[_param1].field_512 = _param2
                              unknown1065cf73[_param1].field_2048 = _param3
                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if stor0 == caller:
              if not unknown1065cf73[_param1].field_1808:
                  if not unknown1065cf73[_param1].field_1792:
                      if unknown1065cf73[_param1].field_1536 >= block.timestamp:
                          if _param2 >= 0:
                              if _param3 >= 0:
                                  unknown1065cf73[_param1].field_512 = _param2
                                  unknown1065cf73[_param1].field_2048 = _param3
                                  log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0xe1b56a7d
# getter = None
# const = None
# payable = False
def unknowne1b56a7d(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4): # not payable
  if unknown1065cf73[_param1].field_1024:
      if unknown1065cf73[_param1].field_1024 == caller:
          if not unknown1065cf73[_param1].field_1808:
              if not unknown1065cf73[_param1].field_1792:
                  if _param3 <= unknown1065cf73[_param1].field_768:
                      unknown1065cf73[_param1].field_768 = _param3
                      unknown1065cf73[_param1].field_512 = _param2
                      unknown1065cf73[_param1].field_1536 = _param4
                      log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                  else:
                      require ext_code.size(addr(code.data[11619 len 32]))
                      call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                           gas gas_remaining - 50 wei
                          args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                      require ext_call.success
                      require ext_code.size(addr(ext_call.return_data[0]))
                      call addr(ext_call.return_data[0]).0xb1eb7998 with:
                           gas gas_remaining - 50 wei
                          args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                      require ext_call.success
                      if ext_call.return_data[0] >= _param3 - unknown1065cf73[_param1].field_768:
                          unknown1065cf73[_param1].field_768 = _param3
                          unknown1065cf73[_param1].field_512 = _param2
                          unknown1065cf73[_param1].field_1536 = _param4
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
      else:
          if stor0 == caller:
              if not unknown1065cf73[_param1].field_1808:
                  if not unknown1065cf73[_param1].field_1792:
                      if _param3 <= unknown1065cf73[_param1].field_768:
                          unknown1065cf73[_param1].field_768 = _param3
                          unknown1065cf73[_param1].field_512 = _param2
                          unknown1065cf73[_param1].field_1536 = _param4
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, unknown1065cf73[unknown1065cf73[_param1].field_0].field_512, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0
                      else:
                          require ext_code.size(addr(code.data[11619 len 32]))
                          call addr(code.data[11619 len 32]).addressOf(bytes32 name) with:
                               gas gas_remaining - 50 wei
                              args 0x637573746f6469616e0000000000000000000000000000000000000000000000
                          require ext_call.success
                          require ext_code.size(addr(ext_call.return_data[0]))
                          call addr(ext_call.return_data[0]).0xb1eb7998 with:
                               gas gas_remaining - 50 wei
                              args unknown1065cf73[_param1].field_256, unknown1065cf73[_param1].field_1024
                          require ext_call.success
                          if ext_call.return_data[0] >= _param3 - unknown1065cf73[_param1].field_768:
                              unknown1065cf73[_param1].field_768 = _param3
                              unknown1065cf73[_param1].field_512 = _param2
                              unknown1065cf73[_param1].field_1536 = _param4
                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_param1].field_0].field_256, 0, unknown1065cf73[unknown1065cf73[_param1].field_0].field_768, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1024, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1280, unknown1065cf73[unknown1065cf73[_param1].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_param1].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_param1].field_0].field_0


# hash = 0xf19b8273
# getter = ['bool', ['storage', 8, 0, ['add', 7, ['sha3', ['data', ['cd', 4], 1]]]]]
# const = None
# payable = False
def unknownf19b8273(uint256 _param1): # not payable
  return bool(unknown1065cf73[_param1].field_1792)


# hash = 0xf7d97577
# getter = None
# const = None
# payable = False
def setPrice(uint256 _date, uint256 _priceAtDate): # not payable
  if unknown1065cf73[_date].field_1024:
      if unknown1065cf73[_date].field_1024 == caller:
          if not unknown1065cf73[_date].field_1808:
              if not unknown1065cf73[_date].field_1792:
                  if unknown1065cf73[_date].field_1536 >= block.timestamp:
                      if _priceAtDate >= 0:
                          unknown1065cf73[_date].field_512 = _priceAtDate
                          log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_date].field_0].field_256, unknown1065cf73[unknown1065cf73[_date].field_0].field_512, unknown1065cf73[unknown1065cf73[_date].field_0].field_768, unknown1065cf73[unknown1065cf73[_date].field_0].field_1024, unknown1065cf73[unknown1065cf73[_date].field_0].field_1280, unknown1065cf73[unknown1065cf73[_date].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_date].field_0].field_0
      else:
          if stor0 == caller:
              if not unknown1065cf73[_date].field_1808:
                  if not unknown1065cf73[_date].field_1792:
                      if unknown1065cf73[_date].field_1536 >= block.timestamp:
                          if _priceAtDate >= 0:
                              unknown1065cf73[_date].field_512 = _priceAtDate
                              log 0x1d3cd45a: unknown1065cf73[unknown1065cf73[_date].field_0].field_256, unknown1065cf73[unknown1065cf73[_date].field_0].field_512, unknown1065cf73[unknown1065cf73[_date].field_0].field_768, unknown1065cf73[unknown1065cf73[_date].field_0].field_1024, unknown1065cf73[unknown1065cf73[_date].field_0].field_1280, unknown1065cf73[unknown1065cf73[_date].field_0].field_1536, bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1792), bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1800), bool(unknown1065cf73[unknown1065cf73[_date].field_0].field_1808), 13, unknown1065cf73[unknown1065cf73[_date].field_0].field_0


# hash = 0xffcf88fd
# getter = ['storage', 256, 0, ['add', ['cd', 36], ['sha3', ['sha3', ['data', ['cd', 4], 2]]]]]
# const = None
# payable = False
def unknownffcf88fd(uint256 _param1, uint256 _param2): # not payable
  require _param2 < unknown5e8b360e[_param1].field_0
  return unknown5e8b360e[_param1][_param2].field_0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


