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
def owner(bytes32 m_symbol) payable: 
  return addr(mownerm[uint256(mstor7m[m_symbolm]m.field_0)m]m.field_256)


# hash = 0x02927d20
# getter = None
# const = None
# payable = True
def setupEventsHistory(address m_eventsHistory) payable: 
  if addr(mstor1m.length) != caller:
      return 0
  if addr(meventsHistoryAddress) != 0:
      return 0
  uint256(mstor10) = m_eventsHistory or Mask(96, 160, uint256(mstor10))
  return 1


# hash = 0x0610e037
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = True
def isEnabled(bytes32 m_switch) payable: 
  return bool(uint8(mstor3m[m_switchm]))


# hash = 0x06489899
# getter = None
# const = None
# payable = True
def unknown06489899(addr m_param1, uint256 m_param2, uint256 m_param3) payable: 
  if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]):
      call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
      else:
          if uint256(mallowancem[m_param3m]m.field_0):
              if uint256(mallowancem[m_param3m]m.field_0) == mholderIdm[callerm]:
                  uint256(mproxiesm[m_param3m]m[1m]m[addr(m_param1)m]m.field_0) = m_param2 or Mask(248, 8, uint256(mproxiesm[m_param3m]m[1m]m[addr(m_param1)m]m.field_0))
                  return 1
  else:
      if not addr(munknown4d1d2dbem[mstor6m[callerm]m]):
          if uint256(mallowancem[m_param3m]m.field_0):
              if uint256(mallowancem[m_param3m]m.field_0) == mholderIdm[callerm]:
                  uint256(mproxiesm[m_param3m]m[1m]m[addr(m_param1)m]m.field_0) = m_param2 or Mask(248, 8, uint256(mproxiesm[m_param3m]m[1m]m[addr(m_param1)m]m.field_0))
                  return 1
      else:
          call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
          else:
              if uint256(mallowancem[m_param3m]m.field_0):
                  if uint256(mallowancem[m_param3m]m.field_0) == mholderIdm[callerm]:
                      uint256(mproxiesm[m_param3m]m[1m]m[addr(m_param1)m]m.field_0) = m_param2 or Mask(248, 8, uint256(mproxiesm[m_param3m]m[1m]m[addr(m_param1)m]m.field_0))
                      return 1
  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
       gas gas_remaining - 25050 wei
      args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
  require ext_call.success
  return 0


# hash = 0x085a4705
# getter = None
# const = None
# payable = True
def issueAsset(bytes32 m_symbol, uint256 m_value, string m_name, string m_description, uint8 m_baseUnit, bool m_isReissuable) payable: 
  if not uint8(mstor3m[m_symbolm][uint8(m_isReissuable)m][0m]):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x466561747572652069732064697361626c6564000000000000000000000000
      require ext_call.success
      return 0
  if 0 == m_value:
      if not m_isReissuable:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot issue 0 value fixed asset'
          require ext_call.success
          return 0
  if uint256(mallowancem[m_symbolm]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Asset already issued'
      require ext_call.success
      return 0
  if mholderIdm[callerm] != 0:
      uint256(mallowancem[m_symbolm]m.field_0) = mholderIdm[callerm]
      uint256(mallowancem[m_symbolm]m.field_256) = m_value
      uint256(mallowancem[m_symbolm]m[2m]m[m]m.field_0) = Array(len=m_name.length, data=m_name[allm])
      uint256(mallowancem[m_symbolm]m[3m]m[m]m.field_0) = Array(len=m_description.length, data=m_description[allm])
      uint8(mallowancem[m_symbolm]m.field_1024) = uint8(m_isReissuable)
      Mask(248, 0, mallowancem[m_symbolm]m.field_1032) = Mask(248, 0, m_baseUnit)
      Mask(240, 0, mallowancem[m_symbolm]m.field_1040) = Mask(240, 16, m_isReissuable) >> 16
      uint256(mallowancem[m_symbolm]m[5m]m[mstor6m[callerm]m]m.field_0) = m_value
      call addr(meventsHistoryAddress).emitIssue(bytes32 symbol, uint256 value, address by) with:
           gas gas_remaining - 25050 wei
          args m_symbol, m_value, addr(mownerm[mstor6m[callerm]m]m.field_256)
  else:
      mstor4m.length++
      addr(mownerm[mstor4m.length + 1m]m.field_256) = caller
      mholderIdm[callerm] = mstor4m.length + 1
      uint256(mallowancem[m_symbolm]m.field_0) = mstor4m.length + 1
      uint256(mallowancem[m_symbolm]m.field_256) = m_value
      uint256(mallowancem[m_symbolm]m[2m]m[m]m.field_0) = Array(len=m_name.length, data=m_name[allm])
      uint256(mallowancem[m_symbolm]m[3m]m[m]m.field_0) = Array(len=m_description.length, data=m_description[allm])
      uint8(mallowancem[m_symbolm]m.field_1024) = uint8(m_isReissuable)
      Mask(248, 0, mallowancem[m_symbolm]m.field_1032) = Mask(248, 0, m_baseUnit)
      Mask(240, 0, mallowancem[m_symbolm]m.field_1040) = Mask(240, 16, m_isReissuable) >> 16
      uint256(mallowancem[m_symbolm]m[5m]m[mstor4m.length + 1m]m.field_0) = m_value
      call addr(meventsHistoryAddress).emitIssue(bytes32 symbol, uint256 value, address by) with:
           gas gas_remaining - 25050 wei
          args m_symbol, m_value, addr(mownerm[mstor4m.length + 1m]m.field_256)
  require ext_call.success
  return 1


# hash = 0x0af3e660
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 6]]]
# const = None
# payable = True
def getHolderId(address m_holder) payable: 
  return mholderIdm[addr(m_holder)m]


# hash = 0x12ab7242
# getter = None
# const = None
# payable = True
def setupStackDepthLib(address m_stackDepthLib) payable: 
  if addr(mstor0m.field_0) != 0:
      return 0
  uint256(mstor0m.field_0) = m_stackDepthLib or Mask(96, 160, uint256(mstor0m.field_0))
  return 1


# hash = 0x1c8d5d38
# getter = ['storage', 256, 0, ['sha3', ['data', ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], 6]]], ['add', 1, ['sha3', ['data', ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 6]]], ['add', 5, ['sha3', ['data', ['cd', 68], 7]]]]]]]]]
# const = None
# payable = True
def allowance(address m_from, address m_spender, bytes32 m_symbol) payable: 
  return uint256(mallowancem[m_symbolm]m[5m]m[mstor6m[addr(m_from)m]m]m[1m]m[mstor6m[addr(m_spender)m]m]m.field_0)


# hash = 0x2a11ced0
# getter = ['struct', ['loc', 5]]
# const = None
# payable = True
def holders(uint256 m_param1) payable: 
  return uint256(mownerm[m_param1m]m.field_0), addr(mownerm[m_param1m]m.field_256)


# hash = 0x2e59c036
# getter = None
# const = None
# payable = True
def unknown2e59c036(uint256 m_param1, uint256 m_param2) payable: 
  if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param2m]):
      call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param2m]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          return 0
  else:
      if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
          call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
  if mholderIdm[callerm] != 0:
      uint256(munknown4d1d2dbem[mstor6m[callerm]m][m_param2m]) = m_param1 or Mask(96, 160, uint256(munknown4d1d2dbem[mstor6m[callerm]m][m_param2m]))
  else:
      mstor4m.length++
      addr(mownerm[mstor4m.length + 1m]m.field_256) = caller
      mholderIdm[callerm] = mstor4m.length + 1
      uint256(munknown4d1d2dbem[mstor4m.length + 1m][m_param2m]) = m_param1 or Mask(96, 160, uint256(munknown4d1d2dbem[mstor4m.length + 1m][m_param2m]))
  return 1


# hash = 0x2f553d31
# getter = None
# const = None
# payable = True
def isCreated(bytes32 m_symbol) payable: 
  return not not uint256(mallowancem[m_symbolm]m.field_0)


