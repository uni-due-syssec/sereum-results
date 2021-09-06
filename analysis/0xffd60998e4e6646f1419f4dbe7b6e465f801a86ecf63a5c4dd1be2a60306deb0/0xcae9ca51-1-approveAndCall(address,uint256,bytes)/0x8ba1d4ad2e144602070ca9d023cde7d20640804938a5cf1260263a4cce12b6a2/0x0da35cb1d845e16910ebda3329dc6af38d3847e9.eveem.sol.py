# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x0dA35cb1d845E16910eBDA3329Dc6aF38d3847e9 
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
def makeCall(address m_target, bytes m_data) payable: 
  require caller == mowner
  call m_target with:
     value call.value wei
       gas gas_remaining wei
      args m_data[allm]
  return bool(ext_call.success)


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


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


