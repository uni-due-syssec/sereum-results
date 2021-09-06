# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x9ddCd47592b4D68E53633C6ba118faC9cCCD1f98 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    unknown08294e44Address # mask: a s
    # storage address 2
    unknown415b52e2
    # storage address 3
    unknown3319c688
    # storage address 4
    unknowne0cc6bb2
    # storage address 5
    stor5
    # storage address 6
    unknown424c6041
    # storage address 7
    unknown1d81333bAddress # mask: a s
    # storage address 8
    stor8
# hash = 0x03cd4f49
# getter = None
# const = None
# payable = False
def unknown03cd4f49(uint256 m_param1): # not payable
  require ext_code.size(munknown08294e44Address)
  call munknown08294e44Address.ownerOf(uint256 tokenId) with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      require ext_code.size(munknown08294e44Address)
      call munknown08294e44Address.0xbb19f507 with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
  if bool(mstor5m[m_param1m]) == 1:
      require ext_code.size(munknown08294e44Address)
      call munknown08294e44Address.tokenTypes(uint256 param1) with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require 1 <= munknown3319c688m[ext_call.return_data[0]m]m.field_0
      require ext_code.size(munknown08294e44Address)
      call munknown08294e44Address.tokenTypes(uint256 param1) with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require munknown3319c688m[ext_call.return_data[0]m]m.field_0 - 1 < munknown3319c688m[ext_call.return_data[0]m]m.field_0
      munknowne0cc6bb2m[mstor3m[ext_call.return_data[0]m]m[mstor3m[ext_call.return_data[0]m]m.field_0m]m.field_0m] = munknowne0cc6bb2m[m_param1m]
      require ext_code.size(munknown08294e44Address)
      call munknown08294e44Address.tokenTypes(uint256 param1) with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require munknowne0cc6bb2m[m_param1m] < munknown3319c688m[ext_call.return_data[0]m]m.field_0
      munknown3319c688m[ext_call.return_data[0]m]m[mstor4m[m_param1m]m]m.field_0 = munknown3319c688m[ext_call.return_data[0]m]m[munknown3319c688m[ext_call.return_data[0]m]m.field_0m]m.field_0
      require ext_code.size(munknown08294e44Address)
      call munknown08294e44Address.tokenTypes(uint256 param1) with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      munknown3319c688m[ext_call.return_data[0]m]m.field_0--
      if munknown3319c688m[ext_call.return_data[0]m]m.field_0 > munknown3319c688m[ext_call.return_data[0]m]m.field_0 - 1:
          [94midx = munknown3319c688m[ext_call.return_data[0]m]m.field_0 - 1
          mwhile munknown3319c688m[ext_call.return_data[0]m]m.field_0 > [94midxm:
              munknown3319c688m[ext_call.return_data[0]m]m[[94midxm]m.field_0 = 0
              [94midx = [94midx + 1
              mcontinue 
      mstor5m[m_param1m] = 0
      require ext_code.size(munknown08294e44Address)
      call munknown08294e44Address.0x7f05ebf2 with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0x08294e44
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown08294e44(): # not payable
  return munknown08294e44Address


# hash = 0x119a80f1
# getter = None
# const = None
# payable = False
def unknown119a80f1(uint256 m_param1, uint256 m_param2): # not payable
  require caller == munknown08294e44Address
  require uint8(mstor8m[m_param2m])
  munknown3319c688m[m_param2m]m.field_0++
  munknown3319c688m[m_param2m]m[munknown3319c688m[m_param2m]m.field_0m]m.field_0 = m_param1
  require 1 <= munknown3319c688m[m_param2m]m.field_0
  munknowne0cc6bb2m[m_param1m] = munknown3319c688m[m_param2m]m.field_0 - 1
  mstor5m[m_param1m] = 1


# hash = 0x1d81333b
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def unknown1d81333b(): # not payable
  return munknown1d81333bAddress


# hash = 0x2831f2f4
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 5]]]]
# const = None
# payable = False
def unknown2831f2f4(uint256 m_param1): # not payable
  return bool(mstor5m[m_param1m])


# hash = 0x3319c688
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 3]]], ['cd', 36]]]
# const = None
# payable = False
def unknown3319c688(uint256 m_param1, uint256 m_param2): # not payable
  require m_param2 < munknown3319c688m[m_param1m]m.field_0
  return munknown3319c688m[m_param1m]m[m_param2m]m.field_0


# hash = 0x415b52e2
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 2]]], ['cd', 36]]]
# const = None
# payable = False
def unknown415b52e2(uint256 m_param1, uint256 m_param2): # not payable
  require m_param2 < munknown415b52e2m[m_param1m]m.field_0
  return munknown415b52e2m[m_param1m]m[m_param2m]m.field_0


