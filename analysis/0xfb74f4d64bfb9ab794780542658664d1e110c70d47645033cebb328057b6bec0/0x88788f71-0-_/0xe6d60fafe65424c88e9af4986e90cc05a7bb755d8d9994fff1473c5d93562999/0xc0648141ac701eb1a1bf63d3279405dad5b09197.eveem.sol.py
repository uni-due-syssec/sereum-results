# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xC0648141ac701eB1a1bF63D3279405daD5b09197 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x09c5a317': 'unknown09c5a317(?)'} 

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
    # storage address 3759358406934317647883046264491191442455605918977129010104418545991709917066550
    stor3759358406934317647883046264491191442455605918977129010104418545991709917066550
    # storage address 29456154062828672557473723247354683789153397515171478680395262379846516970189683
    stor29456154062828672557473723247354683789153397515171478680395262379846516970189683
    # storage address 1227326242933425195610638786373842767099986346445051720540204598784149518740190067
    stor1227326242933425195610638786373842767099986346445051720540204598784149518740190067
    # storage address 314670265799158229021154762285524441673326758555173735815261779228073799381270279478
    stor314670265799158229021154762285524441673326758555173735815261779228073799381270279478
    # storage address 345363845990158578749239147842276833049654305397491675352759186696237954790302270405519791502646
    stor345363845990158578749239147842276833049654305397491675352759186696237954790302270405519791502646
    # storage address 59270214650926482349764189863209587540947084731898323102022459520854313176618002166735941726008128822
    stor59270214650926482349764189863209587540947084731898323102022459520854313176618002166735941726008128822
# hash = 0x093983bd
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 14]]]
# const = None
# payable = True
def orderLender(bytes32 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return morderLenderm[m_param1m]


# hash = 0x13e97c71
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 22]]]]]
# const = None
# payable = True
def tokenInterestOwed(address m_param1, address m_param2) payable: 
  require calldata.size - 4 >=′ 64
  return mtokenInterestOwedm[m_param1m]m[m_param2m]


