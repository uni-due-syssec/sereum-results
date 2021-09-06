# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xCFC94Faf8b9a21Df1ac973Cce4d0b6685e4253A0 
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
  if caller == stor13:
      return stor13
  [93mdelegate stor12 with:
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
def unknown025ec81a(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown025ec81a[_param1]


# hash = 0x44bfa56e
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 3]]]]], ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = False
def unknown44bfa56e(uint256 _param1): # not payable
  return unknown44bfa56e[_param1][0 len unknown44bfa56e[_param1].length]


# hash = 0x4c77e5ba
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def unknown4c77e5ba(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown4c77e5ba[_param1]


# hash = 0x54fd4d50
# getter = None
# const = None
# payable = False
def version(): # not payable
  if stor13 != caller:
      [93mdelegate stor12 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  mem[128] = uint256(stor11.field_0)
  [94midx = 128
  [94ms = 0
  while stor11.length + 96 > [94midx:
      mem[[94midx + 32] = stor11[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return Array(len=stor11.length, data=mem[128 len stor11.length])


# hash = 0x5a8b1a9f
# getter = None
# const = None
# payable = False
def upgradeTo(string _version, address _implementation): # not payable
  require calldata.size - 4 >= 64
  require _version <= 4294967296
  require _version + 36 <= calldata.size
  require _version.length <= 4294967296 and _version + _version.length + 36 <= calldata.size
  if stor13 != caller:
      [93mdelegate stor12 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  mem[128 len _version.length] = _version[all]
  mem[_version.length + 128] = 0
  if stor12 == _implementation:
      revert with 0, 
                  32,
                  70,
                  0x744f6c642061646472657373206973206e6f7420616c6c6f77656420616e6420696d706c656d656e746174696f6e20616464726573732073686f756c64206e6f742062652030,
                  mem[ceil32(_version.length) + 266 len 26]
  if not _implementation:
      revert with 0, 
                  32,
                  70,
                  0x744f6c642061646472657373206973206e6f7420616c6c6f77656420616e6420696d706c656d656e746174696f6e20616464726573732073686f756c64206e6f742062652030,
                  mem[ceil32(_version.length) + 266 len 26]
  if not ext_code.size(_implementation):
      revert with 0, 
                  32,
                  59,
                  0x7843616e6e6f742073657420612070726f787920696d706c656d656e746174696f6e20746f2061206e6f6e2d636f6e747261637420616464726573,
                  mem[ceil32(_version.length) + 255 len 5]
  if _version.length <= 0:
      revert with 0, 
                  32,
                  34,
                  0xfe56657273696f6e2073686f756c64206e6f7420626520656d70747920737472696e,
                  mem[ceil32(_version.length) + 230 len 30]
  mem[ceil32(_version.length) + 160 len floor32(_version.length)] = call.data[_version + 36 len floor32(_version.length)]
  mem[ceil32(_version.length) + floor32(_version.length) + -(_version.length % 32) + 192 len _version.length % 32] = mem[floor32(_version.length) + -(_version.length % 32) + 160 len _version.length % 32]
  mem[ceil32(_version.length) + 128] = _version.length
  [94m_85 = sha3(mem[ceil32(_version.length) + 160 len Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)]])
  mem[_version.length + ceil32(_version.length) + 192] = uint256(stor11.field_0)
  [94midx = _version.length + ceil32(_version.length) + 192
  [94ms = 0
  while _version.length + ceil32(_version.length) + stor11.length + 160 > [94midx:
      mem[[94midx + 32] = stor11[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  if sha3(mem[_version.length + ceil32(_version.length) + 192 len stor11.length]) == [94m_85:
      revert with 0, 'New version equals to current'
  stor11[].field_0 = Array(len=_version.length, data=_version[all])
  stor12 = _implementation
  log Upgraded(
        string version=Array(len=_version.length, data=_version[all]),
        address implementation=_implementation)


# hash = 0x5c60da1b
# getter = None
# const = None
# payable = False
def implementation(): # not payable
  if caller == stor13:
      return stor12
  [93mdelegate stor12 with:
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
def unknown6f3b8ce2(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if not stor9[_param1].field_0:
      mem[(32 * stor9[_param1].field_0) + 128] = 32
      mem[(32 * stor9[_param1].field_0) + 160] = stor9[_param1].field_0
      mem[(32 * stor9[_param1].field_0) + 192 len floor32(stor9[_param1].field_0)] = mem[128 len floor32(stor9[_param1].field_0)]
      return memory
        from (32 * stor9[_param1].field_0) + 128
         [93mlen (96 * stor9[_param1].field_0) + 64
  mem[128] = stor9[_param1].field_0
  [94midx = 128
  [94ms = 0
  while (32 * stor9[_param1].field_0) + 96 > [94midx:
      mem[[94midx + 32] = stor9[_param1][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * stor9[_param1].field_0) + 192 len floor32(stor9[_param1].field_0)] = mem[128 len floor32(stor9[_param1].field_0)]
  return Array(len=stor9[_param1].field_0, data=mem[128 len floor32(stor9[_param1].field_0)], mem[(32 * stor9[_param1].field_0) + floor32(stor9[_param1].field_0) + 192 len (32 * stor9[_param1].field_0) - floor32(stor9[_param1].field_0)]), 


# hash = 0x8ffa9690
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]]
# const = None
# payable = False
def unknown8ffa9690(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return bool(stor4[_param1])


# hash = 0x958a41dd
# getter = None
# const = None
# payable = True
def upgradeToAndCall(string _version, address _implementation, bytes _data) payable: 
  require calldata.size - 4 >= 96
  require _version <= 4294967296
  require _version + 36 <= calldata.size
  require _version.length <= 4294967296 and _version + _version.length + 36 <= calldata.size
  require _data <= 4294967296
  require _data + 36 <= calldata.size
  require _data.length <= 4294967296 and _data + _data.length + 36 <= calldata.size
  if stor13 != caller:
      [93mdelegate stor12 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  mem[96] = _version.length
  mem[128 len _version.length] = _version[all]
  mem[_version.length + 128] = 0
  mem[ceil32(_version.length) + 128] = _data.length
  mem[ceil32(_version.length) + 160 len _data.length] = _data[all]
  mem[ceil32(_version.length) + _data.length + 160] = 0
  if stor12 == _implementation:
      revert with 0, 
                  32,
                  70,
                  0x744f6c642061646472657373206973206e6f7420616c6c6f77656420616e6420696d706c656d656e746174696f6e20616464726573732073686f756c64206e6f742062652030,
                  mem[ceil32(_version.length) + ceil32(_data.length) + 298 len 26]
  if not _implementation:
      revert with 0, 
                  32,
                  70,
                  0x744f6c642061646472657373206973206e6f7420616c6c6f77656420616e6420696d706c656d656e746174696f6e20616464726573732073686f756c64206e6f742062652030,
                  mem[ceil32(_version.length) + ceil32(_data.length) + 298 len 26]
  if not ext_code.size(_implementation):
      revert with 0, 
                  32,
                  59,
                  0x7843616e6e6f742073657420612070726f787920696d706c656d656e746174696f6e20746f2061206e6f6e2d636f6e747261637420616464726573,
                  mem[ceil32(_version.length) + ceil32(_data.length) + 287 len 5]
  if _version.length <= 0:
      revert with 0, 
                  32,
                  34,
                  0xfe56657273696f6e2073686f756c64206e6f7420626520656d70747920737472696e,
                  mem[ceil32(_version.length) + ceil32(_data.length) + 262 len 30]
  mem[ceil32(_version.length) + ceil32(_data.length) + 192 len floor32(_version.length)] = call.data[_version + 36 len floor32(_version.length)]
  mem[ceil32(_version.length) + ceil32(_data.length) + floor32(_version.length) + -(_version.length % 32) + 224 len _version.length % 32] = mem[floor32(_version.length) + -(_version.length % 32) + 160 len _version.length % 32]
  mem[ceil32(_version.length) + ceil32(_data.length) + 160] = _version.length
  [94m_218 = sha3(mem[ceil32(_version.length) + ceil32(_data.length) + 192 len Mask(8 * -ceil32(_data.length) + _data.length + 32, 0, 0), mem[ceil32(_version.length) + _data.length + 192 len -_data.length + ceil32(_data.length)]])
  mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + 224] = uint256(stor11.field_0)
  [94midx = _version.length + ceil32(_version.length) + ceil32(_data.length) + 224
  [94ms = 0
  while _version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + 192 > [94midx:
      mem[[94midx + 32] = stor11[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + 192] = stor11.length
  mem[64] = _version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + 224
  if sha3(mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + 224 len stor11.length]) == [94m_218:
      revert with 0, 'New version equals to current'
  mem[0] = 11
  stor11[].field_0 = Array(len=_version.length, data=_version[all])
  stor12 = _implementation
  mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + 224] = 32
  mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + 256] = _version.length
  mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + 288 len ceil32(_version.length)] = _version[all], mem[_version.length + 128 len ceil32(_version.length) - _version.length]
  log Upgraded(
        string version=Array(len=_version.length, data=_version[all]),
        address implementation=_implementation)
  [94m_1201 = Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)]
  mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + 224 len floor32(Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)])] = mem[ceil32(_version.length) + 160 len floor32(Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)])]
  mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + floor32(Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)]) + 224] = mem[ceil32(_version.length) + floor32(Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)]) + -(Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)] % 32) + 192 len Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)] % 32] or Mask(8 * -(Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)] % 32) + 32, -(8 * -(Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)] % 32) + 32) + 256, mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + floor32(Mask(8 * -ceil32(_version.length) + _version.length + 32, 0, 0), mem[_version.length + 160 len -_version.length + ceil32(_version.length)]) + 224])
  call this.address with:
     value call.value wei
       gas gas_remaining wei
      args mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + 228 len [94m_1201 - 4]
  if not return_data.size:
      if not ext_call.success:
          revert with 0, 
                      32,
                      57,
                      0x674661696c20696e20657865637574696e67207468652066756e6374696f6e206f6620696d706c656d656e746174696f6e20636f6e74726163,
                      mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + 349 len 7]
  else:
      if not ext_call.success:
          revert with 0, 
                      32,
                      57,
                      0x674661696c20696e20657865637574696e67207468652066756e6374696f6e206f6620696d706c656d656e746174696f6e20636f6e74726163,
                      mem[_version.length + ceil32(_version.length) + ceil32(_data.length) + stor11.length + ceil32(return_data.size) + 350 len 7]
  ('bool', 'ext_call.success')


