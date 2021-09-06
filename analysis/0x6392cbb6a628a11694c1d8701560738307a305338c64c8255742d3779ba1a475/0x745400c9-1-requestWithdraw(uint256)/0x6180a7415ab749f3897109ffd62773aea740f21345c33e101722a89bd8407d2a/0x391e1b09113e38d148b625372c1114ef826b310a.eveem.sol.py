# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x391e1b09113e38d148b625372C1114Ef826b310a 
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
    stor6 # mask: a s
# hash = 0x06fdde03
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def name(): # not payable
  return mname


# hash = 0x1878d1f1
# getter = None
# const = ['return', 1364068194842176056990105843868530818345537040110]
# payable = False
const ETH_TOKEN_ADDRESS = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


# hash = 0x2e1a7d4d
# getter = None
# const = None
# payable = False
def withdraw(uint256 m_wdamount): # not payable
  require caller == mowner
  require m_wdamount <= eth.balance(this.address)
  if m_wdamount:
      call caller with:
         value m_wdamount wei
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
  require caller == mowner
  mstor6 = 0
  return 1


# hash = 0x334f5401
# getter = None
# const = None
# payable = True
def unknown334f5401(addr m_param1, addr m_param2, uint256 m_param3, uint256 m_param4, addr m_param5) payable: 
  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == m_param1:
      require m_param3 == call.value
      if m_param3 > eth.balance(this.address):
          return 0
  else:
      require not call.value
      require ext_code.size(m_param1)
      call m_param1.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args mkyberAddress, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(m_param1)
      call m_param1.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args mkyberAddress, m_param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == m_param2:
      require ext_code.size(mkyberAddress)
      call mkyberAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
           gas gas_remaining wei
          args addr(m_param1), addr(m_param2), m_param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if ext_call.return_data[32] < m_param4:
          return 0
      require ext_code.size(mkyberAddress)
      call mkyberAddress.trade(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId) with:
         value call.value wei
           gas gas_remaining wei
          args 0, ext_call.return_data[32], uint32(m_param3), addr(m_param2), addr(m_param5), -1, m_param4, mwalletIdAddress
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == m_param2:
          require eth.balance(m_param5) < eth.balance(m_param5)
      else:
          require ext_code.size(m_param2)
          call m_param2.balanceOf(address owner) with:
               gas gas_remaining wei
              args m_param5
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] > 0
  else:
      require ext_code.size(m_param2)
      call m_param2.balanceOf(address owner) with:
           gas gas_remaining wei
          args m_param5
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(mkyberAddress)
      call mkyberAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
           gas gas_remaining wei
          args addr(m_param1), addr(m_param2), m_param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if ext_call.return_data[32] < m_param4:
          return 0
      require ext_code.size(mkyberAddress)
      call mkyberAddress.trade(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId) with:
         value call.value wei
           gas gas_remaining wei
          args 0, ext_call.return_data[32], uint32(m_param3), addr(m_param2), addr(m_param5), -1, m_param4, mwalletIdAddress
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == m_param2:
          require 0 < eth.balance(m_param5)
      else:
          require ext_code.size(m_param2)
          call m_param2.balanceOf(address owner) with:
               gas gas_remaining wei
              args m_param5
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] > ext_call.return_data[0]
  return 1


# hash = 0x42bff0d0
# getter = None
# const = None
# payable = False
def setExchangeAdapterManager(address m_exchangeAdapterManager): # not payable
  require caller == mowner
  mexchangeAdapterManagerAddress = m_exchangeAdapterManager


# hash = 0x4dafdc50
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def exchangeId(): # not payable
  return mexchangeId


# hash = 0x4edba7bf
# getter = ['bool', ['storage', 8, 160, 6]]
# const = None
# payable = False
def adapterEnabled(): # not payable
  return bool(mstor6)


# hash = 0x5cd87c71
# getter = None
# const = None
# payable = False
def supportsTradingPair(address m_srcAddress, address m_destAddress): # not payable
  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == m_srcAddress:
      require ext_code.size(this.address)
      call this.address.getPrice(address sourceAddress, address destAddress, uint256 amount) with:
           gas gas_remaining wei
          args addr(m_srcAddress), addr(m_destAddress), 10^18
  else:
      require ext_code.size(m_srcAddress)
      call m_srcAddress.decimals() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(this.address)
      call this.address.getPrice(address sourceAddress, address destAddress, uint256 amount) with:
           gas gas_remaining wei
          args addr(m_srcAddress), addr(m_destAddress), 10^ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return (0 < ext_call.return_data[0])


