# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x0ea6683d9c7eb95329b11310364574430c7549bd 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown26839e53
    # storage address 1
    unknown69ba0fe9
    # storage address 2
    unknownbaed8bb1
    # storage address 3
    unknownc6cb7ab8
    # storage address 4
    stor4
    # storage address 6
    unknownb3447ac9
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


# hash = 0x1d8acf1b
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]]
# const = None
# payable = False
def unknown1d8acf1b(uint256 _param1): # not payable
  return bool(stor4[_param1])


# hash = 0x26839e53
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 0]]]
# const = None
# payable = False
def unknown26839e53(uint256 _param1): # not payable
  return unknown26839e53[_param1]


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
  if stor12 == _implementation:
      revert with 0, 'Old address is not allowed and implementation address should not be 0x'
  if not _implementation:
      revert with 0, 'Old address is not allowed and implementation address should not be 0x'
  if ext_code.size(_implementation) <= 0:
      revert with 0, 'Cannot set a proxy implementation to a non-contract address'
  if 0 >= _version.length:
      revert with 0, 'Version should not be empty string'
  mem[ceil32(_version.length) + 160 len floor32(_version.length)] = call.data[_version + 36 len floor32(_version.length)]
  mem[ceil32(_version.length) + floor32(_version.length) + -(_version.length % 32) + 192 len _version.length % 32] = mem[floor32(_version.length) + -(_version.length % 32) + 160 len _version.length % 32]
  mem[ceil32(_version.length) + 128] = _version.length
  mem[_version.length + ceil32(_version.length) + 160 len floor32(_version.length)] = call.data[_version + 36 len floor32(_version.length)]
  mem[(2 * floor32(_version.length)) + ceil32(_version.length) + 192 len _version.length % 32] = mem[ceil32(_version.length) + -(_version.length % 32) + floor32(_version.length) + 192 len _version.length % 32]
  [94m_182 = sha3(call.data[_version + 36 len floor32(_version.length)], mem[_version.length + ceil32(_version.length) + floor32(_version.length) + 160 len _version.length % 32])
  mem[_version.length + ceil32(_version.length) + 192] = uint256(stor11.field_0)
  [94midx = _version.length + ceil32(_version.length) + 192
  [94ms = 0
  while _version.length + ceil32(_version.length) + stor11.length + 160 > [94midx:
      mem[[94midx + 32] = stor11[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[_version.length + ceil32(_version.length) + 160] = stor11.length
  mem[64] = _version.length + ceil32(_version.length) + stor11.length + 192
  mem[_version.length + ceil32(_version.length) + stor11.length + 192 len floor32(stor11.length)] = mem[_version.length + ceil32(_version.length) + 192 len floor32(stor11.length)]
  mem[_version.length + ceil32(_version.length) + stor11.length + floor32(stor11.length) + -stor11.length % 32 + 224 len stor11.length % 32] = mem[_version.length + ceil32(_version.length) + floor32(stor11.length) + -stor11.length % 32 + 224 len stor11.length % 32]
  if sha3(mem[_version.length + ceil32(_version.length) + stor11.length + 192 len stor11.length]) == [94m_182:
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


# hash = 0x69ba0fe9
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 1]]]]], ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown69ba0fe9(uint256 _param1): # not payable
  return unknown69ba0fe9[_param1][0 len unknown69ba0fe9[_param1].length]


# hash = 0x958a41dd
# getter = None
# const = None
# payable = True
def upgradeToAndCall(string _version, address _implementation, bytes _data) payable: 
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
  if stor12 == _implementation:
      revert with 0, 'Old address is not allowed and implementation address should not be 0x'
  if not _implementation:
      revert with 0, 'Old address is not allowed and implementation address should not be 0x'
  if ext_code.size(_implementation) <= 0:
      revert with 0, 'Cannot set a proxy implementation to a non-contract address'
  if 0 >= _version.length:
      revert with 0, 'Version should not be empty string'
  mem[ceil32(_version.length) + 160 len floor32(_version.length)] = call.data[_version + 36 len floor32(_version.length)]
  mem[ceil32(_version.length) + floor32(_version.length) + -(_version.length % 32) + 192 len _version.length % 32] = mem[floor32(_version.length) + -(_version.length % 32) + 160 len _version.length % 32]
  mem[ceil32(_version.length) + 128] = _version.length
  mem[_version.length + ceil32(_version.length) + 160 len floor32(_version.length)] = call.data[_version + 36 len floor32(_version.length)]
  mem[(2 * floor32(_version.length)) + ceil32(_version.length) + 192 len _version.length % 32] = mem[ceil32(_version.length) + -(_version.length % 32) + floor32(_version.length) + 192 len _version.length % 32]
  [94m_278 = sha3(call.data[_version + 36 len floor32(_version.length)], mem[_version.length + ceil32(_version.length) + floor32(_version.length) + 160 len _version.length % 32])
  mem[_version.length + ceil32(_version.length) + 192] = uint256(stor11.field_0)
  [94midx = _version.length + ceil32(_version.length) + 192
  [94ms = 0
  while _version.length + ceil32(_version.length) + stor11.length + 160 > [94midx:
      mem[[94midx + 32] = stor11[[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[_version.length + ceil32(_version.length) + 160] = stor11.length
  mem[64] = _version.length + ceil32(_version.length) + stor11.length + 192
  mem[_version.length + ceil32(_version.length) + stor11.length + 192 len floor32(stor11.length)] = mem[_version.length + ceil32(_version.length) + 192 len floor32(stor11.length)]
  mem[_version.length + ceil32(_version.length) + stor11.length + floor32(stor11.length) + -stor11.length % 32 + 224 len stor11.length % 32] = mem[_version.length + ceil32(_version.length) + -stor11.length % 32 + floor32(stor11.length) + 224 len stor11.length % 32]
  if sha3(mem[_version.length + ceil32(_version.length) + stor11.length + 192 len stor11.length]) == [94m_278:
      revert with 0, 'New version equals to current'
  stor11[].field_0 = Array(len=_version.length, data=_version[all])
  stor12 = _implementation
  log Upgraded(
        string version=Array(len=_version.length, data=_version[all]),
        address implementation=_implementation)
  call this.address with:
     value call.value wei
       gas gas_remaining wei
      args _data[all]
  if not ext_call.success:
      revert with 0, 'Fail in executing the function of implementation contract'


# hash = 0xb3447ac9
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def unknownb3447ac9(uint256 _param1): # not payable
  return unknownb3447ac9[_param1]


# hash = 0xbaed8bb1
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def unknownbaed8bb1(uint256 _param1): # not payable
  return unknownbaed8bb1[_param1]


# hash = 0xc6cb7ab8
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 3]]]]], ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = False
def unknownc6cb7ab8(uint256 _param1): # not payable
  return unknownc6cb7ab8[_param1][0 len unknownc6cb7ab8[_param1].length]


# hash = 0xf1739cae
# getter = None
# const = None
# payable = False
def transferProxyOwnership(address _newOwner): # not payable
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


