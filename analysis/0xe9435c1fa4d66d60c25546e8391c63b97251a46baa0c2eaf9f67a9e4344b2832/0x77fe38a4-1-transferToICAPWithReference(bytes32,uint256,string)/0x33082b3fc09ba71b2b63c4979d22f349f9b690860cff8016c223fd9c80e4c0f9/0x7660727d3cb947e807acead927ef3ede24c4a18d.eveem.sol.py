# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x7660727D3cb947e807AceAD927eF3Ede24C4a18D 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    multiAssetAddress # mask: a s
    # storage address 2
    symbol # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4
    # storage address 5
    unknownaa46f961Address # mask: a s
    # storage address 5
    stor5 # mask: a s
# hash = 0x029a8bf7
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def multiAsset() payable: 
  return addr(mmultiAssetAddress)


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = True
def approve(address m_spender, uint256 m_value) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if tx.origin != caller:
      return 0
  call addr(mmultiAssetAddress).0x4f09eba7 with:
       gas gas_remaining - 25050 wei
      args addr(m_spender), m_value, msymbol
  require ext_call.success
  return bool(ext_call.return_data[0])


# hash = 0x12ab7242
# getter = None
# const = None
# payable = True
def setupStackDepthLib(address m_stackDepthLib) payable: 
  if addr(mstor0) != 0:
      return 0
  uint256(mstor0) = m_stackDepthLib or Mask(96, 160, uint256(mstor0))
  return 1


# hash = 0x18160ddd
# getter = None
# const = None
# payable = True
def totalSupply() payable: 
  call addr(mmultiAssetAddress).totalSupply(bytes32 symbol) with:
       gas gas_remaining - 25050 wei
      args msymbol
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x1a9237de
# getter = None
# const = None
# payable = True
def unknown1a9237de(uint256 m_param1) payable: 
  call addr(mmultiAssetAddress).registryICAP() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
       gas gas_remaining - 25050 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
  return bool(uint8(mstor4m[ext_call.return_data[12 len 20]m]))


# hash = 0x23385089
# getter = None
# const = None
# payable = True
def emitApprove(address m_from, address m_spender, uint256 m_value) payable: 
  if caller == addr(mmultiAssetAddress):
      log Approve(
            address target=_value,
            address spender=_from,
            uint256 value=_spender)


