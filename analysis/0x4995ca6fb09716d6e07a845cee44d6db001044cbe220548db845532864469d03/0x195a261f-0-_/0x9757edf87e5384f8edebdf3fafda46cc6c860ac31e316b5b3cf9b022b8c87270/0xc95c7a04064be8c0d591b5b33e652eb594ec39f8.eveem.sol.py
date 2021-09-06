# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xC95C7a04064BE8c0d591b5B33E652eB594ec39f8 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x08a6d790': 'unknown08a6d790(?)', '0x353e27cb': 'unknown353e27cb(?)'} 

# storage definitions
def storage:
    # storage address 0
    unknowndce52dfa # mask: a s
# hash = 0x09218e91
# getter = None
# const = ['return', 0]
# payable = False
const unknown09218e91 = 0


# hash = 0x2290a2c6
# getter = None
# const = ['return', 54928375836495650091188001833959803130895678047166071282133256510423296901120]
# payable = False
const unknown2290a2c6 = 0x79705be700000000000000000000000000000000000000000000000000000000


# hash = 0x3e00afba
# getter = None
# const = None
# payable = False
def unknown3e00afba(uint256 m_param1): # not payable
  if not m_param1:
      if not call.data[164]:
          require call.data[196]
          require ext_code.size(caller)
          call caller.0x365a86fc with:
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
          call addr(ext_call.return_data[0]).getReferencePriceInfo(address ofBase, address ofQuote) with:
               gas gas_remaining wei
              args addr(call.data[100]), addr(call.data[68])
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).getOrderPriceInfo(address sellAsset, address buyAsset, uint256 sellQuantity, uint256 buyQuantity) with:
               gas gas_remaining wei
              args addr(call.data[100]), addr(call.data[68]), call.data[228], 0 / call.data[196]
      else:
          require call.data[164]
          if call.data[228] * call.data[164] / call.data[164] != call.data[228]:
              revert with 0, 'ds-math-mul-overflow'
          require call.data[196]
          require ext_code.size(caller)
          call caller.0x365a86fc with:
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
          call addr(ext_call.return_data[0]).getReferencePriceInfo(address ofBase, address ofQuote) with:
               gas gas_remaining wei
              args addr(call.data[100]), addr(call.data[68])
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).getOrderPriceInfo(address sellAsset, address buyAsset, uint256 sellQuantity, uint256 buyQuantity) with:
               gas gas_remaining wei
              args addr(call.data[100]), addr(call.data[68]), call.data[228], call.data[228] * call.data[164] / call.data[196]
  else:
      require ext_code.size(addr(call.data[132]))
      call addr(call.data[132]).getOffer(uint256 id) with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 128
      if not ext_call.return_data[0]:
          require ext_call.return_data[64]
          require ext_code.size(caller)
          call caller.0x365a86fc with:
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
          call addr(ext_call.return_data[0]).getReferencePriceInfo(address ofBase, address ofQuote) with:
               gas gas_remaining wei
              args addr(ext_call.return_data[96]), addr(ext_call.return_data[32])
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).getOrderPriceInfo(address sellAsset, address buyAsset, uint256 sellQuantity, uint256 buyQuantity) with:
               gas gas_remaining wei
              args addr(ext_call.return_data[96]), addr(ext_call.return_data[32]), call.data[228], 0 / ext_call.return_data[64]
      else:
          require ext_call.return_data[0]
          if call.data[228] * ext_call.return_data[0] / ext_call.return_data[0] != call.data[228]:
              revert with 0, 'ds-math-mul-overflow'
          require ext_call.return_data[64]
          require ext_code.size(caller)
          call caller.0x365a86fc with:
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
          call addr(ext_call.return_data[0]).getReferencePriceInfo(address ofBase, address ofQuote) with:
               gas gas_remaining wei
              args addr(ext_call.return_data[96]), addr(ext_call.return_data[32])
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).getOrderPriceInfo(address sellAsset, address buyAsset, uint256 sellQuantity, uint256 buyQuantity) with:
               gas gas_remaining wei
              args addr(ext_call.return_data[96]), addr(ext_call.return_data[32]), call.data[228], call.data[228] * ext_call.return_data[0] / ext_call.return_data[64]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      if ext_call.return_data[0] > ext_call.return_data[0]:
          revert with 0, 'ds-math-sub-underflow'
      return ext_call.return_data[0] <= ext_call.return_data[0]
  require ext_call.return_data[0]
  if munknowndce52dfa * ext_call.return_data[0] / ext_call.return_data[0] != munknowndce52dfa:
      revert with 0, 'ds-math-mul-overflow'
  if ext_call.return_data[0] - (munknowndce52dfa * ext_call.return_data[0] / 10^18) > ext_call.return_data[0]:
      revert with 0, 'ds-math-sub-underflow'
  return ext_call.return_data[0] - (munknowndce52dfa * ext_call.return_data[0] / 10^18) <= ext_call.return_data[0]


# hash = 0x7998a1c4
# getter = None
# const = ['return', ['data', ['arr', 15, ['mask_shl', 120, 0, 0, "'Price tolerance'"]]]]
# payable = False
const identifier = 'Price tolerance'


