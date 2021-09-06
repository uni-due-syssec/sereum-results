# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x3Ea951A0A631cBB11befCd178E871A72671CA8cD 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 5
    initialized # mask: a s
    # storage address 5
    tokenFactoryAddress # mask: a s
    # storage address 6
    name
    # storage address 7
    symbol
    # storage address 8
    controllerAddress # mask: a s
    # storage address 8
    decimals # mask: a s
    # storage address 9
    unknowncbaec476Address # mask: a s
    # storage address 10
    moduleRegistryAddress # mask: a s
    # storage address 11
    securityTokenRegistryAddress # mask: a s
    # storage address 12
    unknown05d97f4fAddress # mask: a s
    # storage address 13
    unknown2fb3b99dAddress # mask: a s
    # storage address 14
    dataStoreAddress # mask: a s
    # storage address 15
    granularity # mask: a s
    # storage address 16
    currentCheckpointId # mask: a s
    # storage address 17
    tokenDetails
    # storage address 18
    unknown7a802c71 # mask: a s
    # storage address 18
    transfersFrozen # mask: a s
    # storage address 19
    holderCount # mask: a s
    # storage address 32
    stor32
    # storage address 33
    stor33 # mask: a s
    # storage address 34
    stor34 # mask: a s
# hash = 0x025313a2
# getter = None
# const = None
# payable = False
def proxyOwner(): # not payable
  if caller == mstor34:
      return mstor34
  [93mdelegate mstor33 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


# hash = 0x05d97f4f
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def unknown05d97f4f(): # not payable
  return munknown05d97f4fAddress


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 6]]]], ['loc', 6]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x158ef93e
# getter = ['bool', ['storage', 8, 160, 5]]
# const = None
# payable = False
def initialized(): # not payable
  return bool(minitialized)


# hash = 0x1aab9a9f
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def holderCount(): # not payable
  return mholderCount


# hash = 0x2fb3b99d
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknown2fb3b99d(): # not payable
  return munknown2fb3b99dAddress


# hash = 0x313ce567
# getter = ['storage', 8, 0, 8]
# const = None
# payable = False
def decimals(): # not payable
  return mdecimals


# hash = 0x5488cc80
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def currentCheckpointId(): # not payable
  return mcurrentCheckpointId


