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
  return stor28.length.field_24


# hash = 0x0c06b1e1
# getter = None
# const = None
# payable = False
def unknown0c06b1e1(uint256 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param1 < uint256(unknown404c568f[caller])
  require addr(unknown404c568f[caller][_param1])
  require _param1 < uint256(unknown404c568f[caller])
  require ext_code.size(addr(unknown404c568f[caller][_param1]))
  static call addr(unknown404c568f[caller][_param1]).0xe852e741 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(unknown404c568f[caller][_param1]))
  static call addr(unknown404c568f[caller][_param1]).0x2f884710 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] == unknown2f884710
  require ext_code.size(addr(unknown404c568f[caller][_param1]))
  call addr(unknown404c568f[caller][_param1]).0xab7b1c89 with:
       gas gas_remaining wei
      args _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0xeb8df86c: uint256(unknown404c568f[caller]) - 1, addr(unknown404c568f[caller][_param1]), _param2, unknown2f884710, caller


# hash = 0x0c99c9ea
# getter = None
# const = None
# payable = False
def unknown0c99c9ea(bool _param1): # not payable
  require calldata.size - 4 >= 32
  if 3 >= unknown2f884710:
      return 0
  if stor52[stor9][caller]:
      if _param1:
          return 0
      stor52[stor9][caller] = 0
      if unknown2f884710 <= 3:
          if 0 > unknown92bba1fc[stor9]:
              revert with 0, 'SafeMath: subtraction overflow'
      else:
          if not caller:
              if 0 > unknown92bba1fc[stor9]:
                  revert with 0, 'SafeMath: subtraction overflow'
          else:
              if 3 > unknown2f884710:
                  revert with 0, 'SafeMath: subtraction overflow'
              require ext_code.size(stor53)
              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                      gas gas_remaining wei
                     args caller, unknowna940646d[stor9 - 3]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] > unknown92bba1fc[stor9]:
                  revert with 0, 'SafeMath: subtraction overflow'
              unknown92bba1fc[stor9] -= ext_call.return_data[0]
  else:
      if _param1 != 1:
          return 0
      stor52[stor9][caller] = 1
      if unknown2f884710 <= 3:
          if unknown92bba1fc[stor9] < unknown92bba1fc[stor9]:
              revert with 0, 'SafeMath: addition overflow'
      else:
          if not caller:
              if unknown92bba1fc[stor9] < unknown92bba1fc[stor9]:
                  revert with 0, 'SafeMath: addition overflow'
          else:
              if 3 > unknown2f884710:
                  revert with 0, 'SafeMath: subtraction overflow'
              require ext_code.size(stor53)
              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                      gas gas_remaining wei
                     args caller, unknowna940646d[stor9 - 3]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] + unknown92bba1fc[stor9] < unknown92bba1fc[stor9]:
                  revert with 0, 'SafeMath: addition overflow'
              unknown92bba1fc[stor9] += ext_call.return_data[0]
  log 0x257d79cd: unknown2f884710, caller, _param1
  return 1


# hash = 0x0cba5355
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknown0cba5355(): # not payable
  return unknown0cba5355


# hash = 0x0e187cac
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 25]]]]
# const = None
# payable = False
def isKyberToken(address _tokenContract): # not payable
  require calldata.size - 4 >= 32
  return bool(stor25[_tokenContract])


# hash = 0x13d3d00e
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknown13d3d00e(): # not payable
  return unknown13d3d00e


# hash = 0x1a454ea6
# getter = None
# const = ['return', 200000000000000000]
# payable = False
const COMMISSION_RATE = 2 * 10^17


# hash = 0x1f5c6a51
# getter = None
# const = None
# payable = False
def unknown1f5c6a51(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  require calldata.size - 4 >= 96
  require _param1 < uint256(unknown404c568f[caller])
  require addr(unknown404c568f[caller][_param1])
  require _param1 < uint256(unknown404c568f[caller])
  require ext_code.size(addr(unknown404c568f[caller][_param1]))
  static call addr(unknown404c568f[caller][_param1]).0xe852e741 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(unknown404c568f[caller][_param1]))
  static call addr(unknown404c568f[caller][_param1]).0x2f884710 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] == unknown2f884710
  require ext_code.size(addr(unknown404c568f[caller][_param1]))
  call addr(unknown404c568f[caller][_param1]).sellOrder(uint256 sellPrice, uint256 amount) with:
       gas gas_remaining wei
      args _param2, _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_code.size(addr(unknown404c568f[caller][_param1]))
  static call addr(unknown404c568f[caller][_param1]).stake() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(unknown404c568f[caller][_param1]))
  static call addr(unknown404c568f[caller][_param1]).stake() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      if ext_call.return_data[0] <= 0:
          revert with 0, 'SafeMath: division by zero'
      require ext_call.return_data[0]
      require ext_code.size(stor53)
      call stor53.destroyTokens(address owner, uint256 amount) with:
           gas gas_remaining wei
          args this.address, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(stor53)
      call stor53.generateTokens(address holder, uint256 amount) with:
           gas gas_remaining wei
          args caller, 0 / ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(addr(unknown404c568f[caller][_param1]))
      static call addr(unknown404c568f[caller][_param1]).0x3eeb4ca with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] > block.timestamp:
          revert with 0, 'SafeMath: subtraction overflow'
      if not ext_call.return_data[0]:
          if unknownbdbcb576[caller][stor9] < unknownbdbcb576[caller][stor9]:
              revert with 0, 'SafeMath: addition overflow'
      else:
          if (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) / ext_call.return_data[0] != block.timestamp - ext_call.return_data[0]:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) + unknownbdbcb576[caller][stor9] < unknownbdbcb576[caller][stor9]:
              revert with 0, 'SafeMath: addition overflow'
          unknownbdbcb576[caller][stor9] = (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) + unknownbdbcb576[caller][stor9]
      if ext_call.return_data[0] > unknown0cba5355:
          revert with 0, 'SafeMath: subtraction overflow'
      if ext_call.return_data[32] < 0:
          revert with 0, 'SafeMath: addition overflow'
      unknown0cba5355 = ext_call.return_data[32] + unknown0cba5355 - ext_call.return_data[0]
      require ext_code.size(addr(unknown404c568f[caller][_param1]))
      static call addr(unknown404c568f[caller][_param1]).0x6f17591f with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(unknown404c568f[caller][_param1]))
      static call addr(unknown404c568f[caller][_param1]).0x76017b64 with:
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
      require ext_code.size(stor53)
      call stor53.destroyTokens(address owner, uint256 amount) with:
           gas gas_remaining wei
          args this.address, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(stor53)
      call stor53.generateTokens(address holder, uint256 amount) with:
           gas gas_remaining wei
          args caller, ext_call.return_data[32] * ext_call.return_data[0] / ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(addr(unknown404c568f[caller][_param1]))
      static call addr(unknown404c568f[caller][_param1]).0x3eeb4ca with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] > block.timestamp:
          revert with 0, 'SafeMath: subtraction overflow'
      if not ext_call.return_data[0]:
          if unknownbdbcb576[caller][stor9] < unknownbdbcb576[caller][stor9]:
              revert with 0, 'SafeMath: addition overflow'
      else:
          if (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) / ext_call.return_data[0] != block.timestamp - ext_call.return_data[0]:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) + unknownbdbcb576[caller][stor9] < unknownbdbcb576[caller][stor9]:
              revert with 0, 'SafeMath: addition overflow'
          unknownbdbcb576[caller][stor9] = (block.timestamp * ext_call.return_data[0]) - (ext_call.return_data[0] * ext_call.return_data[0]) + unknownbdbcb576[caller][stor9]
      if ext_call.return_data[0] > unknown0cba5355:
          revert with 0, 'SafeMath: subtraction overflow'
      if ext_call.return_data[32] < 0:
          revert with 0, 'SafeMath: addition overflow'
      unknown0cba5355 = ext_call.return_data[32] + unknown0cba5355 - ext_call.return_data[0]
      require ext_code.size(addr(unknown404c568f[caller][_param1]))
      static call addr(unknown404c568f[caller][_param1]).0x6f17591f with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(unknown404c568f[caller][_param1]))
      static call addr(unknown404c568f[caller][_param1]).0x76017b64 with:
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
  return unknown25f842c5