# hash = 0x16a6bff6
# getter = ['storage', 160, 0, ['sha3', ['data', ['mask_shl', 32, 224, 0, ['cd', 4]], 39]]]
# const = None
# payable = True
def targets(bytes4 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return mtargetsm[Mask(32, 224, m_param1)m]


# hash = 0x2035d73b
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 32, 224, 0, ['cd', 4]], 40]]]]
# const = None
# payable = True
def targetIsPaused(bytes4 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return bool(mstor40m[Mask(32, 224, m_param1)m])


# hash = 0x2274346b
# getter = ['storage', 160, 0, 6]
# const = None
# payable = True
def vaultContract() payable: 
  return mvaultContractAddress


# hash = 0x42ad3526
# getter = ['struct', ['loc', 18]]
# const = None
# payable = True
def orderListIndex(bytes32 m_param1, address m_param2) payable: 
  require calldata.size - 4 >=′ 64
  return morderListIndexm[m_param1m]m[m_param2m]m.field_0, bool(morderListIndexm[m_param1m]m[m_param2m]m.field_256)


# hash = 0x4780eac1
# getter = ['storage', 160, 0, 5]
# const = None
# payable = True
def wethContract() payable: 
  return mwethContractAddress


# hash = 0x4a7c3d50
# getter = ['struct', ['loc', 21]]
# const = None
# payable = True
def positionListIndex(uint256 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return mpositionListIndexm[m_param1m]m.field_0, bool(mpositionListIndexm[m_param1m]m.field_256)


# hash = 0x4b4056c5
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 24]]]
# const = None
# payable = True
def lenderOrderInterest(bytes32 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return mlenderOrderInterestm[m_param1m]m.field_0, mlenderOrderInterestm[m_param1m]m.field_256, mlenderOrderInterestm[m_param1m]m.field_512


# hash = 0x52cccdb3
# getter = None
# const = None
# payable = True
def unknown52cccdb3(uint256 m_param1, addr m_param2, uint256 m_param3) payable: 
  require calldata.size - 4 >=′ 96
  require 1 == mstor0
  mstor0 = 2
  mstor2 = gas_remaining + 21000
  if m_param3 <= 0:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  ':BZxLoanHealth::depositCollatera: depositAmount too low'
  if not mordersm[m_param1m]m.field_0:
      revert with 0, ':BZxLoanHealth::depositCollatera: loanOrder.loanTokenAddress == address(0)'
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768:
      revert with 0, ':BZxLoanHealth::depositCollatera: loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304:
      revert with 0, ':BZxLoanHealth::depositCollatera: loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  require ext_code.size(mvaultContractAddress)
  if mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256 == m_param2:
      call mvaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(m_param2), caller, m_param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ':BZxLoanHealth::depositCollatera: BZxVault.depositToken position failed'
      require m_param3 + mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280 >= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280
      mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280 += m_param3
      require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
      call moraclem[mstor10m[m_param1m]m.field_768m].0x33ac22b4 with:
           gas gas_remaining wei
          args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, m_param3, mstor2
  else:
      call mvaultContractAddress.transferTokenFrom(address tokenContract, address transferTo, address transferFrom, uint256 value) with:
           gas gas_remaining wei
          args addr(m_param2), caller, moraclem[mstor10m[m_param1m]m.field_768m], m_param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ':BZxLoanHealth::depositCollatera: BZxVault.transferTokenFrom failed'
      require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
      call moraclem[mstor10m[m_param1m]m.field_768m].0x4849b6c8 with:
           gas gas_remaining wei
          args addr(m_param2), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, m_param3, -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 64
      if not ext_call.return_data[0]:
          revert with 0, ':BZxLoanHealth::depositCollatera: collateralTokenAmountReceived == 0'
      if ext_call.return_data[32] < m_param3:
          require ext_call.return_data[32] <= m_param3
          require ext_code.size(mvaultContractAddress)
          call mvaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args addr(m_param2), caller, m_param3 - ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ':BZxLoanHealth::depositCollatera: BZxVault.withdrawToken deposit failed'
      require ext_call.return_data[0] + mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280 >= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280
      mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280 += ext_call.return_data[0]
      require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
      call moraclem[mstor10m[m_param1m]m.field_768m].0x33ac22b4 with:
           gas gas_remaining wei
          args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, ext_call.return_data[0], mstor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, ':BZxLoanHealth::depositCollatera: OracleInterface.didDepositCollateral failed'
  mstor2 = 0
  mstor0 = 1
  return 1


# hash = 0x5c445c86
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 23]]]]]]]
# const = None
# payable = True
def lenderOracleInterest(address m_param1, address m_param2, address m_param3) payable: 
  require calldata.size - 4 >=′ 96
  return mlenderOracleInterestm[m_param1m]m[m_param2m]m[m_param3m]m.field_0, 
         mlenderOracleInterestm[m_param1m]m[m_param2m]m[m_param3m]m.field_256,
         mlenderOracleInterestm[m_param1m]m[m_param2m]m[m_param3m]m.field_512


# hash = 0x64a71040
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def bZxEtherContract() payable: 
  return mbZxEtherContractAddress


# hash = 0x71eb125e
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 26]]]
# const = None
# payable = True
def oracleAddresses(address m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return moraclem[m_param1m]


# hash = 0x779dec5b
# getter = ['storage', 160, 0, 3]
# const = None
# payable = True
def bZRxTokenContract() payable: 
  return mbZRxTokenContractAddress


# hash = 0x7955f60f
# getter = ['struct', ['loc', 20]]
# const = None
# payable = True
def positionList(uint256 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  require m_param1 < mpositionListm.length
  return mpositionListm[m_param1m]m.field_0, mpositionListm[m_param1m]m.field_256


# hash = 0x7b8e3514
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 28]]]]]]
# const = None
# payable = True
def allowedValidators(address m_param1, address m_param2) payable: 
  require calldata.size - 4 >=′ 64
  return bool(mstor28m[m_param1m]m[m_param2m])


# hash = 0x82c174d0
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 27]]]]]]
# const = None
# payable = True
def preSigned(bytes32 m_param1, address m_param2) payable: 
  require calldata.size - 4 >=′ 64
  return bool(mstor27m[m_param1m]m[m_param2m])


