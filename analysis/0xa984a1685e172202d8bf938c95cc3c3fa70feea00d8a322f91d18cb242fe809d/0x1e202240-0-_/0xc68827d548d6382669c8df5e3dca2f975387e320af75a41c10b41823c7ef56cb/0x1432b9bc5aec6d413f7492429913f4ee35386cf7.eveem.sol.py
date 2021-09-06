# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x1432B9bC5aec6D413F7492429913F4Ee35386CF7 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x00432cf3': 'getCurrentMarginAmount(address _loanTokenAddress, address _positionTokenAddress, address _collateralTokenAddress, uint256 _loanTokenAmount, uint256 _positionTokenAmount, uint256 _collateralTokenAmount)', '0x016d7c64': 'unknown016d7c64(?)', '0x051c8a8d': 'unknown051c8a8d(?)', '0x06599aa0': 'unknown06599aa0(?)', '0x369308ce': 'unknown369308ce(?)', '0x4849b6c8': 'unknown4849b6c8(?)', '0x5e3f4b3c': 'unknown5e3f4b3c(?)', '0x89611678': 'unknown89611678(?)', '0xc3feec61': 'unknownc3feec61(?)', '0xff8a2640': 'unknownff8a2640(?)'} 

# storage definitions
def storage:
    # storage address 0
    emaValue # mask: a s
    # storage address 1
    emaPeriods # mask: a s
    # storage address 2
    unknown903509d6 # mask: a s
    # storage address 3
    unknown7ca7cbc1 # mask: a s
    # storage address 4
    owner # mask: a s
    # storage address 4
    throwOnGasRefundFail # mask: a s
    # storage address 5
    bZxContractAddress # mask: a s
    # storage address 7
    stor7
    # storage address 8
    decimals
    # storage address 9
    unknown032b04b1
    # storage address 10
    unknown4eb60611 # mask: a s
    # storage address 11
    unknownf0ad0b7f # mask: a s
    # storage address 12
    interestFeePercent # mask: a s
    # storage address 13
    unknown783882be # mask: a s
    # storage address 14
    unknowncc11a3b6 # mask: a s
    # storage address 15
    minInitialMarginAmount # mask: a s
    # storage address 16
    minMaintenanceMarginAmount # mask: a s
    # storage address 17
    unknown38a56582 # mask: a s
    # storage address 17
    stor17 # mask: a s
    # storage address 17
    stor17 # mask: a s
    # storage address 17
    unknown035ab37f # mask: a s
    # storage address 18
    unknown787f7fca # mask: a s
    # storage address 19
    unknown938dd426 # mask: a s
    # storage address 20
    stor20 # mask: a s
    # storage address 20
    feeWalletAddress # mask: a s
    # storage address 21
    vaultContractAddress # mask: a s
    # storage address 22
    kyberContractAddress # mask: a s
    # storage address 23
    kyberNetworkContractAddress # mask: a s
    # storage address 24
    stor24 # mask: a s
    # storage address 24
    stor24 # mask: a s
    # storage address 24
    wethContractAddress # mask: a s
    # storage address 25
    bZRxTokenContractAddress # mask: a s
    # storage address 26
    unknownf0ef5e0dAddress # mask: a s
    # storage address 27
    unknownfbb7f232
# hash = 0x032b04b1
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = False
def unknown032b04b1(addr _param1): # not payable
  require calldata.size - 4 >=′ 32
  return unknown032b04b1[_param1]


# hash = 0x035ab37f
# getter = ['bool', ['storage', 8, 0, 17]]
# const = None
# payable = False
def unknown035ab37f(): # not payable
  return bool(unknown035ab37f)


# hash = 0x05b1137b
# getter = None
# const = None
# payable = False
def transferEther(address _to, uint256 _value): # not payable
  require calldata.size - 4 >=′ 64
  require caller == owner
  if _value <= eth.balance(this.address):
      call _to with:
         value _value wei
           gas 2300 * is_zero(value) wei
  else:
      call _to with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
  return bool(ext_call.success)


# hash = 0x2274346b
# getter = ['storage', 160, 0, 21]
# const = None
# payable = False
def vaultContract(): # not payable
  return vaultContractAddress


# hash = 0x26e010c8
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def minInitialMarginAmount(): # not payable
  return minInitialMarginAmount


# hash = 0x2aed1390
# getter = ['storage', 160, 0, 22]
# const = None
# payable = False
def kyberContract(): # not payable
  return kyberContractAddress


# hash = 0x2c9f6792
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def emaPeriods(): # not payable
  return emaPeriods


