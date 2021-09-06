# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x98a715181466035e10Ea4B7da5635a356b1D1C4d 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x4f71ef81': 'parse(bytes32 _icap)'} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1
    # storage address 2
    addr
    # storage address 3
    institutionOwners
    # storage address 4
    assets
# hash = 0x12ab7242
# getter = None
# const = None
# payable = True
def setupStackDepthLib(address _stackDepthLib) payable: 
  if addr(stor0) != 0:
      return 0
  uint256(stor0) = _stackDepthLib or Mask(96, 160, uint256(stor0))
  return 1


# hash = 0x3b3b57de
# getter = ['storage', 160, 0, ['sha3', ['data', ['sha3', ['data', ['mask_shl', 24, 232, -232, "'ETH'"], 0, ['mask_shl', 8, ['add', 256, ['mul', -1, [['mask_shl', 256, 0, -3, ['cd', 4]], 0]]], ['add', -256, [['mask_shl', 256, 0, -3, ['cd', 4]], 0]], 1], ['mask_shl', 8, ['add', 256, ['mul', -1, [['mask_shl', 256, 0, -3, ['cd', 4]], 0]]], ['add', -256, [['mask_shl', 256, 0, -3, ['cd', 4]], 0]], 2], ['mask_shl', 8, ['add', 256, ['mul', -1, [['mask_shl', 256, 0, -3, ['cd', 4]], 0]]], ['add', -256, [['mask_shl', 256, 0, -3, ['cd', 4]], 0]], 3]]], 2]]]
# const = None
# payable = True
def addr(bytes32 _node) payable: 
  return addr(addr['ETH'][0][Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_node')), 0) + 256, 1) << (('mask_shl', 256, 0, -3, ('param', '_node')), 0) - 256][Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_node')), 0) + 256, 2) << (('mask_shl', 256, 0, -3, ('param', '_node')), 0) - 256][Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_node')), 0) + 256, 3) << (('mask_shl', 256, 0, -3, ('param', '_node')), 0) - 256])


# hash = 0x5524d548
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = True
def registered(bytes32 _param1) payable: 
  return bool(stor1[_param1])


# hash = 0x65bdfd2e
# getter = None
# const = None
# payable = True
def changeInstitutionOwner(string _institution, address _address) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if addr(institutionOwners[_institution[all]]) != caller:
      return 0
  uint256(institutionOwners[_institution[all]]) = _address or Mask(96, 160, uint256(institutionOwners[_institution[all]]))
  return 1


# hash = 0x67f10e8c
# getter = None
# const = None
# payable = True
def updateInstitutionAsset(string _asset, string _institution, address _address) payable: 
  mem[ceil32(_asset.length) + 160 len _institution.length] = _institution[all]
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length] = _institution[all]
  if addr(institutionOwners[_institution[all]]) != caller:
      return 0
  mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _asset.length] = _asset[all]
  mem[_asset.length + ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length] = _institution[all]
  if not stor1[mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length + _asset.length]]:
      return 0
  uint256(addr[mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length + _asset.length]]) = _address or Mask(96, 160, uint256(addr[mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length + _asset.length]]))
  return 1


# hash = 0x7e32fc47
# getter = None
# const = None
# payable = True
def registerAsset(string _asset, bytes32 _symbol) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if _asset.length != 3:
      return 0
  if stor1[_asset[all]]:
      return 0
  stor1[_asset[all]] = 1
  assets[_asset[all]] = _symbol
  return 1


# hash = 0x8f87b786
# getter = None
# const = None
# payable = True
def registerInstitutionAsset(string _asset, string _institution, address _address) payable: 
  mem[ceil32(_asset.length) + 160 len _institution.length] = _institution[all]
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length] = _institution[all]
  if addr(institutionOwners[_institution[all]]) != caller:
      return 0
  if not stor1[_asset[all]]:
      return 0
  mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _asset.length] = _asset[all]
  mem[_asset.length + ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length] = _institution[all]
  if stor1[mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length + _asset.length]]:
      return 0
  stor1[mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length + _asset.length]] = 1
  uint256(addr[mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length + _asset.length]]) = _address or Mask(96, 160, uint256(addr[mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length + _asset.length]]))
  return 1


# hash = 0x95829738
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = True
def institutions(bytes32 _param1) payable: 
  return addr(addr[_param1])


# hash = 0x9fda5b66
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = True
def assets(bytes32 _param1) payable: 
  return assets[_param1]


# hash = 0xbd23cd30
# getter = None
# const = None
# payable = True
def registerInstitution(string _institution, address _address) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if _institution.length != 4:
      return 0
  if addr(institutionOwners[_institution[all]]) != 0:
      return 0
  uint256(institutionOwners[_institution[all]]) = _address or Mask(96, 160, uint256(institutionOwners[_institution[all]]))
  return 1


# hash = 0xc221c620
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 3]]]
# const = None
# payable = True
def institutionOwners(bytes32 _param1) payable: 
  return addr(institutionOwners[_param1])


