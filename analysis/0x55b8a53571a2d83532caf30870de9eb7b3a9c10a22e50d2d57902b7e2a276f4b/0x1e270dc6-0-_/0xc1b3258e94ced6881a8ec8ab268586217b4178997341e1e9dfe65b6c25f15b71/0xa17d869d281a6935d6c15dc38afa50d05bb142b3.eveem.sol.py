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
  return munknown0d77a3c5


# hash = 0x0f055139
# getter = ['bool', ['storage', 8, 0, 10]]
# const = None
# payable = False
def unknown0f055139(): # not payable
  return bool(munknown0f055139)


# hash = 0x12d15611
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknown12d15611(): # not payable
  return munknown12d15611


# hash = 0x27a099d8
# getter = None
# const = None
# payable = False
def getOperators(): # not payable
  if not moperatorsm.length:
      mem[(32 * moperatorsm.length) + 128] = 32
      mem[(32 * moperatorsm.length) + 160] = moperatorsm.length
      mem[(32 * moperatorsm.length) + 192 len floor32(moperatorsm.length)] = mem[128 len floor32(moperatorsm.length)]
      return memory
        from (32 * moperatorsm.length) + 128
         [93mlen (96 * moperatorsm.length) + 64
  mem[128] = addr(moperatorsm.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * moperatorsm.length) + 96 > [94midxm:
      mem[[94midx + 32] = addr(moperatorsm[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * moperatorsm.length) + 192 len floor32(moperatorsm.length)] = mem[128 len floor32(moperatorsm.length)]
  return Array(len=moperatorsm.length, data=mem[128 len floor32(moperatorsm.length)], mem[(32 * moperatorsm.length) + floor32(moperatorsm.length) + 192 len (32 * moperatorsm.length) - floor32(moperatorsm.length)]), 


# hash = 0x2a1e747e
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 12]]]]
# const = None
# payable = False
def unknown2a1e747e(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return bool(mstor12m[m_param1m])


# hash = 0x2a3ec233
# getter = None
# const = None
# payable = False
def unknown2a3ec233(bool m_param1): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  munknown0f055139 = uint8(m_param1)
  log 0x77db83c1: not _param1


# hash = 0x2e1d3f02
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def unknown2e1d3f02(): # not payable
  return munknown2e1d3f02


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
  return munknown354a476a


# hash = 0x3a61c4bf
# getter = ['storage', 256, 0, 3]
# const = None
# payable = False
def unknown3a61c4bf(): # not payable
  return munknown3a61c4bf


# hash = 0x4eb8ffb4
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def ORACLIZE_GAS_LIMIT(): # not payable
  return mORACLIZE_GAS_LIMIT


# hash = 0x54bedb4a
# getter = None
# const = None
# payable = False
def unknown54bedb4a(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  mMAX_GAS_PRICE = 10^9 * m_param1
  log 0x46a9321b: (10^9 * _param1)


# hash = 0x6cd0f102
# getter = None
# const = None
# payable = False
def setHouseEdge(uint256 m_value): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  require m_value < 100000
  mHOUSE_EDGE = m_value
  log 0x88a54f8c: _value


# hash = 0x6e25128e
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def unknown6e25128e(): # not payable
  return munknown6e25128e


# hash = 0x7826dc4c
# getter = None
# const = None
# payable = False
def unknown7826dc4c(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  require m_param1 >= 2
  munknown12d15611 = m_param1


# hash = 0x7f5354db
# getter = None
# const = ['return', 1000000000]
# payable = False
const unknown7f5354db = 10^9


# hash = 0x89355eb6
# getter = None
# const = None
# payable = False
def unknown89355eb6(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  munknown354a476a = m_param1
  log 0x9cf3e206: _param1


# hash = 0x8b5f240e
# getter = None
# const = None
# payable = False
def unknown8b5f240e(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  munknown2e1d3f02 = m_param1
  log 0xb2e21dab: _param1


# hash = 0x8daaaa2f
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def HOUSE_EDGE(): # not payable
  return mHOUSE_EDGE


# hash = 0x8ddf792b
# getter = None
# const = None
# payable = False
def setOraclizeGasLimit(uint256 m_value): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  mORACLIZE_GAS_LIMIT = m_value


# hash = 0x91417df8
# getter = None
# const = None
# payable = False
def unknown91417df8(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  munknown6e25128e = 10^9 * m_param1
  log 0xe5c4ba28: (10^9 * _param1)


# hash = 0x9870d7fe
# getter = None
# const = None
# payable = False
def addOperator(address m_operator): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  require not mstor12m[addr(m_operator)m]
  moperatorsm.length++
  addr(moperatorsm[moperatorsm.lengthm]m.field_0) = m_operator
  mstor12m[addr(m_operator)m] = 1


# hash = 0xa9f38bb0
# getter = None
# const = None
# payable = False
def unknowna9f38bb0(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  munknown3a61c4bf = m_param1
  log 0xcab52564: _param1


# hash = 0xac8a584a
# getter = None
# const = None
# payable = False
def removeOperator(address m_operator): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  require mstor12m[addr(m_operator)m]
  [94midx = 0
  mwhile [94midx < moperatorsm.lengthm:
      mem[0] = 14
      if addr(moperatorsm[[94midxm]m.field_0) != m_operator:
          [94midx = [94midx + 1
          mcontinue 
      require moperatorsm.length - 1 < moperatorsm.length
      require [94midx < moperatorsm.length
      addr(moperatorsm[[94midxm]m.field_0) = addr(moperatorsm[moperatorsm.lengthm]m.field_0)
      require moperatorsm.length - 1 < moperatorsm.length
      addr(moperatorsm[moperatorsm.lengthm]m.field_0) = 0
      moperatorsm.length--
      if moperatorsm.length > moperatorsm.length - 1:
          [94midx = moperatorsm.length + sha3(14) - 1
          mwhile sha3(14) + moperatorsm.length > [94midxm:
              mstor[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      mstor12m[addr(m_operator)m] = 0
      stop


# hash = 0xad58fb4e
# getter = None
# const = None
# payable = False
def unknownad58fb4e(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  munknownfcddaa0c = m_param1
  log 0x1fa8d35a: _param1


# hash = 0xbce24669
# getter = None
# const = None
# payable = False
def removeGame(address m_contractAddress): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  require mstor11m[addr(m_contractAddress)m]
  [94midx = 0
  mwhile [94midx < munknowndedfb13bm.lengthm:
      mem[0] = 13
      if addr(munknowndedfb13bm[[94midxm]m.field_0) != m_contractAddress:
          [94midx = [94midx + 1
          mcontinue 
      require munknowndedfb13bm.length - 1 < munknowndedfb13bm.length
      require [94midx < munknowndedfb13bm.length
      addr(munknowndedfb13bm[[94midxm]m.field_0) = addr(munknowndedfb13bm[munknowndedfb13bm.lengthm]m.field_0)
      require munknowndedfb13bm.length - 1 < munknowndedfb13bm.length
      addr(munknowndedfb13bm[munknowndedfb13bm.lengthm]m.field_0) = 0
      munknowndedfb13bm.length--
      if munknowndedfb13bm.length > munknowndedfb13bm.length - 1:
          [94midx = munknowndedfb13bm.length + sha3(13) - 1
          mwhile sha3(13) + munknowndedfb13bm.length > [94midxm:
              mstor[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      mstor11m[addr(m_contractAddress)m] = 0
      stop


# hash = 0xc04c5947
# getter = None
# const = None
# payable = False
def getGames(): # not payable
  if munknowndedfb13bm.length:
      mem[128] = addr(munknowndedfb13bm.field_0)
      if (32 * munknowndedfb13bm.length) + 32 > 64:
          mem[160] = addr(munknowndedfb13bm.field_256)
          [94midx = 160
          [94ms = 1
          mwhile (32 * munknowndedfb13bm.length) + 96 > [94midxm:
              mem[[94midx + 32] = addr(munknowndedfb13bm[[94msm]m.field_256)
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
  mem[(32 * munknowndedfb13bm.length) + 128] = 32
  mem[(32 * munknowndedfb13bm.length) + 160] = munknowndedfb13bm.length
  mem[(32 * munknowndedfb13bm.length) + 192 len floor32(munknowndedfb13bm.length)] = mem[128 len floor32(munknowndedfb13bm.length)]
  return memory
    from (32 * munknowndedfb13bm.length) + 128
     [93mlen (96 * munknowndedfb13bm.length) + 64


# hash = 0xcf01a601
# getter = None
# const = None
# payable = False
def unknowncf01a601(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  munknown0d77a3c5 = m_param1
  log 0xf6a8ffda: _param1


# hash = 0xd72d04db
# getter = None
# const = None
# payable = False
def addGame(address m_contractAddress): # not payable
  require calldata.size - 4 >= 32
  require mstor12m[callerm]
  require not mstor11m[addr(m_contractAddress)m]
  munknowndedfb13bm.length++
  addr(munknowndedfb13bm[munknowndedfb13bm.lengthm]m.field_0) = m_contractAddress
  mstor11m[addr(m_contractAddress)m] = 1


# hash = 0xdd2f4ebd
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknowndd2f4ebd(): # not payable
  return munknowndedfb13bm.length


# hash = 0xdedfb13b
# getter = ['storage', 160, 0, ['add', ['sha3', 13], ['cd', 4]]]
# const = None
# payable = False
def unknowndedfb13b(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < munknowndedfb13bm.length
  return addr(munknowndedfb13bm[m_param1m]m.field_0)


# hash = 0xe28d4906
# getter = ['storage', 160, 0, ['add', ['sha3', 14], ['cd', 4]]]
# const = None
# payable = False
def operators(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < moperatorsm.length
  return addr(moperatorsm[m_param1m]m.field_0)


# hash = 0xe3bbb4f1
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def MAX_GAS_PRICE(): # not payable
  return mMAX_GAS_PRICE


# hash = 0xeeee2023
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 11]]]]
# const = None
# payable = False
def unknowneeee2023(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return bool(mstor11m[m_param1m])


# hash = 0xfcddaa0c
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def unknownfcddaa0c(): # not payable
  return munknownfcddaa0c


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


