# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xef5dCfd29f24F0148DA839e050f3F7cbFA56b7b8 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x107556fd': 'unknown107556fd(?)', '0x1aaeebe3': 'unknown1aaeebe3(?)', '0x70a08231': 'balanceOf(address _owner)', '0x733480b7': 'transferToICAP(bytes32 _icap, uint256 _value)', '0x77fe38a4': 'transferToICAPWithReference(bytes32 _icap, uint256 _value, string _reference)', '0xa9059cbb': 'transfer(address _to, uint256 _value)', '0xac35caee': 'transferWithReference(address _to, uint256 _value, string _reference)', '0xdae04fa2': 'unknowndae04fa2(?)', '0xf0149751': 'unknownf0149751(?)'} 

# storage definitions
def storage:
    # storage address 0
    contractOwner # mask: a s
    # storage address 1
    unknown16318a6e
    # storage address 2
    startTime # mask: a s
    # storage address 3
    symbol
# hash = 0x029a8bf7
# getter = None
# const = None
# payable = False
def multiAsset(): # not payable
  require ext_code.size(unknown16318a6e[stor3[caller]].field_0)
  call unknown16318a6e[stor3[caller]].field_0.multiAsset() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  return ext_call.return_data[12 len 20]


# hash = 0x149b4bc1
# getter = None
# const = None
# payable = False
def unknown149b4bc1(uint256 _param1, uint256 _param2): # not payable
  if contractOwner != caller:
      return 0
  require ext_code.size(unknown16318a6e[stor3[caller]].field_0)
  call unknown16318a6e[stor3[caller]].field_0.multiAsset() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).registryICAP() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).assets(bytes32 param1) with:
       gas gas_remaining - 50 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
  require ext_call.success
  require ext_code.size(unknown16318a6e[ext_call.return_data[0]].field_0)
  if not unknown16318a6e[ext_call.return_data[0]].field_1536:
      call unknown16318a6e[ext_call.return_data[0]].field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
           gas gas_remaining - 9050 wei
          args _param1, _param2, 96, 0
  else:
      call unknown16318a6e[ext_call.return_data[0]].field_0.balanceOf(address owner) with:
           gas gas_remaining - 50 wei
          args this.address
      require ext_call.success
      require ext_code.size(unknown16318a6e[ext_call.return_data[0]].field_0)
      if ext_call.return_data[0] >= _param2:
          call unknown16318a6e[ext_call.return_data[0]].field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
               gas gas_remaining - 9050 wei
              args _param1, _param2, 96, 0
      else:
          call unknown16318a6e[ext_call.return_data[0]].field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
             value eth.balance(this.address) wei
               gas gas_remaining - 9050 wei
              args _param1, _param2, 96, 0
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  log 0x73d7feb5: _param2, 64, 0, caller, _param1
  return 1


# hash = 0x15070401
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, 'caller'], 3]]]
# const = None
# payable = False
def getSymbol(): # not payable
  return symbol[caller]


# hash = 0x16318a6e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], ['add', 4, ['sha3', ['data', ['cd', 36], 1]]]]]]
# const = None
# payable = False
def unknown16318a6e(uint256 _param1, uint256 _param2): # not payable
  return unknown16318a6e[_param2][4][_param1].field_0


# hash = 0x1e52dec8
# getter = None
# const = None
# payable = False
def unknown1e52dec8(addr _param1, uint256 _param2, uint256 _param3): # not payable
  if contractOwner != caller:
      return 0
  require ext_code.size(unknown16318a6e[_param3].field_0)
  if not unknown16318a6e[_param3].field_1536:
      call unknown16318a6e[_param3].field_0.transferWithReference(address to, uint256 value, string reference) with:
           gas gas_remaining - 9050 wei
          args addr(_param1), _param2, 96, 0
  else:
      call unknown16318a6e[_param3].field_0.balanceOf(address owner) with:
           gas gas_remaining - 50 wei
          args this.address
      require ext_call.success
      require ext_code.size(unknown16318a6e[_param3].field_0)
      if ext_call.return_data[0] >= _param2:
          call unknown16318a6e[_param3].field_0.transferWithReference(address to, uint256 value, string reference) with:
               gas gas_remaining - 9050 wei
              args addr(_param1), _param2, 96, 0
      else:
          call unknown16318a6e[_param3].field_0.transferWithReference(address to, uint256 value, string reference) with:
             value eth.balance(this.address) wei
               gas gas_remaining - 9050 wei
              args addr(_param1), _param2, 96, 0
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  log 0xae7443dd: _param2, 64, 0, caller, _param1, _param3
  return 1


# hash = 0x274a6c2b
# getter = None
# const = None
# payable = False
def unknown274a6c2b(uint256 _param1, uint256 _param2, uint256 _param3, uint256 _param4): # not payable
  if contractOwner != caller:
      return 0
  unknown16318a6e[_param4][5][_param2 - _param3 % 24 * 3600 / 2 * 3600].field_0 += _param1
  return 1


