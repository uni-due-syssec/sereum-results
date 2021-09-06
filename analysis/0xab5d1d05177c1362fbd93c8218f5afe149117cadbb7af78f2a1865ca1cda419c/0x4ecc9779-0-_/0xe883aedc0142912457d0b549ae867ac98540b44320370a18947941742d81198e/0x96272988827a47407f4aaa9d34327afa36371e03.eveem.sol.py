# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x96272988827a47407F4aAa9d34327aFa36371E03 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    backupOwner # mask: a s
    # storage address 2
    unknown88b45046 # mask: a s
    # storage address 3
    unknownef95b90e # mask: a s
    # storage address 4
    unknownf51efd7a
    # storage address 5
    unknown585c5b83
    # storage address 6
    name
    # storage address 7
    symbol
    # storage address 8
    decimals # mask: a s
    # storage address 9
    totalSupply # mask: a s
    # storage address 10
    stor10
    # storage address 11
    stor11
    # storage address 12
    balanceOf
    # storage address 13
    allowance
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 6]]]], ['loc', 6]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address _spender, uint256 _tokens): # not payable
  if _tokens > balanceOf[caller]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'balanceOf msg.sender is not enough'
  allowance[caller][addr(_spender)] = _tokens
  log Approval(
        address owner=_tokens,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x12065fe0
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const getBalance = eth.balance(this.address)


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def totalSupply(): # not payable
  return totalSupply


# hash = 0x1b71d0f2
# getter = None
# const = None
# payable = False
def unknown1b71d0f2(addr _param1, uint256 _param2): # not payable
  if owner != caller:
      revert with 0, 'you are not the owner'
  unknownf51efd7a[addr(_param1)] = _param2


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address _from, address _to, uint256 _tokens): # not payable
  if _tokens > allowance[addr(_from)][caller]:
      revert with 0, '_value exceed allowance'
  allowance[addr(_from)][caller] -= _tokens
  if not _to:
      revert with 0, 'address _to must not be 0x0'
  if _tokens > balanceOf[addr(_from)]:
      revert with 0, 'balanceOf _from is not enough'
  if balanceOf[addr(_to)] + _tokens < balanceOf[addr(_to)]:
      revert with 0, 'check overflows fail'
  balanceOf[_from] -= _tokens
  balanceOf[addr(_to)] += _tokens
  log Transfer(
        address from=_tokens,
        address to=_from,
        uint256 value=_to)
  require balanceOf[addr(_to)] + balanceOf[_from] == balanceOf[_from] + balanceOf[addr(_to)]
  return 1


# hash = 0x313ce567
# getter = ['storage', 8, 0, 8]
# const = None
# payable = False
def decimals(): # not payable
  return decimals


# hash = 0x3291fa5f
# getter = None
# const = None
# payable = False
def unknown3291fa5f(array _param1, uint256 _param2): # not payable
  mem[128 len _param1.length] = _param1[all]
  if owner != caller:
      revert with 0, 'you are not the owner'
  mem[ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[ceil32(_param1.length) + floor32(_param1.length) + -(_param1.length % 32) + 192 len _param1.length % 32] = mem[floor32(_param1.length) + -(_param1.length % 32) + 160 len _param1.length % 32]
  mem[_param1.length + ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] = 256^(-(_param1.length % 32) + 32) - 1 and mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] or mem[ceil32(_param1.length) + floor32(_param1.length) + 160] and !(256^(-(_param1.length % 32) + 32) - 1)
  unknown585c5b83[call.data[_param1 + 36 len floor32(_param1.length)]][mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160 len _param1.length % 32]] = _param2


# hash = 0x3af8e4ab
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def backupOwner(): # not payable
  return backupOwner


# hash = 0x3e74d449
# getter = None
# const = None
# payable = False
def unknown3e74d449(addr _param1, uint256 _param2): # not payable
  mem[202 len 0] = None
  mem[202] = mem[212 len 2], Mask(80, 0, 'tansferETH'), mem[224 len 10]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[202 len 10]]:
      revert with 0, 'permission deny'
  if _param2 > unknownef95b90e:
      revert with 0, 'single excceed'
  call _param1 with:
     value _param2 wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x42966c68
# getter = None
# const = None
# payable = False
def burn(uint256 _amount): # not payable
  if _amount > balanceOf[caller]:
      revert with 0, 'balanceOf is not enough'
  balanceOf[caller] -= _amount
  totalSupply -= _amount
  log Burn(
        address from=_amount,
        uint256 value=caller)
  return 1


