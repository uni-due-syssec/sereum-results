# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xF257246627f7CB036AE40Aa6cFe8D8CE5F0EbA63 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x00432cf3': 'getCurrentMarginAmount(address _loanTokenAddress, address _positionTokenAddress, address _collateralTokenAddress, uint256 _loanTokenAmount, uint256 _positionTokenAmount, uint256 _collateralTokenAmount)', '0x016d7c64': 'unknown016d7c64(?)', '0x051c8a8d': 'unknown051c8a8d(?)', '0x369308ce': 'unknown369308ce(?)', '0x3913c2fd': 'unknown3913c2fd(?)', '0x4849b6c8': 'unknown4849b6c8(?)', '0x4e8440a5': 'unknown4e8440a5(?)', '0x5e3f4b3c': 'unknown5e3f4b3c(?)', '0x89611678': 'unknown89611678(?)', '0xc3feec61': 'unknownc3feec61(?)', '0xdaebc33e': 'unknowndaebc33e(?)', '0xff8a2640': 'unknownff8a2640(?)'} 

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
    unknownc21c8972 # mask: a s
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


# hash = 0x05f23196
# getter = None
# const = None
# payable = False
def unknown05f23196(bool _param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _param1 != bool(unknownc21c8972)
  unknownc21c8972 = uint8(_param1)


# hash = 0x06599aa0
# getter = None
# const = None
# payable = False
def unknown06599aa0(addr _param1, addr _param2, uint256 _param3): # not payable
  require calldata.size - 4 >=′ 96
  if _param1 == _param2:
      if not _param3:
          return 10^18, 10^18, 0
      if 10^18 * _param3 / _param3 == 10^18:
          return 10^18, 10^18, 10^18 * _param3 / 10^18
  else:
      if not unknownc21c8972:
          require ext_code.size(kyberContractAddress)
          static call kyberContractAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
                  gas gas_remaining wei
                 args addr(_param1), addr(_param2), _param3
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 64
          if _param1 == _param2:
              if not _param3:
                  return ext_call.return_data[0], 10^18, 0
              if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                  return ext_call.return_data[0], 10^18, ext_call.return_data[0] * _param3 / 10^18
          else:
              if stor7[addr(_param1)].field_0:
                  if stor7[addr(_param2)].field_0:
                      if stor7[addr(_param2)].field_0 < stor7[addr(_param1)].field_0:
                          if stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18 >= 18:
                              if not _param3:
                                  if 10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18):
                                      return ext_call.return_data[0], 
                                             10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18),
                                             0 / 10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18)
                              else:
                                  if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                      if 10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18):
                                          return ext_call.return_data[0], 
                                                 10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18),
                                                 ext_call.return_data[0] * _param3 / 10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18)
                      else:
                          if stor7[addr(_param2)].field_0 - stor7[addr(_param1)].field_0 <= 18:
                              if not _param3:
                                  if 10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18):
                                      return ext_call.return_data[0], 
                                             10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18),
                                             0 / 10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18)
                              else:
                                  if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                      if 10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18):
                                          return ext_call.return_data[0], 
                                                 10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18),
                                                 ext_call.return_data[0] * _param3 / 10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18)
                  else:
                      require ext_code.size(_param2)
                      static call _param2.decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 32
                      if ext_call.return_data[31 len 1] < stor7[addr(_param1)].field_0:
                          if stor7[addr(_param1)].field_0 + -ext_call.return_data[31 len 1] + 18 >= 18:
                              if not _param3:
                                  if 10^(stor7[addr(_param1)].field_0 + -ext_call.return_data[31 len 1] + 18):
                                      return ext_call.return_data[0], 
                                             10^(stor7[addr(_param1)].field_0 + -uint8(ext_call.return_data[0]) + 18),
                                             0 / 10^(stor7[addr(_param1)].field_0 + -uint8(ext_call.return_data[0]) + 18)
                              else:
                                  if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                      if 10^(stor7[addr(_param1)].field_0 + -ext_call.return_data[31 len 1] + 18):
                                          return ext_call.return_data[0], 
                                                 10^(stor7[addr(_param1)].field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                 ext_call.return_data[0] * _param3 / 10^(stor7[addr(_param1)].field_0 + -uint8(ext_call.return_data[0]) + 18)
                      else:
                          if ext_call.return_data[31 len 1] - stor7[addr(_param1)].field_0 <= 18:
                              if not _param3:
                                  if 10^(-ext_call.return_data[31 len 1] + stor7[addr(_param1)].field_0 + 18):
                                      return ext_call.return_data[0], 
                                             10^(-uint8(ext_call.return_data[0]) + stor7[addr(_param1)].field_0 + 18),
                                             0 / 10^(-uint8(ext_call.return_data[0]) + stor7[addr(_param1)].field_0 + 18)
                              else:
                                  if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                      if 10^(-ext_call.return_data[31 len 1] + stor7[addr(_param1)].field_0 + 18):
                                          return ext_call.return_data[0], 
                                                 10^(-uint8(ext_call.return_data[0]) + stor7[addr(_param1)].field_0 + 18),
                                                 ext_call.return_data[0] * _param3 / 10^(-uint8(ext_call.return_data[0]) + stor7[addr(_param1)].field_0 + 18)
              else:
                  require ext_code.size(_param1)
                  static call _param1.decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >=′ 32
                  if stor7[addr(_param2)].field_0:
                      if stor7[addr(_param2)].field_0 < ext_call.return_data[31 len 1]:
                          if ext_call.return_data[31 len 1] + -stor7[addr(_param2)].field_0 + 18 >= 18:
                              if not _param3:
                                  if 10^(ext_call.return_data[31 len 1] + -stor7[addr(_param2)].field_0 + 18):
                                      return ext_call.return_data[0], 
                                             10^(uint8(ext_call.return_data[0]) + -stor7[addr(_param2)].field_0 + 18),
                                             0 / 10^(uint8(ext_call.return_data[0]) + -stor7[addr(_param2)].field_0 + 18)
                              else:
                                  if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                      if 10^(ext_call.return_data[31 len 1] + -stor7[addr(_param2)].field_0 + 18):
                                          return ext_call.return_data[0], 
                                                 10^(uint8(ext_call.return_data[0]) + -stor7[addr(_param2)].field_0 + 18),
                                                 ext_call.return_data[0] * _param3 / 10^(uint8(ext_call.return_data[0]) + -stor7[addr(_param2)].field_0 + 18)
                      else:
                          if stor7[addr(_param2)].field_0 - ext_call.return_data[31 len 1] <= 18:
                              if not _param3:
                                  if 10^(-stor7[addr(_param2)].field_0 + ext_call.return_data[31 len 1] + 18):
                                      return ext_call.return_data[0], 
                                             10^(-stor7[addr(_param2)].field_0 + uint8(ext_call.return_data[0]) + 18),
                                             0 / 10^(-stor7[addr(_param2)].field_0 + uint8(ext_call.return_data[0]) + 18)
                              else:
                                  if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                      if 10^(-stor7[addr(_param2)].field_0 + ext_call.return_data[31 len 1] + 18):
                                          return ext_call.return_data[0], 
                                                 10^(-stor7[addr(_param2)].field_0 + uint8(ext_call.return_data[0]) + 18),
                                                 ext_call.return_data[0] * _param3 / 10^(-stor7[addr(_param2)].field_0 + uint8(ext_call.return_data[0]) + 18)
                  else:
                      require ext_code.size(_param2)
                      static call _param2.decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 32
                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                          if uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18:
                              if not _param3:
                                  if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                      return ext_call.return_data[0], 10^18, 0 / 10^18
                              else:
                                  if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                      if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                          return ext_call.return_data[0], 10^18, ext_call.return_data[0] * _param3 / 10^18
                      else:
                          if ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18:
                              if not _param3:
                                  if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                      return ext_call.return_data[0], 10^18, 0 / 10^18
                              else:
                                  if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                      if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                          return ext_call.return_data[0], 10^18, ext_call.return_data[0] * _param3 / 10^18
      else:
          if _param3 - 0x8000000000000000000000000000000000000000000000000000000000000000 >= _param3:
              require ext_code.size(kyberContractAddress)
              static call kyberContractAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
                      gas gas_remaining wei
                     args addr(_param1), addr(_param2), _param3 - 0x8000000000000000000000000000000000000000000000000000000000000000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 64
              if _param1 == _param2:
                  if not _param3:
                      return ext_call.return_data[0], 10^18, 0
                  if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                      return ext_call.return_data[0], 10^18, ext_call.return_data[0] * _param3 / 10^18
              else:
                  if stor7[addr(_param1)].field_0:
                      if stor7[addr(_param2)].field_0:
                          if stor7[addr(_param2)].field_0 < stor7[addr(_param1)].field_0:
                              if stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18 >= 18:
                                  if not _param3:
                                      if 10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18):
                                          return ext_call.return_data[0], 
                                                 10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18),
                                                 0 / 10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18)
                                  else:
                                      if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                          if 10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18):
                                              return ext_call.return_data[0], 
                                                     10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18),
                                                     ext_call.return_data[0] * _param3 / 10^(stor7[addr(_param1)].field_0 + -stor7[addr(_param2)].field_0 + 18)
                          else:
                              if stor7[addr(_param2)].field_0 - stor7[addr(_param1)].field_0 <= 18:
                                  if not _param3:
                                      if 10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18):
                                          return ext_call.return_data[0], 
                                                 10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18),
                                                 0 / 10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18)
                                  else:
                                      if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                          if 10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18):
                                              return ext_call.return_data[0], 
                                                     10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18),
                                                     ext_call.return_data[0] * _param3 / 10^(-stor7[addr(_param2)].field_0 + stor7[addr(_param1)].field_0 + 18)
                      else:
                          require ext_code.size(_param2)
                          static call _param2.decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 32
                          if ext_call.return_data[31 len 1] < stor7[addr(_param1)].field_0:
                              if stor7[addr(_param1)].field_0 + -ext_call.return_data[31 len 1] + 18 >= 18:
                                  if not _param3:
                                      if 10^(stor7[addr(_param1)].field_0 + -ext_call.return_data[31 len 1] + 18):
                                          return ext_call.return_data[0], 
                                                 10^(stor7[addr(_param1)].field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                 0 / 10^(stor7[addr(_param1)].field_0 + -uint8(ext_call.return_data[0]) + 18)
                                  else:
                                      if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                          if 10^(stor7[addr(_param1)].field_0 + -ext_call.return_data[31 len 1] + 18):
                                              return ext_call.return_data[0], 
                                                     10^(stor7[addr(_param1)].field_0 + -uint8(ext_call.return_data[0]) + 18),
                                                     ext_call.return_data[0] * _param3 / 10^(stor7[addr(_param1)].field_0 + -uint8(ext_call.return_data[0]) + 18)
                          else:
                              if ext_call.return_data[31 len 1] - stor7[addr(_param1)].field_0 <= 18:
                                  if not _param3:
                                      if 10^(-ext_call.return_data[31 len 1] + stor7[addr(_param1)].field_0 + 18):
                                          return ext_call.return_data[0], 
                                                 10^(-uint8(ext_call.return_data[0]) + stor7[addr(_param1)].field_0 + 18),
                                                 0 / 10^(-uint8(ext_call.return_data[0]) + stor7[addr(_param1)].field_0 + 18)
                                  else:
                                      if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                          if 10^(-ext_call.return_data[31 len 1] + stor7[addr(_param1)].field_0 + 18):
                                              return ext_call.return_data[0], 
                                                     10^(-uint8(ext_call.return_data[0]) + stor7[addr(_param1)].field_0 + 18),
                                                     ext_call.return_data[0] * _param3 / 10^(-uint8(ext_call.return_data[0]) + stor7[addr(_param1)].field_0 + 18)
                  else:
                      require ext_code.size(_param1)
                      static call _param1.decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 32
                      if stor7[addr(_param2)].field_0:
                          if stor7[addr(_param2)].field_0 < ext_call.return_data[31 len 1]:
                              if ext_call.return_data[31 len 1] + -stor7[addr(_param2)].field_0 + 18 >= 18:
                                  if not _param3:
                                      if 10^(ext_call.return_data[31 len 1] + -stor7[addr(_param2)].field_0 + 18):
                                          return ext_call.return_data[0], 
                                                 10^(uint8(ext_call.return_data[0]) + -stor7[addr(_param2)].field_0 + 18),
                                                 0 / 10^(uint8(ext_call.return_data[0]) + -stor7[addr(_param2)].field_0 + 18)
                                  else:
                                      if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                          if 10^(ext_call.return_data[31 len 1] + -stor7[addr(_param2)].field_0 + 18):
                                              return ext_call.return_data[0], 
                                                     10^(uint8(ext_call.return_data[0]) + -stor7[addr(_param2)].field_0 + 18),
                                                     ext_call.return_data[0] * _param3 / 10^(uint8(ext_call.return_data[0]) + -stor7[addr(_param2)].field_0 + 18)
                          else:
                              if stor7[addr(_param2)].field_0 - ext_call.return_data[31 len 1] <= 18:
                                  if not _param3:
                                      if 10^(-stor7[addr(_param2)].field_0 + ext_call.return_data[31 len 1] + 18):
                                          return ext_call.return_data[0], 
                                                 10^(-stor7[addr(_param2)].field_0 + uint8(ext_call.return_data[0]) + 18),
                                                 0 / 10^(-stor7[addr(_param2)].field_0 + uint8(ext_call.return_data[0]) + 18)
                                  else:
                                      if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                          if 10^(-stor7[addr(_param2)].field_0 + ext_call.return_data[31 len 1] + 18):
                                              return ext_call.return_data[0], 
                                                     10^(-stor7[addr(_param2)].field_0 + uint8(ext_call.return_data[0]) + 18),
                                                     ext_call.return_data[0] * _param3 / 10^(-stor7[addr(_param2)].field_0 + uint8(ext_call.return_data[0]) + 18)
                      else:
                          require ext_code.size(_param2)
                          static call _param2.decimals() with:
                                  gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 32
                          if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                              if uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18:
                                  if not _param3:
                                      if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                          return ext_call.return_data[0], 10^18, 0 / 10^18
                                  else:
                                      if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                          if 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18):
                                              return ext_call.return_data[0], 10^18, ext_call.return_data[0] * _param3 / 10^18
                          else:
                              if ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18:
                                  if not _param3:
                                      if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                          return ext_call.return_data[0], 10^18, 0 / 10^18
                                  else:
                                      if ext_call.return_data[0] * _param3 / _param3 == ext_call.return_data[0]:
                                          if 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18):
                                              return ext_call.return_data[0], 10^18, ext_call.return_data[0] * _param3 / 10^18
  revert


