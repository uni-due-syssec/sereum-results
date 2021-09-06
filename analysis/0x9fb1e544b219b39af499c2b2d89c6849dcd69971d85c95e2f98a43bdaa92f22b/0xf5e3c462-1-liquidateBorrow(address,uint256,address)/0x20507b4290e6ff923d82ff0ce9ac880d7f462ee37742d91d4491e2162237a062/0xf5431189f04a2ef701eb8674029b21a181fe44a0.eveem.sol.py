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
def unknown06846ec0(uint256 m_param1) payable: 
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


# hash = 0x124644e2
# getter = None
# const = None
# payable = True
def unknown124644e2(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(m_param2)
  static call m_param2.0x182df0f5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      return 0
  require ext_call.return_data[0]
  require ext_call.return_data[0] * m_param1 / ext_call.return_data[0] == m_param1
  return (ext_call.return_data[0] * m_param1 / 10^18)


# hash = 0x1e907595
# getter = None
# const = None
# payable = True
def unknown1e907595(uint256 m_param1) payable: 
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
# payable = True
def unknown26273199(addr m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(m_param2)
  static call m_param2.balanceOf(address owner) with:
          gas gas_remaining wei
         args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x27ea6f2b
# getter = None
# const = None
# payable = True
def setLimit(uint256 m_limit) payable: 
  require calldata.size - 4 >= 32
  if mstor1 != caller:
      revert with 0, 'Must be the commander.'
  mlimit = m_limit


# hash = 0x2c8952ea
# getter = ['storage', 160, 0, 5]
# const = None
# payable = True
def unknown2c8952ea() payable: 
  return munknown2c8952eaAddress


# hash = 0x392d661c
# getter = None
# const = None
# payable = True
def depositERC20(uint256 m_amount, address m_contractAddress) payable: 
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
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def unknown44c89894() payable: 
  return munknown44c89894Address


# hash = 0x4e89a711
# getter = None
# const = None
# payable = True
def unknown4e89a711(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if m_param1 == munknowna1b4d011Address:
      return mETHAddress
  require ext_code.size(m_param1)
  static call m_param1.underlying() with:
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
  if not munknown8b738e2fm.length:
      mem[(32 * munknown8b738e2fm.length) + 128] = 32
      mem[(32 * munknown8b738e2fm.length) + 160] = munknown8b738e2fm.length
      mem[(32 * munknown8b738e2fm.length) + 192 len floor32(munknown8b738e2fm.length)] = mem[128 len floor32(munknown8b738e2fm.length)]
      return memory
        from (32 * munknown8b738e2fm.length) + 128
         [93mlen (96 * munknown8b738e2fm.length) + 64
  mem[128] = addr(munknown8b738e2fm.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknown8b738e2fm.length) + 96 > [94midxm:
      mem[[94midx + 32] = munknown8b738e2fm[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * munknown8b738e2fm.length) + 192 len floor32(munknown8b738e2fm.length)] = mem[128 len floor32(munknown8b738e2fm.length)]
  return Array(len=munknown8b738e2fm.length, data=mem[128 len floor32(munknown8b738e2fm.length)], mem[(32 * munknown8b738e2fm.length) + floor32(munknown8b738e2fm.length) + 192 len (32 * munknown8b738e2fm.length) - floor32(munknown8b738e2fm.length)]), 


# hash = 0x7e5465ba
# getter = None
# const = None
# payable = True
def approve(address m_token, address m_proxy) payable: 
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
# getter = ['storage', 160, 0, 6]
# const = None
# payable = True
def ETH() payable: 
  return mETHAddress


# hash = 0x8b738e2f
# getter = ['storage', 160, 0, ['add', ['sha3', 10], ['cd', 4]]]
# const = None
# payable = True
def unknown8b738e2f(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  require m_param1 < munknown8b738e2fm.length
  return munknown8b738e2fm[m_param1m]m.field_0


# hash = 0xa1b4d011
# getter = ['storage', 160, 0, 7]
# const = None
# payable = True
def unknowna1b4d011() payable: 
  return munknowna1b4d011Address


# hash = 0xa4d66daf
# getter = ['storage', 256, 0, 9]
# const = None
# payable = True
def limit() payable: 
  return mlimit


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
  if mstor1 != caller:
      revert with 0, 'Must be the commander.'
  [93mselfdestruct([91mstor1[93m)


# hash = 0xc20938e0
# getter = None
# const = None
# payable = True
def unknownc20938e0(uint256 m_param1, addr m_param2) payable: 
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


# hash = 0xcb90a988
# getter = None
# const = None
# payable = True
def unknowncb90a988() payable: 
  require calldata.size - 4 >= 32
  require cd[4] <= 4294967296
  require cd[4] + 36 <= calldata.size
  require m('cd', 4).length <= 4294967296 and cd[4] + (32 * m('cd', 4).length) + 36 <= calldata.size
  if not munknown8b738e2fm.length:
      if not m('cd', 4).length:
          [94midx = 0
          [94ms = 0
          mwhile [94midx < m('cd', 4).lengthm:
              require ext_code.size(munknown2c8952eaAddress)
              static call munknown2c8952eaAddress.getAccountLiquidity(address account) with:
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
              mwhile [94mt < munknown8b738e2fm.lengthm:
                  require [94mu < 0
                  mem[(32 * [94mu) + 128] = [94mt
                  require [94mt < munknown8b738e2fm.length
                  require [94midx < m('cd', 4).length
                  mem[132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                  require ext_code.size(munknown8b738e2fm[[94mtm]m.field_0)
                  static call munknown8b738e2fm[[94mtm]m.field_0.0x95dd9193 with:
                          gas gas_remaining wei
                         args addr(cd[((32 * [94midx) + cd[4] + 36)])
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mu + 1 < 0
                  mem[(32 * [94mu + 1) + 128] = ext_call.return_data[0]
                  require [94mt < munknown8b738e2fm.length
                  mem[0] = 10
                  require [94midx < m('cd', 4).length
                  mem[132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                  require ext_code.size(munknown8b738e2fm[[94mtm]m.field_0)
                  static call munknown8b738e2fm[[94mtm]m.field_0.balanceOf(address owner) with:
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
                  mcontinue 
              [94midx = [94midx + 1
              [94ms = [94ms + (3 * munknown8b738e2fm.length) + 2
              mcontinue 
          return ''
      require m('cd', 4).length
      require 2 * m('cd', 4).length / m('cd', 4).length == 2
      if uint255(m('cd', 4).length):
          mem[128 len 64 * m('cd', 4).length] = code.data[14816 len 64 * m('cd', 4).length]
      [94midx = 0
      [94ms = 0
      mwhile [94midx < m('cd', 4).lengthm:
          require ext_code.size(munknown2c8952eaAddress)
          static call munknown2c8952eaAddress.getAccountLiquidity(address account) with:
                  gas gas_remaining wei
                 args addr(cd[((32 * [94midx) + cd[4] + 36)])
          mem[(64 * m('cd', 4).length) + 128 len 96] = ext_call.return_data[0 len 96]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 96
          require [94ms < 2 * m('cd', 4).length
          mem[(32 * [94ms) + 128] = [94midx
          require [94ms + 1 < 2 * m('cd', 4).length
          mem[(32 * [94ms + 1) + 128] = ext_call.return_data[64]
          [94mt = 0
          [94mu = [94ms + 2
          mwhile [94mt < munknown8b738e2fm.lengthm:
              require [94mu < 2 * m('cd', 4).length
              mem[(32 * [94mu) + 128] = [94mt
              require [94mt < munknown8b738e2fm.length
              require [94midx < m('cd', 4).length
              require ext_code.size(munknown8b738e2fm[[94mtm]m.field_0)
              static call munknown8b738e2fm[[94mtm]m.field_0.0x95dd9193 with:
                      gas gas_remaining wei
                     args addr(cd[((32 * [94midx) + cd[4] + 36)])
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require [94mu + 1 < 2 * m('cd', 4).length
              mem[(32 * [94mu + 1) + 128] = ext_call.return_data[0]
              require [94mt < munknown8b738e2fm.length
              mem[0] = 10
              require [94midx < m('cd', 4).length
              mem[(64 * m('cd', 4).length) + 132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              require ext_code.size(munknown8b738e2fm[[94mtm]m.field_0)
              static call munknown8b738e2fm[[94mtm]m.field_0.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args addr(cd[((32 * [94midx) + cd[4] + 36)])
              mem[(64 * m('cd', 4).length) + 128] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require [94mu + 2 < 2 * m('cd', 4).length
              mem[(32 * [94mu + 2) + 128] = ext_call.return_data[0]
              [94mt = [94mt + 1
              [94mu = [94mu + 3
              mcontinue 
          [94midx = [94midx + 1
          [94ms = [94ms + (3 * munknown8b738e2fm.length) + 2
          mcontinue 
      mem[(64 * m('cd', 4).length) + 192 len 2 * Mask(251, 4, m('cd', 4).length)] = mem[128 len 2 * Mask(251, 4, m('cd', 4).length)]
      return Array(len=2 * m('cd', 4).length, data=mem[128 len 2 * Mask(251, 4, m('cd', 4).length)], mem[(64 * m('cd', 4).length) + (2 * Mask(251, 4, m('cd', 4).length)) + 192 len (64 * m('cd', 4).length) - (2 * Mask(251, 4, m('cd', 4).length))]), 
  require munknown8b738e2fm.length
  require 3 * munknown8b738e2fm.length / munknown8b738e2fm.length == 3
  require (3 * munknown8b738e2fm.length) + 2 >= 3 * munknown8b738e2fm.length
  if not m('cd', 4).length:
      [94midx = 0
      [94ms = 0
      mwhile [94midx < m('cd', 4).lengthm:
          require ext_code.size(munknown2c8952eaAddress)
          static call munknown2c8952eaAddress.getAccountLiquidity(address account) with:
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
          mwhile [94mt < munknown8b738e2fm.lengthm:
              require [94mu < 0
              mem[(32 * [94mu) + 128] = [94mt
              require [94mt < munknown8b738e2fm.length
              require [94midx < m('cd', 4).length
              mem[132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              require ext_code.size(munknown8b738e2fm[[94mtm]m.field_0)
              static call munknown8b738e2fm[[94mtm]m.field_0.0x95dd9193 with:
                      gas gas_remaining wei
                     args addr(cd[((32 * [94midx) + cd[4] + 36)])
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require [94mu + 1 < 0
              mem[(32 * [94mu + 1) + 128] = ext_call.return_data[0]
              require [94mt < munknown8b738e2fm.length
              mem[0] = 10
              require [94midx < m('cd', 4).length
              mem[132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              require ext_code.size(munknown8b738e2fm[[94mtm]m.field_0)
              static call munknown8b738e2fm[[94mtm]m.field_0.balanceOf(address owner) with:
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
              mcontinue 
          [94midx = [94midx + 1
          [94ms = [94ms + (3 * munknown8b738e2fm.length) + 2
          mcontinue 
      return ''
  require m('cd', 4).length
  require (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length) / m('cd', 4).length == (3 * munknown8b738e2fm.length) + 2
  if (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length):
      mem[128 len 32 * (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)] = code.data[14816 len 32 * (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m('cd', 4).lengthm:
      require ext_code.size(munknown2c8952eaAddress)
      static call munknown2c8952eaAddress.getAccountLiquidity(address account) with:
              gas gas_remaining wei
             args addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[(32 * (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)) + 128 len 96] = ext_call.return_data[0 len 96]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 96
      require [94ms < (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)
      mem[(32 * [94ms) + 128] = [94midx
      require [94ms + 1 < (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)
      mem[(32 * [94ms + 1) + 128] = ext_call.return_data[64]
      [94mt = 0
      [94mu = [94ms + 2
      mwhile [94mt < munknown8b738e2fm.lengthm:
          require [94mu < (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)
          mem[(32 * [94mu) + 128] = [94mt
          require [94mt < munknown8b738e2fm.length
          require [94midx < m('cd', 4).length
          require ext_code.size(munknown8b738e2fm[[94mtm]m.field_0)
          static call munknown8b738e2fm[[94mtm]m.field_0.0x95dd9193 with:
                  gas gas_remaining wei
                 args addr(cd[((32 * [94midx) + cd[4] + 36)])
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require [94mu + 1 < (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)
          mem[(32 * [94mu + 1) + 128] = ext_call.return_data[0]
          require [94mt < munknown8b738e2fm.length
          mem[0] = 10
          require [94midx < m('cd', 4).length
          mem[(32 * (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)) + 132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
          require ext_code.size(munknown8b738e2fm[[94mtm]m.field_0)
          static call munknown8b738e2fm[[94mtm]m.field_0.balanceOf(address owner) with:
                  gas gas_remaining wei
                 args addr(cd[((32 * [94midx) + cd[4] + 36)])
          mem[(32 * (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require [94mu + 2 < (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)
          mem[(32 * [94mu + 2) + 128] = ext_call.return_data[0]
          [94mt = [94mt + 1
          [94mu = [94mu + 3
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + (3 * munknown8b738e2fm.length) + 2
      mcontinue 
  mem[(32 * (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)) + 128] = 32
  mem[(32 * (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)) + 160] = (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)
  mem[(32 * (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)) + 192 len floor32((2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length))] = mem[128 len floor32((2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length))]
  return Array(len=(2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length), data=mem[(32 * (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)) + 192 len 32 * (2 * m('cd', 4).length) + (3 * munknown8b738e2fm.length * m('cd', 4).length)]), 


# hash = 0xe0bab4c4
# getter = ['storage', 160, 0, 8]
# const = None
# payable = True
def DAI() payable: 
  return mDAIAddress


# hash = 0xf14210a6
# getter = None
# const = None
# payable = True
def withdrawETH(uint256 m_amount) payable: 
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


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


