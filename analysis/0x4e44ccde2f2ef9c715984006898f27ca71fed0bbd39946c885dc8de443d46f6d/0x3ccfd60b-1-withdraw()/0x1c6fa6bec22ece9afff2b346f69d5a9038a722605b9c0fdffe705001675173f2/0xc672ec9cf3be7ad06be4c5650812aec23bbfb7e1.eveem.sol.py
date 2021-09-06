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
  return mresolverAddress


# hash = 0x097298b4
# getter = None
# const = None
# payable = False
def unknown097298b4(uint256 m_param1, uint256 m_param2): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:config'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  mstor11 = m_param1
  mstor12 = m_param2
  return 1


# hash = 0x09a0c130
# getter = None
# const = None
# payable = False
def unknown09a0c130(addr m_param1): # not payable
  if munknowne0fe1d46m[addr(m_param1)m]m.field_0:
      return munknowne0fe1d46m[addr(m_param1)m]m.field_512, 
             munknowne0fe1d46m[addr(m_param1)m]m.field_256,
             bool(munknowne0fe1d46m[addr(m_param1)m]m.field_0)
  return munknowne0fe1d46m[addr(m_param1)m]m.field_512, munknowne0fe1d46m[addr(m_param1)m]m.field_256, bool(uint8(mstor7m.field_0))


# hash = 0x0d8c1c17
# getter = None
# const = None
# payable = False
def unknown0d8c1c17(): # not payable
  return munknown57e7946f, munknownda736c25


# hash = 0x0e71e7ac
# getter = None
# const = None
# payable = False
def unknown0e71e7ac(addr m_param1, bool m_param2, bool m_param3, bool m_param4): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:config'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  munknowne0fe1d46m[addr(m_param1)m]m.field_0 = uint8(m_param2)
  munknowne0fe1d46m[addr(m_param1)m]m.field_8 = Mask(248, 0, m_param3)
  munknowne0fe1d46m[addr(m_param1)m]m.field_16 = Mask(240, 0, m_param4)
  return 1


# hash = 0x1326a78a
# getter = None
# const = None
# payable = False
def unknown1326a78a(addr m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'sv:tdemurrage'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  munknowne0fe1d46m[mstor3m]m.field_512 = m_param4
  munknowne0fe1d46m[addr(m_param1)m]m.field_512 = m_param2
  munknowne0fe1d46m[addr(m_param1)m]m.field_256 = m_param3
  return 1


# hash = 0x1611f8e1
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def unknown1611f8e1(addr m_param1): # not payable
  return munknowne0fe1d46m[addr(m_param1)m]m.field_512, bool(munknowne0fe1d46m[addr(m_param1)m]m.field_16)


# hash = 0x3943380c
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def key(): # not payable
  return mkey


# hash = 0x3982b10d
# getter = None
# const = None
# payable = False
def unknown3982b10d(): # not payable
  return mstor3, mstor4, mstor5


# hash = 0x39d20a5f
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def unknown39d20a5f(addr m_param1): # not payable
  return munknowne0fe1d46m[addr(m_param1)m]m.field_256 > 0, 
         munknowne0fe1d46m[addr(m_param1)m]m.field_512,
         munknowne0fe1d46m[addr(m_param1)m]m.field_256,
         bool(munknowne0fe1d46m[addr(m_param1)m]m.field_0),
         bool(munknowne0fe1d46m[addr(m_param1)m]m.field_16),
         bool(munknowne0fe1d46m[addr(m_param1)m]m.field_8)


# hash = 0x3f83acff
# getter = None
# const = None
# payable = False
def get_contract(bytes32 m_key): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args m_key
  require ext_call.success
  return ext_call.return_data[12 len 20]


# hash = 0x493f8d30
# getter = None
# const = None
# payable = False
def unknown493f8d30(): # not payable
  return mstor9, mstor10, mstor3, bool(uint8(mstor7m.field_0))


# hash = 0x57e7946f
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknown57e7946f(): # not payable
  return munknown57e7946f


# hash = 0x5aad90f8
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['add', 3, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 17]]]]]]
# const = None
# payable = False
def unknown5aad90f8(addr m_param1, addr m_param2): # not payable
  return munknowne0fe1d46m[addr(m_param1)m]m[3m]m[addr(m_param2)m]m.field_0


# hash = 0x6f27ea4c
# getter = None
# const = None
# payable = False
def unknown6f27ea4c(addr m_param1, addr m_param2, uint256 m_param3): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:approval'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  munknowne0fe1d46m[addr(m_param1)m]m[3m]m[addr(m_param2)m]m.field_0 = m_param3
  return 1


# hash = 0x6f6259ba
# getter = None
# const = None
# payable = False
def unknown6f6259ba(uint256 m_param1): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:asset'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  munknownda736c25 = m_param1
  return 1


# hash = 0x749c2fea
# getter = None
# const = None
# payable = False
def unknown749c2fea(addr m_param1, uint256 m_param2, addr m_param3, uint256 m_param4, uint256 m_param5, addr m_param6, uint256 m_param7): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:transfer'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  munknowne0fe1d46m[addr(m_param1)m]m.field_512 = m_param2
  munknowne0fe1d46m[addr(m_param3)m]m.field_512 = m_param4
  munknowne0fe1d46m[mstor5m]m.field_512 = m_param5
  munknowne0fe1d46m[addr(m_param1)m]m[3m]m[addr(m_param6)m]m.field_0 = m_param7
  return 1


