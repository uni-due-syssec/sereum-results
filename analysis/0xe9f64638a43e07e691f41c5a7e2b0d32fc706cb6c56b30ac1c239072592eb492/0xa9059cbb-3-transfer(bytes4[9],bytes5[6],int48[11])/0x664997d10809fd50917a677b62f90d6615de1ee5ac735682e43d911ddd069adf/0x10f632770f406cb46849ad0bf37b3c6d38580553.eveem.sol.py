# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x10f632770F406cb46849AD0bF37B3C6d38580553 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x23b872dd': 'transferFrom(address _from, address _to, uint256 _value)', '0x67fbd289': 'destroyTokens(uint256 _destroyAmount)', '0x827f32c0': 'generateTokens(address _holder, uint256 _amount)', '0xa9059cbb': 'transfer(address _to, uint256 _value)'} 

# storage definitions
def storage:
    # storage address 0
    controllerAddress # mask: a s
    # storage address 1
    name
    # storage address 2
    symbol
    # storage address 3
    decimals # mask: a s
    # storage address 4
    version
    # storage address 5
    maxSupply # mask: a s
    # storage address 6
    parentTokenAddress # mask: a s
    # storage address 7
    parentSnapShotBlock # mask: a s
    # storage address 8
    creationBlock # mask: a s
    # storage address 9
    stor9
    # storage address 10
    allowance
    # storage address 11
    stor11
    # storage address 12
    transfersEnabled # mask: a s
    # storage address 12
    unknowna43a43d7 # mask: a s
    # storage address 12
    stor12 # mask: a s
    # storage address 12
    tokenFactoryAddress # mask: a s
    # storage address 13
    foundationAddress # mask: a s
    # storage address 14
    arbiterAddress # mask: a s
    # storage address 15
    unknown47bf5d40
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 1]]]], ['loc', 1]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address _spender, uint256 _value): # not payable
  if not transfersEnabled:
      if foundationAddress != caller:
          require caller == controllerAddress
          require caller
          require ext_code.size(caller) > 0
  if _value:
      require not allowance[caller][addr(_spender)]
  if controllerAddress:
      if ext_code.size(controllerAddress) > 0:
          require ext_code.size(controllerAddress)
          call controllerAddress.onApprove(address param1, address param2, uint256 param3) with:
               gas gas_remaining wei
              args caller, addr(_spender), _value
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
  allowance[caller][addr(_spender)] = _value
  log Approval(
        address owner=_value,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x0b7f402c
# getter = None
# const = None
# payable = False
def unknown0b7f402c(array _param1, array _param2, uint8 _param3, uint256 _param4, bool _param5, bool _param6, addr _param7, addr _param8): # not payable
  mem[128 len _param1.length] = _param1[all]
  mem[ceil32(_param1.length) + 128] = _param2.length
  mem[ceil32(_param1.length) + 160 len _param2.length] = _param2[all]
  if foundationAddress != caller:
      if controllerAddress != caller:
          require caller == arbiterAddress
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 160] = 0xcc77d69300000000000000000000000000000000000000000000000000000000
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 484 len ceil32(_param1.length)] = _param1[all], mem[_param1.length + 128 len ceil32(_param1.length) - _param1.length]
  mem[_param1.length + ceil32(_param1.length) + ceil32(_param2.length) + 484] = _param2.length
  mem[_param1.length + ceil32(_param1.length) + ceil32(_param2.length) + 516 len ceil32(_param2.length)] = _param2[all], mem[ceil32(_param1.length) + _param2.length + 160 len ceil32(_param2.length) - _param2.length]
  if not _param4:
      if not _param2.length % 32:
          require ext_code.size(tokenFactoryAddress)
          call tokenFactoryAddress.0xcc77d693 with:
               gas gas_remaining wei
              args addr(this.address), block.number - 1, Array(len=_param1.length, data=Mask(8 * ceil32(_param1.length), -(8 * ceil32(_param1.length)) + 256, _param1[all], mem[_param1.length + 128 len ceil32(_param1.length) - _param1.length]) << (8 * ceil32(_param1.length)) - 256, mem[(2 * ceil32(_param1.length)) + ceil32(_param2.length) + 484 len _param2.length + _param1.length + -ceil32(_param1.length) + 32]), _param1.length + 320, _param3 << 248, _param5, _param6, addr(_param7), addr(_param8)
      else:
          mem[floor32(_param2.length) + _param1.length + ceil32(_param1.length) + ceil32(_param2.length) + 516] = mem[floor32(_param2.length) + _param1.length + ceil32(_param1.length) + ceil32(_param2.length) + -(_param2.length % 32) + 548 len _param2.length % 32]
          require ext_code.size(tokenFactoryAddress)
          call tokenFactoryAddress.0xcc77d693 with:
               gas gas_remaining wei
              args addr(this.address), block.number - 1, Array(len=_param1.length, data=Mask(8 * ceil32(_param1.length), -(8 * ceil32(_param1.length)) + 256, _param1[all], mem[_param1.length + 128 len ceil32(_param1.length) - _param1.length]) << (8 * ceil32(_param1.length)) - 256, mem[(2 * ceil32(_param1.length)) + ceil32(_param2.length) + 484 len floor32(_param2.length) + _param1.length + -ceil32(_param1.length) + 64]), _param1.length + 320, _param3 << 248, _param5, _param6, addr(_param7), addr(_param8)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).changeController(address newController) with:
           gas gas_remaining wei
          args caller
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log NewCloneToken(
            address cloneToken=(block.number - 1),
            uint256 snapshotBlock=addr(ext_call.return_data[0]))
  else:
      if not _param2.length % 32:
          require ext_code.size(tokenFactoryAddress)
          call tokenFactoryAddress.0xcc77d693 with:
               gas gas_remaining wei
              args addr(this.address), _param4, Array(len=_param1.length, data=Mask(8 * ceil32(_param1.length), -(8 * ceil32(_param1.length)) + 256, _param1[all], mem[_param1.length + 128 len ceil32(_param1.length) - _param1.length]) << (8 * ceil32(_param1.length)) - 256, mem[(2 * ceil32(_param1.length)) + ceil32(_param2.length) + 484 len _param2.length + _param1.length + -ceil32(_param1.length) + 32]), _param1.length + 320, _param3 << 248, _param5, _param6, addr(_param7), addr(_param8)
      else:
          mem[floor32(_param2.length) + _param1.length + ceil32(_param1.length) + ceil32(_param2.length) + 516] = mem[floor32(_param2.length) + _param1.length + ceil32(_param1.length) + ceil32(_param2.length) + -(_param2.length % 32) + 548 len _param2.length % 32]
          require ext_code.size(tokenFactoryAddress)
          call tokenFactoryAddress.0xcc77d693 with:
               gas gas_remaining wei
              args addr(this.address), _param4, Array(len=_param1.length, data=Mask(8 * ceil32(_param1.length), -(8 * ceil32(_param1.length)) + 256, _param1[all], mem[_param1.length + 128 len ceil32(_param1.length) - _param1.length]) << (8 * ceil32(_param1.length)) - 256, mem[(2 * ceil32(_param1.length)) + ceil32(_param2.length) + 484 len floor32(_param2.length) + _param1.length + -ceil32(_param1.length) + 64]), _param1.length + 320, _param3 << 248, _param5, _param6, addr(_param7), addr(_param8)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).changeController(address newController) with:
           gas gas_remaining wei
          args caller
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log NewCloneToken(
            address cloneToken=_param4,
            uint256 snapshotBlock=addr(ext_call.return_data[0]))
  return addr(ext_call.return_data[0])


