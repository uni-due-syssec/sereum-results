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
def unknown2247e780(uint256 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return munknown2247e780m[m_param1m]


# hash = 0x72e98a79
# getter = None
# const = None
# payable = True
def transferBZxOwnership(address m_newBZxContractAddress) payable: 
  require calldata.size - 4 >=′ 32
  require caller == mowner
  if not m_newBZxContractAddress:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'transferBZxOwnership::unauthorized'
  if mowner == m_newBZxContractAddress:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'transferBZxOwnership::unauthorized'
  log BZxOwnershipTransferred(
        address previousBZxContract=bZxContractAddress,
        address newBZxContract=_newBZxContractAddress)
  mbZxContractAddress = m_newBZxContractAddress


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def owner() payable: 
  return mowner


# hash = 0x8f67d21c
# getter = None
# const = None
# payable = True
def unknown8f67d21c(uint256 m_param1, array m_param2) payable: 
  require calldata.size - 4 >=′ 64
  require m_param2 <= 18446744073709551615
  require calldata.size >′ m_param2 + 35
  require m_param2.length <= 18446744073709551615
  require ceil32(m_param2.length) + 128 >= 96 and ceil32(m_param2.length) + 128 <= 18446744073709551615
  require m_param2 + m_param2.length + 36 <= calldata.size
  mem[128 len m_param2.length] = m_param2[allm]
  mem[m_param2.length + 128] = 0
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if m_param2.length >= 20:
      munknown2247e780m[m_param1m] = mem[128 len 20]


# hash = 0xe4a72b13
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def bZxContractAddress() payable: 
  return mbZxContractAddress


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address m_newOwner) payable: 
  require calldata.size - 4 >=′ 32
  require caller == mowner
  if not m_newOwner:
      revert with 0, 'transferOwnership::unauthorized'
  if mbZxContractAddress == m_newOwner:
      revert with 0, 'transferOwnership::unauthorized'
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