# hash = 0x8e37f623
# getter = None
# const = None
# payable = False
def unknown8e37f623(addr m_param1, uint256 m_param2, uint256 m_param3): # not payable
  require ext_code.size(m_param1)
  call m_param1.getOffer(uint256 id) with:
       gas gas_remaining wei
      args m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 128
  if not ext_call.return_data[0]:
      require ext_call.return_data[64]
      require ext_code.size(caller)
      call caller.0x365a86fc with:
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
      call addr(ext_call.return_data[0]).getReferencePriceInfo(address ofBase, address ofQuote) with:
           gas gas_remaining wei
          args addr(ext_call.return_data[96]), addr(ext_call.return_data[32])
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).getOrderPriceInfo(address sellAsset, address buyAsset, uint256 sellQuantity, uint256 buyQuantity) with:
           gas gas_remaining wei
          args 0, 0, addr(ext_call.return_data[32]), m_param3, 0 / ext_call.return_data[64]
  else:
      require ext_call.return_data[0]
      if m_param3 * ext_call.return_data[0] / ext_call.return_data[0] != m_param3:
          revert with 0, 'ds-math-mul-overflow'
      require ext_call.return_data[64]
      require ext_code.size(caller)
      call caller.0x365a86fc with:
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
      call addr(ext_call.return_data[0]).getReferencePriceInfo(address ofBase, address ofQuote) with:
           gas gas_remaining wei
          args addr(ext_call.return_data[96]), addr(ext_call.return_data[32])
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).getOrderPriceInfo(address sellAsset, address buyAsset, uint256 sellQuantity, uint256 buyQuantity) with:
           gas gas_remaining wei
          args 0, 0, addr(ext_call.return_data[32]), m_param3, m_param3 * ext_call.return_data[0] / ext_call.return_data[64]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      if ext_call.return_data[0] > ext_call.return_data[0]:
          revert with 0, 'ds-math-sub-underflow'
      return ext_call.return_data[0] <= ext_call.return_data[0]
  require ext_call.return_data[0]
  if munknowndce52dfa * ext_call.return_data[0] / ext_call.return_data[0] != munknowndce52dfa:
      revert with 0, 'ds-math-mul-overflow'
  if ext_call.return_data[0] - (munknowndce52dfa * ext_call.return_data[0] / 10^18) > ext_call.return_data[0]:
      revert with 0, 'ds-math-sub-underflow'
  return ext_call.return_data[0] - (munknowndce52dfa * ext_call.return_data[0] / 10^18) <= ext_call.return_data[0]


# hash = 0xc50a07d6
# getter = None
# const = None
# payable = False
def unknownc50a07d6(addr m_param1, addr m_param2): # not payable
  if not call.data[68]:
      require call.data[100]
      require ext_code.size(caller)
      call caller.0x365a86fc with:
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
      call addr(ext_call.return_data[0]).getReferencePriceInfo(address ofBase, address ofQuote) with:
           gas gas_remaining wei
          args addr(m_param2), m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).getOrderPriceInfo(address sellAsset, address buyAsset, uint256 sellQuantity, uint256 buyQuantity) with:
           gas gas_remaining wei
          args addr(m_param2), addr(m_param1), call.data[132], 0 / call.data[100]
  else:
      require call.data[68]
      if call.data[132] * call.data[68] / call.data[68] != call.data[132]:
          revert with 0, 'ds-math-mul-overflow'
      require call.data[100]
      require ext_code.size(caller)
      call caller.0x365a86fc with:
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
      call addr(ext_call.return_data[0]).getReferencePriceInfo(address ofBase, address ofQuote) with:
           gas gas_remaining wei
          args addr(m_param2), m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).getOrderPriceInfo(address sellAsset, address buyAsset, uint256 sellQuantity, uint256 buyQuantity) with:
           gas gas_remaining wei
          args addr(m_param2), addr(m_param1), call.data[132], call.data[132] * call.data[68] / call.data[100]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      if ext_call.return_data[0] > ext_call.return_data[0]:
          revert with 0, 'ds-math-sub-underflow'
      return ext_call.return_data[0] <= ext_call.return_data[0]
  require ext_call.return_data[0]
  if munknowndce52dfa * ext_call.return_data[0] / ext_call.return_data[0] != munknowndce52dfa:
      revert with 0, 'ds-math-mul-overflow'
  if ext_call.return_data[0] - (munknowndce52dfa * ext_call.return_data[0] / 10^18) > ext_call.return_data[0]:
      revert with 0, 'ds-math-sub-underflow'
  return ext_call.return_data[0] - (munknowndce52dfa * ext_call.return_data[0] / 10^18) <= ext_call.return_data[0]


# hash = 0xdce52dfa
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def unknowndce52dfa(): # not payable
  return munknowndce52dfa


# hash = 0xe9ae57e5
# getter = None
# const = ['return', 103628940852684407923009524072668737776206138074533032731110828308622494138368]
# payable = False
const unknowne9ae57e5 = 0xe51be6e800000000000000000000000000000000000000000000000000000000


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