# hash = 0x424c6041
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 6]]]]]]]
# const = None
# payable = False
def unknown424c6041(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  return munknown424c6041m[m_param1m]m[m_param2m]m[m_param3m]


# hash = 0x43c542ca
# getter = None
# const = None
# payable = False
def unknown43c542ca(uint256 m_param1): # not payable
  if not munknown3319c688m[m_param1m]m.field_0:
      mem[(32 * munknown3319c688m[m_param1m]m.field_0) + 128] = 32
      mem[(32 * munknown3319c688m[m_param1m]m.field_0) + 160] = munknown3319c688m[m_param1m]m.field_0
      mem[(32 * munknown3319c688m[m_param1m]m.field_0) + 192 len floor32(munknown3319c688m[m_param1m]m.field_0)] = mem[128 len floor32(munknown3319c688m[m_param1m]m.field_0)]
      return memory
        from (32 * munknown3319c688m[m_param1m]m.field_0) + 128
         [93mlen (96 * munknown3319c688m[m_param1m]m.field_0) + 64
  mem[128] = munknown3319c688m[m_param1m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknown3319c688m[m_param1m]m.field_0) + 96 > [94midxm:
      mem[[94midx + 32] = munknown3319c688m[m_param1m]m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * munknown3319c688m[m_param1m]m.field_0) + 192 len floor32(munknown3319c688m[m_param1m]m.field_0)] = mem[128 len floor32(munknown3319c688m[m_param1m]m.field_0)]
  return Array(len=munknown3319c688m[m_param1m]m.field_0, data=mem[128 len floor32(munknown3319c688m[m_param1m]m.field_0)], mem[(32 * munknown3319c688m[m_param1m]m.field_0) + floor32(munknown3319c688m[m_param1m]m.field_0) + 192 len (32 * munknown3319c688m[m_param1m]m.field_0) - floor32(munknown3319c688m[m_param1m]m.field_0)]), 


# hash = 0x4d6861a6
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 8]]]]
# const = None
# payable = False
def unknown4d6861a6(uint256 m_param1): # not payable
  return bool(uint8(mstor8m[m_param1m]))


