# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x5032DB65dA304c128d1DFd4b5b26774AB716eBFC 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    stor8 # mask: a s
# hash = 0x06846ec0
# getter = None
# const = None
# payable = False
def unknown06846ec0(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if stor0[tx.origin] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if stor0[caller] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if eth.balance(this.address) > 0:
      require ext_code.size(stor3)
      if _param1 != -1:
          call stor3.deposit() with:
             value _param1 wei
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(stor3)
          call stor3.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args stor2, _param1
      else:
          call stor3.deposit() with:
             value eth.balance(this.address) wei
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(stor3)
          call stor3.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args stor2, eth.balance(this.address)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


# hash = 0x15bc08a8
# getter = None
# const = None
# payable = False
def unknown15bc08a8(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(stor5)
  static call stor5.0x182df0f5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require 10^18 * _param1 / 10^18 == _param1
      if 10^18 * _param1:
          require 10^18 * _param1
          require 1000000000000000000 * 10^18 * _param1 / 10^18 * _param1 == 10^18
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          return (1000000000000000000 * 10^18 * _param1 / ext_call.return_data[0] / 10^18)
      else:
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          return (0 / ext_call.return_data[0] / 10^18)


# hash = 0x1e907595
# getter = None
# const = None
# payable = False
def unknown1e907595(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if stor0[tx.origin] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if stor0[caller] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
  static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
          gas gas_remaining wei
         args stor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < _param1:
      revert with 0, 'Not enough WETH funds'
  require ext_code.size(stor3)
  call stor3.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args stor2, addr(this.address), _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(stor3)
  call stor3.withdraw(uint256 wdamount) with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x26273199
# getter = None
# const = None
# payable = False
def unknown26273199(addr _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(_param2)
  static call _param2.balanceOf(address owner) with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x392d661c
# getter = None
# const = None
# payable = False
def depositERC20(uint256 _amount, address _contractAddress): # not payable
  require calldata.size - 4 >= 64
  if stor0[tx.origin] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if stor0[caller] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  require ext_code.size(_contractAddress)
  static call _contractAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args stor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < _amount:
      revert with 0, 'Not enough ERC20 funds'
  require ext_code.size(_contractAddress)
  call _contractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args stor2, addr(this.address), _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0x4b660cc5
# getter = None
# const = None
# payable = False
def unknown4b660cc5(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(stor5)
  static call stor5.0x182df0f5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  require ext_call.return_data[0]
  require ext_call.return_data[0] * _param1 / ext_call.return_data[0] == _param1
  return (ext_call.return_data[0] * _param1 / 10^18)


# hash = 0x4d489323
# getter = None
# const = None
# payable = False
def unknown4d489323(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if _param2 != stor4:
      return -1
  require ext_code.size(stor7)
  static call stor7.getTokenToEthOutputPrice(uint256 eth_bought) with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _param2 != stor4:
      return -1
  require ext_code.size(stor5)
  static call stor5.balanceOf(address owner) with:
          gas gas_remaining wei
         args stor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < ext_call.return_data[0]:
      return -1
  require ext_code.size(stor5)
  static call stor5.0x182df0f5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  require ext_call.return_data[0]
  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
  return (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)


# hash = 0x59a87bc1
# getter = None
# const = None
# payable = False
def buy(uint256 _stepSize, uint256 _protectRatio, address _recommendAddr): # not payable
  require calldata.size - 4 >= 96
  if stor0[tx.origin] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  else:
      if stor0[caller] != 1:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      39,
                      0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                      mem[203 len 25]
      else:
          require ext_code.size(stor5)
          static call stor5.0x182df0f5 with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              require 10^18 * _protectRatio / 10^18 == _protectRatio
              if 10^18 * _protectRatio:
                  require 10^18 * _protectRatio
                  require 1000000000000000000 * 10^18 * _protectRatio / 10^18 * _protectRatio == 10^18
                  require ext_call.return_data[0] > 0
                  require ext_call.return_data[0]
                  if stor0[tx.origin] != 1:
                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                  else:
                      if stor0[caller] != 1:
                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                      else:
                          require ext_code.size(stor5)
                          static call stor5.balanceOf(address owner) with:
                                  gas gas_remaining wei
                                 args stor2
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if ext_call.return_data[0] < 1000000000000000000 * 10^18 * _protectRatio / ext_call.return_data[0] / 10^18:
                                  revert with 0, 'Not enough ERC20 funds'
                              else:
                                  require ext_code.size(stor5)
                                  call stor5.transferFrom(address from, address to, uint256 value) with:
                                       gas gas_remaining wei
                                      args stor2, addr(this.address), 1000000000000000000 * 10^18 * _protectRatio / ext_call.return_data[0] / 10^18
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(stor7)
                                      call stor7.tokenToEthSwapOutput(uint256 eth_bought, uint256 max_tokens, uint256 deadline) with:
                                           gas gas_remaining wei
                                          args _stepSize, 1000000000000000000 * 10^18 * _protectRatio / ext_call.return_data[0] / 10^18, block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          require ext_code.size(stor5)
                                          static call stor5.0x182df0f5 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              if ext_call.return_data[0]:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  if stor0[tx.origin] != 1:
                                                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                  else:
                                                      if stor0[caller] != 1:
                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                      else:
                                                          require ext_code.size(stor5)
                                                          static call stor5.balanceOf(address owner) with:
                                                                  gas gas_remaining wei
                                                                 args this.address
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 32
                                                              if ext_call.return_data[0] > 0:
                                                                  require ext_code.size(stor5)
                                                                  static call stor5.balanceOf(address owner) with:
                                                                          gas gas_remaining wei
                                                                         args this.address
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >= 32
                                                                      require ext_code.size(stor5)
                                                                      call stor5.transfer(address to, uint256 value) with:
                                                                           gas gas_remaining wei
                                                                          args stor2, ext_call.return_data[0]
                                                                      if not ext_call.success:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          if stor0[tx.origin] != 1:
                                                                              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                          else:
                                                                              if stor0[caller] != 1:
                                                                                  revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                              else:
                                                                                  if eth.balance(this.address) > 0:
                                                                                      require ext_code.size(stor3)
                                                                                      call stor3.deposit() with:
                                                                                         value eth.balance(this.address) wei
                                                                                           gas gas_remaining wei
                                                                                      if not ext_call.success:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require ext_code.size(stor3)
                                                                                          call stor3.transfer(address to, uint256 value) with:
                                                                                               gas gas_remaining wei
                                                                                              args stor2, eth.balance(this.address)
                                                                                          if not ext_call.success:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >= 32
                                                                                              log 0xbc43d7c0: _stepSize, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                                              return ext_call.return_data[0]
                                                                                  else:
                                                                                      log 0xbc43d7c0: _stepSize, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                                      return ext_call.return_data[0]
                                                              else:
                                                                  if stor0[tx.origin] != 1:
                                                                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                  else:
                                                                      if stor0[caller] != 1:
                                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                      else:
                                                                          if eth.balance(this.address) > 0:
                                                                              require ext_code.size(stor3)
                                                                              call stor3.deposit() with:
                                                                                 value eth.balance(this.address) wei
                                                                                   gas gas_remaining wei
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require ext_code.size(stor3)
                                                                                  call stor3.transfer(address to, uint256 value) with:
                                                                                       gas gas_remaining wei
                                                                                      args stor2, eth.balance(this.address)
                                                                                  if not ext_call.success:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >= 32
                                                                                      log 0xbc43d7c0: _stepSize, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                                      return ext_call.return_data[0]
                                                                          else:
                                                                              log 0xbc43d7c0: _stepSize, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                              return ext_call.return_data[0]
                                              else:
                                                  if stor0[tx.origin] != 1:
                                                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                  else:
                                                      if stor0[caller] != 1:
                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                      else:
                                                          require ext_code.size(stor5)
                                                          static call stor5.balanceOf(address owner) with:
                                                                  gas gas_remaining wei
                                                                 args this.address
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 32
                                                              if ext_call.return_data[0] > 0:
                                                                  require ext_code.size(stor5)
                                                                  static call stor5.balanceOf(address owner) with:
                                                                          gas gas_remaining wei
                                                                         args this.address
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >= 32
                                                                      require ext_code.size(stor5)
                                                                      call stor5.transfer(address to, uint256 value) with:
                                                                           gas gas_remaining wei
                                                                          args stor2, ext_call.return_data[0]
                                                                      if not ext_call.success:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          if stor0[tx.origin] != 1:
                                                                              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                          else:
                                                                              if stor0[caller] != 1:
                                                                                  revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                              else:
                                                                                  if eth.balance(this.address) > 0:
                                                                                      require ext_code.size(stor3)
                                                                                      call stor3.deposit() with:
                                                                                         value eth.balance(this.address) wei
                                                                                           gas gas_remaining wei
                                                                                      if not ext_call.success:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require ext_code.size(stor3)
                                                                                          call stor3.transfer(address to, uint256 value) with:
                                                                                               gas gas_remaining wei
                                                                                              args stor2, eth.balance(this.address)
                                                                                          if not ext_call.success:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >= 32
                                                                                              log 0xbc43d7c0: _stepSize, 0, stor8
                                                                                              return ext_call.return_data[0]
                                                                                  else:
                                                                                      log 0xbc43d7c0: _stepSize, 0, stor8
                                                                                      return ext_call.return_data[0]
                                                              else:
                                                                  if stor0[tx.origin] != 1:
                                                                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                  else:
                                                                      if stor0[caller] != 1:
                                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                      else:
                                                                          if eth.balance(this.address) > 0:
                                                                              require ext_code.size(stor3)
                                                                              call stor3.deposit() with:
                                                                                 value eth.balance(this.address) wei
                                                                                   gas gas_remaining wei
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require ext_code.size(stor3)
                                                                                  call stor3.transfer(address to, uint256 value) with:
                                                                                       gas gas_remaining wei
                                                                                      args stor2, eth.balance(this.address)
                                                                                  if not ext_call.success:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >= 32
                                                                                      log 0xbc43d7c0: _stepSize, 0, stor8
                                                                                      return ext_call.return_data[0]
                                                                          else:
                                                                              log 0xbc43d7c0: _stepSize, 0, stor8
                                                                              return ext_call.return_data[0]
              else:
                  require ext_call.return_data[0] > 0
                  require ext_call.return_data[0]
                  if stor0[tx.origin] != 1:
                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                  else:
                      if stor0[caller] != 1:
                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                      else:
                          require ext_code.size(stor5)
                          static call stor5.balanceOf(address owner) with:
                                  gas gas_remaining wei
                                 args stor2
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if ext_call.return_data[0] < 0 / ext_call.return_data[0] / 10^18:
                                  revert with 0, 'Not enough ERC20 funds'
                              else:
                                  require ext_code.size(stor5)
                                  call stor5.transferFrom(address from, address to, uint256 value) with:
                                       gas gas_remaining wei
                                      args stor2, addr(this.address), 0 / ext_call.return_data[0] / 10^18
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(stor7)
                                      call stor7.tokenToEthSwapOutput(uint256 eth_bought, uint256 max_tokens, uint256 deadline) with:
                                           gas gas_remaining wei
                                          args _stepSize, 0 / ext_call.return_data[0] / 10^18, block.timestamp
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          require ext_code.size(stor5)
                                          static call stor5.0x182df0f5 with:
                                                  gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              if ext_call.return_data[0]:
                                                  require ext_call.return_data[0]
                                                  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                  if stor0[tx.origin] != 1:
                                                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                  else:
                                                      if stor0[caller] != 1:
                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                      else:
                                                          require ext_code.size(stor5)
                                                          static call stor5.balanceOf(address owner) with:
                                                                  gas gas_remaining wei
                                                                 args this.address
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 32
                                                              if ext_call.return_data[0] > 0:
                                                                  require ext_code.size(stor5)
                                                                  static call stor5.balanceOf(address owner) with:
                                                                          gas gas_remaining wei
                                                                         args this.address
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >= 32
                                                                      require ext_code.size(stor5)
                                                                      call stor5.transfer(address to, uint256 value) with:
                                                                           gas gas_remaining wei
                                                                          args stor2, ext_call.return_data[0]
                                                                      if not ext_call.success:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          if stor0[tx.origin] != 1:
                                                                              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                          else:
                                                                              if stor0[caller] != 1:
                                                                                  revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                              else:
                                                                                  if eth.balance(this.address) > 0:
                                                                                      require ext_code.size(stor3)
                                                                                      call stor3.deposit() with:
                                                                                         value eth.balance(this.address) wei
                                                                                           gas gas_remaining wei
                                                                                      if not ext_call.success:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require ext_code.size(stor3)
                                                                                          call stor3.transfer(address to, uint256 value) with:
                                                                                               gas gas_remaining wei
                                                                                              args stor2, eth.balance(this.address)
                                                                                          if not ext_call.success:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >= 32
                                                                                              log 0xbc43d7c0: _stepSize, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                                              return ext_call.return_data[0]
                                                                                  else:
                                                                                      log 0xbc43d7c0: _stepSize, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                                      return ext_call.return_data[0]
                                                              else:
                                                                  if stor0[tx.origin] != 1:
                                                                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                  else:
                                                                      if stor0[caller] != 1:
                                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                      else:
                                                                          if eth.balance(this.address) > 0:
                                                                              require ext_code.size(stor3)
                                                                              call stor3.deposit() with:
                                                                                 value eth.balance(this.address) wei
                                                                                   gas gas_remaining wei
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require ext_code.size(stor3)
                                                                                  call stor3.transfer(address to, uint256 value) with:
                                                                                       gas gas_remaining wei
                                                                                      args stor2, eth.balance(this.address)
                                                                                  if not ext_call.success:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >= 32
                                                                                      log 0xbc43d7c0: _stepSize, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                                      return ext_call.return_data[0]
                                                                          else:
                                                                              log 0xbc43d7c0: _stepSize, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                              return ext_call.return_data[0]
                                              else:
                                                  if stor0[tx.origin] != 1:
                                                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                  else:
                                                      if stor0[caller] != 1:
                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                      else:
                                                          require ext_code.size(stor5)
                                                          static call stor5.balanceOf(address owner) with:
                                                                  gas gas_remaining wei
                                                                 args this.address
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 32
                                                              if ext_call.return_data[0] > 0:
                                                                  require ext_code.size(stor5)
                                                                  static call stor5.balanceOf(address owner) with:
                                                                          gas gas_remaining wei
                                                                         args this.address
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >= 32
                                                                      require ext_code.size(stor5)
                                                                      call stor5.transfer(address to, uint256 value) with:
                                                                           gas gas_remaining wei
                                                                          args stor2, ext_call.return_data[0]
                                                                      if not ext_call.success:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          if stor0[tx.origin] != 1:
                                                                              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                          else:
                                                                              if stor0[caller] != 1:
                                                                                  revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                              else:
                                                                                  if eth.balance(this.address) > 0:
                                                                                      require ext_code.size(stor3)
                                                                                      call stor3.deposit() with:
                                                                                         value eth.balance(this.address) wei
                                                                                           gas gas_remaining wei
                                                                                      if not ext_call.success:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require ext_code.size(stor3)
                                                                                          call stor3.transfer(address to, uint256 value) with:
                                                                                               gas gas_remaining wei
                                                                                              args stor2, eth.balance(this.address)
                                                                                          if not ext_call.success:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >= 32
                                                                                              log 0xbc43d7c0: _stepSize, 0, stor8
                                                                                              return ext_call.return_data[0]
                                                                                  else:
                                                                                      log 0xbc43d7c0: _stepSize, 0, stor8
                                                                                      return ext_call.return_data[0]
                                                              else:
                                                                  if stor0[tx.origin] != 1:
                                                                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                  else:
                                                                      if stor0[caller] != 1:
                                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                                      else:
                                                                          if eth.balance(this.address) > 0:
                                                                              require ext_code.size(stor3)
                                                                              call stor3.deposit() with:
                                                                                 value eth.balance(this.address) wei
                                                                                   gas gas_remaining wei
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require ext_code.size(stor3)
                                                                                  call stor3.transfer(address to, uint256 value) with:
                                                                                       gas gas_remaining wei
                                                                                      args stor2, eth.balance(this.address)
                                                                                  if not ext_call.success:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >= 32
                                                                                      log 0xbc43d7c0: _stepSize, 0, stor8
                                                                                      return ext_call.return_data[0]
                                                                          else:
                                                                              log 0xbc43d7c0: _stepSize, 0, stor8
                                                                              return ext_call.return_data[0]


# hash = 0x5f8334fc
# getter = None
# const = None
# payable = False
def unknown5f8334fc(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if _param2 == stor4:
      require ext_code.size(stor5)
      static call stor5.0x182df0f5 with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require 10^18 * _param1 / 10^18 == _param1
          if 10^18 * _param1:
              require 10^18 * _param1
              require 1000000000000000000 * 10^18 * _param1 / 10^18 * _param1 == 10^18
              require ext_call.return_data[0] > 0
              require ext_call.return_data[0]
              require ext_code.size(stor7)
              static call stor7.getEthToTokenOutputPrice(uint256 tokens_bought) with:
                      gas gas_remaining wei
                     args (1000000000000000000 * 10^18 * _param1 / ext_call.return_data[0] / 10^18)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  return ext_call.return_data[0]
          else:
              require ext_call.return_data[0] > 0
              require ext_call.return_data[0]
              require ext_code.size(stor7)
              static call stor7.getEthToTokenOutputPrice(uint256 tokens_bought) with:
                      gas gas_remaining wei
                     args (0 / ext_call.return_data[0] / 10^18)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  return ext_call.return_data[0]
  else:
      return -1


# hash = 0x7e5465ba
# getter = None
# const = None
# payable = False
def approve(address _token, address _proxy): # not payable
  require calldata.size - 4 >= 64
  if stor0[tx.origin] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if stor0[caller] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  require ext_code.size(_proxy)
  static call _proxy.allowance(address owner, address spender) with:
          gas gas_remaining wei
         args addr(this.address), _token
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < -1:
      require ext_code.size(_proxy)
      call _proxy.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args addr(_token), -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


# hash = 0x8da6bfe6
# getter = None
# const = None
# payable = False
def unknown8da6bfe6(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if _param2 == stor4:
      require ext_code.size(stor5)
      static call stor5.0x182df0f5 with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require 10^18 * _param1 / 10^18 == _param1
          if 10^18 * _param1:
              require 10^18 * _param1
              require 1000000000000000000 * 10^18 * _param1 / 10^18 * _param1 == 10^18
              require ext_call.return_data[0] > 0
              require ext_call.return_data[0]
              if _param2 == stor4:
                  require ext_code.size(stor5)
                  static call stor5.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args stor2
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if ext_call.return_data[0] >= 1000000000000000000 * 10^18 * _param1 / ext_call.return_data[0] / 10^18:
                          require ext_code.size(stor7)
                          static call stor7.getTokenToEthInputPrice(uint256 tokens_sold) with:
                                  gas gas_remaining wei
                                 args (1000000000000000000 * 10^18 * _param1 / ext_call.return_data[0] / 10^18)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              return ext_call.return_data[0]
                      else:
                          return 0
              else:
                  return 0
          else:
              require ext_call.return_data[0] > 0
              require ext_call.return_data[0]
              if _param2 == stor4:
                  require ext_code.size(stor5)
                  static call stor5.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args stor2
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if ext_call.return_data[0] >= 0 / ext_call.return_data[0] / 10^18:
                          require ext_code.size(stor7)
                          static call stor7.getTokenToEthInputPrice(uint256 tokens_sold) with:
                                  gas gas_remaining wei
                                 args (0 / ext_call.return_data[0] / 10^18)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              return ext_call.return_data[0]
                      else:
                          return 0
              else:
                  return 0
  else:
      return 0


# hash = 0x9134709e
# getter = None
# const = None
# payable = False
def unknown9134709e(uint256 _param1): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(stor5)
  static call stor5.0x182df0f5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require 10^18 * _param1 / 10^18 == _param1
      if 10^18 * _param1:
          require 10^18 * _param1
          require 1000000000000000000 * 10^18 * _param1 / 10^18 * _param1 == 10^18
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          require ext_code.size(stor7)
          static call stor7.getEthToTokenOutputPrice(uint256 tokens_bought) with:
                  gas gas_remaining wei
                 args (1000000000000000000 * 10^18 * _param1 / ext_call.return_data[0] / 10^18)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              if stor0[tx.origin] != 1:
                  revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
              else:
                  if stor0[caller] != 1:
                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                  else:
                      require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
                      static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
                              gas gas_remaining wei
                             args stor2
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          if ext_call.return_data[0] < ext_call.return_data[0]:
                              revert with 0, 'Not enough WETH funds'
                          else:
                              require ext_code.size(stor3)
                              call stor3.transferFrom(address from, address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args stor2, addr(this.address), ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(stor3)
                                  call stor3.withdraw(uint256 wdamount) with:
                                       gas gas_remaining wei
                                      args ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require ext_code.size(stor7)
                                      call stor7.ethToTokenTransferOutput(uint256 tokens_bought, uint256 deadline, address recipient) with:
                                         value ext_call.return_data[0] wei
                                           gas gas_remaining wei
                                          args 1000000000000000000 * 10^18 * _param1 / ext_call.return_data[0] / 10^18, block.timestamp, stor2
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          log 0xbc43d7c0: ext_call.return_data[0], _param1, stor8
                                          return ext_call.return_data[0]
      else:
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          require ext_code.size(stor7)
          static call stor7.getEthToTokenOutputPrice(uint256 tokens_bought) with:
                  gas gas_remaining wei
                 args (0 / ext_call.return_data[0] / 10^18)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              if stor0[tx.origin] != 1:
                  revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
              else:
                  if stor0[caller] != 1:
                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                  else:
                      require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
                      static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
                              gas gas_remaining wei
                             args stor2
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          if ext_call.return_data[0] < ext_call.return_data[0]:
                              revert with 0, 'Not enough WETH funds'
                          else:
                              require ext_code.size(stor3)
                              call stor3.transferFrom(address from, address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args stor2, addr(this.address), ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(stor3)
                                  call stor3.withdraw(uint256 wdamount) with:
                                       gas gas_remaining wei
                                      args ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require ext_code.size(stor7)
                                      call stor7.ethToTokenTransferOutput(uint256 tokens_bought, uint256 deadline, address recipient) with:
                                         value ext_call.return_data[0] wei
                                           gas gas_remaining wei
                                          args 0 / ext_call.return_data[0] / 10^18, block.timestamp, stor2
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          log 0xbc43d7c0: ext_call.return_data[0], _param1, stor8
                                          return ext_call.return_data[0]


# hash = 0xad5c4648
# getter = None
# const = ['return', 1097077688018008265106216665536940668749033598146]
# payable = False
const WETH = 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2


# hash = 0xb8b3dbc6
# getter = None
# const = None
# payable = False
def unknownb8b3dbc6(): # not payable
  if stor1 != caller:
      revert with 0, 'Must be the commander.'
  [93mselfdestruct([91mstor1[93m)


# hash = 0xc20938e0
# getter = None
# const = None
# payable = False
def unknownc20938e0(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if stor0[tx.origin] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if stor0[caller] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  require ext_code.size(_param2)
  static call _param2.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > 0:
      require ext_code.size(_param2)
      if _param1 != -1:
          call _param2.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args stor2, _param1
      else:
          static call _param2.balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(_param2)
          call _param2.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args stor2, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0xd04c6983
# getter = None
# const = None
# payable = False
def unknownd04c6983(uint256 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 96
  if stor0[tx.origin] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  else:
      if stor0[caller] != 1:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      39,
                      0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                      mem[203 len 25]
      else:
          require ext_code.size(stor5)
          static call stor5.0x182df0f5 with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              require 10^18 * _param2 / 10^18 == _param2
              if 10^18 * _param2:
                  require 10^18 * _param2
                  require 1000000000000000000 * 10^18 * _param2 / 10^18 * _param2 == 10^18
                  require ext_call.return_data[0] > 0
                  require ext_call.return_data[0]
                  if stor0[tx.origin] != 1:
                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                  else:
                      if stor0[caller] != 1:
                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                      else:
                          require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
                          static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
                                  gas gas_remaining wei
                                 args stor2
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if ext_call.return_data[0] < _param1:
                                  revert with 0, 'Not enough WETH funds'
                              else:
                                  require ext_code.size(stor3)
                                  call stor3.transferFrom(address from, address to, uint256 value) with:
                                       gas gas_remaining wei
                                      args stor2, addr(this.address), _param1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(stor3)
                                      call stor3.withdraw(uint256 wdamount) with:
                                           gas gas_remaining wei
                                          args _param1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require ext_code.size(stor7)
                                          call stor7.ethToTokenTransferInput(uint256 min_tokens, uint256 deadline, address recipient) with:
                                             value _param1 wei
                                               gas gas_remaining wei
                                              args 1000000000000000000 * 10^18 * _param2 / ext_call.return_data[0] / 10^18, block.timestamp, stor2
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              require ext_code.size(stor5)
                                              static call stor5.0x182df0f5 with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if stor0[tx.origin] != 1:
                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                      else:
                                                          if stor0[caller] != 1:
                                                              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                          else:
                                                              require ext_code.size(stor5)
                                                              static call stor5.balanceOf(address owner) with:
                                                                      gas gas_remaining wei
                                                                     args this.address
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 32
                                                                  if ext_call.return_data[0] > 0:
                                                                      if ext_call.return_data[0] != -1:
                                                                          require ext_code.size(stor5)
                                                                          call stor5.transfer(address to, uint256 value) with:
                                                                               gas gas_remaining wei
                                                                              args stor2, ext_call.return_data[0]
                                                                          if not ext_call.success:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              log 0xbc43d7c0: _param1, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                              return ext_call.return_data[0]
                                                                      else:
                                                                          require ext_code.size(stor5)
                                                                          static call stor5.balanceOf(address owner) with:
                                                                                  gas gas_remaining wei
                                                                                 args this.address
                                                                          if not ext_call.success:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >= 32
                                                                              require ext_code.size(stor5)
                                                                              call stor5.transfer(address to, uint256 value) with:
                                                                                   gas gas_remaining wei
                                                                                  args stor2, ext_call.return_data[0]
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  log 0xbc43d7c0: _param1, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                                  return ext_call.return_data[0]
                                                                  else:
                                                                      log 0xbc43d7c0: _param1, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                      return ext_call.return_data[0]
                                                  else:
                                                      if stor0[tx.origin] != 1:
                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                      else:
                                                          if stor0[caller] != 1:
                                                              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                          else:
                                                              require ext_code.size(stor5)
                                                              static call stor5.balanceOf(address owner) with:
                                                                      gas gas_remaining wei
                                                                     args this.address
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 32
                                                                  if ext_call.return_data[0] > 0:
                                                                      if ext_call.return_data[0] != -1:
                                                                          require ext_code.size(stor5)
                                                                          call stor5.transfer(address to, uint256 value) with:
                                                                               gas gas_remaining wei
                                                                              args stor2, ext_call.return_data[0]
                                                                          if not ext_call.success:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              log 0xbc43d7c0: _param1, 0, stor8
                                                                              return ext_call.return_data[0]
                                                                      else:
                                                                          require ext_code.size(stor5)
                                                                          static call stor5.balanceOf(address owner) with:
                                                                                  gas gas_remaining wei
                                                                                 args this.address
                                                                          if not ext_call.success:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >= 32
                                                                              require ext_code.size(stor5)
                                                                              call stor5.transfer(address to, uint256 value) with:
                                                                                   gas gas_remaining wei
                                                                                  args stor2, ext_call.return_data[0]
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  log 0xbc43d7c0: _param1, 0, stor8
                                                                                  return ext_call.return_data[0]
                                                                  else:
                                                                      log 0xbc43d7c0: _param1, 0, stor8
                                                                      return ext_call.return_data[0]
              else:
                  require ext_call.return_data[0] > 0
                  require ext_call.return_data[0]
                  if stor0[tx.origin] != 1:
                      revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                  else:
                      if stor0[caller] != 1:
                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                      else:
                          require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
                          static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
                                  gas gas_remaining wei
                                 args stor2
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              if ext_call.return_data[0] < _param1:
                                  revert with 0, 'Not enough WETH funds'
                              else:
                                  require ext_code.size(stor3)
                                  call stor3.transferFrom(address from, address to, uint256 value) with:
                                       gas gas_remaining wei
                                      args stor2, addr(this.address), _param1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(stor3)
                                      call stor3.withdraw(uint256 wdamount) with:
                                           gas gas_remaining wei
                                          args _param1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require ext_code.size(stor7)
                                          call stor7.ethToTokenTransferInput(uint256 min_tokens, uint256 deadline, address recipient) with:
                                             value _param1 wei
                                               gas gas_remaining wei
                                              args 0 / ext_call.return_data[0] / 10^18, block.timestamp, stor2
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              require ext_code.size(stor5)
                                              static call stor5.0x182df0f5 with:
                                                      gas gas_remaining wei
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      if stor0[tx.origin] != 1:
                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                      else:
                                                          if stor0[caller] != 1:
                                                              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                          else:
                                                              require ext_code.size(stor5)
                                                              static call stor5.balanceOf(address owner) with:
                                                                      gas gas_remaining wei
                                                                     args this.address
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 32
                                                                  if ext_call.return_data[0] > 0:
                                                                      if ext_call.return_data[0] != -1:
                                                                          require ext_code.size(stor5)
                                                                          call stor5.transfer(address to, uint256 value) with:
                                                                               gas gas_remaining wei
                                                                              args stor2, ext_call.return_data[0]
                                                                          if not ext_call.success:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              log 0xbc43d7c0: _param1, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                              return ext_call.return_data[0]
                                                                      else:
                                                                          require ext_code.size(stor5)
                                                                          static call stor5.balanceOf(address owner) with:
                                                                                  gas gas_remaining wei
                                                                                 args this.address
                                                                          if not ext_call.success:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >= 32
                                                                              require ext_code.size(stor5)
                                                                              call stor5.transfer(address to, uint256 value) with:
                                                                                   gas gas_remaining wei
                                                                                  args stor2, ext_call.return_data[0]
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  log 0xbc43d7c0: _param1, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                                  return ext_call.return_data[0]
                                                                  else:
                                                                      log 0xbc43d7c0: _param1, ext_call.return_data[0] * ext_call.return_data[0] / 10^18, stor8
                                                                      return ext_call.return_data[0]
                                                  else:
                                                      if stor0[tx.origin] != 1:
                                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                      else:
                                                          if stor0[caller] != 1:
                                                              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[491 len 25]
                                                          else:
                                                              require ext_code.size(stor5)
                                                              static call stor5.balanceOf(address owner) with:
                                                                      gas gas_remaining wei
                                                                     args this.address
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >= 32
                                                                  if ext_call.return_data[0] > 0:
                                                                      if ext_call.return_data[0] != -1:
                                                                          require ext_code.size(stor5)
                                                                          call stor5.transfer(address to, uint256 value) with:
                                                                               gas gas_remaining wei
                                                                              args stor2, ext_call.return_data[0]
                                                                          if not ext_call.success:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              log 0xbc43d7c0: _param1, 0, stor8
                                                                              return ext_call.return_data[0]
                                                                      else:
                                                                          require ext_code.size(stor5)
                                                                          static call stor5.balanceOf(address owner) with:
                                                                                  gas gas_remaining wei
                                                                                 args this.address
                                                                          if not ext_call.success:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >= 32
                                                                              require ext_code.size(stor5)
                                                                              call stor5.transfer(address to, uint256 value) with:
                                                                                   gas gas_remaining wei
                                                                                  args stor2, ext_call.return_data[0]
                                                                              if not ext_call.success:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  log 0xbc43d7c0: _param1, 0, stor8
                                                                                  return ext_call.return_data[0]
                                                                  else:
                                                                      log 0xbc43d7c0: _param1, 0, stor8
                                                                      return ext_call.return_data[0]


# hash = 0xdaea85c5
# getter = None
# const = None
# payable = False
def approve(address _token): # not payable
  require calldata.size - 4 >= 32
  if stor0[tx.origin] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if stor0[caller] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if stor0[tx.origin] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if stor0[caller] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  require ext_code.size(stor5)
  static call stor5.allowance(address owner, address spender) with:
          gas gas_remaining wei
         args addr(this.address), stor7
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < -1:
      require ext_code.size(stor5)
      call stor5.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args stor7, -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


# hash = 0xdd4549b7
# getter = None
# const = None
# payable = False
def unknowndd4549b7(uint256 _param1): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(stor5)
  static call stor5.0x182df0f5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require 10^18 * _param1 / 10^18 == _param1
      if 10^18 * _param1:
          require 10^18 * _param1
          require 1000000000000000000 * 10^18 * _param1 / 10^18 * _param1 == 10^18
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          if stor0[tx.origin] != 1:
              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
          else:
              if stor0[caller] != 1:
                  revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
              else:
                  require ext_code.size(stor5)
                  static call stor5.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args stor2
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if ext_call.return_data[0] < 1000000000000000000 * 10^18 * _param1 / ext_call.return_data[0] / 10^18:
                          revert with 0, 'Not enough ERC20 funds'
                      else:
                          require ext_code.size(stor5)
                          call stor5.transferFrom(address from, address to, uint256 value) with:
                               gas gas_remaining wei
                              args stor2, addr(this.address), 1000000000000000000 * 10^18 * _param1 / ext_call.return_data[0] / 10^18
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(stor7)
                              static call stor7.getTokenToEthInputPrice(uint256 tokens_sold) with:
                                      gas gas_remaining wei
                                     args (1000000000000000000 * 10^18 * _param1 / ext_call.return_data[0] / 10^18)
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(stor7)
                                  call stor7.tokenToEthSwapInput(uint256 tokens_sold, uint256 min_eth, uint256 deadline) with:
                                       gas gas_remaining wei
                                      args 1000000000000000000 * 10^18 * _param1 / ext_call.return_data[0] / 10^18, ext_call.return_data[0], block.timestamp
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if stor0[tx.origin] != 1:
                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                                      else:
                                          if stor0[caller] != 1:
                                              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                                          else:
                                              if eth.balance(this.address) > 0:
                                                  if ext_call.return_data[0] != -1:
                                                      require ext_code.size(stor3)
                                                      call stor3.deposit() with:
                                                         value ext_call.return_data[0] wei
                                                           gas gas_remaining wei
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      else:
                                                          require ext_code.size(stor3)
                                                          call stor3.transfer(address to, uint256 value) with:
                                                               gas gas_remaining wei
                                                              args stor2, ext_call.return_data[0]
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 32
                                                              log 0xbc43d7c0: ext_call.return_data[0], _param1, stor8
                                                              return ext_call.return_data[0]
                                                  else:
                                                      require ext_code.size(stor3)
                                                      call stor3.deposit() with:
                                                         value eth.balance(this.address) wei
                                                           gas gas_remaining wei
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      else:
                                                          require ext_code.size(stor3)
                                                          call stor3.transfer(address to, uint256 value) with:
                                                               gas gas_remaining wei
                                                              args stor2, eth.balance(this.address)
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 32
                                                              log 0xbc43d7c0: ext_call.return_data[0], _param1, stor8
                                                              return ext_call.return_data[0]
                                              else:
                                                  log 0xbc43d7c0: ext_call.return_data[0], _param1, stor8
                                                  return ext_call.return_data[0]
      else:
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          if stor0[tx.origin] != 1:
              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
          else:
              if stor0[caller] != 1:
                  revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
              else:
                  require ext_code.size(stor5)
                  static call stor5.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args stor2
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if ext_call.return_data[0] < 0 / ext_call.return_data[0] / 10^18:
                          revert with 0, 'Not enough ERC20 funds'
                      else:
                          require ext_code.size(stor5)
                          call stor5.transferFrom(address from, address to, uint256 value) with:
                               gas gas_remaining wei
                              args stor2, addr(this.address), 0 / ext_call.return_data[0] / 10^18
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(stor7)
                              static call stor7.getTokenToEthInputPrice(uint256 tokens_sold) with:
                                      gas gas_remaining wei
                                     args (0 / ext_call.return_data[0] / 10^18)
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(stor7)
                                  call stor7.tokenToEthSwapInput(uint256 tokens_sold, uint256 min_eth, uint256 deadline) with:
                                       gas gas_remaining wei
                                      args 0 / ext_call.return_data[0] / 10^18, ext_call.return_data[0], block.timestamp
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if stor0[tx.origin] != 1:
                                          revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                                      else:
                                          if stor0[caller] != 1:
                                              revert with 0, 32, 39, 0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e, mem[363 len 25]
                                          else:
                                              if eth.balance(this.address) > 0:
                                                  if ext_call.return_data[0] != -1:
                                                      require ext_code.size(stor3)
                                                      call stor3.deposit() with:
                                                         value ext_call.return_data[0] wei
                                                           gas gas_remaining wei
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      else:
                                                          require ext_code.size(stor3)
                                                          call stor3.transfer(address to, uint256 value) with:
                                                               gas gas_remaining wei
                                                              args stor2, ext_call.return_data[0]
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 32
                                                              log 0xbc43d7c0: ext_call.return_data[0], _param1, stor8
                                                              return ext_call.return_data[0]
                                                  else:
                                                      require ext_code.size(stor3)
                                                      call stor3.deposit() with:
                                                         value eth.balance(this.address) wei
                                                           gas gas_remaining wei
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      else:
                                                          require ext_code.size(stor3)
                                                          call stor3.transfer(address to, uint256 value) with:
                                                               gas gas_remaining wei
                                                              args stor2, eth.balance(this.address)
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >= 32
                                                              log 0xbc43d7c0: ext_call.return_data[0], _param1, stor8
                                                              return ext_call.return_data[0]
                                              else:
                                                  log 0xbc43d7c0: ext_call.return_data[0], _param1, stor8
                                                  return ext_call.return_data[0]


# hash = 0xe456e0f6
# getter = None
# const = None
# payable = False
def unknowne456e0f6(): # not payable
  require calldata.size - 4 >= 64
  require cd[4] <= 4294967296
  require cd[4] + 36 <= calldata.size
  require ('cd', 4).length <= 4294967296 and cd[4] + (32 * ('cd', 4).length) + 36 <= calldata.size
  if addr(cd[36]) != stor4:
      return ''
  mem[96] = 3 * ('cd', 4).length
  mem[64] = (32 * 3 * ('cd', 4).length) + 128
  if not 3 * ('cd', 4).length:
      [94midx = 0
      [94ms = 0
      while [94midx < ('cd', 4).length:
          require [94ms < mem[96]
          mem[(32 * [94ms) + 128] = cd[((32 * [94midx) + cd[4] + 36)]
          require [94midx < ('cd', 4).length
          if addr(cd[36]) == stor4:
              mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
              require ext_code.size(stor7)
              static call stor7.getTokenToEthOutputPrice(uint256 eth_bought) with:
                      gas gas_remaining wei
                     args cd[((32 * [94midx) + cd[4] + 36)]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if addr(cd[36]) == stor4:
                      mem[mem[64] + 4] = stor2
                      require ext_code.size(stor5)
                      static call stor5.balanceOf(address owner) with:
                              gas gas_remaining wei
                             args stor2
                      mem[mem[64]] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          if ext_call.return_data[0] >= ext_call.return_data[0]:
                              require ext_code.size(stor5)
                              static call stor5.0x182df0f5 with:
                                      gas gas_remaining wei
                              mem[mem[64]] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  [94m_317 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_317] = ext_call.return_data[0]
                                  [94m_326 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_326] = 0
                                  [94m_338 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_338] = 0
                                  if ext_call.return_data[0]:
                                      require ext_call.return_data[0]
                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                      [94m_378 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_378] = ext_call.return_data[0] * ext_call.return_data[0]
                                      require [94ms + 1 < mem[96]
                                      mem[(32 * [94ms + 1) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                      require [94midx < ('cd', 4).length
                                      if addr(cd[36]) == stor4:
                                          mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
                                          require ext_code.size(stor7)
                                          static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
                                                  gas gas_remaining wei
                                                 args cd[((32 * [94midx) + cd[4] + 36)]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              require ext_code.size(stor5)
                                              static call stor5.0x182df0f5 with:
                                                      gas gas_remaining wei
                                              mem[mem[64]] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  [94m_475 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_475] = ext_call.return_data[0]
                                                  [94m_480 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_480] = 0
                                                  [94m_486 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_486] = 0
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      [94m_498 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_498] = ext_call.return_data[0] * ext_call.return_data[0]
                                                      require [94ms + 2 < mem[96]
                                                      mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                      [94midx = [94midx + 1
                                                      [94ms = [94ms + 3
                                                      continue 
                                                  else:
                                                      [94m_492 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_492] = 0
                                                      require [94ms + 2 < mem[96]
                                                      mem[(32 * [94ms + 2) + 128] = 0 / 10^18
                                                      [94midx = [94midx + 1
                                                      [94ms = [94ms + 3
                                                      continue 
                                      else:
                                          require [94ms + 2 < mem[96]
                                          mem[(32 * [94ms + 2) + 128] = 0
                                          [94midx = [94midx + 1
                                          [94ms = [94ms + 3
                                          continue 
                                  else:
                                      [94m_368 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_368] = 0
                                      require [94ms + 1 < mem[96]
                                      mem[(32 * [94ms + 1) + 128] = 0 / 10^18
                                      require [94midx < ('cd', 4).length
                                      if addr(cd[36]) == stor4:
                                          mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
                                          require ext_code.size(stor7)
                                          static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
                                                  gas gas_remaining wei
                                                 args cd[((32 * [94midx) + cd[4] + 36)]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              require ext_code.size(stor5)
                                              static call stor5.0x182df0f5 with:
                                                      gas gas_remaining wei
                                              mem[mem[64]] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  [94m_467 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_467] = ext_call.return_data[0]
                                                  [94m_476 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_476] = 0
                                                  [94m_482 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_482] = 0
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      [94m_493 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_493] = ext_call.return_data[0] * ext_call.return_data[0]
                                                      require [94ms + 2 < mem[96]
                                                      mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                      [94midx = [94midx + 1
                                                      [94ms = [94ms + 3
                                                      continue 
                                                  else:
                                                      [94m_490 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_490] = 0
                                                      require [94ms + 2 < mem[96]
                                                      mem[(32 * [94ms + 2) + 128] = 0 / 10^18
                                                      [94midx = [94midx + 1
                                                      [94ms = [94ms + 3
                                                      continue 
                                      else:
                                          require [94ms + 2 < mem[96]
                                          mem[(32 * [94ms + 2) + 128] = 0
                                          [94midx = [94midx + 1
                                          [94ms = [94ms + 3
                                          continue 
                          else:
                              require [94ms + 1 < mem[96]
                              mem[(32 * [94ms + 1) + 128] = -1
                              require [94midx < ('cd', 4).length
                              if addr(cd[36]) == stor4:
                                  mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
                                  require ext_code.size(stor7)
                                  static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
                                          gas gas_remaining wei
                                         args cd[((32 * [94midx) + cd[4] + 36)]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(stor5)
                                      static call stor5.0x182df0f5 with:
                                              gas gas_remaining wei
                                      mem[mem[64]] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          [94m_385 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_385] = ext_call.return_data[0]
                                          [94m_396 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_396] = 0
                                          [94m_403 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_403] = 0
                                          if ext_call.return_data[0]:
                                              require ext_call.return_data[0]
                                              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                              [94m_424 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_424] = ext_call.return_data[0] * ext_call.return_data[0]
                                              require [94ms + 2 < mem[96]
                                              mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                              [94midx = [94midx + 1
                                              [94ms = [94ms + 3
                                              continue 
                                          else:
                                              [94m_420 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_420] = 0
                                              require [94ms + 2 < mem[96]
                                              mem[(32 * [94ms + 2) + 128] = 0 / 10^18
                                              [94midx = [94midx + 1
                                              [94ms = [94ms + 3
                                              continue 
                              else:
                                  require [94ms + 2 < mem[96]
                                  mem[(32 * [94ms + 2) + 128] = 0
                                  [94midx = [94midx + 1
                                  [94ms = [94ms + 3
                                  continue 
                  else:
                      require [94ms + 1 < mem[96]
                      mem[(32 * [94ms + 1) + 128] = -1
                      require [94midx < ('cd', 4).length
                      if addr(cd[36]) == stor4:
                          mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
                          require ext_code.size(stor7)
                          static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
                                  gas gas_remaining wei
                                 args cd[((32 * [94midx) + cd[4] + 36)]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(stor5)
                              static call stor5.0x182df0f5 with:
                                      gas gas_remaining wei
                              mem[mem[64]] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  [94m_364 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_364] = ext_call.return_data[0]
                                  [94m_374 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_374] = 0
                                  [94m_393 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_393] = 0
                                  if ext_call.return_data[0]:
                                      require ext_call.return_data[0]
                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                      [94m_414 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_414] = ext_call.return_data[0] * ext_call.return_data[0]
                                      require [94ms + 2 < mem[96]
                                      mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                      [94midx = [94midx + 1
                                      [94ms = [94ms + 3
                                      continue 
                                  else:
                                      [94m_407 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_407] = 0
                                      require [94ms + 2 < mem[96]
                                      mem[(32 * [94ms + 2) + 128] = 0 / 10^18
                                      [94midx = [94midx + 1
                                      [94ms = [94ms + 3
                                      continue 
                      else:
                          require [94ms + 2 < mem[96]
                          mem[(32 * [94ms + 2) + 128] = 0
                          [94midx = [94midx + 1
                          [94ms = [94ms + 3
                          continue 
          else:
              require [94ms + 1 < mem[96]
              mem[(32 * [94ms + 1) + 128] = -1
              require [94midx < ('cd', 4).length
              if addr(cd[36]) == stor4:
                  mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
                  require ext_code.size(stor7)
                  static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
                          gas gas_remaining wei
                         args cd[((32 * [94midx) + cd[4] + 36)]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      require ext_code.size(stor5)
                      static call stor5.0x182df0f5 with:
                              gas gas_remaining wei
                      mem[mem[64]] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          [94m_323 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_323] = ext_call.return_data[0]
                          [94m_332 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_332] = 0
                          [94m_347 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_347] = 0
                          if ext_call.return_data[0]:
                              require ext_call.return_data[0]
                              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                              [94m_386 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_386] = ext_call.return_data[0] * ext_call.return_data[0]
                              require [94ms + 2 < mem[96]
                              mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                              [94midx = [94midx + 1
                              [94ms = [94ms + 3
                              continue 
                          else:
                              [94m_375 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_375] = 0
                              require [94ms + 2 < mem[96]
                              mem[(32 * [94ms + 2) + 128] = 0 / 10^18
                              [94midx = [94midx + 1
                              [94ms = [94ms + 3
                              continue 
              else:
                  require [94ms + 2 < mem[96]
                  mem[(32 * [94ms + 2) + 128] = 0
                  [94midx = [94midx + 1
                  [94ms = [94ms + 3
                  continue 
  else:
      mem[128 len 32 * 3 * ('cd', 4).length] = code.data[12710 len 32 * 3 * ('cd', 4).length]
      [94midx = 0
      [94ms = 0
      while [94midx < ('cd', 4).length:
          require [94ms < mem[96]
          mem[(32 * [94ms) + 128] = cd[((32 * [94midx) + cd[4] + 36)]
          require [94midx < ('cd', 4).length
          if addr(cd[36]) == stor4:
              mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
              require ext_code.size(stor7)
              static call stor7.getTokenToEthOutputPrice(uint256 eth_bought) with:
                      gas gas_remaining wei
                     args cd[((32 * [94midx) + cd[4] + 36)]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  require return_data.size >= 32
                  if addr(cd[36]) == stor4:
                      mem[mem[64] + 4] = stor2
                      require ext_code.size(stor5)
                      static call stor5.balanceOf(address owner) with:
                              gas gas_remaining wei
                             args stor2
                      mem[mem[64]] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          if ext_call.return_data[0] >= ext_call.return_data[0]:
                              require ext_code.size(stor5)
                              static call stor5.0x182df0f5 with:
                                      gas gas_remaining wei
                              mem[mem[64]] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  [94m_320 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_320] = ext_call.return_data[0]
                                  [94m_329 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_329] = 0
                                  [94m_340 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_340] = 0
                                  if ext_call.return_data[0]:
                                      require ext_call.return_data[0]
                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                      [94m_381 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_381] = ext_call.return_data[0] * ext_call.return_data[0]
                                      require [94ms + 1 < mem[96]
                                      mem[(32 * [94ms + 1) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                      require [94midx < ('cd', 4).length
                                      if addr(cd[36]) == stor4:
                                          mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
                                          require ext_code.size(stor7)
                                          static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
                                                  gas gas_remaining wei
                                                 args cd[((32 * [94midx) + cd[4] + 36)]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              require ext_code.size(stor5)
                                              static call stor5.0x182df0f5 with:
                                                      gas gas_remaining wei
                                              mem[mem[64]] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  [94m_478 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_478] = ext_call.return_data[0]
                                                  [94m_481 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_481] = 0
                                                  [94m_487 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_487] = 0
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      [94m_501 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_501] = ext_call.return_data[0] * ext_call.return_data[0]
                                                      require [94ms + 2 < mem[96]
                                                      mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                      [94midx = [94midx + 1
                                                      [94ms = [94ms + 3
                                                      continue 
                                                  else:
                                                      [94m_495 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_495] = 0
                                                      require [94ms + 2 < mem[96]
                                                      mem[(32 * [94ms + 2) + 128] = 0 / 10^18
                                                      [94midx = [94midx + 1
                                                      [94ms = [94ms + 3
                                                      continue 
                                      else:
                                          require [94ms + 2 < mem[96]
                                          mem[(32 * [94ms + 2) + 128] = 0
                                          [94midx = [94midx + 1
                                          [94ms = [94ms + 3
                                          continue 
                                  else:
                                      [94m_371 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_371] = 0
                                      require [94ms + 1 < mem[96]
                                      mem[(32 * [94ms + 1) + 128] = 0 / 10^18
                                      require [94midx < ('cd', 4).length
                                      if addr(cd[36]) == stor4:
                                          mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
                                          require ext_code.size(stor7)
                                          static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
                                                  gas gas_remaining wei
                                                 args cd[((32 * [94midx) + cd[4] + 36)]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              require ext_code.size(stor5)
                                              static call stor5.0x182df0f5 with:
                                                      gas gas_remaining wei
                                              mem[mem[64]] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  [94m_470 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_470] = ext_call.return_data[0]
                                                  [94m_479 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_479] = 0
                                                  [94m_483 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_483] = 0
                                                  if ext_call.return_data[0]:
                                                      require ext_call.return_data[0]
                                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                      [94m_496 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_496] = ext_call.return_data[0] * ext_call.return_data[0]
                                                      require [94ms + 2 < mem[96]
                                                      mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                                      [94midx = [94midx + 1
                                                      [94ms = [94ms + 3
                                                      continue 
                                                  else:
                                                      [94m_491 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_491] = 0
                                                      require [94ms + 2 < mem[96]
                                                      mem[(32 * [94ms + 2) + 128] = 0 / 10^18
                                                      [94midx = [94midx + 1
                                                      [94ms = [94ms + 3
                                                      continue 
                                      else:
                                          require [94ms + 2 < mem[96]
                                          mem[(32 * [94ms + 2) + 128] = 0
                                          [94midx = [94midx + 1
                                          [94ms = [94ms + 3
                                          continue 
                          else:
                              require [94ms + 1 < mem[96]
                              mem[(32 * [94ms + 1) + 128] = -1
                              require [94midx < ('cd', 4).length
                              if addr(cd[36]) == stor4:
                                  mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
                                  require ext_code.size(stor7)
                                  static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
                                          gas gas_remaining wei
                                         args cd[((32 * [94midx) + cd[4] + 36)]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(stor5)
                                      static call stor5.0x182df0f5 with:
                                              gas gas_remaining wei
                                      mem[mem[64]] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          [94m_389 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_389] = ext_call.return_data[0]
                                          [94m_399 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_399] = 0
                                          [94m_405 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_405] = 0
                                          if ext_call.return_data[0]:
                                              require ext_call.return_data[0]
                                              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                              [94m_426 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_426] = ext_call.return_data[0] * ext_call.return_data[0]
                                              require [94ms + 2 < mem[96]
                                              mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                              [94midx = [94midx + 1
                                              [94ms = [94ms + 3
                                              continue 
                                          else:
                                              [94m_422 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_422] = 0
                                              require [94ms + 2 < mem[96]
                                              mem[(32 * [94ms + 2) + 128] = 0 / 10^18
                                              [94midx = [94midx + 1
                                              [94ms = [94ms + 3
                                              continue 
                              else:
                                  require [94ms + 2 < mem[96]
                                  mem[(32 * [94ms + 2) + 128] = 0
                                  [94midx = [94midx + 1
                                  [94ms = [94ms + 3
                                  continue 
                  else:
                      require [94ms + 1 < mem[96]
                      mem[(32 * [94ms + 1) + 128] = -1
                      require [94midx < ('cd', 4).length
                      if addr(cd[36]) == stor4:
                          mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
                          require ext_code.size(stor7)
                          static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
                                  gas gas_remaining wei
                                 args cd[((32 * [94midx) + cd[4] + 36)]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(stor5)
                              static call stor5.0x182df0f5 with:
                                      gas gas_remaining wei
                              mem[mem[64]] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  [94m_367 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_367] = ext_call.return_data[0]
                                  [94m_376 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_376] = 0
                                  [94m_395 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_395] = 0
                                  if ext_call.return_data[0]:
                                      require ext_call.return_data[0]
                                      require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                      [94m_417 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_417] = ext_call.return_data[0] * ext_call.return_data[0]
                                      require [94ms + 2 < mem[96]
                                      mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                                      [94midx = [94midx + 1
                                      [94ms = [94ms + 3
                                      continue 
                                  else:
                                      [94m_410 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_410] = 0
                                      require [94ms + 2 < mem[96]
                                      mem[(32 * [94ms + 2) + 128] = 0 / 10^18
                                      [94midx = [94midx + 1
                                      [94ms = [94ms + 3
                                      continue 
                      else:
                          require [94ms + 2 < mem[96]
                          mem[(32 * [94ms + 2) + 128] = 0
                          [94midx = [94midx + 1
                          [94ms = [94ms + 3
                          continue 
          else:
              require [94ms + 1 < mem[96]
              mem[(32 * [94ms + 1) + 128] = -1
              require [94midx < ('cd', 4).length
              if addr(cd[36]) == stor4:
                  mem[mem[64] + 4] = cd[((32 * [94midx) + cd[4] + 36)]
                  require ext_code.size(stor7)
                  static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
                          gas gas_remaining wei
                         args cd[((32 * [94midx) + cd[4] + 36)]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      require ext_code.size(stor5)
                      static call stor5.0x182df0f5 with:
                              gas gas_remaining wei
                      mem[mem[64]] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          [94m_325 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_325] = ext_call.return_data[0]
                          [94m_333 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_333] = 0
                          [94m_353 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_353] = 0
                          if ext_call.return_data[0]:
                              require ext_call.return_data[0]
                              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                              [94m_390 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_390] = ext_call.return_data[0] * ext_call.return_data[0]
                              require [94ms + 2 < mem[96]
                              mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / 10^18
                              [94midx = [94midx + 1
                              [94ms = [94ms + 3
                              continue 
                          else:
                              [94m_377 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_377] = 0
                              require [94ms + 2 < mem[96]
                              mem[(32 * [94ms + 2) + 128] = 0 / 10^18
                              [94midx = [94midx + 1
                              [94ms = [94ms + 3
                              continue 
              else:
                  require [94ms + 2 < mem[96]
                  mem[(32 * [94ms + 2) + 128] = 0
                  [94midx = [94midx + 1
                  [94ms = [94ms + 3
                  continue 
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[96]
  mem[mem[64] + 64 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  return 32, mem[mem[64] + 32 len (32 * mem[96]) + 32]


# hash = 0xeba1b60b
# getter = None
# const = None
# payable = False
def unknowneba1b60b(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if _param2 != stor4:
      return 0
  require ext_code.size(stor7)
  static call stor7.getEthToTokenInputPrice(uint256 eth_sold) with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(stor5)
  static call stor5.0x182df0f5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  require ext_call.return_data[0]
  require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
  return (ext_call.return_data[0] * ext_call.return_data[0] / 10^18)


# hash = 0xf14210a6
# getter = None
# const = None
# payable = False
def withdrawETH(uint256 _amount): # not payable
  require calldata.size - 4 >= 32
  if stor0[tx.origin] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if stor0[caller] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if eth.balance(this.address) > 0:
      call stor2 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


