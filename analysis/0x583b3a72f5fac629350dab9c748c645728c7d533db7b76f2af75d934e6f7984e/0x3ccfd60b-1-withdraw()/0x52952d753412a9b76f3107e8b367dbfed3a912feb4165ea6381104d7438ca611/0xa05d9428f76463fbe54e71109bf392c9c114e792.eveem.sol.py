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
def adjustFeeMode(uint8 _newMode): # not payable
  require caller == owner
  require _newMode <= 1
  feeMode = _newMode
  return 1


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 11]]]], ['loc', 11]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x280dd460
# getter = None
# const = None
# payable = False
def adjustFeePercentage(uint256 _newPercentage): # not payable
  require caller == owner
  require _newPercentage <= 10000
  feePercentage = _newPercentage
  return 1


# hash = 0x46479541
# getter = None
# const = None
# payable = False
def setWalletId(address _newWallet): # not payable
  require caller == owner
  require _newWallet
  stor10 = _newWallet
  return 1


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 14]]]], ['loc', 14]]]
# const = None
# payable = False
def version(): # not payable
  return version[0 len version.length]


# hash = 0x5faa299a
# getter = None
# const = None
# payable = False
def unknown5faa299a(uint256 _param1, addr _param2): # not payable
  if stor5[caller][_param1]:
      return bool(stor4[caller][_param1][addr(_param2)])
  return 1


# hash = 0x69e15404
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def feeAmount(): # not payable
  return feeAmount


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipRenounced(address previousOwner=owner)
  owner = 0


# hash = 0x7284e416
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 12]]]], ['loc', 12]]]
# const = None
# payable = False
def description(): # not payable
  return description[0 len description.length]


# hash = 0x866fd38e
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 4]]]]]]]]
# const = None
# payable = False
def unknown866fd38e(addr _param1, uint256 _param2, addr _param3): # not payable
  return bool(stor4[_param1][_param2][_param3])


# hash = 0x8719e8ac
# getter = None
# const = None
# payable = False
def unknown8719e8ac(uint256 _param1, bool _param2): # not payable
  stor5[caller][_param1] = uint8(_param2)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x919253e8
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 5]]]]]]
# const = None
# payable = False
def unknown919253e8(addr _param1, uint256 _param2): # not payable
  return bool(stor5[_param1][_param2])


# hash = 0x977919bf
# getter = None
# const = None
# payable = False
def adjustFeeAmount(uint256 _newAmount): # not payable
  require caller == owner
  feeAmount = _newAmount
  return 1


# hash = 0x99a5d747
# getter = None
# const = None
# payable = False
def calculateFee(uint256 _value): # not payable
  require feeMode <= 1
  if feeMode:
      require feeMode <= 1
      if feeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      return feeAmount
  if not _value:
      return 0
  require feePercentage * _value / _value == feePercentage
  return (feePercentage * _value / 10000)


# hash = 0xa001ecdd
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def feePercentage(): # not payable
  return feePercentage


# hash = 0xb188c70d
# getter = ['storage', 8, 160, 7]
# const = None
# payable = False
def feeMode(): # not payable
  require feeMode <= 1
  return feeMode


# hash = 0xb65c7c81
# getter = None
# const = None
# payable = False
def unknownb65c7c81(): # not payable
  require feeMode <= 1
  require feeMode <= 1
  if feeMode:
      if feeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      if feeAmount > 0:
          require ext_code.size(MOTAddress)
          call MOTAddress.balanceOf(address owner) with:
               gas gas_remaining wei
              args caller
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] >= feeAmount
          require ext_code.size(MOTAddress)
          call MOTAddress.allowance(address owner, address spender) with:
               gas gas_remaining wei
              args caller, this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] >= feeAmount
  if feeMode:
      require feeMode <= 1
      if feeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      if feeAmount:
          require ext_code.size(MOTAddress)
          call MOTAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args caller, stor10, feeAmount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
  [94midx = 0
  while [94midx < ('cd', 4).length:
      require addr(cd[((32 * [94midx) + cd[4] + 36)]) != 0
      require [94midx < ('cd', 4).length
      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
      mem[32] = sha3(cd[36], sha3(caller, 4))
      stor4[caller][cd[36]][addr(cd[((32 * [94midx) + cd[4] + 36)])] = uint8(bool(cd[68]))
      [94midx = [94midx + 1
      continue 
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
  return MOTAddress


# hash = 0xc892693b
# getter = None
# const = None
# payable = False
def setMotAddress(address _motAddress): # not payable
  require caller == owner
  require _motAddress
  require MOTAddress != _motAddress
  MOTAddress = _motAddress
  mem[128] = 'MOT'
  mem[131 len 0] = None
  mem[131] = Mask(208, 0, 'MOT'), mem[160 len 3]
  [94m_31 = sha3(mem[131 len 3])
  mem[131] = 0x95d89b4100000000000000000000000000000000000000000000000000000000
  require ext_code.size(MOTAddress)
  call MOTAddress.symbol() with:
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
  return category[0 len category.length]


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require caller == owner
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