# hash = 0x34752a34
# getter = None
# const = None
# payable = False
def unknown34752a34(): # not payable
  require calldata.size - 4 >=′ 448
  require calldata.size - 4 >=′ 320
  require cd[324] <= 18446744073709551615
  require calldata.size + -cd[324] - 4 >=′ 320
  require ('cd', 324)[8] <= 18446744073709551615
  require calldata.size >′ cd[324] + ('cd', 324)[8] + 35
  require cd[(cd[324] + ('cd', 324)[8] + 4)] <= 18446744073709551615
  require ceil32(cd[(cd[324] + ('cd', 324)[8] + 4)]) + 768 >= 736 and ceil32(cd[(cd[324] + ('cd', 324)[8] + 4)]) + 768 <= 18446744073709551615
  require cd[324] + ('cd', 324)[8] + cd[(cd[324] + ('cd', 324)[8] + 4)] + 36 <= calldata.size
  require cd[356] <= 18446744073709551615
  require calldata.size >′ cd[356] + 35
  require ('cd', 356).length <= 18446744073709551615
  require ceil32(('cd', 356).length) + 800 >= 768 and ceil32(cd[(cd[324] + ('cd', 324)[8] + 4)]) + ceil32(('cd', 356).length) + 800 <= 18446744073709551615
  require cd[356] + ('cd', 356).length + 36 <= calldata.size
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  require ext_code.size(unknownf0ef5e0dAddress)
  call unknownf0ef5e0dAddress with:
       gas gas_remaining wei
      args cd[292], Array(len=('cd', 356).length, data=call.data[cd[356] + 36 len ('cd', 356).length])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if block.gasprice <= emaValue:
      require emaPeriods + 1
      require emaValue + (2 * block.gasprice / emaPeriods + 1) >= 2 * block.gasprice / emaPeriods + 1
      require emaPeriods + 1
      require 2 * emaValue / emaPeriods + 1 <= emaValue + (2 * block.gasprice / emaPeriods + 1)
      emaValue = emaValue + (2 * block.gasprice / emaPeriods + 1) - (2 * emaValue / emaPeriods + 1)
  else:
      if not unknown903509d6:
          require unknown7ca7cbc1 >= 0
          if block.gasprice < unknown7ca7cbc1:
              require emaPeriods + 1
              require emaValue + (2 * block.gasprice / emaPeriods + 1) >= 2 * block.gasprice / emaPeriods + 1
              require emaPeriods + 1
              require 2 * emaValue / emaPeriods + 1 <= emaValue + (2 * block.gasprice / emaPeriods + 1)
              emaValue = emaValue + (2 * block.gasprice / emaPeriods + 1) - (2 * emaValue / emaPeriods + 1)
      else:
          require emaValue * unknown903509d6 / unknown903509d6 == emaValue
          require unknown7ca7cbc1 + (emaValue * unknown903509d6) >= emaValue * unknown903509d6
          if block.gasprice < unknown7ca7cbc1 + (emaValue * unknown903509d6):
              require emaPeriods + 1
              require emaValue + (2 * block.gasprice / emaPeriods + 1) >= 2 * block.gasprice / emaPeriods + 1
              require emaPeriods + 1
              require 2 * emaValue / emaPeriods + 1 <= emaValue + (2 * block.gasprice / emaPeriods + 1)
              emaValue = emaValue + (2 * block.gasprice / emaPeriods + 1) - (2 * emaValue / emaPeriods + 1)
  return 0, 1


# hash = 0x38a56582
# getter = ['bool', ['storage', 8, 8, 17]]
# const = None
# payable = False
def unknown38a56582(): # not payable
  return bool(unknown38a56582)


# hash = 0x3913c2fd
# getter = None
# const = None
# payable = False
def unknown3913c2fd(addr _param1, addr _param2, uint256 _param3): # not payable
  require calldata.size - 4 >=′ 416
  require calldata.size - 4 >=′ 320
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if not _param3:
      require 0 <= _param3
      require ext_code.size(_param1)
      call _param1.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(_param2), _param3
  else:
      require interestFeePercent * _param3 / _param3 == interestFeePercent
      require interestFeePercent * _param3 / 100 * 10^18 <= _param3
      require ext_code.size(_param1)
      call _param1.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(_param2), _param3 - (interestFeePercent * _param3 / 100 * 10^18)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if return_data.size:
      require return_data.size == 32
      if not ext_call.return_data[0]:
          revert with 0, 'eip20Transfer failed'
  return 1


