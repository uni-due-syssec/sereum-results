# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x68C769478002B2E2Db64fE3Be55C943fE4Fbd6b1 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x733480b7': 'transferToICAP(bytes32 _icap, uint256 _value)', '0x77fe38a4': 'transferToICAPWithReference(bytes32 _icap, uint256 _value, string _reference)', '0xa48a663c': 'transferFromToICAPWithReference(address _from, bytes32 _icap, uint256 _value, string _reference)', '0xa525f42c': 'transferFromToICAP(address _from, bytes32 _icap, uint256 _value)', '0xc5487661': 'unknownc5487661(?)', '0xea98e540': 'unknownea98e540(?)'} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 0
    stor0 # mask: a s
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1
    # storage address 2
    stor2
    # storage address 3
    stor3
    # storage address 4
    stor4
    # storage address 5
    owner
    # storage address 6
    holderId
    # storage address 7
    allowance
    # storage address 8
    proxies
    # storage address 9
    registryICAPAddress # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 10
    stor10 # mask: a s
    # storage address 10
    eventsHistoryAddress # mask: a s
    # storage address 11
    unknown4d1d2dbe
# hash = 0x02571be3
# getter = ['storage', 160, 0, ['add', 1, ['sha3', ['data', ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 7]]], 5]]]]
# const = None
# payable = True
def owner(bytes32 _symbol) payable: 
  return addr(owner[uint256(stor7[_symbol].field_0)].field_256)


# hash = 0x02927d20
# getter = None
# const = None
# payable = True
def setupEventsHistory(address _eventsHistory) payable: 
  if addr(stor1.length) != caller:
      return 0
  if addr(eventsHistoryAddress) != 0:
      return 0
  uint256(stor10) = _eventsHistory or Mask(96, 160, uint256(stor10))
  return 1


# hash = 0x0610e037
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = True
def isEnabled(bytes32 _switch) payable: 
  return bool(uint8(stor3[_switch]))


# hash = 0x06489899
# getter = None
# const = None
# payable = True
def unknown06489899(addr _param1, uint256 _param2, uint256 _param3) payable: 
  if addr(unknown4d1d2dbe[stor6[caller]][_param3]):
      call addr(unknown4d1d2dbe[stor6[caller]][_param3]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], holderId[caller])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
      else:
          if uint256(allowance[_param3].field_0):
              if uint256(allowance[_param3].field_0) == holderId[caller]:
                  uint256(proxies[_param3][1][addr(_param1)].field_0) = _param2 or Mask(248, 8, uint256(proxies[_param3][1][addr(_param1)].field_0))
                  return 1
  else:
      if not addr(unknown4d1d2dbe[stor6[caller]]):
          if uint256(allowance[_param3].field_0):
              if uint256(allowance[_param3].field_0) == holderId[caller]:
                  uint256(proxies[_param3][1][addr(_param1)].field_0) = _param2 or Mask(248, 8, uint256(proxies[_param3][1][addr(_param1)].field_0))
                  return 1
      else:
          call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
          else:
              if uint256(allowance[_param3].field_0):
                  if uint256(allowance[_param3].field_0) == holderId[caller]:
                      uint256(proxies[_param3][1][addr(_param1)].field_0) = _param2 or Mask(248, 8, uint256(proxies[_param3][1][addr(_param1)].field_0))
                      return 1
  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
       gas gas_remaining - 25050 wei
      args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
  require ext_call.success
  return 0


# hash = 0x085a4705
# getter = None
# const = None
# payable = True
def issueAsset(bytes32 _symbol, uint256 _value, string _name, string _description, uint8 _baseUnit, bool _isReissuable) payable: 
  if not uint8(stor3[_symbol][uint8(_isReissuable)][0]):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x466561747572652069732064697361626c6564000000000000000000000000
      require ext_call.success
      return 0
  if 0 == _value:
      if not _isReissuable:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot issue 0 value fixed asset'
          require ext_call.success
          return 0
  if uint256(allowance[_symbol].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Asset already issued'
      require ext_call.success
      return 0
  if holderId[caller] != 0:
      uint256(allowance[_symbol].field_0) = holderId[caller]
      uint256(allowance[_symbol].field_256) = _value
      uint256(allowance[_symbol][2][].field_0) = Array(len=_name.length, data=_name[all])
      uint256(allowance[_symbol][3][].field_0) = Array(len=_description.length, data=_description[all])
      uint8(allowance[_symbol].field_1024) = uint8(_isReissuable)
      Mask(248, 0, allowance[_symbol].field_1032) = Mask(248, 0, _baseUnit)
      Mask(240, 0, allowance[_symbol].field_1040) = Mask(240, 16, _isReissuable) >> 16
      uint256(allowance[_symbol][5][stor6[caller]].field_0) = _value
      call addr(eventsHistoryAddress).emitIssue(bytes32 symbol, uint256 value, address by) with:
           gas gas_remaining - 25050 wei
          args _symbol, _value, addr(owner[stor6[caller]].field_256)
  else:
      stor4.length++
      addr(owner[stor4.length + 1].field_256) = caller
      holderId[caller] = stor4.length + 1
      uint256(allowance[_symbol].field_0) = stor4.length + 1
      uint256(allowance[_symbol].field_256) = _value
      uint256(allowance[_symbol][2][].field_0) = Array(len=_name.length, data=_name[all])
      uint256(allowance[_symbol][3][].field_0) = Array(len=_description.length, data=_description[all])
      uint8(allowance[_symbol].field_1024) = uint8(_isReissuable)
      Mask(248, 0, allowance[_symbol].field_1032) = Mask(248, 0, _baseUnit)
      Mask(240, 0, allowance[_symbol].field_1040) = Mask(240, 16, _isReissuable) >> 16
      uint256(allowance[_symbol][5][stor4.length + 1].field_0) = _value
      call addr(eventsHistoryAddress).emitIssue(bytes32 symbol, uint256 value, address by) with:
           gas gas_remaining - 25050 wei
          args _symbol, _value, addr(owner[stor4.length + 1].field_256)
  require ext_call.success
  return 1


# hash = 0x0af3e660
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 6]]]
# const = None
# payable = True
def getHolderId(address _holder) payable: 
  return holderId[addr(_holder)]


# hash = 0x12ab7242
# getter = None
# const = None
# payable = True
def setupStackDepthLib(address _stackDepthLib) payable: 
  if addr(stor0.field_0) != 0:
      return 0
  uint256(stor0.field_0) = _stackDepthLib or Mask(96, 160, uint256(stor0.field_0))
  return 1


# hash = 0x1c8d5d38
# getter = ['storage', 256, 0, ['sha3', ['data', ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], 6]]], ['add', 1, ['sha3', ['data', ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 6]]], ['add', 5, ['sha3', ['data', ['cd', 68], 7]]]]]]]]]
# const = None
# payable = True
def allowance(address _from, address _spender, bytes32 _symbol) payable: 
  return uint256(allowance[_symbol][5][stor6[addr(_from)]][1][stor6[addr(_spender)]].field_0)


# hash = 0x2a11ced0
# getter = ['struct', ['loc', 5]]
# const = None
# payable = True
def holders(uint256 _param1) payable: 
  return uint256(owner[_param1].field_0), addr(owner[_param1].field_256)


# hash = 0x2e59c036
# getter = None
# const = None
# payable = True
def unknown2e59c036(uint256 _param1, uint256 _param2) payable: 
  if addr(unknown4d1d2dbe[stor6[caller]][_param2]):
      call addr(unknown4d1d2dbe[stor6[caller]][_param2]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], holderId[caller])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          return 0
  else:
      if addr(unknown4d1d2dbe[stor6[caller]]):
          call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
  if holderId[caller] != 0:
      uint256(unknown4d1d2dbe[stor6[caller]][_param2]) = _param1 or Mask(96, 160, uint256(unknown4d1d2dbe[stor6[caller]][_param2]))
  else:
      stor4.length++
      addr(owner[stor4.length + 1].field_256) = caller
      holderId[caller] = stor4.length + 1
      uint256(unknown4d1d2dbe[stor4.length + 1][_param2]) = _param1 or Mask(96, 160, uint256(unknown4d1d2dbe[stor4.length + 1][_param2]))
  return 1