# hash = 0xcf82601b
# getter = None
# const = None
# payable = True
def removeInstitutionAsset(string _asset, string _institution) payable: 
  mem[ceil32(_asset.length) + 160 len _institution.length] = _institution[all]
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length] = _institution[all]
  if addr(institutionOwners[_institution[all]]) != caller:
      return 0
  mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _asset.length] = _asset[all]
  mem[_asset.length + ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length] = _institution[all]
  if not stor1[mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length + _asset.length]]:
      return 0
  stor1[mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length + _asset.length]] = 0
  addr(addr[mem[ceil32(_asset.length) + ceil32(_institution.length) + 160 len _institution.length + _asset.length]]) = 0
  return 1


# hash = 0xd7768c47
# getter = None
# const = None
# payable = True
def prepare(bytes _bban) payable: 
  mem[128 len _bban.length] = _bban[all]
  mem[ceil32(_bban.length) + 128] = 0
  [94ms = 0
  [94midx = 0
  while uint8([94midx) < 16:
      require uint8([94midx) < _bban.length
      [94m_9 = mem[uint8([94midx) + 128]
      if mem[uint8([94midx) + 128 len 1] < 65:
          [94ms = mem[uint8([94midx) + 128 len 1]
          [94midx = [94midx + 1
          continue 
      if mem[uint8([94midx) + 128 len 1] > 90:
          [94ms = mem[uint8([94midx) + 128 len 1]
          [94midx = [94midx + 1
          continue 
      require uint8([94midx) < _bban.length
      mem[uint8([94midx) + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', -55, ('mem', ('range', ('add', 128, ('mask_shl', 8, 0, 0, ('var', 0))), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', -55, ('mem', ('range', ('add', 128, ('mask_shl', 8, 0, 0, ('var', 0))), 1)))), 0) - 256
      [94ms = Mask(8, 248, [94m_9) >> 248
      [94midx = [94midx + 1
      continue 
  require 16 < _bban.length
  mem[144 len 8] = 33
  require 17 < _bban.length
  mem[145 len 8] = 14
  return Array(len=_bban.length, data=mem[128 len _bban.length])


# hash = 0xe98c7608
# getter = None
# const = None
# payable = True
def mod9710(bytes _prepared) payable: 
  mem[128 len _prepared.length] = _prepared[all]
  [94ms = 0
  [94midx = 0
  [94ms = 0
  while uint8([94midx) < 18:
      require uint8([94midx) < _prepared.length
      if mem[uint8([94midx) + 128 len 1] < 48:
          [94ms = mem[uint8([94midx) + 128 len 1]
          [94midx = [94midx + 1
          [94ms = (10 * (10 * [94ms) + uint8(mem[uint8([94midx) + 128 len 1] / 10) % 97) + uint8(mem[uint8([94midx) + 128 len 1] % 10) % 97
          continue 
      [94ms = mem[uint8([94midx) + 128 len 1]
      [94midx = [94midx + 1
      [94ms = uint8(mem[uint8([94midx) + 128 len 1] - 48) + (10 * [94ms) % 97
      continue 
  return uint8(10 * 10 * [94ms % 97 % 97)


# hash = 0xee9ce090
# getter = None
# const = None
# payable = True
def decodeIndirect(bytes _bban) payable: 
  mem[96] = _bban.length
  mem[128 len _bban.length] = _bban[all]
  mem[ceil32(_bban.length) + 128] = 0
  mem[ceil32(_bban.length) + 160] = 0
  mem[ceil32(_bban.length) + 192] = 0
  mem[ceil32(_bban.length) + 224] = 0
  mem[ceil32(_bban.length) + 256] = 0
  mem[ceil32(_bban.length) + 288] = 0
  mem[ceil32(_bban.length) + 320] = 3
  mem[ceil32(_bban.length) + 448] = 4
  mem[ceil32(_bban.length) + 480] = 9
  mem[64] = ceil32(_bban.length) + 800
  [94midx = 0
  [94ms = 0
  while uint8([94midx) < 3:
      require uint8([94ms) < _bban.length
      require uint8([94midx) < mem[ceil32(_bban.length) + 320]
      mem[ceil32(_bban.length) + uint8([94midx) + 352 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('mask_shl', 8, 0, 0, ('var', 1))), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('mask_shl', 8, 0, 0, ('var', 1))), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  [94m_706 = mem[ceil32(_bban.length) + 448]
  [94midx = 0
  [94ms = None
  while uint8([94midx) < [94m_706:
      require uint8([94ms) < _bban.length
      require uint8([94midx) < mem[ceil32(_bban.length) + 448]
      mem[ceil32(_bban.length) + uint8([94midx) + 480 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('mask_shl', 8, 0, 0, ('var', 1))), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('mask_shl', 8, 0, 0, ('var', 1))), 32))), 0) - 256
      [94m_706 = mem[ceil32(_bban.length) + 448]
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  [94m_1010 = mem[ceil32(_bban.length) + 480]
  [94midx = 0
  [94ms = 2 * None
  while uint8([94midx) < [94m_1010:
      require uint8([94ms) < _bban.length
      require uint8([94midx) < mem[ceil32(_bban.length) + 480]
      mem[ceil32(_bban.length) + uint8([94midx) + 512 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('mask_shl', 8, 0, 0, ('var', 1))), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('mask_shl', 8, 0, 0, ('var', 1))), 32))), 0) - 256
      [94m_1010 = mem[ceil32(_bban.length) + 480]
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  mem[ceil32(_bban.length) + 800] = 96
  mem[ceil32(_bban.length) + 896] = mem[ceil32(_bban.length) + 320]
  mem[ceil32(_bban.length) + 928 len mem[ceil32(_bban.length) + 320]] = mem[ceil32(_bban.length) + 352 len mem[ceil32(_bban.length) + 320]]
  mem[ceil32(_bban.length) + 832] = mem[ceil32(_bban.length) + 320] + 128
  mem[mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + 928] = mem[ceil32(_bban.length) + 448]
  mem[mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + 960 len mem[ceil32(_bban.length) + 448]] = mem[ceil32(_bban.length) + 480 len mem[ceil32(_bban.length) + 448]]
  if not mem[ceil32(_bban.length) + 448] % 32:
      mem[ceil32(_bban.length) + 864] = mem[ceil32(_bban.length) + 448] + mem[ceil32(_bban.length) + 320] + 160
      mem[mem[ceil32(_bban.length) + 448] + mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + 960] = mem[ceil32(_bban.length) + 480]
      mem[mem[ceil32(_bban.length) + 448] + mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + 992 len mem[ceil32(_bban.length) + 480]] = mem[ceil32(_bban.length) + 512 len mem[ceil32(_bban.length) + 480]]
      if not mem[ceil32(_bban.length) + 480] % 32:
          return Array(len=mem[ceil32(_bban.length) + 320], data=mem[ceil32(_bban.length) + 928 len mem[ceil32(_bban.length) + 480] + mem[ceil32(_bban.length) + 448] + mem[ceil32(_bban.length) + 320] + 64]), 
                 mem[ceil32(_bban.length) + 320] + 128,
                 mem[ceil32(_bban.length) + 448] + mem[ceil32(_bban.length) + 320] + 160
      mem[floor32(mem[ceil32(_bban.length) + 480]) + mem[ceil32(_bban.length) + 448] + mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + 992] = mem[floor32(mem[ceil32(_bban.length) + 480]) + mem[ceil32(_bban.length) + 448] + mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + -(mem[ceil32(_bban.length) + 480] % 32) + 1024 len mem[ceil32(_bban.length) + 480] % 32]
      return Array(len=mem[ceil32(_bban.length) + 320], data=mem[ceil32(_bban.length) + 928 len mem[ceil32(_bban.length) + 448] + mem[ceil32(_bban.length) + 320] + 32], mem[ceil32(_bban.length) + 480], mem[ceil32(_bban.length) + mem[ceil32(_bban.length) + 448] + mem[ceil32(_bban.length) + 320] + 992 len floor32(mem[ceil32(_bban.length) + 480]) + 32]), 
             mem[ceil32(_bban.length) + 320] + 128,
             mem[ceil32(_bban.length) + 448] + mem[ceil32(_bban.length) + 320] + 160
  mem[floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + 960] = mem[floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + -(mem[ceil32(_bban.length) + 448] % 32) + 992 len mem[ceil32(_bban.length) + 448] % 32]
  mem[ceil32(_bban.length) + 864] = floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + 192
  mem[floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + 992] = mem[ceil32(_bban.length) + 480]
  mem[floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + 1024 len mem[ceil32(_bban.length) + 480]] = mem[ceil32(_bban.length) + 512 len mem[ceil32(_bban.length) + 480]]
  if not mem[ceil32(_bban.length) + 480] % 32:
      return Array(len=mem[ceil32(_bban.length) + 320], data=mem[ceil32(_bban.length) + 928 len mem[ceil32(_bban.length) + 480] + floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + 96]), 
             mem[ceil32(_bban.length) + 320] + 128,
             floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + 192
  mem[floor32(mem[ceil32(_bban.length) + 480]) + floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + 1024] = mem[floor32(mem[ceil32(_bban.length) + 480]) + floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + ceil32(_bban.length) + -(mem[ceil32(_bban.length) + 480] % 32) + 1056 len mem[ceil32(_bban.length) + 480] % 32]
  return Array(len=mem[ceil32(_bban.length) + 320], data=mem[ceil32(_bban.length) + 928 len floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + 64], mem[ceil32(_bban.length) + 480], mem[ceil32(_bban.length) + floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + 1024 len floor32(mem[ceil32(_bban.length) + 480]) + 32]), 
         mem[ceil32(_bban.length) + 320] + 128,
         floor32(mem[ceil32(_bban.length) + 448]) + mem[ceil32(_bban.length) + 320] + 192


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


