# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x43eA9D8aa1EDaa7699eb795d9fE8F427e5f31af4 
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
    stor1 # mask: a s
    # storage address 2
    name # mask: a s
    # storage address 3
    multiAssetAddress # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    symbol # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6
    # storage address 7
    unknownaa46f961Address # mask: a s
    # storage address 7
    stor7 # mask: a s
# hash = 0x029a8bf7
# getter = ['storage', 160, 0, 3]
# const = None
# payable = True
def multiAsset() payable: 
  return addr(multiAssetAddress)


# hash = 0x06fdde03
# getter = ['storage', 256, 0, 2]
# const = None
# payable = True
def name() payable: 
  return name


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = True
def approve(address _spender, uint256 _value) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if tx.origin != caller:
      return 0
  call addr(multiAssetAddress).0x4f09eba7 with:
       gas gas_remaining - 25050 wei
      args addr(_spender), _value, symbol
  require ext_call.success
  return bool(ext_call.return_data[0])


# hash = 0x12ab7242
# getter = None
# const = None
# payable = True
def setupStackDepthLib(address _stackDepthLib) payable: 
  if addr(stor0) != 0:
      return 0
  uint256(stor0) = _stackDepthLib or Mask(96, 160, uint256(stor0))
  return 1


# hash = 0x18160ddd
# getter = None
# const = None
# payable = True
def totalSupply() payable: 
  call addr(multiAssetAddress).totalSupply(bytes32 symbol) with:
       gas gas_remaining - 25050 wei
      args symbol
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x1a9237de
# getter = None
# const = None
# payable = True
def unknown1a9237de(uint256 _param1) payable: 
  call addr(multiAssetAddress).registryICAP() with:
       gas gas_remaining - 25050 wei
  require ext_call.success
  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
       gas gas_remaining - 25050 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
  return not bool(uint8(stor6[ext_call.return_data[12 len 20]]))


# hash = 0x21f8a721
# getter = None
# const = None
# payable = True
def getAddress(bytes32 _key) payable: 
  call addr(stor1).0x2ade6c36 with:
       gas gas_remaining - 25050 wei
      args _key
  require ext_call.success
  return ext_call.return_data[12 len 20]


# hash = 0x23385089
# getter = None
# const = None
# payable = True
def emitApprove(address _from, address _spender, uint256 _value) payable: 
  if caller == addr(multiAssetAddress):
      log Approve(
            address target=_value,
            address spender=_from,
            uint256 value=_spender)


