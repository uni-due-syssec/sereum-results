# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xdb2ddb220b8a55e0e4412130E6aE74d136c04bA2 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    new_owner # mask: a s
    # storage address 2
    stor2
    # storage address 3
    _contract
    # storage address 4
    unknown4cb76b85 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 4
    locked # mask: a s
    # storage address 5
    unknownec5e40c2 # mask: a s
# hash = 0x0207e20e
# getter = None
# const = None
# payable = False
def unknown0207e20e(addr _param1): # not payable
  require caller == owner
  stor2['admins'][addr(_param1)] = 0
  return 1


# hash = 0x253c8bd4
# getter = None
# const = None
# payable = False
def change_owner(address _new_owner): # not payable
  require caller == owner
  new_owner = _new_owner
  return 1


# hash = 0x3f83acff
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 3]]]
# const = None
# payable = False
def get_contract(bytes32 _key): # not payable
  require _contract[_key]
  return _contract[_key]


# hash = 0x4552b04f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def new_owner(): # not payable
  return new_owner


# hash = 0x4cb76b85
# getter = ['bool', ['storage', 8, 8, 4]]
# const = None
# payable = False
def unknown4cb76b85(): # not payable
  return bool(unknown4cb76b85)


# hash = 0x630f1275
# getter = None
# const = None
# payable = False
def unknown630f1275(): # not payable
  require stor2['nsadmins'][caller]
  locked = 1
  return 1


# hash = 0x682d038a
# getter = None
# const = None
# payable = False
def unknown682d038a(uint256 _param1, addr _param2): # not payable
  require stor2['admins'][caller]
  require _param1 != 'admins'
  stor2[_param1][addr(_param2)] = 1
  return 1


# hash = 0x74bfd437
# getter = None
# const = None
# payable = False
def unknown74bfd437(): # not payable
  require stor2['nsadmins'][caller]
  locked = 0
  return 1


# hash = 0x79f0a895
# getter = None
# const = None
# payable = False
def unknown79f0a895(addr _param1): # not payable
  require caller == owner
  stor2['admins'][addr(_param1)] = 1
  return 1


# hash = 0x84a02763
# getter = None
# const = None
# payable = False
def unknown84a02763(uint256 _param1, addr _param2): # not payable
  require stor2['nsadmins'][caller]
  require tx.origin == owner
  require not locked
  if unknown4cb76b85:
      require unknownec5e40c2 >= block.timestamp
  require not _contract[_param1]
  _contract[_param1] = _param2
  log 0x27e557ae: _param1, _param2
  return 1


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0xb692ee23
# getter = None
# const = None
# payable = False
def unknownb692ee23(uint256 _param1, addr _param2): # not payable
  require stor2['admins'][caller]
  require _param1 != 'admins'
  stor2[_param1][addr(_param2)] = 0
  return 1


# hash = 0xc0f6ef4a
# getter = None
# const = None
# payable = False
def unknownc0f6ef4a(uint256 _param1, addr _param2): # not payable
  require tx.origin == owner
  require not locked
  require not _contract[_param1]
  if unknown4cb76b85:
      require unknownec5e40c2 >= block.timestamp
  _contract[_param1] = _param2
  return 1


# hash = 0xc8b56bda
# getter = None
# const = None
# payable = False
def unknownc8b56bda(uint256 _param1): # not payable
  if unknown4cb76b85:
      require unknownec5e40c2 >= block.timestamp
  require tx.origin == owner
  require not locked
  require _contract[_param1]
  require caller == _contract[_param1]
  _contract[_param1] = 0
  log 0x5c4b05c4: _param1
  return 1


# hash = 0xcf309012
# getter = ['bool', ['storage', 8, 0, 4]]
# const = None
# payable = False
def locked(): # not payable
  return bool(locked)


# hash = 0xe6fc01a9
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['cd', 4], 2]]]]]]
# const = None
# payable = False
def unknowne6fc01a9(uint256 _param1, addr _param2): # not payable
  return bool(stor2[_param1][addr(_param2)])


# hash = 0xec5e40c2
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknownec5e40c2(): # not payable
  return unknownec5e40c2


# hash = 0xf7a79a02
# getter = None
# const = None
# payable = False
def unknownf7a79a02(): # not payable
  stor2['nsadmins'][stor0] = 0
  stor2['nsadmins'][stor1] = 1
  stor2['admins'][stor0] = 0
  stor2['admins'][stor1] = 1
  require caller == new_owner
  owner = new_owner
  return 1


# hash = 0xff574fb4
# getter = None
# const = None
# payable = False
def unknownff574fb4(uint256 _param1): # not payable
  require caller == owner
  if unknown4cb76b85:
      require unknownec5e40c2 >= block.timestamp
  unknownec5e40c2 = _param1
  stor4 = 1
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