# hash = 0x853002d3
# getter = None
# const = None
# payable = True
def unknown853002d3(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >=′ 64
  if not mordersm[m_param1m]m.field_0:
      return 0
  if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768:
      return 0
  if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2304:
      return 0
  require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
  static call moraclem[mstor10m[m_param1m]m.field_768m].'^?K<' with:
          gas gas_remaining wei
         args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2560
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 128
  return bool(ext_call.return_data[0]), ext_call.return_data[32], ext_call.return_data[64], ext_call.return_data[96]


# hash = 0x86042ec6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 16]]]]]
# const = None
# payable = True
def loanPositionsIds(bytes32 m_param1, address m_param2) payable: 
  require calldata.size - 4 >=′ 64
  return mloanPositionsIdsm[m_param1m]m[m_param2m]


# hash = 0x8638aa65
# getter = ['bool', ['storage', 8, 160, 9]]
# const = None
# payable = True
def DEBUG_MODE() payable: 
  return bool(mDEBUG_MODE)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def owner() payable: 
  return mowner


# hash = 0x9048617a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 25]]]
# const = None
# payable = True
def traderLoanInterest(uint256 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return mtraderLoanInterestm[m_param1m]m.field_0, 
         mtraderLoanInterestm[m_param1m]m.field_256,
         mtraderLoanInterestm[m_param1m]m.field_512,
         mtraderLoanInterestm[m_param1m]m.field_768


# hash = 0x9437d0ea
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 19]]], ['cd', 36]]]
# const = None
# payable = True
def orderPositionList(bytes32 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >=′ 64
  require m_param2 < morderPositionListm[m_param1m]
  return morderPositionListm[m_param1m]m[m_param2m]


# hash = 0x9ae6b186
# getter = ['storage', 160, 0, 9]
# const = None
# payable = True
def bZxTo0xV2Contract() payable: 
  return mbZxTo0xV2ContractAddress


# hash = 0x9c3f1e90
# getter = ['struct', ['loc', 10]]
# const = None
# payable = True
def orders(bytes32 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return mordersm[m_param1m]m.field_0, 
         mordersm[m_param1m]m.field_256,
         mordersm[m_param1m]m.field_512,
         mordersm[m_param1m]m.field_768,
         mordersm[m_param1m]m.field_1024,
         mordersm[m_param1m]m.field_1280,
         mordersm[m_param1m]m.field_1536,
         mordersm[m_param1m]m.field_1792,
         mordersm[m_param1m]m.field_2048,
         mordersm[m_param1m]m.field_2304


# hash = 0x9e312dac
# getter = ['struct', ['loc', 15]]
# const = None
# payable = True
def loanPositions(uint256 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return mloanPositionsm[m_param1m]m.field_0, 
         mloanPositionsm[m_param1m]m.field_256,
         mloanPositionsm[m_param1m]m.field_512,
         mloanPositionsm[m_param1m]m.field_768,
         mloanPositionsm[m_param1m]m.field_1024,
         mloanPositionsm[m_param1m]m.field_1280,
         mloanPositionsm[m_param1m]m.field_1536,
         mloanPositionsm[m_param1m]m.field_1792,
         mloanPositionsm[m_param1m]m.field_2048,
         bool(mloanPositionsm[m_param1m]m.field_2304),
         mloanPositionsm[m_param1m]m.field_2560


# hash = 0xa1e93482
# getter = None
# const = None
# payable = True
def unknowna1e93482(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >=′ 64
  require 1 == mstor0
  mstor0 = 2
  mstor2 = gas_remaining + 21000
  if not mordersm[m_param1m]m.field_0:
      mstor2 = 0
      mstor0 = 1
      return 0
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768:
      mstor2 = 0
      mstor0 = 1
      return 0
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304:
      mstor2 = 0
      mstor0 = 1
      return 0
  require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
  static call moraclem[mstor10m[m_param1m]m.field_768m].'^?K<' with:
          gas gas_remaining wei
         args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 128
  if not ext_call.return_data[96]:
      mstor2 = 0
      mstor0 = 1
      return 0
  if not ext_call.return_data[0]:
      mstor2 = 0
      mstor0 = 1
      return 0
  if m_param2 < ext_call.return_data[96]:
      if m_param2 <= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280:
          if not m_param2:
              mstor2 = 0
              mstor0 = 1
              return 0
          require ext_code.size(mvaultContractAddress)
          call mvaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, caller, m_param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawCollateral: BZxVault.withdrawToken collateral failed'
          require m_param2 <= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280
          mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280 -= m_param2
          require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
          call moraclem[mstor10m[m_param1m]m.field_768m].0x18ddd6a8 with:
               gas gas_remaining wei
              args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, m_param2, mstor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawCollateral: OracleInterface.didWithdrawCollateral failed'
          mstor2 = 0
          mstor0 = 1
          return m_param2
  else:
      if ext_call.return_data[96] <= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280:
          if not ext_call.return_data[96]:
              mstor2 = 0
              mstor0 = 1
              return 0
          require ext_code.size(mvaultContractAddress)
          call mvaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, caller, ext_call.return_data[96]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawCollateral: BZxVault.withdrawToken collateral failed'
          require ext_call.return_data[96] <= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280
          mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280 -= ext_call.return_data[96]
          require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
          call moraclem[mstor10m[m_param1m]m.field_768m].0x18ddd6a8 with:
               gas gas_remaining wei
              args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, ext_call.return_data[96], mstor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawCollateral: OracleInterface.didWithdrawCollateral failed'
          mstor2 = 0
          mstor0 = 1
          return ext_call.return_data[96]
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280:
      mstor2 = 0
      mstor0 = 1
      return 0
  require ext_code.size(mvaultContractAddress)
  call mvaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
       gas gas_remaining wei
      args mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, caller, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, 'BZxLoanHealth::withdrawCollateral: BZxVault.withdrawToken collateral failed'
  require mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280 <= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280
  mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280 = 0
  require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
  call moraclem[mstor10m[m_param1m]m.field_768m].0x18ddd6a8 with:
       gas gas_remaining wei
      args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mstor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, 'BZxLoanHealth::withdrawCollateral: OracleInterface.didWithdrawCollateral failed'
  mstor2 = 0
  mstor0 = 1
  return mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280


# hash = 0xa72480ae
# getter = None
# const = None
# payable = True
def orderAux(bytes32 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  mem[128] = mstor11m[m_param1m]m[9m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile mstor11m[m_param1m]m[9m]m.length + 96 > [94midxm:
      mem[[94midx + 32] = mstor11m[m_param1m]m[[94ms + 9m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return mstor11m[m_param1m]m.field_0, 
         mstor11m[m_param1m]m.field_256,
         mstor11m[m_param1m]m.field_512,
         mstor11m[m_param1m]m.field_768,
         mstor11m[m_param1m]m.field_1024,
         mstor11m[m_param1m]m.field_1280,
         mstor11m[m_param1m]m.field_1536,
         mstor11m[m_param1m]m.field_1792,
         bool(mstor11m[m_param1m]m.field_2048),
         Array(len=mstor11m[m_param1m]m[9m]m.length, data=mem[128 len ceil32(mstor11m[m_param1m]m[9m]m.length)])


# hash = 0xac5da9db
# getter = None
# const = None
# payable = True
def unknownac5da9db(uint256 m_param1, addr m_param2, uint256 m_param3) payable: 
  require calldata.size - 4 >=′ 96
  require 1 == mstor0
  mstor0 = 2
  mstor2 = gas_remaining + 21000
  if m_param3 <= 0:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  ')BZxLoanHealth::depositPosition:depositAmount too low'
  if not mordersm[m_param1m]m.field_0:
      revert with 0, ')BZxLoanHealth::depositPosition:loanOrder.loanTokenAddress == address(0)'
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768:
      revert with 0, ')BZxLoanHealth::depositPosition:loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304:
      revert with 0, ')BZxLoanHealth::depositPosition:loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  require ext_code.size(mvaultContractAddress)
  if mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512 == m_param2:
      call mvaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(m_param2), caller, m_param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::depositPosition:BZxVault.depositToken position failed'
      require m_param3 + mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536 >= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536
      mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536 += m_param3
      require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
      call moraclem[mstor10m[m_param1m]m.field_768m].0xfd670cbd with:
           gas gas_remaining wei
          args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, m_param3, mstor2
  else:
      call mvaultContractAddress.transferTokenFrom(address tokenContract, address transferTo, address transferFrom, uint256 value) with:
           gas gas_remaining wei
          args addr(m_param2), caller, moraclem[mstor10m[m_param1m]m.field_768m], m_param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::depositPosition:BZxVault.transferTokenFrom failed'
      require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
      call moraclem[mstor10m[m_param1m]m.field_768m].0x4849b6c8 with:
           gas gas_remaining wei
          args addr(m_param2), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, m_param3, -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 64
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::depositPosition:positionTokenAmountReceived == 0'
      if ext_call.return_data[32] < m_param3:
          require ext_call.return_data[32] <= m_param3
          require ext_code.size(mvaultContractAddress)
          call mvaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args addr(m_param2), caller, m_param3 - ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::depositPosition:BZxVault.withdrawToken deposit failed'
      require ext_call.return_data[0] + mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536 >= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536
      mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536 += ext_call.return_data[0]
      require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
      call moraclem[mstor10m[m_param1m]m.field_768m].0xfd670cbd with:
           gas gas_remaining wei
          args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, ext_call.return_data[0], mstor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, ')BZxLoanHealth::depositPosition:OracleInterface.didDepositPosition failed'
  mstor2 = 0
  mstor0 = 1
  return 1


# hash = 0xb7a025f9
# getter = ['storage', 160, 0, 8]
# const = None
# payable = True
def bZxTo0xContract() payable: 
  return mbZxTo0xContractAddress


# hash = 0xc4d66de8
# getter = None
# const = None
# payable = True
def initialize(address m_sender) payable: 
  require calldata.size - 4 >=′ 32
  require caller == mowner
  mstor39m[Mask(32, 224, ('name', 'stor6C64', 59270214650926482349764189863209587540947084731898323102022459520854313176618002166735941726008128822))m] = m_sender
  mstor39m[Mask(32, 224, ('name', 'stor2977', 314670265799158229021154762285524441673326758555173735815261779228073799381270279478))m] = m_sender
  mstor39m[Mask(32, 224, ('name', 'storFE63', 29456154062828672557473723247354683789153397515171478680395262379846516970189683))m] = m_sender
  mstor39m[Mask(32, 224, ('name', 'stor2077', 3759358406934317647883046264491191442455605918977129010104418545991709917066550))m] = m_sender
  mstor39m[Mask(32, 224, ('name', 'stor2964', 345363845990158578749239147842276833049654305397491675352759186696237954790302270405519791502646))m] = m_sender
  mstor39m[Mask(32, 224, ('name', 'stor2967', 1227326242933425195610638786373842767099986346445051720540204598784149518740190067))m] = m_sender
  mtargetsm[Mask(32, 224, sha3(0.00390625 / 'getTotalEscrow(bytes32,address)'))m] = m_sender


# hash = 0xcce37f3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 12]]]
# const = None
# payable = True
def orderFilledAmounts(bytes32 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return morderFilledAmountsm[m_param1m]


# hash = 0xd9fd7341
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 13]]]
# const = None
# payable = True
def orderCancelledAmounts(bytes32 m_param1) payable: 
  require calldata.size - 4 >=′ 32
  return morderCancelledAmountsm[m_param1m]


# hash = 0xde3f26eb
# getter = ['storage', 160, 0, 7]
# const = None
# payable = True
def oracleRegistryContract() payable: 
  return moracleRegistryContractAddress


# hash = 0xe53599c3
# getter = None
# const = None
# payable = True
def unknowne53599c3(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >=′ 64
  require 1 == mstor0
  mstor0 = 2
  mstor2 = gas_remaining + 21000
  if not mordersm[m_param1m]m.field_0:
      mstor2 = 0
      mstor0 = 1
      return 0
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768:
      mstor2 = 0
      mstor0 = 1
      return 0
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304:
      mstor2 = 0
      mstor0 = 1
      return 0
  require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
  static call moraclem[mstor10m[m_param1m]m.field_768m].'^?K<' with:
          gas gas_remaining wei
         args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 128
  if not ext_call.return_data[32]:
      mstor2 = 0
      mstor0 = 1
      return 0
  if not ext_call.return_data[0]:
      mstor2 = 0
      mstor0 = 1
      return 0
  if block.timestamp >= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048:
      mstor2 = 0
      mstor0 = 1
      return 0
  if m_param2 < ext_call.return_data[32]:
      if m_param2 <= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536:
          if not m_param2:
              mstor2 = 0
              mstor0 = 1
              return 0
          require ext_code.size(mvaultContractAddress)
          call mvaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, caller, m_param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawPosition: BZxVault.withdrawToken loan failed'
          require m_param2 <= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536
          mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536 -= m_param2
          require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
          call moraclem[mstor10m[m_param1m]m.field_768m].0xf2a2583a with:
               gas gas_remaining wei
              args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, m_param2, mstor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawPosition: OracleInterface.didWithdrawPosition failed'
          log LogWithdrawPosition(
                bytes32 loanOrderHash=_param2,
                address trader=loanPositions[stor16[_param1][caller]].field_1536,
                uint256 positionAmount=loanPositions[stor16[_param1][caller]].field_2560,
                uint256 remainingPosition=orders[_param1].field_2304,
                uint256 positionId=caller)
          mstor2 = 0
          mstor0 = 1
          return m_param2
  else:
      if ext_call.return_data[32] <= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536:
          if not ext_call.return_data[32]:
              mstor2 = 0
              mstor0 = 1
              return 0
          require ext_code.size(mvaultContractAddress)
          call mvaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, caller, ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawPosition: BZxVault.withdrawToken loan failed'
          require ext_call.return_data[32] <= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536
          mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536 -= ext_call.return_data[32]
          require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
          call moraclem[mstor10m[m_param1m]m.field_768m].0xf2a2583a with:
               gas gas_remaining wei
              args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, ext_call.return_data[32], mstor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawPosition: OracleInterface.didWithdrawPosition failed'
          log LogWithdrawPosition(
                bytes32 loanOrderHash=ext_call.return_data[32],
                address trader=loanPositions[stor16[_param1][caller]].field_1536,
                uint256 positionAmount=loanPositions[stor16[_param1][caller]].field_2560,
                uint256 remainingPosition=orders[_param1].field_2304,
                uint256 positionId=caller)
          mstor2 = 0
          mstor0 = 1
          return ext_call.return_data[32]
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536:
      mstor2 = 0
      mstor0 = 1
      return 0
  require ext_code.size(mvaultContractAddress)
  call mvaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
       gas gas_remaining wei
      args mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, caller, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, 'BZxLoanHealth::withdrawPosition: BZxVault.withdrawToken loan failed'
  require mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536 <= mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536
  mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536 = 0
  require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
  call moraclem[mstor10m[m_param1m]m.field_768m].0xf2a2583a with:
       gas gas_remaining wei
      args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mstor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, 'BZxLoanHealth::withdrawPosition: OracleInterface.didWithdrawPosition failed'
  log LogWithdrawPosition(
        bytes32 loanOrderHash=loanPositions[stor16[_param1][caller]].field_1536,
        address trader=loanPositions[stor16[_param1][caller]].field_1536,
        uint256 positionAmount=loanPositions[stor16[_param1][caller]].field_2560,
        uint256 remainingPosition=orders[_param1].field_2304,
        uint256 positionId=caller)
  mstor2 = 0
  mstor0 = 1
  return mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address m_newOwner) payable: 
  require calldata.size - 4 >=′ 32
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf4fb9b2f
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 17]]], ['cd', 36]]]
# const = None
# payable = True
def orderList(address m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >=′ 64
  require m_param2 < morderListm[m_param1m]
  return morderListm[m_param1m]m[m_param2m]


# hash = 0xf7a8c508
# getter = None
# const = None
# payable = True
def unknownf7a8c508(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >=′ 64
  if not mordersm[m_param1m]m.field_0:
      return 0
  if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768:
      return 0
  if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2304:
      return 0
  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_512 == mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_256:
      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_256 == mordersm[m_param1m]m.field_0:
          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 > mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768:
              if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 >= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                      return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                             0,
                             mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                      if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                          return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                 0,
                                 mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                          return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                 (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                 mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
          else:
              if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536:
                  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                      return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                      if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                          return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                          return 0, 
                                 (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                 mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
              else:
                  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                          return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536, 
                                 0,
                                 mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                          if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536, 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536, 
                                     (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
      else:
          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 <= 0:
              if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 > 0:
                  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 >= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                          return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                 0,
                                 mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                          if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                     (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
              else:
                  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 <= -mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                          return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                          if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                              return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                              return 0, 
                                     (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  else:
                      if -mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536, 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536, 
                                         0,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536, 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
          else:
              require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
              static call moraclem[mstor10m[m_param1m]m.field_768m].0x6599aa0 with:
                      gas gas_remaining wei
                     args mordersm[m_param1m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 96
              if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 > ext_call.return_data[64]:
                  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 - ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 >= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                          return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 - ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                 0,
                                 mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                          if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 - ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 - ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                     (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
              else:
                  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 <= ext_call.return_data[64] - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                          return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                          if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                              return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                              return 0, 
                                     (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  else:
                      if ext_call.return_data[64] - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536, 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536, 
                                         0,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536, 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
  else:
      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536 <= 0:
          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_256 == mordersm[m_param1m]m.field_0:
              if 0 > mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768:
                  if -mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 >= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                          return -mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                 0,
                                 mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                          if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                              return -mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                              return -mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                     (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
              else:
                  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                          return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                          if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                              return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                              return 0, 
                                     (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  else:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768, 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768, 
                                         0,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768, 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
          else:
              if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 <= 0:
                  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 <= 0:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                          return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                          if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                              return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                              return 0, 
                                     (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  else:
                      if 0 <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
              else:
                  require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
                  static call moraclem[mstor10m[m_param1m]m.field_768m].0x6599aa0 with:
                          gas gas_remaining wei
                         args mordersm[m_param1m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >=′ 96
                  if 0 > ext_call.return_data[64]:
                      if -ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 >= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return -ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return -ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                         0,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return -ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  else:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 <= ext_call.return_data[64]:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return 0, 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      else:
                          if ext_call.return_data[64] <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                              if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - ext_call.return_data[64], 
                                         0,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                                  if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                      return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - ext_call.return_data[64], 
                                             0,
                                             mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                                  if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                      return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - ext_call.return_data[64], 
                                             (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                             mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
      else:
          require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
          static call moraclem[mstor10m[m_param1m]m.field_768m].0x6599aa0 with:
                  gas gas_remaining wei
                 args mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1536
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 96
          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_256 == mordersm[m_param1m]m.field_0:
              if ext_call.return_data[64] > mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768:
                  if ext_call.return_data[64] - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 >= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                          return ext_call.return_data[64] - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                 0,
                                 mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                          if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                              return ext_call.return_data[64] - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                              return ext_call.return_data[64] - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                     (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
              else:
                  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 - ext_call.return_data[64]:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                          return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                          if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                              return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                              return 0, 
                                     (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  else:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 - ext_call.return_data[64] <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + ext_call.return_data[64], 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + ext_call.return_data[64], 
                                         0,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 - mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 + ext_call.return_data[64], 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
          else:
              if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768 <= 0:
                  if ext_call.return_data[64] > 0:
                      if ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 >= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                     0,
                                     mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                         0,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return ext_call.return_data[64] + mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  else:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 <= -ext_call.return_data[64]:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return 0, 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      else:
                          if -ext_call.return_data[64] <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                              if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 + ext_call.return_data[64], 
                                         0,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                                  if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                      return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 + ext_call.return_data[64], 
                                             0,
                                             mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                                  if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                      return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 + ext_call.return_data[64], 
                                             (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                             mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
              else:
                  require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
                  static call moraclem[mstor10m[m_param1m]m.field_768m].0x6599aa0 with:
                          gas gas_remaining wei
                         args mordersm[m_param1m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >=′ 96
                  if ext_call.return_data[64] > ext_call.return_data[64]:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 >= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                  else:
                      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280 <= 0:
                          if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                              return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                          if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                              if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                  return 0, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                  return 0, 
                                         (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                         mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                      else:
                          if 0 <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280:
                              if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 <= block.timestamp:
                                  return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                              if block.timestamp <= mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048:
                                  if not mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp:
                                      return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 0, mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
                                  if (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 - block.timestamp == mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0:
                                      return mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_1280, 
                                             (mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2048 * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) - (block.timestamp * mtraderLoanInterestm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_0) / 24 * 3600,
                                             mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768
  revert


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert with 0, 'fallback not allowed'


