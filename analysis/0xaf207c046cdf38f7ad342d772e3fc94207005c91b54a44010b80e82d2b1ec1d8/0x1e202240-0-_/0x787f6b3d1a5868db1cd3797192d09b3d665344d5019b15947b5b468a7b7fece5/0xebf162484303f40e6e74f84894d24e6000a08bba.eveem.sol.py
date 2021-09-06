# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xEbF162484303F40e6e74f84894d24e6000A08bba 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    owner # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    bZRxTokenContractAddress # mask: a s
    # storage address 4
    bZxEtherContractAddress # mask: a s
    # storage address 5
    wethContractAddress # mask: a s
    # storage address 6
    vaultContractAddress # mask: a s
    # storage address 7
    oracleRegistryContractAddress # mask: a s
    # storage address 8
    bZxTo0xContractAddress # mask: a s
    # storage address 9
    DEBUG_MODE # mask: a s
    # storage address 9
    bZxTo0xV2ContractAddress # mask: a s
    # storage address 10
    orders
    # storage address 11
    stor11
    # storage address 12
    orderFilledAmounts
    # storage address 13
    orderCancelledAmounts
    # storage address 14
    orderLender
    # storage address 15
    loanPositions
    # storage address 16
    loanPositionsIds
    # storage address 17
    orderList
    # storage address 18
    orderListIndex
    # storage address 19
    orderPositionList
    # storage address 20
    positionList
    # storage address 21
    positionListIndex
    # storage address 22
    tokenInterestOwed
    # storage address 23
    lenderOracleInterest
    # storage address 24
    lenderOrderInterest
    # storage address 25
    traderLoanInterest
    # storage address 26
    oracle
    # storage address 27
    stor27
    # storage address 28
    stor28
    # storage address 39
    targets
    # storage address 40
    stor40
    # storage address 1227326242905548082114417476897002760953536771216552247799863072803670142175359794
    stor1227326242905548082114417476897002760953536771216552247799863072803670142175359794
    # storage address 20608571293394017686664154269169437409893635303088270681801712505759373932876682376868723
    stor20608571293394017686664154269169437409893635303088270681801712505759373932876682376868723
    # storage address 88438176167387057176243982077467603867738321418432754950529205842872764004585143215618934570316659
    stor88438176167387057176243982077467603867738321418432754950529205842872764004585143215618934570316659
    # storage address 656934418636052665012613038398210091551940171530713301052580931037275567232969908084325251790440639841023001997146602173299
    stor656934418636052665012613038398210091551940171530713301052580931037275567232969908084325251790440639841023001997146602173299
# hash = 0x093983bd
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 14]]]
# const = None
# payable = True
def orderLender(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return orderLender[_param1]


# hash = 0x0a90b578
# getter = None
# const = None
# payable = True
def unknown0a90b578(addr _param1, addr _param2, addr _param3) payable: 
  require calldata.size - 4 >=′ 96
  require lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512 <= block.timestamp
  if not block.timestamp - lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512:
      if 0 <= tokenInterestOwed[addr(_param1)][addr(_param3)]:
          if lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256 > 0:
              return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512,
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
                     0
      else:
          if lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256 > 0:
              if 0 < lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512:
                  return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
                         lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512,
                         lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
                         tokenInterestOwed[addr(_param1)][addr(_param3)]
              return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512,
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
                     0
          if 0 < lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512:
              return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
                     0,
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
                     tokenInterestOwed[addr(_param1)][addr(_param3)]
  else:
      require (block.timestamp * lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0) - (lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512 * lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0) / block.timestamp - lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512 == lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0
      if (block.timestamp * lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0) - (lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512 * lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0) / 24 * 3600 <= tokenInterestOwed[addr(_param1)][addr(_param3)]:
          if lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256 > 0:
              if 0 < lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512:
                  return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
                         lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512,
                         lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
                         (block.timestamp * lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0) - (lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512 * lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0) / 24 * 3600
              return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512,
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
                     0
          if 0 < lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512:
              return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
                     0,
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
                     (block.timestamp * lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0) - (lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512 * lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0) / 24 * 3600
      else:
          if lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256 > 0:
              if 0 < lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512:
                  return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
                         lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512,
                         lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
                         tokenInterestOwed[addr(_param1)][addr(_param3)]
              return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512,
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
                     0
          if 0 < lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_512:
              return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
                     0,
                     lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
                     tokenInterestOwed[addr(_param1)][addr(_param3)]
      ('ge', 0, ('field', 512, ('stor', ('map', ('mask_shl', 160, 0, 0, ('param', '_param3')), ('map', ('mask_shl', 160, 0, 0, ('param', '_param2')), ('map', ('mask_shl', 160, 0, 0, ('param', '_param1')), ('name', 'lenderOracleInterest', 23)))))))
  return lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_256, 
         0,
         lenderOracleInterest[addr(_param1)][addr(_param2)][addr(_param3)].field_0,
         0


# hash = 0x13e97c71
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 22]]]]]
# const = None
# payable = True
def tokenInterestOwed(address _param1, address _param2) payable: 
  require calldata.size - 4 >=′ 64
  return tokenInterestOwed[_param1][_param2]


