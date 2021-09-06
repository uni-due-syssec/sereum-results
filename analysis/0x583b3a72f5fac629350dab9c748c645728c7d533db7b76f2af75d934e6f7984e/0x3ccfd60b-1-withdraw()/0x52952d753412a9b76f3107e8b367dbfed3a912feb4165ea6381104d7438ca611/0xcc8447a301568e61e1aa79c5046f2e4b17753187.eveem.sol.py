# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xCC8447a301568E61e1aA79c5046F2e4B17753187 
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
    unknown97194bd3
    # storage address 10
    unknown5de28ae0
    # storage address 11
    unknownaf99263a
    # storage address 12
    unknown62d6914c
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 5]]]], ['loc', 5]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 8]]]], ['loc', 8]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x5de28ae0
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], ['sha3', ['data', 'caller', 10]]]]]
# const = None
# payable = False
def unknown5de28ae0(uint256 m_param1): # not payable
  return munknown5de28ae0m[callerm]m[m_param1m]


# hash = 0x62d6914c
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 12]]]]]
# const = None
# payable = False
def unknown62d6914c(addr m_param1, uint256 m_param2): # not payable
  return munknown62d6914cm[m_param1m]m[m_param2m]


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


# hash = 0x8a59eb56
# getter = None
# const = None
# payable = False
def updateStatus(bytes32 m_listingHash): # not payable
  munknown5de28ae0m[callerm]m[m_listingHashm]++
  munknown62d6914cm[callerm]m[m_listingHashm] = 0
  return 1


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x92584d80
# getter = None
# const = None
# payable = False
def finalize(bytes32 m_hash): # not payable
  munknownaf99263am[callerm]m[m_hashm] = 0
  munknown62d6914cm[callerm]m[m_hashm] = 0
  munknown5de28ae0m[callerm]m[m_hashm] = 0
  return 1


# hash = 0x97194bd3
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], ['sha3', ['data', 'caller', 9]]]]]
# const = None
# payable = False
def unknown97194bd3(uint256 m_param1): # not payable
  return munknown97194bd3m[callerm]m[m_param1m]


# hash = 0xaf99263a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 11]]]]]
# const = None
# payable = False
def unknownaf99263a(addr m_param1, uint256 m_param2): # not payable
  return munknownaf99263am[m_param1m]m[m_param2m]


# hash = 0xb3ba59ab
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 9]]]]]
# const = None
# payable = False
def unknownb3ba59ab(addr m_param1, uint256 m_param2): # not payable
  return munknown97194bd3m[m_param1m]m[m_param2m]


# hash = 0xd63a81f0
# getter = None
# const = None
# payable = False
def unknownd63a81f0(uint256 m_param1, uint256 m_param2): # not payable
  require m_param2 > 0
  munknown97194bd3m[callerm]m[m_param1m] = m_param2


# hash = 0xd6d76ed5
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 10]]]]]
# const = None
# payable = False
def unknownd6d76ed5(addr m_param1, uint256 m_param2): # not payable
  return munknown5de28ae0m[m_param1m]m[m_param2m]


# hash = 0xd75bc29b
# getter = None
# const = None
# payable = False
def unknownd75bc29b(uint256 m_param1): # not payable
  if munknown97194bd3m[callerm]m[m_param1m] <= munknownaf99263am[callerm]m[m_param1m]:
      return 0
  munknownaf99263am[callerm]m[m_param1m]++
  munknown62d6914cm[callerm]m[m_param1m]++
  return 1


# hash = 0xda48d889
# getter = None
# const = None
# payable = False
def unknownda48d889(uint256 m_param1): # not payable
  require 0 < munknown97194bd3m[callerm]m[m_param1m]
  munknownaf99263am[callerm]m[m_param1m] = 0
  if not munknown5de28ae0m[callerm]m[m_param1m]:
      munknown5de28ae0m[callerm]m[m_param1m] = 1
  return munknown62d6914cm[callerm]m[m_param1m]


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


# hash = 0xfdb880b9
# getter = None
# const = None
# payable = False
def unknownfdb880b9(): # not payable
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      require [94midx < m('cd', 36).length
      require cd[((32 * [94midx) + cd[36] + 36)] > 0
      require [94midx < m('cd', 36).length
      require [94midx < m('cd', 4).length
      mem[0] = cd[((32 * [94midx) + cd[4] + 36)]
      mem[32] = sha3(caller, 9)
      munknown97194bd3m[callerm]m[cd[((32 * [94midx) + cd[4] + 36)]m] = cd[((32 * [94midx) + cd[36] + 36)]
      [94midx = [94midx + 1
      mcontinue 


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