# hash = 0x23b872dd
# getter = None
# const = None
# payable = True
def transferFrom(address _from, address _to, uint256 _value) payable: 
  if call.value <= 0:
      if tx.origin != caller:
          return 0
      if not uint8(stor6[addr(_to)]):
          call addr(multiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args 0, 0, addr(_to), _value, symbol, 160, 0, None
          require ext_call.success
          return bool(ext_call.return_data[0])
      uint8(stor5.field_0) = 1
      call addr(multiAssetAddress).0xf0cbe059 with:
           gas gas_remaining - 25050 wei
          args 0, 0, addr(this.address), _value, symbol, 160, 0, None
      if ext_call.success:
          uint8(stor5.field_0) = 0
          if not ext_call.return_data[0]:
              return 0
          if _to == this.address:
              call caller with:
                 value _value wei
                   gas gas_remaining - 34050 wei
          else:
              call _to with:
                 value _value wei
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
          if not uint8(stor6[addr(_to)]):
              call addr(multiAssetAddress).0xf0cbe059 with:
                   gas gas_remaining - 25050 wei
                  args 0, 0, addr(_to), _value, symbol, 160, 0, None
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(stor5.field_0) = 1
          call addr(multiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args 0, 0, addr(this.address), _value, symbol, 160, 0, None
          if ext_call.success:
              uint8(stor5.field_0) = 0
              if not ext_call.return_data[0]:
                  return 0
              if _to == this.address:
                  call caller with:
                     value _value wei
                       gas gas_remaining - 34050 wei
              else:
                  call _to with:
                     value _value wei
                       gas gas_remaining - 34050 wei
              if ext_call.success:
                  return 1
  revert 


# hash = 0x23de6651
# getter = None
# const = None
# payable = True
def emitTransfer(address _from, address _to, uint256 _value) payable: 
  if caller == addr(multiAssetAddress):
      log Transfer(
            address from=_value,
            address to=_from,
            uint256 value=_to)
  if _to == this.address:
      if uint8(stor5.field_0):
          stop
  else:
      if not uint8(stor6[addr(_to)]):
          stop
      if uint8(stor5.field_8):
          stop
  revert 


# hash = 0x2cc0b254
# getter = None
# const = None
# payable = True
def init(address _multiAsset, bytes32 _symbol) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if addr(multiAssetAddress):
      return 0
  call _multiAsset.issueAsset(bytes32 symbol, uint256 value, string name, string description, uint8 baseUnit, bool isReissuable) with:
       gas gas_remaining - 25050 wei
      args 0, uint32(_symbol), 0, 192, 256, 0, 1, 8, 'WeiToken', 16, '1-to-1 with wei.'
  require ext_call.success
  if not ext_call.return_data[0]:
      if not uint8(stor6[0]):
          uint256(stor3) = _multiAsset or Mask(96, 160, uint256(stor3))
          symbol = _symbol
          uint8(stor6[addr(this.address)]) = 1
          return 0
      else:
          return 0
  call _multiAsset.0x6489899 with:
       gas gas_remaining - 25050 wei
      args addr(this.address), 1, _symbol
  require ext_call.success
  require ext_call.return_data[0]
  call _multiAsset.0x30d30c89 with:
       gas gas_remaining - 25050 wei
      args addr(this.address), _symbol
  require ext_call.success
  require ext_call.return_data[0]
  call _multiAsset.0xf01b0220 with:
       gas gas_remaining - 25050 wei
      args 0, 1, _symbol
  require ext_call.success
  require ext_call.return_data[0]
  uint256(stor3) = _multiAsset or Mask(96, 160, uint256(stor3))
  symbol = _symbol
  return 1


# hash = 0x490c0e8f
# getter = None
# const = None
# payable = True
def unknown490c0e8f(addr _param1, array _param2) payable: 
  if 0 == call.value:
      return 0
  if _param1 == this.address:
      if call.value <= 0:
          return 0
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
      return 0
  uint8(stor5.field_0) = 1
  call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
       gas gas_remaining - 25050 wei
      args addr(this.address), symbol
  require ext_call.success
  if ext_call.return_data[0] >= call.value:
      uint8(stor5.field_0) = 0
  else:
      call addr(multiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
           gas gas_remaining - 25050 wei
          args symbol, call.value
      require ext_call.success
      uint8(stor5.field_0) = 0
      if not ext_call.return_data[0]:
          if call.value <= 0:
              return 0
          call caller with:
             value call.value wei
               gas gas_remaining - 34050 wei
          require ext_call.success
          return 0
  uint8(stor5.field_8) = 1
  call addr(multiAssetAddress).0x6e293817 with:
       gas gas_remaining - 25050 wei
      args addr(_param1), call.value, symbol, Array(len=_param2.length, data=_param2[all])
  require ext_call.success
  uint8(stor5.field_8) = 0
  if ext_call.return_data[0]:
      return 1
  if call.value <= 0:
      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), symbol
      require ext_call.success
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), symbol
  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
       gas gas_remaining - 25050 wei
      args symbol, ext_call.return_data[0]
  return bool(ext_call.return_data[0])


# hash = 0x6461fe39
# getter = None
# const = None
# payable = True
def transferFromWithReference(address _from, address _to, uint256 _value, string _reference) payable: 
  if call.value <= 0:
      if tx.origin != caller:
          return 0
      if not uint8(stor6[addr(_to)]):
          call addr(multiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args addr(_from), addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
          require ext_call.success
          return bool(ext_call.return_data[0])
      uint8(stor5.field_0) = 1
      call addr(multiAssetAddress).0xf0cbe059 with:
           gas gas_remaining - 25050 wei
          args addr(_from), addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
      if ext_call.success:
          uint8(stor5.field_0) = 0
          if not ext_call.return_data[0]:
              return 0
          if _to == this.address:
              call caller with:
                 value _value wei
                   gas gas_remaining - 34050 wei
          else:
              call _to with:
                 value _value wei
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
          if not uint8(stor6[addr(_to)]):
              call addr(multiAssetAddress).0xf0cbe059 with:
                   gas gas_remaining - 25050 wei
                  args addr(_from), addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(stor5.field_0) = 1
          call addr(multiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args addr(_from), addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
          if ext_call.success:
              uint8(stor5.field_0) = 0
              if not ext_call.return_data[0]:
                  return 0
              if _to == this.address:
                  call caller with:
                     value _value wei
                       gas gas_remaining - 34050 wei
              else:
                  call _to with:
                     value _value wei
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


# hash = 0x66325155
# getter = None
# const = None
# payable = True
def unknown66325155(uint256 _param1, uint256 _param2, array _param3) payable: 
  if call.value <= 0:
      call addr(multiAssetAddress).registryICAP() with:
           gas gas_remaining - 25050 wei
      if ext_call.success:
          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
               gas gas_remaining - 25050 wei
              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
          if not uint8(stor6[ext_call.return_data[12 len 20]]):
              if caller == tx.origin:
                  call addr(multiAssetAddress).0xc5487661 with:
                       gas gas_remaining - 25050 wei
                      args _param1, _param2, Array(len=_param3.length, data=_param3[all])
              else:
                  call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                       gas gas_remaining - 25050 wei
                      args caller, _param1, _param2, Array(len=_param3.length, data=_param3[all])
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(stor5.field_0) = 1
          if caller == tx.origin:
              call addr(multiAssetAddress).0x64ef212e with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), _param2, symbol, Array(len=_param3.length, data=_param3[all])
          else:
              call addr(multiAssetAddress).0x31c6c4cf with:
                   gas gas_remaining - 25050 wei
                  args caller, addr(this.address), _param2, symbol, Array(len=_param3.length, data=_param3[all])
          if ext_call.success:
              uint8(stor5.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              call addr(unknownaa46f961Address).0xd882aa0 with:
                 value _param2 wei
                   gas gas_remaining - 34050 wei
                  args _param1, Array(len=_param3.length, data=_param3[all])
              if ext_call.success:
                  if ext_call.return_data[0]:
                      return bool(ext_call.return_data[0])
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      if ext_call.success:
          call addr(multiAssetAddress).registryICAP() with:
               gas gas_remaining - 25050 wei
          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
               gas gas_remaining - 25050 wei
              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
          if not uint8(stor6[ext_call.return_data[12 len 20]]):
              if caller == tx.origin:
                  call addr(multiAssetAddress).0xc5487661 with:
                       gas gas_remaining - 25050 wei
                      args _param1, _param2, Array(len=_param3.length, data=_param3[all])
              else:
                  call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                       gas gas_remaining - 25050 wei
                      args caller, _param1, _param2, Array(len=_param3.length, data=_param3[all])
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(stor5.field_0) = 1
          if caller == tx.origin:
              call addr(multiAssetAddress).0x64ef212e with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), _param2, symbol, Array(len=_param3.length, data=_param3[all])
          else:
              call addr(multiAssetAddress).0x31c6c4cf with:
                   gas gas_remaining - 25050 wei
                  args caller, addr(this.address), _param2, symbol, Array(len=_param3.length, data=_param3[all])
          if ext_call.success:
              uint8(stor5.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              call addr(unknownaa46f961Address).0xd882aa0 with:
                 value _param2 wei
                   gas gas_remaining - 34050 wei
                  args _param1, Array(len=_param3.length, data=_param3[all])
              if ext_call.success:
                  if ext_call.return_data[0]:
                      return bool(ext_call.return_data[0])
  revert 


# hash = 0x70a08231
# getter = None
# const = None
# payable = True
def balanceOf(address _owner) payable: 
  call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
       gas gas_remaining - 25050 wei
      args addr(_owner), symbol
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x733480b7
# getter = None
# const = None
# payable = True
def transferToICAP(bytes32 _icap, uint256 _value) payable: 
  if 0 == call.value:
      call addr(multiAssetAddress).registryICAP() with:
           gas gas_remaining - 25050 wei
      if ext_call.success:
          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
               gas gas_remaining - 25050 wei
              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
          if not uint8(stor6[ext_call.return_data[12 len 20]]):
              if caller == tx.origin:
                  call addr(multiAssetAddress).0xc5487661 with:
                       gas gas_remaining - 25050 wei
                      args _icap, _value, 96, 0
              else:
                  call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                       gas gas_remaining - 25050 wei
                      args caller, _icap, _value, 128, 0
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(stor5.field_0) = 1
          if caller == tx.origin:
              call addr(multiAssetAddress).0x64ef212e with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), _value, symbol, 128, 0
          else:
              call addr(multiAssetAddress).0x31c6c4cf with:
                   gas gas_remaining - 25050 wei
                  args caller, addr(this.address), _value, symbol, 160, 0
          if ext_call.success:
              uint8(stor5.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              call addr(unknownaa46f961Address).0xd882aa0 with:
                 value _value wei
                   gas gas_remaining - 34050 wei
                  args _icap, 64, 0
              if ext_call.success:
                  if ext_call.return_data[0]:
                      return bool(ext_call.return_data[0])
  else:
      if caller == this.address:
          if call.value <= 0:
              call addr(multiAssetAddress).registryICAP() with:
                   gas gas_remaining - 25050 wei
              if ext_call.success:
                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                       gas gas_remaining - 25050 wei
                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                      if caller == tx.origin:
                          call addr(multiAssetAddress).0xc5487661 with:
                               gas gas_remaining - 25050 wei
                              args _icap, _value, 96, 0
                      else:
                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                               gas gas_remaining - 25050 wei
                              args caller, _icap, _value, 128, 0
                      require ext_call.success
                      return bool(ext_call.return_data[0])
                  uint8(stor5.field_0) = 1
                  if caller == tx.origin:
                      call addr(multiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), _value, symbol, 128, 0
                  else:
                      call addr(multiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), _value, symbol, 160, 0
                  if ext_call.success:
                      uint8(stor5.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      call addr(unknownaa46f961Address).0xd882aa0 with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                          args _icap, 64, 0
                      if ext_call.success:
                          if ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
          else:
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  call addr(multiAssetAddress).registryICAP() with:
                       gas gas_remaining - 25050 wei
                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                       gas gas_remaining - 25050 wei
                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                      if caller == tx.origin:
                          call addr(multiAssetAddress).0xc5487661 with:
                               gas gas_remaining - 25050 wei
                              args _icap, _value, 96, 0
                      else:
                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                               gas gas_remaining - 25050 wei
                              args caller, _icap, _value, 128, 0
                      require ext_call.success
                      return bool(ext_call.return_data[0])
                  uint8(stor5.field_0) = 1
                  if caller == tx.origin:
                      call addr(multiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), _value, symbol, 128, 0
                  else:
                      call addr(multiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), _value, symbol, 160, 0
                  if ext_call.success:
                      uint8(stor5.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      call addr(unknownaa46f961Address).0xd882aa0 with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                          args _icap, 64, 0
                      if ext_call.success:
                          if ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
      else:
          uint8(stor5.field_0) = 1
          call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
               gas gas_remaining - 25050 wei
              args addr(this.address), symbol
          if ext_call.success:
              if ext_call.return_data[0] >= call.value:
                  uint8(stor5.field_0) = 0
                  uint8(stor5.field_8) = 1
                  mem[356] = mem[381 len 7]
                  call addr(multiAssetAddress).0x6e293817 with:
                       gas gas_remaining - 25050 wei
                      args caller, call.value, symbol, Array(len=7, data=mem[356])
                  if ext_call.success:
                      uint8(stor5.field_8) = 0
                      if ext_call.return_data[0]:
                          call addr(multiAssetAddress).registryICAP() with:
                               gas gas_remaining - 25050 wei
                          if ext_call.success:
                              call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                   gas gas_remaining - 25050 wei
                                  args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                              if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0xc5487661 with:
                                           gas gas_remaining - 25050 wei
                                          args _icap, _value, 96, 0
                                  else:
                                      call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                           gas gas_remaining - 25050 wei
                                          args caller, _icap, _value, 128, 0
                                  require ext_call.success
                                  return bool(ext_call.return_data[0])
                              uint8(stor5.field_0) = 1
                              if caller == tx.origin:
                                  call addr(multiAssetAddress).0x64ef212e with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), _value, symbol, 128, 0
                              else:
                                  call addr(multiAssetAddress).0x31c6c4cf with:
                                       gas gas_remaining - 25050 wei
                                      args caller, addr(this.address), _value, symbol, 160, 0
                              if ext_call.success:
                                  uint8(stor5.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return bool(ext_call.return_data[0])
                                  call addr(unknownaa46f961Address).0xd882aa0 with:
                                     value _value wei
                                       gas gas_remaining - 34050 wei
                                      args _icap, 64, 0
                                  if ext_call.success:
                                      if ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                      else:
                          if call.value <= 0:
                              call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), symbol
                              if ext_call.success:
                                  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args symbol, ext_call.return_data[0]
                                  call addr(multiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args _icap, _value, 96, 0
                                      else:
                                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, _icap, _value, 128, 0
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, 128, 0
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, 160, 0
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(unknownaa46f961Address).0xd882aa0 with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                          args _icap, 64, 0
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), symbol
                                  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args symbol, ext_call.return_data[0]
                                  call addr(multiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args _icap, _value, 96, 0
                                      else:
                                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, _icap, _value, 128, 0
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, 128, 0
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, 160, 0
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(unknownaa46f961Address).0xd882aa0 with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                          args _icap, 64, 0
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
              else:
                  call addr(multiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
                       gas gas_remaining - 25050 wei
                      args symbol, call.value
                  if ext_call.success:
                      uint8(stor5.field_0) = 0
                      if not ext_call.return_data[0]:
                          if call.value <= 0:
                              call addr(multiAssetAddress).registryICAP() with:
                                   gas gas_remaining - 25050 wei
                              if ext_call.success:
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args _icap, _value, 96, 0
                                      else:
                                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, _icap, _value, 128, 0
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, 128, 0
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, 160, 0
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(unknownaa46f961Address).0xd882aa0 with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                          args _icap, 64, 0
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  call addr(multiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args _icap, _value, 96, 0
                                      else:
                                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, _icap, _value, 128, 0
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, 128, 0
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, 160, 0
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(unknownaa46f961Address).0xd882aa0 with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                          args _icap, 64, 0
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                      else:
                          uint8(stor5.field_8) = 1
                          mem[356] = mem[381 len 7]
                          call addr(multiAssetAddress).0x6e293817 with:
                               gas gas_remaining - 25050 wei
                              args caller, call.value, symbol, Array(len=7, data=mem[356])
                          if ext_call.success:
                              uint8(stor5.field_8) = 0
                              if ext_call.return_data[0]:
                                  call addr(multiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  if ext_call.success:
                                      call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                           gas gas_remaining - 25050 wei
                                          args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                      if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0xc5487661 with:
                                                   gas gas_remaining - 25050 wei
                                                  args _icap, _value, 96, 0
                                          else:
                                              call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, _icap, _value, 128, 0
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                      uint8(stor5.field_0) = 1
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0x64ef212e with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), _value, symbol, 128, 0
                                      else:
                                          call addr(multiAssetAddress).0x31c6c4cf with:
                                               gas gas_remaining - 25050 wei
                                              args caller, addr(this.address), _value, symbol, 160, 0
                                      if ext_call.success:
                                          uint8(stor5.field_0) = 0
                                          if not ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                                          call addr(unknownaa46f961Address).0xd882aa0 with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                              args _icap, 64, 0
                                          if ext_call.success:
                                              if ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                              else:
                                  if call.value <= 0:
                                      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), symbol
                                      if ext_call.success:
                                          call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args symbol, ext_call.return_data[0]
                                          call addr(multiAssetAddress).registryICAP() with:
                                               gas gas_remaining - 25050 wei
                                          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                               gas gas_remaining - 25050 wei
                                              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                          if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                              if caller == tx.origin:
                                                  call addr(multiAssetAddress).0xc5487661 with:
                                                       gas gas_remaining - 25050 wei
                                                      args _icap, _value, 96, 0
                                              else:
                                                  call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                       gas gas_remaining - 25050 wei
                                                      args caller, _icap, _value, 128, 0
                                              require ext_call.success
                                              return bool(ext_call.return_data[0])
                                          uint8(stor5.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), _value, symbol, 128, 0
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), _value, symbol, 160, 0
                                          if ext_call.success:
                                              uint8(stor5.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              call addr(unknownaa46f961Address).0xd882aa0 with:
                                                 value _value wei
                                                   gas gas_remaining - 34050 wei
                                                  args _icap, 64, 0
                                              if ext_call.success:
                                                  if ext_call.return_data[0]:
                                                      return bool(ext_call.return_data[0])
                                  else:
                                      call caller with:
                                         value call.value wei
                                           gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), symbol
                                          call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args symbol, ext_call.return_data[0]
                                          call addr(multiAssetAddress).registryICAP() with:
                                               gas gas_remaining - 25050 wei
                                          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                               gas gas_remaining - 25050 wei
                                              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                          if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                              if caller == tx.origin:
                                                  call addr(multiAssetAddress).0xc5487661 with:
                                                       gas gas_remaining - 25050 wei
                                                      args _icap, _value, 96, 0
                                              else:
                                                  call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                       gas gas_remaining - 25050 wei
                                                      args caller, _icap, _value, 128, 0
                                              require ext_call.success
                                              return bool(ext_call.return_data[0])
                                          uint8(stor5.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), _value, symbol, 128, 0
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), _value, symbol, 160, 0
                                          if ext_call.success:
                                              uint8(stor5.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              call addr(unknownaa46f961Address).0xd882aa0 with:
                                                 value _value wei
                                                   gas gas_remaining - 34050 wei
                                                  args _icap, 64, 0
                                              if ext_call.success:
                                                  if ext_call.return_data[0]:
                                                      return bool(ext_call.return_data[0])
  revert 


# hash = 0x77fe38a4
# getter = None
# const = None
# payable = True
def transferToICAPWithReference(bytes32 _icap, uint256 _value, string _reference) payable: 
  if 0 == call.value:
      call addr(multiAssetAddress).registryICAP() with:
           gas gas_remaining - 25050 wei
      if ext_call.success:
          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
               gas gas_remaining - 25050 wei
              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
          if not uint8(stor6[ext_call.return_data[12 len 20]]):
              if caller == tx.origin:
                  call addr(multiAssetAddress).0xc5487661 with:
                       gas gas_remaining - 25050 wei
                      args _icap, _value, Array(len=_reference.length, data=_reference[all])
              else:
                  call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                       gas gas_remaining - 25050 wei
                      args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(stor5.field_0) = 1
          if caller == tx.origin:
              call addr(multiAssetAddress).0x64ef212e with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
          else:
              call addr(multiAssetAddress).0x31c6c4cf with:
                   gas gas_remaining - 25050 wei
                  args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
          if ext_call.success:
              uint8(stor5.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              call addr(unknownaa46f961Address).0xd882aa0 with:
                 value _value wei
                   gas gas_remaining - 34050 wei
                  args _icap, Array(len=_reference.length, data=_reference[all])
              if ext_call.success:
                  if ext_call.return_data[0]:
                      return bool(ext_call.return_data[0])
  else:
      if caller == this.address:
          if call.value <= 0:
              call addr(multiAssetAddress).registryICAP() with:
                   gas gas_remaining - 25050 wei
              if ext_call.success:
                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                       gas gas_remaining - 25050 wei
                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                      if caller == tx.origin:
                          call addr(multiAssetAddress).0xc5487661 with:
                               gas gas_remaining - 25050 wei
                              args _icap, _value, Array(len=_reference.length, data=_reference[all])
                      else:
                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                               gas gas_remaining - 25050 wei
                              args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
                      require ext_call.success
                      return bool(ext_call.return_data[0])
                  uint8(stor5.field_0) = 1
                  if caller == tx.origin:
                      call addr(multiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                  else:
                      call addr(multiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                  if ext_call.success:
                      uint8(stor5.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      call addr(unknownaa46f961Address).0xd882aa0 with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                          args _icap, Array(len=_reference.length, data=_reference[all])
                      if ext_call.success:
                          if ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
          else:
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  call addr(multiAssetAddress).registryICAP() with:
                       gas gas_remaining - 25050 wei
                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                       gas gas_remaining - 25050 wei
                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                      if caller == tx.origin:
                          call addr(multiAssetAddress).0xc5487661 with:
                               gas gas_remaining - 25050 wei
                              args _icap, _value, Array(len=_reference.length, data=_reference[all])
                      else:
                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                               gas gas_remaining - 25050 wei
                              args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
                      require ext_call.success
                      return bool(ext_call.return_data[0])
                  uint8(stor5.field_0) = 1
                  if caller == tx.origin:
                      call addr(multiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                  else:
                      call addr(multiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                  if ext_call.success:
                      uint8(stor5.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      call addr(unknownaa46f961Address).0xd882aa0 with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                          args _icap, Array(len=_reference.length, data=_reference[all])
                      if ext_call.success:
                          if ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
      else:
          uint8(stor5.field_0) = 1
          call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
               gas gas_remaining - 25050 wei
              args addr(this.address), symbol
          if ext_call.success:
              if ext_call.return_data[0] >= call.value:
                  uint8(stor5.field_0) = 0
                  uint8(stor5.field_8) = 1
                  mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 381 len 7]
                  call addr(multiAssetAddress).0x6e293817 with:
                       gas gas_remaining - 25050 wei
                      args caller, call.value, symbol, Array(len=7, data=mem[ceil32(_reference.length) + 356])
                  if ext_call.success:
                      uint8(stor5.field_8) = 0
                      if ext_call.return_data[0]:
                          call addr(multiAssetAddress).registryICAP() with:
                               gas gas_remaining - 25050 wei
                          if ext_call.success:
                              call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                   gas gas_remaining - 25050 wei
                                  args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                              if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0xc5487661 with:
                                           gas gas_remaining - 25050 wei
                                          args _icap, _value, Array(len=_reference.length, data=_reference[all])
                                  else:
                                      call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                           gas gas_remaining - 25050 wei
                                          args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
                                  require ext_call.success
                                  return bool(ext_call.return_data[0])
                              uint8(stor5.field_0) = 1
                              if caller == tx.origin:
                                  call addr(multiAssetAddress).0x64ef212e with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                              else:
                                  call addr(multiAssetAddress).0x31c6c4cf with:
                                       gas gas_remaining - 25050 wei
                                      args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                              if ext_call.success:
                                  uint8(stor5.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return bool(ext_call.return_data[0])
                                  call addr(unknownaa46f961Address).0xd882aa0 with:
                                     value _value wei
                                       gas gas_remaining - 34050 wei
                                      args _icap, Array(len=_reference.length, data=_reference[all])
                                  if ext_call.success:
                                      if ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                      else:
                          if call.value <= 0:
                              call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), symbol
                              if ext_call.success:
                                  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args symbol, ext_call.return_data[0]
                                  call addr(multiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args _icap, _value, Array(len=_reference.length, data=_reference[all])
                                      else:
                                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(unknownaa46f961Address).0xd882aa0 with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                          args _icap, Array(len=_reference.length, data=_reference[all])
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), symbol
                                  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args symbol, ext_call.return_data[0]
                                  call addr(multiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args _icap, _value, Array(len=_reference.length, data=_reference[all])
                                      else:
                                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(unknownaa46f961Address).0xd882aa0 with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                          args _icap, Array(len=_reference.length, data=_reference[all])
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
              else:
                  call addr(multiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
                       gas gas_remaining - 25050 wei
                      args symbol, call.value
                  if ext_call.success:
                      uint8(stor5.field_0) = 0
                      if not ext_call.return_data[0]:
                          if call.value <= 0:
                              call addr(multiAssetAddress).registryICAP() with:
                                   gas gas_remaining - 25050 wei
                              if ext_call.success:
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args _icap, _value, Array(len=_reference.length, data=_reference[all])
                                      else:
                                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(unknownaa46f961Address).0xd882aa0 with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                          args _icap, Array(len=_reference.length, data=_reference[all])
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  call addr(multiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                       gas gas_remaining - 25050 wei
                                      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                  if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0xc5487661 with:
                                               gas gas_remaining - 25050 wei
                                              args _icap, _value, Array(len=_reference.length, data=_reference[all])
                                      else:
                                          call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                               gas gas_remaining - 25050 wei
                                              args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      call addr(unknownaa46f961Address).0xd882aa0 with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                          args _icap, Array(len=_reference.length, data=_reference[all])
                                      if ext_call.success:
                                          if ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                      else:
                          uint8(stor5.field_8) = 1
                          mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 381 len 7]
                          call addr(multiAssetAddress).0x6e293817 with:
                               gas gas_remaining - 25050 wei
                              args caller, call.value, symbol, Array(len=7, data=mem[ceil32(_reference.length) + 356])
                          if ext_call.success:
                              uint8(stor5.field_8) = 0
                              if ext_call.return_data[0]:
                                  call addr(multiAssetAddress).registryICAP() with:
                                       gas gas_remaining - 25050 wei
                                  if ext_call.success:
                                      call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                           gas gas_remaining - 25050 wei
                                          args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                      if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0xc5487661 with:
                                                   gas gas_remaining - 25050 wei
                                                  args _icap, _value, Array(len=_reference.length, data=_reference[all])
                                          else:
                                              call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                      uint8(stor5.field_0) = 1
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0x64ef212e with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                      else:
                                          call addr(multiAssetAddress).0x31c6c4cf with:
                                               gas gas_remaining - 25050 wei
                                              args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                      if ext_call.success:
                                          uint8(stor5.field_0) = 0
                                          if not ext_call.return_data[0]:
                                              return bool(ext_call.return_data[0])
                                          call addr(unknownaa46f961Address).0xd882aa0 with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                              args _icap, Array(len=_reference.length, data=_reference[all])
                                          if ext_call.success:
                                              if ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                              else:
                                  if call.value <= 0:
                                      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), symbol
                                      if ext_call.success:
                                          call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args symbol, ext_call.return_data[0]
                                          call addr(multiAssetAddress).registryICAP() with:
                                               gas gas_remaining - 25050 wei
                                          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                               gas gas_remaining - 25050 wei
                                              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                          if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                              if caller == tx.origin:
                                                  call addr(multiAssetAddress).0xc5487661 with:
                                                       gas gas_remaining - 25050 wei
                                                      args _icap, _value, Array(len=_reference.length, data=_reference[all])
                                              else:
                                                  call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                       gas gas_remaining - 25050 wei
                                                      args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
                                              require ext_call.success
                                              return bool(ext_call.return_data[0])
                                          uint8(stor5.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          if ext_call.success:
                                              uint8(stor5.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              call addr(unknownaa46f961Address).0xd882aa0 with:
                                                 value _value wei
                                                   gas gas_remaining - 34050 wei
                                                  args _icap, Array(len=_reference.length, data=_reference[all])
                                              if ext_call.success:
                                                  if ext_call.return_data[0]:
                                                      return bool(ext_call.return_data[0])
                                  else:
                                      call caller with:
                                         value call.value wei
                                           gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), symbol
                                          call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args symbol, ext_call.return_data[0]
                                          call addr(multiAssetAddress).registryICAP() with:
                                               gas gas_remaining - 25050 wei
                                          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                                               gas gas_remaining - 25050 wei
                                              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
                                          if not uint8(stor6[ext_call.return_data[12 len 20]]):
                                              if caller == tx.origin:
                                                  call addr(multiAssetAddress).0xc5487661 with:
                                                       gas gas_remaining - 25050 wei
                                                      args _icap, _value, Array(len=_reference.length, data=_reference[all])
                                              else:
                                                  call addr(multiAssetAddress).transferFromToICAPWithReference(address from, bytes32 icap, uint256 value, string reference) with:
                                                       gas gas_remaining - 25050 wei
                                                      args caller, _icap, _value, Array(len=_reference.length, data=_reference[all])
                                              require ext_call.success
                                              return bool(ext_call.return_data[0])
                                          uint8(stor5.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          if ext_call.success:
                                              uint8(stor5.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              call addr(unknownaa46f961Address).0xd882aa0 with:
                                                 value _value wei
                                                   gas gas_remaining - 34050 wei
                                                  args _icap, Array(len=_reference.length, data=_reference[all])
                                              if ext_call.success:
                                                  if ext_call.return_data[0]:
                                                      return bool(ext_call.return_data[0])
  revert 


# hash = 0x7948f523
# getter = None
# const = None
# payable = True
def setAmbiAddress(address _ambi, bytes32 _name) payable: 
  if addr(stor1) != 0:
      return 0
  call _ambi.0x2ade6c36 with:
       gas gas_remaining - 25050 wei
      args _name
  require ext_call.success
  if ext_call.return_data[12 len 20] != this.address:
      call _ambi.0x76849376 with:
           gas gas_remaining - 25050 wei
          args _name, this.address
      require ext_call.success
      if not ext_call.return_data[0]:
          return 0
  name = _name
  uint256(stor1) = _ambi or Mask(96, 160, uint256(stor1))
  return 1


# hash = 0x82fc49b8
# getter = None
# const = None
# payable = True
def setCosignerAddress(address _cosigner) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if tx.origin != caller:
      return 0
  call addr(multiAssetAddress).0xe82b7cb2 with:
       gas gas_remaining - 25050 wei
      args addr(_cosigner), symbol
  require ext_call.success
  return bool(ext_call.return_data[0])


# hash = 0x8bbbbfd3
# getter = None
# const = None
# payable = True
def unknown8bbbbfd3(uint256 _param1) payable: 
  uint256(stor6[caller]) = _param1 or Mask(248, 8, uint256(stor6[caller]))
  return 1


# hash = 0x95d89b41
# getter = ['storage', 256, 0, 4]
# const = None
# payable = True
def symbol() payable: 
  return symbol


# hash = 0xa340fff4
# getter = None
# const = None
# payable = True
def unknowna340fff4() payable: 
  if call.value <= 0:
      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), symbol
      require ext_call.success
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), symbol
  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
       gas gas_remaining - 25050 wei
      args symbol, ext_call.return_data[0]
  return bool(ext_call.return_data[0])


# hash = 0xa48a663c
# getter = None
# const = None
# payable = True
def transferFromToICAPWithReference(address _from, bytes32 _icap, uint256 _value, string _reference) payable: 
  if call.value <= 0:
      if tx.origin != caller:
          return 0
      call addr(multiAssetAddress).registryICAP() with:
           gas gas_remaining - 25050 wei
      if ext_call.success:
          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
               gas gas_remaining - 25050 wei
              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
          if not uint8(stor6[ext_call.return_data[12 len 20]]):
              call addr(multiAssetAddress).0xea98e540 with:
                   gas gas_remaining - 25050 wei
                  args addr(_from), _icap, _value, Array(len=_reference.length, data=_reference[all])
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(stor5.field_0) = 1
          call addr(multiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args addr(_from), addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
          if ext_call.success:
              uint8(stor5.field_0) = 0
              if not ext_call.return_data[0]:
                  return 0
              call addr(unknownaa46f961Address).0xd882aa0 with:
                 value _value wei
                   gas gas_remaining - 34050 wei
                  args _icap, Array(len=_reference.length, data=_reference[all])
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
          call addr(multiAssetAddress).registryICAP() with:
               gas gas_remaining - 25050 wei
          if ext_call.success:
              call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                   gas gas_remaining - 25050 wei
                  args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
              if not uint8(stor6[ext_call.return_data[12 len 20]]):
                  call addr(multiAssetAddress).0xea98e540 with:
                       gas gas_remaining - 25050 wei
                      args addr(_from), _icap, _value, Array(len=_reference.length, data=_reference[all])
                  require ext_call.success
                  return bool(ext_call.return_data[0])
              uint8(stor5.field_0) = 1
              call addr(multiAssetAddress).0xf0cbe059 with:
                   gas gas_remaining - 25050 wei
                  args addr(_from), addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
              if ext_call.success:
                  uint8(stor5.field_0) = 0
                  if not ext_call.return_data[0]:
                      return 0
                  call addr(unknownaa46f961Address).0xd882aa0 with:
                     value _value wei
                       gas gas_remaining - 34050 wei
                      args _icap, Array(len=_reference.length, data=_reference[all])
                  if ext_call.success:
                      if ext_call.return_data[0]:
                          return 1
  revert 


# hash = 0xa525f42c
# getter = None
# const = None
# payable = True
def transferFromToICAP(address _from, bytes32 _icap, uint256 _value) payable: 
  if call.value <= 0:
      if tx.origin != caller:
          return 0
      call addr(multiAssetAddress).registryICAP() with:
           gas gas_remaining - 25050 wei
      if ext_call.success:
          call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
               gas gas_remaining - 25050 wei
              args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
          if not uint8(stor6[ext_call.return_data[12 len 20]]):
              call addr(multiAssetAddress).0xea98e540 with:
                   gas gas_remaining - 25050 wei
                  args 0, 0, _icap, _value, 128, 0, 0, None
              require ext_call.success
              return bool(ext_call.return_data[0])
          uint8(stor5.field_0) = 1
          call addr(multiAssetAddress).0xf0cbe059 with:
               gas gas_remaining - 25050 wei
              args 0, 0, addr(this.address), _value, symbol, 160, 0, None
          if ext_call.success:
              uint8(stor5.field_0) = 0
              if not ext_call.return_data[0]:
                  return 0
              call addr(unknownaa46f961Address).0xd882aa0 with:
                 value _value wei
                   gas gas_remaining - 34050 wei
                  args _icap, 64, 0
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
          call addr(multiAssetAddress).registryICAP() with:
               gas gas_remaining - 25050 wei
          if ext_call.success:
              call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
                   gas gas_remaining - 25050 wei
                  args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
              if not uint8(stor6[ext_call.return_data[12 len 20]]):
                  call addr(multiAssetAddress).0xea98e540 with:
                       gas gas_remaining - 25050 wei
                      args 0, 0, _icap, _value, 128, 0, 0, None
                  require ext_call.success
                  return bool(ext_call.return_data[0])
              uint8(stor5.field_0) = 1
              call addr(multiAssetAddress).0xf0cbe059 with:
                   gas gas_remaining - 25050 wei
                  args 0, 0, addr(this.address), _value, symbol, 160, 0, None
              if ext_call.success:
                  uint8(stor5.field_0) = 0
                  if not ext_call.return_data[0]:
                      return 0
                  call addr(unknownaa46f961Address).0xd882aa0 with:
                     value _value wei
                       gas gas_remaining - 34050 wei
                      args _icap, 64, 0
                  if ext_call.success:
                      if ext_call.return_data[0]:
                          return 1
  revert 


# hash = 0xa7f43779
# getter = None
# const = None
# payable = True
def remove() payable: 
  if 0 == addr(stor1):
      stop
  call addr(stor1).0xa1add510 with:
       gas gas_remaining - 25050 wei
      args name, 'owner', caller
  require ext_call.success
  if not ext_call.return_data[0]:
      stop
  [93mselfdestruct([91mcaller[93m)


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = True
def transfer(address _to, uint256 _value) payable: 
  if 0 == call.value:
      if caller == _to:
          if eth.balance(this.address) < _value:
              return 0
      if not uint8(stor6[addr(_to)]):
          if _to != caller:
              if caller == tx.origin:
                  call addr(multiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args addr(_to), _value, symbol, 128, 0
              else:
                  call addr(multiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args caller, addr(_to), _value, symbol, 160, 0
              require ext_call.success
              return bool(ext_call.return_data[0])
      uint8(stor5.field_0) = 1
      if caller == tx.origin:
          call addr(multiAssetAddress).0x64ef212e with:
               gas gas_remaining - 25050 wei
              args addr(this.address), _value, symbol, 128, 0
      else:
          call addr(multiAssetAddress).0x31c6c4cf with:
               gas gas_remaining - 25050 wei
              args caller, addr(this.address), _value, symbol, 160, 0
      if ext_call.success:
          uint8(stor5.field_0) = 0
          if not ext_call.return_data[0]:
              return bool(ext_call.return_data[0])
          if _to == this.address:
              call caller with:
                 value _value wei
                   gas gas_remaining - 34050 wei
          else:
              call _to with:
                 value _value wei
                   gas gas_remaining - 34050 wei
          if ext_call.success:
              return bool(ext_call.return_data[0])
  else:
      if caller == this.address:
          if call.value <= 0:
              if caller == _to:
                  if eth.balance(this.address) < _value:
                      return 0
              if not uint8(stor6[addr(_to)]):
                  if _to != caller:
                      if caller == tx.origin:
                          call addr(multiAssetAddress).0x64ef212e with:
                               gas gas_remaining - 25050 wei
                              args addr(_to), _value, symbol, 128, 0
                      else:
                          call addr(multiAssetAddress).0x31c6c4cf with:
                               gas gas_remaining - 25050 wei
                              args caller, addr(_to), _value, symbol, 160, 0
                      require ext_call.success
                      return bool(ext_call.return_data[0])
              uint8(stor5.field_0) = 1
              if caller == tx.origin:
                  call addr(multiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args addr(this.address), _value, symbol, 128, 0
              else:
                  call addr(multiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args caller, addr(this.address), _value, symbol, 160, 0
              if ext_call.success:
                  uint8(stor5.field_0) = 0
                  if not ext_call.return_data[0]:
                      return bool(ext_call.return_data[0])
                  if _to == this.address:
                      call caller with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                  else:
                      call _to with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                  if ext_call.success:
                      return bool(ext_call.return_data[0])
          else:
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  if caller == _to:
                      if eth.balance(this.address) < _value:
                          return 0
                  if not uint8(stor6[addr(_to)]):
                      if _to != caller:
                          if caller == tx.origin:
                              call addr(multiAssetAddress).0x64ef212e with:
                                   gas gas_remaining - 25050 wei
                                  args addr(_to), _value, symbol, 128, 0
                          else:
                              call addr(multiAssetAddress).0x31c6c4cf with:
                                   gas gas_remaining - 25050 wei
                                  args caller, addr(_to), _value, symbol, 160, 0
                          require ext_call.success
                          return bool(ext_call.return_data[0])
                  uint8(stor5.field_0) = 1
                  if caller == tx.origin:
                      call addr(multiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), _value, symbol, 128, 0
                  else:
                      call addr(multiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), _value, symbol, 160, 0
                  if ext_call.success:
                      uint8(stor5.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      if _to == this.address:
                          call caller with:
                             value _value wei
                               gas gas_remaining - 34050 wei
                      else:
                          call _to with:
                             value _value wei
                               gas gas_remaining - 34050 wei
                      if ext_call.success:
                          return bool(ext_call.return_data[0])
      else:
          uint8(stor5.field_0) = 1
          call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
               gas gas_remaining - 25050 wei
              args addr(this.address), symbol
          if ext_call.success:
              if ext_call.return_data[0] >= call.value:
                  uint8(stor5.field_0) = 0
                  uint8(stor5.field_8) = 1
                  mem[356] = mem[381 len 7]
                  call addr(multiAssetAddress).0x6e293817 with:
                       gas gas_remaining - 25050 wei
                      args caller, call.value, symbol, Array(len=7, data=mem[356])
                  if ext_call.success:
                      uint8(stor5.field_8) = 0
                      if ext_call.return_data[0]:
                          if caller == _to:
                              if eth.balance(this.address) < _value:
                                  return 0
                          if not uint8(stor6[addr(_to)]):
                              if _to != caller:
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(_to), _value, symbol, 128, 0
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(_to), _value, symbol, 160, 0
                                  require ext_call.success
                                  return bool(ext_call.return_data[0])
                          uint8(stor5.field_0) = 1
                          if caller == tx.origin:
                              call addr(multiAssetAddress).0x64ef212e with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), _value, symbol, 128, 0
                          else:
                              call addr(multiAssetAddress).0x31c6c4cf with:
                                   gas gas_remaining - 25050 wei
                                  args caller, addr(this.address), _value, symbol, 160, 0
                          if ext_call.success:
                              uint8(stor5.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return bool(ext_call.return_data[0])
                              if _to == this.address:
                                  call caller with:
                                     value _value wei
                                       gas gas_remaining - 34050 wei
                              else:
                                  call _to with:
                                     value _value wei
                                       gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return bool(ext_call.return_data[0])
                      else:
                          if call.value <= 0:
                              call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), symbol
                              if ext_call.success:
                                  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args symbol, ext_call.return_data[0]
                                  if caller == _to:
                                      if eth.balance(this.address) < _value:
                                          return 0
                                  if not uint8(stor6[addr(_to)]):
                                      if _to != caller:
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(_to), _value, symbol, 128, 0
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(_to), _value, symbol, 160, 0
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, 128, 0
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, 160, 0
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if _to == this.address:
                                          call caller with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call _to with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), symbol
                                  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args symbol, ext_call.return_data[0]
                                  if caller == _to:
                                      if eth.balance(this.address) < _value:
                                          return 0
                                  if not uint8(stor6[addr(_to)]):
                                      if _to != caller:
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(_to), _value, symbol, 128, 0
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(_to), _value, symbol, 160, 0
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, 128, 0
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, 160, 0
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if _to == this.address:
                                          call caller with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call _to with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
              else:
                  call addr(multiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
                       gas gas_remaining - 25050 wei
                      args symbol, call.value
                  if ext_call.success:
                      uint8(stor5.field_0) = 0
                      if not ext_call.return_data[0]:
                          if call.value <= 0:
                              if caller == _to:
                                  if eth.balance(this.address) < _value:
                                      return 0
                              if not uint8(stor6[addr(_to)]):
                                  if _to != caller:
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0x64ef212e with:
                                               gas gas_remaining - 25050 wei
                                              args addr(_to), _value, symbol, 128, 0
                                      else:
                                          call addr(multiAssetAddress).0x31c6c4cf with:
                                               gas gas_remaining - 25050 wei
                                              args caller, addr(_to), _value, symbol, 160, 0
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                              uint8(stor5.field_0) = 1
                              if caller == tx.origin:
                                  call addr(multiAssetAddress).0x64ef212e with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), _value, symbol, 128, 0
                              else:
                                  call addr(multiAssetAddress).0x31c6c4cf with:
                                       gas gas_remaining - 25050 wei
                                      args caller, addr(this.address), _value, symbol, 160, 0
                              if ext_call.success:
                                  uint8(stor5.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return bool(ext_call.return_data[0])
                                  if _to == this.address:
                                      call caller with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                  else:
                                      call _to with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  if caller == _to:
                                      if eth.balance(this.address) < _value:
                                          return 0
                                  if not uint8(stor6[addr(_to)]):
                                      if _to != caller:
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(_to), _value, symbol, 128, 0
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(_to), _value, symbol, 160, 0
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, 128, 0
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, 160, 0
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if _to == this.address:
                                          call caller with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call _to with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                      else:
                          uint8(stor5.field_8) = 1
                          mem[356] = mem[381 len 7]
                          call addr(multiAssetAddress).0x6e293817 with:
                               gas gas_remaining - 25050 wei
                              args caller, call.value, symbol, Array(len=7, data=mem[356])
                          if ext_call.success:
                              uint8(stor5.field_8) = 0
                              if ext_call.return_data[0]:
                                  if caller == _to:
                                      if eth.balance(this.address) < _value:
                                          return 0
                                  if not uint8(stor6[addr(_to)]):
                                      if _to != caller:
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(_to), _value, symbol, 128, 0
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(_to), _value, symbol, 160, 0
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, 128, 0
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, 160, 0
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if _to == this.address:
                                          call caller with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call _to with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                              else:
                                  if call.value <= 0:
                                      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), symbol
                                      if ext_call.success:
                                          call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args symbol, ext_call.return_data[0]
                                          if caller == _to:
                                              if eth.balance(this.address) < _value:
                                                  return 0
                                          if not uint8(stor6[addr(_to)]):
                                              if _to != caller:
                                                  if caller == tx.origin:
                                                      call addr(multiAssetAddress).0x64ef212e with:
                                                           gas gas_remaining - 25050 wei
                                                          args addr(_to), _value, symbol, 128, 0
                                                  else:
                                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                                           gas gas_remaining - 25050 wei
                                                          args caller, addr(_to), _value, symbol, 160, 0
                                                  require ext_call.success
                                                  return bool(ext_call.return_data[0])
                                          uint8(stor5.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), _value, symbol, 128, 0
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), _value, symbol, 160, 0
                                          if ext_call.success:
                                              uint8(stor5.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              if _to == this.address:
                                                  call caller with:
                                                     value _value wei
                                                       gas gas_remaining - 34050 wei
                                              else:
                                                  call _to with:
                                                     value _value wei
                                                       gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  return bool(ext_call.return_data[0])
                                  else:
                                      call caller with:
                                         value call.value wei
                                           gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), symbol
                                          call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args symbol, ext_call.return_data[0]
                                          if caller == _to:
                                              if eth.balance(this.address) < _value:
                                                  return 0
                                          if not uint8(stor6[addr(_to)]):
                                              if _to != caller:
                                                  if caller == tx.origin:
                                                      call addr(multiAssetAddress).0x64ef212e with:
                                                           gas gas_remaining - 25050 wei
                                                          args addr(_to), _value, symbol, 128, 0
                                                  else:
                                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                                           gas gas_remaining - 25050 wei
                                                          args caller, addr(_to), _value, symbol, 160, 0
                                                  require ext_call.success
                                                  return bool(ext_call.return_data[0])
                                          uint8(stor5.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), _value, symbol, 128, 0
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), _value, symbol, 160, 0
                                          if ext_call.success:
                                              uint8(stor5.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              if _to == this.address:
                                                  call caller with:
                                                     value _value wei
                                                       gas gas_remaining - 34050 wei
                                              else:
                                                  call _to with:
                                                     value _value wei
                                                       gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  return bool(ext_call.return_data[0])
  revert 


# hash = 0xaa46f961
# getter = ['storage', 160, 0, 7]
# const = None
# payable = True
def unknownaa46f961() payable: 
  return addr(unknownaa46f961Address)


# hash = 0xac35caee
# getter = None
# const = None
# payable = True
def transferWithReference(address _to, uint256 _value, string _reference) payable: 
  if 0 == call.value:
      if caller == _to:
          if eth.balance(this.address) < _value:
              return 0
      if not uint8(stor6[addr(_to)]):
          if _to != caller:
              if caller == tx.origin:
                  call addr(multiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
              else:
                  call addr(multiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
              require ext_call.success
              return bool(ext_call.return_data[0])
      uint8(stor5.field_0) = 1
      if caller == tx.origin:
          call addr(multiAssetAddress).0x64ef212e with:
               gas gas_remaining - 25050 wei
              args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
      else:
          call addr(multiAssetAddress).0x31c6c4cf with:
               gas gas_remaining - 25050 wei
              args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
      if ext_call.success:
          uint8(stor5.field_0) = 0
          if not ext_call.return_data[0]:
              return bool(ext_call.return_data[0])
          if _to == this.address:
              call caller with:
                 value _value wei
                   gas gas_remaining - 34050 wei
          else:
              call _to with:
                 value _value wei
                   gas gas_remaining - 34050 wei
          if ext_call.success:
              return bool(ext_call.return_data[0])
  else:
      if caller == this.address:
          if call.value <= 0:
              if caller == _to:
                  if eth.balance(this.address) < _value:
                      return 0
              if not uint8(stor6[addr(_to)]):
                  if _to != caller:
                      if caller == tx.origin:
                          call addr(multiAssetAddress).0x64ef212e with:
                               gas gas_remaining - 25050 wei
                              args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                      else:
                          call addr(multiAssetAddress).0x31c6c4cf with:
                               gas gas_remaining - 25050 wei
                              args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                      require ext_call.success
                      return bool(ext_call.return_data[0])
              uint8(stor5.field_0) = 1
              if caller == tx.origin:
                  call addr(multiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
              else:
                  call addr(multiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
              if ext_call.success:
                  uint8(stor5.field_0) = 0
                  if not ext_call.return_data[0]:
                      return bool(ext_call.return_data[0])
                  if _to == this.address:
                      call caller with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                  else:
                      call _to with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                  if ext_call.success:
                      return bool(ext_call.return_data[0])
          else:
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  if caller == _to:
                      if eth.balance(this.address) < _value:
                          return 0
                  if not uint8(stor6[addr(_to)]):
                      if _to != caller:
                          if caller == tx.origin:
                              call addr(multiAssetAddress).0x64ef212e with:
                                   gas gas_remaining - 25050 wei
                                  args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                          else:
                              call addr(multiAssetAddress).0x31c6c4cf with:
                                   gas gas_remaining - 25050 wei
                                  args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                          require ext_call.success
                          return bool(ext_call.return_data[0])
                  uint8(stor5.field_0) = 1
                  if caller == tx.origin:
                      call addr(multiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                  else:
                      call addr(multiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                  if ext_call.success:
                      uint8(stor5.field_0) = 0
                      if not ext_call.return_data[0]:
                          return bool(ext_call.return_data[0])
                      if _to == this.address:
                          call caller with:
                             value _value wei
                               gas gas_remaining - 34050 wei
                      else:
                          call _to with:
                             value _value wei
                               gas gas_remaining - 34050 wei
                      if ext_call.success:
                          return bool(ext_call.return_data[0])
      else:
          uint8(stor5.field_0) = 1
          call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
               gas gas_remaining - 25050 wei
              args addr(this.address), symbol
          if ext_call.success:
              if ext_call.return_data[0] >= call.value:
                  uint8(stor5.field_0) = 0
                  uint8(stor5.field_8) = 1
                  mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 381 len 7]
                  call addr(multiAssetAddress).0x6e293817 with:
                       gas gas_remaining - 25050 wei
                      args caller, call.value, symbol, Array(len=7, data=mem[ceil32(_reference.length) + 356])
                  if ext_call.success:
                      uint8(stor5.field_8) = 0
                      if ext_call.return_data[0]:
                          if caller == _to:
                              if eth.balance(this.address) < _value:
                                  return 0
                          if not uint8(stor6[addr(_to)]):
                              if _to != caller:
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  require ext_call.success
                                  return bool(ext_call.return_data[0])
                          uint8(stor5.field_0) = 1
                          if caller == tx.origin:
                              call addr(multiAssetAddress).0x64ef212e with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                          else:
                              call addr(multiAssetAddress).0x31c6c4cf with:
                                   gas gas_remaining - 25050 wei
                                  args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                          if ext_call.success:
                              uint8(stor5.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return bool(ext_call.return_data[0])
                              if _to == this.address:
                                  call caller with:
                                     value _value wei
                                       gas gas_remaining - 34050 wei
                              else:
                                  call _to with:
                                     value _value wei
                                       gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return bool(ext_call.return_data[0])
                      else:
                          if call.value <= 0:
                              call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                   gas gas_remaining - 25050 wei
                                  args addr(this.address), symbol
                              if ext_call.success:
                                  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args symbol, ext_call.return_data[0]
                                  if caller == _to:
                                      if eth.balance(this.address) < _value:
                                          return 0
                                  if not uint8(stor6[addr(_to)]):
                                      if _to != caller:
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if _to == this.address:
                                          call caller with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call _to with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), symbol
                                  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                       gas gas_remaining - 25050 wei
                                      args symbol, ext_call.return_data[0]
                                  if caller == _to:
                                      if eth.balance(this.address) < _value:
                                          return 0
                                  if not uint8(stor6[addr(_to)]):
                                      if _to != caller:
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if _to == this.address:
                                          call caller with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call _to with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
              else:
                  call addr(multiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
                       gas gas_remaining - 25050 wei
                      args symbol, call.value
                  if ext_call.success:
                      uint8(stor5.field_0) = 0
                      if not ext_call.return_data[0]:
                          if call.value <= 0:
                              if caller == _to:
                                  if eth.balance(this.address) < _value:
                                      return 0
                              if not uint8(stor6[addr(_to)]):
                                  if _to != caller:
                                      if caller == tx.origin:
                                          call addr(multiAssetAddress).0x64ef212e with:
                                               gas gas_remaining - 25050 wei
                                              args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                      else:
                                          call addr(multiAssetAddress).0x31c6c4cf with:
                                               gas gas_remaining - 25050 wei
                                              args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                      require ext_call.success
                                      return bool(ext_call.return_data[0])
                              uint8(stor5.field_0) = 1
                              if caller == tx.origin:
                                  call addr(multiAssetAddress).0x64ef212e with:
                                       gas gas_remaining - 25050 wei
                                      args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                              else:
                                  call addr(multiAssetAddress).0x31c6c4cf with:
                                       gas gas_remaining - 25050 wei
                                      args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                              if ext_call.success:
                                  uint8(stor5.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return bool(ext_call.return_data[0])
                                  if _to == this.address:
                                      call caller with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                  else:
                                      call _to with:
                                         value _value wei
                                           gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      return bool(ext_call.return_data[0])
                          else:
                              call caller with:
                                 value call.value wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  if caller == _to:
                                      if eth.balance(this.address) < _value:
                                          return 0
                                  if not uint8(stor6[addr(_to)]):
                                      if _to != caller:
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if _to == this.address:
                                          call caller with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call _to with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                      else:
                          uint8(stor5.field_8) = 1
                          mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 381 len 7]
                          call addr(multiAssetAddress).0x6e293817 with:
                               gas gas_remaining - 25050 wei
                              args caller, call.value, symbol, Array(len=7, data=mem[ceil32(_reference.length) + 356])
                          if ext_call.success:
                              uint8(stor5.field_8) = 0
                              if ext_call.return_data[0]:
                                  if caller == _to:
                                      if eth.balance(this.address) < _value:
                                          return 0
                                  if not uint8(stor6[addr(_to)]):
                                      if _to != caller:
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(stor5.field_0) = 1
                                  if caller == tx.origin:
                                      call addr(multiAssetAddress).0x64ef212e with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  else:
                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                           gas gas_remaining - 25050 wei
                                          args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                  if ext_call.success:
                                      uint8(stor5.field_0) = 0
                                      if not ext_call.return_data[0]:
                                          return bool(ext_call.return_data[0])
                                      if _to == this.address:
                                          call caller with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      else:
                                          call _to with:
                                             value _value wei
                                               gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          return bool(ext_call.return_data[0])
                              else:
                                  if call.value <= 0:
                                      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                           gas gas_remaining - 25050 wei
                                          args addr(this.address), symbol
                                      if ext_call.success:
                                          call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args symbol, ext_call.return_data[0]
                                          if caller == _to:
                                              if eth.balance(this.address) < _value:
                                                  return 0
                                          if not uint8(stor6[addr(_to)]):
                                              if _to != caller:
                                                  if caller == tx.origin:
                                                      call addr(multiAssetAddress).0x64ef212e with:
                                                           gas gas_remaining - 25050 wei
                                                          args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                                  else:
                                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                                           gas gas_remaining - 25050 wei
                                                          args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                                  require ext_call.success
                                                  return bool(ext_call.return_data[0])
                                          uint8(stor5.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          if ext_call.success:
                                              uint8(stor5.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              if _to == this.address:
                                                  call caller with:
                                                     value _value wei
                                                       gas gas_remaining - 34050 wei
                                              else:
                                                  call _to with:
                                                     value _value wei
                                                       gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  return bool(ext_call.return_data[0])
                                  else:
                                      call caller with:
                                         value call.value wei
                                           gas gas_remaining - 34050 wei
                                      if ext_call.success:
                                          call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                                               gas gas_remaining - 25050 wei
                                              args addr(this.address), symbol
                                          call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
                                               gas gas_remaining - 25050 wei
                                              args symbol, ext_call.return_data[0]
                                          if caller == _to:
                                              if eth.balance(this.address) < _value:
                                                  return 0
                                          if not uint8(stor6[addr(_to)]):
                                              if _to != caller:
                                                  if caller == tx.origin:
                                                      call addr(multiAssetAddress).0x64ef212e with:
                                                           gas gas_remaining - 25050 wei
                                                          args addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                                  else:
                                                      call addr(multiAssetAddress).0x31c6c4cf with:
                                                           gas gas_remaining - 25050 wei
                                                          args caller, addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                                  require ext_call.success
                                                  return bool(ext_call.return_data[0])
                                          uint8(stor5.field_0) = 1
                                          if caller == tx.origin:
                                              call addr(multiAssetAddress).0x64ef212e with:
                                                   gas gas_remaining - 25050 wei
                                                  args addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          else:
                                              call addr(multiAssetAddress).0x31c6c4cf with:
                                                   gas gas_remaining - 25050 wei
                                                  args caller, addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
                                          if ext_call.success:
                                              uint8(stor5.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              if _to == this.address:
                                                  call caller with:
                                                     value _value wei
                                                       gas gas_remaining - 34050 wei
                                              else:
                                                  call _to with:
                                                     value _value wei
                                                       gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  return bool(ext_call.return_data[0])
  revert 


# hash = 0xbe9b42d2
# getter = None
# const = None
# payable = True
def unknownbe9b42d2(addr _param1) payable: 
  return not bool(uint8(stor6[addr(_param1)]))


# hash = 0xdd62ed3e
# getter = None
# const = None
# payable = True
def allowance(address _owner, address _spender) payable: 
  call addr(multiAssetAddress).allowance(address from, address spender, bytes32 symbol) with:
       gas gas_remaining - 25050 wei
      args addr(_owner), addr(_spender), symbol
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0xf2ee5968
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 6]]]]
# const = None
# payable = True
def unknownf2ee5968(uint256 _param1) payable: 
  return bool(uint8(stor6[_param1]))


# hash = 0xf340fa01
# getter = None
# const = None
# payable = True
def deposit(address _payee) payable: 
  if 0 == call.value:
      return 0
  if _payee == this.address:
      if call.value <= 0:
          return 0
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
      return 0
  uint8(stor5.field_0) = 1
  call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
       gas gas_remaining - 25050 wei
      args addr(this.address), symbol
  require ext_call.success
  if ext_call.return_data[0] >= call.value:
      uint8(stor5.field_0) = 0
  else:
      call addr(multiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
           gas gas_remaining - 25050 wei
          args symbol, call.value
      require ext_call.success
      uint8(stor5.field_0) = 0
      if not ext_call.return_data[0]:
          if call.value <= 0:
              return 0
          call caller with:
             value call.value wei
               gas gas_remaining - 34050 wei
          require ext_call.success
          return 0
  uint8(stor5.field_8) = 1
  mem[324] = mem[349 len 7]
  call addr(multiAssetAddress).0x6e293817 with:
       gas gas_remaining - 25050 wei
      args 0, 0, call.value, symbol, 128, 7, mem[324]
  require ext_call.success
  uint8(stor5.field_8) = 0
  if ext_call.return_data[0]:
      return 1
  if call.value <= 0:
      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), symbol
      require ext_call.success
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), symbol
  call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
       gas gas_remaining - 25050 wei
      args symbol, ext_call.return_data[0]
  return bool(ext_call.return_data[0])


# hash = 0xf359671c
# getter = None
# const = None
# payable = True
def unknownf359671c(addr _param1, uint256 _param2, array _param3) payable: 
  if call.value <= 0:
      if not uint8(stor6[addr(_param1)]):
          if _param1 != caller:
              if caller == tx.origin:
                  call addr(multiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args addr(_param1), _param2, symbol, Array(len=_param3.length, data=_param3[all])
              else:
                  call addr(multiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args caller, addr(_param1), _param2, symbol, Array(len=_param3.length, data=_param3[all])
              require ext_call.success
              return bool(ext_call.return_data[0])
      uint8(stor5.field_0) = 1
      if caller == tx.origin:
          call addr(multiAssetAddress).0x64ef212e with:
               gas gas_remaining - 25050 wei
              args addr(this.address), _param2, symbol, Array(len=_param3.length, data=_param3[all])
      else:
          call addr(multiAssetAddress).0x31c6c4cf with:
               gas gas_remaining - 25050 wei
              args caller, addr(this.address), _param2, symbol, Array(len=_param3.length, data=_param3[all])
      if ext_call.success:
          uint8(stor5.field_0) = 0
          if not ext_call.return_data[0]:
              return bool(ext_call.return_data[0])
          if _param1 == this.address:
              call caller with:
                 value _param2 wei
                   gas gas_remaining - 34050 wei
          else:
              call _param1 with:
                 value _param2 wei
                   gas gas_remaining - 34050 wei
          if ext_call.success:
              return bool(ext_call.return_data[0])
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      if ext_call.success:
          if not uint8(stor6[addr(_param1)]):
              if _param1 != caller:
                  if caller == tx.origin:
                      call addr(multiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args addr(_param1), _param2, symbol, Array(len=_param3.length, data=_param3[all])
                  else:
                      call addr(multiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args caller, addr(_param1), _param2, symbol, Array(len=_param3.length, data=_param3[all])
                  require ext_call.success
                  return bool(ext_call.return_data[0])
          uint8(stor5.field_0) = 1
          if caller == tx.origin:
              call addr(multiAssetAddress).0x64ef212e with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), _param2, symbol, Array(len=_param3.length, data=_param3[all])
          else:
              call addr(multiAssetAddress).0x31c6c4cf with:
                   gas gas_remaining - 25050 wei
                  args caller, addr(this.address), _param2, symbol, Array(len=_param3.length, data=_param3[all])
          if ext_call.success:
              uint8(stor5.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              if _param1 == this.address:
                  call caller with:
                     value _param2 wei
                       gas gas_remaining - 34050 wei
              else:
                  call _param1 with:
                     value _param2 wei
                       gas gas_remaining - 34050 wei
              if ext_call.success:
                  return bool(ext_call.return_data[0])
  revert 


# hash = 0xf3fef3a3
# getter = None
# const = None
# payable = True
def withdraw(address _address, uint256 _amount) payable: 
  if call.value <= 0:
      if not uint8(stor6[addr(_address)]):
          if _address != caller:
              if caller == tx.origin:
                  call addr(multiAssetAddress).0x64ef212e with:
                       gas gas_remaining - 25050 wei
                      args 0, 0, _amount, symbol, 128, 0, 0, None
              else:
                  call addr(multiAssetAddress).0x31c6c4cf with:
                       gas gas_remaining - 25050 wei
                      args 0, uint32(caller), addr(_address), _amount, symbol, 160, 0, None
              require ext_call.success
              return bool(ext_call.return_data[0])
      uint8(stor5.field_0) = 1
      if caller == tx.origin:
          call addr(multiAssetAddress).0x64ef212e with:
               gas gas_remaining - 25050 wei
              args 0, 0, _amount, symbol, 128, 0, 0, None
      else:
          call addr(multiAssetAddress).0x31c6c4cf with:
               gas gas_remaining - 25050 wei
              args 0, uint32(caller), addr(this.address), _amount, symbol, 160, 0, None
      if ext_call.success:
          uint8(stor5.field_0) = 0
          if not ext_call.return_data[0]:
              return bool(ext_call.return_data[0])
          if _address == this.address:
              call caller with:
                 value _amount wei
                   gas gas_remaining - 34050 wei
          else:
              call _address with:
                 value _amount wei
                   gas gas_remaining - 34050 wei
          if ext_call.success:
              return bool(ext_call.return_data[0])
  else:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      if ext_call.success:
          if not uint8(stor6[addr(_address)]):
              if _address != caller:
                  if caller == tx.origin:
                      call addr(multiAssetAddress).0x64ef212e with:
                           gas gas_remaining - 25050 wei
                          args 0, 0, _amount, symbol, 128, 0, 0, None
                  else:
                      call addr(multiAssetAddress).0x31c6c4cf with:
                           gas gas_remaining - 25050 wei
                          args 0, uint32(caller), addr(_address), _amount, symbol, 160, 0, None
                  require ext_call.success
                  return bool(ext_call.return_data[0])
          uint8(stor5.field_0) = 1
          if caller == tx.origin:
              call addr(multiAssetAddress).0x64ef212e with:
                   gas gas_remaining - 25050 wei
                  args 0, 0, _amount, symbol, 128, 0, 0, None
          else:
              call addr(multiAssetAddress).0x31c6c4cf with:
                   gas gas_remaining - 25050 wei
                  args 0, uint32(caller), addr(this.address), _amount, symbol, 160, 0, None
          if ext_call.success:
              uint8(stor5.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              if _address == this.address:
                  call caller with:
                     value _amount wei
                       gas gas_remaining - 34050 wei
              else:
                  call _address with:
                     value _amount wei
                       gas gas_remaining - 34050 wei
              if ext_call.success:
                  return bool(ext_call.return_data[0])
  revert 


# hash = 0xf77b8d7a
# getter = None
# const = None
# payable = True
def unknownf77b8d7a(uint256 _param1) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if addr(unknownaa46f961Address):
      return 0
  uint256(stor7) = _param1 or Mask(96, 160, uint256(stor7))
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
      uint8(stor5.field_0) = 1
      call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(this.address), symbol
      require ext_call.success
      if ext_call.return_data[0] >= call.value:
          uint8(stor5.field_0) = 0
      else:
          call addr(multiAssetAddress).reissueAsset(bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args symbol, call.value
          require ext_call.success
          uint8(stor5.field_0) = 0
          if not ext_call.return_data[0]:
              if call.value <= 0:
                  stop
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              require ext_call.success
              stop
      uint8(stor5.field_8) = 1
      mem[324] = mem[349 len 7]
      call addr(multiAssetAddress).0x6e293817 with:
           gas gas_remaining - 25050 wei
          args 0, uint32(caller), call.value, symbol, 128, 7, mem[324]
      require ext_call.success
      uint8(stor5.field_8) = 0
      if not ext_call.return_data[0]:
          if call.value <= 0:
              call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), symbol
              require ext_call.success
          else:
              call caller with:
                 value call.value wei
                   gas gas_remaining - 34050 wei
              require ext_call.success
              call addr(multiAssetAddress).balanceOf(address holder, bytes32 symbol) with:
                   gas gas_remaining - 25050 wei
                  args addr(this.address), symbol
          call addr(multiAssetAddress).revokeAsset(bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args symbol, ext_call.return_data[0]