# hash = 0x30d30c89
# getter = None
# const = None
# payable = True
def unknown30d30c89(uint256 m_param1, uint256 m_param2) payable: 
  if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param2m]):
      call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param2m]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
      else:
          if uint256(mallowancem[m_param2m]m.field_0):
              if uint256(mallowancem[m_param2m]m.field_0) == mholderIdm[callerm]:
                  uint256(mproxiesm[m_param2m]m.field_0) = m_param1 or Mask(96, 160, uint256(mproxiesm[m_param2m]m.field_0))
                  return 1
  else:
      if not addr(munknown4d1d2dbem[mstor6m[callerm]m]):
          if uint256(mallowancem[m_param2m]m.field_0):
              if uint256(mallowancem[m_param2m]m.field_0) == mholderIdm[callerm]:
                  uint256(mproxiesm[m_param2m]m.field_0) = m_param1 or Mask(96, 160, uint256(mproxiesm[m_param2m]m.field_0))
                  return 1
      else:
          call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
          else:
              if uint256(mallowancem[m_param2m]m.field_0):
                  if uint256(mallowancem[m_param2m]m.field_0) == mholderIdm[callerm]:
                      uint256(mproxiesm[m_param2m]m.field_0) = m_param1 or Mask(96, 160, uint256(mproxiesm[m_param2m]m.field_0))
                      return 1
  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
       gas gas_remaining - 25050 wei
      args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
  require ext_call.success
  return 0


# hash = 0x31c6c4cf
# getter = None
# const = None
# payable = True
def unknown31c6c4cf(addr m_param1, addr m_param2, uint256 m_param3, uint256 m_param4, array m_param5) payable: 
  if mholderIdm[addr(m_param2)m] != 0:
      if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param4m]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param4m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
              call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_param4m]m.field_160):
          if not uint8(mproxiesm[m_param4m]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[addr(m_param1)m] == mholderIdm[addr(m_param2)m]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_param3:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m.field_0) < m_param3:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if m_param5.length > 0:
          if not uint8(mstor3m[('map', ('param', '_param4'), ('name', 'stor1', 1))m]):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if mholderIdm[addr(m_param1)m] != mholderIdm[callerm]:
          if uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m[1m]m[mstor6m[callerm]m]m.field_0) < m_param3:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m.field_0) -= m_param3
      uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param2)m]m]m.field_0) += m_param3
      if mholderIdm[callerm] != mholderIdm[addr(m_param1)m]:
          uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m[1m]m[mstor6m[callerm]m]m.field_0) -= m_param3
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), addr(mownerm[mstor6m[addr(m_param2)m]m]m.field_256), m_param4, m_param3, Array(len=m_param5.length, data=m_param5[allm])
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_param4m]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_param4m]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), addr(mownerm[mstor6m[addr(m_param2)m]m]m.field_256), m_param3
          if not ext_call.success:
              require not uint8(mproxiesm[m_param4m]m.field_168)
          uint8(mstor0m.field_160) = 0
  else:
      mstor4m.length++
      uint256(mownerm[mstor4m.length + 1m]m.field_256) = m_param2 or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
      mholderIdm[addr(m_param2)m] = mstor4m.length + 1
      if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param4m]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param4m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
              call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_param4m]m.field_160):
          if not uint8(mproxiesm[m_param4m]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[addr(m_param1)m] == mstor4m.length + 1:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_param3:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m.field_0) < m_param3:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if m_param5.length > 0:
          if not uint8(mstor3m[('map', ('param', '_param4'), ('name', 'stor1', 1))m]):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if mholderIdm[addr(m_param1)m] != mholderIdm[callerm]:
          if uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m[1m]m[mstor6m[callerm]m]m.field_0) < m_param3:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m.field_0) -= m_param3
      uint256(mallowancem[m_param4m]m[5m]m[mstor4m.length + 1m]m.field_0) += m_param3
      if mholderIdm[callerm] != mholderIdm[addr(m_param1)m]:
          uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m[1m]m[mstor6m[callerm]m]m.field_0) -= m_param3
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param4, m_param3, Array(len=m_param5.length, data=m_param5[allm])
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_param4m]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_param4m]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param3
          if not ext_call.success:
              require not uint8(mproxiesm[m_param4m]m.field_168)
          uint8(mstor0m.field_160) = 0
  return 1


# hash = 0x401e3367
# getter = None
# const = None
# payable = True
def transferFrom(address m_from, address m_to, uint256 m_value, bytes32 m_data) payable: 
  if mholderIdm[addr(m_to)m] != 0:
      if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_datam]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_datam]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
              call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_datam]m.field_160):
          if not uint8(mproxiesm[m_datam]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[addr(m_from)m] == mholderIdm[addr(m_to)m]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_value:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_datam]m[5m]m[mstor6m[addr(m_from)m]m]m.field_0) < m_value:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if mholderIdm[addr(m_from)m] != mholderIdm[callerm]:
          if uint256(mallowancem[m_datam]m[5m]m[mstor6m[addr(m_from)m]m]m[1m]m[mstor6m[callerm]m]m.field_0) < m_value:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_datam]m[5m]m[mstor6m[addr(m_from)m]m]m.field_0) -= m_value
      uint256(mallowancem[m_datam]m[5m]m[mstor6m[addr(m_to)m]m]m.field_0) += m_value
      if mholderIdm[callerm] != mholderIdm[addr(m_from)m]:
          uint256(mallowancem[m_datam]m[5m]m[mstor6m[addr(m_from)m]m]m[1m]m[mstor6m[callerm]m]m.field_0) -= m_value
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args 0, uint32(mownerm[mstor6m[addr(m_from)m]m]m.field_256), addr(mownerm[mstor6m[addr(m_to)m]m]m.field_256), m_data, m_value, 160, 0, None
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_datam]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_datam]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[addr(m_from)m]m]m.field_256), addr(mownerm[mstor6m[addr(m_to)m]m]m.field_256), m_value
          if not ext_call.success:
              require not uint8(mproxiesm[m_datam]m.field_168)
          uint8(mstor0m.field_160) = 0
  else:
      mstor4m.length++
      uint256(mownerm[mstor4m.length + 1m]m.field_256) = m_to or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
      mholderIdm[addr(m_to)m] = mstor4m.length + 1
      if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_datam]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_datam]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
              call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_datam]m.field_160):
          if not uint8(mproxiesm[m_datam]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[addr(m_from)m] == mstor4m.length + 1:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_value:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_datam]m[5m]m[mstor6m[addr(m_from)m]m]m.field_0) < m_value:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if mholderIdm[addr(m_from)m] != mholderIdm[callerm]:
          if uint256(mallowancem[m_datam]m[5m]m[mstor6m[addr(m_from)m]m]m[1m]m[mstor6m[callerm]m]m.field_0) < m_value:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_datam]m[5m]m[mstor6m[addr(m_from)m]m]m.field_0) -= m_value
      uint256(mallowancem[m_datam]m[5m]m[mstor4m.length + 1m]m.field_0) += m_value
      if mholderIdm[callerm] != mholderIdm[addr(m_from)m]:
          uint256(mallowancem[m_datam]m[5m]m[mstor6m[addr(m_from)m]m]m[1m]m[mstor6m[callerm]m]m.field_0) -= m_value
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args 0, uint32(mownerm[mstor6m[addr(m_from)m]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_data, m_value, 160, 0, None
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_datam]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_datam]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[addr(m_from)m]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_value
          if not ext_call.success:
              require not uint8(mproxiesm[m_datam]m.field_168)
          uint8(mstor0m.field_160) = 0
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
  if addr(mstor2m.length) != caller:
      return 0
  addr(mstor1m.length) = addr(mstor2m.length)
  addr(mstor2m.length) = 0
  return 1


# hash = 0x4637d827
# getter = None
# const = None
# payable = True
def trust(address m_newDealer) payable: 
  if mholderIdm[callerm] != 0:
      if mholderIdm[callerm] == mholderIdm[addr(m_newDealer)m]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot trust to oneself'
          require ext_call.success
          return 0
      if uint256(mownerm[mstor6m[callerm]m]m[3m]m[addr(m_newDealer)m]m.field_0):
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Already trusted'
          require ext_call.success
          return 0
      uint256(mownerm[mstor6m[callerm]m]m.field_0)++
      uint256(mownerm[mstor6m[callerm]m]m[3m]m[addr(m_newDealer)m]m.field_0) = uint256(mownerm[mstor6m[callerm]m]m.field_0) + 1
      uint256(mownerm[mstor6m[callerm]m]m[2m]m[uint256(mownerm[mstor6m[callerm]m]m.field_0) + 1m]m.field_0) = m_newDealer or Mask(96, 160, uint256(mownerm[mstor6m[callerm]m]m[2m]m[uint256(mownerm[mstor6m[callerm]m]m.field_0) + 1m]m.field_0))
  else:
      mstor4m.length++
      addr(mownerm[mstor4m.length + 1m]m.field_256) = caller
      mholderIdm[callerm] = mstor4m.length + 1
      if mstor4m.length + 1 == mholderIdm[addr(m_newDealer)m]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot trust to oneself'
          require ext_call.success
          return 0
      if uint256(mownerm[mstor6m[callerm]m]m[3m]m[addr(m_newDealer)m]m.field_0):
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Already trusted'
          require ext_call.success
          return 0
      uint256(mownerm[mstor4m.length + 1m]m.field_0)++
      uint256(mownerm[mstor4m.length + 1m]m[3m]m[addr(m_newDealer)m]m.field_0) = uint256(mownerm[mstor4m.length + 1m]m.field_0) + 1
      uint256(mownerm[mstor4m.length + 1m]m[2m]m[uint256(mownerm[mstor4m.length + 1m]m.field_0) + 1m]m.field_0) = m_newDealer or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m[2m]m[uint256(mownerm[mstor4m.length + 1m]m.field_0) + 1m]m.field_0))
  return 1


