# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xD176ff3D44fDAe552bDC5b566fa1F0066E81fe0b 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x22d40045': 'unknown22d40045(?)', '0x2b23c8a0': 'unknown2b23c8a0(?)', '0x2e1ed949': 'unknown2e1ed949(?)', '0x3eadb6db': 'unknown3eadb6db(?)', '0x4b25fe92': 'unknown4b25fe92(?)', '0x7113aef2': 'unknown7113aef2(?)', '0x967e26ca': 'unknown967e26ca(?)'} 

# storage definitions
def storage:
    # storage address 18
    unknownbdbcb576
    # storage address 53
    stor53 # mask: a s
    # storage address 29
    unknown623e3d1a
    # storage address 28
    stor28
    # storage address 20
    investmentsCount
    # storage address 13
    unknownae2f89c2 # mask: a s
    # storage address 59
    stor59 # mask: a s
    # storage address 4
    unknowna03040c3Address # mask: a s
    # storage address 21
    unknown404c568f
    # storage address 27
    stor27
    # storage address 43
    stor43
    # storage address 52
    stor52
    # storage address 23
    unknowna940646d
    # storage address 38
    stor38
    # storage address 24
    unknownfa845ca9
    # storage address 6
    unknown2914af34Address # mask: a s
    # storage address 39
    unknowne96e22b9
    # storage address 33
    stor33
    # storage address 51
    unknown92bba1fc
    # storage address 25
    stor25
    # storage address 57
    unknowncb0ef21dAddress # mask: a s
    # storage address 14
    unknown56f7e7ff
    # storage address 8
    unknowndb3d1ccfAddress # mask: a s
    # storage address 10
    unknown0cba5355 # mask: a s
    # storage address 19
    unknown5825b04c
    # storage address 56
    unknownd95393ebAddress # mask: a s
    # storage address 2
    unknowndc87454cAddress # mask: a s
    # storage address 2
    unknownb7ac4ff3 # mask: a s
    # storage address 7
    unknownfbf35f46Address # mask: a s
    # storage address 34
    candidates
    # storage address 49
    unknown627d50df # mask: a s
    # storage address 12
    unknown13d3d00e # mask: a s
    # storage address 9
    unknown2f884710 # mask: a s
    # storage address 58
    stor58 # mask: a s
    # storage address 3
    unknownd7615d37Address # mask: a s
    # storage address 0
    owner # mask: a s
    # storage address 22
    unknown7cd9fb1c
    # storage address 50
    stor50
    # storage address 17
    stor17
    # storage address 11
    unknown25f842c5 # mask: a s
    # storage address 5
    unknown9a8a2145Address # mask: a s
    # storage address 26
    stor26
    # storage address 16
    unknown821f9824
    # storage address 44
    unknown5ebad714
# hash = 0x0bafd60e
# getter = ['storage', 160, 24, 28]
# const = None
# payable = False
def nextVersion(): # not payable
  return mstor28m.lengthm.field_24


# hash = 0x0c06b1e1
# getter = None
# const = None
# payable = False
def unknown0c06b1e1(uint256 m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param1 < uint256(munknown404c568fm[callerm])
  require addr(munknown404c568fm[callerm]m[m_param1m])
  require m_param1 < uint256(munknown404c568fm[callerm])
  require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
  static call addr(munknown404c568fm[callerm]m[m_param1m]).0xe852e741 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
  static call addr(munknown404c568fm[callerm]m[m_param1m]).0x2f884710 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] == munknown2f884710
  require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
  call addr(munknown404c568fm[callerm]m[m_param1m]).0xab7b1c89 with:
       gas gas_remaining wei
      args m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0xeb8df86c: uint256(unknown404c568f[caller]) - 1, addr(unknown404c568f[caller][_param1]), _param2, unknown2f884710, caller


# hash = 0x0c99c9ea
# getter = None
# const = None
# payable = False
def unknown0c99c9ea(bool m_param1): # not payable
  require calldata.size - 4 >= 32
  if 3 >= munknown2f884710:
      return 0
  if mstor52m[mstor9m]m[callerm]:
      if m_param1:
          return 0
      mstor52m[mstor9m]m[callerm] = 0
      if munknown2f884710 <= 3:
          if 0 > munknown92bba1fcm[mstor9m]:
              revert with 0, 'SafeMath: subtraction overflow'
      else:
          if not caller:
              if 0 > munknown92bba1fcm[mstor9m]:
                  revert with 0, 'SafeMath: subtraction overflow'
          else:
              if 3 > munknown2f884710:
                  revert with 0, 'SafeMath: subtraction overflow'
              require ext_code.size(mstor53)
              static call mstor53.balanceOfAt(address owner, uint256 blockNumber) with:
                      gas gas_remaining wei
                     args caller, munknowna940646dm[mstor9 - 3m]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] > munknown92bba1fcm[mstor9m]:
                  revert with 0, 'SafeMath: subtraction overflow'
              munknown92bba1fcm[mstor9m] -= ext_call.return_data[0]
  else:
      if m_param1 != 1:
          return 0
      mstor52m[mstor9m]m[callerm] = 1
      if munknown2f884710 <= 3:
          if munknown92bba1fcm[mstor9m] < munknown92bba1fcm[mstor9m]:
              revert with 0, 'SafeMath: addition overflow'
      else:
          if not caller:
              if munknown92bba1fcm[mstor9m] < munknown92bba1fcm[mstor9m]:
                  revert with 0, 'SafeMath: addition overflow'
          else:
              if 3 > munknown2f884710:
                  revert with 0, 'SafeMath: subtraction overflow'
              require ext_code.size(mstor53)
              static call mstor53.balanceOfAt(address owner, uint256 blockNumber) with:
                      gas gas_remaining wei
                     args caller, munknowna940646dm[mstor9 - 3m]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] + munknown92bba1fcm[mstor9m] < munknown92bba1fcm[mstor9m]:
                  revert with 0, 'SafeMath: addition overflow'
              munknown92bba1fcm[mstor9m] += ext_call.return_data[0]
  log 0x257d79cd: unknown2f884710, caller, _param1
  return 1


# hash = 0x0cba5355
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknown0cba5355(): # not payable
  return munknown0cba5355


# hash = 0x0e187cac
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 25]]]]
# const = None
# payable = False
def isKyberToken(address m_tokenContract): # not payable
  require calldata.size - 4 >= 32
  return bool(mstor25m[m_tokenContractm])


# hash = 0x13d3d00e
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknown13d3d00e(): # not payable
  return munknown13d3d00e


# hash = 0x1a454ea6
# getter = None
# const = ['return', 200000000000000000]
# payable = False
const COMMISSION_RATE = 2 * 10^17


