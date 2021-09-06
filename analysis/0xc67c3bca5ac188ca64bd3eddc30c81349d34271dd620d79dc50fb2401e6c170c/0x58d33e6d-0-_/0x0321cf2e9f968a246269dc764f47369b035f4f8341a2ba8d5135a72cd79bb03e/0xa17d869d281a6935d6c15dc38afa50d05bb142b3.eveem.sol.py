# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xa17d869D281A6935D6c15dc38afa50d05bb142b3 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    ORACLIZE_GAS_LIMIT # mask: a s
    # storage address 1
    MAX_GAS_PRICE # mask: a s
    # storage address 2
    unknown6e25128e # mask: a s
    # storage address 3
    unknown3a61c4bf # mask: a s
    # storage address 4
    unknown2e1d3f02 # mask: a s
    # storage address 5
    unknown354a476a # mask: a s
    # storage address 6
    HOUSE_EDGE # mask: a s
    # storage address 7
    unknownfcddaa0c # mask: a s
    # storage address 8
    unknown0d77a3c5 # mask: a s
    # storage address 9
    unknown12d15611 # mask: a s
    # storage address 10
    unknown0f055139 # mask: a s
    # storage address 11
    stor11
    # storage address 12
    stor12
    # storage address 13
    unknowndedfb13b
    # storage address 14
    operators
# hash = 0x0d77a3c5
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def unknown0d77a3c5(): # not payable
  return unknown0d77a3c5


# hash = 0x0f055139
# getter = ['bool', ['storage', 8, 0, 10]]
# const = None
# payable = False
def unknown0f055139(): # not payable
  return bool(unknown0f055139)


# hash = 0x12d15611
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknown12d15611(): # not payable
  return unknown12d15611


