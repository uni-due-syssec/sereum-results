# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x61Dc3506FcEc16Aec5C501d6a0d55f55EB51E867 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x107556fd': 'unknown107556fd(?)', '0x1aaeebe3': 'unknown1aaeebe3(?)', '0x70a08231': 'balanceOf(address _owner)', '0x733480b7': 'transferToICAP(bytes32 _icap, uint256 _value)', '0x77fe38a4': 'transferToICAPWithReference(bytes32 _icap, uint256 _value, string _reference)', '0xa9059cbb': 'transfer(address _to, uint256 _value)', '0xac35caee': 'transferWithReference(address _to, uint256 _value, string _reference)', '0xdae04fa2': 'unknowndae04fa2(?)', '0xf0149751': 'unknownf0149751(?)'} 

# storage definitions
def storage:
    # storage address 0
    contractOwner # mask: a s
    # storage address 1
    pendingContractOwner # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    unknown16318a6e
    # storage address 3
    startTime # mask: a s
    # storage address 4
    symbol
# hash = 0x029a8bf7
# getter = None
# const = None
# payable = True
def multiAsset() payable: 
  call munknown16318a6em[mstor4m[callerm]m]m.field_0.multiAsset() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  return ext_call.return_data[12 len 20]


# hash = 0x149b4bc1
# getter = None
# const = None
# payable = True
def unknown149b4bc1(uint256 m_param1, uint256 m_param2) payable: 
  if mcontractOwner != caller:
      return 0
  call munknown16318a6em[mstor4m[callerm]m]m.field_0.multiAsset() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  call addr(ext_call.return_data[0]).registryICAP() with:
       gas gas_remaining - 25050 wei
  call addr(ext_call.return_data[0]).assets(bytes32 param1) with:
       gas gas_remaining - 25050 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
  if not munknown16318a6em[ext_call.return_data[0]m]m.field_1536:
      call munknown16318a6em[ext_call.return_data[0]m]m.field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
           gas gas_remaining - 34050 wei
          args m_param1, m_param2, 96, 0
  else:
      call munknown16318a6em[ext_call.return_data[0]m]m.field_0.balanceOf(address owner) with:
           gas gas_remaining - 25050 wei
          args this.address
      require ext_call.success
      if ext_call.return_data[0] >= m_param2:
          call munknown16318a6em[ext_call.return_data[0]m]m.field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
               gas gas_remaining - 34050 wei
              args m_param1, m_param2, 96, 0
      else:
          call munknown16318a6em[ext_call.return_data[0]m]m.field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
             value eth.balance(this.address) wei
               gas gas_remaining - 34050 wei
              args m_param1, m_param2, 96, 0
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  log 0x73d7feb5: _param2, 64, 0, caller, _param1
  return 1


# hash = 0x15070401
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, 'caller'], 4]]]
# const = None
# payable = True
def getSymbol() payable: 
  return msymbolm[callerm]


# hash = 0x16318a6e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], ['add', 4, ['sha3', ['data', ['cd', 36], 2]]]]]]
# const = None
# payable = True
def unknown16318a6e(uint256 m_param1, uint256 m_param2) payable: 
  return munknown16318a6em[m_param2m]m[4m]m[m_param1m]m.field_0


# hash = 0x1e52dec8
# getter = None
# const = None
# payable = True
def unknown1e52dec8(addr m_param1, uint256 m_param2, uint256 m_param3) payable: 
  if mcontractOwner != caller:
      return 0
  if not munknown16318a6em[m_param3m]m.field_1536:
      call munknown16318a6em[m_param3m]m.field_0.transferWithReference(address to, uint256 value, string reference) with:
           gas gas_remaining - 34050 wei
          args addr(m_param1), m_param2, 96, 0
  else:
      call munknown16318a6em[m_param3m]m.field_0.balanceOf(address owner) with:
           gas gas_remaining - 25050 wei
          args this.address
      require ext_call.success
      if ext_call.return_data[0] >= m_param2:
          call munknown16318a6em[m_param3m]m.field_0.transferWithReference(address to, uint256 value, string reference) with:
               gas gas_remaining - 34050 wei
              args addr(m_param1), m_param2, 96, 0
      else:
          call munknown16318a6em[m_param3m]m.field_0.transferWithReference(address to, uint256 value, string reference) with:
             value eth.balance(this.address) wei
               gas gas_remaining - 34050 wei
              args addr(m_param1), m_param2, 96, 0
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  log 0xae7443dd: _param2, 64, 0, caller, _param1, _param3
  return 1


