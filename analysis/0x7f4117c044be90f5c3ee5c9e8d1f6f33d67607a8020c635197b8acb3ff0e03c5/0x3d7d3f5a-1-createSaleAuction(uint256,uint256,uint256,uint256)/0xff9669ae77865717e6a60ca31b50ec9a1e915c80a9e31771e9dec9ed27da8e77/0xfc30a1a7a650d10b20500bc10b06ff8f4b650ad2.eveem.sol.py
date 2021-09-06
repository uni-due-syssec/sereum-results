# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xfc30a1a7A650d10B20500BC10b06ff8F4B650AD2 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0xe25c5bce': 'unknowne25c5bce(?)'} 

# storage definitions
def storage:
    # storage address 0
    unknown55909f87 # mask: a s
    # storage address 0
    owner # mask: a s
    # storage address 1
    unknown64c66395
    # storage address 2
    unknownbe8fb1c1
    # storage address 3
    stor3
    # storage address 4
    stor4
    # storage address 5
    stor5
    # storage address 6
    stor6
    # storage address 7
    unknown7944013a
# hash = 0x051f403f
# getter = None
# const = ['return', 1]
# payable = False
const unknown051f403f = 1


# hash = 0x0cc29d29
# getter = None
# const = None
# payable = False
def unknown0cc29d29(uint256 _param1): # not payable
  [94midx = 224
  [94ms = 0
  while 352 > [94midx + 32:
      mem[[94midx + 32] = stor6[_param1][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return stor6[_param1].field_0, mem[256 len 96]


# hash = 0x2292bc1e
# getter = None
# const = None
# payable = False
def unknown2292bc1e(uint256 _param1): # not payable
  [94midx = 224
  [94ms = 1
  while 288 > [94midx + 32:
      mem[[94midx + 32] = stor5[_param1][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return stor5[_param1].field_0, stor5[_param1].field_256, mem[256]


# hash = 0x30346966
# getter = None
# const = None
# payable = False
def unknown30346966(): # not payable
  require caller == owner
  [94ms = 0
  [94midx = 36
  while 164 > [94midx:
      stor6[cd[4]][[94ms].field_0 = cd[[94midx]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 4
  while 4 > [94midx:
      stor6[cd[4]][[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 


# hash = 0x55909f87
# getter = ['bool', ['storage', 8, 160, 0]]
# const = None
# payable = False
def unknown55909f87(): # not payable
  return bool(unknown55909f87)


# hash = 0x627fe2e7
# getter = None
# const = None
# payable = False
def unknown627fe2e7(): # not payable
  require caller == owner
  unknownbe8fb1c1[cd[4]].field_0 = cd[36]
  [94ms = 1
  [94midx = 68
  while 100 > [94midx:
      unknownbe8fb1c1[cd[4]][[94ms].field_0 = cd[[94midx]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 2
  while 2 > [94midx:
      unknownbe8fb1c1[cd[4]][[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 


# hash = 0x64c66395
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def unknown64c66395(uint256 _param1): # not payable
  return unknown64c66395[_param1]


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipRenounced(address previousOwner=owner)
  owner = 0


# hash = 0x74554de4
# getter = None
# const = None
# payable = False
def unknown74554de4(): # not payable
  require caller == owner
  [94ms = 0
  [94midx = 36
  while 164 > [94midx:
      stor4[cd[4]][[94ms].field_0 = cd[[94midx]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 4
  while 4 > [94midx:
      stor4[cd[4]][[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 


# hash = 0x7944013a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 7]]]]]
# const = None
# payable = False
def unknown7944013a(uint256 _param1, uint256 _param2): # not payable
  return unknown7944013a[_param1][_param2]


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x9761a68a
# getter = None
# const = None
# payable = False
def unknown9761a68a(uint256 _param1): # not payable
  [94midx = 256
  [94ms = 1
  while 352 > [94midx + 32:
      mem[[94midx + 32] = stor4[_param1][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return stor4[_param1].field_0, stor4[_param1].field_256, mem[288 len 64]


# hash = 0xb0c93bba
# getter = None
# const = None
# payable = False
def unknownb0c93bba(uint256 _param1, uint256 _param2): # not payable
  require caller == owner
  unknown64c66395[_param1] = _param2


# hash = 0xbe8fb1c1
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def unknownbe8fb1c1(uint256 _param1): # not payable
  [94midx = 192
  [94ms = 1
  while 224 > [94midx + 32:
      mem[[94midx + 32] = unknownbe8fb1c1[_param1][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return unknownbe8fb1c1[_param1].field_0, unknownbe8fb1c1[_param1].field_256


# hash = 0xc6aad68c
# getter = None
# const = None
# payable = False
def unknownc6aad68c(): # not payable
  require caller == owner
  stor3[cd[4]].field_0 = cd[36]
  [94ms = 1
  [94midx = 68
  while 132 > [94midx:
      stor3[cd[4]][[94ms].field_0 = cd[[94midx]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 3
  while 3 > [94midx:
      stor3[cd[4]][[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 


# hash = 0xccf9bbb6
# getter = None
# const = None
# payable = False
def unknownccf9bbb6(uint256 _param1): # not payable
  if not _param1:
      return 1, 10
  if _param1 == 1:
      return 21, 7
  if _param1 == 2:
      return 41, 6
  if _param1 != 3:
      return code.data[2869 len 32], code.data[2901 len 32]
  return 61, 6


# hash = 0xe4c5efe9
# getter = None
# const = None
# payable = False
def unknowne4c5efe9(uint256 _param1): # not payable
  [94midx = 224
  [94ms = 1
  while 288 > [94midx + 32:
      mem[[94midx + 32] = stor3[_param1][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return stor3[_param1].field_0, stor3[_param1].field_256, mem[256]


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


# hash = 0xf8a7b163
# getter = None
# const = None
# payable = False
def unknownf8a7b163(): # not payable
  require caller == owner
  stor5[cd[4]].field_0 = cd[36]
  [94ms = 1
  [94midx = 68
  while 132 > [94midx:
      stor5[cd[4]][[94ms].field_0 = cd[[94midx]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      continue 
  [94midx = 3
  while 3 > [94midx:
      stor5[cd[4]][[94midx].field_0 = 0
      [94midx = [94midx + 1
      continue 


# hash = 0xffa1ad74
# getter = None
# const = ['return', 21]
# payable = False
const VERSION = 21


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


