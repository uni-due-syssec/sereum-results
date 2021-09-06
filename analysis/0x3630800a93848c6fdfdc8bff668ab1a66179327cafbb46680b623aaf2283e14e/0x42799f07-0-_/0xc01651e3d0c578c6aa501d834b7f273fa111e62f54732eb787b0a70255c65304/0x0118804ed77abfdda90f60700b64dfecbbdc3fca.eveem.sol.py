# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x0118804ED77ABFdDA90f60700b64DFecbBdc3fCa 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    name
    # storage address 1
    symbol
    # storage address 2
    _totalSupply # mask: a s
    # storage address 3
    owner # mask: a s
    # storage address 4
    balanceOf
    # storage address 5
    allowance
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 0]]]], ['loc', 0]]]
# const = None
# payable = True
def name() payable: 
  return name[0 len name.length]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = True
def approve(address _spender, uint256 _tokens) payable: 
  require calldata.size - 4 >= 64
  allowance[caller][addr(_spender)] = _tokens
  log Approval(
        address owner=_tokens,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 2]
# const = None
# payable = True
def totalSupply() payable: 
  return _totalSupply


# hash = 0x23b872dd
# getter = None
# const = None
# payable = True
def transferFrom(address _from, address _to, uint256 _tokens) payable: 
  require calldata.size - 4 >= 96
  if not _to:
      revert with 0, 'Invalid address'
  if _tokens > balanceOf[addr(_from)]:
      revert with 0, 'Insufficient tokens transferable'
  if _tokens > allowance[addr(_from)][caller]:
      revert with 0, 'Insufficient tokens allowable'
  require _tokens <= balanceOf[addr(_from)]
  balanceOf[addr(_from)] -= _tokens
  require _tokens + balanceOf[_to] >= balanceOf[_to]
  balanceOf[addr(_to)] = _tokens + balanceOf[_to]
  require _tokens <= allowance[addr(_from)][caller]
  allowance[addr(_from)][caller] -= _tokens
  log Transfer(
        address from=_tokens,
        address to=_from,
        uint256 value=_to)
  return 1


# hash = 0x313ce567
# getter = None
# const = ['return', 18]
# payable = True
const decimals = 18


# hash = 0x32424aa3
# getter = None
# const = ['return', 18]
# payable = True
const _decimals = 18


# hash = 0x3eaaf86b
# getter = ['storage', 256, 0, 2]
# const = None
# payable = True
def _totalSupply() payable: 
  return _totalSupply


# hash = 0x66188463
# getter = None
# const = None
# payable = True
def decreaseApproval(address _spender, uint256 _subtractedValue) payable: 
  require calldata.size - 4 >= 64
  if _subtractedValue <= allowance[caller][addr(_spender)]:
      allowance[caller][addr(_spender)] -= _subtractedValue
  else:
      allowance[caller][addr(_spender)] = 0
  log Approval(
        address owner=allowance[caller][addr(_spender)],
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x6d6a6a4d
# getter = None
# const = ['return', 1000000000000000000]
# payable = True
const decimalFactor = 10^18


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 4]]]
# const = None
# payable = True
def balanceOf(address _tokenOwner) payable: 
  require calldata.size - 4 >= 32
  return balanceOf[addr(_tokenOwner)]


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 3]
# const = None
# payable = True
def owner() payable: 
  return owner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = True
def isOwner() payable: 
  return (caller == owner)


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 1]]]], ['loc', 1]]]
# const = None
# payable = True
def symbol() payable: 
  return symbol[0 len symbol.length]


# hash = 0xa0712d68
# getter = None
# const = None
# payable = True
def mint(uint256 _value) payable: 
  require calldata.size - 4 >= 32
  require caller == owner
  if _value <= 0:
      revert with 0, 'Invalid mint'
  require _value + balanceOf[stor3] >= balanceOf[stor3]
  balanceOf[stor3] += _value
  require _value + _totalSupply >= _totalSupply
  _totalSupply += _value
  log Transfer(
        address from=_value,
        address to=0,
        uint256 value=owner)


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = True
def transfer(address _to, uint256 _tokens) payable: 
  require calldata.size - 4 >= 64
  if not _to:
      revert with 0, 'Invalid address'
  if _tokens > balanceOf[caller]:
      revert with 0, 'Insufficient tokens transferable'
  require _tokens <= balanceOf[caller]
  balanceOf[caller] -= _tokens
  require _tokens + balanceOf[_to] >= balanceOf[_to]
  balanceOf[addr(_to)] = _tokens + balanceOf[_to]
  log Transfer(
        address from=_tokens,
        address to=caller,
        uint256 value=_to)
  return 1


# hash = 0xd73dd623
# getter = None
# const = None
# payable = True
def increaseApproval(address _spender, uint256 _addedValue) payable: 
  require calldata.size - 4 >= 64
  require _addedValue + allowance[caller][addr(_spender)] >= allowance[caller][addr(_spender)]
  allowance[caller][addr(_spender)] += _addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 5]]]]]
# const = None
# payable = True
def allowance(address _tokenOwner, address _spender) payable: 
  require calldata.size - 4 >= 64
  return allowance[addr(_tokenOwner)][addr(_spender)]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


