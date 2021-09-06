# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x3BB0754eaFe418e336A269906eFCDCc94FfF1454 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    kyberAddress # mask: a s
    # storage address 2
    exchangeAdapterManagerAddress # mask: a s
    # storage address 3
    unknown9efe1cd2Address # mask: a s
    # storage address 4
    exchangeId # mask: a s
    # storage address 5
    name # mask: a s
    # storage address 6
    walletIdAddress # mask: a s
    # storage address 6
    isEnabled # mask: a s
    # storage address 7
    unknowna91fbf9a
# hash = 0x01d16cec
# getter = None
# const = None
# payable = False
def unknown01d16cec(): # not payable
  require caller == owner
  unknowna91fbf9a.length = ('cd', 4).length
  if not ('cd', 4).length:
      [94midx = 0
      while unknowna91fbf9a.length > [94midx:
          unknowna91fbf9a[[94midx].field_0 = 0
          [94midx = [94midx + 1
          continue 
  else:
      [94ms = 0
      [94midx = cd[4] + 36
      while cd[4] + (32 * ('cd', 4).length) + 36 > [94midx:
          unknowna91fbf9a[[94ms].field_0 = addr(cd[[94midx])
          [94ms = [94ms + 1
          [94midx = [94midx + 32
          continue 
      [94midx = Mask(251, 0, (32 * ('cd', 4).length) + 31) >> 5
      while unknowna91fbf9a.length > [94midx:
          unknowna91fbf9a[[94midx].field_0 = 0
          [94midx = [94midx + 1
          continue 
  return 1


# hash = 0x06fdde03
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def name(): # not payable
  return name


# hash = 0x1878d1f1
# getter = None
# const = ['return', 1364068194842176056990105843868530818345537040110]
# payable = False
const ETH_TOKEN_ADDRESS = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


# hash = 0x2e1a7d4d
# getter = None
# const = None
# payable = False
def withdraw(uint256 _wdamount): # not payable
  require caller == owner
  require _wdamount <= eth.balance(this.address)
  if _wdamount:
      call caller with:
         value _wdamount wei
           gas 2300 * is_zero(value) wei
  else:
      call caller with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x2f2770db
# getter = None
# const = None
# payable = False
def disable(): # not payable
  require caller == owner
  isEnabled = 0
  return 1


# hash = 0x334f5401
# getter = None
# const = None
# payable = True
def unknown334f5401(addr _param1, addr _param2, uint256 _param3, uint256 _param4, addr _param5) payable: 
  [94midx = 0
  while [94midx < unknowna91fbf9a.length:
      mem[0] = 7
      if unknowna91fbf9a[[94midx].field_0 == _param2:
          revert with 0, 'broken token'
      [94midx = [94midx + 1
      continue 
  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _param1:
      require _param3 == call.value
      if _param3 > eth.balance(this.address):
          return 0
  else:
      require not call.value
      require ext_code.size(_param1)
      call _param1.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args kyberAddress, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(_param1)
      call _param1.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args kyberAddress, _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _param2:
      require ext_code.size(kyberAddress)
      call kyberAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
           gas gas_remaining wei
          args addr(_param1), addr(_param2), _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if ext_call.return_data[32] < _param4:
          return 0
      require ext_code.size(kyberAddress)
      call kyberAddress.trade(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId) with:
         value call.value wei
           gas gas_remaining wei
          args 0, ext_call.return_data[32], uint32(_param3), addr(_param2), addr(_param5), -1, _param4, walletIdAddress
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _param2:
          require eth.balance(_param5) < eth.balance(_param5)
      else:
          require ext_code.size(_param2)
          call _param2.balanceOf(address owner) with:
               gas gas_remaining wei
              args _param5
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] > 0
  else:
      require ext_code.size(_param2)
      call _param2.balanceOf(address owner) with:
           gas gas_remaining wei
          args _param5
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(kyberAddress)
      call kyberAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
           gas gas_remaining wei
          args addr(_param1), addr(_param2), _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if ext_call.return_data[32] < _param4:
          return 0
      require ext_code.size(kyberAddress)
      call kyberAddress.trade(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId) with:
         value call.value wei
           gas gas_remaining wei
          args 0, ext_call.return_data[32], uint32(_param3), addr(_param2), addr(_param5), -1, _param4, walletIdAddress
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _param2:
          require 0 < eth.balance(_param5)
      else:
          require ext_code.size(_param2)
          call _param2.balanceOf(address owner) with:
               gas gas_remaining wei
              args _param5
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] > ext_call.return_data[0]
  return 1


# hash = 0x42bff0d0
# getter = None
# const = None
# payable = False
def setExchangeAdapterManager(address _exchangeAdapterManager): # not payable
  require caller == owner
  exchangeAdapterManagerAddress = _exchangeAdapterManager


# hash = 0x4dafdc50
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def exchangeId(): # not payable
  return exchangeId


# hash = 0x4edba7bf
# getter = ['bool', ['storage', 8, 160, 6]]
# const = None
# payable = False
def adapterEnabled(): # not payable
  return bool(isEnabled)


# hash = 0x5cd87c71
# getter = None
# const = None
# payable = False
def supportsTradingPair(address _srcAddress, address _destAddress): # not payable
  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _srcAddress:
      require ext_code.size(this.address)
      call this.address.getPrice(address sourceAddress, address destAddress, uint256 amount) with:
           gas gas_remaining wei
          args addr(_srcAddress), addr(_destAddress), 10^18
  else:
      require ext_code.size(_srcAddress)
      call _srcAddress.decimals() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(this.address)
      call this.address.getPrice(address sourceAddress, address destAddress, uint256 amount) with:
           gas gas_remaining wei
          args addr(_srcAddress), addr(_destAddress), 10^ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return (0 < ext_call.return_data[0])


# hash = 0x6601cd77
# getter = None
# const = None
# payable = False
def getExchangeDetails(): # not payable
  return name, bool(isEnabled)


# hash = 0x6aa633b6
# getter = ['bool', ['storage', 8, 160, 6]]
# const = None
# payable = False
def isEnabled(): # not payable
  return bool(isEnabled)


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipRenounced(address previousOwner=owner)
  owner = 0


# hash = 0x80b2edd8
# getter = None
# const = None
# payable = False
def unknown80b2edd8(addr _param1): # not payable
  require ext_code.size(_param1)
  call _param1.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args unknown9efe1cd2Address, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(_param1)
  call _param1.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args unknown9efe1cd2Address, 0x8000000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x926b7769
# getter = None
# const = None
# payable = False
def unknown926b7769(addr _param1): # not payable
  require caller == owner
  unknown9efe1cd2Address = _param1


# hash = 0x9efe1cd2
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknown9efe1cd2(): # not payable
  return unknown9efe1cd2Address


# hash = 0xa09c996f
# getter = None
# const = None
# payable = True
def buyToken(address _token, uint256 _amount, uint256 _minimumRate, address _depositAddress) payable: 
  [94midx = 0
  while [94midx < unknowna91fbf9a.length:
      mem[0] = 7
      if unknowna91fbf9a[[94midx].field_0 == _token:
          revert with 0, 'broken token'
      [94midx = [94midx + 1
      continue 
  if _amount > eth.balance(this.address):
      return 0
  require _amount == call.value
  require ext_code.size(kyberAddress)
  call kyberAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
       gas gas_remaining wei
      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(_token), _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if ext_call.return_data[32] < _minimumRate:
      return 0
  require ext_code.size(_token)
  call _token.balanceOf(address owner) with:
       gas gas_remaining wei
      args _depositAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(kyberAddress)
  call kyberAddress.trade(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId) with:
     value call.value wei
       gas gas_remaining wei
      args 0, ext_call.return_data[32], uint32(_amount), addr(_token), addr(_depositAddress), -1, _minimumRate, walletIdAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(_token)
  call _token.balanceOf(address owner) with:
       gas gas_remaining wei
      args _depositAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] > ext_call.return_data[0]
  return 1


# hash = 0xa2d10ba5
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def kyber(): # not payable
  return kyberAddress


# hash = 0xa3907d71
# getter = None
# const = None
# payable = False
def enable(): # not payable
  require caller == owner
  isEnabled = 1
  return 1


# hash = 0xa91fbf9a
# getter = ['storage', 160, 0, ['add', ['sha3', 7], ['cd', 4]]]
# const = None
# payable = False
def unknowna91fbf9a(uint256 _param1): # not payable
  require _param1 < unknowna91fbf9a.length
  return unknowna91fbf9a[_param1].field_0


# hash = 0xa9dd14d6
# getter = None
# const = None
# payable = False
def getPrice(address _sourceAddress, address _destAddress, uint256 _amount): # not payable
  [94midx = 0
  while [94midx < unknowna91fbf9a.length:
      mem[0] = 7
      if unknowna91fbf9a[[94midx].field_0 != _destAddress:
          [94midx = [94midx + 1
          continue 
      else:
          return 0
  require ext_code.size(kyberAddress)
  call kyberAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
       gas gas_remaining wei
      args addr(_sourceAddress), addr(_destAddress), _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[0], ext_call.return_data[32]


# hash = 0xc162ba2f
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def walletId(): # not payable
  return walletIdAddress


# hash = 0xca626232
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def exchangeAdapterManager(): # not payable
  return exchangeAdapterManagerAddress


# hash = 0xce22958b
# getter = None
# const = None
# payable = False
def sellToken(address _token, uint256 _amount, uint256 _minimumRate, address _depositAddress): # not payable
  [94midx = 0
  while [94midx < unknowna91fbf9a.length:
      mem[0] = 7
      if unknowna91fbf9a[[94midx].field_0 == _token:
          revert with 0, 'broken token'
      [94midx = [94midx + 1
      continue 
  require ext_code.size(_token)
  call _token.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args kyberAddress, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(_token)
  call _token.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args kyberAddress, _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(kyberAddress)
  call kyberAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
       gas gas_remaining wei
      args addr(_token), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if ext_call.return_data[32] < _minimumRate:
      return 0
  require ext_code.size(kyberAddress)
  call kyberAddress.trade(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId) with:
       gas gas_remaining wei
      args 0, ext_call.return_data[32], uint32(_amount), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(_depositAddress), -1, _minimumRate, walletIdAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 1


# hash = 0xdda89912
# getter = None
# const = None
# payable = False
def setExchangeDetails(bytes32 _id, bytes32 _name): # not payable
  require caller == exchangeAdapterManagerAddress
  exchangeId = _id
  name = _name
  return 1


# hash = 0xe13f20c8
# getter = None
# const = None
# payable = False
def unknowne13f20c8(): # not payable
  if not unknowna91fbf9a.length:
      mem[(32 * unknowna91fbf9a.length) + 128] = 32
      mem[(32 * unknowna91fbf9a.length) + 160] = unknowna91fbf9a.length
      mem[(32 * unknowna91fbf9a.length) + 192 len floor32(unknowna91fbf9a.length)] = mem[128 len floor32(unknowna91fbf9a.length)]
      return memory
        from (32 * unknowna91fbf9a.length) + 128
         [93mlen (96 * unknowna91fbf9a.length) + 64
  mem[128] = addr(unknowna91fbf9a.field_0)
  [94midx = 128
  [94ms = 0
  while (32 * unknowna91fbf9a.length) + 96 > [94midx:
      mem[[94midx + 32] = unknowna91fbf9a[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * unknowna91fbf9a.length) + 192 len floor32(unknowna91fbf9a.length)] = mem[128 len floor32(unknowna91fbf9a.length)]
  return Array(len=unknowna91fbf9a.length, data=mem[128 len floor32(unknowna91fbf9a.length)], mem[(32 * unknowna91fbf9a.length) + floor32(unknowna91fbf9a.length) + 192 len (32 * unknowna91fbf9a.length) - floor32(unknowna91fbf9a.length)]), 


# hash = 0xf0bb2af7
# getter = None
# const = None
# payable = False
def configAdapter(address _kyber, address _walletId): # not payable
  require caller == owner
  if _kyber:
      kyberAddress = _kyber
  if _walletId:
      walletIdAddress = _walletId
  return 1


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


