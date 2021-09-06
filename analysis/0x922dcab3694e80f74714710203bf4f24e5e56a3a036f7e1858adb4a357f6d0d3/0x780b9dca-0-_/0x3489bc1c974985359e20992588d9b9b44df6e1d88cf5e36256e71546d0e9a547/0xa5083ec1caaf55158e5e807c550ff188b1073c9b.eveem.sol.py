# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xa5083Ec1CaAF55158E5e807c550fF188B1073C9b 
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
    decimals # mask: a s
    # storage address 3
    balanceOf
    # storage address 4
    allowance
    # storage address 5
    totalSupply # mask: a s
    # storage address 6
    unknownf26230f1 # mask: a s
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 0]]]], ['loc', 0]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address _spender, uint256 _tokens): # not payable
  require calldata.size - 4 >= 64
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve from the zero address'
  if not _spender:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve to the zero address'
  allowance[caller][addr(_spender)] = _tokens
  log Approval(
        address owner=_tokens,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def totalSupply(): # not payable
  return totalSupply


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address _from, address _to, uint256 _tokens): # not payable
  require calldata.size - 4 >= 96
  if not _from:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer from the zero address'
  if not _to:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer to the zero address'
  if _tokens > balanceOf[addr(_from)]:
      revert with 0, 'SafeMath: subtraction overflow'
  balanceOf[addr(_from)] -= _tokens
  if _tokens + balanceOf[_to] < balanceOf[_to]:
      revert with 0, 'SafeMath: addition overflow'
  balanceOf[addr(_to)] = _tokens + balanceOf[_to]
  log Transfer(
        address from=_tokens,
        address to=_from,
        uint256 value=_to)
  if _tokens > allowance[addr(_from)][caller]:
      revert with 0, 'SafeMath: subtraction overflow'
  if not _from:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve from the zero address'
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve to the zero address'
  allowance[addr(_from)][caller] = allowance[addr(_from)][caller] - _tokens
  log Approval(
        address owner=(allowance[addr(_from)][caller] - _tokens),
        address spender=_from,
        uint256 value=caller)
  return 1


# hash = 0x313ce567
# getter = ['storage', 8, 0, 2]
# const = None
# payable = False
def decimals(): # not payable
  return decimals


# hash = 0x39509351
# getter = None
# const = None
# payable = False
def increaseAllowance(address _spender, uint256 _addedValue): # not payable
  require calldata.size - 4 >= 64
  if _addedValue + allowance[caller][addr(_spender)] < allowance[caller][addr(_spender)]:
      revert with 0, 'SafeMath: addition overflow'
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve from the zero address'
  if not _spender:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve to the zero address'
  allowance[caller][addr(_spender)] = _addedValue + allowance[caller][addr(_spender)]
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 3]]]
# const = None
# payable = False
def balanceOf(address _tokenOwner): # not payable
  require calldata.size - 4 >= 32
  return balanceOf[addr(_tokenOwner)]


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 1]]]], ['loc', 1]]]
# const = None
# payable = False
def symbol(): # not payable
  return symbol[0 len symbol.length]


# hash = 0xa457c2d7
# getter = None
# const = None
# payable = False
def decreaseAllowance(address _spender, uint256 _subtractedValue): # not payable
  require calldata.size - 4 >= 64
  if _subtractedValue > allowance[caller][addr(_spender)]:
      revert with 0, 'SafeMath: subtraction overflow'
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve from the zero address'
  if not _spender:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: approve to the zero address'
  allowance[caller][addr(_spender)] = allowance[caller][addr(_spender)] - _subtractedValue
  log Approval(
        address owner=(allowance[caller][addr(_spender)] - _subtractedValue),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address _to, uint256 _tokens): # not payable
  require calldata.size - 4 >= 64
  if not caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer from the zero address'
  if not _to:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC20: transfer to the zero address'
  if _tokens > balanceOf[caller]:
      revert with 0, 'SafeMath: subtraction overflow'
  balanceOf[caller] -= _tokens
  if _tokens + balanceOf[_to] < balanceOf[_to]:
      revert with 0, 'SafeMath: addition overflow'
  balanceOf[addr(_to)] = _tokens + balanceOf[_to]
  log Transfer(
        address from=_tokens,
        address to=caller,
        uint256 value=_to)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 4]]]]]
# const = None
# payable = False
def allowance(address _tokenOwner, address _spender): # not payable
  require calldata.size - 4 >= 64
  return allowance[addr(_tokenOwner)][addr(_spender)]


# hash = 0xf26230f1
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknownf26230f1(): # not payable
  return unknownf26230f1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


