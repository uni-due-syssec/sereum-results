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
def unknown0d48669a(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < munknown0d48669am.length
  return munknown0d48669am[m_param1m]m.field_768


# hash = 0x0dc6f847
# getter = ['storage', 256, 0, ['add', ['mask_shl', 254, 0, 2, ['cd', 4]], ['sha3', 10]]]
# const = None
# payable = False
def unknown0dc6f847(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < munknown0d48669am.length
  return uint256(munknown0d48669am[m_param1m]m.field_0)


# hash = 0x0ea9c984
# getter = None
# const = None
# payable = False
def unknown0ea9c984(): # not payable
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5444000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor4) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor4))
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4352000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor6) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor6))
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5144000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor5) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor5))
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor7) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor7))
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5446000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor8) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor8))
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.tokenAddress() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor9) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor9))
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5443000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor3) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor3))


# hash = 0x0ead3e72
# getter = None
# const = None
# payable = True
def unknown0ead3e72(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  require m_param1
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isPause() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      revert with 0, 'Emergency Pause Applied'
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x5154000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      require ext_code.size(addr(mstor5))
      static call addr(mstor5).0xde75b5ea with:
              gas gas_remaining wei
             args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require not ext_call.return_data[0]
      require ext_code.size(munknowna0b2d57fAddress)
      static call munknowna0b2d57fAddress.isMember(address param1) with:
              gas gas_remaining wei
             args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require not ext_call.return_data[0]
      require ext_code.size(addr(mstor4))
      static call addr(mstor4).0x6eeeaaa5 with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require call.value == ext_call.return_data[0]
      require ext_code.size(addr(mstor5))
      call addr(mstor5).0xf63a87d4 with:
           gas gas_remaining wei
          args addr(m_param1), 1
  else:
      require ext_code.size(addr(mstor4))
      static call addr(mstor4).walletAddress() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[12 len 20]:
          revert with 0, 'No walletAddress present'
      require ext_code.size(addr(munknowneaf2c477Address))
      call addr(munknowneaf2c477Address).addToWhitelist(address user) with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require 2 < munknown0d48669am.length
      require not uint8(munknown0d48669am[9m]m[addr(m_param1)m]m.field_0)
      require 2 < munknown0d48669am.length
      require uint256(munknown0d48669am.field_2048) + 1 >= uint256(munknown0d48669am.field_2048)
      require 2 < munknown0d48669am.length
      uint256(munknown0d48669am.field_2048)++
      uint8(munknown0d48669am[9m]m[addr(m_param1)m]m.field_0) = 1
      uint256(munknown0d48669am.field_2560)++
      mstor[('array', 10, ('name', 'unknown0d48669a', 10)) + uint256(munknown0d48669am.field_2560)m]m.field_0 = m_param1
      require ext_code.size(addr(mstor4))
      static call addr(mstor4).walletAddress() with:
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
  return addr(mtkAddress)


# hash = 0x22ce7254
# getter = None
# const = None
# payable = False
def unknown22ce7254(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(mmasterAddress)
  static call mmasterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return (ext_call.return_data[12 len 20] == m_param1)


# hash = 0x2dc4bdca
# getter = None
# const = None
# payable = False
def unknown2dc4bdca(uint256 m_param1, array m_param2, addr m_param3): # not payable
  require calldata.size - 4 >= 96
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + m_param2.length + 36 <= calldata.size
  mem[128 len m_param2.length] = m_param2[allm]
  mem[m_param2.length + 128] = 0
  require ext_code.size(mmasterAddress)
  static call mmasterAddress.0x1382858 with:
          gas gas_remaining wei
         args 0x4756000000000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, 'Not authorized'
  mem[ceil32(m_param2.length) + 128] = m_param1
  mem[ceil32(m_param2.length) + 224 len ceil32(m_param2.length)] = m_param2[allm], mem[m_param2.length + 128 len ceil32(m_param2.length) - m_param2.length]
  if not m_param2.length % 32:
      log 0xe2981862: 0, Mask(224, 0, _param1), 64, _param2.length, Mask(8 * _param2.length, -(8 * _param2.length) + 256, _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]) << (8 * _param2.length) - 256, unknown0d48669a.length
  else:
      mem[floor32(m_param2.length) + ceil32(m_param2.length) + 224] = mem[floor32(m_param2.length) + ceil32(m_param2.length) + -(m_param2.length % 32) + 256 len m_param2.length % 32]
      log 0xe2981862: 0, Mask(224, 0, _param1), 64, _param2.length, Mask(8 * ceil32(_param2.length), -(8 * ceil32(_param2.length)) + 256, _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]) << (8 * ceil32(_param2.length)) - 256, mem[(2 * ceil32(_param2.length)) + 224 len floor32(_param2.length) + -ceil32(_param2.length) + 32], unknown0d48669a.length
  munknown0d48669am.length++
  uint256(munknown0d48669am[munknown0d48669am.lengthm]m.field_0) = 0
  mstorC65Am[mstor10m.lengthm] = 0
  [94midx = 0
  mwhile mstorC65Am[mstor10m.lengthm] > [94midxm:
      mstor[[94midx + sha3((4 * mstor10m.length) - 0x39a5844729cae3e308f36a5ce933956d7c6367997d26743ca06a70b77c062d56)m] = 0
      [94midx = [94midx + 1
      mcontinue 
  mstorC65Am[mstor10m.lengthm] = m_param3


# hash = 0x2f473021
# getter = None
# const = None
# payable = False
def unknown2f473021(addr m_param1, uint256 m_param2, bool m_param3): # not payable
  require calldata.size - 4 >= 96
  require m_param2 < munknown0d48669am.length
  if munknown0d48669am[m_param2m]m.field_768:
      require m_param2 < munknown0d48669am.length
      require caller == munknown0d48669am[m_param2m]m.field_768
  else:
      require ext_code.size(mmasterAddress)
      static call mmasterAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4756000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          revert with 0, 'Not Authorized'
  require m_param2 < munknown0d48669am.length
  if not m_param3:
      require uint8(mstor[(4 * m_param2) + ('name', 'unknown0d48669a', 10) + 1m]m[addr(m_param1)m]m.field_0)
      require m_param2 < munknown0d48669am.length
      require 1 <= uint256(munknown0d48669am[m_param2m]m.field_0)
      require m_param2 < munknown0d48669am.length
      uint256(munknown0d48669am[m_param2m]m.field_0)--
      uint8(mstor[(4 * m_param2) + ('name', 'unknown0d48669a', 10) + 1m]m[addr(m_param1)m]m.field_0) = 0
  else:
      require not uint8(mstor[(4 * m_param2) + ('name', 'unknown0d48669a', 10) + 1m]m[addr(m_param1)m]m.field_0)
      require m_param2 < munknown0d48669am.length
      require uint256(munknown0d48669am[m_param2m]m.field_0) + 1 >= uint256(munknown0d48669am[m_param2m]m.field_0)
      require m_param2 < munknown0d48669am.length
      uint256(munknown0d48669am[m_param2m]m.field_0)++
      uint8(mstor[('name', 'unknown0d48669a', 10) + (4 * m_param2) + 1m]m[addr(m_param1)m]m.field_0) = 1
      uint256(munknown0d48669am[m_param2m]m.field_512)++
      mstor[sha3(('name', 'unknown0d48669a', 10) + (4 * m_param2) + 2) + uint256(munknown0d48669am[m_param2m]m.field_512)m]m.field_0 = m_param1


# hash = 0x37f15a58
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def unknown37f15a58(): # not payable
  return munknown37f15a58


# hash = 0x505ef22f
# getter = None
# const = None
# payable = False
def unknown505ef22f(addr m_param1, uint256 m_param2): # not payable
  require calldata.size - 4 >= 64
  if m_param2:
      require m_param2 < munknown0d48669am.length
      if not uint8(mstor[(4 * m_param2) + ('name', 'unknown0d48669a', 10) + 1m]m[addr(m_param1)m]m.field_0):
          return 0
  return 1


# hash = 0x5daf08ca
# getter = None
# const = None
# payable = False
def members(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < munknown0d48669am.length
  if uint256(munknown0d48669am[m_param1m]m.field_0):
      mem[128 len 32 * uint256(munknown0d48669am[m_param1m]m.field_0)] = code.data[12571 len 32 * uint256(munknown0d48669am[m_param1m]m.field_0)]
  [94midx = 0
  mwhile [94midx < uint256(munknown0d48669am[m_param1m]m.field_512)m:
      require m_param1 < munknown0d48669am.length
      require [94midx < uint256(munknown0d48669am[m_param1m]m.field_512)
      require m_param1 < munknown0d48669am.length
      mem[0] = mstor[sha3((4 * m_param1) + ('name', 'unknown0d48669a', 10) + 2) + [94midxm]m.field_0
      mem[32] = (4 * m_param1) + sha3(10) + 1
      if uint8(mstor[(4 * m_param1) + ('name', 'unknown0d48669a', 10) + 1m]m[mstor[sha3((4 * m_param1) + ('name', 'unknown0d48669a', 10) + 2) + [94midxm]m.field_0m]m.field_0):
          [94ms = 0
          mwhile [94ms < uint256(munknown0d48669am[m_param1m]m.field_0)m:
              require [94ms < uint256(munknown0d48669am[m_param1m]m.field_0)
              if mem[(32 * [94ms) + 140 len 20] != mstor[sha3((4 * m_param1) + ('name', 'unknown0d48669a', 10) + 2) + [94midxm]m.field_0:
                  [94ms = [94ms + 1
                  mcontinue 
              [94midx = [94midx + 1
              mcontinue 
          require 0 < uint256(munknown0d48669am[m_param1m]m.field_0)
          mem[128] = mstor[sha3((4 * m_param1) + ('name', 'unknown0d48669a', 10) + 2) + [94midxm]m.field_0
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * uint256(munknown0d48669am[m_param1m]m.field_0)) + 224 len floor32(uint256(munknown0d48669am[m_param1m]m.field_0))] = mem[128 len floor32(uint256(munknown0d48669am[m_param1m]m.field_0))]
  return m_param1, 
         Array(len=uint256(munknown0d48669am[m_param1m]m.field_0), data=mem[128 len floor32(uint256(munknown0d48669am[m_param1m]m.field_0))], mem[(32 * uint256(munknown0d48669am[m_param1m]m.field_0)) + floor32(uint256(munknown0d48669am[m_param1m]m.field_0)) + 224 len (32 * uint256(munknown0d48669am[m_param1m]m.field_0)) - floor32(uint256(munknown0d48669am[m_param1m]m.field_0))])


# hash = 0x648edd9c
# getter = None
# const = None
# payable = False
def unknown648edd9c(): # not payable
  require calldata.size - 4 >= 32
  require cd[4] <= 4294967296
  require cd[4] + 36 <= calldata.size
  require m('cd', 4).length <= 4294967296 and cd[4] + (32 * m('cd', 4).length) + 36 <= calldata.size
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isOwner(address addr) with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0xc15041d5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require 1 < munknown0d48669am.length
  require m('cd', 4).length + uint256(munknown0d48669am.field_1024) >= uint256(munknown0d48669am.field_1024)
  require munknown37f15a58 >= m('cd', 4).length + uint256(munknown0d48669am.field_1024)
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      require 2 < munknown0d48669am.length
      require uint8(munknown0d48669am[9m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m.field_0)
      require [94midx < m('cd', 4).length
      require 1 < munknown0d48669am.length
      require not uint8(munknown0d48669am[5m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m.field_0)
      require 1 < munknown0d48669am.length
      require uint256(munknown0d48669am.field_1024) + 1 >= uint256(munknown0d48669am.field_1024)
      require 1 < munknown0d48669am.length
      uint256(munknown0d48669am.field_1024)++
      mem[32] = sha3(10) + 5
      uint8(munknown0d48669am[5m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m.field_0) = 1
      uint256(munknown0d48669am.field_1536)++
      mem[0] = sha3(10) + 6
      mstor[('array', 6, ('name', 'unknown0d48669a', 10)) + uint256(munknown0d48669am.field_1536)m]m.field_0 = addr(cd[((32 * [94midx) + cd[4] + 36)])
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x6d1c31d2
# getter = None
# const = None
# payable = False
def unknown6d1c31d2(): # not payable
  if munknown0d48669am.length:
      mem[128 len 32 * munknown0d48669am.length] = code.data[12571 len 32 * munknown0d48669am.length]
  [94midx = 0
  mwhile [94midx < munknown0d48669am.lengthm:
      mem[0] = 10
      require [94midx < munknown0d48669am.length
      mem[(32 * [94midx) + 128] = uint256(munknown0d48669am[[94midxm]m.field_0)
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * munknown0d48669am.length) + 128] = 32
  mem[(32 * munknown0d48669am.length) + 160] = munknown0d48669am.length
  [94ms = 0
  mwhile munknown0d48669am.length < 32 * munknown0d48669am.lengthm:
      mem[(34 * munknown0d48669am.length) + 192] = mem[munknown0d48669am.length + 128]
      [94ms = munknown0d48669am.length + 32
      mcontinue 
  return memory
    from (32 * munknown0d48669am.length) + 128
     [93mlen (96 * munknown0d48669am.length) + 64


# hash = 0x6eb4b91f
# getter = None
# const = None
# payable = False
def unknown6eb4b91f(array m_param1, array m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isOwner(address addr) with:
          gas gas_remaining wei
         args caller
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require not mlaunched
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      [94m_36 = mem[(32 * [94midx) + 128]
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = mem[(32 * [94midx) + 140 len 20]
      require ext_code.size(munknowna0b2d57fAddress)
      static call munknowna0b2d57fAddress.isMember(address param1) with:
              gas gas_remaining wei
             args addr([94m_36)
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require not ext_call.return_data[0]
      require [94midx < m_param1.length
      [94m_42 = mem[(32 * [94midx) + 128]
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0xe43252d700000000000000000000000000000000000000000000000000000000
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = addr([94m_42)
      require ext_code.size(addr(munknowneaf2c477Address))
      call addr(munknowneaf2c477Address).addToWhitelist(address user) with:
           gas gas_remaining wei
          args addr([94m_42)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require [94midx < m_param1.length
      require 2 < munknown0d48669am.length
      require not uint8(munknown0d48669am[9m]m[mem[(32 * [94midx) + 140 len 20]m]m.field_0)
      require 2 < munknown0d48669am.length
      require uint256(munknown0d48669am.field_2048) + 1 >= uint256(munknown0d48669am.field_2048)
      require 2 < munknown0d48669am.length
      uint256(munknown0d48669am.field_2048)++
      mem[32] = sha3(10) + 9
      uint8(munknown0d48669am[9m]m[addr(mem[(32 * [94midx) + 128])m]m.field_0) = 1
      uint256(munknown0d48669am.field_2560)++
      mem[0] = sha3(10) + 10
      mstor[('array', 10, ('name', 'unknown0d48669a', 10)) + uint256(munknown0d48669am.field_2560)m]m.field_0 = mem[(32 * [94midx) + 140 len 20]
      require [94midx < m_param1.length
      [94m_56 = mem[(32 * [94midx) + 128]
      require [94midx < m_param2.length
      [94m_58 = mem[(32 * [94midx) + (32 * m_param1.length) + 160]
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0x40c10f1900000000000000000000000000000000000000000000000000000000
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = addr([94m_56)
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = [94m_58
      require ext_code.size(addr(munknowneaf2c477Address))
      call addr(munknowneaf2c477Address).mint(address to, uint256 value) with:
           gas gas_remaining wei
          args addr([94m_56), [94m_58
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      mcontinue 
  mlaunched = 1
  munknowndf05eef5 = block.timestamp


# hash = 0x790e118c
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def unknown790e118c(): # not payable
  return munknown0d48669am.length


# hash = 0x8091f3bf
# getter = ['bool', ['storage', 8, 0, 13]]
# const = None
# payable = False
def launched(): # not payable
  return bool(mlaunched)


# hash = 0x8f8c0094
# getter = None
# const = None
# payable = False
def unknown8f8c0094(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.0x8f16c41c with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknown37f15a58 = m_param1


# hash = 0x90a79368
# getter = None
# const = None
# payable = False
def unknown90a79368(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require caller == munknowna0b2d57fAddress
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.owner() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require 3 < munknown0d48669am.length
  require uint8(munknown0d48669am[13m]m[addr(ext_call.return_data[0])m]m.field_0)
  require 3 < munknown0d48669am.length
  require 1 <= uint256(munknown0d48669am.field_3072)
  require 3 < munknown0d48669am.length
  uint256(munknown0d48669am.field_3072)--
  uint8(munknown0d48669am[13m]m[addr(ext_call.return_data[0])m]m.field_0) = 0
  require 3 < munknown0d48669am.length
  require not uint8(munknown0d48669am[13m]m[addr(m_param1)m]m.field_0)
  require 3 < munknown0d48669am.length
  require uint256(munknown0d48669am.field_3072) + 1 >= uint256(munknown0d48669am.field_3072)
  require 3 < munknown0d48669am.length
  uint256(munknown0d48669am.field_3072)++
  uint8(munknown0d48669am[13m]m[addr(m_param1)m]m.field_0) = 1
  uint256(munknown0d48669am.field_3584)++
  mstor[('array', 14, ('name', 'unknown0d48669a', 10)) + uint256(munknown0d48669am.field_3584)m]m.field_0 = m_param1


# hash = 0x99374642
# getter = None
# const = None
# payable = False
def roles(address m_param1): # not payable
  require calldata.size - 4 >= 32
  if munknown0d48669am.length:
      mem[128 len 32 * munknown0d48669am.length] = code.data[12571 len 32 * munknown0d48669am.length]
  [94midx = 1
  [94ms = 0
  mwhile [94midx < munknown0d48669am.lengthm:
      mem[0] = m_param1
      mem[32] = (4 * [94midx) + sha3(10) + 1
      if not uint8(mstor[(4 * [94midx) + ('name', 'unknown0d48669a', 10) + 1m]m[addr(m_param1)m]m.field_0):
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      require [94ms < munknown0d48669am.length
      mem[(32 * [94ms) + 128] = [94midx
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * munknown0d48669am.length) + 192 len floor32(munknown0d48669am.length)] = mem[128 len floor32(munknown0d48669am.length)]
  return Array(len=munknown0d48669am.length, data=mem[128 len floor32(munknown0d48669am.length)], mem[(32 * munknown0d48669am.length) + floor32(munknown0d48669am.length) + 192 len (32 * munknown0d48669am.length) - floor32(munknown0d48669am.length)]), 


# hash = 0xa0b2d57f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def unknowna0b2d57f(): # not payable
  return munknowna0b2d57fAddress


# hash = 0xaa561f9d
# getter = None
# const = None
# payable = False
def unknownaa561f9d(uint256 m_param1, addr m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param1 < munknown0d48669am.length
  if munknown0d48669am[m_param1m]m.field_768:
      require m_param1 < munknown0d48669am.length
      require caller == munknown0d48669am[m_param1m]m.field_768
  else:
      require ext_code.size(mmasterAddress)
      static call mmasterAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4756000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          revert with 0, 'Not Authorized'
  require m_param1 < munknown0d48669am.length
  munknown0d48669am[m_param1m]m.field_768 = m_param2


# hash = 0xae393df9
# getter = None
# const = None
# payable = False
def unknownae393df9(): # not payable
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isPause() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isMember(address param1) with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(munknowneaf2c477Address))
  static call addr(munknowneaf2c477Address).0x39081b92 with:
          gas gas_remaining wei
         args caller, block.timestamp
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(mstor8))
  static call addr(mstor8).0xac5adaf6 with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(mstor6))
  static call addr(mstor6).0x35afb14e with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(mstor7))
  call addr(mstor7).0xf0466c73 with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(mtkAddress))
  static call addr(mtkAddress).balanceOf(address owner) with:
          gas gas_remaining wei
         args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(munknowneaf2c477Address))
  call addr(munknowneaf2c477Address).burnFrom(address from, uint256 value) with:
       gas gas_remaining wei
      args caller, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require 2 < munknown0d48669am.length
  require uint8(munknown0d48669am[9m]m[callerm]m.field_0)
  require 2 < munknown0d48669am.length
  require 1 <= uint256(munknown0d48669am.field_2048)
  require 2 < munknown0d48669am.length
  uint256(munknown0d48669am.field_2048)--
  uint8(munknown0d48669am[9m]m[callerm]m.field_0) = 0
  require ext_code.size(addr(munknowneaf2c477Address))
  call addr(munknowneaf2c477Address).removeFromWhitelist(address user) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xc578f230
# getter = None
# const = None
# payable = False
def unknownc578f230(addr m_param1, addr m_param2): # not payable
  require calldata.size - 4 >= 64
  require 1 < munknown0d48669am.length
  if addr(munknown0d48669am.field_1792):
      require 1 < munknown0d48669am.length
      require caller == addr(munknown0d48669am.field_1792)
  else:
      require ext_code.size(mmasterAddress)
      static call mmasterAddress.0x1382858 with:
              gas gas_remaining wei
             args 0x4756000000000000000000000000000000000000000000000000000000000000
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          revert with 0, 'Not Authorized'
  require 1 < munknown0d48669am.length
  require not uint8(munknown0d48669am[5m]m[addr(m_param1)m]m.field_0)
  require 1 < munknown0d48669am.length
  require uint256(munknown0d48669am.field_1024) + 1 >= uint256(munknown0d48669am.field_1024)
  require 1 < munknown0d48669am.length
  uint256(munknown0d48669am.field_1024)++
  uint8(munknown0d48669am[5m]m[addr(m_param1)m]m.field_0) = 1
  uint256(munknown0d48669am.field_1536)++
  mstor[('array', 6, ('name', 'unknown0d48669a', 10)) + uint256(munknown0d48669am.field_1536)m]m.field_0 = m_param1
  require 1 < munknown0d48669am.length
  require uint8(munknown0d48669am[5m]m[addr(m_param2)m]m.field_0)
  require 1 < munknown0d48669am.length
  require 1 <= uint256(munknown0d48669am.field_1024)
  require 1 < munknown0d48669am.length
  uint256(munknown0d48669am.field_1024)--
  uint8(munknown0d48669am[5m]m[addr(m_param2)m]m.field_0) = 0


# hash = 0xd365a08e
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def masterAddress(): # not payable
  return mmasterAddress


# hash = 0xd46655f4
# getter = None
# const = None
# payable = False
def unknownd46655f4(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  if mmasterAddress:
      require caller == mmasterAddress
  mmasterAddress = m_param1
  munknowna0b2d57fAddress = m_param1
  munknownf17a3becAddress = m_param1


# hash = 0xd8b2114e
# getter = None
# const = None
# payable = False
def unknownd8b2114e(addr m_param1, bool m_param2): # not payable
  require calldata.size - 4 >= 64
  require ext_code.size(addr(mstor5))
  static call addr(mstor5).0x84434b9f with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require caller == ext_call.return_data[12 len 20]
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isPause() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require m_param1
  require ext_code.size(munknowna0b2d57fAddress)
  static call munknowna0b2d57fAddress.isMember(address param1) with:
          gas gas_remaining wei
         args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(addr(mstor5))
  static call addr(mstor5).0xde75b5ea with:
          gas gas_remaining wei
         args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(mstor5))
  call addr(mstor5).0xf63a87d4 with:
       gas gas_remaining wei
      args addr(m_param1), 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(mstor4))
  static call addr(mstor4).0x6eeeaaa5 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not m_param2:
      call m_param1 with:
         value ext_call.return_data[0] wei
           gas 2300 * is_zero(value) wei
  else:
      require ext_code.size(addr(munknowneaf2c477Address))
      call addr(munknowneaf2c477Address).addToWhitelist(address user) with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require 2 < munknown0d48669am.length
      require not uint8(munknown0d48669am[9m]m[addr(m_param1)m]m.field_0)
      require 2 < munknown0d48669am.length
      require uint256(munknown0d48669am.field_2048) + 1 >= uint256(munknown0d48669am.field_2048)
      require 2 < munknown0d48669am.length
      uint256(munknown0d48669am.field_2048)++
      uint8(munknown0d48669am[9m]m[addr(m_param1)m]m.field_0) = 1
      uint256(munknown0d48669am.field_2560)++
      mstor[('array', 10, ('name', 'unknown0d48669a', 10)) + uint256(munknown0d48669am.field_2560)m]m.field_0 = m_param1
      require ext_code.size(addr(mstor4))
      static call addr(mstor4).walletAddress() with:
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
  return munknowndf05eef5


# hash = 0xeaf2c477
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def unknowneaf2c477(): # not payable
  return addr(munknowneaf2c477Address)


# hash = 0xf17a3bec
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknownf17a3bec(): # not payable
  return munknownf17a3becAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


