# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x5a85120F1DC701D725Bce3f712cFDD24e2760f47 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknowne82617fb
    # storage address 1
    unknowna209a29c
    # storage address 2
    unknown4c77e5ba
    # storage address 3
    unknown44bfa56e
    # storage address 4
    stor4
    # storage address 6
    unknown025ec81a
    # storage address 7
    stor7
    # storage address 8
    stor8
    # storage address 9
    stor9
    # storage address 11
    stor11
    # storage address 12
    stor12 # mask: a s
    # storage address 13
    stor13 # mask: a s
# hash = 0x025313a2
# getter = None
# const = None
# payable = False
def proxyOwner(): # not payable
  if caller == mstor13:
      return mstor13
  [93mdelegate mstor12 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


# hash = 0x025ec81a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def unknown025ec81a(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown025ec81am[m_param1m]


# hash = 0x44bfa56e
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 3]]]]], ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = False
def unknown44bfa56e(uint256 m_param1): # not payable
  return munknown44bfa56em[m_param1m]m[0 len munknown44bfa56em[m_param1m]m.lengthm]


# hash = 0x4c77e5ba
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def unknown4c77e5ba(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown4c77e5bam[m_param1m]


# hash = 0x54fd4d50
# getter = None
# const = None
# payable = False
def version(): # not payable
  if mstor13 != caller:
      [93mdelegate mstor12 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  mem[128] = uint256(mstor11m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile mstor11m.length + 96 > [94midxm:
      mem[[94midx + 32] = mstor11m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return Array(len=mstor11m.length, data=mem[128 len mstor11m.length])


# hash = 0x5a8b1a9f
# getter = None
# const = None
# payable = False
def upgradeTo(string m_version, address m_implementation): # not payable
  require calldata.size - 4 >= 64
  require m_version <= 4294967296
  require m_version + 36 <= calldata.size
  require m_version.length <= 4294967296 and m_version + m_version.length + 36 <= calldata.size
  if mstor13 != caller:
      [93mdelegate mstor12 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  mem[128 len m_version.length] = m_version[allm]
  mem[m_version.length + 128] = 0
  if mstor12 == m_implementation:
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
  mem[m_version.length + ceil32(m_version.length) + 192] = uint256(mstor11m.field_0)
  [94midx = m_version.length + ceil32(m_version.length) + 192
  [94ms = 0
  mwhile m_version.length + ceil32(m_version.length) + mstor11m.length + 160 > [94midxm:
      mem[[94midx + 32] = mstor11m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  if sha3(mem[m_version.length + ceil32(m_version.length) + 192 len mstor11m.length]) == [94m_85:
      revert with 0, 'New version equals to current'
  mstor11m[m]m.field_0 = Array(len=m_version.length, data=m_version[allm])
  mstor12 = m_implementation
  log Upgraded(
        string version=Array(len=_version.length, data=_version[all]),
        address implementation=_implementation)


# hash = 0x5c60da1b
# getter = None
# const = None
# payable = False
def implementation(): # not payable
  if caller == mstor13:
      return mstor12
  [93mdelegate mstor12 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


# hash = 0x6f3b8ce2
# getter = None
# const = None
# payable = False
def unknown6f3b8ce2(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if not mstor9m[m_param1m]m.field_0:
      mem[(32 * mstor9m[m_param1m]m.field_0) + 128] = 32
      mem[(32 * mstor9m[m_param1m]m.field_0) + 160] = mstor9m[m_param1m]m.field_0
      mem[(32 * mstor9m[m_param1m]m.field_0) + 192 len floor32(mstor9m[m_param1m]m.field_0)] = mem[128 len floor32(mstor9m[m_param1m]m.field_0)]
      return memory
        from (32 * mstor9m[m_param1m]m.field_0) + 128
         [93mlen (96 * mstor9m[m_param1m]m.field_0) + 64
  mem[128] = mstor9m[m_param1m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile (32 * mstor9m[m_param1m]m.field_0) + 96 > [94midxm:
      mem[[94midx + 32] = mstor9m[m_param1m]m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mstor9m[m_param1m]m.field_0) + 192 len floor32(mstor9m[m_param1m]m.field_0)] = mem[128 len floor32(mstor9m[m_param1m]m.field_0)]
  return Array(len=mstor9m[m_param1m]m.field_0, data=mem[128 len floor32(mstor9m[m_param1m]m.field_0)], mem[(32 * mstor9m[m_param1m]m.field_0) + floor32(mstor9m[m_param1m]m.field_0) + 192 len (32 * mstor9m[m_param1m]m.field_0) - floor32(mstor9m[m_param1m]m.field_0)]), 


# hash = 0x8ffa9690
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]]
# const = None
# payable = False
def unknown8ffa9690(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return bool(mstor4m[m_param1m])


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
  if mstor13 != caller:
      [93mdelegate mstor12 with:
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
  if mstor12 == m_implementation:
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
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 224] = uint256(mstor11m.field_0)
  [94midx = m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 224
  [94ms = 0
  mwhile m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + 192 > [94midxm:
      mem[[94midx + 32] = mstor11m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 192] = mstor11m.length
  mem[64] = m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + 224
  if sha3(mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + 224 len mstor11m.length]) == [94m_218:
      revert with 0, 'New version equals to current'
  mem[0] = 11
  mstor11m[m]m.field_0 = Array(len=m_version.length, data=m_version[allm])
  mstor12 = m_implementation
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + 224] = 32
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + 256] = m_version.length
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + 288 len ceil32(m_version.length)] = m_version[allm], mem[m_version.length + 128 len ceil32(m_version.length) - m_version.length]
  log Upgraded(
        string version=Array(len=_version.length, data=_version[all]),
        address implementation=_implementation)
  [94m_1201 = Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + 224 len floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)])] = mem[ceil32(m_version.length) + 160 len floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)])]
  mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]) + 224] = mem[ceil32(m_version.length) + floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]) + -(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32) + 192 len Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32] or Mask(8 * -(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32) + 32, -(8 * -(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)] % 32) + 32) + 256, mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + floor32(Mask(8 * -ceil32(m_version.length) + m_version.length + 32, 0, 0), mem[m_version.length + 160 len -m_version.length + ceil32(m_version.length)]) + 224])
  call this.address with:
     value call.value wei
       gas gas_remaining wei
      args mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + 228 len [94m_1201 - 4]
  if not return_data.size:
      if not ext_call.success:
          revert with 0, 
                      32,
                      57,
                      0x674661696c20696e20657865637574696e67207468652066756e6374696f6e206f6620696d706c656d656e746174696f6e20636f6e74726163,
                      mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + 349 len 7]
  else:
      if not ext_call.success:
          revert with 0, 
                      32,
                      57,
                      0x674661696c20696e20657865637574696e67207468652066756e6374696f6e206f6620696d706c656d656e746174696f6e20636f6e74726163,
                      mem[m_version.length + ceil32(m_version.length) + ceil32(m_data.length) + mstor11m.length + ceil32(return_data.size) + 350 len 7]
  ('bool', 'ext_call.success')