# hash = 0x2f553d31
# getter = None
# const = None
# payable = True
def isCreated(bytes32 _symbol) payable: 
  return not not uint256(allowance[_symbol].field_0)


# hash = 0x30d30c89
# getter = None
# const = None
# payable = True
def unknown30d30c89(uint256 _param1, uint256 _param2) payable: 
  if addr(unknown4d1d2dbe[stor6[caller]][_param2]):
      call addr(unknown4d1d2dbe[stor6[caller]][_param2]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], holderId[caller])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
      else:
          if uint256(allowance[_param2].field_0):
              if uint256(allowance[_param2].field_0) == holderId[caller]:
                  uint256(proxies[_param2].field_0) = _param1 or Mask(96, 160, uint256(proxies[_param2].field_0))
                  return 1
  else:
      if not addr(unknown4d1d2dbe[stor6[caller]]):
          if uint256(allowance[_param2].field_0):
              if uint256(allowance[_param2].field_0) == holderId[caller]:
                  uint256(proxies[_param2].field_0) = _param1 or Mask(96, 160, uint256(proxies[_param2].field_0))
                  return 1
      else:
          call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
          else:
              if uint256(allowance[_param2].field_0):
                  if uint256(allowance[_param2].field_0) == holderId[caller]:
                      uint256(proxies[_param2].field_0) = _param1 or Mask(96, 160, uint256(proxies[_param2].field_0))
                      return 1
  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
       gas gas_remaining - 25050 wei
      args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
  require ext_call.success
  return 0


# hash = 0x31c6c4cf
# getter = None
# const = None
# payable = True
def unknown31c6c4cf(addr _param1, addr _param2, uint256 _param3, uint256 _param4, array _param5) payable: 
  if holderId[addr(_param2)] != 0:
      if addr(unknown4d1d2dbe[stor6[caller]][_param4]) != 0:
          call addr(unknown4d1d2dbe[stor6[caller]][_param4]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[caller]]):
              call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[caller])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_param4].field_160):
          if not uint8(proxies[_param4][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[addr(_param1)] == holderId[addr(_param2)]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _param3:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_param4][5][stor6[addr(_param1)]].field_0) < _param3:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if _param5.length > 0:
          if not uint8(stor3[('map', ('param', '_param4'), ('name', 'stor1', 1))]):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if holderId[addr(_param1)] != holderId[caller]:
          if uint256(allowance[_param4][5][stor6[addr(_param1)]][1][stor6[caller]].field_0) < _param3:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_param4][5][stor6[addr(_param1)]].field_0) -= _param3
      uint256(allowance[_param4][5][stor6[addr(_param2)]].field_0) += _param3
      if holderId[caller] != holderId[addr(_param1)]:
          uint256(allowance[_param4][5][stor6[addr(_param1)]][1][stor6[caller]].field_0) -= _param3
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(owner[stor6[addr(_param1)]].field_256), addr(owner[stor6[addr(_param2)]].field_256), _param4, _param3, Array(len=_param5.length, data=_param5[all])
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_param4].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_param4].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[addr(_param1)]].field_256), addr(owner[stor6[addr(_param2)]].field_256), _param3
          if not ext_call.success:
              require not uint8(proxies[_param4].field_168)
          uint8(stor0.field_160) = 0
  else:
      stor4.length++
      uint256(owner[stor4.length + 1].field_256) = _param2 or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
      holderId[addr(_param2)] = stor4.length + 1
      if addr(unknown4d1d2dbe[stor6[caller]][_param4]) != 0:
          call addr(unknown4d1d2dbe[stor6[caller]][_param4]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[caller]]):
              call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[caller])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_param4].field_160):
          if not uint8(proxies[_param4][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[addr(_param1)] == stor4.length + 1:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _param3:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_param4][5][stor6[addr(_param1)]].field_0) < _param3:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if _param5.length > 0:
          if not uint8(stor3[('map', ('param', '_param4'), ('name', 'stor1', 1))]):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if holderId[addr(_param1)] != holderId[caller]:
          if uint256(allowance[_param4][5][stor6[addr(_param1)]][1][stor6[caller]].field_0) < _param3:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_param4][5][stor6[addr(_param1)]].field_0) -= _param3
      uint256(allowance[_param4][5][stor4.length + 1].field_0) += _param3
      if holderId[caller] != holderId[addr(_param1)]:
          uint256(allowance[_param4][5][stor6[addr(_param1)]][1][stor6[caller]].field_0) -= _param3
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(owner[stor6[addr(_param1)]].field_256), addr(owner[stor4.length + 1].field_256), _param4, _param3, Array(len=_param5.length, data=_param5[all])
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_param4].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_param4].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[addr(_param1)]].field_256), addr(owner[stor4.length + 1].field_256), _param3
          if not ext_call.success:
              require not uint8(proxies[_param4].field_168)
          uint8(stor0.field_160) = 0
  return 1


# hash = 0x401e3367
# getter = None
# const = None
# payable = True
def transferFrom(address _from, address _to, uint256 _value, bytes32 _data) payable: 
  if holderId[addr(_to)] != 0:
      if addr(unknown4d1d2dbe[stor6[caller]][_data]) != 0:
          call addr(unknown4d1d2dbe[stor6[caller]][_data]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[caller]]):
              call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[caller])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_data].field_160):
          if not uint8(proxies[_data][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[addr(_from)] == holderId[addr(_to)]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _value:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_data][5][stor6[addr(_from)]].field_0) < _value:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if holderId[addr(_from)] != holderId[caller]:
          if uint256(allowance[_data][5][stor6[addr(_from)]][1][stor6[caller]].field_0) < _value:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_data][5][stor6[addr(_from)]].field_0) -= _value
      uint256(allowance[_data][5][stor6[addr(_to)]].field_0) += _value
      if holderId[caller] != holderId[addr(_from)]:
          uint256(allowance[_data][5][stor6[addr(_from)]][1][stor6[caller]].field_0) -= _value
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args 0, uint32(owner[stor6[addr(_from)]].field_256), addr(owner[stor6[addr(_to)]].field_256), _data, _value, 160, 0, None
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_data].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_data].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[addr(_from)]].field_256), addr(owner[stor6[addr(_to)]].field_256), _value
          if not ext_call.success:
              require not uint8(proxies[_data].field_168)
          uint8(stor0.field_160) = 0
  else:
      stor4.length++
      uint256(owner[stor4.length + 1].field_256) = _to or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
      holderId[addr(_to)] = stor4.length + 1
      if addr(unknown4d1d2dbe[stor6[caller]][_data]) != 0:
          call addr(unknown4d1d2dbe[stor6[caller]][_data]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[caller]]):
              call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[caller])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_data].field_160):
          if not uint8(proxies[_data][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[addr(_from)] == stor4.length + 1:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _value:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_data][5][stor6[addr(_from)]].field_0) < _value:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if holderId[addr(_from)] != holderId[caller]:
          if uint256(allowance[_data][5][stor6[addr(_from)]][1][stor6[caller]].field_0) < _value:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_data][5][stor6[addr(_from)]].field_0) -= _value
      uint256(allowance[_data][5][stor4.length + 1].field_0) += _value
      if holderId[caller] != holderId[addr(_from)]:
          uint256(allowance[_data][5][stor6[addr(_from)]][1][stor6[caller]].field_0) -= _value
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args 0, uint32(owner[stor6[addr(_from)]].field_256), addr(owner[stor4.length + 1].field_256), _data, _value, 160, 0, None
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_data].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_data].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[addr(_from)]].field_256), addr(owner[stor4.length + 1].field_256), _value
          if not ext_call.success:
              require not uint8(proxies[_data].field_168)
          uint8(stor0.field_160) = 0
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
  if addr(stor2.length) != caller:
      return 0
  addr(stor1.length) = addr(stor2.length)
  addr(stor2.length) = 0
  return 1