# hash = 0x1f5c6a51
# getter = None
# const = None
# payable = False
def unknown1f5c6a51(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  require calldata.size - 4 >= 96
  require m_param1 < uint256(munknown404c568fm[callerm])
  require addr(munknown404c568fm[callerm]m[m_param1m])
  require m_param1 < uint256(munknown404c568fm[callerm])
  require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
  static call addr(munknown404c568fm[callerm]m[m_param1m]).0xe852e741 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
  static call addr(munknown404c568fm[callerm]m[m_param1m]).0x2f884710 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] == munknown2f884710
  require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
  call addr(munknown404c568fm[callerm]m[m_param1m]).sellOrder(uint256 sellPrice, uint256 amount) with:
       gas gas_remaining wei
      args m_param2, m_param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
  static call addr(munknown404c568fm[callerm]m[m_param1m]).stake() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
  static call addr(munknown404c568fm[callerm]m[m_param1m]).stake() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      if ext_call.return_data[0] <= 0:
          revert with 0, 'SafeMath: division by zero'
      require ext_call.return_data[0]
      require ext_code.size(mstor53)
      call mstor53.destroyTokens(address owner, uint256 amount) with:
           gas gas_remaining wei
          args this.address, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(mstor53)
      call mstor53.generateTokens(address holder, uint256 amount) with:
           gas gas_remaining wei
          args caller, 0 / ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
      static call addr(munknown404c568fm[callerm]m[m_param1m]).0x3eeb4ca with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] > block.timestamp:
          revert with 0, 'SafeMath: subtraction overflow'
      if not ext_call.return_data[0]:
          if munknownbdbcb576m[callerm]m[mstor9m] < munknownbdbcb576m[callerm]m[mstor9m]:
              revert with 0, 'SafeMath: addition overflow'
      else:
          if (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) / ext_call.return_data[0] != block.timestamp - ext_call.return_data[0]:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) + munknownbdbcb576m[callerm]m[mstor9m] < munknownbdbcb576m[callerm]m[mstor9m]:
              revert with 0, 'SafeMath: addition overflow'
          munknownbdbcb576m[callerm]m[mstor9m] = (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) + munknownbdbcb576m[callerm]m[mstor9m]
      if ext_call.return_data[0] > munknown0cba5355:
          revert with 0, 'SafeMath: subtraction overflow'
      if ext_call.return_data[32] < 0:
          revert with 0, 'SafeMath: addition overflow'
      munknown0cba5355 = ext_call.return_data[32] + munknown0cba5355 - ext_call.return_data[0]
      require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
      static call addr(munknown404c568fm[callerm]m[m_param1m]).0x6f17591f with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
      static call addr(munknown404c568fm[callerm]m[m_param1m]).0x76017b64 with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      log 0x1b6d154f: uint256(unknown404c568f[caller]) - 1, ext_call.return_data[32], bool(ext_call.return_data[0]), addr(ext_call.return_data[0]), 0 / ext_call.return_data[0], ext_call.return_data[32], unknown2f884710, caller
  else:
      if ext_call.return_data[32] * ext_call.return_data[0] / ext_call.return_data[0] != ext_call.return_data[32]:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      33,
                      0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                      mem[197 len 31]
      if ext_call.return_data[0] <= 0:
          revert with 0, 'SafeMath: division by zero'
      require ext_call.return_data[0]
      require ext_code.size(mstor53)
      call mstor53.destroyTokens(address owner, uint256 amount) with:
           gas gas_remaining wei
          args this.address, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(mstor53)
      call mstor53.generateTokens(address holder, uint256 amount) with:
           gas gas_remaining wei
          args caller, ext_call.return_data[32] * ext_call.return_data[0] / ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
      static call addr(munknown404c568fm[callerm]m[m_param1m]).0x3eeb4ca with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] > block.timestamp:
          revert with 0, 'SafeMath: subtraction overflow'
      if not ext_call.return_data[0]:
          if munknownbdbcb576m[callerm]m[mstor9m] < munknownbdbcb576m[callerm]m[mstor9m]:
              revert with 0, 'SafeMath: addition overflow'
      else:
          if (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) / ext_call.return_data[0] != block.timestamp - ext_call.return_data[0]:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) + munknownbdbcb576m[callerm]m[mstor9m] < munknownbdbcb576m[callerm]m[mstor9m]:
              revert with 0, 'SafeMath: addition overflow'
          munknownbdbcb576m[callerm]m[mstor9m] = (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) + munknownbdbcb576m[callerm]m[mstor9m]
      if ext_call.return_data[0] > munknown0cba5355:
          revert with 0, 'SafeMath: subtraction overflow'
      if ext_call.return_data[32] < 0:
          revert with 0, 'SafeMath: addition overflow'
      munknown0cba5355 = ext_call.return_data[32] + munknown0cba5355 - ext_call.return_data[0]
      require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
      static call addr(munknown404c568fm[callerm]m[m_param1m]).0x6f17591f with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(munknown404c568fm[callerm]m[m_param1m]))
      static call addr(munknown404c568fm[callerm]m[m_param1m]).0x76017b64 with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      log 0x1b6d154f: uint256(unknown404c568f[caller]) - 1, ext_call.return_data[32], bool(ext_call.return_data[0]), addr(ext_call.return_data[0]), ext_call.return_data[32] * ext_call.return_data[0] / ext_call.return_data[0], ext_call.return_data[32], unknown2f884710, caller


# hash = 0x25f842c5
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def unknown25f842c5(): # not payable
  return munknown25f842c5


# hash = 0x2893f5cc
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 26]]]]
# const = None
# payable = False
def unknown2893f5cc(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return bool(mstor26m[m_param1m])


# hash = 0x28ad7cef
# getter = None
# const = None
# payable = False
def unknown28ad7cef(): # not payable
  if munknown2f884710 <= 3:
      return 0
  if 3 > munknown2f884710:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(mstor53)
  static call mstor53.totalSupplyAt(uint256 blockNumber) with:
          gas gas_remaining wei
         args munknowna940646dm[mstor9 - 3m]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if munknown627d50df > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  return (ext_call.return_data[0] - munknown627d50df)


# hash = 0x2914af34
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def unknown2914af34(): # not payable
  return munknown2914af34Address


# hash = 0x2df182c9
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 52]]]]]]
# const = None
# payable = False
def unknown2df182c9(uint256 m_param1, addr m_param2): # not payable
  require calldata.size - 4 >= 64
  return bool(mstor52m[m_param1m]m[m_param2m])


# hash = 0x2e80d9b6
# getter = None
# const = ['return', 100000000000000000]
# payable = False
const QUORUM = 10^17


# hash = 0x2f884710
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def unknown2f884710(): # not payable
  return munknown2f884710


# hash = 0x2f9fb6a4
# getter = None
# const = ['return', 10000000000000000]
# payable = False
const unknown2f9fb6a4 = 10^16


