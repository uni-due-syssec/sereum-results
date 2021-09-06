# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x03E0635A77Ca3DbC23748aF10a568663964f4BAD 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x00432cf3': 'getCurrentMarginAmount(address _loanTokenAddress, address _positionTokenAddress, address _collateralTokenAddress, uint256 _loanTokenAmount, uint256 _positionTokenAmount, uint256 _collateralTokenAmount)', '0x016d7c64': 'unknown016d7c64(?)', '0x051c8a8d': 'unknown051c8a8d(?)', '0x369308ce': 'unknown369308ce(?)', '0x4849b6c8': 'unknown4849b6c8(?)', '0x4e8440a5': 'unknown4e8440a5(?)', '0x5e3f4b3c': 'unknown5e3f4b3c(?)', '0x89611678': 'unknown89611678(?)', '0xc3feec61': 'unknownc3feec61(?)', '0xff8a2640': 'unknownff8a2640(?)'} 

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
    unknown4eb60611 # mask: a s
    # storage address 9
    unknownf0ad0b7f # mask: a s
    # storage address 10
    interestFeePercent # mask: a s
    # storage address 11
    unknown783882be # mask: a s
    # storage address 12
    unknowncc11a3b6 # mask: a s
    # storage address 13
    minInitialMarginAmount # mask: a s
    # storage address 14
    minMaintenanceMarginAmount # mask: a s
    # storage address 15
    stor15 # mask: a s
    # storage address 15
    unknown035ab37f # mask: a s
    # storage address 15
    unknown38a56582 # mask: a s
    # storage address 15
    stor15 # mask: a s
    # storage address 16
    unknown787f7fca # mask: a s
    # storage address 17
    unknownf481e71b # mask: a s
    # storage address 18
    vaultContractAddress # mask: a s
    # storage address 19
    kyberContractAddress # mask: a s
    # storage address 20
    kyberNetworkContractAddress # mask: a s
    # storage address 21
    wethContractAddress # mask: a s
    # storage address 22
    bZRxTokenContractAddress # mask: a s
    # storage address 23
    unknownf0ef5e0dAddress # mask: a s
    # storage address 24
    unknownfbb7f232
# hash = 0x035ab37f
# getter = ['bool', ['storage', 8, 0, 15]]
# const = None
# payable = False
def unknown035ab37f(): # not payable
  return bool(munknown035ab37f)


# hash = 0x05b1137b
# getter = None
# const = None
# payable = False
def transferEther(address m_to, uint256 m_value): # not payable
  require calldata.size - 4 >=′ 64
  require caller == mowner
  if m_value <= eth.balance(this.address):
      call m_to with:
         value m_value wei
           gas 2300 * is_zero(value) wei
  else:
      call m_to with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
  return bool(ext_call.success)


