# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xA5ba609B260284865Ad2987383493eE27C31Fb9f 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x95eb84c0': 'unknown95eb84c0(?)'} 

# storage definitions
def storage:
    # storage address 1
    owner # mask: a s
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
    bZxTo0xV2ContractAddress # mask: a s
    # storage address 9
    DEBUG_MODE # mask: a s
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
    # storage address 19477241400247949911419557613101861442939480356726391298614698583888311039039608088296577469792662202188216407536805948961320988688788826389795291219025507959669873706302594390995310092595663353276231532
    stor19477241400247949911419557613101861442939480356726391298614698583888311039039608088296577469792662202188216407536805948961320988688788826389795291219025507959669873706302594390995310092595663353276231532
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
  mstor39m[Mask(32, 224, ('name', 'storFE74', 19477241400247949911419557613101861442939480356726391298614698583888311039039608088296577469792662202188216407536805948961320988688788826389795291219025507959669873706302594390995310092595663353276231532))m] = m_sender


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


