# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x5C3daB41baD87bf56EC91Acc873B6fD966cf6e96 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    exchangeAdapters
    # storage address 2
    exchanges
    # storage address 3
    stor3 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4
# hash = 0x07930644
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def getExchangeAdapter(bytes32 m_id): # not payable
  return mexchangeAdaptersm[m_idm]


# hash = 0x1ddfd7db
# getter = None
# const = None
# payable = False
def supportsTradingPair(address m_srcAddress, address m_destAddress, bytes32 m_exchangeId): # not payable
  if not m_exchangeId:
      [94ms = 0
      [94midx = 0
      [94ms = 0
      mwhile [94midx < mexchangesm.lengthm:
          mem[0] = mexchangesm[[94midxm]m.field_0
          mem[32] = 1
          require ext_code.size(mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m])
          call mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m].isEnabled() with:
               gas gas_remaining wei
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94ms = mexchangesm[[94midxm]m.field_0
              [94midx = [94midx + 1
              [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
              mcontinue 
          mem[100] = m_srcAddress
          mem[132] = m_destAddress
          require ext_code.size(mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m])
          call mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m].supportsTradingPair(address srcAddress, address destAddress) with:
               gas gas_remaining wei
              args addr(m_srcAddress), m_destAddress
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94ms = mexchangesm[[94midxm]m.field_0
              [94midx = [94midx + 1
              [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
              mcontinue 
          return 1
      return 0
  require ext_code.size(mexchangeAdaptersm[0m])
  call mexchangeAdaptersm[0m].isEnabled() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  require ext_code.size(mexchangeAdaptersm[0m])
  call mexchangeAdaptersm[0m].supportsTradingPair(address srcAddress, address destAddress) with:
       gas gas_remaining wei
      args addr(m_srcAddress), m_destAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  return 1


# hash = 0x1e2e3a6b
# getter = None
# const = None
# payable = False
def getExchanges(): # not payable
  if not mexchangesm.length:
      mem[(32 * mexchangesm.length) + 128] = 32
      mem[(32 * mexchangesm.length) + 160] = mexchangesm.length
      mem[(32 * mexchangesm.length) + 192 len floor32(mexchangesm.length)] = mem[128 len floor32(mexchangesm.length)]
      return memory
        from (32 * mexchangesm.length) + 128
         [93mlen (96 * mexchangesm.length) + 64
  mem[128] = uint256(mexchangesm.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * mexchangesm.length) + 96 > [94midxm:
      mem[[94midx + 32] = mexchangesm[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mexchangesm.length) + 192 len floor32(mexchangesm.length)] = mem[128 len floor32(mexchangesm.length)]
  return Array(len=mexchangesm.length, data=mem[128 len floor32(mexchangesm.length)], mem[(32 * mexchangesm.length) + floor32(mexchangesm.length) + 192 len (32 * mexchangesm.length) - floor32(mexchangesm.length)]), 


# hash = 0x2839fc29
# getter = ['storage', 256, 0, ['add', ['sha3', 2], ['cd', 4]]]
# const = None
# payable = False
def exchanges(uint256 m_param1): # not payable
  require m_param1 < mexchangesm.length
  return mexchangesm[m_param1m]m.field_0


# hash = 0x4fbe0858
# getter = None
# const = None
# payable = False
def unknown4fbe0858(uint256 m_param1): # not payable
  require caller == mowner
  [94midx = 0
  mwhile [94midx < mexchangesm.lengthm:
      mem[0] = 2
      if mexchangesm[[94midxm]m.field_0 != m_param1:
          [94midx = [94midx + 1
          mcontinue 
      if [94midx >= mexchangesm.length:
          return 0
      [94ms = [94midx
      mwhile [94ms < mexchangesm.length - 1m:
          require [94ms + 1 < mexchangesm.length
          require [94ms < mexchangesm.length
          mem[0] = 2
          mexchangesm[[94msm]m.field_0 = mexchangesm[[94msm]m.field_256
          [94ms = [94ms + 1
          mcontinue 
      mexchangesm.length--
      if mexchangesm.length > mexchangesm.length - 1:
          [94midx = mexchangesm.length + sha3(2) - 1
          mwhile sha3(2) + mexchangesm.length > [94midxm:
              mstor[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      return 1
  return 0


# hash = 0x5fc6b623
# getter = None
# const = None
# payable = False
def getPrice(address m_sourceAddress, address m_destAddress, uint256 m_amount, bytes32 m_exchangeId): # not payable
  if not m_exchangeId:
      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == m_sourceAddress:
          [94ms = 0
          [94ms = 0
          [94midx = 0
          mwhile [94midx < mexchangesm.lengthm:
              mem[0] = mexchangesm[[94midxm]m.field_0
              mem[32] = 1
              require ext_code.size(mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m])
              call mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m].isEnabled() with:
                   gas gas_remaining wei
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if ext_call.return_data[0]:
                      mem[132] = m_destAddress
                      mem[164] = m_amount
                      require ext_code.size(mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m])
                      call mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m].getPrice(address sourceAddress, address destAddress, uint256 amount) with:
                           gas gas_remaining wei
                          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(m_destAddress), m_amount
                      mem[96 len 64] = ext_call.return_data[0 len 64]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if ext_call.return_data[32] >=′ 0:
                                  if ext_call.return_data[32] <′ -1:
                                      [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                                      [94ms = mexchangesm[[94midxm]m.field_0
                                      [94midx = [94midx + 1
                                      mcontinue 
                                  else:
                                      [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                                      [94ms = mexchangesm[[94midxm]m.field_0
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                                  [94ms = mexchangesm[[94midxm]m.field_0
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                              [94ms = mexchangesm[[94midxm]m.field_0
                              [94midx = [94midx + 1
                              mcontinue 
                  else:
                      [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                      [94ms = mexchangesm[[94midxm]m.field_0
                      [94midx = [94midx + 1
                      mcontinue 
      else:
          [94ms = 0
          [94ms = 0
          [94midx = 0
          mwhile [94midx < mexchangesm.lengthm:
              mem[0] = mexchangesm[[94midxm]m.field_0
              mem[32] = 1
              require ext_code.size(mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m])
              call mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m].isEnabled() with:
                   gas gas_remaining wei
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if ext_call.return_data[0]:
                      mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                      mem[164] = m_amount
                      require ext_code.size(mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m])
                      call mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m].getPrice(address sourceAddress, address destAddress, uint256 amount) with:
                           gas gas_remaining wei
                          args addr(m_sourceAddress), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, m_amount
                      mem[96 len 64] = ext_call.return_data[0 len 64]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if ext_call.return_data[32] >=′ 0:
                                  if ext_call.return_data[32] <′ -1:
                                      [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                                      [94ms = mexchangesm[[94midxm]m.field_0
                                      [94midx = [94midx + 1
                                      mcontinue 
                                  else:
                                      [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                                      [94ms = mexchangesm[[94midxm]m.field_0
                                      [94midx = [94midx + 1
                                      mcontinue 
                              else:
                                  [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                                  [94ms = mexchangesm[[94midxm]m.field_0
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                              [94ms = mexchangesm[[94midxm]m.field_0
                              [94midx = [94midx + 1
                              mcontinue 
                  else:
                      [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                      [94ms = mexchangesm[[94midxm]m.field_0
                      [94midx = [94midx + 1
                      mcontinue 
      return 0
  require ext_code.size(mexchangeAdaptersm[m_exchangeIdm])
  call mexchangeAdaptersm[m_exchangeIdm].getPrice(address sourceAddress, address destAddress, uint256 amount) with:
       gas gas_remaining wei
      args addr(m_sourceAddress), addr(m_destAddress), m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[0], ext_call.return_data[32]


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x7eda80c2
# getter = None
# const = None
# payable = False
def pickExchange(address m_token, uint256 m_amount, uint256 m_rate, bool m_isBuying): # not payable
  [94ms = 0
  [94ms = 0
  [94midx = 0
  mwhile [94midx < mexchangesm.lengthm:
      mem[0] = mexchangesm[[94midxm]m.field_0
      mem[32] = 1
      require ext_code.size(mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m])
      call mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m].isEnabled() with:
           gas gas_remaining wei
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          if ext_call.return_data[0]:
              if not m_isBuying:
                  mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[164] = m_amount
                  require ext_code.size(mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m])
                  call mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m].getPrice(address sourceAddress, address destAddress, uint256 amount) with:
                       gas gas_remaining wei
                      args addr(m_token), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, m_amount
                  mem[96 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 64
                      if ext_call.return_data[0]:
                          if ext_call.return_data[32] >=′ m_rate:
                              if ext_call.return_data[32] <′ -1:
                                  [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                                  [94ms = mexchangesm[[94midxm]m.field_0
                                  [94midx = [94midx + 1
                                  mcontinue 
                              else:
                                  [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                                  [94ms = mexchangesm[[94midxm]m.field_0
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                              [94ms = mexchangesm[[94midxm]m.field_0
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                          [94ms = mexchangesm[[94midxm]m.field_0
                          [94midx = [94midx + 1
                          mcontinue 
              else:
                  mem[132] = m_token
                  mem[164] = m_amount
                  require ext_code.size(mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m])
                  call mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m].getPrice(address sourceAddress, address destAddress, uint256 amount) with:
                       gas gas_remaining wei
                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(m_token), m_amount
                  mem[96 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 64
                      if ext_call.return_data[0]:
                          if ext_call.return_data[32] >=′ m_rate:
                              if ext_call.return_data[32] <′ -1:
                                  [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                                  [94ms = mexchangesm[[94midxm]m.field_0
                                  [94midx = [94midx + 1
                                  mcontinue 
                              else:
                                  [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                                  [94ms = mexchangesm[[94midxm]m.field_0
                                  [94midx = [94midx + 1
                                  mcontinue 
                          else:
                              [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                              [94ms = mexchangesm[[94midxm]m.field_0
                              [94midx = [94midx + 1
                              mcontinue 
                      else:
                          [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
                          [94ms = mexchangesm[[94midxm]m.field_0
                          [94midx = [94midx + 1
                          mcontinue 
          else:
              [94ms = mexchangeAdaptersm[mstor2m[[94midxm]m.field_0m]
              [94ms = mexchangesm[[94midxm]m.field_0
              [94midx = [94midx + 1
              mcontinue 
  return 0


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x8fe13b92
# getter = None
# const = None
# payable = False
def addExchange(bytes32 m_name, address m_adapter): # not payable
  require caller == mowner
  require m_adapter
  uint256(mstor3m.field_0)++
  require ext_code.size(m_adapter)
  call m_adapter.setExchangeDetails(bytes32 id, bytes32 name) with:
       gas gas_remaining wei
      args sha3(m_adapter, Mask(96, 0, mstor3m.field_160), addr(mstor3m.field_0)), m_name
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mexchangesm.length++
  mexchangesm[mexchangesm.lengthm]m.field_0 = sha3(m_adapter, Mask(96, 0, mstor3m.field_160), addr(mstor3m.field_0))
  mexchangeAdaptersm[m_adapterm][Mask(96, 0, mstor3m.field_160)m][addr(mstor3m.field_0)m] = m_adapter
  mstor4m[addr(m_adapter)m]++
  log AddedExchange(bytes32 id=sha3(_adapter, Mask(96, 0, stor3.field_160), addr(stor3.field_0)))
  return 1


# hash = 0xbd5bda09
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def exchangeAdapters(bytes32 m_param1): # not payable
  return mexchangeAdaptersm[m_param1m]


# hash = 0xccff42b2
# getter = None
# const = None
# payable = False
def isValidAdapter(address m_adapter): # not payable
  return (mstor4m[addr(m_adapter)m] > 0)


# hash = 0xde6cdd2e
# getter = None
# const = None
# payable = False
def getExchangeInfo(bytes32 m_id): # not payable
  require mexchangeAdaptersm[m_idm]
  require ext_code.size(mexchangeAdaptersm[m_idm])
  call mexchangeAdaptersm[m_idm].getExchangeDetails() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[0], bool(ext_call.return_data[32])


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