# hash = 0x387309ce
# getter = None
# const = ['return', 12]
# payable = False
const unknown387309ce = 12


# hash = 0x3dd7f552
# getter = None
# const = None
# payable = False
def unknown3dd7f552(uint256 _param1, uint256 _param2, array _param3): # not payable
  if contractOwner != caller:
      return 0
  require ext_code.size(unknown16318a6e[stor3[caller]].field_0)
  call unknown16318a6e[stor3[caller]].field_0.multiAsset() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).registryICAP() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).assets(bytes32 param1) with:
       gas gas_remaining - 50 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
  require ext_call.success
  require ext_code.size(unknown16318a6e[ext_call.return_data[0]].field_0)
  if not unknown16318a6e[ext_call.return_data[0]].field_1536:
      call unknown16318a6e[ext_call.return_data[0]].field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
           gas gas_remaining - 9050 wei
          args _param1, _param2, Array(len=_param3.length, data=_param3[all])
  else:
      call unknown16318a6e[ext_call.return_data[0]].field_0.balanceOf(address owner) with:
           gas gas_remaining - 50 wei
          args this.address
      require ext_call.success
      require ext_code.size(unknown16318a6e[ext_call.return_data[0]].field_0)
      if ext_call.return_data[0] >= _param2:
          call unknown16318a6e[ext_call.return_data[0]].field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
               gas gas_remaining - 9050 wei
              args _param1, _param2, Array(len=_param3.length, data=_param3[all])
      else:
          call unknown16318a6e[ext_call.return_data[0]].field_0.transferToICAPWithReference(bytes32 icap, uint256 value, string reference) with:
             value eth.balance(this.address) wei
               gas gas_remaining - 9050 wei
              args _param1, _param2, Array(len=_param3.length, data=_param3[all])
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  log 0x73d7feb5: _param2, Array(len=_param3.length, data=_param3[all]), caller, _param1
  return 1


# hash = 0x4ba79dfe
# getter = None
# const = None
# payable = False
def removeAddress(address _remAddress): # not payable
  if contractOwner != caller:
      return 0
  symbol[addr(_remAddress)] = 0
  return 1


# hash = 0x57a12ae5
# getter = None
# const = None
# payable = False
def unknown57a12ae5(addr _param1, uint256 _param2): # not payable
  if contractOwner != caller:
      return 0
  if not unknown16318a6e[_param2].field_1544:
      return 0
  symbol[addr(_param1)] = _param2
  return 1


# hash = 0x5d68c8f5
# getter = None
# const = None
# payable = False
def unknown5d68c8f5(uint256 _param1, uint256 _param2): # not payable
  if contractOwner != caller:
      return 0
  unknown16318a6e[_param2][5][block.timestamp - stor2 % 24 * 3600 / 2 * 3600].field_0 += _param1
  return 1


# hash = 0x6effec50
# getter = None
# const = None
# payable = True
def unknown6effec50(addr _param1, uint256 _param2, array _param3) payable: 
  mem[128 len _param3.length] = _param3[all]
  if contractOwner != caller:
      return 0
  mem[ceil32(_param3.length) + 128 len _param3.length] = _param3[all]
  if not _param3.length % 32:
      call _param1 with:
         value _param2 wei
           gas gas_remaining - 34050 wei
          args _param3[all]
  else:
      mem[floor32(_param3.length) + ceil32(_param3.length) + 128] = mem[floor32(_param3.length) + ceil32(_param3.length) + -(_param3.length % 32) + 160 len _param3.length % 32]
      call _param1.mem[ceil32(_param3.length) + 128 len 4] with:
         value _param2 wei
           gas gas_remaining - 34050 wei
          args mem[ceil32(_param3.length) + 132 len floor32(_param3.length) + 28]
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
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 3]]]
# const = None
# payable = False
def access(address _addr): # not payable
  return symbol[_addr]


# hash = 0x78e97925
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def startTime(): # not payable
  return startTime


# hash = 0x7e7c0c20
# getter = None
# const = None
# payable = False
def unknown7e7c0c20(addr _param1, uint256 _param2, uint8 _param3): # not payable
  if contractOwner != caller:
      return 0
  require ext_code.size(_param1)
  call _param1.symbol() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  if unknown16318a6e[ext_call.return_data[0]].field_0:
      return 0
  require ext_code.size(_param1)
  call _param1.multiAsset() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  if not ext_call.return_data[12 len 20]:
      return 0
  require ext_code.size(_param1)
  call _param1.multiAsset() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).isCreated(bytes32 symbol) with:
       gas gas_remaining - 50 wei
      args ext_call.return_data[0]
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  require ext_code.size(_param1)
  call _param1.multiAsset() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).0x8180f2fc with:
       gas gas_remaining - 50 wei
      args addr(_param1), -1, ext_call.return_data[0]
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  unknown16318a6e[ext_call.return_data[0]].field_0 = _param1
  unknown16318a6e[ext_call.return_data[0]].field_256 = _param2
  unknown16318a6e[ext_call.return_data[0]].field_512 = block.timestamp - startTime % 24 * 3600 / 2 * 3600
  unknown16318a6e[ext_call.return_data[0]].field_768 = block.timestamp
  unknown16318a6e[ext_call.return_data[0]].field_1536 = _param3
  unknown16318a6e[ext_call.return_data[0]].field_1544 = 1
  return 1