# hash = 0x18ddd6a8
# getter = None
# const = None
# payable = False
def unknown18ddd6a8(): # not payable
  require calldata.size - 4 >=′ 736
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
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


# hash = 0x2274346b
# getter = ['storage', 160, 0, 18]
# const = None
# payable = False
def vaultContract(): # not payable
  return vaultContractAddress


# hash = 0x26e010c8
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def minInitialMarginAmount(): # not payable
  return minInitialMarginAmount


# hash = 0x2aed1390
# getter = ['storage', 160, 0, 19]
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


# hash = 0x33ac22b4
# getter = None
# const = None
# payable = False
def unknown33ac22b4(): # not payable
  require calldata.size - 4 >=′ 736
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
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
# getter = ['storage', 160, 0, 21]
# const = None
# payable = False
def wethContract(): # not payable
  return wethContractAddress


# hash = 0x4a00709d
# getter = None
# const = None
# payable = False
def unknown4a00709d(addr _param1): # not payable
  require calldata.size - 4 >=′ 32
  require ext_code.size(_param1)
  static call _param1.decimals() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  stor7[addr(_param1)].field_0 = ext_call.return_data[31 len 1]
  stor7[addr(_param1)].field_8 = 0


# hash = 0x4eb60611
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def unknown4eb60611(): # not payable
  return unknown4eb60611


