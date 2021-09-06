# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x920C890a90dB8fbA7604864b0cF38Ee667331323 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0xab7366f7': 'remove(GroveLib.Index storage _index, bytes32 _id)', '0xbacd6958': 'insert(GroveLib.Index storage _index, bytes32 _id, int256 _value)', '0xe6ce3a6a': 'query(GroveLib.Index storage _index, bytes2 _operator, int256 _value)'} 

# storage definitions
def storage:
    # storage address 1
    nodeValue
    # storage address 2
    nodeParent
    # storage address 3
    nodeLeftChild
    # storage address 4
    nodeRightChild
    # storage address 5
    nodeHeight
# hash = 0x0e9f1a3c
# getter = ['storage', 256, 0, ['add', 4, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]]
# const = None
# payable = True
def getNodeRightChild(GroveLib.Index storage m_index, bytes32 m_nodeId) payable: 
  return mnodeRightChildm[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]


# hash = 0x2b4096b4
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]]
# const = None
# payable = True
def getNodeLeftChild(GroveLib.Index storage m_index, bytes32 m_nodeId) payable: 
  return mnodeLeftChildm[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]


# hash = 0x6ec13982
# getter = ['storage', 256, 0, ['add', 2, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]]
# const = None
# payable = True
def getNodeParent(GroveLib.Index storage m_index, bytes32 m_nodeId) payable: 
  return mnodeParentm[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]


# hash = 0xa3119e57
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]]
# const = None
# payable = True
def getNodeValue(GroveLib.Index storage m_index, bytes32 m_nodeId) payable: 
  return mnodeValuem[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]


# hash = 0xa749f19b
# getter = ['storage', 256, 0, ['add', 5, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]]
# const = None
# payable = True
def getNodeHeight(GroveLib.Index storage m_index, bytes32 m_nodeId) payable: 
  return mnodeHeightm[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]


# hash = 0xbfdf87c0
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]
# const = None
# payable = True
def getNodeId(GroveLib.Index storage m_index, bytes32 m_nodeId) payable: 
  return mstor[m_index + 1m]m[m_nodeIdm]


