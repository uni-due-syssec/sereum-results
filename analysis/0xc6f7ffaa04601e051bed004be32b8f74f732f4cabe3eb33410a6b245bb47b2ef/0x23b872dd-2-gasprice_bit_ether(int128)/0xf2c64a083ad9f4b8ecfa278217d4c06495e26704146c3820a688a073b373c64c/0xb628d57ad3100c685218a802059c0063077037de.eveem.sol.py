# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xB628D57aD3100C685218a802059c0063077037de 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
# hash = 0x14d2d884
# getter = None
# const = None
# payable = True
def unknown14d2d884(addr m_param1, addr m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5) payable: 
  require calldata.size - 4 >= 160
  require ext_code.size(m_param1)
  static call m_param1.balanceOf(address owner) with:
          gas gas_remaining wei
         args m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] <= m_param3:
      return 0
  if block.number > m_param5:
      return 0
  require ext_code.size(m_param2)
  call m_param2.ethToTokenSwapInput(uint256 min_tokens, uint256 deadline) with:
     value m_param4 wei
       gas gas_remaining wei
      args 1, block.timestamp
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x3bf148a0
# getter = None
# const = None
# payable = True
def unknown3bf148a0(addr m_param1, addr m_param2, uint256 m_param3) payable: 
  require calldata.size - 4 >= 96
  require ext_code.size(m_param1)
  static call m_param1.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  require ext_code.size(m_param1)
  if ext_call.return_data[0] <= m_param3:
      call m_param1.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args addr(m_param2), ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(m_param2)
      call m_param2.tokenToEthSwapInput(uint256 tokens_sold, uint256 min_eth, uint256 deadline) with:
           gas gas_remaining wei
          args ext_call.return_data[0], 1, block.timestamp
  else:
      call m_param1.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args addr(m_param2), m_param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(m_param2)
      call m_param2.tokenToEthSwapInput(uint256 tokens_sold, uint256 min_eth, uint256 deadline) with:
           gas gas_remaining wei
          args m_param3, 1, block.timestamp
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0xaa94f177
# getter = None
# const = None
# payable = True
def unknownaa94f177(addr m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(m_param1)
  static call m_param1.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  require ext_code.size(m_param1)
  call m_param1.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args addr(m_param2), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_param2)
  call m_param2.tokenToEthSwapInput(uint256 tokens_sold, uint256 min_eth, uint256 deadline) with:
       gas gas_remaining wei
      args ext_call.return_data[0], 1, block.timestamp
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


