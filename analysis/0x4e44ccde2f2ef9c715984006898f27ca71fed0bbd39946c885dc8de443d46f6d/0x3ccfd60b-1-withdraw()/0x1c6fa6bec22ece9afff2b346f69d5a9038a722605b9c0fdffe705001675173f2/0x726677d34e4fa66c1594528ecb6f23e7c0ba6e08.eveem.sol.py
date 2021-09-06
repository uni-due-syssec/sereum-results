# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x726677d34E4fA66C1594528Ecb6F23e7c0BA6E08 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 4
    owner # mask: a s
    # storage address 5
    name
    # storage address 6
    description
    # storage address 7
    category
    # storage address 8
    version
    # storage address 9
    unknown0997fa31
    # storage address 10
    unknown05374a91
    # storage address 11
    unknown6357e530
    # storage address 12
    unknown7b18c46c
# hash = 0x05374a91
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 10]]]]]
# const = None
# payable = False
def unknown05374a91(addr m_param1, uint256 m_param2): # not payable
  return munknown05374a91m[m_param1m]m[m_param2m]


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 5]]]], ['loc', 5]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x0997fa31
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 9]]]]]
# const = None
# payable = False
def unknown0997fa31(addr m_param1, uint256 m_param2): # not payable
  return munknown0997fa31m[m_param1m]m[m_param2m]


# hash = 0x38a1ff63
# getter = None
# const = None
# payable = False
def unknown38a1ff63(): # not payable
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      require [94midx < m('cd', 36).length
      require [94midx < m('cd', 4).length
      mem[0] = cd[((32 * [94midx) + cd[4] + 36)]
      mem[32] = sha3(caller, 12)
      munknown7b18c46cm[callerm]m[cd[((32 * [94midx) + cd[4] + 36)]m] = cd[((32 * [94midx) + cd[36] + 36)]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x3bce34a4
# getter = None
# const = None
# payable = False
def unknown3bce34a4(uint256 m_param1): # not payable
  require block.timestamp >= munknown6357e530m[callerm]m[m_param1m]
  require munknown7b18c46cm[callerm]m[m_param1m] + block.timestamp >= block.timestamp
  munknown6357e530m[callerm]m[m_param1m] = munknown7b18c46cm[callerm]m[m_param1m] + block.timestamp


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 8]]]], ['loc', 8]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x62f0ce85
# getter = None
# const = None
# payable = False
def unknown62f0ce85(uint256 m_param1, uint256 m_param2): # not payable
  if not m_param2:
      munknown7b18c46cm[callerm]m[m_param1m] = 0
  else:
      require m_param2 / m_param2 == 1
      munknown7b18c46cm[callerm]m[m_param1m] = m_param2


# hash = 0x6357e530
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 11]]]]]
# const = None
# payable = False
def unknown6357e530(addr m_param1, uint256 m_param2): # not payable
  return munknown6357e530m[m_param1m]m[m_param2m]


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x7284e416
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 6]]]], ['loc', 6]]]
# const = None
# payable = False
def description(): # not payable
  return mdescriptionm[0 len mdescriptionm.lengthm]


# hash = 0x7b18c46c
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 12]]]]]
# const = None
# payable = False
def unknown7b18c46c(addr m_param1, uint256 m_param2): # not payable
  return munknown7b18c46cm[m_param1m]m[m_param2m]


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x8ee7ad22
# getter = None
# const = None
# payable = False
def unknown8ee7ad22(uint256 m_param1, uint256 m_param2): # not payable
  munknown05374a91m[callerm]m[m_param1m] = m_param2


# hash = 0xdab08e26
# getter = None
# const = None
# payable = False
def unknowndab08e26(uint256 m_param1): # not payable
  require block.number >= munknown0997fa31m[callerm]m[m_param1m]
  require munknown05374a91m[callerm]m[m_param1m] + block.number >= block.number
  munknown0997fa31m[callerm]m[m_param1m] = munknown05374a91m[callerm]m[m_param1m] + block.number


# hash = 0xe89617c4
# getter = None
# const = None
# payable = False
def unknowne89617c4(): # not payable
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      require [94midx < m('cd', 36).length
      require [94midx < m('cd', 4).length
      mem[0] = cd[((32 * [94midx) + cd[4] + 36)]
      mem[32] = sha3(caller, 10)
      munknown05374a91m[callerm]m[cd[((32 * [94midx) + cd[4] + 36)]m] = cd[((32 * [94midx) + cd[36] + 36)]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xef430aa6
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 7]]]], ['loc', 7]]]
# const = None
# payable = False
def category(): # not payable
  return mcategorym[0 len mcategorym.lengthm]


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


