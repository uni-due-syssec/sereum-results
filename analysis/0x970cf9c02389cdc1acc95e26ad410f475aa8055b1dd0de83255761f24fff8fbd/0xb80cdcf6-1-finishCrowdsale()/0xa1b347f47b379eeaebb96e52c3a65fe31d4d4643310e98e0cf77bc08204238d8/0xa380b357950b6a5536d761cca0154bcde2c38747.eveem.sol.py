# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xa380b357950b6A5536D761cCa0154BcdE2C38747 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    totalSupply # mask: a s
    # storage address 1
    balanceOf
    # storage address 2
    allowance
    # storage address 3
    INITIAL_SUPPLY # mask: a s
    # storage address 4
    controllerAddress # mask: a s
# hash = 0x06fdde03
# getter = None
# const = ['return', ['data', ['arr', 14, ['mask_shl', 112, 0, 0, "'MFX Coin Token'"]]]]
# payable = False
const name = 'MFX Coin Token'


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
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def totalSupply(): # not payable
  return mtotalSupply


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_value): # not payable
  require ext_code.size(mcontrollerAddress)
  call mcontrollerAddress.isTransferable(address addr) with:
       gas gas_remaining wei
      args caller
  require ext_call.success
  require ext_call.return_data[0]
  require m_to
  require m_value <= mbalanceOfm[addr(m_from)m]
  require m_value <= mallowancem[addr(m_from)m]m[callerm]
  require m_value <= mbalanceOfm[addr(m_from)m]
  mbalanceOfm[addr(m_from)m] -= m_value
  require m_value + mbalanceOfm[m_tom] >= mbalanceOfm[m_tom]
  mbalanceOfm[addr(m_to)m] = m_value + mbalanceOfm[m_tom]
  require m_value <= mallowancem[addr(m_from)m]m[callerm]
  mallowancem[addr(m_from)m]m[callerm] -= m_value
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 value=_to)
  return 1


# hash = 0x2ff2e9dc
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def INITIAL_SUPPLY(): # not payable
  return mINITIAL_SUPPLY


# hash = 0x313ce567
# getter = None
# const = ['return', 18]
# payable = False
const decimals = 18


# hash = 0x42966c68
# getter = None
# const = None
# payable = False
def burn(uint256 m_value): # not payable
  require m_value > 0
  require m_value <= mbalanceOfm[callerm]
  require m_value <= mbalanceOfm[callerm]
  mbalanceOfm[callerm] -= m_value
  require m_value <= mtotalSupply
  mtotalSupply -= m_value
  log Burn(
        address from=caller,
        uint256 value=_value)


# hash = 0x66188463
# getter = None
# const = None
# payable = False
def decreaseApproval(address m_spender, uint256 m_subtractedValue): # not payable
  if m_subtractedValue <= mallowancem[callerm]m[addr(m_spender)m]:
      mallowancem[callerm]m[addr(m_spender)m] -= m_subtractedValue
  else:
      mallowancem[callerm]m[addr(m_spender)m] = 0
  log Approval(
        address owner=allowance[caller][addr(_spender)],
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 1]]]
# const = None
# payable = False
def balanceOf(address m_owner): # not payable
  return mbalanceOfm[addr(m_owner)m]


# hash = 0x95d89b41
# getter = None
# const = ['return', ['data', ['arr', 3, ['mask_shl', 24, 0, 0, "'MFX'"]]]]
# payable = False
const symbol = 'MFX'


# hash = 0x9975038c
# getter = None
# const = None
# payable = False
def burnAll(): # not payable
  require mbalanceOfm[callerm] <= mtotalSupply
  mtotalSupply -= mbalanceOfm[callerm]
  log Burn(
        address from=caller,
        uint256 value=balanceOf[caller])
  mbalanceOfm[callerm] = 0


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_value): # not payable
  require ext_code.size(mcontrollerAddress)
  call mcontrollerAddress.isTransferable(address addr) with:
       gas gas_remaining wei
      args caller
  require ext_call.success
  require ext_call.return_data[0]
  require m_to
  require m_value <= mbalanceOfm[callerm]
  require m_value <= mbalanceOfm[callerm]
  mbalanceOfm[callerm] -= m_value
  require m_value + mbalanceOfm[m_tom] >= mbalanceOfm[m_tom]
  mbalanceOfm[addr(m_to)m] = m_value + mbalanceOfm[m_tom]
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=_to)
  if ext_code.size(m_to) <= 0:
      return 1
  require ext_code.size(m_to)
  call m_to.tokenFallback(address from, uint256 value, bytes param3) with:
       gas gas_remaining wei
      args caller, m_value, 96, 0
  require ext_call.success
  return bool(ext_call.return_data[0])


# hash = 0xbe45fd62
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_value, bytes m_data): # not payable
  require ext_code.size(mcontrollerAddress)
  call mcontrollerAddress.isTransferable(address addr) with:
       gas gas_remaining wei
      args caller
  require ext_call.success
  require ext_call.return_data[0]
  require m_to
  require m_value <= mbalanceOfm[callerm]
  require m_value <= mbalanceOfm[callerm]
  mbalanceOfm[callerm] -= m_value
  require m_value + mbalanceOfm[m_tom] >= mbalanceOfm[m_tom]
  mbalanceOfm[addr(m_to)m] = m_value + mbalanceOfm[m_tom]
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=_to)
  if ext_code.size(m_to) <= 0:
      return 1
  require ext_code.size(m_to)
  call m_to.tokenFallback(address from, uint256 value, bytes param3) with:
       gas gas_remaining wei
      args caller, m_value, Array(len=m_data.length, data=m_data[allm])
  require ext_call.success
  return bool(ext_call.return_data[0])


# hash = 0xd73dd623
# getter = None
# const = None
# payable = False
def increaseApproval(address m_spender, uint256 m_addedValue): # not payable
  require m_addedValue + mallowancem[callerm]m[addr(m_spender)m] >= mallowancem[callerm]m[addr(m_spender)m]
  mallowancem[callerm]m[addr(m_spender)m] += m_addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]
# const = None
# payable = False
def allowance(address m_owner, address m_spender): # not payable
  return mallowancem[addr(m_owner)m]m[addr(m_spender)m]


# hash = 0xf77c4791
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def controller(): # not payable
  return mcontrollerAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


