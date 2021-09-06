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
  return mname


# hash = 0x12ab7242
# getter = None
# const = None
# payable = True
def setupStackDepthLib(address m_stackDepthLib) payable: 
  if addr(mstor2) != 0:
      return 0
  uint256(mstor2) = m_stackDepthLib or Mask(96, 160, uint256(mstor2))
  return 1


# hash = 0x13426d87
# getter = None
# const = None
# payable = True
def addEmitter(bytes4 m_eventSignature, address m_emitter) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if not addr(mstor0):
      return 0
  call addr(mstor0).0xa1add510 with:
       gas gas_remaining - 25050 wei
      args mname, 0x61646d696e000000000000000000000000000000000000000000000000000000, caller
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  if addr(memittersm[Mask(32, 224, m_eventSignature)m]):
      return 0
  uint256(memittersm[Mask(32, 224, m_eventSignature)m]) = m_emitter or Mask(96, 160, uint256(memittersm[Mask(32, 224, m_eventSignature)m]))
  return 1


# hash = 0x21f8a721
# getter = None
# const = None
# payable = True
def getAddress(bytes32 m_key) payable: 
  call addr(mstor0).0x2ade6c36 with:
       gas gas_remaining - 25050 wei
      args m_key
  require ext_call.success
  return ext_call.return_data[12 len 20]


# hash = 0x488725a0
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = True
def versions(address m_param1) payable: 
  return mversionsm[m_param1m]


# hash = 0x62d020d9
# getter = None
# const = None
# payable = True
def addVersion(address m_caller, string m_name, string m_changelog) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if not addr(mstor0):
      return 0
  call addr(mstor0).0xa1add510 with:
       gas gas_remaining - 25050 wei
      args mname, 0x61646d696e000000000000000000000000000000000000000000000000000000, caller
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  if mversionsm[addr(m_caller)m]:
      return 0
  if 0 == m_name.length:
      return 0
  if 0 == m_changelog.length:
      return 0
  mlatestVersion++
  mversionsm[addr(m_caller)m] = mlatestVersion + 1
  mversionInfom[mstor6 + 1m]m.field_0 = block.number
  mversionInfom[mstor6 + 1m]m.field_256 = caller
  mversionInfom[mstor6 + 1m]m.field_512 = m_caller or Mask(96, 160, mversionInfom[mstor6 + 1m]m.field_512)
  mversionInfom[mstor6 + 1m]m[3m]m[m]m.field_0 = Array(len=m_name.length, data=m_name[allm])
  mversionInfom[mstor6 + 1m]m[4m]m[m]m.field_0 = Array(len=m_changelog.length, data=m_changelog[allm])
  return 1


# hash = 0x7948f523
# getter = None
# const = None
# payable = True
def setAmbiAddress(address m_ambi, bytes32 m_name) payable: 
  if addr(mstor0) != 0:
      return 0
  call m_ambi.0x2ade6c36 with:
       gas gas_remaining - 25050 wei
      args m_name
  require ext_call.success
  if ext_call.return_data[12 len 20] != this.address:
      call m_ambi.0x76849376 with:
           gas gas_remaining - 25050 wei
          args m_name, this.address
      require ext_call.success
      if not ext_call.return_data[0]:
          return 0
  mname = m_name
  uint256(mstor0) = m_ambi or Mask(96, 160, uint256(mstor0))
  return 1


# hash = 0x87114b8c
# getter = ['struct', ['loc', 5]]
# const = None
# payable = True
def versionInfo(uint256 m_param1) payable: 
  mem[288] = mversionInfom[m_param1m]m[3m]m.field_0
  [94midx = 288
  [94ms = 0
  mwhile mversionInfom[m_param1m]m[3m]m.length + 288 > [94midx + 32m:
      mem[[94midx + 32] = mversionInfom[m_param1m]m[[94ms + 3m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[mversionInfom[m_param1m]m[3m]m.length + (floor32(mversionInfom[m_param1m]m[3m]m.length - 1) + -mversionInfom[m_param1m]m[3m]m.length + 32 % 32) + 288] = mversionInfom[m_param1m]m[4m]m.length
  mem[mversionInfom[m_param1m]m[3m]m.length + (floor32(mversionInfom[m_param1m]m[3m]m.length - 1) + -mversionInfom[m_param1m]m[3m]m.length + 32 % 32) + 320] = mversionInfom[m_param1m]m[4m]m.field_0
  [94midx = mversionInfom[m_param1m]m[3m]m.length + (floor32(mversionInfom[m_param1m]m[3m]m.length - 1) + -mversionInfom[m_param1m]m[3m]m.length + 32 % 32) + 320
  [94ms = 0
  mwhile mversionInfom[m_param1m]m[3m]m.length + (floor32(mversionInfom[m_param1m]m[3m]m.length - 1) + -mversionInfom[m_param1m]m[3m]m.length + 32 % 32) + mversionInfom[m_param1m]m[4m]m.length + 320 > [94midx + 32m:
      mem[[94midx + 32] = mversionInfom[m_param1m]m[[94ms + 4m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return mversionInfom[m_param1m]m.field_0, 
         mversionInfom[m_param1m]m.field_256,
         mversionInfom[m_param1m]m.field_512,
         Array(len=mversionInfom[m_param1m]m[3m]m.length, data=mem[288 len mversionInfom[m_param1m]m[3m]m.length + (floor32(mversionInfom[m_param1m]m[3m]m.length - 1) + -mversionInfom[m_param1m]m[3m]m.length + 32 % 32) + mversionInfom[m_param1m]m[4m]m.length + (floor32(mversionInfom[m_param1m]m[4m]m.length - 1) + -mversionInfom[m_param1m]m[4m]m.length + 32 % 32) + 32]),
         mversionInfom[m_param1m]m[3m]m.length + (floor32(mversionInfom[m_param1m]m[3m]m.length - 1) + -mversionInfom[m_param1m]m[3m]m.length + 32 % 32) + 192


# hash = 0xa7f43779
# getter = None
# const = None
# payable = True
def remove() payable: 
  if not addr(mstor0):
      stop
  call addr(mstor0).0xa1add510 with:
       gas gas_remaining - 25050 wei
      args mname, 'owner', caller
  require ext_call.success
  if not ext_call.return_data[0]:
      stop
  [93mselfdestruct([91mcaller[93m)


# hash = 0xc07f47d4
# getter = ['storage', 256, 0, 6]
# const = None
# payable = True
def latestVersion() payable: 
  return mlatestVersion


# hash = 0xe33dafbf
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 3]]]
# const = None
# payable = True
def emitters(bytes4 m_param1) payable: 
  return addr(memittersm[m_param1m])


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if call.value <= 0:
      if not mversionsm[callerm]:
          stop
      [93mdelegate addr(memittersm[mcall.func_hashm]) with:
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
          if not mversionsm[callerm]:
              stop
          [93mdelegate addr(memittersm[mcall.func_hashm]) with:
             funct call.data[0 len 4]
               gas gas_remaining - 50 wei
              args call.data[4 len calldata.size - 4]
          if delegate.return_code:
              if delegate.return_data[0]:
                  stop
  revert 


