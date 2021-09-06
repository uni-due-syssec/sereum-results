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
def getExchangeAdapter(bytes32 _id): # not payable
  return exchangeAdapters[_id]


# hash = 0x1ddfd7db
# getter = None
# const = None
# payable = False
def supportsTradingPair(address _srcAddress, address _destAddress, bytes32 _exchangeId): # not payable
  if not _exchangeId:
      [94ms = 0
      [94midx = 0
      [94ms = 0
      while [94midx < exchanges.length:
          mem[0] = exchanges[[94midx].field_0
          mem[32] = 1
          require ext_code.size(exchangeAdapters[stor2[[94midx].field_0])
          call exchangeAdapters[stor2[[94midx].field_0].isEnabled() with:
               gas gas_remaining wei
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94ms = exchanges[[94midx].field_0
              [94midx = [94midx + 1
              [94ms = exchangeAdapters[stor2[[94midx].field_0]
              continue 
          mem[100] = _srcAddress
          mem[132] = _destAddress
          require ext_code.size(exchangeAdapters[stor2[[94midx].field_0])
          call exchangeAdapters[stor2[[94midx].field_0].supportsTradingPair(address srcAddress, address destAddress) with:
               gas gas_remaining wei
              args addr(_srcAddress), _destAddress
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94ms = exchanges[[94midx].field_0
              [94midx = [94midx + 1
              [94ms = exchangeAdapters[stor2[[94midx].field_0]
              continue 
          return 1
      return 0
  require ext_code.size(exchangeAdapters[0])
  call exchangeAdapters[0].isEnabled() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  require ext_code.size(exchangeAdapters[0])
  call exchangeAdapters[0].supportsTradingPair(address srcAddress, address destAddress) with:
       gas gas_remaining wei
      args addr(_srcAddress), _destAddress
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
  if not exchanges.length:
      mem[(32 * exchanges.length) + 128] = 32
      mem[(32 * exchanges.length) + 160] = exchanges.length
      mem[(32 * exchanges.length) + 192 len floor32(exchanges.length)] = mem[128 len floor32(exchanges.length)]
      return memory
        from (32 * exchanges.length) + 128
         [93mlen (96 * exchanges.length) + 64
  mem[128] = uint256(exchanges.field_0)
  [94midx = 128
  [94ms = 0
  while (32 * exchanges.length) + 96 > [94midx:
      mem[[94midx + 32] = exchanges[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * exchanges.length) + 192 len floor32(exchanges.length)] = mem[128 len floor32(exchanges.length)]
  return Array(len=exchanges.length, data=mem[128 len floor32(exchanges.length)], mem[(32 * exchanges.length) + floor32(exchanges.length) + 192 len (32 * exchanges.length) - floor32(exchanges.length)]), 


# hash = 0x2839fc29
# getter = ['storage', 256, 0, ['add', ['sha3', 2], ['cd', 4]]]
# const = None
# payable = False
def exchanges(uint256 _param1): # not payable
  require _param1 < exchanges.length
  return exchanges[_param1].field_0


# hash = 0x4fbe0858
# getter = None
# const = None
# payable = False
def unknown4fbe0858(uint256 _param1): # not payable
  require caller == owner
  [94midx = 0
  while [94midx < exchanges.length:
      mem[0] = 2
      if exchanges[[94midx].field_0 != _param1:
          [94midx = [94midx + 1
          continue 
      if [94midx >= exchanges.length:
          return 0
      [94ms = [94midx
      while [94ms < exchanges.length - 1:
          require [94ms + 1 < exchanges.length
          require [94ms < exchanges.length
          mem[0] = 2
          exchanges[[94ms].field_0 = exchanges[[94ms].field_256
          [94ms = [94ms + 1
          continue 
      exchanges.length--
      if exchanges.length > exchanges.length - 1:
          [94midx = exchanges.length + sha3(2) - 1
          while sha3(2) + exchanges.length > [94midx:
              stor[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      return 1
  return 0


# hash = 0x5fc6b623
# getter = None
# const = None
# payable = False
def getPrice(address _sourceAddress, address _destAddress, uint256 _amount, bytes32 _exchangeId): # not payable
  if not _exchangeId:
      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _sourceAddress:
          [94ms = 0
          [94ms = 0
          [94midx = 0
          while [94midx < exchanges.length:
              mem[0] = exchanges[[94midx].field_0
              mem[32] = 1
              require ext_code.size(exchangeAdapters[stor2[[94midx].field_0])
              call exchangeAdapters[stor2[[94midx].field_0].isEnabled() with:
                   gas gas_remaining wei
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if ext_call.return_data[0]:
                      mem[132] = _destAddress
                      mem[164] = _amount
                      require ext_code.size(exchangeAdapters[stor2[[94midx].field_0])
                      call exchangeAdapters[stor2[[94midx].field_0].getPrice(address sourceAddress, address destAddress, uint256 amount) with:
                           gas gas_remaining wei
                          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(_destAddress), _amount
                      mem[96 len 64] = ext_call.return_data[0 len 64]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if ext_call.return_data[32] >=′ 0:
                                  if ext_call.return_data[32] <′ -1:
                                      [94ms = exchangeAdapters[stor2[[94midx].field_0]
                                      [94ms = exchanges[[94midx].field_0
                                      [94midx = [94midx + 1
                                      continue 
                                  else:
                                      [94ms = exchangeAdapters[stor2[[94midx].field_0]
                                      [94ms = exchanges[[94midx].field_0
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  [94ms = exchangeAdapters[stor2[[94midx].field_0]
                                  [94ms = exchanges[[94midx].field_0
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              [94ms = exchangeAdapters[stor2[[94midx].field_0]
                              [94ms = exchanges[[94midx].field_0
                              [94midx = [94midx + 1
                              continue 
                  else:
                      [94ms = exchangeAdapters[stor2[[94midx].field_0]
                      [94ms = exchanges[[94midx].field_0
                      [94midx = [94midx + 1
                      continue 
      else:
          [94ms = 0
          [94ms = 0
          [94midx = 0
          while [94midx < exchanges.length:
              mem[0] = exchanges[[94midx].field_0
              mem[32] = 1
              require ext_code.size(exchangeAdapters[stor2[[94midx].field_0])
              call exchangeAdapters[stor2[[94midx].field_0].isEnabled() with:
                   gas gas_remaining wei
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if ext_call.return_data[0]:
                      mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                      mem[164] = _amount
                      require ext_code.size(exchangeAdapters[stor2[[94midx].field_0])
                      call exchangeAdapters[stor2[[94midx].field_0].getPrice(address sourceAddress, address destAddress, uint256 amount) with:
                           gas gas_remaining wei
                          args addr(_sourceAddress), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _amount
                      mem[96 len 64] = ext_call.return_data[0 len 64]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if ext_call.return_data[32] >=′ 0:
                                  if ext_call.return_data[32] <′ -1:
                                      [94ms = exchangeAdapters[stor2[[94midx].field_0]
                                      [94ms = exchanges[[94midx].field_0
                                      [94midx = [94midx + 1
                                      continue 
                                  else:
                                      [94ms = exchangeAdapters[stor2[[94midx].field_0]
                                      [94ms = exchanges[[94midx].field_0
                                      [94midx = [94midx + 1
                                      continue 
                              else:
                                  [94ms = exchangeAdapters[stor2[[94midx].field_0]
                                  [94ms = exchanges[[94midx].field_0
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              [94ms = exchangeAdapters[stor2[[94midx].field_0]
                              [94ms = exchanges[[94midx].field_0
                              [94midx = [94midx + 1
                              continue 
                  else:
                      [94ms = exchangeAdapters[stor2[[94midx].field_0]
                      [94ms = exchanges[[94midx].field_0
                      [94midx = [94midx + 1
                      continue 
      return 0
  require ext_code.size(exchangeAdapters[_exchangeId])
  call exchangeAdapters[_exchangeId].getPrice(address sourceAddress, address destAddress, uint256 amount) with:
       gas gas_remaining wei
      args addr(_sourceAddress), addr(_destAddress), _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[0], ext_call.return_data[32]


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipRenounced(address previousOwner=owner)
  owner = 0


# hash = 0x7eda80c2
# getter = None
# const = None
# payable = False
def pickExchange(address _token, uint256 _amount, uint256 _rate, bool _isBuying): # not payable
  [94ms = 0
  [94ms = 0
  [94midx = 0
  while [94midx < exchanges.length:
      mem[0] = exchanges[[94midx].field_0
      mem[32] = 1
      require ext_code.size(exchangeAdapters[stor2[[94midx].field_0])
      call exchangeAdapters[stor2[[94midx].field_0].isEnabled() with:
           gas gas_remaining wei
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          if ext_call.return_data[0]:
              if not _isBuying:
                  mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[164] = _amount
                  require ext_code.size(exchangeAdapters[stor2[[94midx].field_0])
                  call exchangeAdapters[stor2[[94midx].field_0].getPrice(address sourceAddress, address destAddress, uint256 amount) with:
                       gas gas_remaining wei
                      args addr(_token), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _amount
                  mem[96 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 64
                      if ext_call.return_data[0]:
                          if ext_call.return_data[32] >=′ _rate:
                              if ext_call.return_data[32] <′ -1:
                                  [94ms = exchangeAdapters[stor2[[94midx].field_0]
                                  [94ms = exchanges[[94midx].field_0
                                  [94midx = [94midx + 1
                                  continue 
                              else:
                                  [94ms = exchangeAdapters[stor2[[94midx].field_0]
                                  [94ms = exchanges[[94midx].field_0
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              [94ms = exchangeAdapters[stor2[[94midx].field_0]
                              [94ms = exchanges[[94midx].field_0
                              [94midx = [94midx + 1
                              continue 
                      else:
                          [94ms = exchangeAdapters[stor2[[94midx].field_0]
                          [94ms = exchanges[[94midx].field_0
                          [94midx = [94midx + 1
                          continue 
              else:
                  mem[132] = _token
                  mem[164] = _amount
                  require ext_code.size(exchangeAdapters[stor2[[94midx].field_0])
                  call exchangeAdapters[stor2[[94midx].field_0].getPrice(address sourceAddress, address destAddress, uint256 amount) with:
                       gas gas_remaining wei
                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(_token), _amount
                  mem[96 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 64
                      if ext_call.return_data[0]:
                          if ext_call.return_data[32] >=′ _rate:
                              if ext_call.return_data[32] <′ -1:
                                  [94ms = exchangeAdapters[stor2[[94midx].field_0]
                                  [94ms = exchanges[[94midx].field_0
                                  [94midx = [94midx + 1
                                  continue 
                              else:
                                  [94ms = exchangeAdapters[stor2[[94midx].field_0]
                                  [94ms = exchanges[[94midx].field_0
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              [94ms = exchangeAdapters[stor2[[94midx].field_0]
                              [94ms = exchanges[[94midx].field_0
                              [94midx = [94midx + 1
                              continue 
                      else:
                          [94ms = exchangeAdapters[stor2[[94midx].field_0]
                          [94ms = exchanges[[94midx].field_0
                          [94midx = [94midx + 1
                          continue 
          else:
              [94ms = exchangeAdapters[stor2[[94midx].field_0]
              [94ms = exchanges[[94midx].field_0
              [94midx = [94midx + 1
              continue 
  return 0


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8fe13b92
# getter = None
# const = None
# payable = False
def addExchange(bytes32 _name, address _adapter): # not payable
  require caller == owner
  require _adapter
  uint256(stor3.field_0)++
  require ext_code.size(_adapter)
  call _adapter.setExchangeDetails(bytes32 id, bytes32 name) with:
       gas gas_remaining wei
      args sha3(_adapter, Mask(96, 0, stor3.field_160), addr(stor3.field_0)), _name
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  exchanges.length++
  exchanges[exchanges.length].field_0 = sha3(_adapter, Mask(96, 0, stor3.field_160), addr(stor3.field_0))
  exchangeAdapters[_adapter][Mask(96, 0, stor3.field_160)][addr(stor3.field_0)] = _adapter
  stor4[addr(_adapter)]++
  log AddedExchange(bytes32 id=sha3(_adapter, Mask(96, 0, stor3.field_160), addr(stor3.field_0)))
  return 1


# hash = 0xbd5bda09
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def exchangeAdapters(bytes32 _param1): # not payable
  return exchangeAdapters[_param1]


# hash = 0xccff42b2
# getter = None
# const = None
# payable = False
def isValidAdapter(address _adapter): # not payable
  return (stor4[addr(_adapter)] > 0)


# hash = 0xde6cdd2e
# getter = None
# const = None
# payable = False
def getExchangeInfo(bytes32 _id): # not payable
  require exchangeAdapters[_id]
  require ext_code.size(exchangeAdapters[_id])
  call exchangeAdapters[_id].getExchangeDetails() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[0], bool(ext_call.return_data[32])


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require caller == owner
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


