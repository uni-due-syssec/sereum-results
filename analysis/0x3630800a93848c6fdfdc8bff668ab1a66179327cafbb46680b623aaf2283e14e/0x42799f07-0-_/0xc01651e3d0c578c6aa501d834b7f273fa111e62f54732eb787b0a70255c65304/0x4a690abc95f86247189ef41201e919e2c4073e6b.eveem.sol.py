# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x4a690ABc95F86247189EF41201e919e2c4073e6B 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    stor1
# hash = 0x2f0019f2
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['sha3', ['call.data', ['add', 36, ['cd', 4]], ['cd', ['add', 4, ['cd', 4]]]]], 1]]]]
# const = None
# payable = True
def unknown2f0019f2(array _param1) payable: 
  require calldata.size - 4 >= 32
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + _param1.length + 36 <= calldata.size
  return bool(stor1[_param1[all]])


# hash = 0x715018a6
# getter = None
# const = None
# payable = True
def renounceOwnership() payable: 
  require caller == owner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  owner = 0


# hash = 0x8905fd4f
# getter = None
# const = None
# payable = True
def reclaimERC20(address _tokenContract) payable: 
  require calldata.size - 4 >= 32
  require caller == owner
  if not _tokenContract:
      revert with 0, 'Invalid address'
  require ext_code.size(_tokenContract)
  static call _tokenContract.balanceOf(address owner) with:
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
# payable = True
def owner() payable: 
  return owner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = True
def isOwner() payable: 
  return (caller == owner)


# hash = 0xe43c4083
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = True
def unknowne43c4083(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  return bool(stor1[_param1])


# hash = 0xf2983257
# getter = None
# const = None
# payable = True
def unknownf2983257(array _param1, bool _param2) payable: 
  require calldata.size - 4 >= 64
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + _param1.length + 36 <= calldata.size
  require caller == owner
  if _param2 == bool(stor1[_param1[all]]):
      revert with 0, 'Status unchanged'
  log 0xc4f204a5: Array(len=_param1.length, data=_param1[all]), _param2
  stor1[_param1[all]] = uint8(_param2)


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address _newOwner) payable: 
  require calldata.size - 4 >= 32
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


