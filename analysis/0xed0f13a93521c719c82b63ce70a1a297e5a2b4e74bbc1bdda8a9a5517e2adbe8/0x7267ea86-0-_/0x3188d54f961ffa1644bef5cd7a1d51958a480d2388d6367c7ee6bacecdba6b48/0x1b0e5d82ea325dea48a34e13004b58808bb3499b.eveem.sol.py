# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x1B0e5d82EA325DEA48A34e13004B58808BB3499B 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x473ac3ed': 'unknown473ac3ed(?)', '0x7267ea86': 'unknown7267ea86(?)', '0x88788f71': 'unknown88788f71(?)'} 

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
    # storage address 314077755436407835579166785924651578029017063492875439391122844475994613090633266486
    stor314077755436407835579166785924651578029017063492875439391122844475994613090633266486
    # storage address 9116240346629778611544642497426355420922274765357132336487647104597442812329491707313637076434203893183798
    stor9116240346629778611544642497426355420922274765357132336487647104597442812329491707313637076434203893183798
    # storage address 15302688835956636895082872600760033051118199715947966345941300693962120731031717322773901573417949012419731812136246
    stor15302688835956636895082872600760033051118199715947966345941300693962120731031717322773901573417949012419731812136246
# hash = 0x093983bd
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 14]]]
# const = None
# payable = True
def orderLender(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return orderLender[_param1]


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
  stor39[Mask(32, 224, ('name', 'stor2963', 314077755436407835579166785924651578029017063492875439391122844475994613090633266486))] = _sender
  stor39[Mask(32, 224, ('name', 'storFE63', 9116240346629778611544642497426355420922274765357132336487647104597442812329491707313637076434203893183798))] = _sender
  stor39[Mask(32, 224, ('name', 'stor636C', 15302688835956636895082872600760033051118199715947966345941300693962120731031717322773901573417949012419731812136246))] = _sender


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


# hash = 0xde3f26eb
# getter = ['storage', 160, 0, 7]
# const = None
# payable = True
def oracleRegistryContract() payable: 
  return oracleRegistryContractAddress


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


