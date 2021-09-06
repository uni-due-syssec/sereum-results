# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xb465B9eC037A06dD52E743ed54fc5447583F7B70 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x733480b7': 'transferToICAP(bytes32 _icap, uint256 _value)', '0x77fe38a4': 'transferToICAPWithReference(bytes32 _icap, uint256 _value, string _reference)', '0xa9059cbb': 'transfer(address _to, uint256 _value)', '0xac35caee': 'transferWithReference(address _to, uint256 _value, string _reference)'} 

# storage definitions
def storage:
    # storage address 0
    multiAssetAddress # mask: a s
    # storage address 1
    symbol # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3
    # storage address 4
    stor4
    # storage address 5
    unknownaa46f961Address # mask: a s
# hash = 0x029a8bf7
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def multiAsset(): # not payable
  return multiAssetAddress


# hash = 0x06fdde03
# getter = None
# const = ['return', ['data', ['arr', 9, ['mem', ['range', 224, 32]]]]]
# payable = False
const name = Array(len=9, data=mem[224])


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address _spender, uint256 _value): # not payable
  if tx.origin != caller:
      return 0
  require ext_code.size(multiAssetAddress)
  call multiAssetAddress.0x4f09eba7 with:
       gas gas_remaining - 50 wei
      args addr(_spender), _value, symbol
  require ext_call.success
  if stor4[caller]:
      return bool(ext_call.return_data[0])
  if tx.origin != caller:
      return bool(ext_call.return_data[0])
  if eth.balance(caller) >= 10^16:
      return bool(ext_call.return_data[0])
  if stor3[caller]:
      if caller != caller:
          if caller == tx.origin:
              mem[324] = mem[351 len 5]
              require ext_code.size(multiAssetAddress)
              call multiAssetAddress.0x64ef212e with:
                   gas gas_remaining - 50 wei
                  args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
          else:
              mem[356] = mem[383 len 5]
              require ext_code.size(multiAssetAddress)
              call multiAssetAddress.0x31c6c4cf with:
                   gas gas_remaining - 50 wei
                  args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
          require ext_call.success
          return bool(ext_call.return_data[0])
  uint8(stor2.field_0) = 1
  if caller == tx.origin:
      mem[324] = mem[351 len 5]
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0x64ef212e with:
               gas gas_remaining - 50 wei
              args 0, 0, 10^17, symbol, 128, 5, mem[324]
          if ext_call.success:
              uint8(stor2.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              call caller with:
                 value 10^17 wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  return bool(ext_call.return_data[0])
  else:
      mem[356] = mem[383 len 5]
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0x31c6c4cf with:
               gas gas_remaining - 50 wei
              args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
          if ext_call.success:
              uint8(stor2.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              call caller with:
                 value 10^17 wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  return bool(ext_call.return_data[0])
  revert 


# hash = 0x18160ddd
# getter = None
# const = None
# payable = False
def totalSupply(): # not payable
  require ext_code.size(multiAssetAddress)
  call multiAssetAddress.totalSupply(bytes32 symbol) with:
       gas gas_remaining - 50 wei
      args symbol
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x1a9237de
# getter = None
# const = None
# payable = False
def unknown1a9237de(uint256 _param1): # not payable
  require ext_code.size(multiAssetAddress)
  call multiAssetAddress.registryICAP() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
       gas gas_remaining - 50 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
  require ext_call.success
  return bool(stor3[ext_call.return_data[12 len 20]])


# hash = 0x23385089
# getter = None
# const = None
# payable = False
def emitApprove(address _from, address _spender, uint256 _value): # not payable
  if multiAssetAddress == caller:
      log Approve(
            address target=_value,
            address spender=_from,
            uint256 value=_spender)


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address _from, address _to, uint256 _value): # not payable
  if tx.origin != caller:
      return 0
  if stor3[addr(_to)]:
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0xf0cbe059 with:
               gas gas_remaining - 50 wei
              args 0, 0, 0, _value, symbol, 160, 0, 0, None
          if ext_call.success:
              if stor4[caller]:
                  return bool(ext_call.return_data[0])
              if tx.origin != caller:
                  return bool(ext_call.return_data[0])
              if eth.balance(caller) >= 10^16:
                  return bool(ext_call.return_data[0])
              if stor3[caller]:
                  if caller != caller:
                      if caller == tx.origin:
                          mem[356] = mem[383 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x64ef212e with:
                               gas gas_remaining - 50 wei
                              args caller, 10^17, symbol, 128, 0, 5, mem[356]
                      else:
                          mem[388] = mem[415 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x31c6c4cf with:
                               gas gas_remaining - 50 wei
                              args 0, uint32(caller), caller, 10^17, symbol, 0, 160, 5, mem[388]
                      require ext_call.success
                      return bool(ext_call.return_data[0])
              uint8(stor2.field_0) = 1
              if caller == tx.origin:
                  mem[356] = mem[383 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x64ef212e with:
                           gas gas_remaining - 50 wei
                          args addr(this.address), 10^17, symbol, 128, 0, 5, mem[356]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              return bool(ext_call.return_data[0])
              else:
                  mem[388] = mem[415 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x31c6c4cf with:
                           gas gas_remaining - 50 wei
                          args 0, uint32(caller), addr(this.address), 10^17, symbol, 0, 160, 5, mem[388]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              return bool(ext_call.return_data[0])
  else:
      uint8(stor2.field_0) = 1
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0xf0cbe059 with:
               gas gas_remaining - 50 wei
              args 0, 0, 0, _value, symbol, 160, 0, 0, None
          if ext_call.success:
              uint8(stor2.field_0) = 0
              if not ext_call.return_data[0]:
                  if stor4[caller]:
                      return 0
                  if tx.origin != caller:
                      return 0
                  if eth.balance(caller) >= 10^16:
                      return 0
                  if stor3[caller]:
                      if caller != caller:
                          if caller == tx.origin:
                              mem[356] = mem[383 len 5]
                              require ext_code.size(multiAssetAddress)
                              call multiAssetAddress.0x64ef212e with:
                                   gas gas_remaining - 50 wei
                                  args caller, 10^17, symbol, 128, 0, 5, mem[356]
                          else:
                              mem[388] = mem[415 len 5]
                              require ext_code.size(multiAssetAddress)
                              call multiAssetAddress.0x31c6c4cf with:
                                   gas gas_remaining - 50 wei
                                  args 0, uint32(caller), caller, 10^17, symbol, 0, 160, 5, mem[388]
                          require ext_call.success
                          return 0
                  uint8(stor2.field_0) = 1
                  if caller == tx.origin:
                      mem[356] = mem[383 len 5]
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.0x64ef212e with:
                               gas gas_remaining - 50 wei
                              args addr(this.address), 10^17, symbol, 128, 0, 5, mem[356]
                          if ext_call.success:
                              uint8(stor2.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return 0
                              call caller with:
                                 value 10^17 wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return 0
                  else:
                      mem[388] = mem[415 len 5]
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.0x31c6c4cf with:
                               gas gas_remaining - 50 wei
                              args 0, uint32(caller), addr(this.address), 10^17, symbol, 0, 160, 5, mem[388]
                          if ext_call.success:
                              uint8(stor2.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return 0
                              call caller with:
                                 value 10^17 wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return 0
              else:
                  if _to == this.address:
                      call caller with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                  else:
                      call _to with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                  if ext_call.success:
                      if stor4[caller]:
                          return 1
                      if tx.origin != caller:
                          return 1
                      if eth.balance(caller) >= 10^16:
                          return 1
                      if stor3[caller]:
                          if caller != caller:
                              if caller == tx.origin:
                                  mem[356] = mem[383 len 5]
                                  require ext_code.size(multiAssetAddress)
                                  call multiAssetAddress.0x64ef212e with:
                                       gas gas_remaining - 50 wei
                                      args caller, 10^17, symbol, 128, 0, 5, mem[356]
                              else:
                                  mem[388] = mem[415 len 5]
                                  require ext_code.size(multiAssetAddress)
                                  call multiAssetAddress.0x31c6c4cf with:
                                       gas gas_remaining - 50 wei
                                      args 0, uint32(caller), caller, 10^17, symbol, 0, 160, 5, mem[388]
                              require ext_call.success
                              return 1
                      uint8(stor2.field_0) = 1
                      if caller == tx.origin:
                          mem[356] = mem[383 len 5]
                          if ext_code.size(multiAssetAddress):
                              call multiAssetAddress.0x64ef212e with:
                                   gas gas_remaining - 50 wei
                                  args addr(this.address), 10^17, symbol, 128, 0, 5, mem[356]
                              if ext_call.success:
                                  uint8(stor2.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return 1
                                  call caller with:
                                     value 10^17 wei
                                       gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      return 1
                      else:
                          mem[388] = mem[415 len 5]
                          if ext_code.size(multiAssetAddress):
                              call multiAssetAddress.0x31c6c4cf with:
                                   gas gas_remaining - 50 wei
                                  args 0, uint32(caller), addr(this.address), 10^17, symbol, 0, 160, 5, mem[388]
                              if ext_call.success:
                                  uint8(stor2.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return 1
                                  call caller with:
                                     value 10^17 wei
                                       gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      return 1
  revert 


# hash = 0x23de6651
# getter = None
# const = None
# payable = False
def emitTransfer(address _from, address _to, uint256 _value): # not payable
  if multiAssetAddress == caller:
      if _to == this.address:
          require uint8(stor2.field_0)
      else:
          if not stor3[addr(_to)]:
              require uint8(stor2.field_8)
      log Transfer(
            address from=_value,
            address to=_from,
            uint256 value=_to)


# hash = 0x2cc0b254
# getter = None
# const = None
# payable = False
def init(address _multiAsset, bytes32 _symbol): # not payable
  if multiAssetAddress:
      return 0
  mem[388] = mem[411 len 9]
  require ext_code.size(_multiAsset)
  call _multiAsset.issueAsset(bytes32 symbol, uint256 value, string name, string description, uint8 baseUnit, bool isReissuable) with:
       gas gas_remaining - 50 wei
      args 0, 0, 0, 192, 256, 18, 1, 9, 0, mem[397 len 23], 16, '1-to-1 with wei.'
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  require ext_code.size(_multiAsset)
  call _multiAsset.0x6489899 with:
       gas gas_remaining - 50 wei
      args addr(this.address), 1, _symbol
  require ext_call.success
  require ext_call.return_data[0]
  require ext_code.size(_multiAsset)
  call _multiAsset.0x30d30c89 with:
       gas gas_remaining - 50 wei
      args addr(this.address), _symbol
  require ext_call.success
  require ext_call.return_data[0]
  require ext_code.size(_multiAsset)
  call _multiAsset.0xf01b0220 with:
       gas gas_remaining - 50 wei
      args 0, 1, _symbol
  require ext_call.success
  require ext_call.return_data[0]
  multiAssetAddress = _multiAsset
  symbol = _symbol
  return 1


# hash = 0x313ce567
# getter = None
# const = ['return', 18]
# payable = False
const decimals = 18


# hash = 0x32e4a382
# getter = None
# const = ['return', 10000000000000000]
# payable = False
const unknown32e4a382 = 10^16


# hash = 0x6461fe39
# getter = None
# const = None
# payable = False
def transferFromWithReference(address _from, address _to, uint256 _value, string _reference): # not payable
  if tx.origin != caller:
      return 0
  if stor3[addr(_to)]:
      mem[ceil32(_reference.length) + 324 len _reference.length] = _reference[all]
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0xf0cbe059 with:
               gas gas_remaining - 50 wei
              args addr(_from), addr(_to), _value, symbol, Array(len=_reference.length, data=_reference[all])
          if ext_call.success:
              if stor4[caller]:
                  return bool(ext_call.return_data[0])
              if tx.origin != caller:
                  return bool(ext_call.return_data[0])
              if eth.balance(caller) >= 10^16:
                  return bool(ext_call.return_data[0])
              if stor3[caller]:
                  if caller != caller:
                      if caller == tx.origin:
                          mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x64ef212e with:
                               gas gas_remaining - 50 wei
                              args caller, 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                      else:
                          mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x31c6c4cf with:
                               gas gas_remaining - 50 wei
                              args caller, caller, 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                      require ext_call.success
                      return bool(ext_call.return_data[0])
              uint8(stor2.field_0) = 1
              if caller == tx.origin:
                  mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x64ef212e with:
                           gas gas_remaining - 50 wei
                          args addr(this.address), 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              return bool(ext_call.return_data[0])
              else:
                  mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x31c6c4cf with:
                           gas gas_remaining - 50 wei
                          args caller, addr(this.address), 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              return bool(ext_call.return_data[0])
  else:
      uint8(stor2.field_0) = 1
      mem[ceil32(_reference.length) + 324 len _reference.length] = _reference[all]
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0xf0cbe059 with:
               gas gas_remaining - 50 wei
              args addr(_from), addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
          if ext_call.success:
              uint8(stor2.field_0) = 0
              if not ext_call.return_data[0]:
                  if stor4[caller]:
                      return 0
                  if tx.origin != caller:
                      return 0
                  if eth.balance(caller) >= 10^16:
                      return 0
                  if stor3[caller]:
                      if caller != caller:
                          if caller == tx.origin:
                              mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                              require ext_code.size(multiAssetAddress)
                              call multiAssetAddress.0x64ef212e with:
                                   gas gas_remaining - 50 wei
                                  args caller, 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                          else:
                              mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                              require ext_code.size(multiAssetAddress)
                              call multiAssetAddress.0x31c6c4cf with:
                                   gas gas_remaining - 50 wei
                                  args caller, caller, 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                          require ext_call.success
                          return 0
                  uint8(stor2.field_0) = 1
                  if caller == tx.origin:
                      mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.0x64ef212e with:
                               gas gas_remaining - 50 wei
                              args addr(this.address), 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                          if ext_call.success:
                              uint8(stor2.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return 0
                              call caller with:
                                 value 10^17 wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return 0
                  else:
                      mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.0x31c6c4cf with:
                               gas gas_remaining - 50 wei
                              args caller, addr(this.address), 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                          if ext_call.success:
                              uint8(stor2.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return 0
                              call caller with:
                                 value 10^17 wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return 0
              else:
                  if _to == this.address:
                      call caller with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                  else:
                      call _to with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                  if ext_call.success:
                      if stor4[caller]:
                          return 1
                      if tx.origin != caller:
                          return 1
                      if eth.balance(caller) >= 10^16:
                          return 1
                      if stor3[caller]:
                          if caller != caller:
                              if caller == tx.origin:
                                  mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                                  require ext_code.size(multiAssetAddress)
                                  call multiAssetAddress.0x64ef212e with:
                                       gas gas_remaining - 50 wei
                                      args caller, 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                              else:
                                  mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                                  require ext_code.size(multiAssetAddress)
                                  call multiAssetAddress.0x31c6c4cf with:
                                       gas gas_remaining - 50 wei
                                      args caller, caller, 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                              require ext_call.success
                              return 1
                      uint8(stor2.field_0) = 1
                      if caller == tx.origin:
                          mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                          if ext_code.size(multiAssetAddress):
                              call multiAssetAddress.0x64ef212e with:
                                   gas gas_remaining - 50 wei
                                  args addr(this.address), 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                              if ext_call.success:
                                  uint8(stor2.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return 1
                                  call caller with:
                                     value 10^17 wei
                                       gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      return 1
                      else:
                          mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                          if ext_code.size(multiAssetAddress):
                              call multiAssetAddress.0x31c6c4cf with:
                                   gas gas_remaining - 50 wei
                                  args caller, addr(this.address), 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                              if ext_call.success:
                                  uint8(stor2.field_0) = 0
                                  if not ext_call.return_data[0]:
                                      return 1
                                  call caller with:
                                     value 10^17 wei
                                       gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      return 1
  revert 


# hash = 0x69f1169f
# getter = None
# const = None
# payable = False
def unknown69f1169f(bool _param1): # not payable
  stor4[caller] = uint8(not _param1)
  return 1


# hash = 0x70a08231
# getter = None
# const = None
# payable = False
def balanceOf(address _owner): # not payable
  require ext_code.size(multiAssetAddress)
  call multiAssetAddress.balanceOf(address holder, bytes32 symbol) with:
       gas gas_remaining - 50 wei
      args addr(_owner), symbol
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x82fc49b8
# getter = None
# const = None
# payable = False
def setCosignerAddress(address _cosigner): # not payable
  if tx.origin != caller:
      return 0
  require ext_code.size(multiAssetAddress)
  call multiAssetAddress.0xe82b7cb2 with:
       gas gas_remaining - 50 wei
      args addr(_cosigner), symbol
  require ext_call.success
  if stor4[caller]:
      return bool(ext_call.return_data[0])
  if tx.origin != caller:
      return bool(ext_call.return_data[0])
  if eth.balance(caller) >= 10^16:
      return bool(ext_call.return_data[0])
  if stor3[caller]:
      if caller != caller:
          if caller == tx.origin:
              mem[324] = mem[351 len 5]
              require ext_code.size(multiAssetAddress)
              call multiAssetAddress.0x64ef212e with:
                   gas gas_remaining - 50 wei
                  args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
          else:
              mem[356] = mem[383 len 5]
              require ext_code.size(multiAssetAddress)
              call multiAssetAddress.0x31c6c4cf with:
                   gas gas_remaining - 50 wei
                  args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
          require ext_call.success
          return bool(ext_call.return_data[0])
  uint8(stor2.field_0) = 1
  if caller == tx.origin:
      mem[324] = mem[351 len 5]
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0x64ef212e with:
               gas gas_remaining - 50 wei
              args 0, 0, 10^17, symbol, 128, 5, mem[324]
          if ext_call.success:
              uint8(stor2.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              call caller with:
                 value 10^17 wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  return bool(ext_call.return_data[0])
  else:
      mem[356] = mem[383 len 5]
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0x31c6c4cf with:
               gas gas_remaining - 50 wei
              args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
          if ext_call.success:
              uint8(stor2.field_0) = 0
              if not ext_call.return_data[0]:
                  return bool(ext_call.return_data[0])
              call caller with:
                 value 10^17 wei
                   gas gas_remaining - 34050 wei
              if ext_call.success:
                  return bool(ext_call.return_data[0])
  revert 


# hash = 0x883cbde4
# getter = None
# const = None
# payable = False
def unknown883cbde4(addr _param1): # not payable
  return not bool(stor4[addr(_param1)])


# hash = 0x8bbbbfd3
# getter = None
# const = None
# payable = False
def unknown8bbbbfd3(uint8 _param1): # not payable
  stor3[caller] = _param1
  return 1


# hash = 0x8d6a5117
# getter = None
# const = ['return', 100000000000000000]
# payable = False
const unknown8d6a5117 = 10^17


# hash = 0x95d89b41
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def symbol(): # not payable
  return symbol


# hash = 0xa48a663c
# getter = None
# const = None
# payable = False
def transferFromToICAPWithReference(address _from, bytes32 _icap, uint256 _value, string _reference): # not payable
  if tx.origin != caller:
      return 0
  require ext_code.size(multiAssetAddress)
  call multiAssetAddress.registryICAP() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
       gas gas_remaining - 50 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
  require ext_call.success
  if stor3[ext_call.return_data[12 len 20]]:
      mem[ceil32(_reference.length) + 292 len _reference.length] = _reference[all]
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0xea98e540 with:
               gas gas_remaining - 50 wei
              args addr(_from), _icap, _value, Array(len=_reference.length, data=_reference[all])
          if ext_call.success:
              if stor4[caller]:
                  return bool(ext_call.return_data[0])
              if tx.origin != caller:
                  return bool(ext_call.return_data[0])
              if eth.balance(caller) >= 10^16:
                  return bool(ext_call.return_data[0])
              if stor3[caller]:
                  if caller != caller:
                      if caller == tx.origin:
                          mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x64ef212e with:
                               gas gas_remaining - 50 wei
                              args caller, 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                      else:
                          mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x31c6c4cf with:
                               gas gas_remaining - 50 wei
                              args caller, caller, 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                      require ext_call.success
                      return bool(ext_call.return_data[0])
              uint8(stor2.field_0) = 1
              if caller == tx.origin:
                  mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x64ef212e with:
                           gas gas_remaining - 50 wei
                          args addr(this.address), 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              return bool(ext_call.return_data[0])
              else:
                  mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x31c6c4cf with:
                           gas gas_remaining - 50 wei
                          args caller, addr(this.address), 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              return bool(ext_call.return_data[0])
  else:
      uint8(stor2.field_0) = 1
      mem[ceil32(_reference.length) + 324 len _reference.length] = _reference[all]
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0xf0cbe059 with:
               gas gas_remaining - 50 wei
              args addr(_from), addr(this.address), _value, symbol, Array(len=_reference.length, data=_reference[all])
          if ext_call.success:
              uint8(stor2.field_0) = 0
              if not ext_call.return_data[0]:
                  if stor4[caller]:
                      return 0
                  if tx.origin != caller:
                      return 0
                  if eth.balance(caller) >= 10^16:
                      return 0
                  if stor3[caller]:
                      if caller != caller:
                          if caller == tx.origin:
                              mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                              require ext_code.size(multiAssetAddress)
                              call multiAssetAddress.0x64ef212e with:
                                   gas gas_remaining - 50 wei
                                  args caller, 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                          else:
                              mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                              require ext_code.size(multiAssetAddress)
                              call multiAssetAddress.0x31c6c4cf with:
                                   gas gas_remaining - 50 wei
                                  args caller, caller, 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                          require ext_call.success
                          return 0
                  uint8(stor2.field_0) = 1
                  if caller == tx.origin:
                      mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.0x64ef212e with:
                               gas gas_remaining - 50 wei
                              args addr(this.address), 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                          if ext_call.success:
                              uint8(stor2.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return 0
                              call caller with:
                                 value 10^17 wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return 0
                  else:
                      mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.0x31c6c4cf with:
                               gas gas_remaining - 50 wei
                              args caller, addr(this.address), 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                          if ext_call.success:
                              uint8(stor2.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return 0
                              call caller with:
                                 value 10^17 wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return 0
              else:
                  mem[ceil32(_reference.length) + 228 len _reference.length] = _reference[all]
                  if ext_code.size(unknownaa46f961Address):
                      call unknownaa46f961Address.0xd882aa0 with:
                         value _value wei
                           gas gas_remaining - 9050 wei
                          args _icap, Array(len=_reference.length, data=_reference[all])
                      if ext_call.success:
                          if ext_call.return_data[0]:
                              if stor4[caller]:
                                  return 1
                              if tx.origin != caller:
                                  return 1
                              if eth.balance(caller) >= 10^16:
                                  return 1
                              if stor3[caller]:
                                  if caller != caller:
                                      if caller == tx.origin:
                                          mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                                          require ext_code.size(multiAssetAddress)
                                          call multiAssetAddress.0x64ef212e with:
                                               gas gas_remaining - 50 wei
                                              args caller, 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                                      else:
                                          mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                                          require ext_code.size(multiAssetAddress)
                                          call multiAssetAddress.0x31c6c4cf with:
                                               gas gas_remaining - 50 wei
                                              args caller, caller, 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                                      require ext_call.success
                                      return 1
                              uint8(stor2.field_0) = 1
                              if caller == tx.origin:
                                  mem[ceil32(_reference.length) + 356] = mem[ceil32(_reference.length) + 383 len 5]
                                  if ext_code.size(multiAssetAddress):
                                      call multiAssetAddress.0x64ef212e with:
                                           gas gas_remaining - 50 wei
                                          args addr(this.address), 10^17, symbol, 128, 5, mem[ceil32(_reference.length) + 356]
                                      if ext_call.success:
                                          uint8(stor2.field_0) = 0
                                          if not ext_call.return_data[0]:
                                              return 1
                                          call caller with:
                                             value 10^17 wei
                                               gas gas_remaining - 34050 wei
                                          if ext_call.success:
                                              return 1
                              else:
                                  mem[ceil32(_reference.length) + 388] = mem[ceil32(_reference.length) + 415 len 5]
                                  if ext_code.size(multiAssetAddress):
                                      call multiAssetAddress.0x31c6c4cf with:
                                           gas gas_remaining - 50 wei
                                          args caller, addr(this.address), 10^17, symbol, 160, 5, mem[ceil32(_reference.length) + 388]
                                      if ext_call.success:
                                          uint8(stor2.field_0) = 0
                                          if not ext_call.return_data[0]:
                                              return 1
                                          call caller with:
                                             value 10^17 wei
                                               gas gas_remaining - 34050 wei
                                          if ext_call.success:
                                              return 1
  revert 


# hash = 0xa525f42c
# getter = None
# const = None
# payable = False
def transferFromToICAP(address _from, bytes32 _icap, uint256 _value): # not payable
  if tx.origin != caller:
      return 0
  require ext_code.size(multiAssetAddress)
  call multiAssetAddress.registryICAP() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).institutions(bytes32 param1) with:
       gas gas_remaining - 50 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 7) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 8) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 9) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_icap')), 0) + 256, 10) << (('mask_shl', 256, 0, -3, ('param', '_icap')), 0) - 256)
  require ext_call.success
  if stor3[ext_call.return_data[12 len 20]]:
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0xea98e540 with:
               gas gas_remaining - 50 wei
              args 0, 0, _icap, _value, 128, 0, 0, None
          if ext_call.success:
              if stor4[caller]:
                  return bool(ext_call.return_data[0])
              if tx.origin != caller:
                  return bool(ext_call.return_data[0])
              if eth.balance(caller) >= 10^16:
                  return bool(ext_call.return_data[0])
              if stor3[caller]:
                  if caller != caller:
                      if caller == tx.origin:
                          mem[356] = mem[383 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x64ef212e with:
                               gas gas_remaining - 50 wei
                              args caller, 10^17, symbol, 0, 128, 5, mem[356]
                      else:
                          mem[388] = mem[415 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x31c6c4cf with:
                               gas gas_remaining - 50 wei
                              args 0, uint32(caller), caller, 10^17, 0, symbol, 160, 5, mem[388]
                      require ext_call.success
                      return bool(ext_call.return_data[0])
              uint8(stor2.field_0) = 1
              if caller == tx.origin:
                  mem[356] = mem[383 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x64ef212e with:
                           gas gas_remaining - 50 wei
                          args addr(this.address), 10^17, symbol, 0, 128, 5, mem[356]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              return bool(ext_call.return_data[0])
              else:
                  mem[388] = mem[415 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x31c6c4cf with:
                           gas gas_remaining - 50 wei
                          args 0, uint32(caller), addr(this.address), 10^17, 0, symbol, 160, 5, mem[388]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              return bool(ext_call.return_data[0])
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              return bool(ext_call.return_data[0])
  else:
      uint8(stor2.field_0) = 1
      if ext_code.size(multiAssetAddress):
          call multiAssetAddress.0xf0cbe059 with:
               gas gas_remaining - 50 wei
              args 0, 0, 0, _value, symbol, 160, 0, 0, None
          if ext_call.success:
              uint8(stor2.field_0) = 0
              if not ext_call.return_data[0]:
                  if stor4[caller]:
                      return 0
                  if tx.origin != caller:
                      return 0
                  if eth.balance(caller) >= 10^16:
                      return 0
                  if stor3[caller]:
                      if caller != caller:
                          if caller == tx.origin:
                              mem[356] = mem[383 len 5]
                              require ext_code.size(multiAssetAddress)
                              call multiAssetAddress.0x64ef212e with:
                                   gas gas_remaining - 50 wei
                                  args caller, 10^17, symbol, 128, 0, 5, mem[356]
                          else:
                              mem[388] = mem[415 len 5]
                              require ext_code.size(multiAssetAddress)
                              call multiAssetAddress.0x31c6c4cf with:
                                   gas gas_remaining - 50 wei
                                  args 0, uint32(caller), caller, 10^17, symbol, 0, 160, 5, mem[388]
                          require ext_call.success
                          return 0
                  uint8(stor2.field_0) = 1
                  if caller == tx.origin:
                      mem[356] = mem[383 len 5]
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.0x64ef212e with:
                               gas gas_remaining - 50 wei
                              args addr(this.address), 10^17, symbol, 128, 0, 5, mem[356]
                          if ext_call.success:
                              uint8(stor2.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return 0
                              call caller with:
                                 value 10^17 wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return 0
                  else:
                      mem[388] = mem[415 len 5]
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.0x31c6c4cf with:
                               gas gas_remaining - 50 wei
                              args 0, uint32(caller), addr(this.address), 10^17, symbol, 0, 160, 5, mem[388]
                          if ext_call.success:
                              uint8(stor2.field_0) = 0
                              if not ext_call.return_data[0]:
                                  return 0
                              call caller with:
                                 value 10^17 wei
                                   gas gas_remaining - 34050 wei
                              if ext_call.success:
                                  return 0
              else:
                  if ext_code.size(unknownaa46f961Address):
                      call unknownaa46f961Address.0xd882aa0 with:
                         value _value wei
                           gas gas_remaining - 9050 wei
                          args _icap, 64, 0
                      if ext_call.success:
                          if ext_call.return_data[0]:
                              if stor4[caller]:
                                  return 1
                              if tx.origin != caller:
                                  return 1
                              if eth.balance(caller) >= 10^16:
                                  return 1
                              if stor3[caller]:
                                  if caller != caller:
                                      if caller == tx.origin:
                                          mem[356] = mem[383 len 5]
                                          require ext_code.size(multiAssetAddress)
                                          call multiAssetAddress.0x64ef212e with:
                                               gas gas_remaining - 50 wei
                                              args caller, 10^17, symbol, 128, 0, 5, mem[356]
                                      else:
                                          mem[388] = mem[415 len 5]
                                          require ext_code.size(multiAssetAddress)
                                          call multiAssetAddress.0x31c6c4cf with:
                                               gas gas_remaining - 50 wei
                                              args 0, uint32(caller), caller, 10^17, symbol, 0, 160, 5, mem[388]
                                      require ext_call.success
                                      return 1
                              uint8(stor2.field_0) = 1
                              if caller == tx.origin:
                                  mem[356] = mem[383 len 5]
                                  if ext_code.size(multiAssetAddress):
                                      call multiAssetAddress.0x64ef212e with:
                                           gas gas_remaining - 50 wei
                                          args addr(this.address), 10^17, symbol, 128, 0, 5, mem[356]
                                      if ext_call.success:
                                          uint8(stor2.field_0) = 0
                                          if not ext_call.return_data[0]:
                                              return 1
                                          call caller with:
                                             value 10^17 wei
                                               gas gas_remaining - 34050 wei
                                          if ext_call.success:
                                              return 1
                              else:
                                  mem[388] = mem[415 len 5]
                                  if ext_code.size(multiAssetAddress):
                                      call multiAssetAddress.0x31c6c4cf with:
                                           gas gas_remaining - 50 wei
                                          args 0, uint32(caller), addr(this.address), 10^17, symbol, 0, 160, 5, mem[388]
                                      if ext_call.success:
                                          uint8(stor2.field_0) = 0
                                          if not ext_call.return_data[0]:
                                              return 1
                                          call caller with:
                                             value 10^17 wei
                                               gas gas_remaining - 34050 wei
                                          if ext_call.success:
                                              return 1
  revert 


# hash = 0xaa46f961
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def unknownaa46f961(): # not payable
  return unknownaa46f961Address


# hash = 0xbe9b42d2
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 3]]]]
# const = None
# payable = False
def unknownbe9b42d2(addr _param1): # not payable
  return bool(stor3[addr(_param1)])


# hash = 0xdd62ed3e
# getter = None
# const = None
# payable = False
def allowance(address _owner, address _spender): # not payable
  require ext_code.size(multiAssetAddress)
  call multiAssetAddress.allowance(address from, address spender, bytes32 symbol) with:
       gas gas_remaining - 50 wei
      args addr(_owner), addr(_spender), symbol
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0xf340fa01
# getter = None
# const = None
# payable = True
def deposit(address _payee) payable: 
  if call.value <= 0:
      if stor4[caller]:
          return 0
      if tx.origin != caller:
          return 0
      if eth.balance(caller) >= 10^16:
          return 0
      if stor3[caller]:
          if caller != caller:
              if caller == tx.origin:
                  mem[324] = mem[351 len 5]
                  require ext_code.size(multiAssetAddress)
                  call multiAssetAddress.0x64ef212e with:
                       gas gas_remaining - 50 wei
                      args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
              else:
                  mem[356] = mem[383 len 5]
                  require ext_code.size(multiAssetAddress)
                  call multiAssetAddress.0x31c6c4cf with:
                       gas gas_remaining - 50 wei
                      args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
              require ext_call.success
              return 0
      uint8(stor2.field_0) = 1
      if caller == tx.origin:
          mem[324] = mem[351 len 5]
          if ext_code.size(multiAssetAddress):
              call multiAssetAddress.0x64ef212e with:
                   gas gas_remaining - 50 wei
                  args 0, 0, 10^17, symbol, 128, 5, mem[324]
              if ext_call.success:
                  uint8(stor2.field_0) = 0
                  if not ext_call.return_data[0]:
                      return 0
                  call caller with:
                     value 10^17 wei
                       gas gas_remaining - 34050 wei
                  if ext_call.success:
                      return 0
      else:
          mem[356] = mem[383 len 5]
          if ext_code.size(multiAssetAddress):
              call multiAssetAddress.0x31c6c4cf with:
                   gas gas_remaining - 50 wei
                  args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
              if ext_call.success:
                  uint8(stor2.field_0) = 0
                  if not ext_call.return_data[0]:
                      return 0
                  call caller with:
                     value 10^17 wei
                       gas gas_remaining - 34050 wei
                  if ext_call.success:
                      return 0
  else:
      if _payee == this.address:
          call caller with:
             value call.value wei
               gas gas_remaining - 34050 wei
          if ext_call.success:
              if stor4[caller]:
                  return 0
              if tx.origin != caller:
                  return 0
              if eth.balance(caller) >= 10^16:
                  return 0
              if stor3[caller]:
                  if caller != caller:
                      if caller == tx.origin:
                          mem[324] = mem[351 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x64ef212e with:
                               gas gas_remaining - 50 wei
                              args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                      else:
                          mem[356] = mem[383 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x31c6c4cf with:
                               gas gas_remaining - 50 wei
                              args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                      require ext_call.success
                      return 0
              uint8(stor2.field_0) = 1
              if caller == tx.origin:
                  mem[324] = mem[351 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x64ef212e with:
                           gas gas_remaining - 50 wei
                          args 0, 0, 10^17, symbol, 128, 5, mem[324]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              return 0
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              return 0
              else:
                  mem[356] = mem[383 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x31c6c4cf with:
                           gas gas_remaining - 50 wei
                          args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              return 0
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              return 0
      else:
          if ext_code.size(multiAssetAddress):
              call multiAssetAddress.balanceOf(address holder, bytes32 symbol) with:
                   gas gas_remaining - 50 wei
                  args addr(this.address), symbol
              if ext_call.success:
                  if ext_call.return_data[0] >= call.value:
                      uint8(stor2.field_8) = 1
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.0x6e293817 with:
                               gas gas_remaining - 50 wei
                              args 0, 0, uint32(call.value), symbol, 128, 7, 'Deposit'
                          if ext_call.success:
                              uint8(stor2.field_8) = 0
                              if ext_call.return_data[0]:
                                  if stor4[caller]:
                                      return bool(ext_call.return_data[0])
                                  if tx.origin != caller:
                                      return bool(ext_call.return_data[0])
                                  if eth.balance(caller) >= 10^16:
                                      return bool(ext_call.return_data[0])
                                  if stor3[caller]:
                                      if caller != caller:
                                          if caller == tx.origin:
                                              mem[324] = mem[351 len 5]
                                              require ext_code.size(multiAssetAddress)
                                              call multiAssetAddress.0x64ef212e with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                                          else:
                                              mem[356] = mem[383 len 5]
                                              require ext_code.size(multiAssetAddress)
                                              call multiAssetAddress.0x31c6c4cf with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                                          require ext_call.success
                                          return bool(ext_call.return_data[0])
                                  uint8(stor2.field_0) = 1
                                  if caller == tx.origin:
                                      mem[324] = mem[351 len 5]
                                      if ext_code.size(multiAssetAddress):
                                          call multiAssetAddress.0x64ef212e with:
                                               gas gas_remaining - 50 wei
                                              args 0, 0, 10^17, symbol, 128, 5, mem[324]
                                          if ext_call.success:
                                              uint8(stor2.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              call caller with:
                                                 value 10^17 wei
                                                   gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  return bool(ext_call.return_data[0])
                                  else:
                                      mem[356] = mem[383 len 5]
                                      if ext_code.size(multiAssetAddress):
                                          call multiAssetAddress.0x31c6c4cf with:
                                               gas gas_remaining - 50 wei
                                              args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                                          if ext_call.success:
                                              uint8(stor2.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  return bool(ext_call.return_data[0])
                                              call caller with:
                                                 value 10^17 wei
                                                   gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  return bool(ext_call.return_data[0])
                              else:
                                  call caller with:
                                     value call.value wei
                                       gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      if stor4[caller]:
                                          return 0
                                      if tx.origin != caller:
                                          return 0
                                      if eth.balance(caller) >= 10^16:
                                          return 0
                                      if stor3[caller]:
                                          if caller != caller:
                                              if caller == tx.origin:
                                                  mem[324] = mem[351 len 5]
                                                  require ext_code.size(multiAssetAddress)
                                                  call multiAssetAddress.0x64ef212e with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                                              else:
                                                  mem[356] = mem[383 len 5]
                                                  require ext_code.size(multiAssetAddress)
                                                  call multiAssetAddress.0x31c6c4cf with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                                              require ext_call.success
                                              return 0
                                      uint8(stor2.field_0) = 1
                                      if caller == tx.origin:
                                          mem[324] = mem[351 len 5]
                                          if ext_code.size(multiAssetAddress):
                                              call multiAssetAddress.0x64ef212e with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, 10^17, symbol, 128, 5, mem[324]
                                              if ext_call.success:
                                                  uint8(stor2.field_0) = 0
                                                  if not ext_call.return_data[0]:
                                                      return 0
                                                  call caller with:
                                                     value 10^17 wei
                                                       gas gas_remaining - 34050 wei
                                                  if ext_call.success:
                                                      return 0
                                      else:
                                          mem[356] = mem[383 len 5]
                                          if ext_code.size(multiAssetAddress):
                                              call multiAssetAddress.0x31c6c4cf with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                                              if ext_call.success:
                                                  uint8(stor2.field_0) = 0
                                                  if not ext_call.return_data[0]:
                                                      return 0
                                                  call caller with:
                                                     value 10^17 wei
                                                       gas gas_remaining - 34050 wei
                                                  if ext_call.success:
                                                      return 0
                  else:
                      uint8(stor2.field_0) = 1
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.reissueAsset(bytes32 symbol, uint256 value) with:
                               gas gas_remaining - 50 wei
                              args symbol, call.value - ext_call.return_data[0]
                          if ext_call.success:
                              uint8(stor2.field_0) = 0
                              if not ext_call.return_data[0]:
                                  call caller with:
                                     value call.value wei
                                       gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      if stor4[caller]:
                                          return 0
                                      if tx.origin != caller:
                                          return 0
                                      if eth.balance(caller) >= 10^16:
                                          return 0
                                      if stor3[caller]:
                                          if caller != caller:
                                              if caller == tx.origin:
                                                  mem[324] = mem[351 len 5]
                                                  require ext_code.size(multiAssetAddress)
                                                  call multiAssetAddress.0x64ef212e with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                                              else:
                                                  mem[356] = mem[383 len 5]
                                                  require ext_code.size(multiAssetAddress)
                                                  call multiAssetAddress.0x31c6c4cf with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                                              require ext_call.success
                                              return 0
                                      uint8(stor2.field_0) = 1
                                      if caller == tx.origin:
                                          mem[324] = mem[351 len 5]
                                          if ext_code.size(multiAssetAddress):
                                              call multiAssetAddress.0x64ef212e with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, 10^17, symbol, 128, 5, mem[324]
                                              if ext_call.success:
                                                  uint8(stor2.field_0) = 0
                                                  if not ext_call.return_data[0]:
                                                      return 0
                                                  call caller with:
                                                     value 10^17 wei
                                                       gas gas_remaining - 34050 wei
                                                  if ext_call.success:
                                                      return 0
                                      else:
                                          mem[356] = mem[383 len 5]
                                          if ext_code.size(multiAssetAddress):
                                              call multiAssetAddress.0x31c6c4cf with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                                              if ext_call.success:
                                                  uint8(stor2.field_0) = 0
                                                  if not ext_call.return_data[0]:
                                                      return 0
                                                  call caller with:
                                                     value 10^17 wei
                                                       gas gas_remaining - 34050 wei
                                                  if ext_call.success:
                                                      return 0
                              else:
                                  uint8(stor2.field_8) = 1
                                  if ext_code.size(multiAssetAddress):
                                      call multiAssetAddress.0x6e293817 with:
                                           gas gas_remaining - 50 wei
                                          args 0, 0, uint32(call.value), symbol, 128, 7, 'Deposit'
                                      if ext_call.success:
                                          uint8(stor2.field_8) = 0
                                          if ext_call.return_data[0]:
                                              if stor4[caller]:
                                                  return bool(ext_call.return_data[0])
                                              if tx.origin != caller:
                                                  return bool(ext_call.return_data[0])
                                              if eth.balance(caller) >= 10^16:
                                                  return bool(ext_call.return_data[0])
                                              if stor3[caller]:
                                                  if caller != caller:
                                                      if caller == tx.origin:
                                                          mem[324] = mem[351 len 5]
                                                          require ext_code.size(multiAssetAddress)
                                                          call multiAssetAddress.0x64ef212e with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                                                      else:
                                                          mem[356] = mem[383 len 5]
                                                          require ext_code.size(multiAssetAddress)
                                                          call multiAssetAddress.0x31c6c4cf with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                                                      require ext_call.success
                                                      return bool(ext_call.return_data[0])
                                              uint8(stor2.field_0) = 1
                                              if caller == tx.origin:
                                                  mem[324] = mem[351 len 5]
                                                  if ext_code.size(multiAssetAddress):
                                                      call multiAssetAddress.0x64ef212e with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, 10^17, symbol, 128, 5, mem[324]
                                                      if ext_call.success:
                                                          uint8(stor2.field_0) = 0
                                                          if not ext_call.return_data[0]:
                                                              return bool(ext_call.return_data[0])
                                                          call caller with:
                                                             value 10^17 wei
                                                               gas gas_remaining - 34050 wei
                                                          if ext_call.success:
                                                              return bool(ext_call.return_data[0])
                                              else:
                                                  mem[356] = mem[383 len 5]
                                                  if ext_code.size(multiAssetAddress):
                                                      call multiAssetAddress.0x31c6c4cf with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                                                      if ext_call.success:
                                                          uint8(stor2.field_0) = 0
                                                          if not ext_call.return_data[0]:
                                                              return bool(ext_call.return_data[0])
                                                          call caller with:
                                                             value 10^17 wei
                                                               gas gas_remaining - 34050 wei
                                                          if ext_call.success:
                                                              return bool(ext_call.return_data[0])
                                          else:
                                              call caller with:
                                                 value call.value wei
                                                   gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  if stor4[caller]:
                                                      return 0
                                                  if tx.origin != caller:
                                                      return 0
                                                  if eth.balance(caller) >= 10^16:
                                                      return 0
                                                  if stor3[caller]:
                                                      if caller != caller:
                                                          if caller == tx.origin:
                                                              mem[324] = mem[351 len 5]
                                                              require ext_code.size(multiAssetAddress)
                                                              call multiAssetAddress.0x64ef212e with:
                                                                   gas gas_remaining - 50 wei
                                                                  args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                                                          else:
                                                              mem[356] = mem[383 len 5]
                                                              require ext_code.size(multiAssetAddress)
                                                              call multiAssetAddress.0x31c6c4cf with:
                                                                   gas gas_remaining - 50 wei
                                                                  args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                                                          require ext_call.success
                                                          return 0
                                                  uint8(stor2.field_0) = 1
                                                  if caller == tx.origin:
                                                      mem[324] = mem[351 len 5]
                                                      if ext_code.size(multiAssetAddress):
                                                          call multiAssetAddress.0x64ef212e with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, 0, 10^17, symbol, 128, 5, mem[324]
                                                          if ext_call.success:
                                                              uint8(stor2.field_0) = 0
                                                              if not ext_call.return_data[0]:
                                                                  return 0
                                                              call caller with:
                                                                 value 10^17 wei
                                                                   gas gas_remaining - 34050 wei
                                                              if ext_call.success:
                                                                  return 0
                                                  else:
                                                      mem[356] = mem[383 len 5]
                                                      if ext_code.size(multiAssetAddress):
                                                          call multiAssetAddress.0x31c6c4cf with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                                                          if ext_call.success:
                                                              uint8(stor2.field_0) = 0
                                                              if not ext_call.return_data[0]:
                                                                  return 0
                                                              call caller with:
                                                                 value 10^17 wei
                                                                   gas gas_remaining - 34050 wei
                                                              if ext_call.success:
                                                                  return 0
  revert 


# hash = 0xf77b8d7a
# getter = None
# const = None
# payable = False
def unknownf77b8d7a(addr _param1): # not payable
  if unknownaa46f961Address:
      return 0
  unknownaa46f961Address = _param1
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if call.value <= 0:
      if stor4[caller]:
          stop
      if tx.origin != caller:
          stop
      if eth.balance(caller) >= 10^16:
          stop
      if stor3[caller]:
          if caller != caller:
              if caller == tx.origin:
                  mem[324] = mem[351 len 5]
                  require ext_code.size(multiAssetAddress)
                  call multiAssetAddress.0x64ef212e with:
                       gas gas_remaining - 50 wei
                      args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
              else:
                  mem[356] = mem[383 len 5]
                  require ext_code.size(multiAssetAddress)
                  call multiAssetAddress.0x31c6c4cf with:
                       gas gas_remaining - 50 wei
                      args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
              require ext_call.success
              stop
      uint8(stor2.field_0) = 1
      if caller == tx.origin:
          mem[324] = mem[351 len 5]
          if ext_code.size(multiAssetAddress):
              call multiAssetAddress.0x64ef212e with:
                   gas gas_remaining - 50 wei
                  args 0, 0, 10^17, symbol, 128, 5, mem[324]
              if ext_call.success:
                  uint8(stor2.field_0) = 0
                  if not ext_call.return_data[0]:
                      stop
                  call caller with:
                     value 10^17 wei
                       gas gas_remaining - 34050 wei
                  if ext_call.success:
                      stop
      else:
          mem[356] = mem[383 len 5]
          if ext_code.size(multiAssetAddress):
              call multiAssetAddress.0x31c6c4cf with:
                   gas gas_remaining - 50 wei
                  args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
              if ext_call.success:
                  uint8(stor2.field_0) = 0
                  if not ext_call.return_data[0]:
                      stop
                  call caller with:
                     value 10^17 wei
                       gas gas_remaining - 34050 wei
                  if ext_call.success:
                      stop
  else:
      if caller == this.address:
          call caller with:
             value call.value wei
               gas gas_remaining - 34050 wei
          if ext_call.success:
              if stor4[caller]:
                  stop
              if tx.origin != caller:
                  stop
              if eth.balance(caller) >= 10^16:
                  stop
              if stor3[caller]:
                  if caller != caller:
                      if caller == tx.origin:
                          mem[324] = mem[351 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x64ef212e with:
                               gas gas_remaining - 50 wei
                              args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                      else:
                          mem[356] = mem[383 len 5]
                          require ext_code.size(multiAssetAddress)
                          call multiAssetAddress.0x31c6c4cf with:
                               gas gas_remaining - 50 wei
                              args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                      require ext_call.success
                      stop
              uint8(stor2.field_0) = 1
              if caller == tx.origin:
                  mem[324] = mem[351 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x64ef212e with:
                           gas gas_remaining - 50 wei
                          args 0, 0, 10^17, symbol, 128, 5, mem[324]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              stop
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              stop
              else:
                  mem[356] = mem[383 len 5]
                  if ext_code.size(multiAssetAddress):
                      call multiAssetAddress.0x31c6c4cf with:
                           gas gas_remaining - 50 wei
                          args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                      if ext_call.success:
                          uint8(stor2.field_0) = 0
                          if not ext_call.return_data[0]:
                              stop
                          call caller with:
                             value 10^17 wei
                               gas gas_remaining - 34050 wei
                          if ext_call.success:
                              stop
      else:
          if ext_code.size(multiAssetAddress):
              call multiAssetAddress.balanceOf(address holder, bytes32 symbol) with:
                   gas gas_remaining - 50 wei
                  args addr(this.address), symbol
              if ext_call.success:
                  if ext_call.return_data[0] >= call.value:
                      uint8(stor2.field_8) = 1
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.0x6e293817 with:
                               gas gas_remaining - 50 wei
                              args 0, 0, uint32(call.value), symbol, 128, 7, 'Deposit'
                          if ext_call.success:
                              uint8(stor2.field_8) = 0
                              if ext_call.return_data[0]:
                                  if stor4[caller]:
                                      stop
                                  if tx.origin != caller:
                                      stop
                                  if eth.balance(caller) >= 10^16:
                                      stop
                                  if stor3[caller]:
                                      if caller != caller:
                                          if caller == tx.origin:
                                              mem[324] = mem[351 len 5]
                                              require ext_code.size(multiAssetAddress)
                                              call multiAssetAddress.0x64ef212e with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                                          else:
                                              mem[356] = mem[383 len 5]
                                              require ext_code.size(multiAssetAddress)
                                              call multiAssetAddress.0x31c6c4cf with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                                          require ext_call.success
                                          stop
                                  uint8(stor2.field_0) = 1
                                  if caller == tx.origin:
                                      mem[324] = mem[351 len 5]
                                      if ext_code.size(multiAssetAddress):
                                          call multiAssetAddress.0x64ef212e with:
                                               gas gas_remaining - 50 wei
                                              args 0, 0, 10^17, symbol, 128, 5, mem[324]
                                          if ext_call.success:
                                              uint8(stor2.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  stop
                                              call caller with:
                                                 value 10^17 wei
                                                   gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  stop
                                  else:
                                      mem[356] = mem[383 len 5]
                                      if ext_code.size(multiAssetAddress):
                                          call multiAssetAddress.0x31c6c4cf with:
                                               gas gas_remaining - 50 wei
                                              args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                                          if ext_call.success:
                                              uint8(stor2.field_0) = 0
                                              if not ext_call.return_data[0]:
                                                  stop
                                              call caller with:
                                                 value 10^17 wei
                                                   gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  stop
                              else:
                                  call caller with:
                                     value call.value wei
                                       gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      if stor4[caller]:
                                          stop
                                      if tx.origin != caller:
                                          stop
                                      if eth.balance(caller) >= 10^16:
                                          stop
                                      if stor3[caller]:
                                          if caller != caller:
                                              if caller == tx.origin:
                                                  mem[324] = mem[351 len 5]
                                                  require ext_code.size(multiAssetAddress)
                                                  call multiAssetAddress.0x64ef212e with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                                              else:
                                                  mem[356] = mem[383 len 5]
                                                  require ext_code.size(multiAssetAddress)
                                                  call multiAssetAddress.0x31c6c4cf with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                                              require ext_call.success
                                              stop
                                      uint8(stor2.field_0) = 1
                                      if caller == tx.origin:
                                          mem[324] = mem[351 len 5]
                                          if ext_code.size(multiAssetAddress):
                                              call multiAssetAddress.0x64ef212e with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, 10^17, symbol, 128, 5, mem[324]
                                              if ext_call.success:
                                                  uint8(stor2.field_0) = 0
                                                  if not ext_call.return_data[0]:
                                                      stop
                                                  call caller with:
                                                     value 10^17 wei
                                                       gas gas_remaining - 34050 wei
                                                  if ext_call.success:
                                                      stop
                                      else:
                                          mem[356] = mem[383 len 5]
                                          if ext_code.size(multiAssetAddress):
                                              call multiAssetAddress.0x31c6c4cf with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                                              if ext_call.success:
                                                  uint8(stor2.field_0) = 0
                                                  if not ext_call.return_data[0]:
                                                      stop
                                                  call caller with:
                                                     value 10^17 wei
                                                       gas gas_remaining - 34050 wei
                                                  if ext_call.success:
                                                      stop
                  else:
                      uint8(stor2.field_0) = 1
                      if ext_code.size(multiAssetAddress):
                          call multiAssetAddress.reissueAsset(bytes32 symbol, uint256 value) with:
                               gas gas_remaining - 50 wei
                              args symbol, call.value - ext_call.return_data[0]
                          if ext_call.success:
                              uint8(stor2.field_0) = 0
                              if not ext_call.return_data[0]:
                                  call caller with:
                                     value call.value wei
                                       gas gas_remaining - 34050 wei
                                  if ext_call.success:
                                      if stor4[caller]:
                                          stop
                                      if tx.origin != caller:
                                          stop
                                      if eth.balance(caller) >= 10^16:
                                          stop
                                      if stor3[caller]:
                                          if caller != caller:
                                              if caller == tx.origin:
                                                  mem[324] = mem[351 len 5]
                                                  require ext_code.size(multiAssetAddress)
                                                  call multiAssetAddress.0x64ef212e with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                                              else:
                                                  mem[356] = mem[383 len 5]
                                                  require ext_code.size(multiAssetAddress)
                                                  call multiAssetAddress.0x31c6c4cf with:
                                                       gas gas_remaining - 50 wei
                                                      args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                                              require ext_call.success
                                              stop
                                      uint8(stor2.field_0) = 1
                                      if caller == tx.origin:
                                          mem[324] = mem[351 len 5]
                                          if ext_code.size(multiAssetAddress):
                                              call multiAssetAddress.0x64ef212e with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, 10^17, symbol, 128, 5, mem[324]
                                              if ext_call.success:
                                                  uint8(stor2.field_0) = 0
                                                  if not ext_call.return_data[0]:
                                                      stop
                                                  call caller with:
                                                     value 10^17 wei
                                                       gas gas_remaining - 34050 wei
                                                  if ext_call.success:
                                                      stop
                                      else:
                                          mem[356] = mem[383 len 5]
                                          if ext_code.size(multiAssetAddress):
                                              call multiAssetAddress.0x31c6c4cf with:
                                                   gas gas_remaining - 50 wei
                                                  args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                                              if ext_call.success:
                                                  uint8(stor2.field_0) = 0
                                                  if not ext_call.return_data[0]:
                                                      stop
                                                  call caller with:
                                                     value 10^17 wei
                                                       gas gas_remaining - 34050 wei
                                                  if ext_call.success:
                                                      stop
                              else:
                                  uint8(stor2.field_8) = 1
                                  if ext_code.size(multiAssetAddress):
                                      call multiAssetAddress.0x6e293817 with:
                                           gas gas_remaining - 50 wei
                                          args 0, 0, uint32(call.value), symbol, 128, 7, 'Deposit'
                                      if ext_call.success:
                                          uint8(stor2.field_8) = 0
                                          if ext_call.return_data[0]:
                                              if stor4[caller]:
                                                  stop
                                              if tx.origin != caller:
                                                  stop
                                              if eth.balance(caller) >= 10^16:
                                                  stop
                                              if stor3[caller]:
                                                  if caller != caller:
                                                      if caller == tx.origin:
                                                          mem[324] = mem[351 len 5]
                                                          require ext_code.size(multiAssetAddress)
                                                          call multiAssetAddress.0x64ef212e with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                                                      else:
                                                          mem[356] = mem[383 len 5]
                                                          require ext_code.size(multiAssetAddress)
                                                          call multiAssetAddress.0x31c6c4cf with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                                                      require ext_call.success
                                                      stop
                                              uint8(stor2.field_0) = 1
                                              if caller == tx.origin:
                                                  mem[324] = mem[351 len 5]
                                                  if ext_code.size(multiAssetAddress):
                                                      call multiAssetAddress.0x64ef212e with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, 10^17, symbol, 128, 5, mem[324]
                                                      if ext_call.success:
                                                          uint8(stor2.field_0) = 0
                                                          if not ext_call.return_data[0]:
                                                              stop
                                                          call caller with:
                                                             value 10^17 wei
                                                               gas gas_remaining - 34050 wei
                                                          if ext_call.success:
                                                              stop
                                              else:
                                                  mem[356] = mem[383 len 5]
                                                  if ext_code.size(multiAssetAddress):
                                                      call multiAssetAddress.0x31c6c4cf with:
                                                           gas gas_remaining - 50 wei
                                                          args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                                                      if ext_call.success:
                                                          uint8(stor2.field_0) = 0
                                                          if not ext_call.return_data[0]:
                                                              stop
                                                          call caller with:
                                                             value 10^17 wei
                                                               gas gas_remaining - 34050 wei
                                                          if ext_call.success:
                                                              stop
                                          else:
                                              call caller with:
                                                 value call.value wei
                                                   gas gas_remaining - 34050 wei
                                              if ext_call.success:
                                                  if stor4[caller]:
                                                      stop
                                                  if tx.origin != caller:
                                                      stop
                                                  if eth.balance(caller) >= 10^16:
                                                      stop
                                                  if stor3[caller]:
                                                      if caller != caller:
                                                          if caller == tx.origin:
                                                              mem[324] = mem[351 len 5]
                                                              require ext_code.size(multiAssetAddress)
                                                              call multiAssetAddress.0x64ef212e with:
                                                                   gas gas_remaining - 50 wei
                                                                  args 0, uint32(caller), 10^17, symbol, 128, 5, mem[324]
                                                          else:
                                                              mem[356] = mem[383 len 5]
                                                              require ext_code.size(multiAssetAddress)
                                                              call multiAssetAddress.0x31c6c4cf with:
                                                                   gas gas_remaining - 50 wei
                                                                  args 0, 0, uint32(caller), 10^17, symbol, 160, 5, mem[356]
                                                          require ext_call.success
                                                          stop
                                                  uint8(stor2.field_0) = 1
                                                  if caller == tx.origin:
                                                      mem[324] = mem[351 len 5]
                                                      if ext_code.size(multiAssetAddress):
                                                          call multiAssetAddress.0x64ef212e with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, 0, 10^17, symbol, 128, 5, mem[324]
                                                          if ext_call.success:
                                                              uint8(stor2.field_0) = 0
                                                              if not ext_call.return_data[0]:
                                                                  stop
                                                              call caller with:
                                                                 value 10^17 wei
                                                                   gas gas_remaining - 34050 wei
                                                              if ext_call.success:
                                                                  stop
                                                  else:
                                                      mem[356] = mem[383 len 5]
                                                      if ext_code.size(multiAssetAddress):
                                                          call multiAssetAddress.0x31c6c4cf with:
                                                               gas gas_remaining - 50 wei
                                                              args 0, 0, 0, 10^17, symbol, 160, 5, mem[356]
                                                          if ext_call.success:
                                                              uint8(stor2.field_0) = 0
                                                              if not ext_call.return_data[0]:
                                                                  stop
                                                              call caller with:
                                                                 value 10^17 wei
                                                                   gas gas_remaining - 34050 wei
                                                              if ext_call.success:
                                                                  stop
  revert 