# hash = 0x16a6bff6
# getter = ['storage', 160, 0, ['sha3', ['data', ['mask_shl', 32, 224, 0, ['cd', 4]], 39]]]
# const = None
# payable = True
def targets(bytes4 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return targets[Mask(32, 224, _param1)]


# hash = 0x2035d73b
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 32, 224, 0, ['cd', 4]], 40]]]]
# const = None
# payable = True
def targetIsPaused(bytes4 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return bool(stor40[Mask(32, 224, _param1)])


# hash = 0x2274346b
# getter = ['storage', 160, 0, 6]
# const = None
# payable = True
def vaultContract() payable: 
  return vaultContractAddress


# hash = 0x327ab639
# getter = None
# const = None
# payable = True
def unknown327ab639(addr _param1, addr _param2) payable: 
  require calldata.size - 4 >=′ 64
  require 1 == stor0
  stor0 = 2
  if 0 >= lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0:
      lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 = block.timestamp
      stor0 = 1
      return 0
  if lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 <= 0:
      lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 = block.timestamp
      stor0 = 1
      return 0
  if not _param2:
      lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 = block.timestamp
      stor0 = 1
      return 0
  require lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 <= block.timestamp
  if not block.timestamp - lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512:
      if 0 <= tokenInterestOwed[caller][addr(_param2)]:
          lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 = block.timestamp
          stor0 = 1
          return 0
  else:
      require (block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / block.timestamp - lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 == lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0
      if (block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / 24 * 3600 <= tokenInterestOwed[caller][addr(_param2)]:
          if (block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / 24 * 3600 > 0:
              require ((block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / 24 * 3600) + lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_256 >= lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_256
              lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_256 += (block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / 24 * 3600
              require (block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / 24 * 3600 <= tokenInterestOwed[caller][addr(_param2)]
              tokenInterestOwed[caller][addr(_param2)] -= (block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / 24 * 3600
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(_param2), oracle[addr(_param1)], (block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / 24 * 3600
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, 'payInterestForOracle: BZxVault.withdrawToken failed'
              require ext_code.size(oracle[addr(_param1)])
              call oracle[addr(_param1)].0xdaebc33e with:
                   gas gas_remaining wei
                  args caller, addr(_param2), (block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / 24 * 3600, stor2
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, 'payInterestForOracle: OracleInterface.didPayInterestByLender failed'
              log LogPayInterestForOracle(
                    address lender=(block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / 24 * 3600,
                    address oracleAddress=lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_256,
                    address interestTokenAddress=caller,
                    uint256 amountPaid=oracle[addr(_param1)],
                    uint256 totalAccrued=_param2)
          lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 = block.timestamp
          stor0 = 1
          return ((block.timestamp * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) - (lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 * lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_0) / 24 * 3600)
  if tokenInterestOwed[caller][addr(_param2)] > 0:
      require tokenInterestOwed[caller][addr(_param2)] + lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_256 >= lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_256
      lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_256 += tokenInterestOwed[caller][addr(_param2)]
      require tokenInterestOwed[caller][addr(_param2)] <= tokenInterestOwed[caller][addr(_param2)]
      tokenInterestOwed[caller][addr(_param2)] = 0
      require ext_code.size(vaultContractAddress)
      call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
           gas gas_remaining wei
          args addr(_param2), oracle[addr(_param1)], tokenInterestOwed[caller][addr(_param2)]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, 'payInterestForOracle: BZxVault.withdrawToken failed'
      require ext_code.size(oracle[addr(_param1)])
      call oracle[addr(_param1)].0xdaebc33e with:
           gas gas_remaining wei
          args caller, addr(_param2), tokenInterestOwed[caller][addr(_param2)], stor2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, 'payInterestForOracle: OracleInterface.didPayInterestByLender failed'
      log LogPayInterestForOracle(
            address lender=tokenInterestOwed[caller][addr(_param2)],
            address oracleAddress=lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_256,
            address interestTokenAddress=caller,
            uint256 amountPaid=oracle[addr(_param1)],
            uint256 totalAccrued=_param2)
  lenderOracleInterest[caller][addr(_param1)][addr(_param2)].field_512 = block.timestamp
  stor0 = 1
  return tokenInterestOwed[caller][addr(_param2)]


# hash = 0x42ad3526
# getter = ['struct', ['loc', 18]]
# const = None
# payable = True
def orderListIndex(bytes32 _param1, address _param2) payable: 
  require calldata.size - 4 >=′ 64
  return orderListIndex[_param1][_param2].field_0, bool(orderListIndex[_param1][_param2].field_256)


# hash = 0x4780eac1
# getter = ['storage', 160, 0, 5]
# const = None
# payable = True
def wethContract() payable: 
  return wethContractAddress


# hash = 0x4a7c3d50
# getter = ['struct', ['loc', 21]]
# const = None
# payable = True
def positionListIndex(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return positionListIndex[_param1].field_0, bool(positionListIndex[_param1].field_256)


# hash = 0x4b4056c5
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 24]]]
# const = None
# payable = True
def lenderOrderInterest(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return lenderOrderInterest[_param1].field_0, lenderOrderInterest[_param1].field_256, lenderOrderInterest[_param1].field_512


# hash = 0x4ca3bfc5
# getter = None
# const = None
# payable = True
def unknown4ca3bfc5(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 <= lenderOrderInterest[_param1].field_512:
      require lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 <= block.timestamp
      if not block.timestamp - lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512:
          if 0 <= tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]:
              if lenderOrderInterest[_param1].field_256 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         0
          else:
              if lenderOrderInterest[_param1].field_256 > 0:
                  if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                      return orderLender[_param1], 
                             orders[_param1].field_256,
                             lenderOrderInterest[_param1].field_256,
                             lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                             lenderOrderInterest[_param1].field_0,
                             tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         0
              if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         0,
                         lenderOrderInterest[_param1].field_0,
                         tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
      else:
          require (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / block.timestamp - lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 == lenderOrderInterest[_param1].field_0
          if (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600 <= tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]:
              if lenderOrderInterest[_param1].field_256 > 0:
                  if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                      return orderLender[_param1], 
                             orders[_param1].field_256,
                             lenderOrderInterest[_param1].field_256,
                             lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                             lenderOrderInterest[_param1].field_0,
                             (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         0
              if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         0,
                         lenderOrderInterest[_param1].field_0,
                         (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600
          else:
              if lenderOrderInterest[_param1].field_256 > 0:
                  if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                      return orderLender[_param1], 
                             orders[_param1].field_256,
                             lenderOrderInterest[_param1].field_256,
                             lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                             lenderOrderInterest[_param1].field_0,
                             tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         0
              if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         0,
                         lenderOrderInterest[_param1].field_0,
                         tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
          ('le', ('field', 512, ('stor', ('map', ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor10', 10)))), ('map', ('field', 768, ('stor', ('map', ('param', '_param1'), ('name', 'stor10', 10)))), ('map', ('stor', ('map', ('param', '_param1'), ('name', 'stor14', 14))), ('name', 'lenderOracleInterest', 23)))))), 0)
      return orderLender[_param1], 
             orders[_param1].field_256,
             lenderOrderInterest[_param1].field_256,
             0,
             lenderOrderInterest[_param1].field_0,
             0
  require lenderOrderInterest[_param1].field_512 <= lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512
  if not lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 - lenderOrderInterest[_param1].field_512:
      require lenderOrderInterest[_param1].field_256 >= lenderOrderInterest[_param1].field_256
      require lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 <= block.timestamp
      if not block.timestamp - lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512:
          if 0 <= tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]:
              if lenderOrderInterest[_param1].field_256 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         0
          else:
              if lenderOrderInterest[_param1].field_256 > 0:
                  if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                      return orderLender[_param1], 
                             orders[_param1].field_256,
                             lenderOrderInterest[_param1].field_256,
                             lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                             lenderOrderInterest[_param1].field_0,
                             tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         0
              if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         0,
                         lenderOrderInterest[_param1].field_0,
                         tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
      else:
          require (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / block.timestamp - lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 == lenderOrderInterest[_param1].field_0
          if (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600 <= tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]:
              if lenderOrderInterest[_param1].field_256 > 0:
                  if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                      return orderLender[_param1], 
                             orders[_param1].field_256,
                             lenderOrderInterest[_param1].field_256,
                             lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                             lenderOrderInterest[_param1].field_0,
                             (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         0
              if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         0,
                         lenderOrderInterest[_param1].field_0,
                         (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600
          else:
              if lenderOrderInterest[_param1].field_256 > 0:
                  if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                      return orderLender[_param1], 
                             orders[_param1].field_256,
                             lenderOrderInterest[_param1].field_256,
                             lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                             lenderOrderInterest[_param1].field_0,
                             tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         0
              if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         lenderOrderInterest[_param1].field_256,
                         0,
                         lenderOrderInterest[_param1].field_0,
                         tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
          ('le', ('field', 512, ('stor', ('map', ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor10', 10)))), ('map', ('field', 768, ('stor', ('map', ('param', '_param1'), ('name', 'stor10', 10)))), ('map', ('stor', ('map', ('param', '_param1'), ('name', 'stor14', 14))), ('name', 'lenderOracleInterest', 23)))))), 0)
      return orderLender[_param1], 
             orders[_param1].field_256,
             lenderOrderInterest[_param1].field_256,
             0,
             lenderOrderInterest[_param1].field_0,
             0
  require (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 - lenderOrderInterest[_param1].field_512 == lenderOrderInterest[_param1].field_0
  require ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256 >= lenderOrderInterest[_param1].field_256
  require lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 <= block.timestamp
  if not block.timestamp - lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512:
      if 0 <= tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]:
          if ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256 > 0:
              return orderLender[_param1], 
                     orders[_param1].field_256,
                     ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
                     lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                     lenderOrderInterest[_param1].field_0,
                     0
      else:
          if ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256 > 0:
              if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
              return orderLender[_param1], 
                     orders[_param1].field_256,
                     ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
                     lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                     lenderOrderInterest[_param1].field_0,
                     0
          if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
              return orderLender[_param1], 
                     orders[_param1].field_256,
                     ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
                     0,
                     lenderOrderInterest[_param1].field_0,
                     tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
  else:
      require (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / block.timestamp - lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 == lenderOrderInterest[_param1].field_0
      if (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600 <= tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]:
          if ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256 > 0:
              if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600
              return orderLender[_param1], 
                     orders[_param1].field_256,
                     ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
                     lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                     lenderOrderInterest[_param1].field_0,
                     0
          if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
              return orderLender[_param1], 
                     orders[_param1].field_256,
                     ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
                     0,
                     lenderOrderInterest[_param1].field_0,
                     (block.timestamp * lenderOrderInterest[_param1].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600
      else:
          if ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256 > 0:
              if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
                  return orderLender[_param1], 
                         orders[_param1].field_256,
                         ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
                         lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                         lenderOrderInterest[_param1].field_0,
                         tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
              return orderLender[_param1], 
                     orders[_param1].field_256,
                     ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
                     lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512,
                     lenderOrderInterest[_param1].field_0,
                     0
          if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 > 0:
              return orderLender[_param1], 
                     orders[_param1].field_256,
                     ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
                     0,
                     lenderOrderInterest[_param1].field_0,
                     tokenInterestOwed[stor14[_param1]][stor10[_param1].field_256]
      ('le', ('field', 512, ('stor', ('map', ('field', 256, ('stor', ('map', ('param', '_param1'), ('name', 'stor10', 10)))), ('map', ('field', 768, ('stor', ('map', ('param', '_param1'), ('name', 'stor10', 10)))), ('map', ('stor', ('map', ('param', '_param1'), ('name', 'stor14', 14))), ('name', 'lenderOracleInterest', 23)))))), 0)
  return orderLender[_param1], 
         orders[_param1].field_256,
         ((lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOrderInterest[_param1].field_0) - (lenderOrderInterest[_param1].field_512 * lenderOrderInterest[_param1].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256,
         0,
         lenderOrderInterest[_param1].field_0,
         0


# hash = 0x5c445c86
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 23]]]]]]]
# const = None
# payable = True
def lenderOracleInterest(address _param1, address _param2, address _param3) payable: 
  require calldata.size - 4 >=′ 96
  return lenderOracleInterest[_param1][_param2][_param3].field_0, 
         lenderOracleInterest[_param1][_param2][_param3].field_256,
         lenderOracleInterest[_param1][_param2][_param3].field_512


# hash = 0x64a71040
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def bZxEtherContract() payable: 
  return bZxEtherContractAddress


# hash = 0x71eb125e
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 26]]]
# const = None
# payable = True
def oracleAddresses(address _param1) payable: 
  require calldata.size - 4 >=′ 32
  return oracle[_param1]


# hash = 0x779dec5b
# getter = ['storage', 160, 0, 3]
# const = None
# payable = True
def bZRxTokenContract() payable: 
  return bZRxTokenContractAddress


# hash = 0x7955f60f
# getter = ['struct', ['loc', 20]]
# const = None
# payable = True
def positionList(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  require _param1 < positionList.length
  return positionList[_param1].field_0, positionList[_param1].field_256


# hash = 0x7b8e3514
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 28]]]]]]
# const = None
# payable = True
def allowedValidators(address _param1, address _param2) payable: 
  require calldata.size - 4 >=′ 64
  return bool(stor28[_param1][_param2])


# hash = 0x82c174d0
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 27]]]]]]
# const = None
# payable = True
def preSigned(bytes32 _param1, address _param2) payable: 
  require calldata.size - 4 >=′ 64
  return bool(stor27[_param1][_param2])


# hash = 0x86042ec6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 16]]]]]
# const = None
# payable = True
def loanPositionsIds(bytes32 _param1, address _param2) payable: 
  require calldata.size - 4 >=′ 64
  return loanPositionsIds[_param1][_param2]


# hash = 0x8638aa65
# getter = ['bool', ['storage', 8, 160, 9]]
# const = None
# payable = True
def DEBUG_MODE() payable: 
  return bool(DEBUG_MODE)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def owner() payable: 
  return owner


# hash = 0x9048617a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 25]]]
# const = None
# payable = True
def traderLoanInterest(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return traderLoanInterest[_param1].field_0, 
         traderLoanInterest[_param1].field_256,
         traderLoanInterest[_param1].field_512,
         traderLoanInterest[_param1].field_768


# hash = 0x9437d0ea
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 19]]], ['cd', 36]]]
# const = None
# payable = True
def orderPositionList(bytes32 _param1, uint256 _param2) payable: 
  require calldata.size - 4 >=′ 64
  require _param2 < orderPositionList[_param1]
  return orderPositionList[_param1][_param2]


# hash = 0x9ae6b186
# getter = ['storage', 160, 0, 9]
# const = None
# payable = True
def bZxTo0xV2Contract() payable: 
  return bZxTo0xV2ContractAddress


# hash = 0x9c3f1e90
# getter = ['struct', ['loc', 10]]
# const = None
# payable = True
def orders(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return orders[_param1].field_0, 
         orders[_param1].field_256,
         orders[_param1].field_512,
         orders[_param1].field_768,
         orders[_param1].field_1024,
         orders[_param1].field_1280,
         orders[_param1].field_1536,
         orders[_param1].field_1792,
         orders[_param1].field_2048,
         orders[_param1].field_2304


# hash = 0x9e312dac
# getter = ['struct', ['loc', 15]]
# const = None
# payable = True
def loanPositions(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return loanPositions[_param1].field_0, 
         loanPositions[_param1].field_256,
         loanPositions[_param1].field_512,
         loanPositions[_param1].field_768,
         loanPositions[_param1].field_1024,
         loanPositions[_param1].field_1280,
         loanPositions[_param1].field_1536,
         loanPositions[_param1].field_1792,
         loanPositions[_param1].field_2048,
         bool(loanPositions[_param1].field_2304),
         loanPositions[_param1].field_2560


# hash = 0xa72480ae
# getter = None
# const = None
# payable = True
def orderAux(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  mem[128] = stor11[_param1][9].field_0
  [94midx = 128
  [94ms = 0
  while stor11[_param1][9].length + 96 > [94midx:
      mem[[94midx + 32] = stor11[_param1][[94ms + 9].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return stor11[_param1].field_0, 
         stor11[_param1].field_256,
         stor11[_param1].field_512,
         stor11[_param1].field_768,
         stor11[_param1].field_1024,
         stor11[_param1].field_1280,
         stor11[_param1].field_1536,
         stor11[_param1].field_1792,
         bool(stor11[_param1].field_2048),
         Array(len=stor11[_param1][9].length, data=mem[128 len ceil32(stor11[_param1][9].length)])


# hash = 0xb7a025f9
# getter = ['storage', 160, 0, 8]
# const = None
# payable = True
def bZxTo0xContract() payable: 
  return bZxTo0xContractAddress


# hash = 0xc4d66de8
# getter = None
# const = None
# payable = True
def initialize(address _sender) payable: 
  require calldata.size - 4 >=′ 32
  require caller == owner
  targets[Mask(32, 224, sha3('payInterestForOrder(bytes32)'))] = _sender
  stor39[Mask(32, 224, ('name', 'stor2970', 20608571293394017686664154269169437409893635303088270681801712505759373932876682376868723))] = _sender
  targets[Mask(32, 224, sha3('getMarginLevels(bytes32,address)'))] = _sender
  stor39[Mask(32, 224, ('name', 'storFE67', 656934418636052665012613038398210091551940171530713301052580931037275567232969908084325251790440639841023001997146602173299))] = _sender
  stor39[Mask(32, 224, ('name', 'stor2967', 1227326242905548082114417476897002760953536771216552247799863072803670142175359794))] = _sender
  stor39[Mask(32, 224, ('name', 'stor2967', 88438176167387057176243982077467603867738321418432754950529205842872764004585143215618934570316659))] = _sender


# hash = 0xcce37f3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 12]]]
# const = None
# payable = True
def orderFilledAmounts(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return orderFilledAmounts[_param1]


# hash = 0xd9fd7341
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 13]]]
# const = None
# payable = True
def orderCancelledAmounts(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return orderCancelledAmounts[_param1]


# hash = 0xdb4d0ae0
# getter = None
# const = None
# payable = True
def unknowndb4d0ae0(uint256 _param1, addr _param2) payable: 
  require calldata.size - 4 >=′ 64
  if not orders[_param1].field_0:
      return 0
  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
      return 0
  if not loanPositions[stor16[_param1][addr(_param2)]].field_2304:
      return 0
  require ext_code.size(oracle[stor10[_param1].field_768])
  static call oracle[stor10[_param1].field_768].getCurrentMarginAmount(address loanTokenAddress, address positionTokenAddress, address collateralTokenAddress, uint256 loanTokenAmount, uint256 positionTokenAmount, uint256 collateralTokenAmount) with:
          gas gas_remaining wei
         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_768, loanPositions[stor16[_param1][addr(_param2)]].field_1536, loanPositions[stor16[_param1][addr(_param2)]].field_1280
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  return orders[_param1].field_1536, orders[_param1].field_1792, ext_call.return_data[0]


# hash = 0xdd28b20b
# getter = None
# const = None
# payable = True
def unknowndd28b20b(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  require 1 == stor0
  stor0 = 2
  if 0 >= lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0:
      lenderOrderInterest[_param1].field_512 = block.timestamp
      lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 = block.timestamp
      stor0 = 1
      return 0
  if lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 <= 0:
      lenderOrderInterest[_param1].field_512 = block.timestamp
      lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 = block.timestamp
      stor0 = 1
      return 0
  if not orders[_param1].field_256:
      lenderOrderInterest[_param1].field_512 = block.timestamp
      lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 = block.timestamp
      stor0 = 1
      return 0
  require lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 <= block.timestamp
  if not block.timestamp - lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512:
      if 0 <= tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256]:
          lenderOrderInterest[_param1].field_512 = block.timestamp
          lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 = block.timestamp
          stor0 = 1
          return 0
  else:
      require (block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / block.timestamp - lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 == lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0
      if (block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600 <= tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256]:
          if (block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600 > 0:
              require ((block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600) + lenderOrderInterest[_param1].field_256 >= lenderOrderInterest[_param1].field_256
              lenderOrderInterest[_param1].field_256 += (block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600
              require ((block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600) + lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_256 >= lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_256
              lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_256 += (block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600
              require (block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600 <= tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256]
              tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256] -= (block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args orders[_param1].field_256, oracle[stor10[_param1].field_768], (block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, '_payInterest: BZxVault.withdrawToken interest failed'
              require ext_code.size(oracle[stor10[_param1].field_768])
              call oracle[stor10[_param1].field_768].0x3913c2fd with:
                   gas gas_remaining wei
                  args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, orderLender[stor10[_param1].field_2304], (block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600, stor2
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, '_payInterest: OracleInterface.didPayInterest failed'
              log LogPayInterestForOrder(
                    bytes32 loanOrderHash=(block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600,
                    address lender=lenderOrderInterest[_param1].field_256,
                    address interestTokenAddress=orderPositionList[stor10[_param1].field_2304],
                    uint256 amountPaid=orders[_param1].field_2304,
                    uint256 totalAccrued=orderLender[stor10[_param1].field_2304],
                    uint256 loanCount=orders[_param1].field_256)
          lenderOrderInterest[_param1].field_512 = block.timestamp
          lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 = block.timestamp
          stor0 = 1
          return ((block.timestamp * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) - (lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 * lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_0) / 24 * 3600)
  if tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256] > 0:
      require tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256] + lenderOrderInterest[_param1].field_256 >= lenderOrderInterest[_param1].field_256
      lenderOrderInterest[_param1].field_256 += tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256]
      require tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256] + lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_256 >= lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_256
      lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_256 += tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256]
      require tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256] <= tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256]
      tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256] = 0
      require ext_code.size(vaultContractAddress)
      call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
           gas gas_remaining wei
          args orders[_param1].field_256, oracle[stor10[_param1].field_768], tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, '_payInterest: BZxVault.withdrawToken interest failed'
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x3913c2fd with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, orderLender[stor10[_param1].field_2304], tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256], stor2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, '_payInterest: OracleInterface.didPayInterest failed'
      log LogPayInterestForOrder(
            bytes32 loanOrderHash=tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256],
            address lender=lenderOrderInterest[_param1].field_256,
            address interestTokenAddress=orderPositionList[stor10[_param1].field_2304],
            uint256 amountPaid=orders[_param1].field_2304,
            uint256 totalAccrued=orderLender[stor10[_param1].field_2304],
            uint256 loanCount=orders[_param1].field_256)
  lenderOrderInterest[_param1].field_512 = block.timestamp
  lenderOracleInterest[stor14[_param1]][stor10[_param1].field_768][stor10[_param1].field_256].field_512 = block.timestamp
  stor0 = 1
  return tokenInterestOwed[stor14[stor10[_param1].field_2304]][stor10[_param1].field_256]


# hash = 0xde3f26eb
# getter = ['storage', 160, 0, 7]
# const = None
# payable = True
def oracleRegistryContract() payable: 
  return oracleRegistryContractAddress


# hash = 0xe4a95319
# getter = None
# const = None
# payable = True
def unknowne4a95319(uint256 _param1, addr _param2) payable: 
  require calldata.size - 4 >=′ 64
  if block.timestamp > loanPositions[stor16[_param1][addr(_param2)]].field_2048:
      if traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 <= 0:
          if loanPositions[stor16[_param1][addr(_param2)]].field_2048 >= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
              return orders[_param1].field_256, 
                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                     0
          if loanPositions[stor16[_param1][addr(_param2)]].field_2048 <= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
              return orders[_param1].field_256, 
                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                     0
      else:
          if 0 >= traderLoanInterest[stor16[_param1][addr(_param2)]].field_0:
              if loanPositions[stor16[_param1][addr(_param2)]].field_2048 >= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                  return orders[_param1].field_256, 
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                         0
              if loanPositions[stor16[_param1][addr(_param2)]].field_2048 <= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                  return orders[_param1].field_256, 
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                         0
          else:
              if traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 <= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                  if not loanPositions[stor16[_param1][addr(_param2)]].field_2048 - traderLoanInterest[stor16[_param1][addr(_param2)]].field_768:
                      if traderLoanInterest[stor16[_param1][addr(_param2)]].field_256 >= traderLoanInterest[stor16[_param1][addr(_param2)]].field_256:
                          if loanPositions[stor16[_param1][addr(_param2)]].field_2048 >= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                              return orders[_param1].field_256, 
                                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                                     0
                          if loanPositions[stor16[_param1][addr(_param2)]].field_2048 <= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                              return orders[_param1].field_256, 
                                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                                     0
                  else:
                      if (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / loanPositions[stor16[_param1][addr(_param2)]].field_2048 - traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 == traderLoanInterest[stor16[_param1][addr(_param2)]].field_0:
                          if ((loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600) + traderLoanInterest[stor16[_param1][addr(_param2)]].field_256 >= traderLoanInterest[stor16[_param1][addr(_param2)]].field_256:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_2048 >= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                                  return orders[_param1].field_256, 
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                                         ((loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600) + traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                                         0
                              if loanPositions[stor16[_param1][addr(_param2)]].field_2048 <= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                                  return orders[_param1].field_256, 
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                                         ((loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600) + traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                                         0
  else:
      if traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 <= 0:
          if block.timestamp >= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
              return orders[_param1].field_256, 
                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                     0
          if block.timestamp <= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
              if not loanPositions[stor16[_param1][addr(_param2)]].field_2048 - block.timestamp:
                  return orders[_param1].field_256, 
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                         0
              if (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / loanPositions[stor16[_param1][addr(_param2)]].field_2048 - block.timestamp == traderLoanInterest[stor16[_param1][addr(_param2)]].field_0:
                  return orders[_param1].field_256, 
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600
      else:
          if 0 >= traderLoanInterest[stor16[_param1][addr(_param2)]].field_0:
              if block.timestamp >= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                  return orders[_param1].field_256, 
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                         0
              if block.timestamp <= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                  if not loanPositions[stor16[_param1][addr(_param2)]].field_2048 - block.timestamp:
                      return orders[_param1].field_256, 
                             traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                             traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                             traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                             0
                  if (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / loanPositions[stor16[_param1][addr(_param2)]].field_2048 - block.timestamp == traderLoanInterest[stor16[_param1][addr(_param2)]].field_0:
                      return orders[_param1].field_256, 
                             traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                             traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                             traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600
          else:
              if traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 <= block.timestamp:
                  if not block.timestamp - traderLoanInterest[stor16[_param1][addr(_param2)]].field_768:
                      if traderLoanInterest[stor16[_param1][addr(_param2)]].field_256 >= traderLoanInterest[stor16[_param1][addr(_param2)]].field_256:
                          if block.timestamp >= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                              return orders[_param1].field_256, 
                                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                                     traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                                     0
                          if block.timestamp <= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                              if not loanPositions[stor16[_param1][addr(_param2)]].field_2048 - block.timestamp:
                                  return orders[_param1].field_256, 
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                                         0
                              if (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / loanPositions[stor16[_param1][addr(_param2)]].field_2048 - block.timestamp == traderLoanInterest[stor16[_param1][addr(_param2)]].field_0:
                                  return orders[_param1].field_256, 
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600
                  else:
                      if (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / block.timestamp - traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 == traderLoanInterest[stor16[_param1][addr(_param2)]].field_0:
                          if ((block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600) + traderLoanInterest[stor16[_param1][addr(_param2)]].field_256 >= traderLoanInterest[stor16[_param1][addr(_param2)]].field_256:
                              if block.timestamp >= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                                  return orders[_param1].field_256, 
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                                         ((block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600) + traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                                         traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                                         0
                              if block.timestamp <= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_2048 - block.timestamp:
                                      return orders[_param1].field_256, 
                                             traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                                             ((block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600) + traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                                             traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                                             0
                                  if (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / loanPositions[stor16[_param1][addr(_param2)]].field_2048 - block.timestamp == traderLoanInterest[stor16[_param1][addr(_param2)]].field_0:
                                      return orders[_param1].field_256, 
                                             traderLoanInterest[stor16[_param1][addr(_param2)]].field_0,
                                             ((block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (traderLoanInterest[stor16[_param1][addr(_param2)]].field_768 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600) + traderLoanInterest[stor16[_param1][addr(_param2)]].field_256,
                                             traderLoanInterest[stor16[_param1][addr(_param2)]].field_512,
                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600
  revert


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address _newOwner) payable: 
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = 0xf4fb9b2f
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 17]]], ['cd', 36]]]
# const = None
# payable = True
def orderList(address _param1, uint256 _param2) payable: 
  require calldata.size - 4 >=′ 64
  require _param2 < orderList[_param1]
  return orderList[_param1][_param2]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert with 0, 'fallback not allowed'