# hash = 0x4637d827
# getter = None
# const = None
# payable = True
def trust(address _newDealer) payable: 
  if holderId[caller] != 0:
      if holderId[caller] == holderId[addr(_newDealer)]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot trust to oneself'
          require ext_call.success
          return 0
      if uint256(owner[stor6[caller]][3][addr(_newDealer)].field_0):
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Already trusted'
          require ext_call.success
          return 0
      uint256(owner[stor6[caller]].field_0)++
      uint256(owner[stor6[caller]][3][addr(_newDealer)].field_0) = uint256(owner[stor6[caller]].field_0) + 1
      uint256(owner[stor6[caller]][2][uint256(owner[stor6[caller]].field_0) + 1].field_0) = _newDealer or Mask(96, 160, uint256(owner[stor6[caller]][2][uint256(owner[stor6[caller]].field_0) + 1].field_0))
  else:
      stor4.length++
      addr(owner[stor4.length + 1].field_256) = caller
      holderId[caller] = stor4.length + 1
      if stor4.length + 1 == holderId[addr(_newDealer)]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot trust to oneself'
          require ext_call.success
          return 0
      if uint256(owner[stor6[caller]][3][addr(_newDealer)].field_0):
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Already trusted'
          require ext_call.success
          return 0
      uint256(owner[stor4.length + 1].field_0)++
      uint256(owner[stor4.length + 1][3][addr(_newDealer)].field_0) = uint256(owner[stor4.length + 1].field_0) + 1
      uint256(owner[stor4.length + 1][2][uint256(owner[stor4.length + 1].field_0) + 1].field_0) = _newDealer or Mask(96, 160, uint256(owner[stor4.length + 1][2][uint256(owner[stor4.length + 1].field_0) + 1].field_0))
  return 1


# hash = 0x4d1d2dbe
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 11]]]
# const = None
# payable = True
def unknown4d1d2dbe(uint256 _param1) payable: 
  return addr(unknown4d1d2dbe[_param1])


# hash = 0x4d30b6be
# getter = ['storage', 256, 0, ['sha3', ['data', ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 6]]], ['add', 5, ['sha3', ['data', ['cd', 36], 7]]]]]]
# const = None
# payable = True
def balanceOf(address _holder, bytes32 _symbol) payable: 
  return uint256(allowance[_symbol][5][stor6[addr(_holder)]].field_0)


