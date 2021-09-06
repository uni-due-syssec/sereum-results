# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x150f200B6BF29959130F8995Ca4b68E336FC147B 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    unknown5d973e47
    # storage address 2
    stor2
    # storage address 3
    stor3
# hash = 0x1f9838b5
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 2]]]]]]
# const = None
# payable = True
def unknown1f9838b5(addr _param1, addr _param2) payable: 
  require calldata.size - 4 >= 64
  return bool(stor2[_param1][_param2])


# hash = 0x5d973e47
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 1]]]]]
# const = None
# payable = True
def unknown5d973e47(addr _param1, addr _param2) payable: 
  require calldata.size - 4 >= 64
  return unknown5d973e47[addr(_param1)][addr(_param2)]


# hash = 0x70284d19
# getter = None
# const = None
# payable = True
def grant(address _owner) payable: 
  require calldata.size - 4 >= 32
  require not stor0
  stor0 = 1
  if not _owner:
      revert with 0, 'Address is invalid'
  if _owner == this.address:
      revert with 0, 'Address is contract address'
  if caller == _owner:
      revert with 0, 'modification attempt on self'
  if _owner == caller:
      revert with 0, 'caller is already permissioned'
  if stor2[caller][addr(_owner)]:
      revert with 0, 'caller is already permissioned'
  stor2[caller][addr(_owner)] = 1
  log 0x65827c2b: caller, _owner
  require bool(stor2[caller][addr(_owner)]) == 1
  stor0 = 0
  return 1


# hash = 0x74a8f103
# getter = None
# const = None
# payable = True
def revoke(address _token) payable: 
  require calldata.size - 4 >= 32
  require not stor0
  stor0 = 1
  if not _token:
      revert with 0, 'Address is invalid'
  if _token == this.address:
      revert with 0, 'Address is contract address'
  if _token != caller:
      if not stor2[caller][addr(_token)]:
          revert with 0, 'caller does not have permission'
  if caller == _token:
      revert with 0, 'modification attempt on self'
  stor2[caller][addr(_token)] = 0
  log 0xbec7db88: caller, _token
  require not stor2[caller][addr(_token)]
  stor0 = 0
  return 1


# hash = 0x8340f549
# getter = None
# const = None
# payable = True
def deposit(address _darknode, address _token, uint256 _value) payable: 
  require calldata.size - 4 >= 96
  require not stor0
  stor0 = 1
  if _value <= 0:
      revert with 0, 'Quantity is less than 1'
  if not _darknode:
      revert with 0, 'Address is invalid'
  if _darknode == this.address:
      revert with 0, 'Address is contract address'
  if not _token:
      revert with 0, 'Address is invalid'
  if _token == this.address:
      revert with 0, 'Address is contract address'
  require unknown5d973e47[addr(_darknode)][addr(_token)] + _value >= unknown5d973e47[addr(_darknode)][addr(_token)]
  unknown5d973e47[addr(_darknode)][addr(_token)] += _value
  log 0xc1688a9c: _value, caller, _darknode, _token
  require ext_code.size(_token)
  call _token.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args caller, addr(this.address), _value
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'token transfer failed'
  require 0 == _value
  stor0 = 0
  return 1


# hash = 0x8f601f66
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 1]]]]]
# const = None
# payable = True
def deposits(address _param1, address _param2) payable: 
  require calldata.size - 4 >= 64
  return unknown5d973e47[_param1][_param2]


# hash = 0xa3f4df7e
# getter = None
# const = ['return', ['data', ['arr', 19, ['mask_shl', 152, 0, 0, "'Neutral Token Vault'"]]]]
# payable = True
const NAME = 'Neutral Token Vault'


# hash = 0xb1383fdc
# getter = None
# const = None
# payable = True
def unknownb1383fdc(addr _param1, addr _param2) payable: 
  require calldata.size - 4 >= 64
  if _param2 == _param1:
      return True
  return bool(stor2[addr(_param1)][addr(_param2)])


# hash = 0xb5f5e722
# getter = None
# const = None
# payable = True
def unknownb5f5e722() payable: 
  require not stor0
  stor0 = 1
  require ext_code.size(caller)
  static call caller.0x829dd895 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[31 len 1] == 200
  log 0x8cd81c49: 1, caller
  stor3[caller] = 1
  stor0 = 0
  return 1


# hash = 0xd9caed12
# getter = None
# const = None
# payable = True
def withdraw(address _owner, address _token, uint256 _tokens) payable: 
  require calldata.size - 4 >= 96
  require not stor0
  stor0 = 1
  if _tokens <= 0:
      revert with 0, 'Quantity is less than 1'
  if not _owner:
      revert with 0, 'Address is invalid'
  if _owner == this.address:
      revert with 0, 'Address is contract address'
  if not _token:
      revert with 0, 'Address is invalid'
  if _token == this.address:
      revert with 0, 'Address is contract address'
  if _tokens > unknown5d973e47[caller][addr(_token)]:
      revert with 0, 'Insufficient balance'
  require _tokens <= unknown5d973e47[caller][addr(_token)]
  unknown5d973e47[caller][addr(_token)] -= _tokens
  log 0xfbd82180: _tokens, caller, _owner, _token
  require ext_code.size(_token)
  call _token.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(_owner), _tokens
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  33,
                  0xfe546f6b656e207472616e73666572206661696c6564206f6e2077697468647261,
                  mem[197 len 31]
  require 0 == _tokens
  stor0 = 0
  return 1


# hash = 0xf18d03cc
# getter = None
# const = None
# payable = True
def transfer(address _token, address _from, address _to, uint256 _amount) payable: 
  require calldata.size - 4 >= 128
  require not stor0
  stor0 = 1
  if not _token:
      revert with 0, 'Address is invalid'
  if _token == this.address:
      revert with 0, 'Address is contract address'
  if not _from:
      revert with 0, 'Address is invalid'
  if _from == this.address:
      revert with 0, 'Address is contract address'
  if not _to:
      revert with 0, 'Address is invalid'
  if _to == this.address:
      revert with 0, 'Address is contract address'
  if _amount <= 0:
      revert with 0, 'Quantity is less than 1'
  if _token == _from:
      revert with 0, '_from and _to are the same'
  if caller == _to:
      require bool(stor3[addr(_to)]) == 1
  else:
      if _token != caller:
          if not stor2[addr(_token)][caller]:
              revert with 0, 'caller does not have permission'
  if _amount > unknown5d973e47[addr(_token)][addr(_to)]:
      revert with 0, 'Insufficient balance'
  require _amount <= unknown5d973e47[addr(_token)][addr(_to)]
  unknown5d973e47[addr(_token)][addr(_to)] -= _amount
  require unknown5d973e47[addr(_from)][addr(_to)] + _amount >= unknown5d973e47[addr(_from)][addr(_to)]
  unknown5d973e47[addr(_from)][addr(_to)] += _amount
  log 0x95b51c2e: caller, _amount, _token, _from, _to
  require 0 == _amount
  require 0 == _amount
  stor0 = 0
  return 1


# hash = 0xffa1ad74
# getter = None
# const = ['return', ['data', ['arr', 3, ['mask_shl', 24, 0, 0, "'1.4'"]]]]
# payable = True
const VERSION = '1.4'


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


