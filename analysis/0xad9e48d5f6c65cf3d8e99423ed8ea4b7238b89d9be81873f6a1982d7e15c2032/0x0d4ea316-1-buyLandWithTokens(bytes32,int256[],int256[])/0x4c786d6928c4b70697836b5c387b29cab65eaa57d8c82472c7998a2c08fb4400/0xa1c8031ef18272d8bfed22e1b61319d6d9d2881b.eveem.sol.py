# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xA1c8031EF18272d8BfeD22E1b61319D6d9d2881B 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    balanceOf
    # storage address 1
    allowance
    # storage address 2
    totalSupply # mask: a s
    # storage address 3
    name
    # storage address 4
    symbol
    # storage address 5
    decimals # mask: a s
    # storage address 6
    stor6
    # storage address 7
    stor7 # mask: a s
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 3]]]], ['loc', 3]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address m_spender, uint256 m_value): # not payable
  require m_spender
  mallowancem[callerm]m[addr(m_spender)m] = m_value
  log Approval(
        address owner=_value,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def totalSupply(): # not payable
  return mtotalSupply


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_value): # not payable
  require m_value <= mallowancem[addr(m_from)m]m[callerm]
  mallowancem[addr(m_from)m]m[callerm] -= m_value
  require m_to
  require m_value <= mbalanceOfm[addr(m_from)m]
  mbalanceOfm[addr(m_from)m] -= m_value
  require m_value + mbalanceOfm[m_tom] >= mbalanceOfm[m_tom]
  mbalanceOfm[addr(m_to)m] = m_value + mbalanceOfm[m_tom]
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 value=_to)
  return 1


# hash = 0x313ce567
# getter = ['storage', 8, 0, 5]
# const = None
# payable = False
def decimals(): # not payable
  return mdecimals


# hash = 0x39509351
# getter = None
# const = None
# payable = False
def increaseAllowance(address m_spender, uint256 m_addedValue): # not payable
  require m_spender
  require m_addedValue + mallowancem[callerm]m[addr(m_spender)m] >= mallowancem[callerm]m[addr(m_spender)m]
  mallowancem[callerm]m[addr(m_spender)m] += m_addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x40c10f19
# getter = None
# const = None
# payable = False
def mint(address m_to, uint256 m_value): # not payable
  require caller
  require mstor6m[callerm]
  require m_to
  require m_value + mtotalSupply >= mtotalSupply
  mtotalSupply += m_value
  require m_value + mbalanceOfm[addr(m_to)m] >= mbalanceOfm[addr(m_to)m]
  mbalanceOfm[addr(m_to)m] += m_value
  log Transfer(
        address from=_value,
        address to=0,
        uint256 value=_to)
  return 1


# hash = 0x42966c68
# getter = None
# const = None
# payable = False
def burn(uint256 m_value): # not payable
  require caller
  require m_value <= mtotalSupply
  mtotalSupply -= m_value
  require m_value <= mbalanceOfm[callerm]
  mbalanceOfm[callerm] -= m_value
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=0)


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 0]]]
# const = None
# payable = False
def balanceOf(address m_owner): # not payable
  return mbalanceOfm[addr(m_owner)m]


# hash = 0x79cc6790
# getter = None
# const = None
# payable = False
def burnFrom(address m_from, uint256 m_value): # not payable
  require m_value <= mallowancem[addr(m_from)m]m[callerm]
  mallowancem[addr(m_from)m]m[callerm] -= m_value
  require m_from
  require m_value <= mtotalSupply
  mtotalSupply -= m_value
  require m_value <= mbalanceOfm[addr(m_from)m]
  mbalanceOfm[addr(m_from)m] -= m_value
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 value=0)


# hash = 0x7d960d60
# getter = None
# const = None
# payable = False
def unknown7d960d60(addr m_param1): # not payable
  require caller == mstor7
  mstor7 = m_param1


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = False
def symbol(): # not payable
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0x983b2d56
# getter = None
# const = None
# payable = False
def addMinter(address m_account): # not payable
  require caller
  require mstor6m[callerm]
  require m_account
  require not mstor6m[addr(m_account)m]
  mstor6m[addr(m_account)m] = 1
  log MinterAdded(address account=_account)


# hash = 0x98650275
# getter = None
# const = None
# payable = False
def renounceMinter(): # not payable
  require caller
  require mstor6m[callerm]
  mstor6m[callerm] = 0
  log MinterRemoved(address account=caller)


# hash = 0xa457c2d7
# getter = None
# const = None
# payable = False
def decreaseAllowance(address m_spender, uint256 m_subtractedValue): # not payable
  require m_spender
  require m_subtractedValue <= mallowancem[callerm]m[addr(m_spender)m]
  mallowancem[callerm]m[addr(m_spender)m] -= m_subtractedValue
  log Approval(
        address owner=(allowance[caller][addr(_spender)] - _subtractedValue),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_value): # not payable
  require m_to
  require m_value <= mbalanceOfm[callerm]
  mbalanceOfm[callerm] -= m_value
  require m_value + mbalanceOfm[m_tom] >= mbalanceOfm[m_tom]
  mbalanceOfm[addr(m_to)m] = m_value + mbalanceOfm[m_tom]
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=_to)
  return 1


# hash = 0xaa271e1a
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 6]]]]
# const = None
# payable = False
def isMinter(address m_account): # not payable
  require m_account
  return bool(mstor6m[addr(m_account)m])


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 1]]]]]
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