# hash = 0x274a6c2b
# getter = None
# const = None
# payable = True
def unknown274a6c2b(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4) payable: 
  if mcontractOwner != caller:
      return 0
  munknown16318a6em[m_param4m]m[5m]m[m_param2 - m_param3 % 24 * 3600 / 2 * 3600m]m.field_0 += m_param1
  return 1


# hash = 0x387309ce
# getter = None
# const = ['return', 12]
# payable = True
const unknown387309ce = 12


# hash = 0x3dd7f552
# getter = None
# const = None
# payable = True
def unknown3dd7f552(uint256 m_param1, uint256 m_param2, array m_param3) payable: 
  if mcontractOwner != caller:
      return 0
  call munknown16318a6em[mstor4m[callerm]m]m.field_0.multiAsset() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  call addr(ext_call.return_data[0]).registryICAP() with:
       gas gas_remaining - 25050 wei
  call addr(ext_call.return_data[0]).assets(bytes32 param1) with:
       gas gas_remaining - 25050 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
  if not munknown16318a6em[ext_call.return_data[0]m]m.field_1536:
      call munknown16318a6em[ext_call.return_data[0]m]m.field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
           gas gas_remaining - 34050 wei
          args m_param1, m_param2, Array(len=m_param3.length, data=m_param3[allm])
  else:
      call munknown16318a6em[ext_call.return_data[0]m]m.field_0.balanceOf(address owner) with:
           gas gas_remaining - 25050 wei
          args this.address
      require ext_call.success
      if ext_call.return_data[0] >= m_param2:
          call munknown16318a6em[ext_call.return_data[0]m]m.field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
               gas gas_remaining - 34050 wei
              args m_param1, m_param2, Array(len=m_param3.length, data=m_param3[allm])
      else:
          call munknown16318a6em[ext_call.return_data[0]m]m.field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
             value eth.balance(this.address) wei
               gas gas_remaining - 34050 wei
              args m_param1, m_param2, Array(len=m_param3.length, data=m_param3[allm])
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  log 0x73d7feb5: _param2, Array(len=_param3.length, data=_param3[all]), caller, _param1
  return 1


# hash = 0x4592cd1d
# getter = None
# const = None
# payable = True
def claimContractOwnership() payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if addr(mpendingContractOwner) != caller:
      return 0
  mcontractOwner = addr(mpendingContractOwner)
  addr(mpendingContractOwner) = 0
  return 1


# hash = 0x4ba79dfe
# getter = None
# const = None
# payable = True
def removeAddress(address m_addr) payable: 
  if mcontractOwner != caller:
      return 0
  msymbolm[addr(m_addr)m] = 0
  return 1