# hash = 0x4d1d2dbe
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 11]]]
# const = None
# payable = True
def unknown4d1d2dbe(uint256 m_param1) payable: 
  return addr(munknown4d1d2dbem[m_param1m])


# hash = 0x4d30b6be
# getter = ['storage', 256, 0, ['sha3', ['data', ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 6]]], ['add', 5, ['sha3', ['data', ['cd', 36], 7]]]]]]
# const = None
# payable = True
def balanceOf(address m_holder, bytes32 m_symbol) payable: 
  return uint256(mallowancem[m_symbolm]m[5m]m[mstor6m[addr(m_holder)m]m]m.field_0)


# hash = 0x4f09eba7
# getter = None
# const = None
# payable = True
def unknown4f09eba7(addr m_param1, uint256 m_param2, uint256 m_param3) payable: 
  if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if uint8(mstor0m.field_160):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if mholderIdm[addr(m_param1)m] != 0:
      if mholderIdm[tx.originm] != 0:
          require addr(mstor0m.field_0) != 0
          [93mdelegate addr(mstor0m.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(mstor0m.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not mstor3m[('map', ('param', '_param3'), ('name', 'stor4', 4))m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param3m]):
              call addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param3m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(munknown4d1d2dbem[mstor6m[tx.originm]m]):
                  call addr(munknown4d1d2dbem[mstor6m[tx.originm]m]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(mproxiesm[m_param3m]m.field_160):
              if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(mallowancem[m_param3m]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if mholderIdm[tx.originm] == mholderIdm[addr(m_param1)m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(mallowancem[m_param3m]m[5m]m[mstor6m[tx.originm]m]m[1m]m[mstor6m[addr(m_param1)m]m]m.field_0) = m_param2
          call addr(meventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(mownerm[mstor6m[tx.originm]m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param3, m_param2
          require ext_call.success
          if addr(mproxiesm[m_param3m]m.field_0):
              uint8(mstor0m.field_160) = 1
              call addr(mproxiesm[m_param3m]m.field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(mownerm[mstor6m[tx.originm]m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param2
              if not ext_call.success:
                  require not uint8(mproxiesm[m_param3m]m.field_168)
              uint8(mstor0m.field_160) = 0
      else:
          mstor4m.length++
          uint256(mownerm[mstor4m.length + 1m]m.field_256) = tx.origin or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
          mholderIdm[tx.originm] = mstor4m.length + 1
          require addr(mstor0m.field_0) != 0
          [93mdelegate addr(mstor0m.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(mstor0m.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not mstor3m[('map', ('param', '_param3'), ('name', 'stor4', 4))m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(munknown4d1d2dbem[mstor4m.length + 1m][m_param3m]):
              call addr(munknown4d1d2dbem[mstor4m.length + 1m][m_param3m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mstor4m.length + 1)
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(munknown4d1d2dbem[mstor4m.length + 1m]):
                  call addr(munknown4d1d2dbem[mstor4m.length + 1m]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], mstor4m.length + 1)
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(mproxiesm[m_param3m]m.field_160):
              if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(mallowancem[m_param3m]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if mstor4m.length + 1 == mholderIdm[addr(m_param1)m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(mallowancem[m_param3m]m[5m]m[mstor4m.length + 1m]m[1m]m[mstor6m[addr(m_param1)m]m]m.field_0) = m_param2
          call addr(meventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(mownerm[mstor4m.length + 1m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param3, m_param2
          require ext_call.success
          if addr(mproxiesm[m_param3m]m.field_0):
              uint8(mstor0m.field_160) = 1
              call addr(mproxiesm[m_param3m]m.field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(mownerm[mstor4m.length + 1m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param2
              if not ext_call.success:
                  require not uint8(mproxiesm[m_param3m]m.field_168)
              uint8(mstor0m.field_160) = 0
  else:
      mstor4m.length++
      uint256(mownerm[mstor4m.length + 1m]m.field_256) = m_param1 or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
      mholderIdm[addr(m_param1)m] = mstor4m.length + 1
      if mholderIdm[tx.originm] != 0:
          require addr(mstor0m.field_0) != 0
          [93mdelegate addr(mstor0m.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(mstor0m.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not mstor3m[('map', ('param', '_param3'), ('name', 'stor4', 4))m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param3m]):
              call addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param3m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(munknown4d1d2dbem[mstor6m[tx.originm]m]):
                  call addr(munknown4d1d2dbem[mstor6m[tx.originm]m]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(mproxiesm[m_param3m]m.field_160):
              if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(mallowancem[m_param3m]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if mholderIdm[tx.originm] == mstor4m.length + 1:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(mallowancem[m_param3m]m[5m]m[mstor6m[tx.originm]m]m[1m]m[mstor4m.length + 1m]m.field_0) = m_param2
          call addr(meventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(mownerm[mstor6m[tx.originm]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param3, m_param2
          require ext_call.success
          if addr(mproxiesm[m_param3m]m.field_0):
              uint8(mstor0m.field_160) = 1
              call addr(mproxiesm[m_param3m]m.field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(mownerm[mstor6m[tx.originm]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param2
              if not ext_call.success:
                  require not uint8(mproxiesm[m_param3m]m.field_168)
              uint8(mstor0m.field_160) = 0
      else:
          mstor4m.length++
          uint256(mownerm[mstor4m.length + 1m]m.field_256) = tx.origin or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
          mholderIdm[tx.originm] = mstor4m.length + 1
          require addr(mstor0m.field_0) != 0
          [93mdelegate addr(mstor0m.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(mstor0m.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not mstor3m[('map', ('param', '_param3'), ('name', 'stor4', 4))m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(munknown4d1d2dbem[mstor4m.length + 1m][m_param3m]):
              call addr(munknown4d1d2dbem[mstor4m.length + 1m][m_param3m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mstor4m.length + 1)
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(munknown4d1d2dbem[mstor4m.length + 1m]):
                  call addr(munknown4d1d2dbem[mstor4m.length + 1m]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], mstor4m.length + 1)
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(mproxiesm[m_param3m]m.field_160):
              if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(mallowancem[m_param3m]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if mstor4m.length + 1 == mstor4m.length + 1:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(mallowancem[m_param3m]m[5m]m[mstor4m.length + 1m]m[1m]m[mstor4m.length + 1m]m.field_0) = m_param2
          call addr(meventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(mownerm[mstor4m.length + 1m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param3, m_param2
          require ext_call.success
          if addr(mproxiesm[m_param3m]m.field_0):
              uint8(mstor0m.field_160) = 1
              call addr(mproxiesm[m_param3m]m.field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(mownerm[mstor4m.length + 1m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param2
              if not ext_call.success:
                  require not uint8(mproxiesm[m_param3m]m.field_168)
              uint8(mstor0m.field_160) = 0
  return 1


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
  if addr(mstor1m.length) != caller:
      return 0
  mstor2m.length = m_to or Mask(96, 160, mstor2m.length)
  return 1


# hash = 0x57cfeeee
# getter = None
# const = None
# payable = True
def transfer(address m_to, uint256 m_value, bytes32 m_data) payable: 
  if mholderIdm[addr(m_to)m] != 0:
      if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_datam]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_datam]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
              call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_datam]m.field_160):
          if not uint8(mproxiesm[m_datam]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[callerm] == mholderIdm[addr(m_to)m]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_value:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_datam]m[5m]m[mstor6m[callerm]m]m.field_0) < m_value:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if mholderIdm[callerm] != mholderIdm[callerm]:
          if uint256(mallowancem[m_datam]m[5m]m[mstor6m[callerm]m]m[1m]m[mstor6m[callerm]m]m.field_0) < m_value:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_datam]m[5m]m[mstor6m[callerm]m]m.field_0) -= m_value
      uint256(mallowancem[m_datam]m[5m]m[mstor6m[addr(m_to)m]m]m.field_0) += m_value
      if mholderIdm[callerm] != mholderIdm[callerm]:
          uint256(mallowancem[m_datam]m[5m]m[mstor6m[callerm]m]m[1m]m[mstor6m[callerm]m]m.field_0) -= m_value
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args 0, uint32(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor6m[addr(m_to)m]m]m.field_256), m_data, m_value, 160, 0, None
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_datam]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_datam]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor6m[addr(m_to)m]m]m.field_256), m_value
          if not ext_call.success:
              require not uint8(mproxiesm[m_datam]m.field_168)
          uint8(mstor0m.field_160) = 0
  else:
      mstor4m.length++
      uint256(mownerm[mstor4m.length + 1m]m.field_256) = m_to or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
      mholderIdm[addr(m_to)m] = mstor4m.length + 1
      if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_datam]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_datam]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
              call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_datam]m.field_160):
          if not uint8(mproxiesm[m_datam]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[callerm] == mstor4m.length + 1:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_value:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_datam]m[5m]m[mstor6m[callerm]m]m.field_0) < m_value:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if mholderIdm[callerm] != mholderIdm[callerm]:
          if uint256(mallowancem[m_datam]m[5m]m[mstor6m[callerm]m]m[1m]m[mstor6m[callerm]m]m.field_0) < m_value:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_datam]m[5m]m[mstor6m[callerm]m]m.field_0) -= m_value
      uint256(mallowancem[m_datam]m[5m]m[mstor4m.length + 1m]m.field_0) += m_value
      if mholderIdm[callerm] != mholderIdm[callerm]:
          uint256(mallowancem[m_datam]m[5m]m[mstor6m[callerm]m]m[1m]m[mstor6m[callerm]m]m.field_0) -= m_value
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args 0, uint32(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_data, m_value, 160, 0, None
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_datam]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_datam]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_value
          if not ext_call.success:
              require not uint8(mproxiesm[m_datam]m.field_168)
          uint8(mstor0m.field_160) = 0
  return 1


# hash = 0x5aa77d3c
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def pendingContractOwner() payable: 
  return addr(mstor2m.length)


# hash = 0x648bf774
# getter = None
# const = None
# payable = True
def recover(address m_from, address m_to) payable: 
  if not uint256(mownerm[mstor6m[addr(m_from)m]m]m[3m]m[callerm]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Only trusted: access denied'
      require ext_call.success
      return 0
  if addr(munknown4d1d2dbem[mstor6m[addr(m_from)m]m]):
      call addr(munknown4d1d2dbem[mstor6m[addr(m_from)m]m]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], mholderIdm[addr(m_from)m])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Only trusted: access denied'
          return 0
  if mholderIdm[addr(m_to)m] != 0:
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Should recover to new address'
      require ext_call.success
      return 0
  uint256(mownerm[mstor6m[addr(m_from)m]m]m.field_256) = m_to or Mask(96, 160, uint256(mownerm[mstor6m[addr(m_from)m]m]m.field_256))
  mholderIdm[addr(m_to)m] = mholderIdm[addr(m_from)m]
  call addr(meventsHistoryAddress).emitRecovery(address from, address to, address by) with:
       gas gas_remaining - 25050 wei
      args addr(mownerm[mstor6m[addr(m_from)m]m]m.field_256), addr(m_to), caller
  require ext_call.success
  return 1


# hash = 0x64ef212e
# getter = None
# const = None
# payable = True
def unknown64ef212e(addr m_param1, uint256 m_param2, uint256 m_param3, array m_param4) payable: 
  if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if uint8(mstor0m.field_160):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if mholderIdm[addr(m_param1)m] != 0:
      if addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param3m]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param3m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[tx.originm]m]):
              call addr(munknown4d1d2dbem[mstor6m[tx.originm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_param3m]m.field_160):
          if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[tx.originm] == mholderIdm[addr(m_param1)m]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_param2:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_param3m]m[5m]m[mstor6m[tx.originm]m]m.field_0) < m_param2:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if m_param4.length > 0:
          if not uint8(mstor3m[('map', ('param', '_param3'), ('name', 'stor1', 1))m]):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if mholderIdm[tx.originm] != mholderIdm[tx.originm]:
          if uint256(mallowancem[m_param3m]m[5m]m[mstor6m[tx.originm]m]m[1m]m[mstor6m[tx.originm]m]m.field_0) < m_param2:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_param3m]m[5m]m[mstor6m[tx.originm]m]m.field_0) -= m_param2
      uint256(mallowancem[m_param3m]m[5m]m[mstor6m[addr(m_param1)m]m]m.field_0) += m_param2
      if mholderIdm[tx.originm] != mholderIdm[tx.originm]:
          uint256(mallowancem[m_param3m]m[5m]m[mstor6m[tx.originm]m]m[1m]m[mstor6m[tx.originm]m]m.field_0) -= m_param2
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(mownerm[mstor6m[tx.originm]m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param3, m_param2, Array(len=m_param4.length, data=m_param4[allm])
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_param3m]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_param3m]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[tx.originm]m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param2
          if not ext_call.success:
              require not uint8(mproxiesm[m_param3m]m.field_168)
          uint8(mstor0m.field_160) = 0
  else:
      mstor4m.length++
      uint256(mownerm[mstor4m.length + 1m]m.field_256) = m_param1 or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
      mholderIdm[addr(m_param1)m] = mstor4m.length + 1
      if addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param3m]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param3m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[tx.originm]m]):
              call addr(munknown4d1d2dbem[mstor6m[tx.originm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_param3m]m.field_160):
          if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[tx.originm] == mstor4m.length + 1:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_param2:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_param3m]m[5m]m[mstor6m[tx.originm]m]m.field_0) < m_param2:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if m_param4.length > 0:
          if not uint8(mstor3m[('map', ('param', '_param3'), ('name', 'stor1', 1))m]):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if mholderIdm[tx.originm] != mholderIdm[tx.originm]:
          if uint256(mallowancem[m_param3m]m[5m]m[mstor6m[tx.originm]m]m[1m]m[mstor6m[tx.originm]m]m.field_0) < m_param2:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_param3m]m[5m]m[mstor6m[tx.originm]m]m.field_0) -= m_param2
      uint256(mallowancem[m_param3m]m[5m]m[mstor4m.length + 1m]m.field_0) += m_param2
      if mholderIdm[tx.originm] != mholderIdm[tx.originm]:
          uint256(mallowancem[m_param3m]m[5m]m[mstor6m[tx.originm]m]m[1m]m[mstor6m[tx.originm]m]m.field_0) -= m_param2
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(mownerm[mstor6m[tx.originm]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param3, m_param2, Array(len=m_param4.length, data=m_param4[allm])
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_param3m]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_param3m]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[tx.originm]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param2
          if not ext_call.success:
              require not uint8(mproxiesm[m_param3m]m.field_168)
          uint8(mstor0m.field_160) = 0
  return 1


# hash = 0x6713e230
# getter = None
# const = None
# payable = True
def isTrusted(address m_from, address m_to) payable: 
  return not not uint256(mownerm[mstor6m[addr(m_from)m]m]m[3m]m[addr(m_to)m]m.field_0)


# hash = 0x691f3431
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['add', 2, ['sha3', ['data', ['cd', 4], 7]]]]]], ['add', 2, ['sha3', ['data', ['cd', 4], 7]]]]]
# const = None
# payable = True
def name(bytes32 m_node) payable: 
  return uint256(mallowancem[m_nodem]m[2m]m[0 len mallowancem[m_nodem]m[2m]m.lengthm]m.field_0)


# hash = 0x6932af36
# getter = ['struct', ['loc', 8]]
# const = None
# payable = True
def proxies(bytes32 m_param1) payable: 
  return addr(mproxiesm[m_param1m]m.field_0), bool(uint8(mproxiesm[m_param1m]m.field_160)), bool(uint8(mproxiesm[m_param1m]m.field_168))


# hash = 0x6b4ed21b
# getter = ['storage', 256, 0, 4]
# const = None
# payable = True
def holdersCount() payable: 
  return mstor4m.length


# hash = 0x6e293817
# getter = None
# const = None
# payable = True
def unknown6e293817(addr m_param1, uint256 m_param2, uint256 m_param3, array m_param4) payable: 
  if mholderIdm[addr(m_param1)m] != 0:
      if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
              call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_param3m]m.field_160):
          if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[callerm] == mholderIdm[addr(m_param1)m]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_param2:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m.field_0) < m_param2:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if m_param4.length > 0:
          if not uint8(mstor3m[('map', ('param', '_param3'), ('name', 'stor1', 1))m]):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if mholderIdm[callerm] != mholderIdm[callerm]:
          if uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m[1m]m[mstor6m[callerm]m]m.field_0) < m_param2:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m.field_0) -= m_param2
      uint256(mallowancem[m_param3m]m[5m]m[mstor6m[addr(m_param1)m]m]m.field_0) += m_param2
      if mholderIdm[callerm] != mholderIdm[callerm]:
          uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m[1m]m[mstor6m[callerm]m]m.field_0) -= m_param2
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param3, m_param2, Array(len=m_param4.length, data=m_param4[allm])
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_param3m]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_param3m]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param2
          if not ext_call.success:
              require not uint8(mproxiesm[m_param3m]m.field_168)
          uint8(mstor0m.field_160) = 0
  else:
      mstor4m.length++
      uint256(mownerm[mstor4m.length + 1m]m.field_256) = m_param1 or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
      mholderIdm[addr(m_param1)m] = mstor4m.length + 1
      if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
              call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_param3m]m.field_160):
          if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[callerm] == mstor4m.length + 1:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_param2:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m.field_0) < m_param2:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if m_param4.length > 0:
          if not uint8(mstor3m[('map', ('param', '_param3'), ('name', 'stor1', 1))m]):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if mholderIdm[callerm] != mholderIdm[callerm]:
          if uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m[1m]m[mstor6m[callerm]m]m.field_0) < m_param2:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m.field_0) -= m_param2
      uint256(mallowancem[m_param3m]m[5m]m[mstor4m.length + 1m]m.field_0) += m_param2
      if mholderIdm[callerm] != mholderIdm[callerm]:
          uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m[1m]m[mstor6m[callerm]m]m.field_0) -= m_param2
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param3, m_param2, Array(len=m_param4.length, data=m_param4[allm])
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_param3m]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_param3m]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param2
          if not ext_call.success:
              require not uint8(mproxiesm[m_param3m]m.field_168)
          uint8(mstor0m.field_160) = 0
  return 1


