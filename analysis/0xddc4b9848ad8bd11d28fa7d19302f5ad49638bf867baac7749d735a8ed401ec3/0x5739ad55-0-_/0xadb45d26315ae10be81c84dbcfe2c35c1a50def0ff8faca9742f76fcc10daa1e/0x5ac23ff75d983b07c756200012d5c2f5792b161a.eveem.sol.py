# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x5Ac23ff75D983b07C756200012D5C2F5792b161A 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0xb00d4ec5': 'unknownb00d4ec5(?)'} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    unknown8aec6a26 # mask: a s
    # storage address 8
    unknown15b4477e
    # storage address 9
    unknown21c8bd88
    # storage address 10
    unknown0731630e
    # storage address 11
    unknown5d7fab15
    # storage address 12
    stor12
    # storage address 13
    stor13
    # storage address 14
    stor14 # mask: a s
    # storage address 15
    unknownd95bb468
    # storage address 16
    unknown707f5432
    # storage address 17
    unknown575cfa73
    # storage address 18
    stor18 # mask: a s
    # storage address 18
    stor18 # mask: a s
    # storage address 19
    unknown19d23303Address # mask: a s
# hash = 0x0731630e
# getter = ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 36]], ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 10]]]]]
# const = None
# payable = True
def unknown0731630e(uint8 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  return munknown0731630em[m_param1 << 248m]m[m_param2 << 248m]


# hash = 0x0c11930b
# getter = None
# const = None
# payable = True
def unknown0c11930b(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  mstor14 = m_param1


# hash = 0x0c5d0b48
# getter = None
# const = None
# payable = True
def unknown0c5d0b48(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  uint8(mstor5m.field_8) = m_param1


# hash = 0x15b4477e
# getter = ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 8]]]
# const = None
# payable = True
def unknown15b4477e(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown15b4477em[m_param1 << 248m]


# hash = 0x19d23303
# getter = ['storage', 160, 0, 19]
# const = None
# payable = True
def unknown19d23303() payable: 
  return munknown19d23303Address


# hash = 0x1cadc34c
# getter = None
# const = None
# payable = True
def unknown1cadc34c(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  uint8(mstor4m.field_24) = m_param1


# hash = 0x1cea8e0a
# getter = None
# const = None
# payable = True
def unknown1cea8e0a(uint8 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param2 > 0
  require m_param2 <= mstor3
  munknown21c8bd88m[m_param1 << 248m] = m_param2


# hash = 0x20b14189
# getter = None
# const = ['return', 1]
# payable = True
const unknown20b14189 = 1


# hash = 0x21c8bd88
# getter = ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 9]]]
# const = None
# payable = True
def unknown21c8bd88(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown21c8bd88m[m_param1 << 248m]


# hash = 0x322ddff2
# getter = None
# const = None
# payable = True
def unknown322ddff2(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 < uint8(mstor4m.field_16)
  uint8(mstor6m.field_40) = m_param1


# hash = 0x47560ae8
# getter = None
# const = None
# payable = True
def unknown47560ae8(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  uint8(mstor6m.field_24) = m_param1


# hash = 0x53fbd66d
# getter = None
# const = None
# payable = True
def unknown53fbd66d(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  uint8(mstor4m.field_16) = m_param1


# hash = 0x575cfa73
# getter = ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 17]]]
# const = None
# payable = True
def unknown575cfa73(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown575cfa73m[m_param1 << 248m]


# hash = 0x57eec461
# getter = None
# const = None
# payable = True
def unknown57eec461() payable: 
  return mstor14, uint8(mstor18m.field_0), uint8(mstor18m.field_8)


# hash = 0x5d4a6d81
# getter = None
# const = None
# payable = True
def unknown5d4a6d81(uint8 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param2 > 0
  require m_param2 <= mstor3
  munknown5d7fab15m[m_param1 << 248m] = m_param2


# hash = 0x5d7fab15
# getter = ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 11]]]
# const = None
# payable = True
def unknown5d7fab15(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown5d7fab15m[m_param1 << 248m]


# hash = 0x6331b55d
# getter = None
# const = None
# payable = True
def unknown6331b55d(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 < uint8(mstor4m.field_16)
  uint8(mstor5m.field_16) = m_param1


# hash = 0x651e9d28
# getter = None
# const = None
# payable = True
def unknown651e9d28(uint8 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param2 > 0
  require m_param2 <= mstor3
  munknown707f5432m[m_param1 << 248m] = m_param2


# hash = 0x707f5432
# getter = ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 16]]]
# const = None
# payable = True
def unknown707f5432(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown707f5432m[m_param1 << 248m]


# hash = 0x70b5f5c6
# getter = None
# const = None
# payable = True
def unknown70b5f5c6(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  require 11 <= mstor2
  require mstor1^10
  require mstor1
  require mstor3
  require mstor3^2
  require mstor3
  require mstor3^3
  require mstor3
  require 3 <= mstor2
  require mstor1^2
  require mstor1
  require mstor3
  require mstor3^2
  require mstor3
  require mstor3^3
  require mstor3
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^3 % mstor3) != 3:
      return (uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^3 % mstor3) == 3)
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^2 % mstor3) >= uint8(mstor4m.field_24):
      return (uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^2 % mstor3) < uint8(mstor4m.field_24))
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3 % mstor3) >= uint8(mstor4m.field_16):
      return (uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3 % mstor3) < uint8(mstor4m.field_16))
  if uint8(uint32(m_param1 / mstor1^2 % mstor1) / mstor3^2 % mstor3) >= mstor14:
      return (uint8(uint32(m_param1 / mstor1^2 % mstor1) / mstor3^2 % mstor3) < mstor14)
  if uint8(uint32(m_param1 / mstor1^2 % mstor1) / mstor3^3 % mstor3) >= munknownd95bb468m[uint32(m_param1 / mstor1^2 % mstor1) / mstor3^2 % mstor3 << 248m]:
      return (uint8(uint32(m_param1 / mstor1^2 % mstor1) / mstor3^3 % mstor3) < munknownd95bb468m[uint32(m_param1 / mstor1^2 % mstor1) / mstor3^2 % mstor3 << 248m])
  if uint8(uint32(m_param1 / mstor1^2 % mstor1) / mstor3 % mstor3) >= munknown707f5432m[uint32(m_param1 / mstor1^2 % mstor1) / mstor3^2 % mstor3 << 248m]:
      return (uint8(uint32(m_param1 / mstor1^2 % mstor1) / mstor3 % mstor3) < munknown707f5432m[uint32(m_param1 / mstor1^2 % mstor1) / mstor3^2 % mstor3 << 248m])
  return (uint8(uint32(m_param1 / mstor1^2 % mstor1) % mstor3) < munknown575cfa73m[uint32(m_param1 / mstor1^2 % mstor1) / mstor3^2 % mstor3 << 248m])


# hash = 0x715018a6
# getter = None
# const = None
# payable = True
def renounceOwnership() payable: 
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x7ef80059
# getter = None
# const = None
# payable = True
def unknown7ef80059(uint8 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param2 > 0
  require m_param2 <= mstor3
  munknown575cfa73m[m_param1 << 248m] = m_param2


# hash = 0x837bfd4d
# getter = None
# const = None
# payable = True
def unknown837bfd4d(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  uint8(mstor6m.field_0) = m_param1


# hash = 0x894fe335
# getter = None
# const = None
# payable = True
def unknown894fe335(uint256 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  require 11 <= mstor2
  require mstor1^10
  require mstor1
  require mstor3
  require mstor3^2
  require mstor3
  require mstor3^3
  require mstor3
  require 8 <= mstor2
  require mstor1^7
  require mstor1
  require mstor3
  require mstor3^2
  require mstor3
  require mstor3^3
  require mstor3
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^3 % mstor3):
      return not bool(uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^3 % mstor3))
  if m_param2 >= uint8(mstor4m.field_0):
      return (m_param2 < uint8(mstor4m.field_0))
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^2 % mstor3) >= uint8(mstor4m.field_24):
      return (uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^2 % mstor3) < uint8(mstor4m.field_24))
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3 % mstor3) >= uint8(mstor4m.field_16):
      return (uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3 % mstor3) < uint8(mstor4m.field_16))
  if uint8(uint32(m_param1 / mstor1^7 % mstor1) / mstor3^2 % mstor3) >= uint8(mstor5m.field_0):
      return (uint8(uint32(m_param1 / mstor1^7 % mstor1) / mstor3^2 % mstor3) < uint8(mstor5m.field_0))
  return (uint8(uint32(m_param1 / mstor1^7 % mstor1) / mstor3 % mstor3) < uint8(mstor5m.field_8))


# hash = 0x8aec6a26
# getter = ['storage', 8, 0, 7]
# const = None
# payable = True
def unknown8aec6a26() payable: 
  return munknown8aec6a26


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def owner() payable: 
  return mowner


# hash = 0x91926664
# getter = None
# const = None
# payable = True
def unknown91926664() payable: 
  return uint8(mstor6m.field_0), 
         uint8(mstor6m.field_0),
         uint8(mstor6m.field_0),
         uint8(mstor6m.field_0),
         uint8(mstor6m.field_32),
         uint8(mstor6m.field_0),
         uint8(mstor6m.field_48)


# hash = 0x92559d13
# getter = None
# const = None
# payable = True
def unknown92559d13(uint8 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param2 > 0
  require m_param2 <= mstor3
  munknown575cfa73m[m_param1 << 248m] = m_param2


# hash = 0x95157b62
# getter = None
# const = None
# payable = True
def unknown95157b62(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 < uint8(mstor4m.field_16)
  uint8(mstor6m.field_48) = m_param1


# hash = 0xa8912657
# getter = None
# const = None
# payable = True
def unknowna8912657(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 < uint8(mstor4m.field_16)
  uint8(mstor18m.field_8) = m_param1


# hash = 0xacea7bc7
# getter = None
# const = None
# payable = True
def unknownacea7bc7(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  munknown8aec6a26 = m_param1


# hash = 0xb1cad7a6
# getter = None
# const = None
# payable = True
def unknownb1cad7a6(uint256 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  require 11 <= mstor2
  require mstor1^10
  require mstor1
  require mstor3
  require mstor3^2
  require mstor3
  require mstor3^3
  require mstor3
  require 10 <= mstor2
  require mstor1^9
  require mstor1
  require mstor3
  require mstor3^2
  require mstor3
  require mstor3^3
  require mstor3
  require 9 <= mstor2
  require mstor1^8
  require mstor1
  require mstor3^3
  require mstor3
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^3 % mstor3) != 1:
      return (1 == uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^3 % mstor3))
  if m_param2 >= uint8(mstor4m.field_0):
      return (m_param2 < uint8(mstor4m.field_0))
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^2 % mstor3) >= uint8(mstor4m.field_24):
      return (uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^2 % mstor3) < uint8(mstor4m.field_24))
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3 % mstor3) >= uint8(mstor4m.field_16):
      return (uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3 % mstor3) < uint8(mstor4m.field_16))
  if uint8(uint32(m_param1 / mstor1^9 % mstor1) / mstor3^3 % mstor3) >= uint8(mstor6m.field_32):
      return (uint8(uint32(m_param1 / mstor1^9 % mstor1) / mstor3^3 % mstor3) < uint8(mstor6m.field_32))
  if uint8(uint32(m_param1 / mstor1^9 % mstor1) / mstor3^2 % mstor3) >= uint8(mstor6m.field_0):
      return (uint8(uint32(m_param1 / mstor1^9 % mstor1) / mstor3^2 % mstor3) < uint8(mstor6m.field_0))
  if uint8(uint32(m_param1 / mstor1^9 % mstor1) / mstor3 % mstor3) >= uint8(mstor6m.field_8):
      return (uint8(uint32(m_param1 / mstor1^9 % mstor1) / mstor3 % mstor3) < uint8(mstor6m.field_8))
  if uint8(uint32(m_param1 / mstor1^9 % mstor1) % mstor3) >= uint8(mstor6m.field_16):
      return (uint8(uint32(m_param1 / mstor1^9 % mstor1) % mstor3) < uint8(mstor6m.field_16))
  return (uint8(uint32(m_param1 / mstor1^8 % mstor1) / mstor3^3 % mstor3) < uint8(mstor6m.field_24))


# hash = 0xb2206f34
# getter = None
# const = None
# payable = True
def unknownb2206f34(uint8 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param2 < uint8(mstor4m.field_16)
  mstor13m[m_param1 << 248m] = m_param2


# hash = 0xb3958790
# getter = None
# const = None
# payable = True
def unknownb3958790() payable: 
  return uint8(mstor5m.field_0), uint8(mstor5m.field_0), uint8(mstor5m.field_0), uint8(mstor5m.field_24)


# hash = 0xbf003178
# getter = None
# const = None
# payable = True
def unknownbf003178(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  uint8(mstor4m.field_0) = m_param1


# hash = 0xd03133e8
# getter = None
# const = None
# payable = True
def unknownd03133e8(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 < uint8(mstor4m.field_16)
  uint8(mstor5m.field_24) = m_param1


# hash = 0xd040d536
# getter = None
# const = None
# payable = True
def unknownd040d536(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  if not m_param1:
      revert with 0, 'invalid argument'
  if this.address == m_param1:
      revert with 0, 'invalid argument'
  munknown19d23303Address = m_param1


# hash = 0xd4545fe6
# getter = None
# const = None
# payable = True
def unknownd4545fe6(uint8 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param2 < uint8(mstor4m.field_16)
  mstor12m[m_param1 << 248m] = m_param2


# hash = 0xd8589690
# getter = None
# const = None
# payable = True
def unknownd8589690(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 < uint8(mstor4m.field_16)
  uint8(mstor18m.field_0) = m_param1


# hash = 0xd95bb468
# getter = ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 8, 0, 248, ['cd', 4]], 15]]]
# const = None
# payable = True
def unknownd95bb468(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknownd95bb468m[m_param1 << 248m]


# hash = 0xddb9ea17
# getter = None
# const = None
# payable = True
def unknownddb9ea17(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  uint8(mstor6m.field_8) = m_param1


# hash = 0xe7d53e23
# getter = None
# const = None
# payable = True
def unknowne7d53e23(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  uint8(mstor4m.field_8) = m_param1


# hash = 0xe85946df
# getter = None
# const = None
# payable = True
def unknowne85946df(uint8 m_param1, uint8 m_param2, uint8 m_param3) payable: 
  require calldata.size - 4 >= 96
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param3 > 0
  require m_param3 <= mstor3
  munknown0731630em[m_param1 << 248m]m[m_param2 << 248m] = m_param3


# hash = 0xedcdfeac
# getter = None
# const = None
# payable = True
def unknownedcdfeac(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  uint8(mstor5m.field_0) = m_param1


# hash = 0xf031251b
# getter = None
# const = None
# payable = True
def unknownf031251b(uint8 m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param1 > 0
  require m_param1 <= mstor3
  uint8(mstor6m.field_16) = m_param1


# hash = 0xf1d6b88d
# getter = None
# const = None
# payable = True
def unknownf1d6b88d() payable: 
  return uint8(mstor4m.field_0), uint8(mstor4m.field_0), uint8(mstor4m.field_0), uint8(mstor4m.field_24)


# hash = 0xf1eb6de8
# getter = None
# const = None
# payable = True
def unknownf1eb6de8(uint8 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_param2 > 0
  require m_param2 <= mstor3
  munknown15b4477em[m_param1 << 248m] = m_param2


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address m_newOwner) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf9e986d0
# getter = None
# const = None
# payable = True
def unknownf9e986d0(uint256 m_param1, uint8 m_param2) payable: 
  require calldata.size - 4 >= 64
  require 11 <= mstor2
  require mstor1^10
  require mstor1
  require mstor3
  require mstor3^2
  require mstor3
  require mstor3^3
  require mstor3
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^3 % mstor3) != 2:
      return 0
  if m_param2 >= uint8(mstor4m.field_0):
      return 0
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3^2 % mstor3) >= uint8(mstor4m.field_24):
      return 0
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) / mstor3 % mstor3) >= uint8(mstor4m.field_16):
      return 0
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) % mstor3) >= munknown8aec6a26:
      return 0
  if not uint8(uint32(m_param1 / mstor1^10 % mstor1) % mstor3):
      require 7 <= mstor2
      require mstor1^6
      require mstor1
      require mstor3
      require mstor3^2
      require mstor3
      require mstor3^3
      require mstor3
      if uint8(uint32(m_param1 / mstor1^6 % mstor1) / mstor3^2 % mstor3) >= munknown15b4477em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m]:
          return (uint8(uint32(m_param1 / mstor1^6 % mstor1) / mstor3^2 % mstor3) < munknown15b4477em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m])
      if uint8(uint32(m_param1 / mstor1^6 % mstor1) / mstor3^3 % mstor3) >= munknown0731630em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m]m[uint32(m_param1 / mstor1^6 % mstor1) / mstor3^2 % mstor3 << 248m]:
          return (uint8(uint32(m_param1 / mstor1^6 % mstor1) / mstor3^3 % mstor3) < munknown0731630em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m]m[uint32(m_param1 / mstor1^6 % mstor1) / mstor3^2 % mstor3 << 248m])
      return (uint8(uint32(m_param1 / mstor1^6 % mstor1) / mstor3 % mstor3) < munknown5d7fab15m[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m])
  if 1 == uint8(uint32(m_param1 / mstor1^10 % mstor1) % mstor3):
      require 6 <= mstor2
      require mstor1^5
      require mstor1
      require mstor3
      require mstor3^2
      require mstor3
      require mstor3^3
      require mstor3
      if uint8(uint32(m_param1 / mstor1^5 % mstor1) / mstor3^2 % mstor3) >= munknown15b4477em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m]:
          return (uint8(uint32(m_param1 / mstor1^5 % mstor1) / mstor3^2 % mstor3) < munknown15b4477em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m])
      if uint8(uint32(m_param1 / mstor1^5 % mstor1) / mstor3^3 % mstor3) >= munknown0731630em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m]m[uint32(m_param1 / mstor1^5 % mstor1) / mstor3^2 % mstor3 << 248m]:
          return (uint8(uint32(m_param1 / mstor1^5 % mstor1) / mstor3^3 % mstor3) < munknown0731630em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m]m[uint32(m_param1 / mstor1^5 % mstor1) / mstor3^2 % mstor3 << 248m])
      return (uint8(uint32(m_param1 / mstor1^5 % mstor1) / mstor3 % mstor3) < munknown5d7fab15m[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m])
  if uint8(uint32(m_param1 / mstor1^10 % mstor1) % mstor3) != 2:
      require 4 <= mstor2
      require mstor1^3
      require mstor1
      require mstor3
      require mstor3^2
      require mstor3
      require mstor3^3
      require mstor3
      if uint8(uint32(m_param1 / mstor1^3 % mstor1) / mstor3^3 % mstor3) >= munknown15b4477em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m]:
          return (uint8(uint32(m_param1 / mstor1^3 % mstor1) / mstor3^3 % mstor3) < munknown15b4477em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m])
      if uint8(uint32(m_param1 / mstor1^3 % mstor1) / mstor3^2 % mstor3) >= munknown21c8bd88m[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m]:
          return (uint8(uint32(m_param1 / mstor1^3 % mstor1) / mstor3^2 % mstor3) < munknown21c8bd88m[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m])
      return (uint8(uint32(m_param1 / mstor1^3 % mstor1) / mstor3 % mstor3) < munknown5d7fab15m[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m])
  require 5 <= mstor2
  require mstor1^4
  require mstor1
  require mstor3
  require mstor3^2
  require mstor3
  require mstor3^3
  require mstor3
  if uint8(uint32(m_param1 / mstor1^4 % mstor1) / mstor3^3 % mstor3) >= munknown15b4477em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m]:
      return (uint8(uint32(m_param1 / mstor1^4 % mstor1) / mstor3^3 % mstor3) < munknown15b4477em[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m])
  if uint8(uint32(m_param1 / mstor1^4 % mstor1) / mstor3^2 % mstor3) >= munknown21c8bd88m[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m]:
      return (uint8(uint32(m_param1 / mstor1^4 % mstor1) / mstor3^2 % mstor3) < munknown21c8bd88m[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m])
  return (uint8(uint32(m_param1 / mstor1^4 % mstor1) / mstor3 % mstor3) < munknown5d7fab15m[uint32(m_param1 / mstor1^10 % mstor1) % mstor3 << 248m])


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


