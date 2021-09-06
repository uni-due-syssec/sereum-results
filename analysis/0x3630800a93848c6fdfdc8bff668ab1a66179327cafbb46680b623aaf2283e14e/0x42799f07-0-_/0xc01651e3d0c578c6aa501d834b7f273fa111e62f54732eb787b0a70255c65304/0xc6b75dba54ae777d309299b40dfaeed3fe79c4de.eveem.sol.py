# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xc6B75DBA54ae777d309299b40DfAeed3fE79C4dE 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 18
    unknown7a802c71 # mask: a s
    # storage address 18
    transfersFrozen # mask: a s
    # storage address 25
    stor25
    # storage address 6
    name
    # storage address 8
    controllerAddress # mask: a s
    # storage address 8
    decimals # mask: a s
    # storage address 17
    tokenDetails
    # storage address 0
    balanceOf
    # storage address 16
    currentCheckpointId # mask: a s
    # storage address 26
    stor26
    # storage address 22
    stor22 # mask: a s
    # storage address 12
    stor12 # mask: a s
    # storage address 12
    unknown05d97f4fAddress # mask: a s
    # storage address 9
    unknowncbaec476Address # mask: a s
    # storage address 20
    stor20 # mask: a s
    # storage address 19755060433000999595795757568161372333120116823939020588554525149188588669836
    stor19755060433000999595795757568161372333120116823939020588554525149188588669836
    # storage address 1
    allowance
    # storage address 5
    initialized # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    tokenFactoryAddress # mask: a s
    # storage address 7
    symbol
    # storage address 11
    securityTokenRegistryAddress # mask: a s
    # storage address 11
    stor11 # mask: a s
    # storage address 2
    totalSupply # mask: a s
    # storage address 24
    stor24
    # storage address 31
    stor31
    # storage address 4
    owner # mask: a s
    # storage address 13
    unknown2fb3b99dAddress # mask: a s
    # storage address 23
    stor23 # mask: a s
    # storage address 23
    stor23 # mask: a s
    # storage address 23
    stor23 # mask: a s
    # storage address 23
    stor23 # mask: a s
    # storage address 97789825912453899259273410636466998099043528421815129078110847000656284369545
    stor97789825912453899259273410636466998099043528421815129078110847000656284369545
    # storage address 10
    stor10 # mask: a s
    # storage address 10
    moduleRegistryAddress # mask: a s
    # storage address 19
    stor19 # mask: a s
    # storage address 19
    holderCount # mask: a s
    # storage address 27
    stor27
    # storage address 3
    stor3 # mask: a s
    # storage address 15
    granularity # mask: a s
    # storage address 14
    dataStoreAddress # mask: a s
# hash = 0x010648ca
# getter = None
# const = None
# payable = False
def unknown010648ca(uint256 m_param1, array m_param2, uint256 m_param3): # not payable
  require calldata.size - 4 >= 96
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + m_param2.length + 36 <= calldata.size
  require caller == mowner
  mem[324 len m_param2.length] = m_param2[allm]
  mem[m_param2.length + 324] = 0
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0xe8f20292 with:
       gas gas_remaining wei
      args 0, 29, 21, 30, m_param1, 192, m_param3, m_param2.length, m_param2[allm], mem[m_param2.length + 324 len ceil32(m_param2.length) - m_param2.length]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x01502460
# getter = None
# const = None
# payable = False
def freezeTransfers(): # not payable
  require caller == mowner
  require not mtransfersFrozen
  mtransfersFrozen = 1
  log 0xac199452: 1