# hash = 0x83197ef0
# getter = None
# const = None
# payable = False
def destroy(): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.locked() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require not ext_call.return_data[0]
  require ext_code.size(mresolverAddress)
  call mresolverAddress.owner() with:
       gas gas_remaining - 710 wei
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  require ext_code.size(mresolverAddress)
  call mresolverAddress.0xc8b56bda with:
       gas gas_remaining - 710 wei
      args mkey
  require ext_call.success
  require ext_call.return_data[0]
  [93mselfdestruct([91maddr(ext_call.return_data[0])[93m)


# hash = 0x86362094
# getter = None
# const = None
# payable = False
def unknown86362094(): # not payable
  return mstor6, bool(uint8(mstor7m.field_0)), bool(uint8(mstor7m.field_8)), mstor8


# hash = 0xa6e653f6
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def unknowna6e653f6(addr m_param1): # not payable
  return bool(munknowne0fe1d46m[addr(m_param1)m]m.field_0), 
         bool(munknowne0fe1d46m[addr(m_param1)m]m.field_8),
         bool(munknowne0fe1d46m[addr(m_param1)m]m.field_16)


# hash = 0xa77af36e
# getter = None
# const = None
# payable = False
def unknowna77af36e(): # not payable
  if not uint8(mstor7m.field_0):
      return munknowne0fe1d46m[mstor3m]m.field_512, mstor9, mstor10, mstor3
  return munknowne0fe1d46m[mstor3m]m.field_512, 0, 0, mstor3


# hash = 0xda736c25
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def unknownda736c25(): # not payable
  return munknownda736c25


# hash = 0xdb4ecbc1
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def CONTRACT_ADDRESS(): # not payable
  return mCONTRACT_ADDRESS


# hash = 0xdd2555f3
# getter = None
# const = None
# payable = False
def unknowndd2555f3(addr m_param1, uint256 m_param2, addr m_param3, uint256 m_param4, uint256 m_param5): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:transfer'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  munknowne0fe1d46m[addr(m_param1)m]m.field_512 = m_param2
  munknowne0fe1d46m[addr(m_param3)m]m.field_512 = m_param4
  munknowne0fe1d46m[mstor5m]m.field_512 = m_param5
  return 1


# hash = 0xe0fe1d46
# getter = ['struct', ['loc', 17]]
# const = None
# payable = False
def unknowne0fe1d46(addr m_param1): # not payable
  return munknowne0fe1d46m[addr(m_param1)m]m.field_512, bool(munknowne0fe1d46m[addr(m_param1)m]m.field_8)


# hash = 0xe2958974
# getter = None
# const = None
# payable = False
def unknowne2958974(): # not payable
  return munknowne0fe1d46m[mstor5m]m.field_512, mstor13, mstor14, mstor5, bool(uint8(mstor7m.field_8)), mstor8


# hash = 0xe53bd61e
# getter = None
# const = None
# payable = False
def unknowne53bd61e(addr m_param1, addr m_param2, addr m_param3): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:config'
  require ext_call.success
  require caller == addr(ext_call.return_data[0])
  munknowne0fe1d46m[addr(m_param1)m]m.field_512 += munknowne0fe1d46m[mstor3m]m.field_512
  munknowne0fe1d46m[mstor3m]m.field_512 = 0
  munknowne0fe1d46m[addr(m_param2)m]m.field_512 += munknowne0fe1d46m[mstor4m]m.field_512
  munknowne0fe1d46m[mstor4m]m.field_512 = 0
  munknowne0fe1d46m[addr(m_param3)m]m.field_512 += munknowne0fe1d46m[mstor5m]m.field_512
  munknowne0fe1d46m[mstor5m]m.field_512 = 0
  return 1, munknowne0fe1d46m[mstor3m]m.field_512, munknowne0fe1d46m[mstor4m]m.field_512, munknowne0fe1d46m[mstor5m]m.field_512


# hash = 0xe65d2e21
# getter = None
# const = None
# payable = False
def unknowne65d2e21(uint256 m_param1, uint256 m_param2, bool m_param3, uint256 m_param4): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:config'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  mstor13 = m_param1
  mstor14 = m_param2
  Mask(248, 0, mstor7m.field_8) = Mask(248, 0, m_param3)
  mstor8 = m_param4
  return 1


# hash = 0xf06a0674
# getter = None
# const = None
# payable = False
def unknownf06a0674(addr m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:asset'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  munknowne0fe1d46m[addr(m_param1)m]m.field_512 = m_param2
  munknown57e7946f = m_param3
  munknownda736c25 = m_param4
  return 1


# hash = 0xf14206be
# getter = None
# const = None
# payable = False
def unknownf14206be(addr m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:asset:recast'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  munknowne0fe1d46m[addr(m_param1)m]m.field_512 = m_param2
  munknowne0fe1d46m[mstor4m]m.field_512 = m_param3
  munknown57e7946f = m_param4
  munknownda736c25 = m_param5
  return 1


# hash = 0xf7e44409
# getter = None
# const = None
# payable = False
def unknownf7e44409(uint256 m_param1, uint256 m_param2, bool m_param3): # not payable
  require ext_code.size(mresolverAddress)
  call mresolverAddress.get_contract(bytes32 key) with:
       gas gas_remaining - 710 wei
      args 'c:token:config'
  require ext_call.success
  require caller == ext_call.return_data[12 len 20]
  mstor9 = m_param1
  mstor10 = m_param2
  uint8(mstor7m.field_0) = uint8(m_param3)
  return 1


# hash = 0xfe4215f7
# getter = None
# const = None
# payable = False
def unknownfe4215f7(): # not payable
  return mstor11, mstor12, munknown57e7946f, munknownda736c25, mstor4, munknowne0fe1d46m[mstor4m]m.field_512


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