# hash = 0xa209a29c
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 1]]]]], ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknowna209a29c(uint256 m_param1): # not payable
  return munknowna209a29cm[m_param1m]m[0 len munknowna209a29cm[m_param1m]m.lengthm]


# hash = 0xa8f0d3a7
# getter = None
# const = None
# payable = False
def unknowna8f0d3a7(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if not mstor7m[m_param1m]m.field_0:
      mem[(32 * mstor7m[m_param1m]m.field_0) + 128] = 32
      mem[(32 * mstor7m[m_param1m]m.field_0) + 160] = mstor7m[m_param1m]m.field_0
      mem[(32 * mstor7m[m_param1m]m.field_0) + 192 len floor32(mstor7m[m_param1m]m.field_0)] = mem[128 len floor32(mstor7m[m_param1m]m.field_0)]
      return memory
        from (32 * mstor7m[m_param1m]m.field_0) + 128
         [93mlen (96 * mstor7m[m_param1m]m.field_0) + 64
  mem[128] = mstor7m[m_param1m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile (32 * mstor7m[m_param1m]m.field_0) + 96 > [94midxm:
      mem[[94midx + 32] = mstor7m[m_param1m]m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mstor7m[m_param1m]m.field_0) + 192 len floor32(mstor7m[m_param1m]m.field_0)] = mem[128 len floor32(mstor7m[m_param1m]m.field_0)]
  return Array(len=mstor7m[m_param1m]m.field_0, data=mem[128 len floor32(mstor7m[m_param1m]m.field_0)], mem[(32 * mstor7m[m_param1m]m.field_0) + floor32(mstor7m[m_param1m]m.field_0) + 192 len (32 * mstor7m[m_param1m]m.field_0) - floor32(mstor7m[m_param1m]m.field_0)]), 


# hash = 0xe82617fb
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 0]]]
# const = None
# payable = False
def unknowne82617fb(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknowne82617fbm[m_param1m]


# hash = 0xf1739cae
# getter = None
# const = None
# payable = False
def transferProxyOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >= 32
  if mstor13 != caller:
      [93mdelegate mstor12 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  if not m_newOwner:
      revert with 0, 'Address should not be 0x'
  log ProxyOwnershipTransferred(
        address previousOwner=stor13,
        address newOwner=_newOwner)
  mstor13 = m_newOwner


# hash = 0xf6fcbee1
# getter = None
# const = None
# payable = False
def unknownf6fcbee1(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if mstor8m[m_param1m]m.field_0:
      mem[128] = mstor8m[m_param1m]m.field_0
      if (32 * mstor8m[m_param1m]m.field_0) + 32 > 64:
          mem[160] = mstor8m[m_param1m]m.field_256
          [94midx = 160
          [94ms = 1
          mwhile (32 * mstor8m[m_param1m]m.field_0) + 96 > [94midxm:
              mem[[94midx + 32] = mstor8m[m_param1m]m[[94msm]m.field_256
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
  mem[(32 * mstor8m[m_param1m]m.field_0) + 128] = 32
  mem[(32 * mstor8m[m_param1m]m.field_0) + 160] = mstor8m[m_param1m]m.field_0
  mem[(32 * mstor8m[m_param1m]m.field_0) + 192 len floor32(mstor8m[m_param1m]m.field_0)] = mem[128 len floor32(mstor8m[m_param1m]m.field_0)]
  return memory
    from (32 * mstor8m[m_param1m]m.field_0) + 128
     [93mlen (96 * mstor8m[m_param1m]m.field_0) + 64


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  [93mdelegate mstor12 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


