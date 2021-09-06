# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x65Bb69FBFDcD46A99328ea752630a85CFf37Fe47 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown8870455fAddress # mask: a s
    # storage address 1
    tokenAddress # mask: a s
    # storage address 1
    initialized # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    vesting
    # storage address 3
    vestingsLengths
# hash = 0x0ca075d9
# getter = None
# const = None
# payable = False
def unknown0ca075d9(uint256 _param1, uint256 _param2): # not payable
  require ext_code.size(unknown8870455fAddress)
  static call unknown8870455fAddress.0x4c77e5ba with:
          gas gas_remaining wei
         args sha3('role.confirmed', _param1, _param2)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return addr(ext_call.return_data[0])


# hash = 0x0db3971b
# getter = None
# const = ['return', 50]
# payable = False
const MAX_VESTINGS_PER_ADDRESS = 50


# hash = 0x0f8f8b83
# getter = None
# const = None
# payable = True
def spendableBalanceOf(address _holder) payable: 
  mem[64] = 96
  require not call.value
  mem[32] = 3
  [94ms = 0
  [94midx = 0
  while [94midx < vestingsLengths[addr(_holder)]:
      mem[0] = [94midx
      mem[32] = sha3(addr(_holder), 2)
      if block.timestamp >= vesting[addr(_holder)][[94midx].field_384:
          [94m_133 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_133] = 17
          mem[[94m_133 + 32] = 'MATH_ADD_OVERFLOW'
          [94ms = sha3([94midx, sha3(addr(_holder), 2))
          [94midx = [94midx + 1
          continue 
      if block.timestamp < vesting[addr(_holder)][[94midx].field_320:
          [94m_136 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_136] = 17
          mem[[94m_136 + 32] = 'MATH_ADD_OVERFLOW'
          if vesting[addr(_holder)][[94midx].field_0 >= 0:
              [94ms = sha3([94midx, sha3(addr(_holder), 2))
              [94midx = [94midx + 1
              continue 
          mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = 32
          mem[mem[64] + 36] = 17
          mem[mem[64] + 68] = 'MATH_ADD_OVERFLOW'
          [94midx = 32
          while [94midx < 17:
              mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_136 + 32]
              [94midx = [94midx + 32
              continue 
      else:
          [94m_126 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_126] = 18
          mem[[94m_126 + 32] = 'MATH_SUB_UNDERFLOW'
          if vesting[addr(_holder)][[94midx].field_256 > vesting[addr(_holder)][[94midx].field_384:
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 18
              mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
              [94midx = 32
              while [94midx < 18:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_126 + 32]
                  [94midx = [94midx + 32
                  continue 
              revert with 0, 'MATH_SUB_UNDERFLOW'
          [94m_139 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_139] = 18
          mem[[94m_139 + 32] = 'MATH_SUB_UNDERFLOW'
          if vesting[addr(_holder)][[94midx].field_256 > block.timestamp:
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 18
              mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
              [94midx = 32
              while [94midx < 18:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_139 + 32]
                  [94midx = [94midx + 32
                  continue 
              revert with 0, 'MATH_SUB_UNDERFLOW'
          if not vesting[addr(_holder)][[94midx].field_0:
              require vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256
              [94m_183 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_183] = 18
              mem[[94m_183 + 32] = 'MATH_SUB_UNDERFLOW'
              if 0 / vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256 > vesting[addr(_holder)][[94midx].field_0:
                  mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 32
                  mem[mem[64] + 36] = 18
                  mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
                  [94midx = 32
                  while [94midx < 18:
                      mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_183 + 32]
                      [94midx = [94midx + 32
                      continue 
                  revert with 0, 'MATH_SUB_UNDERFLOW'
              [94m_204 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_204] = 17
              mem[[94m_204 + 32] = 'MATH_ADD_OVERFLOW'
              if vesting[addr(_holder)][[94midx].field_0 - (0 / vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256) >= 0:
                  [94ms = sha3([94midx, sha3(addr(_holder), 2))
                  [94midx = [94midx + 1
                  continue 
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 17
              mem[mem[64] + 68] = 'MATH_ADD_OVERFLOW'
              [94midx = 32
              while [94midx < 17:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_204 + 32]
                  [94midx = [94midx + 32
                  continue 
          else:
              [94m_172 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_172] = 17
              mem[[94m_172 + 32] = 'MATH_MUL_OVERFLOW'
              if (block.timestamp * vesting[addr(_holder)][[94midx].field_0) - (vesting[addr(_holder)][[94midx].field_256 * vesting[addr(_holder)][[94midx].field_0) / vesting[addr(_holder)][[94midx].field_0 != block.timestamp - vesting[addr(_holder)][[94midx].field_256:
                  mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 32
                  mem[mem[64] + 36] = 17
                  mem[mem[64] + 68] = 'MATH_MUL_OVERFLOW'
                  [94midx = 32
                  while [94midx < 17:
                      mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_172 + 32]
                      [94midx = [94midx + 32
                      continue 
                  revert with 0, 'MATH_MUL_OVERFLOW'
              require vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256
              [94m_189 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_189] = 18
              mem[[94m_189 + 32] = 'MATH_SUB_UNDERFLOW'
              if (block.timestamp * vesting[addr(_holder)][[94midx].field_0) - (vesting[addr(_holder)][[94midx].field_256 * vesting[addr(_holder)][[94midx].field_0) / vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256 > vesting[addr(_holder)][[94midx].field_0:
                  mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 32
                  mem[mem[64] + 36] = 18
                  mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
                  [94midx = 32
                  while [94midx < 18:
                      mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_189 + 32]
                      [94midx = [94midx + 32
                      continue 
                  revert with 0, 'MATH_SUB_UNDERFLOW'
              [94m_213 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_213] = 17
              mem[[94m_213 + 32] = 'MATH_ADD_OVERFLOW'
              if vesting[addr(_holder)][[94midx].field_0 - ((block.timestamp * vesting[addr(_holder)][[94midx].field_0) - (vesting[addr(_holder)][[94midx].field_256 * vesting[addr(_holder)][[94midx].field_0) / vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256) >= 0:
                  [94ms = sha3([94midx, sha3(addr(_holder), 2))
                  [94midx = [94midx + 1
                  continue 
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 17
              mem[mem[64] + 68] = 'MATH_ADD_OVERFLOW'
              [94midx = 32
              while [94midx < 17:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_213 + 32]
                  [94midx = [94midx + 32
                  continue 
      revert with 0, 'MATH_ADD_OVERFLOW'
  require ext_code.size(tokenAddress)
  static call tokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args addr(_holder)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 0 > ext_call.return_data[0]:
      revert with 0, 'MATH_SUB_UNDERFLOW'
  return ext_call.return_data[0]


# hash = 0x158ef93e
# getter = ['bool', ['storage', 8, 160, 1]]
# const = None
# payable = False
def initialized(): # not payable
  return bool(initialized)


# hash = 0x21cb18cd
# getter = None
# const = None
# payable = False
def assignVested(address _receiver, uint256 _amount, uint64 _start, uint64 _cliff, uint64 _vested, bool _revokable): # not payable
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require delegate.return_data[12 len 20] == caller
  if 50 <= vestingsLengths[addr(_receiver)]:
      revert with 0, 'TM_TOO_MANY_VESTINGS'
  if _start > _cliff:
      revert with 0, 'TM_WRONG_CLIFF_DATE'
  if _cliff > _vested:
      revert with 0, 'TM_WRONG_CLIFF_DATE'
  vestingsLengths[addr(_receiver)]++
  if not _amount:
      vesting[addr(_receiver)][stor3[addr(_receiver)]].field_0 = 0
      vesting[addr(_receiver)][stor3[addr(_receiver)]].field_256 = _start
      vesting[addr(_receiver)][stor3[addr(_receiver)]].field_320 = _cliff
      vesting[addr(_receiver)][stor3[addr(_receiver)]].field_384 = _vested
      vesting[addr(_receiver)][stor3[addr(_receiver)]].field_448 = uint64(_revokable)
      require ext_code.size(tokenAddress)
      call tokenAddress.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args this.address, addr(_receiver), 0
  else:
      if 10^18 * _amount / _amount != 10^18:
          revert with 0, 'MATH_MUL_OVERFLOW'
      vesting[addr(_receiver)][stor3[addr(_receiver)]].field_0 = 10^18 * _amount
      vesting[addr(_receiver)][stor3[addr(_receiver)]].field_256 = _start
      vesting[addr(_receiver)][stor3[addr(_receiver)]].field_320 = _cliff
      vesting[addr(_receiver)][stor3[addr(_receiver)]].field_384 = _vested
      vesting[addr(_receiver)][stor3[addr(_receiver)]].field_448 = uint64(_revokable)
      if not _amount:
          require ext_code.size(tokenAddress)
          call tokenAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, addr(_receiver), 0
      else:
          if 10^18 * _amount / _amount != 10^18:
              revert with 0, 'MATH_MUL_OVERFLOW'
          require ext_code.size(tokenAddress)
          call tokenAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args this.address, addr(_receiver), 10^18 * _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'TM_ASSIGN_TRANSFER_FROM_REVERTED'
  if not _amount:
      log NewVesting(
            address receiver=vestingsLengths[addr(_receiver)],
            uint256 vestingId=0,
            uint256 amount=_receiver)
  else:
      if 10^18 * _amount / _amount != 10^18:
          revert with 0, 'MATH_MUL_OVERFLOW'
      log NewVesting(
            address receiver=vestingsLengths[addr(_receiver)],
            uint256 vestingId=10^18 * _amount,
            uint256 amount=_receiver)
  return vestingsLengths[addr(_receiver)]


# hash = 0x383a18bc
# getter = None
# const = None
# payable = False
def unknown383a18bc(addr _param1, uint256 _param2): # not payable
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require delegate.return_data[12 len 20] == caller
  require ext_code.size(tokenAddress)
  call tokenAddress.0x383a18bc with:
       gas gas_remaining wei
      args addr(_param1), _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 0


# hash = 0x3e05a36d
# getter = ['struct', ['loc', 2]]
# const = None
# payable = False
def getVesting(address _recipient, uint256 _vestingId): # not payable
  if _vestingId >= vestingsLengths[addr(_recipient)]:
      revert with 0, 'TM_NO_VESTING'
  return vesting[addr(_recipient)][_vestingId].field_0, 
         vesting[addr(_recipient)][_vestingId].field_256,
         vesting[addr(_recipient)][_vestingId].field_256,
         vesting[addr(_recipient)][_vestingId].field_256,
         bool(vesting[addr(_recipient)][_vestingId].field_448)


# hash = 0x400ada75
# getter = None
# const = None
# payable = False
def unknown400ada75(addr _param1, bool _param2): # not payable
  require not initialized
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 'foundation', 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if delegate.return_data[12 len 20] != caller:
      require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
      [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
           gas gas_remaining wei
          args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if delegate.return_data[12 len 20] != caller:
          require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
          [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
               gas gas_remaining wei
              args unknown8870455fAddress, 'arbiter', 0x64616f0000000000000000000000000000000000000000000000000000000000
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if delegate.return_data[12 len 20] != caller:
              require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
              [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
                   gas gas_remaining wei
                  args unknown8870455fAddress, 0x64616f0000000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
              if not delegate.return_code:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if delegate.return_data[12 len 20] != caller:
                  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
                  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
                       gas gas_remaining wei
                      args unknown8870455fAddress, 'voting', 0x64616f0000000000000000000000000000000000000000000000000000000000
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require delegate.return_data[12 len 20] == caller
  require ext_code.size(_param1)
  static call _param1.controller() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if addr(ext_call.return_data[0]) != this.address:
      revert with 0, 'TM_TOKEN_CONTROLLER'
  tokenAddress = _param1
  stor1 = 0
  initialized = 1
  require ext_code.size(_param1)
  static call _param1.transfersEnabled() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if bool(ext_call.return_data[0]) != _param2:
      require ext_code.size(tokenAddress)
      call tokenAddress.enableTransfers(bool transfersEnabled) with:
           gas gas_remaining wei
          args _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32


# hash = 0x40c10f19
# getter = None
# const = None
# payable = False
def mint(address _to, uint256 _value): # not payable
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require delegate.return_data[12 len 20] == caller
  if not _value:
      require ext_code.size(tokenAddress)
      call tokenAddress.generateTokens(address holder, uint256 amount) with:
           gas gas_remaining wei
          args addr(_to), 0
  else:
      if 10^18 * _value / _value != 10^18:
          revert with 0, 'MATH_MUL_OVERFLOW'
      require ext_code.size(tokenAddress)
      call tokenAddress.generateTokens(address holder, uint256 amount) with:
           gas gas_remaining wei
          args addr(_to), 10^18 * _value
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0x4a393149
# getter = None
# const = None
# payable = False
def onTransfer(address _from, address _to, uint256 _amount): # not payable
  require initialized
  mem[64] = 160
  mem[96] = 24
  mem[128] = 'TM_TRANSFER_WRONG_SENDER'
  if tokenAddress != caller:
      revert with 0, 'TM_TRANSFER_WRONG_SENDER'
  if this.address == _from:
      return 1
  if this.address == _to:
      return 1
  mem[32] = 3
  [94ms = 0
  [94midx = 0
  while [94midx < vestingsLengths[addr(_from)]:
      mem[0] = [94midx
      mem[32] = sha3(addr(_from), 2)
      if block.timestamp >= vesting[addr(_from)][[94midx].field_384:
          [94m_155 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_155] = 17
          mem[[94m_155 + 32] = 'MATH_ADD_OVERFLOW'
          [94ms = sha3([94midx, sha3(addr(_from), 2))
          [94midx = [94midx + 1
          continue 
      if block.timestamp < vesting[addr(_from)][[94midx].field_320:
          [94m_158 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_158] = 17
          mem[[94m_158 + 32] = 'MATH_ADD_OVERFLOW'
          if vesting[addr(_from)][[94midx].field_0 >= 0:
              [94ms = sha3([94midx, sha3(addr(_from), 2))
              [94midx = [94midx + 1
              continue 
          mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = 32
          mem[mem[64] + 36] = 17
          mem[mem[64] + 68] = 'MATH_ADD_OVERFLOW'
          [94midx = 32
          while [94midx < 17:
              mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_158 + 32]
              [94midx = [94midx + 32
              continue 
      else:
          [94m_148 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_148] = 18
          mem[[94m_148 + 32] = 'MATH_SUB_UNDERFLOW'
          if vesting[addr(_from)][[94midx].field_256 > vesting[addr(_from)][[94midx].field_384:
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 18
              mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
              [94midx = 32
              while [94midx < 18:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_148 + 32]
                  [94midx = [94midx + 32
                  continue 
              revert with 0, 'MATH_SUB_UNDERFLOW'
          [94m_161 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_161] = 18
          mem[[94m_161 + 32] = 'MATH_SUB_UNDERFLOW'
          if vesting[addr(_from)][[94midx].field_256 > block.timestamp:
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 18
              mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
              [94midx = 32
              while [94midx < 18:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_161 + 32]
                  [94midx = [94midx + 32
                  continue 
              revert with 0, 'MATH_SUB_UNDERFLOW'
          if not vesting[addr(_from)][[94midx].field_0:
              require vesting[addr(_from)][[94midx].field_384 - vesting[addr(_from)][[94midx].field_256
              [94m_207 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_207] = 18
              mem[[94m_207 + 32] = 'MATH_SUB_UNDERFLOW'
              if 0 / vesting[addr(_from)][[94midx].field_384 - vesting[addr(_from)][[94midx].field_256 > vesting[addr(_from)][[94midx].field_0:
                  mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 32
                  mem[mem[64] + 36] = 18
                  mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
                  [94midx = 32
                  while [94midx < 18:
                      mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_207 + 32]
                      [94midx = [94midx + 32
                      continue 
                  revert with 0, 'MATH_SUB_UNDERFLOW'
              [94m_228 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_228] = 17
              mem[[94m_228 + 32] = 'MATH_ADD_OVERFLOW'
              if vesting[addr(_from)][[94midx].field_0 - (0 / vesting[addr(_from)][[94midx].field_384 - vesting[addr(_from)][[94midx].field_256) >= 0:
                  [94ms = sha3([94midx, sha3(addr(_from), 2))
                  [94midx = [94midx + 1
                  continue 
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 17
              mem[mem[64] + 68] = 'MATH_ADD_OVERFLOW'
              [94midx = 32
              while [94midx < 17:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_228 + 32]
                  [94midx = [94midx + 32
                  continue 
          else:
              [94m_196 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_196] = 17
              mem[[94m_196 + 32] = 'MATH_MUL_OVERFLOW'
              if (block.timestamp * vesting[addr(_from)][[94midx].field_0) - (vesting[addr(_from)][[94midx].field_256 * vesting[addr(_from)][[94midx].field_0) / vesting[addr(_from)][[94midx].field_0 != block.timestamp - vesting[addr(_from)][[94midx].field_256:
                  mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 32
                  mem[mem[64] + 36] = 17
                  mem[mem[64] + 68] = 'MATH_MUL_OVERFLOW'
                  [94midx = 32
                  while [94midx < 17:
                      mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_196 + 32]
                      [94midx = [94midx + 32
                      continue 
                  revert with 0, 'MATH_MUL_OVERFLOW'
              require vesting[addr(_from)][[94midx].field_384 - vesting[addr(_from)][[94midx].field_256
              [94m_213 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_213] = 18
              mem[[94m_213 + 32] = 'MATH_SUB_UNDERFLOW'
              if (block.timestamp * vesting[addr(_from)][[94midx].field_0) - (vesting[addr(_from)][[94midx].field_256 * vesting[addr(_from)][[94midx].field_0) / vesting[addr(_from)][[94midx].field_384 - vesting[addr(_from)][[94midx].field_256 > vesting[addr(_from)][[94midx].field_0:
                  mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 32
                  mem[mem[64] + 36] = 18
                  mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
                  [94midx = 32
                  while [94midx < 18:
                      mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_213 + 32]
                      [94midx = [94midx + 32
                      continue 
                  revert with 0, 'MATH_SUB_UNDERFLOW'
              [94m_237 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_237] = 17
              mem[[94m_237 + 32] = 'MATH_ADD_OVERFLOW'
              if vesting[addr(_from)][[94midx].field_0 - ((block.timestamp * vesting[addr(_from)][[94midx].field_0) - (vesting[addr(_from)][[94midx].field_256 * vesting[addr(_from)][[94midx].field_0) / vesting[addr(_from)][[94midx].field_384 - vesting[addr(_from)][[94midx].field_256) >= 0:
                  [94ms = sha3([94midx, sha3(addr(_from), 2))
                  [94midx = [94midx + 1
                  continue 
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 17
              mem[mem[64] + 68] = 'MATH_ADD_OVERFLOW'
              [94midx = 32
              while [94midx < 17:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_237 + 32]
                  [94midx = [94midx + 32
                  continue 
      revert with 0, 'MATH_ADD_OVERFLOW'
  require ext_code.size(tokenAddress)
  static call tokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args addr(_from)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 0 > ext_call.return_data[0]:
      revert with 0, 'MATH_SUB_UNDERFLOW'
  if ext_call.return_data[0] >= _amount:
      return 1
  return 0


# hash = 0x72f8393c
# getter = None
# const = None
# payable = True
def transferableBalance(address _holder, uint256 _time) payable: 
  mem[64] = 96
  require not call.value
  mem[32] = 3
  [94ms = 0
  [94midx = 0
  while [94midx < vestingsLengths[addr(_holder)]:
      mem[0] = [94midx
      mem[32] = sha3(addr(_holder), 2)
      if _time >= vesting[addr(_holder)][[94midx].field_384:
          [94m_133 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_133] = 17
          mem[[94m_133 + 32] = 'MATH_ADD_OVERFLOW'
          [94ms = sha3([94midx, sha3(addr(_holder), 2))
          [94midx = [94midx + 1
          continue 
      if _time < vesting[addr(_holder)][[94midx].field_320:
          [94m_136 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_136] = 17
          mem[[94m_136 + 32] = 'MATH_ADD_OVERFLOW'
          if vesting[addr(_holder)][[94midx].field_0 >= 0:
              [94ms = sha3([94midx, sha3(addr(_holder), 2))
              [94midx = [94midx + 1
              continue 
          mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = 32
          mem[mem[64] + 36] = 17
          mem[mem[64] + 68] = 'MATH_ADD_OVERFLOW'
          [94midx = 32
          while [94midx < 17:
              mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_136 + 32]
              [94midx = [94midx + 32
              continue 
      else:
          [94m_126 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_126] = 18
          mem[[94m_126 + 32] = 'MATH_SUB_UNDERFLOW'
          if vesting[addr(_holder)][[94midx].field_256 > vesting[addr(_holder)][[94midx].field_384:
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 18
              mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
              [94midx = 32
              while [94midx < 18:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_126 + 32]
                  [94midx = [94midx + 32
                  continue 
              revert with 0, 'MATH_SUB_UNDERFLOW'
          [94m_141 = mem[64]
          mem[64] = mem[64] + 64
          mem[[94m_141] = 18
          mem[[94m_141 + 32] = 'MATH_SUB_UNDERFLOW'
          if vesting[addr(_holder)][[94midx].field_256 > _time:
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 18
              mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
              [94midx = 32
              while [94midx < 18:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_141 + 32]
                  [94midx = [94midx + 32
                  continue 
              revert with 0, 'MATH_SUB_UNDERFLOW'
          if not vesting[addr(_holder)][[94midx].field_0:
              require vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256
              [94m_183 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_183] = 18
              mem[[94m_183 + 32] = 'MATH_SUB_UNDERFLOW'
              if 0 / vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256 > vesting[addr(_holder)][[94midx].field_0:
                  mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 32
                  mem[mem[64] + 36] = 18
                  mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
                  [94midx = 32
                  while [94midx < 18:
                      mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_183 + 32]
                      [94midx = [94midx + 32
                      continue 
                  revert with 0, 'MATH_SUB_UNDERFLOW'
              [94m_204 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_204] = 17
              mem[[94m_204 + 32] = 'MATH_ADD_OVERFLOW'
              if vesting[addr(_holder)][[94midx].field_0 - (0 / vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256) >= 0:
                  [94ms = sha3([94midx, sha3(addr(_holder), 2))
                  [94midx = [94midx + 1
                  continue 
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 17
              mem[mem[64] + 68] = 'MATH_ADD_OVERFLOW'
              [94midx = 32
              while [94midx < 17:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_204 + 32]
                  [94midx = [94midx + 32
                  continue 
          else:
              [94m_172 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_172] = 17
              mem[[94m_172 + 32] = 'MATH_MUL_OVERFLOW'
              if (_time * vesting[addr(_holder)][[94midx].field_0) - (vesting[addr(_holder)][[94midx].field_256 * vesting[addr(_holder)][[94midx].field_0) / vesting[addr(_holder)][[94midx].field_0 != _time - vesting[addr(_holder)][[94midx].field_256:
                  mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 32
                  mem[mem[64] + 36] = 17
                  mem[mem[64] + 68] = 'MATH_MUL_OVERFLOW'
                  [94midx = 32
                  while [94midx < 17:
                      mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_172 + 32]
                      [94midx = [94midx + 32
                      continue 
                  revert with 0, 'MATH_MUL_OVERFLOW'
              require vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256
              [94m_189 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_189] = 18
              mem[[94m_189 + 32] = 'MATH_SUB_UNDERFLOW'
              if (_time * vesting[addr(_holder)][[94midx].field_0) - (vesting[addr(_holder)][[94midx].field_256 * vesting[addr(_holder)][[94midx].field_0) / vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256 > vesting[addr(_holder)][[94midx].field_0:
                  mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 32
                  mem[mem[64] + 36] = 18
                  mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
                  [94midx = 32
                  while [94midx < 18:
                      mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_189 + 32]
                      [94midx = [94midx + 32
                      continue 
                  revert with 0, 'MATH_SUB_UNDERFLOW'
              [94m_213 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_213] = 17
              mem[[94m_213 + 32] = 'MATH_ADD_OVERFLOW'
              if vesting[addr(_holder)][[94midx].field_0 - ((_time * vesting[addr(_holder)][[94midx].field_0) - (vesting[addr(_holder)][[94midx].field_256 * vesting[addr(_holder)][[94midx].field_0) / vesting[addr(_holder)][[94midx].field_384 - vesting[addr(_holder)][[94midx].field_256) >= 0:
                  [94ms = sha3([94midx, sha3(addr(_holder), 2))
                  [94midx = [94midx + 1
                  continue 
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 17
              mem[mem[64] + 68] = 'MATH_ADD_OVERFLOW'
              [94midx = 32
              while [94midx < 17:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_213 + 32]
                  [94midx = [94midx + 32
                  continue 
      revert with 0, 'MATH_ADD_OVERFLOW'
  require ext_code.size(tokenAddress)
  static call tokenAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args addr(_holder)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 0 > ext_call.return_data[0]:
      revert with 0, 'MATH_SUB_UNDERFLOW'
  return ext_call.return_data[0]


# hash = 0x748f6184
# getter = None
# const = None
# payable = False
def unknown748f6184(addr _param1, uint256 _param2): # not payable
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require delegate.return_data[12 len 20] == caller
  require ext_code.size(tokenAddress)
  call tokenAddress.0x748f6184 with:
       gas gas_remaining wei
      args addr(_param1), _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x7e7db6e1
# getter = None
# const = None
# payable = False
def allowRecoverability(address _param1): # not payable
  return _param1 != tokenAddress


# hash = 0x8870455f
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def unknown8870455f(): # not payable
  return unknown8870455fAddress


# hash = 0x94b2b680
# getter = None
# const = None
# payable = False
def unknown94b2b680(addr _param1, uint256 _param2): # not payable
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 'foundation', 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if delegate.return_data[12 len 20] != caller:
      require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
      [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
           gas gas_remaining wei
          args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if delegate.return_data[12 len 20] != caller:
          require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
          [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
               gas gas_remaining wei
              args unknown8870455fAddress, 'arbiter', 0x64616f0000000000000000000000000000000000000000000000000000000000
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if delegate.return_data[12 len 20] != caller:
              require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
              [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
                   gas gas_remaining wei
                  args unknown8870455fAddress, 0x64616f0000000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
              if not delegate.return_code:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if delegate.return_data[12 len 20] != caller:
                  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
                  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
                       gas gas_remaining wei
                      args unknown8870455fAddress, 'voting', 0x64616f0000000000000000000000000000000000000000000000000000000000
                  if not delegate.return_code:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require delegate.return_data[12 len 20] == caller
  require ext_code.size(unknown8870455fAddress)
  static call unknown8870455fAddress.0x4c77e5ba with:
          gas gas_remaining wei
         args sha3('role.confirmed', 'foundation', _param2)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not _param1:
      call addr(ext_call.return_data[0]) with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  else:
      require ext_code.size(tokenAddress)
      static call tokenAddress.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(_param1)
      call _param1.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      log 0xf71e34a2: ext_call.return_data[0], _param1, addr(ext_call.return_data[0])


# hash = 0x97f2562a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 3]]]
# const = None
# payable = False
def vestingsLengths(address _param1): # not payable
  return vestingsLengths[_param1]


# hash = 0xbe760488
# getter = None
# const = None
# payable = False
def assign(address _receiver, uint256 _amount): # not payable
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require delegate.return_data[12 len 20] == caller
  if not _amount:
      require ext_code.size(tokenAddress)
      call tokenAddress.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args this.address, addr(_receiver), 0
  else:
      if 10^18 * _amount / _amount != 10^18:
          revert with 0, 'MATH_MUL_OVERFLOW'
      require ext_code.size(tokenAddress)
      call tokenAddress.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args this.address, addr(_receiver), 10^18 * _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'TM_ASSIGN_TRANSFER_FROM_REVERTED'


# hash = 0xcc872b66
# getter = None
# const = None
# payable = False
def issue(uint256 _amount): # not payable
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require delegate.return_data[12 len 20] == caller
  if not _amount:
      require ext_code.size(tokenAddress)
      call tokenAddress.generateTokens(address holder, uint256 amount) with:
           gas gas_remaining wei
          args addr(this.address), 0
  else:
      if 10^18 * _amount / _amount != 10^18:
          revert with 0, 'MATH_MUL_OVERFLOW'
      require ext_code.size(tokenAddress)
      call tokenAddress.generateTokens(address holder, uint256 amount) with:
           gas gas_remaining wei
          args addr(this.address), 10^18 * _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0xda682aeb
# getter = None
# const = ['return', 1]
# payable = False
const onApprove(address _param1, address _param2, uint256 _param3) = 1


# hash = 0xdf8de3e7
# getter = None
# const = None
# payable = False
def claimTokens(address _token): # not payable
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require delegate.return_data[12 len 20] == caller
  require ext_code.size(tokenAddress)
  call tokenAddress.claimTokens(address token) with:
       gas gas_remaining wei
      args _token
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xf41e60c5
# getter = None
# const = None
# payable = False
def enableTransfers(bool _transfersEnabled): # not payable
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require delegate.return_data[12 len 20] == caller
  require ext_code.size(tokenAddress)
  call tokenAddress.enableTransfers(bool transfersEnabled) with:
       gas gas_remaining wei
      args _transfersEnabled
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 0


# hash = 0xf48c3054
# getter = None
# const = None
# payable = True
def proxyPayment(address _param1) payable: 
  if tokenAddress != caller:
      revert with 0, 'TM_PROXY_PAYMENT_WRONG_SENDER'
  return 1


# hash = 0xfa6799f2
# getter = None
# const = None
# payable = False
def revokeVesting(address _holder, uint256 _vestingId): # not payable
  require ext_code.size(0x99b21e8ba841a3a0325a151bea4e435efed99991)
  [93mdelegate 0x99b21e8ba841a3a0325a151bea4e435efed99991.0xc2c15528 with:
       gas gas_remaining wei
      args unknown8870455fAddress, 0x61646d696e000000000000000000000000000000000000000000000000000000, 0x64616f0000000000000000000000000000000000000000000000000000000000
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require delegate.return_data[12 len 20] == caller
  if _vestingId >= vestingsLengths[addr(_holder)]:
      revert with 0, 'TM_NO_VESTING'
  if not vesting[addr(_holder)][_vestingId].field_448:
      revert with 0, 'TM_VESTING_NOT_REVOKABLE'
  if block.timestamp >= vesting[addr(_holder)][_vestingId].field_384:
      vesting[addr(_holder)][_vestingId].field_0 = 0
      vesting[addr(_holder)][_vestingId].field_256 = 0
      require ext_code.size(tokenAddress)
      call tokenAddress.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args addr(_holder), this.address, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          revert with 0, 'TM_REVOKE_TRANSFER_FROM_REVERTED'
      log VestingRevoked(
            address revokedAddress=_vestingId,
            uint256 amountWithdrawn=0,
            uint256 amountRefunded=_holder)
  else:
      if block.timestamp < vesting[addr(_holder)][_vestingId].field_320:
          vesting[addr(_holder)][_vestingId].field_0 = 0
          vesting[addr(_holder)][_vestingId].field_256 = 0
          require ext_code.size(tokenAddress)
          call tokenAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args addr(_holder), this.address, vesting[addr(_holder)][_vestingId].field_0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'TM_REVOKE_TRANSFER_FROM_REVERTED'
          log VestingRevoked(
                address revokedAddress=_vestingId,
                uint256 amountWithdrawn=vesting[addr(_holder)][_vestingId].field_0,
                uint256 amountRefunded=_holder)
      else:
          if vesting[addr(_holder)][_vestingId].field_256 > vesting[addr(_holder)][_vestingId].field_384:
              revert with 0, 'MATH_SUB_UNDERFLOW'
          if vesting[addr(_holder)][_vestingId].field_256 > block.timestamp:
              revert with 0, 'MATH_SUB_UNDERFLOW'
          if not vesting[addr(_holder)][_vestingId].field_0:
              require vesting[addr(_holder)][_vestingId].field_384 - vesting[addr(_holder)][_vestingId].field_256
              if 0 / vesting[addr(_holder)][_vestingId].field_384 - vesting[addr(_holder)][_vestingId].field_256 > vesting[addr(_holder)][_vestingId].field_0:
                  revert with 0, 'MATH_SUB_UNDERFLOW'
              vesting[addr(_holder)][_vestingId].field_0 = 0
              vesting[addr(_holder)][_vestingId].field_256 = 0
              require ext_code.size(tokenAddress)
              call tokenAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(_holder), this.address, vesting[addr(_holder)][_vestingId].field_0 - (0 / vesting[addr(_holder)][_vestingId].field_384 - vesting[addr(_holder)][_vestingId].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'TM_REVOKE_TRANSFER_FROM_REVERTED'
              log VestingRevoked(
                    address revokedAddress=_vestingId,
                    uint256 amountWithdrawn=vesting[addr(_holder)][_vestingId].field_0 - (0 / vesting[addr(_holder)][_vestingId].field_384 - vesting[addr(_holder)][_vestingId].field_256),
                    uint256 amountRefunded=_holder)
          else:
              if (block.timestamp * vesting[addr(_holder)][_vestingId].field_0) - (vesting[addr(_holder)][_vestingId].field_256 * vesting[addr(_holder)][_vestingId].field_0) / vesting[addr(_holder)][_vestingId].field_0 != block.timestamp - vesting[addr(_holder)][_vestingId].field_256:
                  revert with 0, 'MATH_MUL_OVERFLOW'
              require vesting[addr(_holder)][_vestingId].field_384 - vesting[addr(_holder)][_vestingId].field_256
              if (block.timestamp * vesting[addr(_holder)][_vestingId].field_0) - (vesting[addr(_holder)][_vestingId].field_256 * vesting[addr(_holder)][_vestingId].field_0) / vesting[addr(_holder)][_vestingId].field_384 - vesting[addr(_holder)][_vestingId].field_256 > vesting[addr(_holder)][_vestingId].field_0:
                  revert with 0, 'MATH_SUB_UNDERFLOW'
              vesting[addr(_holder)][_vestingId].field_0 = 0
              vesting[addr(_holder)][_vestingId].field_256 = 0
              require ext_code.size(tokenAddress)
              call tokenAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(_holder), this.address, vesting[addr(_holder)][_vestingId].field_0 - ((block.timestamp * vesting[addr(_holder)][_vestingId].field_0) - (vesting[addr(_holder)][_vestingId].field_256 * vesting[addr(_holder)][_vestingId].field_0) / vesting[addr(_holder)][_vestingId].field_384 - vesting[addr(_holder)][_vestingId].field_256)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'TM_REVOKE_TRANSFER_FROM_REVERTED'
              log VestingRevoked(
                    address revokedAddress=_vestingId,
                    uint256 amountWithdrawn=vesting[addr(_holder)][_vestingId].field_0 - ((block.timestamp * vesting[addr(_holder)][_vestingId].field_0) - (vesting[addr(_holder)][_vestingId].field_256 * vesting[addr(_holder)][_vestingId].field_0) / vesting[addr(_holder)][_vestingId].field_384 - vesting[addr(_holder)][_vestingId].field_256),
                    uint256 amountRefunded=_holder)


# hash = 0xfc0c546a
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def token(): # not payable
  return tokenAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