# hash = 0xa209a29c
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 1]]]]], ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknowna209a29c(uint256 _param1): # not payable
  return unknowna209a29c[_param1][0 len unknowna209a29c[_param1].length]


# hash = 0xa8f0d3a7
# getter = None
# const = None
# payable = False
def unknowna8f0d3a7(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if not stor7[_param1].field_0:
      mem[(32 * stor7[_param1].field_0) + 128] = 32
      mem[(32 * stor7[_param1].field_0) + 160] = stor7[_param1].field_0
      mem[(32 * stor7[_param1].field_0) + 192 len floor32(stor7[_param1].field_0)] = mem[128 len floor32(stor7[_param1].field_0)]
      return memory
        from (32 * stor7[_param1].field_0) + 128
         [93mlen (96 * stor7[_param1].field_0) + 64
  mem[128] = stor7[_param1].field_0
  [94midx = 128
  [94ms = 0
  while (32 * stor7[_param1].field_0) + 96 > [94midx:
      mem[[94midx + 32] = stor7[_param1][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * stor7[_param1].field_0) + 192 len floor32(stor7[_param1].field_0)] = mem[128 len floor32(stor7[_param1].field_0)]
  return Array(len=stor7[_param1].field_0, data=mem[128 len floor32(stor7[_param1].field_0)], mem[(32 * stor7[_param1].field_0) + floor32(stor7[_param1].field_0) + 192 len (32 * stor7[_param1].field_0) - floor32(stor7[_param1].field_0)]), 


# hash = 0xe82617fb
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 0]]]
# const = None
# payable = False
def unknowne82617fb(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknowne82617fb[_param1]


# hash = 0xf1739cae
# getter = None
# const = None
# payable = False
def transferProxyOwnership(address _newOwner): # not payable
  require calldata.size - 4 >= 32
  if stor13 != caller:
      [93mdelegate stor12 with:
         funct call.data[0 len 4]
           gas gas_remaining wei
          args call.data[4 len calldata.size - 4]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      return ext_call.return_data[0 len return_data.size]
  if not _newOwner:
      revert with 0, 'Address should not be 0x'
  log ProxyOwnershipTransferred(
        address previousOwner=stor13,
        address newOwner=_newOwner)
  stor13 = _newOwner


# hash = 0xf6fcbee1
# getter = None
# const = None
# payable = False
def unknownf6fcbee1(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if stor8[_param1].field_0:
      mem[128] = stor8[_param1].field_0
      if (32 * stor8[_param1].field_0) + 32 > 64:
          mem[160] = stor8[_param1].field_256
          [94midx = 160
          [94ms = 1
          while (32 * stor8[_param1].field_0) + 96 > [94midx:
              mem[[94midx + 32] = stor8[_param1][[94ms].field_256
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              continue 
  mem[(32 * stor8[_param1].field_0) + 128] = 32
  mem[(32 * stor8[_param1].field_0) + 160] = stor8[_param1].field_0
  mem[(32 * stor8[_param1].field_0) + 192 len floor32(stor8[_param1].field_0)] = mem[128 len floor32(stor8[_param1].field_0)]
  return memory
    from (32 * stor8[_param1].field_0) + 128
     [93mlen (96 * stor8[_param1].field_0) + 64


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  [93mdelegate stor12 with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