# hash = 0x54a77049
# getter = None
# const = None
# payable = True
def unknown54a77049(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4) payable: 
  mem[64] = 96
  if mcontractOwner != caller:
      return 0
  mem[0] = m_param4
  mem[32] = 2
  if m_param2 - munknown16318a6em[m_param4m]m.field_768 > 22 * 3600:
      [94midx = 0
      mwhile uint8([94midx) < 12m:
          mem[0] = uint8([94midx)
          munknown16318a6em[m_param4m]m[4m]m[[94midx << 248m]m.field_0 = 0
          mem[32] = sha3(m_param4, 2) + 5
          munknown16318a6em[m_param4m]m[5m]m[[94midx << 248m]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
      munknown16318a6em[m_param4m]m.field_512 = m_param2 - m_param3 % 24 * 3600 / 2 * 3600
      munknown16318a6em[m_param4m]m[4m]m[m_param2 - m_param3 % 24 * 3600 / 2 * 3600m]m.field_0 += m_param1
      munknown16318a6em[m_param4m]m.field_768 = m_param2
      return (m_param2 - m_param3 % 24 * 3600 / 2 * 3600)
  if munknown16318a6em[m_param4m]m.field_512 >= m_param2 - m_param3 % 24 * 3600 / 2 * 3600:
      if munknown16318a6em[m_param4m]m.field_512 <= m_param2 - m_param3 % 24 * 3600 / 2 * 3600:
          munknown16318a6em[m_param4m]m.field_512 = m_param2 - m_param3 % 24 * 3600 / 2 * 3600
          munknown16318a6em[m_param4m]m[4m]m[m_param2 - m_param3 % 24 * 3600 / 2 * 3600m]m.field_0 += m_param1
          munknown16318a6em[m_param4m]m.field_768 = m_param2
          return (m_param2 - m_param3 % 24 * 3600 / 2 * 3600)
      [94midx = 0
      mwhile [94midx <= m_param2 - m_param3 % 24 * 3600 / 2 * 3600m:
          mem[0] = [94midx
          munknown16318a6em[m_param4m]m[4m]m[[94midxm]m.field_0 = 0
          mem[32] = sha3(m_param4, 2) + 5
          munknown16318a6em[m_param4m]m[5m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
      mem[0] = munknown16318a6em[m_param4m]m.field_512 + 1
      munknown16318a6em[m_param4m]m[4m]m[munknown16318a6em[m_param4m]m.field_512 + 1m]m.field_0 = 0
      mem[32] = sha3(m_param4, 2) + 5
      munknown16318a6em[m_param4m]m[5m]m[munknown16318a6em[m_param4m]m.field_512 + 1m]m.field_0 = 0
      [94mvar15002 = [94mvar15002 + 1
      mcontinue 
  [94midx = munknown16318a6em[sha3(mem[0 len 64])m]m.field_0 + 1
  mwhile [94midx <= m_param2 - m_param3 % 24 * 3600 / 2 * 3600m:
      mem[0] = [94midx
      munknown16318a6em[m_param4m]m[4m]m[[94midxm]m.field_0 = 0
      mem[32] = sha3(m_param4, 2) + 5
      munknown16318a6em[m_param4m]m[5m]m[[94midxm]m.field_0 = 0
      [94midx = [94midx + 1
      mcontinue 
  if munknown16318a6em[m_param4m]m.field_512 <= m_param2 - m_param3 % 24 * 3600 / 2 * 3600:
      munknown16318a6em[m_param4m]m.field_512 = m_param2 - m_param3 % 24 * 3600 / 2 * 3600
      munknown16318a6em[m_param4m]m[4m]m[m_param2 - m_param3 % 24 * 3600 / 2 * 3600m]m.field_0 += m_param1
      munknown16318a6em[m_param4m]m.field_768 = m_param2
      return (m_param2 - m_param3 % 24 * 3600 / 2 * 3600)
  [94midx = 0
  mwhile [94midx <= m_param2 - m_param3 % 24 * 3600 / 2 * 3600m:
      mem[0] = [94midx
      munknown16318a6em[m_param4m]m[4m]m[[94midxm]m.field_0 = 0
      mem[32] = sha3(m_param4, 2) + 5
      munknown16318a6em[m_param4m]m[5m]m[[94midxm]m.field_0 = 0
      [94midx = [94midx + 1
      mcontinue 
  mem[0] = munknown16318a6em[m_param4m]m.field_512 + 1
  munknown16318a6em[m_param4m]m[4m]m[munknown16318a6em[m_param4m]m.field_512 + 1m]m.field_0 = 0
  mem[32] = sha3(m_param4, 2) + 5
  munknown16318a6em[m_param4m]m[5m]m[munknown16318a6em[m_param4m]m.field_512 + 1m]m.field_0 = 0
  [94mvar18002 = [94mvar18002 + 1
  mcontinue 


# hash = 0x557f4bc9
# getter = None
# const = None
# payable = True
def changeContractOwnership(address m_to) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if mcontractOwner != caller:
      return 0
  uint256(mstor1) = m_to or Mask(96, 160, uint256(mstor1))
  return 1


# hash = 0x57a12ae5
# getter = None
# const = None
# payable = True
def unknown57a12ae5(addr m_param1, uint256 m_param2) payable: 
  if mcontractOwner != caller:
      return 0
  if not munknown16318a6em[m_param2m]m.field_1544:
      return 0
  msymbolm[addr(m_param1)m] = m_param2
  return 1


# hash = 0x5aa77d3c
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def pendingContractOwner() payable: 
  return addr(mpendingContractOwner)


# hash = 0x5d68c8f5
# getter = None
# const = None
# payable = True
def unknown5d68c8f5(uint256 m_param1, uint256 m_param2) payable: 
  if mcontractOwner != caller:
      return 0
  munknown16318a6em[m_param2m]m[5m]m[block.timestamp - mstor3 % 24 * 3600 / 2 * 3600m]m.field_0 += m_param1
  return 1


# hash = 0x6effec50
# getter = None
# const = None
# payable = True
def unknown6effec50(addr m_param1, uint256 m_param2, array m_param3) payable: 
  mem[128 len m_param3.length] = m_param3[allm]
  if mcontractOwner != caller:
      return 0
  mem[ceil32(m_param3.length) + 128 len m_param3.length] = m_param3[allm]
  if not m_param3.length % 32:
      call m_param1 with:
         value m_param2 wei
           gas gas_remaining - 34050 wei
          args m_param3[allm]
  else:
      mem[floor32(m_param3.length) + ceil32(m_param3.length) + 128] = mem[floor32(m_param3.length) + ceil32(m_param3.length) + -(m_param3.length % 32) + 160 len m_param3.length % 32]
      call m_param1.mem[ceil32(m_param3.length) + 128 len 4] with:
         value m_param2 wei
           gas gas_remaining - 34050 wei
          args mem[ceil32(m_param3.length) + 132 len floor32(m_param3.length) + 28]
  if ext_call.success:
      return 1
  if call.value <= 0:
      return 0
  call caller with:
     value call.value wei
       gas gas_remaining - 34050 wei
  require ext_call.success
  return 0


# hash = 0x6fae3d76
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = True
def access(address m_param1) payable: 
  return msymbolm[m_param1m]


# hash = 0x78e97925
# getter = ['storage', 256, 0, 3]
# const = None
# payable = True
def startTime() payable: 
  return mstartTime


# hash = 0x7e7c0c20
# getter = None
# const = None
# payable = True
def unknown7e7c0c20(addr m_param1, uint256 m_param2, uint8 m_param3) payable: 
  if mcontractOwner != caller:
      return 0
  call m_param1.symbol() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  if 0 == ext_call.return_data[0]:
      return 0
  call m_param1.multiAsset() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  if 0 == ext_call.return_data[12 len 20]:
      return 0
  call m_param1.multiAsset() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  call addr(ext_call.return_data[0]).'/U=1' with:
       gas gas_remaining - 25050 wei
      args ext_call.return_data[0]
  if not ext_call.return_data[0]:
      return 0
  call m_param1.multiAsset() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  call addr(ext_call.return_data[0]).0x8180f2fc with:
       gas gas_remaining - 25050 wei
      args addr(m_param1), -1, ext_call.return_data[0]
  if not ext_call.return_data[0]:
      return 0
  munknown16318a6em[ext_call.return_data[0]m]m.field_0 = munknown16318a6em[ext_call.return_data[0]m]m.field_160
  munknown16318a6em[ext_call.return_data[0]m]m.field_256 = m_param2
  munknown16318a6em[ext_call.return_data[0]m]m.field_512 = block.timestamp - mstartTime % 24 * 3600 / 2 * 3600
  munknown16318a6em[ext_call.return_data[0]m]m.field_768 = block.timestamp
  munknown16318a6em[ext_call.return_data[0]m]m.field_1536 = m_param3
  munknown16318a6em[ext_call.return_data[0]m]m.field_1544 = 1
  munknown16318a6em[ext_call.return_data[0]m]m.field_1552 = Mask(240, 16, m_param3) >> 16
  return 1


# hash = 0x84691767
# getter = None
# const = None
# payable = True
def unknown84691767(uint256 m_param1) payable: 
  if mcontractOwner != caller:
      return 0
  mstartTime = m_param1
  return 1


# hash = 0x8af07bfa
# getter = None
# const = None
# payable = True
def unknown8af07bfa(addr m_param1, uint256 m_param2, uint256 m_param3, array m_param4) payable: 
  if mcontractOwner != caller:
      return 0
  if not munknown16318a6em[m_param3m]m.field_1536:
      call munknown16318a6em[m_param3m]m.field_0.transferWithReference(address to, uint256 value, string reference) with:
           gas gas_remaining - 34050 wei
          args addr(m_param1), m_param2, Array(len=m_param4.length, data=m_param4[allm])
  else:
      call munknown16318a6em[m_param3m]m.field_0.balanceOf(address owner) with:
           gas gas_remaining - 25050 wei
          args this.address
      require ext_call.success
      if ext_call.return_data[0] >= m_param2:
          call munknown16318a6em[m_param3m]m.field_0.transferWithReference(address to, uint256 value, string reference) with:
               gas gas_remaining - 34050 wei
              args addr(m_param1), m_param2, Array(len=m_param4.length, data=m_param4[allm])
      else:
          call munknown16318a6em[m_param3m]m.field_0.transferWithReference(address to, uint256 value, string reference) with:
             value eth.balance(this.address) wei
               gas gas_remaining - 34050 wei
              args addr(m_param1), m_param2, Array(len=m_param4.length, data=m_param4[allm])
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  log 0xae7443dd: _param2, Array(len=_param4.length, data=_param4[all]), caller, _param1, _param3
  return 1


# hash = 0x8d2ffdc9
# getter = None
# const = None
# payable = True
def unknown8d2ffdc9(uint256 m_param1) payable: 
  call munknown16318a6em[mstor4m[callerm]m]m.field_0.multiAsset() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  call addr(ext_call.return_data[0]).registryICAP() with:
       gas gas_remaining - 25050 wei
  call addr(ext_call.return_data[0]).assets(bytes32 param1) with:
       gas gas_remaining - 25050 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
  return ext_call.return_data[0]


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, 'caller'], 4]]]
# const = None
# payable = True
def symbol() payable: 
  return msymbolm[callerm]


# hash = 0x9fb2f43b
# getter = None
# const = ['return', 7200]
# payable = True
const unknown9fb2f43b = (2 * 3600)


# hash = 0x9fda5b66
# getter = ['struct', ['loc', 2]]
# const = None
# payable = True
def assets(bytes32 m_param1) payable: 
  return munknown16318a6em[m_param1m]m.field_0, 
         munknown16318a6em[m_param1m]m.field_256,
         munknown16318a6em[m_param1m]m.field_512,
         munknown16318a6em[m_param1m]m.field_768,
         bool(munknown16318a6em[m_param1m]m.field_1536),
         bool(munknown16318a6em[m_param1m]m.field_1544)


# hash = 0xb214faa5
# getter = None
# const = None
# payable = True
def deposit(bytes32 m_walletID) payable: 
  if call.value <= 0:
      return 0
  log 0x14fb04f0: call.value, caller, _walletID
  log 0x7a0322de: _walletID, call.value, caller, this.address
  return 1


# hash = 0xce606ee0
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def contractOwner() payable: 
  return mcontractOwner


# hash = 0xd0e30db0
# getter = None
# const = None
# payable = True
def deposit() payable: 
  if call.value <= 0:
      return 0
  log Deposit(address from, uint256 value, string comment):
              call.value,
              64,
              0,
              caller,
  return 1


# hash = 0xd2e646d2
# getter = None
# const = None
# payable = True
def unknownd2e646d2(uint256 m_param1, uint256 m_param2) payable: 
  return (m_param1 - m_param2 % 24 * 3600 / 2 * 3600)


# hash = 0xf89005e7
# getter = None
# const = None
# payable = True
def unknownf89005e7(array m_param1) payable: 
  if call.value <= 0:
      return 0
  log Deposit(
        address from=call.value,
        uint256 value=Array(len=_param1.length, data=_param1[all]),
        string comment=caller)
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


