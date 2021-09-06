# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x8284C4e557FB70A318fb704DC738C3C3dF8047b9 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
# hash = 0x1cb9ce63
# getter = None
# const = None
# payable = True
def makeCall(address _target, bytes _data) payable: 
  require caller == owner
  call _target with:
     value call.value wei
       gas gas_remaining wei
      args _data[all]
  return bool(ext_call.success)


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipRenounced(address previousOwner=owner)
  owner = 0


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


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


