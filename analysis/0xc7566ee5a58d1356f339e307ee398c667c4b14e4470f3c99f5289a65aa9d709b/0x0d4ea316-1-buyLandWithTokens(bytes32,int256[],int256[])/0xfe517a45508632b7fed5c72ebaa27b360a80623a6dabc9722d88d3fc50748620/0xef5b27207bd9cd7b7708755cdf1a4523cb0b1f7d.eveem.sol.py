# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xEF5B27207bD9Cd7B7708755CDF1A4523CB0b1f7D 
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
  return name[0 len name.length]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address _spender, uint256 _value): # not payable
  require _spender
  allowance[caller][addr(_spender)] = _value
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
  return totalSupply


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address _from, address _to, uint256 _value): # not payable
  require _value <= allowance[addr(_from)][caller]
  allowance[addr(_from)][caller] -= _value
  require _to
  require _value <= balanceOf[addr(_from)]
  balanceOf[addr(_from)] -= _value
  require _value + balanceOf[_to] >= balanceOf[_to]
  balanceOf[addr(_to)] = _value + balanceOf[_to]
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
  return decimals


# hash = 0x39509351
# getter = None
# const = None
# payable = False
def increaseAllowance(address _spender, uint256 _addedValue): # not payable
  require _spender
  require _addedValue + allowance[caller][addr(_spender)] >= allowance[caller][addr(_spender)]
  allowance[caller][addr(_spender)] += _addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x40c10f19
# getter = None
# const = None
# payable = False
def mint(address _to, uint256 _value): # not payable
  require caller
  require stor6[caller]
  require _to
  require _value + totalSupply >= totalSupply
  totalSupply += _value
  require _value + balanceOf[addr(_to)] >= balanceOf[addr(_to)]
  balanceOf[addr(_to)] += _value
  log Transfer(
        address from=_value,
        address to=0,
        uint256 value=_to)
  return 1


# hash = 0x42966c68
# getter = None
# const = None
# payable = False
def burn(uint256 _value): # not payable
  require caller
  require _value <= totalSupply
  totalSupply -= _value
  require _value <= balanceOf[caller]
  balanceOf[caller] -= _value
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=0)


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 0]]]
# const = None
# payable = False
def balanceOf(address _owner): # not payable
  return balanceOf[addr(_owner)]


# hash = 0x79cc6790
# getter = None
# const = None
# payable = False
def burnFrom(address _from, uint256 _value): # not payable
  require _value <= allowance[addr(_from)][caller]
  allowance[addr(_from)][caller] -= _value
  require _from
  require _value <= totalSupply
  totalSupply -= _value
  require _value <= balanceOf[addr(_from)]
  balanceOf[addr(_from)] -= _value
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 value=0)


# hash = 0x7d960d60
# getter = None
# const = None
# payable = False
def unknown7d960d60(addr _param1): # not payable
  require caller == stor7
  stor7 = _param1


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = False
def symbol(): # not payable
  return symbol[0 len symbol.length]


# hash = 0x983b2d56
# getter = None
# const = None
# payable = False
def addMinter(address _account): # not payable
  require caller
  require stor6[caller]
  require _account
  require not stor6[addr(_account)]
  stor6[addr(_account)] = 1
  log MinterAdded(address account=_account)


# hash = 0x98650275
# getter = None
# const = None
# payable = False
def renounceMinter(): # not payable
  require caller
  require stor6[caller]
  stor6[caller] = 0
  log MinterRemoved(address account=caller)


# hash = 0xa457c2d7
# getter = None
# const = None
# payable = False
def decreaseAllowance(address _spender, uint256 _subtractedValue): # not payable
  require _spender
  require _subtractedValue <= allowance[caller][addr(_spender)]
  allowance[caller][addr(_spender)] -= _subtractedValue
  log Approval(
        address owner=(allowance[caller][addr(_spender)] - _subtractedValue),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address _to, uint256 _value): # not payable
  require _to
  require _value <= balanceOf[caller]
  balanceOf[caller] -= _value
  require _value + balanceOf[_to] >= balanceOf[_to]
  balanceOf[addr(_to)] = _value + balanceOf[_to]
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=_to)
  return 1


# hash = 0xaa271e1a
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 6]]]]
# const = None
# payable = False
def isMinter(address _account): # not payable
  require _account
  return bool(stor6[addr(_account)])


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 1]]]]]
# const = None
# payable = False
def allowance(address _owner, address _spender): # not payable
  return allowance[addr(_owner)][addr(_spender)]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


