# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x1029Ee8B0CcA9665b09d813C7630620ae88461A2 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    authorityAddress # mask: a s
    # storage address 1
    owner # mask: a s
    # storage address 2
    unknown365a86fcAddress # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 10
    unknown20531bc9Address # mask: a s
    # storage address 11
    registryAddress # mask: a s
    # storage address 12
    versionAddress # mask: a s
    # storage address 13
    unknownc9d4623fAddress # mask: a s
    # storage address 14
    unknown8a471df9Address # mask: a s
    # storage address 15
    initialized # mask: a s
    # storage address 16
    unknownd19c4bda
    # storage address 17
    stor17
    # storage address 18
    NATIVE_ASSETAddress # mask: a s
    # storage address 19
    unknown0194497fAddress # mask: a s
    # storage address 20
    unknown522ed92a # mask: a s
    # storage address 21
    unknown6218f812 # mask: a s
    # storage address 22
    stor22 # mask: a s
    # storage address 23
    stor23 # mask: a s
    # storage address 24
    stor24 # mask: a s
    # storage address 25
    stor25 # mask: a s
    # storage address 26
    stor26 # mask: a s
# hash = 0x0194497f
# getter = ['storage', 160, 0, 19]
# const = None
# payable = False
def unknown0194497f(): # not payable
  return munknown0194497fAddress


# hash = 0x07afbe74
# getter = None
# const = None
# payable = False
def unknown07afbe74(addr m_param1): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  if not mstor17m[addr(m_param1)m]:
      if 20 <= munknownd19c4bdam.length:
          revert with 0, 'Max owned asset limit reached'
      mstor17m[addr(m_param1)m] = 1
      munknownd19c4bdam.length++
      munknownd19c4bdam[munknownd19c4bdam.lengthm] = m_param1
      log 0x7c823d8b: _param1


# hash = 0x0a47185d
# getter = None
# const = None
# payable = False
def unknown0a47185d(uint256 m_param1, uint256 m_param2): # not payable
  if m_param1 - m_param2 > m_param1:
      revert with 0, 'ds-math-sub-underflow'
  return (m_param1 - m_param2)


# hash = 0x0e7a2d4e
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 17]]]]
# const = None
# payable = False
def unknown0e7a2d4e(addr m_param1): # not payable
  return bool(mstor17m[m_param1m])


# hash = 0x13af4035
# getter = None
# const = None
# payable = False
def setOwner(address m_newOwner): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  mowner = m_newOwner
  log LogSetOwner(address owner=_newOwner)


# hash = 0x158ef93e
# getter = ['bool', ['storage', 8, 0, 15]]
# const = None
# payable = False
def initialized(): # not payable
  return bool(minitialized)


# hash = 0x20531bc9
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def unknown20531bc9(): # not payable
  return munknown20531bc9Address