# hash = 0x27a099d8
# getter = None
# const = None
# payable = False
def getOperators(): # not payable
  if not operators.length:
      mem[(32 * operators.length) + 128] = 32
      mem[(32 * operators.length) + 160] = operators.length
      mem[(32 * operators.length) + 192 len floor32(operators.length)] = mem[128 len floor32(operators.length)]
      return memory
        from (32 * operators.length) + 128
         [93mlen (96 * operators.length) + 64
  mem[128] = addr(operators.field_0)
  [94midx = 128
  [94ms = 0
  while (32 * operators.length) + 96 > [94midx:
      mem[[94midx + 32] = addr(operators[[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * operators.length) + 192 len floor32(operators.length)] = mem[128 len floor32(operators.length)]
  return Array(len=operators.length, data=mem[128 len floor32(operators.length)], mem[(32 * operators.length) + floor32(operators.length) + 192 len (32 * operators.length) - floor32(operators.length)]), 


# hash = 0x2a1e747e
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 12]]]]
# const = None
# payable = False
def unknown2a1e747e(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return bool(stor12[_param1])


# hash = 0x2a3ec233
# getter = None
# const = None
# payable = False
def unknown2a3ec233(bool _param1): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  unknown0f055139 = uint8(_param1)
  log 0x77db83c1: not _param1


# hash = 0x2e1d3f02
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def unknown2e1d3f02(): # not payable
  return unknown2e1d3f02


# hash = 0x34854101
# getter = None
# const = ['return', 1000000000000000000]
# payable = False
const ETH_TO_WEI = 10^18


# hash = 0x354a476a
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def unknown354a476a(): # not payable
  return unknown354a476a


# hash = 0x3a61c4bf
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknown3a61c4bf(): # not payable
  return unknown3a61c4bf


# hash = 0x4eb8ffb4
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def ORACLIZE_GAS_LIMIT(): # not payable
  return ORACLIZE_GAS_LIMIT


# hash = 0x54bedb4a
# getter = None
# const = None
# payable = False
def unknown54bedb4a(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  MAX_GAS_PRICE = 10^9 * _param1
  log 0x46a9321b: (10^9 * _param1)


# hash = 0x6cd0f102
# getter = None
# const = None
# payable = False
def setHouseEdge(uint256 _value): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  require _value < 100000
  HOUSE_EDGE = _value
  log 0x88a54f8c: _value


# hash = 0x6e25128e
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def unknown6e25128e(): # not payable
  return unknown6e25128e


# hash = 0x7826dc4c
# getter = None
# const = None
# payable = False
def unknown7826dc4c(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  require _param1 >= 2
  unknown12d15611 = _param1


# hash = 0x7f5354db
# getter = None
# const = ['return', 1000000000]
# payable = False
const unknown7f5354db = 10^9


# hash = 0x89355eb6
# getter = None
# const = None
# payable = False
def unknown89355eb6(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  unknown354a476a = _param1
  log 0x9cf3e206: _param1


# hash = 0x8b5f240e
# getter = None
# const = None
# payable = False
def unknown8b5f240e(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  unknown2e1d3f02 = _param1
  log 0xb2e21dab: _param1


# hash = 0x8daaaa2f
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def HOUSE_EDGE(): # not payable
  return HOUSE_EDGE


# hash = 0x8ddf792b
# getter = None
# const = None
# payable = False
def setOraclizeGasLimit(uint256 _value): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  ORACLIZE_GAS_LIMIT = _value


# hash = 0x91417df8
# getter = None
# const = None
# payable = False
def unknown91417df8(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  unknown6e25128e = 10^9 * _param1
  log 0xe5c4ba28: (10^9 * _param1)


# hash = 0x9870d7fe
# getter = None
# const = None
# payable = False
def addOperator(address _operator): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  require not stor12[addr(_operator)]
  operators.length++
  addr(operators[operators.length].field_0) = _operator
  stor12[addr(_operator)] = 1


# hash = 0xa9f38bb0
# getter = None
# const = None
# payable = False
def unknowna9f38bb0(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  unknown3a61c4bf = _param1
  log 0xcab52564: _param1


# hash = 0xac8a584a
# getter = None
# const = None
# payable = False
def removeOperator(address _operator): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  require stor12[addr(_operator)]
  [94midx = 0
  while [94midx < operators.length:
      mem[0] = 14
      if addr(operators[[94midx].field_0) != _operator:
          [94midx = [94midx + 1
          continue 
      require operators.length - 1 < operators.length
      require [94midx < operators.length
      addr(operators[[94midx].field_0) = addr(operators[operators.length].field_0)
      require operators.length - 1 < operators.length
      addr(operators[operators.length].field_0) = 0
      operators.length--
      if operators.length > operators.length - 1:
          [94midx = operators.length + sha3(14) - 1
          while sha3(14) + operators.length > [94midx:
              stor[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      stor12[addr(_operator)] = 0
      stop


# hash = 0xad58fb4e
# getter = None
# const = None
# payable = False
def unknownad58fb4e(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  unknownfcddaa0c = _param1
  log 0x1fa8d35a: _param1


# hash = 0xbce24669
# getter = None
# const = None
# payable = False
def removeGame(address _contractAddress): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  require stor11[addr(_contractAddress)]
  [94midx = 0
  while [94midx < unknowndedfb13b.length:
      mem[0] = 13
      if addr(unknowndedfb13b[[94midx].field_0) != _contractAddress:
          [94midx = [94midx + 1
          continue 
      require unknowndedfb13b.length - 1 < unknowndedfb13b.length
      require [94midx < unknowndedfb13b.length
      addr(unknowndedfb13b[[94midx].field_0) = addr(unknowndedfb13b[unknowndedfb13b.length].field_0)
      require unknowndedfb13b.length - 1 < unknowndedfb13b.length
      addr(unknowndedfb13b[unknowndedfb13b.length].field_0) = 0
      unknowndedfb13b.length--
      if unknowndedfb13b.length > unknowndedfb13b.length - 1:
          [94midx = unknowndedfb13b.length + sha3(13) - 1
          while sha3(13) + unknowndedfb13b.length > [94midx:
              stor[[94midx] = 0
              [94midx = [94midx + 1
              continue 
      stor11[addr(_contractAddress)] = 0
      stop


# hash = 0xc04c5947
# getter = None
# const = None
# payable = False
def getGames(): # not payable
  if unknowndedfb13b.length:
      mem[128] = addr(unknowndedfb13b.field_0)
      if (32 * unknowndedfb13b.length) + 32 > 64:
          mem[160] = addr(unknowndedfb13b.field_256)
          [94midx = 160
          [94ms = 1
          while (32 * unknowndedfb13b.length) + 96 > [94midx:
              mem[[94midx + 32] = addr(unknowndedfb13b[[94ms].field_256)
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              continue 
  mem[(32 * unknowndedfb13b.length) + 128] = 32
  mem[(32 * unknowndedfb13b.length) + 160] = unknowndedfb13b.length
  mem[(32 * unknowndedfb13b.length) + 192 len floor32(unknowndedfb13b.length)] = mem[128 len floor32(unknowndedfb13b.length)]
  return memory
    from (32 * unknowndedfb13b.length) + 128
     [93mlen (96 * unknowndedfb13b.length) + 64


# hash = 0xcf01a601
# getter = None
# const = None
# payable = False
def unknowncf01a601(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  unknown0d77a3c5 = _param1
  log 0xf6a8ffda: _param1


# hash = 0xd72d04db
# getter = None
# const = None
# payable = False
def addGame(address _contractAddress): # not payable
  require calldata.size - 4 >= 32
  require stor12[caller]
  require not stor11[addr(_contractAddress)]
  unknowndedfb13b.length++
  addr(unknowndedfb13b[unknowndedfb13b.length].field_0) = _contractAddress
  stor11[addr(_contractAddress)] = 1


# hash = 0xdd2f4ebd
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknowndd2f4ebd(): # not payable
  return unknowndedfb13b.length


# hash = 0xdedfb13b
# getter = ['storage', 160, 0, ['add', ['sha3', 13], ['cd', 4]]]
# const = None
# payable = False
def unknowndedfb13b(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < unknowndedfb13b.length
  return addr(unknowndedfb13b[_param1].field_0)


# hash = 0xe28d4906
# getter = ['storage', 160, 0, ['add', ['sha3', 14], ['cd', 4]]]
# const = None
# payable = False
def operators(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < operators.length
  return addr(operators[_param1].field_0)


# hash = 0xe3bbb4f1
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def MAX_GAS_PRICE(): # not payable
  return MAX_GAS_PRICE


# hash = 0xeeee2023
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 11]]]]
# const = None
# payable = False
def unknowneeee2023(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return bool(stor11[_param1])


# hash = 0xfcddaa0c
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def unknownfcddaa0c(): # not payable
  return unknownfcddaa0c


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


