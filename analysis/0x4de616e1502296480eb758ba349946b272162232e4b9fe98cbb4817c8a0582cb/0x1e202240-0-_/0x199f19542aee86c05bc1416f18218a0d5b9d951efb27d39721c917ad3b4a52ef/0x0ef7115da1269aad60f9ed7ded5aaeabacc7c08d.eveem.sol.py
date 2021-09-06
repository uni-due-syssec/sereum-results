# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x0EF7115dA1269AAD60F9ed7DEd5AaEaBaCc7c08D 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x229e0b16': 'unknown229e0b16(?)'} 

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
    # storage address 14563319108714636299656993787038929139863683616751058534425004095353235305553359800644236147
    stor14563319108714636299656993787038929139863683616751058534425004095353235305553359800644236147
    # storage address 14563319108714636313881142528467608147449384777707876736727982404118908968301067878961345395
    stor14563319108714636313881142528467608147449384777707876736727982404118908968301067878961345395
    # storage address 657076066398364225529838432376929932492728515619368335845332051488632707330923217557107083741321696577649810259918887990582
    stor657076066398364225529838432376929932492728515619368335845332051488632707330923217557107083741321696577649810259918887990582
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


# hash = 0x438d1df0
# getter = None
# const = None
# payable = True
def unknown438d1df0(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >=′ 64
  if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_768:
      if mloanPositionsm[mstor16m[m_param1m]m[addr(m_param2)m]m]m.field_2304:
          return 1
      else:
          return 0
  else:
      return 0


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


# hash = 0x7465577a
# getter = None
# const = None
# payable = True
def unknown7465577a(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >=′ 64
  require 1 == mstor0
  mstor0 = 2
  mstor2 = gas_remaining + 21000
  if morderLenderm[m_param1m] != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  ')BZxLoanMaintenance::changeLendeOwnership: msg.sender is not the lender in this position'
  if morderListIndexm[m_param1m]m[addr(m_param2)m]m.field_256:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  ')BZxLoanMaintenance::changeLendeOwnership: new owner is invalid'
  if not mordersm[m_param1m]m.field_0:
      revert with 0, ')BZxLoanMaintenance::changeLendeOwnership: loanOrder.loanTokenAddress == address(0)'
  if morderListIndexm[m_param1m]m[callerm]m.field_256:
      require morderListm[callerm] > 0
      if 1 < morderListm[callerm]:
          require morderListm[callerm] - 1 < morderListm[callerm]
          require morderListIndexm[m_param1m]m[callerm]m.field_0 < morderListm[callerm]
          morderListm[callerm]m[mstor18m[m_param1m]m[callerm]m.field_0m] = morderListm[callerm]m[morderListm[callerm]m]
          require morderListIndexm[m_param1m]m[callerm]m.field_0 < morderListm[callerm]
          morderListIndexm[mstor17m[callerm]m[morderListIndexm[m_param1m]m[callerm]m.field_0m]m]m[callerm]m.field_0 = morderListIndexm[m_param1m]m[callerm]m.field_0
      morderListm[callerm]--
      if morderListm[callerm] > morderListm[callerm] - 1:
          [94midx = morderListm[callerm] - 1
          mwhile morderListm[callerm] > [94midxm:
              morderListm[callerm]m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      morderListIndexm[m_param1m]m[callerm]m.field_0 = 0
      morderListIndexm[m_param1m]m[callerm]m.field_256 = 0
  morderLenderm[m_param1m] = m_param2
  morderListm[addr(m_param2)m]++
  morderListm[addr(m_param2)m]m[morderListm[addr(m_param2)m]m] = m_param1
  morderListIndexm[m_param1m]m[addr(m_param2)m]m.field_0 = morderListm[addr(m_param2)m] - 1
  morderListIndexm[m_param1m]m[addr(m_param2)m]m.field_256 = 1
  require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
  call moraclem[mstor10m[m_param1m]m.field_768m].0x5bdf0751 with:
       gas gas_remaining wei
      args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, caller, addr(m_param2), mstor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, ')BZxLoanMaintenance::changeLendeOwnership: OracleInterface.didChangeLenderOwnership failed'
  log LogChangeLenderOwnership(
        bytes32 loanOrderHash=orders[_param1].field_2304,
        address oldOwner=caller,
        address newOwner=_param2)
  mstor2 = 0
  mstor0 = 1
  return 1


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


# hash = 0xb71a86ce
# getter = None
# const = None
# payable = True
def unknownb71a86ce(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >=′ 64
  require 1 == mstor0
  mstor0 = 2
  mstor2 = gas_remaining + 21000
  if morderListIndexm[m_param1m]m[addr(m_param2)m]m.field_256:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  ')BZxLoanMaintenance::changeTradeOwnership: new owner is invalid'
  if not mordersm[m_param1m]m.field_0:
      revert with 0, ')BZxLoanMaintenance::changeTradeOwnership: loanOrder.loanTokenAddress == address(0)'
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768:
      revert with 0, ')BZxLoanMaintenance::changeTradeOwnership: loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if not mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304:
      revert with 0, ')BZxLoanMaintenance::changeTradeOwnership: loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0 != caller:
      revert with 0, ')BZxLoanMaintenance::changeTradeOwnership: msg.sender is not the trader in this position'
  mloanPositionsIdsm[m_param1m]m[callerm] = 0
  if morderListIndexm[m_param1m]m[callerm]m.field_256:
      require morderListm[callerm] > 0
      if 1 < morderListm[callerm]:
          require morderListm[callerm] - 1 < morderListm[callerm]
          require morderListIndexm[m_param1m]m[callerm]m.field_0 < morderListm[callerm]
          morderListm[callerm]m[mstor18m[m_param1m]m[callerm]m.field_0m] = morderListm[callerm]m[morderListm[callerm]m]
          require morderListIndexm[m_param1m]m[callerm]m.field_0 < morderListm[callerm]
          morderListIndexm[mstor17m[callerm]m[morderListIndexm[m_param1m]m[callerm]m.field_0m]m]m[callerm]m.field_0 = morderListIndexm[m_param1m]m[callerm]m.field_0
      morderListm[callerm]--
      if morderListm[callerm] > morderListm[callerm] - 1:
          [94midx = morderListm[callerm] - 1
          mwhile morderListm[callerm] > [94midxm:
              morderListm[callerm]m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      morderListIndexm[m_param1m]m[callerm]m.field_0 = 0
      morderListIndexm[m_param1m]m[callerm]m.field_256 = 0
  mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0 = m_param2
  mloanPositionsIdsm[m_param1m]m[addr(m_param2)m] = mloanPositionsIdsm[m_param1m]m[callerm]
  morderListm[addr(m_param2)m]++
  morderListm[addr(m_param2)m]m[morderListm[addr(m_param2)m]m] = m_param1
  morderListIndexm[m_param1m]m[addr(m_param2)m]m.field_0 = morderListm[addr(m_param2)m] - 1
  morderListIndexm[m_param1m]m[addr(m_param2)m]m.field_256 = 1
  require ext_code.size(moraclem[mstor10m[m_param1m]m.field_768m])
  call moraclem[mstor10m[m_param1m]m.field_768m].0x7d0cdec3 with:
       gas gas_remaining wei
      args mordersm[m_param1m]m.field_0, mordersm[m_param1m]m.field_256, mordersm[m_param1m]m.field_512, mordersm[m_param1m]m.field_768, mordersm[m_param1m]m.field_1024, mordersm[m_param1m]m.field_1280, mordersm[m_param1m]m.field_1536, mordersm[m_param1m]m.field_1792, mordersm[m_param1m]m.field_2048, mordersm[m_param1m]m.field_2304, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_0, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_256, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_512, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_768, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1024, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1280, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1536, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_1792, mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2048, bool(mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2304), mloanPositionsm[mstor16m[m_param1m]m[callerm]m]m.field_2560, caller, mstor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, ')BZxLoanMaintenance::changeTradeOwnership: OracleInterface.didChangeTraderOwnership failed'
  log LogChangeTraderOwnership(
        bytes32 loanOrderHash=orders[_param1].field_2304,
        address oldOwner=caller,
        address newOwner=_param2)
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
  mstor39m[Mask(32, 224, ('name', 'stor7263', 14563319108714636313881142528467608147449384777707876736727982404118908968301067878961345395))m] = m_sender
  mstor39m[Mask(32, 224, ('name', 'stor7263', 14563319108714636299656993787038929139863683616751058534425004095353235305553359800644236147))m] = m_sender
  mstor39m[Mask(32, 224, ('name', 'storFE75', 657076066398364225529838432376929932492728515619368335845332051488632707330923217557107083741321696577649810259918887990582))m] = m_sender
  mtargetsm[Mask(32, 224, sha3(0.00390625 / 'isPositionOpen(bytes32,address)'))m] = m_sender
  mtargetsm[Mask(32, 224, sha3('setLoanOrderDesc(bytes32,string)'))m] = m_sender


# hash = 0xc8319c61
# getter = None
# const = None
# payable = True
def unknownc8319c61() payable: 
  require calldata.size - 4 >=′ 64
  require cd[36] <= 18446744073709551615
  require calldata.size >′ cd[36] + 35
  require m('cd', 36).length <= 18446744073709551615
  require cd[36] + m('cd', 36).length + 36 <= calldata.size
  require 1 == mstor0
  mstor0 = 2
  mstor2 = gas_remaining + 21000
  if mstor11m[cd[4]m]m.field_0 != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  'BZxLoanMaintenance::setLoanOrderDesc: loanOrderAux.makerAddress != msg.sender'
  mstor11m[cd[4]m]m.field_2304 = (2 * m('cd', 36).length) + 1
  [94ms = 0
  [94midx = cd[36] + 36
  mwhile cd[36] + m('cd', 36).length + 36 > [94midxm:
      mstor11m[cd[4]m]m[[94ms + 9m]m.field_0 = cd[[94midx]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      mcontinue 
  [94midx = Mask(251, 0, m('cd', 36).length + 31) >> 5
  mwhile mstor11m[cd[4]m]m[9m]m.length + 31 / 32 > [94midxm:
      mstor11m[cd[4]m]m[[94midx + 9m]m.field_0 = 0
      [94midx = [94midx + 1
      mcontinue 
  mstor2 = 0
  mstor0 = 1
  return 1


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


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert with 0, 'fallback not allowed'