# hash = 0x6601cd77
# getter = None
# const = None
# payable = False
def getExchangeDetails(): # not payable
  return mname, bool(mstor6)


# hash = 0x6aa633b6
# getter = ['bool', ['storage', 8, 160, 6]]
# const = None
# payable = False
def isEnabled(): # not payable
  return bool(mstor6)


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x80b2edd8
# getter = None
# const = None
# payable = False
def unknown80b2edd8(addr m_param1): # not payable
  require ext_code.size(m_param1)
  call m_param1.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown9efe1cd2Address, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(m_param1)
  call m_param1.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown9efe1cd2Address, 0x8000000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x926b7769
# getter = None
# const = None
# payable = False
def unknown926b7769(addr m_param1): # not payable
  require caller == mowner
  munknown9efe1cd2Address = m_param1


# hash = 0x9efe1cd2
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknown9efe1cd2(): # not payable
  return munknown9efe1cd2Address


# hash = 0xa09c996f
# getter = None
# const = None
# payable = True
def buyToken(address m_token, uint256 m_amount, uint256 m_minimumRate, address m_depositAddress) payable: 
  if m_amount > eth.balance(this.address):
      return 0
  require m_amount == call.value
  require ext_code.size(mkyberAddress)
  call mkyberAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
       gas gas_remaining wei
      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(m_token), m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if ext_call.return_data[32] < m_minimumRate:
      return 0
  require ext_code.size(m_token)
  call m_token.balanceOf(address owner) with:
       gas gas_remaining wei
      args m_depositAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mkyberAddress)
  call mkyberAddress.trade(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId) with:
     value call.value wei
       gas gas_remaining wei
      args 0, ext_call.return_data[32], uint32(m_amount), addr(m_token), addr(m_depositAddress), -1, m_minimumRate, mwalletIdAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_token)
  call m_token.balanceOf(address owner) with:
       gas gas_remaining wei
      args m_depositAddress
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
  return mkyberAddress


# hash = 0xa3907d71
# getter = None
# const = None
# payable = False
def enable(): # not payable
  require caller == mowner
  mstor6 = 1
  return 1


# hash = 0xa9dd14d6
# getter = None
# const = None
# payable = False
def getPrice(address m_sourceAddress, address m_destAddress, uint256 m_amount): # not payable
  require ext_code.size(mkyberAddress)
  call mkyberAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
       gas gas_remaining wei
      args addr(m_sourceAddress), addr(m_destAddress), m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[0], ext_call.return_data[32]


# hash = 0xc162ba2f
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def walletId(): # not payable
  return mwalletIdAddress


# hash = 0xca626232
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def exchangeAdapterManager(): # not payable
  return mexchangeAdapterManagerAddress


# hash = 0xce22958b
# getter = None
# const = None
# payable = False
def sellToken(address m_token, uint256 m_amount, uint256 m_minimumRate, address m_depositAddress): # not payable
  require ext_code.size(m_token)
  call m_token.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mkyberAddress, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(m_token)
  call m_token.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mkyberAddress, m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(mkyberAddress)
  call mkyberAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
       gas gas_remaining wei
      args addr(m_token), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if ext_call.return_data[32] < m_minimumRate:
      return 0
  require ext_code.size(mkyberAddress)
  call mkyberAddress.trade(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId) with:
       gas gas_remaining wei
      args 0, ext_call.return_data[32], uint32(m_amount), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(m_depositAddress), -1, m_minimumRate, mwalletIdAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 1


# hash = 0xdda89912
# getter = None
# const = None
# payable = False
def setExchangeDetails(bytes32 m_id, bytes32 m_name): # not payable
  require caller == mexchangeAdapterManagerAddress
  mexchangeId = m_id
  mname = m_name
  return 1


# hash = 0xf0bb2af7
# getter = None
# const = None
# payable = False
def configAdapter(address m_kyber, address m_walletId): # not payable
  require caller == mowner
  if m_kyber:
      mkyberAddress = m_kyber
  if m_walletId:
      mwalletIdAddress = m_walletId
  return 1


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