# hash = 0x4f61ff8b
# getter = ['storage', 160, 0, 20]
# const = None
# payable = False
def kyberNetworkContract(): # not payable
  return kyberNetworkContractAddress


# hash = 0x5a1e921b
# getter = None
# const = None
# payable = False
def isTradeSupported(address _sourceTokenAddress, address _destTokenAddress, uint256 _sourceTokenAmount): # not payable
  require calldata.size - 4 >=′ 96
  if _sourceTokenAddress != _destTokenAddress:
      if not unknownc21c8972:
          require ext_code.size(kyberContractAddress)
          static call kyberContractAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
                  gas gas_remaining wei
                 args addr(_sourceTokenAddress), addr(_destTokenAddress), _sourceTokenAmount
      else:
          require _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000 >= _sourceTokenAmount
          require ext_code.size(kyberContractAddress)
          static call kyberContractAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
                  gas gas_remaining wei
                 args addr(_sourceTokenAddress), addr(_destTokenAddress), _sourceTokenAmount - 0x8000000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 64
      if ext_call.return_data[0] <= 0:
          return 0
      if _sourceTokenAmount:
          if ext_call.return_data[32] <= 0:
              return 0
  return 1


# hash = 0x5bdf0751
# getter = None
# const = None
# payable = False
def unknown5bdf0751(): # not payable
  require calldata.size - 4 >=′ 416
  require calldata.size - 4 >=′ 320
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
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
      mem[32] = 7
      stor7[mem[(32 * [94midx) + 140 len 20]].field_0 = uint8([94m_28)
      stor7[mem[(32 * [94midx) + 140 len 20]].field_8 = 0
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


# hash = 0x6f0231bd
# getter = None
# const = None
# payable = False
def unknown6f0231bd(): # not payable
  require calldata.size - 4 >=′ 480
  require calldata.size - 4 >=′ 320
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
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


# hash = 0x6f1296d2
# getter = None
# const = None
# payable = False
def wrapEther(): # not payable
  require caller == owner
  if eth.balance(this.address) > 0:
      require ext_code.size(wethContractAddress)
      call wethContractAddress.deposit() with:
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


# hash = 0x7724d39a
# getter = None
# const = None
# payable = False
def unknown7724d39a(): # not payable
  require calldata.size - 4 >=′ 704
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
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


# hash = 0x779dec5b
# getter = ['storage', 160, 0, 22]
# const = None
# payable = False
def bZRxTokenContract(): # not payable
  return bZRxTokenContractAddress


# hash = 0x783882be
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def unknown783882be(): # not payable
  return unknown783882be


# hash = 0x787f7fca
# getter = ['storage', 256, 0, 16]
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


# hash = 0x7d0cdec3
# getter = None
# const = None
# payable = False
def unknown7d0cdec3(): # not payable
  require calldata.size - 4 >=′ 736
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
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


# hash = 0x9a2c2864
# getter = None
# const = None
# payable = False
def unknown9a2c2864(): # not payable
  require calldata.size - 4 >=′ 704
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
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


# hash = 0xaae71452
# getter = None
# const = None
# payable = False
def unknownaae71452(): # not payable
  require calldata.size - 4 >=′ 768
  require calldata.size - 4 >=′ 320
  require cd[324] <= 18446744073709551615
  require calldata.size + -cd[324] - 4 >=′ 320
  require ('cd', 324)[8] <= 18446744073709551615
  require calldata.size >′ cd[324] + ('cd', 324)[8] + 35
  require cd[(cd[324] + ('cd', 324)[8] + 4)] <= 18446744073709551615
  require ceil32(cd[(cd[324] + ('cd', 324)[8] + 4)]) + 768 >= 736 and ceil32(cd[(cd[324] + ('cd', 324)[8] + 4)]) + 768 <= 18446744073709551615
  require cd[324] + ('cd', 324)[8] + cd[(cd[324] + ('cd', 324)[8] + 4)] + 36 <= calldata.size
  require calldata.size - 356 >=′ 352
  require bool(ceil32(cd[(cd[324] + ('cd', 324)[8] + 4)]) + 1120 <= 18446744073709551615)
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
  if wethContractAddress == addr(cd[388]):
      if unknownf0ad0b7f:
          if cd[516] < unknown4eb60611:
              revert with 0, 'collateral below minimum for BZxOracle'
      unknownfbb7f232[cd[676]] = cd[516]
  else:
      if addr(cd[388]) == wethContractAddress:
          if addr(cd[388]) == wethContractAddress:
              if not cd[516]:
                  if unknownf0ad0b7f:
                      if 0 < unknown4eb60611:
                          revert with 0, 'collateral below minimum for BZxOracle'
                  unknownfbb7f232[cd[676]] = 0
              else:
                  require 10^18 * cd[516] / cd[516] == 10^18
                  if unknownf0ad0b7f:
                      if 10^18 * cd[516] / 10^18 < unknown4eb60611:
                          revert with 0, 'collateral below minimum for BZxOracle'
                  unknownfbb7f232[cd[676]] = 10^18 * cd[516] / 10^18
          else:
              if stor7[addr(cd[388])].field_0:
                  if stor7[stor21].field_0:
                      if stor7[stor21].field_0 < stor7[addr(cd[388])].field_0:
                          require stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18 >= 18
                          if not cd[516]:
                              require 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18)
                          else:
                              require 10^18 * cd[516] / cd[516] == 10^18
                              require 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 10^18 * cd[516] / 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 10^18 * cd[516] / 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18)
                      else:
                          require stor7[stor21].field_0 - stor7[addr(cd[388])].field_0 <= 18
                          if not cd[516]:
                              require 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18)
                          else:
                              require 10^18 * cd[516] / cd[516] == 10^18
                              require 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 10^18 * cd[516] / 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 10^18 * cd[516] / 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18)
                  else:
                      require ext_code.size(wethContractAddress)
                      static call wethContractAddress.decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 32
                      if ext_call.return_data[31 len 1] < stor7[addr(cd[388])].field_0:
                          require stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18 >= 18
                          if not cd[516]:
                              require 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18)
                          else:
                              require 10^18 * cd[516] / cd[516] == 10^18
                              require 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if 10^18 * cd[516] / 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 10^18 * cd[516] / 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18)
                      else:
                          require ext_call.return_data[31 len 1] - stor7[addr(cd[388])].field_0 <= 18
                          if not cd[516]:
                              require 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18)
                          else:
                              require 10^18 * cd[516] / cd[516] == 10^18
                              require 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 10^18 * cd[516] / 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 10^18 * cd[516] / 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18)
              else:
                  require ext_code.size(addr(cd[388]))
                  static call addr(cd[388]).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >=′ 32
                  if stor7[stor21].field_0:
                      if stor7[stor21].field_0 < ext_call.return_data[31 len 1]:
                          require ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18 >= 18
                          if not cd[516]:
                              require 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18)
                          else:
                              require 10^18 * cd[516] / cd[516] == 10^18
                              require 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 10^18 * cd[516] / 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 10^18 * cd[516] / 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18)
                      else:
                          require stor7[stor21].field_0 - ext_call.return_data[31 len 1] <= 18
                          if not cd[516]:
                              require 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18)
                          else:
                              require 10^18 * cd[516] / cd[516] == 10^18
                              require 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if 10^18 * cd[516] / 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 10^18 * cd[516] / 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18)
                  else:
                      require ext_code.size(wethContractAddress)
                      static call wethContractAddress.decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 32
                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                          require uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18
                          if not cd[516]:
                              require 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18)
                          else:
                              require 10^18 * cd[516] / cd[516] == 10^18
                              require 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if 10^18 * cd[516] / 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 10^18 * cd[516] / 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18)
                      else:
                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                          if not cd[516]:
                              require 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18)
                          else:
                              require 10^18 * cd[516] / cd[516] == 10^18
                              require 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18)
                              if unknownf0ad0b7f:
                                  if 10^18 * cd[516] / 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 10^18 * cd[516] / 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18)
      else:
          if not unknownc21c8972:
              require ext_code.size(kyberContractAddress)
              static call kyberContractAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
                      gas gas_remaining wei
                     args addr(cd[388]), wethContractAddress, cd[516]
          else:
              require cd[516] - 0x8000000000000000000000000000000000000000000000000000000000000000 >= cd[516]
              require ext_code.size(kyberContractAddress)
              static call kyberContractAddress.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
                      gas gas_remaining wei
                     args addr(cd[388]), wethContractAddress, cd[516] - 0x8000000000000000000000000000000000000000000000000000000000000000
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 64
          if addr(cd[388]) == wethContractAddress:
              if not cd[516]:
                  if unknownf0ad0b7f:
                      if 0 < unknown4eb60611:
                          revert with 0, 'collateral below minimum for BZxOracle'
                  unknownfbb7f232[cd[676]] = 0
              else:
                  require ext_call.return_data[0] * cd[516] / cd[516] == ext_call.return_data[0]
                  if unknownf0ad0b7f:
                      if ext_call.return_data[0] * cd[516] / 10^18 < unknown4eb60611:
                          revert with 0, 'collateral below minimum for BZxOracle'
                  unknownfbb7f232[cd[676]] = ext_call.return_data[0] * cd[516] / 10^18
          else:
              if stor7[addr(cd[388])].field_0:
                  if stor7[stor21].field_0:
                      if stor7[stor21].field_0 < stor7[addr(cd[388])].field_0:
                          require stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18 >= 18
                          if not cd[516]:
                              require 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18)
                          else:
                              require ext_call.return_data[0] * cd[516] / cd[516] == ext_call.return_data[0]
                              require 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if ext_call.return_data[0] * cd[516] / 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = ext_call.return_data[0] * cd[516] / 10^(stor7[addr(cd[388])].field_0 + -stor7[stor21].field_0 + 18)
                      else:
                          require stor7[stor21].field_0 - stor7[addr(cd[388])].field_0 <= 18
                          if not cd[516]:
                              require 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18)
                          else:
                              require ext_call.return_data[0] * cd[516] / cd[516] == ext_call.return_data[0]
                              require 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if ext_call.return_data[0] * cd[516] / 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = ext_call.return_data[0] * cd[516] / 10^(-stor7[stor21].field_0 + stor7[addr(cd[388])].field_0 + 18)
                  else:
                      require ext_code.size(wethContractAddress)
                      static call wethContractAddress.decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 32
                      if ext_call.return_data[31 len 1] < stor7[addr(cd[388])].field_0:
                          require stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18 >= 18
                          if not cd[516]:
                              require 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18)
                          else:
                              require ext_call.return_data[0] * cd[516] / cd[516] == ext_call.return_data[0]
                              require 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if ext_call.return_data[0] * cd[516] / 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = ext_call.return_data[0] * cd[516] / 10^(stor7[addr(cd[388])].field_0 + -ext_call.return_data[31 len 1] + 18)
                      else:
                          require ext_call.return_data[31 len 1] - stor7[addr(cd[388])].field_0 <= 18
                          if not cd[516]:
                              require 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18)
                          else:
                              require ext_call.return_data[0] * cd[516] / cd[516] == ext_call.return_data[0]
                              require 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if ext_call.return_data[0] * cd[516] / 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = ext_call.return_data[0] * cd[516] / 10^(-ext_call.return_data[31 len 1] + stor7[addr(cd[388])].field_0 + 18)
              else:
                  require ext_code.size(addr(cd[388]))
                  static call addr(cd[388]).decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >=′ 32
                  if stor7[stor21].field_0:
                      if stor7[stor21].field_0 < ext_call.return_data[31 len 1]:
                          require ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18 >= 18
                          if not cd[516]:
                              require 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18)
                          else:
                              require ext_call.return_data[0] * cd[516] / cd[516] == ext_call.return_data[0]
                              require 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18)
                              if unknownf0ad0b7f:
                                  if ext_call.return_data[0] * cd[516] / 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = ext_call.return_data[0] * cd[516] / 10^(ext_call.return_data[31 len 1] + -stor7[stor21].field_0 + 18)
                      else:
                          require stor7[stor21].field_0 - ext_call.return_data[31 len 1] <= 18
                          if not cd[516]:
                              require 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18)
                          else:
                              require ext_call.return_data[0] * cd[516] / cd[516] == ext_call.return_data[0]
                              require 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if ext_call.return_data[0] * cd[516] / 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = ext_call.return_data[0] * cd[516] / 10^(-stor7[stor21].field_0 + ext_call.return_data[31 len 1] + 18)
                  else:
                      require ext_code.size(wethContractAddress)
                      static call wethContractAddress.decimals() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 32
                      if ext_call.return_data[31 len 1] < uint8(ext_call.return_data[0]):
                          require uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18 >= 18
                          if not cd[516]:
                              require 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18)
                          else:
                              require ext_call.return_data[0] * cd[516] / cd[516] == ext_call.return_data[0]
                              require 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18)
                              if unknownf0ad0b7f:
                                  if ext_call.return_data[0] * cd[516] / 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = ext_call.return_data[0] * cd[516] / 10^(uint8(ext_call.return_data[0]) + -ext_call.return_data[31 len 1] + 18)
                      else:
                          require ext_call.return_data[31 len 1] - uint8(ext_call.return_data[0]) <= 18
                          if not cd[516]:
                              require 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18)
                              if unknownf0ad0b7f:
                                  if 0 / 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = 0 / 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18)
                          else:
                              require ext_call.return_data[0] * cd[516] / cd[516] == ext_call.return_data[0]
                              require 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18)
                              if unknownf0ad0b7f:
                                  if ext_call.return_data[0] * cd[516] / 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18) < unknown4eb60611:
                                      revert with 0, 'collateral below minimum for BZxOracle'
                              unknownfbb7f232[cd[676]] = ext_call.return_data[0] * cd[516] / 10^(-ext_call.return_data[31 len 1] + uint8(ext_call.return_data[0]) + 18)
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


