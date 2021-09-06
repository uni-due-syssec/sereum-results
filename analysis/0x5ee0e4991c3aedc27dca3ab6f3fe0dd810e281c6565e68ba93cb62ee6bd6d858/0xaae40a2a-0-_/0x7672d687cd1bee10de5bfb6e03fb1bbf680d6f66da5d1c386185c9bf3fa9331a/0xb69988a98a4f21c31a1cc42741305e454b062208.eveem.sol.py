# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xB69988A98A4F21c31a1cC42741305e454B062208 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0xa79745e1': 'unknowna79745e1(?)'} 

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
    unknowne9610916Address # mask: a s
    # storage address 5
    unknown44c89894Address # mask: a s
    # storage address 6
    unknown2c8952eaAddress # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    ETHAddress # mask: a s
    # storage address 9
    unknowna1b4d011Address # mask: a s
    # storage address 10
    DAIAddress # mask: a s
    # storage address 11
    limit # mask: a s
    # storage address 12
    unknown8b738e2f
# hash = 0x06846ec0
# getter = None
# const = None
# payable = False
def unknown06846ec0(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if eth.balance(this.address) > 0:
      require ext_code.size(mstor3)
      if m_param1 != -1:
          call mstor3.deposit() with:
             value m_param1 wei
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(mstor3)
          call mstor3.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args mstor2, m_param1
      else:
          call mstor3.deposit() with:
             value eth.balance(this.address) wei
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(mstor3)
          call mstor3.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args mstor2, eth.balance(this.address)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


# hash = 0x12424e3f
# getter = None
# const = None
# payable = False
def unknown12424e3f(): # not payable
  if mstor1 != caller:
      revert with 0, 'Must be the commander.'
  [94midx = 0
  mwhile [94midx < munknown8b738e2fm.lengthm:
      mem[100] = munknown8b738e2fm[[94midxm]
      mem[132] = -1
      require ext_code.size(munknown8b738e2fm[[94midxm])
      call munknown8b738e2fm[[94midxm].approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args munknown8b738e2fm[[94midxm], -1
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require [94midx < munknown8b738e2fm.length
      mem[0] = 12
      if munknown8b738e2fm[[94midxm] != munknowna1b4d011Address:
          require [94midx < munknown8b738e2fm.length
          require ext_code.size(munknown8b738e2fm[[94midxm])
          static call munknown8b738e2fm[[94midxm].underlying() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require [94midx < munknown8b738e2fm.length
          mem[0] = 12
          mem[100] = munknown8b738e2fm[[94midxm]
          mem[132] = -1
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args munknown8b738e2fm[[94midxm], -1
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x1e907595
# getter = None
# const = None
# payable = False
def unknown1e907595(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
  static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
          gas gas_remaining wei
         args mstor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < m_param1:
      revert with 0, 'Not enough WETH funds'
  require ext_code.size(mstor3)
  call mstor3.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args mstor2, addr(this.address), m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor3)
  call mstor3.withdraw(uint256 wdamount) with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x26273199
# getter = None
# const = None
# payable = False
def unknown26273199(addr m_param1, addr m_param2): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(m_param2)
  static call m_param2.balanceOf(address owner) with:
          gas gas_remaining wei
         args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x2c8952ea
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def unknown2c8952ea(): # not payable
  return munknown2c8952eaAddress


# hash = 0x392d661c
# getter = None
# const = None
# payable = False
def depositERC20(uint256 m_amount, address m_contractAddress): # not payable
  require calldata.size - 4 >= 64
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  require ext_code.size(m_contractAddress)
  static call m_contractAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args mstor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < m_amount:
      revert with 0, 'Not enough ERC20 funds'
  require ext_code.size(m_contractAddress)
  call m_contractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args mstor2, addr(this.address), m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0x44c89894
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def unknown44c89894(): # not payable
  return munknown44c89894Address


# hash = 0x7e5465ba
# getter = None
# const = None
# payable = False
def approve(address m_token, address m_proxy): # not payable
  require calldata.size - 4 >= 64
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  require ext_code.size(m_proxy)
  static call m_proxy.allowance(address owner, address spender) with:
          gas gas_remaining wei
         args addr(this.address), m_token
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < -1:
      require ext_code.size(m_proxy)
      call m_proxy.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args addr(m_token), -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


# hash = 0x8322fff2
# getter = ['storage', 160, 0, 8]
# const = None
# payable = False
def ETH(): # not payable
  return mETHAddress


# hash = 0x8b738e2f
# getter = ['storage', 160, 0, ['add', ['sha3', 12], ['cd', 4]]]
# const = None
# payable = False
def unknown8b738e2f(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < munknown8b738e2fm.length
  return munknown8b738e2fm[m_param1m]


# hash = 0xa1b4d011
# getter = ['storage', 160, 0, 9]
# const = None
# payable = False
def unknowna1b4d011(): # not payable
  return munknowna1b4d011Address


# hash = 0xa4d66daf
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def limit(): # not payable
  return mlimit


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
  if mstor1 != caller:
      revert with 0, 'Must be the commander.'
  [93mselfdestruct([91mstor1[93m)


# hash = 0xc20938e0
# getter = None
# const = None
# payable = False
def unknownc20938e0(uint256 m_param1, addr m_param2): # not payable
  require calldata.size - 4 >= 64
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  require ext_code.size(m_param2)
  static call m_param2.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > 0:
      require ext_code.size(m_param2)
      if m_param1 != -1:
          call m_param2.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args mstor2, m_param1
      else:
          static call m_param2.balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(m_param2)
          call m_param2.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args mstor2, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0xe0bab4c4
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def DAI(): # not payable
  return mDAIAddress


# hash = 0xe9610916
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def unknowne9610916(): # not payable
  return munknowne9610916Address


# hash = 0xf14210a6
# getter = None
# const = None
# payable = False
def withdrawETH(uint256 m_amount): # not payable
  require calldata.size - 4 >= 32
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  mem[203 len 25]
  if eth.balance(this.address) > 0:
      call mstor2 with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0xf97cf9ed
# getter = None
# const = None
# payable = False
def unknownf97cf9ed(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  if mstor1 != caller:
      revert with 0, 'Must be the commander.'
  mstor7 = m_param1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