# hash = 0x56029aea
# getter = None
# const = None
# payable = False
def unknown56029aea(uint256 _param1): # not payable
  mem[212 len 0] = None
  mem[212] = mem[232 len 12]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[212 len 20]]:
      revert with 0, 'permission deny'
  unknownef95b90e = _param1


# hash = 0x585c5b83
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 5]]]
# const = None
# payable = False
def unknown585c5b83(uint256 _param1): # not payable
  return unknown585c5b83[_param1]


# hash = 0x64020558
# getter = None
# const = None
# payable = False
def unknown64020558(uint256 _param1, addr _param2): # not payable
  if owner != caller:
      revert with 0, 'you are not the owner'
  if _param1 != 201901261442:
      revert with 0, 'password is not right'
  [93mselfdestruct([91m_param2[93m)


# hash = 0x67e0e5c7
# getter = None
# const = None
# payable = False
def unknown67e0e5c7(addr _param1, bool _param2): # not payable
  mem[210 len 0] = None
  mem[210] = mem[228 len 14]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[210 len 18]]:
      revert with 0, 'permission deny'
  stor10[addr(_param1)] = uint8(_param2)


# hash = 0x69205798
# getter = None
# const = None
# payable = False
def unknown69205798(addr _param1, addr _param2, uint256 _param3): # not payable
  if bool(stor11[caller]) != 1:
      revert with 0, 'ilegal Agent'
  if not _param2:
      revert with 0, 'address _to must not be 0x0'
  if _param3 > balanceOf[addr(_param1)]:
      revert with 0, 'balanceOf _from is not enough'
  if balanceOf[addr(_param2)] + _param3 < balanceOf[addr(_param2)]:
      revert with 0, 'check overflows fail'
  balanceOf[_param1] -= _param3
  balanceOf[addr(_param2)] += _param3
  log Transfer(
        address from=_param3,
        address to=_param1,
        uint256 value=_param2)
  require balanceOf[addr(_param2)] + balanceOf[_param1] == balanceOf[_param1] + balanceOf[addr(_param2)]


# hash = 0x6e5de674
# getter = None
# const = None
# payable = False
def unknown6e5de674(addr _param1): # not payable
  if owner != caller:
      revert with 0, 'you are not the owner'
  owner = _param1


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 12]]]
# const = None
# payable = False
def balanceOf(address _tokenOwner): # not payable
  return balanceOf[_tokenOwner]


# hash = 0x771625aa
# getter = None
# const = None
# payable = False
def unknown771625aa(addr _param1, bool _param2): # not payable
  mem[208 len 0] = None
  mem[208] = mem[224 len 16]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[208 len 16]]:
      revert with 0, 'permission deny'
  stor11[addr(_param1)] = uint8(_param2)


# hash = 0x79c65068
# getter = None
# const = None
# payable = False
def mintToken(address _target, uint256 _mintedAmount): # not payable
  mem[201 len 0] = None
  mem[201] = mem[210 len 5], Mask(72, 0, 'mintToken'), mem[224 len 9]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[201 len 9]]:
      revert with 0, 'permission deny'
  balanceOf[addr(_target)] += _mintedAmount
  totalSupply += _mintedAmount
  log Transfer(
        address from=_mintedAmount,
        address to=0,
        uint256 value=this.address)
  log Transfer(
        address from=_mintedAmount,
        address to=this.address,
        uint256 value=_target)


# hash = 0x79cc6790
# getter = None
# const = None
# payable = False
def burnFrom(address _account, uint256 _amount): # not payable
  if _amount > balanceOf[addr(_account)]:
      revert with 0, 'balanceOf is not enough'
  if _amount > allowance[addr(_account)][caller]:
      revert with 0, 'allowance is not enough'
  balanceOf[addr(_account)] -= _amount
  allowance[addr(_account)][caller] -= _amount
  totalSupply -= _amount
  log Burn(
        address from=_amount,
        uint256 value=_account)
  return 1


