# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xC28E49C5253808A23e275Dd10a2581D55E0cbA98 
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
    unknown6bf2ca06
    # storage address 5
    ids
    # storage address 6
    stor6
    # storage address 7
    stor7 # mask: a s
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


# hash = 0x395389c7
# getter = None
# const = None
# payable = True
def unknown395389c7(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  [94midx = 0
  [94ms = 0
  [94mt = 0
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param2
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0x8da6bfe6 with:
              gas gas_remaining wei
             args m_param1, m_param2
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] <= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  return [94mt, addr([94ms)


# hash = 0x4189a68e
# getter = None
# const = None
# payable = True
def sell(uint256 m_amountOfTokens, address m_charity) payable: 
  require calldata.size - 4 >= 64
  [94midx = 0
  [94ms = 0
  [94mt = 0
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_amountOfTokens
      mem[132] = m_charity
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xeba1b60b with:
              gas gas_remaining wei
             args m_amountOfTokens, m_charity
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] <= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  require ext_code.size(addr([94ms))
  call addr([94ms).0xd04c6983 with:
       gas gas_remaining wei
      args m_amountOfTokens, [94mt, m_charity
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor7)
  call mstor7.0x9041a74e with:
       gas gas_remaining wei
      args 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0]


# hash = 0x59a87bc1
# getter = None
# const = None
# payable = True
def buy(uint256 m_stepSize, uint256 m_protectRatio, address m_recommendAddr) payable: 
  require calldata.size - 4 >= 96
  [94midx = 0
  [94ms = 0
  [94mt = -1
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_stepSize
      mem[132] = m_recommendAddr
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0x4d489323 with:
              gas gas_remaining wei
             args m_stepSize, m_recommendAddr
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] >= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  if [94mt > m_protectRatio:
      revert with 0, 'Sell is lower than required'
  require ext_code.size(addr([94ms))
  call addr([94ms).buy(uint256 stepSize, uint256 protectRatio, address recommendAddr) with:
       gas gas_remaining wei
      args m_stepSize, m_protectRatio, m_recommendAddr
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor7)
  call mstor7.0x9041a74e with:
       gas gas_remaining wei
      args 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0]


# hash = 0x6bf2ca06
# getter = ['storage', 160, 0, ['add', ['sha3', 4], ['cd', 4]]]
# const = None
# payable = True
def unknown6bf2ca06(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  require m_param1 < munknown6bf2ca06m.length
  return addr(munknown6bf2ca06m[m_param1m]m.field_0)


# hash = 0x766078ea
# getter = None
# const = None
# payable = True
def unknown766078ea(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  [94midx = 0
  [94ms = 0
  [94mt = -1
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param2
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0x5f8334fc with:
              gas gas_remaining wei
             args m_param1, m_param2
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] >= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  [94midx = 0
  [94mu = 0
  [94mv = 0
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param2
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0x8da6bfe6 with:
              gas gas_remaining wei
             args m_param1, m_param2
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] <= [94mv:
          [94midx = [94midx + 1
          [94mu = [94mu
          [94mv = [94mv
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94mu = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mv = ext_call.return_data[0]
      mcontinue 
  return [94mt, addr([94ms), [94mv, addr([94mu)


# hash = 0x7deb6025
# getter = None
# const = None
# payable = True
def buy(uint256 m_0xbtcAmount, address m_referredBy) payable: 
  require calldata.size - 4 >= 64
  [94midx = 0
  [94ms = 0
  [94mt = -1
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_0xbtcAmount
      mem[132] = m_referredBy
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0x4d489323 with:
              gas gas_remaining wei
             args m_0xbtcAmount, m_referredBy
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] >= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  require ext_code.size(addr([94ms))
  call addr([94ms).buy(uint256 stepSize, uint256 protectRatio, address recommendAddr) with:
       gas gas_remaining wei
      args m_0xbtcAmount, [94mt, m_referredBy
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor7)
  call mstor7.0x9041a74e with:
       gas gas_remaining wei
      args 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
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


# hash = 0x8945257c
# getter = None
# const = None
# payable = True
def unknown8945257c(uint256 m_param1, uint256 m_param2, addr m_param3, uint256 m_param4) payable: 
  require calldata.size - 4 >= 128
  require ext_code.size(midsm[m_param4m])
  call midsm[m_param4m].buy(uint256 stepSize, uint256 protectRatio, address recommendAddr) with:
       gas gas_remaining wei
      args m_param1, m_param2, m_param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor7)
  call mstor7.0x9041a74e with:
       gas gas_remaining wei
      args 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0]


# hash = 0x8a038a54
# getter = None
# const = None
# payable = True
def unknown8a038a54(uint256 m_param1, uint256 m_param2, addr m_param3, uint256 m_param4) payable: 
  require calldata.size - 4 >= 128
  require ext_code.size(midsm[m_param4m])
  call midsm[m_param4m].0xd04c6983 with:
       gas gas_remaining wei
      args m_param1, m_param2, m_param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor7)
  call mstor7.0x9041a74e with:
       gas gas_remaining wei
      args 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0]


# hash = 0x9134709e
# getter = None
# const = None
# payable = True
def unknown9134709e(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  [94midx = 0
  [94ms = 0
  [94mt = -1
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param2
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0x5f8334fc with:
              gas gas_remaining wei
             args m_param1, m_param2
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] >= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  require ext_code.size(addr([94ms))
  call addr([94ms).0x9134709e with:
       gas gas_remaining wei
      args m_param1, m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor7)
  call mstor7.0x9041a74e with:
       gas gas_remaining wei
      args 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return [94mt


# hash = 0x99a3c0f2
# getter = None
# const = None
# payable = True
def unknown99a3c0f2(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  [94midx = 0
  [94ms = 0
  [94mt = -1
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param2
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0x4d489323 with:
              gas gas_remaining wei
             args m_param1, m_param2
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] >= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  return [94mt, addr([94ms)


# hash = 0x9dff19bd
# getter = None
# const = None
# payable = True
def unknown9dff19bd() payable: 
  if not munknown6bf2ca06m.length:
      mem[(32 * munknown6bf2ca06m.length) + 128] = 32
      mem[(32 * munknown6bf2ca06m.length) + 160] = munknown6bf2ca06m.length
      mem[(32 * munknown6bf2ca06m.length) + 192 len floor32(munknown6bf2ca06m.length)] = mem[128 len floor32(munknown6bf2ca06m.length)]
      return memory
        from (32 * munknown6bf2ca06m.length) + 128
         [93mlen (96 * munknown6bf2ca06m.length) + 64
  mem[128] = addr(munknown6bf2ca06m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknown6bf2ca06m.length) + 96 > [94midxm:
      mem[[94midx + 32] = addr(munknown6bf2ca06m[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * munknown6bf2ca06m.length) + 192 len floor32(munknown6bf2ca06m.length)] = mem[128 len floor32(munknown6bf2ca06m.length)]
  return Array(len=munknown6bf2ca06m.length, data=mem[128 len floor32(munknown6bf2ca06m.length)], mem[(32 * munknown6bf2ca06m.length) + floor32(munknown6bf2ca06m.length) + 192 len (32 * munknown6bf2ca06m.length) - floor32(munknown6bf2ca06m.length)]), 


# hash = 0xaacfea3b
# getter = None
# const = None
# payable = True
def unknownaacfea3b(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  [94midx = 0
  [94ms = 0
  [94mt = -1
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param2
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0x4d489323 with:
              gas gas_remaining wei
             args m_param1, m_param2
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] >= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  [94midx = 0
  [94mu = 0
  [94mv = 0
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param2
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xeba1b60b with:
              gas gas_remaining wei
             args m_param1, m_param2
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] <= [94mv:
          [94midx = [94midx + 1
          [94mu = [94mu
          [94mv = [94mv
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94mu = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mv = ext_call.return_data[0]
      mcontinue 
  return [94mt, addr([94ms), [94mv, addr([94mu)


# hash = 0xad5c4648
# getter = None
# const = ['return', 1097077688018008265106216665536940668749033598146]
# payable = True
const WETH = 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2


# hash = 0xb4919226
# getter = None
# const = None
# payable = True
def unknownb4919226(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  [94midx = 0
  [94ms = 0
  [94mt = 0
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param2
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xeba1b60b with:
              gas gas_remaining wei
             args m_param1, m_param2
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] <= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  return [94mt, addr([94ms)


# hash = 0xb576a9ef
# getter = None
# const = None
# payable = True
def unknownb576a9ef(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mstor1 != caller:
      revert with 0, 'Must be the commander.'
  [94midx = 0
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      if addr(munknown6bf2ca06m[[94midxm]m.field_0) == midsm[m_param1m]:
          require munknown6bf2ca06m.length - 1 < munknown6bf2ca06m.length
          require [94midx < munknown6bf2ca06m.length
          addr(munknown6bf2ca06m[[94midxm]m.field_0) = addr(munknown6bf2ca06m[munknown6bf2ca06m.lengthm]m.field_0)
          require munknown6bf2ca06m.length - 1 < munknown6bf2ca06m.length
          addr(munknown6bf2ca06m[munknown6bf2ca06m.lengthm]m.field_0) = 0
          munknown6bf2ca06m.length--
          if munknown6bf2ca06m.length > munknown6bf2ca06m.length - 1:
              [94ms = sha3(4) + munknown6bf2ca06m.length - 1
              mwhile sha3(4) + munknown6bf2ca06m.length > [94msm:
                  mstor[[94msm] = 0
                  [94ms = [94ms + 1
                  mcontinue 
          mem[0] = m_param1
          mem[32] = 5
          midsm[m_param1m] = 0
          mem[96] = midsm[m_param1m]
          log 0x4aedad4e: ids[_param1]
      [94midx = [94midx + 1
      mcontinue 


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


# hash = 0xccc7b708
# getter = None
# const = None
# payable = True
def unknownccc7b708(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  [94midx = 0
  [94ms = 0
  [94mt = -1
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param2
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0x5f8334fc with:
              gas gas_remaining wei
             args m_param1, m_param2
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] >= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  return [94mt, addr([94ms)


# hash = 0xd04c6983
# getter = None
# const = None
# payable = True
def unknownd04c6983(uint256 m_param1, uint256 m_param2, addr m_param3) payable: 
  require calldata.size - 4 >= 96
  [94midx = 0
  [94ms = 0
  [94mt = 0
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param3
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xeba1b60b with:
              gas gas_remaining wei
             args m_param1, m_param3
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] <= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  if [94mt < m_param2:
      revert with 0, 'Buy is higher than required'
  require ext_code.size(addr([94ms))
  call addr([94ms).0xd04c6983 with:
       gas gas_remaining wei
      args m_param1, m_param2, m_param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor7)
  call mstor7.0x9041a74e with:
       gas gas_remaining wei
      args 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0]


# hash = 0xdd4549b7
# getter = None
# const = None
# payable = True
def unknowndd4549b7(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  [94midx = 0
  [94ms = 0
  [94mt = 0
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[100] = m_param1
      mem[132] = m_param2
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0x8da6bfe6 with:
              gas gas_remaining wei
             args m_param1, m_param2
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] <= [94mt:
          [94midx = [94midx + 1
          [94ms = [94ms
          [94mt = [94mt
          mcontinue 
      require [94midx < munknown6bf2ca06m.length
      mem[0] = 4
      [94midx = [94midx + 1
      [94ms = addr(munknown6bf2ca06m[[94midxm]m.field_0)
      [94mt = ext_call.return_data[0]
      mcontinue 
  require ext_code.size(addr([94ms))
  call addr([94ms).0xdd4549b7 with:
       gas gas_remaining wei
      args m_param1, m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor7)
  call mstor7.0x9041a74e with:
       gas gas_remaining wei
      args 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0]


# hash = 0xe456e0f6
# getter = None
# const = None
# payable = True
def unknowne456e0f6(array m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  if not m_param1.length:
      if not munknown6bf2ca06m.length:
          require munknown6bf2ca06m.length >= 0
          mem[96] = munknown6bf2ca06m.length
          mem[64] = (32 * munknown6bf2ca06m.length) + 128
          if not munknown6bf2ca06m.length:
              [94midx = 0
              mwhile [94midx < munknown6bf2ca06m.lengthm:
                  mem[0] = 4
                  mem[mem[64]] = 0xe456e0f600000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 36] = m_param2
                  mem[mem[64] + 4] = 64
                  mem[mem[64] + 68] = m_param1.length
                  mem[mem[64] + 100 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
                  mem[mem[64] + (32 * m_param1.length) + 100] = 0
                  require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
                  static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xe456e0f6 with:
                          gas gas_remaining wei
                         args Array(len=m_param1.length, data=call.data[m_param1 + 36 len floor32(m_param1.length)]), addr(m_param2)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94m_203 = mem[64]
                  mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                  mem[64] = mem[64] + ceil32(return_data.size)
                  require return_data.size >= 32
                  [94m_232 = mem[[94m_203]
                  require mem[[94m_203] <= 4294967296
                  require mem[[94m_203] + 32 <= return_data.size
                  require mem[mem[[94m_203] + [94m_203] <= 4294967296 and mem[[94m_203] + (32 * mem[mem[[94m_203] + [94m_203]) + 32 <= return_data.size
                  if mem[mem[[94m_203] + [94m_203]:
                      require [94midx < munknown6bf2ca06m.length
                      mem[0] = addr(munknown6bf2ca06m[[94midxm]m.field_0)
                      mem[32] = 6
                      require 0 < mem[96]
                      mem[128] = mstor6m[addr(mstor4m[[94midxm]m.field_0)m]
                      [94m_331 = mem[[94m_232 + [94m_203]
                      [94ms = 0
                      [94mt = 1
                      mwhile [94ms < [94m_331m:
                          require [94ms < mem[[94m_232 + [94m_203]
                          require [94mt < mem[96]
                          mem[(32 * [94mt) + 128] = mem[(32 * [94ms) + [94m_232 + [94m_203 + 32]
                          [94ms = [94ms + 1
                          [94mt = [94mt + 1
                          mcontinue 
                  [94midx = [94midx + 1
                  mcontinue 
              [94m_171 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_171 + 32] = block.number
              mem[[94m_171 + 64] = 64
              mem[[94m_171 + 96] = mem[[94m_171]
              mem[[94m_171 + 128 len floor32(mem[[94m_171])] = mem[[94m_171 + 32 len floor32(mem[[94m_171])]
              return block.number, 64, mem[[94m_171 + 96 len (32 * mem[[94m_171]) + 32]
          mem[128 len 32 * munknown6bf2ca06m.length] = code.data[14564 len 32 * munknown6bf2ca06m.length]
          [94midx = 0
          mwhile [94midx < munknown6bf2ca06m.lengthm:
              mem[0] = 4
              mem[mem[64]] = 0xe456e0f600000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 36] = m_param2
              mem[mem[64] + 4] = 64
              mem[mem[64] + 68] = m_param1.length
              mem[mem[64] + 100 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
              mem[mem[64] + (32 * m_param1.length) + 100] = 0
              require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
              static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xe456e0f6 with:
                      gas gas_remaining wei
                     args Array(len=m_param1.length, data=call.data[m_param1 + 36 len floor32(m_param1.length)]), addr(m_param2)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_204 = mem[64]
              mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >= 32
              [94m_236 = mem[[94m_204]
              require mem[[94m_204] <= 4294967296
              require mem[[94m_204] + 32 <= return_data.size
              require mem[mem[[94m_204] + [94m_204] <= 4294967296 and mem[[94m_204] + (32 * mem[mem[[94m_204] + [94m_204]) + 32 <= return_data.size
              if mem[mem[[94m_204] + [94m_204]:
                  require [94midx < munknown6bf2ca06m.length
                  mem[0] = addr(munknown6bf2ca06m[[94midxm]m.field_0)
                  mem[32] = 6
                  require 0 < mem[96]
                  mem[128] = mstor6m[addr(mstor4m[[94midxm]m.field_0)m]
                  [94m_332 = mem[[94m_236 + [94m_204]
                  [94ms = 0
                  [94mt = 1
                  mwhile [94ms < [94m_332m:
                      require [94ms < mem[[94m_236 + [94m_204]
                      require [94mt < mem[96]
                      mem[(32 * [94mt) + 128] = mem[(32 * [94ms) + [94m_236 + [94m_204 + 32]
                      [94ms = [94ms + 1
                      [94mt = [94mt + 1
                      mcontinue 
              [94midx = [94midx + 1
              mcontinue 
          [94m_172 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_172 + 32] = block.number
          mem[[94m_172 + 64] = 64
          mem[[94m_172 + 96] = mem[[94m_172]
          mem[[94m_172 + 128 len floor32(mem[[94m_172])] = mem[[94m_172 + 32 len floor32(mem[[94m_172])]
          return block.number, 64, mem[[94m_172 + 96 len (32 * mem[[94m_172]) + 32]
      require munknown6bf2ca06m.length
      require not 0 / munknown6bf2ca06m.length
      require munknown6bf2ca06m.length >= 0
      mem[96] = munknown6bf2ca06m.length
      mem[64] = (32 * munknown6bf2ca06m.length) + 128
      if not munknown6bf2ca06m.length:
          [94midx = 0
          mwhile [94midx < munknown6bf2ca06m.lengthm:
              mem[0] = 4
              mem[mem[64]] = 0xe456e0f600000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 36] = m_param2
              mem[mem[64] + 4] = 64
              mem[mem[64] + 68] = m_param1.length
              mem[mem[64] + 100 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
              mem[mem[64] + (32 * m_param1.length) + 100] = 0
              require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
              static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xe456e0f6 with:
                      gas gas_remaining wei
                     args Array(len=m_param1.length, data=call.data[m_param1 + 36 len floor32(m_param1.length)]), addr(m_param2)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_201 = mem[64]
              mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >= 32
              [94m_224 = mem[[94m_201]
              require mem[[94m_201] <= 4294967296
              require mem[[94m_201] + 32 <= return_data.size
              require mem[mem[[94m_201] + [94m_201] <= 4294967296 and mem[[94m_201] + (32 * mem[mem[[94m_201] + [94m_201]) + 32 <= return_data.size
              if mem[mem[[94m_201] + [94m_201]:
                  require [94midx < munknown6bf2ca06m.length
                  mem[0] = addr(munknown6bf2ca06m[[94midxm]m.field_0)
                  mem[32] = 6
                  require 0 < mem[96]
                  mem[128] = mstor6m[addr(mstor4m[[94midxm]m.field_0)m]
                  [94m_329 = mem[[94m_224 + [94m_201]
                  [94ms = 0
                  [94mt = 1
                  mwhile [94ms < [94m_329m:
                      require [94ms < mem[[94m_224 + [94m_201]
                      require [94mt < mem[96]
                      mem[(32 * [94mt) + 128] = mem[(32 * [94ms) + [94m_224 + [94m_201 + 32]
                      [94ms = [94ms + 1
                      [94mt = [94mt + 1
                      mcontinue 
              [94midx = [94midx + 1
              mcontinue 
          [94m_169 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_169 + 32] = block.number
          mem[[94m_169 + 64] = 64
          mem[[94m_169 + 96] = mem[[94m_169]
          mem[[94m_169 + 128 len floor32(mem[[94m_169])] = mem[[94m_169 + 32 len floor32(mem[[94m_169])]
          return block.number, 64, mem[[94m_169 + 96 len (32 * mem[[94m_169]) + 32]
      mem[128 len 32 * munknown6bf2ca06m.length] = code.data[14564 len 32 * munknown6bf2ca06m.length]
      [94midx = 0
      mwhile [94midx < munknown6bf2ca06m.lengthm:
          mem[0] = 4
          mem[mem[64]] = 0xe456e0f600000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 36] = m_param2
          mem[mem[64] + 4] = 64
          mem[mem[64] + 68] = m_param1.length
          mem[mem[64] + 100 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
          mem[mem[64] + (32 * m_param1.length) + 100] = 0
          require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
          static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xe456e0f6 with:
                  gas gas_remaining wei
                 args Array(len=m_param1.length, data=call.data[m_param1 + 36 len floor32(m_param1.length)]), addr(m_param2)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_202 = mem[64]
          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >= 32
          [94m_228 = mem[[94m_202]
          require mem[[94m_202] <= 4294967296
          require mem[[94m_202] + 32 <= return_data.size
          require mem[mem[[94m_202] + [94m_202] <= 4294967296 and mem[[94m_202] + (32 * mem[mem[[94m_202] + [94m_202]) + 32 <= return_data.size
          if mem[mem[[94m_202] + [94m_202]:
              require [94midx < munknown6bf2ca06m.length
              mem[0] = addr(munknown6bf2ca06m[[94midxm]m.field_0)
              mem[32] = 6
              require 0 < mem[96]
              mem[128] = mstor6m[addr(mstor4m[[94midxm]m.field_0)m]
              [94m_330 = mem[[94m_228 + [94m_202]
              [94ms = 0
              [94mt = 1
              mwhile [94ms < [94m_330m:
                  require [94ms < mem[[94m_228 + [94m_202]
                  require [94mt < mem[96]
                  mem[(32 * [94mt) + 128] = mem[(32 * [94ms) + [94m_228 + [94m_202 + 32]
                  [94ms = [94ms + 1
                  [94mt = [94mt + 1
                  mcontinue 
          [94midx = [94midx + 1
          mcontinue 
      [94m_170 = mem[64]
      mem[64] = mem[64] + 32
      mem[[94m_170 + 32] = block.number
      mem[[94m_170 + 64] = 64
      mem[[94m_170 + 96] = mem[[94m_170]
      mem[[94m_170 + 128 len floor32(mem[[94m_170])] = mem[[94m_170 + 32 len floor32(mem[[94m_170])]
      return block.number, 64, mem[[94m_170 + 96 len (32 * mem[[94m_170]) + 32]
  require m_param1.length
  require 3 * m_param1.length / m_param1.length == 3
  if not munknown6bf2ca06m.length:
      require munknown6bf2ca06m.length >= 0
      mem[96] = munknown6bf2ca06m.length
      mem[64] = (32 * munknown6bf2ca06m.length) + 128
      if not munknown6bf2ca06m.length:
          [94midx = 0
          mwhile [94midx < munknown6bf2ca06m.lengthm:
              mem[0] = 4
              mem[mem[64]] = 0xe456e0f600000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 36] = m_param2
              mem[mem[64] + 4] = 64
              mem[mem[64] + 68] = m_param1.length
              mem[mem[64] + 100 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
              mem[mem[64] + (32 * m_param1.length) + 100] = 0
              require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
              static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xe456e0f6 with:
                      gas gas_remaining wei
                     args Array(len=m_param1.length, data=call.data[m_param1 + 36 len floor32(m_param1.length)]), addr(m_param2)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              [94m_199 = mem[64]
              mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >= 32
              [94m_216 = mem[[94m_199]
              require mem[[94m_199] <= 4294967296
              require mem[[94m_199] + 32 <= return_data.size
              require mem[mem[[94m_199] + [94m_199] <= 4294967296 and mem[[94m_199] + (32 * mem[mem[[94m_199] + [94m_199]) + 32 <= return_data.size
              if mem[mem[[94m_199] + [94m_199]:
                  require [94midx < munknown6bf2ca06m.length
                  mem[0] = addr(munknown6bf2ca06m[[94midxm]m.field_0)
                  mem[32] = 6
                  require 0 < mem[96]
                  mem[128] = mstor6m[addr(mstor4m[[94midxm]m.field_0)m]
                  [94m_327 = mem[[94m_216 + [94m_199]
                  [94ms = 0
                  [94mt = 1
                  mwhile [94ms < [94m_327m:
                      require [94ms < mem[[94m_216 + [94m_199]
                      require [94mt < mem[96]
                      mem[(32 * [94mt) + 128] = mem[(32 * [94ms) + [94m_216 + [94m_199 + 32]
                      [94ms = [94ms + 1
                      [94mt = [94mt + 1
                      mcontinue 
              [94midx = [94midx + 1
              mcontinue 
          [94m_167 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_167 + 32] = block.number
          mem[[94m_167 + 64] = 64
          mem[[94m_167 + 96] = mem[[94m_167]
          mem[[94m_167 + 128 len floor32(mem[[94m_167])] = mem[[94m_167 + 32 len floor32(mem[[94m_167])]
          return block.number, 64, mem[[94m_167 + 96 len (32 * mem[[94m_167]) + 32]
      mem[128 len 32 * munknown6bf2ca06m.length] = code.data[14564 len 32 * munknown6bf2ca06m.length]
      [94midx = 0
      mwhile [94midx < munknown6bf2ca06m.lengthm:
          mem[0] = 4
          mem[mem[64]] = 0xe456e0f600000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 36] = m_param2
          mem[mem[64] + 4] = 64
          mem[mem[64] + 68] = m_param1.length
          mem[mem[64] + 100 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
          mem[mem[64] + (32 * m_param1.length) + 100] = 0
          require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
          static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xe456e0f6 with:
                  gas gas_remaining wei
                 args Array(len=m_param1.length, data=call.data[m_param1 + 36 len floor32(m_param1.length)]), addr(m_param2)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_200 = mem[64]
          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >= 32
          [94m_220 = mem[[94m_200]
          require mem[[94m_200] <= 4294967296
          require mem[[94m_200] + 32 <= return_data.size
          require mem[mem[[94m_200] + [94m_200] <= 4294967296 and mem[[94m_200] + (32 * mem[mem[[94m_200] + [94m_200]) + 32 <= return_data.size
          if mem[mem[[94m_200] + [94m_200]:
              require [94midx < munknown6bf2ca06m.length
              mem[0] = addr(munknown6bf2ca06m[[94midxm]m.field_0)
              mem[32] = 6
              require 0 < mem[96]
              mem[128] = mstor6m[addr(mstor4m[[94midxm]m.field_0)m]
              [94m_328 = mem[[94m_220 + [94m_200]
              [94ms = 0
              [94mt = 1
              mwhile [94ms < [94m_328m:
                  require [94ms < mem[[94m_220 + [94m_200]
                  require [94mt < mem[96]
                  mem[(32 * [94mt) + 128] = mem[(32 * [94ms) + [94m_220 + [94m_200 + 32]
                  [94ms = [94ms + 1
                  [94mt = [94mt + 1
                  mcontinue 
          [94midx = [94midx + 1
          mcontinue 
      [94m_168 = mem[64]
      mem[64] = mem[64] + 32
      mem[[94m_168 + 32] = block.number
      mem[[94m_168 + 64] = 64
      mem[[94m_168 + 96] = mem[[94m_168]
      mem[[94m_168 + 128 len floor32(mem[[94m_168])] = mem[[94m_168 + 32 len floor32(mem[[94m_168])]
      return block.number, 64, mem[[94m_168 + 96 len (32 * mem[[94m_168]) + 32]
  require munknown6bf2ca06m.length
  require 3 * munknown6bf2ca06m.length * m_param1.length / munknown6bf2ca06m.length == 3 * m_param1.length
  require (3 * munknown6bf2ca06m.length * m_param1.length) + munknown6bf2ca06m.length >= 3 * munknown6bf2ca06m.length * m_param1.length
  mem[96] = (3 * munknown6bf2ca06m.length * m_param1.length) + munknown6bf2ca06m.length
  mem[64] = (32 * (3 * munknown6bf2ca06m.length * m_param1.length) + munknown6bf2ca06m.length) + 128
  if not (3 * munknown6bf2ca06m.length * m_param1.length) + munknown6bf2ca06m.length:
      [94midx = 0
      mwhile [94midx < munknown6bf2ca06m.lengthm:
          mem[0] = 4
          mem[mem[64]] = 0xe456e0f600000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 36] = m_param2
          mem[mem[64] + 4] = 64
          mem[mem[64] + 68] = m_param1.length
          mem[mem[64] + 100 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
          mem[mem[64] + (32 * m_param1.length) + 100] = 0
          require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
          static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xe456e0f6 with:
                  gas gas_remaining wei
                 args Array(len=m_param1.length, data=call.data[m_param1 + 36 len floor32(m_param1.length)]), addr(m_param2)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          [94m_197 = mem[64]
          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = mem[64] + ceil32(return_data.size)
          require return_data.size >= 32
          [94m_208 = mem[[94m_197]
          require mem[[94m_197] <= 4294967296
          require mem[[94m_197] + 32 <= return_data.size
          require mem[mem[[94m_197] + [94m_197] <= 4294967296 and mem[[94m_197] + (32 * mem[mem[[94m_197] + [94m_197]) + 32 <= return_data.size
          if mem[mem[[94m_197] + [94m_197]:
              require [94midx < munknown6bf2ca06m.length
              mem[0] = addr(munknown6bf2ca06m[[94midxm]m.field_0)
              mem[32] = 6
              require 0 < mem[96]
              mem[128] = mstor6m[addr(mstor4m[[94midxm]m.field_0)m]
              [94m_325 = mem[[94m_208 + [94m_197]
              [94ms = 0
              [94mt = 1
              mwhile [94ms < [94m_325m:
                  require [94ms < mem[[94m_208 + [94m_197]
                  require [94mt < mem[96]
                  mem[(32 * [94mt) + 128] = mem[(32 * [94ms) + [94m_208 + [94m_197 + 32]
                  [94ms = [94ms + 1
                  [94mt = [94mt + 1
                  mcontinue 
          [94midx = [94midx + 1
          mcontinue 
      [94m_165 = mem[64]
      mem[64] = mem[64] + 32
      mem[[94m_165 + 32] = block.number
      mem[[94m_165 + 64] = 64
      mem[[94m_165 + 96] = mem[[94m_165]
      mem[[94m_165 + 128 len floor32(mem[[94m_165])] = mem[[94m_165 + 32 len floor32(mem[[94m_165])]
      return block.number, 64, mem[[94m_165 + 96 len (32 * mem[[94m_165]) + 32]
  mem[128 len 32 * (3 * munknown6bf2ca06m.length * m_param1.length) + munknown6bf2ca06m.length] = code.data[14564 len 32 * (3 * munknown6bf2ca06m.length * m_param1.length) + munknown6bf2ca06m.length]
  [94midx = 0
  mwhile [94midx < munknown6bf2ca06m.lengthm:
      mem[0] = 4
      mem[mem[64]] = 0xe456e0f600000000000000000000000000000000000000000000000000000000
      mem[mem[64] + 36] = m_param2
      mem[mem[64] + 4] = 64
      mem[mem[64] + 68] = m_param1.length
      mem[mem[64] + 100 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
      mem[mem[64] + (32 * m_param1.length) + 100] = 0
      require ext_code.size(addr(munknown6bf2ca06m[[94midxm]m.field_0))
      static call addr(munknown6bf2ca06m[[94midxm]m.field_0).0xe456e0f6 with:
              gas gas_remaining wei
             args Array(len=m_param1.length, data=call.data[m_param1 + 36 len floor32(m_param1.length)]), addr(m_param2)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94m_198 = mem[64]
      mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
      mem[64] = mem[64] + ceil32(return_data.size)
      require return_data.size >= 32
      [94m_212 = mem[[94m_198]
      require mem[[94m_198] <= 4294967296
      require mem[[94m_198] + 32 <= return_data.size
      require mem[mem[[94m_198] + [94m_198] <= 4294967296 and mem[[94m_198] + (32 * mem[mem[[94m_198] + [94m_198]) + 32 <= return_data.size
      if mem[mem[[94m_198] + [94m_198]:
          require [94midx < munknown6bf2ca06m.length
          mem[0] = addr(munknown6bf2ca06m[[94midxm]m.field_0)
          mem[32] = 6
          require 0 < mem[96]
          mem[128] = mstor6m[addr(mstor4m[[94midxm]m.field_0)m]
          [94m_326 = mem[[94m_212 + [94m_198]
          [94ms = 0
          [94mt = 1
          mwhile [94ms < [94m_326m:
              require [94ms < mem[[94m_212 + [94m_198]
              require [94mt < mem[96]
              mem[(32 * [94mt) + 128] = mem[(32 * [94ms) + [94m_212 + [94m_198 + 32]
              [94ms = [94ms + 1
              [94mt = [94mt + 1
              mcontinue 
      [94midx = [94midx + 1
      mcontinue 
  [94m_166 = mem[64]
  mem[64] = mem[64] + 32
  mem[[94m_166 + 32] = block.number
  mem[[94m_166 + 64] = 64
  mem[[94m_166 + 96] = mem[[94m_166]
  mem[[94m_166 + 128 len floor32(mem[[94m_166])] = mem[[94m_166 + 32 len floor32(mem[[94m_166])]
  return block.number, 64, mem[[94m_166 + 96 len (32 * mem[[94m_166]) + 32]


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


# hash = 0xf3984da4
# getter = None
# const = None
# payable = True
def unknownf3984da4(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  if mstor1 != caller:
      revert with 0, 'Must be the commander.'
  munknown6bf2ca06m.length++
  addr(munknown6bf2ca06m[munknown6bf2ca06m.lengthm]m.field_0) = m_param2
  midsm[m_param1m] = m_param2
  mstor6m[addr(m_param2)m] = m_param1
  log 0x774628d0: _param2


# hash = 0xf97cf9ed
# getter = None
# const = None
# payable = True
def unknownf97cf9ed(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if mstor1 != caller:
      revert with 0, 'Must be the commander.'
  mstor7 = m_param1
  log 0xdb67c1b8: _param1


# hash = 0xfac333ac
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 5]]]
# const = None
# payable = True
def ids(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return midsm[m_param1m]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


