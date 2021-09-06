# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xdFC2c105b945474ff696bb839F268d29FEe5b8E4 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x173e7707': 'unknown173e7707(?)', '0x2fcfb8ab': 'unknown2fcfb8ab(?)', '0x338b5dea': 'depositToken(address _token, uint256 _amount)', '0x3bed33ce': 'withdrawEther(uint256 _amount)', '0x3f677210': 'unknown3f677210(?)', '0x98ea5fca': 'depositEther()', '0x9bcc8e7b': 'unknown9bcc8e7b(?)', '0x9e281a98': 'withdrawToken(address _token, uint256 _amount)', '0xd2ec1fe7': 'unknownd2ec1fe7(?)'} 

# storage definitions
def storage:
    # storage address 26
    stor26
    # storage address 56
    unknownd95393ebAddress # mask: a s
    # storage address 2
    unknowndc87454cAddress # mask: a s
    # storage address 2
    unknownb7ac4ff3 # mask: a s
    # storage address 27
    stor27
    # storage address 7
    unknownfbf35f46Address # mask: a s
    # storage address 1
    stor1
    # storage address 13
    unknownae2f89c2 # mask: a s
    # storage address 20
    investmentsCount
    # storage address 10
    unknown0cba5355 # mask: a s
    # storage address 23
    unknowna940646d
    # storage address 22
    unknown7cd9fb1c
    # storage address 28
    stor28 # mask: a s
    # storage address 28
    nextVersionAddress # mask: a s
    # storage address 28
    unknowndb77839b # mask: a s
    # storage address 28
    unknownf6558b00 # mask: a s
    # storage address 28
    unknown5f88967b # mask: a s
    # storage address 16
    unknown821f9824
    # storage address 19
    unknown5825b04c
    # storage address 25
    stor25
    # storage address 39
    unknowne96e22b9
    # storage address 58
    stor58 # mask: a s
    # storage address 55
    stor55 # mask: a s
    # storage address 17
    stor17
    # storage address 0
    owner # mask: a s
    # storage address 12
    unknown13d3d00e # mask: a s
    # storage address 21
    unknown404c568f
    # storage address 14
    unknown56f7e7ff
    # storage address 18
    unknownbdbcb576
    # storage address 24
    unknownfa845ca9
    # storage address 57
    unknowncb0ef21dAddress # mask: a s
    # storage address 53
    stor53 # mask: a s
    # storage address 4
    unknowna03040c3Address # mask: a s
    # storage address 49
    unknown627d50df # mask: a s
    # storage address 52
    stor52
    # storage address 51
    unknown92bba1fc
    # storage address 6
    unknown2914af34Address # mask: a s
    # storage address 3
    unknownd7615d37Address # mask: a s
    # storage address 9
    unknown2f884710 # mask: a s
    # storage address 29
    unknown623e3d1a
    # storage address 54
    stor54 # mask: a s
    # storage address 8
    unknowndb3d1ccfAddress # mask: a s
    # storage address 44
    unknown5ebad714
    # storage address 5
    unknown9a8a2145Address # mask: a s
    # storage address 11
    unknown25f842c5 # mask: a s
    # storage address 34
    candidates
# hash = 0x0076b283
# getter = None
# const = None
# payable = False
def unknown0076b283(): # not payable
  stor1.length++
  require bool(unknown5f88967b) == 1
  require unknown56f7e7ff.length + unknown25f842c5 >= unknown25f842c5
  require block.timestamp > unknown56f7e7ff.length + unknown25f842c5
  require ext_code.size(stor53)
  call stor53.transferOwnership(address newOwner) with:
       gas gas_remaining wei
      args nextVersionAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(stor54)
  call stor54.transferOwnership(address newOwner) with:
       gas gas_remaining wei
      args nextVersionAddress
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(stor55)
  call stor55.0x1aa3ba16 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require stor1.length + 1 == stor1.length


# hash = 0x0bafd60e
# getter = ['storage', 160, 24, 28]
# const = None
# payable = False
def nextVersion(): # not payable
  return nextVersionAddress


