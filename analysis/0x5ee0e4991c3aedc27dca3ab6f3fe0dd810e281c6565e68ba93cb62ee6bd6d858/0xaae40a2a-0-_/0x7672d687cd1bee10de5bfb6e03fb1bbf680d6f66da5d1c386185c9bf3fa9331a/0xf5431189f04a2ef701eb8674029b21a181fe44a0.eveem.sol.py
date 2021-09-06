# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xF5431189F04a2Ef701EB8674029b21A181FE44a0 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x2d6ef077': 'unknown2d6ef077(?)', '0x725aaa3c': 'unknown725aaa3c(?)'} 

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
    unknown44c89894Address # mask: a s
    # storage address 5
    unknown2c8952eaAddress # mask: a s
    # storage address 6
    ETHAddress # mask: a s
    # storage address 7
    unknowna1b4d011Address # mask: a s
    # storage address 8
    DAIAddress # mask: a s
    # storage address 9
    limit # mask: a s
    # storage address 10
    unknown8b738e2f
# hash = 0x06846ec0
# getter = None
# const = None
# payable = True
def unknown06846ec0(uint256 _param1) payable: 
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


# hash = 0x124644e2
# getter = None
# const = None
# payable = True
def unknown124644e2(uint256 _param1, addr _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(_param2)
  static call _param2.0x182df0f5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  require ext_call.return_data[0]
  require ext_call.return_data[0] * _param1 / ext_call.return_data[0] == _param1
  return (ext_call.return_data[0] * _param1 / 10^18)


# hash = 0x1e907595
# getter = None
# const = None
# payable = True
def unknown1e907595(uint256 _param1) payable: 
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
# payable = True
def unknown26273199(addr _param1, addr _param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(_param2)
  static call _param2.balanceOf(address owner) with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x27ea6f2b
# getter = None
# const = None
# payable = True
def setLimit(uint256 _limit) payable: 
  require calldata.size - 4 >= 32
  if stor1 != caller:
      revert with 0, 'Must be the commander.'
  limit = _limit


# hash = 0x2c8952ea
# getter = ['storage', 160, 0, 5]
# const = None
# payable = True
def unknown2c8952ea() payable: 
  return unknown2c8952eaAddress


# hash = 0x392d661c
# getter = None
# const = None
# payable = True
def depositERC20(uint256 _amount, address _contractAddress) payable: 
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


# hash = 0x44c89894
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def unknown44c89894() payable: 
  return unknown44c89894Address


# hash = 0x4e89a711
# getter = None
# const = None
# payable = True
def unknown4e89a711(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if _param1 == unknowna1b4d011Address:
      return ETHAddress
  require ext_code.size(_param1)
  static call _param1.underlying() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[12 len 20]


# hash = 0x523602b7
# getter = None
# const = None
# payable = True
def unknown523602b7() payable: 
  if not unknown8b738e2f.length:
      mem[(32 * unknown8b738e2f.length) + 128] = 32
      mem[(32 * unknown8b738e2f.length) + 160] = unknown8b738e2f.length
      mem[(32 * unknown8b738e2f.length) + 192 len floor32(unknown8b738e2f.length)] = mem[128 len floor32(unknown8b738e2f.length)]
      return memory
        from (32 * unknown8b738e2f.length) + 128
         [93mlen (96 * unknown8b738e2f.length) + 64
  mem[128] = addr(unknown8b738e2f.field_0)
  [94midx = 128
  [94ms = 0
  while (32 * unknown8b738e2f.length) + 96 > [94midx:
      mem[[94midx + 32] = unknown8b738e2f[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * unknown8b738e2f.length) + 192 len floor32(unknown8b738e2f.length)] = mem[128 len floor32(unknown8b738e2f.length)]
  return Array(len=unknown8b738e2f.length, data=mem[128 len floor32(unknown8b738e2f.length)], mem[(32 * unknown8b738e2f.length) + floor32(unknown8b738e2f.length) + 192 len (32 * unknown8b738e2f.length) - floor32(unknown8b738e2f.length)]), 


# hash = 0x7e5465ba
# getter = None
# const = None
# payable = True
def approve(address _token, address _proxy) payable: 
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


# hash = 0x8322fff2
# getter = ['storage', 160, 0, 6]
# const = None
# payable = True
def ETH() payable: 
  return ETHAddress


# hash = 0x8b738e2f
# getter = ['storage', 160, 0, ['add', ['sha3', 10], ['cd', 4]]]
# const = None
# payable = True
def unknown8b738e2f(uint256 _param1) payable: 
  require calldata.size - 4 >= 32
  require _param1 < unknown8b738e2f.length
  return unknown8b738e2f[_param1].field_0


# hash = 0xa1b4d011
# getter = ['storage', 160, 0, 7]
# const = None
# payable = True
def unknowna1b4d011() payable: 
  return unknowna1b4d011Address


# hash = 0xa4d66daf
# getter = ['storage', 256, 0, 9]
# const = None
# payable = True
def limit() payable: 
  return limit


# hash = 0xad5c4648
# getter = None
# const = ['return', 1097077688018008265106216665536940668749033598146]
# payable = True
const WETH = 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2


# hash = 0xb8b3dbc6
# getter = None
# const = None
# payable = True
def unknownb8b3dbc6() payable: 
  if stor1 != caller:
      revert with 0, 'Must be the commander.'
  [93mselfdestruct([91mstor1[93m)


# hash = 0xc20938e0
# getter = None
# const = None
# payable = True
def unknownc20938e0(uint256 _param1, addr _param2) payable: 
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


# hash = 0xcb90a988
# getter = None
# const = None
# payable = True
def unknowncb90a988() payable: 
  require calldata.size - 4 >= 32
  require cd[4] <= 4294967296
  require cd[4] + 36 <= calldata.size
  require ('cd', 4).length <= 4294967296 and cd[4] + (32 * ('cd', 4).length) + 36 <= calldata.size
  if not unknown8b738e2f.length:
      if not ('cd', 4).length:
          [94midx = 0
          [94ms = 0
          while [94midx < ('cd', 4).length:
              require ext_code.size(unknown2c8952eaAddress)
              static call unknown2c8952eaAddress.getAccountLiquidity(address account) with:
                      gas gas_remaining wei
                     args addr(cd[((32 * [94midx) + cd[4] + 36)])
              mem[128 len 96] = ext_call.return_data[0 len 96]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 96
              require [94ms < 0
              mem[(32 * [94ms) + 128] = [94midx
              require [94ms + 1 < 0
              mem[(32 * [94ms + 1) + 128] = ext_call.return_data[64]
              [94mt = 0
              [94mu = [94ms + 2
              while [94mt < unknown8b738e2f.length:
                  require [94mu < 0
                  mem[(32 * [94mu) + 128] = [94mt
                  require [94mt < unknown8b738e2f.length
                  require [94midx < ('cd', 4).length
                  mem[132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                  require ext_code.size(unknown8b738e2f[[94mt].field_0)
                  static call unknown8b738e2f[[94mt].field_0.0x95dd9193 with:
                          gas gas_remaining wei
                         args addr(cd[((32 * [94midx) + cd[4] + 36)])
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mu + 1 < 0
                  mem[(32 * [94mu + 1) + 128] = ext_call.return_data[0]
                  require [94mt < unknown8b738e2f.length
                  mem[0] = 10
                  require [94midx < ('cd', 4).length
                  mem[132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                  require ext_code.size(unknown8b738e2f[[94mt].field_0)
                  static call unknown8b738e2f[[94mt].field_0.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args addr(cd[((32 * [94midx) + cd[4] + 36)])
                  mem[128] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mu + 2 < 0
                  mem[(32 * [94mu + 2) + 128] = ext_call.return_data[0]
                  [94mt = [94mt + 1
                  [94mu = [94mu + 3
                  continue 
              [94midx = [94midx + 1
              [94ms = [94ms + (3 * unknown8b738e2f.length) + 2
              continue 
          return ''
      require ('cd', 4).length
      require 2 * ('cd', 4).length / ('cd', 4).length == 2
      if uint255(('cd', 4).length):
          mem[128 len 64 * ('cd', 4).length] = code.data[14816 len 64 * ('cd', 4).length]
      [94midx = 0
      [94ms = 0
      while [94midx < ('cd', 4).length:
          require ext_code.size(unknown2c8952eaAddress)
          static call unknown2c8952eaAddress.getAccountLiquidity(address account) with:
                  gas gas_remaining wei
                 args addr(cd[((32 * [94midx) + cd[4] + 36)])
          mem[(64 * ('cd', 4).length) + 128 len 96] = ext_call.return_data[0 len 96]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 96
          require [94ms < 2 * ('cd', 4).length
          mem[(32 * [94ms) + 128] = [94midx
          require [94ms + 1 < 2 * ('cd', 4).length
          mem[(32 * [94ms + 1) + 128] = ext_call.return_data[64]
          [94mt = 0
          [94mu = [94ms + 2
          while [94mt < unknown8b738e2f.length:
              require [94mu < 2 * ('cd', 4).length
              mem[(32 * [94mu) + 128] = [94mt
              require [94mt < unknown8b738e2f.length
              require [94midx < ('cd', 4).length
              require ext_code.size(unknown8b738e2f[[94mt].field_0)
              static call unknown8b738e2f[[94mt].field_0.0x95dd9193 with:
                      gas gas_remaining wei
                     args addr(cd[((32 * [94midx) + cd[4] + 36)])
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require [94mu + 1 < 2 * ('cd', 4).length
              mem[(32 * [94mu + 1) + 128] = ext_call.return_data[0]
              require [94mt < unknown8b738e2f.length
              mem[0] = 10
              require [94midx < ('cd', 4).length
              mem[(64 * ('cd', 4).length) + 132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              require ext_code.size(unknown8b738e2f[[94mt].field_0)
              static call unknown8b738e2f[[94mt].field_0.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args addr(cd[((32 * [94midx) + cd[4] + 36)])
              mem[(64 * ('cd', 4).length) + 128] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require [94mu + 2 < 2 * ('cd', 4).length
              mem[(32 * [94mu + 2) + 128] = ext_call.return_data[0]
              [94mt = [94mt + 1
              [94mu = [94mu + 3
              continue 
          [94midx = [94midx + 1
          [94ms = [94ms + (3 * unknown8b738e2f.length) + 2
          continue 
      mem[(64 * ('cd', 4).length) + 192 len 2 * Mask(251, 4, ('cd', 4).length)] = mem[128 len 2 * Mask(251, 4, ('cd', 4).length)]
      return Array(len=2 * ('cd', 4).length, data=mem[128 len 2 * Mask(251, 4, ('cd', 4).length)], mem[(64 * ('cd', 4).length) + (2 * Mask(251, 4, ('cd', 4).length)) + 192 len (64 * ('cd', 4).length) - (2 * Mask(251, 4, ('cd', 4).length))]), 
  require unknown8b738e2f.length
  require 3 * unknown8b738e2f.length / unknown8b738e2f.length == 3
  require (3 * unknown8b738e2f.length) + 2 >= 3 * unknown8b738e2f.length
  if not ('cd', 4).length:
      [94midx = 0
      [94ms = 0
      while [94midx < ('cd', 4).length:
          require ext_code.size(unknown2c8952eaAddress)
          static call unknown2c8952eaAddress.getAccountLiquidity(address account) with:
                  gas gas_remaining wei
                 args addr(cd[((32 * [94midx) + cd[4] + 36)])
          mem[128 len 96] = ext_call.return_data[0 len 96]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 96
          require [94ms < 0
          mem[(32 * [94ms) + 128] = [94midx
          require [94ms + 1 < 0
          mem[(32 * [94ms + 1) + 128] = ext_call.return_data[64]
          [94mt = 0
          [94mu = [94ms + 2
          while [94mt < unknown8b738e2f.length:
              require [94mu < 0
              mem[(32 * [94mu) + 128] = [94mt
              require [94mt < unknown8b738e2f.length
              require [94midx < ('cd', 4).length
              mem[132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              require ext_code.size(unknown8b738e2f[[94mt].field_0)
              static call unknown8b738e2f[[94mt].field_0.0x95dd9193 with:
                      gas gas_remaining wei
                     args addr(cd[((32 * [94midx) + cd[4] + 36)])
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require [94mu + 1 < 0
              mem[(32 * [94mu + 1) + 128] = ext_call.return_data[0]
              require [94mt < unknown8b738e2f.length
              mem[0] = 10
              require [94midx < ('cd', 4).length
              mem[132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              require ext_code.size(unknown8b738e2f[[94mt].field_0)
              static call unknown8b738e2f[[94mt].field_0.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args addr(cd[((32 * [94midx) + cd[4] + 36)])
              mem[128] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require [94mu + 2 < 0
              mem[(32 * [94mu + 2) + 128] = ext_call.return_data[0]
              [94mt = [94mt + 1
              [94mu = [94mu + 3
              continue 
          [94midx = [94midx + 1
          [94ms = [94ms + (3 * unknown8b738e2f.length) + 2
          continue 
      return ''
  require ('cd', 4).length
  require (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length) / ('cd', 4).length == (3 * unknown8b738e2f.length) + 2
  if (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length):
      mem[128 len 32 * (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)] = code.data[14816 len 32 * (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)]
  [94midx = 0
  [94ms = 0
  while [94midx < ('cd', 4).length:
      require ext_code.size(unknown2c8952eaAddress)
      static call unknown2c8952eaAddress.getAccountLiquidity(address account) with:
              gas gas_remaining wei
             args addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[(32 * (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)) + 128 len 96] = ext_call.return_data[0 len 96]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 96
      require [94ms < (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)
      mem[(32 * [94ms) + 128] = [94midx
      require [94ms + 1 < (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)
      mem[(32 * [94ms + 1) + 128] = ext_call.return_data[64]
      [94mt = 0
      [94mu = [94ms + 2
      while [94mt < unknown8b738e2f.length:
          require [94mu < (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)
          mem[(32 * [94mu) + 128] = [94mt
          require [94mt < unknown8b738e2f.length
          require [94midx < ('cd', 4).length
          require ext_code.size(unknown8b738e2f[[94mt].field_0)
          static call unknown8b738e2f[[94mt].field_0.0x95dd9193 with:
                  gas gas_remaining wei
                 args addr(cd[((32 * [94midx) + cd[4] + 36)])
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require [94mu + 1 < (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)
          mem[(32 * [94mu + 1) + 128] = ext_call.return_data[0]
          require [94mt < unknown8b738e2f.length
          mem[0] = 10
          require [94midx < ('cd', 4).length
          mem[(32 * (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)) + 132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
          require ext_code.size(unknown8b738e2f[[94mt].field_0)
          static call unknown8b738e2f[[94mt].field_0.balanceOf(address owner) with:
                  gas gas_remaining wei
                 args addr(cd[((32 * [94midx) + cd[4] + 36)])
          mem[(32 * (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require [94mu + 2 < (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)
          mem[(32 * [94mu + 2) + 128] = ext_call.return_data[0]
          [94mt = [94mt + 1
          [94mu = [94mu + 3
          continue 
      [94midx = [94midx + 1
      [94ms = [94ms + (3 * unknown8b738e2f.length) + 2
      continue 
  mem[(32 * (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)) + 128] = 32
  mem[(32 * (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)) + 160] = (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)
  mem[(32 * (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)) + 192 len floor32((2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length))] = mem[128 len floor32((2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length))]
  return Array(len=(2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length), data=mem[(32 * (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)) + 192 len 32 * (2 * ('cd', 4).length) + (3 * unknown8b738e2f.length * ('cd', 4).length)]), 


# hash = 0xe0bab4c4
# getter = ['storage', 160, 0, 8]
# const = None
# payable = True
def DAI() payable: 
  return DAIAddress


# hash = 0xf14210a6
# getter = None
# const = None
# payable = True
def withdrawETH(uint256 _amount) payable: 
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
  revert


