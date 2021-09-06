# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x8CB3E810027d97BE5E890257338b9Cc755dE9c67 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = 0x1878d1f1
# getter = None
# const = ['return', 1364068194842176056990105843868530818345537040110]
# payable = False
const ETH_TOKEN_ADDRESS = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


# hash = 0x61346679
# getter = None
# const = None
# payable = False
def unknown61346679(): # not payable
  revert with 0, 'Unimplemented'


# hash = 0x79705be7
# getter = None
# const = None
# payable = False
def unknown79705be7(): # not payable
  revert with 0, 'Unimplemented'


# hash = 0xd7d1c4d5
# getter = None
# const = None
# payable = False
def unknownd7d1c4d5(): # not payable
  revert with 0, 'Unimplemented'


# hash = 0xe51be6e8
# getter = None
# const = None
# payable = False
def unknowne51be6e8(addr m_param1): # not payable
  require ext_code.size(this.address)
  call this.address.0x365a86fc with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).manager() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, 'Manager must be sender'
  require ext_code.size(this.address)
  call this.address.0x365a86fc with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).isShutDown() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      revert with 0, 'Hub must not be shut down'
  require ext_code.size(this.address)
  call this.address.0x365a86fc with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if call.data[420] != call.data[260]:
      revert with 0, 'fillTakerQuantity must equal takerAssetQuantity'
  require ext_code.size(this.address)
  call this.address.0x365a86fc with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x20531bc9 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).getOrderPriceInfo(address sellAsset, address buyAsset, uint256 sellQuantity, uint256 buyQuantity) with:
       gas gas_remaining wei
      args addr(call.data[132]), addr(call.data[100]), call.data[260], call.data[228]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(this.address)
  call this.address.0x365a86fc with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x9624e83e with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).NATIVE_ASSET() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(this.address)
  call this.address.0x365a86fc with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).vault() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  if ext_call.return_data[12 len 20] == addr(call.data[132]):
      call addr(ext_call.return_data[0]).withdraw(address address, uint256 amount) with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), call.data[260]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).withdraw(uint256 wdamount) with:
           gas gas_remaining wei
          args call.data[260]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(m_param1)
      call m_param1.swapEtherToToken(address token, uint256 minConversionRate) with:
         value call.data[260] wei
           gas gas_remaining wei
          args addr(call.data[100]), ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
  else:
      call addr(ext_call.return_data[0]).withdraw(address address, uint256 amount) with:
           gas gas_remaining wei
          args addr(call.data[132]), call.data[260]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(addr(call.data[132]))
      call addr(call.data[132]).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args addr(m_param1), call.data[260]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(m_param1)
      if addr(call.data[100]) != ext_call.return_data[12 len 20]:
          call m_param1.swapTokenToToken(address src, uint256 srcAmount, address dest, uint256 minConversionRate) with:
               gas gas_remaining wei
              args addr(call.data[132]), call.data[260], addr(call.data[100]), ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      else:
          call m_param1.swapTokenToEther(address token, uint256 srcAmount, uint256 minConversionRate) with:
               gas gas_remaining wei
              args addr(call.data[132]), call.data[260], ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).deposit() with:
             value ext_call.return_data[0] wei
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
  if ext_call.return_data[0] < call.data[228]:
      revert with 0, 'Received less than expected from Kyber swap'
  require ext_code.size(this.address)
  call this.address.0x365a86fc with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x9624e83e with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x7afbe74 with:
       gas gas_remaining wei
      args addr(call.data[100])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(this.address)
  call this.address.0x365a86fc with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x9624e83e with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x71b58058 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(this.address)
  call this.address.0x19ab7f43 with:
       gas gas_remaining wei
      args addr(call.data[100])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(this.address)
  call this.address.0x195a261f with:
       gas gas_remaining wei
      args addr(m_param1), 0, 1, addr(call.data[100]), addr(call.data[132]) >> 256, ext_call.return_data[0], call.data[260], call.data[260]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