# hash = 0x33ec6100
# getter = None
# const = None
# payable = True
def unknown33ec6100() payable: 
  [94ms = 0
  [94midx = 0
  mwhile [94midx < munknownd19c4bdam.lengthm:
      mem[0] = 16
      require ext_code.size(munknownd19c4bdam[[94midxm])
      call munknownd19c4bdam[[94midxm].balanceOf(address owner) with:
           gas gas_remaining wei
          args mstor9
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = munknownd19c4bdam[[94midxm]
      require ext_code.size(mstor8)
      call mstor8.0x6c0770e with:
           gas gas_remaining wei
          args munknownd19c4bdam[[94midxm]
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
          revert with 0, 'ds-math-add-overflow'
      if not 2 * ext_call.return_data[0]:
          if munknown0194497fAddress != munknownd19c4bdam[[94midxm]:
              mem[100] = munknownd19c4bdam[[94midxm]
              require ext_code.size(mstor8)
              call mstor8.0x28f5cd02 with:
                   gas gas_remaining wei
                  args munknownd19c4bdam[[94midxm]
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  mem[0] = munknownd19c4bdam[[94midxm]
                  mem[32] = 17
                  if mstor17m[mstor16m[[94midxm]m]:
                      mem[0] = munknownd19c4bdam[[94midxm]
                      mem[32] = 17
                      mstor17m[mstor16m[[94midxm]m] = 0
                      [94ms = 0
                      mwhile [94ms < munknownd19c4bdam.lengthm:
                          mem[0] = 16
                          if munknownd19c4bdam[[94msm] != munknownd19c4bdam[[94midxm]:
                              [94ms = [94ms + 1
                              mcontinue 
                          require munknownd19c4bdam.length - 1 < munknownd19c4bdam.length
                          require [94ms < munknownd19c4bdam.length
                          mem[0] = 16
                          munknownd19c4bdam[[94msm] = munknownd19c4bdam[munknownd19c4bdam.lengthm]
                          munknownd19c4bdam.length--
                          if munknownd19c4bdam.length > munknownd19c4bdam.length - 1:
                              mem[0] = 16
                              [94ms = munknownd19c4bdam.length + sha3(16) - 1
                              mwhile sha3(16) + munknownd19c4bdam.length > [94msm:
                                  mstor[[94msm] = 0
                                  [94ms = [94ms + 1
                                  mcontinue 
                          log 0x78c7527d: unknownd19c4bda[idx]
                          [94ms = munknownd19c4bdam[[94midxm]
                          [94midx = [94midx + 1
                          mcontinue 
                      log 0x78c7527d: unknownd19c4bda[idx]
      [94ms = munknownd19c4bdam[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  [94ms = 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < munknownd19c4bdam.lengthm:
      mem[0] = 16
      require ext_code.size(munknownd19c4bdam[[94midxm])
      call munknownd19c4bdam[[94midxm].balanceOf(address owner) with:
           gas gas_remaining wei
          args mstor9
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = munknownd19c4bdam[[94midxm]
      require ext_code.size(mstor8)
      call mstor8.0x6c0770e with:
           gas gas_remaining wei
          args munknownd19c4bdam[[94midxm]
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
          revert with 0, 'ds-math-add-overflow'
      if 2 * ext_call.return_data[0]:
          mem[100] = 2 * ext_call.return_data[0]
          mem[132] = munknownd19c4bdam[[94midxm]
          mem[164] = munknown0194497fAddress
          require ext_code.size(munknown20531bc9Address)
          call munknown20531bc9Address.0x7e3bfc2f with:
               gas gas_remaining wei
              args 2 * ext_call.return_data[0], munknownd19c4bdam[[94midxm], munknown0194497fAddress
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] < 0:
              revert with 0, 'ds-math-add-overflow'
      [94ms = 2 * ext_call.return_data[0]
      [94ms = munknownd19c4bdam[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(mstor7)
  call mstor7.totalSupply() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4)
  call mstor4.0x96521716 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 'ds-math-add-overflow'
  if not ext_call.return_data[0]:
      if ext_call.return_data[0] > 0:
          if 2 * ext_call.return_data[0] <= 0:
              revert with 0, 'No shares to calculate value for'
          require 2 * ext_call.return_data[0]
          if ext_call.return_data[0] > 0:
              require ext_code.size(mstor4)
              call mstor4.0x380eec66 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
                  revert with 0, 'ds-math-add-overflow'
              if 2 * ext_call.return_data[0] <= 0:
                  revert with 0, 'No shares to calculate value for'
              require 2 * ext_call.return_data[0]
      require ext_code.size(mstor7)
      call mstor7.totalSupply() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(mstor4)
      call mstor4.0xc56c862f with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      mstor22 = 0
      mstor23 = 0
      mstor24 = 0
  else:
      require 2 * ext_call.return_data[0]
      if -0 / 2 * ext_call.return_data[0] > 0:
          revert with 0, 'ds-math-sub-underflow'
      if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
          revert with 0, 'ds-math-add-overflow'
      if ext_call.return_data[0] > 0:
          if 2 * ext_call.return_data[0] <= 0:
              revert with 0, 'No shares to calculate value for'
          require 2 * ext_call.return_data[0]
          if ext_call.return_data[0] > 0:
              require ext_code.size(mstor4)
              call mstor4.0x380eec66 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
                  revert with 0, 'ds-math-add-overflow'
              if 2 * ext_call.return_data[0] <= 0:
                  revert with 0, 'No shares to calculate value for'
              require 2 * ext_call.return_data[0]
      require ext_code.size(mstor7)
      call mstor7.totalSupply() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(mstor4)
      call mstor4.0xc56c862f with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      mstor22 = 0
      mstor23 = -0 / 2 * ext_call.return_data[0]
      mstor24 = 0 / 2 * ext_call.return_data[0]
  mstor25 = ext_call.return_data[0]
  mstor26 = block.timestamp
  require ext_code.size(munknownc9d4623fAddress)
  call munknownc9d4623fAddress.0x709bb567 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 0 > gas_remaining:
      revert with 0, 'ds-math-sub-underflow'
  require ext_code.size(mregistryAddress)
  call mregistryAddress.0x74d32ad4 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(munknown20531bc9Address)
  call munknown20531bc9Address.0x7e3bfc2f with:
       gas gas_remaining wei
      args 0, munknown8a471df9Address, addr(ext_call.return_data[0])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 'ds-math-add-overflow'
  if call.value < ext_call.return_data[0]:
      revert with 0, 'Insufficent AMGU and/or incentive'
  require ext_code.size(munknownc9d4623fAddress)
  call munknownc9d4623fAddress.0x5ce1fb54 with:
     value ext_call.return_data[0] wei
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if call.value - ext_call.return_data[0] > call.value:
      revert with 0, 'ds-math-sub-underflow'
  call caller with:
     value call.value - ext_call.return_data[0] wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with 0, 'Refund failed'


# hash = 0x365a86fc
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknown365a86fc(): # not payable
  return munknown365a86fcAddress


# hash = 0x474e19f2
# getter = None
# const = ['return', 18]
# payable = False
const unknown474e19f2 = 18


# hash = 0x522ed92a
# getter = ['storage', 256, 0, 20]
# const = None
# payable = False
def unknown522ed92a(): # not payable
  return munknown522ed92a


# hash = 0x54fd4d50
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def version(): # not payable
  return mversionAddress


# hash = 0x56cff99f
# getter = None
# const = None
# payable = False
def unknown56cff99f(): # not payable
  [94ms = 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < munknownd19c4bdam.lengthm:
      mem[0] = 16
      require ext_code.size(munknownd19c4bdam[[94midxm])
      call munknownd19c4bdam[[94midxm].balanceOf(address owner) with:
           gas gas_remaining wei
          args mstor9
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = munknownd19c4bdam[[94midxm]
      require ext_code.size(mstor8)
      call mstor8.0x6c0770e with:
           gas gas_remaining wei
          args munknownd19c4bdam[[94midxm]
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
          revert with 0, 'ds-math-add-overflow'
      if 2 * ext_call.return_data[0]:
          mem[100] = 2 * ext_call.return_data[0]
          mem[132] = munknownd19c4bdam[[94midxm]
          mem[164] = munknown0194497fAddress
          require ext_code.size(munknown20531bc9Address)
          call munknown20531bc9Address.0x7e3bfc2f with:
               gas gas_remaining wei
              args 2 * ext_call.return_data[0], munknownd19c4bdam[[94midxm], munknown0194497fAddress
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] < 0:
              revert with 0, 'ds-math-add-overflow'
      [94ms = 2 * ext_call.return_data[0]
      [94ms = munknownd19c4bdam[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  return 0


# hash = 0x596d38d1
# getter = None
# const = None
# payable = False
def unknown596d38d1(): # not payable
  [94ms = 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < munknownd19c4bdam.lengthm:
      mem[0] = 16
      require ext_code.size(munknownd19c4bdam[[94midxm])
      call munknownd19c4bdam[[94midxm].balanceOf(address owner) with:
           gas gas_remaining wei
          args mstor9
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = munknownd19c4bdam[[94midxm]
      require ext_code.size(mstor8)
      call mstor8.0x6c0770e with:
           gas gas_remaining wei
          args munknownd19c4bdam[[94midxm]
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
          revert with 0, 'ds-math-add-overflow'
      if 2 * ext_call.return_data[0]:
          mem[100] = 2 * ext_call.return_data[0]
          mem[132] = munknownd19c4bdam[[94midxm]
          mem[164] = munknown0194497fAddress
          require ext_code.size(munknown20531bc9Address)
          call munknown20531bc9Address.0x7e3bfc2f with:
               gas gas_remaining wei
              args 2 * ext_call.return_data[0], munknownd19c4bdam[[94midxm], munknown0194497fAddress
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] < 0:
              revert with 0, 'ds-math-add-overflow'
      [94ms = 2 * ext_call.return_data[0]
      [94ms = munknownd19c4bdam[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(mstor7)
  call mstor7.totalSupply() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4)
  call mstor4.0x96521716 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 'ds-math-add-overflow'
  if not ext_call.return_data[0]:
      if ext_call.return_data[0] <= 0:
          return munknown6218f812
      if 2 * ext_call.return_data[0] <= 0:
          revert with 0, 'No shares to calculate value for'
      if 2 * ext_call.return_data[0]:
          if ext_call.return_data[0] <= 0:
              return munknown6218f812
          require ext_code.size(mstor4)
          call mstor4.0x380eec66 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
              revert with 0, 'ds-math-add-overflow'
          if 2 * ext_call.return_data[0] <= 0:
              revert with 0, 'No shares to calculate value for'
          if 2 * ext_call.return_data[0]:
              return (0 / 2 * ext_call.return_data[0])
  else:
      if 2 * ext_call.return_data[0]:
          if -0 / 2 * ext_call.return_data[0] > 0:
              revert with 0, 'ds-math-sub-underflow'
          if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
              revert with 0, 'ds-math-add-overflow'
          if ext_call.return_data[0] <= 0:
              return munknown6218f812
          if 2 * ext_call.return_data[0] <= 0:
              revert with 0, 'No shares to calculate value for'
          if 2 * ext_call.return_data[0]:
              if ext_call.return_data[0] <= 0:
                  return munknown6218f812
              require ext_code.size(mstor4)
              call mstor4.0x380eec66 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
                  revert with 0, 'ds-math-add-overflow'
              if 2 * ext_call.return_data[0] <= 0:
                  revert with 0, 'No shares to calculate value for'
              if 2 * ext_call.return_data[0]:
                  return (0 / 2 * ext_call.return_data[0])
  revert


# hash = 0x6218f812
# getter = ['storage', 256, 0, 21]
# const = None
# payable = False
def unknown6218f812(): # not payable
  return munknown6218f812


# hash = 0x635cbb14
# getter = None
# const = None
# payable = False
def unknown635cbb14(addr m_param1): # not payable
  require ext_code.size(m_param1)
  call m_param1.balanceOf(address owner) with:
       gas gas_remaining wei
      args mstor9
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor8)
  call mstor8.0x6c0770e with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 'ds-math-add-overflow'
  require ext_code.size(munknown20531bc9Address)
  call munknown20531bc9Address.0x7e3bfc2f with:
       gas gas_remaining wei
      args 2 * ext_call.return_data[0], addr(m_param1), munknown0194497fAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x71b58058
# getter = None
# const = None
# payable = False
def unknown71b58058(): # not payable
  [94ms = 0
  [94midx = 0
  mwhile [94midx < munknownd19c4bdam.lengthm:
      mem[0] = 16
      require ext_code.size(munknownd19c4bdam[[94midxm])
      call munknownd19c4bdam[[94midxm].balanceOf(address owner) with:
           gas gas_remaining wei
          args mstor9
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = munknownd19c4bdam[[94midxm]
      require ext_code.size(mstor8)
      call mstor8.0x6c0770e with:
           gas gas_remaining wei
          args munknownd19c4bdam[[94midxm]
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
          revert with 0, 'ds-math-add-overflow'
      if not 2 * ext_call.return_data[0]:
          if munknown0194497fAddress != munknownd19c4bdam[[94midxm]:
              mem[100] = munknownd19c4bdam[[94midxm]
              require ext_code.size(mstor8)
              call mstor8.0x28f5cd02 with:
                   gas gas_remaining wei
                  args munknownd19c4bdam[[94midxm]
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  mem[0] = munknownd19c4bdam[[94midxm]
                  mem[32] = 17
                  if mstor17m[mstor16m[[94midxm]m]:
                      mem[0] = munknownd19c4bdam[[94midxm]
                      mem[32] = 17
                      mstor17m[mstor16m[[94midxm]m] = 0
                      [94ms = 0
                      mwhile [94ms < munknownd19c4bdam.lengthm:
                          mem[0] = 16
                          if munknownd19c4bdam[[94msm] != munknownd19c4bdam[[94midxm]:
                              [94ms = [94ms + 1
                              mcontinue 
                          require munknownd19c4bdam.length - 1 < munknownd19c4bdam.length
                          require [94ms < munknownd19c4bdam.length
                          mem[0] = 16
                          munknownd19c4bdam[[94msm] = munknownd19c4bdam[munknownd19c4bdam.lengthm]
                          munknownd19c4bdam.length--
                          if munknownd19c4bdam.length > munknownd19c4bdam.length - 1:
                              mem[0] = 16
                              [94ms = munknownd19c4bdam.length + sha3(16) - 1
                              mwhile sha3(16) + munknownd19c4bdam.length > [94msm:
                                  mstor[[94msm] = 0
                                  [94ms = [94ms + 1
                                  mcontinue 
                          log 0x78c7527d: unknownd19c4bda[idx]
                          [94ms = munknownd19c4bdam[[94midxm]
                          [94midx = [94midx + 1
                          mcontinue 
                      log 0x78c7527d: unknownd19c4bda[idx]
      [94ms = munknownd19c4bdam[[94midxm]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x7a9e5e4b
# getter = None
# const = None
# payable = False
def setAuthority(address m_authority): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  mauthorityAddress = m_authority_
  log LogSetAuthority(address authority=_authority_)


# hash = 0x7b103999
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def registry(): # not payable
  return mregistryAddress


# hash = 0x83259ed9
# getter = None
# const = None
# payable = False
def unknown83259ed9(addr m_param1, addr m_param2, addr m_param3, addr m_param4, addr m_param5, addr m_param6, addr m_param7, addr m_param8, addr m_param9, addr m_param10, addr m_param11, addr m_param12): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  require caller == munknown365a86fcAddress
  if minitialized:
      revert with 0, 'Already initialized'
  mstor3 = m_param1
  mstor4 = m_param2
  mstor5 = m_param3
  mstor6 = m_param4
  mstor7 = m_param5
  mstor8 = m_param6
  mstor9 = m_param7
  munknown20531bc9Address = m_param8
  mregistryAddress = m_param9
  mversionAddress = m_param10
  munknownc9d4623fAddress = m_param11
  munknown8a471df9Address = m_param12
  minitialized = 1
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  mowner = 0
  log LogSetOwner(address owner)
  log 0x0 


# hash = 0x896aad53
# getter = None
# const = None
# payable = False
def unknown896aad53(uint256 m_param1, addr m_param2): # not payable
  [94ms = 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < munknownd19c4bdam.lengthm:
      mem[0] = 16
      require ext_code.size(munknownd19c4bdam[[94midxm])
      call munknownd19c4bdam[[94midxm].balanceOf(address owner) with:
           gas gas_remaining wei
          args mstor9
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = munknownd19c4bdam[[94midxm]
      require ext_code.size(mstor8)
      call mstor8.0x6c0770e with:
           gas gas_remaining wei
          args munknownd19c4bdam[[94midxm]
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
          revert with 0, 'ds-math-add-overflow'
      if 2 * ext_call.return_data[0]:
          mem[100] = 2 * ext_call.return_data[0]
          mem[132] = munknownd19c4bdam[[94midxm]
          mem[164] = munknown0194497fAddress
          require ext_code.size(munknown20531bc9Address)
          call munknown20531bc9Address.0x7e3bfc2f with:
               gas gas_remaining wei
              args 2 * ext_call.return_data[0], munknownd19c4bdam[[94midxm], munknown0194497fAddress
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] < 0:
              revert with 0, 'ds-math-add-overflow'
      [94ms = 2 * ext_call.return_data[0]
      [94ms = munknownd19c4bdam[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(mstor7)
  call mstor7.totalSupply() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4)
  call mstor4.0x96521716 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 'ds-math-add-overflow'
  if ext_call.return_data[0]:
      require 2 * ext_call.return_data[0]
      if -0 / 2 * ext_call.return_data[0] > 0:
          revert with 0, 'ds-math-sub-underflow'
  if ext_call.return_data[0] <= 0:
      if not munknown6218f812:
          require ext_code.size(munknown20531bc9Address)
          call munknown20531bc9Address.0x7e3bfc2f with:
               gas gas_remaining wei
              args 0, munknown0194497fAddress, m_param2
      else:
          require munknown6218f812
          if m_param1 * munknown6218f812 / munknown6218f812 != m_param1:
              revert with 0, 'ds-math-mul-overflow'
          require ext_code.size(munknown20531bc9Address)
          call munknown20531bc9Address.0x7e3bfc2f with:
               gas gas_remaining wei
              args m_param1 * munknown6218f812 / 10^18, munknown0194497fAddress, m_param2
  else:
      if 2 * ext_call.return_data[0] <= 0:
          revert with 0, 'No shares to calculate value for'
      require 2 * ext_call.return_data[0]
      if ext_call.return_data[0] <= 0:
          if not munknown6218f812:
              require ext_code.size(munknown20531bc9Address)
              call munknown20531bc9Address.0x7e3bfc2f with:
                   gas gas_remaining wei
                  args 0, munknown0194497fAddress, m_param2
          else:
              require munknown6218f812
              if m_param1 * munknown6218f812 / munknown6218f812 != m_param1:
                  revert with 0, 'ds-math-mul-overflow'
              require ext_code.size(munknown20531bc9Address)
              call munknown20531bc9Address.0x7e3bfc2f with:
                   gas gas_remaining wei
                  args m_param1 * munknown6218f812 / 10^18, munknown0194497fAddress, m_param2
      else:
          require ext_code.size(mstor4)
          call mstor4.0x380eec66 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
              revert with 0, 'ds-math-add-overflow'
          if 2 * ext_call.return_data[0] <= 0:
              revert with 0, 'No shares to calculate value for'
          require 2 * ext_call.return_data[0]
          if not 0 / 2 * ext_call.return_data[0]:
              require ext_code.size(munknown20531bc9Address)
              call munknown20531bc9Address.0x7e3bfc2f with:
                   gas gas_remaining wei
                  args 0, munknown0194497fAddress, m_param2
          else:
              require 0 / 2 * ext_call.return_data[0]
              if m_param1 * 0 / 2 * ext_call.return_data[0] / 0 / 2 * ext_call.return_data[0] != m_param1:
                  revert with 0, 'ds-math-mul-overflow'
              require ext_code.size(munknown20531bc9Address)
              call munknown20531bc9Address.0x7e3bfc2f with:
                   gas gas_remaining wei
                  args m_param1 * 0 / 2 * ext_call.return_data[0] / 10^18, munknown0194497fAddress, m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x8a471df9
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def unknown8a471df9(): # not payable
  return munknown8a471df9Address


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x9489fa84
# getter = None
# const = None
# payable = False
def unknown9489fa84(): # not payable
  [94ms = 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < munknownd19c4bdam.lengthm:
      mem[0] = 16
      require ext_code.size(munknownd19c4bdam[[94midxm])
      call munknownd19c4bdam[[94midxm].balanceOf(address owner) with:
           gas gas_remaining wei
          args mstor9
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = munknownd19c4bdam[[94midxm]
      require ext_code.size(mstor8)
      call mstor8.0x6c0770e with:
           gas gas_remaining wei
          args munknownd19c4bdam[[94midxm]
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
          revert with 0, 'ds-math-add-overflow'
      if 2 * ext_call.return_data[0]:
          mem[100] = 2 * ext_call.return_data[0]
          mem[132] = munknownd19c4bdam[[94midxm]
          mem[164] = munknown0194497fAddress
          require ext_code.size(munknown20531bc9Address)
          call munknown20531bc9Address.0x7e3bfc2f with:
               gas gas_remaining wei
              args 2 * ext_call.return_data[0], munknownd19c4bdam[[94midxm], munknown0194497fAddress
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] < 0:
              revert with 0, 'ds-math-add-overflow'
      [94ms = 2 * ext_call.return_data[0]
      [94ms = munknownd19c4bdam[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(mstor7)
  call mstor7.totalSupply() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4)
  call mstor4.0x96521716 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 'ds-math-add-overflow'
  if not ext_call.return_data[0]:
      if ext_call.return_data[0] <= 0:
          return munknown6218f812
      if 2 * ext_call.return_data[0] <= 0:
          revert with 0, 'No shares to calculate value for'
      if 2 * ext_call.return_data[0]:
          if ext_call.return_data[0] <= 0:
              return (0 / 2 * ext_call.return_data[0])
          require ext_code.size(mstor4)
          call mstor4.0x380eec66 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
              revert with 0, 'ds-math-add-overflow'
          if 2 * ext_call.return_data[0] <= 0:
              revert with 0, 'No shares to calculate value for'
          if 2 * ext_call.return_data[0]:
              return (0 / 2 * ext_call.return_data[0])
  else:
      if 2 * ext_call.return_data[0]:
          if -0 / 2 * ext_call.return_data[0] > 0:
              revert with 0, 'ds-math-sub-underflow'
          if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
              revert with 0, 'ds-math-add-overflow'
          if ext_call.return_data[0] <= 0:
              return munknown6218f812
          if 2 * ext_call.return_data[0] <= 0:
              revert with 0, 'No shares to calculate value for'
          if 2 * ext_call.return_data[0]:
              if ext_call.return_data[0] <= 0:
                  return (0 / 2 * ext_call.return_data[0])
              require ext_code.size(mstor4)
              call mstor4.0x380eec66 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
                  revert with 0, 'ds-math-add-overflow'
              if 2 * ext_call.return_data[0] <= 0:
                  revert with 0, 'No shares to calculate value for'
              if 2 * ext_call.return_data[0]:
                  return (0 / 2 * ext_call.return_data[0])
  revert


# hash = 0xa759822b
# getter = None
# const = None
# payable = False
def unknowna759822b(): # not payable
  [94ms = 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < munknownd19c4bdam.lengthm:
      mem[0] = 16
      require ext_code.size(munknownd19c4bdam[[94midxm])
      call munknownd19c4bdam[[94midxm].balanceOf(address owner) with:
           gas gas_remaining wei
          args mstor9
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = munknownd19c4bdam[[94midxm]
      require ext_code.size(mstor8)
      call mstor8.0x6c0770e with:
           gas gas_remaining wei
          args munknownd19c4bdam[[94midxm]
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
          revert with 0, 'ds-math-add-overflow'
      if 2 * ext_call.return_data[0]:
          mem[100] = 2 * ext_call.return_data[0]
          mem[132] = munknownd19c4bdam[[94midxm]
          mem[164] = munknown0194497fAddress
          require ext_code.size(munknown20531bc9Address)
          call munknown20531bc9Address.0x7e3bfc2f with:
               gas gas_remaining wei
              args 2 * ext_call.return_data[0], munknownd19c4bdam[[94midxm], munknown0194497fAddress
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] < 0:
              revert with 0, 'ds-math-add-overflow'
      [94ms = 2 * ext_call.return_data[0]
      [94ms = munknownd19c4bdam[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(mstor7)
  call mstor7.totalSupply() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4)
  call mstor4.0x96521716 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 'ds-math-add-overflow'
  if not ext_call.return_data[0]:
      if ext_call.return_data[0] <= 0:
          return 0, 0, ext_call.return_data[0], 0, munknown6218f812, munknown6218f812
      if 2 * ext_call.return_data[0] <= 0:
          revert with 0, 'No shares to calculate value for'
      if 2 * ext_call.return_data[0]:
          if ext_call.return_data[0] <= 0:
              return 0, 0, ext_call.return_data[0], 0, 0 / 2 * ext_call.return_data[0], munknown6218f812
          require ext_code.size(mstor4)
          call mstor4.0x380eec66 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
              revert with 0, 'ds-math-add-overflow'
          if 2 * ext_call.return_data[0] <= 0:
              revert with 0, 'No shares to calculate value for'
          if 2 * ext_call.return_data[0]:
              return 0, 0, ext_call.return_data[0], 0, 0 / 2 * ext_call.return_data[0], 0 / 2 * ext_call.return_data[0]
  else:
      if 2 * ext_call.return_data[0]:
          if -0 / 2 * ext_call.return_data[0] > 0:
              revert with 0, 'ds-math-sub-underflow'
          if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
              revert with 0, 'ds-math-add-overflow'
          if ext_call.return_data[0] <= 0:
              return 0, 
                     0 / 2 * ext_call.return_data[0],
                     ext_call.return_data[0],
                     -0 / 2 * ext_call.return_data[0],
                     munknown6218f812,
                     munknown6218f812
          if 2 * ext_call.return_data[0] <= 0:
              revert with 0, 'No shares to calculate value for'
          if 2 * ext_call.return_data[0]:
              if ext_call.return_data[0] <= 0:
                  return 0, 
                         0 / 2 * ext_call.return_data[0],
                         ext_call.return_data[0],
                         -0 / 2 * ext_call.return_data[0],
                         0 / 2 * ext_call.return_data[0],
                         munknown6218f812
              require ext_code.size(mstor4)
              call mstor4.0x380eec66 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
                  revert with 0, 'ds-math-add-overflow'
              if 2 * ext_call.return_data[0] <= 0:
                  revert with 0, 'No shares to calculate value for'
              if 2 * ext_call.return_data[0]:
                  return 0, 
                         0 / 2 * ext_call.return_data[0],
                         ext_call.return_data[0],
                         -0 / 2 * ext_call.return_data[0],
                         0 / 2 * ext_call.return_data[0],
                         0 / 2 * ext_call.return_data[0]
  revert


# hash = 0xb057d5c9
# getter = None
# const = None
# payable = False
def unknownb057d5c9(): # not payable
  return mstor22, mstor23, mstor24, mstor25, mstor26


# hash = 0xb1ffd471
# getter = None
# const = None
# payable = False
def unknownb1ffd471(): # not payable
  return mstor3, 
         mstor4,
         mstor5,
         mstor6,
         mstor7,
         mstor8,
         mstor9,
         munknown20531bc9Address,
         mregistryAddress,
         mversionAddress,
         munknownc9d4623fAddress,
         munknown8a471df9Address


# hash = 0xbf53253b
# getter = ['storage', 160, 0, 18]
# const = None
# payable = False
def NATIVE_ASSET(): # not payable
  return mNATIVE_ASSETAddress


# hash = 0xbf7e214f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def authority(): # not payable
  return mauthorityAddress


# hash = 0xc9d4623f
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknownc9d4623f(): # not payable
  return munknownc9d4623fAddress


# hash = 0xca334fe5
# getter = None
# const = None
# payable = False
def unknownca334fe5(addr m_param1): # not payable
  require ext_code.size(m_param1)
  call m_param1.balanceOf(address owner) with:
       gas gas_remaining wei
      args mstor9
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor8)
  call mstor8.0x6c0770e with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 'ds-math-add-overflow'
  return (2 * ext_call.return_data[0])


# hash = 0xd19c4bda
# getter = ['storage', 160, 0, ['add', ['sha3', 16], ['cd', 4]]]
# const = None
# payable = False
def unknownd19c4bda(uint256 m_param1): # not payable
  require m_param1 < munknownd19c4bdam.length
  return munknownd19c4bdam[m_param1m]


# hash = 0xe47d3ede
# getter = None
# const = None
# payable = False
def unknowne47d3ede(uint256 m_param1, uint256 m_param2): # not payable
  if m_param2 <= 0:
      revert with 0, 'No shares to calculate value for'
  require m_param2
  return (10^18 * m_param1 / m_param2)


# hash = 0xece28066
# getter = None
# const = None
# payable = False
def unknownece28066(): # not payable
  if not munknownd19c4bdam.length:
      mem[(32 * munknownd19c4bdam.length) + 128] = munknownd19c4bdam.length
  else:
      mem[128 len 32 * munknownd19c4bdam.length] = code.data[8034 len 32 * munknownd19c4bdam.length]
      mem[(32 * munknownd19c4bdam.length) + 128] = munknownd19c4bdam.length
      mem[(32 * munknownd19c4bdam.length) + 160 len 32 * munknownd19c4bdam.length] = code.data[8034 len 32 * munknownd19c4bdam.length]
  [94ms = 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < munknownd19c4bdam.lengthm:
      mem[0] = 16
      require ext_code.size(munknownd19c4bdam[[94midxm])
      call munknownd19c4bdam[[94midxm].balanceOf(address owner) with:
           gas gas_remaining wei
          args mstor9
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[(64 * munknownd19c4bdam.length) + 164] = munknownd19c4bdam[[94midxm]
      require ext_code.size(mstor8)
      call mstor8.0x6c0770e with:
           gas gas_remaining wei
          args munknownd19c4bdam[[94midxm]
      mem[(64 * munknownd19c4bdam.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 2 * ext_call.return_data[0] < ext_call.return_data[0]:
          revert with 0, 'ds-math-add-overflow'
      require [94midx < mem[(32 * munknownd19c4bdam.length) + 128]
      mem[(32 * munknownd19c4bdam.length) + (32 * [94midx) + 160] = munknownd19c4bdam[[94midxm]
      require [94midx < munknownd19c4bdam.length
      mem[(32 * [94midx) + 128] = 2 * ext_call.return_data[0]
      [94ms = 2 * ext_call.return_data[0]
      [94ms = munknownd19c4bdam[[94midxm]
      [94midx = [94midx + 1
      mcontinue 
  mem[(64 * munknownd19c4bdam.length) + 160] = 64
  mem[(64 * munknownd19c4bdam.length) + 224] = munknownd19c4bdam.length
  mem[(64 * munknownd19c4bdam.length) + 256 len floor32(munknownd19c4bdam.length)] = mem[128 len floor32(munknownd19c4bdam.length)]
  mem[(64 * munknownd19c4bdam.length) + 192] = (32 * munknownd19c4bdam.length) + 96
  mem[(98 * munknownd19c4bdam.length) + 256] = mem[(32 * munknownd19c4bdam.length) + 128]
  mem[(98 * munknownd19c4bdam.length) + 288 len floor32(mem[(32 * munknownd19c4bdam.length) + 128])] = mem[(32 * munknownd19c4bdam.length) + 160 len floor32(mem[(32 * munknownd19c4bdam.length) + 128])]
  return memory
    from (64 * munknownd19c4bdam.length) + 160
     [93mlen (32 * mem[(32 * munknownd19c4bdam.length) + 128]) + (32 * munknownd19c4bdam.length) + 128


# hash = 0xedf3ee5e
# getter = None
# const = ['return', 20]
# payable = False
const unknownedf3ee5e = 20


# hash = 0xf234b68e
# getter = None
# const = None
# payable = False
def unknownf234b68e(addr m_param1): # not payable
  if caller != this.address:
      if mowner != caller:
          if not mauthorityAddress:
              revert with 0, 'ds-auth-unauthorized'
          require ext_code.size(mauthorityAddress)
          call mauthorityAddress.canCall(address caller, address code, bytes4 sig) with:
               gas gas_remaining wei
              args caller, this.address, mcall.func_hash
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'ds-auth-unauthorized'
  if mstor17m[addr(m_param1)m]:
      mstor17m[addr(m_param1)m] = 0
      [94midx = 0
      mwhile [94midx < munknownd19c4bdam.lengthm:
          mem[0] = 16
          if munknownd19c4bdam[[94midxm] != m_param1:
              [94midx = [94midx + 1
              mcontinue 
          require munknownd19c4bdam.length - 1 < munknownd19c4bdam.length
          require [94midx < munknownd19c4bdam.length
          munknownd19c4bdam[[94midxm] = munknownd19c4bdam[munknownd19c4bdam.lengthm]
          munknownd19c4bdam.length--
          if munknownd19c4bdam.length > munknownd19c4bdam.length - 1:
              [94midx = munknownd19c4bdam.length + sha3(16) - 1
              mwhile sha3(16) + munknownd19c4bdam.length > [94midxm:
                  mstor[[94midxm] = 0
                  [94midx = [94midx + 1
                  mcontinue 
          log 0x78c7527d: _param1
          stop
      log 0x78c7527d: _param1


# hash = 0xfddc4686
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknownfddc4686(): # not payable
  return munknownd19c4bdam.length


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


