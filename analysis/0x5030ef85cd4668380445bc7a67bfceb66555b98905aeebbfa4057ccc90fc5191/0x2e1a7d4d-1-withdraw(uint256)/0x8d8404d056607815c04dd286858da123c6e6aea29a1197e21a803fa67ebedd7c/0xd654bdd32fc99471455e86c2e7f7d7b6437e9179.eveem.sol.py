# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xd654bDD32FC99471455e86C2E7f7D7b6437e9179 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    balanceOf
    # storage address 1
    allowance
# hash = 0x095ea7b3
# getter = None
# const = None
# payable = True
def approve(address m_spender, uint256 m_value) payable: 
  mallowancem[callerm]m[addr(m_spender)m] = m_value
  log Approval(
        address owner=_value,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x18160ddd
# getter = None
# const = ['return', ['balance', 'address']]
# payable = True
const totalSupply = eth.balance(this.address)


# hash = 0x23b872dd
# getter = None
# const = None
# payable = True
def transferFrom(address m_from, address m_to, uint256 m_value) payable: 
  require mbalanceOfm[addr(m_from)m] >= m_value
  require mallowancem[addr(m_from)m]m[callerm] >= m_value
  require mbalanceOfm[addr(m_to)m] + m_value >= mbalanceOfm[addr(m_to)m]
  mallowancem[addr(m_from)m]m[callerm] -= m_value
  mbalanceOfm[addr(m_from)m] -= m_value
  mbalanceOfm[addr(m_to)m] += m_value
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 value=_to)
  return 1


# hash = 0x2e1a7d4d
# getter = None
# const = None
# payable = True
def withdraw(uint256 m_wdamount) payable: 
  if mbalanceOfm[callerm] < m_wdamount:
      return 0
  call caller with:
     value m_wdamount wei
       gas gas_remaining - 34050 wei
  if not ext_call.success:
      return 0
  mbalanceOfm[callerm] -= m_wdamount
  log Withdrawal(
        address src=_wdamount,
        uint256 amt=caller)
  return 1


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 0]]]
# const = None
# payable = True
def balanceOf(address m_owner) payable: 
  return mbalanceOfm[addr(m_owner)m]


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = True
def transfer(address m_to, uint256 m_value) payable: 
  require mbalanceOfm[callerm] >= m_value
  require mbalanceOfm[addr(m_to)m] + m_value >= mbalanceOfm[addr(m_to)m]
  mbalanceOfm[callerm] -= m_value
  mbalanceOfm[addr(m_to)m] += m_value
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=_to)
  return 1


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  mbalanceOfm[callerm] += call.value
  log Deposit(
        address sender=call.value,
        uint256 value=caller)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 1]]]]]
# const = None
# payable = True
def allowance(address m_owner, address m_spender) payable: 
  return mallowancem[addr(m_owner)m]m[addr(m_spender)m]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