# hash = 0x17634514
# getter = ['storage', 256, 0, 8]
# const = None
# payable = False
def creationBlock(): # not payable
  return creationBlock


# hash = 0x18160ddd
# getter = None
# const = None
# payable = False
def totalSupply(): # not payable
  if not stor11.length:
      if not parentTokenAddress:
          return 0
      require ext_code.size(parentTokenAddress)
      if block.number < parentSnapShotBlock:
          static call parentTokenAddress.totalSupplyAt(uint256 blockNumber) with:
                  gas gas_remaining wei
                 args block.number
      else:
          static call parentTokenAddress.totalSupplyAt(uint256 blockNumber) with:
                  gas gas_remaining wei
                 args parentSnapShotBlock
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return ext_call.return_data[0]
  require 0 < stor11.length
  if uint128(stor11.field_0) > block.number:
      if not parentTokenAddress:
          return 0
      require ext_code.size(parentTokenAddress)
      if block.number < parentSnapShotBlock:
          static call parentTokenAddress.totalSupplyAt(uint256 blockNumber) with:
                  gas gas_remaining wei
                 args block.number
      else:
          static call parentTokenAddress.totalSupplyAt(uint256 blockNumber) with:
                  gas gas_remaining wei
                 args parentSnapShotBlock
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return ext_call.return_data[0]
  if 0 == stor11.length:
      return 0
  mem[96] = 18
  mem[128] = 'MATH_SUB_UNDERFLOW'
  if 1 > stor11.length:
      revert with 0, 'MATH_SUB_UNDERFLOW'
  require stor11.length - 1 < stor11.length
  if block.number >= stor11[stor11.length].field_0:
      if 1 > stor11.length:
          revert with 0, 'MATH_SUB_UNDERFLOW'
      if stor11.length - 1 < stor11.length:
          return stor11[stor11.length].field_0
  else:
      if 0 < stor11.length:
          if block.number < uint128(stor11.field_0):
              return 0
          mem[64] = 224
          mem[160] = 18
          mem[192] = 'MATH_SUB_UNDERFLOW'
          if 1 > stor11.length:
              revert with 0, 'MATH_SUB_UNDERFLOW'
          [94ms = 0
          [94midx = 0
          while stor11.length - 1 > [94midx:
              [94m_103 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_103] = 17
              mem[[94m_103 + 32] = 'MATH_ADD_OVERFLOW'
              require [94midx + stor11.length / 2 < stor11.length
              mem[0] = 11
              if stor11[0.5 / [94midx + stor11.length].field_0 <= block.number:
                  [94ms = [94midx + stor11.length / 2
                  [94midx = [94midx + stor11.length / 2
                  continue 
              [94m_123 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_123] = 18
              mem[[94m_123 + 32] = 'MATH_SUB_UNDERFLOW'
              if 1 <= [94midx + stor11.length / 2:
                  [94ms = [94midx + stor11.length / 2
                  [94midx = [94midx
                  continue 
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 18
              mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
              [94midx = 32
              while [94midx < 18:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_123 + 32]
                  [94midx = [94midx + 32
                  continue 
              revert with 0, 'MATH_SUB_UNDERFLOW'
          if [94midx < stor11.length:
              return stor11[[94midx].field_128
  revert


# hash = 0x313ce567
# getter = ['storage', 8, 0, 3]
# const = None
# payable = False
def decimals(): # not payable
  return decimals


# hash = 0x383a18bc
# getter = None
# const = None
# payable = False
def unknown383a18bc(addr _param1, uint256 _param2): # not payable
  if foundationAddress != caller:
      if controllerAddress != caller:
          require caller == arbiterAddress
  require _param1
  if _param2 != 'foundation':
      if _param2 != 'controller':
          require _param2 == 'arbiter'
  if not unknown47bf5d40[_param2].field_416:
      return 0
  if caller == unknown47bf5d40[_param2].field_0:
      return 0
  if unknown47bf5d40[_param2].field_256 != _param1:
      return 0
  unknown47bf5d40[_param2].field_416 = 0
  if sha3(_param2) == sha3('foundation'):
      foundationAddress = _param1
  else:
      if sha3(_param2) == sha3('arbiter'):
          arbiterAddress = _param1
      else:
          if sha3(_param2) == sha3('controller'):
              controllerAddress = _param1
  return 1


# hash = 0x3cebb823
# getter = None
# const = None
# payable = False
def changeController(address _newController): # not payable
  require caller == controllerAddress
  require _newController
  require _newController != caller
  controllerAddress = _newController


# hash = 0x41fbb050
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def foundation(): # not payable
  return foundationAddress


# hash = 0x47bf5d40
# getter = ['struct', ['loc', 15]]
# const = None
# payable = False
def unknown47bf5d40(uint256 _param1): # not payable
  return unknown47bf5d40[_param1].field_0, unknown47bf5d40[_param1].field_256, bool(unknown47bf5d40[_param1].field_416)


# hash = 0x4ee2cd7e
# getter = None
# const = None
# payable = False
def balanceOfAt(address _owner, uint256 _blockNumber): # not payable
  if not stor9[addr(_owner)].field_0:
      if not parentTokenAddress:
          return 0
      require ext_code.size(parentTokenAddress)
      if _blockNumber < parentSnapShotBlock:
          static call parentTokenAddress.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args addr(_owner), _blockNumber
      else:
          static call parentTokenAddress.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args addr(_owner), parentSnapShotBlock
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return ext_call.return_data[0]
  require 0 < stor9[addr(_owner)].field_0
  if stor9[addr(_owner)].field_0 > _blockNumber:
      if not parentTokenAddress:
          return 0
      require ext_code.size(parentTokenAddress)
      if _blockNumber < parentSnapShotBlock:
          static call parentTokenAddress.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args addr(_owner), _blockNumber
      else:
          static call parentTokenAddress.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args addr(_owner), parentSnapShotBlock
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return ext_call.return_data[0]
  mem[32] = 9
  if 0 == stor9[addr(_owner)].field_0:
      return 0
  mem[96] = 18
  mem[128] = 'MATH_SUB_UNDERFLOW'
  if 1 > stor9[addr(_owner)].field_0:
      revert with 0, 'MATH_SUB_UNDERFLOW'
  require stor9[addr(_owner)].field_0 - 1 < stor9[addr(_owner)].field_0
  if _blockNumber >= stor9[addr(_owner)][stor9[addr(_owner)].field_0].field_0:
      if 1 > stor9[addr(_owner)].field_0:
          revert with 0, 'MATH_SUB_UNDERFLOW'
      if stor9[addr(_owner)].field_0 - 1 < stor9[addr(_owner)].field_0:
          return stor9[addr(_owner)][stor9[addr(_owner)].field_0].field_0
  else:
      if 0 < stor9[addr(_owner)].field_0:
          if _blockNumber < stor9[addr(_owner)].field_0:
              return 0
          mem[64] = 224
          mem[160] = 18
          mem[192] = 'MATH_SUB_UNDERFLOW'
          if 1 > stor9[addr(_owner)].field_0:
              revert with 0, 'MATH_SUB_UNDERFLOW'
          [94ms = 0
          [94midx = 0
          while stor9[addr(_owner)].field_0 - 1 > [94midx:
              [94m_106 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_106] = 17
              mem[[94m_106 + 32] = 'MATH_ADD_OVERFLOW'
              require [94midx + stor9[addr(_owner)].field_0 / 2 < stor9[addr(_owner)].field_0
              mem[0] = sha3(addr(_owner), 9)
              if stor9[addr(_owner)][0.5 / [94midx + stor9[addr(_owner)].field_0].field_0 <= _blockNumber:
                  [94ms = [94midx + stor9[addr(_owner)].field_0 / 2
                  [94midx = [94midx + stor9[addr(_owner)].field_0 / 2
                  continue 
              [94m_126 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_126] = 18
              mem[[94m_126 + 32] = 'MATH_SUB_UNDERFLOW'
              if 1 <= [94midx + stor9[addr(_owner)].field_0 / 2:
                  [94ms = [94midx + stor9[addr(_owner)].field_0 / 2
                  [94midx = [94midx
                  continue 
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 18
              mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
              [94midx = 32
              while [94midx < 18:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_126 + 32]
                  [94midx = [94midx + 32
                  continue 
              revert with 0, 'MATH_SUB_UNDERFLOW'
          if [94midx < stor9[addr(_owner)].field_0:
              return stor9[addr(_owner)][[94midx].field_128
  revert


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = False
def version(): # not payable
  return version[0 len version.length]


# hash = 0x70a08231
# getter = None
# const = None
# payable = False
def balanceOf(address _owner): # not payable
  if not stor9[addr(_owner)].field_0:
      if not parentTokenAddress:
          return 0
      require ext_code.size(parentTokenAddress)
      if block.number < parentSnapShotBlock:
          static call parentTokenAddress.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args addr(_owner), block.number
      else:
          static call parentTokenAddress.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args addr(_owner), parentSnapShotBlock
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return ext_call.return_data[0]
  require 0 < stor9[addr(_owner)].field_0
  if stor9[addr(_owner)].field_0 > block.number:
      if not parentTokenAddress:
          return 0
      require ext_code.size(parentTokenAddress)
      if block.number < parentSnapShotBlock:
          static call parentTokenAddress.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args addr(_owner), block.number
      else:
          static call parentTokenAddress.balanceOfAt(address owner, uint256 blockNumber) with:
                  gas gas_remaining wei
                 args addr(_owner), parentSnapShotBlock
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return ext_call.return_data[0]
  mem[32] = 9
  if 0 == stor9[addr(_owner)].field_0:
      return 0
  mem[96] = 18
  mem[128] = 'MATH_SUB_UNDERFLOW'
  if 1 > stor9[addr(_owner)].field_0:
      revert with 0, 'MATH_SUB_UNDERFLOW'
  require stor9[addr(_owner)].field_0 - 1 < stor9[addr(_owner)].field_0
  if block.number >= stor9[addr(_owner)][stor9[addr(_owner)].field_0].field_0:
      if 1 > stor9[addr(_owner)].field_0:
          revert with 0, 'MATH_SUB_UNDERFLOW'
      if stor9[addr(_owner)].field_0 - 1 < stor9[addr(_owner)].field_0:
          return stor9[addr(_owner)][stor9[addr(_owner)].field_0].field_0
  else:
      if 0 < stor9[addr(_owner)].field_0:
          if block.number < stor9[addr(_owner)].field_0:
              return 0
          mem[64] = 224
          mem[160] = 18
          mem[192] = 'MATH_SUB_UNDERFLOW'
          if 1 > stor9[addr(_owner)].field_0:
              revert with 0, 'MATH_SUB_UNDERFLOW'
          [94ms = 0
          [94midx = 0
          while stor9[addr(_owner)].field_0 - 1 > [94midx:
              [94m_106 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_106] = 17
              mem[[94m_106 + 32] = 'MATH_ADD_OVERFLOW'
              require [94midx + stor9[addr(_owner)].field_0 / 2 < stor9[addr(_owner)].field_0
              mem[0] = sha3(addr(_owner), 9)
              if stor9[addr(_owner)][0.5 / [94midx + stor9[addr(_owner)].field_0].field_0 <= block.number:
                  [94ms = [94midx + stor9[addr(_owner)].field_0 / 2
                  [94midx = [94midx + stor9[addr(_owner)].field_0 / 2
                  continue 
              [94m_126 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_126] = 18
              mem[[94m_126 + 32] = 'MATH_SUB_UNDERFLOW'
              if 1 <= [94midx + stor9[addr(_owner)].field_0 / 2:
                  [94ms = [94midx + stor9[addr(_owner)].field_0 / 2
                  [94midx = [94midx
                  continue 
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 18
              mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
              [94midx = 32
              while [94midx < 18:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_126 + 32]
                  [94midx = [94midx + 32
                  continue 
              revert with 0, 'MATH_SUB_UNDERFLOW'
          if [94midx < stor9[addr(_owner)].field_0:
              return stor9[addr(_owner)][[94midx].field_128
  revert


# hash = 0x748f6184
# getter = None
# const = None
# payable = False
def unknown748f6184(addr _param1, uint256 _param2): # not payable
  if foundationAddress != caller:
      if controllerAddress != caller:
          require caller == arbiterAddress
  require _param1
  if _param2 != 'foundation':
      if _param2 != 'controller':
          require _param2 == 'arbiter'
  unknown47bf5d40[_param2].field_0 = caller
  unknown47bf5d40[_param2].field_256 = _param1
  unknown47bf5d40[_param2].field_416 = 1


# hash = 0x80a54001
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def parentToken(): # not payable
  return parentTokenAddress


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 2]]]], ['loc', 2]]]
# const = None
# payable = False
def symbol(): # not payable
  return symbol[0 len symbol.length]


# hash = 0x981b24d0
# getter = None
# const = None
# payable = False
def totalSupplyAt(uint256 _blockNumber): # not payable
  if not stor11.length:
      if not parentTokenAddress:
          return 0
      require ext_code.size(parentTokenAddress)
      if _blockNumber < parentSnapShotBlock:
          static call parentTokenAddress.totalSupplyAt(uint256 blockNumber) with:
                  gas gas_remaining wei
                 args _blockNumber
      else:
          static call parentTokenAddress.totalSupplyAt(uint256 blockNumber) with:
                  gas gas_remaining wei
                 args parentSnapShotBlock
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return ext_call.return_data[0]
  require 0 < stor11.length
  if uint128(stor11.field_0) > _blockNumber:
      if not parentTokenAddress:
          return 0
      require ext_code.size(parentTokenAddress)
      if _blockNumber < parentSnapShotBlock:
          static call parentTokenAddress.totalSupplyAt(uint256 blockNumber) with:
                  gas gas_remaining wei
                 args _blockNumber
      else:
          static call parentTokenAddress.totalSupplyAt(uint256 blockNumber) with:
                  gas gas_remaining wei
                 args parentSnapShotBlock
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return ext_call.return_data[0]
  if 0 == stor11.length:
      return 0
  mem[96] = 18
  mem[128] = 'MATH_SUB_UNDERFLOW'
  if 1 > stor11.length:
      revert with 0, 'MATH_SUB_UNDERFLOW'
  require stor11.length - 1 < stor11.length
  if _blockNumber >= stor11[stor11.length].field_0:
      if 1 > stor11.length:
          revert with 0, 'MATH_SUB_UNDERFLOW'
      if stor11.length - 1 < stor11.length:
          return stor11[stor11.length].field_0
  else:
      if 0 < stor11.length:
          if _blockNumber < uint128(stor11.field_0):
              return 0
          mem[64] = 224
          mem[160] = 18
          mem[192] = 'MATH_SUB_UNDERFLOW'
          if 1 > stor11.length:
              revert with 0, 'MATH_SUB_UNDERFLOW'
          [94ms = 0
          [94midx = 0
          while stor11.length - 1 > [94midx:
              [94m_103 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_103] = 17
              mem[[94m_103 + 32] = 'MATH_ADD_OVERFLOW'
              require [94midx + stor11.length / 2 < stor11.length
              mem[0] = 11
              if stor11[0.5 / [94midx + stor11.length].field_0 <= _blockNumber:
                  [94ms = [94midx + stor11.length / 2
                  [94midx = [94midx + stor11.length / 2
                  continue 
              [94m_123 = mem[64]
              mem[64] = mem[64] + 64
              mem[[94m_123] = 18
              mem[[94m_123 + 32] = 'MATH_SUB_UNDERFLOW'
              if 1 <= [94midx + stor11.length / 2:
                  [94ms = [94midx + stor11.length / 2
                  [94midx = [94midx
                  continue 
              mem[mem[64]] = 0x8c379a000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 32
              mem[mem[64] + 36] = 18
              mem[mem[64] + 68] = 'MATH_SUB_UNDERFLOW'
              [94midx = 32
              while [94midx < 18:
                  mem[[94midx + mem[64] + 68] = mem[[94midx + [94m_123 + 32]
                  [94midx = [94midx + 32
                  continue 
              revert with 0, 'MATH_SUB_UNDERFLOW'
          if [94midx < stor11.length:
              return stor11[[94midx].field_128
  revert


# hash = 0xa43a43d7
# getter = ['bool', ['storage', 8, 0, 12]]
# const = None
# payable = False
def unknowna43a43d7(): # not payable
  return bool(unknowna43a43d7)


# hash = 0xb0c74210
# getter = None
# const = None
# payable = False
def unknownb0c74210(bool _param1): # not payable
  require controllerAddress != caller
  if foundationAddress != caller:
      require caller == arbiterAddress
  unknowna43a43d7 = uint8(_param1)


# hash = 0xbef97c87
# getter = ['bool', ['storage', 8, 8, 12]]
# const = None
# payable = False
def transfersEnabled(): # not payable
  return bool(transfersEnabled)


# hash = 0xc5bcc4f1
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def parentSnapShotBlock(): # not payable
  return parentSnapShotBlock


# hash = 0xcae9ca51
# getter = None
# const = None
# payable = False
def approveAndCall(address _spender, uint256 _value, bytes _extraData): # not payable
  if not transfersEnabled:
      if foundationAddress != caller:
          require caller == controllerAddress
          require caller
          require ext_code.size(caller) > 0
  if _value:
      require not allowance[caller][addr(_spender)]
  if controllerAddress:
      if ext_code.size(controllerAddress) > 0:
          require ext_code.size(controllerAddress)
          call controllerAddress.onApprove(address param1, address param2, uint256 param3) with:
               gas gas_remaining wei
              args caller, addr(_spender), _value
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
  allowance[caller][addr(_spender)] = _value
  log Approval(
        address owner=_value,
        address spender=caller,
        uint256 value=_spender)
  require ext_code.size(_spender)
  call _spender.receiveApproval(address sender, uint256 amount, address tokenAddress, bytes bytes) with:
       gas gas_remaining wei
      args caller, _value, this.address, Array(len=_extraData.length, data=_extraData[all])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0xd5abeb01
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def maxSupply(): # not payable
  return maxSupply


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 10]]]]]
# const = None
# payable = False
def allowance(address _owner, address _spender): # not payable
  return allowance[addr(_owner)][addr(_spender)]


# hash = 0xdf8de3e7
# getter = None
# const = None
# payable = False
def claimTokens(address _token): # not payable
  require caller == controllerAddress
  require controllerAddress
  require ext_code.size(controllerAddress) > 0
  if not _token:
      call controllerAddress with:
         value eth.balance(this.address) wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  else:
      require ext_code.size(_token)
      static call _token.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(_token)
      call _token.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args controllerAddress, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      log ClaimedTokens(
            address token=ext_call.return_data[0],
            address controller=_token,
            uint256 amount=controllerAddress)


# hash = 0xe77772fe
# getter = ['storage', 160, 16, 12]
# const = None
# payable = False
def tokenFactory(): # not payable
  return tokenFactoryAddress


# hash = 0xf41e60c5
# getter = None
# const = None
# payable = False
def enableTransfers(bool _transfersEnabled): # not payable
  require caller == controllerAddress
  require unknowna43a43d7
  stor12 = Mask(248, 0, _transfersEnabled)
  return 1


# hash = 0xf77c4791
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def controller(): # not payable
  return controllerAddress


# hash = 0xfe25e00a
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def arbiter(): # not payable
  return arbiterAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  require controllerAddress
  require ext_code.size(controllerAddress) > 0
  require ext_code.size(controllerAddress)
  call controllerAddress.proxyPayment(address param1) with:
     value call.value wei
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]