# hash = 0x05d97f4f
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def unknown05d97f4f(): # not payable
  return addr(munknown05d97f4fAddress)


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 6]]]], ['loc', 6]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]m.field_0


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address m_spender, uint256 m_tokens): # not payable
  require calldata.size - 4 >= 64
  require m_spender
  require caller
  uint256(mallowancem[callerm]m[addr(m_spender)m]) = m_tokens
  log Approval(
        address owner=_tokens,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x0c912555
# getter = None
# const = None
# payable = False
def unknown0c912555(): # not payable
  require caller == mowner
  require ext_code.size(mtokenFactoryAddress)
  call mtokenFactoryAddress.0xa62d3a45 with:
       gas gas_remaining wei
      args 10
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log 0x23af9b47: uint8(stor23.field_0), uint8(stor23.field_0), uint8(stor23.field_16)


# hash = 0x103ef9e1
# getter = None
# const = None
# payable = False
def unknown103ef9e1(uint256 m_param1, addr m_param2): # not payable
  require calldata.size - 4 >= 64
  if m_param1 != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
      revert with 0, 'Invalid partition'
  mstor31m[callerm]m[m_param1m]m[addr(m_param2)m] = 1
  log 0x3646a897: _param1, _param2, caller


# hash = 0x122eb575
# getter = None
# const = None
# payable = False
def unknown122eb575(addr m_param1, addr m_param2, uint256 m_param3, array m_param4): # not payable
  require calldata.size - 4 >= 128
  require m_param4 <= 4294967296
  require m_param4 + 36 <= calldata.size
  require m_param4.length <= 4294967296 and m_param4 + m_param4.length + 36 <= calldata.size
  require mgranularity
  if m_param3 % mgranularity:
      mem[ceil32(m_param4.length) + 128] = 0x5000000000000000000000000000000000000000000000000000000000000000
      mem[ceil32(m_param4.length) + 160] = 0
      return Mask(8 * -ceil32(m_param4.length) + m_param4.length + 32, 0, 0), 
             mem[m_param4.length + 160 len -m_param4.length + ceil32(m_param4.length) + 32]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x0 with:
       gas gas_remaining wei
      args sha3(2, 24), 25, addr(m_param1), addr(m_param2), m_param3, Array(len=m_param4.length, data=m_param4[allm]), bool(mtransfersFrozen)
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x2c94d97b with:
       gas gas_remaining wei
      args bool(delegate.return_data[0]), delegate.return_data[32], addr(m_param2), m_param3, mbalanceOfm[addr(m_param1)m]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if Mask(4, 248, delegate.return_data[0]) != 0x100000000000000000000000000000000000000000000000000000000000000:
      return 0, 0, delegate.return_data[32]
  if m_param3 <= uint256(mallowancem[addr(m_param1)m]m[callerm]):
      return 0, 0, delegate.return_data[32]
  else:
      return 0


# hash = 0x12ef7fe2
# getter = None
# const = None
# payable = False
def unknown12ef7fe2(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x97137350 with:
       gas gas_remaining wei
      args addr(mmoduleRegistryAddress), sha3(addr(m_param1), 25)
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x13d557bc
# getter = None
# const = None
# payable = False
def unknown13d557bc(): # not payable
  require calldata.size - 4 >= 160
  require cd[100] <= 4294967296
  require cd[100] + 36 <= calldata.size
  require m('cd', 100).length <= 4294967296 and cd[100] + m('cd', 100).length + 36 <= calldata.size
  require cd[132] <= 4294967296
  require cd[132] + 36 <= calldata.size
  require m('cd', 132).length <= 4294967296 and cd[132] + m('cd', 132).length + 36 <= calldata.size
  require addr(mstor25m[callerm]m.field_256) == caller
  require not uint8(mstor25m[callerm]m.field_672)
  require 0 < mstor25m[callerm]m.field_768
  require 0 < mstor25m[callerm]m.field_768
  [94ms = 0
  mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor25', 25))) + (0.03125 / s))m[uint8([94ms)m] != 5m:
      require [94ms + 1 < mstor25m[callerm]m.field_768
      mem[32] = 25
      require [94ms + 1 < mstor25m[callerm]m.field_768
      mem[0] = sha3(caller, 25) + 3
      [94ms = [94ms + 1
      mcontinue 
  require 0 < m('cd', 132).length
  require Mask(8, 248, m('cd', 132)[0]) != 0
  if not addr(cd[36]):
      revert with 0, 'Invalid address'
  if cd[4] != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
      revert with 0, 'Invalid partition'
  if uint256(mallowancem[addr(cd[36])m]m[callerm]) == -1:
      mem[96] = m('cd', 100).length
      mem[128 len m('cd', 100).length] = call.data[cd[100] + 36 len m('cd', 100).length]
      mem[m('cd', 100).length + 128] = 0
      mem[64] = ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 160
      mem[ceil32(m('cd', 100).length) + 128] = m('cd', 132).length
      mem[ceil32(m('cd', 100).length) + 160 len m('cd', 132).length] = call.data[cd[132] + 36 len m('cd', 132).length]
      mem[ceil32(m('cd', 100).length) + m('cd', 132).length + 160] = 0
      mstor3++
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 164] = uint256(mholderCount)
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 196] = addr(cd[36])
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 228] = 0
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 260] = cd[68]
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 292] = mbalanceOf
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 324] = mbalanceOfm[addr(cd[36])m]
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 356] = mdataStoreAddress
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
           gas gas_remaining wei
          args uint256(mholderCount), addr(cd[36]), 0, cd[68], mbalanceOf, mbalanceOfm[addr(cd[36])m], mdataStoreAddress
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 160] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mholderCount) = delegate.return_data[0]
      require mgranularity
      if cd[68] % mgranularity:
          revert with 0, 'Invalid granularity'
      if mtransfersFrozen:
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(addr(cd[36]), 28), mbalanceOfm[addr(cd[36])m], mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require mstor3 + 1 == mstor3
          require addr(cd[36])
          require cd[68] <= mtotalSupply
          mtotalSupply -= cd[68]
          require cd[68] <= mbalanceOfm[addr(cd[36])m]
          mbalanceOfm[addr(cd[36])m] -= cd[68]
          log Transfer(address from, address to, uint256 value):
                       0,
                       Mask(224, 0, cd[68]),
                       addr(cd[36]),
                       0,
          mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 256 len ceil32(m('cd', 100).length)] = call.data[cd[100] + 36 len m('cd', 100).length], mem[m('cd', 100).length + 128 len ceil32(m('cd', 100).length) - m('cd', 100).length]
          if not m('cd', 100).length % 32:
              log 0xb7d0d6b6: 0, Mask(224, 0, cd[68]), 64, ('cd', 100).length, Mask(8 * ('cd', 100).length, -(8 * ('cd', 100).length) + 256, call.data[cd[100] + 36 len ('cd', 100).length], mem[('cd', 100).length + 128 len ceil32(('cd', 100).length) - ('cd', 100).length]) << (8 * ('cd', 100).length) - 256, 0, caller
          else:
              mem[floor32(m('cd', 100).length) + ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 256] = mem[floor32(m('cd', 100).length) + ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + -(m('cd', 100).length % 32) + 288 len m('cd', 100).length % 32]
              log 0xb7d0d6b6: 0, Mask(224, 0, cd[68]), 64, ('cd', 100).length, Mask(8 * ceil32(('cd', 100).length), -(8 * ceil32(('cd', 100).length)) + 256, call.data[cd[100] + 36 len ('cd', 100).length], mem[('cd', 100).length + 128 len ceil32(('cd', 100).length) - ('cd', 100).length]) << (8 * ceil32(('cd', 100).length)) - 256, mem[(2 * ceil32(('cd', 100).length)) + ceil32(('cd', 132).length) + 256 len floor32(('cd', 100).length) + -ceil32(('cd', 100).length) + 32], 0, caller
      else:
          mem[0] = 2
          mem[32] = 24
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              mem[0] = mstor2BACm[[94midxm]
              mem[32] = 25
              if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                  [94m_322 = mem[64]
                  mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = addr(cd[36])
                  mem[mem[64] + 36] = 0
                  mem[mem[64] + 68] = cd[68]
                  mem[mem[64] + 100] = 128
                  mem[mem[64] + 132] = mem[96]
                  [94mt = 0
                  mwhile [94mt < mem[96]m:
                      mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                      [94mt = [94mt + 32
                      mcontinue 
                  if not mem[96] % 32:
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len mem[96] + [94m_322 + -mem[64] + 160]
                  else:
                      mem[floor32(mem[96]) + [94m_322 + 164] = mem[floor32(mem[96]) + [94m_322 + -(mem[96] % 32) + 196 len mem[96] % 32]
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len floor32(mem[96]) + [94m_322 + -mem[64] + 192]
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 3
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      [94ms = mstor2BACm[[94midxm]
                      [94ms = 1
                      mcontinue 
                  require ext_call.return_data[0] <= 3
                  if ext_call.return_data[0] != 2:
                      require ext_call.return_data[0] <= 3
              [94midx = [94midx + 1
              [94ms = mstor2BACm[[94midxm]
              [94ms = [94ms
              mcontinue 
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(addr(cd[36]), 28), mbalanceOfm[addr(cd[36])m], mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          mem[mem[64] + 68] = mcurrentCheckpointId
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require mstor3 + 1 == mstor3
          require addr(cd[36])
          require cd[68] <= mtotalSupply
          mtotalSupply -= cd[68]
          require cd[68] <= mbalanceOfm[addr(cd[36])m]
          mem[0] = addr(cd[36])
          mem[32] = 0
          mbalanceOfm[addr(cd[36])m] -= cd[68]
          log Transfer(
                address from=cd[68],
                address to=addr(cd[36]),
                uint256 value=0)
          mem[mem[64]] = cd[68]
          mem[mem[64] + 32] = 64
          mem[mem[64] + 64] = mem[96]
          if [94ms:
              mem[mem[64] + 96 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
              if not mem[96] % 32:
                  log 0xb7d0d6b6: cd[68], 64, mem[mem[64] + 64 len mem[96] + 32], 0, caller
              else:
                  mem[floor32(mem[96]) + mem[64] + 96] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 128 len mem[96] % 32]
                  log 0xb7d0d6b6: cd[68], 64, mem[mem[64] + 64 len floor32(mem[96]) + 64], 0, caller
          else:
              [94m_406 = mem[96]
              mem[mem[64] + 96 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
              if not mem[96] % 32:
                  log 0xb7d0d6b6: cd[68], 64, mem[mem[64] + 64 len mem[96] + 32], 0, caller
              else:
                  mem[floor32(mem[96]) + mem[64] + 96] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 128 len mem[96] % 32]
                  log 0xb7d0d6b6: cd[68], 64, mem[mem[64] + 64 len floor32(_406) + 64], 0, caller
  else:
      if not mstor31m[addr(cd[36])m]m[cd[4]m]m[callerm]:
          revert with 0, 'Not Authorised'
      mem[96] = m('cd', 100).length
      mem[128 len m('cd', 100).length] = call.data[cd[100] + 36 len m('cd', 100).length]
      mem[m('cd', 100).length + 128] = 0
      mem[64] = ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 160
      mem[ceil32(m('cd', 100).length) + 128] = m('cd', 132).length
      mem[ceil32(m('cd', 100).length) + 160 len m('cd', 132).length] = call.data[cd[132] + 36 len m('cd', 132).length]
      mem[ceil32(m('cd', 100).length) + m('cd', 132).length + 160] = 0
      mstor3++
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 164] = uint256(mholderCount)
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 196] = addr(cd[36])
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 228] = 0
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 260] = cd[68]
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 292] = mbalanceOf
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 324] = mbalanceOfm[addr(cd[36])m]
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 356] = mdataStoreAddress
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
           gas gas_remaining wei
          args uint256(mholderCount), addr(cd[36]), 0, cd[68], mbalanceOf, mbalanceOfm[addr(cd[36])m], mdataStoreAddress
      mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 160] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mholderCount) = delegate.return_data[0]
      require mgranularity
      if cd[68] % mgranularity:
          revert with 0, 'Invalid granularity'
      if mtransfersFrozen:
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(addr(cd[36]), 28), mbalanceOfm[addr(cd[36])m], mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require mstor3 + 1 == mstor3
          require addr(cd[36])
          require cd[68] <= mtotalSupply
          mtotalSupply -= cd[68]
          require cd[68] <= mbalanceOfm[addr(cd[36])m]
          mbalanceOfm[addr(cd[36])m] -= cd[68]
          log Transfer(address from, address to, uint256 value):
                       0,
                       Mask(224, 0, cd[68]),
                       addr(cd[36]),
                       0,
          mem[ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 256 len ceil32(m('cd', 100).length)] = call.data[cd[100] + 36 len m('cd', 100).length], mem[m('cd', 100).length + 128 len ceil32(m('cd', 100).length) - m('cd', 100).length]
          if not m('cd', 100).length % 32:
              log 0xb7d0d6b6: 0, Mask(224, 0, cd[68]), 64, ('cd', 100).length, Mask(8 * ('cd', 100).length, -(8 * ('cd', 100).length) + 256, call.data[cd[100] + 36 len ('cd', 100).length], mem[('cd', 100).length + 128 len ceil32(('cd', 100).length) - ('cd', 100).length]) << (8 * ('cd', 100).length) - 256, 0, caller
          else:
              mem[floor32(m('cd', 100).length) + ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + 256] = mem[floor32(m('cd', 100).length) + ceil32(m('cd', 100).length) + ceil32(m('cd', 132).length) + -(m('cd', 100).length % 32) + 288 len m('cd', 100).length % 32]
              log 0xb7d0d6b6: 0, Mask(224, 0, cd[68]), 64, ('cd', 100).length, Mask(8 * ceil32(('cd', 100).length), -(8 * ceil32(('cd', 100).length)) + 256, call.data[cd[100] + 36 len ('cd', 100).length], mem[('cd', 100).length + 128 len ceil32(('cd', 100).length) - ('cd', 100).length]) << (8 * ceil32(('cd', 100).length)) - 256, mem[(2 * ceil32(('cd', 100).length)) + ceil32(('cd', 132).length) + 256 len floor32(('cd', 100).length) + -ceil32(('cd', 100).length) + 32], 0, caller
      else:
          mem[0] = 2
          mem[32] = 24
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              mem[0] = mstor2BACm[[94midxm]
              mem[32] = 25
              if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                  [94m_326 = mem[64]
                  mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = addr(cd[36])
                  mem[mem[64] + 36] = 0
                  mem[mem[64] + 68] = cd[68]
                  mem[mem[64] + 100] = 128
                  mem[mem[64] + 132] = mem[96]
                  [94mt = 0
                  mwhile [94mt < mem[96]m:
                      mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                      [94mt = [94mt + 32
                      mcontinue 
                  if not mem[96] % 32:
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len mem[96] + [94m_326 + -mem[64] + 160]
                  else:
                      mem[floor32(mem[96]) + [94m_326 + 164] = mem[floor32(mem[96]) + [94m_326 + -(mem[96] % 32) + 196 len mem[96] % 32]
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len floor32(mem[96]) + [94m_326 + -mem[64] + 192]
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 3
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      [94ms = mstor2BACm[[94midxm]
                      [94ms = 1
                      mcontinue 
                  require ext_call.return_data[0] <= 3
                  if ext_call.return_data[0] != 2:
                      require ext_call.return_data[0] <= 3
              [94midx = [94midx + 1
              [94ms = mstor2BACm[[94midxm]
              [94ms = [94ms
              mcontinue 
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(addr(cd[36]), 28), mbalanceOfm[addr(cd[36])m], mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          mem[mem[64] + 68] = mcurrentCheckpointId
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require mstor3 + 1 == mstor3
          require addr(cd[36])
          require cd[68] <= mtotalSupply
          mtotalSupply -= cd[68]
          require cd[68] <= mbalanceOfm[addr(cd[36])m]
          mem[0] = addr(cd[36])
          mem[32] = 0
          mbalanceOfm[addr(cd[36])m] -= cd[68]
          log Transfer(
                address from=cd[68],
                address to=addr(cd[36]),
                uint256 value=0)
          mem[mem[64]] = cd[68]
          mem[mem[64] + 32] = 64
          mem[mem[64] + 64] = mem[96]
          mem[mem[64] + 96 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
          if not mem[96] % 32:
              log 0xb7d0d6b6: cd[68], 64, mem[mem[64] + 64 len mem[96] + 32], 0, caller
          else:
              mem[floor32(mem[96]) + mem[64] + 96] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 128 len mem[96] % 32]
              log 0xb7d0d6b6: cd[68], 64, mem[mem[64] + 64 len floor32(mem[96]) + 64], 0, caller
  revert with 0, 'Invalid redeem'


# hash = 0x158ef93e
# getter = ['bool', ['storage', 8, 160, 5]]
# const = None
# payable = False
def initialized(): # not payable
  return bool(minitialized)


# hash = 0x168ecec5
# getter = None
# const = None
# payable = False
def unknown168ecec5(uint256 m_param1, addr m_param2): # not payable
  require calldata.size - 4 >= 64
  if m_param1 != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
      revert with 0, 'Invalid partition'
  mstor31m[callerm]m[m_param1m]m[addr(m_param2)m] = 0
  log 0x3b287c4f: _param1, _param2, caller


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def totalSupply(): # not payable
  return mtotalSupply


# hash = 0x1aab9a9f
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def holderCount(): # not payable
  return uint256(mholderCount)


# hash = 0x1badb25c
# getter = None
# const = None
# payable = False
def unknown1badb25c(addr m_param1, uint256 m_param2, array m_param3): # not payable
  require calldata.size - 4 >= 96
  require m_param3 <= 4294967296
  require m_param3 + 36 <= calldata.size
  require m_param3.length <= 4294967296 and m_param3 + m_param3.length + 36 <= calldata.size
  require mgranularity
  if m_param2 % mgranularity:
      mem[ceil32(m_param3.length) + 128] = 0x5000000000000000000000000000000000000000000000000000000000000000
      mem[ceil32(m_param3.length) + 160] = 0
      return Mask(8 * -ceil32(m_param3.length) + m_param3.length + 32, 0, 0), 
             mem[m_param3.length + 160 len -m_param3.length + ceil32(m_param3.length) + 32]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x0 with:
       gas gas_remaining wei
      args sha3(2, 24), 25, caller, addr(m_param1), m_param2, Array(len=m_param3.length, data=m_param3[allm]), bool(mtransfersFrozen)
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x2c94d97b with:
       gas gas_remaining wei
      args bool(delegate.return_data[0]), delegate.return_data[32], addr(m_param1), m_param2, mbalanceOfm[callerm]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return 0, 0, delegate.return_data[32]


# hash = 0x1e6f20f8
# getter = None
# const = None
# payable = False
def unknown1e6f20f8(addr m_param1, array m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5, bool m_param6): # not payable
  require calldata.size - 4 >= 192
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + m_param2.length + 36 <= calldata.size
  mem[96] = m_param2.length
  mem[128 len m_param2.length] = m_param2[allm]
  mem[m_param2.length + 128] = 0
  mstor3++
  require caller == mowner
  mem[ceil32(m_param2.length) + 132] = m_param1
  mem[ceil32(m_param2.length) + 164] = 0
  require ext_code.size(addr(mmoduleRegistryAddress))
  call addr(mmoduleRegistryAddress).0x36ef22ce with:
       gas gas_remaining wei
      args addr(m_param1), 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(m_param2.length) + 128] = 0xb4579d6000000000000000000000000000000000000000000000000000000000
  require ext_code.size(m_param1)
  static call m_param1.getTypes() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(m_param2.length) + 128 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(m_param2.length) + ceil32(return_data.size) + 128
  require return_data.size >= 32
  [94m_7 = 0, mem[ceil32(m_param2.length) + 132 len 28]
  require 0, mem[ceil32(m_param2.length) + 132 len 28] <= 4294967296
  require 0, mem[ceil32(m_param2.length) + 132 len 28] + 32 <= return_data.size
  require mem[ceil32(m_param2.length) + 0, mem[ceil32(m_param2.length) + 132 len 28] + 128] <= 4294967296 and 0, mem[ceil32(m_param2.length) + 132 len 28] + (32 * mem[ceil32(m_param2.length) + 0, mem[ceil32(m_param2.length) + 132 len 28] + 128]) + 32 <= return_data.size
  require ext_code.size(m_param1)
  call m_param1.0xb6cf3a62 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > m_param3:
      revert with 0, 'Invalid cost'
  require ext_code.size(addr(munknown05d97f4fAddress))
  call addr(munknown05d97f4fAddress).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args addr(m_param1), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128] = 'wC`'
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 196 len ceil32(m_param2.length)] = m_param2[allm], mem[m_param2.length + 128 len ceil32(m_param2.length) - m_param2.length]
  require ext_code.size(m_param1)
  call m_param1 with:
     funct Mask(32, 224, 'wC`') >> 224
       gas gas_remaining wei
      args Array(len=m_param2.length, data=m_param2[allm])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if addr(mstor25m[addr(ext_call.return_data[0])m]m.field_256):
      revert with 0, 'Module exists'
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 132] = addr(ext_call.return_data[0])
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 164] = m_param4
  require ext_code.size(addr(munknown05d97f4fAddress))
  call addr(munknown05d97f4fAddress).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args addr(ext_call.return_data[0]), m_param4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_param1)
  static call m_param1.name() with:
          gas gas_remaining wei
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94m_335 = mem[ceil32(m_param2.length) + [94m_7 + 128]
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128] = mem[ceil32(m_param2.length) + [94m_7 + 128]
  if not [94m_335:
      [94m_597 = mem[ceil32(m_param2.length) + [94m_7 + 128]
      [94midx = 0
      mwhile [94midx < [94m_597m:
          require [94midx < mem[ceil32(m_param2.length) + [94m_7 + 128]
          require [94midx < mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[(32 * [94midx) + ceil32(m_param2.length) + ceil32(return_data.size) + 160] = uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])
          require [94midx < mem[ceil32(m_param2.length) + [94m_7 + 128]
          mem[32] = 24
          uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])++
          mem[0] = sha3(mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1], 24)
          addr(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m]m[uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])m]) = addr(ext_call.return_data[0])
          [94midx = [94midx + 1
          mcontinue 
      mem[64] = ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 160] = ext_call.return_data[0]
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 192] = addr(ext_call.return_data[0])
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 224] = m_param1
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 256] = m_param6
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 288] = ceil32(m_param2.length) + [94m_7 + 128
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 320] = ceil32(m_param2.length) + ceil32(return_data.size) + 128
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 352] = uint256(mstor26m[ext_call.return_data[0]m])
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 384] = m_param5
      mem[32] = 25
      mstor25m[addr(ext_call.return_data[0])m]m.field_0 = ext_call.return_data[0]
      addr(mstor25m[addr(ext_call.return_data[0])m]m.field_256) = addr(ext_call.return_data[0])
      addr(mstor25m[addr(ext_call.return_data[0])m]m.field_512) = m_param1
      Mask(96, 0, mstor25m[addr(ext_call.return_data[0])m]m.field_672) = Mask(96, 0, m_param6)
      mstor25m[addr(ext_call.return_data[0])m]m.field_768 = mem[ceil32(m_param2.length) + [94m_7 + 128]
      mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 3
      if not mem[ceil32(m_param2.length) + [94m_7 + 128]:
          [94midx = 0
          mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_768 + 31 / 32 > [94midxm:
              uint8(mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor25m[addr(ext_call.return_data[0])m]m.field_1024 = mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 4
          if not mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]:
              [94midx = 0
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = m_param5
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param6
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1043 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              [94mvar67001 = floor32([94m_1043)
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, _param5, _param6, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1043) + 32], ext_call.return_data[0], _param1
          else:
              [94ms = 0
              [94midx = ceil32(m_param2.length) + ceil32(return_data.size) + 160
              mwhile ceil32(m_param2.length) + ceil32(return_data.size) + (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 160 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0 = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 31) >> 5
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = m_param5
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param6
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1211 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              [94mvar70001 = floor32([94m_1211)
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, _param5, _param6, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1211) + 32], ext_call.return_data[0], _param1
      else:
          [94ms = 0
          [94midx = ceil32(m_param2.length) + [94m_7 + 160
          mwhile ceil32(m_param2.length) + [94m_7 + (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 160 > [94midxm:
              mstor25m[addr(ext_call.return_data[0])m]m[3m]m.field_0 = mem[[94midx + 31 len 1] * 256^[94ms or !(255 * 256^[94ms) and mstor25m[addr(ext_call.return_data[0])m]m[3m]m.field_0
              [94ms = [94ms + -([94ms + 1 / 32) + (-1 * [94ms * [94ms + 1 / 32) + 1
              [94midx = [94midx + 32
              mcontinue 
          [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 31) >> 5
          [94ms = sha3(sha3(addr(ext_call.return_data[0]), 25) + 3)
          mwhile [94midxm:
              mstor[[94msm] = !(255 * 256^[94midx) and mstor[[94msm]
              [94midx = [94midx + -([94midx + 1 / 32) + (-1 * [94midx * [94midx + 1 / 32) + 1
              [94ms = ([94midx + 1 / 32) + [94ms
              mcontinue 
          [94midx = (floor32(None + 3) >> 4) + (None * None + 3 / 32) - (Mask(251, 0, (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 31) >> 5 * None + 3 / 32)
          mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_768 + 31 / 32 > [94midxm:
              uint8(mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor25m[addr(ext_call.return_data[0])m]m.field_1024 = mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 4
          if not mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]:
              [94midx = 0
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = m_param5
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param6
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1347 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, _param5, _param6, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1347) + 32], ext_call.return_data[0], _param1
          else:
              [94ms = 0
              [94midx = ceil32(m_param2.length) + ceil32(return_data.size) + 160
              mwhile ceil32(m_param2.length) + ceil32(return_data.size) + (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 160 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0 = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 31) >> 5
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = m_param5
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param6
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1427 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, _param5, _param6, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1427) + 32], ext_call.return_data[0], _param1
  else:
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + 160 len 32 * [94m_335] = code.data[24259 len 32 * [94m_335]
      [94m_598 = mem[ceil32(m_param2.length) + [94m_7 + 128]
      [94midx = 0
      mwhile [94midx < [94m_598m:
          require [94midx < mem[ceil32(m_param2.length) + [94m_7 + 128]
          require [94midx < mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[(32 * [94midx) + ceil32(m_param2.length) + ceil32(return_data.size) + 160] = uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])
          require [94midx < mem[ceil32(m_param2.length) + [94m_7 + 128]
          mem[32] = 24
          uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])++
          mem[0] = sha3(mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1], 24)
          addr(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m]m[uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])m]) = addr(ext_call.return_data[0])
          [94midx = [94midx + 1
          mcontinue 
      mem[64] = ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 160] = ext_call.return_data[0]
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 192] = addr(ext_call.return_data[0])
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 224] = m_param1
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 256] = m_param6
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 288] = ceil32(m_param2.length) + [94m_7 + 128
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 320] = ceil32(m_param2.length) + ceil32(return_data.size) + 128
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 352] = uint256(mstor26m[ext_call.return_data[0]m])
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 384] = m_param5
      mem[32] = 25
      mstor25m[addr(ext_call.return_data[0])m]m.field_0 = ext_call.return_data[0]
      addr(mstor25m[addr(ext_call.return_data[0])m]m.field_256) = addr(ext_call.return_data[0])
      addr(mstor25m[addr(ext_call.return_data[0])m]m.field_512) = m_param1
      Mask(96, 0, mstor25m[addr(ext_call.return_data[0])m]m.field_672) = Mask(96, 0, m_param6)
      mstor25m[addr(ext_call.return_data[0])m]m.field_768 = mem[ceil32(m_param2.length) + [94m_7 + 128]
      mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 3
      if not mem[ceil32(m_param2.length) + [94m_7 + 128]:
          [94midx = 0
          mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_768 + 31 / 32 > [94midxm:
              uint8(mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor25m[addr(ext_call.return_data[0])m]m.field_1024 = mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 4
          if not mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]:
              [94midx = 0
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = m_param5
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param6
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1050 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              [94mvar68001 = floor32([94m_1050)
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, _param5, _param6, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1050) + 32], ext_call.return_data[0], _param1
          else:
              [94ms = 0
              [94midx = ceil32(m_param2.length) + ceil32(return_data.size) + 160
              mwhile ceil32(m_param2.length) + ceil32(return_data.size) + (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 160 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0 = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 31) >> 5
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = m_param5
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param6
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1220 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              [94mvar71001 = floor32([94m_1220)
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, _param5, _param6, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1220) + 32], ext_call.return_data[0], _param1
      else:
          [94ms = 0
          [94midx = ceil32(m_param2.length) + [94m_7 + 160
          mwhile ceil32(m_param2.length) + [94m_7 + (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 160 > [94midxm:
              mstor25m[addr(ext_call.return_data[0])m]m[3m]m.field_0 = mem[[94midx + 31 len 1] * 256^[94ms or !(255 * 256^[94ms) and mstor25m[addr(ext_call.return_data[0])m]m[3m]m.field_0
              [94ms = [94ms + -([94ms + 1 / 32) + (-1 * [94ms * [94ms + 1 / 32) + 1
              [94midx = [94midx + 32
              mcontinue 
          [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 31) >> 5
          [94ms = sha3(sha3(addr(ext_call.return_data[0]), 25) + 3)
          mwhile [94midxm:
              mstor[[94msm] = !(255 * 256^[94midx) and mstor[[94msm]
              [94midx = [94midx + -([94midx + 1 / 32) + (-1 * [94midx * [94midx + 1 / 32) + 1
              [94ms = ([94midx + 1 / 32) + [94ms
              mcontinue 
          [94midx = (floor32(None + 3) >> 4) + (None * None + 3 / 32) - (Mask(251, 0, (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 31) >> 5 * None + 3 / 32)
          mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_768 + 31 / 32 > [94midxm:
              uint8(mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor25m[addr(ext_call.return_data[0])m]m.field_1024 = mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 4
          if not mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]:
              [94midx = 0
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = m_param5
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param6
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1354 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, _param5, _param6, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1354) + 32], ext_call.return_data[0], _param1
          else:
              [94ms = 0
              [94midx = ceil32(m_param2.length) + ceil32(return_data.size) + 160
              mwhile ceil32(m_param2.length) + ceil32(return_data.size) + (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 160 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0 = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 31) >> 5
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = m_param5
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param6
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1434 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, _param5, _param6, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1434) + 32], ext_call.return_data[0], _param1
  require mstor3 + 1 == mstor3


# hash = 0x210a8d0e
# getter = None
# const = None
# payable = False
def changeGranularity(uint256 m_granularity): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  if not m_granularity:
      revert with 0, 'Invalid granularity'
  log 0x7728e5c4: granularity, _granularity
  mgranularity = m_granularity


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_tokens): # not payable
  require calldata.size - 4 >= 96
  mem[64] = 128
  mem[96] = 0
  mstor3++
  mem[132] = uint256(mholderCount)
  mem[164] = m_from
  mem[196] = m_to
  mem[228] = m_tokens
  mem[260] = mbalanceOfm[addr(m_to)m]
  mem[292] = mbalanceOfm[addr(m_from)m]
  mem[324] = mdataStoreAddress
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
       gas gas_remaining wei
      args 0, uint32(mstor19), addr(m_from), addr(m_to), m_tokens, mbalanceOfm[addr(m_to)m], mbalanceOfm[addr(m_from)m], mdataStoreAddress
  mem[128] = delegate.return_data[0]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mholderCount) = delegate.return_data[0]
  require mgranularity
  if m_tokens % mgranularity:
      revert with 0, 'Invalid granularity'
  if not mtransfersFrozen:
      mem[0] = 2
      mem[32] = 24
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          mem[0] = mstor2BACm[[94midxm]
          mem[32] = 25
          if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
              [94m_45 = mem[64]
              mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = m_from
              mem[mem[64] + 36] = m_to
              mem[mem[64] + 68] = m_tokens
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = mem[96]
              [94mt = 0
              mwhile [94mt < mem[96]m:
                  mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                  [94mt = [94mt + 32
                  mcontinue 
              if not mem[96] % 32:
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len mem[96] + [94m_45 + -mem[64] + 160]
              else:
                  mem[floor32(mem[96]) + [94m_45 + 164] = mem[floor32(mem[96]) + [94m_45 + -(mem[96] % 32) + 196 len mem[96] % 32]
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len floor32(mem[96]) + [94m_45 + -mem[64] + 192]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
          [94midx = [94midx + 1
          [94ms = mstor2BACm[[94midxm]
          [94ms = [94ms
          mcontinue 
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(m_from), 28), mbalanceOfm[addr(m_from)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(m_to), 28), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mstor3 + 1 == mstor3
  revert with 0, 'Transfer Invalid'


# hash = 0x2535f762
# getter = None
# const = None
# payable = False
def transferWithData(address m_to, uint256 m_value, bytes m_data): # not payable
  require calldata.size - 4 >= 96
  require m_data <= 4294967296
  require m_data + 36 <= calldata.size
  require m_data.length <= 4294967296 and m_data + m_data.length + 36 <= calldata.size
  mem[64] = ceil32(m_data.length) + 128
  mem[96] = m_data.length
  mem[128 len m_data.length] = m_data[allm]
  mem[m_data.length + 128] = 0
  mstor3++
  mem[ceil32(m_data.length) + 132] = uint256(mholderCount)
  mem[ceil32(m_data.length) + 164] = caller
  mem[ceil32(m_data.length) + 196] = m_to
  mem[ceil32(m_data.length) + 228] = m_value
  mem[ceil32(m_data.length) + 260] = mbalanceOfm[addr(m_to)m]
  mem[ceil32(m_data.length) + 292] = mbalanceOfm[callerm]
  mem[ceil32(m_data.length) + 324] = mdataStoreAddress
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
       gas gas_remaining wei
      args uint256(mholderCount), caller, addr(m_to), m_value, mbalanceOfm[addr(m_to)m], mbalanceOfm[callerm], mdataStoreAddress
  mem[ceil32(m_data.length) + 128] = delegate.return_data[0]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mholderCount) = delegate.return_data[0]
  require mgranularity
  if m_value % mgranularity:
      revert with 0, 'Invalid granularity'
  if not mtransfersFrozen:
      mem[0] = 2
      mem[32] = 24
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          mem[0] = mstor2BACm[[94midxm]
          mem[32] = 25
          if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
              [94m_45 = mem[64]
              mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = caller
              mem[mem[64] + 36] = m_to
              mem[mem[64] + 68] = m_value
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = mem[96]
              [94mt = 0
              mwhile [94mt < mem[96]m:
                  mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                  [94mt = [94mt + 32
                  mcontinue 
              if not mem[96] % 32:
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len mem[96] + [94m_45 + -mem[64] + 160]
              else:
                  mem[floor32(mem[96]) + [94m_45 + 164] = mem[floor32(mem[96]) + [94m_45 + -(mem[96] % 32) + 196 len mem[96] % 32]
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len floor32(mem[96]) + [94m_45 + -mem[64] + 192]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
          [94midx = [94midx + 1
          [94ms = mstor2BACm[[94midxm]
          [94ms = [94ms
          mcontinue 
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(caller, 28), mbalanceOfm[callerm], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(m_to), 28), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mstor3 + 1 == mstor3
  revert with 0, 'Transfer Invalid'


# hash = 0x2bc6acc3
# getter = None
# const = None
# payable = False
def unknown2bc6acc3(addr m_param1, uint256 m_param2, array m_param3, array m_param4): # not payable
  require calldata.size - 4 >= 128
  require m_param3 <= 4294967296
  require m_param3 + 36 <= calldata.size
  require m_param3.length <= 4294967296 and m_param3 + m_param3.length + 36 <= calldata.size
  require m_param4 <= 4294967296
  require m_param4 + 36 <= calldata.size
  require m_param4.length <= 4294967296 and m_param4 + m_param4.length + 36 <= calldata.size
  if mcontrollerAddress != caller:
      revert with 0, 'Not Authorised'
  if munknown7a802c71:
      revert with 0, 'Not Authorised'
  mem[64] = ceil32(m_param3.length) + 128
  mem[96] = m_param3.length
  mem[128 len m_param3.length] = m_param3[allm]
  mem[m_param3.length + 128] = 0
  mstor3++
  mem[ceil32(m_param3.length) + 132] = uint256(mholderCount)
  mem[ceil32(m_param3.length) + 164] = m_param1
  mem[ceil32(m_param3.length) + 196] = 0
  mem[ceil32(m_param3.length) + 228] = m_param2
  mem[ceil32(m_param3.length) + 260] = mbalanceOf
  mem[ceil32(m_param3.length) + 292] = mbalanceOfm[addr(m_param1)m]
  mem[ceil32(m_param3.length) + 324] = mdataStoreAddress
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
       gas gas_remaining wei
      args uint256(mholderCount), addr(m_param1), 0, m_param2, mbalanceOf, mbalanceOfm[addr(m_param1)m], mdataStoreAddress
  mem[ceil32(m_param3.length) + 128] = delegate.return_data[0]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mholderCount) = delegate.return_data[0]
  require mgranularity
  if m_param2 % mgranularity:
      revert with 0, 'Invalid granularity'
  if mtransfersFrozen:
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(addr(m_param1), 28), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mstor3 + 1 == mstor3
      require m_param1
      require m_param2 <= mtotalSupply
      mtotalSupply -= m_param2
      require m_param2 <= mbalanceOfm[addr(m_param1)m]
      mbalanceOfm[addr(m_param1)m] -= m_param2
      log Transfer(address from, address to, uint256 value):
                   0,
                   Mask(224, 0, _param2),
                   _param1,
                   0,
      mem[ceil32(m_param3.length) + 128] = m_param2
      mem[ceil32(m_param3.length) + 224 len ceil32(m_param3.length)] = m_param3[allm], mem[m_param3.length + 128 len ceil32(m_param3.length) - m_param3.length]
      if not m_param3.length % 32:
          log 0xb7d0d6b6: 0, Mask(224, 0, _param2), 64, _param3.length, Mask(8 * _param3.length, -(8 * _param3.length) + 256, _param3[all], mem[_param3.length + 128 len ceil32(_param3.length) - _param3.length]) << (8 * _param3.length) - 256, 0, caller
      else:
          mem[floor32(m_param3.length) + ceil32(m_param3.length) + 224] = mem[floor32(m_param3.length) + ceil32(m_param3.length) + -(m_param3.length % 32) + 256 len m_param3.length % 32]
          log 0xb7d0d6b6: 0, Mask(224, 0, _param2), 64, _param3.length, Mask(8 * ceil32(_param3.length), -(8 * ceil32(_param3.length)) + 256, _param3[all], mem[_param3.length + 128 len ceil32(_param3.length) - _param3.length]) << (8 * ceil32(_param3.length)) - 256, mem[(2 * ceil32(_param3.length)) + 224 len floor32(_param3.length) + -ceil32(_param3.length) + 32], 0, caller
      mem[(2 * ceil32(m_param3.length)) + 320 len m_param4.length] = m_param4[allm]
      mem[m_param4.length + (2 * ceil32(m_param3.length)) + 320] = 0
      log 0x876b7cb4: caller, _param2, 128, ceil32(_param3.length) + 160, _param3.length, _param3[all], 0, mem[ceil32(_param3.length) + _param3.length + 320 len ceil32(_param3.length) - _param3.length], _param4[all], mem[(2 * ceil32(_param3.length)) + _param4.length + 320 len ceil32(_param4.length) - _param4.length], _param1
  else:
      mem[0] = 2
      mem[32] = 24
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          mem[0] = mstor2BACm[[94midxm]
          mem[32] = 25
          if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
              mem[ceil32(m_param3.length) + 128] = 0x3d32173100000000000000000000000000000000000000000000000000000000
              mem[ceil32(m_param3.length) + 132] = m_param1
              mem[ceil32(m_param3.length) + 164] = 0
              mem[ceil32(m_param3.length) + 196] = m_param2
              mem[ceil32(m_param3.length) + 228] = 128
              mem[ceil32(m_param3.length) + 260] = mem[96]
              [94mt = 0
              mwhile [94mt < mem[96]m:
                  mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                  [94mt = [94mt + 32
                  mcontinue 
              if not mem[96] % 32:
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len mem[96] + ceil32(m_param3.length) + -mem[64] + 288]
              else:
                  mem[floor32(mem[96]) + ceil32(m_param3.length) + 292] = mem[floor32(mem[96]) + ceil32(m_param3.length) + -(mem[96] % 32) + 324 len mem[96] % 32]
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_param3.length) + -mem[64] + 320]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
          [94midx = [94midx + 1
          [94ms = mstor2BACm[[94midxm]
          [94ms = [94ms
          mcontinue 
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(addr(m_param1), 28), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      mem[ceil32(m_param3.length) + 196] = mcurrentCheckpointId
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mstor3 + 1 == mstor3
      require m_param1
      require m_param2 <= mtotalSupply
      mtotalSupply -= m_param2
      require m_param2 <= mbalanceOfm[addr(m_param1)m]
      mbalanceOfm[addr(m_param1)m] -= m_param2
      log Transfer(
            address from=_param2,
            address to=_param1,
            uint256 value=0)
      mem[ceil32(m_param3.length) + 128] = m_param2
      mem[ceil32(m_param3.length) + 160] = 64
      mem[ceil32(m_param3.length) + 192] = mem[96]
      mem[ceil32(m_param3.length) + 224 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
      if not mem[96] % 32:
          log 0xb7d0d6b6: _param2, 64, mem[ceil32(_param3.length) + 192 len mem[96] + 32], 0, caller
      else:
          mem[floor32(mem[96]) + ceil32(m_param3.length) + 224] = mem[floor32(mem[96]) + ceil32(m_param3.length) + -(mem[96] % 32) + 256 len mem[96] % 32]
          log 0xb7d0d6b6: _param2, Array(len=mem[96], data=mem[ceil32(_param3.length) + 224 len floor32(mem[96]) + 32]), 0, caller
      mem[(2 * ceil32(m_param3.length)) + 320 len m_param4.length] = m_param4[allm]
      mem[m_param4.length + (2 * ceil32(m_param3.length)) + 320] = 0
      log 0x876b7cb4: caller, _param2, 128, ceil32(_param3.length) + 160, _param3.length, _param3[all], 0, mem[ceil32(_param3.length) + _param3.length + 320 len ceil32(_param3.length) + ceil32(_param4.length) - _param3.length], _param1


# hash = 0x2fb3b99d
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknown2fb3b99d(): # not payable
  return munknown2fb3b99dAddress


# hash = 0x30e82803
# getter = None
# const = None
# payable = False
def unknown30e82803(uint256 m_param1, addr m_param2): # not payable
  require calldata.size - 4 >= 64
  if not mstor2BACm.length:
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          require [94midx < mstor2BACm.length
          [94m_16 = mem[(32 * [94midx) + 128]
          mem[(32 * mstor2BACm.length) + 132] = m_param1
          mem[(32 * mstor2BACm.length) + 164] = m_param2
          mem[(32 * mstor2BACm.length) + 196] = 0
          require ext_code.size(addr([94m_16))
          static call addr([94m_16).0x2829e651 with:
                  gas gas_remaining wei
                 args m_param1, addr(m_param2), 0
          mem[(32 * mstor2BACm.length) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if m_param1 != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
              if [94ms >= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  mcontinue 
          else:
              if ext_call.return_data[0] >= [94ms:
                  if [94midx:
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      [94ms = [94ms
                      mcontinue 
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          [94ms = ext_call.return_data[0]
          mcontinue 
  else:
      mem[128] = mstor2BAC
      [94midx = 128
      [94ms = sha3(0x2bacf7cca723d030d12aee795132f2c5f2d14ad131f16f3f27eeba3e79d18b8c)
      mwhile (32 * mstor2BACm.length) + 96 > [94midxm:
          mem[[94midx + 32] = addr(mallowancem[[94msm])
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          require [94midx < mstor2BACm.length
          [94m_38 = mem[(32 * [94midx) + 128]
          mem[(32 * mstor2BACm.length) + 132] = m_param1
          mem[(32 * mstor2BACm.length) + 164] = m_param2
          mem[(32 * mstor2BACm.length) + 196] = 0
          require ext_code.size(addr([94m_38))
          static call addr([94m_38).0x2829e651 with:
                  gas gas_remaining wei
                 args m_param1, addr(m_param2), 0
          mem[(32 * mstor2BACm.length) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if m_param1 != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
              if [94ms >= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  mcontinue 
          else:
              if ext_call.return_data[0] >= [94ms:
                  if [94midx:
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      [94ms = [94ms
                      mcontinue 
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          [94ms = ext_call.return_data[0]
          mcontinue 
  return [94ms


# hash = 0x313ce567
# getter = ['storage', 8, 0, 8]
# const = None
# payable = False
def decimals(): # not payable
  return mdecimals


# hash = 0x31c420d4
# getter = None
# const = None
# payable = False
def unfreezeTransfers(): # not payable
  require caller == mowner
  require mtransfersFrozen
  mtransfersFrozen = 0
  log 0xac199452: 0


# hash = 0x3576857e
# getter = None
# const = None
# payable = False
def unknown3576857e(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0xad242615 with:
       gas gas_remaining wei
      args sha3(addr(m_param1), 25)
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x39509351
# getter = None
# const = None
# payable = False
def increaseAllowance(address m_spender, uint256 m_addedValue): # not payable
  require calldata.size - 4 >= 64
  require m_addedValue + uint256(mallowancem[callerm]m[addr(m_spender)m]) >= uint256(mallowancem[callerm]m[addr(m_spender)m])
  require m_spender
  require caller
  uint256(mallowancem[callerm]m[addr(m_spender)m]) = m_addedValue + uint256(mallowancem[callerm]m[addr(m_spender)m])
  log Approval(
        address owner=(_addedValue + uint256(allowance[caller][addr(_spender)])),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x4c783bf5
# getter = None
# const = None
# payable = False
def unknown4c783bf5(): # not payable
  return not bool(munknown7a802c71)


# hash = 0x52cfe563
# getter = None
# const = None
# payable = False
def unknown52cfe563(addr m_param1, uint8 m_param2): # not payable
  require calldata.size - 4 >= 64
  if addr(mstor25m[addr(m_param1)m]m.field_256) == m_param1:
      if not uint8(mstor25m[addr(m_param1)m]m.field_672):
          [94midx = 0
          mwhile [94midx < mstor25m[addr(m_param1)m]m.field_768m:
              require [94midx < mstor25m[addr(m_param1)m]m.field_768
              if mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, ('param', '_param1')), ('name', 'stor25', 25))) + (0.03125 / idx))m[uint8([94midx)m] == m_param2:
                  return 1
              mem[0] = m_param1
              mem[32] = 25
              [94midx = [94midx + 1
              mcontinue 
          return 0
      else:
          return 0
  else:
      return 0


# hash = 0x5353a2d8
# getter = None
# const = None
# payable = False
def changeName(string m_newName): # not payable
  require calldata.size - 4 >= 32
  require m_newName <= 4294967296
  require m_newName + 36 <= calldata.size
  require m_newName.length <= 4294967296 and m_newName + m_newName.length + 36 <= calldata.size
  require caller == mowner
  require m_newName.length
  mem[192] = uint256(mnamem.field_0)
  [94midx = 192
  [94ms = 0
  mwhile mnamem.length + 192 > [94midx + 32m:
      mem[[94midx + 32] = mnamem[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[mnamem.length + (floor32(mnamem.length - 1) + -mnamem.length + 32 % 32) + 192] = m_newName.length
  mem[mnamem.length + (floor32(mnamem.length - 1) + -mnamem.length + 32 % 32) + 224 len m_newName.length] = m_newName[allm]
  mem[m_newName.length + mnamem.length + (floor32(mnamem.length - 1) + -mnamem.length + 32 % 32) + 224] = 0
  log 0x99b81fd1: Array(len=name.length, data=mem[192 len name.length + (floor32(name.length - 1) + -name.length + 32 % 32) + 32], _newName[all], mem[name.length + (floor32(name.length - 1) + -name.length + 32 % 32) + _newName.length + 224 len ceil32(_newName.length) - _newName.length]), name.length + (floor32(name.length - 1) + -name.length + 32 % 32) + 96
  mnamem.length = (2 * m_newName.length) + 1
  [94ms = 0
  [94midx = m_newName + 36
  mwhile m_newName + m_newName.length + 36 > [94midxm:
      mnamem[[94msm]m.field_0 = cd[[94midx]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      mcontinue 
  [94midx = Mask(251, 0, m_newName.length + 31) >> 5
  mwhile mnamem.length + 31 / 32 > [94midxm:
      mnamem[[94midxm]m.field_0 = 0
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x537c1ac7
# getter = None
# const = None
# payable = False
def unknown537c1ac7(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  if not m_param1:
      revert with 0, 'Invalid address'
  require ext_code.size(mdataStoreAddress)
  static call mdataStoreAddress.getAddress(bytes32 key) with:
          gas gas_remaining wei
         args 0xaae8817359f3dcb67d050f44f3e49f982e0359d90ca4b5f18569926304aaece6
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  log 0x419d7181: ext_call.return_data[12 len 20], addr(_param1)
  require ext_code.size(mdataStoreAddress)
  call mdataStoreAddress.setAddress(bytes32 key, address value) with:
       gas gas_remaining wei
      args 0xaae8817359f3dcb67d050f44f3e49f982e0359d90ca4b5f18569926304aaece6, m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x5488cc80
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def currentCheckpointId(): # not payable
  return mcurrentCheckpointId


# hash = 0x556f0dc7
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def granularity(): # not payable
  return mgranularity


# hash = 0x62b348c3
# getter = None
# const = None
# payable = False
def unknown62b348c3(uint256 m_param1, bool m_param2): # not payable
  require calldata.size - 4 >= 96
  require caller == mowner
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0xdfb1f411 with:
       gas gas_remaining wei
      args 0, 0, m_param1, m_param2, addr(munknown05d97f4fAddress), 25
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x62eb0068
# getter = None
# const = None
# payable = False
def unknown62eb0068(uint256 m_param1, uint256 m_param2, array m_param3): # not payable
  require calldata.size - 4 >= 96
  require m_param3 <= 4294967296
  require m_param3 + 36 <= calldata.size
  require m_param3.length <= 4294967296 and m_param3 + m_param3.length + 36 <= calldata.size
  require addr(mstor25m[callerm]m.field_256) == caller
  require not uint8(mstor25m[callerm]m.field_672)
  require 0 < mstor25m[callerm]m.field_768
  require 0 < mstor25m[callerm]m.field_768
  [94ms = 0
  mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor25', 25))) + (0.03125 / s))m[uint8([94ms)m] != 5m:
      require [94ms + 1 < mstor25m[callerm]m.field_768
      mem[32] = 25
      require [94ms + 1 < mstor25m[callerm]m.field_768
      mem[0] = sha3(caller, 25) + 3
      [94ms = [94ms + 1
      mcontinue 
  if m_param1 != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
      revert with 0, 'Invalid partition'
  mem[96] = m_param3.length
  mem[128 len m_param3.length] = m_param3[allm]
  mem[m_param3.length + 128] = 0
  mem[64] = ceil32(m_param3.length) + 160
  mem[ceil32(m_param3.length) + 128] = 0
  mstor3++
  mem[ceil32(m_param3.length) + 164] = uint256(mholderCount)
  mem[ceil32(m_param3.length) + 196] = caller
  mem[ceil32(m_param3.length) + 228] = 0
  mem[ceil32(m_param3.length) + 260] = m_param2
  mem[ceil32(m_param3.length) + 292] = mbalanceOf
  mem[ceil32(m_param3.length) + 324] = mbalanceOfm[callerm]
  mem[ceil32(m_param3.length) + 356] = mdataStoreAddress
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
       gas gas_remaining wei
      args uint256(mholderCount), caller, 0, m_param2, mbalanceOf, mbalanceOfm[callerm], mdataStoreAddress
  mem[ceil32(m_param3.length) + 160] = delegate.return_data[0]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mholderCount) = delegate.return_data[0]
  require mgranularity
  if m_param2 % mgranularity:
      revert with 0, 'Invalid granularity'
  if mtransfersFrozen:
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(caller, 28), mbalanceOfm[callerm], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mstor3 + 1 == mstor3
      require caller
      require m_param2 <= mtotalSupply
      mtotalSupply -= m_param2
      require m_param2 <= mbalanceOfm[callerm]
      mbalanceOfm[callerm] -= m_param2
      log Transfer(
            address from=_param2,
            address to=caller,
            uint256 value=0)
      log 0xb7d0d6b6: _param2, Array(len=_param3.length, data=_param3[all]), 0, caller
  else:
      mem[0] = 2
      mem[32] = 24
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          mem[0] = mstor2BACm[[94midxm]
          mem[32] = 25
          if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
              [94m_161 = mem[64]
              mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = caller
              mem[mem[64] + 36] = 0
              mem[mem[64] + 68] = m_param2
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = mem[96]
              [94mt = 0
              mwhile [94mt < mem[96]m:
                  mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                  [94mt = [94mt + 32
                  mcontinue 
              if not mem[96] % 32:
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len mem[96] + [94m_161 + -mem[64] + 160]
              else:
                  mem[floor32(mem[96]) + [94m_161 + 164] = mem[floor32(mem[96]) + [94m_161 + -(mem[96] % 32) + 196 len mem[96] % 32]
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len floor32(mem[96]) + [94m_161 + -mem[64] + 192]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
          [94midx = [94midx + 1
          [94ms = mstor2BACm[[94midxm]
          [94ms = [94ms
          mcontinue 
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(caller, 28), mbalanceOfm[callerm], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      mem[mem[64] + 68] = mcurrentCheckpointId
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mstor3 + 1 == mstor3
      require caller
      require m_param2 <= mtotalSupply
      mtotalSupply -= m_param2
      require m_param2 <= mbalanceOfm[callerm]
      mem[0] = caller
      mem[32] = 0
      mbalanceOfm[callerm] -= m_param2
      log Transfer(
            address from=_param2,
            address to=caller,
            uint256 value=0)
      mem[mem[64]] = m_param2
      mem[mem[64] + 32] = 64
      mem[mem[64] + 64] = mem[96]
      if [94ms:
          [94m_202 = mem[96]
          mem[mem[64] + 96 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
          if not mem[96] % 32:
              log 0xb7d0d6b6: _param2, 64, mem[mem[64] + 64 len mem[96] + 32], 0, caller
          else:
              mem[floor32(mem[96]) + mem[64] + 96] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 128 len mem[96] % 32]
              log 0xb7d0d6b6: _param2, 64, mem[mem[64] + 64 len floor32(_202) + 64], 0, caller
      else:
          [94m_205 = mem[96]
          mem[mem[64] + 96 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
          if not mem[96] % 32:
              log 0xb7d0d6b6: _param2, 64, mem[mem[64] + 64 len mem[96] + 32], 0, caller
          else:
              mem[floor32(mem[96]) + mem[64] + 96] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 128 len mem[96] % 32]
              log 0xb7d0d6b6: _param2, 64, mem[mem[64] + 64 len floor32(_205) + 64], 0, caller
  revert with 0, 'Invalid redeem'


# hash = 0x660d0d67
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def dataStore(): # not payable
  return mdataStoreAddress


# hash = 0x67c84919
# getter = None
# const = None
# payable = False
def unknown67c84919(uint256 m_param1, addr m_param2, uint256 m_param3, array m_param4): # not payable
  require calldata.size - 4 >= 128
  require m_param4 <= 4294967296
  require m_param4 + 36 <= calldata.size
  require m_param4.length <= 4294967296 and m_param4 + m_param4.length + 36 <= calldata.size
  if m_param1 != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
      revert with 0, 'Invalid partition'
  mem[64] = ceil32(m_param4.length) + 128
  mem[96] = m_param4.length
  mem[128 len m_param4.length] = m_param4[allm]
  mem[m_param4.length + 128] = 0
  if not mstor20:
      revert with 0, 'Issuance frozen'
  if caller == mowner:
      mstor3++
      mem[ceil32(m_param4.length) + 132] = uint256(mholderCount)
      mem[ceil32(m_param4.length) + 164] = 0
      mem[ceil32(m_param4.length) + 196] = m_param2
      mem[ceil32(m_param4.length) + 228] = m_param3
      mem[ceil32(m_param4.length) + 260] = mbalanceOfm[addr(m_param2)m]
      mem[ceil32(m_param4.length) + 292] = mbalanceOf
      mem[ceil32(m_param4.length) + 324] = mdataStoreAddress
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
           gas gas_remaining wei
          args uint256(mholderCount), 0, addr(m_param2), m_param3, mbalanceOfm[addr(m_param2)m], mbalanceOf, mdataStoreAddress
      mem[ceil32(m_param4.length) + 128] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mholderCount) = delegate.return_data[0]
      require mgranularity
      if m_param3 % mgranularity:
          revert with 0, 'Invalid granularity'
      if not mtransfersFrozen:
          mem[0] = 2
          mem[32] = 24
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              mem[0] = mstor2BACm[[94midxm]
              mem[32] = 25
              if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                  mem[ceil32(m_param4.length) + 128] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                  mem[ceil32(m_param4.length) + 132] = 0
                  mem[ceil32(m_param4.length) + 164] = m_param2
                  mem[ceil32(m_param4.length) + 196] = m_param3
                  mem[ceil32(m_param4.length) + 228] = 128
                  mem[ceil32(m_param4.length) + 260] = mem[96]
                  [94mt = 0
                  mwhile [94mt < mem[96]m:
                      mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                      [94mt = [94mt + 32
                      mcontinue 
                  if not mem[96] % 32:
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len mem[96] + ceil32(m_param4.length) + -mem[64] + 288]
                  else:
                      mem[floor32(mem[96]) + ceil32(m_param4.length) + 292] = mem[floor32(mem[96]) + ceil32(m_param4.length) + -(mem[96] % 32) + 324 len mem[96] % 32]
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_param4.length) + -mem[64] + 320]
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 3
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      [94ms = mstor2BACm[[94midxm]
                      [94ms = 1
                      mcontinue 
                  require ext_call.return_data[0] <= 3
                  if ext_call.return_data[0] != 2:
                      require ext_call.return_data[0] <= 3
              [94midx = [94midx + 1
              [94ms = mstor2BACm[[94midxm]
              [94ms = [94ms
              mcontinue 
  else:
      require addr(mstor25m[callerm]m.field_256) == caller
      require not uint8(mstor25m[callerm]m.field_672)
      require 0 < mstor25m[callerm]m.field_768
      require 0 < mstor25m[callerm]m.field_768
      [94ms = 0
      mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor25', 25))) + (0.03125 / s))m[uint8([94ms)m] != 3m:
          require [94ms + 1 < mstor25m[callerm]m.field_768
          mem[32] = 25
          require [94ms + 1 < mstor25m[callerm]m.field_768
          mem[0] = sha3(caller, 25) + 3
          [94ms = [94ms + 1
          mcontinue 
      mstor3++
      mem[ceil32(m_param4.length) + 132] = uint256(mholderCount)
      mem[ceil32(m_param4.length) + 164] = 0
      mem[ceil32(m_param4.length) + 196] = m_param2
      mem[ceil32(m_param4.length) + 228] = m_param3
      mem[ceil32(m_param4.length) + 260] = mbalanceOfm[addr(m_param2)m]
      mem[ceil32(m_param4.length) + 292] = mbalanceOf
      mem[ceil32(m_param4.length) + 324] = mdataStoreAddress
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
           gas gas_remaining wei
          args uint256(mholderCount), 0, addr(m_param2), m_param3, mbalanceOfm[addr(m_param2)m], mbalanceOf, mdataStoreAddress
      mem[ceil32(m_param4.length) + 128] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mholderCount) = delegate.return_data[0]
      require mgranularity
      if m_param3 % mgranularity:
          revert with 0, 'Invalid granularity'
      if not mtransfersFrozen:
          mem[0] = 2
          mem[32] = 24
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              mem[0] = mstor2BACm[[94midxm]
              mem[32] = 25
              if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                  [94m_178 = mem[64]
                  mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 0
                  mem[mem[64] + 36] = m_param2
                  mem[mem[64] + 68] = m_param3
                  mem[mem[64] + 100] = 128
                  mem[mem[64] + 132] = mem[96]
                  [94mt = 0
                  mwhile [94mt < mem[96]m:
                      mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                      [94mt = [94mt + 32
                      mcontinue 
                  if not mem[96] % 32:
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len mem[96] + [94m_178 + -mem[64] + 160]
                  else:
                      mem[floor32(mem[96]) + [94m_178 + 164] = mem[floor32(mem[96]) + [94m_178 + -(mem[96] % 32) + 196 len mem[96] % 32]
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len floor32(mem[96]) + [94m_178 + -mem[64] + 192]
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 3
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      [94ms = mstor2BACm[[94midxm]
                      [94ms = 1
                      mcontinue 
                  require ext_call.return_data[0] <= 3
                  if ext_call.return_data[0] != 2:
                      require ext_call.return_data[0] <= 3
              [94midx = [94midx + 1
              [94ms = mstor2BACm[[94midxm]
              [94ms = [94ms
              mcontinue 
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(m_param2), 28), mbalanceOfm[addr(m_param2)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mstor3 + 1 == mstor3
  revert with 0, 'Transfer Invalid'


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 0]]]
# const = None
# payable = False
def balanceOf(address m_tokenOwner): # not payable
  require calldata.size - 4 >= 32
  return mbalanceOfm[addr(m_tokenOwner)m]


# hash = 0x73826a93
# getter = None
# const = None
# payable = False
def updateTokenDetails(string m_newTokenDetails): # not payable
  require calldata.size - 4 >= 32
  require m_newTokenDetails <= 4294967296
  require m_newTokenDetails + 36 <= calldata.size
  require m_newTokenDetails.length <= 4294967296 and m_newTokenDetails + m_newTokenDetails.length + 36 <= calldata.size
  require caller == mowner
  mem[192] = uint256(mtokenDetailsm.field_0)
  [94midx = 192
  [94ms = 0
  mwhile mtokenDetailsm.length + 192 > [94midx + 32m:
      mem[[94midx + 32] = mtokenDetailsm[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[mtokenDetailsm.length + (floor32(mtokenDetailsm.length - 1) + -mtokenDetailsm.length + 32 % 32) + 192] = m_newTokenDetails.length
  mem[mtokenDetailsm.length + (floor32(mtokenDetailsm.length - 1) + -mtokenDetailsm.length + 32 % 32) + 224 len m_newTokenDetails.length] = m_newTokenDetails[allm]
  mem[m_newTokenDetails.length + mtokenDetailsm.length + (floor32(mtokenDetailsm.length - 1) + -mtokenDetailsm.length + 32 % 32) + 224] = 0
  log 0x4f5dc3fe: Array(len=tokenDetails.length, data=mem[192 len tokenDetails.length + (floor32(tokenDetails.length - 1) + -tokenDetails.length + 32 % 32) + 32], _newTokenDetails[all], mem[tokenDetails.length + (floor32(tokenDetails.length - 1) + -tokenDetails.length + 32 % 32) + _newTokenDetails.length + 224 len ceil32(_newTokenDetails.length) - _newTokenDetails.length]), tokenDetails.length + (floor32(tokenDetails.length - 1) + -tokenDetails.length + 32 % 32) + 96
  mtokenDetailsm.length = (2 * m_newTokenDetails.length) + 1
  [94ms = 0
  [94midx = m_newTokenDetails + 36
  mwhile m_newTokenDetails + m_newTokenDetails.length + 36 > [94midxm:
      mtokenDetailsm[[94msm]m.field_0 = cd[[94midx]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      mcontinue 
  [94midx = Mask(251, 0, m_newTokenDetails.length + 31) >> 5
  mwhile mtokenDetailsm.length + 31 / 32 > [94midxm:
      mtokenDetailsm[[94midxm]m.field_0 = 0
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x74c96372
# getter = None
# const = None
# payable = False
def unknown74c96372(array m_param1, array m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[96] = m_param1.length
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if not mstor20:
      revert with 0, 'Issuance frozen'
  if caller == mowner:
      require m_param1.length == m_param2.length
      if 0 >= m_param1.length:
          stop
      require 0 < m_param1.length
      [94m_11 = mem[128]
      require 0 < m_param2.length
      [94m_14 = mem[(32 * m_param1.length) + 160]
      mem[64] = (32 * m_param1.length) + (32 * m_param2.length) + 192
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
      mstor3++
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = uint256(mholderCount)
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = 0
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 260] = mem[140 len 20]
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 292] = [94m_14
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 324] = mbalanceOfm[addr(mem[128])m]
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 356] = mbalanceOf
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 388] = mdataStoreAddress
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
           gas gas_remaining wei
          args uint256(mholderCount), 0, mem[140 len 20], [94m_14, mbalanceOfm[addr(mem[128])m], mbalanceOf, mdataStoreAddress
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 192] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mholderCount) = delegate.return_data[0]
      require mgranularity
      if [94m_14 % mgranularity:
          revert with 0, 'Invalid granularity'
      if mtransfersFrozen:
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(addr(mem[128]), 28), mbalanceOfm[addr(mem[128])m], mcurrentCheckpointId
      else:
          mem[0] = 2
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              mem[0] = mstor2BACm[[94midxm]
              mem[32] = 25
              if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                  mem[(32 * m_param1.length) + (32 * m_param2.length) + 192] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                  mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = 0
                  mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = addr([94m_11)
                  mem[(32 * m_param1.length) + (32 * m_param2.length) + 260] = [94m_14
                  mem[(32 * m_param1.length) + (32 * m_param2.length) + 292] = 128
                  mem[(32 * m_param1.length) + (32 * m_param2.length) + 324] = mem[(32 * m_param1.length) + (32 * m_param2.length) + 160]
                  [94m_115 = mem[(32 * m_param1.length) + (32 * m_param2.length) + 160]
                  [94mt = 0
                  mwhile [94mt < [94m_115m:
                      mem[[94mt + mem[64] + 164] = mem[[94mt + (32 * m_param1.length) + (32 * m_param2.length) + 192]
                      [94mt = [94mt + 32
                      mcontinue 
                  if not [94m_115 % 32:
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len [94m_115 + (32 * m_param1.length) + (32 * m_param2.length) + -mem[64] + 352]
                  else:
                      mem[floor32([94m_115) + (32 * m_param1.length) + (32 * m_param2.length) + 356] = mem[floor32([94m_115) + (32 * m_param1.length) + (32 * m_param2.length) + -([94m_115 % 32) + 388 len [94m_115 % 32]
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len floor32([94m_115) + (32 * m_param1.length) + (32 * m_param2.length) + -mem[64] + 384]
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 3
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      [94ms = mstor2BACm[[94midxm]
                      [94ms = 1
                      mcontinue 
                  require ext_call.return_data[0] <= 3
                  if ext_call.return_data[0] != 2:
                      require ext_call.return_data[0] <= 3
              [94midx = [94midx + 1
              [94ms = mstor2BACm[[94midxm]
              [94ms = [94ms
              mcontinue 
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(addr([94m_11), 28), mbalanceOfm[addr([94m_11)m], mcurrentCheckpointId
  else:
      require addr(mstor25m[callerm]m.field_256) == caller
      require not uint8(mstor25m[callerm]m.field_672)
      require 0 < mstor25m[callerm]m.field_768
      require 0 < mstor25m[callerm]m.field_768
      [94ms = 0
      mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor25', 25))) + (0.03125 / s))m[uint8([94ms)m] != 3m:
          require [94ms + 1 < mstor25m[callerm]m.field_768
          mem[32] = 25
          require [94ms + 1 < mstor25m[callerm]m.field_768
          mem[0] = sha3(caller, 25) + 3
          [94ms = [94ms + 1
          mcontinue 
      require m_param1.length == m_param2.length
      if 0 >= m_param1.length:
          stop
      require 0 < m_param1.length
      [94m_136 = mem[128]
      require 0 < m_param2.length
      [94m_138 = mem[(32 * m_param1.length) + 160]
      mem[64] = (32 * m_param1.length) + (32 * m_param2.length) + 192
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
      mstor3++
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = uint256(mholderCount)
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = 0
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 260] = mem[140 len 20]
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 292] = [94m_138
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 324] = mbalanceOfm[addr(mem[128])m]
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 356] = mbalanceOf
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 388] = mdataStoreAddress
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
           gas gas_remaining wei
          args uint256(mholderCount), 0, mem[140 len 20], [94m_138, mbalanceOfm[addr(mem[128])m], mbalanceOf, mdataStoreAddress
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 192] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mholderCount) = delegate.return_data[0]
      require mgranularity
      if [94m_138 % mgranularity:
          revert with 0, 'Invalid granularity'
      if mtransfersFrozen:
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(addr(mem[128]), 28), mbalanceOfm[addr(mem[128])m], mcurrentCheckpointId
      else:
          mem[0] = 2
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              mem[0] = mstor2BACm[[94midxm]
              mem[32] = 25
              if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                  [94m_199 = mem[64]
                  mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 0
                  mem[mem[64] + 36] = addr([94m_136)
                  mem[mem[64] + 68] = [94m_138
                  mem[mem[64] + 100] = 128
                  mem[mem[64] + 132] = mem[(32 * m_param1.length) + (32 * m_param2.length) + 160]
                  [94m_201 = mem[(32 * m_param1.length) + (32 * m_param2.length) + 160]
                  [94mt = 0
                  mwhile [94mt < [94m_201m:
                      mem[[94mt + mem[64] + 164] = mem[[94mt + (32 * m_param1.length) + (32 * m_param2.length) + 192]
                      [94mt = [94mt + 32
                      mcontinue 
                  if not [94m_201 % 32:
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len [94m_201 + [94m_199 + -mem[64] + 160]
                  else:
                      mem[floor32([94m_201) + [94m_199 + 164] = mem[floor32([94m_201) + [94m_199 + -([94m_201 % 32) + 196 len [94m_201 % 32]
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len floor32([94m_201) + [94m_199 + -mem[64] + 192]
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 3
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      [94ms = mstor2BACm[[94midxm]
                      [94ms = 1
                      mcontinue 
                  require ext_call.return_data[0] <= 3
                  if ext_call.return_data[0] != 2:
                      require ext_call.return_data[0] <= 3
              [94midx = [94midx + 1
              [94ms = mstor2BACm[[94midxm]
              [94ms = [94ms
              mcontinue 
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
               gas gas_remaining wei
              args sha3(addr([94m_136), 28), mbalanceOfm[addr([94m_136)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mstor3 + 1 == mstor3
  revert with 0, 'Transfer Invalid'


# hash = 0x74fee0c0
# getter = None
# const = None
# payable = False
def unknown74fee0c0(array m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + m_param1.length + 36 <= calldata.size
  require caller == mowner
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x5a34d4d9 with:
       gas gas_remaining wei
      args Array(len=m_param1.length, data=m_param1[allm])
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mowner != delegate.return_data[12 len 20]:
      revert with 0, 'Owner did not sign'
  require not munknown7a802c71
  munknown7a802c71 = 1
  mcontrollerAddress = 0
  log 0xf7ec83c3 


# hash = 0x7a802c71
# getter = ['bool', ['storage', 8, 0, 18]]
# const = None
# payable = False
def unknown7a802c71(): # not payable
  return bool(munknown7a802c71)


# hash = 0x8c0dee9c
# getter = None
# const = None
# payable = False
def unknown8c0dee9c(): # not payable
  require calldata.size - 4 >= 192
  require cd[132] <= 4294967296
  require cd[132] + 36 <= calldata.size
  require m('cd', 132).length <= 4294967296 and cd[132] + m('cd', 132).length + 36 <= calldata.size
  require cd[164] <= 4294967296
  require cd[164] + 36 <= calldata.size
  require m('cd', 164).length <= 4294967296 and cd[164] + m('cd', 164).length + 36 <= calldata.size
  if cd[4] != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
      revert with 0, 'Invalid partition'
  if uint256(mallowancem[addr(cd[36])m]m[callerm]) == -1:
      require 0 < m('cd', 164).length
      require Mask(8, 248, m('cd', 164)[0]) != 0
      mem[96] = m('cd', 132).length
      mem[128 len m('cd', 132).length] = call.data[cd[132] + 36 len m('cd', 132).length]
      mem[m('cd', 132).length + 128] = 0
      mem[ceil32(m('cd', 132).length) + 128] = m('cd', 164).length
      mem[ceil32(m('cd', 132).length) + 160 len m('cd', 164).length] = call.data[cd[164] + 36 len m('cd', 164).length]
      mem[ceil32(m('cd', 132).length) + m('cd', 164).length + 160] = 0
      if cd[4] != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
          revert with 0, 'Invalid partition'
      mem[64] = ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 192
      mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + 160] = mstor2BACm.length
      if not mstor2BACm.length:
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              require [94midx < mstor2BACm.length
              [94m_136 = mem[(32 * [94midx) + ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + 192]
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 196] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 228] = addr(cd[68])
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 260] = 0
              require ext_code.size(addr([94m_136))
              static call addr([94m_136).0x2829e651 with:
                      gas gas_remaining wei
                     args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(cd[68]), 0
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if [94ms >= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  mcontinue 
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              [94ms = ext_call.return_data[0]
              mcontinue 
          mstor3++
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 196] = uint256(mholderCount)
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 228] = addr(cd[36])
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 260] = addr(cd[68])
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 292] = cd[100]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 324] = mbalanceOfm[addr(cd[68])m]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 356] = mbalanceOfm[addr(cd[36])m]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 388] = mdataStoreAddress
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
               gas gas_remaining wei
              args uint256(mholderCount), addr(cd[36]), addr(cd[68]), cd[100], mbalanceOfm[addr(cd[68])m], mbalanceOfm[addr(cd[36])m], mdataStoreAddress
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 192] = delegate.return_data[0]
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          uint256(mholderCount) = delegate.return_data[0]
          require mgranularity
          if cd[100] % mgranularity:
              revert with 0, 'Invalid granularity'
          if not mtransfersFrozen:
              mem[0] = 2
              mem[32] = 24
              [94midx = 0
              [94ms = 0
              [94ms = 0
              mwhile [94midx < mstor2BACm.lengthm:
                  mem[0] = mstor2BACm[[94midxm]
                  mem[32] = 25
                  if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                      [94m_240 = mem[64]
                      mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 4] = addr(cd[36])
                      mem[mem[64] + 36] = addr(cd[68])
                      mem[mem[64] + 68] = cd[100]
                      mem[mem[64] + 100] = 128
                      mem[mem[64] + 132] = mem[96]
                      [94mt = 0
                      mwhile [94mt < mem[96]m:
                          mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                          [94mt = [94mt + 32
                          mcontinue 
                      if not mem[96] % 32:
                          require ext_code.size(mstor2BACm[[94midxm])
                          call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                               gas gas_remaining wei
                              args mem[mem[64] + 4 len mem[96] + [94m_240 + -mem[64] + 160]
                      else:
                          mem[floor32(mem[96]) + [94m_240 + 164] = mem[floor32(mem[96]) + [94m_240 + -(mem[96] % 32) + 196 len mem[96] % 32]
                          require ext_code.size(mstor2BACm[[94midxm])
                          call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                               gas gas_remaining wei
                              args mem[mem[64] + 4 len floor32(mem[96]) + [94m_240 + -mem[64] + 192]
                      mem[mem[64]] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 3
                      if not ext_call.return_data[0]:
                          [94midx = [94midx + 1
                          [94ms = mstor2BACm[[94midxm]
                          [94ms = 1
                          mcontinue 
                      require ext_call.return_data[0] <= 3
                      if ext_call.return_data[0] != 2:
                          require ext_call.return_data[0] <= 3
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = [94ms
                  mcontinue 
      else:
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + 192] = mstor2BAC
          [94midx = ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + 192
          [94ms = sha3(0x2bacf7cca723d030d12aee795132f2c5f2d14ad131f16f3f27eeba3e79d18b8c)
          mwhile ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 160 > [94midxm:
              mem[[94midx + 32] = addr(mallowancem[[94msm])
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              require [94midx < mstor2BACm.length
              [94m_406 = mem[(32 * [94midx) + ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + 192]
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 196] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 228] = addr(cd[68])
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 260] = 0
              require ext_code.size(addr([94m_406))
              static call addr([94m_406).0x2829e651 with:
                      gas gas_remaining wei
                     args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(cd[68]), 0
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if [94ms >= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  mcontinue 
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              [94ms = ext_call.return_data[0]
              mcontinue 
          mstor3++
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 196] = uint256(mholderCount)
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 228] = addr(cd[36])
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 260] = addr(cd[68])
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 292] = cd[100]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 324] = mbalanceOfm[addr(cd[68])m]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 356] = mbalanceOfm[addr(cd[36])m]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 388] = mdataStoreAddress
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
               gas gas_remaining wei
              args uint256(mholderCount), addr(cd[36]), addr(cd[68]), cd[100], mbalanceOfm[addr(cd[68])m], mbalanceOfm[addr(cd[36])m], mdataStoreAddress
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 192] = delegate.return_data[0]
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          uint256(mholderCount) = delegate.return_data[0]
          require mgranularity
          if cd[100] % mgranularity:
              revert with 0, 'Invalid granularity'
          if not mtransfersFrozen:
              mem[0] = 2
              mem[32] = 24
              [94midx = 0
              [94ms = 0
              [94ms = 0
              mwhile [94midx < mstor2BACm.lengthm:
                  mem[0] = mstor2BACm[[94midxm]
                  mem[32] = 25
                  if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                      [94m_518 = mem[64]
                      mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 4] = addr(cd[36])
                      mem[mem[64] + 36] = addr(cd[68])
                      mem[mem[64] + 68] = cd[100]
                      mem[mem[64] + 100] = 128
                      mem[mem[64] + 132] = mem[96]
                      [94mt = 0
                      mwhile [94mt < mem[96]m:
                          mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                          [94mt = [94mt + 32
                          mcontinue 
                      if not mem[96] % 32:
                          require ext_code.size(mstor2BACm[[94midxm])
                          call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                               gas gas_remaining wei
                              args mem[mem[64] + 4 len mem[96] + [94m_518 + -mem[64] + 160]
                      else:
                          mem[floor32(mem[96]) + [94m_518 + 164] = mem[floor32(mem[96]) + [94m_518 + -(mem[96] % 32) + 196 len mem[96] % 32]
                          require ext_code.size(mstor2BACm[[94midxm])
                          call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                               gas gas_remaining wei
                              args mem[mem[64] + 4 len floor32(mem[96]) + [94m_518 + -mem[64] + 192]
                      mem[mem[64]] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 3
                      if not ext_call.return_data[0]:
                          [94midx = [94midx + 1
                          [94ms = mstor2BACm[[94midxm]
                          [94ms = 1
                          mcontinue 
                      require ext_call.return_data[0] <= 3
                      if ext_call.return_data[0] != 2:
                          require ext_call.return_data[0] <= 3
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = [94ms
                  mcontinue 
  else:
      if not mstor31m[addr(cd[36])m]m[cd[4]m]m[callerm]:
          revert with 0, 'Not Authorised'
      require 0 < m('cd', 164).length
      require Mask(8, 248, m('cd', 164)[0]) != 0
      mem[96] = m('cd', 132).length
      mem[128 len m('cd', 132).length] = call.data[cd[132] + 36 len m('cd', 132).length]
      mem[m('cd', 132).length + 128] = 0
      mem[ceil32(m('cd', 132).length) + 128] = m('cd', 164).length
      mem[ceil32(m('cd', 132).length) + 160 len m('cd', 164).length] = call.data[cd[164] + 36 len m('cd', 164).length]
      mem[ceil32(m('cd', 132).length) + m('cd', 164).length + 160] = 0
      if cd[4] != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
          revert with 0, 'Invalid partition'
      mem[64] = ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 192
      mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + 160] = mstor2BACm.length
      if not mstor2BACm.length:
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              require [94midx < mstor2BACm.length
              [94m_139 = mem[(32 * [94midx) + ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + 192]
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 196] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 228] = addr(cd[68])
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 260] = 0
              require ext_code.size(addr([94m_139))
              static call addr([94m_139).0x2829e651 with:
                      gas gas_remaining wei
                     args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(cd[68]), 0
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if [94ms >= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  mcontinue 
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              [94ms = ext_call.return_data[0]
              mcontinue 
          mstor3++
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 196] = uint256(mholderCount)
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 228] = addr(cd[36])
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 260] = addr(cd[68])
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 292] = cd[100]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 324] = mbalanceOfm[addr(cd[68])m]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 356] = mbalanceOfm[addr(cd[36])m]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 388] = mdataStoreAddress
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
               gas gas_remaining wei
              args uint256(mholderCount), addr(cd[36]), addr(cd[68]), cd[100], mbalanceOfm[addr(cd[68])m], mbalanceOfm[addr(cd[36])m], mdataStoreAddress
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 192] = delegate.return_data[0]
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          uint256(mholderCount) = delegate.return_data[0]
          require mgranularity
          if cd[100] % mgranularity:
              revert with 0, 'Invalid granularity'
          if not mtransfersFrozen:
              mem[0] = 2
              mem[32] = 24
              [94midx = 0
              [94ms = 0
              [94ms = 0
              mwhile [94midx < mstor2BACm.lengthm:
                  mem[0] = mstor2BACm[[94midxm]
                  mem[32] = 25
                  if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                      [94m_246 = mem[64]
                      mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 4] = addr(cd[36])
                      mem[mem[64] + 36] = addr(cd[68])
                      mem[mem[64] + 68] = cd[100]
                      mem[mem[64] + 100] = 128
                      mem[mem[64] + 132] = mem[96]
                      [94mt = 0
                      mwhile [94mt < mem[96]m:
                          mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                          [94mt = [94mt + 32
                          mcontinue 
                      if not mem[96] % 32:
                          require ext_code.size(mstor2BACm[[94midxm])
                          call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                               gas gas_remaining wei
                              args mem[mem[64] + 4 len mem[96] + [94m_246 + -mem[64] + 160]
                      else:
                          mem[floor32(mem[96]) + [94m_246 + 164] = mem[floor32(mem[96]) + [94m_246 + -(mem[96] % 32) + 196 len mem[96] % 32]
                          require ext_code.size(mstor2BACm[[94midxm])
                          call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                               gas gas_remaining wei
                              args mem[mem[64] + 4 len floor32(mem[96]) + [94m_246 + -mem[64] + 192]
                      mem[mem[64]] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 3
                      if not ext_call.return_data[0]:
                          [94midx = [94midx + 1
                          [94ms = mstor2BACm[[94midxm]
                          [94ms = 1
                          mcontinue 
                      require ext_call.return_data[0] <= 3
                      if ext_call.return_data[0] != 2:
                          require ext_call.return_data[0] <= 3
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = [94ms
                  mcontinue 
      else:
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + 192] = mstor2BAC
          [94midx = ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + 192
          [94ms = sha3(0x2bacf7cca723d030d12aee795132f2c5f2d14ad131f16f3f27eeba3e79d18b8c)
          mwhile ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 160 > [94midxm:
              mem[[94midx + 32] = addr(mallowancem[[94msm])
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              require [94midx < mstor2BACm.length
              [94m_411 = mem[(32 * [94midx) + ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + 192]
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 196] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 228] = addr(cd[68])
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 260] = 0
              require ext_code.size(addr([94m_411))
              static call addr([94m_411).0x2829e651 with:
                      gas gas_remaining wei
                     args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(cd[68]), 0
              mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if [94ms >= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  [94ms = [94ms
                  mcontinue 
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              [94ms = ext_call.return_data[0]
              mcontinue 
          mstor3++
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 196] = uint256(mholderCount)
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 228] = addr(cd[36])
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 260] = addr(cd[68])
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 292] = cd[100]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 324] = mbalanceOfm[addr(cd[68])m]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 356] = mbalanceOfm[addr(cd[36])m]
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 388] = mdataStoreAddress
          require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
          [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
               gas gas_remaining wei
              args uint256(mholderCount), addr(cd[36]), addr(cd[68]), cd[100], mbalanceOfm[addr(cd[68])m], mbalanceOfm[addr(cd[36])m], mdataStoreAddress
          mem[ceil32(m('cd', 132).length) + ceil32(m('cd', 164).length) + (32 * mstor2BACm.length) + 192] = delegate.return_data[0]
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          uint256(mholderCount) = delegate.return_data[0]
          require mgranularity
          if cd[100] % mgranularity:
              revert with 0, 'Invalid granularity'
          if not mtransfersFrozen:
              mem[0] = 2
              mem[32] = 24
              [94midx = 0
              [94ms = 0
              [94ms = 0
              mwhile [94midx < mstor2BACm.lengthm:
                  mem[0] = mstor2BACm[[94midxm]
                  mem[32] = 25
                  if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                      [94m_521 = mem[64]
                      mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                      mem[mem[64] + 4] = addr(cd[36])
                      mem[mem[64] + 36] = addr(cd[68])
                      mem[mem[64] + 68] = cd[100]
                      mem[mem[64] + 100] = 128
                      mem[mem[64] + 132] = mem[96]
                      [94mt = 0
                      mwhile [94mt < mem[96]m:
                          mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                          [94mt = [94mt + 32
                          mcontinue 
                      if not mem[96] % 32:
                          require ext_code.size(mstor2BACm[[94midxm])
                          call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                               gas gas_remaining wei
                              args mem[mem[64] + 4 len mem[96] + [94m_521 + -mem[64] + 160]
                      else:
                          mem[floor32(mem[96]) + [94m_521 + 164] = mem[floor32(mem[96]) + [94m_521 + -(mem[96] % 32) + 196 len mem[96] % 32]
                          require ext_code.size(mstor2BACm[[94midxm])
                          call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                               gas gas_remaining wei
                              args mem[mem[64] + 4 len floor32(mem[96]) + [94m_521 + -mem[64] + 192]
                      mem[mem[64]] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= 3
                      if not ext_call.return_data[0]:
                          [94midx = [94midx + 1
                          [94ms = mstor2BACm[[94midxm]
                          [94ms = 1
                          mcontinue 
                      require ext_call.return_data[0] <= 3
                      if ext_call.return_data[0] != 2:
                          require ext_call.return_data[0] <= 3
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = [94ms
                  mcontinue 
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(cd[36]), 28), mbalanceOfm[addr(cd[36])m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(cd[68]), 28), mbalanceOfm[addr(cd[68])m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mstor3 + 1 == mstor3
  revert with 0, 'Transfer Invalid'


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 4]
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


# hash = 0x92eefe9b
# getter = None
# const = None
# payable = False
def setController(address m_controller): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require not munknown7a802c71
  log 0x9fdb0721: controllerAddress, _controller
  mcontrollerAddress = m_controller


# hash = 0x942df325
# getter = None
# const = None
# payable = False
def unknown942df325(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  if not m_param1:
      revert with 0, 'Invalid address'
  mdataStoreAddress = m_param1


# hash = 0x959b8c3f
# getter = None
# const = None
# payable = False
def authorizeOperator(address m_operator): # not payable
  require calldata.size - 4 >= 32
  require m_operator
  require caller
  uint256(mallowancem[callerm]m[addr(m_operator)m]) = -1
  log Approval(
        address owner=-1,
        address spender=caller,
        uint256 value=_operator)
  log AuthorizedOperator(
        address operator=_operator,
        address tokenHolder=caller)


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 7]]]], ['loc', 7]]]
# const = None
# payable = False
def symbol(): # not payable
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0x9675193c
# getter = None
# const = None
# payable = False
def unknown9675193c(addr m_param1, uint256 m_param2, array m_param3): # not payable
  require calldata.size - 4 >= 96
  require m_param3 <= 4294967296
  require m_param3 + 36 <= calldata.size
  require m_param3.length <= 4294967296 and m_param3 + m_param3.length + 36 <= calldata.size
  require addr(mstor25m[callerm]m.field_256) == caller
  require not uint8(mstor25m[callerm]m.field_672)
  require 0 < mstor25m[callerm]m.field_768
  require 0 < mstor25m[callerm]m.field_768
  [94ms = 0
  mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor25', 25))) + (0.03125 / s))m[uint8([94ms)m] != 5m:
      require [94ms + 1 < mstor25m[callerm]m.field_768
      mem[32] = 25
      require [94ms + 1 < mstor25m[callerm]m.field_768
      mem[0] = sha3(caller, 25) + 3
      [94ms = [94ms + 1
      mcontinue 
  mem[64] = ceil32(m_param3.length) + 128
  mem[96] = m_param3.length
  mem[128 len m_param3.length] = m_param3[allm]
  mem[m_param3.length + 128] = 0
  mstor3++
  mem[ceil32(m_param3.length) + 132] = uint256(mholderCount)
  mem[ceil32(m_param3.length) + 164] = m_param1
  mem[ceil32(m_param3.length) + 196] = 0
  mem[ceil32(m_param3.length) + 228] = m_param2
  mem[ceil32(m_param3.length) + 260] = mbalanceOf
  mem[ceil32(m_param3.length) + 292] = mbalanceOfm[addr(m_param1)m]
  mem[ceil32(m_param3.length) + 324] = mdataStoreAddress
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
       gas gas_remaining wei
      args uint256(mholderCount), addr(m_param1), 0, m_param2, mbalanceOf, mbalanceOfm[addr(m_param1)m], mdataStoreAddress
  mem[ceil32(m_param3.length) + 128] = delegate.return_data[0]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mholderCount) = delegate.return_data[0]
  require mgranularity
  if m_param2 % mgranularity:
      revert with 0, 'Invalid granularity'
  if not mtransfersFrozen:
      mem[0] = 2
      mem[32] = 24
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          mem[0] = mstor2BACm[[94midxm]
          mem[32] = 25
          if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
              [94m_95 = mem[64]
              mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = m_param1
              mem[mem[64] + 36] = 0
              mem[mem[64] + 68] = m_param2
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = mem[96]
              [94mt = 0
              mwhile [94mt < mem[96]m:
                  mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                  [94mt = [94mt + 32
                  mcontinue 
              if not mem[96] % 32:
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len mem[96] + [94m_95 + -mem[64] + 160]
              else:
                  mem[floor32(mem[96]) + [94m_95 + 164] = mem[floor32(mem[96]) + [94m_95 + -(mem[96] % 32) + 196 len mem[96] % 32]
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len floor32(mem[96]) + [94m_95 + -mem[64] + 192]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
          [94midx = [94midx + 1
          [94ms = mstor2BACm[[94midxm]
          [94ms = [94ms
          mcontinue 
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(m_param1), 28), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mstor3 + 1 == mstor3
  revert with 0, 'Invalid redeem'


# hash = 0x9945e70e
# getter = None
# const = None
# payable = False
def unknown9945e70e(addr m_param1, addr m_param2, uint256 m_param3, uint256 m_param4, array m_param5): # not payable
  require calldata.size - 4 >= 160
  require m_param5 <= 4294967296
  require m_param5 + 36 <= calldata.size
  require m_param5.length <= 4294967296 and m_param5 + m_param5.length + 36 <= calldata.size
  if m_param3 != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
      return 0x5000000000000000000000000000000000000000000000000000000000000000, 0, 0
  mem[128 len m_param5.length] = m_param5[allm]
  mem[m_param5.length + 128] = 0
  require mgranularity
  if m_param4 % mgranularity:
      mem[ceil32(m_param5.length) + 128] = 0x5000000000000000000000000000000000000000000000000000000000000000
      mem[ceil32(m_param5.length) + 160] = 0
      return Mask(8 * -ceil32(m_param5.length) + m_param5.length + 32, 0, 0), 
             mem[m_param5.length + 160 len ceil32(m_param5.length) + -m_param5.length + 32],
             0
  mem[ceil32(m_param5.length) + 128] = 0x1658f46a00000000000000000000000000000000000000000000000000000000
  mem[ceil32(m_param5.length) + 324] = bool(mtransfersFrozen)
  mem[ceil32(m_param5.length) + 292] = 224
  mem[ceil32(m_param5.length) + 356] = m_param5.length
  mem[ceil32(m_param5.length) + 388 len ceil32(m_param5.length)] = m_param5[allm], mem[m_param5.length + 128 len ceil32(m_param5.length) - m_param5.length]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x0 with:
       gas gas_remaining wei
      args sha3(2, 24), 25, addr(m_param1), addr(m_param2), m_param4, Array(len=m_param5.length, data=m_param5[allm]), bool(mtransfersFrozen)
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  mem[ceil32(m_param5.length) + 164] = delegate.return_data[32]
  mem[ceil32(m_param5.length) + 196] = m_param2
  mem[ceil32(m_param5.length) + 228] = m_param4
  mem[ceil32(m_param5.length) + 260] = mbalanceOfm[addr(m_param1)m]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x2c94d97b with:
       gas gas_remaining wei
      args bool(delegate.return_data[0]), delegate.return_data[32], addr(m_param2), m_param4, mbalanceOfm[addr(m_param1)m]
  mem[ceil32(m_param5.length) + 128 len 64] = delegate.return_data[0 len 64]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if Mask(4, 248, delegate.return_data[0]) != 0x100000000000000000000000000000000000000000000000000000000000000:
      return 0, 0, delegate.return_data[32], 0
  if not mstor2BACm.length:
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          require [94midx < mstor2BACm.length
          [94m_206 = mem[(32 * [94midx) + ceil32(m_param5.length) + 160]
          mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 164] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
          mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 196] = m_param2
          mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 228] = 0
          require ext_code.size(addr([94m_206))
          static call addr([94m_206).0x2829e651 with:
                  gas gas_remaining wei
                 args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(m_param2), 0
          mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if [94ms >= ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              [94ms = [94ms
              mcontinue 
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          [94ms = ext_call.return_data[0]
          mcontinue 
      mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 160] = mstor2BACm.length
      if not mstor2BACm.length:
          [94midx = 0
          [94mt = 0
          [94mt = 0
          mwhile [94midx < mstor2BACm.lengthm:
              require [94midx < mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 160]
              [94m_266 = mem[(32 * [94midx) + ceil32(m_param5.length) + (32 * mstor2BACm.length) + 192]
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 196] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 228] = m_param2
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 260] = m_param4
              require ext_code.size(addr([94m_266))
              static call addr([94m_266).0x2829e651 with:
                      gas gas_remaining wei
                     args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(m_param2), m_param4
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if [94mt >= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94mt = ext_call.return_data[0]
                  [94mt = [94mt
                  mcontinue 
              [94midx = [94midx + 1
              [94mt = ext_call.return_data[0]
              [94mt = ext_call.return_data[0]
              mcontinue 
      else:
          mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 192] = mstor2BAC
          [94midx = ceil32(m_param5.length) + (32 * mstor2BACm.length) + 192
          [94mt = sha3(0x2bacf7cca723d030d12aee795132f2c5f2d14ad131f16f3f27eeba3e79d18b8c)
          mwhile ceil32(m_param5.length) + (64 * mstor2BACm.length) + 160 > [94midxm:
              mem[[94midx + 32] = addr(mallowancem[[94mtm])
              [94midx = [94midx + 32
              [94mt = [94mt + 1
              mcontinue 
          [94midx = 0
          [94mt = 0
          [94mt = 0
          mwhile [94midx < mstor2BACm.lengthm:
              require [94midx < mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 160]
              [94m_456 = mem[(32 * [94midx) + ceil32(m_param5.length) + (32 * mstor2BACm.length) + 192]
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 196] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 228] = m_param2
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 260] = m_param4
              require ext_code.size(addr([94m_456))
              static call addr([94m_456).0x2829e651 with:
                      gas gas_remaining wei
                     args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(m_param2), m_param4
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if [94mt >= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94mt = ext_call.return_data[0]
                  [94mt = [94mt
                  mcontinue 
              [94midx = [94midx + 1
              [94mt = ext_call.return_data[0]
              [94mt = ext_call.return_data[0]
              mcontinue 
  else:
      mem[ceil32(m_param5.length) + 160] = mstor2BAC
      [94midx = ceil32(m_param5.length) + 160
      [94ms = sha3(0x2bacf7cca723d030d12aee795132f2c5f2d14ad131f16f3f27eeba3e79d18b8c)
      mwhile ceil32(m_param5.length) + (32 * mstor2BACm.length) + 128 > [94midxm:
          mem[[94midx + 32] = addr(mallowancem[[94msm])
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          require [94midx < mstor2BACm.length
          [94m_363 = mem[(32 * [94midx) + ceil32(m_param5.length) + 160]
          mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 164] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
          mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 196] = m_param2
          mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 228] = 0
          require ext_code.size(addr([94m_363))
          static call addr([94m_363).0x2829e651 with:
                  gas gas_remaining wei
                 args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(m_param2), 0
          mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if [94ms >= ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              [94ms = [94ms
              mcontinue 
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          [94ms = ext_call.return_data[0]
          mcontinue 
      mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 160] = mstor2BACm.length
      if not mstor2BACm.length:
          [94midx = 0
          [94mt = 0
          [94mt = 0
          mwhile [94midx < mstor2BACm.lengthm:
              require [94midx < mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 160]
              [94m_459 = mem[(32 * [94midx) + ceil32(m_param5.length) + (32 * mstor2BACm.length) + 192]
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 196] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 228] = m_param2
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 260] = m_param4
              require ext_code.size(addr([94m_459))
              static call addr([94m_459).0x2829e651 with:
                      gas gas_remaining wei
                     args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(m_param2), m_param4
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if [94mt >= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94mt = ext_call.return_data[0]
                  [94mt = [94mt
                  mcontinue 
              [94midx = [94midx + 1
              [94mt = ext_call.return_data[0]
              [94mt = ext_call.return_data[0]
              mcontinue 
      else:
          mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 192] = mstor2BAC
          [94midx = ceil32(m_param5.length) + (32 * mstor2BACm.length) + 192
          [94mt = sha3(0x2bacf7cca723d030d12aee795132f2c5f2d14ad131f16f3f27eeba3e79d18b8c)
          mwhile ceil32(m_param5.length) + (64 * mstor2BACm.length) + 160 > [94midxm:
              mem[[94midx + 32] = addr(mallowancem[[94mtm])
              [94midx = [94midx + 32
              [94mt = [94mt + 1
              mcontinue 
          [94midx = 0
          [94mt = 0
          [94mt = 0
          mwhile [94midx < mstor2BACm.lengthm:
              require [94midx < mem[ceil32(m_param5.length) + (32 * mstor2BACm.length) + 160]
              [94m_554 = mem[(32 * [94midx) + ceil32(m_param5.length) + (32 * mstor2BACm.length) + 192]
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 196] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 228] = m_param2
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 260] = m_param4
              require ext_code.size(addr([94m_554))
              static call addr([94m_554).0x2829e651 with:
                      gas gas_remaining wei
                     args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(m_param2), m_param4
              mem[ceil32(m_param5.length) + (64 * mstor2BACm.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if [94mt >= ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94mt = ext_call.return_data[0]
                  [94mt = [94mt
                  mcontinue 
              [94midx = [94midx + 1
              [94mt = ext_call.return_data[0]
              [94mt = ext_call.return_data[0]
              mcontinue 
  require [94ms <= [94mt
  if [94mt - [94ms == m_param4:
      return Mask(8, 248, delegate.return_data[0]), 
             delegate.return_data[32],
             0xfe4c4f434b454400000000000000000000000000000000000000000000000000
  return Mask(8, 248, delegate.return_data[0]), 
         delegate.return_data[32],
         0x554e4c4f434b45440000000000000000000000000000000000000000000000


# hash = 0xa0632461
# getter = None
# const = None
# payable = False
def unknowna0632461(): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0xc38890e1 with:
       gas gas_remaining wei
      args 0, 0, 24, 25, 26
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xa16c3a09
# getter = None
# const = None
# payable = False
def unknowna16c3a09(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x4a02280e with:
       gas gas_remaining wei
      args addr(mmoduleRegistryAddress), sha3(addr(m_param1), 25)
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xa1db9782
# getter = None
# const = None
# payable = False
def withdrawERC20(address m_contractAddress, uint256 m_amount): # not payable
  require calldata.size - 4 >= 64
  require caller == mowner
  require ext_code.size(m_contractAddress)
  call m_contractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mowner, m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]


# hash = 0xa457c2d7
# getter = None
# const = None
# payable = False
def decreaseAllowance(address m_spender, uint256 m_subtractedValue): # not payable
  require calldata.size - 4 >= 64
  require m_subtractedValue <= uint256(mallowancem[callerm]m[addr(m_spender)m])
  require m_spender
  require caller
  uint256(mallowancem[callerm]m[addr(m_spender)m]) = uint256(mallowancem[callerm]m[addr(m_spender)m]) - m_subtractedValue
  log Approval(
        address owner=(uint256(allowance[caller][addr(_spender)]) - _subtractedValue),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_tokens): # not payable
  require calldata.size - 4 >= 64
  mem[64] = 128
  mem[96] = 0
  mstor3++
  mem[132] = uint256(mholderCount)
  mem[164] = caller
  mem[196] = m_to
  mem[228] = m_tokens
  mem[260] = mbalanceOfm[addr(m_to)m]
  mem[292] = mbalanceOfm[callerm]
  mem[324] = mdataStoreAddress
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
       gas gas_remaining wei
      args 0, uint32(mstor19), caller, addr(m_to), m_tokens, mbalanceOfm[addr(m_to)m], mbalanceOfm[callerm], mdataStoreAddress
  mem[128] = delegate.return_data[0]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mholderCount) = delegate.return_data[0]
  require mgranularity
  if m_tokens % mgranularity:
      revert with 0, 'Invalid granularity'
  if not mtransfersFrozen:
      mem[0] = 2
      mem[32] = 24
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          mem[0] = mstor2BACm[[94midxm]
          mem[32] = 25
          if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
              [94m_45 = mem[64]
              mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = caller
              mem[mem[64] + 36] = m_to
              mem[mem[64] + 68] = m_tokens
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = mem[96]
              [94mt = 0
              mwhile [94mt < mem[96]m:
                  mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                  [94mt = [94mt + 32
                  mcontinue 
              if not mem[96] % 32:
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len mem[96] + [94m_45 + -mem[64] + 160]
              else:
                  mem[floor32(mem[96]) + [94m_45 + 164] = mem[floor32(mem[96]) + [94m_45 + -(mem[96] % 32) + 196 len mem[96] % 32]
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len floor32(mem[96]) + [94m_45 + -mem[64] + 192]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
          [94midx = [94midx + 1
          [94ms = mstor2BACm[[94midxm]
          [94ms = [94ms
          mcontinue 
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(caller, 28), mbalanceOfm[callerm], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(m_to), 28), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mstor3 + 1 == mstor3
  revert with 0, 'Transfer Invalid'


# hash = 0xa9f86e2c
# getter = None
# const = None
# payable = False
def unknowna9f86e2c(addr m_param1, array m_param2, uint256 m_param3, uint256 m_param4, bool m_param5): # not payable
  require calldata.size - 4 >= 160
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + m_param2.length + 36 <= calldata.size
  mem[96] = m_param2.length
  mem[128 len m_param2.length] = m_param2[allm]
  mem[m_param2.length + 128] = 0
  mstor3++
  require caller == mowner
  mem[ceil32(m_param2.length) + 132] = m_param1
  mem[ceil32(m_param2.length) + 164] = 0
  require ext_code.size(addr(mmoduleRegistryAddress))
  call addr(mmoduleRegistryAddress).0x36ef22ce with:
       gas gas_remaining wei
      args addr(m_param1), 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(m_param2.length) + 128] = 0xb4579d6000000000000000000000000000000000000000000000000000000000
  require ext_code.size(m_param1)
  static call m_param1.getTypes() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(m_param2.length) + 128 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(m_param2.length) + ceil32(return_data.size) + 128
  require return_data.size >= 32
  [94m_7 = 0, mem[ceil32(m_param2.length) + 132 len 28]
  require 0, mem[ceil32(m_param2.length) + 132 len 28] <= 4294967296
  require 0, mem[ceil32(m_param2.length) + 132 len 28] + 32 <= return_data.size
  require mem[ceil32(m_param2.length) + 0, mem[ceil32(m_param2.length) + 132 len 28] + 128] <= 4294967296 and 0, mem[ceil32(m_param2.length) + 132 len 28] + (32 * mem[ceil32(m_param2.length) + 0, mem[ceil32(m_param2.length) + 132 len 28] + 128]) + 32 <= return_data.size
  require ext_code.size(m_param1)
  call m_param1.0xb6cf3a62 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > m_param3:
      revert with 0, 'Invalid cost'
  require ext_code.size(addr(munknown05d97f4fAddress))
  call addr(munknown05d97f4fAddress).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args addr(m_param1), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128] = 'wC`'
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 196 len ceil32(m_param2.length)] = m_param2[allm], mem[m_param2.length + 128 len ceil32(m_param2.length) - m_param2.length]
  require ext_code.size(m_param1)
  call m_param1 with:
     funct Mask(32, 224, 'wC`') >> 224
       gas gas_remaining wei
      args Array(len=m_param2.length, data=m_param2[allm])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if addr(mstor25m[addr(ext_call.return_data[0])m]m.field_256):
      revert with 0, 'Module exists'
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 132] = addr(ext_call.return_data[0])
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 164] = m_param4
  require ext_code.size(addr(munknown05d97f4fAddress))
  call addr(munknown05d97f4fAddress).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args addr(ext_call.return_data[0]), m_param4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_param1)
  static call m_param1.name() with:
          gas gas_remaining wei
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94m_335 = mem[ceil32(m_param2.length) + [94m_7 + 128]
  mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128] = mem[ceil32(m_param2.length) + [94m_7 + 128]
  if not [94m_335:
      [94m_597 = mem[ceil32(m_param2.length) + [94m_7 + 128]
      [94midx = 0
      mwhile [94midx < [94m_597m:
          require [94midx < mem[ceil32(m_param2.length) + [94m_7 + 128]
          require [94midx < mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[(32 * [94midx) + ceil32(m_param2.length) + ceil32(return_data.size) + 160] = uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])
          require [94midx < mem[ceil32(m_param2.length) + [94m_7 + 128]
          mem[32] = 24
          uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])++
          mem[0] = sha3(mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1], 24)
          addr(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m]m[uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])m]) = addr(ext_call.return_data[0])
          [94midx = [94midx + 1
          mcontinue 
      mem[64] = ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 160] = ext_call.return_data[0]
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 192] = addr(ext_call.return_data[0])
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 224] = m_param1
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 256] = m_param5
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 288] = ceil32(m_param2.length) + [94m_7 + 128
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 320] = ceil32(m_param2.length) + ceil32(return_data.size) + 128
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 352] = uint256(mstor26m[ext_call.return_data[0]m])
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 384] = 0
      mem[32] = 25
      mstor25m[addr(ext_call.return_data[0])m]m.field_0 = ext_call.return_data[0]
      addr(mstor25m[addr(ext_call.return_data[0])m]m.field_256) = addr(ext_call.return_data[0])
      addr(mstor25m[addr(ext_call.return_data[0])m]m.field_512) = m_param1
      Mask(96, 0, mstor25m[addr(ext_call.return_data[0])m]m.field_672) = Mask(96, 0, m_param5)
      mstor25m[addr(ext_call.return_data[0])m]m.field_768 = mem[ceil32(m_param2.length) + [94m_7 + 128]
      mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 3
      if not mem[ceil32(m_param2.length) + [94m_7 + 128]:
          [94midx = 0
          mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_768 + 31 / 32 > [94midxm:
              uint8(mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor25m[addr(ext_call.return_data[0])m]m.field_1024 = mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 4
          if not mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]:
              [94midx = 0
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = 0
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = 0
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1043 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              [94mvar68001 = floor32([94m_1043)
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, 0, _param5, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1043) + 32], ext_call.return_data[0], _param1
          else:
              [94ms = 0
              [94midx = ceil32(m_param2.length) + ceil32(return_data.size) + 160
              mwhile ceil32(m_param2.length) + ceil32(return_data.size) + (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 160 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0 = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 31) >> 5
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = 0
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = 0
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1211 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              [94mvar71001 = floor32([94m_1211)
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, 0, _param5, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1211) + 32], ext_call.return_data[0], _param1
      else:
          [94ms = 0
          [94midx = ceil32(m_param2.length) + [94m_7 + 160
          mwhile ceil32(m_param2.length) + [94m_7 + (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 160 > [94midxm:
              mstor25m[addr(ext_call.return_data[0])m]m[3m]m.field_0 = mem[[94midx + 31 len 1] * 256^[94ms or !(255 * 256^[94ms) and mstor25m[addr(ext_call.return_data[0])m]m[3m]m.field_0
              [94ms = [94ms + -([94ms + 1 / 32) + (-1 * [94ms * [94ms + 1 / 32) + 1
              [94midx = [94midx + 32
              mcontinue 
          [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 31) >> 5
          [94ms = sha3(sha3(addr(ext_call.return_data[0]), 25) + 3)
          mwhile [94midxm:
              mstor[[94msm] = !(255 * 256^[94midx) and mstor[[94msm]
              [94midx = [94midx + -([94midx + 1 / 32) + (-1 * [94midx * [94midx + 1 / 32) + 1
              [94ms = ([94midx + 1 / 32) + [94ms
              mcontinue 
          [94midx = (floor32(None + 3) >> 4) + (None * None + 3 / 32) - (Mask(251, 0, (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 31) >> 5 * None + 3 / 32)
          mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_768 + 31 / 32 > [94midxm:
              uint8(mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor25m[addr(ext_call.return_data[0])m]m.field_1024 = mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 4
          if not mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]:
              [94midx = 0
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = 0
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = 0
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1347 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, 0, _param5, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1347) + 32], ext_call.return_data[0], _param1
          else:
              [94ms = 0
              [94midx = ceil32(m_param2.length) + ceil32(return_data.size) + 160
              mwhile ceil32(m_param2.length) + ceil32(return_data.size) + (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 160 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0 = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 31) >> 5
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = 0
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = 0
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1427 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, 0, _param5, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1427) + 32], ext_call.return_data[0], _param1
  else:
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + 160 len 32 * [94m_335] = code.data[24259 len 32 * [94m_335]
      [94m_598 = mem[ceil32(m_param2.length) + [94m_7 + 128]
      [94midx = 0
      mwhile [94midx < [94m_598m:
          require [94midx < mem[ceil32(m_param2.length) + [94m_7 + 128]
          require [94midx < mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[(32 * [94midx) + ceil32(m_param2.length) + ceil32(return_data.size) + 160] = uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])
          require [94midx < mem[ceil32(m_param2.length) + [94m_7 + 128]
          mem[32] = 24
          uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])++
          mem[0] = sha3(mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1], 24)
          addr(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m]m[uint256(mstor24m[mem[(32 * [94midx) + ceil32(m_param2.length) + [94m_7 + 191 len 1]m])m]) = addr(ext_call.return_data[0])
          [94midx = [94midx + 1
          mcontinue 
      mem[64] = ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 160] = ext_call.return_data[0]
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 192] = addr(ext_call.return_data[0])
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 224] = m_param1
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 256] = m_param5
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 288] = ceil32(m_param2.length) + [94m_7 + 128
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 320] = ceil32(m_param2.length) + ceil32(return_data.size) + 128
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 352] = uint256(mstor26m[ext_call.return_data[0]m])
      mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 384] = 0
      mem[32] = 25
      mstor25m[addr(ext_call.return_data[0])m]m.field_0 = ext_call.return_data[0]
      addr(mstor25m[addr(ext_call.return_data[0])m]m.field_256) = addr(ext_call.return_data[0])
      addr(mstor25m[addr(ext_call.return_data[0])m]m.field_512) = m_param1
      Mask(96, 0, mstor25m[addr(ext_call.return_data[0])m]m.field_672) = Mask(96, 0, m_param5)
      mstor25m[addr(ext_call.return_data[0])m]m.field_768 = mem[ceil32(m_param2.length) + [94m_7 + 128]
      mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 3
      if not mem[ceil32(m_param2.length) + [94m_7 + 128]:
          [94midx = 0
          mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_768 + 31 / 32 > [94midxm:
              uint8(mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor25m[addr(ext_call.return_data[0])m]m.field_1024 = mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 4
          if not mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]:
              [94midx = 0
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = 0
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = 0
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1050 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              [94mvar69001 = floor32([94m_1050)
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, 0, _param5, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1050) + 32], ext_call.return_data[0], _param1
          else:
              [94ms = 0
              [94midx = ceil32(m_param2.length) + ceil32(return_data.size) + 160
              mwhile ceil32(m_param2.length) + ceil32(return_data.size) + (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 160 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0 = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 31) >> 5
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = 0
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = 0
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1220 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              [94mvar72001 = floor32([94m_1220)
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, 0, _param5, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1220) + 32], ext_call.return_data[0], _param1
      else:
          [94ms = 0
          [94midx = ceil32(m_param2.length) + [94m_7 + 160
          mwhile ceil32(m_param2.length) + [94m_7 + (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 160 > [94midxm:
              mstor25m[addr(ext_call.return_data[0])m]m[3m]m.field_0 = mem[[94midx + 31 len 1] * 256^[94ms or !(255 * 256^[94ms) and mstor25m[addr(ext_call.return_data[0])m]m[3m]m.field_0
              [94ms = [94ms + -([94ms + 1 / 32) + (-1 * [94ms * [94ms + 1 / 32) + 1
              [94midx = [94midx + 32
              mcontinue 
          [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 31) >> 5
          [94ms = sha3(sha3(addr(ext_call.return_data[0]), 25) + 3)
          mwhile [94midxm:
              mstor[[94msm] = !(255 * 256^[94midx) and mstor[[94msm]
              [94midx = [94midx + -([94midx + 1 / 32) + (-1 * [94midx * [94midx + 1 / 32) + 1
              [94ms = ([94midx + 1 / 32) + [94ms
              mcontinue 
          [94midx = (floor32(None + 3) >> 4) + (None * None + 3 / 32) - (Mask(251, 0, (32 * mem[ceil32(m_param2.length) + [94m_7 + 128]) + 31) >> 5 * None + 3 / 32)
          mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_768 + 31 / 32 > [94midxm:
              uint8(mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          mstor25m[addr(ext_call.return_data[0])m]m.field_1024 = mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]
          mem[0] = sha3(addr(ext_call.return_data[0]), 25) + 4
          if not mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]:
              [94midx = 0
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = 0
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = 0
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1354 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, 0, _param5, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1354) + 32], ext_call.return_data[0], _param1
          else:
              [94ms = 0
              [94midx = ceil32(m_param2.length) + ceil32(return_data.size) + 160
              mwhile ceil32(m_param2.length) + ceil32(return_data.size) + (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 160 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0 = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(m_param2.length) + ceil32(return_data.size) + 128]) + 31) >> 5
              mwhile mstor25m[addr(ext_call.return_data[0])m]m.field_1024 > [94midxm:
                  mstor25m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0 = 0
                  [94midx = [94midx + 1
                  mcontinue 
              mstor25m[addr(ext_call.return_data[0])m]m.field_1280 = uint256(mstor26m[ext_call.return_data[0]m])
              mstor25m[addr(ext_call.return_data[0])m]m.field_1536 = 0
              uint256(mstor26m[ext_call.return_data[0]m])++
              addr(mstor26m[ext_call.return_data[0]m]m[uint256(mstor26m[ext_call.return_data[0]m])m]) = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 480] = ext_call.return_data[0]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 512] = m_param4
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 544] = 0
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 576] = m_param5
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 416] = 192
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 608] = mem[ceil32(m_param2.length) + [94m_7 + 128]
              [94m_1434 = mem[ceil32(m_param2.length) + [94m_7 + 128]
              mem[ceil32(m_param2.length) + ceil32(return_data.size) + (32 * [94m_335) + 640 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])] = mem[ceil32(m_param2.length) + [94m_7 + 160 len floor32(mem[ceil32(m_param2.length) + [94m_7 + 128])]
              log 0xfa9cc8fa: 192, addr(ext_call.return_data[0]), ext_call.return_data[0], _param4, 0, _param5, mem[ceil32(_param2.length) + ceil32(return_data.size) + (32 * _335) + 608 len (32 * _1434) + 32], ext_call.return_data[0], _param1
  require mstor3 + 1 == mstor3


# hash = 0xb95459e4
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def moduleRegistry(): # not payable
  return addr(mmoduleRegistryAddress)


# hash = 0xbb3acde9
# getter = None
# const = None
# payable = False
def unknownbb3acde9(addr m_param1, uint256 m_param2, array m_param3): # not payable
  require calldata.size - 4 >= 96
  require m_param3 <= 4294967296
  require m_param3 + 36 <= calldata.size
  require m_param3.length <= 4294967296 and m_param3 + m_param3.length + 36 <= calldata.size
  mem[64] = ceil32(m_param3.length) + 128
  mem[96] = m_param3.length
  mem[128 len m_param3.length] = m_param3[allm]
  mem[m_param3.length + 128] = 0
  if not mstor20:
      revert with 0, 'Issuance frozen'
  if caller == mowner:
      mstor3++
      mem[ceil32(m_param3.length) + 132] = uint256(mholderCount)
      mem[ceil32(m_param3.length) + 164] = 0
      mem[ceil32(m_param3.length) + 196] = m_param1
      mem[ceil32(m_param3.length) + 228] = m_param2
      mem[ceil32(m_param3.length) + 260] = mbalanceOfm[addr(m_param1)m]
      mem[ceil32(m_param3.length) + 292] = mbalanceOf
      mem[ceil32(m_param3.length) + 324] = mdataStoreAddress
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
           gas gas_remaining wei
          args uint256(mholderCount), 0, addr(m_param1), m_param2, mbalanceOfm[addr(m_param1)m], mbalanceOf, mdataStoreAddress
      mem[ceil32(m_param3.length) + 128] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mholderCount) = delegate.return_data[0]
      require mgranularity
      if m_param2 % mgranularity:
          revert with 0, 'Invalid granularity'
      if not mtransfersFrozen:
          mem[0] = 2
          mem[32] = 24
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              mem[0] = mstor2BACm[[94midxm]
              mem[32] = 25
              if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                  [94m_96 = mem[64]
                  mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = 0
                  mem[mem[64] + 36] = m_param1
                  mem[mem[64] + 68] = m_param2
                  mem[mem[64] + 100] = 128
                  mem[mem[64] + 132] = mem[96]
                  [94mt = 0
                  mwhile [94mt < mem[96]m:
                      mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                      [94mt = [94mt + 32
                      mcontinue 
                  if not mem[96] % 32:
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len mem[96] + [94m_96 + -mem[64] + 160]
                  else:
                      mem[floor32(mem[96]) + [94m_96 + 164] = mem[floor32(mem[96]) + [94m_96 + -(mem[96] % 32) + 196 len mem[96] % 32]
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len floor32(mem[96]) + [94m_96 + -mem[64] + 192]
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 3
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      [94ms = mstor2BACm[[94midxm]
                      [94ms = 1
                      mcontinue 
                  require ext_call.return_data[0] <= 3
                  if ext_call.return_data[0] != 2:
                      require ext_call.return_data[0] <= 3
              [94midx = [94midx + 1
              [94ms = mstor2BACm[[94midxm]
              [94ms = [94ms
              mcontinue 
  else:
      require addr(mstor25m[callerm]m.field_256) == caller
      require not uint8(mstor25m[callerm]m.field_672)
      require 0 < mstor25m[callerm]m.field_768
      require 0 < mstor25m[callerm]m.field_768
      [94ms = 0
      mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor25', 25))) + (0.03125 / s))m[uint8([94ms)m] != 3m:
          require [94ms + 1 < mstor25m[callerm]m.field_768
          mem[32] = 25
          require [94ms + 1 < mstor25m[callerm]m.field_768
          mem[0] = sha3(caller, 25) + 3
          [94ms = [94ms + 1
          mcontinue 
      mstor3++
      mem[ceil32(m_param3.length) + 132] = uint256(mholderCount)
      mem[ceil32(m_param3.length) + 164] = 0
      mem[ceil32(m_param3.length) + 196] = m_param1
      mem[ceil32(m_param3.length) + 228] = m_param2
      mem[ceil32(m_param3.length) + 260] = mbalanceOfm[addr(m_param1)m]
      mem[ceil32(m_param3.length) + 292] = mbalanceOf
      mem[ceil32(m_param3.length) + 324] = mdataStoreAddress
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
           gas gas_remaining wei
          args uint256(mholderCount), 0, addr(m_param1), m_param2, mbalanceOfm[addr(m_param1)m], mbalanceOf, mdataStoreAddress
      mem[ceil32(m_param3.length) + 128] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mholderCount) = delegate.return_data[0]
      require mgranularity
      if m_param2 % mgranularity:
          revert with 0, 'Invalid granularity'
      if not mtransfersFrozen:
          mem[0] = 2
          mem[32] = 24
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              mem[0] = mstor2BACm[[94midxm]
              mem[32] = 25
              if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                  mem[ceil32(m_param3.length) + 128] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                  mem[ceil32(m_param3.length) + 132] = 0
                  mem[ceil32(m_param3.length) + 164] = m_param1
                  mem[ceil32(m_param3.length) + 196] = m_param2
                  mem[ceil32(m_param3.length) + 228] = 128
                  mem[ceil32(m_param3.length) + 260] = mem[96]
                  [94mt = 0
                  mwhile [94mt < mem[96]m:
                      mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                      [94mt = [94mt + 32
                      mcontinue 
                  if not mem[96] % 32:
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len mem[96] + ceil32(m_param3.length) + -mem[64] + 288]
                  else:
                      mem[floor32(mem[96]) + ceil32(m_param3.length) + 292] = mem[floor32(mem[96]) + ceil32(m_param3.length) + -(mem[96] % 32) + 324 len mem[96] % 32]
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_param3.length) + -mem[64] + 320]
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 3
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      [94ms = mstor2BACm[[94midxm]
                      [94ms = 1
                      mcontinue 
                  require ext_call.return_data[0] <= 3
                  if ext_call.return_data[0] != 2:
                      require ext_call.return_data[0] <= 3
              [94midx = [94midx + 1
              [94ms = mstor2BACm[[94midxm]
              [94ms = [94ms
              mcontinue 
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(m_param1), 28), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mstor3 + 1 == mstor3
  revert with 0, 'Transfer Invalid'


# hash = 0xc3501848
# getter = None
# const = None
# payable = False
def unknownc3501848(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0xb7e2c789 with:
       gas gas_remaining wei
      args 0, 29, 21, 30, m_param1
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xc4d66de8
# getter = None
# const = None
# payable = False
def initialize(address m_sender): # not payable
  require calldata.size - 4 >= 32
  if minitialized:
      revert with 0, 'Already initialized'
  munknown2fb3b99dAddress = m_sender
  uint8(mstor23m.field_0) = 3
  uint16(mstor23m.field_8) = 0
  mstor23m.field_256 % 1 = 0
  require caller == mowner
  require ext_code.size(munknowncbaec476Address)
  static call munknowncbaec476Address.getAddress(string channelId) with:
          gas gas_remaining wei
         args Array(len=14, data='ModuleRegistry')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor10) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor10))
  require ext_code.size(munknowncbaec476Address)
  static call munknowncbaec476Address.getAddress(string channelId) with:
          gas gas_remaining wei
         args Array(len=21, data='SecurityTokenRegistry')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor11) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor11))
  require ext_code.size(munknowncbaec476Address)
  static call munknowncbaec476Address.getAddress(string channelId) with:
          gas gas_remaining wei
         args Array(len=7, data='QTToken')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor12) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor12))
  mtokenFactoryAddress = caller
  minitialized = 1
  mstor5 = Mask(88, 168, caller) >> 168


# hash = 0xcbaec476
# getter = ['storage', 160, 0, 9]
# const = None
# payable = False
def unknowncbaec476(): # not payable
  return munknowncbaec476Address


# hash = 0xce4dbdff
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def securityTokenRegistry(): # not payable
  return addr(msecurityTokenRegistryAddress)


# hash = 0xd6abe110
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 17]]]], ['loc', 17]]]
# const = None
# payable = False
def tokenDetails(): # not payable
  return mtokenDetailsm[0 len mtokenDetailsm.lengthm]m.field_0


# hash = 0xdc722e3a
# getter = None
# const = None
# payable = False
def unknowndc722e3a(array m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + m_param1.length + 36 <= calldata.size
  require caller == mowner
  if not mstor20:
      revert with 0, 'Issuance frozen'
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x7713083e with:
       gas gas_remaining wei
      args Array(len=m_param1.length, data=m_param1[allm])
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mowner != delegate.return_data[12 len 20]:
      revert with 0, 'Owner did not sign'
  mstor20 = 0
  log 0x9ea7d0a1 


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 1]]]]]
# const = None
# payable = False
def allowance(address m_tokenOwner, address m_spender): # not payable
  require calldata.size - 4 >= 64
  return uint256(mallowancem[addr(m_tokenOwner)m]m[addr(m_spender)m])


# hash = 0xe45b8134
# getter = ['bool', ['storage', 8, 8, 18]]
# const = None
# payable = False
def transfersFrozen(): # not payable
  return bool(mtransfersFrozen)


# hash = 0xe77772fe
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def tokenFactory(): # not payable
  return mtokenFactoryAddress


# hash = 0xe77c646d
# getter = None
# const = None
# payable = False
def unknowne77c646d(uint256 m_param1, array m_param2): # not payable
  require calldata.size - 4 >= 64
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + m_param2.length + 36 <= calldata.size
  require addr(mstor25m[callerm]m.field_256) == caller
  require not uint8(mstor25m[callerm]m.field_672)
  require 0 < mstor25m[callerm]m.field_768
  require 0 < mstor25m[callerm]m.field_768
  [94ms = 0
  mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor25', 25))) + (0.03125 / s))m[uint8([94ms)m] != 5m:
      require [94ms + 1 < mstor25m[callerm]m.field_768
      mem[32] = 25
      require [94ms + 1 < mstor25m[callerm]m.field_768
      mem[0] = sha3(caller, 25) + 3
      [94ms = [94ms + 1
      mcontinue 
  mem[64] = ceil32(m_param2.length) + 128
  mem[96] = m_param2.length
  mem[128 len m_param2.length] = m_param2[allm]
  mem[m_param2.length + 128] = 0
  mstor3++
  mem[ceil32(m_param2.length) + 132] = uint256(mholderCount)
  mem[ceil32(m_param2.length) + 164] = caller
  mem[ceil32(m_param2.length) + 196] = 0
  mem[ceil32(m_param2.length) + 228] = m_param1
  mem[ceil32(m_param2.length) + 260] = mbalanceOf
  mem[ceil32(m_param2.length) + 292] = mbalanceOfm[callerm]
  mem[ceil32(m_param2.length) + 324] = mdataStoreAddress
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
       gas gas_remaining wei
      args uint256(mholderCount), caller, 0, m_param1, mbalanceOf, mbalanceOfm[callerm], mdataStoreAddress
  mem[ceil32(m_param2.length) + 128] = delegate.return_data[0]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mholderCount) = delegate.return_data[0]
  require mgranularity
  if m_param1 % mgranularity:
      revert with 0, 'Invalid granularity'
  if mtransfersFrozen:
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(caller, 28), mbalanceOfm[callerm], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mstor3 + 1 == mstor3
      require caller
      require m_param1 <= mtotalSupply
      mtotalSupply -= m_param1
      require m_param1 <= mbalanceOfm[callerm]
      mbalanceOfm[callerm] -= m_param1
      log Transfer(address from, address to, uint256 value):
                   0,
                   Mask(224, 0, _param1),
                   caller,
                   0,
      mem[ceil32(m_param2.length) + 128] = m_param1
      mem[ceil32(m_param2.length) + 224 len ceil32(m_param2.length)] = m_param2[allm], mem[m_param2.length + 128 len ceil32(m_param2.length) - m_param2.length]
      if not m_param2.length % 32:
          log 0xb7d0d6b6: 0, Mask(224, 0, _param1), 64, _param2.length, Mask(8 * _param2.length, -(8 * _param2.length) + 256, _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]) << (8 * _param2.length) - 256, 0, caller
      else:
          mem[floor32(m_param2.length) + ceil32(m_param2.length) + 224] = mem[floor32(m_param2.length) + ceil32(m_param2.length) + -(m_param2.length % 32) + 256 len m_param2.length % 32]
          log 0xb7d0d6b6: 0, Mask(224, 0, _param1), 64, _param2.length, Mask(8 * ceil32(_param2.length), -(8 * ceil32(_param2.length)) + 256, _param2[all], mem[_param2.length + 128 len ceil32(_param2.length) - _param2.length]) << (8 * ceil32(_param2.length)) - 256, mem[(2 * ceil32(_param2.length)) + 224 len floor32(_param2.length) + -ceil32(_param2.length) + 32], 0, caller
  else:
      mem[0] = 2
      mem[32] = 24
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          mem[0] = mstor2BACm[[94midxm]
          mem[32] = 25
          if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
              [94m_151 = mem[64]
              mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = caller
              mem[mem[64] + 36] = 0
              mem[mem[64] + 68] = m_param1
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = mem[96]
              [94mt = 0
              mwhile [94mt < mem[96]m:
                  mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                  [94mt = [94mt + 32
                  mcontinue 
              if not mem[96] % 32:
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len mem[96] + [94m_151 + -mem[64] + 160]
              else:
                  mem[floor32(mem[96]) + [94m_151 + 164] = mem[floor32(mem[96]) + [94m_151 + -(mem[96] % 32) + 196 len mem[96] % 32]
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len floor32(mem[96]) + [94m_151 + -mem[64] + 192]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
          [94midx = [94midx + 1
          [94ms = mstor2BACm[[94midxm]
          [94ms = [94ms
          mcontinue 
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(caller, 28), mbalanceOfm[callerm], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      mem[mem[64] + 68] = mcurrentCheckpointId
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(0, 28), mbalanceOf, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mstor3 + 1 == mstor3
      require caller
      require m_param1 <= mtotalSupply
      mtotalSupply -= m_param1
      require m_param1 <= mbalanceOfm[callerm]
      mem[0] = caller
      mem[32] = 0
      mbalanceOfm[callerm] -= m_param1
      log Transfer(
            address from=_param1,
            address to=caller,
            uint256 value=0)
      mem[mem[64]] = m_param1
      mem[mem[64] + 32] = 64
      mem[mem[64] + 64] = mem[96]
      mem[mem[64] + 96 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
      if not mem[96] % 32:
          log 0xb7d0d6b6: _param1, 64, mem[mem[64] + 64 len mem[96] + 32], 0, caller
      else:
          mem[floor32(mem[96]) + mem[64] + 96] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 128 len mem[96] % 32]
          log 0xb7d0d6b6: _param1, 64, mem[mem[64] + 64 len floor32(mem[96]) + 64], 0, caller
  revert with 0, 'Invalid redeem'


# hash = 0xee532f31
# getter = None
# const = None
# payable = False
def transferFromWithData(address m_from, address m_to, uint256 m_value, bytes m_data): # not payable
  require calldata.size - 4 >= 128
  require m_data <= 4294967296
  require m_data + 36 <= calldata.size
  require m_data.length <= 4294967296 and m_data + m_data.length + 36 <= calldata.size
  mem[64] = ceil32(m_data.length) + 128
  mem[96] = m_data.length
  mem[128 len m_data.length] = m_data[allm]
  mem[m_data.length + 128] = 0
  mstor3++
  mem[ceil32(m_data.length) + 132] = uint256(mholderCount)
  mem[ceil32(m_data.length) + 164] = m_from
  mem[ceil32(m_data.length) + 196] = m_to
  mem[ceil32(m_data.length) + 228] = m_value
  mem[ceil32(m_data.length) + 260] = mbalanceOfm[addr(m_to)m]
  mem[ceil32(m_data.length) + 292] = mbalanceOfm[addr(m_from)m]
  mem[ceil32(m_data.length) + 324] = mdataStoreAddress
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
       gas gas_remaining wei
      args uint256(mholderCount), addr(m_from), addr(m_to), m_value, mbalanceOfm[addr(m_to)m], mbalanceOfm[addr(m_from)m], mdataStoreAddress
  mem[ceil32(m_data.length) + 128] = delegate.return_data[0]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mholderCount) = delegate.return_data[0]
  require mgranularity
  if m_value % mgranularity:
      revert with 0, 'Invalid granularity'
  if not mtransfersFrozen:
      mem[0] = 2
      mem[32] = 24
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          mem[0] = mstor2BACm[[94midxm]
          mem[32] = 25
          if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
              [94m_45 = mem[64]
              mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = m_from
              mem[mem[64] + 36] = m_to
              mem[mem[64] + 68] = m_value
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = mem[96]
              [94mt = 0
              mwhile [94mt < mem[96]m:
                  mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                  [94mt = [94mt + 32
                  mcontinue 
              if not mem[96] % 32:
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len mem[96] + [94m_45 + -mem[64] + 160]
              else:
                  mem[floor32(mem[96]) + [94m_45 + 164] = mem[floor32(mem[96]) + [94m_45 + -(mem[96] % 32) + 196 len mem[96] % 32]
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len floor32(mem[96]) + [94m_45 + -mem[64] + 192]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
          [94midx = [94midx + 1
          [94ms = mstor2BACm[[94midxm]
          [94ms = [94ms
          mcontinue 
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(m_from), 28), mbalanceOfm[addr(m_from)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(m_to), 28), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mstor3 + 1 == mstor3
  revert with 0, 'Transfer Invalid'


# hash = 0xf282527a
# getter = None
# const = None
# payable = False
def unknownf282527a(addr m_param1, addr m_param2, uint256 m_param3, array m_param4, array m_param5): # not payable
  require calldata.size - 4 >= 160
  require m_param4 <= 4294967296
  require m_param4 + 36 <= calldata.size
  require m_param4.length <= 4294967296 and m_param4 + m_param4.length + 36 <= calldata.size
  require m_param5 <= 4294967296
  require m_param5 + 36 <= calldata.size
  require m_param5.length <= 4294967296 and m_param5 + m_param5.length + 36 <= calldata.size
  if mcontrollerAddress != caller:
      revert with 0, 'Not Authorised'
  if munknown7a802c71:
      revert with 0, 'Not Authorised'
  mem[64] = ceil32(m_param4.length) + 128
  mem[96] = m_param4.length
  mem[128 len m_param4.length] = m_param4[allm]
  mem[m_param4.length + 128] = 0
  mstor3++
  mem[ceil32(m_param4.length) + 132] = uint256(mholderCount)
  mem[ceil32(m_param4.length) + 164] = m_param1
  mem[ceil32(m_param4.length) + 196] = m_param2
  mem[ceil32(m_param4.length) + 228] = m_param3
  mem[ceil32(m_param4.length) + 260] = mbalanceOfm[addr(m_param2)m]
  mem[ceil32(m_param4.length) + 292] = mbalanceOfm[addr(m_param1)m]
  mem[ceil32(m_param4.length) + 324] = mdataStoreAddress
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
       gas gas_remaining wei
      args uint256(mholderCount), addr(m_param1), addr(m_param2), m_param3, mbalanceOfm[addr(m_param2)m], mbalanceOfm[addr(m_param1)m], mdataStoreAddress
  mem[ceil32(m_param4.length) + 128] = delegate.return_data[0]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mholderCount) = delegate.return_data[0]
  require mgranularity
  if m_param3 % mgranularity:
      revert with 0, 'Invalid granularity'
  if mtransfersFrozen:
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(addr(m_param1), 28), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(addr(m_param2), 28), mbalanceOfm[addr(m_param2)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mstor3 + 1 == mstor3
      require m_param2
      require m_param3 <= mbalanceOfm[addr(m_param1)m]
      mbalanceOfm[addr(m_param1)m] -= m_param3
      require m_param3 + mbalanceOfm[m_param2m] >= mbalanceOfm[m_param2m]
      mbalanceOfm[addr(m_param2)m] = m_param3 + mbalanceOfm[m_param2m]
      log Transfer(address from, address to, uint256 value):
                   0,
                   Mask(224, 0, _param3),
                   _param1,
                   _param2,
      mem[(2 * ceil32(m_param4.length)) + 320 len m_param5.length] = m_param5[allm]
      mem[m_param5.length + (2 * ceil32(m_param4.length)) + 320] = 0
      log 0x6bf62b4b: caller, _param3, 128, ceil32(_param4.length) + 160, _param4.length, _param4[all], 0, mem[ceil32(_param4.length) + _param4.length + 320 len ceil32(_param4.length) - _param4.length], _param5[all], mem[(2 * ceil32(_param4.length)) + _param5.length + 320 len ceil32(_param5.length) - _param5.length], _param1, _param2
  else:
      mem[0] = 2
      mem[32] = 24
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          mem[0] = mstor2BACm[[94midxm]
          mem[32] = 25
          if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
              [94m_61 = mem[64]
              mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = m_param1
              mem[mem[64] + 36] = m_param2
              mem[mem[64] + 68] = m_param3
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = mem[96]
              [94mt = 0
              mwhile [94mt < mem[96]m:
                  mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                  [94mt = [94mt + 32
                  mcontinue 
              if not mem[96] % 32:
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len mem[96] + [94m_61 + -mem[64] + 160]
              else:
                  mem[floor32(mem[96]) + [94m_61 + 164] = mem[floor32(mem[96]) + [94m_61 + -(mem[96] % 32) + 196 len mem[96] % 32]
                  require ext_code.size(mstor2BACm[[94midxm])
                  call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4 len floor32(mem[96]) + [94m_61 + -mem[64] + 192]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  [94ms = mstor2BACm[[94midxm]
                  [94ms = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
          [94midx = [94midx + 1
          [94ms = mstor2BACm[[94midxm]
          [94ms = [94ms
          mcontinue 
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(addr(m_param1), 28), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      mem[0] = m_param2
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
           gas gas_remaining wei
          args sha3(addr(m_param2), 28), mbalanceOfm[addr(m_param2)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mstor3 + 1 == mstor3
      require m_param2
      require m_param3 <= mbalanceOfm[addr(m_param1)m]
      mbalanceOfm[addr(m_param1)m] -= m_param3
      require m_param3 + mbalanceOfm[m_param2m] >= mbalanceOfm[m_param2m]
      mem[32] = 0
      mbalanceOfm[addr(m_param2)m] = m_param3 + mbalanceOfm[m_param2m]
      log Transfer(
            address from=_param3,
            address to=_param1,
            uint256 value=_param2)
      mem[mem[64] + 64] = 128
      mem[m_param4.length + mem[64] + 160] = 0
      mem[mem[64] + 96] = ceil32(m_param4.length) + 160
      mem[mem[64] + ceil32(m_param4.length) + 160] = m_param5.length
      mem[mem[64] + ceil32(m_param4.length) + 192 len m_param5.length] = m_param5[allm]
      mem[m_param5.length + mem[64] + ceil32(m_param4.length) + 192] = 0
      log 0x6bf62b4b: caller, _param3, 128, ceil32(_param4.length) + 160, _param4.length, _param4[all], 0, mem[mem[64] + _param4.length + 192 len ceil32(_param4.length) + ceil32(_param5.length) - _param4.length], _param1, _param2


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >= 32
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf3d490db
# getter = None
# const = None
# payable = False
def unknownf3d490db(uint256 m_param1, addr m_param2, uint256 m_param3, array m_param4): # not payable
  require calldata.size - 4 >= 128
  require m_param4 <= 4294967296
  require m_param4 + 36 <= calldata.size
  require m_param4.length <= 4294967296 and m_param4 + m_param4.length + 36 <= calldata.size
  mem[96] = m_param4.length
  mem[128 len m_param4.length] = m_param4[allm]
  mem[m_param4.length + 128] = 0
  mem[ceil32(m_param4.length) + 128] = 0
  if m_param1 != 0x554e4c4f434b45440000000000000000000000000000000000000000000000:
      revert with 0, 'Invalid partition'
  mem[64] = ceil32(m_param4.length) + (32 * mstor2BACm.length) + 192
  mem[ceil32(m_param4.length) + 160] = mstor2BACm.length
  if not mstor2BACm.length:
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          require [94midx < mstor2BACm.length
          [94m_63 = mem[(32 * [94midx) + ceil32(m_param4.length) + 192]
          mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 196] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
          mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 228] = m_param2
          mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 260] = 0
          require ext_code.size(addr([94m_63))
          static call addr([94m_63).0x2829e651 with:
                  gas gas_remaining wei
                 args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(m_param2), 0
          mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 192] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if [94ms >= ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              [94ms = [94ms
              mcontinue 
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          [94ms = ext_call.return_data[0]
          mcontinue 
      mstor3++
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 196] = uint256(mholderCount)
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 228] = caller
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 260] = m_param2
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 292] = m_param3
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 324] = mbalanceOfm[addr(m_param2)m]
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 356] = mbalanceOfm[callerm]
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 388] = mdataStoreAddress
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
           gas gas_remaining wei
          args uint256(mholderCount), caller, addr(m_param2), m_param3, mbalanceOfm[addr(m_param2)m], mbalanceOfm[callerm], mdataStoreAddress
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 192] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mholderCount) = delegate.return_data[0]
      require mgranularity
      if m_param3 % mgranularity:
          revert with 0, 'Invalid granularity'
      if not mtransfersFrozen:
          mem[0] = 2
          mem[32] = 24
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              mem[0] = mstor2BACm[[94midxm]
              mem[32] = 25
              if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                  [94m_115 = mem[64]
                  mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = caller
                  mem[mem[64] + 36] = m_param2
                  mem[mem[64] + 68] = m_param3
                  mem[mem[64] + 100] = 128
                  mem[mem[64] + 132] = mem[96]
                  [94mt = 0
                  mwhile [94mt < mem[96]m:
                      mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                      [94mt = [94mt + 32
                      mcontinue 
                  if not mem[96] % 32:
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len mem[96] + [94m_115 + -mem[64] + 160]
                  else:
                      mem[floor32(mem[96]) + [94m_115 + 164] = mem[floor32(mem[96]) + [94m_115 + -(mem[96] % 32) + 196 len mem[96] % 32]
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len floor32(mem[96]) + [94m_115 + -mem[64] + 192]
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 3
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      [94ms = mstor2BACm[[94midxm]
                      [94ms = 1
                      mcontinue 
                  require ext_call.return_data[0] <= 3
                  if ext_call.return_data[0] != 2:
                      require ext_call.return_data[0] <= 3
              [94midx = [94midx + 1
              [94ms = mstor2BACm[[94midxm]
              [94ms = [94ms
              mcontinue 
  else:
      mem[ceil32(m_param4.length) + 192] = mstor2BAC
      [94midx = ceil32(m_param4.length) + 192
      [94ms = sha3(0x2bacf7cca723d030d12aee795132f2c5f2d14ad131f16f3f27eeba3e79d18b8c)
      mwhile ceil32(m_param4.length) + (32 * mstor2BACm.length) + 160 > [94midxm:
          mem[[94midx + 32] = addr(mallowancem[[94msm])
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
      [94midx = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mstor2BACm.lengthm:
          require [94midx < mstor2BACm.length
          [94m_199 = mem[(32 * [94midx) + ceil32(m_param4.length) + 192]
          mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 196] = 0xfe4c4f434b454400000000000000000000000000000000000000000000000000
          mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 228] = m_param2
          mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 260] = 0
          require ext_code.size(addr([94m_199))
          static call addr([94m_199).0x2829e651 with:
                  gas gas_remaining wei
                 args 0xfe4c4f434b454400000000000000000000000000000000000000000000000000, addr(m_param2), 0
          mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 192] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if [94ms >= ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              [94ms = [94ms
              mcontinue 
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          [94ms = ext_call.return_data[0]
          mcontinue 
      mstor3++
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 196] = uint256(mholderCount)
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 228] = caller
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 260] = m_param2
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 292] = m_param3
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 324] = mbalanceOfm[addr(m_param2)m]
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 356] = mbalanceOfm[callerm]
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 388] = mdataStoreAddress
      require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
      [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x943aef7b with:
           gas gas_remaining wei
          args uint256(mholderCount), caller, addr(m_param2), m_param3, mbalanceOfm[addr(m_param2)m], mbalanceOfm[callerm], mdataStoreAddress
      mem[ceil32(m_param4.length) + (32 * mstor2BACm.length) + 192] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      uint256(mholderCount) = delegate.return_data[0]
      require mgranularity
      if m_param3 % mgranularity:
          revert with 0, 'Invalid granularity'
      if not mtransfersFrozen:
          mem[0] = 2
          mem[32] = 24
          [94midx = 0
          [94ms = 0
          [94ms = 0
          mwhile [94midx < mstor2BACm.lengthm:
              mem[0] = mstor2BACm[[94midxm]
              mem[32] = 25
              if not uint8(mstor25m[mstor2BACm[[94midxm]m]m.field_672):
                  [94m_254 = mem[64]
                  mem[mem[64]] = 0x3d32173100000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = caller
                  mem[mem[64] + 36] = m_param2
                  mem[mem[64] + 68] = m_param3
                  mem[mem[64] + 100] = 128
                  mem[mem[64] + 132] = mem[96]
                  [94mt = 0
                  mwhile [94mt < mem[96]m:
                      mem[[94mt + mem[64] + 164] = mem[[94mt + 128]
                      [94mt = [94mt + 32
                      mcontinue 
                  if not mem[96] % 32:
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len mem[96] + [94m_254 + -mem[64] + 160]
                  else:
                      mem[floor32(mem[96]) + [94m_254 + 164] = mem[floor32(mem[96]) + [94m_254 + -(mem[96] % 32) + 196 len mem[96] % 32]
                      require ext_code.size(mstor2BACm[[94midxm])
                      call mstor2BACm[[94midxm].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len floor32(mem[96]) + [94m_254 + -mem[64] + 192]
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] <= 3
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      [94ms = mstor2BACm[[94midxm]
                      [94ms = 1
                      mcontinue 
                  require ext_call.return_data[0] <= 3
                  if ext_call.return_data[0] != 2:
                      require ext_call.return_data[0] <= 3
              [94midx = [94midx + 1
              [94ms = mstor2BACm[[94midxm]
              [94ms = [94ms
              mcontinue 
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(caller, 28), mbalanceOfm[callerm], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x85bf7b56df4640150719e189cfa66e4cded391c7)
  [93mdelegate 0x85bf7b56df4640150719e189cfa66e4cded391c7.0x9def7ee with:
       gas gas_remaining wei
      args sha3(addr(m_param2), 28), mbalanceOfm[addr(m_param2)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mstor3 + 1 == mstor3
  revert with 0, 'Transfer Invalid'


# hash = 0xf433262f
# getter = None
# const = None
# payable = False
def updateFromRegistry(): # not payable
  require caller == mowner
  require ext_code.size(munknowncbaec476Address)
  static call munknowncbaec476Address.getAddress(string channelId) with:
          gas gas_remaining wei
         args Array(len=14, data='ModuleRegistry')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor10) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor10))
  require ext_code.size(munknowncbaec476Address)
  static call munknowncbaec476Address.getAddress(string channelId) with:
          gas gas_remaining wei
         args Array(len=21, data='SecurityTokenRegistry')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor11) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor11))
  require ext_code.size(munknowncbaec476Address)
  static call munknowncbaec476Address.getAddress(string channelId) with:
          gas gas_remaining wei
         args Array(len=7, data='QTToken')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor12) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor12))


# hash = 0xf77c4791
# getter = ['storage', 160, 8, 8]
# const = None
# payable = False
def controller(): # not payable
  return mcontrollerAddress


# hash = 0xfad8b32a
# getter = None
# const = None
# payable = False
def revokeOperator(address m_operator): # not payable
  require calldata.size - 4 >= 32
  require m_operator
  require caller
  uint256(mallowancem[callerm]m[addr(m_operator)m]) = 0
  log Approval(
        address owner=0,
        address spender=caller,
        uint256 value=_operator)
  log RevokedOperator(
        address operator=_operator,
        address tokenHolder=caller)


# hash = 0xff0b9c90
# getter = None
# const = None
# payable = False
def createCheckpoint(): # not payable
  if mowner != caller:
      require addr(mstor25m[callerm]m.field_256) == caller
      require not uint8(mstor25m[callerm]m.field_672)
      require 0 < mstor25m[callerm]m.field_768
      require 0 < mstor25m[callerm]m.field_768
      [94ms = 0
      mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor25', 25))) + (0.03125 / s))m[uint8([94ms)m] != 4m:
          require [94ms + 1 < mstor25m[callerm]m.field_768
          mem[32] = 25
          require [94ms + 1 < mstor25m[callerm]m.field_768
          mem[0] = sha3(caller, 25) + 3
          [94ms = [94ms + 1
          mcontinue 
  mcurrentCheckpointId++
  mstor22++
  mstorD833m[mstor22m] = block.timestamp
  mstor27m[mstor16m] = mtotalSupply
  require ext_code.size(mdataStoreAddress)
  static call mdataStoreAddress.0x2fc94ba6 with:
          gas gas_remaining wei
         args 0xdf3a8dd24acdd05addfc6aeffef7574d2de3f844535ec91e8e0f3e45dba96731
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  log 0x624ea167: ext_call.return_data[0], currentCheckpointId
  return mcurrentCheckpointId


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  [93mdelegate munknown2fb3b99dAddress with:
     funct call.data[0 len 4]
       gas gas_remaining wei
      args call.data[4 len calldata.size - 4]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  return ext_call.return_data[0 len return_data.size]


