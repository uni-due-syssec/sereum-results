# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x69AE9f5500e749eaa8D243685d91858C5A3B537b 
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


# hash = 0x4d489323
# getter = None
# const = None
# payable = True
def unknown4d489323(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  if m_param2 != 0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359:
      return -1
  require ext_code.size(mstor4)
  static call mstor4.getPayAmount(address pay_gem, address buy_gem, uint256 buy_amt) with:
          gas gas_remaining wei
         args addr(m_param2), 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x59a87bc1
# getter = None
# const = None
# payable = True
def buy(uint256 m_stepSize, uint256 m_protectRatio, address m_recommendAddr) payable: 
  require calldata.size - 4 >= 96
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
  require ext_code.size(m_recommendAddr)
  static call m_recommendAddr.balanceOf(address owner) with:
          gas gas_remaining wei
         args mstor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < m_protectRatio:
      revert with 0, 'Not enough ERC20 funds'
  require ext_code.size(m_recommendAddr)
  call m_recommendAddr.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args mstor2, addr(this.address), m_protectRatio
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4)
  call mstor4.buyAllAmount(address buy_gem, uint256 buy_amt, address pay_gem, uint256 max_fill_amount) with:
       gas gas_remaining wei
      args 0, 1014328514, m_stepSize, addr(m_recommendAddr), m_protectRatio
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  Mask(200, 0, m_protectRatio)
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  Mask(200, 0, m_protectRatio)
  require ext_code.size(m_recommendAddr)
  static call m_recommendAddr.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > 0:
      require ext_code.size(m_recommendAddr)
      static call m_recommendAddr.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(m_recommendAddr)
      call m_recommendAddr.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args mstor2, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  Mask(200, 0, m_protectRatio)
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  Mask(200, 0, m_protectRatio)
  require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
  static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > 0:
      require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
      static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
      call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args mstor2, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  log 0xbc43d7c0: _stepSize, ext_call.return_data[0], 2
  return ext_call.return_data[0]


