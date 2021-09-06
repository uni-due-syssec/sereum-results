# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x57AFaF4291105979fAA2BcF34F0149c1B1C7953f 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    issuanceAddress # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    stor2
    # storage address 3
    unknownc449c1d9
    # storage address 4
    factoryAddress # mask: a s
    # storage address 5
    securityTokenAddress # mask: a s
    # storage address 6
    paused # mask: a s
    # storage address 6
    unknown05d97f4fAddress # mask: a s
    # storage address 7
    stor7
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
# hash = 0x025313a2
# getter = None
# const = None
# payable = False
def proxyOwner(): # not payable
  if caller == mstor9:
      return mstor9
  [93mdelegate mstor8 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


# hash = 0x05d97f4f
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def unknown05d97f4f(): # not payable
  return munknown05d97f4fAddress


# hash = 0x1bb7cc99
# getter = None
# const = ['return', "'WHITELIST'"]
# payable = False
const WHITELIST = 'WHITELIST'


# hash = 0x2a0acc6a
# getter = None
# const = ['return', "'ADMIN'"]
# payable = False
const ADMIN = 'ADMIN'


# hash = 0x54fd4d50
# getter = None
# const = None
# payable = False
def version(): # not payable
  if mstor9 != caller:
      [93mdelegate mstor8 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  mem[128] = uint256(mstor7m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile mstor7m.length + 96 > [94midxm:
      mem[[94midx + 32] = mstor7m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return Array(len=mstor7m.length, data=mem[128 len mstor7m.length])


# hash = 0x5a8b1a9f
# getter = None
# const = None
# payable = False
def upgradeTo(string m_version, address m_implementation): # not payable
  require calldata.size - 4 >= 64
  require m_version <= 4294967296
  require m_version + 36 <= calldata.size
  require m_version.length <= 4294967296 and m_version + m_version.length + 36 <= calldata.size
  if mstor9 != caller:
      [93mdelegate mstor8 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  mem[128 len m_version.length] = m_version[allm]
  mem[m_version.length + 128] = 0
  if mstor8 == m_implementation:
      revert with 0, 
                  32,
                  70,
                  0x744f6c642061646472657373206973206e6f7420616c6c6f77656420616e6420696d706c656d656e746174696f6e20616464726573732073686f756c64206e6f742062652030,
                  mem[ceil32(m_version.length) + 266 len 26]
  if not m_implementation:
      revert with 0, 
                  32,
                  70,
                  0x744f6c642061646472657373206973206e6f7420616c6c6f77656420616e6420696d706c656d656e746174696f6e20616464726573732073686f756c64206e6f742062652030,
                  mem[ceil32(m_version.length) + 266 len 26]
  if not ext_code.size(m_implementation):
      revert with 0, 
                  32,
                  59,
                  0x7843616e6e6f742073657420612070726f787920696d706c656d656e746174696f6e20746f2061206e6f6e2d636f6e747261637420616464726573,
                  mem[ceil32(m_version.length) + 255 len 5]
  if m_version.length <= 0:
      revert with 0, 
                  32,
                  34,
                  0xfe56657273696f6e2073686f756c64206e6f7420626520656d70747920737472696e,
                  mem[ceil32(m_version.length) + 230 len 30]
  mem[ceil32(m_version.length) + 160 len floor32(m_version.length)] = call.data[m_version + 36 len floor32(m_version.length)]
  mem[ceil32(m_version.length) + floor32(m_version.length) + -(m_version.length % 32) + 192 len m_version.length % 32] = mem[floor32(m_version.length) + -(m_version.length % 32) + 160 len m_version.length % 32]
  mem[ceil32(m_version.length) + 128] = m_version.length
  [94m_85 = sha3(mem[ceil32(m_version.length) + 160 len Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]])
  mem[m_version.length + ceil32(m_version.length) + 192] = uint256(mstor7m.field_0)
  [94midx = m_version.length + ceil32(m_version.length) + 192
  [94ms = 0
  mwhile m_version.length + ceil32(m_version.length) + mstor7m.length + 160 > [94midxm:
      mem[[94midx + 32] = mstor7m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  if sha3(mem[m_version.length + ceil32(m_version.length) + 192 len mstor7m.length]) == [94m_85:
      revert with 0, 'New version equals to current'
  mstor7m[m]m.field_0 = Array(len=m_version.length, data=m_version[allm])
  mstor8 = m_implementation
  log Upgraded(
        string version=Array(len=_version.length, data=_version[all]),
        address implementation=_implementation)


# hash = 0x5c60da1b
# getter = None
# const = None
# payable = False
def implementation(): # not payable
  if caller == mstor9:
      return mstor8
  [93mdelegate mstor8 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 6]]
# const = None
# payable = False
def paused(): # not payable
  return bool(mpaused)


# hash = 0x65022eff
# getter = None
# const = ['return', "'INVESTORFLAGS'"]
# payable = False
const unknown65022eff = 'INVESTORFLAGS'


# hash = 0x958a41dd
# getter = None
# const = None
# payable = True
def upgradeToAndCall(string m_version, address m_implementation, bytes m_data) payable: 
  require calldata.size - 4 >= 96
  require m_version <= 4294967296
  require m_version + 36 <= calldata.size
  require m_version.length <= 4294967296 and m_version + m_version.length + 36 <= calldata.size
  require m_data <= 4294967296
  require m_data + 36 <= calldata.size
  require m_data.length <= 4294967296 and m_data + m_data.length + 36 <= calldata.size
  if mstor9 != caller:
      [93mdelegate mstor8 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  mem[96] = m_version.length
  mem[128 len m_version.length] = m_version[allm]
  mem[m_version.length + 128] = 0
  mem[ceil32(m_version.length) + 128] = m_data.length
  mem[ceil32(m_version.length) + 160 len m_data.length] = m_data[allm]
  mem[ceil32(m_version.length) + m_data.length + 160] = 0
  if mstor8 == m_implementation:
      revert with 0, 
                  32,
                  70,
                  0x744f6c642061646472657373206973206e6f7420616c6c6f77656420616e6420696d706c656d656e746174696f6e20616464726573732073686f756c64206e6f742062652030,
                  mem[ceil32(m_version.length) + ceil32(m_data.length) + 298 len 26]
  if not m_implementation:
      revert with 0, 
                  32,
                  70,
                  0x744f6c642061646472657373206973206e6f7420616c6c6f77656420616e6420696d706c656d656e746174696f6e20616464726573732073686f756c64206e6f742062652030,
                  mem[ceil32(m_version.length) + ceil32(m_data.length) + 298 len 26]
  if not ext_code.size(m_implementation):
      revert with 0, 
                  32,
                  59,
                  0x7843616e6e6f742073657420612070726f787920696d706c656d656e746174696f6e20746f2061206e6f6e2d636f6e747261637420616464726573,
                  mem[ceil32(m_version.length) + ceil32(m_data.length) + 287 len 5]
  if m_version.length <= 0:
      revert with 0, 
                  32,
                  34,
                  0xfe56657273696f6e2073686f756c64206e6f7420626520656d70747920737472696e,
                  mem[ceil32(m_version.length) + ceil32(m_data.length) + 262 len 30]
  mem[ceil32(m_version.length) + ceil32(m_data.length) + 192 len floor32(m_version.length)] = call.data[m_version + 36 len floor32(m_version.length)]
  mem[ceil32(m_version.length) + ceil32(m_data.length) + floor32(m_version.length) + -(m_version.length % 32) + 224 len m_version.length % 32] = mem[floor32(m_version.length) + -(m_version.length % 32) + 160 len m_version.length % 32]
  mem[ceil32(m_version.length) + ceil32(m_data.length) + 160] = m_version.length
  [94m_218 = sha3(mem[ceil32(m_version.length) + ceil32(m_data.length) + 192 len Mask(8 * -ceil32(m_data.length) + m_data.length + 32, 0, 0), mem[ceil32(m_version.length) + m_data.length + 192 len -m_data.length + ceil32(m_data.length)]])
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 224] = uint256(mstor7m.field_0)
  [94midx = m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 224
  [94ms = 0
  mwhile m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + 192 > [94midxm:
      mem[[94midx + 32] = mstor7m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 192] = mstor7m.length
  mem[64] = m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + 224
  if sha3(mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 224 len mstor7m.length]) == [94m_218:
      revert with 0, 'New version equals to current'
  mem[0] = 7
  mstor7m[m]m.field_0 = Array(len=m_version.length, data=m_version[allm])
  mstor8 = m_implementation
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + 224] = 32
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + 256] = m_version.length
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + 288 len ceil32(m_version.length)] = m_version[allm], mem[m_version.length + 128 len ceil32(m_version.length) - m_version.length]
  log Upgraded(
        string version=Array(len=_version.length, data=_version[all]),
        address implementation=_implementation)
  [94m_1201 = Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + 224 len floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)])] = mem[ceil32(m_version.length) + 160 len floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)])]
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]) + 224] = mem[ceil32(m_version.length) + floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]) + -(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32) + 192 len Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32] or Mask(8 * -(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32) + 32, -(8 * -(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32) + 32) + 256, mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]) + 224])
  call this.address with:
     value call.value wei
       gas gas_remaining wei
      args mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + 228 len [94m_1201 - 4]
  if not return_data.size:
      if not ext_call.success:
          revert with 0, 
                      32,
                      57,
                      0x674661696c20696e20657865637574696e67207468652066756e6374696f6e206f6620696d706c656d656e746174696f6e20636f6e74726163,
                      mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + 349 len 7]
  else:
      if not ext_call.success:
          revert with 0, 
                      32,
                      57,
                      0x674661696c20696e20657865637574696e67207468652066756e6374696f6e206f6620696d706c656d656e746174696f6e20636f6e74726163,
                      mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor7m.length + ceil32(return_data.size) + 350 len 7]
  ('bool', 'ext_call.success')