# hash = 0x3b479208
# getter = None
# const = None
# payable = False
def unknown3b479208(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _param1 != unknown938dd426
  require _param1 <= 100 * 10^18
  unknown938dd426 = _param1


# hash = 0x41ce9f0e
# getter = None
# const = None
# payable = False
def setBZRxTokenContractAddress(address _newAddress): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require bZRxTokenContractAddress != _newAddress
  require _newAddress
  bZRxTokenContractAddress = _newAddress


# hash = 0x4780eac1
# getter = ['storage', 160, 0, 24]
# const = None
# payable = False
def wethContract(): # not payable
  return addr(wethContractAddress)


# hash = 0x4e8440a5
# getter = None
# const = None
# payable = False
def unknown4e8440a5(addr _param1, addr _param2, uint256 _param3, uint256 _param4): # not payable
  require calldata.size - 4 >=′ 128
  require caller == owner
  if not _param3:
      revert with 0, 'destTokenAmountReceived == 0'
  if _param1 == _param2:
      if 10000000000 * 10^18 < _param3:
          if this.address == this.address:
              if this.address != this.address:
                  require ext_code.size(_param2)
                  call _param2.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args addr(this.address), _param3
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if return_data.size:
                      require return_data.size == 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'eip20Transfer failed'
          else:
              if this.address != this.address:
                  require ext_code.size(_param2)
                  call _param2.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args addr(this.address), 10000000000 * 10^18
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if return_data.size:
                      require return_data.size == 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'eip20Transfer failed'
                  if this.address != this.address:
                      if 10000000000 * 10^18 < _param3:
                          require ext_code.size(_param1)
                          call _param1.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(this.address), _param3 - 10000000000 * 10^18
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if return_data.size:
                              require return_data.size == 32
                              if not ext_call.return_data[0]:
                                  revert with 0, 'eip20Transfer failed'
          return 10000000000 * 10^18
      if this.address == this.address:
          if this.address != this.address:
              require ext_code.size(_param2)
              call _param2.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(this.address), _param3
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if return_data.size:
                  require return_data.size == 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'eip20Transfer failed'
      else:
          if this.address != this.address:
              require ext_code.size(_param2)
              call _param2.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(this.address), _param3
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if return_data.size:
                  require return_data.size == 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'eip20Transfer failed'
              if this.address != this.address:
                  if _param3 < _param3:
                      require ext_code.size(_param1)
                      call _param1.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(this.address), 0
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if return_data.size:
                          require return_data.size == 32
                          if not ext_call.return_data[0]:
                              revert with 0, 'eip20Transfer failed'
      if not _param3:
          revert with 0, 'destTokenAmountReceived == 0'
      if _param3 == -1:
          revert with 0, 'destTokenAmountReceived == 0'
      return _param3
  if not stor7[addr(_param1)]:
      revert with 0, 'invalid tokens'
  if not stor7[addr(_param2)]:
      revert with 0, 'invalid tokens'
  if unknown38a56582:
      mem[552] = kyberContractAddress
      require ext_code.size(_param1)
      static call _param1.allowance(address owner, address spender) with:
              gas gas_remaining wei
             args addr(this.address), kyberContractAddress
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if ext_call.return_data[0] < _param3:
          if ext_call.return_data[0]:
              require ext_code.size(_param1)
              call _param1.approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args kyberContractAddress, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if return_data.size:
                  require return_data.size == 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'eip20Approve failed'
          mem[ceil32(return_data.size) + 552] = 10000000000 * 10^18
          require ext_code.size(_param1)
          call _param1.approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args kyberContractAddress, 10000000000 * 10^18
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if return_data.size:
              require return_data.size == 32
              if not ext_call.return_data[0]:
                  revert with 0, 'eip20Approve failed'
      mem[ceil32(return_data.size) + 520] = this.address
      require ext_code.size(_param1)
      static call _param1.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      mem[(2 * ceil32(return_data.size)) + 516 len 320] = tradeWithHint(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId, bytes hint), addr(_param1) << 64, 0, _param3, addr(_param2), addr(this.address), 10000000000 * 10^18, _param4, addr(feeWalletAddress), 256, 4, 'PERM', 0
      mem[(2 * ceil32(return_data.size)) + 836] = ext_call.return_data[24 len 4] or Mask(224, 32, mem[(2 * ceil32(return_data.size)) + 836])
      call kyberContractAddress.0x4 with:
           gas gas_remaining wei
          args 0, mem[(2 * ceil32(return_data.size)) + 836 len 4]
      if not return_data.size:
          require ext_code.size(_param1)
          static call _param1.balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          require ext_call.return_data[0] <= ext_call.return_data[0]
          if 0 > _param3:
              revert with 0, 'too much sourceToken used'
          if this.address != this.address:
              if 0 < _param3:
                  require ext_code.size(_param1)
                  call _param1.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args addr(this.address), _param3
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if return_data.size:
                      require return_data.size == 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'eip20Transfer failed'
          if not ext_call.success:
              revert with 0, 'destTokenAmountReceived == 0'
          if not 'PERM':
              revert with 0, 'destTokenAmountReceived == 0'
          if 'PERM' == -1:
              revert with 0, 'destTokenAmountReceived == 0'
          return 'PERM'
      mem[(2 * ceil32(return_data.size)) + 548 len return_data.size] = ext_call.return_data[0 len return_data.size]
      require ext_code.size(_param1)
      static call _param1.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      require ext_call.return_data[0] <= ext_call.return_data[0]
      if 0 > _param3:
          revert with 0, 'too much sourceToken used'
      if this.address != this.address:
          if 0 < _param3:
              require ext_code.size(_param1)
              call _param1.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(this.address), _param3
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if return_data.size:
                  require return_data.size == 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'eip20Transfer failed'
      if not ext_call.success:
          revert with 0, 'destTokenAmountReceived == 0'
      if not mem[(2 * ceil32(return_data.size)) + 548]:
          revert with 0, 'destTokenAmountReceived == 0'
      if mem[(2 * ceil32(return_data.size)) + 548] == -1:
          revert with 0, 'destTokenAmountReceived == 0'
      return memory
        from (2 * ceil32(return_data.size)) + 548
         [93mlen 32
  mem[488] = kyberContractAddress
  require ext_code.size(_param1)
  static call _param1.allowance(address owner, address spender) with:
          gas gas_remaining wei
         args addr(this.address), kyberContractAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if ext_call.return_data[0] < _param3:
      if ext_call.return_data[0]:
          require ext_code.size(_param1)
          call _param1.approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args kyberContractAddress, 0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if return_data.size:
              require return_data.size == 32
              if not ext_call.return_data[0]:
                  revert with 0, 'eip20Approve failed'
      mem[ceil32(return_data.size) + 488] = 10000000000 * 10^18
      require ext_code.size(_param1)
      call _param1.approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args kyberContractAddress, 10000000000 * 10^18
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      if return_data.size:
          require return_data.size == 32
          if not ext_call.return_data[0]:
              revert with 0, 'eip20Approve failed'
  mem[ceil32(return_data.size) + 456] = this.address
  require ext_code.size(_param1)
  static call _param1.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  mem[(2 * ceil32(return_data.size)) + 452 len 288] = tradeWithHint(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId, bytes hint), addr(_param1) << 64, 0, _param3, addr(_param2), addr(this.address), 10000000000 * 10^18, _param4, addr(feeWalletAddress), 256, 0
  mem[(2 * ceil32(return_data.size)) + 740] = ext_call.return_data[24 len 4] or Mask(224, 32, mem[(2 * ceil32(return_data.size)) + 740])
  call kyberContractAddress.0x100 with:
       gas gas_remaining wei
      args 0, mem[(2 * ceil32(return_data.size)) + 740 len 4]
  if not return_data.size:
      require ext_code.size(_param1)
      static call _param1.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      require ext_call.return_data[0] <= ext_call.return_data[0]
      if 0 > _param3:
          revert with 0, 'too much sourceToken used'
      if this.address != this.address:
          if 0 < _param3:
              require ext_code.size(_param1)
              call _param1.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(this.address), _param3
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if return_data.size:
                  require return_data.size == 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'eip20Transfer failed'
      if not ext_call.success:
          revert with 0, 'destTokenAmountReceived == 0'
      return 292
  mem[(2 * ceil32(return_data.size)) + 484 len return_data.size] = ext_call.return_data[0 len return_data.size]
  require ext_code.size(_param1)
  static call _param1.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  require ext_call.return_data[0] <= ext_call.return_data[0]
  if 0 > _param3:
      revert with 0, 'too much sourceToken used'
  if this.address != this.address:
      if 0 < _param3:
          require ext_code.size(_param1)
          call _param1.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(this.address), _param3
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          if return_data.size:
              require return_data.size == 32
              if not ext_call.return_data[0]:
                  revert with 0, 'eip20Transfer failed'
  if not ext_call.success:
      revert with 0, 'destTokenAmountReceived == 0'
  if not mem[(2 * ceil32(return_data.size)) + 484]:
      revert with 0, 'destTokenAmountReceived == 0'
  if mem[(2 * ceil32(return_data.size)) + 484] == -1:
      revert with 0, 'destTokenAmountReceived == 0'
  return memory
    from (2 * ceil32(return_data.size)) + 484
     [93mlen 32


# hash = 0x4eb60611
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknown4eb60611(): # not payable
  return unknown4eb60611


# hash = 0x4f61ff8b
# getter = ['storage', 160, 0, 23]
# const = None
# payable = False
def kyberNetworkContract(): # not payable
  return kyberNetworkContractAddress


# hash = 0x50c9b1fb
# getter = None
# const = None
# payable = False
def unknown50c9b1fb(): # not payable
  require calldata.size - 4 >=′ 64
  require cd[4] <= 18446744073709551615
  require calldata.size >′ cd[4] + 35
  require ('cd', 4).length <= 18446744073709551615
  require (32 * ('cd', 4).length) + 128 >= 96 and (32 * ('cd', 4).length) + 128 <= 18446744073709551615
  require cd[4] + (32 * ('cd', 4).length) + 36 <= calldata.size
  [94midx = 0
  [94ms = cd[4] + 36
  [94mt = 128
  while [94midx < ('cd', 4).length:
      mem[[94mt] = addr(cd[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  require cd[36] <= 18446744073709551615
  require calldata.size >′ cd[36] + 35
  require ('cd', 36).length <= 18446744073709551615
  require (32 * ('cd', 36).length) + 160 >= 128 and (32 * ('cd', 4).length) + (32 * ('cd', 36).length) + 160 <= 18446744073709551615
  mem[(32 * ('cd', 4).length) + 128] = ('cd', 36).length
  require cd[36] + (32 * ('cd', 36).length) + 36 <= calldata.size
  [94midx = 0
  [94ms = cd[36] + 36
  [94mt = (32 * ('cd', 4).length) + 160
  while [94midx < ('cd', 36).length:
      mem[[94mt] = cd[[94ms]
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  require caller == owner
  if ('cd', 4).length != ('cd', 36).length:
      revert with 0, 'mismatch'
  [94midx = 0
  while [94midx < ('cd', 4).length:
      require [94midx < ('cd', 36).length
      require [94midx < ('cd', 4).length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 9
      unknown032b04b1[mem[(32 * [94midx) + 140 len 20]] = mem[(32 * [94midx) + (32 * ('cd', 4).length) + 160]
      [94midx = [94midx + 1
      continue 


# hash = 0x5a1e921b
# getter = None
# const = None
# payable = False
def isTradeSupported(address _sourceTokenAddress, address _destTokenAddress, uint256 _sourceTokenAmount): # not payable
  require calldata.size - 4 >=′ 96
  if _sourceTokenAddress != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
      if _destTokenAddress != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
          if _sourceTokenAddress != _destTokenAddress:
              if not _sourceTokenAmount:
                  return 0
              if not stor7[addr(_sourceTokenAddress)]:
                  revert with 0, 'invalid tokens'
              if not stor7[addr(_destTokenAddress)]:
                  revert with 0, 'invalid tokens'
              if not unknown035ab37f:
                  mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(_sourceTokenAddress) << 64, 0, addr(_destTokenAddress), Mask(224, 32, _sourceTokenAmount) >> 32
                  static call kyberContractAddress with:
                          gas gas_remaining wei
                         args Mask(224, 32, _sourceTokenAmount) << 480, mem[324 len 4]
              else:
                  require _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000 >= _sourceTokenAmount
                  mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(_sourceTokenAddress) << 64, 0, addr(_destTokenAddress), Mask(224, 32, _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000) >> 32
                  static call kyberContractAddress with:
                          gas gas_remaining wei
                         args Mask(224, 32, _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000) << 480, mem[324 len 4]
              if not return_data.size:
                  if not ext_call.success:
                      return 0
                  if 0 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(_sourceTokenAddress) << 64:
                      return 0
                  if not 0, addr(_destTokenAddress) << 64:
                      return 0
              else:
                  mem[260 len return_data.size] = ext_call.return_data[0 len return_data.size]
                  if not ext_call.success:
                      return 0
                  if 0 == mem[260]:
                      return 0
                  if not mem[292]:
                      return 0
      else:
          if _sourceTokenAddress != addr(wethContractAddress):
              if not _sourceTokenAmount:
                  return 0
              if not stor7[addr(_sourceTokenAddress)]:
                  revert with 0, 'invalid tokens'
              if not stor7[addr(stor24)]:
                  revert with 0, 'invalid tokens'
              if not unknown035ab37f:
                  mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(_sourceTokenAddress) << 64, 0, addr(wethContractAddress), Mask(224, 32, _sourceTokenAmount) >> 32
                  static call kyberContractAddress with:
                       funct uint32(stor24)
                          gas gas_remaining wei
                         args Mask(224, 32, _sourceTokenAmount) << 480, mem[324 len 4]
              else:
                  require _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000 >= _sourceTokenAmount
                  mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(_sourceTokenAddress) << 64, 0, addr(wethContractAddress), Mask(224, 32, _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000) >> 32
                  static call kyberContractAddress with:
                       funct uint32(stor24)
                          gas gas_remaining wei
                         args Mask(224, 32, _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000) << 480, mem[324 len 4]
              if not return_data.size:
                  if not ext_call.success:
                      return 0
                  if 0 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(_sourceTokenAddress) << 64:
                      return 0
                  if not 0, Mask(224, 0, stor24):
                      return 0
              else:
                  mem[260 len return_data.size] = ext_call.return_data[0 len return_data.size]
                  if not ext_call.success:
                      return 0
                  if 0 == mem[260]:
                      return 0
                  if not mem[292]:
                      return 0
  else:
      if _destTokenAddress != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
          if addr(wethContractAddress) != _destTokenAddress:
              if not _sourceTokenAmount:
                  return 0
              if not stor7[addr(stor24)]:
                  revert with 0, 'invalid tokens'
              if not stor7[addr(_destTokenAddress)]:
                  revert with 0, 'invalid tokens'
              if not unknown035ab37f:
                  mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), Mask(224, 0, stor24), uint32(stor24), addr(_destTokenAddress), Mask(224, 32, _sourceTokenAmount) >> 32
                  static call kyberContractAddress with:
                          gas gas_remaining wei
                         args Mask(224, 32, _sourceTokenAmount) << 480, mem[324 len 4]
              else:
                  require _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000 >= _sourceTokenAmount
                  mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), Mask(224, 0, stor24), uint32(stor24), addr(_destTokenAddress), Mask(224, 32, _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000) >> 32
                  static call kyberContractAddress with:
                          gas gas_remaining wei
                         args Mask(224, 32, _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000) << 480, mem[324 len 4]
              if not return_data.size:
                  if not ext_call.success:
                      return 0
                  if 0 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), Mask(224, 0, stor24):
                      return 0
                  if not uint32(stor24), addr(_destTokenAddress) << 64:
                      return 0
              else:
                  mem[260 len return_data.size] = ext_call.return_data[0 len return_data.size]
                  if not ext_call.success:
                      return 0
                  if 0 == mem[260]:
                      return 0
                  if not mem[292]:
                      return 0
      else:
          if addr(wethContractAddress) != addr(wethContractAddress):
              if not _sourceTokenAmount:
                  return 0
              if not stor7[addr(stor24)]:
                  revert with 0, 'invalid tokens'
              if not stor7[addr(stor24)]:
                  revert with 0, 'invalid tokens'
              if not unknown035ab37f:
                  mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), Mask(224, 0, stor24), uint32(stor24), addr(wethContractAddress), Mask(224, 32, _sourceTokenAmount) >> 32
                  static call kyberContractAddress with:
                       funct uint32(stor24)
                          gas gas_remaining wei
                         args Mask(224, 32, _sourceTokenAmount) << 480, mem[324 len 4]
              else:
                  require _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000 >= _sourceTokenAmount
                  mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), Mask(224, 0, stor24), uint32(stor24), addr(wethContractAddress), Mask(224, 32, _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000) >> 32
                  static call kyberContractAddress with:
                       funct uint32(stor24)
                          gas gas_remaining wei
                         args Mask(224, 32, _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000) << 480, mem[324 len 4]
              if not return_data.size:
                  if not ext_call.success:
                      return 0
                  if 0 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), Mask(224, 0, stor24):
                      return 0
                  if not uint32(stor24), Mask(224, 0, stor24):
                      return 0
              else:
                  mem[260 len return_data.size] = ext_call.return_data[0 len return_data.size]
                  if not ext_call.success:
                      return 0
                  if 0 == mem[260]:
                      return 0
                  if not mem[292]:
                      return 0
  return 1


# hash = 0x5e19a6eb
# getter = None
# const = None
# payable = False
def unknown5e19a6eb(): # not payable
  require calldata.size - 4 >=′ 32
  require cd[4] <= 18446744073709551615
  require calldata.size >′ cd[4] + 35
  require ('cd', 4).length <= 18446744073709551615
  require (32 * ('cd', 4).length) + 128 >= 96 and (32 * ('cd', 4).length) + 128 <= 18446744073709551615
  mem[64] = (32 * ('cd', 4).length) + 128
  mem[96] = ('cd', 4).length
  require cd[4] + (32 * ('cd', 4).length) + 36 <= calldata.size
  [94midx = 0
  [94ms = cd[4] + 36
  [94mt = 128
  while [94midx < ('cd', 4).length:
      mem[[94mt] = addr(cd[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  [94midx = 0
  while [94midx < ('cd', 4).length:
      require [94midx < mem[96]
      require ext_code.size(mem[(32 * [94midx) + 140 len 20])
      static call mem[(32 * [94midx) + 140 len 20].decimals() with:
              gas gas_remaining wei
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94m_27 = mem[64]
      mem[64] = mem[64] + ceil32(return_data.size)
      require return_data.size >=′ 32
      [94m_28 = mem[[94m_27]
      require [94midx < mem[96]
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 8
      decimals[mem[(32 * [94midx) + 140 len 20]].field_0 = uint8([94m_28)
      decimals[mem[(32 * [94midx) + 140 len 20]].field_8 = 0
      [94midx = [94midx + 1
      continue 


# hash = 0x63621532
# getter = None
# const = None
# payable = False
def unknown63621532(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _param1 != unknowncc11a3b6
  unknowncc11a3b6 = _param1


# hash = 0x68c4ac26
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 7]]]]
# const = None
# payable = False
def supportedTokens(address _param1): # not payable
  require calldata.size - 4 >=′ 32
  return bool(stor7[_param1])


# hash = 0x6f1296d2
# getter = None
# const = None
# payable = False
def wrapEther(): # not payable
  require caller == owner
  if eth.balance(this.address):
      require ext_code.size(addr(wethContractAddress))
      call addr(wethContractAddress).deposit() with:
         value eth.balance(this.address) wei
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0x72e98a79
# getter = None
# const = None
# payable = False
def transferBZxOwnership(address _newBZxContractAddress): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  if not _newBZxContractAddress:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'transferBZxOwnership::unauthorized'
  if owner == _newBZxContractAddress:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'transferBZxOwnership::unauthorized'
  log BZxOwnershipTransferred(
        address previousBZxContract=bZxContractAddress,
        address newBZxContract=_newBZxContractAddress)
  bZxContractAddress = _newBZxContractAddress


# hash = 0x754efc98
# getter = ['bool', ['storage', 8, 0, 4]]
# const = None
# payable = False
def throwOnGasRefundFail(): # not payable
  return bool(throwOnGasRefundFail)


# hash = 0x760c8859
# getter = None
# const = None
# payable = False
def unknown760c8859(): # not payable
  require caller == owner
  require ext_code.size(kyberContractAddress)
  static call kyberContractAddress.kyberNetworkContract() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  kyberNetworkContractAddress = ext_call.return_data[12 len 20]


# hash = 0x779dec5b
# getter = ['storage', 160, 0, 25]
# const = None
# payable = False
def bZRxTokenContract(): # not payable
  return bZRxTokenContractAddress


# hash = 0x783882be
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknown783882be(): # not payable
  return unknown783882be


# hash = 0x787f7fca
# getter = ['storage', 256, 0, 18]
# const = None
# payable = False
def unknown787f7fca(): # not payable
  return unknown787f7fca


# hash = 0x7ca7cbc1
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknown7ca7cbc1(): # not payable
  return unknown7ca7cbc1


# hash = 0x7dbe6df8
# getter = None
# const = None
# payable = False
def unknown7dbe6df8(): # not payable
  require calldata.size - 4 >=′ 64
  require cd[4] <= 18446744073709551615
  require calldata.size >′ cd[4] + 35
  require ('cd', 4).length <= 18446744073709551615
  require (32 * ('cd', 4).length) + 128 >= 96 and (32 * ('cd', 4).length) + 128 <= 18446744073709551615
  require cd[4] + (32 * ('cd', 4).length) + 36 <= calldata.size
  [94midx = 0
  [94ms = cd[4] + 36
  [94mt = 128
  while [94midx < ('cd', 4).length:
      mem[[94mt] = addr(cd[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  require cd[36] <= 18446744073709551615
  require calldata.size >′ cd[36] + 35
  require ('cd', 36).length <= 18446744073709551615
  require (32 * ('cd', 36).length) + 160 >= 128 and (32 * ('cd', 4).length) + (32 * ('cd', 36).length) + 160 <= 18446744073709551615
  mem[(32 * ('cd', 4).length) + 128] = ('cd', 36).length
  require cd[36] + (32 * ('cd', 36).length) + 36 <= calldata.size
  [94midx = 0
  [94ms = cd[36] + 36
  [94mt = (32 * ('cd', 4).length) + 160
  while [94midx < ('cd', 36).length:
      mem[[94mt] = bool(cd[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  require caller == owner
  if ('cd', 4).length != ('cd', 36).length:
      revert with 0, 'count mismatch'
  [94midx = 0
  while [94midx < ('cd', 4).length:
      require [94midx < ('cd', 36).length
      require [94midx < ('cd', 4).length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 7
      stor7[mem[(32 * [94midx) + 140 len 20]] = uint8(bool(mem[(32 * [94midx) + (32 * ('cd', 4).length) + 160]))
      [94midx = [94midx + 1
      continue 


# hash = 0x8605c97e
# getter = None
# const = None
# payable = False
def setMarginThresholds(uint256 _newInitialMargin, uint256 _newMaintenanceMargin): # not payable
  require calldata.size - 4 >=′ 64
  require caller == owner
  require _newInitialMargin >= _newMaintenanceMargin
  minInitialMarginAmount = _newInitialMargin
  minMaintenanceMarginAmount = _newMaintenanceMargin


# hash = 0x871105cc
# getter = None
# const = None
# payable = False
def setVaultContractAddress(address _newAddress): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require vaultContractAddress != _newAddress
  require _newAddress
  vaultContractAddress = _newAddress


# hash = 0x8c9f7074
# getter = None
# const = None
# payable = False
def setInterestFeePercent(uint256 _newRate): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _newRate != interestFeePercent
  require _newRate <= 100 * 10^18
  interestFeePercent = _newRate


# hash = 0x8da5cb5b
# getter = ['storage', 160, 8, 4]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x903509d6
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def unknown903509d6(): # not payable
  return unknown903509d6


# hash = 0x90d49b9d
# getter = None
# const = None
# payable = False
def setFeeWallet(address _feeWallet): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  if _feeWallet:
      addr(feeWalletAddress) = _feeWallet
  else:
      uint256(stor20) = this.address or Mask(96, 160, uint256(stor20))


# hash = 0x938dd426
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def unknown938dd426(): # not payable
  return unknown938dd426


# hash = 0xa48205cb
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def emaValue(): # not payable
  return emaValue


# hash = 0xa9ada2bd
# getter = None
# const = None
# payable = False
def unknowna9ada2bd(uint256 _param1, bool _param2): # not payable
  require calldata.size - 4 >=′ 64
  require caller == owner
  if _param1 != unknown4eb60611:
      unknown4eb60611 = _param1
  if _param2 != bool(unknownf0ad0b7f):
      unknownf0ad0b7f = uint8(_param2)


# hash = 0xaf2bf027
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def minMaintenanceMarginAmount(): # not payable
  return minMaintenanceMarginAmount


# hash = 0xb36b72df
# getter = None
# const = None
# payable = False
def unknownb36b72df(addr _param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require unknownf0ef5e0dAddress != _param1
  require _param1
  unknownf0ef5e0dAddress = _param1


# hash = 0xb7a6711c
# getter = None
# const = None
# payable = False
def unknownb7a6711c(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _param1 != unknown787f7fca
  unknown787f7fca = _param1


# hash = 0xcc11a3b6
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def unknowncc11a3b6(): # not payable
  return unknowncc11a3b6


# hash = 0xcc677679
# getter = None
# const = None
# payable = False
def setEMAPeriods(uint256 _newEMAPeriods): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _newEMAPeriods > 1
  require _newEMAPeriods != emaPeriods
  emaPeriods = _newEMAPeriods


# hash = 0xd28a4f9e
# getter = None
# const = None
# payable = False
def setKyberContractAddress(address _newAddress): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require kyberContractAddress != _newAddress
  require _newAddress
  kyberContractAddress = _newAddress


# hash = 0xd449a832
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 8]]]
# const = None
# payable = False
def decimals(address _token): # not payable
  require calldata.size - 4 >=′ 32
  return decimals[_token].field_0


# hash = 0xd5a60129
# getter = None
# const = None
# payable = False
def unknownd5a60129(bool _param1, bool _param2): # not payable
  require calldata.size - 4 >=′ 64
  require caller == owner
  unknown035ab37f = uint8(_param1)
  Mask(248, 0, stor17.field_8) = Mask(248, 0, _param2)
  Mask(240, 0, stor17.field_16) = Mask(240, 16, _param1) >> 16


# hash = 0xdaebc33e
# getter = None
# const = None
# payable = False
def unknowndaebc33e(addr _param1, addr _param2, uint256 _param3): # not payable
  require calldata.size - 4 >=′ 128
  if bZxContractAddress != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'only bZx contracts can call this function'
  if not _param3:
      require 0 <= _param3
      require ext_code.size(_param2)
      call _param2.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(_param1), _param3
  else:
      require interestFeePercent * _param3 / _param3 == interestFeePercent
      require interestFeePercent * _param3 / 100 * 10^18 <= _param3
      require ext_code.size(_param2)
      call _param2.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(_param1), _param3 - (interestFeePercent * _param3 / 100 * 10^18)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if return_data.size:
      require return_data.size == 32
      if not ext_call.return_data[0]:
          revert with 0, 'eip20Transfer failed'
  return 1


# hash = 0xe2506eab
# getter = None
# const = None
# payable = False
def unknowne2506eab(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _param1 != emaValue
  emaValue = _param1


# hash = 0xe4a72b13
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def bZxContractAddress(): # not payable
  return bZxContractAddress


# hash = 0xef8d2a40
# getter = None
# const = None
# payable = False
def unknownef8d2a40(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _param1 != unknown783882be
  unknown783882be = _param1


# hash = 0xf0ad0b7f
# getter = ['bool', ['storage', 8, 0, 11]]
# const = None
# payable = False
def unknownf0ad0b7f(): # not payable
  return bool(unknownf0ad0b7f)


# hash = 0xf0ef5e0d
# getter = ['storage', 160, 0, 26]
# const = None
# payable = False
def unknownf0ef5e0d(): # not payable
  return unknownf0ef5e0dAddress


# hash = 0xf1cf5b38
# getter = None
# const = None
# payable = False
def setWethContractAddress(address _newAddress): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require addr(wethContractAddress) != _newAddress
  require _newAddress
  addr(wethContractAddress) = _newAddress


# hash = 0xf25f4b56
# getter = ['storage', 160, 0, 20]
# const = None
# payable = False
def feeWallet(): # not payable
  return addr(feeWalletAddress)


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  if not _newOwner:
      revert with 0, 'transferOwnership::unauthorized'
  if bZxContractAddress == _newOwner:
      revert with 0, 'transferOwnership::unauthorized'
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = 0xf5537ede
# getter = None
# const = None
# payable = False
def transferToken(address _token, address _to, uint256 _val): # not payable
  require calldata.size - 4 >=′ 96
  require caller == owner
  require ext_code.size(_token)
  static call _token.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  require ext_code.size(_token)
  if _val <= ext_call.return_data[0]:
      call _token.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(_to), _val
  else:
      call _token.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(_to), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  return bool(ext_call.return_data[0])


# hash = 0xfbb7f232
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 27]]]
# const = None
# payable = False
def unknownfbb7f232(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  return unknownfbb7f232[_param1]


# hash = 0xfe8925f4
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def interestFeePercent(): # not payable
  return interestFeePercent


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if caller == bZxContractAddress:
      if block.gasprice <= emaValue:
          require emaPeriods + 1
          require emaValue + (2 * block.gasprice / emaPeriods + 1) >= 2 * block.gasprice / emaPeriods + 1
          require emaPeriods + 1
          require 2 * emaValue / emaPeriods + 1 <= emaValue + (2 * block.gasprice / emaPeriods + 1)
          emaValue = emaValue + (2 * block.gasprice / emaPeriods + 1) - (2 * emaValue / emaPeriods + 1)
      else:
          if not unknown903509d6:
              require unknown7ca7cbc1 >= 0
              if block.gasprice < unknown7ca7cbc1:
                  require emaPeriods + 1
                  require emaValue + (2 * block.gasprice / emaPeriods + 1) >= 2 * block.gasprice / emaPeriods + 1
                  require emaPeriods + 1
                  require 2 * emaValue / emaPeriods + 1 <= emaValue + (2 * block.gasprice / emaPeriods + 1)
                  emaValue = emaValue + (2 * block.gasprice / emaPeriods + 1) - (2 * emaValue / emaPeriods + 1)
          else:
              require emaValue * unknown903509d6 / unknown903509d6 == emaValue
              require unknown7ca7cbc1 + (emaValue * unknown903509d6) >= emaValue * unknown903509d6
              if block.gasprice < unknown7ca7cbc1 + (emaValue * unknown903509d6):
                  require emaPeriods + 1
                  require emaValue + (2 * block.gasprice / emaPeriods + 1) >= 2 * block.gasprice / emaPeriods + 1
                  require emaPeriods + 1
                  require 2 * emaValue / emaPeriods + 1 <= emaValue + (2 * block.gasprice / emaPeriods + 1)
                  emaValue = emaValue + (2 * block.gasprice / emaPeriods + 1) - (2 * emaValue / emaPeriods + 1)
  return 1


