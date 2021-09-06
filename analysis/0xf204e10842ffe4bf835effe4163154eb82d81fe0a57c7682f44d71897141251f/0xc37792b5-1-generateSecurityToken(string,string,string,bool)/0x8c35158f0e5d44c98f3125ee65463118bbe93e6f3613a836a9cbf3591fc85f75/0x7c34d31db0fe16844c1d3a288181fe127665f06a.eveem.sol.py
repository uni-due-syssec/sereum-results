# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x7c34d31dB0fe16844C1d3a288181fe127665F06a 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    stored
# hash = 0x6c47e36f
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def storedAddresses(bytes32 _param1): # not payable
  return stored[_param1]


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipRenounced(address previousOwner=owner)
  owner = 0


# hash = 0x8905fd4f
# getter = None
# const = None
# payable = False
def reclaimERC20(address _tokenContract): # not payable
  require caller == owner
  if not _tokenContract:
      revert with 0, 'Invalid address'
  require ext_code.size(_tokenContract)
  call _tokenContract.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(_tokenContract)
  call _tokenContract.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args owner, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'Transfer failed'


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0xa7dbb402
# getter = None
# const = None
# payable = False
def changeAddress(string _name, address _newAddress): # not payable
  require caller == owner
  log 0x685cb966: Array(len=_name.length, data=_name[all]), stored[_name[all]], _newAddress
  stored[_name[all]] = _newAddress


# hash = 0xbf40fac1
# getter = ['storage', 160, 0, ['sha3', ['data', ['sha3', ['call.data', ['add', 36, ['cd', 4]], ['cd', ['add', 4, ['cd', 4]]]]], 1]]]
# const = None
# payable = False
def getAddress(string _channelId): # not payable
  if not stored[_channelId[all]]:
      revert with 0, 'Invalid address key'
  return stored[_channelId[all]]


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


