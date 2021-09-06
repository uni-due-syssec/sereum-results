# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x12c3Aa88A66c0b7de8a81052e6Da467Ee66B2517 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    feeMode # mask: a s
    # storage address 1
    MOTAddress # mask: a s
    # storage address 2
    feePercentage # mask: a s
    # storage address 3
    feeAmount # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 9
    name
    # storage address 10
    description
    # storage address 11
    category
    # storage address 12
    version
    # storage address 13
    unknown21a244e5
    # storage address 14
    stor14
# hash = 0x061d7db7
# getter = None
# const = None
# payable = False
def adjustFeeMode(uint8 m_newMode): # not payable
  require caller == mowner
  require m_newMode <= 1
  mfeeMode = m_newMode
  return 1


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 9]]]], ['loc', 9]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x21a244e5
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 13]]]
# const = None
# payable = False
def unknown21a244e5(addr m_param1): # not payable
  return munknown21a244e5m[m_param1m]


# hash = 0x280dd460
# getter = None
# const = None
# payable = False
def adjustFeePercentage(uint256 m_newPercentage): # not payable
  require caller == mowner
  require m_newPercentage <= 10000
  mfeePercentage = m_newPercentage
  return 1


# hash = 0x46479541
# getter = None
# const = None
# payable = False
def setWalletId(address m_newWallet): # not payable
  require caller == mowner
  require m_newWallet
  mstor4 = m_newWallet
  return 1


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 12]]]], ['loc', 12]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x69e15404
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def feeAmount(): # not payable
  return mfeeAmount


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x7284e416
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 10]]]], ['loc', 10]]]
# const = None
# payable = False
def description(): # not payable
  return mdescriptionm[0 len mdescriptionm.lengthm]


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x977919bf
# getter = None
# const = None
# payable = False
def adjustFeeAmount(uint256 m_newAmount): # not payable
  require caller == mowner
  mfeeAmount = m_newAmount
  return 1


# hash = 0x99a5d747
# getter = None
# const = None
# payable = False
def calculateFee(uint256 m_value): # not payable
  require mfeeMode <= 1
  if not mfeeMode:
      return (m_value * mfeePercentage / 10000)
  require mfeeMode <= 1
  if mfeeMode != 1:
      revert with 0, 'Unsupported fee mode.'
  return mfeeAmount


# hash = 0xa001ecdd
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def feePercentage(): # not payable
  return mfeePercentage


# hash = 0xa6c30b29
# getter = None
# const = None
# payable = False
def unknowna6c30b29(): # not payable
  require not mstor14m[callerm]
  require eth.balance(caller) > 0
  munknown21a244e5m[callerm] = gas_remaining
  mstor14m[callerm] = 1


# hash = 0xb188c70d
# getter = ['storage', 8, 160, 1]
# const = None
# payable = False
def feeMode(): # not payable
  require mfeeMode <= 1
  return mfeeMode


# hash = 0xc55c4115
# getter = None
# const = ['return', 10000]
# payable = False
const FEE_CHARGER_DENOMINATOR = 10000


# hash = 0xc642f094
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def MOT(): # not payable
  return mMOTAddress


# hash = 0xc892693b
# getter = None
# const = None
# payable = False
def setMotAddress(address m_motAddress): # not payable
  require caller == mowner
  require m_motAddress
  require mMOTAddress != m_motAddress
  mMOTAddress = m_motAddress
  mem[128] = 'MOT'
  mem[96] = 3
  mem[131 len 0] = None
  mem[131] = Mask(208, 0, 'MOT'), mem[160 len 3]
  [94m_31 = sha3(mem[131 len 3])
  mem[131] = 0x95d89b4100000000000000000000000000000000000000000000000000000000
  require ext_code.size(mMOTAddress)
  call mMOTAddress.symbol() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[131 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 131
  require return_data.size >= 32
  require mem[131] <= 4294967296
  require mem[131] + 32 <= return_data.size
  require return_data.size >= mem[mem[131] + 131] + mem[131] + 32 and mem[mem[131] + 131] <= 4294967296
  [94m_38 = mem[mem[131] + 131]
  mem[ceil32(return_data.size) + 163 len floor32(mem[mem[131] + 131])] = mem[mem[131] + 163 len floor32(mem[mem[131] + 131])]
  mem[ceil32(return_data.size) + floor32(mem[mem[131] + 131]) + -(mem[mem[131] + 131] % 32) + 195 len mem[mem[131] + 131] % 32] = mem[mem[131] + floor32(mem[mem[131] + 131]) + -(mem[mem[131] + 131] % 32) + 195 len mem[mem[131] + 131] % 32]
  mem[[94m_38 + ceil32(return_data.size) + 163 len floor32([94m_38)] = mem[ceil32(return_data.size) + 163 len floor32([94m_38)]
  mem[(2 * floor32([94m_38)) + ceil32(return_data.size) + 195 len [94m_38 % 32] = mem[ceil32(return_data.size) + floor32([94m_38) + -([94m_38 % 32) + 195 len [94m_38 % 32]
  require sha3(mem[[94m_38 + ceil32(return_data.size) + 163 len [94m_38]) == [94m_31
  return 1


# hash = 0xd3927c15
# getter = None
# const = None
# payable = False
def unknownd3927c15(): # not payable
  require mstor14m[callerm]
  require munknown21a244e5m[callerm] > 0
  require gas_remaining >= 10000
  require eth.balance(caller) > 0
  require (21000 * block.gasprice) + (munknown21a244e5m[callerm] * block.gasprice) - (gas_remaining * block.gasprice) <= eth.balance(caller)
  mstor14m[callerm] = 0
  munknown21a244e5m[callerm] = 0
  return ((21000 * block.gasprice) + (munknown21a244e5m[callerm] * block.gasprice) - (gas_remaining * block.gasprice))


# hash = 0xef430aa6
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 11]]]], ['loc', 11]]]
# const = None
# payable = False
def category(): # not payable
  return mcategorym[0 len mcategorym.lengthm]


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf435f5a7
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 14]]]]
# const = None
# payable = False
def lock(address m_owner): # not payable
  return bool(mstor14m[m_ownerm])


# hash = 0xffd50144
# getter = None
# const = ['return', 10000]
# payable = False
const unknownffd50144 = 10000


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


