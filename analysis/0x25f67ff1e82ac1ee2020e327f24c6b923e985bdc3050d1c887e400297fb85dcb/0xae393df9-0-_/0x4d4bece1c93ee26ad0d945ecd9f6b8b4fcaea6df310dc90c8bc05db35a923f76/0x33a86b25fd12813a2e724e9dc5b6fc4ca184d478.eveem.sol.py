# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x33a86B25Fd12813a2E724e9Dc5B6Fc4Ca184D478 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x1b5c6ded': 'unknown1b5c6ded(?)'} 

# storage definitions
def storage:
    # storage address 0
    masterAddress # mask: a s
    # storage address 1
    unknowna0b2d57fAddress # mask: a s
    # storage address 2
    unknownf17a3becAddress # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 3
    unknowneaf2c477Address # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 9
    tkAddress # mask: a s
    # storage address 10
    unknown0d48669a
    # storage address 12
    unknown37f15a58 # mask: a s
    # storage address 13
    launched # mask: a s
    # storage address 14
    unknowndf05eef5 # mask: a s
    # storage address 89717814153306320011181716697424560163256864414616650038987186496166826726058
    stor89717814153306320011181716697424560163256864414616650038987186496166826726058
    # storage address 89717814153306320011181716697424560163256864414616650038987186496166826726059
    stor89717814153306320011181716697424560163256864414616650038987186496166826726059
# hash = 0x0d48669a
# getter = ['storage', 160, 0, ['add', 3, ['mask_shl', 254, 0, 2, ['cd', 4]], ['sha3', 10]]]
# const = None
# payable = False
def unknown0d48669a(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < unknown0d48669a.length
  return unknown0d48669a[_param1].field_768


# hash = 0x0dc6f847
# getter = ['storage', 256, 0, ['add', ['mask_shl', 254, 0, 2, ['cd', 4]], ['sha3', 10]]]
# const = None
# payable = False
def unknown0dc6f847(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < unknown0d48669a.length
  return uint256(unknown0d48669a[_param1].field_0)


# hash = 0x0ea9c984
# getter = None
# const = None
# payable = False
def unknown0ea9c984(): # not payable
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5444000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor4) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor4))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4352000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor6) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor6))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5144000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor5) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor5))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor7) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor7))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5446000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor8) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor8))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.tokenAddress() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor9) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor9))
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5443000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(stor3) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(stor3))


# hash = 0x0ead3e72
# getter = None
# const = None
# payable = True
def unknown0ead3e72(addr _param1) payable: 
  require calldata.size - 4 >= 32
  require _param1
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.isPause() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      revert with 0, 'Emergency Pause Applied'
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5154000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      require ext_code.size(addr(stor5))
      static call addr(stor5).0xde75b5ea with:
              gas gas_remaining wei
             args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require not ext_call.return_data[0]
      require ext_code.size(unknowna0b2d57fAddress)
      static call unknowna0b2d57fAddress.isMember(address param1) with:
              gas gas_remaining wei
             args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require not ext_call.return_data[0]
      require ext_code.size(addr(stor4))
      static call addr(stor4).0x6eeeaaa5 with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require call.value == ext_call.return_data[0]
      require ext_code.size(addr(stor5))
      call addr(stor5).0xf63a87d4 with:
           gas gas_remaining wei
          args addr(_param1), 1
  else:
      require ext_code.size(addr(stor4))
      static call addr(stor4).walletAddress() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[12 len 20]:
          revert with 0, 'No walletAddress present'
      require ext_code.size(addr(unknowneaf2c477Address))
      call addr(unknowneaf2c477Address).addToWhitelist(address user) with:
           gas gas_remaining wei
          args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require 2 < unknown0d48669a.length
      require not uint8(unknown0d48669a[9][addr(_param1)].field_0)
      require 2 < unknown0d48669a.length
      require uint256(unknown0d48669a.field_2048) + 1 >= uint256(unknown0d48669a.field_2048)
      require 2 < unknown0d48669a.length
      uint256(unknown0d48669a.field_2048)++
      uint8(unknown0d48669a[9][addr(_param1)].field_0) = 1
      uint256(unknown0d48669a.field_2560)++
      stor[('array', 10, ('name', 'unknown0d48669a', 10)) + uint256(unknown0d48669a.field_2560)].field_0 = _param1
      require ext_code.size(addr(stor4))
      static call addr(stor4).walletAddress() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      call ext_call.return_data[12 len 20] with:
         value call.value wei
           gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x21f408be
