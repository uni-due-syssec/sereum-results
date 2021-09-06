# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x4dB0B0476642CAE3fc590175471f4cD6129264dF 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    m_changeable # mask: a s
    # storage address 0
    m_owner # mask: a s
    # storage address 2
    unknown358982a3
    # storage address 3
    unknown26137e6b # mask: a s
    # storage address 4
    unknown88fc56c0
# hash = 0x26137e6b
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknown26137e6b(): # not payable
  return unknown26137e6b


# hash = 0x358982a3
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 2]]]], ['loc', 2]]]
# const = None
# payable = False
def unknown358982a3(): # not payable
  return unknown358982a3[0 len unknown358982a3.length]


# hash = 0x88fc56c0
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = False
def unknown88fc56c0(): # not payable
  return unknown88fc56c0[0 len unknown88fc56c0.length]


# hash = 0xbbac78a9
# getter = None
# const = None
# payable = False
def setImmutableOwnership(address _newOwner): # not payable
  require m_owner == caller
  require m_changeable
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=m_owner,
        address newOwner=_newOwner)
  m_owner = _newOwner
  m_changeable = 0


# hash = 0xdeff41c1
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def m_owner(): # not payable
  return m_owner


# hash = 0xe21b9d08
# getter = ['bool', ['storage', 8, 160, 0]]
# const = None
# payable = False
def m_changeable(): # not payable
  return bool(m_changeable)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