# hash = 0x2893f5cc
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 26]]]]
# const = None
# payable = False
def unknown2893f5cc(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return bool(stor26[_param1])


# hash = 0x28ad7cef
# getter = None
# const = None
# payable = False
def unknown28ad7cef(): # not payable
  if unknown2f884710 <= 3:
      return 0
  if 3 > unknown2f884710:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(stor53)
  static call stor53.totalSupplyAt(uint256 blockNumber) with:
          gas gas_remaining wei
         args unknowna940646d[stor9 - 3]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if unknown627d50df > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  return (ext_call.return_data[0] - unknown627d50df)


# hash = 0x2914af34
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def unknown2914af34(): # not payable
  return unknown2914af34Address


# hash = 0x2df182c9
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 52]]]]]]
# const = None
# payable = False
def unknown2df182c9(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  return bool(stor52[_param1][_param2])


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
  return unknown2f884710


# hash = 0x2f9fb6a4
# getter = None
# const = ['return', 10000000000000000]
# payable = False
const unknown2f9fb6a4 = 10^16


# hash = 0x3477ee2e
# getter = ['storage', 160, 0, ['add', 34, ['cd', 4]]]
# const = None
# payable = False
def candidates(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < 5
  return candidates[_param1]


# hash = 0x381f253c
# getter = None
# const = None
# payable = False
def unknown381f253c(uint256 _param1, bool _param2): # not payable
  require calldata.size - 4 >= 64
  if _param1 < 1:
      return 0
  if 5 < _param1:
      return 0
  require uint8(stor28.length) <= 1
  if uint8(stor28.length) == 1:
      if block.timestamp - unknown25f842c5 / 72 * 24 * 3600 != _param1:
          return 0
  else:
      if _param1 != 0:
          return 0
  require uint8(stor28.length) <= 1
  if uint8(stor28.length) == 1:
      if block.timestamp - unknown25f842c5 % 72 * 24 * 3600 < 24 * 3600:
          return 0
  if not stor28.length.field_16:
      return 0
  if 3 >= unknown2f884710:
      return 0
  if 1 > _param1:
      revert with 0, 'SafeMath: subtraction overflow'
  [94midx = 0
  while [94midx < _param1 - 1:
      require [94midx < 5
      if unknown623e3d1a[[94midx] == caller:
          return 0
      if [94midx + 1 < [94midx:
          revert with 0, 'SafeMath: addition overflow'
      [94midx = [94midx + 1
      continue 
  require _param1 - 1 < 5
  if unknown2f884710 <= 3:
      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
      if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
          if _param2:
              require _param1 - 1 < 5
              stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = 256^(_param1 - 1 % 32) or !(255 * 256^(_param1 - 1 % 32)) and stor50[stor9][caller][0.03125 / _param1 - 1].field_0
              require _param1 - 1 < 5
              if stor38[_param1] < stor38[_param1]:
                  revert with 0, 'SafeMath: addition overflow'
              require _param1 - 1 < 5
              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
              if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 2:
                  require _param1 - 1 < 5
                  if 0 > stor43[_param1]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require _param1 - 1 < 5
          else:
              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
              if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
                  if not _param2:
                      require _param1 - 1 < 5
                      stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                      stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                      require _param1 - 1 < 5
                      if stor43[_param1] < stor43[_param1]:
                          revert with 0, 'SafeMath: addition overflow'
                      require _param1 - 1 < 5
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                          require _param1 - 1 < 5
                          if 0 > stor38[_param1]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          require _param1 - 1 < 5
              else:
                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                  if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                      if not _param2:
                          require _param1 - 1 < 5
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                          require _param1 - 1 < 5
                          if stor43[_param1] < stor43[_param1]:
                              revert with 0, 'SafeMath: addition overflow'
                          require _param1 - 1 < 5
                          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                          if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                              require _param1 - 1 < 5
                              if 0 > stor38[_param1]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require _param1 - 1 < 5
      else:
          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
          if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] != 2:
              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
              if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
                  if not _param2:
                      require _param1 - 1 < 5
                      stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                      stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                      require _param1 - 1 < 5
                      if stor43[_param1] < stor43[_param1]:
                          revert with 0, 'SafeMath: addition overflow'
                      require _param1 - 1 < 5
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                          require _param1 - 1 < 5
                          if 0 > stor38[_param1]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          require _param1 - 1 < 5
              else:
                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                  if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                      if not _param2:
                          require _param1 - 1 < 5
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                          require _param1 - 1 < 5
                          if stor43[_param1] < stor43[_param1]:
                              revert with 0, 'SafeMath: addition overflow'
                          require _param1 - 1 < 5
                          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                          if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                              require _param1 - 1 < 5
                              if 0 > stor38[_param1]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require _param1 - 1 < 5
          else:
              if _param2:
                  require _param1 - 1 < 5
                  stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = 256^(_param1 - 1 % 32) or !(255 * 256^(_param1 - 1 % 32)) and stor50[stor9][caller][0.03125 / _param1 - 1].field_0
                  require _param1 - 1 < 5
                  if stor38[_param1] < stor38[_param1]:
                      revert with 0, 'SafeMath: addition overflow'
                  require _param1 - 1 < 5
                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                  if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 2:
                      require _param1 - 1 < 5
                      if 0 > stor43[_param1]:
                          revert with 0, 'SafeMath: subtraction overflow'
                      require _param1 - 1 < 5
              else:
                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                  if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
                      if not _param2:
                          require _param1 - 1 < 5
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                          require _param1 - 1 < 5
                          if stor43[_param1] < stor43[_param1]:
                              revert with 0, 'SafeMath: addition overflow'
                          require _param1 - 1 < 5
                          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                          if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                              require _param1 - 1 < 5
                              if 0 > stor38[_param1]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require _param1 - 1 < 5
                  else:
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                          if not _param2:
                              require _param1 - 1 < 5
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                              require _param1 - 1 < 5
                              if stor43[_param1] < stor43[_param1]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require _param1 - 1 < 5
                              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                              if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                                  require _param1 - 1 < 5
                                  if 0 > stor38[_param1]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require _param1 - 1 < 5
      log 0xcba8212a: _param2, 0, unknown2f884710, _param1 - 1, caller
  else:
      if not caller:
          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
          if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
              if _param2:
                  require _param1 - 1 < 5
                  stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = 256^(_param1 - 1 % 32) or !(255 * 256^(_param1 - 1 % 32)) and stor50[stor9][caller][0.03125 / _param1 - 1].field_0
                  require _param1 - 1 < 5
                  if stor38[_param1] < stor38[_param1]:
                      revert with 0, 'SafeMath: addition overflow'
                  require _param1 - 1 < 5
                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                  if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 2:
                      require _param1 - 1 < 5
                      if 0 > stor43[_param1]:
                          revert with 0, 'SafeMath: subtraction overflow'
                      require _param1 - 1 < 5
              else:
                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                  if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
                      if not _param2:
                          require _param1 - 1 < 5
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                          require _param1 - 1 < 5
                          if stor43[_param1] < stor43[_param1]:
                              revert with 0, 'SafeMath: addition overflow'
                          require _param1 - 1 < 5
                          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                          if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                              require _param1 - 1 < 5
                              if 0 > stor38[_param1]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require _param1 - 1 < 5
                  else:
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                          if not _param2:
                              require _param1 - 1 < 5
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                              require _param1 - 1 < 5
                              if stor43[_param1] < stor43[_param1]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require _param1 - 1 < 5
                              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                              if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                                  require _param1 - 1 < 5
                                  if 0 > stor38[_param1]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require _param1 - 1 < 5
          else:
              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
              if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] != 2:
                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                  if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
                      if not _param2:
                          require _param1 - 1 < 5
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                          require _param1 - 1 < 5
                          if stor43[_param1] < stor43[_param1]:
                              revert with 0, 'SafeMath: addition overflow'
                          require _param1 - 1 < 5
                          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                          if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                              require _param1 - 1 < 5
                              if 0 > stor38[_param1]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require _param1 - 1 < 5
                  else:
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                          if not _param2:
                              require _param1 - 1 < 5
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                              require _param1 - 1 < 5
                              if stor43[_param1] < stor43[_param1]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require _param1 - 1 < 5
                              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                              if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                                  require _param1 - 1 < 5
                                  if 0 > stor38[_param1]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require _param1 - 1 < 5
              else:
                  if _param2:
                      require _param1 - 1 < 5
                      stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = 256^(_param1 - 1 % 32) or !(255 * 256^(_param1 - 1 % 32)) and stor50[stor9][caller][0.03125 / _param1 - 1].field_0
                      require _param1 - 1 < 5
                      if stor38[_param1] < stor38[_param1]:
                          revert with 0, 'SafeMath: addition overflow'
                      require _param1 - 1 < 5
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 2:
                          require _param1 - 1 < 5
                          if 0 > stor43[_param1]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          require _param1 - 1 < 5
                  else:
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
                          if not _param2:
                              require _param1 - 1 < 5
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                              require _param1 - 1 < 5
                              if stor43[_param1] < stor43[_param1]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require _param1 - 1 < 5
                              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                              if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                                  require _param1 - 1 < 5
                                  if 0 > stor38[_param1]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require _param1 - 1 < 5
                      else:
                          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                          if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                              if not _param2:
                                  require _param1 - 1 < 5
                                  stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                                  stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                                  require _param1 - 1 < 5
                                  if stor43[_param1] < stor43[_param1]:
                                      revert with 0, 'SafeMath: addition overflow'
                                  require _param1 - 1 < 5
                                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                                  if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                                      require _param1 - 1 < 5
                                      if 0 > stor38[_param1]:
                                          revert with 0, 'SafeMath: subtraction overflow'
                                      require _param1 - 1 < 5
          log 0xcba8212a: _param2, 0, unknown2f884710, _param1 - 1, caller
      else:
          if 3 > unknown2f884710:
              revert with 0, 'SafeMath: subtraction overflow'
          require ext_code.size(stor53)
          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args caller, unknowna940646d[stor9 - 3]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
          if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
              if _param2:
                  require _param1 - 1 < 5
                  stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = 256^(_param1 - 1 % 32) or !(255 * 256^(_param1 - 1 % 32)) and stor50[stor9][caller][0.03125 / _param1 - 1].field_0
                  require _param1 - 1 < 5
                  if ext_call.return_data[0] + stor38[_param1] < stor38[_param1]:
                      revert with 0, 'SafeMath: addition overflow'
                  require _param1 - 1 < 5
                  stor38[_param1] += ext_call.return_data[0]
                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                  if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 2:
                      require _param1 - 1 < 5
                      if ext_call.return_data[0] > stor43[_param1]:
                          revert with 0, 'SafeMath: subtraction overflow'
                      require _param1 - 1 < 5
                      stor43[_param1] -= ext_call.return_data[0]
              else:
                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                  if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
                      if not _param2:
                          require _param1 - 1 < 5
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                          require _param1 - 1 < 5
                          if ext_call.return_data[0] + stor43[_param1] < stor43[_param1]:
                              revert with 0, 'SafeMath: addition overflow'
                          require _param1 - 1 < 5
                          stor43[_param1] += ext_call.return_data[0]
                          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                          if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                              require _param1 - 1 < 5
                              if ext_call.return_data[0] > stor38[_param1]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require _param1 - 1 < 5
                              stor38[_param1] -= ext_call.return_data[0]
                  else:
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                          if not _param2:
                              require _param1 - 1 < 5
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                              require _param1 - 1 < 5
                              if ext_call.return_data[0] + stor43[_param1] < stor43[_param1]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require _param1 - 1 < 5
                              stor43[_param1] += ext_call.return_data[0]
                              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                              if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                                  require _param1 - 1 < 5
                                  if ext_call.return_data[0] > stor38[_param1]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require _param1 - 1 < 5
                                  stor38[_param1] -= ext_call.return_data[0]
          else:
              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
              if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] != 2:
                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                  if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
                      if not _param2:
                          require _param1 - 1 < 5
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                          stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                          require _param1 - 1 < 5
                          if ext_call.return_data[0] + stor43[_param1] < stor43[_param1]:
                              revert with 0, 'SafeMath: addition overflow'
                          require _param1 - 1 < 5
                          stor43[_param1] += ext_call.return_data[0]
                          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                          if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                              require _param1 - 1 < 5
                              if ext_call.return_data[0] > stor38[_param1]:
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require _param1 - 1 < 5
                              stor38[_param1] -= ext_call.return_data[0]
                  else:
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                          if not _param2:
                              require _param1 - 1 < 5
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                              require _param1 - 1 < 5
                              if ext_call.return_data[0] + stor43[_param1] < stor43[_param1]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require _param1 - 1 < 5
                              stor43[_param1] += ext_call.return_data[0]
                              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                              if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                                  require _param1 - 1 < 5
                                  if ext_call.return_data[0] > stor38[_param1]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require _param1 - 1 < 5
                                  stor38[_param1] -= ext_call.return_data[0]
              else:
                  if _param2:
                      require _param1 - 1 < 5
                      stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = 256^(_param1 - 1 % 32) or !(255 * 256^(_param1 - 1 % 32)) and stor50[stor9][caller][0.03125 / _param1 - 1].field_0
                      require _param1 - 1 < 5
                      if ext_call.return_data[0] + stor38[_param1] < stor38[_param1]:
                          revert with 0, 'SafeMath: addition overflow'
                      require _param1 - 1 < 5
                      stor38[_param1] += ext_call.return_data[0]
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 2:
                          require _param1 - 1 < 5
                          if ext_call.return_data[0] > stor43[_param1]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          require _param1 - 1 < 5
                          stor43[_param1] -= ext_call.return_data[0]
                  else:
                      require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                      if not stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)]:
                          if not _param2:
                              require _param1 - 1 < 5
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                              stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                              require _param1 - 1 < 5
                              if ext_call.return_data[0] + stor43[_param1] < stor43[_param1]:
                                  revert with 0, 'SafeMath: addition overflow'
                              require _param1 - 1 < 5
                              stor43[_param1] += ext_call.return_data[0]
                              require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                              if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                                  require _param1 - 1 < 5
                                  if ext_call.return_data[0] > stor38[_param1]:
                                      revert with 0, 'SafeMath: subtraction overflow'
                                  require _param1 - 1 < 5
                                  stor38[_param1] -= ext_call.return_data[0]
                      else:
                          require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                          if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                              if not _param2:
                                  require _param1 - 1 < 5
                                  stor50[stor9][caller][0.03125 / _param1 - 1].field_0 = uint255(256^(_param1 - 1 % 32))
                                  stor50[stor9][caller][0.03125 / _param1 - 1].field_255 = 0
                                  require _param1 - 1 < 5
                                  if ext_call.return_data[0] + stor43[_param1] < stor43[_param1]:
                                      revert with 0, 'SafeMath: addition overflow'
                                  require _param1 - 1 < 5
                                  stor43[_param1] += ext_call.return_data[0]
                                  require stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] <= 2
                                  if stor('array', ('div', 0.03125, ('add', -1, ('param', '_param1'))), ('map', 'caller', ('map', ('stor', 256, 0, ('name', 'stor9', 9)), ('name', 'stor50', 50))))[uint8(_param1 - 1)] == 1:
                                      require _param1 - 1 < 5
                                      if ext_call.return_data[0] > stor38[_param1]:
                                          revert with 0, 'SafeMath: subtraction overflow'
                                      require _param1 - 1 < 5
                                      stor38[_param1] -= ext_call.return_data[0]
          log 0xcba8212a: _param2, ext_call.return_data[0], unknown2f884710, _param1 - 1, caller
  return 1


# hash = 0x3f677210
# getter = None
# const = None
# payable = False
def unknown3f677210(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if not _param1:
      return 0
  if this.address == _param1:
      return 0
  if 3 >= unknown2f884710:
      return 0
  stor28.length.field_16 = 1
  stor28.length.field_24 = 0
  stor28.length.field_24 = _param1
  log 0xa5a84dff: _param1, unknown2f884710
  return 1


# hash = 0x404c568f
# getter = ['storage', 160, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 21]]], ['cd', 36]]]
# const = None
# payable = False
def unknown404c568f(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < uint256(unknown404c568f[_param1])
  return addr(unknown404c568f[_param1][_param2])


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
def unknown56f7e7ff(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < 2
  return unknown56f7e7ff[_param1]


# hash = 0x5825b04c
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 19]]]
# const = None
# payable = False
def unknown5825b04c(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown5825b04c[_param1]


# hash = 0x5ebad714
# getter = ['storage', 256, 0, ['add', 44, ['cd', 4]]]
# const = None
# payable = False
def unknown5ebad714(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < 5
  return unknown5ebad714[_param1]


# hash = 0x5f88967b
# getter = ['bool', ['storage', 8, 8, 28]]
# const = None
# payable = False
def unknown5f88967b(): # not payable
  return bool(stor28.length.field_8)


# hash = 0x623e3d1a
# getter = ['storage', 160, 0, ['add', 29, ['cd', 4]]]
# const = None
# payable = False
def unknown623e3d1a(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < 5
  return unknown623e3d1a[_param1]


# hash = 0x627d50df
# getter = ['storage', 256, 0, 49]
# const = None
# payable = False
def unknown627d50df(): # not payable
  return unknown627d50df


# hash = 0x675fb9c4
# getter = None
# const = ['return', 750000000000000000]
# payable = False
const unknown675fb9c4 = 75 * 10^16


# hash = 0x68063a74
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 20]]]
# const = None
# payable = False
def investmentsCount(address _param1): # not payable
  require calldata.size - 4 >= 32
  return investmentsCount[addr(_param1)].field_0


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  owner = 0


# hash = 0x7cd9fb1c
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 22]]]
# const = None
# payable = False
def unknown7cd9fb1c(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown7cd9fb1c[_param1]


# hash = 0x821f9824
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 16]]]
# const = None
# payable = False
def unknown821f9824(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown821f9824[_param1]


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
  return owner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = False
def isOwner(): # not payable
  return (caller == owner)


# hash = 0x8feb82ba
# getter = None
# const = None
# payable = False
def unknown8feb82ba(): # not payable
  require ext_code.size(stor53)
  static call stor53.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      require ext_code.size(stor53)
      static call stor53.totalSupply() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not unknown0cba5355:
          if ext_call.return_data[0] <= 0:
              revert with 0, 'SafeMath: division by zero'
          require ext_call.return_data[0]
          if 0 / ext_call.return_data[0] >= 25 * 10^17:
              return (0 / ext_call.return_data[0])
      else:
          if 10^18 * unknown0cba5355 / unknown0cba5355 != 10^18:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if ext_call.return_data[0] <= 0:
              revert with 0, 'SafeMath: division by zero'
          require ext_call.return_data[0]
          if 10^18 * unknown0cba5355 / ext_call.return_data[0] >= 25 * 10^17:
              return (10^18 * unknown0cba5355 / ext_call.return_data[0])
  return 25 * 10^17


# hash = 0x9244adcd
# getter = ['struct', ['loc', 20]]
# const = None
# payable = False
def unknown9244adcd(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < investmentsCount[_param1].field_0
  return investmentsCount[_param1][_param2].field_0, 
         investmentsCount[_param1][_param2].field_256,
         investmentsCount[_param1][_param2].field_512,
         investmentsCount[_param1][_param2].field_768,
         investmentsCount[_param1][_param2].field_1024,
         investmentsCount[_param1][_param2].field_1280,
         investmentsCount[_param1][_param2].field_1536,
         investmentsCount[_param1][_param2].field_1792,
         bool(investmentsCount[_param1][_param2].field_2048)


# hash = 0x92bba1fc
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 51]]]
# const = None
# payable = False
def unknown92bba1fc(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknown92bba1fc[_param1]


# hash = 0x92d64c9d
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 27]]]]
# const = None
# payable = False
def unknown92d64c9d(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return bool(stor27[_param1])


# hash = 0x9a8a2145
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def unknown9a8a2145(): # not payable
  return unknown9a8a2145Address


# hash = 0x9bcc8e7b
# getter = None
# const = None
# payable = False
def unknown9bcc8e7b(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if _param1 < 1:
      return 0
  if 5 < _param1:
      return 0
  require uint8(stor28.length) <= 1
  if uint8(stor28.length) == 1:
      if block.timestamp - unknown25f842c5 / 72 * 24 * 3600 != _param1:
          return 0
  else:
      if _param1 != 0:
          return 0
  require uint8(stor28.length) <= 1
  if uint8(stor28.length) != 1:
      return 0
  if block.timestamp - unknown25f842c5 % 72 * 24 * 3600 >= 24 * 3600:
      return 0
  if not stor28.length.field_16:
      return 0
  if not _param2:
      return 0
  if not caller:
      return 0
  if 3 >= unknown2f884710:
      return 0
  if 1 > _param1:
      revert with 0, 'SafeMath: subtraction overflow'
  [94midx = 0
  while [94midx < _param1 - 1:
      require [94midx < 5
      if unknown623e3d1a[[94midx] == caller:
          return 0
      require [94midx < 5
      if candidates[[94midx] == _param2:
          return 0
      if [94midx + 1 < [94midx:
          revert with 0, 'SafeMath: addition overflow'
      [94midx = [94midx + 1
      continue 
  if unknown2f884710 <= 3:
      require _param1 - 1 < 5
      if unknown2f884710 <= 3:
          require _param1 - 1 < 5
          require _param1 - 1 < 5
          if caller <= stor28[_param1].field_0:
              if stor28[_param1].field_0 != caller:
                  return 0
          stor28[_param1].field_0 = caller
          stor33[_param1] = _param2
          if unknown627d50df < unknown627d50df:
              revert with 0, 'SafeMath: addition overflow'
          if 0 > unknown627d50df:
              revert with 0, 'SafeMath: subtraction overflow'
      else:
          if not stor28[_param1].field_0:
              require _param1 - 1 < 5
              require _param1 - 1 < 5
              if caller <= stor28[_param1].field_0:
                  if stor28[_param1].field_0 != caller:
                      return 0
              stor28[_param1].field_0 = caller
              stor33[_param1] = _param2
              if unknown627d50df < unknown627d50df:
                  revert with 0, 'SafeMath: addition overflow'
              if 0 > unknown627d50df:
                  revert with 0, 'SafeMath: subtraction overflow'
          else:
              if 3 > unknown2f884710:
                  revert with 0, 'SafeMath: subtraction overflow'
              require ext_code.size(stor53)
              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                      gas gas_remaining wei
                     args stor28[_param1].field_0, unknowna940646d[stor9 - 3]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require _param1 - 1 < 5
              if 0 <= ext_call.return_data[0]:
                  if ext_call.return_data[0] != 0:
                      if stor28[_param1].field_0 != caller:
                          return 0
                  else:
                      if caller <= stor28[_param1].field_0:
                          require _param1 - 1 < 5
                          if stor28[_param1].field_0 != caller:
                              return 0
              stor28[_param1].field_0 = caller
              stor33[_param1] = _param2
              if unknown627d50df < unknown627d50df:
                  revert with 0, 'SafeMath: addition overflow'
              if ext_call.return_data[0] > unknown627d50df:
                  revert with 0, 'SafeMath: subtraction overflow'
              unknown627d50df -= ext_call.return_data[0]
  else:
      if not caller:
          require _param1 - 1 < 5
          if unknown2f884710 <= 3:
              require _param1 - 1 < 5
              require _param1 - 1 < 5
              if caller <= stor28[_param1].field_0:
                  if stor28[_param1].field_0 != caller:
                      return 0
              stor28[_param1].field_0 = caller
              stor33[_param1] = _param2
              if unknown627d50df < unknown627d50df:
                  revert with 0, 'SafeMath: addition overflow'
              if 0 > unknown627d50df:
                  revert with 0, 'SafeMath: subtraction overflow'
          else:
              if not stor28[_param1].field_0:
                  require _param1 - 1 < 5
                  require _param1 - 1 < 5
                  if caller <= stor28[_param1].field_0:
                      if stor28[_param1].field_0 != caller:
                          return 0
                  stor28[_param1].field_0 = caller
                  stor33[_param1] = _param2
                  if unknown627d50df < unknown627d50df:
                      revert with 0, 'SafeMath: addition overflow'
                  if 0 > unknown627d50df:
                      revert with 0, 'SafeMath: subtraction overflow'
              else:
                  if 3 > unknown2f884710:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(stor53)
                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                          gas gas_remaining wei
                         args stor28[_param1].field_0, unknowna940646d[stor9 - 3]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require _param1 - 1 < 5
                  if 0 <= ext_call.return_data[0]:
                      if ext_call.return_data[0] != 0:
                          if stor28[_param1].field_0 != caller:
                              return 0
                      else:
                          if caller <= stor28[_param1].field_0:
                              require _param1 - 1 < 5
                              if stor28[_param1].field_0 != caller:
                                  return 0
                  stor28[_param1].field_0 = caller
                  stor33[_param1] = _param2
                  if unknown627d50df < unknown627d50df:
                      revert with 0, 'SafeMath: addition overflow'
                  if ext_call.return_data[0] > unknown627d50df:
                      revert with 0, 'SafeMath: subtraction overflow'
                  unknown627d50df -= ext_call.return_data[0]
      else:
          if 3 > unknown2f884710:
              revert with 0, 'SafeMath: subtraction overflow'
          require ext_code.size(stor53)
          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args caller, unknowna940646d[stor9 - 3]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require _param1 - 1 < 5
          if unknown2f884710 <= 3:
              require _param1 - 1 < 5
              if ext_call.return_data[0] <= 0:
                  if ext_call.return_data[0]:
                      if stor28[_param1].field_0 != caller:
                          return 0
                  else:
                      if caller <= stor28[_param1].field_0:
                          require _param1 - 1 < 5
                          if stor28[_param1].field_0 != caller:
                              return 0
              stor28[_param1].field_0 = caller
              stor33[_param1] = _param2
              if ext_call.return_data[0] + unknown627d50df < unknown627d50df:
                  revert with 0, 'SafeMath: addition overflow'
              if 0 > ext_call.return_data[0] + unknown627d50df:
                  revert with 0, 'SafeMath: subtraction overflow'
              unknown627d50df += ext_call.return_data[0]
          else:
              if not stor28[_param1].field_0:
                  require _param1 - 1 < 5
                  if ext_call.return_data[0] <= 0:
                      if ext_call.return_data[0]:
                          if stor28[_param1].field_0 != caller:
                              return 0
                      else:
                          if caller <= stor28[_param1].field_0:
                              require _param1 - 1 < 5
                              if stor28[_param1].field_0 != caller:
                                  return 0
                  stor28[_param1].field_0 = caller
                  stor33[_param1] = _param2
                  if ext_call.return_data[0] + unknown627d50df < unknown627d50df:
                      revert with 0, 'SafeMath: addition overflow'
                  if 0 > ext_call.return_data[0] + unknown627d50df:
                      revert with 0, 'SafeMath: subtraction overflow'
                  unknown627d50df += ext_call.return_data[0]
              else:
                  if 3 > unknown2f884710:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(stor53)
                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                          gas gas_remaining wei
                         args stor28[_param1].field_0, unknowna940646d[stor9 - 3]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require _param1 - 1 < 5
                  if ext_call.return_data[0] <= ext_call.return_data[0]:
                      if ext_call.return_data[0] != ext_call.return_data[0]:
                          if stor28[_param1].field_0 != caller:
                              return 0
                      else:
                          if caller <= stor28[_param1].field_0:
                              require _param1 - 1 < 5
                              if stor28[_param1].field_0 != caller:
                                  return 0
                  stor28[_param1].field_0 = caller
                  stor33[_param1] = _param2
                  if ext_call.return_data[0] + unknown627d50df < unknown627d50df:
                      revert with 0, 'SafeMath: addition overflow'
                  if ext_call.return_data[0] > ext_call.return_data[0] + unknown627d50df:
                      revert with 0, 'SafeMath: subtraction overflow'
  log 0x85ded367: _param2, unknown2f884710, _param1 - 1, caller
  return 1


# hash = 0x9c3f1150
# getter = None
# const = None
# payable = False
def unknown9c3f1150(): # not payable
  require uint8(stor28.length) <= 1
  if uint8(stor28.length) == 1:
      if block.timestamp - unknown25f842c5 % 72 * 24 * 3600 < 24 * 3600:
          return 0
  return 1


# hash = 0xa03040c3
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def unknowna03040c3(): # not payable
  return unknowna03040c3Address


# hash = 0xa8b6b2b6
# getter = None
# const = ['return', 1000000000000000000]
# payable = False
const unknowna8b6b2b6 = 10^18


# hash = 0xa940646d
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 23]]]
# const = None
# payable = False
def unknowna940646d(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  return unknowna940646d[_param1]


# hash = 0xae2f89c2
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknownae2f89c2(): # not payable
  return unknownae2f89c2


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
  return bool(unknownb7ac4ff3)


# hash = 0xbdbcb576
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 18]]]]]
# const = None
# payable = False
def unknownbdbcb576(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  return unknownbdbcb576[_param1][_param2]


# hash = 0xbf8519bd
# getter = None
# const = None
# payable = True
def unknownbf8519bd() payable: 
  require stor58 != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
  require ext_code.size(stor59)
  static call stor59.getExpectedRate(address srcToken, address destToken, uint256 srcTokenValue) with:
          gas gas_remaining wei
         args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, stor58, call.value
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_call.return_data[32]
  require ext_code.size(stor59)
  call stor59.tradeWithHint(address src, uint256 srcAmount, address dest, address destAddress, uint256 maxDestAmount, uint256 minConversionRate, address walletId, bytes hint) with:
     value call.value wei
       gas gas_remaining wei
      args 0, 4008636142, call.value, stor58, addr(this.address), 10000000000 * 10^18, ext_call.return_data[32], 0x332d87209f7c8296389c307eae170c2440830a47, 256, 4, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  if eth.balance(this.address) > eth.balance(this.address):
      revert with 0, 'SafeMath: subtraction overflow'
  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == stor58:
      require ext_call.return_data[0] <= 10000000000 * 10^18
      if ext_call.return_data[0]:
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == stor58:
              require ext_call.return_data[0] <= 10000000000 * 10^18
          else:
              require ext_code.size(stor58)
              static call stor58.decimals() with:
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
      require ext_code.size(stor58)
      static call stor58.decimals() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0] <= 10000000000 * 10^18
      if 18 < ext_call.return_data[31 len 1]:
          require ext_call.return_data[31 len 1] - 18 <= 18
          if ext_call.return_data[0]:
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == stor58:
                  require ext_call.return_data[0] <= 10000000000 * 10^18
              else:
                  require ext_code.size(stor58)
                  static call stor58.decimals() with:
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
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == stor58:
                  require ext_call.return_data[0] <= 10000000000 * 10^18
              else:
                  require ext_code.size(stor58)
                  static call stor58.decimals() with:
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
  return unknowncb0ef21dAddress


# hash = 0xcdf8b9f8
# getter = None
# const = ['return', 100000000000000000000]
# payable = False
const unknowncdf8b9f8 = 100 * 10^18


# hash = 0xce977bc2
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 17]]]]]]
# const = None
# payable = False
def unknownce977bc2(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  return bool(stor17[_param1][_param2])


# hash = 0xd2ec1fe7
# getter = None
# const = None
# payable = False
def unknownd2ec1fe7(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if _param1 < 1:
      return 0
  if 5 < _param1:
      return 0
  if 3 >= unknown2f884710:
      return 0
  if _param1 < 1:
      return 0
  if 5 < _param1:
      return 0
  if 1 > _param1:
      revert with 0, 'SafeMath: subtraction overflow'
  require _param1 - 1 < 5
  if stor43[_param1] + stor38[_param1] < stor38[_param1]:
      revert with 0, 'SafeMath: addition overflow'
  require _param1 - 1 < 5
  if not stor38[_param1]:
      if stor43[_param1] + stor38[_param1] <= 0:
          revert with 0, 'SafeMath: division by zero'
      require stor43[_param1] + stor38[_param1]
      if 0 / stor43[_param1] + stor38[_param1] <= 75 * 10^16:
          return 0
  else:
      if 10^18 * stor38[_param1] / stor38[_param1] != 10^18:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      33,
                      0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                      mem[197 len 31]
      if stor43[_param1] + stor38[_param1] <= 0:
          revert with 0, 'SafeMath: division by zero'
      require stor43[_param1] + stor38[_param1]
      if 10^18 * stor38[_param1] / stor43[_param1] + stor38[_param1] <= 75 * 10^16:
          return 0
  if unknown2f884710 <= 3:
      require _param1 - 1 < 5
      if stor43[_param1] + stor38[_param1] < stor38[_param1]:
          revert with 0, 'SafeMath: addition overflow'
      if stor43[_param1] + stor38[_param1] <= 0:
          return 0
  else:
      if 3 > unknown2f884710:
          revert with 0, 'SafeMath: subtraction overflow'
      require ext_code.size(stor53)
      static call stor53.totalSupplyAt(uint256 blockNumber) with:
              gas gas_remaining wei
             args unknowna940646d[stor9 - 3]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if unknown627d50df > ext_call.return_data[0]:
          revert with 0, 'SafeMath: subtraction overflow'
      if not ext_call.return_data[0] - unknown627d50df:
          require _param1 - 1 < 5
          if stor43[_param1] + stor38[_param1] < stor38[_param1]:
              revert with 0, 'SafeMath: addition overflow'
          if stor43[_param1] + stor38[_param1] <= 0:
              return 0
      else:
          if (10^17 * ext_call.return_data[0]) - (10^17 * unknown627d50df) / ext_call.return_data[0] - unknown627d50df != 10^17:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          require _param1 - 1 < 5
          if stor43[_param1] + stor38[_param1] < stor38[_param1]:
              revert with 0, 'SafeMath: addition overflow'
          if stor43[_param1] + stor38[_param1] <= (10^17 * ext_call.return_data[0]) - (10^17 * unknown627d50df) / 10^18:
              return 0
  require uint8(stor28.length) <= 1
  if uint8(stor28.length) == 1:
      if _param1 >= block.timestamp - unknown25f842c5 / 72 * 24 * 3600:
          return 0
  else:
      if _param1 >= 0:
          return 0
  [94midx = 1
  while [94midx < _param1:
      if [94midx >= 1:
          if 5 >= [94midx:
              if 1 > [94midx:
                  revert with 0, 'SafeMath: subtraction overflow'
              require [94midx - 1 < 5
              if stor43[[94midx] + stor38[[94midx] < stor38[[94midx]:
                  revert with 0, 'SafeMath: addition overflow'
              require [94midx - 1 < 5
              if not stor38[[94midx]:
                  if stor43[[94midx] + stor38[[94midx] <= 0:
                      revert with 0, 'SafeMath: division by zero'
                  require stor43[[94midx] + stor38[[94midx]
                  if 0 / stor43[[94midx] + stor38[[94midx] > 75 * 10^16:
                      if unknown2f884710 <= 3:
                          require [94midx - 1 < 5
                          if stor43[[94midx] + stor38[[94midx] < stor38[[94midx]:
                              revert with 0, 'SafeMath: addition overflow'
                          if stor43[[94midx] + stor38[[94midx] > 0:
                              return 0
                      else:
                          if 3 > unknown2f884710:
                              revert with 0, 'SafeMath: subtraction overflow'
                          mem[0] = unknown2f884710 - 3
                          mem[32] = 23
                          mem[100] = unknowna940646d[stor9 - 3]
                          require ext_code.size(stor53)
                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                  gas gas_remaining wei
                                 args unknowna940646d[stor9 - 3]
                          mem[96] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if unknown627d50df > ext_call.return_data[0]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          if not ext_call.return_data[0] - unknown627d50df:
                              require [94midx - 1 < 5
                              if stor43[[94midx] + stor38[[94midx] < stor38[[94midx]:
                                  revert with 0, 'SafeMath: addition overflow'
                              if stor43[[94midx] + stor38[[94midx] > 0:
                                  return 0
                          else:
                              if (10^17 * ext_call.return_data[0]) - (10^17 * unknown627d50df) / ext_call.return_data[0] - unknown627d50df != 10^17:
                                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[197 len 31]
                              require [94midx - 1 < 5
                              if stor43[[94midx] + stor38[[94midx] < stor38[[94midx]:
                                  revert with 0, 'SafeMath: addition overflow'
                              if stor43[[94midx] + stor38[[94midx] > (10^17 * ext_call.return_data[0]) - (10^17 * unknown627d50df) / 10^18:
                                  return 0
              else:
                  if 10^18 * stor38[[94midx] / stor38[[94midx] != 10^18:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[197 len 31]
                  if stor43[[94midx] + stor38[[94midx] <= 0:
                      revert with 0, 'SafeMath: division by zero'
                  require stor43[[94midx] + stor38[[94midx]
                  if 10^18 * stor38[[94midx] / stor43[[94midx] + stor38[[94midx] > 75 * 10^16:
                      if unknown2f884710 <= 3:
                          require [94midx - 1 < 5
                          if stor43[[94midx] + stor38[[94midx] < stor38[[94midx]:
                              revert with 0, 'SafeMath: addition overflow'
                          if stor43[[94midx] + stor38[[94midx] > 0:
                              return 0
                      else:
                          if 3 > unknown2f884710:
                              revert with 0, 'SafeMath: subtraction overflow'
                          mem[0] = unknown2f884710 - 3
                          mem[32] = 23
                          mem[100] = unknowna940646d[stor9 - 3]
                          require ext_code.size(stor53)
                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                  gas gas_remaining wei
                                 args unknowna940646d[stor9 - 3]
                          mem[96] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          if unknown627d50df > ext_call.return_data[0]:
                              revert with 0, 'SafeMath: subtraction overflow'
                          if not ext_call.return_data[0] - unknown627d50df:
                              require [94midx - 1 < 5
                              if stor43[[94midx] + stor38[[94midx] < stor38[[94midx]:
                                  revert with 0, 'SafeMath: addition overflow'
                              if stor43[[94midx] + stor38[[94midx] > 0:
                                  return 0
                          else:
                              if (10^17 * ext_call.return_data[0]) - (10^17 * unknown627d50df) / ext_call.return_data[0] - unknown627d50df != 10^17:
                                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[197 len 31]
                              require [94midx - 1 < 5
                              if stor43[[94midx] + stor38[[94midx] < stor38[[94midx]:
                                  revert with 0, 'SafeMath: addition overflow'
                              if stor43[[94midx] + stor38[[94midx] > (10^17 * ext_call.return_data[0]) - (10^17 * unknown627d50df) / 10^18:
                                  return 0
      if [94midx + 1 < [94midx:
          revert with 0, 'SafeMath: addition overflow'
      [94midx = [94midx + 1
      continue 
  stor28.length.field_16 = 0
  if 1 > _param1:
      revert with 0, 'SafeMath: subtraction overflow'
  require _param1 - 1 < 5
  stor28.length.field_8 = 1
  stor28.length.field_16 = stor28.length.field_16
  stor28.length.field_24 = stor33[_param1]
  return 1


# hash = 0xd5da24b9
# getter = None
# const = None
# payable = False
def getVotingWeight(address _address): # not payable
  require calldata.size - 4 >= 32
  if unknown2f884710 <= 3:
      return 0
  if not _address:
      return 0
  if 3 > unknown2f884710:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(stor53)
  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
          gas gas_remaining wei
         args addr(_address), unknowna940646d[stor9 - 3]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0xd7615d37
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknownd7615d37(): # not payable
  return unknownd7615d37Address


# hash = 0xd95393eb
# getter = ['storage', 160, 0, 56]
# const = None
# payable = False
def unknownd95393eb(): # not payable
  return unknownd95393ebAddress


# hash = 0xdb3d1ccf
# getter = ['storage', 160, 0, 8]
# const = None
# payable = False
def unknowndb3d1ccf(): # not payable
  return unknowndb3d1ccfAddress


# hash = 0xdb77839b
# getter = ['bool', ['storage', 8, 16, 28]]
# const = None
# payable = False
def unknowndb77839b(): # not payable
  return bool(stor28.length.field_16)


# hash = 0xdc87454c
# getter = ['storage', 160, 8, 2]
# const = None
# payable = False
def unknowndc87454c(): # not payable
  return unknowndc87454cAddress


# hash = 0xe91e13a9
# getter = None
# const = ['return', 259200]
# payable = False
const CHUNK_SIZE = (72 * 24 * 3600)


# hash = 0xe96e22b9
# getter = ['storage', 256, 0, ['add', 39, ['cd', 4]]]
# const = None
# payable = False
def unknowne96e22b9(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < 5
  return unknowne96e22b9[_param1]


# hash = 0xe9fc335d
# getter = None
# const = None
# payable = False
def unknowne9fc335d(): # not payable
  require uint8(stor28.length) <= 1
  if uint8(stor28.length) == 1:
      return (block.timestamp - unknown25f842c5 / 72 * 24 * 3600)
  else:
      return 0


# hash = 0xee00f705
# getter = ['storage', 8, ['mask_shl', 5, 0, 3, ['cd', 68]], ['add', ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 50]]]], ['mask_shl', 251, 5, -5, ['cd', 68]]]]
# const = None
# payable = False
def unknownee00f705(uint256 _param1, addr _param2, uint256 _param3): # not payable
  require calldata.size - 4 >= 96
  require _param3 < 5
  require unknownee00f705[uint8(_param3)] <= 2
  return unknownee00f705[uint8(_param3)]


# hash = 0xf04e1f3b
# getter = None
# const = None
# payable = False
def unknownf04e1f3b(): # not payable
  require ext_code.size(stor53)
  static call stor53.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(stor53)
  static call stor53.totalSupply() with:
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
      if not unknown0cba5355:
          if ext_call.return_data[0] <= 0:
              revert with 0, 'SafeMath: division by zero'
          require ext_call.return_data[0]
          require ext_code.size(stor53)
          static call stor53.totalSupply() with:
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
          if 10^18 * unknown0cba5355 / unknown0cba5355 != 10^18:
              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                          32,
                          33,
                          0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                          mem[197 len 31]
          if ext_call.return_data[0] <= 0:
              revert with 0, 'SafeMath: division by zero'
          require ext_call.return_data[0]
          require ext_code.size(stor53)
          static call stor53.totalSupply() with:
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
          if 10^18 * unknown0cba5355 / ext_call.return_data[0] >= 25 * 10^17:
              if 10^16 * ext_call.return_data[0] / 10^18:
                  if 10^18 * unknown0cba5355 / ext_call.return_data[0] * 10^16 * ext_call.return_data[0] / 10^18 / 10^16 * ext_call.return_data[0] / 10^18 != 10^18 * unknown0cba5355 / ext_call.return_data[0]:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                                  32,
                                  33,
                                  0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                  mem[197 len 31]
                  if 10^18 * unknown0cba5355 / ext_call.return_data[0] * 10^16 * ext_call.return_data[0] / 10^18 / 10^18 >= 100 * 10^18:
                      return (10^18 * unknown0cba5355 / ext_call.return_data[0] * 10^16 * ext_call.return_data[0] / 10^18 / 10^18)
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
def transferOwnership(address _newOwner): # not payable
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  if not _newOwner:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  38,
                  0xfe4f776e61626c653a206e6577206f776e657220697320746865207a65726f20616464726573,
                  mem[202 len 26]
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


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
  require uint8(stor28.length) <= 1
  return uint8(stor28.length)


# hash = 0xfa845ca9
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 24]]]
# const = None
# payable = False
def unknownfa845ca9(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return unknownfa845ca9[_param1]


# hash = 0xfbf35f46
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def unknownfbf35f46(): # not payable
  return unknownfbf35f46Address


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