# hash = 0x4f09eba7
# getter = None
# const = None
# payable = True
def unknown4f09eba7(addr _param1, uint256 _param2, uint256 _param3) payable: 
  if not uint8(proxies[_param3][1][caller].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if uint8(stor0.field_160):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if holderId[addr(_param1)] != 0:
      if holderId[tx.origin] != 0:
          require addr(stor0.field_0) != 0
          [93mdelegate addr(stor0.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(stor0.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not stor3[('map', ('param', '_param3'), ('name', 'stor4', 4))]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(unknown4d1d2dbe[stor6[tx.origin]][_param3]):
              call addr(unknown4d1d2dbe[stor6[tx.origin]][_param3]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[tx.origin])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(unknown4d1d2dbe[stor6[tx.origin]]):
                  call addr(unknown4d1d2dbe[stor6[tx.origin]]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], holderId[tx.origin])
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(proxies[_param3].field_160):
              if not uint8(proxies[_param3][1][caller].field_0):
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(allowance[_param3].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if holderId[tx.origin] == holderId[addr(_param1)]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(allowance[_param3][5][stor6[tx.origin]][1][stor6[addr(_param1)]].field_0) = _param2
          call addr(eventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(owner[stor6[tx.origin]].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param3, _param2
          require ext_call.success
          if addr(proxies[_param3].field_0):
              uint8(stor0.field_160) = 1
              call addr(proxies[_param3].field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(owner[stor6[tx.origin]].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param2
              if not ext_call.success:
                  require not uint8(proxies[_param3].field_168)
              uint8(stor0.field_160) = 0
      else:
          stor4.length++
          uint256(owner[stor4.length + 1].field_256) = tx.origin or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
          holderId[tx.origin] = stor4.length + 1
          require addr(stor0.field_0) != 0
          [93mdelegate addr(stor0.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(stor0.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not stor3[('map', ('param', '_param3'), ('name', 'stor4', 4))]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(unknown4d1d2dbe[stor4.length + 1][_param3]):
              call addr(unknown4d1d2dbe[stor4.length + 1][_param3]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], stor4.length + 1)
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(unknown4d1d2dbe[stor4.length + 1]):
                  call addr(unknown4d1d2dbe[stor4.length + 1]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], stor4.length + 1)
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(proxies[_param3].field_160):
              if not uint8(proxies[_param3][1][caller].field_0):
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(allowance[_param3].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if stor4.length + 1 == holderId[addr(_param1)]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(allowance[_param3][5][stor4.length + 1][1][stor6[addr(_param1)]].field_0) = _param2
          call addr(eventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(owner[stor4.length + 1].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param3, _param2
          require ext_call.success
          if addr(proxies[_param3].field_0):
              uint8(stor0.field_160) = 1
              call addr(proxies[_param3].field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(owner[stor4.length + 1].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param2
              if not ext_call.success:
                  require not uint8(proxies[_param3].field_168)
              uint8(stor0.field_160) = 0
  else:
      stor4.length++
      uint256(owner[stor4.length + 1].field_256) = _param1 or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
      holderId[addr(_param1)] = stor4.length + 1
      if holderId[tx.origin] != 0:
          require addr(stor0.field_0) != 0
          [93mdelegate addr(stor0.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(stor0.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not stor3[('map', ('param', '_param3'), ('name', 'stor4', 4))]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(unknown4d1d2dbe[stor6[tx.origin]][_param3]):
              call addr(unknown4d1d2dbe[stor6[tx.origin]][_param3]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[tx.origin])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(unknown4d1d2dbe[stor6[tx.origin]]):
                  call addr(unknown4d1d2dbe[stor6[tx.origin]]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], holderId[tx.origin])
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(proxies[_param3].field_160):
              if not uint8(proxies[_param3][1][caller].field_0):
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(allowance[_param3].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if holderId[tx.origin] == stor4.length + 1:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(allowance[_param3][5][stor6[tx.origin]][1][stor4.length + 1].field_0) = _param2
          call addr(eventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(owner[stor6[tx.origin]].field_256), addr(owner[stor4.length + 1].field_256), _param3, _param2
          require ext_call.success
          if addr(proxies[_param3].field_0):
              uint8(stor0.field_160) = 1
              call addr(proxies[_param3].field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(owner[stor6[tx.origin]].field_256), addr(owner[stor4.length + 1].field_256), _param2
              if not ext_call.success:
                  require not uint8(proxies[_param3].field_168)
              uint8(stor0.field_160) = 0
      else:
          stor4.length++
          uint256(owner[stor4.length + 1].field_256) = tx.origin or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
          holderId[tx.origin] = stor4.length + 1
          require addr(stor0.field_0) != 0
          [93mdelegate addr(stor0.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(stor0.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not stor3[('map', ('param', '_param3'), ('name', 'stor4', 4))]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(unknown4d1d2dbe[stor4.length + 1][_param3]):
              call addr(unknown4d1d2dbe[stor4.length + 1][_param3]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], stor4.length + 1)
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(unknown4d1d2dbe[stor4.length + 1]):
                  call addr(unknown4d1d2dbe[stor4.length + 1]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], stor4.length + 1)
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(proxies[_param3].field_160):
              if not uint8(proxies[_param3][1][caller].field_0):
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(allowance[_param3].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if stor4.length + 1 == stor4.length + 1:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(allowance[_param3][5][stor4.length + 1][1][stor4.length + 1].field_0) = _param2
          call addr(eventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(owner[stor4.length + 1].field_256), addr(owner[stor4.length + 1].field_256), _param3, _param2
          require ext_call.success
          if addr(proxies[_param3].field_0):
              uint8(stor0.field_160) = 1
              call addr(proxies[_param3].field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(owner[stor4.length + 1].field_256), addr(owner[stor4.length + 1].field_256), _param2
              if not ext_call.success:
                  require not uint8(proxies[_param3].field_168)
              uint8(stor0.field_160) = 0
  return 1


# hash = 0x557f4bc9
# getter = None
# const = None
# payable = True
def changeContractOwnership(address _to) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if addr(stor1.length) != caller:
      return 0
  stor2.length = _to or Mask(96, 160, stor2.length)
  return 1


# hash = 0x57cfeeee
# getter = None
# const = None
# payable = True
def transfer(address _to, uint256 _value, bytes32 _data) payable: 
  if holderId[addr(_to)] != 0:
      if addr(unknown4d1d2dbe[stor6[caller]][_data]) != 0:
          call addr(unknown4d1d2dbe[stor6[caller]][_data]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[caller]]):
              call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[caller])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_data].field_160):
          if not uint8(proxies[_data][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[caller] == holderId[addr(_to)]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _value:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_data][5][stor6[caller]].field_0) < _value:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if holderId[caller] != holderId[caller]:
          if uint256(allowance[_data][5][stor6[caller]][1][stor6[caller]].field_0) < _value:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_data][5][stor6[caller]].field_0) -= _value
      uint256(allowance[_data][5][stor6[addr(_to)]].field_0) += _value
      if holderId[caller] != holderId[caller]:
          uint256(allowance[_data][5][stor6[caller]][1][stor6[caller]].field_0) -= _value
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args 0, uint32(owner[stor6[caller]].field_256), addr(owner[stor6[addr(_to)]].field_256), _data, _value, 160, 0, None
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_data].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_data].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[caller]].field_256), addr(owner[stor6[addr(_to)]].field_256), _value
          if not ext_call.success:
              require not uint8(proxies[_data].field_168)
          uint8(stor0.field_160) = 0
  else:
      stor4.length++
      uint256(owner[stor4.length + 1].field_256) = _to or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
      holderId[addr(_to)] = stor4.length + 1
      if addr(unknown4d1d2dbe[stor6[caller]][_data]) != 0:
          call addr(unknown4d1d2dbe[stor6[caller]][_data]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[caller]]):
              call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[caller])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_data].field_160):
          if not uint8(proxies[_data][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[caller] == stor4.length + 1:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _value:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_data][5][stor6[caller]].field_0) < _value:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if holderId[caller] != holderId[caller]:
          if uint256(allowance[_data][5][stor6[caller]][1][stor6[caller]].field_0) < _value:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_data][5][stor6[caller]].field_0) -= _value
      uint256(allowance[_data][5][stor4.length + 1].field_0) += _value
      if holderId[caller] != holderId[caller]:
          uint256(allowance[_data][5][stor6[caller]][1][stor6[caller]].field_0) -= _value
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args 0, uint32(owner[stor6[caller]].field_256), addr(owner[stor4.length + 1].field_256), _data, _value, 160, 0, None
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_data].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_data].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[caller]].field_256), addr(owner[stor4.length + 1].field_256), _value
          if not ext_call.success:
              require not uint8(proxies[_data].field_168)
          uint8(stor0.field_160) = 0
  return 1


# hash = 0x5aa77d3c
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def pendingContractOwner() payable: 
  return addr(stor2.length)


# hash = 0x648bf774
# getter = None
# const = None
# payable = True
def recover(address _from, address _to) payable: 
  if not uint256(owner[stor6[addr(_from)]][3][caller].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Only trusted: access denied'
      require ext_call.success
      return 0
  if addr(unknown4d1d2dbe[stor6[addr(_from)]]):
      call addr(unknown4d1d2dbe[stor6[addr(_from)]]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], holderId[addr(_from)])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Only trusted: access denied'
          return 0
  if holderId[addr(_to)] != 0:
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Should recover to new address'
      require ext_call.success
      return 0
  uint256(owner[stor6[addr(_from)]].field_256) = _to or Mask(96, 160, uint256(owner[stor6[addr(_from)]].field_256))
  holderId[addr(_to)] = holderId[addr(_from)]
  call addr(eventsHistoryAddress).emitRecovery(address from, address to, address by) with:
       gas gas_remaining - 25050 wei
      args addr(owner[stor6[addr(_from)]].field_256), addr(_to), caller
  require ext_call.success
  return 1


# hash = 0x64ef212e
# getter = None
# const = None
# payable = True
def unknown64ef212e(addr _param1, uint256 _param2, uint256 _param3, array _param4) payable: 
  if not uint8(proxies[_param3][1][caller].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if uint8(stor0.field_160):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if holderId[addr(_param1)] != 0:
      if addr(unknown4d1d2dbe[stor6[tx.origin]][_param3]) != 0:
          call addr(unknown4d1d2dbe[stor6[tx.origin]][_param3]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[tx.origin])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[tx.origin]]):
              call addr(unknown4d1d2dbe[stor6[tx.origin]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[tx.origin])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_param3].field_160):
          if not uint8(proxies[_param3][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[tx.origin] == holderId[addr(_param1)]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _param2:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_param3][5][stor6[tx.origin]].field_0) < _param2:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if _param4.length > 0:
          if not uint8(stor3[('map', ('param', '_param3'), ('name', 'stor1', 1))]):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if holderId[tx.origin] != holderId[tx.origin]:
          if uint256(allowance[_param3][5][stor6[tx.origin]][1][stor6[tx.origin]].field_0) < _param2:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_param3][5][stor6[tx.origin]].field_0) -= _param2
      uint256(allowance[_param3][5][stor6[addr(_param1)]].field_0) += _param2
      if holderId[tx.origin] != holderId[tx.origin]:
          uint256(allowance[_param3][5][stor6[tx.origin]][1][stor6[tx.origin]].field_0) -= _param2
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(owner[stor6[tx.origin]].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param3, _param2, Array(len=_param4.length, data=_param4[all])
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_param3].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_param3].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[tx.origin]].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param2
          if not ext_call.success:
              require not uint8(proxies[_param3].field_168)
          uint8(stor0.field_160) = 0
  else:
      stor4.length++
      uint256(owner[stor4.length + 1].field_256) = _param1 or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
      holderId[addr(_param1)] = stor4.length + 1
      if addr(unknown4d1d2dbe[stor6[tx.origin]][_param3]) != 0:
          call addr(unknown4d1d2dbe[stor6[tx.origin]][_param3]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[tx.origin])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[tx.origin]]):
              call addr(unknown4d1d2dbe[stor6[tx.origin]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[tx.origin])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_param3].field_160):
          if not uint8(proxies[_param3][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[tx.origin] == stor4.length + 1:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _param2:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_param3][5][stor6[tx.origin]].field_0) < _param2:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if _param4.length > 0:
          if not uint8(stor3[('map', ('param', '_param3'), ('name', 'stor1', 1))]):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if holderId[tx.origin] != holderId[tx.origin]:
          if uint256(allowance[_param3][5][stor6[tx.origin]][1][stor6[tx.origin]].field_0) < _param2:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_param3][5][stor6[tx.origin]].field_0) -= _param2
      uint256(allowance[_param3][5][stor4.length + 1].field_0) += _param2
      if holderId[tx.origin] != holderId[tx.origin]:
          uint256(allowance[_param3][5][stor6[tx.origin]][1][stor6[tx.origin]].field_0) -= _param2
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(owner[stor6[tx.origin]].field_256), addr(owner[stor4.length + 1].field_256), _param3, _param2, Array(len=_param4.length, data=_param4[all])
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_param3].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_param3].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[tx.origin]].field_256), addr(owner[stor4.length + 1].field_256), _param2
          if not ext_call.success:
              require not uint8(proxies[_param3].field_168)
          uint8(stor0.field_160) = 0
  return 1


