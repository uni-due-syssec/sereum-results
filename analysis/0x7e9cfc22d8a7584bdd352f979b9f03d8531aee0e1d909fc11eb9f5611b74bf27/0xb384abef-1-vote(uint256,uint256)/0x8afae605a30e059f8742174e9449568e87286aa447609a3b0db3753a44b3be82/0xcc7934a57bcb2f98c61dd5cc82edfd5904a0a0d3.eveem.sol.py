# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xcC7934a57Bcb2F98C61dd5cC82edFD5904a0a0D3 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    tokenAddress # mask: a s
# hash = 0x19eb8d48
# getter = None
# const = None
# payable = True
def unknown19eb8d48(addr m_param1, uint256 m_param2) payable: 
  call caller.proposals(uint256 param1) with:
       gas gas_remaining - 25050 wei
      args m_param2
  require ext_call.success
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining - 25050 wei
      args m_param1
  if ext_call.return_data[0] <= 0:
      return 0
  if block.timestamp >= ext_call.return_data[224] + ext_call.return_data[192]:
      return 0
  call mtokenAddress.0xc215290a with:
       gas gas_remaining - 25050 wei
      args m_param1
  require ext_call.success
  if ext_call.return_data[0] <= ext_call.return_data[224] + ext_call.return_data[192]:
      return 0
  call caller.hasVoted(uint256 proposalNumber, address shareholder) with:
       gas gas_remaining - 25050 wei
      args m_param2, m_param1
  require ext_call.success
  if ext_call.return_data[0]:
      return 0
  return 1


# hash = 0x42b4632e
# getter = None
# const = None
# payable = True
def unknown42b4632e(addr m_param1) payable: 
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining - 25050 wei
      args m_param1
  require ext_call.success
  if ext_call.return_data[0] <= 0:
      return 0
  return 1


# hash = 0x60dddfb1
# getter = None
# const = None
# payable = True
def unknown60dddfb1(addr m_param1) payable: 
  call mtokenAddress.balanceOf(address owner) with:
       gas gas_remaining - 25050 wei
      args m_param1
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x75eeadc3
# getter = None
# const = None
# payable = True
def unknown75eeadc3(uint256 m_param1) payable: 
  call caller.proposals(uint256 param1) with:
       gas gas_remaining - 25050 wei
      args m_param1
  require ext_call.success
  call caller.0x7a43cb62 with:
       gas gas_remaining - 25050 wei
      args m_param1, 0
  call caller.0x7a43cb62 with:
       gas gas_remaining - 25050 wei
      args m_param1, 1
  call mtokenAddress.token() with:
       gas gas_remaining - 25050 wei
  call addr(ext_call.return_data[0]).totalSupply() with:
       gas gas_remaining - 25050 wei
  if 2 * ext_call.return_data[0] <= ext_call.return_data[0] / 20:
      return 0
  if ext_call.return_data[0] <= ext_call.return_data[0]:
      return 0
  return 1


# hash = 0xfc0c546a
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def token() payable: 
  return mtokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