# hash = 0x5f8334fc
# getter = None
# const = None
# payable = True
def unknown5f8334fc(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  if m_param2 != 0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359:
      return -1
  require ext_code.size(mstor4)
  static call mstor4.getPayAmount(address pay_gem, address buy_gem, uint256 buy_amt) with:
          gas gas_remaining wei
         args 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, addr(m_param2), m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


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


# hash = 0x8da6bfe6
# getter = None
# const = None
# payable = True
def unknown8da6bfe6(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  if m_param2 != 0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359:
      return 0
  require ext_code.size(mstor4)
  static call mstor4.getBuyAmount(address buy_gem, address pay_gem, uint256 pay_amt) with:
          gas gas_remaining wei
         args 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, addr(m_param2), m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x9134709e
# getter = None
# const = None
# payable = True
def unknown9134709e(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(mstor4)
  static call mstor4.getPayAmount(address pay_gem, address buy_gem, uint256 buy_amt) with:
          gas gas_remaining wei
         args 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, addr(m_param2), m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
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
  if ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 'Not enough ERC20 funds'
  require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
  call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args mstor2, addr(this.address), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4)
  call mstor4.buyAllAmount(address buy_gem, uint256 buy_amt, address pay_gem, uint256 max_fill_amount) with:
       gas gas_remaining wei
      args 0, 0, m_param1, 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  ext_call.return_data[7 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  ext_call.return_data[7 len 25]
  require ext_code.size(m_param2)
  static call m_param2.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > 0:
      require ext_code.size(m_param2)
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
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  ext_call.return_data[7 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  ext_call.return_data[7 len 25]
  require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
  static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > 0:
      require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
      static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
      call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args mstor2, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  log 0xbc43d7c0: ext_call.return_data[0], _param1, 1
  return ext_call.return_data[0]


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


# hash = 0xd04c6983
# getter = None
# const = None
# payable = True
def unknownd04c6983(uint256 m_param1, uint256 m_param2, addr m_param3) payable: 
  require calldata.size - 4 >= 96
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
      revert with 0, 'Not enough ERC20 funds'
  require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
  call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args mstor2, addr(this.address), m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4)
  call mstor4.sellAllAmount(address pay_gem, uint256 pay_amt, address buy_gem, uint256 min_fill_amount) with:
       gas gas_remaining wei
      args 0, 1014328514, m_param1, addr(m_param3), m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  Mask(200, 0, m_param2)
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  Mask(200, 0, m_param2)
  require ext_code.size(m_param3)
  static call m_param3.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > 0:
      require ext_code.size(m_param3)
      static call m_param3.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(m_param3)
      call m_param3.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args mstor2, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  log 0xbc43d7c0: _param1, ext_call.return_data[0], 2
  return ext_call.return_data[0]


# hash = 0xdaea85c5
# getter = None
# const = None
# payable = True
def approve(address m_token) payable: 
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
  require ext_code.size(m_token)
  static call m_token.allowance(address owner, address spender) with:
          gas gas_remaining wei
         args addr(this.address), mstor4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < -1:
      require ext_code.size(m_token)
      call m_token.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args mstor4, -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


# hash = 0xdd4549b7
# getter = None
# const = None
# payable = True
def unknowndd4549b7(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  require ext_code.size(mstor4)
  static call mstor4.getBuyAmount(address buy_gem, address pay_gem, uint256 pay_amt) with:
          gas gas_remaining wei
         args 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, addr(m_param2), m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
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
         args mstor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < m_param1:
      revert with 0, 'Not enough ERC20 funds'
  require ext_code.size(m_param2)
  call m_param2.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args mstor2, addr(this.address), m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4)
  call mstor4.sellAllAmount(address pay_gem, uint256 pay_amt, address buy_gem, uint256 min_fill_amount) with:
       gas gas_remaining wei
      args 0, 0, m_param1, 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  ext_call.return_data[7 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  ext_call.return_data[7 len 25]
  require ext_code.size(m_param2)
  static call m_param2.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > 0:
      require ext_code.size(m_param2)
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
  if mstor0m[tx.originm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  ext_call.return_data[7 len 25]
  if mstor0m[callerm] != 1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  39,
                  0xfe4f726967696e20616e642073656e646572206d757374206265206120626162796c6f6e69616e,
                  ext_call.return_data[7 len 25]
  require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
  static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > 0:
      require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
      static call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
      call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args mstor2, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  log 0xbc43d7c0: ext_call.return_data[0], _param1, 1
  return ext_call.return_data[0]


# hash = 0xe456e0f6
# getter = None
# const = None
# payable = True
def unknowne456e0f6() payable: 
  require calldata.size - 4 >= 64
  require cd[4] <= 4294967296
  require cd[4] + 36 <= calldata.size
  require m('cd', 4).length <= 4294967296 and cd[4] + (32 * m('cd', 4).length) + 36 <= calldata.size
  if addr(cd[36]) != 0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359:
      return ''
  if 3 * m('cd', 4).length:
      mem[128 len 32 * 3 * m('cd', 4).length] = code.data[12632 len 32 * 3 * m('cd', 4).length]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m('cd', 4).lengthm:
      require [94ms < 3 * m('cd', 4).length
      mem[(32 * [94ms) + 128] = cd[((32 * [94midx) + cd[4] + 36)]
      require [94midx < m('cd', 4).length
      require ext_code.size(mstor4)
      static call mstor4.getPayAmount(address pay_gem, address buy_gem, uint256 buy_amt) with:
              gas gas_remaining wei
             args addr(cd[36]), 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, cd[((32 * [94midx) + cd[4] + 36)]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require [94ms + 1 < 3 * m('cd', 4).length
      mem[(32 * [94ms + 1) + 128] = ext_call.return_data[0]
      require [94midx < m('cd', 4).length
      mem[(32 * 3 * m('cd', 4).length) + 132] = addr(cd[36])
      mem[(32 * 3 * m('cd', 4).length) + 164] = 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
      mem[(32 * 3 * m('cd', 4).length) + 196] = cd[((32 * [94midx) + cd[4] + 36)]
      require ext_code.size(mstor4)
      static call mstor4.getBuyAmount(address buy_gem, address pay_gem, uint256 pay_amt) with:
              gas gas_remaining wei
             args addr(cd[36]), 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, cd[((32 * [94midx) + cd[4] + 36)]
      mem[(32 * 3 * m('cd', 4).length) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require [94ms + 2 < 3 * m('cd', 4).length
      mem[(32 * [94ms + 2) + 128] = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94ms = [94ms + 3
      mcontinue 
  mem[(32 * 3 * m('cd', 4).length) + 192 len floor32(3 * m('cd', 4).length)] = mem[128 len floor32(3 * m('cd', 4).length)]
  return Array(len=3 * m('cd', 4).length, data=mem[128 len floor32(3 * m('cd', 4).length)], mem[(32 * 3 * m('cd', 4).length) + floor32(3 * m('cd', 4).length) + 192 len (32 * 3 * m('cd', 4).length) - floor32(3 * m('cd', 4).length)]), 


# hash = 0xeba1b60b
# getter = None
# const = None
# payable = True
def unknowneba1b60b(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  if m_param2 != 0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359:
      return 0
  require ext_code.size(mstor4)
  static call mstor4.getBuyAmount(address buy_gem, address pay_gem, uint256 pay_amt) with:
          gas gas_remaining wei
         args addr(m_param2), 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


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


