# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xC672EC9CF3Be7Ad06Be4C5650812aEc23BBfB7E1 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    resolverAddress # mask: a s
    # storage address 1
    key # mask: a s
    # storage address 2
    CONTRACT_ADDRESS # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 10
    stor10 # mask: a s
    # storage address 11
    stor11 # mask: a s
    # storage address 12
    stor12 # mask: a s
    # storage address 13
    stor13 # mask: a s
    # storage address 14
    stor14 # mask: a s
    # storage address 15
    unknown57e7946f # mask: a s
    # storage address 16
    unknownda736c25 # mask: a s
    # storage address 17
    unknowne0fe1d46
# hash = 0x04f3bcec
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def resolver(): # not payable
  return resolverAddress


# hash = 0x097298b4
# getter = None
# const = None
# payable = False
def unknown097298b4(uint256 _param1, uint256 _param2): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:config'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  stor11 = _param1
  stor12 = _param2
  return 1


# hash = 0x09a0c130
# getter = None
# const = None
# payable = False
def unknown09a0c130(addr _param1): # not payable
  if unknowne0fe1d46[addr(_param1)].field_0:
      return unknowne0fe1d46[addr(_param1)].field_512, 
             unknowne0fe1d46[addr(_param1)].field_256,
             bool(unknowne0fe1d46[addr(_param1)].field_0)
  return unknowne0fe1d46[addr(_param1)].field_512, unknowne0fe1d46[addr(_param1)].field_256, bool(uint8(stor7.field_0))


# hash = 0x0d8c1c17
# getter = None
# const = None
# payable = False
def unknown0d8c1c17(): # not payable
  return unknown57e7946f, unknownda736c25


# hash = 0x0e71e7ac
# getter = None
# const = None
# payable = False
def unknown0e71e7ac(addr _param1, bool _param2, bool _param3, bool _param4): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:config'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  unknowne0fe1d46[addr(_param1)].field_0 = uint8(_param2)
  unknowne0fe1d46[addr(_param1)].field_8 = Mask(248, 0, _param3)
  unknowne0fe1d46[addr(_param1)].field_16 = Mask(240, 0, _param4)
  return 1


# hash = 0x1326a78a
# getter = None
# const = None
# payable = False
def unknown1326a78a(addr _param1, uint256 _param2, uint256 _param3, uint256 _param4): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'sv:tdemurrage'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  unknowne0fe1d46[stor3].field_512 = _param4
  unknowne0fe1d46[addr(_param1)].field_512 = _param2
  unknowne0fe1d46[addr(_param1)].field_256 = _param3
  return 1


# hash = 0x1611f8e1
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def unknown1611f8e1(addr _param1): # not payable
  return unknowne0fe1d46[addr(_param1)].field_512, bool(unknowne0fe1d46[addr(_param1)].field_16)


# hash = 0x3943380c
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def key(): # not payable
  return key


# hash = 0x3982b10d
# getter = None
# const = None
# payable = False
def unknown3982b10d(): # not payable
  return stor3, stor4, stor5


# hash = 0x39d20a5f
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def unknown39d20a5f(addr _param1): # not payable
  return unknowne0fe1d46[addr(_param1)].field_256 > 0, 
         unknowne0fe1d46[addr(_param1)].field_512,
         unknowne0fe1d46[addr(_param1)].field_256,
         bool(unknowne0fe1d46[addr(_param1)].field_0),
         bool(unknowne0fe1d46[addr(_param1)].field_16),
         bool(unknowne0fe1d46[addr(_param1)].field_8)


# hash = 0x3f83acff
# getter = None
# const = None
# payable = False
def get_contract(bytes32 _key): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args _key
  require ext_call.success
  return ext_call.return_data[12 len 20]


# hash = 0x493f8d30
# getter = None
# const = None
# payable = False
def unknown493f8d30(): # not payable
  return stor9, stor10, stor3, bool(uint8(stor7.field_0))


# hash = 0x57e7946f
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknown57e7946f(): # not payable
  return unknown57e7946f


# hash = 0x5aad90f8
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['add', 3, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 17]]]]]]
# const = None
# payable = False
def unknown5aad90f8(addr _param1, addr _param2): # not payable
  return unknowne0fe1d46[addr(_param1)][3][addr(_param2)].field_0


# hash = 0x6f27ea4c
# getter = None
# const = None
# payable = False
def unknown6f27ea4c(addr _param1, addr _param2, uint256 _param3): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:approval'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  unknowne0fe1d46[addr(_param1)][3][addr(_param2)].field_0 = _param3
  return 1


# hash = 0x6f6259ba
# getter = None
# const = None
# payable = False
def unknown6f6259ba(uint256 _param1): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:asset'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  unknownda736c25 = _param1
  return 1


# hash = 0x749c2fea
# getter = None
# const = None
# payable = False
def unknown749c2fea(addr _param1, uint256 _param2, addr _param3, uint256 _param4, uint256 _param5, addr _param6, uint256 _param7): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:transfer'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  unknowne0fe1d46[addr(_param1)].field_512 = _param2
  unknowne0fe1d46[addr(_param3)].field_512 = _param4
  unknowne0fe1d46[stor5].field_512 = _param5
  unknowne0fe1d46[addr(_param1)][3][addr(_param6)].field_0 = _param7
  return 1