# getter = ['storage', 160, 0, 9]
# const = None
# payable = False
def tk(): # not payable
  return addr(tkAddress)


# hash = 0x22ce7254
# getter = None
# const = None
# payable = False
def unknown22ce7254(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(masterAddress)
  static call masterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return (ext_call.return_data[12 len 20] == _param1)


# hash = 0x2dc4bdca
# getter = None
# const = None
# payable = False
def unknown2dc4bdca(uint256 _param1, array _param2, addr _param3): # not payable
  require calldata.size - 4 >= 96
  require _param2 <= 4294967296
  require _param2 + 36 <= calldata.size
  require _param2.length <= 4294967296 and _param2 + _param2.length + 36 <= calldata.size
  mem[128 len _param2.length] = _param2[all]
  mem[_param2.length + 128] = 0
  require ext_code.size(masterAddress)
  static call masterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, 'Not authorized'
  mem[ceil32(_param2.length) + 128] = _param1
  mem[ceil32(_param2.length) + 224 len ceil32(_param2.length)] = _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]
  if not _param2.length % 32:
      log 0xe2981862: 0, Mask(224, 0, _param1), 64, _param2.length, Mask(8 * _param2.length, -(8 * _param2.length) + 256, _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]) << (8 * _param2.length) - 256, unknown0d48669a.length
  else:
      mem[floor32(_param2.length) + ceil32(_param2.length) + 224] = mem[floor32(_param2.length) + ceil32(_param2.length) + -(_param2.length % 32) + 256 len _param2.length % 32]
      log 0xe2981862: 0, Mask(224, 0, _param1), 64, _param2.length, Mask(8 * ceil32(_param2.length), -(8 * ceil32(_param2.length)) + 256, _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]) << (8 * ceil32(_param2.length)) - 256, mem[(2 * ceil32(_param2.length)) + 224 len floor32(_param2.length) + -ceil32(_param2.length) + 32], unknown0d48669a.length
  unknown0d48669a.length++
  uint256(unknown0d48669a[unknown0d48669a.length].field_0) = 0
  storC65A[stor10.length] = 0
  [94midx = 0
  while storC65A[stor10.length] > [94midx:
      stor[[94midx + sha3((4 * stor10.length) - 0x39a5844729cae3e308f36a5ce933956d7c6367997d26743ca06a70b77c062d56)] = 0
      [94midx = [94midx + 1
      continue 
  storC65A[stor10.length] = _param3


# hash = 0x2f473021
# getter = None
# const = None
# payable = False
def unknown2f473021(addr _param1, uint256 _param2, bool _param3): # not payable
  require calldata.size - 4 >= 96
  require _param2 < unknown0d48669a.length
  if unknown0d48669a[_param2].field_768:
      require _param2 < unknown0d48669a.length
      require caller == unknown0d48669a[_param2].field_768
  else:
      require ext_code.size(masterAddress)
      static call masterAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4756000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          revert with 0, 'Not Authorized'
  require _param2 < unknown0d48669a.length
  if not _param3:
      require uint8(stor[(4 * _param2) + ('name', 'unknown0d48669a', 10) + 1][addr(_param1)].field_0)
      require _param2 < unknown0d48669a.length
      require 1 <= uint256(unknown0d48669a[_param2].field_0)
      require _param2 < unknown0d48669a.length
      uint256(unknown0d48669a[_param2].field_0)--
      uint8(stor[(4 * _param2) + ('name', 'unknown0d48669a', 10) + 1][addr(_param1)].field_0) = 0
  else:
      require not uint8(stor[(4 * _param2) + ('name', 'unknown0d48669a', 10) + 1][addr(_param1)].field_0)
      require _param2 < unknown0d48669a.length
      require uint256(unknown0d48669a[_param2].field_0) + 1 >= uint256(unknown0d48669a[_param2].field_0)
      require _param2 < unknown0d48669a.length
      uint256(unknown0d48669a[_param2].field_0)++
      uint8(stor[('name', 'unknown0d48669a', 10) + (4 * _param2) + 1][addr(_param1)].field_0) = 1
      uint256(unknown0d48669a[_param2].field_512)++
      stor[sha3(('name', 'unknown0d48669a', 10) + (4 * _param2) + 2) + uint256(unknown0d48669a[_param2].field_512)].field_0 = _param1


# hash = 0x37f15a58
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknown37f15a58(): # not payable
  return unknown37f15a58


# hash = 0x505ef22f
# getter = None
# const = None
# payable = False
def unknown505ef22f(addr _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  if _param2:
      require _param2 < unknown0d48669a.length
      if not uint8(stor[(4 * _param2) + ('name', 'unknown0d48669a', 10) + 1][addr(_param1)].field_0):
          return 0
  return 1


# hash = 0x5daf08ca
# getter = None
# const = None
# payable = False
def members(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 < unknown0d48669a.length
  if uint256(unknown0d48669a[_param1].field_0):
      mem[128 len 32 * uint256(unknown0d48669a[_param1].field_0)] = code.data[12571 len 32 * uint256(unknown0d48669a[_param1].field_0)]
  [94midx = 0
  while [94midx < uint256(unknown0d48669a[_param1].field_512):
      require _param1 < unknown0d48669a.length
      require [94midx < uint256(unknown0d48669a[_param1].field_512)
      require _param1 < unknown0d48669a.length
      mem[0] = stor[sha3((4 * _param1) + ('name', 'unknown0d48669a', 10) + 2) + [94midx].field_0
      mem[32] = (4 * _param1) + sha3(10) + 1
      if uint8(stor[(4 * _param1) + ('name', 'unknown0d48669a', 10) + 1][stor[sha3((4 * _param1) + ('name', 'unknown0d48669a', 10) + 2) + [94midx].field_0].field_0):
          [94ms = 0
          while [94ms < uint256(unknown0d48669a[_param1].field_0):
              require [94ms < uint256(unknown0d48669a[_param1].field_0)
              if mem[(32 * [94ms) + 140 len 20] != stor[sha3((4 * _param1) + ('name', 'unknown0d48669a', 10) + 2) + [94midx].field_0:
                  [94ms = [94ms + 1
                  continue 
              [94midx = [94midx + 1
              continue 
          require 0 < uint256(unknown0d48669a[_param1].field_0)
          mem[128] = stor[sha3((4 * _param1) + ('name', 'unknown0d48669a', 10) + 2) + [94midx].field_0
      [94midx = [94midx + 1
      continue 
  mem[(32 * uint256(unknown0d48669a[_param1].field_0)) + 224 len floor32(uint256(unknown0d48669a[_param1].field_0))] = mem[128 len floor32(uint256(unknown0d48669a[_param1].field_0))]
  return _param1, 
         Array(len=uint256(unknown0d48669a[_param1].field_0), data=mem[128 len floor32(uint256(unknown0d48669a[_param1].field_0))], mem[(32 * uint256(unknown0d48669a[_param1].field_0)) + floor32(uint256(unknown0d48669a[_param1].field_0)) + 224 len (32 * uint256(unknown0d48669a[_param1].field_0)) - floor32(uint256(unknown0d48669a[_param1].field_0))])


# hash = 0x648edd9c
# getter = None
# const = None
# payable = False
def unknown648edd9c(): # not payable
  require calldata.size - 4 >= 32
  require cd[4] <= 4294967296
  require cd[4] + 36 <= calldata.size
  require ('cd', 4).length <= 4294967296 and cd[4] + (32 * ('cd', 4).length) + 36 <= calldata.size
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.isOwner(address addr) with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0xc15041d5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require 1 < unknown0d48669a.length
  require ('cd', 4).length + uint256(unknown0d48669a.field_1024) >= uint256(unknown0d48669a.field_1024)
  require unknown37f15a58 >= ('cd', 4).length + uint256(unknown0d48669a.field_1024)
  [94midx = 0
  while [94midx < ('cd', 4).length:
      require 2 < unknown0d48669a.length
      require uint8(unknown0d48669a[9][addr(cd[((32 * [94midx) + cd[4] + 36)])].field_0)
      require [94midx < ('cd', 4).length
      require 1 < unknown0d48669a.length
      require not uint8(unknown0d48669a[5][addr(cd[((32 * [94midx) + cd[4] + 36)])].field_0)
      require 1 < unknown0d48669a.length
      require uint256(unknown0d48669a.field_1024) + 1 >= uint256(unknown0d48669a.field_1024)
      require 1 < unknown0d48669a.length
      uint256(unknown0d48669a.field_1024)++
      mem[32] = sha3(10) + 5
      uint8(unknown0d48669a[5][addr(cd[((32 * [94midx) + cd[4] + 36)])].field_0) = 1
      uint256(unknown0d48669a.field_1536)++
      mem[0] = sha3(10) + 6
      stor[('array', 6, ('name', 'unknown0d48669a', 10)) + uint256(unknown0d48669a.field_1536)].field_0 = addr(cd[((32 * [94midx) + cd[4] + 36)])
      [94midx = [94midx + 1
      continue 


# hash = 0x6d1c31d2
# getter = None
# const = None
# payable = False
def unknown6d1c31d2(): # not payable
  if unknown0d48669a.length:
      mem[128 len 32 * unknown0d48669a.length] = code.data[12571 len 32 * unknown0d48669a.length]
  [94midx = 0
  while [94midx < unknown0d48669a.length:
      mem[0] = 10
      require [94midx < unknown0d48669a.length
      mem[(32 * [94midx) + 128] = uint256(unknown0d48669a[[94midx].field_0)
      [94midx = [94midx + 1
      continue 
  mem[(32 * unknown0d48669a.length) + 128] = 32
  mem[(32 * unknown0d48669a.length) + 160] = unknown0d48669a.length
  [94ms = 0
  while unknown0d48669a.length < 32 * unknown0d48669a.length:
      mem[(34 * unknown0d48669a.length) + 192] = mem[unknown0d48669a.length + 128]
      [94ms = unknown0d48669a.length + 32
      continue 
  return memory
    from (32 * unknown0d48669a.length) + 128
     [93mlen (96 * unknown0d48669a.length) + 64


# hash = 0x6eb4b91f
# getter = None
# const = None
# payable = False
def unknown6eb4b91f(array _param1, array _param2): # not payable
  require calldata.size - 4 >= 64
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + (32 * _param1.length) + 36 <= calldata.size
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  require _param2 <= 4294967296
  require _param2 + 36 <= calldata.size
  require _param2.length <= 4294967296 and _param2 + (32 * _param2.length) + 36 <= calldata.size
  mem[(32 * _param1.length) + 128] = _param2.length
  mem[(32 * _param1.length) + 160 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  mem[(32 * _param1.length) + (32 * _param2.length) + 164] = caller
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.isOwner(address addr) with:
          gas gas_remaining wei
         args caller
  mem[(32 * _param1.length) + (32 * _param2.length) + 160] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require not launched
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      [94m_36 = mem[(32 * [94midx) + 128]
      mem[(32 * _param1.length) + (32 * _param2.length) + 164] = mem[(32 * [94midx) + 140 len 20]
      require ext_code.size(unknowna0b2d57fAddress)
      static call unknowna0b2d57fAddress.isMember(address param1) with:
              gas gas_remaining wei
             args addr([94m_36)
      mem[(32 * _param1.length) + (32 * _param2.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require not ext_call.return_data[0]
      require [94midx < _param1.length
      [94m_42 = mem[(32 * [94midx) + 128]
      mem[(32 * _param1.length) + (32 * _param2.length) + 160] = 0xe43252d700000000000000000000000000000000000000000000000000000000
      mem[(32 * _param1.length) + (32 * _param2.length) + 164] = addr([94m_42)
      require ext_code.size(addr(unknowneaf2c477Address))
      call addr(unknowneaf2c477Address).addToWhitelist(address user) with:
           gas gas_remaining wei
          args addr([94m_42)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require [94midx < _param1.length
      require 2 < unknown0d48669a.length
      require not uint8(unknown0d48669a[9][mem[(32 * [94midx) + 140 len 20]].field_0)
      require 2 < unknown0d48669a.length
      require uint256(unknown0d48669a.field_2048) + 1 >= uint256(unknown0d48669a.field_2048)
      require 2 < unknown0d48669a.length
      uint256(unknown0d48669a.field_2048)++
      mem[32] = sha3(10) + 9
      uint8(unknown0d48669a[9][addr(mem[(32 * [94midx) + 128])].field_0) = 1
      uint256(unknown0d48669a.field_2560)++
      mem[0] = sha3(10) + 10
      stor[('array', 10, ('name', 'unknown0d48669a', 10)) + uint256(unknown0d48669a.field_2560)].field_0 = mem[(32 * [94midx) + 140 len 20]
      require [94midx < _param1.length
      [94m_56 = mem[(32 * [94midx) + 128]
      require [94midx < _param2.length
      [94m_58 = mem[(32 * [94midx) + (32 * _param1.length) + 160]
      mem[(32 * _param1.length) + (32 * _param2.length) + 160] = 0x40c10f1900000000000000000000000000000000000000000000000000000000
      mem[(32 * _param1.length) + (32 * _param2.length) + 164] = addr([94m_56)
      mem[(32 * _param1.length) + (32 * _param2.length) + 196] = [94m_58
      require ext_code.size(addr(unknowneaf2c477Address))
      call addr(unknowneaf2c477Address).mint(address to, uint256 value) with:
           gas gas_remaining wei
          args addr([94m_56), [94m_58
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 
  launched = 1
  unknowndf05eef5 = block.timestamp


# hash = 0x790e118c
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknown790e118c(): # not payable
  return unknown0d48669a.length


# hash = 0x8091f3bf
# getter = ['bool', ['storage', 8, 0, 13]]
# const = None
# payable = False
def launched(): # not payable
  return bool(launched)


# hash = 0x8f8c0094
# getter = None
# const = None
# payable = False
def unknown8f8c0094(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  unknown37f15a58 = _param1


# hash = 0x90a79368
# getter = None
# const = None
# payable = False
def unknown90a79368(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require caller == unknowna0b2d57fAddress
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.owner() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require 3 < unknown0d48669a.length
  require uint8(unknown0d48669a[13][addr(ext_call.return_data[0])].field_0)
  require 3 < unknown0d48669a.length
  require 1 <= uint256(unknown0d48669a.field_3072)
  require 3 < unknown0d48669a.length
  uint256(unknown0d48669a.field_3072)--
  uint8(unknown0d48669a[13][addr(ext_call.return_data[0])].field_0) = 0
  require 3 < unknown0d48669a.length
  require not uint8(unknown0d48669a[13][addr(_param1)].field_0)
  require 3 < unknown0d48669a.length
  require uint256(unknown0d48669a.field_3072) + 1 >= uint256(unknown0d48669a.field_3072)
  require 3 < unknown0d48669a.length
  uint256(unknown0d48669a.field_3072)++
  uint8(unknown0d48669a[13][addr(_param1)].field_0) = 1
  uint256(unknown0d48669a.field_3584)++
  stor[('array', 14, ('name', 'unknown0d48669a', 10)) + uint256(unknown0d48669a.field_3584)].field_0 = _param1


# hash = 0x99374642
# getter = None
# const = None
# payable = False
def roles(address _param1): # not payable
  require calldata.size - 4 >= 32
  if unknown0d48669a.length:
      mem[128 len 32 * unknown0d48669a.length] = code.data[12571 len 32 * unknown0d48669a.length]
  [94midx = 1
  [94ms = 0
  while [94midx < unknown0d48669a.length:
      mem[0] = _param1
      mem[32] = (4 * [94midx) + sha3(10) + 1
      if not uint8(stor[(4 * [94midx) + ('name', 'unknown0d48669a', 10) + 1][addr(_param1)].field_0):
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      require [94ms < unknown0d48669a.length
      mem[(32 * [94ms) + 128] = [94midx
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  mem[(32 * unknown0d48669a.length) + 192 len floor32(unknown0d48669a.length)] = mem[128 len floor32(unknown0d48669a.length)]
  return Array(len=unknown0d48669a.length, data=mem[128 len floor32(unknown0d48669a.length)], mem[(32 * unknown0d48669a.length) + floor32(unknown0d48669a.length) + 192 len (32 * unknown0d48669a.length) - floor32(unknown0d48669a.length)]), 


# hash = 0xa0b2d57f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknowna0b2d57f(): # not payable
  return unknowna0b2d57fAddress


# hash = 0xaa561f9d
# getter = None
# const = None
# payable = False
def unknownaa561f9d(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  require _param1 < unknown0d48669a.length
  if unknown0d48669a[_param1].field_768:
      require _param1 < unknown0d48669a.length
      require caller == unknown0d48669a[_param1].field_768
  else:
      require ext_code.size(masterAddress)
      static call masterAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4756000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          revert with 0, 'Not Authorized'
  require _param1 < unknown0d48669a.length
  unknown0d48669a[_param1].field_768 = _param2


# hash = 0xae393df9
# getter = None
# const = None
# payable = False
def unknownae393df9(): # not payable
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.isPause() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.isMember(address param1) with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(unknowneaf2c477Address))
  static call addr(unknowneaf2c477Address).0x39081b92 with:
          gas gas_remaining wei
         args caller, block.timestamp
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(stor8))
  static call addr(stor8).0xac5adaf6 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(stor6))
  static call addr(stor6).0x35afb14e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(stor7))
  call addr(stor7).0xf0466c73 with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(tkAddress))
  static call addr(tkAddress).balanceOf(address owner) with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(unknowneaf2c477Address))
  call addr(unknowneaf2c477Address).burnFrom(address from, uint256 value) with:
       gas gas_remaining wei
      args caller, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require 2 < unknown0d48669a.length
  require uint8(unknown0d48669a[9][caller].field_0)
  require 2 < unknown0d48669a.length
  require 1 <= uint256(unknown0d48669a.field_2048)
  require 2 < unknown0d48669a.length
  uint256(unknown0d48669a.field_2048)--
  uint8(unknown0d48669a[9][caller].field_0) = 0
  require ext_code.size(addr(unknowneaf2c477Address))
  call addr(unknowneaf2c477Address).removeFromWhitelist(address user) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xc578f230
# getter = None
# const = None
# payable = False
def unknownc578f230(addr _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  require 1 < unknown0d48669a.length
  if addr(unknown0d48669a.field_1792):
      require 1 < unknown0d48669a.length
      require caller == addr(unknown0d48669a.field_1792)
  else:
      require ext_code.size(masterAddress)
      static call masterAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4756000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          revert with 0, 'Not Authorized'
  require 1 < unknown0d48669a.length
  require not uint8(unknown0d48669a[5][addr(_param1)].field_0)
  require 1 < unknown0d48669a.length
  require uint256(unknown0d48669a.field_1024) + 1 >= uint256(unknown0d48669a.field_1024)
  require 1 < unknown0d48669a.length
  uint256(unknown0d48669a.field_1024)++
  uint8(unknown0d48669a[5][addr(_param1)].field_0) = 1
  uint256(unknown0d48669a.field_1536)++
  stor[('array', 6, ('name', 'unknown0d48669a', 10)) + uint256(unknown0d48669a.field_1536)].field_0 = _param1
  require 1 < unknown0d48669a.length
  require uint8(unknown0d48669a[5][addr(_param2)].field_0)
  require 1 < unknown0d48669a.length
  require 1 <= uint256(unknown0d48669a.field_1024)
  require 1 < unknown0d48669a.length
  uint256(unknown0d48669a.field_1024)--
  uint8(unknown0d48669a[5][addr(_param2)].field_0) = 0


# hash = 0xd365a08e
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def masterAddress(): # not payable
  return masterAddress


# hash = 0xd46655f4
# getter = None
# const = None
# payable = False
def unknownd46655f4(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if masterAddress:
      require caller == masterAddress
  masterAddress = _param1
  unknowna0b2d57fAddress = _param1
  unknownf17a3becAddress = _param1


# hash = 0xd8b2114e
# getter = None
# const = None
# payable = False
def unknownd8b2114e(addr _param1, bool _param2): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(addr(stor5))
  static call addr(stor5).0x84434b9f with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require caller == ext_call.return_data[12 len 20]
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.isPause() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require _param1
  require ext_code.size(unknowna0b2d57fAddress)
  static call unknowna0b2d57fAddress.isMember(address param1) with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(stor5))
  static call addr(stor5).0xde75b5ea with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(stor5))
  call addr(stor5).0xf63a87d4 with:
       gas gas_remaining wei
      args addr(_param1), 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(stor4))
  static call addr(stor4).0x6eeeaaa5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not _param2:
      call _param1 with:
         value ext_call.return_data[0] wei
           gas 2300 * is_zero(value) wei
  else:
      require ext_code.size(addr(unknowneaf2c477Address))
      call addr(unknowneaf2c477Address).addToWhitelist(address user) with:
           gas gas_remaining wei
          args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require 2 < unknown0d48669a.length
      require not uint8(unknown0d48669a[9][addr(_param1)].field_0)
      require 2 < unknown0d48669a.length
      require uint256(unknown0d48669a.field_2048) + 1 >= uint256(unknown0d48669a.field_2048)
      require 2 < unknown0d48669a.length
      uint256(unknown0d48669a.field_2048)++
      uint8(unknown0d48669a[9][addr(_param1)].field_0) = 1
      uint256(unknown0d48669a.field_2560)++
      stor[('array', 10, ('name', 'unknown0d48669a', 10)) + uint256(unknown0d48669a.field_2560)].field_0 = _param1
      require ext_code.size(addr(stor4))
      static call addr(stor4).walletAddress() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      call ext_call.return_data[12 len 20] with:
         value ext_call.return_data[0] wei
           gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xdf05eef5
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def unknowndf05eef5(): # not payable
  return unknowndf05eef5


# hash = 0xeaf2c477
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknowneaf2c477(): # not payable
  return addr(unknowneaf2c477Address)


# hash = 0xf17a3bec
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknownf17a3bec(): # not payable
  return unknownf17a3becAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