# hash = 0x0c06b1e1
# getter = None
# const = None
# payable = False
def unknown0c06b1e1(uint32 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require unknownf6558b00 <= 1
  require unknownf6558b00 == 1
  stor1.length++
  [93mdelegate unknown2914af34Address with:
     funct _param1
       gas gas_remaining wei
      args Mask(224, 32, _param2) << 224, mem[260 len 4]
  require delegate.return_code
  require stor1.length + 1 == stor1.length


# hash = 0x0c99c9ea
# getter = None
# const = None
# payable = False
def unknown0c99c9ea(bool _param1): # not payable
  require calldata.size - 4 >= 32
  require unknownf6558b00 <= 1
  require not unknownf6558b00
  require not unknown5f88967b
  mem[224 len 4] = Mask(32, 64, _param1) >> 64
  [93mdelegate unknown2914af34Address.0xc99c9ea with:
       gas gas_remaining wei
      args Mask(224, 32, _param1) >> 32, mem[196 len 4]
  if not return_data.size:
      if delegate.return_code:
          return bool(211405290, Mask(224, 32, _param1) >> 32)
      else:
          return 0
  mem[196 len return_data.size] = ext_call.return_data[0 len return_data.size]
  if not delegate.return_code:
      return 0
  require return_data.size >= 32
  mem[ceil32(return_data.size) + 165] = bool(mem[196 len 28], Mask(32, 64, _param1) >> 64)
  return memory
    from ceil32(return_data.size) + 165
     [93mlen 32


# hash = 0x0cba5355
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknown0cba5355(): # not payable
  return unknown0cba5355


# hash = 0x0d52aeec
# getter = None
# const = None
# payable = False
def unknown0d52aeec(addr _param1): # not payable
  require calldata.size - 4 >= 32
  stor1.length++
  require unknownf6558b00 <= 1
  require not unknownf6558b00
  require _param1
  require ext_code.size(_param1)
  static call _param1.0xe852e741 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(_param1)
  static call _param1.0x2f884710 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] < unknown2f884710
  require ext_code.size(stor58)
  static call stor58.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(_param1)
  call _param1.sellOrder(uint256 sellPrice, uint256 amount) with:
       gas gas_remaining wei
      args 0, 10000000000 * 10^18
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_code.size(stor58)
  static call stor58.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] <= ext_call.return_data[0]
  require unknown0cba5355 >= unknown0cba5355
  require stor1.length + 1 == stor1.length


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
def unknown1f5c6a51(uint32 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 96
  require unknownf6558b00 <= 1
  require unknownf6558b00 == 1
  stor1.length++
  [93mdelegate unknown2914af34Address with:
     funct _param1
       gas gas_remaining wei
      args Mask(224, 32, _param2) << 480, mem[324 len 4]
  require delegate.return_code
  require stor1.length + 1 == stor1.length


# hash = 0x22d40045
# getter = None
# const = None
# payable = False
def unknown22d40045(addr _param1, uint32 _param2, uint256 _param3): # not payable
  require calldata.size - 4 >= 160
  stor1.length++
  require unknownf6558b00 <= 1
  require unknownf6558b00 == 1
  require _param1
  if _param1 != 0xfe000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
      require _param1
      require ext_code.size(_param1)
  [93mdelegate unknown2914af34Address with:
     funct _param2
       gas gas_remaining wei
      args Mask(224, 32, _param3) << 992, mem[452 len 4]
  require delegate.return_code
  require stor1.length + 1 == stor1.length


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
  require 3 <= unknown2f884710
  require ext_code.size(stor53)
  static call stor53.totalSupplyAt(uint256 blockNumber) with:
          gas gas_remaining wei
         args unknowna940646d[stor9 - 3]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require unknown627d50df <= ext_call.return_data[0]
  return (ext_call.return_data[0] - unknown627d50df)


# hash = 0x2914af34
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def unknown2914af34(): # not payable
  return unknown2914af34Address


# hash = 0x2a5addf3
# getter = None
# const = None
# payable = False
def unknown2a5addf3(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require caller == owner
  require _param1 < 10^18
  require _param1 < unknown13d3d00e
  unknown13d3d00e = _param1


# hash = 0x2b23c8a0
# getter = None
# const = None
# payable = False
def unknown2b23c8a0(addr _param1, uint32 _param2, uint256 _param3): # not payable
  require calldata.size - 4 >= 128
  stor1.length++
  require _param1
  if _param1 != 0xfe000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
      require _param1
      require ext_code.size(_param1)
  require unknownf6558b00 <= 1
  require unknownf6558b00 == 1
  [93mdelegate unknown2914af34Address with:
     funct _param2
       gas gas_remaining wei
      args Mask(224, 32, _param3) << 736, mem[388 len 4]
  require delegate.return_code
  require stor1.length + 1 == stor1.length


# hash = 0x2df182c9
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 52]]]]]]
# const = None
# payable = False
def unknown2df182c9(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  return bool(stor52[_param1][_param2])


# hash = 0x2e1ed949
# getter = None
# const = None
# payable = False
def unknown2e1ed949(uint256 _param1): # not payable
  require calldata.size - 4 >= 64
  stor1.length++
  [93mdelegate unknown2914af34Address.0x0 with:
       gas gas_remaining wei
      args Mask(224, 32, _param1) << 224, mem[260 len 4]
  require delegate.return_code
  require stor1.length + 1 == stor1.length


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


# hash = 0x31f55422
# getter = None
# const = None
# payable = False
def unknown31f55422(addr _param1): # not payable
  require calldata.size - 4 >= 32
  stor1.length++
  require unknownf6558b00 <= 1
  require not unknownf6558b00
  require _param1 != this.address
  require unknownfa845ca9[addr(_param1)] <= unknown2f884710
  require unknown2f884710 - unknownfa845ca9[addr(_param1)] >= 6
  require ext_code.size(stor53)
  static call stor53.balanceOf(address owner) with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(stor53)
  call stor53.destroyTokens(address owner, uint256 amount) with:
       gas gas_remaining wei
      args addr(_param1), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require stor1.length + 1 == stor1.length


# hash = 0x3477ee2e
# getter = ['storage', 160, 0, ['add', 34, ['cd', 4]]]
# const = None
# payable = False
def candidates(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < 5
  return candidates[_param1]


# hash = 0x365833e1
# getter = None
# const = None
# payable = False
def unknown365833e1(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require unknownf6558b00 <= 1
  require not unknownf6558b00
  stor1.length++
  require not unknown5f88967b
  require ext_code.size(stor58)
  call stor58.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args caller, this.address, _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(stor54)
  static call stor54.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(stor54)
  if not ext_call.return_data[0]:
      call stor54.generateTokens(address holder, uint256 amount) with:
           gas gas_remaining wei
          args caller, _param1
  else:
      if not unknown0cba5355:
          call stor54.generateTokens(address holder, uint256 amount) with:
               gas gas_remaining wei
              args caller, _param1
      else:
          static call stor54.totalSupply() with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not _param1:
              require unknown0cba5355 > 0
              require unknown0cba5355
              require ext_code.size(stor54)
              call stor54.generateTokens(address holder, uint256 amount) with:
                   gas gas_remaining wei
                  args caller, 0 / unknown0cba5355
          else:
              require ext_call.return_data[0] * _param1 / _param1 == ext_call.return_data[0]
              require unknown0cba5355 > 0
              require unknown0cba5355
              require ext_code.size(stor54)
              call stor54.generateTokens(address holder, uint256 amount) with:
                   gas gas_remaining wei
                  args caller, ext_call.return_data[0] * _param1 / unknown0cba5355
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require _param1 + unknown0cba5355 >= unknown0cba5355
  unknown0cba5355 += _param1
  log 0xee7ee7a1: unknownd95393ebAddress, _param1, _param1, block.timestamp, unknown2f884710, caller
  require stor1.length + 1 == stor1.length


# hash = 0x381f253c
# getter = None
# const = None
# payable = False
def unknown381f253c(uint256 _param1, bool _param2): # not payable
  require calldata.size - 4 >= 64
  require unknownf6558b00 <= 1
  require unknownf6558b00 == 1
  require not unknown5f88967b
  mem[196 len 64] = 941565244, _param1, Mask(224, 32, _param2) >> 32
  mem[288 len 4] = Mask(32, 64, _param2) >> 64
  [93mdelegate unknown2914af34Address with:
     funct uint32(_param1)
       gas gas_remaining wei
      args Mask(224, 32, _param2) << 224, mem[260 len 4]
  if not return_data.size:
      if delegate.return_code:
          return bool(941565244, Mask(224, 32, _param1) >> 32)
      else:
          return 0
  mem[228 len return_data.size] = ext_call.return_data[0 len return_data.size]
  if not delegate.return_code:
      return 0
  require return_data.size >= 32
  mem[ceil32(return_data.size) + 197] = bool(mem[228])
  return memory
    from ceil32(return_data.size) + 197
     [93mlen 32


# hash = 0x3d981474
# getter = None
# const = None
# payable = False
def unknown3d981474(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if unknown821f9824[addr(_param1)] < unknown2f884710:
      if not unknown821f9824[addr(_param1)]:
          [94midx = 1
          while [94midx < unknown2f884710:
              mem[0] = [94midx
              mem[32] = sha3(addr(_param1), 17)
              if not stor17[addr(_param1)][[94midx]:
                  require 1 <= [94midx
                  mem[100] = _param1
                  mem[132] = unknowna940646d[[94midx - 1]
                  require ext_code.size(stor53)
                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                          gas gas_remaining wei
                         args addr(_param1), unknowna940646d[[94midx - 1]
                  mem[96] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          mem[0] = _param1
                          mem[32] = 19
                          if unknown5825b04c[addr(_param1)]:
                              if unknown5825b04c[addr(_param1)]:
                                  require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] / unknown5825b04c[addr(_param1)] == 216 * 24 * 3600
                                  if unknownbdbcb576[addr(_param1)][[94midx]:
                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / unknownbdbcb576[addr(_param1)][[94midx] == 10^18
                                      require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 0
                                      require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                      if 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 10^18:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = _param1
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args addr(_param1), unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                      else:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = _param1
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args addr(_param1), unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                  else:
                                      require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 0
                                      require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                      if 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 10^18:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = _param1
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args addr(_param1), unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                      else:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = _param1
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args addr(_param1), unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                              else:
                                  require unknownbdbcb576[addr(_param1)][[94midx]
                                  require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / unknownbdbcb576[addr(_param1)][[94midx] != 10^18
                                  revert
                          else:
                              require [94midx + 1 >= [94midx
                              [94midx = [94midx + 1
                              continue 
                      else:
                          if ext_call.return_data[0]:
                              require 216 * 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 216 * 24 * 3600
                              if unknownbdbcb576[addr(_param1)][[94midx]:
                                  require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / unknownbdbcb576[addr(_param1)][[94midx] == 10^18
                                  require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                  require 216 * 24 * 3600 * ext_call.return_data[0]
                                  if 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = _param1
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args addr(_param1), unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                  else:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = _param1
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args addr(_param1), unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                              else:
                                  require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                  require 216 * 24 * 3600 * ext_call.return_data[0]
                                  if 0 / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = _param1
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args addr(_param1), unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                  else:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = _param1
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args addr(_param1), unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                          else:
                              mem[0] = _param1
                              mem[32] = 19
                              if unknown5825b04c[addr(_param1)]:
                                  if ext_call.return_data[0]:
                                      require 216 * 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 216 * 24 * 3600
                                      if unknownbdbcb576[addr(_param1)][[94midx]:
                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / unknownbdbcb576[addr(_param1)][[94midx] == 10^18
                                          require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                          require 216 * 24 * 3600 * ext_call.return_data[0]
                                          if 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = _param1
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args addr(_param1), unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                          else:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = _param1
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args addr(_param1), unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                      else:
                                          require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                          require 216 * 24 * 3600 * ext_call.return_data[0]
                                          if 0 / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = _param1
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args addr(_param1), unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                          else:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = _param1
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args addr(_param1), unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                  else:
                                      require unknownbdbcb576[addr(_param1)][[94midx]
                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / unknownbdbcb576[addr(_param1)][[94midx] != 10^18
                                      revert
                              else:
                                  require [94midx + 1 >= [94midx
                                  [94midx = [94midx + 1
                                  continue 
              else:
                  require [94midx + 1 >= [94midx
                  [94midx = [94midx + 1
                  continue 
      else:
          mem[0] = _param1
          mem[32] = 16
          [94midx = stor[sha3(mem[0 len 64])]
          while [94midx < unknown2f884710:
              mem[0] = [94midx
              mem[32] = sha3(addr(_param1), 17)
              if not stor17[addr(_param1)][[94midx]:
                  require 1 <= [94midx
                  mem[100] = _param1
                  mem[132] = unknowna940646d[[94midx - 1]
                  require ext_code.size(stor53)
                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                          gas gas_remaining wei
                         args addr(_param1), unknowna940646d[[94midx - 1]
                  mem[96] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          mem[0] = _param1
                          mem[32] = 19
                          if unknown5825b04c[addr(_param1)]:
                              if unknown5825b04c[addr(_param1)]:
                                  require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] / unknown5825b04c[addr(_param1)] == 216 * 24 * 3600
                                  if unknownbdbcb576[addr(_param1)][[94midx]:
                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / unknownbdbcb576[addr(_param1)][[94midx] == 10^18
                                      require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 0
                                      require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                      if 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 10^18:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = _param1
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args addr(_param1), unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                      else:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = _param1
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args addr(_param1), unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                  else:
                                      require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 0
                                      require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                      if 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 10^18:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = _param1
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args addr(_param1), unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                      else:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = _param1
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args addr(_param1), unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                              else:
                                  require unknownbdbcb576[addr(_param1)][[94midx]
                                  require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / unknownbdbcb576[addr(_param1)][[94midx] != 10^18
                                  revert
                          else:
                              require [94midx + 1 >= [94midx
                              [94midx = [94midx + 1
                              continue 
                      else:
                          if ext_call.return_data[0]:
                              require 216 * 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 216 * 24 * 3600
                              if unknownbdbcb576[addr(_param1)][[94midx]:
                                  require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / unknownbdbcb576[addr(_param1)][[94midx] == 10^18
                                  require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                  require 216 * 24 * 3600 * ext_call.return_data[0]
                                  if 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = _param1
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args addr(_param1), unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                  else:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = _param1
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args addr(_param1), unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                              else:
                                  require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                  require 216 * 24 * 3600 * ext_call.return_data[0]
                                  if 0 / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = _param1
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args addr(_param1), unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                  else:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = _param1
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args addr(_param1), unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                          else:
                              mem[0] = _param1
                              mem[32] = 19
                              if unknown5825b04c[addr(_param1)]:
                                  if ext_call.return_data[0]:
                                      require 216 * 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 216 * 24 * 3600
                                      if unknownbdbcb576[addr(_param1)][[94midx]:
                                          require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / unknownbdbcb576[addr(_param1)][[94midx] == 10^18
                                          require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                          require 216 * 24 * 3600 * ext_call.return_data[0]
                                          if 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = _param1
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args addr(_param1), unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                          else:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = _param1
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args addr(_param1), unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                      else:
                                          require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                          require 216 * 24 * 3600 * ext_call.return_data[0]
                                          if 0 / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = _param1
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args addr(_param1), unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                          else:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = _param1
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args addr(_param1), unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                  else:
                                      require unknownbdbcb576[addr(_param1)][[94midx]
                                      require 10^18 * unknownbdbcb576[addr(_param1)][[94midx] / unknownbdbcb576[addr(_param1)][[94midx] != 10^18
                                      revert
                              else:
                                  require [94midx + 1 >= [94midx
                                  [94midx = [94midx + 1
                                  continue 
              else:
                  require [94midx + 1 >= [94midx
                  [94midx = [94midx + 1
                  continue 
      return 0
  else:
      return 0


# hash = 0x3eadb6db
# getter = None
# const = None
# payable = False
def unknown3eadb6db(): # not payable
  mem[132 len 0] = None
  [93mdelegate unknown2914af34Address.mem[132 len 4] with:
       gas gas_remaining wei
      args 
  require delegate.return_code


# hash = 0x404c568f
# getter = ['storage', 160, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 21]]], ['cd', 36]]]
# const = None
# payable = False
def unknown404c568f(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  require _param2 < uint256(unknown404c568f[_param1])
  return addr(unknown404c568f[_param1][_param2])


# hash = 0x407fa2a3
# getter = None
# const = None
# payable = False
def unknown407fa2a3(): # not payable
  [94midx = 160
  [94ms = 14
  while 224 > [94midx + 32:
      mem[[94midx + 32] = stor1[[94ms]
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return unknown56f7e7ff.length, mem[192]


# hash = 0x4a393149
# getter = None
# const = None
# payable = False
def onTransfer(address _from, address _to, uint256 _amount): # not payable
  require calldata.size - 4 >= 96
  return 1


# hash = 0x4b25fe92
# getter = None
# const = None
# payable = False
def unknown4b25fe92(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  stor1.length++
  [93mdelegate unknown2914af34Address.0x4b25fe92 with:
       gas gas_remaining wei
      args Mask(224, 32, _param1) >> 32, mem[196 len 4]
  require delegate.return_code
  require stor1.length + 1 == stor1.length


# hash = 0x4cc0fc39
# getter = None
# const = ['return', 3]
# payable = False
const unknown4cc0fc39 = 3


# hash = 0x4f2094a1
# getter = None
# const = ['return', 777600]
# payable = False
const unknown4f2094a1 = (216 * 24 * 3600)


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
  return bool(unknown5f88967b)


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


# hash = 0x7113aef2
# getter = None
# const = None
# payable = False
def unknown7113aef2(uint32 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 128
  require unknownf6558b00 <= 1
  require unknownf6558b00 == 1
  stor1.length++
  [93mdelegate unknown2914af34Address with:
     funct _param1
       gas gas_remaining wei
      args Mask(224, 32, _param2) << 736, mem[388 len 4]
  require delegate.return_code
  require stor1.length + 1 == stor1.length


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
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


# hash = 0x852a89d5
# getter = None
# const = None
# payable = False
def unknown852a89d5(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  if not stor17[addr(_param1)][_param2]:
      require 1 <= _param2
      require ext_code.size(stor53)
      static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
              gas gas_remaining wei
             args addr(_param1), unknowna940646d[_param2 - 1]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              if unknown5825b04c[addr(_param1)]:
                  if unknown5825b04c[addr(_param1)]:
                      require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] / unknown5825b04c[addr(_param1)] == 216 * 24 * 3600
                      if unknownbdbcb576[addr(_param1)][_param2]:
                          require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / unknownbdbcb576[addr(_param1)][_param2] == 10^18
                          require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 0
                          require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                          if 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 10^18:
                              require ext_code.size(stor53)
                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                      gas gas_remaining wei
                                     args unknowna940646d[_param2]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(stor53)
                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                          gas gas_remaining wei
                                         args addr(_param1), unknowna940646d[_param2]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if unknown7cd9fb1c[_param2]:
                                          require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 10^18
                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                              return 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                     (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                          else:
                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                              return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                      else:
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if 0 / ext_call.return_data[0]:
                                              require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                              return 10^18 * 0 / ext_call.return_data[0] / 10^18, 
                                                     (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18)
                                          else:
                                              require 0 <= 0 / ext_call.return_data[0]
                                              return 0, 0 / ext_call.return_data[0]
                          else:
                              require ext_code.size(stor53)
                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                      gas gas_remaining wei
                                     args unknowna940646d[_param2]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(stor53)
                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                          gas gas_remaining wei
                                         args addr(_param1), unknowna940646d[_param2]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if unknown7cd9fb1c[_param2]:
                                          require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                              require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                              require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                              return 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                     (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                          else:
                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                              return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                      else:
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if 0 / ext_call.return_data[0]:
                                              require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                              require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                              return 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18, 
                                                     (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18)
                                          else:
                                              require 0 <= 0 / ext_call.return_data[0]
                                              return 0, 0 / ext_call.return_data[0]
                      else:
                          require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 0
                          require 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                          if 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] > 10^18:
                              require ext_code.size(stor53)
                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                      gas gas_remaining wei
                                     args unknowna940646d[_param2]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(stor53)
                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                          gas gas_remaining wei
                                         args addr(_param1), unknowna940646d[_param2]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if unknown7cd9fb1c[_param2]:
                                          require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 10^18
                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                              return 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                     (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                          else:
                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                              return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                      else:
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if 0 / ext_call.return_data[0]:
                                              require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                              return 10^18 * 0 / ext_call.return_data[0] / 10^18, 
                                                     (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18)
                                          else:
                                              require 0 <= 0 / ext_call.return_data[0]
                                              return 0, 0 / ext_call.return_data[0]
                          else:
                              require ext_code.size(stor53)
                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                      gas gas_remaining wei
                                     args unknowna940646d[_param2]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(stor53)
                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                          gas gas_remaining wei
                                         args addr(_param1), unknowna940646d[_param2]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if unknown7cd9fb1c[_param2]:
                                          require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                              require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                              require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                              return 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                     (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                          else:
                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                              return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                      else:
                                          require ext_call.return_data[0] > 0
                                          require ext_call.return_data[0]
                                          if 0 / ext_call.return_data[0]:
                                              require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)]
                                              require 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                              return 0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18, 
                                                     (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * unknown5825b04c[addr(_param1)] * 0 / ext_call.return_data[0] / 10^18)
                                          else:
                                              require 0 <= 0 / ext_call.return_data[0]
                                              return 0, 0 / ext_call.return_data[0]
                  else:
                      require unknownbdbcb576[addr(_param1)][_param2]
                      require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / unknownbdbcb576[addr(_param1)][_param2] != 10^18
                      revert
              else:
                  return 0
          else:
              if ext_call.return_data[0]:
                  require 216 * 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 216 * 24 * 3600
                  if unknownbdbcb576[addr(_param1)][_param2]:
                      require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / unknownbdbcb576[addr(_param1)][_param2] == 10^18
                      require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                      require 216 * 24 * 3600 * ext_call.return_data[0]
                      if 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                          require ext_code.size(stor53)
                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                  gas gas_remaining wei
                                 args unknowna940646d[_param2]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(stor53)
                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                      gas gas_remaining wei
                                     args addr(_param1), unknowna940646d[_param2]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  if unknown7cd9fb1c[_param2]:
                                      require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 10^18
                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          return 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                 (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                      else:
                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                  else:
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if 0 / ext_call.return_data[0]:
                                          require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                          return 10^18 * 0 / ext_call.return_data[0] / 10^18, 
                                                 (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18)
                                      else:
                                          require 0 <= 0 / ext_call.return_data[0]
                                          return 0, 0 / ext_call.return_data[0]
                      else:
                          require ext_code.size(stor53)
                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                  gas gas_remaining wei
                                 args unknowna940646d[_param2]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(stor53)
                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                      gas gas_remaining wei
                                     args addr(_param1), unknowna940646d[_param2]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  if unknown7cd9fb1c[_param2]:
                                      require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                          require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0]
                                          require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          return 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                 (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                      else:
                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                  else:
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if 0 / ext_call.return_data[0]:
                                          require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0]
                                          require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                          return 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18, 
                                                 (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18)
                                      else:
                                          require 0 <= 0 / ext_call.return_data[0]
                                          return 0, 0 / ext_call.return_data[0]
                  else:
                      require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                      require 216 * 24 * 3600 * ext_call.return_data[0]
                      if 0 / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                          require ext_code.size(stor53)
                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                  gas gas_remaining wei
                                 args unknowna940646d[_param2]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(stor53)
                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                      gas gas_remaining wei
                                     args addr(_param1), unknowna940646d[_param2]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  if unknown7cd9fb1c[_param2]:
                                      require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 10^18
                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          return 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                 (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                      else:
                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                  else:
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if 0 / ext_call.return_data[0]:
                                          require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                          return 10^18 * 0 / ext_call.return_data[0] / 10^18, 
                                                 (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18)
                                      else:
                                          require 0 <= 0 / ext_call.return_data[0]
                                          return 0, 0 / ext_call.return_data[0]
                      else:
                          require ext_code.size(stor53)
                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                  gas gas_remaining wei
                                 args unknowna940646d[_param2]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(stor53)
                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                      gas gas_remaining wei
                                     args addr(_param1), unknowna940646d[_param2]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  if unknown7cd9fb1c[_param2]:
                                      require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                          require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                          require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          return 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                 (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                      else:
                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                  else:
                                      require ext_call.return_data[0] > 0
                                      require ext_call.return_data[0]
                                      if 0 / ext_call.return_data[0]:
                                          require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                          require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                          return 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18, 
                                                 (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18)
                                      else:
                                          require 0 <= 0 / ext_call.return_data[0]
                                          return 0, 0 / ext_call.return_data[0]
              else:
                  if unknown5825b04c[addr(_param1)]:
                      if ext_call.return_data[0]:
                          require 216 * 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 216 * 24 * 3600
                          if unknownbdbcb576[addr(_param1)][_param2]:
                              require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / unknownbdbcb576[addr(_param1)][_param2] == 10^18
                              require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                              require 216 * 24 * 3600 * ext_call.return_data[0]
                              if 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                  require ext_code.size(stor53)
                                  static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                          gas gas_remaining wei
                                         args unknowna940646d[_param2]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(stor53)
                                      static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args addr(_param1), unknowna940646d[_param2]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          if unknown7cd9fb1c[_param2]:
                                              require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                              require ext_call.return_data[0] > 0
                                              require ext_call.return_data[0]
                                              if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                                  require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 10^18
                                                  require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                                  return 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                         (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                              else:
                                                  require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                                  return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          else:
                                              require ext_call.return_data[0] > 0
                                              require ext_call.return_data[0]
                                              if 0 / ext_call.return_data[0]:
                                                  require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                  require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                  return 10^18 * 0 / ext_call.return_data[0] / 10^18, 
                                                         (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18)
                                              else:
                                                  require 0 <= 0 / ext_call.return_data[0]
                                                  return 0, 0 / ext_call.return_data[0]
                              else:
                                  require ext_code.size(stor53)
                                  static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                          gas gas_remaining wei
                                         args unknowna940646d[_param2]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(stor53)
                                      static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args addr(_param1), unknowna940646d[_param2]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          if unknown7cd9fb1c[_param2]:
                                              require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                              require ext_call.return_data[0] > 0
                                              require ext_call.return_data[0]
                                              if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                                  require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                  require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                                  return 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                         (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                              else:
                                                  require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                                  return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          else:
                                              require ext_call.return_data[0] > 0
                                              require ext_call.return_data[0]
                                              if 0 / ext_call.return_data[0]:
                                                  require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                  require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                  return 10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18, 
                                                         (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[addr(_param1)][_param2] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18)
                                              else:
                                                  require 0 <= 0 / ext_call.return_data[0]
                                                  return 0, 0 / ext_call.return_data[0]
                          else:
                              require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                              require 216 * 24 * 3600 * ext_call.return_data[0]
                              if 0 / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                  require ext_code.size(stor53)
                                  static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                          gas gas_remaining wei
                                         args unknowna940646d[_param2]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(stor53)
                                      static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args addr(_param1), unknowna940646d[_param2]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          if unknown7cd9fb1c[_param2]:
                                              require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                              require ext_call.return_data[0] > 0
                                              require ext_call.return_data[0]
                                              if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                                  require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 10^18
                                                  require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                                  return 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                         (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                              else:
                                                  require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                                  return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          else:
                                              require ext_call.return_data[0] > 0
                                              require ext_call.return_data[0]
                                              if 0 / ext_call.return_data[0]:
                                                  require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                  require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                  return 10^18 * 0 / ext_call.return_data[0] / 10^18, 
                                                         (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18)
                                              else:
                                                  require 0 <= 0 / ext_call.return_data[0]
                                                  return 0, 0 / ext_call.return_data[0]
                              else:
                                  require ext_code.size(stor53)
                                  static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                          gas gas_remaining wei
                                         args unknowna940646d[_param2]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_code.size(stor53)
                                      static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args addr(_param1), unknowna940646d[_param2]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          if unknown7cd9fb1c[_param2]:
                                              require ext_call.return_data[0] * unknown7cd9fb1c[_param2] / unknown7cd9fb1c[_param2] == ext_call.return_data[0]
                                              require ext_call.return_data[0] > 0
                                              require ext_call.return_data[0]
                                              if ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]:
                                                  require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                  require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                                  return 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18, 
                                                         (ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0] / 10^18)
                                              else:
                                                  require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                                  return 0, ext_call.return_data[0] * unknown7cd9fb1c[_param2] / ext_call.return_data[0]
                                          else:
                                              require ext_call.return_data[0] > 0
                                              require ext_call.return_data[0]
                                              if 0 / ext_call.return_data[0]:
                                                  require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                  require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                  return 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18, 
                                                         (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18)
                                              else:
                                                  require 0 <= 0 / ext_call.return_data[0]
                                                  return 0, 0 / ext_call.return_data[0]
                      else:
                          require unknownbdbcb576[addr(_param1)][_param2]
                          require 10^18 * unknownbdbcb576[addr(_param1)][_param2] / unknownbdbcb576[addr(_param1)][_param2] != 10^18
                          revert
                  else:
                      return 0
  else:
      return 0


# hash = 0x8606c91a
# getter = None
# const = ['return', 86400]
# payable = False
const unknown8606c91a = (24 * 3600)


# hash = 0x8b14799d
# getter = None
# const = None
# payable = False
def unknown8b14799d(array _param1, array _param2, array _param3): # not payable
  require calldata.size - 4 >= 96
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + (32 * _param1.length) + 36 <= calldata.size
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  require _param2 <= 4294967296
  require _param2 + 36 <= calldata.size
  require _param2.length <= 4294967296 and _param2 + (32 * _param2.length) + 36 <= calldata.size
  mem[(32 * _param1.length) + 128] = _param2.length
  mem[(32 * _param1.length) + 160 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  require _param3 <= 4294967296
  require _param3 + 36 <= calldata.size
  require _param3.length <= 4294967296 and _param3 + (32 * _param3.length) + 36 <= calldata.size
  mem[(32 * _param1.length) + (32 * _param2.length) + 160] = _param3.length
  mem[(32 * _param1.length) + (32 * _param2.length) + 192 len 32 * _param3.length] = call.data[_param3 + 36 len 32 * _param3.length]
  mem[(32 * _param1.length) + (32 * _param2.length) + (32 * _param3.length) + 192] = 0
  require caller == owner
  require not unknownb7ac4ff3
  unknownb7ac4ff3 = 1
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = 25
      stor25[mem[(32 * [94midx) + 140 len 20]] = 1
      require [94midx + 1 >= [94midx
      [94midx = [94midx + 1
      continue 
  [94midx = 0
  while [94midx < _param2.length:
      require [94midx < _param2.length
      mem[0] = mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]
      mem[32] = 26
      stor26[mem[(32 * [94midx) + (32 * _param1.length) + 172 len 20]] = 1
      require [94midx + 1 >= [94midx
      [94midx = [94midx + 1
      continue 
  [94midx = 0
  while [94midx < _param3.length:
      require [94midx < _param3.length
      mem[0] = mem[(32 * [94midx) + (32 * _param1.length) + (32 * _param2.length) + 204 len 20]
      mem[32] = 27
      stor27[mem[(32 * [94midx) + (32 * _param1.length) + (32 * _param2.length) + 204 len 20]] = 1
      require [94midx + 1 >= [94midx
      [94midx = [94midx + 1
      continue 


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
          require ext_call.return_data[0] > 0
          require ext_call.return_data[0]
          if 0 / ext_call.return_data[0] >= 25 * 10^17:
              return (0 / ext_call.return_data[0])
      else:
          require 10^18 * unknown0cba5355 / unknown0cba5355 == 10^18
          require ext_call.return_data[0] > 0
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
  return addr(investmentsCount[_param1][_param2].field_0), 
         investmentsCount[_param1][_param2].field_256,
         investmentsCount[_param1][_param2].field_512,
         investmentsCount[_param1][_param2].field_768,
         investmentsCount[_param1][_param2].field_1024,
         investmentsCount[_param1][_param2].field_1280,
         investmentsCount[_param1][_param2].field_1536,
         investmentsCount[_param1][_param2].field_1792,
         bool(uint8(investmentsCount[_param1][_param2].field_2048))


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


# hash = 0x97107d6d
# getter = None
# const = None
# payable = False
def setProxy(address _proxy): # not payable
  require calldata.size - 4 >= 32
  require caller == owner
  require _proxy
  require not unknowna03040c3Address
  unknowna03040c3Address = _proxy
  stor55 = _proxy


# hash = 0x9a8a2145
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def unknown9a8a2145(): # not payable
  return unknown9a8a2145Address


# hash = 0x9add7438
# getter = None
# const = None
# payable = False
def unknown9add7438(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require unknownf6558b00 <= 1
  require not unknownf6558b00
  stor1.length++
  require ext_code.size(stor54)
  static call stor54.totalSupply() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not _param1:
      require unknown0cba5355 > 0
      require unknown0cba5355
      require ext_code.size(stor54)
      call stor54.destroyTokens(address owner, uint256 amount) with:
           gas gas_remaining wei
          args caller, 0 / unknown0cba5355
  else:
      require ext_call.return_data[0] * _param1 / _param1 == ext_call.return_data[0]
      require unknown0cba5355 > 0
      require unknown0cba5355
      require ext_code.size(stor54)
      call stor54.destroyTokens(address owner, uint256 amount) with:
           gas gas_remaining wei
          args caller, ext_call.return_data[0] * _param1 / unknown0cba5355
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require _param1 <= unknown0cba5355
  unknown0cba5355 -= _param1
  require ext_code.size(stor58)
  call stor58.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  log 0xae96a66b: unknownd95393ebAddress, _param1, _param1, block.timestamp, unknown2f884710, caller
  require stor1.length + 1 == stor1.length


# hash = 0x9c3f1150
# getter = None
# const = None
# payable = False
def unknown9c3f1150(): # not payable
  require unknownf6558b00 <= 1
  if unknownf6558b00 == 1:
      if block.timestamp - unknown25f842c5 % 72 * 24 * 3600 < 24 * 3600:
          return 0
  return 1


# hash = 0xa03040c3
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def unknowna03040c3(): # not payable
  return unknowna03040c3Address


# hash = 0xa6f561ec
# getter = None
# const = None
# payable = False
def unknowna6f561ec(bool _param1): # not payable
  require calldata.size - 4 >= 32
  require unknownf6558b00 <= 1
  require not unknownf6558b00
  stor1.length++
  require unknown2f884710 > unknown821f9824[caller]
  if unknown821f9824[caller] < unknown2f884710:
      if not unknown821f9824[caller]:
          [94midx = 1
          while [94midx < unknown2f884710:
              mem[0] = [94midx
              mem[32] = sha3(caller, 17)
              if not stor17[caller][[94midx]:
                  require 1 <= [94midx
                  mem[100] = caller
                  mem[132] = unknowna940646d[[94midx - 1]
                  require ext_code.size(stor53)
                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                          gas gas_remaining wei
                         args caller, unknowna940646d[[94midx - 1]
                  mem[96] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          mem[0] = caller
                          mem[32] = 19
                          if unknown5825b04c[caller]:
                              if unknown5825b04c[caller]:
                                  require 216 * 24 * 3600 * unknown5825b04c[caller] / unknown5825b04c[caller] == 216 * 24 * 3600
                                  if unknownbdbcb576[caller][[94midx]:
                                      require 10^18 * unknownbdbcb576[caller][[94midx] / unknownbdbcb576[caller][[94midx] == 10^18
                                      require 216 * 24 * 3600 * unknown5825b04c[caller] > 0
                                      require 216 * 24 * 3600 * unknown5825b04c[caller]
                                      if 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] > 10^18:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = caller
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args caller, unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                      else:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = caller
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args caller, unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller]
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller]
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                  else:
                                      require 216 * 24 * 3600 * unknown5825b04c[caller] > 0
                                      require 216 * 24 * 3600 * unknown5825b04c[caller]
                                      if 0 / 216 * 24 * 3600 * unknown5825b04c[caller] > 10^18:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = caller
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args caller, unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                      else:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = caller
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args caller, unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * unknown5825b04c[caller]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * unknown5825b04c[caller]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                              else:
                                  require unknownbdbcb576[caller][[94midx]
                                  require 10^18 * unknownbdbcb576[caller][[94midx] / unknownbdbcb576[caller][[94midx] != 10^18
                                  revert
                          else:
                              require [94midx + 1 >= [94midx
                              [94midx = [94midx + 1
                              continue 
                      else:
                          if ext_call.return_data[0]:
                              require 216 * 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 216 * 24 * 3600
                              if unknownbdbcb576[caller][[94midx]:
                                  require 10^18 * unknownbdbcb576[caller][[94midx] / unknownbdbcb576[caller][[94midx] == 10^18
                                  require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                  require 216 * 24 * 3600 * ext_call.return_data[0]
                                  if 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = caller
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args caller, unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                  else:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = caller
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args caller, unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                              else:
                                  require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                  require 216 * 24 * 3600 * ext_call.return_data[0]
                                  if 0 / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = caller
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args caller, unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                  else:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = caller
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args caller, unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                          else:
                              mem[0] = caller
                              mem[32] = 19
                              if unknown5825b04c[caller]:
                                  if ext_call.return_data[0]:
                                      require 216 * 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 216 * 24 * 3600
                                      if unknownbdbcb576[caller][[94midx]:
                                          require 10^18 * unknownbdbcb576[caller][[94midx] / unknownbdbcb576[caller][[94midx] == 10^18
                                          require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                          require 216 * 24 * 3600 * ext_call.return_data[0]
                                          if 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = caller
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args caller, unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                          else:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = caller
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args caller, unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                      else:
                                          require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                          require 216 * 24 * 3600 * ext_call.return_data[0]
                                          if 0 / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = caller
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args caller, unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                          else:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = caller
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args caller, unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                  else:
                                      require unknownbdbcb576[caller][[94midx]
                                      require 10^18 * unknownbdbcb576[caller][[94midx] / unknownbdbcb576[caller][[94midx] != 10^18
                                      revert
                              else:
                                  require [94midx + 1 >= [94midx
                                  [94midx = [94midx + 1
                                  continue 
              else:
                  require [94midx + 1 >= [94midx
                  [94midx = [94midx + 1
                  continue 
      else:
          mem[0] = caller
          mem[32] = 16
          [94midx = stor[sha3(mem[0 len 64])]
          while [94midx < unknown2f884710:
              mem[0] = [94midx
              mem[32] = sha3(caller, 17)
              if not stor17[caller][[94midx]:
                  require 1 <= [94midx
                  mem[100] = caller
                  mem[132] = unknowna940646d[[94midx - 1]
                  require ext_code.size(stor53)
                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                          gas gas_remaining wei
                         args caller, unknowna940646d[[94midx - 1]
                  mem[96] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          mem[0] = caller
                          mem[32] = 19
                          if unknown5825b04c[caller]:
                              if unknown5825b04c[caller]:
                                  require 216 * 24 * 3600 * unknown5825b04c[caller] / unknown5825b04c[caller] == 216 * 24 * 3600
                                  if unknownbdbcb576[caller][[94midx]:
                                      require 10^18 * unknownbdbcb576[caller][[94midx] / unknownbdbcb576[caller][[94midx] == 10^18
                                      require 216 * 24 * 3600 * unknown5825b04c[caller] > 0
                                      require 216 * 24 * 3600 * unknown5825b04c[caller]
                                      if 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] > 10^18:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = caller
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args caller, unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                      else:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = caller
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args caller, unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller]
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller]
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                  else:
                                      require 216 * 24 * 3600 * unknown5825b04c[caller] > 0
                                      require 216 * 24 * 3600 * unknown5825b04c[caller]
                                      if 0 / 216 * 24 * 3600 * unknown5825b04c[caller] > 10^18:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = caller
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args caller, unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                      else:
                                          require ext_code.size(stor53)
                                          static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args unknowna940646d[[94midx]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[100] = caller
                                              mem[132] = unknowna940646d[[94midx]
                                              require ext_code.size(stor53)
                                              static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args caller, unknowna940646d[[94midx]
                                              mem[96] = ext_call.return_data[0]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[0] = [94midx
                                                  mem[32] = 22
                                                  if unknown7cd9fb1c[[94midx]:
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * unknown5825b04c[caller]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                          require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * unknown5825b04c[caller] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      require ext_call.return_data[0] > 0
                                                      require ext_call.return_data[0]
                                                      if 0 / ext_call.return_data[0]:
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * unknown5825b04c[caller]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                          require 0 / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                          require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * unknown5825b04c[caller] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                                                      else:
                                                          require 0 <= 0 / ext_call.return_data[0]
                                                          require 0 / ext_call.return_data[0] >= 0
                                                          require [94midx + 1 >= [94midx
                                                          [94midx = [94midx + 1
                                                          continue 
                              else:
                                  require unknownbdbcb576[caller][[94midx]
                                  require 10^18 * unknownbdbcb576[caller][[94midx] / unknownbdbcb576[caller][[94midx] != 10^18
                                  revert
                          else:
                              require [94midx + 1 >= [94midx
                              [94midx = [94midx + 1
                              continue 
                      else:
                          if ext_call.return_data[0]:
                              require 216 * 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 216 * 24 * 3600
                              if unknownbdbcb576[caller][[94midx]:
                                  require 10^18 * unknownbdbcb576[caller][[94midx] / unknownbdbcb576[caller][[94midx] == 10^18
                                  require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                  require 216 * 24 * 3600 * ext_call.return_data[0]
                                  if 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = caller
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args caller, unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                  else:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = caller
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args caller, unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                              else:
                                  require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                  require 216 * 24 * 3600 * ext_call.return_data[0]
                                  if 0 / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = caller
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args caller, unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                  else:
                                      require ext_code.size(stor53)
                                      static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                              gas gas_remaining wei
                                             args unknowna940646d[[94midx]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          mem[100] = caller
                                          mem[132] = unknowna940646d[[94midx]
                                          require ext_code.size(stor53)
                                          static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                  gas gas_remaining wei
                                                 args caller, unknowna940646d[[94midx]
                                          mem[96] = ext_call.return_data[0]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 32
                                              mem[0] = [94midx
                                              mem[32] = 22
                                              if unknown7cd9fb1c[[94midx]:
                                                  require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                      require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                      require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                              else:
                                                  require ext_call.return_data[0] > 0
                                                  require ext_call.return_data[0]
                                                  if 0 / ext_call.return_data[0]:
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                      require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                      require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  else:
                                                      require 0 <= 0 / ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      require [94midx + 1 >= [94midx
                                                      [94midx = [94midx + 1
                                                      continue 
                          else:
                              mem[0] = caller
                              mem[32] = 19
                              if unknown5825b04c[caller]:
                                  if ext_call.return_data[0]:
                                      require 216 * 24 * 3600 * ext_call.return_data[0] / ext_call.return_data[0] == 216 * 24 * 3600
                                      if unknownbdbcb576[caller][[94midx]:
                                          require 10^18 * unknownbdbcb576[caller][[94midx] / unknownbdbcb576[caller][[94midx] == 10^18
                                          require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                          require 216 * 24 * 3600 * ext_call.return_data[0]
                                          if 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = caller
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args caller, unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                          else:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = caller
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args caller, unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * unknownbdbcb576[caller][[94midx] / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                      else:
                                          require 216 * 24 * 3600 * ext_call.return_data[0] > 0
                                          require 216 * 24 * 3600 * ext_call.return_data[0]
                                          if 0 / 216 * 24 * 3600 * ext_call.return_data[0] > 10^18:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = caller
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args caller, unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 10^18
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (10^18 * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 10^18 * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 10^18
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 10^18 * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (10^18 * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                          else:
                                              require ext_code.size(stor53)
                                              static call stor53.totalSupplyAt(uint256 blockNumber) with:
                                                      gas gas_remaining wei
                                                     args unknowna940646d[[94midx]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 32
                                                  mem[100] = caller
                                                  mem[132] = unknowna940646d[[94midx]
                                                  require ext_code.size(stor53)
                                                  static call stor53.balanceOfAt(address owner, uint256 blockNumber) with:
                                                          gas gas_remaining wei
                                                         args caller, unknowna940646d[[94midx]
                                                  mem[96] = ext_call.return_data[0]
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  else:
                                                      require return_data.size >= 32
                                                      mem[0] = [94midx
                                                      mem[32] = 22
                                                      if unknown7cd9fb1c[[94midx]:
                                                          require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / unknown7cd9fb1c[[94midx] == ext_call.return_data[0]
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]:
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18 >= 0
                                                              require (ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0]
                                                              require ext_call.return_data[0] * unknown7cd9fb1c[[94midx] / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                      else:
                                                          require ext_call.return_data[0] > 0
                                                          require ext_call.return_data[0]
                                                          if 0 / ext_call.return_data[0]:
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 0 / ext_call.return_data[0] == 0 / 216 * 24 * 3600 * ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 <= 0 / ext_call.return_data[0]
                                                              require 0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18 >= 0
                                                              require (0 / ext_call.return_data[0]) - (0 / 216 * 24 * 3600 * ext_call.return_data[0] * 0 / ext_call.return_data[0] / 10^18) >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                                          else:
                                                              require 0 <= 0 / ext_call.return_data[0]
                                                              require 0 / ext_call.return_data[0] >= 0
                                                              require [94midx + 1 >= [94midx
                                                              [94midx = [94midx + 1
                                                              continue 
                                  else:
                                      require unknownbdbcb576[caller][[94midx]
                                      require 10^18 * unknownbdbcb576[caller][[94midx] / unknownbdbcb576[caller][[94midx] != 10^18
                                      revert
                              else:
                                  require [94midx + 1 >= [94midx
                                  [94midx = [94midx + 1
                                  continue 
              else:
                  require [94midx + 1 >= [94midx
                  [94midx = [94midx + 1
                  continue 
  mem[0] = caller
  mem[32] = 16
  [94midx = stor[sha3(mem[0 len 64])]
  while [94midx < unknown2f884710:
      mem[0] = [94midx
      mem[32] = sha3(caller, 17)
      stor17[caller][[94midx] = 1
      require [94midx + 1 >= [94midx
      [94midx = [94midx + 1
      continue 
  unknown821f9824[caller] = unknown2f884710
  require 0 <= unknownae2f89c2
  require unknown7cd9fb1c[stor9] >= unknown7cd9fb1c[stor9]
  investmentsCount[caller].field_0 = 0
  [94midx = 0
  while 9 * investmentsCount[caller].field_0 > [94midx:
      addr(investmentsCount[caller][[94midx].field_0) = 0
      investmentsCount[caller][[94midx].field_256 = 0
      investmentsCount[caller][[94midx].field_512 = 0
      investmentsCount[caller][[94midx].field_768 = 0
      investmentsCount[caller][[94midx].field_1024 = 0
      investmentsCount[caller][[94midx].field_1280 = 0
      investmentsCount[caller][[94midx].field_1536 = 0
      investmentsCount[caller][[94midx].field_1792 = 0
      uint8(investmentsCount[caller][[94midx].field_2048) = 0
      [94midx = [94midx + 9
      continue 
  uint256(unknown404c568f[caller]) = 0
  [94midx = 0
  while uint256(unknown404c568f[caller]) > [94midx:
      uint256(unknown404c568f[caller][[94midx]) = 0
      [94midx = [94midx + 1
      continue 
  log 0xec530ab7: 0, unknown2f884710, caller
  if not _param1:
      require ext_code.size(stor58)
      call stor58.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args caller, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
  else:
      require ext_code.size(stor54)
      static call stor54.totalSupply() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(stor54)
      if not ext_call.return_data[0]:
          call stor54.generateTokens(address holder, uint256 amount) with:
               gas gas_remaining wei
              args caller, 0
      else:
          if not unknown0cba5355:
              call stor54.generateTokens(address holder, uint256 amount) with:
                   gas gas_remaining wei
                  args caller, 0
          else:
              static call stor54.totalSupply() with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require unknown0cba5355 > 0
              require unknown0cba5355
              require ext_code.size(stor54)
              call stor54.generateTokens(address holder, uint256 amount) with:
                   gas gas_remaining wei
                  args caller, 0 / unknown0cba5355
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require unknown0cba5355 >= unknown0cba5355
      log 0xee7ee7a1: unknownd95393ebAddress, 0, 0, block.timestamp, unknown2f884710, caller
  require stor1.length + 1 == stor1.length


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


# hash = 0xb18e8a8d
# getter = None
# const = None
# payable = False
def unknownb18e8a8d(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require caller == owner
  require _param1
  require _param1 != this.address
  unknownfbf35f46Address = _param1


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


# hash = 0xb4230d1a
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 21]]]
# const = None
# payable = False
def unknownb4230d1a(addr _param1): # not payable
  require calldata.size - 4 >= 32
  return uint256(unknown404c568f[addr(_param1)])


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


# hash = 0xb8fc41ac
# getter = None
# const = None
# payable = False
def unknownb8fc41ac(addr _param1): # not payable
  require calldata.size - 4 >= 32
  stor1.length++
  require bool(unknown5f88967b) == 1
  require unknown56f7e7ff.length + unknown25f842c5 >= unknown25f842c5
  require block.timestamp > unknown56f7e7ff.length + unknown25f842c5
  require _param1
  if _param1 != 0xfe000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:
      require _param1
      require ext_code.size(_param1)
  if 0xfe000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _param1:
      call nextVersionAddress with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  else:
      require ext_code.size(_param1)
      static call _param1.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(_param1)
      call _param1.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args stor28, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
  require stor1.length + 1 == stor1.length


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
  stor1.length++
  mem[132 len 0] = None
  [93mdelegate unknown2914af34Address.mem[132 len 4] with:
       gas gas_remaining wei
      args 
  require delegate.return_code
  require stor1.length + 1 == stor1.length


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
  require 3 <= unknown2f884710
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


# hash = 0xda682aeb
# getter = None
# const = None
# payable = False
def onApprove(address _param1, address _param2, uint256 _param3): # not payable
  require calldata.size - 4 >= 96
  return 1


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
  return bool(unknowndb77839b)


# hash = 0xdc87454c
# getter = ['storage', 160, 8, 2]
# const = None
# payable = False
def unknowndc87454c(): # not payable
  return unknowndc87454cAddress


# hash = 0xe1024b4d
# getter = None
# const = None
# payable = False
def unknowne1024b4d(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require caller == owner
  stor25[addr(_param1)] = 1


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
  require unknownf6558b00 <= 1
  if unknownf6558b00 == 1:
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


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require calldata.size - 4 >= 32
  require caller == owner
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = 0xf48c3054
# getter = None
# const = None
# payable = True
def proxyPayment(address _param1) payable: 
  require calldata.size - 4 >= 32
  return 0


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
  require unknownf6558b00 <= 1
  return unknownf6558b00


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
  stop


