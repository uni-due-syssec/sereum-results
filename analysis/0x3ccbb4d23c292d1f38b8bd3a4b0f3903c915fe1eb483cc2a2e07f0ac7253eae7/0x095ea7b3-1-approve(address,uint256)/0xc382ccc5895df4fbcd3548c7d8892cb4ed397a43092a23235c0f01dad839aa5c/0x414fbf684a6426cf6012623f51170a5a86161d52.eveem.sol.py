# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x414FBf684A6426cf6012623f51170a5A86161d52 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    name # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    emitters
    # storage address 4
    versions
    # storage address 5
    versionInfo
    # storage address 6
    latestVersion # mask: a s
# hash = 0x06fdde03
# getter = ['storage', 256, 0, 1]
# const = None
# payable = True
def name() payable: 
  return name


# hash = 0x12ab7242
# getter = None
# const = None
# payable = True
def setupStackDepthLib(address _stackDepthLib) payable: 
  if addr(stor2) != 0:
      return 0
  uint256(stor2) = _stackDepthLib or Mask(96, 160, uint256(stor2))
  return 1


# hash = 0x13426d87
# getter = None
# const = None
# payable = True
def addEmitter(bytes4 _eventSignature, address _emitter) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if not addr(stor0):
      return 0
  call addr(stor0).0xa1add510 with:
       gas gas_remaining - 25050 wei
      args name, 0x61646d696e000000000000000000000000000000000000000000000000000000, caller
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  if addr(emitters[Mask(32, 224, _eventSignature)]):
      return 0
  uint256(emitters[Mask(32, 224, _eventSignature)]) = _emitter or Mask(96, 160, uint256(emitters[Mask(32, 224, _eventSignature)]))
  return 1


# hash = 0x21f8a721
# getter = None
# const = None
# payable = True
def getAddress(bytes32 _key) payable: 
  call addr(stor0).0x2ade6c36 with:
       gas gas_remaining - 25050 wei
      args _key
  require ext_call.success
  return ext_call.return_data[12 len 20]


# hash = 0x488725a0
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = True
def versions(address _param1) payable: 
  return versions[_param1]


# hash = 0x62d020d9
# getter = None
# const = None
# payable = True
def addVersion(address _caller, string _name, string _changelog) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if not addr(stor0):
      return 0
  call addr(stor0).0xa1add510 with:
       gas gas_remaining - 25050 wei
      args name, 0x61646d696e000000000000000000000000000000000000000000000000000000, caller
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  if versions[addr(_caller)]:
      return 0
  if 0 == _name.length:
      return 0
  if 0 == _changelog.length:
      return 0
  latestVersion++
  versions[addr(_caller)] = latestVersion + 1
  versionInfo[stor6 + 1].field_0 = block.number
  versionInfo[stor6 + 1].field_256 = caller
  versionInfo[stor6 + 1].field_512 = _caller or Mask(96, 160, versionInfo[stor6 + 1].field_512)
  versionInfo[stor6 + 1][3][].field_0 = Array(len=_name.length, data=_name[all])
  versionInfo[stor6 + 1][4][].field_0 = Array(len=_changelog.length, data=_changelog[all])
  return 1


# hash = 0x7948f523
# getter = None
# const = None
# payable = True
def setAmbiAddress(address _ambi, bytes32 _name) payable: 
  if addr(stor0) != 0:
      return 0
  call _ambi.0x2ade6c36 with:
       gas gas_remaining - 25050 wei
      args _name
  require ext_call.success
  if ext_call.return_data[12 len 20] != this.address:
      call _ambi.0x76849376 with:
           gas gas_remaining - 25050 wei
          args _name, this.address
      require ext_call.success
      if not ext_call.return_data[0]:
          return 0
  name = _name
  uint256(stor0) = _ambi or Mask(96, 160, uint256(stor0))
  return 1


# hash = 0x87114b8c
# getter = ['struct', ['loc', 5]]
# const = None
# payable = True
def versionInfo(uint256 _param1) payable: 
  mem[288] = versionInfo[_param1][3].field_0
  [94midx = 288
  [94ms = 0
  while versionInfo[_param1][3].length + 288 > [94midx + 32:
      mem[[94midx + 32] = versionInfo[_param1][[94ms + 3].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[versionInfo[_param1][3].length + (floor32(versionInfo[_param1][3].length - 1) + -versionInfo[_param1][3].length + 32 % 32) + 288] = versionInfo[_param1][4].length
  mem[versionInfo[_param1][3].length + (floor32(versionInfo[_param1][3].length - 1) + -versionInfo[_param1][3].length + 32 % 32) + 320] = versionInfo[_param1][4].field_0
  [94midx = versionInfo[_param1][3].length + (floor32(versionInfo[_param1][3].length - 1) + -versionInfo[_param1][3].length + 32 % 32) + 320
  [94ms = 0
  while versionInfo[_param1][3].length + (floor32(versionInfo[_param1][3].length - 1) + -versionInfo[_param1][3].length + 32 % 32) + versionInfo[_param1][4].length + 320 > [94midx + 32:
      mem[[94midx + 32] = versionInfo[_param1][[94ms + 4].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return versionInfo[_param1].field_0, 
         versionInfo[_param1].field_256,
         versionInfo[_param1].field_512,
         Array(len=versionInfo[_param1][3].length, data=mem[288 len versionInfo[_param1][3].length + (floor32(versionInfo[_param1][3].length - 1) + -versionInfo[_param1][3].length + 32 % 32) + versionInfo[_param1][4].length + (floor32(versionInfo[_param1][4].length - 1) + -versionInfo[_param1][4].length + 32 % 32) + 32]),
         versionInfo[_param1][3].length + (floor32(versionInfo[_param1][3].length - 1) + -versionInfo[_param1][3].length + 32 % 32) + 192


# hash = 0xa7f43779
# getter = None
# const = None
# payable = True
def remove() payable: 
  if not addr(stor0):
      stop
  call addr(stor0).0xa1add510 with:
       gas gas_remaining - 25050 wei
      args name, 'owner', caller
  require ext_call.success
  if not ext_call.return_data[0]:
      stop
  [93mselfdestruct([91mcaller[93m)


# hash = 0xc07f47d4
# getter = ['storage', 256, 0, 6]
# const = None
# payable = True
def latestVersion() payable: 
  return latestVersion


# hash = 0xe33dafbf
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 3]]]
# const = None
# payable = True
def emitters(bytes4 _param1) payable: 
  return addr(emitters[_param1])


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if call.value <= 0:
      if not versions[caller]:
          stop
      [93mdelegate addr(emitters[call.func_hash]) with:
         funct call.data[0 len 4]
           gas gas_remaining - 50 wei
          args call.data[4 len calldata.size - 4]
      if delegate.return_code:
          if delegate.return_data[0]:
              stop
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      if ext_call.success:
          if not versions[caller]:
              stop
          [93mdelegate addr(emitters[call.func_hash]) with:
             funct call.data[0 len 4]
               gas gas_remaining - 50 wei
              args call.data[4 len calldata.size - 4]
          if delegate.return_code:
              if delegate.return_data[0]:
                  stop
  revert 


