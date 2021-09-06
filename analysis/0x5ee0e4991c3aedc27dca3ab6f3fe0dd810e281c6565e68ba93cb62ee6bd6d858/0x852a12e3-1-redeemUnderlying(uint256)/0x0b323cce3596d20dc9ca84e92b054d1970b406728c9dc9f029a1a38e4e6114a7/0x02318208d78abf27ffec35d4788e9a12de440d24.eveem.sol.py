# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x02318208d78abF27fFEc35D4788E9A12dE440d24 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x59690e70': 'unknown59690e70(?)', '0x5f2d554b': 'unknown5f2d554b(?)', '0x6db153de': 'unknown6db153de(?)', '0x7461df11': 'unknown7461df11(?)', '0xf7fa7202': 'unknownf7fa7202(?)'} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    unknown5f82c67eAddress # mask: a s
    # storage address 2
    unknown38013f02Address # mask: a s
    # storage address 3
    unknown878f7603Address # mask: a s
    # storage address 4
    unknown50fbd642Address # mask: a s
    # storage address 5
    stake # mask: a s
    # storage address 6
    unknown2fe7d446 # mask: a s
    # storage address 7
    unknown62141fcc # mask: a s
    # storage address 8
    unknown2f884710 # mask: a s
    # storage address 9
    unknown03eeb4ca # mask: a s
    # storage address 10
    unknown94d5567a # mask: a s
    # storage address 11
    unknown6f17591f # mask: a s
    # storage address 11
    unknown76017b64Address # mask: a s
    # storage address 11
    unknowne852e741 # mask: a s
    # storage address 12
    logicContractAddress # mask: a s
    # storage address 13
    unknownd95393ebAddress # mask: a s
    # storage address 14
    unknowncb0ef21dAddress # mask: a s
# hash = 0x03eeb4ca
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknown03eeb4ca(): # not payable
  return unknown03eeb4ca


# hash = 0x2e27f486
# getter = None
# const = None
# payable = False
def unknown2e27f486(): # not payable
  mem[132 len 0] = None
  [93mdelegate logicContractAddress.mem[132 len 4] with:
       gas gas_remaining wei
      args 
  require return_data.size
  mem[164 len return_data.size] = ext_call.return_data[0 len return_data.size]
  require delegate.return_code
  require return_data.size >= 32
  mem[ceil32(return_data.size) + 133] = mem[164]
  return memory
    from ceil32(return_data.size) + 133
     [93mlen 32


# hash = 0x2f884710
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def unknown2f884710(): # not payable
  return unknown2f884710


# hash = 0x2fe7d446
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def unknown2fe7d446(): # not payable
  return unknown2fe7d446


# hash = 0x38013f02
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknown38013f02(): # not payable
  return unknown38013f02Address


# hash = 0x3a4b66f1
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def stake(): # not payable
  return stake


# hash = 0x3bc3c23b
# getter = None
# const = None
# payable = False
def unknown3bc3c23b(): # not payable
  mem[132 len 0] = None
  [93mdelegate logicContractAddress.mem[132 len 4] with:
       gas gas_remaining wei
      args 
  require return_data.size
  mem[164 len return_data.size] = ext_call.return_data[0 len return_data.size]
  require delegate.return_code
  require return_data.size >= 64
  [94m_30 = mem[196]
  mem[ceil32(return_data.size) + 133] = bool(mem[164])
  return mem[ceil32(return_data.size) + 133], [94m_30


# hash = 0x50fbd642
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def unknown50fbd642(): # not payable
  return unknown50fbd642Address


# hash = 0x5f82c67e
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknown5f82c67e(): # not payable
  return unknown5f82c67eAddress


# hash = 0x62141fcc
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def unknown62141fcc(): # not payable
  return unknown62141fcc


# hash = 0x6f17591f
# getter = ['bool', ['storage', 8, 168, 11]]
# const = None
# payable = False
def unknown6f17591f(): # not payable
  return bool(unknown6f17591f)


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  owner = 0


# hash = 0x76017b64
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def unknown76017b64(): # not payable
  return unknown76017b64Address


# hash = 0x878f7603
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknown878f7603(): # not payable
  return unknown878f7603Address


# hash = 0x8b98a2c5
# getter = None
# const = ['return', ['data', 32, 4, 0]]
# payable = False
const unknown8b98a2c5 = ''


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = False
def isOwner(): # not payable
  return (caller == owner)


# hash = 0x94d5567a
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknown94d5567a(): # not payable
  return unknown94d5567a


# hash = 0xab7b1c89
# getter = None
# const = None
# payable = False
def unknownab7b1c89(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  [93mdelegate logicContractAddress.0xab7b1c89 with:
       gas gas_remaining wei
      args Mask(224, 32, _param1) >> 32, mem[196 len 4]
  require delegate.return_code


# hash = 0xcb0ef21d
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def unknowncb0ef21d(): # not payable
  return unknowncb0ef21dAddress


# hash = 0xcc0e97c9
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def logicContract(): # not payable
  return logicContractAddress


# hash = 0xcd61a95a
# getter = None
# const = None
# payable = False
def sellOrder(uint256 _sellPrice, uint256 _amount): # not payable
  require calldata.size - 4 >= 64
  mem[196 len 64] = sellOrder(uint256 sellPrice, uint256 amount), _sellPrice, Mask(224, 32, _amount) >> 32
  mem[288 len 4] = uint32(_amount)
  [93mdelegate logicContractAddress with:
     funct uint32(_sellPrice)
       gas gas_remaining wei
      args Mask(224, 32, _amount) << 224, mem[260 len 4]
  if not return_data.size:
      require delegate.return_code
      return sellOrder(uint256 sellPrice, uint256 amount), _sellPrice, Mask(224, 32, _amount) >> 32
  mem[228 len return_data.size] = ext_call.return_data[0 len return_data.size]
  require delegate.return_code
  require return_data.size >= 64
  [94m_31 = mem[260 len 28], uint32(_amount)
  mem[ceil32(return_data.size) + 197] = mem[228]
  return mem[ceil32(return_data.size) + 197], [94m_31


# hash = 0xd95393eb
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknownd95393eb(): # not payable
  return unknownd95393ebAddress


# hash = 0xe852e741
# getter = ['bool', ['storage', 8, 160, 11]]
# const = None
# payable = False
def unknowne852e741(): # not payable
  return bool(unknowne852e741)


# hash = 0xef46e0ca
# getter = None
# const = None
# payable = False
def executeOrder(uint256 _assetId, uint256 _price): # not payable
  require calldata.size - 4 >= 64
  [93mdelegate logicContractAddress with:
     funct uint32(_assetId)
       gas gas_remaining wei
      args Mask(224, 32, _price) << 224, mem[260 len 4]
  require delegate.return_code


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require calldata.size - 4 >= 32
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
  stop