# hash = 0x6713e230
# getter = None
# const = None
# payable = True
def isTrusted(address _from, address _to) payable: 
  return not not uint256(owner[stor6[addr(_from)]][3][addr(_to)].field_0)


# hash = 0x691f3431
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['add', 2, ['sha3', ['data', ['cd', 4], 7]]]]]], ['add', 2, ['sha3', ['data', ['cd', 4], 7]]]]]
# const = None
# payable = True
def name(bytes32 _node) payable: 
  return uint256(allowance[_node][2][0 len allowance[_node][2].length].field_0)


# hash = 0x6932af36
# getter = ['struct', ['loc', 8]]
# const = None
# payable = True
def proxies(bytes32 _param1) payable: 
  return addr(proxies[_param1].field_0), bool(uint8(proxies[_param1].field_160)), bool(uint8(proxies[_param1].field_168))


# hash = 0x6b4ed21b
# getter = ['storage', 256, 0, 4]
# const = None
# payable = True
def holdersCount() payable: 
  return stor4.length


# hash = 0x6e293817
# getter = None
# const = None
# payable = True
def unknown6e293817(addr _param1, uint256 _param2, uint256 _param3, array _param4) payable: 
  if holderId[addr(_param1)] != 0:
      if addr(unknown4d1d2dbe[stor6[caller]][_param3]) != 0:
          call addr(unknown4d1d2dbe[stor6[caller]][_param3]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[caller]]):
              call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[caller])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_param3].field_160):
          if not uint8(proxies[_param3][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[caller] == holderId[addr(_param1)]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _param2:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_param3][5][stor6[caller]].field_0) < _param2:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if _param4.length > 0:
          if not uint8(stor3[('map', ('param', '_param3'), ('name', 'stor1', 1))]):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if holderId[caller] != holderId[caller]:
          if uint256(allowance[_param3][5][stor6[caller]][1][stor6[caller]].field_0) < _param2:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_param3][5][stor6[caller]].field_0) -= _param2
      uint256(allowance[_param3][5][stor6[addr(_param1)]].field_0) += _param2
      if holderId[caller] != holderId[caller]:
          uint256(allowance[_param3][5][stor6[caller]][1][stor6[caller]].field_0) -= _param2
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(owner[stor6[caller]].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param3, _param2, Array(len=_param4.length, data=_param4[all])
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_param3].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_param3].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[caller]].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param2
          if not ext_call.success:
              require not uint8(proxies[_param3].field_168)
          uint8(stor0.field_160) = 0
  else:
      stor4.length++
      uint256(owner[stor4.length + 1].field_256) = _param1 or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
      holderId[addr(_param1)] = stor4.length + 1
      if addr(unknown4d1d2dbe[stor6[caller]][_param3]) != 0:
          call addr(unknown4d1d2dbe[stor6[caller]][_param3]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[caller]]):
              call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[caller])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_param3].field_160):
          if not uint8(proxies[_param3][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[caller] == stor4.length + 1:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _param2:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_param3][5][stor6[caller]].field_0) < _param2:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if _param4.length > 0:
          if not uint8(stor3[('map', ('param', '_param3'), ('name', 'stor1', 1))]):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if holderId[caller] != holderId[caller]:
          if uint256(allowance[_param3][5][stor6[caller]][1][stor6[caller]].field_0) < _param2:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_param3][5][stor6[caller]].field_0) -= _param2
      uint256(allowance[_param3][5][stor4.length + 1].field_0) += _param2
      if holderId[caller] != holderId[caller]:
          uint256(allowance[_param3][5][stor6[caller]][1][stor6[caller]].field_0) -= _param2
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(owner[stor6[caller]].field_256), addr(owner[stor4.length + 1].field_256), _param3, _param2, Array(len=_param4.length, data=_param4[all])
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_param3].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_param3].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[caller]].field_256), addr(owner[stor4.length + 1].field_256), _param2
          if not ext_call.success:
              require not uint8(proxies[_param3].field_168)
          uint8(stor0.field_160) = 0
  return 1


# hash = 0x6effec50
# getter = None
# const = None
# payable = True
def unknown6effec50(addr _param1, uint256 _param2, array _param3) payable: 
  mem[128 len _param3.length] = _param3[all]
  if addr(stor1.length) != caller:
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


# hash = 0x713574bd
# getter = None
# const = None
# payable = True
def unknown713574bd(uint256 _param1, uint256 _param2) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if addr(stor1.length) != caller:
      return 0
  uint256(stor3[_param1]) = _param2 or Mask(248, 8, uint256(stor3[_param1]))
  return 1


# hash = 0x774248a3
# getter = None
# const = None
# payable = True
def setupRegistryICAP(address _registryICAP) payable: 
  if addr(stor1.length) != caller:
      return 0
  if addr(registryICAPAddress) != 0:
      return 0
  uint256(stor9) = _registryICAP or Mask(96, 160, uint256(stor9))
  return 1


