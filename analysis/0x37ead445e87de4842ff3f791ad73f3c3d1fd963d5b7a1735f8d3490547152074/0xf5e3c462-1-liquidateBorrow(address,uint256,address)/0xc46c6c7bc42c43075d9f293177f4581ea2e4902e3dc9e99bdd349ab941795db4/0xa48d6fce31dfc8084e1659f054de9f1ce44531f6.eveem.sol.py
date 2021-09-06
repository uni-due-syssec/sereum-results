# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xA48D6FCe31dfc8084e1659f054dE9F1cE44531F6 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    stor1 # mask: a s
# hash = 0x2ac247a7
# getter = None
# const = None
# payable = True
def unknown2ac247a7(addr _param1, addr _param2, addr _param3, addr _param4) payable: 
  require calldata.size - 4 >= 128
  require caller == owner
  require ext_code.size(_param2)
  call _param2.0xaae40a2a with:
     value call.value wei
       gas gas_remaining wei
      args addr(_param1), _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(_param3)
  call _param3.redeem(uint256 amount) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _param4:
      require ext_code.size(stor1)
      static call stor1.getExchange(address token) with:
              gas gas_remaining wei
             args _param4
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(_param4)
      call _param4.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).tokenToEthSwapInput(uint256 tokens_sold, uint256 min_eth, uint256 deadline) with:
           gas gas_remaining wei
          args ext_call.return_data[0], 1, -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
  if eth.balance(this.address) <= call.value:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  50,
                  0xfe796f7520776f756c642068617665206c6f7374206d6f6e6579206f6e20746869732074726164652c20726576657274696e,
                  mem[214 len 14]
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x5fd8c710
# getter = None
# const = None
# payable = False
def withdrawBalance(): # not payable
  require caller == owner
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  owner = 0


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = False
def isOwner(): # not payable
  return (caller == owner)


# hash = 0x9db5dbe4
# getter = None
# const = None
# payable = False
def transferERC20(address _token, address _to, uint256 _tokens): # not payable
  require calldata.size - 4 >= 96
  require caller == owner
  require ext_code.size(_token)
  call _token.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(_to), _tokens
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0xa8e5e4aa
# getter = None
# const = None
# payable = False
def unknowna8e5e4aa(addr _param1, addr _param2, uint256 _param3): # not payable
  require calldata.size - 4 >= 96
  require caller == owner
  require ext_code.size(_param1)
  call _param1.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args addr(_param2), _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0xd836f78e
# getter = None
# const = None
# payable = True
def unknownd836f78e(addr _param1, addr _param2, addr _param3, addr _param4, addr _param5) payable: 
  require calldata.size - 4 >= 160
  require caller == owner
  require ext_code.size(stor1)
  static call stor1.getExchange(address token) with:
          gas gas_remaining wei
         args _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).ethToTokenSwapInput(uint256 min_tokens, uint256 deadline) with:
     value call.value wei
       gas gas_remaining wei
      args 1, -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(_param3)
  call _param3.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args addr(_param2), -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(_param2)
  call _param2.0xf5e3c462 with:
       gas gas_remaining wei
      args addr(_param1), ext_call.return_data[0], _param4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(_param4)
  call _param4.redeem(uint256 amount) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _param5:
      require ext_code.size(stor1)
      static call stor1.getExchange(address token) with:
              gas gas_remaining wei
             args _param5
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(_param5)
      call _param5.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).tokenToEthSwapInput(uint256 tokens_sold, uint256 min_eth, uint256 deadline) with:
           gas gas_remaining wei
          args ext_call.return_data[0], 1, -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
  if eth.balance(this.address) <= call.value:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  50,
                  0xfe796f7520776f756c642068617665206c6f7374206d6f6e6579206f6e20746869732074726164652c20726576657274696e,
                  mem[214 len 14]
  call caller with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xecf5717c
# getter = None
# const = None
# payable = False
def unknownecf5717c(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require caller == owner
  stor1 = _param1


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require calldata.size - 4 >= 32
  require caller == owner
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