# hash = 0x983d2737
# getter = None
# const = ['return', "'OPERATOR'"]
# payable = False
const unknown983d2737 = 'OPERATOR'


# hash = 0x9ba0b7c0
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 2]]]]]]
# const = None
# payable = False
def nonceMap(address m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  return bool(mstor2m[m_param1m]m[m_param2m])


# hash = 0xb3fac8ce
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def issuanceAddress(): # not payable
  return missuanceAddress


# hash = 0xb84dfbd2
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def securityToken(): # not payable
  return msecurityTokenAddress


# hash = 0xbc293897
# getter = None
# const = ['return', 100969221179527024975026890885522870763749117541835841361867616504506818848561]
# payable = False
const unknownbc293897 = 0xdf3a8dd24acdd05addfc6aeffef7574d2de3f844535ec91e8e0f3e45dba96731


# hash = 0xc449c1d9
# getter = ['struct', ['loc', 3]]
# const = None
# payable = False
def unknownc449c1d9(uint8 m_param1): # not payable
  require calldata.size - 4 >= 32
  return bool(munknownc449c1d9m[m_param1m]m.field_0), 
         bool(munknownc449c1d9m[m_param1m]m.field_8),
         bool(munknownc449c1d9m[m_param1m]m.field_16),
         bool(munknownc449c1d9m[m_param1m]m.field_24)


# hash = 0xc45a0155
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def factory(): # not payable
  return mfactoryAddress


# hash = 0xedb7a6fa
# getter = None
# const = None
# payable = False
def unknownedb7a6fa(): # not payable
  return uint64(mstor1m.field_0), uint64(mstor1m.field_64)


# hash = 0xf1739cae
# getter = None
# const = None
# payable = False
def transferProxyOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >= 32
  if mstor9 != caller:
      [93mdelegate mstor8 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  if not m_newOwner:
      revert with 0, 'Address should not be 0x'
  log ProxyOwnershipTransferred(
        address previousOwner=stor9,
        address newOwner=_newOwner)
  mstor9 = m_newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  [93mdelegate mstor8 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


