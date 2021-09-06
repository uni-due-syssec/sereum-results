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
def getNodeRightChild(GroveLib.Index storage _index, bytes32 _nodeId) payable: 
  return nodeRightChild[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]


# hash = 0x2b4096b4
# getter = ['storage', 256, 0, ['add', 3, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]]
# const = None
# payable = True
def getNodeLeftChild(GroveLib.Index storage _index, bytes32 _nodeId) payable: 
  return nodeLeftChild[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]


# hash = 0x6ec13982
# getter = ['storage', 256, 0, ['add', 2, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]]
# const = None
# payable = True
def getNodeParent(GroveLib.Index storage _index, bytes32 _nodeId) payable: 
  return nodeParent[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]


# hash = 0xa3119e57
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]]
# const = None
# payable = True
def getNodeValue(GroveLib.Index storage _index, bytes32 _nodeId) payable: 
  return nodeValue[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]


# hash = 0xa749f19b
# getter = ['storage', 256, 0, ['add', 5, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]]
# const = None
# payable = True
def getNodeHeight(GroveLib.Index storage _index, bytes32 _nodeId) payable: 
  return nodeHeight[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]


# hash = 0xbfdf87c0
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['add', 1, ['cd', 4]]]]]
# const = None
# payable = True
def getNodeId(GroveLib.Index storage _index, bytes32 _nodeId) payable: 
  return stor[_index + 1][_nodeId]


# hash = 0xc4144b26
# getter = None
# const = None
# payable = True
def getNextNode(GroveLib.Index storage _index, bytes32 _nodeId) payable: 
  mem[96] = 0
  mem[128] = 0
  mem[160] = 0
  mem[192] = 0
  mem[224] = 0
  mem[256] = 0
  if 0 == stor[_index + 1][_nodeId]:
      return 0
  if 0 == nodeRightChild[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]:
      if 0 == nodeParent[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]:
          return 0
      mem[64] = 480
      [94midx = 0
      [94ms = 288
      while stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 3] != stor[_index + 1][_nodeId]:
          if 0 == stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2]:
              return 0
          [94m_29 = mem[64]
          mem[64] = mem[64] + 192
          mem[[94m_29] = stor[_index + 1][stor2[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]][[94midx]
          mem[[94m_29 + 32] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 1]
          mem[[94m_29 + 64] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2]
          mem[[94m_29 + 96] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 3]
          mem[[94m_29 + 128] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 4]
          mem[[94m_29 + 160] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 5]
          mem[0] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2]
          mem[32] = _index + 1
          [94midx = sha3(nodeParent[[94midx], _index + 1)
          [94ms = [94m_29
          continue 
      return stor[[94midx]
  mem[0] = nodeRightChild[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]
  mem[32] = _index + 1
  mem[64] = 480
  mem[288] = stor[_index + 1][stor4[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]]
  mem[320] = nodeValue[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor4', 4))), ('add', 1, ('param', '_index')))]
  mem[352] = nodeParent[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor4', 4))), ('add', 1, ('param', '_index')))]
  mem[384] = nodeLeftChild[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor4', 4))), ('add', 1, ('param', '_index')))]
  mem[416] = nodeRightChild[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'nodeRightChild', 4))), ('add', 1, ('param', '_index')))]
  mem[448] = nodeHeight[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor4', 4))), ('add', 1, ('param', '_index')))]
  [94ms = 288
  while nodeLeftChild[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor4', 4))), ('add', 1, ('param', '_index')))] != 0:
      mem[0] = mem[[94ms + 96]
      mem[32] = _index + 1
      [94m_27 = sha3(mem[0], _index + 1)
      [94m_28 = mem[64]
      mem[64] = mem[64] + 192
      mem[[94m_28] = stor[_index + 1][mem[0]]
      mem[[94m_28 + 32] = nodeValue[[94m_27]
      mem[[94m_28 + 64] = nodeParent[[94m_27]
      mem[[94m_28 + 96] = nodeLeftChild[[94m_27]
      mem[[94m_28 + 128] = nodeRightChild[[94m_27]
      mem[[94m_28 + 160] = nodeHeight[[94m_27]
      [94ms = [94m_28
      continue 
  mem[mem[64]] = mem[[94ms]
  return memory
    from mem[64]
     [93mlen 32


# hash = 0xcaa46c9c
# getter = None
# const = None
# payable = True
def getPreviousNode(GroveLib.Index storage _index, bytes32 _nodeId) payable: 
  mem[96] = 0
  mem[128] = 0
  mem[160] = 0
  mem[192] = 0
  mem[224] = 0
  mem[256] = 0
  if 0 == stor[_index + 1][_nodeId]:
      return 0
  if 0 == nodeLeftChild[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]:
      if 0 == nodeParent[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]:
          return 0
      mem[64] = 480
      [94midx = 0
      [94ms = 288
      while stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 4] != stor[_index + 1][_nodeId]:
          if 0 == stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2]:
              return 0
          [94m_31 = mem[64]
          mem[64] = mem[64] + 192
          mem[[94m_31] = stor[_index + 1][stor2[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]][[94midx]
          mem[[94m_31 + 32] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 1]
          mem[[94m_31 + 64] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2]
          mem[[94m_31 + 96] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 3]
          mem[[94m_31 + 128] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 4]
          mem[[94m_31 + 160] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 5]
          mem[0] = stor[[94midx + ('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor2', 2))), ('add', 1, ('param', '_index'))) + 2]
          mem[32] = _index + 1
          [94midx = sha3(nodeParent[[94midx], _index + 1)
          [94ms = [94m_31
          continue 
      return stor[[94midx]
  mem[0] = nodeLeftChild[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]
  mem[32] = _index + 1
  mem[64] = 480
  mem[288] = stor[_index + 1][stor3[('map', ('param', '_nodeId'), ('add', 1, ('param', '_index')))]]
  mem[320] = nodeValue[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor3', 3))), ('add', 1, ('param', '_index')))]
  mem[352] = nodeParent[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor3', 3))), ('add', 1, ('param', '_index')))]
  mem[384] = nodeLeftChild[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'nodeLeftChild', 3))), ('add', 1, ('param', '_index')))]
  mem[416] = nodeRightChild[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor3', 3))), ('add', 1, ('param', '_index')))]
  mem[448] = nodeHeight[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor3', 3))), ('add', 1, ('param', '_index')))]
  [94ms = 288
  while nodeRightChild[('map', ('stor', ('array', ('map', ('param', '_nodeId'), ('add', 1, ('param', '_index'))), ('name', 'stor3', 3))), ('add', 1, ('param', '_index')))] != 0:
      mem[0] = mem[[94ms + 128]
      mem[32] = _index + 1
      [94m_29 = sha3(mem[0], _index + 1)
      [94m_30 = mem[64]
      mem[64] = mem[64] + 192
      mem[[94m_30] = stor[_index + 1][mem[0]]
      mem[[94m_30 + 32] = nodeValue[[94m_29]
      mem[[94m_30 + 64] = nodeParent[[94m_29]
      mem[[94m_30 + 96] = nodeLeftChild[[94m_29]
      mem[[94m_30 + 128] = nodeRightChild[[94m_29]
      mem[[94m_30 + 160] = nodeHeight[[94m_29]
      [94ms = [94m_30
      continue 
  mem[mem[64]] = mem[[94ms]
  return memory
    from mem[64]
     [93mlen 32


# hash = 0xed5bd7ea
# getter = None
# const = None
# payable = True
def exists(GroveLib.Index storage _index, bytes32 _id) payable: 
  return (_id == stor[_index + 1][_id])


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


