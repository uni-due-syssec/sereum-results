# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x6d20Ea6fE6d67363684e22F1485712cfDcCf177A 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    bZxContractAddress # mask: a s
    # storage address 2
    unknown2247e780
# hash = 0x2247e780
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = True
def unknown2247e780(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return unknown2247e780[_param1]


# hash = 0x72e98a79
# getter = None
# const = None
# payable = True
def transferBZxOwnership(address _newBZxContractAddress) payable: 
  require calldata.size - 4 >=′ 32
  require caller == owner
  if not _newBZxContractAddress:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'transferBZxOwnership::unauthorized'
  if owner == _newBZxContractAddress:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'transferBZxOwnership::unauthorized'
  log BZxOwnershipTransferred(
        address previousBZxContract=bZxContractAddress,
        address newBZxContract=_newBZxContractAddress)
  bZxContractAddress = _newBZxContractAddress


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def owner() payable: 
  return owner


# hash = 0x8f67d21c
# getter = None
# const = None
# payable = True
def unknown8f67d21c(uint256 _param1, array _param2) payable: 
  require calldata.size - 4 >=′ 64
  require _param2 <= 18446744073709551615
  require calldata.size >′ _param2 + 35
  require _param2.length <= 18446744073709551615
  require ceil32(_param2.length) + 128 >= 96 and ceil32(_param2.length) + 128 <= 18446744073709551615
  require _param2 + _param2.length + 36 <= calldata.size
  mem[128 len _param2.length] = _param2[all]
  mem[_param2.length + 128] = 0
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if _param2.length >= 20:
      unknown2247e780[_param1] = mem[128 len 20]


# hash = 0xe4a72b13
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def bZxContractAddress() payable: 
  return bZxContractAddress


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address _newOwner) payable: 
  require calldata.size - 4 >=′ 32
  require caller == owner
  if not _newOwner:
      revert with 0, 'transferOwnership::unauthorized'
  if bZxContractAddress == _newOwner:
      revert with 0, 'transferOwnership::unauthorized'
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


