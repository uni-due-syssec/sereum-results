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
  return munknown26137e6b


# hash = 0x358982a3
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 2]]]], ['loc', 2]]]
# const = None
# payable = False
def unknown358982a3(): # not payable
  return munknown358982a3m[0 len munknown358982a3m.lengthm]


# hash = 0x88fc56c0
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = False
def unknown88fc56c0(): # not payable
  return munknown88fc56c0m[0 len munknown88fc56c0m.lengthm]


# hash = 0xbbac78a9
# getter = None
# const = None
# payable = False
def setImmutableOwnership(address m_newOwner): # not payable
  require mm_owner == caller
  require mm_changeable
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=m_owner,
        address newOwner=_newOwner)
  mm_owner = m_newOwner
  mm_changeable = 0


# hash = 0xdeff41c1
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def m_owner(): # not payable
  return mm_owner


# hash = 0xe21b9d08
# getter = ['bool', ['storage', 8, 160, 0]]
# const = None
# payable = False
def m_changeable(): # not payable
  return bool(mm_changeable)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