# hash = 0x6effec50
# getter = None
# const = None
# payable = True
def unknown6effec50(addr m_param1, uint256 m_param2, array m_param3) payable: 
  mem[128 len m_param3.length] = m_param3[allm]
  if addr(mstor1m.length) != caller:
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


# hash = 0x713574bd
# getter = None
# const = None
# payable = True
def unknown713574bd(uint256 m_param1, uint256 m_param2) payable: 
  if call.value > 0:
      call caller with:
         value call.value wei
           gas gas_remaining - 34050 wei
      require ext_call.success
  if addr(mstor1m.length) != caller:
      return 0
  uint256(mstor3m[m_param1m]) = m_param2 or Mask(248, 8, uint256(mstor3m[m_param1m]))
  return 1


# hash = 0x774248a3
# getter = None
# const = None
# payable = True
def setupRegistryICAP(address m_registryICAP) payable: 
  if addr(mstor1m.length) != caller:
      return 0
  if addr(mregistryICAPAddress) != 0:
      return 0
  uint256(mstor9) = m_registryICAP or Mask(96, 160, uint256(mstor9))
  return 1


# hash = 0x8180f2fc
# getter = None
# const = None
# payable = True
def unknown8180f2fc(addr m_param1, uint256 m_param2, uint256 m_param3) payable: 
  if mholderIdm[addr(m_param1)m] != 0:
      if mholderIdm[callerm] != 0:
          require addr(mstor0m.field_0) != 0
          [93mdelegate addr(mstor0m.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(mstor0m.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not mstor3m[('map', ('param', '_param3'), ('name', 'stor4', 4))m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]):
              call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
                  call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(mproxiesm[m_param3m]m.field_160):
              if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(mallowancem[m_param3m]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if mholderIdm[callerm] == mholderIdm[addr(m_param1)m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m[1m]m[mstor6m[addr(m_param1)m]m]m.field_0) = m_param2
          call addr(meventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param3, m_param2
          require ext_call.success
          if addr(mproxiesm[m_param3m]m.field_0):
              uint8(mstor0m.field_160) = 1
              call addr(mproxiesm[m_param3m]m.field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param2
              if not ext_call.success:
                  require not uint8(mproxiesm[m_param3m]m.field_168)
              uint8(mstor0m.field_160) = 0
      else:
          mstor4m.length++
          addr(mownerm[mstor4m.length + 1m]m.field_256) = caller
          mholderIdm[callerm] = mstor4m.length + 1
          require addr(mstor0m.field_0) != 0
          [93mdelegate addr(mstor0m.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(mstor0m.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not mstor3m[('map', ('param', '_param3'), ('name', 'stor4', 4))m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(munknown4d1d2dbem[mstor4m.length + 1m][m_param3m]):
              call addr(munknown4d1d2dbem[mstor4m.length + 1m][m_param3m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mstor4m.length + 1)
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(munknown4d1d2dbem[mstor4m.length + 1m]):
                  call addr(munknown4d1d2dbem[mstor4m.length + 1m]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], mstor4m.length + 1)
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(mproxiesm[m_param3m]m.field_160):
              if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(mallowancem[m_param3m]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if mstor4m.length + 1 == mholderIdm[addr(m_param1)m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(mallowancem[m_param3m]m[5m]m[mstor4m.length + 1m]m[1m]m[mstor6m[addr(m_param1)m]m]m.field_0) = m_param2
          call addr(meventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(mownerm[mstor4m.length + 1m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param3, m_param2
          require ext_call.success
          if addr(mproxiesm[m_param3m]m.field_0):
              uint8(mstor0m.field_160) = 1
              call addr(mproxiesm[m_param3m]m.field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(mownerm[mstor4m.length + 1m]m.field_256), addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), m_param2
              if not ext_call.success:
                  require not uint8(mproxiesm[m_param3m]m.field_168)
              uint8(mstor0m.field_160) = 0
  else:
      mstor4m.length++
      uint256(mownerm[mstor4m.length + 1m]m.field_256) = m_param1 or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
      mholderIdm[addr(m_param1)m] = mstor4m.length + 1
      if mholderIdm[callerm] != 0:
          require addr(mstor0m.field_0) != 0
          [93mdelegate addr(mstor0m.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(mstor0m.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not mstor3m[('map', ('param', '_param3'), ('name', 'stor4', 4))m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]):
              call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
                  call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(mproxiesm[m_param3m]m.field_160):
              if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(mallowancem[m_param3m]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if mholderIdm[callerm] == mstor4m.length + 1:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m[1m]m[mstor4m.length + 1m]m.field_0) = m_param2
          call addr(meventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param3, m_param2
          require ext_call.success
          if addr(mproxiesm[m_param3m]m.field_0):
              uint8(mstor0m.field_160) = 1
              call addr(mproxiesm[m_param3m]m.field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param2
              if not ext_call.success:
                  require not uint8(mproxiesm[m_param3m]m.field_168)
              uint8(mstor0m.field_160) = 0
      else:
          mstor4m.length++
          addr(mownerm[mstor4m.length + 1m]m.field_256) = caller
          mholderIdm[callerm] = mstor4m.length + 1
          require addr(mstor0m.field_0) != 0
          [93mdelegate addr(mstor0m.field_0).0x32921690 with:
               gas gas_remaining - 50 wei
              args addr(mstor0m.field_0), 1
          require delegate.return_code
          require delegate.return_data[0]
          if not mstor3m[('map', ('param', '_param3'), ('name', 'stor4', 4))m]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x466561747572652069732064697361626c6564000000000000000000000000
              require ext_call.success
              return 0
          if addr(munknown4d1d2dbem[mstor4m.length + 1m][m_param3m]):
              call addr(munknown4d1d2dbem[mstor4m.length + 1m][m_param3m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mstor4m.length + 1)
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x466561747572652069732064697361626c6564000000000000000000000000
                  return 0
          else:
              if addr(munknown4d1d2dbem[mstor4m.length + 1m]):
                  call addr(munknown4d1d2dbem[mstor4m.length + 1m]).0xa25035b with:
                       gas gas_remaining - 25050 wei
                      args sha3(call.data[0 len calldata.size], mstor4m.length + 1)
                  require ext_call.success
                  if not ext_call.return_data[0]:
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                      require ext_call.success
                      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                           gas gas_remaining - 25050 wei
                          args 0x466561747572652069732064697361626c6564000000000000000000000000
                      return 0
          if uint8(mproxiesm[m_param3m]m.field_160):
              if not uint8(mproxiesm[m_param3m]m[1m]m[callerm]m.field_0):
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 'Access only through proxy'
                  require ext_call.success
                  return 0
          if not uint256(mallowancem[m_param3m]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Asset is not issued'
              require ext_call.success
              return 0
          if mstor4m.length + 1 == mstor4m.length + 1:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot approve to oneself'
              require ext_call.success
              return 0
          uint256(mallowancem[m_param3m]m[5m]m[mstor4m.length + 1m]m[1m]m[mstor4m.length + 1m]m.field_0) = m_param2
          call addr(meventsHistoryAddress).emitApprove(address from, address spender, bytes32 symbol, uint256 value) with:
               gas gas_remaining - 25050 wei
              args 0, uint32(mownerm[mstor4m.length + 1m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param3, m_param2
          require ext_call.success
          if addr(mproxiesm[m_param3m]m.field_0):
              uint8(mstor0m.field_160) = 1
              call addr(mproxiesm[m_param3m]m.field_0) with:
                 funct Mask(32, 224, sha3('emitApprove(address,address,uint', '256)')) >> 224
                   gas gas_remaining - 25050 wei
                  args addr(mownerm[mstor4m.length + 1m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param2
              if not ext_call.success:
                  require not uint8(mproxiesm[m_param3m]m.field_168)
              uint8(mstor0m.field_160) = 0
  return 1


# hash = 0x9fda5b66
# getter = ['struct', ['loc', 7]]
# const = None
# payable = True
def assets(bytes32 m_param1) payable: 
  mem[320] = uint256(mallowancem[m_param1m]m[2m]m.field_0)
  [94midx = 320
  [94ms = 0
  mwhile mallowancem[m_param1m]m[2m]m.length + 320 > [94midx + 32m:
      mem[[94midx + 32] = uint256(mallowancem[m_param1m]m[[94ms + 2m]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[mallowancem[m_param1m]m[2m]m.length + (floor32(mallowancem[m_param1m]m[2m]m.length - 1) + -mallowancem[m_param1m]m[2m]m.length + 32 % 32) + 320] = mallowancem[m_param1m]m[3m]m.length
  mem[mallowancem[m_param1m]m[2m]m.length + (floor32(mallowancem[m_param1m]m[2m]m.length - 1) + -mallowancem[m_param1m]m[2m]m.length + 32 % 32) + 352] = uint256(mallowancem[m_param1m]m[3m]m.field_0)
  [94midx = mallowancem[m_param1m]m[2m]m.length + (floor32(mallowancem[m_param1m]m[2m]m.length - 1) + -mallowancem[m_param1m]m[2m]m.length + 32 % 32) + 352
  [94ms = 0
  mwhile mallowancem[m_param1m]m[2m]m.length + (floor32(mallowancem[m_param1m]m[2m]m.length - 1) + -mallowancem[m_param1m]m[2m]m.length + 32 % 32) + mallowancem[m_param1m]m[3m]m.length + 352 > [94midx + 32m:
      mem[[94midx + 32] = uint256(mallowancem[m_param1m]m[[94ms + 3m]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return uint256(mallowancem[m_param1m]m.field_0), 
         uint256(mallowancem[m_param1m]m.field_256),
         Array(len=mallowancem[m_param1m]m[2m]m.length, data=mem[320 len mallowancem[m_param1m]m[2m]m.length + (floor32(mallowancem[m_param1m]m[2m]m.length - 1) + -mallowancem[m_param1m]m[2m]m.length + 32 % 32) + mallowancem[m_param1m]m[3m]m.length + (floor32(mallowancem[m_param1m]m[3m]m.length - 1) + -mallowancem[m_param1m]m[3m]m.length + 32 % 32) + 32]),
         mallowancem[m_param1m]m[2m]m.length + (floor32(mallowancem[m_param1m]m[2m]m.length - 1) + -mallowancem[m_param1m]m[2m]m.length + 32 % 32) + 224,
         bool(uint8(mallowancem[m_param1m]m.field_1024)),
         uint8(mallowancem[m_param1m]m.field_1024)


# hash = 0xa0f15b87
# getter = ['storage', 160, 0, 9]
# const = None
# payable = True
def registryICAP() payable: 
  return addr(mregistryICAPAddress)


# hash = 0xaeadd049
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = True
def unknownaeadd049(uint256 m_param1) payable: 
  return bool(uint8(mstor3m[m_param1m]))


# hash = 0xb524abcf
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 4], 7]]]]
# const = None
# payable = True
def totalSupply(bytes32 m_symbol) payable: 
  return uint256(mallowancem[m_symbolm]m.field_256)


# hash = 0xbb6e0e2c
# getter = None
# const = None
# payable = True
def unknownbb6e0e2c() payable: 
  if 0 == mholderIdm[callerm]:
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Didn't trust yet'
      require ext_call.success
      return 0
  if not uint256(mownerm[mstor6m[callerm]m]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Didn't trust yet'
      require ext_call.success
      return 0
  mem[0] = mholderIdm[callerm]
  mem[32] = 5
  [94ms = 0
  [94midx = 1
  mwhile [94midx <= uint256(mownerm[mstor6m[callerm]m]m.field_0)m:
      [94m_21 = sha3([94midx, sha3(mem[0 len 64]) + 2)
      uint256(mstor[sha3(mem[0 len 64]) + 3m]m[addr(mstor[sha3(mem[0 len 64]) + 2m]m[[94midxm])m]) = 0
      addr(mstor[sha3(mem[0 len 64]) + 2m]m[[94midxm]) = 0
      mem[0] = mholderIdm[callerm]
      mem[32] = 5
      [94ms = addr(mstor[[94m_21m])
      [94midx = [94midx + 1
      mcontinue 
  uint256(mownerm[mstor6m[callerm]m]m.field_0) = 0
  return 1


# hash = 0xbebcc045
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['add', 3, ['sha3', ['data', ['cd', 4], 7]]]]]], ['add', 3, ['sha3', ['data', ['cd', 4], 7]]]]]
# const = None
# payable = True
def description(bytes32 m_symbol) payable: 
  return uint256(mallowancem[m_symbolm]m[3m]m[0 len mallowancem[m_symbolm]m[3m]m.lengthm]m.field_0)


# hash = 0xc4eeeeb9
# getter = ['bool', ['storage', 8, 0, ['add', 4, ['sha3', ['data', ['cd', 4], 7]]]]]
# const = None
# payable = True
def isReissuable(bytes32 m_symbol) payable: 
  return bool(uint8(mallowancem[m_symbolm]m.field_1024))


# hash = 0xca448a88
# getter = None
# const = None
# payable = True
def revokeAsset(bytes32 m_symbol, uint256 m_value) payable: 
  if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_symbolm]):
      call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_symbolm]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
          require ext_call.success
          return 0
  else:
      if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
          call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
              require ext_call.success
              return 0
  if not uint256(mallowancem[m_symbolm]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if uint256(mallowancem[m_symbolm]m.field_0) != mholderIdm[callerm]:
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if not uint8(mstor3m[('map', ('param', '_symbol'), ('name', 'stor2', 2))m]):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x466561747572652069732064697361626c6564000000000000000000000000
      require ext_call.success
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      return 0
  if 0 == m_value:
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Cannot revoke 0 value'
      require ext_call.success
      return 0
  if uint256(mallowancem[m_symbolm]m[5m]m[mstor6m[callerm]m]m.field_0) < m_value:
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Not enough tokens to revoke'
      require ext_call.success
      return 0
  uint256(mallowancem[m_symbolm]m[5m]m[mstor6m[callerm]m]m.field_0) -= m_value
  uint256(mallowancem[m_symbolm]m.field_256) -= m_value
  call addr(meventsHistoryAddress).emitRevoke(bytes32 symbol, uint256 value, address by) with:
       gas gas_remaining - 25050 wei
      args m_symbol, m_value, addr(mownerm[mstor6m[callerm]m]m.field_256)
  require ext_call.success
  require addr(mstor0m.field_0) != 0
  [93mdelegate addr(mstor0m.field_0).0x32921690 with:
       gas gas_remaining - 50 wei
      args addr(mstor0m.field_0), 1
  require delegate.return_code
  require delegate.return_data[0]
  if addr(mproxiesm[m_symbolm]m.field_0):
      uint8(mstor0m.field_160) = 1
      call addr(mproxiesm[m_symbolm]m.field_0) with:
         funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
           gas gas_remaining - 25050 wei
          args addr(mownerm[mstor6m[callerm]m]m.field_256), addr(mownerm[0m]m.field_256), m_value
      if not ext_call.success:
          require not uint8(mproxiesm[m_symbolm]m.field_168)
      uint8(mstor0m.field_160) = 0
  return 1


# hash = 0xcbbc1bf3
# getter = None
# const = None
# payable = True
def unknowncbbc1bf3(uint256 m_param1) payable: 
  if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
      call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          return 0
  if mholderIdm[callerm] != 0:
      uint256(munknown4d1d2dbem[mstor6m[callerm]m]) = m_param1 or Mask(96, 160, uint256(munknown4d1d2dbem[mstor6m[callerm]m]))
  else:
      mstor4m.length++
      addr(mownerm[mstor4m.length + 1m]m.field_256) = caller
      mholderIdm[callerm] = mstor4m.length + 1
      uint256(munknown4d1d2dbem[mstor4m.length + 1m]) = m_param1 or Mask(96, 160, uint256(munknown4d1d2dbem[mstor4m.length + 1m]))
  return 1


# hash = 0xce606ee0
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def contractOwner() payable: 
  return addr(mstor1m.length)


# hash = 0xdc86e6f0
# getter = ['storage', 8, 8, ['add', 4, ['sha3', ['data', ['cd', 4], 7]]]]
# const = None
# payable = True
def baseUnit(bytes32 m_symbol) payable: 
  return uint8(mallowancem[m_symbolm]m.field_1032)


# hash = 0xe0873c06
# getter = None
# const = None
# payable = True
def reissueAsset(bytes32 m_symbol, uint256 m_value) payable: 
  if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_symbolm]):
      call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_symbolm]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
          require ext_call.success
          return 0
  else:
      if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
          call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
              require ext_call.success
              return 0
  if not uint256(mallowancem[m_symbolm]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if uint256(mallowancem[m_symbolm]m.field_0) != mholderIdm[callerm]:
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if 0 == m_value:
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Cannot reissue 0 value'
      require ext_call.success
      return 0
  if not uint8(mallowancem[m_symbolm]m.field_1024):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Cannot reissue fixed asset'
      require ext_call.success
      return 0
  if m_value + uint256(mallowancem[m_symbolm]m.field_256) < uint256(mallowancem[m_symbolm]m.field_256):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Total supply overflow'
      require ext_call.success
      return 0
  uint256(mallowancem[m_symbolm]m[5m]m[mstor6m[callerm]m]m.field_0) += m_value
  uint256(mallowancem[m_symbolm]m.field_256) += m_value
  call addr(meventsHistoryAddress).emitIssue(bytes32 symbol, uint256 value, address by) with:
       gas gas_remaining - 25050 wei
      args m_symbol, m_value, addr(mownerm[mstor6m[callerm]m]m.field_256)
  require ext_call.success
  require addr(mstor0m.field_0) != 0
  [93mdelegate addr(mstor0m.field_0).0x32921690 with:
       gas gas_remaining - 50 wei
      args addr(mstor0m.field_0), 1
  require delegate.return_code
  require delegate.return_data[0]
  if addr(mproxiesm[m_symbolm]m.field_0):
      uint8(mstor0m.field_160) = 1
      call addr(mproxiesm[m_symbolm]m.field_0) with:
         funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
           gas gas_remaining - 25050 wei
          args addr(mownerm[0m]m.field_256), addr(mownerm[mstor6m[callerm]m]m.field_256), m_value
      if not ext_call.success:
          require not uint8(mproxiesm[m_symbolm]m.field_168)
      uint8(mstor0m.field_160) = 0
  return 1


# hash = 0xe82b7cb2
# getter = None
# const = None
# payable = True
def unknowne82b7cb2(uint256 m_param1, uint256 m_param2) payable: 
  if not uint8(mproxiesm[m_param2m]m[1m]m[callerm]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if uint8(mstor0m.field_160):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param2m]):
      call addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param2m]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args code.data[14790 len 32]
          return 0
  else:
      if addr(munknown4d1d2dbem[mstor6m[tx.originm]m]):
          call addr(munknown4d1d2dbem[mstor6m[tx.originm]m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args code.data[14790 len 32]
              return 0
  if mholderIdm[tx.originm] != 0:
      uint256(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param2m]) = m_param1 or Mask(96, 160, uint256(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param2m]))
  else:
      mstor4m.length++
      uint256(mownerm[mstor4m.length + 1m]m.field_256) = tx.origin or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
      mholderIdm[tx.originm] = mstor4m.length + 1
      uint256(munknown4d1d2dbem[mstor4m.length + 1m][m_param2m]) = m_param1 or Mask(96, 160, uint256(munknown4d1d2dbem[mstor4m.length + 1m][m_param2m]))
  return 1


# hash = 0xe96b462a
# getter = None
# const = None
# payable = True
def isOwner(address m_owner, bytes32 m_symbol) payable: 
  if not uint256(mallowancem[m_symbolm]m.field_0):
      return not not uint256(mallowancem[m_symbolm]m.field_0)
  return (uint256(mallowancem[m_symbolm]m.field_0) == mholderIdm[addr(m_owner)m])


# hash = 0xf01b0220
# getter = None
# const = None
# payable = True
def unknownf01b0220(uint256 m_param1, uint128 m_param2, uint256 m_param3) payable: 
  if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]):
      call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_param3m]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
          require ext_call.success
          return 0
  else:
      if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
          call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
              require ext_call.success
              return 0
  if not uint256(mallowancem[m_param3m]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if uint256(mallowancem[m_param3m]m.field_0) != mholderIdm[callerm]:
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if m_param1:
      if uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m.field_0) != uint256(mallowancem[m_param3m]m.field_256):
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot set with holders'
          require ext_call.success
          return 0
  else:
      if m_param2:
          if uint256(mallowancem[m_param3m]m[5m]m[mstor6m[callerm]m]m.field_0) != uint256(mallowancem[m_param3m]m.field_256):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Cannot set with holders'
              require ext_call.success
              return 0
  uint8(mproxiesm[m_param3m]m.field_160) = uint8(m_param1)
  Mask(88, 0, mproxiesm[m_param3m]m.field_168) = Mask(88, 0, m_param2)
  Mask(80, 0, mproxiesm[m_param3m]m.field_176) = Mask(80, 16, m_param1) >> 16
  Mask(80, 0, mproxiesm[m_param3m]m.field_176) = 0
  return 1


# hash = 0xf07629f8
# getter = ['storage', 160, 0, 10]
# const = None
# payable = True
def eventsHistory() payable: 
  return addr(meventsHistoryAddress)


# hash = 0xf0c06aa5
# getter = None
# const = None
# payable = True
def distrust(address m_dealer) payable: 
  if not uint256(mownerm[mstor6m[callerm]m]m[3m]m[addr(m_dealer)m]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 'Only trusted: access denied'
      require ext_call.success
      return 0
  if uint256(mownerm[mstor6m[callerm]m]m[3m]m[addr(m_dealer)m]m.field_0) < uint256(mownerm[mstor6m[callerm]m]m.field_0):
      addr(mownerm[mstor6m[callerm]m]m[2m]m[uint256(mownerm[mstor6m[callerm]m]m[3m]m[addr(m_dealer)m]m.field_0)m]m.field_0) = addr(mownerm[mstor6m[callerm]m]m[2m]m[uint256(mownerm[mstor6m[callerm]m]m.field_0)m]m.field_0)
      uint256(mownerm[mstor6m[callerm]m]m[3m]m[addr(mownerm[mstor6m[callerm]m]m[2m]m[uint256(mownerm[mstor6m[callerm]m]m.field_0)m]m.field_0)m]m.field_0) = uint256(mownerm[mstor6m[callerm]m]m[3m]m[addr(m_dealer)m]m.field_0)
  uint256(mownerm[mstor6m[callerm]m]m.field_0)--
  addr(mownerm[mstor6m[callerm]m]m[2m]m[uint256(mownerm[mstor6m[callerm]m]m.field_0) - 1m]m.field_0) = 0
  uint256(mownerm[mstor6m[callerm]m]m[3m]m[addr(m_dealer)m]m.field_0) = 0
  return 1


# hash = 0xf0cbe059
# getter = None
# const = None
# payable = True
def unknownf0cbe059(addr m_param1, addr m_param2, uint256 m_param3, uint256 m_param4, array m_param5) payable: 
  if not uint8(mproxiesm[m_param4m]m[1m]m[callerm]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if uint8(mstor0m.field_160):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args code.data[14790 len 32]
      require ext_call.success
      return 0
  if mholderIdm[addr(m_param2)m] != 0:
      if addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param4m]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param4m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[tx.originm]m]):
              call addr(munknown4d1d2dbem[mstor6m[tx.originm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_param4m]m.field_160):
          if not uint8(mproxiesm[m_param4m]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[addr(m_param1)m] == mholderIdm[addr(m_param2)m]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_param3:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m.field_0) < m_param3:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if m_param5.length > 0:
          if not uint8(mstor3m[('map', ('param', '_param4'), ('name', 'stor1', 1))m]):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if mholderIdm[addr(m_param1)m] != mholderIdm[tx.originm]:
          if uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m[1m]m[mstor6m[tx.originm]m]m.field_0) < m_param3:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m.field_0) -= m_param3
      uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param2)m]m]m.field_0) += m_param3
      if mholderIdm[tx.originm] != mholderIdm[addr(m_param1)m]:
          uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m[1m]m[mstor6m[tx.originm]m]m.field_0) -= m_param3
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), addr(mownerm[mstor6m[addr(m_param2)m]m]m.field_256), m_param4, m_param3, Array(len=m_param5.length, data=m_param5[allm])
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_param4m]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_param4m]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), addr(mownerm[mstor6m[addr(m_param2)m]m]m.field_256), m_param3
          if not ext_call.success:
              require not uint8(mproxiesm[m_param4m]m.field_168)
          uint8(mstor0m.field_160) = 0
  else:
      mstor4m.length++
      uint256(mownerm[mstor4m.length + 1m]m.field_256) = m_param2 or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
      mholderIdm[addr(m_param2)m] = mstor4m.length + 1
      if addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param4m]) != 0:
          call addr(munknown4d1d2dbem[mstor6m[tx.originm]m][m_param4m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              return 0
      else:
          if addr(munknown4d1d2dbem[mstor6m[tx.originm]m]):
              call addr(munknown4d1d2dbem[mstor6m[tx.originm]m]).0xa25035b with:
                   gas gas_remaining - 25050 wei
                  args sha3(call.data[0 len calldata.size], mholderIdm[tx.originm])
              require ext_call.success
              if not ext_call.return_data[0]:
                  call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                       gas gas_remaining - 25050 wei
                      args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
                  require ext_call.success
                  return 0
      if uint8(mproxiesm[m_param4m]m.field_160):
          if not uint8(mproxiesm[m_param4m]m[1m]m[callerm]m.field_0):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Access only through proxy'
              require ext_call.success
              return 0
      if mholderIdm[addr(m_param1)m] == mstor4m.length + 1:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send to oneself'
          require ext_call.success
          return 0
      if 0 == m_param3:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot send 0 value'
          require ext_call.success
          return 0
      if uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m.field_0) < m_param3:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Insufficient balance'
          require ext_call.success
          return 0
      if m_param5.length > 0:
          if not uint8(mstor3m[('map', ('param', '_param4'), ('name', 'stor1', 1))m]):
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'References feature is disabled'
              require ext_call.success
              return 0
      if mholderIdm[addr(m_param1)m] != mholderIdm[tx.originm]:
          if uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m[1m]m[mstor6m[tx.originm]m]m.field_0) < m_param3:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 'Not enough allowance'
              require ext_call.success
              return 0
      uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m.field_0) -= m_param3
      uint256(mallowancem[m_param4m]m[5m]m[mstor4m.length + 1m]m.field_0) += m_param3
      if mholderIdm[tx.originm] != mholderIdm[addr(m_param1)m]:
          uint256(mallowancem[m_param4m]m[5m]m[mstor6m[addr(m_param1)m]m]m[1m]m[mstor6m[tx.originm]m]m.field_0) -= m_param3
      call addr(meventsHistoryAddress).emitTransfer(address from, address to, bytes32 symbol, uint256 value, string reference) with:
           gas gas_remaining - 25050 wei
          args addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param4, m_param3, Array(len=m_param5.length, data=m_param5[allm])
      require ext_call.success
      require addr(mstor0m.field_0) != 0
      [93mdelegate addr(mstor0m.field_0).0x32921690 with:
           gas gas_remaining - 50 wei
          args addr(mstor0m.field_0), 1
      require delegate.return_code
      require delegate.return_data[0]
      if addr(mproxiesm[m_param4m]m.field_0):
          uint8(mstor0m.field_160) = 1
          call addr(mproxiesm[m_param4m]m.field_0) with:
             funct Mask(32, 224, sha3('emitTransfer(address,address,uin', 't256)')) >> 224
               gas gas_remaining - 25050 wei
              args addr(mownerm[mstor6m[addr(m_param1)m]m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_param3
          if not ext_call.success:
              require not uint8(mproxiesm[m_param4m]m.field_168)
          uint8(mstor0m.field_160) = 0
  return 1


# hash = 0xfd83915e
# getter = None
# const = None
# payable = True
def changeOwnership(bytes32 m_symbol, address m_newOwner) payable: 
  if addr(munknown4d1d2dbem[mstor6m[callerm]m][m_symbolm]):
      call addr(munknown4d1d2dbem[mstor6m[callerm]m][m_symbolm]).0xa25035b with:
           gas gas_remaining - 25050 wei
          args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
      require ext_call.success
      if not ext_call.return_data[0]:
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
          require ext_call.success
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
          require ext_call.success
          return 0
  else:
      if addr(munknown4d1d2dbem[mstor6m[callerm]m]):
          call addr(munknown4d1d2dbem[mstor6m[callerm]m]).0xa25035b with:
               gas gas_remaining - 25050 wei
              args sha3(call.data[0 len calldata.size], mholderIdm[callerm])
          require ext_call.success
          if not ext_call.return_data[0]:
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x4f7065726174696f6e206973206e6f7420636f7369676e6564000000000000
              require ext_call.success
              call addr(meventsHistoryAddress).emitError(bytes32 message) with:
                   gas gas_remaining - 25050 wei
                  args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
              require ext_call.success
              return 0
  if not uint256(mallowancem[m_symbolm]m.field_0):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if uint256(mallowancem[m_symbolm]m.field_0) != mholderIdm[callerm]:
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      require ext_call.success
      return 0
  if not uint8(mstor3m[('map', ('param', '_symbol'), ('name', 'stor3', 3))m]):
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x466561747572652069732064697361626c6564000000000000000000000000
      require ext_call.success
      call addr(meventsHistoryAddress).emitError(bytes32 message) with:
           gas gas_remaining - 25050 wei
          args 0x564f6e6c79206f776e65723a206163636573732064656e696564000000000000
      return 0
  if mholderIdm[addr(m_newOwner)m] != 0:
      if mholderIdm[addr(m_newOwner)m] == uint256(mallowancem[m_symbolm]m.field_0):
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot pass ownership to oneself'
          require ext_call.success
          return 0
      uint256(mallowancem[m_symbolm]m.field_0) = mholderIdm[addr(m_newOwner)m]
      call addr(meventsHistoryAddress).emitOwnershipChange(address from, address to, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(mownerm[uint256(mstor7m[m_symbolm]m.field_0)m]m.field_256), addr(mownerm[mstor6m[addr(m_newOwner)m]m]m.field_256), m_symbol
  else:
      mstor4m.length++
      uint256(mownerm[mstor4m.length + 1m]m.field_256) = m_newOwner or Mask(96, 160, uint256(mownerm[mstor4m.length + 1m]m.field_256))
      mholderIdm[addr(m_newOwner)m] = mstor4m.length + 1
      if mstor4m.length + 1 == uint256(mallowancem[m_symbolm]m.field_0):
          call addr(meventsHistoryAddress).emitError(bytes32 message) with:
               gas gas_remaining - 25050 wei
              args 'Cannot pass ownership to oneself'
          require ext_call.success
          return 0
      uint256(mallowancem[m_symbolm]m.field_0) = mstor4m.length + 1
      call addr(meventsHistoryAddress).emitOwnershipChange(address from, address to, bytes32 symbol) with:
           gas gas_remaining - 25050 wei
          args addr(mownerm[uint256(mstor7m[m_symbolm]m.field_0)m]m.field_256), addr(mownerm[mstor4m.length + 1m]m.field_256), m_symbol
  require ext_call.success
  return 1


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