# hash = 0x06599aa0
# getter = None
# const = None
# payable = False
def unknown06599aa0(addr m_param1, addr m_param2, uint256 m_param3): # not payable
  require calldata.size - 4 >=′ 96
  if m_param1 == m_param2:
      if not m_param3:
          return 10^18, 10^18, 0
      if 10^18 * m_param3 / m_param3 == 10^18:
          return 10^18, 10^18, 10^18 * m_param3 / 10^18
  else:
      if not munknown035ab37f:
          mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64, 0, addr(m_param2), Mask(224, 32, m_param3) >> 32
          mem[352 len 4] = uint32(m_param3)
          static call mkyberContractAddress with:
                  gas gas_remaining wei
                 args Mask(224, 32, m_param3) << 480, mem[324 len 4]
          if not return_data.size:
              if not ext_call.success:
                  if m_param1 == m_param2:
                      if not m_param3:
                          return 0, 10^18, 0
                      if not 0 / m_param3:
                          return 0, 10^18, 0
                  else:
                      if mstor7m[addr(m_param1)m]m.field_0:
                          if mstor7m[addr(m_param2)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0 < mstor7m[addr(m_param1)m]m.field_0:
                                  if mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                      if not m_param3:
                                          if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                              return 0, 
                                                     10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                     0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                              else:
                                  if mstor7m[addr(m_param2)m]m.field_0 - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                      if not m_param3:
                                          if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                              return 0, 
                                                     10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                     0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                          else:
                              require ext_code.size(m_param2)
                              static call m_param2.decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 32
                              if ext_call.return_data[31 len 1] < mstor7m[addr(m_param1)m]m.field_0:
                                  if mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18 >= 18:
                                      if not m_param3:
                                          if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                              return 0, 
                                                     10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                     0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                                  return 0, 
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                              else:
                                  if ext_call.return_data[31 len 1] - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                      if not m_param3:
                                          if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                              return 0, 
                                                     10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                     0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                      else:
                          require ext_code.size(m_param1)
                          static call m_param1.decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 32
                          if mstor7m[addr(m_param2)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0 < ext_call.return_data[31 len 1]:
                                  if ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                      if not m_param3:
                                          if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                              return 0, 
                                                     10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                     0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                              else:
                                  if mstor7m[addr(m_param2)m]m.field_0 - ext_call.return_data[31 len 1] <= 18:
                                      if not m_param3:
                                          if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                              return 0, 
                                                     10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                     0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                                  return 0, 
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                          else:
                              require ext_code.size(m_param2)
                              static call m_param2.decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 32
                              if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                  if uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18:
                                      if not m_param3:
                                          if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                              return 0, 10^18, 0 / 10^18
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                                  return 0, 10^18, 0 / 10^18
                              else:
                                  if ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18:
                                      if not m_param3:
                                          if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                              return 0, 10^18, 0 / 10^18
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                                  return 0, 10^18, 0 / 10^18
              else:
                  if m_param1 == m_param2:
                      if not m_param3:
                          return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64, 10^18, 0
                      if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                          return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                 addr(m_param1) << 64,
                                 10^18,
                                 getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^18
                  else:
                      if mstor7m[addr(m_param1)m]m.field_0:
                          if mstor7m[addr(m_param2)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0 < mstor7m[addr(m_param1)m]m.field_0:
                                  if mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                      if not m_param3:
                                          if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                              return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                     addr(m_param1) << 64,
                                                     10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                     0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                      else:
                                          if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                              else:
                                  if mstor7m[addr(m_param2)m]m.field_0 - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                      if not m_param3:
                                          if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                              return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                     addr(m_param1) << 64,
                                                     10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                     0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                      else:
                                          if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                          else:
                              require ext_code.size(m_param2)
                              static call m_param2.decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 32
                              if ext_call.return_data[31 len 1] < mstor7m[addr(m_param1)m]m.field_0:
                                  if mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18 >= 18:
                                      if not m_param3:
                                          if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                              return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                     addr(m_param1) << 64,
                                                     10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                     0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                                      else:
                                          if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                         getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                              else:
                                  if ext_call.return_data[31 len 1] - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                      if not m_param3:
                                          if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                              return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                     addr(m_param1) << 64,
                                                     10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                     0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                      else:
                                          if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                              if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                      else:
                          require ext_code.size(m_param1)
                          static call m_param1.decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 32
                          if mstor7m[addr(m_param2)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0 < ext_call.return_data[31 len 1]:
                                  if ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                      if not m_param3:
                                          if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                              return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                     addr(m_param1) << 64,
                                                     10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                     0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                      else:
                                          if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                              if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                              else:
                                  if mstor7m[addr(m_param2)m]m.field_0 - ext_call.return_data[31 len 1] <= 18:
                                      if not m_param3:
                                          if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                              return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                     addr(m_param1) << 64,
                                                     10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                     0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                                      else:
                                          if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                         getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                          else:
                              require ext_code.size(m_param2)
                              static call m_param2.decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 32
                              if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                  if uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18:
                                      if not m_param3:
                                          if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                              return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64, 10^18, 0 / 10^18
                                      else:
                                          if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                              if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^18,
                                                         getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^18
                              else:
                                  if ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18:
                                      if not m_param3:
                                          if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                              return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64, 10^18, 0 / 10^18
                                      else:
                                          if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                              if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^18,
                                                         getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^18
          else:
              mem[260 len return_data.size] = ext_call.return_data[0 len return_data.size]
              if not ext_call.success:
                  if m_param1 == m_param2:
                      if not m_param3:
                          return 0, 10^18, 0
                      if not 0 / m_param3:
                          return 0, 10^18, 0
                  else:
                      if mstor7m[addr(m_param1)m]m.field_0:
                          if mstor7m[addr(m_param2)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0 < mstor7m[addr(m_param1)m]m.field_0:
                                  if mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                      if not m_param3:
                                          if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                              return 0, 
                                                     10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                     0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                              else:
                                  if mstor7m[addr(m_param2)m]m.field_0 - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                      if not m_param3:
                                          if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                              return 0, 
                                                     10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                     0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                          else:
                              require ext_code.size(m_param2)
                              static call m_param2.decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 32
                              if ext_call.return_data[31 len 1] < mstor7m[addr(m_param1)m]m.field_0:
                                  if mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18 >= 18:
                                      if not m_param3:
                                          if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                              return 0, 
                                                     10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                     0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                                  return 0, 
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                              else:
                                  if ext_call.return_data[31 len 1] - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                      if not m_param3:
                                          if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                              return 0, 
                                                     10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                     0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                      else:
                          require ext_code.size(m_param1)
                          static call m_param1.decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 32
                          if mstor7m[addr(m_param2)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0 < ext_call.return_data[31 len 1]:
                                  if ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                      if not m_param3:
                                          if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                              return 0, 
                                                     10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                     0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                              else:
                                  if mstor7m[addr(m_param2)m]m.field_0 - ext_call.return_data[31 len 1] <= 18:
                                      if not m_param3:
                                          if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                              return 0, 
                                                     10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                     0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                                  return 0, 
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                          else:
                              require ext_code.size(m_param2)
                              static call m_param2.decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 32
                              if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                  if uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18:
                                      if not m_param3:
                                          if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                              return 0, 10^18, 0 / 10^18
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                                  return 0, 10^18, 0 / 10^18
                              else:
                                  if ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18:
                                      if not m_param3:
                                          if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                              return 0, 10^18, 0 / 10^18
                                      else:
                                          if not 0 / m_param3:
                                              if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                                  return 0, 10^18, 0 / 10^18
              else:
                  [94m_457 = mem[260]
                  if m_param1 == m_param2:
                      if not m_param3:
                          mem[ceil32(return_data.size) + 229] = mem[260]
                          return mem[ceil32(return_data.size) + 229], 10^18, 0
                      require mem[260] * m_param3 / m_param3 == mem[260]
                      mem[ceil32(return_data.size) + 229] = mem[260]
                      return mem[ceil32(return_data.size) + 229], 10^18, [94m_457 * m_param3 / 10^18
                  if mstor7m[addr(m_param1)m]m.field_0:
                      if mstor7m[addr(m_param2)m]m.field_0:
                          if mstor7m[addr(m_param2)m]m.field_0 < mstor7m[addr(m_param1)m]m.field_0:
                              require mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18
                              if not m_param3:
                                  require 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                  mem[ceil32(return_data.size) + 229] = mem[260]
                                  return mem[ceil32(return_data.size) + 229], 
                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                              require mem[260] * m_param3 / m_param3 == mem[260]
                              require 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                              mem[ceil32(return_data.size) + 229] = mem[260]
                              return mem[ceil32(return_data.size) + 229], 
                                     10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                     [94m_457 * m_param3 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                          require mstor7m[addr(m_param2)m]m.field_0 - mstor7m[addr(m_param1)m]m.field_0 <= 18
                          if not m_param3:
                              require 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                              mem[ceil32(return_data.size) + 229] = mem[260]
                              return mem[ceil32(return_data.size) + 229], 
                                     10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                     0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                          require mem[260] * m_param3 / m_param3 == mem[260]
                          require 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                          mem[ceil32(return_data.size) + 229] = mem[260]
                          return mem[ceil32(return_data.size) + 229], 
                                 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                 [94m_457 * m_param3 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                      require ext_code.size(m_param2)
                      static call m_param2.decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 32
                      if ext_call.return_data[31 len 1] < mstor7m[addr(m_param1)m]m.field_0:
                          if mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18 >= 18:
                              if not m_param3:
                                  if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                      return mem[260], 
                                             10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                             0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                              else:
                                  if mem[260] * m_param3 / m_param3 == mem[260]:
                                      if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                          return mem[260], 
                                                 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                 mem[260] * m_param3 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                      else:
                          if ext_call.return_data[31 len 1] - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                              if not m_param3:
                                  if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                      return mem[260], 
                                             10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                             0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                              else:
                                  if mem[260] * m_param3 / m_param3 == mem[260]:
                                      if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                          return mem[260], 
                                                 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                 mem[260] * m_param3 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                  else:
                      require ext_code.size(m_param1)
                      static call m_param1.decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 32
                      if mstor7m[addr(m_param2)m]m.field_0:
                          if mstor7m[addr(m_param2)m]m.field_0 < ext_call.return_data[31 len 1]:
                              if ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                  if not m_param3:
                                      if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                          return mem[260], 
                                                 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                 0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                  else:
                                      if mem[260] * m_param3 / m_param3 == mem[260]:
                                          if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                              return mem[260], 
                                                     10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                     mem[260] * m_param3 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                          else:
                              if mstor7m[addr(m_param2)m]m.field_0 - ext_call.return_data[31 len 1] <= 18:
                                  if not m_param3:
                                      if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                          return mem[260], 
                                                 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                 0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                                  else:
                                      if mem[260] * m_param3 / m_param3 == mem[260]:
                                          if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                              return mem[260], 
                                                     10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                     mem[260] * m_param3 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                      else:
                          require ext_code.size(m_param2)
                          static call m_param2.decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 32
                          if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                              if uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18:
                                  if not m_param3:
                                      if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                          return mem[260], 10^18, 0 / 10^18
                                  else:
                                      if mem[260] * m_param3 / m_param3 == mem[260]:
                                          if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                              return mem[260], 10^18, mem[260] * m_param3 / 10^18
                          else:
                              if ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18:
                                  if not m_param3:
                                      if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                          return mem[260], 10^18, 0 / 10^18
                                  else:
                                      if mem[260] * m_param3 / m_param3 == mem[260]:
                                          if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                              return mem[260], 10^18, mem[260] * m_param3 / 10^18
      else:
          if m_param3 - 0x8000000000000000000000000000000000000000000000000000000000000000 >= m_param3:
              mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64, 0, addr(m_param2), Mask(224, 32, m_param3 - 0x8000000000000000000000000000000000000000000000000000000000000000) >> 32
              mem[352 len 4] = Mask(32, 64, m_param3 - 0x8000000000000000000000000000000000000000000000000000000000000000) >> 64
              static call mkyberContractAddress with:
                      gas gas_remaining wei
                     args Mask(224, 32, m_param3 - 0x8000000000000000000000000000000000000000000000000000000000000000) << 480, mem[324 len 4]
              if not return_data.size:
                  if not ext_call.success:
                      if m_param1 == m_param2:
                          if not m_param3:
                              return 0, 10^18, 0
                          if not 0 / m_param3:
                              return 0, 10^18, 0
                      else:
                          if mstor7m[addr(m_param1)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0:
                                  if mstor7m[addr(m_param2)m]m.field_0 < mstor7m[addr(m_param1)m]m.field_0:
                                      if mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                          if not m_param3:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                      return 0, 
                                                             10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                             0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                  else:
                                      if mstor7m[addr(m_param2)m]m.field_0 - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                          if not m_param3:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                      return 0, 
                                                             10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                             0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                              else:
                                  require ext_code.size(m_param2)
                                  static call m_param2.decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 32
                                  if ext_call.return_data[31 len 1] < mstor7m[addr(m_param1)m]m.field_0:
                                      if mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18 >= 18:
                                          if not m_param3:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                                  return 0, 
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                                      return 0, 
                                                             10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                             0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                                  else:
                                      if ext_call.return_data[31 len 1] - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                          if not m_param3:
                                              if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                      return 0, 
                                                             10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                             0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                          else:
                              require ext_code.size(m_param1)
                              static call m_param1.decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 32
                              if mstor7m[addr(m_param2)m]m.field_0:
                                  if mstor7m[addr(m_param2)m]m.field_0 < ext_call.return_data[31 len 1]:
                                      if ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                          if not m_param3:
                                              if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                      return 0, 
                                                             10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                             0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                  else:
                                      if mstor7m[addr(m_param2)m]m.field_0 - ext_call.return_data[31 len 1] <= 18:
                                          if not m_param3:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                                  return 0, 
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                                      return 0, 
                                                             10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                             0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                              else:
                                  require ext_code.size(m_param2)
                                  static call m_param2.decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 32
                                  if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                      if uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18:
                                          if not m_param3:
                                              if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                                  return 0, 10^18, 0 / 10^18
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                                      return 0, 10^18, 0 / 10^18
                                  else:
                                      if ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18:
                                          if not m_param3:
                                              if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                                  return 0, 10^18, 0 / 10^18
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                                      return 0, 10^18, 0 / 10^18
                  else:
                      if m_param1 == m_param2:
                          if not m_param3:
                              return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64, 10^18, 0
                          if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                              return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                     addr(m_param1) << 64,
                                     10^18,
                                     getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^18
                      else:
                          if mstor7m[addr(m_param1)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0:
                                  if mstor7m[addr(m_param2)m]m.field_0 < mstor7m[addr(m_param1)m]m.field_0:
                                      if mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                          if not m_param3:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                          else:
                                              if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                                  if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                      return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                             addr(m_param1) << 64,
                                                             10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                             getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                  else:
                                      if mstor7m[addr(m_param2)m]m.field_0 - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                          if not m_param3:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                          else:
                                              if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                                  if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                      return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                             addr(m_param1) << 64,
                                                             10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                             getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                              else:
                                  require ext_code.size(m_param2)
                                  static call m_param2.decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 32
                                  if ext_call.return_data[31 len 1] < mstor7m[addr(m_param1)m]m.field_0:
                                      if mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18 >= 18:
                                          if not m_param3:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                                          else:
                                              if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                                  if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                                      return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                             addr(m_param1) << 64,
                                                             10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                             getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                                  else:
                                      if ext_call.return_data[31 len 1] - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                          if not m_param3:
                                              if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                          else:
                                              if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                                  if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                      return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                             addr(m_param1) << 64,
                                                             10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                             getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                          else:
                              require ext_code.size(m_param1)
                              static call m_param1.decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 32
                              if mstor7m[addr(m_param2)m]m.field_0:
                                  if mstor7m[addr(m_param2)m]m.field_0 < ext_call.return_data[31 len 1]:
                                      if ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                          if not m_param3:
                                              if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                          else:
                                              if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                                  if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                      return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                             addr(m_param1) << 64,
                                                             10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                             getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                  else:
                                      if mstor7m[addr(m_param2)m]m.field_0 - ext_call.return_data[31 len 1] <= 18:
                                          if not m_param3:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                         addr(m_param1) << 64,
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                                          else:
                                              if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                                  if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                                      return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                             addr(m_param1) << 64,
                                                             10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                             getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                              else:
                                  require ext_code.size(m_param2)
                                  static call m_param2.decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 32
                                  if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                      if uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18:
                                          if not m_param3:
                                              if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64, 10^18, 0 / 10^18
                                          else:
                                              if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                                  if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                                      return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                             addr(m_param1) << 64,
                                                             10^18,
                                                             getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^18
                                  else:
                                      if ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18:
                                          if not m_param3:
                                              if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                                  return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64, 10^18, 0 / 10^18
                                          else:
                                              if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / m_param3 == getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64:
                                                  if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                                      return getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), 
                                                             addr(m_param1) << 64,
                                                             10^18,
                                                             getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_param1) << 64 * m_param3 / 10^18
              else:
                  mem[260 len return_data.size] = ext_call.return_data[0 len return_data.size]
                  if not ext_call.success:
                      if m_param1 == m_param2:
                          if not m_param3:
                              return 0, 10^18, 0
                          if not 0 / m_param3:
                              return 0, 10^18, 0
                      else:
                          if mstor7m[addr(m_param1)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0:
                                  if mstor7m[addr(m_param2)m]m.field_0 < mstor7m[addr(m_param1)m]m.field_0:
                                      if mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                          if not m_param3:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                      return 0, 
                                                             10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                             0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                  else:
                                      if mstor7m[addr(m_param2)m]m.field_0 - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                          if not m_param3:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                      return 0, 
                                                             10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                             0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                              else:
                                  require ext_code.size(m_param2)
                                  static call m_param2.decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 32
                                  if ext_call.return_data[31 len 1] < mstor7m[addr(m_param1)m]m.field_0:
                                      if mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18 >= 18:
                                          if not m_param3:
                                              if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                                  return 0, 
                                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                         0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                                      return 0, 
                                                             10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                             0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                                  else:
                                      if ext_call.return_data[31 len 1] - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                          if not m_param3:
                                              if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                         0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                                      return 0, 
                                                             10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                             0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                          else:
                              require ext_code.size(m_param1)
                              static call m_param1.decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 32
                              if mstor7m[addr(m_param2)m]m.field_0:
                                  if mstor7m[addr(m_param2)m]m.field_0 < ext_call.return_data[31 len 1]:
                                      if ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                          if not m_param3:
                                              if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return 0, 
                                                         10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                      return 0, 
                                                             10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                             0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                  else:
                                      if mstor7m[addr(m_param2)m]m.field_0 - ext_call.return_data[31 len 1] <= 18:
                                          if not m_param3:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                                  return 0, 
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                                      return 0, 
                                                             10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                             0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                              else:
                                  require ext_code.size(m_param2)
                                  static call m_param2.decimals() with:
                                          gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 32
                                  if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                      if uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18:
                                          if not m_param3:
                                              if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                                  return 0, 10^18, 0 / 10^18
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                                      return 0, 10^18, 0 / 10^18
                                  else:
                                      if ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18:
                                          if not m_param3:
                                              if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                                  return 0, 10^18, 0 / 10^18
                                          else:
                                              if not 0 / m_param3:
                                                  if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                                      return 0, 10^18, 0 / 10^18
                  else:
                      [94m_453 = mem[260]
                      if m_param1 == m_param2:
                          if not m_param3:
                              mem[ceil32(return_data.size) + 229] = mem[260]
                              return mem[ceil32(return_data.size) + 229], 10^18, 0
                          require mem[260] * m_param3 / m_param3 == mem[260]
                          mem[ceil32(return_data.size) + 229] = mem[260]
                          return mem[ceil32(return_data.size) + 229], 10^18, [94m_453 * m_param3 / 10^18
                      if mstor7m[addr(m_param1)m]m.field_0:
                          if mstor7m[addr(m_param2)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0 < mstor7m[addr(m_param1)m]m.field_0:
                                  require mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18
                                  if not m_param3:
                                      require 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                      mem[ceil32(return_data.size) + 229] = mem[260]
                                      return mem[ceil32(return_data.size) + 229], 
                                             10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                             0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                  require mem[260] * m_param3 / m_param3 == mem[260]
                                  require 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                  mem[ceil32(return_data.size) + 229] = mem[260]
                                  return mem[ceil32(return_data.size) + 229], 
                                         10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                         [94m_453 * m_param3 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                              require mstor7m[addr(m_param2)m]m.field_0 - mstor7m[addr(m_param1)m]m.field_0 <= 18
                              if not m_param3:
                                  require 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                  mem[ceil32(return_data.size) + 229] = mem[260]
                                  return mem[ceil32(return_data.size) + 229], 
                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                         0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                              require mem[260] * m_param3 / m_param3 == mem[260]
                              require 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                              mem[ceil32(return_data.size) + 229] = mem[260]
                              return mem[ceil32(return_data.size) + 229], 
                                     10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                     [94m_453 * m_param3 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + mstor7m[addr(m_param1)m]m.field_0 + 18)
                          require ext_code.size(m_param2)
                          static call m_param2.decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 32
                          if ext_call.return_data[31 len 1] < mstor7m[addr(m_param1)m]m.field_0:
                              if mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18 >= 18:
                                  if not m_param3:
                                      if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                          return mem[260], 
                                                 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                 0 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                                  else:
                                      if mem[260] * m_param3 / m_param3 == mem[260]:
                                          if 10^(mstor7m[addr(m_param1)m]m.field_0 + -ext_call.return_data[31 len 1] + 18):
                                              return mem[260], 
                                                     10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                     mem[260] * m_param3 / 10^(mstor7m[addr(m_param1)m]m.field_0 + -uint8(ext_call.return_data[0]) + 18)
                          else:
                              if ext_call.return_data[31 len 1] - mstor7m[addr(m_param1)m]m.field_0 <= 18:
                                  if not m_param3:
                                      if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                          return mem[260], 
                                                 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                 0 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                                  else:
                                      if mem[260] * m_param3 / m_param3 == mem[260]:
                                          if 10^(-ext_call.return_data[31 len 1] + mstor7m[addr(m_param1)m]m.field_0 + 18):
                                              return mem[260], 
                                                     10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18),
                                                     mem[260] * m_param3 / 10^(-uint8(ext_call.return_data[0]) + mstor7m[addr(m_param1)m]m.field_0 + 18)
                      else:
                          require ext_code.size(m_param1)
                          static call m_param1.decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 32
                          if mstor7m[addr(m_param2)m]m.field_0:
                              if mstor7m[addr(m_param2)m]m.field_0 < ext_call.return_data[31 len 1]:
                                  if ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18 >= 18:
                                      if not m_param3:
                                          if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                              return mem[260], 
                                                     10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                     0 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                                      else:
                                          if mem[260] * m_param3 / m_param3 == mem[260]:
                                              if 10^(ext_call.return_data[31 len 1] + -mstor7m[addr(m_param2)m]m.field_0 + 18):
                                                  return mem[260], 
                                                         10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18),
                                                         mem[260] * m_param3 / 10^(uint8(ext_call.return_data[0]) + -mstor7m[addr(m_param2)m]m.field_0 + 18)
                              else:
                                  if mstor7m[addr(m_param2)m]m.field_0 - ext_call.return_data[31 len 1] <= 18:
                                      if not m_param3:
                                          if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                              return mem[260], 
                                                     10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                     0 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                                      else:
                                          if mem[260] * m_param3 / m_param3 == mem[260]:
                                              if 10^(-mstor7m[addr(m_param2)m]m.field_0 + ext_call.return_data[31 len 1] + 18):
                                                  return mem[260], 
                                                         10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18),
                                                         mem[260] * m_param3 / 10^(-mstor7m[addr(m_param2)m]m.field_0 + uint8(ext_call.return_data[0]) + 18)
                          else:
                              require ext_code.size(m_param2)
                              static call m_param2.decimals() with:
                                      gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 32
                              if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                                  if uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18:
                                      if not m_param3:
                                          if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                              return mem[260], 10^18, 0 / 10^18
                                      else:
                                          if mem[260] * m_param3 / m_param3 == mem[260]:
                                              if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                                  return mem[260], 10^18, mem[260] * m_param3 / 10^18
                              else:
                                  if ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18:
                                      if not m_param3:
                                          if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                              return mem[260], 10^18, 0 / 10^18
                                      else:
                                          if mem[260] * m_param3 / m_param3 == mem[260]:
                                              if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                                  return mem[260], 10^18, mem[260] * m_param3 / 10^18
  revert


# hash = 0x18ddd6a8
# getter = None
# const = None
# payable = False
def unknown18ddd6a8(): # not payable
  require calldata.size - 4 >=′ 736
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 1


# hash = 0x2274346b
# getter = ['storage', 160, 0, 18]
# const = None
# payable = False
def vaultContract(): # not payable
  return mvaultContractAddress


# hash = 0x26e010c8
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def minInitialMarginAmount(): # not payable
  return mminInitialMarginAmount


# hash = 0x2aed1390
# getter = ['storage', 160, 0, 19]
# const = None
# payable = False
def kyberContract(): # not payable
  return mkyberContractAddress


# hash = 0x2c9f6792
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def emaPeriods(): # not payable
  return memaPeriods


# hash = 0x33ac22b4
# getter = None
# const = None
# payable = False
def unknown33ac22b4(): # not payable
  require calldata.size - 4 >=′ 736
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 1


# hash = 0x34752a34
# getter = None
# const = None
# payable = False
def unknown34752a34(): # not payable
  require calldata.size - 4 >=′ 448
  require calldata.size - 4 >=′ 320
  require cd[324] <= 18446744073709551615
  require calldata.size + -cd[324] - 4 >=′ 320
  require m('cd', 324)[8] <= 18446744073709551615
  require calldata.size >′ cd[324] + m('cd', 324)[8] + 35
  require cd[(cd[324] + m('cd', 324)[8] + 4)] <= 18446744073709551615
  require ceil32(cd[(cd[324] + m('cd', 324)[8] + 4)]) + 768 >= 736 and ceil32(cd[(cd[324] + m('cd', 324)[8] + 4)]) + 768 <= 18446744073709551615
  require cd[324] + m('cd', 324)[8] + cd[(cd[324] + m('cd', 324)[8] + 4)] + 36 <= calldata.size
  require cd[356] <= 18446744073709551615
  require calldata.size >′ cd[356] + 35
  require m('cd', 356).length <= 18446744073709551615
  require ceil32(m('cd', 356).length) + 800 >= 768 and ceil32(cd[(cd[324] + m('cd', 324)[8] + 4)]) + ceil32(m('cd', 356).length) + 800 <= 18446744073709551615
  require cd[356] + m('cd', 356).length + 36 <= calldata.size
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  require ext_code.size(munknownf0ef5e0dAddress)
  call munknownf0ef5e0dAddress with:
       gas gas_remaining wei
      args cd[292], Array(len=m('cd', 356).length, data=call.data[cd[356] + 36 len m('cd', 356).length])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 0, 1


# hash = 0x38a56582
# getter = ['bool', ['storage', 8, 8, 15]]
# const = None
# payable = False
def unknown38a56582(): # not payable
  return bool(munknown38a56582)


# hash = 0x3913c2fd
# getter = None
# const = None
# payable = False
def unknown3913c2fd(addr m_param1, addr m_param2, uint256 m_param3): # not payable
  require calldata.size - 4 >=′ 416
  require calldata.size - 4 >=′ 320
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if not m_param3:
      require 0 <= m_param3
      require ext_code.size(m_param1)
      call m_param1.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(m_param2), m_param3
  else:
      require minterestFeePercent * m_param3 / m_param3 == minterestFeePercent
      require minterestFeePercent * m_param3 / 100 * 10^18 <= m_param3
      require ext_code.size(m_param1)
      call m_param1.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(m_param2), m_param3 - (minterestFeePercent * m_param3 / 100 * 10^18)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if return_data.size:
      require return_data.size == 32
      if not ext_call.return_data[0]:
          revert with 0, 'eip20Transfer failed'
  return 1


# hash = 0x41ce9f0e
# getter = None
# const = None
# payable = False
def setBZRxTokenContractAddress(address m_newAddress): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require mbZRxTokenContractAddress != m_newAddress
  require m_newAddress
  mbZRxTokenContractAddress = m_newAddress


# hash = 0x4780eac1
# getter = ['storage', 160, 0, 21]
# const = None
# payable = False
def wethContract(): # not payable
  return mwethContractAddress


# hash = 0x4a00709d
# getter = None
# const = None
# payable = False
def unknown4a00709d(addr m_param1): # not payable
  require calldata.size - 4 >=′ 32
  require ext_code.size(m_param1)
  static call m_param1.decimals() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  mstor7m[addr(m_param1)m]m.field_0 = ext_call.return_data[31 len 1]
  mstor7m[addr(m_param1)m]m.field_8 = 0


# hash = 0x4eb60611
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def unknown4eb60611(): # not payable
  return munknown4eb60611


# hash = 0x4f61ff8b
# getter = ['storage', 160, 0, 20]
# const = None
# payable = False
def kyberNetworkContract(): # not payable
  return mkyberNetworkContractAddress


# hash = 0x5a1e921b
# getter = None
# const = None
# payable = False
def isTradeSupported(address m_sourceTokenAddress, address m_destTokenAddress, uint256 m_sourceTokenAmount): # not payable
  require calldata.size - 4 >=′ 96
  if m_sourceTokenAddress != m_destTokenAddress:
      if not munknown035ab37f:
          mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_sourceTokenAddress) << 64, 0, addr(m_destTokenAddress), Mask(224, 32, m_sourceTokenAmount) >> 32
          static call mkyberContractAddress with:
                  gas gas_remaining wei
                 args Mask(224, 32, m_sourceTokenAmount) << 480, mem[324 len 4]
      else:
          require m_sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000 >= m_sourceTokenAmount
          mem[228 len 96] = getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_sourceTokenAddress) << 64, 0, addr(m_destTokenAddress), Mask(224, 32, m_sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000) >> 32
          static call mkyberContractAddress with:
                  gas gas_remaining wei
                 args Mask(224, 32, m_sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000) << 480, mem[324 len 4]
      if not return_data.size:
          if not ext_call.success:
              return 0
          if getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue), addr(m_sourceTokenAddress) << 64 <= 0:
              return 0
          if m_sourceTokenAmount:
              if 0, addr(m_destTokenAddress) << 64 <= 0:
                  return 0
      else:
          mem[260 len return_data.size] = ext_call.return_data[0 len return_data.size]
          if not ext_call.success:
              return 0
          if mem[260] <= 0:
              return 0
          if m_sourceTokenAmount:
              if mem[292] <= 0:
                  return 0
  return 1


# hash = 0x5bdf0751
# getter = None
# const = None
# payable = False
def unknown5bdf0751(): # not payable
  require calldata.size - 4 >=′ 416
  require calldata.size - 4 >=′ 320
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 1


# hash = 0x5e19a6eb
# getter = None
# const = None
# payable = False
def unknown5e19a6eb(): # not payable
  require calldata.size - 4 >=′ 32
  require cd[4] <= 18446744073709551615
  require calldata.size >′ cd[4] + 35
  require m('cd', 4).length <= 18446744073709551615
  require (32 * m('cd', 4).length) + 128 >= 96 and (32 * m('cd', 4).length) + 128 <= 18446744073709551615
  mem[64] = (32 * m('cd', 4).length) + 128
  mem[96] = m('cd', 4).length
  require cd[4] + (32 * m('cd', 4).length) + 36 <= calldata.size
  [94midx = 0
  [94ms = cd[4] + 36
  [94mt = 128
  mwhile [94midx < m('cd', 4).lengthm:
      mem[[94mt] = addr(cd[[94ms])
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      mcontinue 
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
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
      mem[32] = 7
      mstor7m[mem[(32 * [94midx) + 140 len 20]m]m.field_0 = uint8([94m_28)
      mstor7m[mem[(32 * [94midx) + 140 len 20]m]m.field_8 = 0
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x63621532
# getter = None
# const = None
# payable = False
def unknown63621532(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require m_param1 != munknowncc11a3b6
  munknowncc11a3b6 = m_param1


# hash = 0x6f0231bd
# getter = None
# const = None
# payable = False
def unknown6f0231bd(): # not payable
  require calldata.size - 4 >=′ 480
  require calldata.size - 4 >=′ 320
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 1


# hash = 0x6f1296d2
# getter = None
# const = None
# payable = False
def wrapEther(): # not payable
  require caller == mowner
  if eth.balance(this.address) > 0:
      require ext_code.size(mwethContractAddress)
      call mwethContractAddress.deposit() with:
         value eth.balance(this.address) wei
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0x72e98a79
# getter = None
# const = None
# payable = False
def transferBZxOwnership(address m_newBZxContractAddress): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  if not m_newBZxContractAddress:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'transferBZxOwnership::unauthorized'
  if mowner == m_newBZxContractAddress:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'transferBZxOwnership::unauthorized'
  log BZxOwnershipTransferred(
        address previousBZxContract=bZxContractAddress,
        address newBZxContract=_newBZxContractAddress)
  mbZxContractAddress = m_newBZxContractAddress


# hash = 0x754efc98
# getter = ['bool', ['storage', 8, 0, 4]]
# const = None
# payable = False
def throwOnGasRefundFail(): # not payable
  return bool(mthrowOnGasRefundFail)


# hash = 0x760c8859
# getter = None
# const = None
# payable = False
def unknown760c8859(): # not payable
  require caller == mowner
  require ext_code.size(mkyberContractAddress)
  static call mkyberContractAddress.kyberNetworkContract() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  mkyberNetworkContractAddress = ext_call.return_data[12 len 20]


# hash = 0x7724d39a
# getter = None
# const = None
# payable = False
def unknown7724d39a(): # not payable
  require calldata.size - 4 >=′ 704
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 1


# hash = 0x779dec5b
# getter = ['storage', 160, 0, 22]
# const = None
# payable = False
def bZRxTokenContract(): # not payable
  return mbZRxTokenContractAddress


# hash = 0x783882be
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def unknown783882be(): # not payable
  return munknown783882be


# hash = 0x787f7fca
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknown787f7fca(): # not payable
  return munknown787f7fca


# hash = 0x7ca7cbc1
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknown7ca7cbc1(): # not payable
  return munknown7ca7cbc1


# hash = 0x7d0cdec3
# getter = None
# const = None
# payable = False
def unknown7d0cdec3(): # not payable
  require calldata.size - 4 >=′ 736
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 1


# hash = 0x8605c97e
# getter = None
# const = None
# payable = False
def setMarginThresholds(uint256 m_newInitialMargin, uint256 m_newMaintenanceMargin): # not payable
  require calldata.size - 4 >=′ 64
  require caller == mowner
  require m_newInitialMargin >= m_newMaintenanceMargin
  mminInitialMarginAmount = m_newInitialMargin
  mminMaintenanceMarginAmount = m_newMaintenanceMargin


# hash = 0x871105cc
# getter = None
# const = None
# payable = False
def setVaultContractAddress(address m_newAddress): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require mvaultContractAddress != m_newAddress
  require m_newAddress
  mvaultContractAddress = m_newAddress


# hash = 0x8c9f7074
# getter = None
# const = None
# payable = False
def setInterestFeePercent(uint256 m_newRate): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require m_newRate != minterestFeePercent
  require m_newRate <= 100 * 10^18
  minterestFeePercent = m_newRate


# hash = 0x8da5cb5b
# getter = ['storage', 160, 8, 4]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x903509d6
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def unknown903509d6(): # not payable
  return munknown903509d6


# hash = 0x9a2c2864
# getter = None
# const = None
# payable = False
def unknown9a2c2864(): # not payable
  require calldata.size - 4 >=′ 704
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 1


# hash = 0xa48205cb
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def emaValue(): # not payable
  return memaValue


# hash = 0xa9ada2bd
# getter = None
# const = None
# payable = False
def unknowna9ada2bd(uint256 m_param1, bool m_param2): # not payable
  require calldata.size - 4 >=′ 64
  require caller == mowner
  if m_param1 != munknown4eb60611:
      munknown4eb60611 = m_param1
  if m_param2 != bool(munknownf0ad0b7f):
      munknownf0ad0b7f = uint8(m_param2)


# hash = 0xaae71452
# getter = None
# const = None
# payable = False
def unknownaae71452(): # not payable
  require calldata.size - 4 >=′ 768
  require calldata.size - 4 >=′ 320
  require cd[324] <= 18446744073709551615
  require calldata.size + -cd[324] - 4 >=′ 320
  require m('cd', 324)[8] <= 18446744073709551615
  require calldata.size >′ cd[324] + m('cd', 324)[8] + 35
  require cd[(cd[324] + m('cd', 324)[8] + 4)] <= 18446744073709551615
  require ceil32(cd[(cd[324] + m('cd', 324)[8] + 4)]) + 768 >= 736 and ceil32(cd[(cd[324] + m('cd', 324)[8] + 4)]) + 768 <= 18446744073709551615
  require cd[324] + m('cd', 324)[8] + cd[(cd[324] + m('cd', 324)[8] + 4)] + 36 <= calldata.size
  require calldata.size - 356 >=′ 352
  require bool(ceil32(cd[(cd[324] + m('cd', 324)[8] + 4)]) + 1120 <= 18446744073709551615)
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 1


# hash = 0xaf2bf027
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def minMaintenanceMarginAmount(): # not payable
  return mminMaintenanceMarginAmount


# hash = 0xb36b72df
# getter = None
# const = None
# payable = False
def unknownb36b72df(addr m_param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require munknownf0ef5e0dAddress != m_param1
  require m_param1
  munknownf0ef5e0dAddress = m_param1


# hash = 0xb6517727
# getter = None
# const = None
# payable = False
def unknownb6517727(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require m_param1 != munknownf481e71b
  require m_param1 <= 100 * 10^18
  munknownf481e71b = m_param1


# hash = 0xb7a6711c
# getter = None
# const = None
# payable = False
def unknownb7a6711c(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require m_param1 != munknown787f7fca
  munknown787f7fca = m_param1


# hash = 0xcc11a3b6
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknowncc11a3b6(): # not payable
  return munknowncc11a3b6


# hash = 0xcc677679
# getter = None
# const = None
# payable = False
def setEMAPeriods(uint256 m_newEMAPeriods): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require m_newEMAPeriods > 1
  require m_newEMAPeriods != memaPeriods
  memaPeriods = m_newEMAPeriods


# hash = 0xd28a4f9e
# getter = None
# const = None
# payable = False
def setKyberContractAddress(address m_newAddress): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require mkyberContractAddress != m_newAddress
  require m_newAddress
  mkyberContractAddress = m_newAddress


# hash = 0xd294f093
# getter = None
# const = None
# payable = False
def claimFees(): # not payable
  mem[96] = 0x902f1ac00000000000000000000000000000000000000000000000000000000
  require ext_code.size(mkyberNetworkContractAddress)
  static call mkyberNetworkContractAddress.getReserves() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >=′ 32
  [94m_4 = mem[96]
  require mem[96] <= 18446744073709551615
  require return_data.size + 96 >′ mem[96] + 127
  [94m_5 = mem[mem[96] + 96]
  require mem[mem[96] + 96] <= 18446744073709551615
  require (32 * mem[mem[96] + 96]) + 32 >= 0 and ceil32(return_data.size) + (32 * mem[mem[96] + 96]) + 128 <= 18446744073709551615
  mem[64] = ceil32(return_data.size) + (32 * mem[mem[96] + 96]) + 128
  mem[ceil32(return_data.size) + 96] = [94m_5
  require [94m_4 + (32 * [94m_5) + 32 <= return_data.size
  [94midx = 0
  [94ms = [94m_4 + 128
  [94mt = ceil32(return_data.size) + 128
  mwhile [94midx < [94m_5m:
      mem[[94mt] = mem[[94ms + 12 len 20]
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      mcontinue 
  require ext_code.size(mkyberNetworkContractAddress)
  static call mkyberNetworkContractAddress.feeBurnerContract() with:
          gas gas_remaining wei
  mem[mem[64]] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  [94m_32 = mem[64]
  mem[64] = mem[64] + ceil32(return_data.size)
  require return_data.size >=′ 32
  [94m_33 = mem[[94m_32]
  [94midx = 0
  mwhile [94midx < [94m_5m:
      require [94midx < mem[ceil32(return_data.size) + 96]
      [94m_53 = mem[(32 * [94midx) + ceil32(return_data.size) + 128]
      [94m_54 = mem[64]
      mem[mem[64] + 36] = this.address
      mem[mem[64] + 68] = addr([94m_53)
      [94m_55 = mem[64]
      mem[mem[64]] = 68
      mem[64] = mem[64] + 100
      mem[[94m_55 + 32] = 0xdd3ff4f600000000000000000000000000000000000000000000000000000000 or mem[[94m_55 + 36 len 28]
      [94m_58 = mem[[94m_55]
      [94mt = [94m_55 + 32
      [94mu = [94m_54 + 100
      [94ms = mem[[94m_55]
      mwhile [94ms >= 32m:
          mem[[94mu] = mem[[94mt]
          [94mt = [94mt + 32
          [94mu = [94mu + 32
          [94ms = [94ms - 32
          mcontinue 
      mem[[94m_54 + floor32(mem[[94m_55]) + 100] = mem[[94m_55 + -(mem[[94m_55] % 32) + floor32(mem[[94m_55]) + 64 len mem[[94m_55] % 32] or Mask(8 * -(mem[[94m_55] % 32) + 32, -(8 * -(mem[[94m_55] % 32) + 32) + 256, mem[[94m_54 + floor32(mem[[94m_55]) + 100])
      call addr([94m_33).mem[[94m_54 + 100 len 4] with:
           gas gas_remaining wei
          args mem[[94m_54 + 104 len [94m_58 - 4]
      if return_data.size:
          mem[64] = [94m_54 + ceil32(return_data.size) + 101
          mem[[94m_54 + 100] = return_data.size
          mem[[94m_54 + 132 len return_data.size] = ext_call.return_data[0 len return_data.size]
      if not ext_call.success:
          revert with 0, 'sendFeeToWallet failed'
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xd5a60129
# getter = None
# const = None
# payable = False
def unknownd5a60129(bool m_param1, bool m_param2): # not payable
  require calldata.size - 4 >=′ 64
  require caller == mowner
  munknown035ab37f = uint8(m_param1)
  Mask(248, 0, mstor15m.field_8) = Mask(248, 0, m_param2)
  Mask(240, 0, mstor15m.field_16) = Mask(240, 16, m_param1) >> 16


# hash = 0xdaebc33e
# getter = None
# const = None
# payable = False
def unknowndaebc33e(addr m_param1, addr m_param2, uint256 m_param3): # not payable
  require calldata.size - 4 >=′ 128
  if mbZxContractAddress != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'only bZx contracts can call this function'
  if not m_param3:
      require 0 <= m_param3
      require ext_code.size(m_param2)
      call m_param2.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(m_param1), m_param3
  else:
      require minterestFeePercent * m_param3 / m_param3 == minterestFeePercent
      require minterestFeePercent * m_param3 / 100 * 10^18 <= m_param3
      require ext_code.size(m_param2)
      call m_param2.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(m_param1), m_param3 - (minterestFeePercent * m_param3 / 100 * 10^18)
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
def unknowne2506eab(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require m_param1 != memaValue
  memaValue = m_param1


# hash = 0xe4a72b13
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def bZxContractAddress(): # not payable
  return mbZxContractAddress


# hash = 0xef8d2a40
# getter = None
# const = None
# payable = False
def unknownef8d2a40(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require m_param1 != munknown783882be
  munknown783882be = m_param1


# hash = 0xf0ad0b7f
# getter = ['bool', ['storage', 8, 0, 9]]
# const = None
# payable = False
def unknownf0ad0b7f(): # not payable
  return bool(munknownf0ad0b7f)


# hash = 0xf0ef5e0d
# getter = ['storage', 160, 0, 23]
# const = None
# payable = False
def unknownf0ef5e0d(): # not payable
  return munknownf0ef5e0dAddress


# hash = 0xf1cf5b38
# getter = None
# const = None
# payable = False
def setWethContractAddress(address m_newAddress): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require mwethContractAddress != m_newAddress
  require m_newAddress
  mwethContractAddress = m_newAddress


# hash = 0xf2a2583a
# getter = None
# const = None
# payable = False
def unknownf2a2583a(): # not payable
  require calldata.size - 4 >=′ 736
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 1


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >=′ 32
  require caller == mowner
  if not m_newOwner:
      revert with 0, 'transferOwnership::unauthorized'
  if mbZxContractAddress == m_newOwner:
      revert with 0, 'transferOwnership::unauthorized'
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf481e71b
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknownf481e71b(): # not payable
  return munknownf481e71b


# hash = 0xf5537ede
# getter = None
# const = None
# payable = False
def transferToken(address m_token, address m_to, uint256 m_val): # not payable
  require calldata.size - 4 >=′ 96
  require caller == mowner
  require ext_code.size(m_token)
  static call m_token.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  require ext_code.size(m_token)
  if m_val <= ext_call.return_data[0]:
      call m_token.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(m_to), m_val
  else:
      call m_token.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(m_to), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  return bool(ext_call.return_data[0])


# hash = 0xfbb7f232
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 24]]]
# const = None
# payable = False
def unknownfbb7f232(uint256 m_param1): # not payable
  require calldata.size - 4 >=′ 32
  return munknownfbb7f232m[m_param1m]


# hash = 0xfd670cbd
# getter = None
# const = None
# payable = False
def unknownfd670cbd(): # not payable
  require calldata.size - 4 >=′ 736
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if mbZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if block.gasprice <= memaValue:
      require memaPeriods + 1
      require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
      require memaPeriods + 1
      require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
      memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  else:
      if not munknown903509d6:
          require munknown7ca7cbc1 >= 0
          if block.gasprice < munknown7ca7cbc1:
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
      else:
          require memaValue * munknown903509d6 / munknown903509d6 == memaValue
          require munknown7ca7cbc1 + (memaValue * munknown903509d6) >= memaValue * munknown903509d6
          if block.gasprice < munknown7ca7cbc1 + (memaValue * munknown903509d6):
              require memaPeriods + 1
              require memaValue + (2 * block.gasprice / memaPeriods + 1) >= 2 * block.gasprice / memaPeriods + 1
              require memaPeriods + 1
              require 2 * memaValue / memaPeriods + 1 <= memaValue + (2 * block.gasprice / memaPeriods + 1)
              memaValue = memaValue + (2 * block.gasprice / memaPeriods + 1) - (2 * memaValue / memaPeriods + 1)
  return 1


# hash = 0xfe8925f4
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def interestFeePercent(): # not payable
  return minterestFeePercent


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