# hash = 0xc4144b26
# getter = None
# const = None
# payable = True
def getNextNode(GroveLib.Index storage m_index, bytes32 m_nodeId) payable: 
  mem[96] = 0
  mem[128] = 0
  mem[160] = 0
  mem[192] = 0
  mem[224] = 0
  mem[256] = 0
  if 0 == mstor[m_index + 1m]m[m_nodeIdm]:
      return 0
  if 0 == mnodeRightChildm[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]:
      if 0 == mnodeParentm[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]:
          return 0
      mem[64] = 480
      [94midx = 0
      [94ms = 288
      mwhile mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 3m] != mstor[m_index + 1m]m[m_nodeIdm]m:
          if 0 == mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2m]:
              return 0
          [94m_29 = mem[64]
          mem[64] = mem[64] + 192
          mem[[94m_29] = mstor[m_index + 1m]m[mstor2m[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]m]m[[94midxm]
          mem[[94m_29 + 32] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 1m]
          mem[[94m_29 + 64] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2m]
          mem[[94m_29 + 96] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 3m]
          mem[[94m_29 + 128] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 4m]
          mem[[94m_29 + 160] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 5m]
          mem[0] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2m]
          mem[32] = m_index + 1
          [94midx = sha3(mnodeParentm[[94midxm], m_index + 1)
          [94ms = [94m_29
          mcontinue 
      return mstor[[94midxm]
  mem[0] = mnodeRightChildm[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]
  mem[32] = m_index + 1
  mem[64] = 480
  mem[288] = mstor[m_index + 1m]m[mstor4m[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]m]
  mem[320] = mnodeValuem[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor4', 4))), ('add', 1, ('param', '_index')))m]
  mem[352] = mnodeParentm[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor4', 4))), ('add', 1, ('param', '_index')))m]
  mem[384] = mnodeLeftChildm[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor4', 4))), ('add', 1, ('param', '_index')))m]
  mem[416] = mnodeRightChildm[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'nodeRightChild', 4))), ('add', 1, ('param', '_index')))m]
  mem[448] = mnodeHeightm[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor4', 4))), ('add', 1, ('param', '_index')))m]
  [94ms = 288
  mwhile mnodeLeftChildm[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor4', 4))), ('add', 1, ('param', '_index')))m] != 0m:
      mem[0] = mem[[94ms + 96]
      mem[32] = m_index + 1
      [94m_27 = sha3(mem[0], m_index + 1)
      [94m_28 = mem[64]
      mem[64] = mem[64] + 192
      mem[[94m_28] = mstor[m_index + 1m]m[mem[0]m]
      mem[[94m_28 + 32] = mnodeValuem[[94m_27m]
      mem[[94m_28 + 64] = mnodeParentm[[94m_27m]
      mem[[94m_28 + 96] = mnodeLeftChildm[[94m_27m]
      mem[[94m_28 + 128] = mnodeRightChildm[[94m_27m]
      mem[[94m_28 + 160] = mnodeHeightm[[94m_27m]
      [94ms = [94m_28
      mcontinue 
  mem[mem[64]] = mem[[94ms]
  return memory
    from mem[64]
     [93mlen 32


# hash = 0xcaa46c9c
# getter = None
# const = None
# payable = True
def getPreviousNode(GroveLib.Index storage m_index, bytes32 m_nodeId) payable: 
  mem[96] = 0
  mem[128] = 0
  mem[160] = 0
  mem[192] = 0
  mem[224] = 0
  mem[256] = 0
  if 0 == mstor[m_index + 1m]m[m_nodeIdm]:
      return 0
  if 0 == mnodeLeftChildm[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]:
      if 0 == mnodeParentm[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]:
          return 0
      mem[64] = 480
      [94midx = 0
      [94ms = 288
      mwhile mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 4m] != mstor[m_index + 1m]m[m_nodeIdm]m:
          if 0 == mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2m]:
              return 0
          [94m_31 = mem[64]
          mem[64] = mem[64] + 192
          mem[[94m_31] = mstor[m_index + 1m]m[mstor2m[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]m]m[[94midxm]
          mem[[94m_31 + 32] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 1m]
          mem[[94m_31 + 64] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2m]
          mem[[94m_31 + 96] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 3m]
          mem[[94m_31 + 128] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 4m]
          mem[[94m_31 + 160] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 5m]
          mem[0] = mstor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2m]
          mem[32] = m_index + 1
          [94midx = sha3(mnodeParentm[[94midxm], m_index + 1)
          [94ms = [94m_31
          mcontinue 
      return mstor[[94midxm]
  mem[0] = mnodeLeftChildm[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]
  mem[32] = m_index + 1
  mem[64] = 480
  mem[288] = mstor[m_index + 1m]m[mstor3m[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))m]m]
  mem[320] = mnodeValuem[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor3', 3))), ('add', 1, ('param', '_index')))m]
  mem[352] = mnodeParentm[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor3', 3))), ('add', 1, ('param', '_index')))m]
  mem[384] = mnodeLeftChildm[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'nodeLeftChild', 3))), ('add', 1, ('param', '_index')))m]
  mem[416] = mnodeRightChildm[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor3', 3))), ('add', 1, ('param', '_index')))m]
  mem[448] = mnodeHeightm[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor3', 3))), ('add', 1, ('param', '_index')))m]
  [94ms = 288
  mwhile mnodeRightChildm[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor3', 3))), ('add', 1, ('param', '_index')))m] != 0m:
      mem[0] = mem[[94ms + 128]
      mem[32] = m_index + 1
      [94m_29 = sha3(mem[0], m_index + 1)
      [94m_30 = mem[64]
      mem[64] = mem[64] + 192
      mem[[94m_30] = mstor[m_index + 1m]m[mem[0]m]
      mem[[94m_30 + 32] = mnodeValuem[[94m_29m]
      mem[[94m_30 + 64] = mnodeParentm[[94m_29m]
      mem[[94m_30 + 96] = mnodeLeftChildm[[94m_29m]
      mem[[94m_30 + 128] = mnodeRightChildm[[94m_29m]
      mem[[94m_30 + 160] = mnodeHeightm[[94m_29m]
      [94ms = [94m_30
      mcontinue 
  mem[mem[64]] = mem[[94ms]
  return memory
    from mem[64]
     [93mlen 32


# hash = 0xed5bd7ea
# getter = None
# const = None
# payable = True
def exists(GroveLib.Index storage m_index, bytes32 m_id) payable: 
  return (m_id == mstor[m_index + 1m]m[m_idm])


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


