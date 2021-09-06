# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xf888C125E8E677ac20c9D91074f2eDcc7e5151E3 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    currencyAddress # mask: a s
    # storage address 2
    currencySymbol # mask: a s
    # storage address 3
    manualOverride # mask: a s
    # storage address 4
    manualPrice # mask: a s
    # storage address 5
    stor5 # mask: a s
# hash = 0x1c1cb323
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def currencyAddress() payable: 
  return mcurrencyAddress


# hash = 0x35967501
# getter = None
# const = None
# payable = True
def setManualOverride(bool m_override) payable: 
  require calldata.size - 4 >= 32
  require caller == mowner
  mmanualOverride = uint8(m_override)
  log 0x4baa8606: _override


# hash = 0x5dfc09a4
# getter = ['storage', 256, 0, 2]
# const = None
# payable = True
def getCurrencySymbol() payable: 
  return mcurrencySymbol


# hash = 0x715018a6
# getter = None
# const = None
# payable = True
def renounceOwnership() payable: 
  require caller == mowner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  mowner = 0


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def owner() payable: 
  return mowner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = True
def isOwner() payable: 
  return (caller == mowner)


# hash = 0x968c4209
# getter = ['storage', 256, 0, 2]
# const = None
# payable = True
def currencySymbol() payable: 
  return mcurrencySymbol


# hash = 0x98d5fdca
# getter = None
# const = None
# payable = True
def getPrice() payable: 
  if not mmanualOverride:
      return mstor5
  return mmanualPrice


# hash = 0xa2c9d630
# getter = ['storage', 256, 0, 4]
# const = None
# payable = True
def manualPrice() payable: 
  return mmanualPrice


# hash = 0xbae6d62b
# getter = ['bool', ['storage', 8, 0, 3]]
# const = None
# payable = True
def manualOverride() payable: 
  return bool(mmanualOverride)


# hash = 0xbfe0c27e
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def getCurrencyAddress() payable: 
  return mcurrencyAddress


# hash = 0xd2654219
# getter = None
# const = ['return', "'USD'"]
# payable = True
const getCurrencyDenominated = 'USD'


# hash = 0xd7a71868
# getter = None
# const = None
# payable = True
def setManualPrice(uint256 m_price) payable: 
  require calldata.size - 4 >= 32
  require caller == mowner
  log 0xf9343160: manualPrice, _price
  mmanualPrice = m_price


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address m_newOwner) payable: 
  require calldata.size - 4 >= 32
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