# hash = 0x3477ee2e
# getter = ['storage', 160, 0, ['add', 34, ['cd', 4]]]
# const = None
# payable = False
def candidates(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < 5
  return mcandidatesm[m_param1m]


# hash = 0x381f253c
# getter = None
# const = None
# payable = False
def unknown381f253c(uint256 m_param1, bool m_param2): # not payable
  require calldata.size - 4 >= 64
  if m_param1 < 1:
      return 0
  if 5 < m_param1:
      return 0
  require uint8(mstor28m.length) <= 1
  if uint8(mstor28m.length) == 1:
      if block.timestamp - munknown25f842c5 / 72 * 24 * 3600 != m_param1:
          return 0
  else:
      if m_param1 != 0:
          return 0
  require uint8(mstor28m.length) <= 1
  if uint8(mstor28m.length) == 1:
      if block.timestamp - munknown25f842c5 % 72 * 24 * 3600 < 24 * 3600:
          return 0
  if not mstor28m.lengthm.field_16:
      return 0
  if 3 >= munknown2f884710:
      return 0
  if 1 > m_param1:
      revert with 0, 'SafeMath: subtraction overflow'
  [94midx = 0
  mwhile [94midx < m_param1 - 1m:
      require [94midx < 5
      if munknown623e3d1am[[94midxm] == caller:
          return 0
      if [94midx + 1 < [94midx:
          revert with 0, 'SafeMath: addition overflow'
      [94midx = [94midx + 1
      mcontinue 
  require m_param1 - 1 < 5
  if munknown2f884710 <= 3:
      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
      if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
          if m_param2:
              require m_param1 - 1 < 5
              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = 256^(m_param1 - 1 % 32) or !(255 * 256^(m_param1 - 1 % 32)) and mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0
              require m_param1 - 1 < 5
              if mstor38m[m_param1m] < mstor38m[m_param1m]:
                  revert with 0, 'SafeMath: addition overflow'
              require m_param1 - 1 < 5
              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
              if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 2:
                  require m_param1 - 1 < 5
                  if 0 > mstor43m[m_param1m]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require m_param1 - 1 < 5
          else:
              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
              if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
                  if not m_param2:
                      require m_param1 - 1 < 5
                      mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                      mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                      require m_param1 - 1 < 5
                      if mstor43m[m_param1m] < mstor43m[m_param1m]:
                          revert with 0, 'SafeMath: addition overflow'
                      require m_param1 - 1 < 5
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                          require m_param1 - 1 < 5
                          if 0 > mstor38m[m_param1m]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          require m_param1 - 1 < 5
              else:
                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                  if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                      if not m_param2:
                          require m_param1 - 1 < 5
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                          require m_param1 - 1 < 5
                          if mstor43m[m_param1m] < mstor43m[m_param1m]:
                              revert with 0, 'SafeMath: addition overflow'
                          require m_param1 - 1 < 5
                          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                          if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                              require m_param1 - 1 < 5
                              if 0 > mstor38m[m_param1m]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require m_param1 - 1 < 5
      else:
          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
          if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] != 2:
              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
              if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
                  if not m_param2:
                      require m_param1 - 1 < 5
                      mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                      mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                      require m_param1 - 1 < 5
                      if mstor43m[m_param1m] < mstor43m[m_param1m]:
                          revert with 0, 'SafeMath: addition overflow'
                      require m_param1 - 1 < 5
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                          require m_param1 - 1 < 5
                          if 0 > mstor38m[m_param1m]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          require m_param1 - 1 < 5
              else:
                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                  if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                      if not m_param2:
                          require m_param1 - 1 < 5
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                          require m_param1 - 1 < 5
                          if mstor43m[m_param1m] < mstor43m[m_param1m]:
                              revert with 0, 'SafeMath: addition overflow'
                          require m_param1 - 1 < 5
                          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                          if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                              require m_param1 - 1 < 5
                              if 0 > mstor38m[m_param1m]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require m_param1 - 1 < 5
          else:
              if m_param2:
                  require m_param1 - 1 < 5
                  mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = 256^(m_param1 - 1 % 32) or !(255 * 256^(m_param1 - 1 % 32)) and mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0
                  require m_param1 - 1 < 5
                  if mstor38m[m_param1m] < mstor38m[m_param1m]:
                      revert with 0, 'SafeMath: addition overflow'
                  require m_param1 - 1 < 5
                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                  if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 2:
                      require m_param1 - 1 < 5
                      if 0 > mstor43m[m_param1m]:
                          revert with 0, 'SafeMath: subtraction overflow'
                      require m_param1 - 1 < 5
              else:
                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                  if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
                      if not m_param2:
                          require m_param1 - 1 < 5
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                          require m_param1 - 1 < 5
                          if mstor43m[m_param1m] < mstor43m[m_param1m]:
                              revert with 0, 'SafeMath: addition overflow'
                          require m_param1 - 1 < 5
                          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                          if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                              require m_param1 - 1 < 5
                              if 0 > mstor38m[m_param1m]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require m_param1 - 1 < 5
                  else:
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                          if not m_param2:
                              require m_param1 - 1 < 5
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                              require m_param1 - 1 < 5
                              if mstor43m[m_param1m] < mstor43m[m_param1m]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require m_param1 - 1 < 5
                              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                              if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                                  require m_param1 - 1 < 5
                                  if 0 > mstor38m[m_param1m]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require m_param1 - 1 < 5
      log 0xcba8212a: _param2, 0, unknown2f884710, _param1 - 1, caller
  else:
      if not caller:
          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
          if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
              if m_param2:
                  require m_param1 - 1 < 5
                  mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = 256^(m_param1 - 1 % 32) or !(255 * 256^(m_param1 - 1 % 32)) and mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0
                  require m_param1 - 1 < 5
                  if mstor38m[m_param1m] < mstor38m[m_param1m]:
                      revert with 0, 'SafeMath: addition overflow'
                  require m_param1 - 1 < 5
                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                  if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 2:
                      require m_param1 - 1 < 5
                      if 0 > mstor43m[m_param1m]:
                          revert with 0, 'SafeMath: subtraction overflow'
                      require m_param1 - 1 < 5
              else:
                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                  if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
                      if not m_param2:
                          require m_param1 - 1 < 5
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                          require m_param1 - 1 < 5
                          if mstor43m[m_param1m] < mstor43m[m_param1m]:
                              revert with 0, 'SafeMath: addition overflow'
                          require m_param1 - 1 < 5
                          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                          if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                              require m_param1 - 1 < 5
                              if 0 > mstor38m[m_param1m]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require m_param1 - 1 < 5
                  else:
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                          if not m_param2:
                              require m_param1 - 1 < 5
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                              require m_param1 - 1 < 5
                              if mstor43m[m_param1m] < mstor43m[m_param1m]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require m_param1 - 1 < 5
                              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                              if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                                  require m_param1 - 1 < 5
                                  if 0 > mstor38m[m_param1m]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require m_param1 - 1 < 5
          else:
              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
              if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] != 2:
                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                  if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
                      if not m_param2:
                          require m_param1 - 1 < 5
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                          require m_param1 - 1 < 5
                          if mstor43m[m_param1m] < mstor43m[m_param1m]:
                              revert with 0, 'SafeMath: addition overflow'
                          require m_param1 - 1 < 5
                          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                          if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                              require m_param1 - 1 < 5
                              if 0 > mstor38m[m_param1m]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require m_param1 - 1 < 5
                  else:
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                          if not m_param2:
                              require m_param1 - 1 < 5
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                              require m_param1 - 1 < 5
                              if mstor43m[m_param1m] < mstor43m[m_param1m]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require m_param1 - 1 < 5
                              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                              if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                                  require m_param1 - 1 < 5
                                  if 0 > mstor38m[m_param1m]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require m_param1 - 1 < 5
              else:
                  if m_param2:
                      require m_param1 - 1 < 5
                      mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = 256^(m_param1 - 1 % 32) or !(255 * 256^(m_param1 - 1 % 32)) and mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0
                      require m_param1 - 1 < 5
                      if mstor38m[m_param1m] < mstor38m[m_param1m]:
                          revert with 0, 'SafeMath: addition overflow'
                      require m_param1 - 1 < 5
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 2:
                          require m_param1 - 1 < 5
                          if 0 > mstor43m[m_param1m]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          require m_param1 - 1 < 5
                  else:
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
                          if not m_param2:
                              require m_param1 - 1 < 5
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                              require m_param1 - 1 < 5
                              if mstor43m[m_param1m] < mstor43m[m_param1m]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require m_param1 - 1 < 5
                              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                              if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                                  require m_param1 - 1 < 5
                                  if 0 > mstor38m[m_param1m]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require m_param1 - 1 < 5
                      else:
                          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                          if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                              if not m_param2:
                                  require m_param1 - 1 < 5
                                  mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                                  mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                                  require m_param1 - 1 < 5
                                  if mstor43m[m_param1m] < mstor43m[m_param1m]:
                                      revert with 0, 'SafeMath: addition overflow'
                                  require m_param1 - 1 < 5
                                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                                  if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                                      require m_param1 - 1 < 5
                                      if 0 > mstor38m[m_param1m]:
                                          revert with 0, 'SafeMath: subtraction overflow'
                                      require m_param1 - 1 < 5
          log 0xcba8212a: _param2, 0, unknown2f884710, _param1 - 1, caller
      else:
          if 3 > munknown2f884710:
              revert with 0, 'SafeMath: subtraction overflow'
          require ext_code.size(mstor53)
          static call mstor53.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args caller, munknowna940646dm[mstor9 - 3m]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
          if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
              if m_param2:
                  require m_param1 - 1 < 5
                  mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = 256^(m_param1 - 1 % 32) or !(255 * 256^(m_param1 - 1 % 32)) and mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0
                  require m_param1 - 1 < 5
                  if ext_call.return_data[0] + mstor38m[m_param1m] < mstor38m[m_param1m]:
                      revert with 0, 'SafeMath: addition overflow'
                  require m_param1 - 1 < 5
                  mstor38m[m_param1m] += ext_call.return_data[0]
                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                  if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 2:
                      require m_param1 - 1 < 5
                      if ext_call.return_data[0] > mstor43m[m_param1m]:
                          revert with 0, 'SafeMath: subtraction overflow'
                      require m_param1 - 1 < 5
                      mstor43m[m_param1m] -= ext_call.return_data[0]
              else:
                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                  if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
                      if not m_param2:
                          require m_param1 - 1 < 5
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                          require m_param1 - 1 < 5
                          if ext_call.return_data[0] + mstor43m[m_param1m] < mstor43m[m_param1m]:
                              revert with 0, 'SafeMath: addition overflow'
                          require m_param1 - 1 < 5
                          mstor43m[m_param1m] += ext_call.return_data[0]
                          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                          if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                              require m_param1 - 1 < 5
                              if ext_call.return_data[0] > mstor38m[m_param1m]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require m_param1 - 1 < 5
                              mstor38m[m_param1m] -= ext_call.return_data[0]
                  else:
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                          if not m_param2:
                              require m_param1 - 1 < 5
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                              require m_param1 - 1 < 5
                              if ext_call.return_data[0] + mstor43m[m_param1m] < mstor43m[m_param1m]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require m_param1 - 1 < 5
                              mstor43m[m_param1m] += ext_call.return_data[0]
                              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                              if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                                  require m_param1 - 1 < 5
                                  if ext_call.return_data[0] > mstor38m[m_param1m]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require m_param1 - 1 < 5
                                  mstor38m[m_param1m] -= ext_call.return_data[0]
          else:
              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
              if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] != 2:
                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                  if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
                      if not m_param2:
                          require m_param1 - 1 < 5
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                          mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                          require m_param1 - 1 < 5
                          if ext_call.return_data[0] + mstor43m[m_param1m] < mstor43m[m_param1m]:
                              revert with 0, 'SafeMath: addition overflow'
                          require m_param1 - 1 < 5
                          mstor43m[m_param1m] += ext_call.return_data[0]
                          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                          if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                              require m_param1 - 1 < 5
                              if ext_call.return_data[0] > mstor38m[m_param1m]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require m_param1 - 1 < 5
                              mstor38m[m_param1m] -= ext_call.return_data[0]
                  else:
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                          if not m_param2:
                              require m_param1 - 1 < 5
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                              require m_param1 - 1 < 5
                              if ext_call.return_data[0] + mstor43m[m_param1m] < mstor43m[m_param1m]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require m_param1 - 1 < 5
                              mstor43m[m_param1m] += ext_call.return_data[0]
                              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                              if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                                  require m_param1 - 1 < 5
                                  if ext_call.return_data[0] > mstor38m[m_param1m]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require m_param1 - 1 < 5
                                  mstor38m[m_param1m] -= ext_call.return_data[0]
              else:
                  if m_param2:
                      require m_param1 - 1 < 5
                      mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = 256^(m_param1 - 1 % 32) or !(255 * 256^(m_param1 - 1 % 32)) and mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0
                      require m_param1 - 1 < 5
                      if ext_call.return_data[0] + mstor38m[m_param1m] < mstor38m[m_param1m]:
                          revert with 0, 'SafeMath: addition overflow'
                      require m_param1 - 1 < 5
                      mstor38m[m_param1m] += ext_call.return_data[0]
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 2:
                          require m_param1 - 1 < 5
                          if ext_call.return_data[0] > mstor43m[m_param1m]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          require m_param1 - 1 < 5
                          mstor43m[m_param1m] -= ext_call.return_data[0]
                  else:
                      require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                      if not mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m]:
                          if not m_param2:
                              require m_param1 - 1 < 5
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                              mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                              require m_param1 - 1 < 5
                              if ext_call.return_data[0] + mstor43m[m_param1m] < mstor43m[m_param1m]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require m_param1 - 1 < 5
                              mstor43m[m_param1m] += ext_call.return_data[0]
                              require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                              if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                                  require m_param1 - 1 < 5
                                  if ext_call.return_data[0] > mstor38m[m_param1m]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require m_param1 - 1 < 5
                                  mstor38m[m_param1m] -= ext_call.return_data[0]
                      else:
                          require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                          if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                              if not m_param2:
                                  require m_param1 - 1 < 5
                                  mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_0 = uint255(256^(m_param1 - 1 % 32))
                                  mstor50m[mstor9m]m[callerm]m[0.03125 / m_param1 - 1m]m.field_255 = 0
                                  require m_param1 - 1 < 5
                                  if ext_call.return_data[0] + mstor43m[m_param1m] < mstor43m[m_param1m]:
                                      revert with 0, 'SafeMath: addition overflow'
                                  require m_param1 - 1 < 5
                                  mstor43m[m_param1m] += ext_call.return_data[0]
                                  require mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] <= 2
                                  if mstor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))m[uint8(m_param1 - 1)m] == 1:
                                      require m_param1 - 1 < 5
                                      if ext_call.return_data[0] > mstor38m[m_param1m]:
                                          revert with 0, 'SafeMath: subtraction overflow'
                                      require m_param1 - 1 < 5
                                      mstor38m[m_param1m] -= ext_call.return_data[0]
          log 0xcba8212a: _param2, ext_call.return_data[0], unknown2f884710, _param1 - 1, caller
  return 1


# hash = 0x3f677210
# getter = None
# const = None
# payable = False
def unknown3f677210(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  if not m_param1:
      return 0
  if this.address == m_param1:
      return 0
  if 3 >= munknown2f884710:
      return 0
  mstor28m.lengthm.field_16 = 1
  mstor28m.lengthm.field_24 = 0
  mstor28m.lengthm.field_24 = m_param1
  log 0xa5a84dff: _param1, unknown2f884710
  return 1


# hash = 0x404c568f
# getter = ['storage', 160, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 21]]], ['cd', 36]]]
# const = None
# payable = False
def unknown404c568f(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 < uint256(munknown404c568fm[m_param1m])
  return addr(munknown404c568fm[m_param1m]m[m_param2m])


# hash = 0x4cc0fc39
# getter = None
# const = ['return', 3]
# payable = False
const unknown4cc0fc39 = 3


# hash = 0x4f2094a1
# getter = None
# const = ['return', 259200]
# payable = False
const unknown4f2094a1 = (72 * 24 * 3600)


# hash = 0x56f7e7ff
# getter = ['storage', 256, 0, ['add', 14, ['cd', 4]]]
# const = None
# payable = False
def unknown56f7e7ff(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < 2
  return munknown56f7e7ffm[m_param1m]


# hash = 0x5825b04c
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 19]]]
# const = None
# payable = False
def unknown5825b04c(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown5825b04cm[m_param1m]


# hash = 0x5ebad714
# getter = ['storage', 256, 0, ['add', 44, ['cd', 4]]]
# const = None
# payable = False
def unknown5ebad714(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < 5
  return munknown5ebad714m[m_param1m]


# hash = 0x5f88967b
# getter = ['bool', ['storage', 8, 8, 28]]
# const = None
# payable = False
def unknown5f88967b(): # not payable
  return bool(mstor28m.lengthm.field_8)


# hash = 0x623e3d1a
# getter = ['storage', 160, 0, ['add', 29, ['cd', 4]]]
# const = None
# payable = False
def unknown623e3d1a(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < 5
  return munknown623e3d1am[m_param1m]


# hash = 0x627d50df
# getter = ['storage', 256, 0, 49]
# const = None
# payable = False
def unknown627d50df(): # not payable
  return munknown627d50df


# hash = 0x675fb9c4
# getter = None
# const = ['return', 750000000000000000]
# payable = False
const unknown675fb9c4 = 75 * 10^16


# hash = 0x68063a74
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 20]]]
# const = None
# payable = False
def investmentsCount(address m_param1): # not payable
  require calldata.size - 4 >= 32
  return minvestmentsCountm[addr(m_param1)m]m.field_0


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  if mowner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  mowner = 0


# hash = 0x7cd9fb1c
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 22]]]
# const = None
# payable = False
def unknown7cd9fb1c(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown7cd9fb1cm[m_param1m]


# hash = 0x821f9824
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 16]]]
# const = None
# payable = False
def unknown821f9824(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown821f9824m[m_param1m]


# hash = 0x8606c91a
# getter = None
# const = ['return', 86400]
# payable = False
const unknown8606c91a = (24 * 3600)


# hash = 0x8b98a2c5
# getter = None
# const = ['return', ['data', 32, 4, 0]]
# payable = False
const unknown8b98a2c5 = ''


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = False
def isOwner(): # not payable
  return (caller == mowner)


# hash = 0x8feb82ba
# getter = None
# const = None
# payable = False
def unknown8feb82ba(): # not payable
  require ext_code.size(mstor53)
  static call mstor53.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      require ext_code.size(mstor53)
      static call mstor53.totalSupply() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not munknown0cba5355:
          if ext_call.return_data[0] <= 0:
              revert with 0, 'SafeMath: division by zero'
          require ext_call.return_data[0]
          if 0 / ext_call.return_data[0] >= 25 * 10^17:
              return (0 / ext_call.return_data[0])
      else:
          if 10^18 * munknown0cba5355 / munknown0cba5355 != 10^18:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if ext_call.return_data[0] <= 0:
              revert with 0, 'SafeMath: division by zero'
          require ext_call.return_data[0]
          if 10^18 * munknown0cba5355 / ext_call.return_data[0] >= 25 * 10^17:
              return (10^18 * munknown0cba5355 / ext_call.return_data[0])
  return 25 * 10^17


# hash = 0x9244adcd
# getter = ['struct', ['loc', 20]]
# const = None
# payable = False
def unknown9244adcd(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 < minvestmentsCountm[m_param1m]m.field_0
  return minvestmentsCountm[m_param1m]m[m_param2m]m.field_0, 
         minvestmentsCountm[m_param1m]m[m_param2m]m.field_256,
         minvestmentsCountm[m_param1m]m[m_param2m]m.field_512,
         minvestmentsCountm[m_param1m]m[m_param2m]m.field_768,
         minvestmentsCountm[m_param1m]m[m_param2m]m.field_1024,
         minvestmentsCountm[m_param1m]m[m_param2m]m.field_1280,
         minvestmentsCountm[m_param1m]m[m_param2m]m.field_1536,
         minvestmentsCountm[m_param1m]m[m_param2m]m.field_1792,
         bool(minvestmentsCountm[m_param1m]m[m_param2m]m.field_2048)


# hash = 0x92bba1fc
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 51]]]
# const = None
# payable = False
def unknown92bba1fc(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknown92bba1fcm[m_param1m]


# hash = 0x92d64c9d
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 27]]]]
# const = None
# payable = False
def unknown92d64c9d(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return bool(mstor27m[m_param1m])


# hash = 0x9a8a2145
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def unknown9a8a2145(): # not payable
  return munknown9a8a2145Address


# hash = 0x9bcc8e7b
# getter = None
# const = None
# payable = False
def unknown9bcc8e7b(uint256 m_param1, addr m_param2): # not payable
  require calldata.size - 4 >= 64
  if m_param1 < 1:
      return 0
  if 5 < m_param1:
      return 0
  require uint8(mstor28m.length) <= 1
  if uint8(mstor28m.length) == 1:
      if block.timestamp - munknown25f842c5 / 72 * 24 * 3600 != m_param1:
          return 0
  else:
      if m_param1 != 0:
          return 0
  require uint8(mstor28m.length) <= 1
  if uint8(mstor28m.length) != 1:
      return 0
  if block.timestamp - munknown25f842c5 % 72 * 24 * 3600 >= 24 * 3600:
      return 0
  if not mstor28m.lengthm.field_16:
      return 0
  if not m_param2:
      return 0
  if not caller:
      return 0
  if 3 >= munknown2f884710:
      return 0
  if 1 > m_param1:
      revert with 0, 'SafeMath: subtraction overflow'
  [94midx = 0
  mwhile [94midx < m_param1 - 1m:
      require [94midx < 5
      if munknown623e3d1am[[94midxm] == caller:
          return 0
      require [94midx < 5
      if mcandidatesm[[94midxm] == m_param2:
          return 0
      if [94midx + 1 < [94midx:
          revert with 0, 'SafeMath: addition overflow'
      [94midx = [94midx + 1
      mcontinue 
  if munknown2f884710 <= 3:
      require m_param1 - 1 < 5
      if munknown2f884710 <= 3:
          require m_param1 - 1 < 5
          require m_param1 - 1 < 5
          if caller <= mstor28m[m_param1m]m.field_0:
              if mstor28m[m_param1m]m.field_0 != caller:
                  return 0
          mstor28m[m_param1m]m.field_0 = caller
          mstor33m[m_param1m] = m_param2
          if munknown627d50df < munknown627d50df:
              revert with 0, 'SafeMath: addition overflow'
          if 0 > munknown627d50df:
              revert with 0, 'SafeMath: subtraction overflow'
      else:
          if not mstor28m[m_param1m]m.field_0:
              require m_param1 - 1 < 5
              require m_param1 - 1 < 5
              if caller <= mstor28m[m_param1m]m.field_0:
                  if mstor28m[m_param1m]m.field_0 != caller:
                      return 0
              mstor28m[m_param1m]m.field_0 = caller
              mstor33m[m_param1m] = m_param2
              if munknown627d50df < munknown627d50df:
                  revert with 0, 'SafeMath: addition overflow'
              if 0 > munknown627d50df:
                  revert with 0, 'SafeMath: subtraction overflow'
          else:
              if 3 > munknown2f884710:
                  revert with 0, 'SafeMath: subtraction overflow'
              require ext_code.size(mstor53)
              static call mstor53.balanceOfAt(address owner, uint256 blockNumber) with:
                      gas gas_remaining wei
                     args mstor28m[m_param1m]m.field_0, munknowna940646dm[mstor9 - 3m]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require m_param1 - 1 < 5
              if 0 <= ext_call.return_data[0]:
                  if ext_call.return_data[0] != 0:
                      if mstor28m[m_param1m]m.field_0 != caller:
                          return 0
                  else:
                      if caller <= mstor28m[m_param1m]m.field_0:
                          require m_param1 - 1 < 5
                          if mstor28m[m_param1m]m.field_0 != caller:
                              return 0
              mstor28m[m_param1m]m.field_0 = caller
              mstor33m[m_param1m] = m_param2
              if munknown627d50df < munknown627d50df:
                  revert with 0, 'SafeMath: addition overflow'
              if ext_call.return_data[0] > munknown627d50df:
                  revert with 0, 'SafeMath: subtraction overflow'
              munknown627d50df -= ext_call.return_data[0]
  else:
      if not caller:
          require m_param1 - 1 < 5
          if munknown2f884710 <= 3:
              require m_param1 - 1 < 5
              require m_param1 - 1 < 5
              if caller <= mstor28m[m_param1m]m.field_0:
                  if mstor28m[m_param1m]m.field_0 != caller:
                      return 0
              mstor28m[m_param1m]m.field_0 = caller
              mstor33m[m_param1m] = m_param2
              if munknown627d50df < munknown627d50df:
                  revert with 0, 'SafeMath: addition overflow'
              if 0 > munknown627d50df:
                  revert with 0, 'SafeMath: subtraction overflow'
          else:
              if not mstor28m[m_param1m]m.field_0:
                  require m_param1 - 1 < 5
                  require m_param1 - 1 < 5
                  if caller <= mstor28m[m_param1m]m.field_0:
                      if mstor28m[m_param1m]m.field_0 != caller:
                          return 0
                  mstor28m[m_param1m]m.field_0 = caller
                  mstor33m[m_param1m] = m_param2
                  if munknown627d50df < munknown627d50df:
                      revert with 0, 'SafeMath: addition overflow'
                  if 0 > munknown627d50df:
                      revert with 0, 'SafeMath: subtraction overflow'
              else:
                  if 3 > munknown2f884710:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(mstor53)
                  static call mstor53.balanceOfAt(address owner, uint256 blockNumber) with:
                          gas gas_remaining wei
                         args mstor28m[m_param1m]m.field_0, munknowna940646dm[mstor9 - 3m]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require m_param1 - 1 < 5
                  if 0 <= ext_call.return_data[0]:
                      if ext_call.return_data[0] != 0:
                          if mstor28m[m_param1m]m.field_0 != caller:
                              return 0
                      else:
                          if caller <= mstor28m[m_param1m]m.field_0:
                              require m_param1 - 1 < 5
                              if mstor28m[m_param1m]m.field_0 != caller:
                                  return 0
                  mstor28m[m_param1m]m.field_0 = caller
                  mstor33m[m_param1m] = m_param2
                  if munknown627d50df < munknown627d50df:
                      revert with 0, 'SafeMath: addition overflow'
                  if ext_call.return_data[0] > munknown627d50df:
                      revert with 0, 'SafeMath: subtraction overflow'
                  munknown627d50df -= ext_call.return_data[0]
      else:
          if 3 > munknown2f884710:
              revert with 0, 'SafeMath: subtraction overflow'
          require ext_code.size(mstor53)
          static call mstor53.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args caller, munknowna940646dm[mstor9 - 3m]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require m_param1 - 1 < 5
          if munknown2f884710 <= 3:
              require m_param1 - 1 < 5
              if ext_call.return_data[0] <= 0:
                  if ext_call.return_data[0]:
                      if mstor28m[m_param1m]m.field_0 != caller:
                          return 0
                  else:
                      if caller <= mstor28m[m_param1m]m.field_0:
                          require m_param1 - 1 < 5
                          if mstor28m[m_param1m]m.field_0 != caller:
                              return 0
              mstor28m[m_param1m]m.field_0 = caller
              mstor33m[m_param1m] = m_param2
              if ext_call.return_data[0] + munknown627d50df < munknown627d50df:
                  revert with 0, 'SafeMath: addition overflow'
              if 0 > ext_call.return_data[0] + munknown627d50df:
                  revert with 0, 'SafeMath: subtraction overflow'
              munknown627d50df += ext_call.return_data[0]
          else:
              if not mstor28m[m_param1m]m.field_0:
                  require m_param1 - 1 < 5
                  if ext_call.return_data[0] <= 0:
                      if ext_call.return_data[0]:
                          if mstor28m[m_param1m]m.field_0 != caller:
                              return 0
                      else:
                          if caller <= mstor28m[m_param1m]m.field_0:
                              require m_param1 - 1 < 5
                              if mstor28m[m_param1m]m.field_0 != caller:
                                  return 0
                  mstor28m[m_param1m]m.field_0 = caller
                  mstor33m[m_param1m] = m_param2
                  if ext_call.return_data[0] + munknown627d50df < munknown627d50df:
                      revert with 0, 'SafeMath: addition overflow'
                  if 0 > ext_call.return_data[0] + munknown627d50df:
                      revert with 0, 'SafeMath: subtraction overflow'
                  munknown627d50df += ext_call.return_data[0]
              else:
                  if 3 > munknown2f884710:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(mstor53)
                  static call mstor53.balanceOfAt(address owner, uint256 blockNumber) with:
                          gas gas_remaining wei
                         args mstor28m[m_param1m]m.field_0, munknowna940646dm[mstor9 - 3m]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require m_param1 - 1 < 5
                  if ext_call.return_data[0] <= ext_call.return_data[0]:
                      if ext_call.return_data[0] != ext_call.return_data[0]:
                          if mstor28m[m_param1m]m.field_0 != caller:
                              return 0
                      else:
                          if caller <= mstor28m[m_param1m]m.field_0:
                              require m_param1 - 1 < 5
                              if mstor28m[m_param1m]m.field_0 != caller:
                                  return 0
                  mstor28m[m_param1m]m.field_0 = caller
                  mstor33m[m_param1m] = m_param2
                  if ext_call.return_data[0] + munknown627d50df < munknown627d50df:
                      revert with 0, 'SafeMath: addition overflow'
                  if ext_call.return_data[0] > ext_call.return_data[0] + munknown627d50df:
                      revert with 0, 'SafeMath: subtraction overflow'
  log 0x85ded367: _param2, unknown2f884710, _param1 - 1, caller
  return 1


# hash = 0x9c3f1150
# getter = None
# const = None
# payable = False
def unknown9c3f1150(): # not payable
  require uint8(mstor28m.length) <= 1
  if uint8(mstor28m.length) == 1:
      if block.timestamp - munknown25f842c5 % 72 * 24 * 3600 < 24 * 3600:
          return 0
  return 1


# hash = 0xa03040c3
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def unknowna03040c3(): # not payable
  return munknowna03040c3Address


# hash = 0xa8b6b2b6
# getter = None
# const = ['return', 1000000000000000000]
# payable = False
const unknowna8b6b2b6 = 10^18


# hash = 0xa940646d
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 23]]]
# const = None
# payable = False
def unknowna940646d(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknowna940646dm[m_param1m]


# hash = 0xae2f89c2
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknownae2f89c2(): # not payable
  return munknownae2f89c2


# hash = 0xb1ace0b0
# getter = None
# const = ['return', 1000000000000000]
# payable = False
const unknownb1ace0b0 = 10^15


# hash = 0xb38ca2f2
# getter = None
# const = ['return', 2500000000000000000]
# payable = False
const unknownb38ca2f2 = 25 * 10^17


# hash = 0xb5050ea8
# getter = None
# const = ['return', 6]
# payable = False
const unknownb5050ea8 = 6


# hash = 0xb7ac4ff3
# getter = ['bool', ['storage', 8, 0, 2]]
# const = None
# payable = False
def unknownb7ac4ff3(): # not payable
  return bool(munknownb7ac4ff3)


# hash = 0xbdbcb576
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 18]]]]]
# const = None
# payable = False
def unknownbdbcb576(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  return munknownbdbcb576m[m_param1m]m[m_param2m]


# hash = 0xbf8519bd
# getter = None
# const = None
# payable = True
def unknownbf8519bd() payable: 
  require mstor58 != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
  require ext_code.size(mstor59)
  static call mstor59.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
          gas gas_remaining wei
         args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mstor58, call.value
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_call.return_data[32]
  require ext_code.size(mstor59)
  call mstor59.tradeWithHint(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId, bytes hint) with:
     value call.value wei
       gas gas_remaining wei
      args 0, 4008636142, call.value, mstor58, addr(this.address), 10000000000 * 10^18, ext_call.return_data[32], 0x332d87209f7c8296389c307eae170c2440830a47, 256, 4, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if eth.balance(this.address) > eth.balance(this.address):
      revert with 0, 'SafeMath: subtraction overflow'
  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == mstor58:
      require ext_call.return_data[0] <= 10000000000 * 10^18
      if ext_call.return_data[0]:
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == mstor58:
              require ext_call.return_data[0] <= 10000000000 * 10^18
          else:
              require ext_code.size(mstor58)
              static call mstor58.decimals() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 10000000000 * 10^18
              if ext_call.return_data[31 len 1] < 18:
                  require -ext_call.return_data[31 len 1] + 18 <= 18
              else:
                  require ext_call.return_data[31 len 1] - 18 <= 18
  else:
      require ext_code.size(mstor58)
      static call mstor58.decimals() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0] <= 10000000000 * 10^18
      if 18 < ext_call.return_data[31 len 1]:
          require ext_call.return_data[31 len 1] - 18 <= 18
          if ext_call.return_data[0]:
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == mstor58:
                  require ext_call.return_data[0] <= 10000000000 * 10^18
              else:
                  require ext_code.size(mstor58)
                  static call mstor58.decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < 18:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                  else:
                      require ext_call.return_data[31 len 1] - 18 <= 18
      else:
          require -ext_call.return_data[31 len 1] + 18 <= 18
          if 10^(-ext_call.return_data[31 len 1] + 18) * ext_call.return_data[0]:
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == mstor58:
                  require ext_call.return_data[0] <= 10000000000 * 10^18
              else:
                  require ext_code.size(mstor58)
                  static call mstor58.decimals() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 10000000000 * 10^18
                  if ext_call.return_data[31 len 1] < 18:
                      require -ext_call.return_data[31 len 1] + 18 <= 18
                  else:
                      require ext_call.return_data[31 len 1] - 18 <= 18
  revert


# hash = 0xcb0ef21d
# getter = ['storage', 160, 0, 57]
# const = None
# payable = False
def unknowncb0ef21d(): # not payable
  return munknowncb0ef21dAddress


# hash = 0xcdf8b9f8
# getter = None
# const = ['return', 100000000000000000000]
# payable = False
const unknowncdf8b9f8 = 100 * 10^18


# hash = 0xce977bc2
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 17]]]]]]
# const = None
# payable = False
def unknownce977bc2(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  return bool(mstor17m[m_param1m]m[m_param2m])


# hash = 0xd2ec1fe7
# getter = None
# const = None
# payable = False
def unknownd2ec1fe7(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  if m_param1 < 1:
      return 0
  if 5 < m_param1:
      return 0
  if 3 >= munknown2f884710:
      return 0
  if m_param1 < 1:
      return 0
  if 5 < m_param1:
      return 0
  if 1 > m_param1:
      revert with 0, 'SafeMath: subtraction overflow'
  require m_param1 - 1 < 5
  if mstor43m[m_param1m] + mstor38m[m_param1m] < mstor38m[m_param1m]:
      revert with 0, 'SafeMath: addition overflow'
  require m_param1 - 1 < 5
  if not mstor38m[m_param1m]:
      if mstor43m[m_param1m] + mstor38m[m_param1m] <= 0:
          revert with 0, 'SafeMath: division by zero'
      require mstor43m[m_param1m] + mstor38m[m_param1m]
      if 0 / mstor43m[m_param1m] + mstor38m[m_param1m] <= 75 * 10^16:
          return 0
  else:
      if 10^18 * mstor38m[m_param1m] / mstor38m[m_param1m] != 10^18:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      33,
                      0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                      mem[197 len 31]
      if mstor43m[m_param1m] + mstor38m[m_param1m] <= 0:
          revert with 0, 'SafeMath: division by zero'
      require mstor43m[m_param1m] + mstor38m[m_param1m]
      if 10^18 * mstor38m[m_param1m] / mstor43m[m_param1m] + mstor38m[m_param1m] <= 75 * 10^16:
          return 0
  if munknown2f884710 <= 3:
      require m_param1 - 1 < 5
      if mstor43m[m_param1m] + mstor38m[m_param1m] < mstor38m[m_param1m]:
          revert with 0, 'SafeMath: addition overflow'
      if mstor43m[m_param1m] + mstor38m[m_param1m] <= 0:
          return 0
  else:
      if 3 > munknown2f884710:
          revert with 0, 'SafeMath: subtraction overflow'
      require ext_code.size(mstor53)
      static call mstor53.totalSupplyAt(uint256 blockNumber) with:
              gas gas_remaining wei
             args munknowna940646dm[mstor9 - 3m]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if munknown627d50df > ext_call.return_data[0]:
          revert with 0, 'SafeMath: subtraction overflow'
      if not ext_call.return_data[0] - munknown627d50df:
          require m_param1 - 1 < 5
          if mstor43m[m_param1m] + mstor38m[m_param1m] < mstor38m[m_param1m]:
              revert with 0, 'SafeMath: addition overflow'
          if mstor43m[m_param1m] + mstor38m[m_param1m] <= 0:
              return 0
      else:
          if (10^17 * ext_call.return_data[0]) - (10^17 * munknown627d50df) / ext_call.return_data[0] - munknown627d50df != 10^17:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          require m_param1 - 1 < 5
          if mstor43m[m_param1m] + mstor38m[m_param1m] < mstor38m[m_param1m]:
              revert with 0, 'SafeMath: addition overflow'
          if mstor43m[m_param1m] + mstor38m[m_param1m] <= (10^17 * ext_call.return_data[0]) - (10^17 * munknown627d50df) / 10^18:
              return 0
  require uint8(mstor28m.length) <= 1
  if uint8(mstor28m.length) == 1:
      if m_param1 >= block.timestamp - munknown25f842c5 / 72 * 24 * 3600:
          return 0
  else:
      if m_param1 >= 0:
          return 0
  [94midx = 1
  mwhile [94midx < m_param1m:
      if [94midx >= 1:
          if 5 >= [94midx:
              if 1 > [94midx:
                  revert with 0, 'SafeMath: subtraction overflow'
              require [94midx - 1 < 5
              if mstor43m[[94midxm] + mstor38m[[94midxm] < mstor38m[[94midxm]:
                  revert with 0, 'SafeMath: addition overflow'
              require [94midx - 1 < 5
              if not mstor38m[[94midxm]:
                  if mstor43m[[94midxm] + mstor38m[[94midxm] <= 0:
                      revert with 0, 'SafeMath: division by zero'
                  require mstor43m[[94midxm] + mstor38m[[94midxm]
                  if 0 / mstor43m[[94midxm] + mstor38m[[94midxm] > 75 * 10^16:
                      if munknown2f884710 <= 3:
                          require [94midx - 1 < 5
                          if mstor43m[[94midxm] + mstor38m[[94midxm] < mstor38m[[94midxm]:
                              revert with 0, 'SafeMath: addition overflow'
                          if mstor43m[[94midxm] + mstor38m[[94midxm] > 0:
                              return 0
                      else:
                          if 3 > munknown2f884710:
                              revert with 0, 'SafeMath: subtraction overflow'
                          mem[0] = munknown2f884710 - 3
                          mem[32] = 23
                          mem[100] = munknowna940646dm[mstor9 - 3m]
                          require ext_code.size(mstor53)
                          static call mstor53.totalSupplyAt(uint256 blockNumber) with:
                                  gas gas_remaining wei
                                 args munknowna940646dm[mstor9 - 3m]
                          mem[96] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if munknown627d50df > ext_call.return_data[0]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          if not ext_call.return_data[0] - munknown627d50df:
                              require [94midx - 1 < 5
                              if mstor43m[[94midxm] + mstor38m[[94midxm] < mstor38m[[94midxm]:
                                  revert with 0, 'SafeMath: addition overflow'
                              if mstor43m[[94midxm] + mstor38m[[94midxm] > 0:
                                  return 0
                          else:
                              if (10^17 * ext_call.return_data[0]) - (10^17 * munknown627d50df) / ext_call.return_data[0] - munknown627d50df != 10^17:
                                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[197 len 31]
                              require [94midx - 1 < 5
                              if mstor43m[[94midxm] + mstor38m[[94midxm] < mstor38m[[94midxm]:
                                  revert with 0, 'SafeMath: addition overflow'
                              if mstor43m[[94midxm] + mstor38m[[94midxm] > (10^17 * ext_call.return_data[0]) - (10^17 * munknown627d50df) / 10^18:
                                  return 0
              else:
                  if 10^18 * mstor38m[[94midxm] / mstor38m[[94midxm] != 10^18:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[197 len 31]
                  if mstor43m[[94midxm] + mstor38m[[94midxm] <= 0:
                      revert with 0, 'SafeMath: division by zero'
                  require mstor43m[[94midxm] + mstor38m[[94midxm]
                  if 10^18 * mstor38m[[94midxm] / mstor43m[[94midxm] + mstor38m[[94midxm] > 75 * 10^16:
                      if munknown2f884710 <= 3:
                          require [94midx - 1 < 5
                          if mstor43m[[94midxm] + mstor38m[[94midxm] < mstor38m[[94midxm]:
                              revert with 0, 'SafeMath: addition overflow'
                          if mstor43m[[94midxm] + mstor38m[[94midxm] > 0:
                              return 0
                      else:
                          if 3 > munknown2f884710:
                              revert with 0, 'SafeMath: subtraction overflow'
                          mem[0] = munknown2f884710 - 3
                          mem[32] = 23
                          mem[100] = munknowna940646dm[mstor9 - 3m]
                          require ext_code.size(mstor53)
                          static call mstor53.totalSupplyAt(uint256 blockNumber) with:
                                  gas gas_remaining wei
                                 args munknowna940646dm[mstor9 - 3m]
                          mem[96] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if munknown627d50df > ext_call.return_data[0]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          if not ext_call.return_data[0] - munknown627d50df:
                              require [94midx - 1 < 5
                              if mstor43m[[94midxm] + mstor38m[[94midxm] < mstor38m[[94midxm]:
                                  revert with 0, 'SafeMath: addition overflow'
                              if mstor43m[[94midxm] + mstor38m[[94midxm] > 0:
                                  return 0
                          else:
                              if (10^17 * ext_call.return_data[0]) - (10^17 * munknown627d50df) / ext_call.return_data[0] - munknown627d50df != 10^17:
                                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[197 len 31]
                              require [94midx - 1 < 5
                              if mstor43m[[94midxm] + mstor38m[[94midxm] < mstor38m[[94midxm]:
                                  revert with 0, 'SafeMath: addition overflow'
                              if mstor43m[[94midxm] + mstor38m[[94midxm] > (10^17 * ext_call.return_data[0]) - (10^17 * munknown627d50df) / 10^18:
                                  return 0
      if [94midx + 1 < [94midx:
          revert with 0, 'SafeMath: addition overflow'
      [94midx = [94midx + 1
      mcontinue 
  mstor28m.lengthm.field_16 = 0
  if 1 > m_param1:
      revert with 0, 'SafeMath: subtraction overflow'
  require m_param1 - 1 < 5
  mstor28m.lengthm.field_8 = 1
  mstor28m.lengthm.field_16 = mstor28m.lengthm.field_16
  mstor28m.lengthm.field_24 = mstor33m[m_param1m]
  return 1


# hash = 0xd5da24b9
# getter = None
# const = None
# payable = False
def getVotingWeight(address m_address): # not payable
  require calldata.size - 4 >= 32
  if munknown2f884710 <= 3:
      return 0
  if not m_address:
      return 0
  if 3 > munknown2f884710:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(mstor53)
  static call mstor53.balanceOfAt(address owner, uint256 blockNumber) with:
          gas gas_remaining wei
         args addr(m_address), munknowna940646dm[mstor9 - 3m]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0xd7615d37
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknownd7615d37(): # not payable
  return munknownd7615d37Address


# hash = 0xd95393eb
# getter = ['storage', 160, 0, 56]
# const = None
# payable = False
def unknownd95393eb(): # not payable
  return munknownd95393ebAddress


# hash = 0xdb3d1ccf
# getter = ['storage', 160, 0, 8]
# const = None
# payable = False
def unknowndb3d1ccf(): # not payable
  return munknowndb3d1ccfAddress


# hash = 0xdb77839b
# getter = ['bool', ['storage', 8, 16, 28]]
# const = None
# payable = False
def unknowndb77839b(): # not payable
  return bool(mstor28m.lengthm.field_16)


# hash = 0xdc87454c
# getter = ['storage', 160, 8, 2]
# const = None
# payable = False
def unknowndc87454c(): # not payable
  return munknowndc87454cAddress


# hash = 0xe91e13a9
# getter = None
# const = ['return', 259200]
# payable = False
const CHUNK_SIZE = (72 * 24 * 3600)


# hash = 0xe96e22b9
# getter = ['storage', 256, 0, ['add', 39, ['cd', 4]]]
# const = None
# payable = False
def unknowne96e22b9(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < 5
  return munknowne96e22b9m[m_param1m]


# hash = 0xe9fc335d
# getter = None
# const = None
# payable = False
def unknowne9fc335d(): # not payable
  require uint8(mstor28m.length) <= 1
  if uint8(mstor28m.length) == 1:
      return (block.timestamp - munknown25f842c5 / 72 * 24 * 3600)
  else:
      return 0


# hash = 0xee00f705
# getter = ['storage', 8, ['mask_shl', 5, 0, 3, ['cd', 68]], ['add', ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 50]]]], ['mask_shl', 251, 5, -5, ['cd', 68]]]]
# const = None
# payable = False
def unknownee00f705(uint256 m_param1, addr m_param2, uint256 m_param3): # not payable
  require calldata.size - 4 >= 96
  require m_param3 < 5
  require munknownee00f705m[uint8(m_param3)m] <= 2
  return munknownee00f705m[uint8(m_param3)m]


# hash = 0xf04e1f3b
# getter = None
# const = None
# payable = False
def unknownf04e1f3b(): # not payable
  require ext_code.size(mstor53)
  static call mstor53.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor53)
  static call mstor53.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      if 10^16 * ext_call.return_data[0] / 10^16 != ext_call.return_data[0]:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      33,
                      0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                      mem[197 len 31]
      if 10^16 * ext_call.return_data[0] / 10^18:
          if 25 * 10^17 * 10^16 * ext_call.return_data[0] / 10^18 / 10^16 * ext_call.return_data[0] / 10^18 != 25 * 10^17:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if 25 * 10^17 * 10^16 * ext_call.return_data[0] / 10^18 / 10^18 >= 100 * 10^18:
              return (25 * 10^17 * 10^16 * ext_call.return_data[0] / 10^18 / 10^18)
  else:
      if not munknown0cba5355:
          if ext_call.return_data[0] <= 0:
              revert with 0, 'SafeMath: division by zero'
          require ext_call.return_data[0]
          require ext_code.size(mstor53)
          static call mstor53.totalSupply() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if 10^16 * ext_call.return_data[0] / 10^16 != ext_call.return_data[0]:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if 0 / ext_call.return_data[0] >= 25 * 10^17:
              if 10^16 * ext_call.return_data[0] / 10^18:
                  if 0 / ext_call.return_data[0] * 10^16 * ext_call.return_data[0] / 10^18 / 10^16 * ext_call.return_data[0] / 10^18 != 0 / ext_call.return_data[0]:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  33,
                                  0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                  mem[197 len 31]
                  if 0 / ext_call.return_data[0] * 10^16 * ext_call.return_data[0] / 10^18 / 10^18 >= 100 * 10^18:
                      return (0 / ext_call.return_data[0] * 10^16 * ext_call.return_data[0] / 10^18 / 10^18)
          else:
              if 10^16 * ext_call.return_data[0] / 10^18:
                  if 25 * 10^17 * 10^16 * ext_call.return_data[0] / 10^18 / 10^16 * ext_call.return_data[0] / 10^18 != 25 * 10^17:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  33,
                                  0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                  mem[197 len 31]
                  if 25 * 10^17 * 10^16 * ext_call.return_data[0] / 10^18 / 10^18 >= 100 * 10^18:
                      return (25 * 10^17 * 10^16 * ext_call.return_data[0] / 10^18 / 10^18)
      else:
          if 10^18 * munknown0cba5355 / munknown0cba5355 != 10^18:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if ext_call.return_data[0] <= 0:
              revert with 0, 'SafeMath: division by zero'
          require ext_call.return_data[0]
          require ext_code.size(mstor53)
          static call mstor53.totalSupply() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if 10^16 * ext_call.return_data[0] / 10^16 != ext_call.return_data[0]:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if 10^18 * munknown0cba5355 / ext_call.return_data[0] >= 25 * 10^17:
              if 10^16 * ext_call.return_data[0] / 10^18:
                  if 10^18 * munknown0cba5355 / ext_call.return_data[0] * 10^16 * ext_call.return_data[0] / 10^18 / 10^16 * ext_call.return_data[0] / 10^18 != 10^18 * munknown0cba5355 / ext_call.return_data[0]:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  33,
                                  0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                  mem[197 len 31]
                  if 10^18 * munknown0cba5355 / ext_call.return_data[0] * 10^16 * ext_call.return_data[0] / 10^18 / 10^18 >= 100 * 10^18:
                      return (10^18 * munknown0cba5355 / ext_call.return_data[0] * 10^16 * ext_call.return_data[0] / 10^18 / 10^18)
          else:
              if 10^16 * ext_call.return_data[0] / 10^18:
                  if 25 * 10^17 * 10^16 * ext_call.return_data[0] / 10^18 / 10^16 * ext_call.return_data[0] / 10^18 != 25 * 10^17:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  33,
                                  0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                  mem[197 len 31]
                  if 25 * 10^17 * 10^16 * ext_call.return_data[0] / 10^18 / 10^18 >= 100 * 10^18:
                      return (25 * 10^17 * 10^16 * ext_call.return_data[0] / 10^18 / 10^18)
  return 100 * 10^18


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  if not m_newOwner:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  38,
                  0xfe4f776e61626c653a206e6577206f776e657220697320746865207a65726f20616464726573,
                  mem[202 len 26]
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf4900863
# getter = None
# const = ['return', 750000000000000000]
# payable = False
const unknownf4900863 = 75 * 10^16


# hash = 0xf6558b00
# getter = ['storage', 8, 0, 28]
# const = None
# payable = False
def unknownf6558b00(): # not payable
  require uint8(mstor28m.length) <= 1
  return uint8(mstor28m.length)


# hash = 0xfa845ca9
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 24]]]
# const = None
# payable = False
def unknownfa845ca9(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknownfa845ca9m[m_param1m]


# hash = 0xfbf35f46
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def unknownfbf35f46(): # not payable
  return munknownfbf35f46Address


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


