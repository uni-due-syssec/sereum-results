# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x771500be2e5F90443ca6BF6147FDCc9dDCe2EE4a 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown45ddc85d
    # storage address 1
    stor1 # mask: a s
    # storage address 1
    rulesAddress # mask: a s
# hash = 0x013cf08b
# getter = None
# const = None
# payable = True
def proposals(uint256 m_param1) payable: 
  require m_param1 < munknown45ddc85dm.length
  mem[384] = uint256(munknown45ddc85dm[m_param1m]m.field_0)
  [94midx = 384
  [94ms = 0
  mwhile munknown45ddc85dm[m_param1m]m.length + 384 > [94midx + 32m:
      mem[[94midx + 32] = uint256(munknown45ddc85dm[(11 * m_param1) + [94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return Array(len=munknown45ddc85dm[m_param1m]m.length, data=mem[384 len munknown45ddc85dm[m_param1m]m.length + (floor32(munknown45ddc85dm[m_param1m]m.length - 1) + -munknown45ddc85dm[m_param1m]m.length + 32 % 32)]), 
         addr(munknown45ddc85dm[m_param1m]m.field_256),
         addr(munknown45ddc85dm[m_param1m]m.field_512),
         uint256(munknown45ddc85dm[m_param1m]m.field_768),
         uint256(munknown45ddc85dm[m_param1m]m.field_1024),
         bool(uint8(munknown45ddc85dm[m_param1m]m.field_1280)),
         uint256(munknown45ddc85dm[m_param1m]m.field_1536),
         uint256(munknown45ddc85dm[m_param1m]m.field_1792)


# hash = 0x400e3949
# getter = ['storage', 256, 0, 0]
# const = None
# payable = True
def numProposals() payable: 
  return munknown45ddc85dm.length


# hash = 0x43859632
# getter = None
# const = None
# payable = True
def hasVoted(uint256 m_proposalNumber, address m_shareholder) payable: 
  require m_proposalNumber < munknown45ddc85dm.length
  if uint256(mstor[(11 * m_proposalNumber) + ('name', 'unknown45ddc85d', 0) + 9m]m[addr(m_shareholder)m]m.field_512) <= 0:
      return 0
  return 1


# hash = 0x45ddc85d
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['add', 9, ['mul', 11, ['cd', 4]], ['sha3', 0]]]]]
# const = None
# payable = True
def unknown45ddc85d(uint256 m_param1, addr m_param2) payable: 
  require m_param1 < munknown45ddc85dm.length
  return uint256(mstor[(11 * m_param1) + ('name', 'unknown45ddc85d', 0) + 9m]m[addr(m_param2)m]m.field_0), 
         uint256(mstor[(11 * m_param1) + ('name', 'unknown45ddc85d', 0) + 9m]m[addr(m_param2)m]m.field_256),
         uint256(mstor[(11 * m_param1) + ('name', 'unknown45ddc85d', 0) + 9m]m[addr(m_param2)m]m.field_512)


# hash = 0x52f6747a
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def rules() payable: 
  return addr(mrulesAddress)


# hash = 0x59efcb15
# getter = None
# const = None
# payable = True
def unknown59efcb15(uint256 m_param1, array m_param2) payable: 
  mem[128 len m_param2.length] = m_param2[allm]
  call addr(mrulesAddress).0x75eeadc3 with:
       gas gas_remaining - 25050 wei
      args m_param1
  require ext_call.success
  if ext_call.return_data[0]:
      require m_param1 < munknown45ddc85dm.length
      if not uint8(munknown45ddc85dm[m_param1m]m.field_1280):
          mem[ceil32(m_param2.length) + 128] = addr(munknown45ddc85dm[m_param1m]m.field_256)
          mem[ceil32(m_param2.length) + 148] = uint256(munknown45ddc85dm[m_param1m]m.field_768)
          mem[ceil32(m_param2.length) + 180 len m_param2.length] = m_param2[allm]
          if sha3(addr(munknown45ddc85dm[m_param1m]m.field_256), uint256(munknown45ddc85dm[m_param1m]m.field_768), m_param2[allm]) == uint256(munknown45ddc85dm[m_param1m]m.field_1024):
              uint8(munknown45ddc85dm[m_param1m]m.field_1280) = 1
              if addr(munknown45ddc85dm[m_param1m]m.field_512):
                  call addr(munknown45ddc85dm[m_param1m]m.field_512).0x9f0b17e3 with:
                       gas gas_remaining - 25050 wei
                      args addr(munknown45ddc85dm[m_param1m]m.field_256), uint256(munknown45ddc85dm[m_param1m]m.field_768), Array(len=m_param2.length, data=m_param2[allm])
                  require ext_call.success
              else:
                  mem[ceil32(m_param2.length) + 128 len m_param2.length] = m_param2[allm]
                  if not m_param2.length % 32:
                      call addr(munknown45ddc85dm[m_param1m]m.field_256) with:
                         value uint256(munknown45ddc85dm[m_param1m]m.field_768) wei
                           gas gas_remaining - 34050 wei
                          args m_param2[allm]
                  else:
                      mem[floor32(m_param2.length) + ceil32(m_param2.length) + 128] = mem[floor32(m_param2.length) + ceil32(m_param2.length) + -(m_param2.length % 32) + 160 len m_param2.length % 32]
                      call addr(munknown45ddc85dm[m_param1m]m.field_256).mem[ceil32(m_param2.length) + 128 len 4] with:
                         value uint256(munknown45ddc85dm[m_param1m]m.field_768) wei
                           gas gas_remaining - 34050 wei
                          args mem[ceil32(m_param2.length) + 132 len floor32(m_param2.length) + 28]
                  require ext_call.success
              log 0x9c85b616: _param1, caller


# hash = 0x7a43cb62
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['add', 8, ['mul', 11, ['cd', 4]], ['sha3', 0]]]]]
# const = None
# payable = True
def unknown7a43cb62(uint256 m_param1, uint256 m_param2) payable: 
  require m_param1 < munknown45ddc85dm.length
  return uint256(mstor[(11 * m_param1) + ('name', 'unknown45ddc85d', 0) + 8m]m[m_param2m]m.field_0)


# hash = 0x9be6d404
# getter = None
# const = None
# payable = True
def unknown9be6d404(addr m_param1) payable: 
  if this.address != caller:
      stop
  [93mselfdestruct([91m_param1[93m)


# hash = 0xa294ed7a
# getter = ['storage', 160, 0, ['add', ['cd', 36], ['sha3', ['add', 10, ['mul', 11, ['cd', 4]], ['sha3', 0]]]]]
# const = None
# payable = True
def unknowna294ed7a(uint256 m_param1, uint256 m_param2) payable: 
  require m_param1 < munknown45ddc85dm.length
  require m_param2 < uint256(munknown45ddc85dm[m_param1m]m.field_2560)
  return addr(mstor[m_param2 + sha3((11 * m_param1) + ('name', 'unknown45ddc85d', 0) + 10)m]m.field_0)


# hash = 0xa4b195ff
# getter = ['storage', 256, 0, ['add', 10, ['mul', 11, ['cd', 4]], ['sha3', 0]]]
# const = None
# payable = True
def numVoters(uint256 m_param1) payable: 
  require m_param1 < munknown45ddc85dm.length
  return uint256(munknown45ddc85dm[m_param1m]m.field_2560)


# hash = 0xb384abef
# getter = None
# const = None
# payable = True
def vote(uint256 m_fightID, uint256 m_fighter) payable: 
  call addr(mrulesAddress).0x19eb8d48 with:
       gas gas_remaining - 25050 wei
      args caller, m_fightID
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  call addr(mrulesAddress).0x60dddfb1 with:
       gas gas_remaining - 25050 wei
      args caller, m_fightID
  require ext_call.success
  require m_fightID < munknown45ddc85dm.length
  uint256(mstor[(11 * m_fightID) + ('name', 'unknown45ddc85d', 0) + 9m]m[callerm]m.field_0) = m_fighter
  uint256(mstor[(11 * m_fightID) + ('name', 'unknown45ddc85d', 0) + 9m]m[callerm]m.field_256) = ext_call.return_data[0]
  uint256(mstor[(11 * m_fightID) + ('name', 'unknown45ddc85d', 0) + 9m]m[callerm]m.field_512) = block.timestamp
  uint256(munknown45ddc85dm[m_fightIDm]m.field_2560)++
  if not uint256(munknown45ddc85dm[m_fightIDm]m.field_2560) <= uint256(munknown45ddc85dm[m_fightIDm]m.field_2560) + 1:
      [94midx = uint256(munknown45ddc85dm[m_fightIDm]m.field_2560) + 1
      mwhile uint256(munknown45ddc85dm[m_fightIDm]m.field_2560) > [94midxm:
          uint256(mstor[[94midx + sha3((11 * m_fightID) + ('name', 'unknown45ddc85d', 0) + 10)m]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 
  addr(mstor[uint256(munknown45ddc85dm[m_fightIDm]m.field_2560) + sha3((11 * m_fightID) + ('name', 'unknown45ddc85d', 0) + 10)m]m.field_0) = caller
  require m_fightID < munknown45ddc85dm.length
  uint256(mstor[(11 * m_fightID) + ('name', 'unknown45ddc85d', 0) + 8m]m[m_fighterm]m.field_0) += ext_call.return_data[0]
  log 0xcb5cd4ec: _fightID, _fighter, caller
  return ext_call.return_data[0]


# hash = 0xc3aeacdf
# getter = None
# const = None
# payable = True
def unknownc3aeacdf(uint256 m_param1) payable: 
  if caller == this.address:
      uint256(mstor1) = m_param1 or Mask(96, 160, uint256(mstor1))


# hash = 0xef41f95a
# getter = None
# const = None
# payable = True
def unknownef41f95a(array m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5, array m_param6) payable: 
  call addr(mrulesAddress).0x42b4632e with:
       gas gas_remaining - 25050 wei
      args caller
  require ext_call.success
  if not ext_call.return_data[0]:
      return 0
  munknown45ddc85dm.length++
  if not munknown45ddc85dm.length <= munknown45ddc85dm.length + 1:
      mem[0] = 0
      [94midx = (11 * munknown45ddc85dm.length) + 11
      mwhile sha3(0) + (11 * munknown45ddc85dm.length) > [94midx + sha3(mem[0])m:
          uint256(mstor[[94midx + sha3(mem[0])m]) = 0
          if 31 < mstor[[94midx + sha3(mem[0])m]m.length:
              [94ms = sha3([94midx + sha3(mem[0]))
              mwhile sha3([94midx + sha3(mem[0])) + (mstor[[94midx + sha3(mem[0])m]m.length + 31 / 32) > [94msm:
                  uint256(mstor[[94msm]) = 0
                  [94ms = [94ms + 1
                  mcontinue 
          addr(mstor[[94midx + sha3(mem[0]) + 1m]) = 0
          addr(mstor[[94midx + sha3(mem[0]) + 2m]) = 0
          uint256(mstor[[94midx + sha3(mem[0]) + 3m]) = 0
          uint256(mstor[[94midx + sha3(mem[0]) + 4m]) = 0
          uint8(mstor[[94midx + sha3(mem[0]) + 5m]) = 0
          uint256(mstor[[94midx + sha3(mem[0]) + 6m]) = 0
          uint256(mstor[[94midx + sha3(mem[0]) + 7m]) = 0
          uint256(mstor[[94midx + sha3(mem[0]) + 10m]) = 0
          mem[0] = [94midx + sha3(mem[0]) + 10
          [94ms = sha3([94midx + sha3(mem[0]) + 10)
          mwhile sha3([94midx + sha3(mem[0]) + 10) + uint256(mstor[[94midx + sha3(mem[0]) + 10m]) > [94msm:
              uint256(mstor[[94msm]) = 0
              [94ms = [94ms + 1
              mcontinue 
          [94midx = [94midx + 11
          mcontinue 
  require munknown45ddc85dm.length < munknown45ddc85dm.length
  uint256(munknown45ddc85dm[munknown45ddc85dm.lengthm]m[m]m.field_0) = Array(len=m_param1.length, data=m_param1[allm])
  uint256(munknown45ddc85dm[munknown45ddc85dm.lengthm]m.field_256) = m_param4 or Mask(96, 160, uint256(munknown45ddc85dm[munknown45ddc85dm.lengthm]m.field_256))
  uint256(munknown45ddc85dm[munknown45ddc85dm.lengthm]m.field_768) = m_param5
  uint256(munknown45ddc85dm[munknown45ddc85dm.lengthm]m.field_512) = m_param2 or Mask(96, 160, uint256(munknown45ddc85dm[munknown45ddc85dm.lengthm]m.field_512))
  uint256(munknown45ddc85dm[munknown45ddc85dm.lengthm]m.field_1024) = sha3(addr(m_param4), m_param5, m_param6[allm])
  uint256(munknown45ddc85dm[munknown45ddc85dm.lengthm]m.field_1536) = 24 * 3600 * m_param3
  uint256(munknown45ddc85dm[munknown45ddc85dm.lengthm]m.field_1792) = block.timestamp
  log 0x3417b456: unknown45ddc85d.length, addr(_param4), _param5
  return munknown45ddc85dm.length


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


