# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xF56008909A68b2Da6AF708c94d4CA43d784b7E53 
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
def approve(address _spender, uint256 _value): # not payable
  allowance[caller][addr(_spender)] = _value
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
  return _totalSupply


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address _from, address _to, uint256 _value): # not payable
  balanceOf[addr(_from)] -= _value
  allowance[addr(_from)][caller] -= _value
  balanceOf[addr(_to)] += _value
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
  return decimals


# hash = 0x313ce567
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def decimals(): # not payable
  return decimals


# hash = 0x3eaaf86b
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def _totalSupply(): # not payable
  return _totalSupply


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]
# const = None
# payable = False
def balanceOf(address _owner): # not payable
  return balanceOf[addr(_owner)]


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address _to, uint256 _value): # not payable
  balanceOf[caller] -= _value
  balanceOf[_to] += _value
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=_to)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 3]]]]]
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