# hash = 0x84691767
# getter = None
# const = None
# payable = False
def unknown84691767(uint256 _param1): # not payable
  if contractOwner != caller:
      return 0
  startTime = _param1
  return 1


# hash = 0x8966fa49
# getter = None
# const = None
# payable = False
def unknown8966fa49(uint256 _param1, uint256 _param2, uint8 _param3, uint8 _param4): # not payable
  if contractOwner != caller:
      return 0
  if not unknown16318a6e[_param1].field_0:
      return 0
  unknown16318a6e[_param1].field_256 = _param2
  unknown16318a6e[_param1].field_1536 = _param3
  unknown16318a6e[_param1].field_1544 = _param4
  return 1


# hash = 0x8af07bfa
# getter = None
# const = None
# payable = False
def unknown8af07bfa(addr _param1, uint256 _param2, uint256 _param3, array _param4): # not payable
  if contractOwner != caller:
      return 0
  require ext_code.size(unknown16318a6e[_param3].field_0)
  if not unknown16318a6e[_param3].field_1536:
      call unknown16318a6e[_param3].field_0.transferWithReference(address to, uint256 value, string reference) with:
           gas gas_remaining - 9050 wei
          args addr(_param1), _param2, Array(len=_param4.length, data=_param4[all])
  else:
      call unknown16318a6e[_param3].field_0.balanceOf(address owner) with:
           gas gas_remaining - 50 wei
          args this.address
      require ext_call.success
      require ext_code.size(unknown16318a6e[_param3].field_0)
      if ext_call.return_data[0] >= _param2:
          call unknown16318a6e[_param3].field_0.transferWithReference(address to, uint256 value, string reference) with:
               gas gas_remaining - 9050 wei
              args addr(_param1), _param2, Array(len=_param4.length, data=_param4[all])
      else:
          call unknown16318a6e[_param3].field_0.transferWithReference(address to, uint256 value, string reference) with:
             value eth.balance(this.address) wei
               gas gas_remaining - 9050 wei
              args addr(_param1), _param2, Array(len=_param4.length, data=_param4[all])
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  log 0xae7443dd: _param2, Array(len=_param4.length, data=_param4[all]), caller, _param1, _param3
  return 1


# hash = 0x8d2ffdc9
# getter = None
# const = None
# payable = False
def unknown8d2ffdc9(uint256 _param1): # not payable
  require ext_code.size(unknown16318a6e[stor3[caller]].field_0)
  call unknown16318a6e[stor3[caller]].field_0.multiAsset() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).registryICAP() with:
       gas gas_remaining - 50 wei
  require ext_call.success
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).assets(bytes32 param1) with:
       gas gas_remaining - 50 wei
      args sha3(Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 4) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 5) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256, Mask(8, -(('mask_shl', 256, 0, -3, ('param', '_param1')), 0) + 256, 6) << (('mask_shl', 256, 0, -3, ('param', '_param1')), 0) - 256)
  require ext_call.success
  return ext_call.return_data[0]


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, 'caller'], 3]]]
# const = None
# payable = False
def symbol(): # not payable
  return symbol[caller]


# hash = 0x9fb2f43b
# getter = None
# const = ['return', 7200]
# payable = False
const unknown9fb2f43b = (2 * 3600)


# hash = 0x9fda5b66
# getter = ['struct', ['loc', 1]]
# const = None
# payable = False
def assets(bytes32 _param1): # not payable
  return unknown16318a6e[_param1].field_0, 
         unknown16318a6e[_param1].field_256,
         unknown16318a6e[_param1].field_512,
         unknown16318a6e[_param1].field_768,
         bool(unknown16318a6e[_param1].field_1536),
         bool(unknown16318a6e[_param1].field_1544)


# hash = 0xce606ee0
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def contractOwner(): # not payable
  return contractOwner


# hash = 0xd2e646d2
# getter = None
# const = None
# payable = False
def unknownd2e646d2(uint256 _param1, uint256 _param2): # not payable
  return (_param1 - _param2 % 24 * 3600 / 2 * 3600)


# hash = 0xd613be0a
# getter = None
# const = None
# payable = False
def forceChangeContractOwnership(address _to): # not payable
  if contractOwner != caller:
      return 0
  contractOwner = _to
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