# hash = 0xaf2bf027
# getter = ['storage', 256, 0, 14]
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


# hash = 0xb6517727
# getter = None
# const = None
# payable = False
def unknownb6517727(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _param1 != unknownf481e71b
  require _param1 <= 100 * 10^18
  unknownf481e71b = _param1


# hash = 0xb7a6711c
# getter = None
# const = None
# payable = False
def unknownb7a6711c(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _param1 != unknown787f7fca
  unknown787f7fca = _param1


# hash = 0xc21c8972
# getter = ['bool', ['storage', 8, 0, 15]]
# const = None
# payable = False
def unknownc21c8972(): # not payable
  return bool(unknownc21c8972)


# hash = 0xcc11a3b6
# getter = ['storage', 256, 0, 12]
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


# hash = 0xd294f093
# getter = None
# const = None
# payable = False
def claimFees(): # not payable
  mem[96] = 0x902f1ac00000000000000000000000000000000000000000000000000000000
  require ext_code.size(kyberNetworkContractAddress)
  static call kyberNetworkContractAddress.getReserves() with:
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
  while [94midx < [94m_5:
      mem[[94mt] = mem[[94ms + 12 len 20]
      [94midx = [94midx + 1
      [94ms = [94ms + 32
      [94mt = [94mt + 32
      continue 
  require ext_code.size(kyberNetworkContractAddress)
  static call kyberNetworkContractAddress.feeBurnerContract() with:
          gas gas_remaining wei
  mem[mem[64]] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  [94m_32 = mem[64]
  mem[64] = mem[64] + ceil32(return_data.size)
  require return_data.size >=′ 32
  [94m_33 = mem[[94m_32]
  [94midx = 0
  while [94midx < [94m_5:
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
      while [94ms >= 32:
          mem[[94mu] = mem[[94mt]
          [94mt = [94mt + 32
          [94mu = [94mu + 32
          [94ms = [94ms - 32
          continue 
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
      continue 


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
# getter = ['bool', ['storage', 8, 0, 9]]
# const = None
# payable = False
def unknownf0ad0b7f(): # not payable
  return bool(unknownf0ad0b7f)


# hash = 0xf0ef5e0d
# getter = ['storage', 160, 0, 23]
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
  require wethContractAddress != _newAddress
  require _newAddress
  wethContractAddress = _newAddress


# hash = 0xf2a2583a
# getter = None
# const = None
# payable = False
def unknownf2a2583a(): # not payable
  require calldata.size - 4 >=′ 736
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
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


# hash = 0xf481e71b
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknownf481e71b(): # not payable
  return unknownf481e71b


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
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 24]]]
# const = None
# payable = False
def unknownfbb7f232(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  return unknownfbb7f232[_param1]


# hash = 0xfd670cbd
# getter = None
# const = None
# payable = False
def unknownfd670cbd(): # not payable
  require calldata.size - 4 >=′ 736
  require calldata.size - 4 >=′ 320
  require calldata.size - 324 >=′ 352
  if bZxContractAddress != caller:
      revert with 0, 'only bZx contracts can call this function'
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


# hash = 0xfe8925f4
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def interestFeePercent(): # not payable
  return interestFeePercent


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


