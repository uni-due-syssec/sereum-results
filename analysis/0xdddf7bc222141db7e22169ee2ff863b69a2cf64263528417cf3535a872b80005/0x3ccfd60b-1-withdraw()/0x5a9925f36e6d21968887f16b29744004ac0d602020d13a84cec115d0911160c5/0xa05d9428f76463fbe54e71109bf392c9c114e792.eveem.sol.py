# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xA05d9428f76463fBE54e71109bf392c9C114e792 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 4
    stor4
    # storage address 5
    stor5
    # storage address 6
    owner # mask: a s
    # storage address 7
    MOTAddress # mask: a s
    # storage address 7
    feeMode # mask: a s
    # storage address 8
    feePercentage # mask: a s
    # storage address 9
    feeAmount # mask: a s
    # storage address 10
    stor10 # mask: a s
    # storage address 11
    name
    # storage address 12
    description
    # storage address 13
    category
    # storage address 14
    version
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
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 11]]]], ['loc', 11]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


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
  mstor10 = m_newWallet
  return 1


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 14]]]], ['loc', 14]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x5faa299a
# getter = None
# const = None
# payable = False
def unknown5faa299a(uint256 m_param1, addr m_param2): # not payable
  if mstor5m[callerm]m[m_param1m]:
      return bool(mstor4m[callerm]m[m_param1m]m[addr(m_param2)m])
  return 1


# hash = 0x69e15404
# getter = ['storage', 256, 0, 9]
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
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 12]]]], ['loc', 12]]]
# const = None
# payable = False
def description(): # not payable
  return mdescriptionm[0 len mdescriptionm.lengthm]


# hash = 0x866fd38e
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 4]]]]]]]]
# const = None
# payable = False
def unknown866fd38e(addr m_param1, uint256 m_param2, addr m_param3): # not payable
  return bool(mstor4m[m_param1m]m[m_param2m]m[m_param3m])


# hash = 0x8719e8ac
# getter = None
# const = None
# payable = False
def unknown8719e8ac(uint256 m_param1, bool m_param2): # not payable
  mstor5m[callerm]m[m_param1m] = uint8(m_param2)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x919253e8
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 5]]]]]]
# const = None
# payable = False
def unknown919253e8(addr m_param1, uint256 m_param2): # not payable
  return bool(mstor5m[m_param1m]m[m_param2m])


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
  if mfeeMode:
      require mfeeMode <= 1
      if mfeeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      return mfeeAmount
  if not m_value:
      return 0
  require mfeePercentage * m_value / m_value == mfeePercentage
  return (mfeePercentage * m_value / 10000)


# hash = 0xa001ecdd
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def feePercentage(): # not payable
  return mfeePercentage


# hash = 0xb188c70d
# getter = ['storage', 8, 160, 7]
# const = None
# payable = False
def feeMode(): # not payable
  require mfeeMode <= 1
  return mfeeMode


# hash = 0xb65c7c81
# getter = None
# const = None
# payable = False
def unknownb65c7c81(): # not payable
  require mfeeMode <= 1
  require mfeeMode <= 1
  if mfeeMode:
      if mfeeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      if mfeeAmount > 0:
          require ext_code.size(mMOTAddress)
          call mMOTAddress.balanceOf(address owner) with:
               gas gas_remaining wei
              args caller
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] >= mfeeAmount
          require ext_code.size(mMOTAddress)
          call mMOTAddress.allowance(address owner, address spender) with:
               gas gas_remaining wei
              args caller, this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] >= mfeeAmount
  if mfeeMode:
      require mfeeMode <= 1
      if mfeeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      if mfeeAmount:
          require ext_code.size(mMOTAddress)
          call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args caller, mstor10, mfeeAmount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      require addr(cd[((32 * [94midx) + cd[4] + 36)]) != 0
      require [94midx < m('cd', 4).length
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = sha3(cd[36], sha3(caller, 4))
      mstor4m[callerm]m[cd[36]m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = uint8(bool(cd[68]))
      [94midx = [94midx + 1
      mcontinue 
  return 1


# hash = 0xc55c4115
# getter = None
# const = ['return', 10000]
# payable = False
const FEE_CHARGER_DENOMINATOR = 10000


# hash = 0xc642f094
# getter = ['storage', 160, 0, 7]
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


# hash = 0xef430aa6
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 13]]]], ['loc', 13]]]
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


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