# hash = 0x8180f2fc
# getter = None
# const = None
# payable = True
def unknown8180f2fc(addr _param1, uint256 _param2, uint256 _param3) payable: 
  if holderId[addr(_param1)] != 0:
      if holderId[caller] != 0:
          require addr(stor0.field_0) != 0
          [93mdelegate addr(stor0.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(stor0.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not stor3[('map', ('param', '_param3'), ('name', 'stor4', 4))]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(unknown4d1d2dbe[stor6[caller]][_param3]):
              call addr(unknown4d1d2dbe[stor6[caller]][_param3]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[caller])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(unknown4d1d2dbe[stor6[caller]]):
                  call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], holderId[caller])
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(proxies[_param3].field_160):
              if not uint8(proxies[_param3][1][caller].field_0):
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(allowance[_param3].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if holderId[caller] == holderId[addr(_param1)]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(allowance[_param3][5][stor6[caller]][1][stor6[addr(_param1)]].field_0) = _param2
          call addr(eventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(owner[stor6[caller]].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param3, _param2
          require ext_call.success
          if addr(proxies[_param3].field_0):
              uint8(stor0.field_160) = 1
              call addr(proxies[_param3].field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(owner[stor6[caller]].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param2
              if not ext_call.success:
                  require not uint8(proxies[_param3].field_168)
              uint8(stor0.field_160) = 0
      else:
          stor4.length++
          addr(owner[stor4.length + 1].field_256) = caller
          holderId[caller] = stor4.length + 1
          require addr(stor0.field_0) != 0
          [93mdelegate addr(stor0.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(stor0.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not stor3[('map', ('param', '_param3'), ('name', 'stor4', 4))]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(unknown4d1d2dbe[stor4.length + 1][_param3]):
              call addr(unknown4d1d2dbe[stor4.length + 1][_param3]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], stor4.length + 1)
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(unknown4d1d2dbe[stor4.length + 1]):
                  call addr(unknown4d1d2dbe[stor4.length + 1]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], stor4.length + 1)
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(proxies[_param3].field_160):
              if not uint8(proxies[_param3][1][caller].field_0):
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(allowance[_param3].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if stor4.length + 1 == holderId[addr(_param1)]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(allowance[_param3][5][stor4.length + 1][1][stor6[addr(_param1)]].field_0) = _param2
          call addr(eventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(owner[stor4.length + 1].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param3, _param2
          require ext_call.success
          if addr(proxies[_param3].field_0):
              uint8(stor0.field_160) = 1
              call addr(proxies[_param3].field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(owner[stor4.length + 1].field_256), addr(owner[stor6[addr(_param1)]].field_256), _param2
              if not ext_call.success:
                  require not uint8(proxies[_param3].field_168)
              uint8(stor0.field_160) = 0
  else:
      stor4.length++
      uint256(owner[stor4.length + 1].field_256) = _param1 or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
      holderId[addr(_param1)] = stor4.length + 1
      if holderId[caller] != 0:
          require addr(stor0.field_0) != 0
          [93mdelegate addr(stor0.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(stor0.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not stor3[('map', ('param', '_param3'), ('name', 'stor4', 4))]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(unknown4d1d2dbe[stor6[caller]][_param3]):
              call addr(unknown4d1d2dbe[stor6[caller]][_param3]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[caller])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(unknown4d1d2dbe[stor6[caller]]):
                  call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], holderId[caller])
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(proxies[_param3].field_160):
              if not uint8(proxies[_param3][1][caller].field_0):
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(allowance[_param3].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if holderId[caller] == stor4.length + 1:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(allowance[_param3][5][stor6[caller]][1][stor4.length + 1].field_0) = _param2
          call addr(eventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(owner[stor6[caller]].field_256), addr(owner[stor4.length + 1].field_256), _param3, _param2
          require ext_call.success
          if addr(proxies[_param3].field_0):
              uint8(stor0.field_160) = 1
              call addr(proxies[_param3].field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(owner[stor6[caller]].field_256), addr(owner[stor4.length + 1].field_256), _param2
              if not ext_call.success:
                  require not uint8(proxies[_param3].field_168)
              uint8(stor0.field_160) = 0
      else:
          stor4.length++
          addr(owner[stor4.length + 1].field_256) = caller
          holderId[caller] = stor4.length + 1
          require addr(stor0.field_0) != 0
          [93mdelegate addr(stor0.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(stor0.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not stor3[('map', ('param', '_param3'), ('name', 'stor4', 4))]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(unknown4d1d2dbe[stor4.length + 1][_param3]):
              call addr(unknown4d1d2dbe[stor4.length + 1][_param3]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], stor4.length + 1)
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(unknown4d1d2dbe[stor4.length + 1]):
                  call addr(unknown4d1d2dbe[stor4.length + 1]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], stor4.length + 1)
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(proxies[_param3].field_160):
              if not uint8(proxies[_param3][1][caller].field_0):
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(allowance[_param3].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if stor4.length + 1 == stor4.length + 1:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(allowance[_param3][5][stor4.length + 1][1][stor4.length + 1].field_0) = _param2
          call addr(eventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(owner[stor4.length + 1].field_256), addr(owner[stor4.length + 1].field_256), _param3, _param2
          require ext_call.success
          if addr(proxies[_param3].field_0):
              uint8(stor0.field_160) = 1
              call addr(proxies[_param3].field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(owner[stor4.length + 1].field_256), addr(owner[stor4.length + 1].field_256), _param2
              if not ext_call.success:
                  require not uint8(proxies[_param3].field_168)
              uint8(stor0.field_160) = 0
  return 1


# hash = 0x9fda5b66
# getter = ['struct', ['loc', 7]]
# const = None
# payable = True
def assets(bytes32 _param1) payable: 
  mem[320] = uint256(allowance[_param1][2].field_0)
  [94midx = 320
  [94ms = 0
  while allowance[_param1][2].length + 320 > [94midx + 32:
      mem[[94midx + 32] = uint256(allowance[_param1][[94ms + 2].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[allowance[_param1][2].length + (floor32(allowance[_param1][2].length - 1) + -allowance[_param1][2].length + 32 % 32) + 320] = allowance[_param1][3].length
  mem[allowance[_param1][2].length + (floor32(allowance[_param1][2].length - 1) + -allowance[_param1][2].length + 32 % 32) + 352] = uint256(allowance[_param1][3].field_0)
  [94midx = allowance[_param1][2].length + (floor32(allowance[_param1][2].length - 1) + -allowance[_param1][2].length + 32 % 32) + 352
  [94ms = 0
  while allowance[_param1][2].length + (floor32(allowance[_param1][2].length - 1) + -allowance[_param1][2].length + 32 % 32) + allowance[_param1][3].length + 352 > [94midx + 32:
      mem[[94midx + 32] = uint256(allowance[_param1][[94ms + 3].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return uint256(allowance[_param1].field_0), 
         uint256(allowance[_param1].field_256),
         Array(len=allowance[_param1][2].length, data=mem[320 len allowance[_param1][2].length + (floor32(allowance[_param1][2].length - 1) + -allowance[_param1][2].length + 32 % 32) + allowance[_param1][3].length + (floor32(allowance[_param1][3].length - 1) + -allowance[_param1][3].length + 32 % 32) + 32]),
         allowance[_param1][2].length + (floor32(allowance[_param1][2].length - 1) + -allowance[_param1][2].length + 32 % 32) + 224,
         bool(uint8(allowance[_param1].field_1024)),
         uint8(allowance[_param1].field_1024)


# hash = 0xa0f15b87
# getter = ['storage', 160, 0, 9]
# const = None
# payable = True
def registryICAP() payable: 
  return addr(registryICAPAddress)


# hash = 0xaeadd049
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = True
def unknownaeadd049(uint256 _param1) payable: 
  return bool(uint8(stor3[_param1]))


# hash = 0xb524abcf
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 4], 7]]]]
# const = None
# payable = True
def totalSupply(bytes32 _symbol) payable: 
  return uint256(allowance[_symbol].field_256)


# hash = 0xbb6e0e2c
# getter = None
# const = None
# payable = True
def unknownbb6e0e2c() payable: 
  if 0 == holderId[caller]:
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Didn't trust yet'
      require ext_call.success
      return 0
  if not uint256(owner[stor6[caller]].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Didn't trust yet'
      require ext_call.success
      return 0
  mem[0] = holderId[caller]
  mem[32] = 5
  [94ms = 0
  [94midx = 1
  while [94midx <= uint256(owner[stor6[caller]].field_0):
      [94m_21 = sha3([94midx, sha3(mem[0 len 64]) + 2)
      uint256(stor[sha3(mem[0 len 64]) + 3][addr(stor[sha3(mem[0 len 64]) + 2][[94midx])]) = 0
      addr(stor[sha3(mem[0 len 64]) + 2][[94midx]) = 0
      mem[0] = holderId[caller]
      mem[32] = 5
      [94ms = addr(stor[[94m_21])
      [94midx = [94midx + 1
      continue 
  uint256(owner[stor6[caller]].field_0) = 0
  return 1


# hash = 0xbebcc045
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['add', 3, ['sha3', ['data', ['cd', 4], 7]]]]]], ['add', 3, ['sha3', ['data', ['cd', 4], 7]]]]]
# const = None
# payable = True
def description(bytes32 _symbol) payable: 
  return uint256(allowance[_symbol][3][0 len allowance[_symbol][3].length].field_0)


# hash = 0xc4eeeeb9
# getter = ['bool', ['storage', 8, 0, ['add', 4, ['sha3', ['data', ['cd', 4], 7]]]]]
# const = None
# payable = True
def isReissuable(bytes32 _symbol) payable: 
  return bool(uint8(allowance[_symbol].field_1024))


# hash = 0xca448a88
# getter = None
# const = None
# payable = True
def revokeAsset(bytes32 _symbol, uint256 _value) payable: 
  if addr(unknown4d1d2dbe[stor6[caller]][_symbol]):
      call addr(unknown4d1d2dbe[stor6[caller]][_symbol]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], holderId[caller])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
          require ext_call.success
          return 0
  else:
      if addr(unknown4d1d2dbe[stor6[caller]]):
          call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
              require ext_call.success
              return 0
  if not uint256(allowance[_symbol].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if uint256(allowance[_symbol].field_0) != holderId[caller]:
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if not uint8(stor3[('map', ('param', '_symbol'), ('name', 'stor2', 2))]):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x466561747572652069732064697361626c6564000000000000000000000000
      require ext_call.success
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      return 0
  if 0 == _value:
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Cannot revoke 0 value'
      require ext_call.success
      return 0
  if uint256(allowance[_symbol][5][stor6[caller]].field_0) < _value:
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Not enough tokens to revoke'
      require ext_call.success
      return 0
  uint256(allowance[_symbol][5][stor6[caller]].field_0) -= _value
  uint256(allowance[_symbol].field_256) -= _value
  call addr(eventsHistoryAddress).emitRevoke(bytes32 symbol, uint256 value, address by) with:
       gas gas_remaining - 25050 wei
      args _symbol, _value, addr(owner[stor6[caller]].field_256)
  require ext_call.success
  require addr(stor0.field_0) != 0
  [93mdelegate addr(stor0.field_0).0x32921690 with:
       gas gas_remaining - 50 wei
      args addr(stor0.field_0), 1
  require delegate.return_code
  require delegate.return_data[0]
  if addr(proxies[_symbol].field_0):
      uint8(stor0.field_160) = 1
      call addr(proxies[_symbol].field_0) with:
         funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
           gas gas_remaining - 25050 wei
          args addr(owner[stor6[caller]].field_256), addr(owner[0].field_256), _value
      if not ext_call.success:
          require not uint8(proxies[_symbol].field_168)
      uint8(stor0.field_160) = 0
  return 1


# hash = 0xcbbc1bf3
# getter = None
# const = None
# payable = True
def unknowncbbc1bf3(uint256 _param1) payable: 
  if addr(unknown4d1d2dbe[stor6[caller]]):
      call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], holderId[caller])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          return 0
  if holderId[caller] != 0:
      uint256(unknown4d1d2dbe[stor6[caller]]) = _param1 or Mask(96, 160, uint256(unknown4d1d2dbe[stor6[caller]]))
  else:
      stor4.length++
      addr(owner[stor4.length + 1].field_256) = caller
      holderId[caller] = stor4.length + 1
      uint256(unknown4d1d2dbe[stor4.length + 1]) = _param1 or Mask(96, 160, uint256(unknown4d1d2dbe[stor4.length + 1]))
  return 1


# hash = 0xce606ee0
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def contractOwner() payable: 
  return addr(stor1.length)


# hash = 0xdc86e6f0
# getter = ['storage', 8, 8, ['add', 4, ['sha3', ['data', ['cd', 4], 7]]]]
# const = None
# payable = True
def baseUnit(bytes32 _symbol) payable: 
  return uint8(allowance[_symbol].field_1032)


# hash = 0xe0873c06
# getter = None
# const = None
# payable = True
def reissueAsset(bytes32 _symbol, uint256 _value) payable: 
  if addr(unknown4d1d2dbe[stor6[caller]][_symbol]):
      call addr(unknown4d1d2dbe[stor6[caller]][_symbol]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], holderId[caller])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
          require ext_call.success
          return 0
  else:
      if addr(unknown4d1d2dbe[stor6[caller]]):
          call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
              require ext_call.success
              return 0
  if not uint256(allowance[_symbol].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if uint256(allowance[_symbol].field_0) != holderId[caller]:
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if 0 == _value:
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Cannot reissue 0 value'
      require ext_call.success
      return 0
  if not uint8(allowance[_symbol].field_1024):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Cannot reissue fixed asset'
      require ext_call.success
      return 0
  if _value + uint256(allowance[_symbol].field_256) < uint256(allowance[_symbol].field_256):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Total supply overflow'
      require ext_call.success
      return 0
  uint256(allowance[_symbol][5][stor6[caller]].field_0) += _value
  uint256(allowance[_symbol].field_256) += _value
  call addr(eventsHistoryAddress).emitIssue(bytes32 symbol, uint256 value, address by) with:
       gas gas_remaining - 25050 wei
      args _symbol, _value, addr(owner[stor6[caller]].field_256)
  require ext_call.success
  require addr(stor0.field_0) != 0
  [93mdelegate addr(stor0.field_0).0x32921690 with:
       gas gas_remaining - 50 wei
      args addr(stor0.field_0), 1
  require delegate.return_code
  require delegate.return_data[0]
  if addr(proxies[_symbol].field_0):
      uint8(stor0.field_160) = 1
      call addr(proxies[_symbol].field_0) with:
         funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
           gas gas_remaining - 25050 wei
          args addr(owner[0].field_256), addr(owner[stor6[caller]].field_256), _value
      if not ext_call.success:
          require not uint8(proxies[_symbol].field_168)
      uint8(stor0.field_160) = 0
  return 1


# hash = 0xe82b7cb2
# getter = None
# const = None
# payable = True
def unknowne82b7cb2(uint256 _param1, uint256 _param2) payable: 
  if not uint8(proxies[_param2][1][caller].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if uint8(stor0.field_160):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if addr(unknown4d1d2dbe[stor6[tx.origin]][_param2]):
      call addr(unknown4d1d2dbe[stor6[tx.origin]][_param2]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], holderId[tx.origin])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args code.data[14790 len 32]
          return 0
  else:
      if addr(unknown4d1d2dbe[stor6[tx.origin]]):
          call addr(unknown4d1d2dbe[stor6[tx.origin]]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[tx.origin])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args code.data[14790 len 32]
              return 0
  if holderId[tx.origin] != 0:
      uint256(unknown4d1d2dbe[stor6[tx.origin]][_param2]) = _param1 or Mask(96, 160, uint256(unknown4d1d2dbe[stor6[tx.origin]][_param2]))
  else:
      stor4.length++
      uint256(owner[stor4.length + 1].field_256) = tx.origin or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
      holderId[tx.origin] = stor4.length + 1
      uint256(unknown4d1d2dbe[stor4.length + 1][_param2]) = _param1 or Mask(96, 160, uint256(unknown4d1d2dbe[stor4.length + 1][_param2]))
  return 1


# hash = 0xe96b462a
# getter = None
# const = None
# payable = True
def isOwner(address _owner, bytes32 _symbol) payable: 
  if not uint256(allowance[_symbol].field_0):
      return not not uint256(allowance[_symbol].field_0)
  return (uint256(allowance[_symbol].field_0) == holderId[addr(_owner)])


# hash = 0xf01b0220
# getter = None
# const = None
# payable = True
def unknownf01b0220(uint256 _param1, uint128 _param2, uint256 _param3) payable: 
  if addr(unknown4d1d2dbe[stor6[caller]][_param3]):
      call addr(unknown4d1d2dbe[stor6[caller]][_param3]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], holderId[caller])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
          require ext_call.success
          return 0
  else:
      if addr(unknown4d1d2dbe[stor6[caller]]):
          call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
              require ext_call.success
              return 0
  if not uint256(allowance[_param3].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if uint256(allowance[_param3].field_0) != holderId[caller]:
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if _param1:
      if uint256(allowance[_param3][5][stor6[caller]].field_0) != uint256(allowance[_param3].field_256):
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot set with holders'
          require ext_call.success
          return 0
  else:
      if _param2:
          if uint256(allowance[_param3][5][stor6[caller]].field_0) != uint256(allowance[_param3].field_256):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot set with holders'
              require ext_call.success
              return 0
  uint8(proxies[_param3].field_160) = uint8(_param1)
  Mask(88, 0, proxies[_param3].field_168) = Mask(88, 0, _param2)
  Mask(80, 0, proxies[_param3].field_176) = Mask(80, 16, _param1) >> 16
  Mask(80, 0, proxies[_param3].field_176) = 0
  return 1


# hash = 0xf07629f8
# getter = ['storage', 160, 0, 10]
# const = None
# payable = True
def eventsHistory() payable: 
  return addr(eventsHistoryAddress)


# hash = 0xf0c06aa5
# getter = None
# const = None
# payable = True
def distrust(address _dealer) payable: 
  if not uint256(owner[stor6[caller]][3][addr(_dealer)].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Only trusted: access denied'
      require ext_call.success
      return 0
  if uint256(owner[stor6[caller]][3][addr(_dealer)].field_0) < uint256(owner[stor6[caller]].field_0):
      addr(owner[stor6[caller]][2][uint256(owner[stor6[caller]][3][addr(_dealer)].field_0)].field_0) = addr(owner[stor6[caller]][2][uint256(owner[stor6[caller]].field_0)].field_0)
      uint256(owner[stor6[caller]][3][addr(owner[stor6[caller]][2][uint256(owner[stor6[caller]].field_0)].field_0)].field_0) = uint256(owner[stor6[caller]][3][addr(_dealer)].field_0)
  uint256(owner[stor6[caller]].field_0)--
  addr(owner[stor6[caller]][2][uint256(owner[stor6[caller]].field_0) - 1].field_0) = 0
  uint256(owner[stor6[caller]][3][addr(_dealer)].field_0) = 0
  return 1


# hash = 0xf0cbe059
# getter = None
# const = None
# payable = True
def unknownf0cbe059(addr _param1, addr _param2, uint256 _param3, uint256 _param4, array _param5) payable: 
  if not uint8(proxies[_param4][1][caller].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if uint8(stor0.field_160):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if holderId[addr(_param2)] != 0:
      if addr(unknown4d1d2dbe[stor6[tx.origin]][_param4]) != 0:
          call addr(unknown4d1d2dbe[stor6[tx.origin]][_param4]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[tx.origin])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[tx.origin]]):
              call addr(unknown4d1d2dbe[stor6[tx.origin]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[tx.origin])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_param4].field_160):
          if not uint8(proxies[_param4][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[addr(_param1)] == holderId[addr(_param2)]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _param3:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_param4][5][stor6[addr(_param1)]].field_0) < _param3:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if _param5.length > 0:
          if not uint8(stor3[('map', ('param', '_param4'), ('name', 'stor1', 1))]):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if holderId[addr(_param1)] != holderId[tx.origin]:
          if uint256(allowance[_param4][5][stor6[addr(_param1)]][1][stor6[tx.origin]].field_0) < _param3:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_param4][5][stor6[addr(_param1)]].field_0) -= _param3
      uint256(allowance[_param4][5][stor6[addr(_param2)]].field_0) += _param3
      if holderId[tx.origin] != holderId[addr(_param1)]:
          uint256(allowance[_param4][5][stor6[addr(_param1)]][1][stor6[tx.origin]].field_0) -= _param3
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(owner[stor6[addr(_param1)]].field_256), addr(owner[stor6[addr(_param2)]].field_256), _param4, _param3, Array(len=_param5.length, data=_param5[all])
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_param4].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_param4].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[addr(_param1)]].field_256), addr(owner[stor6[addr(_param2)]].field_256), _param3
          if not ext_call.success:
              require not uint8(proxies[_param4].field_168)
          uint8(stor0.field_160) = 0
  else:
      stor4.length++
      uint256(owner[stor4.length + 1].field_256) = _param2 or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
      holderId[addr(_param2)] = stor4.length + 1
      if addr(unknown4d1d2dbe[stor6[tx.origin]][_param4]) != 0:
          call addr(unknown4d1d2dbe[stor6[tx.origin]][_param4]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[tx.origin])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(unknown4d1d2dbe[stor6[tx.origin]]):
              call addr(unknown4d1d2dbe[stor6[tx.origin]]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], holderId[tx.origin])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(proxies[_param4].field_160):
          if not uint8(proxies[_param4][1][caller].field_0):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if holderId[addr(_param1)] == stor4.length + 1:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == _param3:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(allowance[_param4][5][stor6[addr(_param1)]].field_0) < _param3:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if _param5.length > 0:
          if not uint8(stor3[('map', ('param', '_param4'), ('name', 'stor1', 1))]):
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if holderId[addr(_param1)] != holderId[tx.origin]:
          if uint256(allowance[_param4][5][stor6[addr(_param1)]][1][stor6[tx.origin]].field_0) < _param3:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(allowance[_param4][5][stor6[addr(_param1)]].field_0) -= _param3
      uint256(allowance[_param4][5][stor4.length + 1].field_0) += _param3
      if holderId[tx.origin] != holderId[addr(_param1)]:
          uint256(allowance[_param4][5][stor6[addr(_param1)]][1][stor6[tx.origin]].field_0) -= _param3
      call addr(eventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(owner[stor6[addr(_param1)]].field_256), addr(owner[stor4.length + 1].field_256), _param4, _param3, Array(len=_param5.length, data=_param5[all])
      require ext_call.success
      require addr(stor0.field_0) != 0
      [93mdelegate addr(stor0.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(stor0.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(proxies[_param4].field_0):
          uint8(stor0.field_160) = 1
          call addr(proxies[_param4].field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(owner[stor6[addr(_param1)]].field_256), addr(owner[stor4.length + 1].field_256), _param3
          if not ext_call.success:
              require not uint8(proxies[_param4].field_168)
          uint8(stor0.field_160) = 0
  return 1


# hash = 0xfd83915e
# getter = None
# const = None
# payable = True
def changeOwnership(bytes32 _symbol, address _newOwner) payable: 
  if addr(unknown4d1d2dbe[stor6[caller]][_symbol]):
      call addr(unknown4d1d2dbe[stor6[caller]][_symbol]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], holderId[caller])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
          require ext_call.success
          return 0
  else:
      if addr(unknown4d1d2dbe[stor6[caller]]):
          call addr(unknown4d1d2dbe[stor6[caller]]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], holderId[caller])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              call addr(eventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
              require ext_call.success
              return 0
  if not uint256(allowance[_symbol].field_0):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if uint256(allowance[_symbol].field_0) != holderId[caller]:
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if not uint8(stor3[('map', ('param', '_symbol'), ('name', 'stor3', 3))]):
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x466561747572652069732064697361626c6564000000000000000000000000
      require ext_call.success
      call addr(eventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      return 0
  if holderId[addr(_newOwner)] != 0:
      if holderId[addr(_newOwner)] == uint256(allowance[_symbol].field_0):
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot pass ownership to oneself'
          require ext_call.success
          return 0
      uint256(allowance[_symbol].field_0) = holderId[addr(_newOwner)]
      call addr(eventsHistoryAddress).emitOwnershipChange(address from, address to, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(owner[uint256(stor7[_symbol].field_0)].field_256), addr(owner[stor6[addr(_newOwner)]].field_256), _symbol
  else:
      stor4.length++
      uint256(owner[stor4.length + 1].field_256) = _newOwner or Mask(96, 160, uint256(owner[stor4.length + 1].field_256))
      holderId[addr(_newOwner)] = stor4.length + 1
      if stor4.length + 1 == uint256(allowance[_symbol].field_0):
          call addr(eventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot pass ownership to oneself'
          require ext_call.success
          return 0
      uint256(allowance[_symbol].field_0) = stor4.length + 1
      call addr(eventsHistoryAddress).emitOwnershipChange(address from, address to, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(owner[uint256(stor7[_symbol].field_0)].field_256), addr(owner[stor4.length + 1].field_256), _symbol
  require ext_call.success
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