# hash = 0x83197ef0
# getter = None
# const = None
# payable = False
def destroy(): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.locked() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require not ext_call.return_data[0]
  require ext_code.size(resolverAddress)
  call resolverAddress.owner() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  require ext_code.size(resolverAddress)
  call resolverAddress.0xc8b56bda with:
       gas gas_remaining - 710 wei
      args key
  require ext_call.success
  require ext_call.return_data[0]
  [93mselfdestruct([91maddr(ext_call.return_data[0])[93m)


# hash = 0x86362094
# getter = None
# const = None
# payable = False
def unknown86362094(): # not payable
  return stor6, bool(uint8(stor7.field_0)), bool(uint8(stor7.field_8)), stor8


# hash = 0xa6e653f6
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def unknowna6e653f6(addr _param1): # not payable
  return bool(unknowne0fe1d46[addr(_param1)].field_0), 
         bool(unknowne0fe1d46[addr(_param1)].field_8),
         bool(unknowne0fe1d46[addr(_param1)].field_16)


# hash = 0xa77af36e
# getter = None
# const = None
# payable = False
def unknowna77af36e(): # not payable
  if not uint8(stor7.field_0):
      return unknowne0fe1d46[stor3].field_512, stor9, stor10, stor3
  return unknowne0fe1d46[stor3].field_512, 0, 0, stor3


# hash = 0xda736c25
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknownda736c25(): # not payable
  return unknownda736c25


# hash = 0xdb4ecbc1
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def CONTRACT_ADDRESS(): # not payable
  return CONTRACT_ADDRESS


# hash = 0xdd2555f3
# getter = None
# const = None
# payable = False
def unknowndd2555f3(addr _param1, uint256 _param2, addr _param3, uint256 _param4, uint256 _param5): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:transfer'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  unknowne0fe1d46[addr(_param1)].field_512 = _param2
  unknowne0fe1d46[addr(_param3)].field_512 = _param4
  unknowne0fe1d46[stor5].field_512 = _param5
  return 1


# hash = 0xe0fe1d46
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def unknowne0fe1d46(addr _param1): # not payable
  return unknowne0fe1d46[addr(_param1)].field_512, bool(unknowne0fe1d46[addr(_param1)].field_8)


# hash = 0xe2958974
# getter = None
# const = None
# payable = False
def unknowne2958974(): # not payable
  return unknowne0fe1d46[stor5].field_512, stor13, stor14, stor5, bool(uint8(stor7.field_8)), stor8


# hash = 0xe53bd61e
# getter = None
# const = None
# payable = False
def unknowne53bd61e(addr _param1, addr _param2, addr _param3): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:config'
  require ext_call.success
  require caller == addr(ext_call.return_data[0])
  unknowne0fe1d46[addr(_param1)].field_512 += unknowne0fe1d46[stor3].field_512
  unknowne0fe1d46[stor3].field_512 = 0
  unknowne0fe1d46[addr(_param2)].field_512 += unknowne0fe1d46[stor4].field_512
  unknowne0fe1d46[stor4].field_512 = 0
  unknowne0fe1d46[addr(_param3)].field_512 += unknowne0fe1d46[stor5].field_512
  unknowne0fe1d46[stor5].field_512 = 0
  return 1, unknowne0fe1d46[stor3].field_512, unknowne0fe1d46[stor4].field_512, unknowne0fe1d46[stor5].field_512


# hash = 0xe65d2e21
# getter = None
# const = None
# payable = False
def unknowne65d2e21(uint256 _param1, uint256 _param2, bool _param3, uint256 _param4): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:config'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  stor13 = _param1
  stor14 = _param2
  Mask(248, 0, stor7.field_8) = Mask(248, 0, _param3)
  stor8 = _param4
  return 1


# hash = 0xf06a0674
# getter = None
# const = None
# payable = False
def unknownf06a0674(addr _param1, uint256 _param2, uint256 _param3, uint256 _param4): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:asset'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  unknowne0fe1d46[addr(_param1)].field_512 = _param2
  unknown57e7946f = _param3
  unknownda736c25 = _param4
  return 1


# hash = 0xf14206be
# getter = None
# const = None
# payable = False
def unknownf14206be(addr _param1, uint256 _param2, uint256 _param3, uint256 _param4, uint256 _param5): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:asset:recast'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  unknowne0fe1d46[addr(_param1)].field_512 = _param2
  unknowne0fe1d46[stor4].field_512 = _param3
  unknown57e7946f = _param4
  unknownda736c25 = _param5
  return 1


# hash = 0xf7e44409
# getter = None
# const = None
# payable = False
def unknownf7e44409(uint256 _param1, uint256 _param2, bool _param3): # not payable
  require ext_code.size(resolverAddress)
  call resolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:config'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  stor9 = _param1
  stor10 = _param2
  uint8(stor7.field_0) = uint8(_param3)
  return 1


# hash = 0xfe4215f7
# getter = None
# const = None
# payable = False
def unknownfe4215f7(): # not payable
  return stor11, stor12, unknown57e7946f, unknownda736c25, stor4, unknowne0fe1d46[stor4].field_512


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