# hash = 0x54fd4d50
# getter = None
# const = None
# payable = False
def version(): # not payable
  if mstor34 != caller:
      [93mdelegate mstor33 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  mem[128] = uint256(mstor32m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile mstor32m.length + 96 > [94midxm:
      mem[[94midx + 32] = mstor32m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return Array(len=mstor32m.length, data=mem[128 len mstor32m.length])


# hash = 0x556f0dc7
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def granularity(): # not payable
  return mgranularity


# hash = 0x5a8b1a9f
# getter = None
# const = None
# payable = False
def upgradeTo(string m_version, address m_implementation): # not payable
  require calldata.size - 4 >= 64
  require m_version <= 4294967296
  require m_version + 36 <= calldata.size
  require m_version.length <= 4294967296 and m_version + m_version.length + 36 <= calldata.size
  if mstor34 != caller:
      [93mdelegate mstor33 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  mem[128 len m_version.length] = m_version[allm]
  mem[m_version.length + 128] = 0
  if mstor33 == m_implementation:
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
  mem[ceil32(m_version.length) + floor32(m_version.length) + -(m_version.length % 32) + 192 len m_version.length % 32] = mem[-(m_version.length % 32) + floor32(m_version.length) + 160 len m_version.length % 32]
  mem[ceil32(m_version.length) + 128] = m_version.length
  [94m_85 = sha3(mem[ceil32(m_version.length) + 160 len Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]])
  mem[m_version.length + ceil32(m_version.length) + 192] = uint256(mstor32m.field_0)
  [94midx = m_version.length + ceil32(m_version.length) + 192
  [94ms = 0
  mwhile m_version.length + ceil32(m_version.length) + mstor32m.length + 160 > [94midxm:
      mem[[94midx + 32] = mstor32m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  if sha3(mem[m_version.length + ceil32(m_version.length) + 192 len mstor32m.length]) == [94m_85:
      revert with 0, 'New version equals to current'
  mstor32m[m]m.field_0 = Array(len=m_version.length, data=m_version[allm])
  mstor33 = m_implementation
  log Upgraded(
        string version=Array(len=_version.length, data=_version[all]),
        address implementation=_implementation)


# hash = 0x5c60da1b
# getter = None
# const = None
# payable = False
def implementation(): # not payable
  if caller == mstor34:
      return mstor33
  [93mdelegate mstor33 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


# hash = 0x660d0d67
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def dataStore(): # not payable
  return mdataStoreAddress


# hash = 0x7a802c71
# getter = ['bool', ['storage', 8, 0, 18]]
# const = None
# payable = False
def unknown7a802c71(): # not payable
  return bool(munknown7a802c71)


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
  if mstor34 != caller:
      [93mdelegate mstor33 with:
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
  if mstor33 == m_implementation:
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
  mem[ceil32(m_version.length) + ceil32(m_data.length) + floor32(m_version.length) + -(m_version.length % 32) + 224 len m_version.length % 32] = mem[-(m_version.length % 32) + floor32(m_version.length) + 160 len m_version.length % 32]
  mem[ceil32(m_version.length) + ceil32(m_data.length) + 160] = m_version.length
  [94m_218 = sha3(mem[ceil32(m_version.length) + ceil32(m_data.length) + 192 len Mask(8 * -ceil32(m_data.length) + m_data.length + 32, 0, 0), mem[ceil32(m_version.length) + m_data.length + 192 len -m_data.length + ceil32(m_data.length)]])
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 224] = uint256(mstor32m.field_0)
  [94midx = m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 224
  [94ms = 0
  mwhile m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + 192 > [94midxm:
      mem[[94midx + 32] = mstor32m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 192] = mstor32m.length
  mem[64] = m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + 224
  if sha3(mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 224 len mstor32m.length]) == [94m_218:
      revert with 0, 'New version equals to current'
  mem[0] = 32
  mstor32m[m]m.field_0 = Array(len=m_version.length, data=m_version[allm])
  mstor33 = m_implementation
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + 224] = 32
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + 256] = m_version.length
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + 288 len ceil32(m_version.length)] = m_version[allm], mem[m_version.length + 128 len ceil32(m_version.length) - m_version.length]
  log Upgraded(
        string version=Array(len=_version.length, data=_version[all]),
        address implementation=_implementation)
  [94m_1201 = Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + 224 len floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)])] = mem[ceil32(m_version.length) + 160 len floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)])]
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]) + 224] = mem[ceil32(m_version.length) + floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]) + -(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32) + 192 len Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32] or Mask(8 * -(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32) + 32, -(8 * -(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32) + 32) + 256, mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]) + 224])
  call this.address with:
     value call.value wei
       gas gas_remaining wei
      args mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + 228 len [94m_1201 - 4]
  if not return_data.size:
      if not ext_call.success:
          revert with 0, 
                      32,
                      57,
                      0x674661696c20696e20657865637574696e67207468652066756e6374696f6e206f6620696d706c656d656e746174696f6e20636f6e74726163,
                      mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + 349 len 7]
  else:
      if not ext_call.success:
          revert with 0, 
                      32,
                      57,
                      0x674661696c20696e20657865637574696e67207468652066756e6374696f6e206f6620696d706c656d656e746174696f6e20636f6e74726163,
                      mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor32m.length + ceil32(return_data.size) + 350 len 7]
  ('bool', 'ext_call.success')


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 7]]]], ['loc', 7]]]
# const = None
# payable = False
def symbol(): # not payable
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0xb95459e4
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def moduleRegistry(): # not payable
  return mmoduleRegistryAddress


# hash = 0xcbaec476
# getter = ['storage', 160, 0, 9]
# const = None
# payable = False
def unknowncbaec476(): # not payable
  return munknowncbaec476Address


# hash = 0xce4dbdff
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def securityTokenRegistry(): # not payable
  return msecurityTokenRegistryAddress


# hash = 0xd6abe110
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 17]]]], ['loc', 17]]]
# const = None
# payable = False
def tokenDetails(): # not payable
  return mtokenDetailsm[0 len mtokenDetailsm.lengthm]


# hash = 0xe45b8134
# getter = ['bool', ['storage', 8, 8, 18]]
# const = None
# payable = False
def transfersFrozen(): # not payable
  return bool(mtransfersFrozen)


# hash = 0xe77772fe
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def tokenFactory(): # not payable
  return mtokenFactoryAddress


# hash = 0xf1739cae
# getter = None
# const = None
# payable = False
def transferProxyOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >= 32
  if mstor34 != caller:
      [93mdelegate mstor33 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  if not m_newOwner:
      revert with 0, 'Address should not be 0x'
  log ProxyOwnershipTransferred(
        address previousOwner=stor34,
        address newOwner=_newOwner)
  mstor34 = m_newOwner


# hash = 0xf77c4791
# getter = ['storage', 160, 8, 8]
# const = None
# payable = False
def controller(): # not payable
  return mcontrollerAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  [93mdelegate mstor33 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