# hash = 0x5c0b966f
# getter = None
# const = None
# payable = True
def unknown5c0b966f(uint256 m_param1) payable: 
  require caller
  require this.address != caller
  require ext_code.size(munknown08294e44Address)
  call munknown08294e44Address.exists(uint256 tokenId) with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(munknown08294e44Address)
      call munknown08294e44Address.ownerOf(uint256 tokenId) with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require call.value > 0
          require call.value <= eth.balance(this.address)
          require ext_code.size(munknown08294e44Address)
          call munknown08294e44Address.0xef8998ae with:
               gas gas_remaining wei
              args m_param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              require ext_call.return_data[0] == call.value
              require call.value > 0
              if call.value:
                  require call.value
                  require 10 * call.value / call.value == 10
                  require 10 * call.value / 10 / 100 < call.value
                  require ext_code.size(munknown08294e44Address)
                  call munknown08294e44Address.wallet() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      call ext_call.return_data[12 len 20] with:
                         value 10 * call.value / 10 / 100 wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require ext_code.size(munknown08294e44Address)
                          call munknown08294e44Address.0xef8998ae with:
                               gas gas_remaining wei
                              args m_param1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require 10 * call.value / 10 / 100 <= ext_call.return_data[0]
                              call addr(ext_call.return_data[0]) with:
                                 value ext_call.return_data[0] - (10 * call.value / 10 / 100) wei
                                   gas 2300 * is_zero(value) wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require ext_code.size(munknown08294e44Address)
                                  call munknown08294e44Address.safeTransferFrom(address from, address to, uint256 tokenId) with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[0]), caller, m_param1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      munknown415b52e2m[m_param1m]m.field_0++
                                      munknown415b52e2m[m_param1m]m[munknown415b52e2m[m_param1m]m.field_0m]m.field_0 = call.value
                                      require ext_code.size(munknown08294e44Address)
                                      call munknown08294e44Address.0xef8998ae with:
                                           gas gas_remaining wei
                                          args m_param1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          require ext_code.size(munknown08294e44Address)
                                          call munknown08294e44Address.tokenTypes(uint256 param1) with:
                                               gas gas_remaining wei
                                              args m_param1
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              require ext_code.size(munknown08294e44Address)
                                              call munknown08294e44Address.0x8da0b3ee with:
                                                   gas gas_remaining wei
                                                  args m_param1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  require ext_code.size(munknown08294e44Address)
                                                  call munknown08294e44Address.0x50dc1722 with:
                                                       gas gas_remaining wei
                                                      args m_param1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      munknown424c6041m[ext_call.return_data[0]m]m[ext_call.return_data[0]m]m[ext_call.return_data[0]m] = ext_call.return_data[0]
                                                      require ext_code.size(munknown08294e44Address)
                                                      call munknown08294e44Address.0xed9b079a with:
                                                           gas gas_remaining wei
                                                          args m_param1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      else:
                                                          require ext_code.size(munknown08294e44Address)
                                                          call munknown08294e44Address.tokenTypes(uint256 param1) with:
                                                               gas gas_remaining wei
                                                              args m_param1
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 32
                                                              require 1 <= munknown3319c688m[ext_call.return_data[0]m]m.field_0
                                                              require ext_code.size(munknown08294e44Address)
                                                              call munknown08294e44Address.tokenTypes(uint256 param1) with:
                                                                   gas gas_remaining wei
                                                                  args m_param1
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 32
                                                                  require munknown3319c688m[ext_call.return_data[0]m]m.field_0 - 1 < munknown3319c688m[ext_call.return_data[0]m]m.field_0
                                                                  munknowne0cc6bb2m[mstor3m[ext_call.return_data[0]m]m[mstor3m[ext_call.return_data[0]m]m.field_0m]m.field_0m] = munknowne0cc6bb2m[m_param1m]
                                                                  require ext_code.size(munknown08294e44Address)
                                                                  call munknown08294e44Address.tokenTypes(uint256 param1) with:
                                                                       gas gas_remaining wei
                                                                      args m_param1
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >= 32
                                                                      require munknowne0cc6bb2m[m_param1m] < munknown3319c688m[ext_call.return_data[0]m]m.field_0
                                                                      munknown3319c688m[ext_call.return_data[0]m]m[mstor4m[m_param1m]m]m.field_0 = munknown3319c688m[ext_call.return_data[0]m]m[munknown3319c688m[ext_call.return_data[0]m]m.field_0m]m.field_0
                                                                      require ext_code.size(munknown08294e44Address)
                                                                      call munknown08294e44Address.tokenTypes(uint256 param1) with:
                                                                           gas gas_remaining wei
                                                                          args m_param1
                                                                      if not ext_call.success:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >= 32
                                                                          munknown3319c688m[ext_call.return_data[0]m]m.field_0--
                                                                          if munknown3319c688m[ext_call.return_data[0]m]m.field_0 <= munknown3319c688m[ext_call.return_data[0]m]m.field_0 - 1:
                                                                              mstor5m[m_param1m] = 0
                                                                              require ext_code.size(munknown08294e44Address)
                                                                              call munknown08294e44Address.0x7f05ebf2 with:
                                                                                   gas gas_remaining wei
                                                                                  args m_param1
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  munknown415b52e2m[m_param1m]m.field_0++
                                                                                  munknown415b52e2m[m_param1m]m[munknown415b52e2m[m_param1m]m.field_0m]m.field_0 = call.value
                                                                                  log Received(
                                                                                        address user=_param1,
                                                                                        uint256 ethers=call.value,
                                                                                        uint256 tokens=caller)
                                                                                  stop
                                                                          else:
                                                                              [94midx = munknown3319c688m[ext_call.return_data[0]m]m.field_0 - 1
                                                                              mwhile munknown3319c688m[ext_call.return_data[0]m]m.field_0 > [94midxm:
                                                                                  munknown3319c688m[ext_call.return_data[0]m]m[[94midxm]m.field_0 = 0
                                                                                  [94midx = [94midx + 1
                                                                                  mcontinue 
                                                                              mstor5m[m_param1m] = 0
                                                                              require ext_code.size(munknown08294e44Address)
                                                                              call munknown08294e44Address.0x7f05ebf2 with:
                                                                                   gas gas_remaining wei
                                                                                  args m_param1
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  munknown415b52e2m[m_param1m]m.field_0++
                                                                                  munknown415b52e2m[m_param1m]m[munknown415b52e2m[m_param1m]m.field_0m]m.field_0 = call.value
                                                                                  log Received(
                                                                                        address user=_param1,
                                                                                        uint256 ethers=call.value,
                                                                                        uint256 tokens=caller)
                                                                                  stop
              else:
                  require 0 < call.value
                  require ext_code.size(munknown08294e44Address)
                  call munknown08294e44Address.wallet() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      call ext_call.return_data[12 len 20] with:
                           gas 2300 wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require ext_code.size(munknown08294e44Address)
                          call munknown08294e44Address.0xef8998ae with:
                               gas gas_remaining wei
                              args m_param1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require 0 <= ext_call.return_data[0]
                              call addr(ext_call.return_data[0]) with:
                                 value ext_call.return_data[0] wei
                                   gas 2300 * is_zero(value) wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require ext_code.size(munknown08294e44Address)
                                  call munknown08294e44Address.safeTransferFrom(address from, address to, uint256 tokenId) with:
                                       gas gas_remaining wei
                                      args addr(ext_call.return_data[0]), caller, m_param1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      munknown415b52e2m[m_param1m]m.field_0++
                                      munknown415b52e2m[m_param1m]m[munknown415b52e2m[m_param1m]m.field_0m]m.field_0 = call.value
                                      require ext_code.size(munknown08294e44Address)
                                      call munknown08294e44Address.0xef8998ae with:
                                           gas gas_remaining wei
                                          args m_param1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          require ext_code.size(munknown08294e44Address)
                                          call munknown08294e44Address.tokenTypes(uint256 param1) with:
                                               gas gas_remaining wei
                                              args m_param1
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              require ext_code.size(munknown08294e44Address)
                                              call munknown08294e44Address.0x8da0b3ee with:
                                                   gas gas_remaining wei
                                                  args m_param1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  require ext_code.size(munknown08294e44Address)
                                                  call munknown08294e44Address.0x50dc1722 with:
                                                       gas gas_remaining wei
                                                      args m_param1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      munknown424c6041m[ext_call.return_data[0]m]m[ext_call.return_data[0]m]m[ext_call.return_data[0]m] = ext_call.return_data[0]
                                                      require ext_code.size(munknown08294e44Address)
                                                      call munknown08294e44Address.0xed9b079a with:
                                                           gas gas_remaining wei
                                                          args m_param1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      else:
                                                          require ext_code.size(munknown08294e44Address)
                                                          call munknown08294e44Address.tokenTypes(uint256 param1) with:
                                                               gas gas_remaining wei
                                                              args m_param1
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 32
                                                              require 1 <= munknown3319c688m[ext_call.return_data[0]m]m.field_0
                                                              require ext_code.size(munknown08294e44Address)
                                                              call munknown08294e44Address.tokenTypes(uint256 param1) with:
                                                                   gas gas_remaining wei
                                                                  args m_param1
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 32
                                                                  require munknown3319c688m[ext_call.return_data[0]m]m.field_0 - 1 < munknown3319c688m[ext_call.return_data[0]m]m.field_0
                                                                  munknowne0cc6bb2m[mstor3m[ext_call.return_data[0]m]m[mstor3m[ext_call.return_data[0]m]m.field_0m]m.field_0m] = munknowne0cc6bb2m[m_param1m]
                                                                  require ext_code.size(munknown08294e44Address)
                                                                  call munknown08294e44Address.tokenTypes(uint256 param1) with:
                                                                       gas gas_remaining wei
                                                                      args m_param1
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >= 32
                                                                      require munknowne0cc6bb2m[m_param1m] < munknown3319c688m[ext_call.return_data[0]m]m.field_0
                                                                      munknown3319c688m[ext_call.return_data[0]m]m[mstor4m[m_param1m]m]m.field_0 = munknown3319c688m[ext_call.return_data[0]m]m[munknown3319c688m[ext_call.return_data[0]m]m.field_0m]m.field_0
                                                                      require ext_code.size(munknown08294e44Address)
                                                                      call munknown08294e44Address.tokenTypes(uint256 param1) with:
                                                                           gas gas_remaining wei
                                                                          args m_param1
                                                                      if not ext_call.success:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >= 32
                                                                          munknown3319c688m[ext_call.return_data[0]m]m.field_0--
                                                                          if munknown3319c688m[ext_call.return_data[0]m]m.field_0 <= munknown3319c688m[ext_call.return_data[0]m]m.field_0 - 1:
                                                                              mstor5m[m_param1m] = 0
                                                                              require ext_code.size(munknown08294e44Address)
                                                                              call munknown08294e44Address.0x7f05ebf2 with:
                                                                                   gas gas_remaining wei
                                                                                  args m_param1
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  munknown415b52e2m[m_param1m]m.field_0++
                                                                                  munknown415b52e2m[m_param1m]m[munknown415b52e2m[m_param1m]m.field_0m]m.field_0 = call.value
                                                                                  log Received(
                                                                                        address user=_param1,
                                                                                        uint256 ethers=call.value,
                                                                                        uint256 tokens=caller)
                                                                                  stop
                                                                          else:
                                                                              [94midx = munknown3319c688m[ext_call.return_data[0]m]m.field_0 - 1
                                                                              mwhile munknown3319c688m[ext_call.return_data[0]m]m.field_0 > [94midxm:
                                                                                  munknown3319c688m[ext_call.return_data[0]m]m[[94midxm]m.field_0 = 0
                                                                                  [94midx = [94midx + 1
                                                                                  mcontinue 
                                                                              mstor5m[m_param1m] = 0
                                                                              require ext_code.size(munknown08294e44Address)
                                                                              call munknown08294e44Address.0x7f05ebf2 with:
                                                                                   gas gas_remaining wei
                                                                                  args m_param1
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  munknown415b52e2m[m_param1m]m.field_0++
                                                                                  munknown415b52e2m[m_param1m]m[munknown415b52e2m[m_param1m]m.field_0m]m.field_0 = call.value
                                                                                  log Received(
                                                                                        address user=_param1,
                                                                                        uint256 ethers=call.value,
                                                                                        uint256 tokens=caller)
                                                                                  stop


# hash = 0x690e7c09
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 8]]]]
# const = None
# payable = False
def unknown690e7c09(uint256 m_param1): # not payable
  return bool(uint8(mstor8m[m_param1m]))


# hash = 0x6e76ca40
# getter = None
# const = None
# payable = False
def unknown6e76ca40(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5): # not payable
  require caller == munknown1d81333bAddress
  munknown415b52e2m[m_param1m]m.field_0++
  munknown415b52e2m[m_param1m]m[munknown415b52e2m[m_param1m]m.field_0m]m.field_0 = m_param5
  munknown424c6041m[m_param2m]m[m_param3m]m[m_param4m] = m_param5


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x89f0b550
# getter = None
# const = None
# payable = False
def unknown89f0b550(uint256 m_param1): # not payable
  require m_param1 > 0
  if not m_param1:
      require 0 < m_param1
      return 0
  require m_param1
  require 10 * m_param1 / m_param1 == 10
  require 10 * m_param1 / 10 / 100 < m_param1
  return (10 * m_param1 / 10 / 100)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0xbeaab453
# getter = None
# const = None
# payable = False
def unknownbeaab453(uint256 m_param1): # not payable
  if not munknown415b52e2m[m_param1m]m.field_0:
      mem[(32 * munknown415b52e2m[m_param1m]m.field_0) + 128] = 32
      mem[(32 * munknown415b52e2m[m_param1m]m.field_0) + 160] = munknown415b52e2m[m_param1m]m.field_0
      mem[(32 * munknown415b52e2m[m_param1m]m.field_0) + 192 len floor32(munknown415b52e2m[m_param1m]m.field_0)] = mem[128 len floor32(munknown415b52e2m[m_param1m]m.field_0)]
      return memory
        from (32 * munknown415b52e2m[m_param1m]m.field_0) + 128
         [93mlen (96 * munknown415b52e2m[m_param1m]m.field_0) + 64
  mem[128] = munknown415b52e2m[m_param1m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknown415b52e2m[m_param1m]m.field_0) + 96 > [94midxm:
      mem[[94midx + 32] = munknown415b52e2m[m_param1m]m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * munknown415b52e2m[m_param1m]m.field_0) + 192 len floor32(munknown415b52e2m[m_param1m]m.field_0)] = mem[128 len floor32(munknown415b52e2m[m_param1m]m.field_0)]
  return Array(len=munknown415b52e2m[m_param1m]m.field_0, data=mem[128 len floor32(munknown415b52e2m[m_param1m]m.field_0)], mem[(32 * munknown415b52e2m[m_param1m]m.field_0) + floor32(munknown415b52e2m[m_param1m]m.field_0) + 192 len (32 * munknown415b52e2m[m_param1m]m.field_0) - floor32(munknown415b52e2m[m_param1m]m.field_0)]), 


# hash = 0xe0cc6bb2
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = False
def unknowne0cc6bb2(uint256 m_param1): # not payable
  return munknowne0cc6bb2m[m_param1m]


# hash = 0xf1ea5cd3
# getter = None
# const = None
# payable = False
def unknownf1ea5cd3(uint256 m_param1): # not payable
  require ext_code.size(munknown08294e44Address)
  call munknown08294e44Address.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require caller == ext_call.return_data[12 len 20]
  uint256(mstor8m[m_param1m]) = not bool(uint8(mstor8m[m_param1m])) or Mask(248, 8, uint256(mstor8m[m_param1m]))


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