# hash = 0x23b872dd
# getter = None
# const = None
# payable = True
def transferFrom(address m_from, address m_to, uint256 m_value) payable: 
  if call.value <= 0:
      if tx.origin != caller:
          return 0
      if uint8(mstor4m[addr(m_to)m]):
          call addr(mmultiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args 0, 0, addr(m_to), m_value, msymbol, 160, 0, None
          require ext_call.success
          return bool(ext_call.return_data[0])
      uint8(mstor3m.field_0) = 1
      call addr(mmultiAssetAddress).0xf0cbe059 with:
           gas gas_remaining - 25050 wei
          args 0, 0, addr(this.address), m_value, msymbol, 160, 0, None
      if ext_call.success:
          uint8(mstor3m.field_0) = 0
          if not ext_call.return_data[0]:
              return 0
          if m_to == this.address:
              call caller with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
          else:
              call m_to with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
          if ext_call.success:
              return 1
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      if ext_call.success:
          if tx.origin != caller:
              return 0
          if uint8(mstor4m[addr(m_to)m]):
              call addr(mmultiAssetAddress).0xf0cbe059 with:
                   gas gas_remaining - 25050 wei
                  args 0, 0, addr(m_to), m_value, msymbol, 160, 0, None
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(mstor3m.field_0) = 1
          call addr(mmultiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args 0, 0, addr(this.address), m_value, msymbol, 160, 0, None
          if ext_call.success:
              uint8(mstor3m.field_0) = 0
              if not ext_call.return_data[0]:
                  return 0
              if m_to == this.address:
                  call caller with:
                     value m_value wei
                       gas gas_remaining - 34050 wei
              else:
                  call m_to with:
                     value m_value wei
                       gas gas_remaining - 34050 wei
              if ext_call.success:
                  return 1
  revert 


# hash = 0x23de6651
# getter = None
# const = None
# payable = True
def emitTransfer(address m_from, address m_to, uint256 m_value) payable: 
  if caller == addr(mmultiAssetAddress):
      log Transfer(
            address from=_value,
            address to=_from,
            uint256 value=_to)
  if m_to == this.address:
      if uint8(mstor3m.field_0):
          stop
  else:
      if uint8(mstor4m[addr(m_to)m]):
          stop
      if uint8(mstor3m.field_8):
          stop
      if uint8(mstor3m.field_16):
          stop
  revert 


# hash = 0x2cc0b254
# getter = None
# const = None
# payable = True
def init(address m_multiAsset, bytes32 m_symbol) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if addr(mmultiAssetAddress):
      return 0
  call m_multiAsset.issueAsset(bytes32 symbol, uint256 value, string name, string description, uint8 baseUnit, bool isReissuable) with:
       gas gas_remaining - 25050 wei
      args 0, uint32(m_symbol), 0, 192, 256, 0, 1, 8, 'WeiToken', 16, '1-to-1 with wei.'
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  call m_multiAsset.0x6489899 with:
       gas gas_remaining - 25050 wei
      args addr(this.address), 1, m_symbol
  require ext_call.success
  require ext_call.return_data[0]
  call m_multiAsset.0x30d30c89 with:
       gas gas_remaining - 25050 wei
      args addr(this.address), m_symbol
  require ext_call.success
  require ext_call.return_data[0]
  call m_multiAsset.0xf01b0220 with:
       gas gas_remaining - 25050 wei
      args 0, 1, m_symbol
  require ext_call.success
  require ext_call.return_data[0]
  uint256(mstor1) = m_multiAsset or Mask(96, 160, uint256(mstor1))
  msymbol = m_symbol
  return 1


# hash = 0x490c0e8f
# getter = None
# const = None
# payable = True
def unknown490c0e8f(addr m_param1, array m_param2) payable: 
  if 0 == call.value:
      return 0
  if m_param1 == this.address:
      if call.value <= 0:
          return 0
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
      return 0
  uint8(mstor3m.field_0) = 1
  call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
       gas gas_remaining - 25050 wei
      args addr(this.address), msymbol
  require ext_call.success
  if ext_call.return_data[0] >= call.value:
      uint8(mstor3m.field_0) = 0
  else:
      call addr(mmultiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
           gas gas_remaining - 25050 wei
          args msymbol, call.value
      require ext_call.success
      uint8(mstor3m.field_0) = 0
      if not ext_call.return_data[0]:
          if call.value <= 0:
              return 0
          call caller with:
             value call.value wei
               gas gas_remaining - 34050 wei
          require ext_call.success
          return 0
  uint8(mstor3m.field_8) = 1
  call addr(mmultiAssetAddress).0x6e293817 with:
       gas gas_remaining - 25050 wei
      args addr(m_param1), call.value, msymbol, Array(len=m_param2.length, data=m_param2[allm])
  require ext_call.success
  uint8(mstor3m.field_8) = 0
  if ext_call.return_data[0]:
      return 1
  if call.value <= 0:
      uint8(mstor3m.field_16) = 1
      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), msymbol
      require ext_call.success
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
      uint8(mstor3m.field_16) = 1
      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), msymbol
  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
       gas gas_remaining - 25050 wei
      args msymbol, ext_call.return_data[0]
  uint8(mstor3m.field_16) = 0
  return bool(ext_call.return_data[0])


# hash = 0x6461fe39
# getter = None
# const = None
# payable = True
def transferFromWithReference(address m_from, address m_to, uint256 m_value, string m_reference) payable: 
  if call.value <= 0:
      if tx.origin != caller:
          return 0
      if uint8(mstor4m[addr(m_to)m]):
          call addr(mmultiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args addr(m_from), addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
          require ext_call.success
          return bool(ext_call.return_data[0])
      uint8(mstor3m.field_0) = 1
      call addr(mmultiAssetAddress).0xf0cbe059 with:
           gas gas_remaining - 25050 wei
          args addr(m_from), addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
      if ext_call.success:
          uint8(mstor3m.field_0) = 0
          if not ext_call.return_data[0]:
              return 0
          if m_to == this.address:
              call caller with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
          else:
              call m_to with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
          if ext_call.success:
              return 1
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      if ext_call.success:
          if tx.origin != caller:
              return 0
          if uint8(mstor4m[addr(m_to)m]):
              call addr(mmultiAssetAddress).0xf0cbe059 with:
                   gas gas_remaining - 25050 wei
                  args addr(m_from), addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(mstor3m.field_0) = 1
          call addr(mmultiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args addr(m_from), addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
          if ext_call.success:
              uint8(mstor3m.field_0) = 0
              if not ext_call.return_data[0]:
                  return 0
              if m_to == this.address:
                  call caller with:
                     value m_value wei
                       gas gas_remaining - 34050 wei
              else:
                  call m_to with:
                     value m_value wei
                       gas gas_remaining - 34050 wei
              if ext_call.success:
                  return 1
  revert 


# hash = 0x6620a935
# getter = None
# const = None
# payable = True
def sendToOwner() payable: 
  if call.value <= 0:
      return 1
  call caller with:
     value call.value wei
       gas gas_remaining - 34050 wei
  require ext_call.success
  return 1


# hash = 0x70a08231
# getter = None
# const = None
# payable = True
def balanceOf(address m_owner) payable: 
  call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
       gas gas_remaining - 25050 wei
      args addr(m_owner), msymbol
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x733480b7
# getter = None
# const = None
# payable = True
def transferToICAP(bytes32 m_icap, uint256 m_value) payable: 
  if 0 == call.value:
      call addr(mmultiAssetAddress).registryICAP() with:
           gas gas_remaining - 25050 wei
      if ext_call.success:
          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
               gas gas_remaining - 25050 wei
              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
          if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
              if caller == tx.origin:
                  call addr(mmultiAssetAddress).0xc5487661 with:
                       gas gas_remaining - 25050 wei
                      args m_icap, m_value, 96, 0
              else:
                  call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                       gas gas_remaining - 25050 wei
                      args caller, m_icap, m_value, 128, 0
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(mstor3m.field_0) = 1
          if caller == tx.origin:
              call addr(mmultiAssetAddress).0x64ef212e with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), m_value, msymbol, 128, 0
          else:
              call addr(mmultiAssetAddress).0x31c6c4cf with:
                   gas gas_remaining - 25050 wei
                  args caller, addr(this.address), m_value, msymbol, 160, 0
          if ext_call.success:
              uint8(mstor3m.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              call addr(munknownaa46f961Address).0xd882aa0 with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
                  args m_icap, 64, 0
              if ext_call.success:
                  if ext_call.return_data[0]:
                      return bool(ext_call.return_data[0])
  else:
      if caller == this.address:
          if call.value <= 0:
              call addr(mmultiAssetAddress).registryICAP() with:
                   gas gas_remaining - 25050 wei
              if ext_call.success:
                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                       gas gas_remaining - 25050 wei
                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                      if caller == tx.origin:
                          call addr(mmultiAssetAddress).0xc5487661 with:
                               gas gas_remaining - 25050 wei
                              args m_icap, m_value, 96, 0
                      else:
                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                               gas gas_remaining - 25050 wei
                              args caller, m_icap, m_value, 128, 0
                      require ext_call.success
                      return bool(ext_call.return_data[0])
                  uint8(mstor3m.field_0) = 1
                  if caller == tx.origin:
                      call addr(mmultiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), m_value, msymbol, 128, 0
                  else:
                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), m_value, msymbol, 160, 0
                  if ext_call.success:
                      uint8(mstor3m.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      call addr(munknownaa46f961Address).0xd882aa0 with:
                         value m_value wei
                           gas gas_remaining - 34050 wei
                          args m_icap, 64, 0
                      if ext_call.success:
                          if ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
          else:
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  call addr(mmultiAssetAddress).registryICAP() with:
                       gas gas_remaining - 25050 wei
                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                       gas gas_remaining - 25050 wei
                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                      if caller == tx.origin:
                          call addr(mmultiAssetAddress).0xc5487661 with:
                               gas gas_remaining - 25050 wei
                              args m_icap, m_value, 96, 0
                      else:
                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                               gas gas_remaining - 25050 wei
                              args caller, m_icap, m_value, 128, 0
                      require ext_call.success
                      return bool(ext_call.return_data[0])
                  uint8(mstor3m.field_0) = 1
                  if caller == tx.origin:
                      call addr(mmultiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), m_value, msymbol, 128, 0
                  else:
                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), m_value, msymbol, 160, 0
                  if ext_call.success:
                      uint8(mstor3m.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      call addr(munknownaa46f961Address).0xd882aa0 with:
                         value m_value wei
                           gas gas_remaining - 34050 wei
                          args m_icap, 64, 0
                      if ext_call.success:
                          if ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
      else:
          uint8(mstor3m.field_0) = 1
          call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
               gas gas_remaining - 25050 wei
              args addr(this.address), msymbol
          if ext_call.success:
              if ext_call.return_data[0] >= call.value:
                  uint8(mstor3m.field_0) = 0
                  uint8(mstor3m.field_8) = 1
                  mem[356] = mem[381 len 7]
                  call addr(mmultiAssetAddress).0x6e293817 with:
                       gas gas_remaining - 25050 wei
                      args caller, call.value, msymbol, Array(len=7, data=mem[356])
                  if ext_call.success:
                      uint8(mstor3m.field_8) = 0
                      if ext_call.return_data[0]:
                          call addr(mmultiAssetAddress).registryICAP() with:
                               gas gas_remaining - 25050 wei
                          if ext_call.success:
                              call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                   gas gas_remaining - 25050 wei
                                  args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                              if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0xc5487661 with:
                                           gas gas_remaining - 25050 wei
                                          args m_icap, m_value, 96, 0
                                  else:
                                      call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                           gas gas_remaining - 25050 wei
                                          args caller, m_icap, m_value, 128, 0
                                  require ext_call.success
                                  return bool(ext_call.return_data[0])
                              uint8(mstor3m.field_0) = 1
                              if caller == tx.origin:
                                  call addr(mmultiAssetAddress).0x64ef212e with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), m_value, msymbol, 128, 0
                              else:
                                  call addr(mmultiAssetAddress).0x31c6c4cf with:
                                       gas gas_remaining - 25050 wei
                                      args caller, addr(this.address), m_value, msymbol, 160, 0
                              if ext_call.success:
                                  uint8(mstor3m.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return bool(ext_call.return_data[0])
                                  call addr(munknownaa46f961Address).0xd882aa0 with:
                                     value m_value wei
                                       gas gas_remaining - 34050 wei
                                      args m_icap, 64, 0
                                  if ext_call.success:
                                      if ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                      else:
                          if call.value <= 0:
                              uint8(mstor3m.field_16) = 1
                              call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), msymbol
                              if ext_call.success:
                                  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args msymbol, ext_call.return_data[0]
                                  uint8(mstor3m.field_16) = 0
                                  call addr(mmultiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args m_icap, m_value, 96, 0
                                      else:
                                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, m_icap, m_value, 128, 0
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, 128, 0
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, 160, 0
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(munknownaa46f961Address).0xd882aa0 with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                          args m_icap, 64, 0
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  uint8(mstor3m.field_16) = 1
                                  call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), msymbol
                                  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args msymbol, ext_call.return_data[0]
                                  uint8(mstor3m.field_16) = 0
                                  call addr(mmultiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args m_icap, m_value, 96, 0
                                      else:
                                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, m_icap, m_value, 128, 0
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, 128, 0
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, 160, 0
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(munknownaa46f961Address).0xd882aa0 with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                          args m_icap, 64, 0
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
              else:
                  call addr(mmultiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
                       gas gas_remaining - 25050 wei
                      args msymbol, call.value
                  if ext_call.success:
                      uint8(mstor3m.field_0) = 0
                      if not ext_call.return_data[0]:
                          if call.value <= 0:
                              call addr(mmultiAssetAddress).registryICAP() with:
                                   gas gas_remaining - 25050 wei
                              if ext_call.success:
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args m_icap, m_value, 96, 0
                                      else:
                                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, m_icap, m_value, 128, 0
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, 128, 0
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, 160, 0
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(munknownaa46f961Address).0xd882aa0 with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                          args m_icap, 64, 0
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  call addr(mmultiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args m_icap, m_value, 96, 0
                                      else:
                                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, m_icap, m_value, 128, 0
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, 128, 0
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, 160, 0
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(munknownaa46f961Address).0xd882aa0 with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                          args m_icap, 64, 0
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                      else:
                          uint8(mstor3m.field_8) = 1
                          mem[356] = mem[381 len 7]
                          call addr(mmultiAssetAddress).0x6e293817 with:
                               gas gas_remaining - 25050 wei
                              args caller, call.value, msymbol, Array(len=7, data=mem[356])
                          if ext_call.success:
                              uint8(mstor3m.field_8) = 0
                              if ext_call.return_data[0]:
                                  call addr(mmultiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  if ext_call.success:
                                      call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                           gas gas_remaining - 25050 wei
                                          args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                      if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0xc5487661 with:
                                                   gas gas_remaining - 25050 wei
                                                  args m_icap, m_value, 96, 0
                                          else:
                                              call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, m_icap, m_value, 128, 0
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                      uint8(mstor3m.field_0) = 1
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0x64ef212e with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), m_value, msymbol, 128, 0
                                      else:
                                          call addr(mmultiAssetAddress).0x31c6c4cf with:
                                               gas gas_remaining - 25050 wei
                                              args caller, addr(this.address), m_value, msymbol, 160, 0
                                      if ext_call.success:
                                          uint8(mstor3m.field_0) = 0
                                          if not ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                                          call addr(munknownaa46f961Address).0xd882aa0 with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                              args m_icap, 64, 0
                                          if ext_call.success:
                                              if ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                              else:
                                  if call.value <= 0:
                                      uint8(mstor3m.field_16) = 1
                                      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), msymbol
                                      if ext_call.success:
                                          call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args msymbol, ext_call.return_data[0]
                                          uint8(mstor3m.field_16) = 0
                                          call addr(mmultiAssetAddress).registryICAP() with:
                                               gas gas_remaining - 25050 wei
                                          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                               gas gas_remaining - 25050 wei
                                              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                          if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                              if caller == tx.origin:
                                                  call addr(mmultiAssetAddress).0xc5487661 with:
                                                       gas gas_remaining - 25050 wei
                                                      args m_icap, m_value, 96, 0
                                              else:
                                                  call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                       gas gas_remaining - 25050 wei
                                                      args caller, m_icap, m_value, 128, 0
                                              require ext_call.success
                                              return bool(ext_call.return_data[0])
                                          uint8(mstor3m.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), m_value, msymbol, 128, 0
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), m_value, msymbol, 160, 0
                                          if ext_call.success:
                                              uint8(mstor3m.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              call addr(munknownaa46f961Address).0xd882aa0 with:
                                                 value m_value wei
                                                   gas gas_remaining - 34050 wei
                                                  args m_icap, 64, 0
                                              if ext_call.success:
                                                  if ext_call.return_data[0]:
                                                      return bool(ext_call.return_data[0])
                                  else:
                                      call caller with:
                                         value call.value wei
                                           gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          uint8(mstor3m.field_16) = 1
                                          call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), msymbol
                                          call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args msymbol, ext_call.return_data[0]
                                          uint8(mstor3m.field_16) = 0
                                          call addr(mmultiAssetAddress).registryICAP() with:
                                               gas gas_remaining - 25050 wei
                                          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                               gas gas_remaining - 25050 wei
                                              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                          if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                              if caller == tx.origin:
                                                  call addr(mmultiAssetAddress).0xc5487661 with:
                                                       gas gas_remaining - 25050 wei
                                                      args m_icap, m_value, 96, 0
                                              else:
                                                  call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                       gas gas_remaining - 25050 wei
                                                      args caller, m_icap, m_value, 128, 0
                                              require ext_call.success
                                              return bool(ext_call.return_data[0])
                                          uint8(mstor3m.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), m_value, msymbol, 128, 0
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), m_value, msymbol, 160, 0
                                          if ext_call.success:
                                              uint8(mstor3m.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              call addr(munknownaa46f961Address).0xd882aa0 with:
                                                 value m_value wei
                                                   gas gas_remaining - 34050 wei
                                                  args m_icap, 64, 0
                                              if ext_call.success:
                                                  if ext_call.return_data[0]:
                                                      return bool(ext_call.return_data[0])
  revert 


# hash = 0x77fe38a4
# getter = None
# const = None
# payable = True
def transferToICAPWithReference(bytes32 m_icap, uint256 m_value, string m_reference) payable: 
  if 0 == call.value:
      call addr(mmultiAssetAddress).registryICAP() with:
           gas gas_remaining - 25050 wei
      if ext_call.success:
          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
               gas gas_remaining - 25050 wei
              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
          if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
              if caller == tx.origin:
                  call addr(mmultiAssetAddress).0xc5487661 with:
                       gas gas_remaining - 25050 wei
                      args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
              else:
                  call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                       gas gas_remaining - 25050 wei
                      args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(mstor3m.field_0) = 1
          if caller == tx.origin:
              call addr(mmultiAssetAddress).0x64ef212e with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
          else:
              call addr(mmultiAssetAddress).0x31c6c4cf with:
                   gas gas_remaining - 25050 wei
                  args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
          if ext_call.success:
              uint8(mstor3m.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              call addr(munknownaa46f961Address).0xd882aa0 with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
                  args m_icap, Array(len=m_reference.length, data=m_reference[allm])
              if ext_call.success:
                  if ext_call.return_data[0]:
                      return bool(ext_call.return_data[0])
  else:
      if caller == this.address:
          if call.value <= 0:
              call addr(mmultiAssetAddress).registryICAP() with:
                   gas gas_remaining - 25050 wei
              if ext_call.success:
                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                       gas gas_remaining - 25050 wei
                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                      if caller == tx.origin:
                          call addr(mmultiAssetAddress).0xc5487661 with:
                               gas gas_remaining - 25050 wei
                              args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                      else:
                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                               gas gas_remaining - 25050 wei
                              args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                      require ext_call.success
                      return bool(ext_call.return_data[0])
                  uint8(mstor3m.field_0) = 1
                  if caller == tx.origin:
                      call addr(mmultiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                  else:
                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                  if ext_call.success:
                      uint8(mstor3m.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      call addr(munknownaa46f961Address).0xd882aa0 with:
                         value m_value wei
                           gas gas_remaining - 34050 wei
                          args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                      if ext_call.success:
                          if ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
          else:
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  call addr(mmultiAssetAddress).registryICAP() with:
                       gas gas_remaining - 25050 wei
                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                       gas gas_remaining - 25050 wei
                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                      if caller == tx.origin:
                          call addr(mmultiAssetAddress).0xc5487661 with:
                               gas gas_remaining - 25050 wei
                              args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                      else:
                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                               gas gas_remaining - 25050 wei
                              args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                      require ext_call.success
                      return bool(ext_call.return_data[0])
                  uint8(mstor3m.field_0) = 1
                  if caller == tx.origin:
                      call addr(mmultiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                  else:
                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                  if ext_call.success:
                      uint8(mstor3m.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      call addr(munknownaa46f961Address).0xd882aa0 with:
                         value m_value wei
                           gas gas_remaining - 34050 wei
                          args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                      if ext_call.success:
                          if ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
      else:
          uint8(mstor3m.field_0) = 1
          call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
               gas gas_remaining - 25050 wei
              args addr(this.address), msymbol
          if ext_call.success:
              if ext_call.return_data[0] >= call.value:
                  uint8(mstor3m.field_0) = 0
                  uint8(mstor3m.field_8) = 1
                  mem[ceil32(m_reference.length) + 356] = mem[ceil32(m_reference.length) + 381 len 7]
                  call addr(mmultiAssetAddress).0x6e293817 with:
                       gas gas_remaining - 25050 wei
                      args caller, call.value, msymbol, Array(len=7, data=mem[ceil32(m_reference.length) + 356])
                  if ext_call.success:
                      uint8(mstor3m.field_8) = 0
                      if ext_call.return_data[0]:
                          call addr(mmultiAssetAddress).registryICAP() with:
                               gas gas_remaining - 25050 wei
                          if ext_call.success:
                              call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                   gas gas_remaining - 25050 wei
                                  args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                              if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0xc5487661 with:
                                           gas gas_remaining - 25050 wei
                                          args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                  else:
                                      call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                           gas gas_remaining - 25050 wei
                                          args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                  require ext_call.success
                                  return bool(ext_call.return_data[0])
                              uint8(mstor3m.field_0) = 1
                              if caller == tx.origin:
                                  call addr(mmultiAssetAddress).0x64ef212e with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                              else:
                                  call addr(mmultiAssetAddress).0x31c6c4cf with:
                                       gas gas_remaining - 25050 wei
                                      args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                              if ext_call.success:
                                  uint8(mstor3m.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return bool(ext_call.return_data[0])
                                  call addr(munknownaa46f961Address).0xd882aa0 with:
                                     value m_value wei
                                       gas gas_remaining - 34050 wei
                                      args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                                  if ext_call.success:
                                      if ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                      else:
                          if call.value <= 0:
                              uint8(mstor3m.field_16) = 1
                              call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), msymbol
                              if ext_call.success:
                                  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args msymbol, ext_call.return_data[0]
                                  uint8(mstor3m.field_16) = 0
                                  call addr(mmultiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                      else:
                                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(munknownaa46f961Address).0xd882aa0 with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                          args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  uint8(mstor3m.field_16) = 1
                                  call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), msymbol
                                  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args msymbol, ext_call.return_data[0]
                                  uint8(mstor3m.field_16) = 0
                                  call addr(mmultiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                      else:
                                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(munknownaa46f961Address).0xd882aa0 with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                          args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
              else:
                  call addr(mmultiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
                       gas gas_remaining - 25050 wei
                      args msymbol, call.value
                  if ext_call.success:
                      uint8(mstor3m.field_0) = 0
                      if not ext_call.return_data[0]:
                          if call.value <= 0:
                              call addr(mmultiAssetAddress).registryICAP() with:
                                   gas gas_remaining - 25050 wei
                              if ext_call.success:
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                      else:
                                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(munknownaa46f961Address).0xd882aa0 with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                          args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  call addr(mmultiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                      else:
                                          call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(munknownaa46f961Address).0xd882aa0 with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                          args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                      else:
                          uint8(mstor3m.field_8) = 1
                          mem[ceil32(m_reference.length) + 356] = mem[ceil32(m_reference.length) + 381 len 7]
                          call addr(mmultiAssetAddress).0x6e293817 with:
                               gas gas_remaining - 25050 wei
                              args caller, call.value, msymbol, Array(len=7, data=mem[ceil32(m_reference.length) + 356])
                          if ext_call.success:
                              uint8(mstor3m.field_8) = 0
                              if ext_call.return_data[0]:
                                  call addr(mmultiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  if ext_call.success:
                                      call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                           gas gas_remaining - 25050 wei
                                          args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                      if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0xc5487661 with:
                                                   gas gas_remaining - 25050 wei
                                                  args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                          else:
                                              call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                      uint8(mstor3m.field_0) = 1
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0x64ef212e with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                      else:
                                          call addr(mmultiAssetAddress).0x31c6c4cf with:
                                               gas gas_remaining - 25050 wei
                                              args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                      if ext_call.success:
                                          uint8(mstor3m.field_0) = 0
                                          if not ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                                          call addr(munknownaa46f961Address).0xd882aa0 with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                              args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                                          if ext_call.success:
                                              if ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                              else:
                                  if call.value <= 0:
                                      uint8(mstor3m.field_16) = 1
                                      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), msymbol
                                      if ext_call.success:
                                          call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args msymbol, ext_call.return_data[0]
                                          uint8(mstor3m.field_16) = 0
                                          call addr(mmultiAssetAddress).registryICAP() with:
                                               gas gas_remaining - 25050 wei
                                          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                               gas gas_remaining - 25050 wei
                                              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                          if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                              if caller == tx.origin:
                                                  call addr(mmultiAssetAddress).0xc5487661 with:
                                                       gas gas_remaining - 25050 wei
                                                      args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                              else:
                                                  call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                       gas gas_remaining - 25050 wei
                                                      args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                              require ext_call.success
                                              return bool(ext_call.return_data[0])
                                          uint8(mstor3m.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          if ext_call.success:
                                              uint8(mstor3m.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              call addr(munknownaa46f961Address).0xd882aa0 with:
                                                 value m_value wei
                                                   gas gas_remaining - 34050 wei
                                                  args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                                              if ext_call.success:
                                                  if ext_call.return_data[0]:
                                                      return bool(ext_call.return_data[0])
                                  else:
                                      call caller with:
                                         value call.value wei
                                           gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          uint8(mstor3m.field_16) = 1
                                          call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), msymbol
                                          call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args msymbol, ext_call.return_data[0]
                                          uint8(mstor3m.field_16) = 0
                                          call addr(mmultiAssetAddress).registryICAP() with:
                                               gas gas_remaining - 25050 wei
                                          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                               gas gas_remaining - 25050 wei
                                              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                          if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                                              if caller == tx.origin:
                                                  call addr(mmultiAssetAddress).0xc5487661 with:
                                                       gas gas_remaining - 25050 wei
                                                      args m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                              else:
                                                  call addr(mmultiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                       gas gas_remaining - 25050 wei
                                                      args caller, m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                                              require ext_call.success
                                              return bool(ext_call.return_data[0])
                                          uint8(mstor3m.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          if ext_call.success:
                                              uint8(mstor3m.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              call addr(munknownaa46f961Address).0xd882aa0 with:
                                                 value m_value wei
                                                   gas gas_remaining - 34050 wei
                                                  args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                                              if ext_call.success:
                                                  if ext_call.return_data[0]:
                                                      return bool(ext_call.return_data[0])
  revert 


# hash = 0x82fc49b8
# getter = None
# const = None
# payable = True
def setCosignerAddress(address m_cosigner) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if tx.origin != caller:
      return 0
  call addr(mmultiAssetAddress).0xe82b7cb2 with:
       gas gas_remaining - 25050 wei
      args addr(m_cosigner), msymbol
  require ext_call.success
  return bool(ext_call.return_data[0])


# hash = 0x8bbbbfd3
# getter = None
# const = None
# payable = True
def unknown8bbbbfd3(uint256 m_param1) payable: 
  uint256(mstor4m[callerm]) = m_param1 or Mask(248, 8, uint256(mstor4m[callerm]))
  return 1


# hash = 0x95d89b41
# getter = ['storage', 256, 0, 2]
# const = None
# payable = True
def symbol() payable: 
  return msymbol


# hash = 0xa340fff4
# getter = None
# const = None
# payable = True
def unknowna340fff4() payable: 
  if call.value <= 0:
      uint8(mstor3m.field_16) = 1
      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), msymbol
      require ext_call.success
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
      uint8(mstor3m.field_16) = 1
      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), msymbol
  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
       gas gas_remaining - 25050 wei
      args msymbol, ext_call.return_data[0]
  uint8(mstor3m.field_16) = 0
  return bool(ext_call.return_data[0])


# hash = 0xa48a663c
# getter = None
# const = None
# payable = True
def transferFromToICAPWithReference(address m_from, bytes32 m_icap, uint256 m_value, string m_reference) payable: 
  if call.value <= 0:
      if tx.origin != caller:
          return 0
      call addr(mmultiAssetAddress).registryICAP() with:
           gas gas_remaining - 25050 wei
      if ext_call.success:
          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
               gas gas_remaining - 25050 wei
              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
          if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
              call addr(mmultiAssetAddress).0xea98e540 with:
                   gas gas_remaining - 25050 wei
                  args addr(m_from), m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(mstor3m.field_0) = 1
          call addr(mmultiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args addr(m_from), addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
          if ext_call.success:
              uint8(mstor3m.field_0) = 0
              if not ext_call.return_data[0]:
                  return 0
              call addr(munknownaa46f961Address).0xd882aa0 with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
                  args m_icap, Array(len=m_reference.length, data=m_reference[allm])
              if ext_call.success:
                  if ext_call.return_data[0]:
                      return 1
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      if ext_call.success:
          if tx.origin != caller:
              return 0
          call addr(mmultiAssetAddress).registryICAP() with:
               gas gas_remaining - 25050 wei
          if ext_call.success:
              call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                   gas gas_remaining - 25050 wei
                  args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
              if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                  call addr(mmultiAssetAddress).0xea98e540 with:
                       gas gas_remaining - 25050 wei
                      args addr(m_from), m_icap, m_value, Array(len=m_reference.length, data=m_reference[allm])
                  require ext_call.success
                  return bool(ext_call.return_data[0])
              uint8(mstor3m.field_0) = 1
              call addr(mmultiAssetAddress).0xf0cbe059 with:
                   gas gas_remaining - 25050 wei
                  args addr(m_from), addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
              if ext_call.success:
                  uint8(mstor3m.field_0) = 0
                  if not ext_call.return_data[0]:
                      return 0
                  call addr(munknownaa46f961Address).0xd882aa0 with:
                     value m_value wei
                       gas gas_remaining - 34050 wei
                      args m_icap, Array(len=m_reference.length, data=m_reference[allm])
                  if ext_call.success:
                      if ext_call.return_data[0]:
                          return 1
  revert 


# hash = 0xa525f42c
# getter = None
# const = None
# payable = True
def transferFromToICAP(address m_from, bytes32 m_icap, uint256 m_value) payable: 
  if call.value <= 0:
      if tx.origin != caller:
          return 0
      call addr(mmultiAssetAddress).registryICAP() with:
           gas gas_remaining - 25050 wei
      if ext_call.success:
          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
               gas gas_remaining - 25050 wei
              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
          if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
              call addr(mmultiAssetAddress).0xea98e540 with:
                   gas gas_remaining - 25050 wei
                  args 0, 0, m_icap, m_value, 128, 0, 0, None
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(mstor3m.field_0) = 1
          call addr(mmultiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args 0, 0, addr(this.address), m_value, msymbol, 160, 0, None
          if ext_call.success:
              uint8(mstor3m.field_0) = 0
              if not ext_call.return_data[0]:
                  return 0
              call addr(munknownaa46f961Address).0xd882aa0 with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
                  args m_icap, 64, 0
              if ext_call.success:
                  if ext_call.return_data[0]:
                      return 1
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      if ext_call.success:
          if tx.origin != caller:
              return 0
          call addr(mmultiAssetAddress).registryICAP() with:
               gas gas_remaining - 25050 wei
          if ext_call.success:
              call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                   gas gas_remaining - 25050 wei
                  args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
              if uint8(mstor4m[ext_call.return_data[12 len 20]m]):
                  call addr(mmultiAssetAddress).0xea98e540 with:
                       gas gas_remaining - 25050 wei
                      args 0, 0, m_icap, m_value, 128, 0, 0, None
                  require ext_call.success
                  return bool(ext_call.return_data[0])
              uint8(mstor3m.field_0) = 1
              call addr(mmultiAssetAddress).0xf0cbe059 with:
                   gas gas_remaining - 25050 wei
                  args 0, 0, addr(this.address), m_value, msymbol, 160, 0, None
              if ext_call.success:
                  uint8(mstor3m.field_0) = 0
                  if not ext_call.return_data[0]:
                      return 0
                  call addr(munknownaa46f961Address).0xd882aa0 with:
                     value m_value wei
                       gas gas_remaining - 34050 wei
                      args m_icap, 64, 0
                  if ext_call.success:
                      if ext_call.return_data[0]:
                          return 1
  revert 


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = True
def transfer(address m_to, uint256 m_value) payable: 
  if 0 == call.value:
      if uint8(mstor4m[addr(m_to)m]):
          if m_to != caller:
              if caller == tx.origin:
                  call addr(mmultiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args addr(m_to), m_value, msymbol, 128, 0
              else:
                  call addr(mmultiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args caller, addr(m_to), m_value, msymbol, 160, 0
              require ext_call.success
              return bool(ext_call.return_data[0])
      uint8(mstor3m.field_0) = 1
      if caller == tx.origin:
          call addr(mmultiAssetAddress).0x64ef212e with:
               gas gas_remaining - 25050 wei
              args addr(this.address), m_value, msymbol, 128, 0
      else:
          call addr(mmultiAssetAddress).0x31c6c4cf with:
               gas gas_remaining - 25050 wei
              args caller, addr(this.address), m_value, msymbol, 160, 0
      if ext_call.success:
          uint8(mstor3m.field_0) = 0
          if not ext_call.return_data[0]:
              return bool(ext_call.return_data[0])
          if m_to == this.address:
              call caller with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
          else:
              call m_to with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
          if ext_call.success:
              return bool(ext_call.return_data[0])
  else:
      if caller == this.address:
          if call.value <= 0:
              if uint8(mstor4m[addr(m_to)m]):
                  if m_to != caller:
                      if caller == tx.origin:
                          call addr(mmultiAssetAddress).0x64ef212e with:
                               gas gas_remaining - 25050 wei
                              args addr(m_to), m_value, msymbol, 128, 0
                      else:
                          call addr(mmultiAssetAddress).0x31c6c4cf with:
                               gas gas_remaining - 25050 wei
                              args caller, addr(m_to), m_value, msymbol, 160, 0
                      require ext_call.success
                      return bool(ext_call.return_data[0])
              uint8(mstor3m.field_0) = 1
              if caller == tx.origin:
                  call addr(mmultiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args addr(this.address), m_value, msymbol, 128, 0
              else:
                  call addr(mmultiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args caller, addr(this.address), m_value, msymbol, 160, 0
              if ext_call.success:
                  uint8(mstor3m.field_0) = 0
                  if not ext_call.return_data[0]:
                      return bool(ext_call.return_data[0])
                  if m_to == this.address:
                      call caller with:
                         value m_value wei
                           gas gas_remaining - 34050 wei
                  else:
                      call m_to with:
                         value m_value wei
                           gas gas_remaining - 34050 wei
                  if ext_call.success:
                      return bool(ext_call.return_data[0])
          else:
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  if uint8(mstor4m[addr(m_to)m]):
                      if m_to != caller:
                          if caller == tx.origin:
                              call addr(mmultiAssetAddress).0x64ef212e with:
                                   gas gas_remaining - 25050 wei
                                  args addr(m_to), m_value, msymbol, 128, 0
                          else:
                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                   gas gas_remaining - 25050 wei
                                  args caller, addr(m_to), m_value, msymbol, 160, 0
                          require ext_call.success
                          return bool(ext_call.return_data[0])
                  uint8(mstor3m.field_0) = 1
                  if caller == tx.origin:
                      call addr(mmultiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), m_value, msymbol, 128, 0
                  else:
                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), m_value, msymbol, 160, 0
                  if ext_call.success:
                      uint8(mstor3m.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      if m_to == this.address:
                          call caller with:
                             value m_value wei
                               gas gas_remaining - 34050 wei
                      else:
                          call m_to with:
                             value m_value wei
                               gas gas_remaining - 34050 wei
                      if ext_call.success:
                          return bool(ext_call.return_data[0])
      else:
          uint8(mstor3m.field_0) = 1
          call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
               gas gas_remaining - 25050 wei
              args addr(this.address), msymbol
          if ext_call.success:
              if ext_call.return_data[0] >= call.value:
                  uint8(mstor3m.field_0) = 0
                  uint8(mstor3m.field_8) = 1
                  mem[356] = mem[381 len 7]
                  call addr(mmultiAssetAddress).0x6e293817 with:
                       gas gas_remaining - 25050 wei
                      args caller, call.value, msymbol, Array(len=7, data=mem[356])
                  if ext_call.success:
                      uint8(mstor3m.field_8) = 0
                      if ext_call.return_data[0]:
                          if uint8(mstor4m[addr(m_to)m]):
                              if m_to != caller:
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(m_to), m_value, msymbol, 128, 0
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(m_to), m_value, msymbol, 160, 0
                                  require ext_call.success
                                  return bool(ext_call.return_data[0])
                          uint8(mstor3m.field_0) = 1
                          if caller == tx.origin:
                              call addr(mmultiAssetAddress).0x64ef212e with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), m_value, msymbol, 128, 0
                          else:
                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                   gas gas_remaining - 25050 wei
                                  args caller, addr(this.address), m_value, msymbol, 160, 0
                          if ext_call.success:
                              uint8(mstor3m.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return bool(ext_call.return_data[0])
                              if m_to == this.address:
                                  call caller with:
                                     value m_value wei
                                       gas gas_remaining - 34050 wei
                              else:
                                  call m_to with:
                                     value m_value wei
                                       gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return bool(ext_call.return_data[0])
                      else:
                          if call.value <= 0:
                              uint8(mstor3m.field_16) = 1
                              call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), msymbol
                              if ext_call.success:
                                  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args msymbol, ext_call.return_data[0]
                                  uint8(mstor3m.field_16) = 0
                                  if uint8(mstor4m[addr(m_to)m]):
                                      if m_to != caller:
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(m_to), m_value, msymbol, 128, 0
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(m_to), m_value, msymbol, 160, 0
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, 128, 0
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, 160, 0
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if m_to == this.address:
                                          call caller with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call m_to with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  uint8(mstor3m.field_16) = 1
                                  call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), msymbol
                                  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args msymbol, ext_call.return_data[0]
                                  uint8(mstor3m.field_16) = 0
                                  if uint8(mstor4m[addr(m_to)m]):
                                      if m_to != caller:
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(m_to), m_value, msymbol, 128, 0
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(m_to), m_value, msymbol, 160, 0
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, 128, 0
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, 160, 0
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if m_to == this.address:
                                          call caller with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call m_to with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
              else:
                  call addr(mmultiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
                       gas gas_remaining - 25050 wei
                      args msymbol, call.value
                  if ext_call.success:
                      uint8(mstor3m.field_0) = 0
                      if not ext_call.return_data[0]:
                          if call.value <= 0:
                              if uint8(mstor4m[addr(m_to)m]):
                                  if m_to != caller:
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0x64ef212e with:
                                               gas gas_remaining - 25050 wei
                                              args addr(m_to), m_value, msymbol, 128, 0
                                      else:
                                          call addr(mmultiAssetAddress).0x31c6c4cf with:
                                               gas gas_remaining - 25050 wei
                                              args caller, addr(m_to), m_value, msymbol, 160, 0
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                              uint8(mstor3m.field_0) = 1
                              if caller == tx.origin:
                                  call addr(mmultiAssetAddress).0x64ef212e with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), m_value, msymbol, 128, 0
                              else:
                                  call addr(mmultiAssetAddress).0x31c6c4cf with:
                                       gas gas_remaining - 25050 wei
                                      args caller, addr(this.address), m_value, msymbol, 160, 0
                              if ext_call.success:
                                  uint8(mstor3m.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return bool(ext_call.return_data[0])
                                  if m_to == this.address:
                                      call caller with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                  else:
                                      call m_to with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  if uint8(mstor4m[addr(m_to)m]):
                                      if m_to != caller:
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(m_to), m_value, msymbol, 128, 0
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(m_to), m_value, msymbol, 160, 0
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, 128, 0
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, 160, 0
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if m_to == this.address:
                                          call caller with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call m_to with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                      else:
                          uint8(mstor3m.field_8) = 1
                          mem[356] = mem[381 len 7]
                          call addr(mmultiAssetAddress).0x6e293817 with:
                               gas gas_remaining - 25050 wei
                              args caller, call.value, msymbol, Array(len=7, data=mem[356])
                          if ext_call.success:
                              uint8(mstor3m.field_8) = 0
                              if ext_call.return_data[0]:
                                  if uint8(mstor4m[addr(m_to)m]):
                                      if m_to != caller:
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(m_to), m_value, msymbol, 128, 0
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(m_to), m_value, msymbol, 160, 0
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, 128, 0
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, 160, 0
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if m_to == this.address:
                                          call caller with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call m_to with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                              else:
                                  if call.value <= 0:
                                      uint8(mstor3m.field_16) = 1
                                      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), msymbol
                                      if ext_call.success:
                                          call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args msymbol, ext_call.return_data[0]
                                          uint8(mstor3m.field_16) = 0
                                          if uint8(mstor4m[addr(m_to)m]):
                                              if m_to != caller:
                                                  if caller == tx.origin:
                                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                                           gas gas_remaining - 25050 wei
                                                          args addr(m_to), m_value, msymbol, 128, 0
                                                  else:
                                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                           gas gas_remaining - 25050 wei
                                                          args caller, addr(m_to), m_value, msymbol, 160, 0
                                                  require ext_call.success
                                                  return bool(ext_call.return_data[0])
                                          uint8(mstor3m.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), m_value, msymbol, 128, 0
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), m_value, msymbol, 160, 0
                                          if ext_call.success:
                                              uint8(mstor3m.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              if m_to == this.address:
                                                  call caller with:
                                                     value m_value wei
                                                       gas gas_remaining - 34050 wei
                                              else:
                                                  call m_to with:
                                                     value m_value wei
                                                       gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  return bool(ext_call.return_data[0])
                                  else:
                                      call caller with:
                                         value call.value wei
                                           gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          uint8(mstor3m.field_16) = 1
                                          call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), msymbol
                                          call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args msymbol, ext_call.return_data[0]
                                          uint8(mstor3m.field_16) = 0
                                          if uint8(mstor4m[addr(m_to)m]):
                                              if m_to != caller:
                                                  if caller == tx.origin:
                                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                                           gas gas_remaining - 25050 wei
                                                          args addr(m_to), m_value, msymbol, 128, 0
                                                  else:
                                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                           gas gas_remaining - 25050 wei
                                                          args caller, addr(m_to), m_value, msymbol, 160, 0
                                                  require ext_call.success
                                                  return bool(ext_call.return_data[0])
                                          uint8(mstor3m.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), m_value, msymbol, 128, 0
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), m_value, msymbol, 160, 0
                                          if ext_call.success:
                                              uint8(mstor3m.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              if m_to == this.address:
                                                  call caller with:
                                                     value m_value wei
                                                       gas gas_remaining - 34050 wei
                                              else:
                                                  call m_to with:
                                                     value m_value wei
                                                       gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  return bool(ext_call.return_data[0])
  revert 


# hash = 0xaa46f961
# getter = ['storage', 160, 0, 5]
# const = None
# payable = True
def unknownaa46f961() payable: 
  return addr(munknownaa46f961Address)


# hash = 0xac35caee
# getter = None
# const = None
# payable = True
def transferWithReference(address m_to, uint256 m_value, string m_reference) payable: 
  if 0 == call.value:
      if uint8(mstor4m[addr(m_to)m]):
          if m_to != caller:
              if caller == tx.origin:
                  call addr(mmultiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
              else:
                  call addr(mmultiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
              require ext_call.success
              return bool(ext_call.return_data[0])
      uint8(mstor3m.field_0) = 1
      if caller == tx.origin:
          call addr(mmultiAssetAddress).0x64ef212e with:
               gas gas_remaining - 25050 wei
              args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
      else:
          call addr(mmultiAssetAddress).0x31c6c4cf with:
               gas gas_remaining - 25050 wei
              args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
      if ext_call.success:
          uint8(mstor3m.field_0) = 0
          if not ext_call.return_data[0]:
              return bool(ext_call.return_data[0])
          if m_to == this.address:
              call caller with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
          else:
              call m_to with:
                 value m_value wei
                   gas gas_remaining - 34050 wei
          if ext_call.success:
              return bool(ext_call.return_data[0])
  else:
      if caller == this.address:
          if call.value <= 0:
              if uint8(mstor4m[addr(m_to)m]):
                  if m_to != caller:
                      if caller == tx.origin:
                          call addr(mmultiAssetAddress).0x64ef212e with:
                               gas gas_remaining - 25050 wei
                              args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                      else:
                          call addr(mmultiAssetAddress).0x31c6c4cf with:
                               gas gas_remaining - 25050 wei
                              args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                      require ext_call.success
                      return bool(ext_call.return_data[0])
              uint8(mstor3m.field_0) = 1
              if caller == tx.origin:
                  call addr(mmultiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
              else:
                  call addr(mmultiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
              if ext_call.success:
                  uint8(mstor3m.field_0) = 0
                  if not ext_call.return_data[0]:
                      return bool(ext_call.return_data[0])
                  if m_to == this.address:
                      call caller with:
                         value m_value wei
                           gas gas_remaining - 34050 wei
                  else:
                      call m_to with:
                         value m_value wei
                           gas gas_remaining - 34050 wei
                  if ext_call.success:
                      return bool(ext_call.return_data[0])
          else:
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  if uint8(mstor4m[addr(m_to)m]):
                      if m_to != caller:
                          if caller == tx.origin:
                              call addr(mmultiAssetAddress).0x64ef212e with:
                                   gas gas_remaining - 25050 wei
                                  args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                          else:
                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                   gas gas_remaining - 25050 wei
                                  args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                          require ext_call.success
                          return bool(ext_call.return_data[0])
                  uint8(mstor3m.field_0) = 1
                  if caller == tx.origin:
                      call addr(mmultiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                  else:
                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                  if ext_call.success:
                      uint8(mstor3m.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      if m_to == this.address:
                          call caller with:
                             value m_value wei
                               gas gas_remaining - 34050 wei
                      else:
                          call m_to with:
                             value m_value wei
                               gas gas_remaining - 34050 wei
                      if ext_call.success:
                          return bool(ext_call.return_data[0])
      else:
          uint8(mstor3m.field_0) = 1
          call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
               gas gas_remaining - 25050 wei
              args addr(this.address), msymbol
          if ext_call.success:
              if ext_call.return_data[0] >= call.value:
                  uint8(mstor3m.field_0) = 0
                  uint8(mstor3m.field_8) = 1
                  mem[ceil32(m_reference.length) + 356] = mem[ceil32(m_reference.length) + 381 len 7]
                  call addr(mmultiAssetAddress).0x6e293817 with:
                       gas gas_remaining - 25050 wei
                      args caller, call.value, msymbol, Array(len=7, data=mem[ceil32(m_reference.length) + 356])
                  if ext_call.success:
                      uint8(mstor3m.field_8) = 0
                      if ext_call.return_data[0]:
                          if uint8(mstor4m[addr(m_to)m]):
                              if m_to != caller:
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  require ext_call.success
                                  return bool(ext_call.return_data[0])
                          uint8(mstor3m.field_0) = 1
                          if caller == tx.origin:
                              call addr(mmultiAssetAddress).0x64ef212e with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                          else:
                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                   gas gas_remaining - 25050 wei
                                  args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                          if ext_call.success:
                              uint8(mstor3m.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return bool(ext_call.return_data[0])
                              if m_to == this.address:
                                  call caller with:
                                     value m_value wei
                                       gas gas_remaining - 34050 wei
                              else:
                                  call m_to with:
                                     value m_value wei
                                       gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return bool(ext_call.return_data[0])
                      else:
                          if call.value <= 0:
                              uint8(mstor3m.field_16) = 1
                              call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), msymbol
                              if ext_call.success:
                                  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args msymbol, ext_call.return_data[0]
                                  uint8(mstor3m.field_16) = 0
                                  if uint8(mstor4m[addr(m_to)m]):
                                      if m_to != caller:
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if m_to == this.address:
                                          call caller with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call m_to with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  uint8(mstor3m.field_16) = 1
                                  call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), msymbol
                                  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args msymbol, ext_call.return_data[0]
                                  uint8(mstor3m.field_16) = 0
                                  if uint8(mstor4m[addr(m_to)m]):
                                      if m_to != caller:
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if m_to == this.address:
                                          call caller with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call m_to with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
              else:
                  call addr(mmultiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
                       gas gas_remaining - 25050 wei
                      args msymbol, call.value
                  if ext_call.success:
                      uint8(mstor3m.field_0) = 0
                      if not ext_call.return_data[0]:
                          if call.value <= 0:
                              if uint8(mstor4m[addr(m_to)m]):
                                  if m_to != caller:
                                      if caller == tx.origin:
                                          call addr(mmultiAssetAddress).0x64ef212e with:
                                               gas gas_remaining - 25050 wei
                                              args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                      else:
                                          call addr(mmultiAssetAddress).0x31c6c4cf with:
                                               gas gas_remaining - 25050 wei
                                              args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                              uint8(mstor3m.field_0) = 1
                              if caller == tx.origin:
                                  call addr(mmultiAssetAddress).0x64ef212e with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                              else:
                                  call addr(mmultiAssetAddress).0x31c6c4cf with:
                                       gas gas_remaining - 25050 wei
                                      args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                              if ext_call.success:
                                  uint8(mstor3m.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return bool(ext_call.return_data[0])
                                  if m_to == this.address:
                                      call caller with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                  else:
                                      call m_to with:
                                         value m_value wei
                                           gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  if uint8(mstor4m[addr(m_to)m]):
                                      if m_to != caller:
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if m_to == this.address:
                                          call caller with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call m_to with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                      else:
                          uint8(mstor3m.field_8) = 1
                          mem[ceil32(m_reference.length) + 356] = mem[ceil32(m_reference.length) + 381 len 7]
                          call addr(mmultiAssetAddress).0x6e293817 with:
                               gas gas_remaining - 25050 wei
                              args caller, call.value, msymbol, Array(len=7, data=mem[ceil32(m_reference.length) + 356])
                          if ext_call.success:
                              uint8(mstor3m.field_8) = 0
                              if ext_call.return_data[0]:
                                  if uint8(mstor4m[addr(m_to)m]):
                                      if m_to != caller:
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(mstor3m.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  else:
                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                  if ext_call.success:
                                      uint8(mstor3m.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if m_to == this.address:
                                          call caller with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call m_to with:
                                             value m_value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                              else:
                                  if call.value <= 0:
                                      uint8(mstor3m.field_16) = 1
                                      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), msymbol
                                      if ext_call.success:
                                          call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args msymbol, ext_call.return_data[0]
                                          uint8(mstor3m.field_16) = 0
                                          if uint8(mstor4m[addr(m_to)m]):
                                              if m_to != caller:
                                                  if caller == tx.origin:
                                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                                           gas gas_remaining - 25050 wei
                                                          args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                                  else:
                                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                           gas gas_remaining - 25050 wei
                                                          args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                                  require ext_call.success
                                                  return bool(ext_call.return_data[0])
                                          uint8(mstor3m.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          if ext_call.success:
                                              uint8(mstor3m.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              if m_to == this.address:
                                                  call caller with:
                                                     value m_value wei
                                                       gas gas_remaining - 34050 wei
                                              else:
                                                  call m_to with:
                                                     value m_value wei
                                                       gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  return bool(ext_call.return_data[0])
                                  else:
                                      call caller with:
                                         value call.value wei
                                           gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          uint8(mstor3m.field_16) = 1
                                          call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), msymbol
                                          call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args msymbol, ext_call.return_data[0]
                                          uint8(mstor3m.field_16) = 0
                                          if uint8(mstor4m[addr(m_to)m]):
                                              if m_to != caller:
                                                  if caller == tx.origin:
                                                      call addr(mmultiAssetAddress).0x64ef212e with:
                                                           gas gas_remaining - 25050 wei
                                                          args addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                                  else:
                                                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                           gas gas_remaining - 25050 wei
                                                          args caller, addr(m_to), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                                  require ext_call.success
                                                  return bool(ext_call.return_data[0])
                                          uint8(mstor3m.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(mmultiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          else:
                                              call addr(mmultiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), m_value, msymbol, Array(len=m_reference.length, data=m_reference[allm])
                                          if ext_call.success:
                                              uint8(mstor3m.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              if m_to == this.address:
                                                  call caller with:
                                                     value m_value wei
                                                       gas gas_remaining - 34050 wei
                                              else:
                                                  call m_to with:
                                                     value m_value wei
                                                       gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  return bool(ext_call.return_data[0])
  revert 


# hash = 0xbe9b42d2
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 4]]]]
# const = None
# payable = True
def unknownbe9b42d2(addr m_param1) payable: 
  return bool(uint8(mstor4m[addr(m_param1)m]))


# hash = 0xdd62ed3e
# getter = None
# const = None
# payable = True
def allowance(address m_owner, address m_spender) payable: 
  call addr(mmultiAssetAddress).allowance(address from, address spender, bytes32 symbol) with:
       gas gas_remaining - 25050 wei
      args addr(m_owner), addr(m_spender), msymbol
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0xf2ee5968
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]]
# const = None
# payable = True
def unknownf2ee5968(uint256 m_param1) payable: 
  return bool(uint8(mstor4m[m_param1m]))


# hash = 0xf340fa01
# getter = None
# const = None
# payable = True
def deposit(address m_payee) payable: 
  if 0 == call.value:
      return 0
  if m_payee == this.address:
      if call.value <= 0:
          return 0
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
      return 0
  uint8(mstor3m.field_0) = 1
  call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
       gas gas_remaining - 25050 wei
      args addr(this.address), msymbol
  require ext_call.success
  if ext_call.return_data[0] >= call.value:
      uint8(mstor3m.field_0) = 0
  else:
      call addr(mmultiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
           gas gas_remaining - 25050 wei
          args msymbol, call.value
      require ext_call.success
      uint8(mstor3m.field_0) = 0
      if not ext_call.return_data[0]:
          if call.value <= 0:
              return 0
          call caller with:
             value call.value wei
               gas gas_remaining - 34050 wei
          require ext_call.success
          return 0
  uint8(mstor3m.field_8) = 1
  mem[324] = mem[349 len 7]
  call addr(mmultiAssetAddress).0x6e293817 with:
       gas gas_remaining - 25050 wei
      args 0, 0, call.value, msymbol, 128, 7, mem[324]
  require ext_call.success
  uint8(mstor3m.field_8) = 0
  if ext_call.return_data[0]:
      return 1
  if call.value <= 0:
      uint8(mstor3m.field_16) = 1
      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), msymbol
      require ext_call.success
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
      uint8(mstor3m.field_16) = 1
      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), msymbol
  call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
       gas gas_remaining - 25050 wei
      args msymbol, ext_call.return_data[0]
  uint8(mstor3m.field_16) = 0
  return bool(ext_call.return_data[0])


# hash = 0xf359671c
# getter = None
# const = None
# payable = True
def unknownf359671c(addr m_param1, uint256 m_param2, array m_param3) payable: 
  if call.value <= 0:
      if uint8(mstor4m[addr(m_param1)m]):
          if m_param1 != caller:
              if caller == tx.origin:
                  call addr(mmultiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args addr(m_param1), m_param2, msymbol, Array(len=m_param3.length, data=m_param3[allm])
              else:
                  call addr(mmultiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args caller, addr(m_param1), m_param2, msymbol, Array(len=m_param3.length, data=m_param3[allm])
              require ext_call.success
              return bool(ext_call.return_data[0])
      uint8(mstor3m.field_0) = 1
      if caller == tx.origin:
          call addr(mmultiAssetAddress).0x64ef212e with:
               gas gas_remaining - 25050 wei
              args addr(this.address), m_param2, msymbol, Array(len=m_param3.length, data=m_param3[allm])
      else:
          call addr(mmultiAssetAddress).0x31c6c4cf with:
               gas gas_remaining - 25050 wei
              args caller, addr(this.address), m_param2, msymbol, Array(len=m_param3.length, data=m_param3[allm])
      if ext_call.success:
          uint8(mstor3m.field_0) = 0
          if not ext_call.return_data[0]:
              return bool(ext_call.return_data[0])
          if m_param1 == this.address:
              call caller with:
                 value m_param2 wei
                   gas gas_remaining - 34050 wei
          else:
              call m_param1 with:
                 value m_param2 wei
                   gas gas_remaining - 34050 wei
          if ext_call.success:
              return bool(ext_call.return_data[0])
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      if ext_call.success:
          if uint8(mstor4m[addr(m_param1)m]):
              if m_param1 != caller:
                  if caller == tx.origin:
                      call addr(mmultiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(m_param1), m_param2, msymbol, Array(len=m_param3.length, data=m_param3[allm])
                  else:
                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(m_param1), m_param2, msymbol, Array(len=m_param3.length, data=m_param3[allm])
                  require ext_call.success
                  return bool(ext_call.return_data[0])
          uint8(mstor3m.field_0) = 1
          if caller == tx.origin:
              call addr(mmultiAssetAddress).0x64ef212e with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), m_param2, msymbol, Array(len=m_param3.length, data=m_param3[allm])
          else:
              call addr(mmultiAssetAddress).0x31c6c4cf with:
                   gas gas_remaining - 25050 wei
                  args caller, addr(this.address), m_param2, msymbol, Array(len=m_param3.length, data=m_param3[allm])
          if ext_call.success:
              uint8(mstor3m.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              if m_param1 == this.address:
                  call caller with:
                     value m_param2 wei
                       gas gas_remaining - 34050 wei
              else:
                  call m_param1 with:
                     value m_param2 wei
                       gas gas_remaining - 34050 wei
              if ext_call.success:
                  return bool(ext_call.return_data[0])
  revert 


# hash = 0xf3fef3a3
# getter = None
# const = None
# payable = True
def withdraw(address m_address, uint256 m_amount) payable: 
  if call.value <= 0:
      if uint8(mstor4m[addr(m_address)m]):
          if m_address != caller:
              if caller == tx.origin:
                  call addr(mmultiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args 0, 0, m_amount, msymbol, 128, 0, 0, None
              else:
                  call addr(mmultiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args 0, uint32(caller), addr(m_address), m_amount, msymbol, 160, 0, None
              require ext_call.success
              return bool(ext_call.return_data[0])
      uint8(mstor3m.field_0) = 1
      if caller == tx.origin:
          call addr(mmultiAssetAddress).0x64ef212e with:
               gas gas_remaining - 25050 wei
              args 0, 0, m_amount, msymbol, 128, 0, 0, None
      else:
          call addr(mmultiAssetAddress).0x31c6c4cf with:
               gas gas_remaining - 25050 wei
              args 0, uint32(caller), addr(this.address), m_amount, msymbol, 160, 0, None
      if ext_call.success:
          uint8(mstor3m.field_0) = 0
          if not ext_call.return_data[0]:
              return bool(ext_call.return_data[0])
          if m_address == this.address:
              call caller with:
                 value m_amount wei
                   gas gas_remaining - 34050 wei
          else:
              call m_address with:
                 value m_amount wei
                   gas gas_remaining - 34050 wei
          if ext_call.success:
              return bool(ext_call.return_data[0])
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      if ext_call.success:
          if uint8(mstor4m[addr(m_address)m]):
              if m_address != caller:
                  if caller == tx.origin:
                      call addr(mmultiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args 0, 0, m_amount, msymbol, 128, 0, 0, None
                  else:
                      call addr(mmultiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args 0, uint32(caller), addr(m_address), m_amount, msymbol, 160, 0, None
                  require ext_call.success
                  return bool(ext_call.return_data[0])
          uint8(mstor3m.field_0) = 1
          if caller == tx.origin:
              call addr(mmultiAssetAddress).0x64ef212e with:
                   gas gas_remaining - 25050 wei
                  args 0, 0, m_amount, msymbol, 128, 0, 0, None
          else:
              call addr(mmultiAssetAddress).0x31c6c4cf with:
                   gas gas_remaining - 25050 wei
                  args 0, uint32(caller), addr(this.address), m_amount, msymbol, 160, 0, None
          if ext_call.success:
              uint8(mstor3m.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              if m_address == this.address:
                  call caller with:
                     value m_amount wei
                       gas gas_remaining - 34050 wei
              else:
                  call m_address with:
                     value m_amount wei
                       gas gas_remaining - 34050 wei
              if ext_call.success:
                  return bool(ext_call.return_data[0])
  revert 


# hash = 0xf77b8d7a
# getter = None
# const = None
# payable = True
def unknownf77b8d7a(uint256 m_param1) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if addr(munknownaa46f961Address):
      return 0
  uint256(mstor5) = m_param1 or Mask(96, 160, uint256(mstor5))
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if call.value != 0:
      if caller == this.address:
          if call.value <= 0:
              stop
          call caller with:
             value call.value wei
               gas gas_remaining - 34050 wei
          require ext_call.success
          stop
      uint8(mstor3m.field_0) = 1
      call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), msymbol
      require ext_call.success
      if ext_call.return_data[0] >= call.value:
          uint8(mstor3m.field_0) = 0
      else:
          call addr(mmultiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args msymbol, call.value
          require ext_call.success
          uint8(mstor3m.field_0) = 0
          if not ext_call.return_data[0]:
              if call.value <= 0:
                  stop
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              require ext_call.success
              stop
      uint8(mstor3m.field_8) = 1
      mem[324] = mem[349 len 7]
      call addr(mmultiAssetAddress).0x6e293817 with:
           gas gas_remaining - 25050 wei
          args 0, uint32(caller), call.value, msymbol, 128, 7, mem[324]
      require ext_call.success
      uint8(mstor3m.field_8) = 0
      if not ext_call.return_data[0]:
          if call.value <= 0:
              uint8(mstor3m.field_16) = 1
              call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), msymbol
              require ext_call.success
          else:
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              require ext_call.success
              uint8(mstor3m.field_16) = 1
              call addr(mmultiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), msymbol
          call addr(mmultiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args msymbol, ext_call.return_data[0]
          uint8(mstor3m.field_16) = 0


