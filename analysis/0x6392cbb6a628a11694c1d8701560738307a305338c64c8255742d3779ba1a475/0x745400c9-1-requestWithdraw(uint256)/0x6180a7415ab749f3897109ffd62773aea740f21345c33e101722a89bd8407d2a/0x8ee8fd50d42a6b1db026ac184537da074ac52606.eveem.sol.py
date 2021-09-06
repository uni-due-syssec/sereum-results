# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x8eE8Fd50d42A6B1DB026AC184537DA074aC52606 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    decimals # mask: a s
    # storage address 1
    _totalSupply # mask: a s
    # storage address 2
    balanceOf
    # storage address 3
    allowance
# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address m_spender, uint256 m_value): # not payable
  mallowancem[callerm]m[addr(m_spender)m] = m_value
  log Approval(
        address owner=_value,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def totalSupply(): # not payable
  return m_totalSupply


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_value): # not payable
  mbalanceOfm[addr(m_from)m] -= m_value
  mallowancem[addr(m_from)m]m[callerm] -= m_value
  mbalanceOfm[addr(m_to)m] += m_value
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 value=_to)
  return 1


# hash = 0x30ca1387
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def unknown30ca1387(): # not payable
  return mdecimals


# hash = 0x313ce567
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def decimals(): # not payable
  return mdecimals


# hash = 0x3eaaf86b
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def _totalSupply(): # not payable
  return m_totalSupply


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]
# const = None
# payable = False
def balanceOf(address m_owner): # not payable
  return mbalanceOfm[addr(m_owner)m]


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_value): # not payable
  mbalanceOfm[callerm] -= m_value
  mbalanceOfm[m_tom] += m_value
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=_to)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 3]]]]]
# const = None
# payable = False
def allowance(address m_owner, address m_spender): # not payable
  return mallowancem[addr(m_owner)m]m[addr(m_spender)m]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