# hash = 0x88b45046
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def unknown88b45046(): # not payable
  return unknown88b45046


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8dbc5813
# getter = None
# const = None
# payable = False
def unknown8dbc5813(array _param1): # not payable
  mem[128 len _param1.length] = _param1[all]
  mem[ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[ceil32(_param1.length) + floor32(_param1.length) + -(_param1.length % 32) + 192 len _param1.length % 32] = mem[floor32(_param1.length) + -(_param1.length % 32) + 160 len _param1.length % 32]
  mem[_param1.length + ceil32(_param1.length) + 160 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] = 256^(-(_param1.length % 32) + 32) - 1 and mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160] or mem[ceil32(_param1.length) + floor32(_param1.length) + 160] and !(256^(-(_param1.length % 32) + 32) - 1)
  mem[_param1.length + ceil32(_param1.length) + 160] = unknown585c5b83[call.data[_param1 + 36 len floor32(_param1.length)]][mem[_param1.length + ceil32(_param1.length) + floor32(_param1.length) + 160 len _param1.length % 32]]
  return memory
    from _param1.length + ceil32(_param1.length) + 160
     [93mlen 32


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 7]]]], ['loc', 7]]]
# const = None
# payable = False
def symbol(): # not payable
  return symbol[0 len symbol.length]


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address _to, uint256 _tokens): # not payable
  if not _to:
      revert with 0, 'address _to must not be 0x0'
  if _tokens > balanceOf[caller]:
      revert with 0, 'balanceOf _from is not enough'
  if balanceOf[addr(_to)] + _tokens < balanceOf[addr(_to)]:
      revert with 0, 'check overflows fail'
  balanceOf[caller] -= _tokens
  balanceOf[addr(_to)] += _tokens
  log Transfer(
        address from=_tokens,
        address to=caller,
        uint256 value=_to)
  require balanceOf[addr(_to)] + balanceOf[caller] == balanceOf[caller] + balanceOf[addr(_to)]
  return 1


# hash = 0xaa8ee3ae
# getter = None
# const = None
# payable = False
def unknownaa8ee3ae(addr _param1): # not payable
  if backupOwner != caller:
      revert with 0, 'you are not backupOwner'
  owner = _param1


# hash = 0xcae9ca51
# getter = None
# const = None
# payable = False
def approveAndCall(address _spender, uint256 _tokens, bytes _data): # not payable
  if _tokens > balanceOf[caller]:
      revert with 0, 'balanceOf msg.sender is not enough'
  allowance[caller][addr(_spender)] = _tokens
  log Approval(
        address owner=_tokens,
        address spender=caller,
        uint256 value=_spender)
  require ext_code.size(_spender)
  call _spender.receiveApproval(address sender, uint256 amount, address tokenAddress, bytes bytes) with:
       gas gas_remaining wei
      args caller, _tokens, this.address, Array(len=_data.length, data=_data[all])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0xd5078158
# getter = None
# const = None
# payable = False
def unknownd5078158(addr _param1, addr _param2, uint256 _param3): # not payable
  if bool(stor10[caller]) != 1:
      revert with 0, 'ilegal Agent'
  if not _param2:
      revert with 0, 'address _to must not be 0x0'
  if _param3 > balanceOf[addr(_param1)]:
      revert with 0, 'balanceOf _from is not enough'
  if balanceOf[addr(_param2)] + _param3 < balanceOf[addr(_param2)]:
      revert with 0, 'check overflows fail'
  balanceOf[_param1] -= _param3
  balanceOf[addr(_param2)] += _param3
  log Transfer(
        address from=_param3,
        address to=_param1,
        uint256 value=_param2)
  require balanceOf[addr(_param2)] + balanceOf[_param1] == balanceOf[_param1] + balanceOf[addr(_param2)]


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 13]]]]]
# const = None
# payable = False
def allowance(address _tokenOwner, address _spender): # not payable
  return allowance[_tokenOwner][_spender]


# hash = 0xe67b6444
# getter = None
# const = None
# payable = False
def unknowne67b6444(addr _param1, addr _param2, uint256 _param3): # not payable
  mem[204 len 0] = None
  mem[204] = uint64('tansferERC20'), mem[224 len 12]
  if unknownf51efd7a[caller] < unknown585c5b83[mem[204 len 12]]:
      revert with 0, 'permission deny'
  require ext_code.size(_param1)
  call _param1.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(_param2), _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0xef95b90e
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknownef95b90e(): # not payable
  return unknownef95b90e


# hash = 0xf02f2bf4
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 10]]]]
# const = None
# payable = False
def unknownf02f2bf4(addr _param1): # not payable
  return bool(stor10[_param1])


# hash = 0xf51efd7a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = False
def unknownf51efd7a(addr _param1): # not payable
  return unknownf51efd7a[_param1]


# hash = 0xf583e565
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 11]]]]
# const = None
# payable = False
def unknownf583e565(addr _param1): # not payable
  return bool(stor11[_param1])


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


