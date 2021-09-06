# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x2eb60c101c174cCb4F0dD8a202C9FC722A9a554a 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 3
    name
    # storage address 24
    stor24
    # storage address 20
    stor20
    # storage address 21
    stor21
    # storage address 17
    currentCheckpointId # mask: a s
    # storage address 18
    stor18 # mask: a s
    # storage address 18
    unknown7a802c71 # mask: a s
    # storage address 18
    transfersFrozen # mask: a s
    # storage address 18
    unknowna284de02 # mask: a s
    # storage address 18
    controllerAddress # mask: a s
    # storage address 18
    stor18 # mask: a s
    # storage address 2
    allowance
    # storage address 8
    securityTokenRegistryAddress # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 19
    stor19
    # storage address 15
    tokenDetails
    # storage address 5253140328063329608286456456021344790776737700239285610539250288183334476067
    stor5253140328063329608286456456021344790776737700239285610539250288183334476067
    # storage address 9
    unknowncaf90dabAddress # mask: a s
    # storage address 9
    stor9 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    decimals # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 5
    owner # mask: a s
    # storage address 1
    totalSupply # mask: a s
    # storage address 10
    stor10 # mask: a s
    # storage address 10
    proofTokenAddress # mask: a s
    # storage address 12
    stor12
    # storage address 0
    balanceOf
    # storage address 6
    unknown5aa14a70Address # mask: a s
    # storage address 7
    moduleRegistryAddress # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 80167465652159884487584418398737133515478493586045375474096367959472086682926
    stor80167465652159884487584418398737133515478493586045375474096367959472086682926
    # storage address 4
    symbol
    # storage address 16
    granularity # mask: a s
    # storage address 13
    investorCount # mask: a s
# hash = 0x01502460
# getter = None
# const = None
# payable = False
def freezeTransfers(): # not payable
  require caller == mowner
  if mtransfersFrozen:
      revert with 0, 'Already frozen'
  mtransfersFrozen = 1
  log 0x4f1ca1e6: 1, block.timestamp


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 3]]]], ['loc', 3]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address m_spender, uint256 m_value): # not payable
  mallowancem[callerm]m[addr(m_spender)m] = m_value
  log Approval(
        address owner=_value,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x0d8e6e2c
# getter = None
# const = ['return', ['data', ['arr', 3, ['mem', ['range', 288, 96]]]]]
# payable = False
const getVersion = Array(len=3, data=mem[288 len 96])


# hash = 0x0e94a0ee
# getter = ['storage', 160, 0, 10]
# const = None
# payable = False
def proofToken(): # not payable
  return addr(mproofTokenAddress)


# hash = 0x12ef7fe2
# getter = None
# const = None
# payable = False
def unknown12ef7fe2(addr m_param1): # not payable
  require caller == mowner
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x4e5ba926 with:
       gas gas_remaining wei
      args sha3(addr(m_param1), 20), m_param1
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def totalSupply(): # not payable
  return mtotalSupply


# hash = 0x210a8d0e
# getter = None
# const = None
# payable = False
def changeGranularity(uint256 m_granularity): # not payable
  require caller == mowner
  if not m_granularity:
      revert with 0, 'Invalid granularity'
  log 0x7728e5c4: granularity, _granularity
  mgranularity = m_granularity


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_value): # not payable
  mem[64] = 128
  mem[96] = 0
  require not uint8(mstor5m.field_8)
  uint8(mstor5m.field_8) = 1
  mem[128] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
  mem[132] = 11
  mem[164] = m_from
  mem[196] = m_to
  mem[228] = m_value
  mem[260] = mbalanceOfm[addr(m_to)m]
  mem[292] = mbalanceOfm[addr(m_from)m]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
       gas gas_remaining wei
      args 0, 11, addr(m_from), addr(m_to), m_value, mbalanceOfm[addr(m_to)m], mbalanceOfm[addr(m_from)m]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mgranularity
  if m_value % mgranularity:
      revert with 0, 'Invalid granularity'
  if mtransfersFrozen:
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_from), 22), mbalanceOfm[addr(m_from)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      uint8(mstor5m.field_8) = 0
      revert with 0, 'Transfer invalid'
  mem[0] = 2
  mem[32] = 19
  [94ms = 0
  [94midx = 0
  [94mt = 0
  [94mt = 0
  [94mu = 0
  mwhile [94midx < mstorB9D2m.lengthm:
      if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
          mem[0] = 2
          mem[32] = 19
          [94ms = [94ms
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = [94mt
          [94mu = [94mu
          mcontinue 
      mem[128] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
      mem[132] = m_from
      mem[164] = m_to
      mem[196] = m_value
      mem[260] = 1
      mem[228] = 160
      mem[292] = mem[96]
      [94ms = 0
      mwhile [94ms < mem[96]m:
          mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
          mem[0] = 2
          mem[32] = 19
          [94ms = [94ms + 32
          mcontinue 
      if not mem[96] % 32:
          require ext_code.size(mstorB9D2m[[94midxm])
          call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
               gas gas_remaining wei
              args mem[mem[64] + 4 len mem[96] + -mem[64] + 320]
      else:
          mem[floor32(mem[96]) + 324] = mem[floor32(mem[96]) + -(mem[96] % 32) + 356 len mem[96] % 32]
          require ext_code.size(mstorB9D2m[[94midxm])
          call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
               gas gas_remaining wei
              args mem[mem[64] + 4 len floor32(mem[96]) + -mem[64] + 352]
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0] <= 3
      if not ext_call.return_data[0]:
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = 1
          mcontinue 
      require ext_call.return_data[0] <= 3
      if ext_call.return_data[0] != 2:
          require ext_call.return_data[0] <= 3
      mem[0] = 2
      mem[32] = 19
      [94ms = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94mt = mstorB9D2m[[94midxm]
      [94mt = 1
      [94mu = [94mu
      mcontinue 
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(addr(m_from), 22), mbalanceOfm[addr(m_from)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  uint8(mstor5m.field_8) = 0
  if [94mt:
      revert with 0, 'Transfer invalid'
  require m_to
  require m_value <= mbalanceOfm[addr(m_from)m]
  require m_value <= mallowancem[addr(m_from)m]m[callerm]
  require m_value <= mbalanceOfm[addr(m_from)m]
  mbalanceOfm[addr(m_from)m] -= m_value
  require m_value + mbalanceOfm[m_tom] >= mbalanceOfm[m_tom]
  mbalanceOfm[addr(m_to)m] = m_value + mbalanceOfm[m_tom]
  require m_value <= mallowancem[addr(m_from)m]m[callerm]
  mallowancem[addr(m_from)m]m[callerm] -= m_value
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 value=_to)
  return 1


# hash = 0x2535f762
# getter = None
# const = None
# payable = False
def transferWithData(address m_to, uint256 m_value, bytes m_data): # not payable
  mem[64] = ceil32(m_data.length) + 128
  mem[96] = m_data.length
  mem[128 len m_data.length] = m_data[allm]
  require not uint8(mstor5m.field_8)
  uint8(mstor5m.field_8) = 1
  mem[ceil32(m_data.length) + 128] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
  mem[ceil32(m_data.length) + 132] = 11
  mem[ceil32(m_data.length) + 164] = caller
  mem[ceil32(m_data.length) + 196] = m_to
  mem[ceil32(m_data.length) + 228] = m_value
  mem[ceil32(m_data.length) + 260] = mbalanceOfm[addr(m_to)m]
  mem[ceil32(m_data.length) + 292] = mbalanceOfm[callerm]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
       gas gas_remaining wei
      args 11, caller, addr(m_to), m_value, mbalanceOfm[addr(m_to)m], mbalanceOfm[callerm]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mgranularity
  if m_value % mgranularity:
      revert with 0, 'Invalid granularity'
  if mtransfersFrozen:
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(caller, 22), mbalanceOfm[callerm], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      uint8(mstor5m.field_8) = 0
      revert with 0, 'Transfer invalid'
  mem[0] = 2
  mem[32] = 19
  [94ms = 0
  [94midx = 0
  [94mt = 0
  [94mt = 0
  [94mu = 0
  mwhile [94midx < mstorB9D2m.lengthm:
      if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
          mem[0] = 2
          mem[32] = 19
          [94ms = [94ms
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = [94mt
          [94mu = [94mu
          mcontinue 
      mem[ceil32(m_data.length) + 128] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
      mem[ceil32(m_data.length) + 132] = caller
      mem[ceil32(m_data.length) + 164] = m_to
      mem[ceil32(m_data.length) + 196] = m_value
      mem[ceil32(m_data.length) + 260] = 1
      mem[ceil32(m_data.length) + 228] = 160
      mem[ceil32(m_data.length) + 292] = mem[96]
      [94ms = 0
      mwhile [94ms < mem[96]m:
          mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
          mem[0] = 2
          mem[32] = 19
          [94ms = [94ms + 32
          mcontinue 
      if not mem[96] % 32:
          require ext_code.size(mstorB9D2m[[94midxm])
          call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
               gas gas_remaining wei
              args mem[mem[64] + 4 len mem[96] + ceil32(m_data.length) + -mem[64] + 320]
      else:
          mem[floor32(mem[96]) + ceil32(m_data.length) + 324] = mem[floor32(mem[96]) + ceil32(m_data.length) + -(mem[96] % 32) + 356 len mem[96] % 32]
          require ext_code.size(mstorB9D2m[[94midxm])
          call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
               gas gas_remaining wei
              args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_data.length) + -mem[64] + 352]
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0] <= 3
      if not ext_call.return_data[0]:
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = 1
          mcontinue 
      require ext_call.return_data[0] <= 3
      if ext_call.return_data[0] != 2:
          require ext_call.return_data[0] <= 3
      mem[0] = 2
      mem[32] = 19
      [94ms = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94mt = mstorB9D2m[[94midxm]
      [94mt = 1
      [94mu = [94mu
      mcontinue 
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(caller, 22), mbalanceOfm[callerm], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  uint8(mstor5m.field_8) = 0
  if [94mt:
      revert with 0, 'Transfer invalid'
  require m_to
  require m_value <= mbalanceOfm[callerm]
  require m_value <= mbalanceOfm[callerm]
  mbalanceOfm[callerm] -= m_value
  require m_value + mbalanceOfm[m_tom] >= mbalanceOfm[m_tom]
  mbalanceOfm[addr(m_to)m] = m_value + mbalanceOfm[m_tom]
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=_to)
  return 1


# hash = 0x3052eed8
# getter = None
# const = None
# payable = False
def unknown3052eed8(uint256 m_param1, uint256 m_param2): # not payable
  if m_param2 > mstor12m.length:
      revert with 0, 'Invalid end'
  require m_param1 <= m_param2
  mem[96] = m_param2 - m_param1
  if m_param2 - m_param1:
      mem[128 len 32 * m_param2 - m_param1] = code.data[22195 len 32 * m_param2 - m_param1]
  [94midx = m_param1
  [94ms = 0
  mwhile [94midx < m_param2m:
      require [94midx < mstor12m.length
      mem[0] = 12
      require [94ms < mem[96]
      mem[(32 * [94ms) + 128] = addr(mstor12m[[94midxm]m.field_0)
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * m_param2 - m_param1) + 128] = 32
  mem[(32 * m_param2 - m_param1) + 160] = mem[96]
  mem[(32 * m_param2 - m_param1) + 192 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  return 32, mem[(32 * m_param2 - m_param1) + 160 len (32 * mem[96]) + 32]


# hash = 0x313ce567
# getter = ['storage', 8, 0, 5]
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
  if not mtransfersFrozen:
      revert with 0, 'Not frozen'
  mtransfersFrozen = 0
  log 0x4f1ca1e6: 0, block.timestamp


# hash = 0x3576857e
# getter = None
# const = None
# payable = False
def unknown3576857e(addr m_param1): # not payable
  require caller == mowner
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0xe486dd3b with:
       gas gas_remaining wei
      args sha3(addr(m_param1), 20), m_param1
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x38777af2
# getter = None
# const = None
# payable = False
def unknown38777af2(addr m_param1, uint256 m_param2, array m_param3, array m_param4): # not payable
  mem[96] = m_param3.length
  mem[128 len m_param3.length] = m_param3[allm]
  mem[64] = ceil32(m_param3.length) + ceil32(m_param4.length) + 160
  mem[ceil32(m_param3.length) + 128] = m_param4.length
  mem[ceil32(m_param3.length) + 160 len m_param4.length] = m_param4[allm]
  if mcontrollerAddress != caller:
      revert with 0, 'Not controller'
  if munknown7a802c71:
      revert with 0, 'Controller disabled'
  if m_param2 > mbalanceOfm[addr(m_param1)m]:
      revert with 0, 'Value too high'
  require not uint8(mstor5m.field_8)
  uint8(mstor5m.field_8) = 1
  mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 160] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
  mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 164] = 11
  mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 196] = m_param1
  mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 228] = 0
  mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 260] = m_param2
  mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 292] = mbalanceOf
  mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 324] = mbalanceOfm[addr(m_param1)m]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
       gas gas_remaining wei
      args 11, addr(m_param1), 0, m_param2, mbalanceOf, mbalanceOfm[addr(m_param1)m]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mgranularity
  if m_param2 % mgranularity:
      revert with 0, 'Invalid granularity'
  if mtransfersFrozen:
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_param1), 22), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      uint8(mstor5m.field_8) = 0
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args 23, mtotalSupply, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require m_param2 <= mbalanceOfm[addr(m_param1)m]
      mbalanceOfm[addr(m_param1)m] -= m_param2
      require m_param2 <= mtotalSupply
      mtotalSupply -= m_param2
      log Burnt(
            address from=_param2,
            uint256 value=_param1)
      log Transfer(
            address from=_param2,
            address to=_param1,
            uint256 value=0)
      mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 160] = m_param2
      mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 288 len ceil32(m_param4.length)] = m_param4[allm], mem[ceil32(m_param3.length) + m_param4.length + 160 len ceil32(m_param4.length) - m_param4.length]
      if not m_param4.length % 32:
          log 0x27e232e0: _param2, 0, 96, _param4.length, Mask(8 * _param4.length, -(8 * _param4.length) + 256, _param4[all], mem[ceil32(_param3.length) + _param4.length + 160 len ceil32(_param4.length) - _param4.length]) << (8 * _param4.length) - 256, caller, _param1
      else:
          mem[floor32(m_param4.length) + ceil32(m_param3.length) + ceil32(m_param4.length) + 288] = mem[floor32(m_param4.length) + ceil32(m_param3.length) + ceil32(m_param4.length) + -(m_param4.length % 32) + 320 len m_param4.length % 32]
          log 0x27e232e0: _param2, 0, 96, _param4.length, Mask(8 * ceil32(_param4.length), -(8 * ceil32(_param4.length)) + 256, _param4[all], mem[ceil32(_param3.length) + _param4.length + 160 len ceil32(_param4.length) - _param4.length]) << (8 * ceil32(_param4.length)) - 256, mem[ceil32(_param3.length) + (2 * ceil32(_param4.length)) + 288 len floor32(_param4.length) + -ceil32(_param4.length) + 32], caller, _param1
  else:
      mem[0] = 2
      mem[32] = 19
      [94ms = 0
      [94midx = 0
      [94mt = 0
      [94mt = 0
      [94mu = 0
      mwhile [94midx < mstorB9D2m.lengthm:
          if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = [94mt
              [94mu = [94mu
              mcontinue 
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 160] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 164] = m_param1
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 196] = 0
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 228] = m_param2
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 292] = 1
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 260] = 160
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 324] = mem[96]
          [94ms = 0
          mwhile [94ms < mem[96]m:
              mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms + 32
              mcontinue 
          if not mem[96] % 32:
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len mem[96] + ceil32(m_param3.length) + ceil32(m_param4.length) + -mem[64] + 352]
          else:
              mem[floor32(mem[96]) + ceil32(m_param3.length) + ceil32(m_param4.length) + 356] = mem[floor32(mem[96]) + ceil32(m_param3.length) + ceil32(m_param4.length) + -(mem[96] % 32) + 388 len mem[96] % 32]
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_param3.length) + ceil32(m_param4.length) + -mem[64] + 384]
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 3
          if not ext_call.return_data[0]:
              mem[0] = 2
              mem[32] = 19
              [94ms = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = 1
              [94mu = 1
              mcontinue 
          require ext_call.return_data[0] <= 3
          if ext_call.return_data[0] != 2:
              require ext_call.return_data[0] <= 3
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = [94mu
          mcontinue 
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_param1), 22), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      uint8(mstor5m.field_8) = 0
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args 23, mtotalSupply, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require m_param2 <= mbalanceOfm[addr(m_param1)m]
      mbalanceOfm[addr(m_param1)m] -= m_param2
      require m_param2 <= mtotalSupply
      mtotalSupply -= m_param2
      log Burnt(
            address from=_param2,
            uint256 value=_param1)
      log Transfer(
            address from=_param2,
            address to=_param1,
            uint256 value=0)
      mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 160] = m_param2
      if not [94mt:
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 192] = 1
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 224] = 96
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 256] = mem[ceil32(m_param3.length) + 128]
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 288 len ceil32(mem[ceil32(m_param3.length) + 128])] = mem[ceil32(m_param3.length) + 160 len ceil32(mem[ceil32(m_param3.length) + 128])]
          log 0x27e232e0: _param2, 1, Array(len=mem[ceil32(_param3.length) + 128], data=mem[ceil32(_param3.length) + ceil32(_param4.length) + 288 len mem[ceil32(_param3.length) + 128]]), caller, _param1
      else:
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 192] = 0
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 224] = 96
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 256] = mem[ceil32(m_param3.length) + 128]
          mem[ceil32(m_param3.length) + ceil32(m_param4.length) + 288 len ceil32(mem[ceil32(m_param3.length) + 128])] = mem[ceil32(m_param3.length) + 160 len ceil32(mem[ceil32(m_param3.length) + 128])]
          if not mem[ceil32(m_param3.length) + 128] % 32:
              log 0x27e232e0: _param2, 0, 96, mem[ceil32(_param3.length) + 128], mem[ceil32(_param3.length) + ceil32(_param4.length) + 288 len mem[ceil32(_param3.length) + 128]], caller, _param1
          else:
              mem[floor32(mem[ceil32(m_param3.length) + 128]) + ceil32(m_param3.length) + ceil32(m_param4.length) + 288] = mem[floor32(mem[ceil32(m_param3.length) + 128]) + ceil32(m_param3.length) + ceil32(m_param4.length) + -(mem[ceil32(m_param3.length) + 128] % 32) + 320 len mem[ceil32(m_param3.length) + 128] % 32]
              log 0x27e232e0: _param2, 0, 96, mem[ceil32(_param3.length) + 128], mem[ceil32(_param3.length) + ceil32(_param4.length) + 288 len floor32(mem[ceil32(_param3.length) + 128]) + 32], caller, _param1


# hash = 0x3c9dcebe
# getter = None
# const = None
# payable = False
def unknown3c9dcebe(uint256 m_param1, array m_param2): # not payable
  mem[64] = ceil32(m_param2.length) + 128
  mem[96] = m_param2.length
  mem[128 len m_param2.length] = m_param2[allm]
  if addr(mstor20m[callerm]m.field_256) != caller:
      revert with 0, 'Wrong address'
  if uint8(mstor20m[callerm]m.field_672):
      revert with 0, 'Module archived'
  require 0 < uint256(mstor20m[callerm]m.field_768)
  require 0 < uint256(mstor20m[callerm]m.field_768)
  [94ms = 0
  mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor20', 20))) + (0.03125 / s))m[uint8([94ms)m] != 5m:
      require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
      mem[32] = 20
      require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
      mem[0] = sha3(caller, 20) + 3
      [94ms = [94ms + 1
      mcontinue 
  if m_param1 > mbalanceOfm[callerm]:
      revert with 0, 'Value too high'
  require not uint8(mstor5m.field_8)
  uint8(mstor5m.field_8) = 1
  mem[ceil32(m_param2.length) + 128] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
  mem[ceil32(m_param2.length) + 132] = 11
  mem[ceil32(m_param2.length) + 164] = caller
  mem[ceil32(m_param2.length) + 196] = 0
  mem[ceil32(m_param2.length) + 228] = m_param1
  mem[ceil32(m_param2.length) + 260] = mbalanceOf
  mem[ceil32(m_param2.length) + 292] = mbalanceOfm[callerm]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
       gas gas_remaining wei
      args 11, caller, 0, m_param1, mbalanceOf, mbalanceOfm[callerm]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mgranularity
  if m_param1 % mgranularity:
      revert with 0, 'Invalid granularity'
  if not mtransfersFrozen:
      mem[0] = 2
      mem[32] = 19
      [94ms = 0
      [94midx = 0
      [94mt = 0
      [94mt = 0
      [94mu = 0
      mwhile [94midx < mstorB9D2m.lengthm:
          if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = [94mt
              [94mu = [94mu
              mcontinue 
          mem[ceil32(m_param2.length) + 128] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
          mem[ceil32(m_param2.length) + 132] = caller
          mem[ceil32(m_param2.length) + 164] = 0
          mem[ceil32(m_param2.length) + 196] = m_param1
          mem[ceil32(m_param2.length) + 260] = 1
          mem[ceil32(m_param2.length) + 228] = 160
          mem[ceil32(m_param2.length) + 292] = mem[96]
          [94ms = 0
          mwhile [94ms < mem[96]m:
              mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms + 32
              mcontinue 
          if not mem[96] % 32:
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len mem[96] + ceil32(m_param2.length) + -mem[64] + 320]
          else:
              mem[floor32(mem[96]) + ceil32(m_param2.length) + 324] = mem[floor32(mem[96]) + ceil32(m_param2.length) + -(mem[96] % 32) + 356 len mem[96] % 32]
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_param2.length) + -mem[64] + 352]
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 3
          if not ext_call.return_data[0]:
              mem[0] = 2
              mem[32] = 19
              [94ms = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = 1
              [94mu = 1
              mcontinue 
          require ext_call.return_data[0] <= 3
          if ext_call.return_data[0] != 2:
              require ext_call.return_data[0] <= 3
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = [94mu
          mcontinue 
      if not [94mt:
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(caller, 22), mbalanceOfm[callerm], mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          uint8(mstor5m.field_8) = 0
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args 23, mtotalSupply, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require m_param1 <= mbalanceOfm[callerm]
          mbalanceOfm[callerm] -= m_param1
          require m_param1 <= mtotalSupply
          mtotalSupply -= m_param1
          log Burnt(
                address from=_param1,
                uint256 value=caller)
          log Transfer(
                address from=_param1,
                address to=caller,
                uint256 value=0)
          stop
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(caller, 22), mbalanceOfm[callerm], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  uint8(mstor5m.field_8) = 0
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args 23, mtotalSupply, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require m_param1 <= mbalanceOfm[callerm]
  mbalanceOfm[callerm] -= m_param1
  require m_param1 <= mtotalSupply
  mtotalSupply -= m_param1
  log Burnt(
        address from=_param1,
        uint256 value=caller)
  log Transfer(
        address from=_param1,
        address to=caller,
        uint256 value=0)
  revert with 0, 'Burn invalid'


# hash = 0x3f553586
# getter = None
# const = None
# payable = False
def unknown3f553586(uint256 m_param1): # not payable
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mstor12m.lengthm:
      require m_param1 <= mcurrentCheckpointId
      mem[0] = addr(mstor12m[[94midxm]m.field_0)
      mem[32] = 0
      mem[100] = sha3(addr(mstor12m[[94midxm]m.field_0), 22)
      mem[132] = m_param1
      mem[164] = mbalanceOfm[addr(mstor12m[[94midxm]m.field_0)m]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0xb58ae1e2 with:
           gas gas_remaining wei
          args sha3(addr(mstor12m[[94midxm]m.field_0), 22), m_param1, mbalanceOfm[addr(mstor12m[[94midxm]m.field_0)m]
      mem[96] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if delegate.return_data[0] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  if [94ms:
      mem[128 len 32 * [94ms] = code.data[22195 len 32 * [94ms]
  [94midx = 0
  [94mt = 0
  mwhile [94midx < mstor12m.lengthm:
      require m_param1 <= mcurrentCheckpointId
      mem[0] = addr(mstor12m[[94midxm]m.field_0)
      mem[32] = 0
      mem[(32 * [94ms) + 132] = sha3(addr(mstor12m[[94midxm]m.field_0), 22)
      mem[(32 * [94ms) + 164] = m_param1
      mem[(32 * [94ms) + 196] = mbalanceOfm[addr(mstor12m[[94midxm]m.field_0)m]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0xb58ae1e2 with:
           gas gas_remaining wei
          args sha3(addr(mstor12m[[94midxm]m.field_0), 22), m_param1, mbalanceOfm[addr(mstor12m[[94midxm]m.field_0)m]
      mem[(32 * [94ms) + 128] = delegate.return_data[0]
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if delegate.return_data[0] <= 0:
          [94midx = [94midx + 1
          [94mt = [94mt
          mcontinue 
      require [94midx < mstor12m.length
      mem[0] = 12
      require [94mt < [94ms
      mem[(32 * [94mt) + 128] = addr(mstor12m[[94midxm]m.field_0)
      [94midx = [94midx + 1
      [94mt = [94mt + 1
      mcontinue 
  mem[(32 * [94ms) + 192 len floor32([94ms)] = mem[128 len floor32([94ms)]
  return Array(len=[94ms, data=mem[128 len floor32([94ms)], mem[(32 * [94ms) + floor32([94ms) + 192 len (32 * [94ms) - floor32([94ms)])


# hash = 0x40c10f19
# getter = None
# const = None
# payable = False
def mint(address m_to, uint256 m_value): # not payable
  mem[64] = 128
  mem[96] = 0
  if caller == mowner:
      if munknowna284de02:
          revert with 0, 'Minting frozen'
      if not m_to:
          revert with 0, 'Investor is 0'
      require not uint8(mstor5m.field_8)
      uint8(mstor5m.field_8) = 1
      mem[128] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
      mem[132] = 11
      mem[164] = 0
      mem[196] = m_to
      mem[228] = m_value
      mem[260] = mbalanceOfm[addr(m_to)m]
      mem[292] = mbalanceOf
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
           gas gas_remaining wei
          args 0, 11, 0, addr(m_to), m_value, mbalanceOfm[addr(m_to)m], mbalanceOf
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mgranularity
      if m_value % mgranularity:
          revert with 0, 'Invalid granularity'
      if mtransfersFrozen:
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          uint8(mstor5m.field_8) = 0
          revert with 0, 'Transfer invalid'
      mem[0] = 2
      mem[32] = 19
      [94ms = 0
      [94midx = 0
      [94mt = 0
      [94mt = 0
      [94mu = 0
      mwhile [94midx < mstorB9D2m.lengthm:
          if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = [94mt
              [94mu = [94mu
              mcontinue 
          mem[128] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
          mem[132] = 0
          mem[164] = m_to
          mem[196] = m_value
          mem[260] = 1
          mem[228] = 160
          mem[292] = mem[96]
          [94ms = 0
          mwhile [94ms < mem[96]m:
              mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms + 32
              mcontinue 
          if not mem[96] % 32:
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len mem[96] + -mem[64] + 320]
          else:
              mem[floor32(mem[96]) + 324] = mem[floor32(mem[96]) + -(mem[96] % 32) + 356 len mem[96] % 32]
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len floor32(mem[96]) + -mem[64] + 352]
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 3
          if not ext_call.return_data[0]:
              mem[0] = 2
              mem[32] = 19
              [94ms = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = 1
              [94mu = 1
              mcontinue 
          require ext_call.return_data[0] <= 3
          if ext_call.return_data[0] != 2:
              require ext_call.return_data[0] <= 3
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = [94mu
          mcontinue 
  else:
      if addr(mstor20m[callerm]m.field_256) != caller:
          revert with 0, 'Wrong address'
      if uint8(mstor20m[callerm]m.field_672):
          revert with 0, 'Module archived'
      require 0 < uint256(mstor20m[callerm]m.field_768)
      require 0 < uint256(mstor20m[callerm]m.field_768)
      [94ms = 0
      mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor20', 20))) + (0.03125 / s))m[uint8([94ms)m] != 3m:
          require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
          mem[32] = 20
          require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
          mem[0] = sha3(caller, 20) + 3
          [94ms = [94ms + 1
          mcontinue 
      if munknowna284de02:
          revert with 0, 'Minting frozen'
      if not m_to:
          revert with 0, 'Investor is 0'
      require not uint8(mstor5m.field_8)
      uint8(mstor5m.field_8) = 1
      mem[128] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
      mem[132] = 11
      mem[164] = 0
      mem[196] = m_to
      mem[228] = m_value
      mem[260] = mbalanceOfm[addr(m_to)m]
      mem[292] = mbalanceOf
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
           gas gas_remaining wei
          args 0, 11, 0, addr(m_to), m_value, mbalanceOfm[addr(m_to)m], mbalanceOf
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mgranularity
      if m_value % mgranularity:
          revert with 0, 'Invalid granularity'
      if mtransfersFrozen:
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          uint8(mstor5m.field_8) = 0
          revert with 0, 'Transfer invalid'
      mem[0] = 2
      mem[32] = 19
      [94ms = 0
      [94midx = 0
      [94mt = 0
      [94mt = 0
      [94mu = 0
      mwhile [94midx < mstorB9D2m.lengthm:
          if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = [94mt
              [94mu = [94mu
              mcontinue 
          mem[128] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
          mem[132] = 0
          mem[164] = m_to
          mem[196] = m_value
          mem[260] = 1
          mem[228] = 160
          mem[292] = mem[96]
          [94ms = 0
          mwhile [94ms < mem[96]m:
              mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms + 32
              mcontinue 
          if not mem[96] % 32:
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len mem[96] + -mem[64] + 320]
          else:
              mem[floor32(mem[96]) + 324] = mem[floor32(mem[96]) + -(mem[96] % 32) + 356 len mem[96] % 32]
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len floor32(mem[96]) + -mem[64] + 352]
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 3
          if not ext_call.return_data[0]:
              mem[0] = 2
              mem[32] = 19
              [94ms = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = 1
              [94mu = 1
              mcontinue 
          require ext_call.return_data[0] <= 3
          if ext_call.return_data[0] != 2:
              require ext_call.return_data[0] <= 3
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = [94mu
          mcontinue 
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  uint8(mstor5m.field_8) = 0
  if [94mt:
      revert with 0, 'Transfer invalid'
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args 23, mtotalSupply, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require m_value + mtotalSupply >= mtotalSupply
  mtotalSupply += m_value
  require m_value + mbalanceOfm[addr(m_to)m] >= mbalanceOfm[addr(m_to)m]
  mbalanceOfm[addr(m_to)m] += m_value
  log Minted(
        address to=_value,
        uint256 amount=_to)
  log Transfer(
        address from=_value,
        address to=0,
        uint256 value=_to)
  return 1


# hash = 0x46e4959d
# getter = None
# const = None
# payable = True
def mintMulti(address[] m_investors, uint256[] m_amounts) payable: 
  mem[64] = 96
  require not call.value
  if m_amounts.length != m_investors.length:
      revert with 0, 'Incorrect inputs'
  [94midx = 0
  mwhile [94midx < m_investors.lengthm:
      require [94midx < m_amounts.length
      [94m_123 = mem[64]
      mem[64] = mem[64] + 32
      mem[[94m_123] = 0
      if caller == mowner:
          if munknowna284de02:
              revert with 0, 'Minting frozen'
          if not addr(cd[((32 * [94midx) + m_investors + 36)]):
              revert with 0, 'Investor is 0'
          require not uint8(mstor5m.field_8)
          uint8(mstor5m.field_8) = 1
          mem[mem[64]] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = 11
          mem[mem[64] + 36] = 0
          mem[mem[64] + 68] = addr(cd[((32 * [94midx) + m_investors + 36)])
          mem[mem[64] + 100] = cd[((32 * [94midx) + m_amounts + 36)]
          mem[mem[64] + 132] = mbalanceOfm[addr(cd[((32 * [94midx) + m_investors + 36)])m]
          mem[mem[64] + 164] = mbalanceOf
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
               gas gas_remaining wei
              args 11, 0, addr(cd[((32 * [94midx) + m_investors + 36)]), cd[((32 * [94midx) + m_amounts + 36)], mbalanceOfm[addr(cd[((32 * [94midx) + m_investors + 36)])m], mbalanceOf
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require mgranularity
          if cd[((32 * [94midx) + m_amounts + 36)] % mgranularity:
              revert with 0, 'Invalid granularity'
          if mtransfersFrozen:
              require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
              [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
                   gas gas_remaining wei
                  args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
              if not delegate.return_code:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
              [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
                   gas gas_remaining wei
                  args sha3(addr(cd[((32 * [94midx) + m_investors + 36)]), 22), mbalanceOfm[addr(cd[((32 * [94midx) + m_investors + 36)])m], mcurrentCheckpointId
              if not delegate.return_code:
                  revert with ext_call.return_data[0 len return_data.size]
              uint8(mstor5m.field_8) = 0
              revert with 0, 'Transfer invalid'
          mem[0] = 2
          mem[32] = 19
          [94mt = 0
          [94ms = 0
          [94mu = 0
          [94mu = 0
          [94mv = 0
          mwhile [94ms < mstorB9D2m.lengthm:
              mem[0] = mstorB9D2m[[94msm]
              mem[32] = 20
              if uint8(mstor20m[mstorB9D2m[[94msm]m]m.field_672):
                  mem[0] = 2
                  mem[32] = 19
                  [94mt = [94mt
                  [94ms = [94ms + 1
                  [94mu = mstorB9D2m[[94msm]
                  [94mu = [94mu
                  [94mv = [94mv
                  mcontinue 
              mem[mem[64]] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 0
              mem[mem[64] + 36] = addr(cd[((32 * [94midx) + m_investors + 36)])
              mem[mem[64] + 68] = cd[((32 * [94midx) + m_amounts + 36)]
              mem[mem[64] + 132] = 1
              mem[mem[64] + 100] = 160
              mem[mem[64] + 164] = mem[[94m_123]
              [94m_246 = mem[[94m_123]
              [94mt = 0
              mwhile [94mt < [94m_246m:
                  mem[[94mt + mem[64] + 196] = mem[[94mt + [94m_123 + 32]
                  mem[0] = 2
                  mem[32] = 19
                  [94mt = [94mt + 32
                  mcontinue 
              if not [94m_246 % 32:
                  require ext_code.size(mstorB9D2m[[94msm])
                  call mstorB9D2m[[94msm].verifyTransfer(address from, address to, uint256 param3, bytes param4, bool param5) with:
                       gas gas_remaining wei
                      args 0, addr(cd[((32 * [94midx) + m_investors + 36)]), cd[((32 * [94midx) + m_amounts + 36)], 160, 1, mem[mem[64] + 164 len [94m_246 + 32]
              else:
                  mem[floor32([94m_246) + mem[64] + 196] = mem[floor32([94m_246) + mem[64] + -([94m_246 % 32) + 228 len [94m_246 % 32]
                  require ext_code.size(mstorB9D2m[[94msm])
                  call mstorB9D2m[[94msm].verifyTransfer(address from, address to, uint256 param3, bytes param4, bool param5) with:
                       gas gas_remaining wei
                      args 0, addr(cd[((32 * [94midx) + m_investors + 36)]), cd[((32 * [94midx) + m_amounts + 36)], 160, 1, mem[mem[64] + 164 len floor32([94m_246) + 64]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  mem[0] = 2
                  mem[32] = 19
                  [94mt = ext_call.return_data[0]
                  [94ms = [94ms + 1
                  [94mu = mstorB9D2m[[94msm]
                  [94mu = 1
                  [94mv = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
              mem[0] = 2
              mem[32] = 19
              [94mt = ext_call.return_data[0]
              [94ms = [94ms + 1
              [94mu = mstorB9D2m[[94msm]
              [94mu = 1
              [94mv = [94mv
              mcontinue 
      else:
          if addr(mstor20m[callerm]m.field_256) != caller:
              revert with 0, 'Wrong address'
          if uint8(mstor20m[callerm]m.field_672):
              revert with 0, 'Module archived'
          require 0 < uint256(mstor20m[callerm]m.field_768)
          require 0 < uint256(mstor20m[callerm]m.field_768)
          [94ms = 0
          mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor20', 20))) + (0.03125 / s))m[uint8([94ms)m] != 3m:
              require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
              mem[32] = 20
              require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
              mem[0] = sha3(caller, 20) + 3
              [94ms = [94ms + 1
              mcontinue 
          if munknowna284de02:
              revert with 0, 'Minting frozen'
          if not addr(cd[((32 * [94midx) + m_investors + 36)]):
              revert with 0, 'Investor is 0'
          require not uint8(mstor5m.field_8)
          uint8(mstor5m.field_8) = 1
          mem[mem[64]] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = 11
          mem[mem[64] + 36] = 0
          mem[mem[64] + 68] = addr(cd[((32 * [94midx) + m_investors + 36)])
          mem[mem[64] + 100] = cd[((32 * [94midx) + m_amounts + 36)]
          mem[mem[64] + 132] = mbalanceOfm[addr(cd[((32 * [94midx) + m_investors + 36)])m]
          mem[mem[64] + 164] = mbalanceOf
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
               gas gas_remaining wei
              args 11, 0, addr(cd[((32 * [94midx) + m_investors + 36)]), cd[((32 * [94midx) + m_amounts + 36)], mbalanceOfm[addr(cd[((32 * [94midx) + m_investors + 36)])m], mbalanceOf
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require mgranularity
          if cd[((32 * [94midx) + m_amounts + 36)] % mgranularity:
              revert with 0, 'Invalid granularity'
          if mtransfersFrozen:
              require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
              [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
                   gas gas_remaining wei
                  args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
              if not delegate.return_code:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
              [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
                   gas gas_remaining wei
                  args sha3(addr(cd[((32 * [94midx) + m_investors + 36)]), 22), mbalanceOfm[addr(cd[((32 * [94midx) + m_investors + 36)])m], mcurrentCheckpointId
              if not delegate.return_code:
                  revert with ext_call.return_data[0 len return_data.size]
              uint8(mstor5m.field_8) = 0
              revert with 0, 'Transfer invalid'
          mem[0] = 2
          mem[32] = 19
          [94mt = 0
          [94ms = 0
          [94mu = 0
          [94mu = 0
          [94mv = 0
          mwhile [94ms < mstorB9D2m.lengthm:
              mem[0] = mstorB9D2m[[94msm]
              mem[32] = 20
              if uint8(mstor20m[mstorB9D2m[[94msm]m]m.field_672):
                  mem[0] = 2
                  mem[32] = 19
                  [94mt = [94mt
                  [94ms = [94ms + 1
                  [94mu = mstorB9D2m[[94msm]
                  [94mu = [94mu
                  [94mv = [94mv
                  mcontinue 
              mem[mem[64]] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = 0
              mem[mem[64] + 36] = addr(cd[((32 * [94midx) + m_investors + 36)])
              mem[mem[64] + 68] = cd[((32 * [94midx) + m_amounts + 36)]
              mem[mem[64] + 132] = 1
              mem[mem[64] + 100] = 160
              mem[mem[64] + 164] = mem[[94m_123]
              [94m_357 = mem[[94m_123]
              [94mt = 0
              mwhile [94mt < [94m_357m:
                  mem[[94mt + mem[64] + 196] = mem[[94mt + [94m_123 + 32]
                  mem[0] = 2
                  mem[32] = 19
                  [94mt = [94mt + 32
                  mcontinue 
              if not [94m_357 % 32:
                  require ext_code.size(mstorB9D2m[[94msm])
                  call mstorB9D2m[[94msm].verifyTransfer(address from, address to, uint256 param3, bytes param4, bool param5) with:
                       gas gas_remaining wei
                      args 0, addr(cd[((32 * [94midx) + m_investors + 36)]), cd[((32 * [94midx) + m_amounts + 36)], 160, 1, mem[mem[64] + 164 len [94m_357 + 32]
              else:
                  mem[floor32([94m_357) + mem[64] + 196] = mem[floor32([94m_357) + mem[64] + -([94m_357 % 32) + 228 len [94m_357 % 32]
                  require ext_code.size(mstorB9D2m[[94msm])
                  call mstorB9D2m[[94msm].verifyTransfer(address from, address to, uint256 param3, bytes param4, bool param5) with:
                       gas gas_remaining wei
                      args 0, addr(cd[((32 * [94midx) + m_investors + 36)]), cd[((32 * [94midx) + m_amounts + 36)], 160, 1, mem[mem[64] + 164 len floor32([94m_357) + 64]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] <= 3
              if not ext_call.return_data[0]:
                  mem[0] = 2
                  mem[32] = 19
                  [94mt = ext_call.return_data[0]
                  [94ms = [94ms + 1
                  [94mu = mstorB9D2m[[94msm]
                  [94mu = 1
                  [94mv = 1
                  mcontinue 
              require ext_call.return_data[0] <= 3
              if ext_call.return_data[0] != 2:
                  require ext_call.return_data[0] <= 3
              mem[0] = 2
              mem[32] = 19
              [94mt = ext_call.return_data[0]
              [94ms = [94ms + 1
              [94mu = mstorB9D2m[[94msm]
              [94mu = 1
              [94mv = [94mv
              mcontinue 
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(cd[((32 * [94midx) + m_investors + 36)]), 22), mbalanceOfm[addr(cd[((32 * [94midx) + m_investors + 36)])m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      uint8(mstor5m.field_8) = 0
      if [94mu:
          revert with 0, 'Transfer invalid'
      mem[mem[64] + 4] = 23
      mem[mem[64] + 36] = mtotalSupply
      mem[mem[64] + 68] = mcurrentCheckpointId
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args 23, mtotalSupply, mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require cd[((32 * [94midx) + m_amounts + 36)] + mtotalSupply >= mtotalSupply
      mtotalSupply += cd[((32 * [94midx) + m_amounts + 36)]
      require cd[((32 * [94midx) + m_amounts + 36)] + mbalanceOfm[addr(cd[((32 * [94midx) + m_investors + 36)])m] >= mbalanceOfm[addr(cd[((32 * [94midx) + m_investors + 36)])m]
      mem[32] = 0
      mbalanceOfm[addr(cd[((32 * [94midx) + m_investors + 36)])m] += cd[((32 * [94midx) + m_amounts + 36)]
      log Minted(
            address to=cd[((32 * idx) + _amounts + 36)],
            uint256 amount=addr(cd[((32 * idx) + _investors + 36)]))
      mem[mem[64]] = cd[((32 * [94midx) + m_amounts + 36)]
      mem[0] = addr(cd[((32 * [94midx) + m_investors + 36)])
      log Transfer(
            address from=cd[((32 * idx) + _amounts + 36)],
            address to=0,
            uint256 value=addr(cd[((32 * idx) + _investors + 36)]))
      [94midx = [94midx + 1
      mcontinue 
  return 1


# hash = 0x4c6041d3
# getter = None
# const = None
# payable = False
def unknown4c6041d3(): # not payable
  if not mstor24m.length:
      mem[(32 * mstor24m.length) + 128] = 32
      mem[(32 * mstor24m.length) + 160] = mstor24m.length
      mem[(32 * mstor24m.length) + 192 len floor32(mstor24m.length)] = mem[128 len floor32(mstor24m.length)]
      return memory
        from (32 * mstor24m.length) + 128
         [93mlen (96 * mstor24m.length) + 64
  mem[128] = uint256(mstor24m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * mstor24m.length) + 96 > [94midxm:
      mem[[94midx + 32] = uint256(mstor24m[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mstor24m.length) + 192 len floor32(mstor24m.length)] = mem[128 len floor32(mstor24m.length)]
  return Array(len=mstor24m.length, data=mem[128 len floor32(mstor24m.length)], mem[(32 * mstor24m.length) + floor32(mstor24m.length) + 192 len (32 * mstor24m.length) - floor32(mstor24m.length)]), 


# hash = 0x4ee2cd7e
# getter = None
# const = None
# payable = False
def balanceOfAt(address m_owner, uint256 m_blockNumber): # not payable
  require m_blockNumber <= mcurrentCheckpointId
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0xb58ae1e2 with:
       gas gas_remaining wei
      args sha3(addr(m_owner), 22), m_blockNumber, mbalanceOfm[addr(m_owner)m]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return delegate.return_data[0]


# hash = 0x5488cc80
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def currentCheckpointId(): # not payable
  return mcurrentCheckpointId


# hash = 0x556f0dc7
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def granularity(): # not payable
  return mgranularity


# hash = 0x5aa14a70
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def unknown5aa14a70(): # not payable
  return munknown5aa14a70Address


# hash = 0x5c49de5e
# getter = None
# const = None
# payable = False
def unknown5c49de5e(addr m_param1, addr m_param2, uint256 m_param3, array m_param4, array m_param5): # not payable
  mem[96] = m_param4.length
  mem[128 len m_param4.length] = m_param4[allm]
  mem[64] = ceil32(m_param4.length) + ceil32(m_param5.length) + 160
  mem[ceil32(m_param4.length) + 128] = m_param5.length
  mem[ceil32(m_param4.length) + 160 len m_param5.length] = m_param5[allm]
  if mcontrollerAddress != caller:
      revert with 0, 'Not controller'
  if munknown7a802c71:
      revert with 0, 'Controller disabled'
  require m_param2
  require m_param3 <= mbalanceOfm[addr(m_param1)m]
  require not uint8(mstor5m.field_8)
  uint8(mstor5m.field_8) = 1
  mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 160] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
  mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 164] = 11
  mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 196] = m_param1
  mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 228] = m_param2
  mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 260] = m_param3
  mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 292] = mbalanceOfm[addr(m_param2)m]
  mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 324] = mbalanceOfm[addr(m_param1)m]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
       gas gas_remaining wei
      args 11, addr(m_param1), addr(m_param2), m_param3, mbalanceOfm[addr(m_param2)m], mbalanceOfm[addr(m_param1)m]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mgranularity
  if m_param3 % mgranularity:
      revert with 0, 'Invalid granularity'
  if mtransfersFrozen:
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_param1), 22), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_param2), 22), mbalanceOfm[addr(m_param2)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      uint8(mstor5m.field_8) = 0
      require m_param3 <= mbalanceOfm[addr(m_param1)m]
      mbalanceOfm[addr(m_param1)m] -= m_param3
      require m_param3 + mbalanceOfm[m_param2m] >= mbalanceOfm[m_param2m]
      mbalanceOfm[addr(m_param2)m] = m_param3 + mbalanceOfm[m_param2m]
      mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 160] = m_param3
      mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 288 len ceil32(m_param5.length)] = m_param5[allm], mem[ceil32(m_param4.length) + m_param5.length + 160 len ceil32(m_param5.length) - m_param5.length]
      if not m_param5.length % 32:
          log 0xf38eab8c: _param3, 0, 96, _param5.length, Mask(8 * _param5.length, -(8 * _param5.length) + 256, _param5[all], mem[ceil32(_param4.length) + _param5.length + 160 len ceil32(_param5.length) - _param5.length]) << (8 * _param5.length) - 256, caller, _param1, _param2
      else:
          mem[floor32(m_param5.length) + ceil32(m_param4.length) + ceil32(m_param5.length) + 288] = mem[floor32(m_param5.length) + ceil32(m_param4.length) + ceil32(m_param5.length) + -(m_param5.length % 32) + 320 len m_param5.length % 32]
          log 0xf38eab8c: _param3, 0, 96, _param5.length, Mask(8 * ceil32(_param5.length), -(8 * ceil32(_param5.length)) + 256, _param5[all], mem[ceil32(_param4.length) + _param5.length + 160 len ceil32(_param5.length) - _param5.length]) << (8 * ceil32(_param5.length)) - 256, mem[ceil32(_param4.length) + (2 * ceil32(_param5.length)) + 288 len floor32(_param5.length) + -ceil32(_param5.length) + 32], caller, _param1, _param2
  else:
      mem[0] = 2
      mem[32] = 19
      [94ms = 0
      [94midx = 0
      [94mt = 0
      [94mt = 0
      [94mu = 0
      mwhile [94midx < mstorB9D2m.lengthm:
          if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = [94mt
              [94mu = [94mu
              mcontinue 
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 160] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 164] = m_param1
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 196] = m_param2
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 228] = m_param3
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 292] = 1
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 260] = 160
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 324] = mem[96]
          [94ms = 0
          mwhile [94ms < mem[96]m:
              mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms + 32
              mcontinue 
          if not mem[96] % 32:
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len mem[96] + ceil32(m_param4.length) + ceil32(m_param5.length) + -mem[64] + 352]
          else:
              mem[floor32(mem[96]) + ceil32(m_param4.length) + ceil32(m_param5.length) + 356] = mem[floor32(mem[96]) + ceil32(m_param4.length) + ceil32(m_param5.length) + -(mem[96] % 32) + 388 len mem[96] % 32]
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_param4.length) + ceil32(m_param5.length) + -mem[64] + 384]
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 3
          if not ext_call.return_data[0]:
              mem[0] = 2
              mem[32] = 19
              [94ms = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = 1
              [94mu = 1
              mcontinue 
          require ext_call.return_data[0] <= 3
          if ext_call.return_data[0] != 2:
              require ext_call.return_data[0] <= 3
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = [94mu
          mcontinue 
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_param1), 22), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_param2), 22), mbalanceOfm[addr(m_param2)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      uint8(mstor5m.field_8) = 0
      require m_param3 <= mbalanceOfm[addr(m_param1)m]
      mbalanceOfm[addr(m_param1)m] -= m_param3
      require m_param3 + mbalanceOfm[m_param2m] >= mbalanceOfm[m_param2m]
      mbalanceOfm[addr(m_param2)m] = m_param3 + mbalanceOfm[m_param2m]
      mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 160] = m_param3
      if not [94mt:
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 192] = 1
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 224] = 96
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 256] = mem[ceil32(m_param4.length) + 128]
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 288 len ceil32(mem[ceil32(m_param4.length) + 128])] = mem[ceil32(m_param4.length) + 160 len ceil32(mem[ceil32(m_param4.length) + 128])]
          log 0xf38eab8c: _param3, 1, Array(len=mem[ceil32(_param4.length) + 128], data=mem[ceil32(_param4.length) + ceil32(_param5.length) + 288 len mem[ceil32(_param4.length) + 128]]), caller, _param1, _param2
      else:
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 192] = 0
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 224] = 96
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 256] = mem[ceil32(m_param4.length) + 128]
          mem[ceil32(m_param4.length) + ceil32(m_param5.length) + 288 len ceil32(mem[ceil32(m_param4.length) + 128])] = mem[ceil32(m_param4.length) + 160 len ceil32(mem[ceil32(m_param4.length) + 128])]
          if not mem[ceil32(m_param4.length) + 128] % 32:
              log 0xf38eab8c: _param3, 0, 96, mem[ceil32(_param4.length) + 128], mem[ceil32(_param4.length) + ceil32(_param5.length) + 288 len mem[ceil32(_param4.length) + 128]], caller, _param1, _param2
          else:
              mem[floor32(mem[ceil32(m_param4.length) + 128]) + ceil32(m_param4.length) + ceil32(m_param5.length) + 288] = mem[floor32(mem[ceil32(m_param4.length) + 128]) + ceil32(m_param4.length) + ceil32(m_param5.length) + -(mem[ceil32(m_param4.length) + 128] % 32) + 320 len mem[ceil32(m_param4.length) + 128] % 32]
              log 0xf38eab8c: _param3, 0, 96, mem[ceil32(_param4.length) + 128], mem[ceil32(_param4.length) + ceil32(_param5.length) + 288 len floor32(mem[ceil32(_param4.length) + 128]) + 32], caller, _param1, _param2
  log Transfer(
        address from=_param3,
        address to=_param1,
        uint256 value=_param2)


# hash = 0x62b348c3
# getter = None
# const = None
# payable = False
def unknown62b348c3(addr m_param1, uint256 m_param2, bool m_param3): # not payable
  require caller == mowner
  if not addr(mstor20m[addr(m_param1)m]m.field_256):
      revert with 0, 'Module missing'
  require ext_code.size(addr(mproofTokenAddress))
  call addr(mproofTokenAddress).allowance(address owner, address spender) with:
       gas gas_remaining wei
      args this.address, m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(mproofTokenAddress))
  if not m_param3:
      call addr(mproofTokenAddress).decreaseApproval(address spender, uint256 subtractedValue) with:
           gas gas_remaining wei
          args addr(m_param1), m_param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          revert with 0, 'Insufficient allowance'
      require m_param2 <= ext_call.return_data[0]
      if not uint256(mstor20m[addr(m_param1)m]m.field_768):
          log 0xa00a1c33: ext_call.return_data[0], addr(_param1), ext_call.return_data[0], ext_call.return_data[0] - _param2, uint256(stor20[addr(_param1)].field_768)
      else:
          mem[256] = uint8(mstor20m[addr(m_param1)m]m[3m]m.field_0)
          [94midx = 256
          [94ms = 0
          mwhile (32 * uint256(mstor20m[addr(m_param1)m]m.field_768)) + 256 > [94midx + 32m:
              mem[[94midx + 32] = mstor('array', 3, ('map', ('mask_shl', 160, 0, 96, ('param', '_param1')), ('name', 'stor20', 20)))m[-(0.03125 / [94ms + 1) + [94ms + (-1 * 0.03125 / [94ms + 1 * [94ms) + 1m]
              [94midx = [94midx + 32
              [94ms = -([94ms + 1 / 32) + [94ms + (-1 * [94ms + 1 / 32 * [94ms) + 1
              mcontinue 
          log 0xa00a1c33: ext_call.return_data[0], addr(_param1), ext_call.return_data[0], ext_call.return_data[0] - _param2, uint256(stor20[addr(_param1)].field_768), mem[256 len 32 * uint256(stor20[addr(_param1)].field_768)]
  else:
      call addr(mproofTokenAddress).increaseApproval(address spender, uint256 addedValue) with:
           gas gas_remaining wei
          args addr(m_param1), m_param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          revert with 0, 'IncreaseApproval fail'
      require m_param2 + ext_call.return_data[0] >= ext_call.return_data[0]
      if not uint256(mstor20m[addr(m_param1)m]m.field_768):
          log 0xa00a1c33: ext_call.return_data[0], addr(_param1), ext_call.return_data[0], _param2 + ext_call.return_data[0], uint256(stor20[addr(_param1)].field_768)
      else:
          mem[256] = uint8(mstor20m[addr(m_param1)m]m[3m]m.field_0)
          [94midx = 256
          [94ms = 0
          mwhile (32 * uint256(mstor20m[addr(m_param1)m]m.field_768)) + 256 > [94midx + 32m:
              mem[[94midx + 32] = mstor('array', 3, ('map', ('mask_shl', 160, 0, 96, ('param', '_param1')), ('name', 'stor20', 20)))m[-(0.03125 / [94ms + 1) + [94ms + (-1 * 0.03125 / [94ms + 1 * [94ms) + 1m]
              [94midx = [94midx + 32
              [94ms = -([94ms + 1 / 32) + [94ms + (-1 * [94ms + 1 / 32 * [94ms) + 1
              mcontinue 
          log 0xa00a1c33: ext_call.return_data[0], addr(_param1), ext_call.return_data[0], _param2 + ext_call.return_data[0], uint256(stor20[addr(_param1)].field_768), mem[256 len 32 * uint256(stor20[addr(_param1)].field_768)]


# hash = 0x66188463
# getter = None
# const = None
# payable = False
def decreaseApproval(address m_spender, uint256 m_subtractedValue): # not payable
  if m_subtractedValue <= mallowancem[callerm]m[addr(m_spender)m]:
      mallowancem[callerm]m[addr(m_spender)m] -= m_subtractedValue
  else:
      mallowancem[callerm]m[addr(m_spender)m] = 0
  log Approval(
        address owner=allowance[caller][addr(_spender)],
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 0]]]
# const = None
# payable = False
def balanceOf(address m_owner): # not payable
  return mbalanceOfm[addr(m_owner)m]


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x73826a93
# getter = None
# const = None
# payable = False
def updateTokenDetails(string m_newTokenDetails): # not payable
  require caller == mowner
  mem[192] = uint256(mtokenDetailsm.field_0)
  [94midx = 192
  [94ms = 0
  mwhile mtokenDetailsm.length + 192 > [94midx + 32m:
      mem[[94midx + 32] = uint256(mtokenDetailsm[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[mtokenDetailsm.length + (floor32(mtokenDetailsm.length - 1) + -mtokenDetailsm.length + 32 % 32) + 192] = m_newTokenDetails.length
  log 0x4f5dc3fe: Array(len=tokenDetails.length, data=mem[192 len tokenDetails.length + (floor32(tokenDetails.length - 1) + -tokenDetails.length + 32 % 32) + 32], _newTokenDetails[all]), tokenDetails.length + (floor32(tokenDetails.length - 1) + -tokenDetails.length + 32 % 32) + 96
  mtokenDetailsm.length = (2 * m_newTokenDetails.length) + 1
  [94ms = 0
  [94midx = m_newTokenDetails + 36
  mwhile m_newTokenDetails + m_newTokenDetails.length + 36 > [94midxm:
      uint256(mtokenDetailsm[[94msm]m.field_0) = cd[[94midx]
      [94ms = [94ms + 1
      [94midx = [94midx + 32
      mcontinue 
  [94midx = Mask(251, 0, m_newTokenDetails.length + 31) >> 5
  mwhile mtokenDetailsm.length + 31 / 32 > [94midxm:
      uint256(mtokenDetailsm[[94midxm]m.field_0) = 0
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x764387bd
# getter = None
# const = None
# payable = False
def unknown764387bd(uint256 m_param1): # not payable
  if not uint256(mstor21m[m_param1m]m.field_0):
      mem[(32 * uint256(mstor21m[m_param1m]m.field_0)) + 128] = 32
      mem[(32 * uint256(mstor21m[m_param1m]m.field_0)) + 160] = uint256(mstor21m[m_param1m]m.field_0)
      mem[(32 * uint256(mstor21m[m_param1m]m.field_0)) + 192 len floor32(uint256(mstor21m[m_param1m]m.field_0))] = mem[128 len floor32(uint256(mstor21m[m_param1m]m.field_0))]
      return memory
        from (32 * uint256(mstor21m[m_param1m]m.field_0)) + 128
         [93mlen (96 * uint256(mstor21m[m_param1m]m.field_0)) + 64
  mem[128] = addr(mstor21m[m_param1m]m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * uint256(mstor21m[m_param1m]m.field_0)) + 96 > [94midxm:
      mem[[94midx + 32] = addr(mstor21m[m_param1m]m[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * uint256(mstor21m[m_param1m]m.field_0)) + 192 len floor32(uint256(mstor21m[m_param1m]m.field_0))] = mem[128 len floor32(uint256(mstor21m[m_param1m]m.field_0))]
  return Array(len=uint256(mstor21m[m_param1m]m.field_0), data=mem[128 len floor32(uint256(mstor21m[m_param1m]m.field_0))], mem[(32 * uint256(mstor21m[m_param1m]m.field_0)) + floor32(uint256(mstor21m[m_param1m]m.field_0)) + 192 len (32 * uint256(mstor21m[m_param1m]m.field_0)) - floor32(uint256(mstor21m[m_param1m]m.field_0))]), 


# hash = 0x7a802c71
# getter = ['bool', ['storage', 8, 16, 18]]
# const = None
# payable = False
def unknown7a802c71(): # not payable
  return bool(munknown7a802c71)


# hash = 0x7d6ae27b
# getter = None
# const = None
# payable = False
def unknown7d6ae27b(addr m_param1, uint256 m_param2, array m_param3): # not payable
  mem[64] = ceil32(m_param3.length) + 128
  mem[96] = m_param3.length
  mem[128 len m_param3.length] = m_param3[allm]
  if addr(mstor20m[callerm]m.field_256) != caller:
      revert with 0, 'Wrong address'
  if uint8(mstor20m[callerm]m.field_672):
      revert with 0, 'Module archived'
  require 0 < uint256(mstor20m[callerm]m.field_768)
  require 0 < uint256(mstor20m[callerm]m.field_768)
  [94ms = 0
  mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor20', 20))) + (0.03125 / s))m[uint8([94ms)m] != 5m:
      require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
      mem[32] = 20
      require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
      mem[0] = sha3(caller, 20) + 3
      [94ms = [94ms + 1
      mcontinue 
  if m_param2 > mallowancem[addr(m_param1)m]m[callerm]:
      revert with 0, 'Value too high'
  require m_param2 <= mallowancem[addr(m_param1)m]m[callerm]
  mallowancem[addr(m_param1)m]m[callerm] -= m_param2
  if m_param2 > mbalanceOfm[addr(m_param1)m]:
      revert with 0, 'Value too high'
  require not uint8(mstor5m.field_8)
  uint8(mstor5m.field_8) = 1
  mem[ceil32(m_param3.length) + 128] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
  mem[ceil32(m_param3.length) + 132] = 11
  mem[ceil32(m_param3.length) + 164] = m_param1
  mem[ceil32(m_param3.length) + 196] = 0
  mem[ceil32(m_param3.length) + 228] = m_param2
  mem[ceil32(m_param3.length) + 260] = mbalanceOf
  mem[ceil32(m_param3.length) + 292] = mbalanceOfm[addr(m_param1)m]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
       gas gas_remaining wei
      args 11, addr(m_param1), 0, m_param2, mbalanceOf, mbalanceOfm[addr(m_param1)m]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mgranularity
  if m_param2 % mgranularity:
      revert with 0, 'Invalid granularity'
  if not mtransfersFrozen:
      mem[0] = 2
      mem[32] = 19
      [94ms = 0
      [94midx = 0
      [94mt = 0
      [94mt = 0
      [94mu = 0
      mwhile [94midx < mstorB9D2m.lengthm:
          if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = [94mt
              [94mu = [94mu
              mcontinue 
          mem[ceil32(m_param3.length) + 128] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
          mem[ceil32(m_param3.length) + 132] = m_param1
          mem[ceil32(m_param3.length) + 164] = 0
          mem[ceil32(m_param3.length) + 196] = m_param2
          mem[ceil32(m_param3.length) + 260] = 1
          mem[ceil32(m_param3.length) + 228] = 160
          mem[ceil32(m_param3.length) + 292] = mem[96]
          [94ms = 0
          mwhile [94ms < mem[96]m:
              mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms + 32
              mcontinue 
          if not mem[96] % 32:
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len mem[96] + ceil32(m_param3.length) + -mem[64] + 320]
          else:
              mem[floor32(mem[96]) + ceil32(m_param3.length) + 324] = mem[floor32(mem[96]) + ceil32(m_param3.length) + -(mem[96] % 32) + 356 len mem[96] % 32]
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_param3.length) + -mem[64] + 352]
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 3
          if not ext_call.return_data[0]:
              mem[0] = 2
              mem[32] = 19
              [94ms = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = 1
              [94mu = 1
              mcontinue 
          require ext_call.return_data[0] <= 3
          if ext_call.return_data[0] != 2:
              require ext_call.return_data[0] <= 3
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = [94mu
          mcontinue 
      if not [94mt:
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(addr(m_param1), 22), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          uint8(mstor5m.field_8) = 0
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args 23, mtotalSupply, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require m_param2 <= mbalanceOfm[addr(m_param1)m]
          mbalanceOfm[addr(m_param1)m] -= m_param2
          require m_param2 <= mtotalSupply
          mtotalSupply -= m_param2
          log Burnt(
                address from=_param2,
                uint256 value=_param1)
          log Transfer(
                address from=_param2,
                address to=_param1,
                uint256 value=0)
          stop
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(addr(m_param1), 22), mbalanceOfm[addr(m_param1)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  uint8(mstor5m.field_8) = 0
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args 23, mtotalSupply, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require m_param2 <= mbalanceOfm[addr(m_param1)m]
  mbalanceOfm[addr(m_param1)m] -= m_param2
  require m_param2 <= mtotalSupply
  mtotalSupply -= m_param2
  log Burnt(
        address from=_param2,
        uint256 value=_param1)
  log Transfer(
        address from=_param2,
        address to=_param1,
        uint256 value=0)
  revert with 0, 'Burn invalid'


# hash = 0x8658b8b9
# getter = None
# const = None
# payable = False
def checkPermission(address m_delegate, address m_module, bytes32 m_perm): # not payable
  [94midx = 0
  mwhile [94midx < uint256(mstor19m[1m]m.field_0)m:
      if uint8(mstor20m[addr(mstor19m[1m]m[[94midxm]m.field_0)m]m.field_672):
          mem[0] = 1
          mem[32] = 19
          [94midx = [94midx + 1
          mcontinue 
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x84c0b0ef with:
           gas gas_remaining wei
          args 0, 3523081037, addr(m_delegate), addr(m_module), m_perm
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return bool(delegate.return_data[0])
  return 0


# hash = 0x869e50c7
# getter = None
# const = None
# payable = False
def unknown869e50c7(): # not payable
  require ext_code.size(addr(munknowncaf90dabAddress))
  call addr(munknowncaf90dabAddress).0x2f0019f2 with:
       gas gas_remaining wei
      args 'disableControllerAllowed'
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require caller == mowner
  require not munknown7a802c71
  munknown7a802c71 = 1
  mcontrollerAddress = 0
  Mask(72, 0, mstor18m.field_184) = 0
  mstor18m.field_256 % 1 = 0
  log 0x6d4b279f: block.timestamp


# hash = 0x8da5cb5b
# getter = ['storage', 160, 16, 5]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x92eefe9b
# getter = None
# const = None
# payable = False
def setController(address m_controller): # not payable
  require caller == mowner
  require not munknown7a802c71
  log 0x9fdb0721: controllerAddress, _controller
  mcontrollerAddress = m_controller


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = False
def symbol(): # not payable
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0x960524e3
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def getInvestorCount(): # not payable
  return minvestorCount


# hash = 0x96adfe42
# getter = None
# const = None
# payable = False
def mintWithData(address m_to, uint256 m_amount, bytes m_data): # not payable
  mem[64] = ceil32(m_data.length) + 128
  mem[96] = m_data.length
  mem[128 len m_data.length] = m_data[allm]
  if caller == mowner:
      if munknowna284de02:
          revert with 0, 'Minting frozen'
      if not m_to:
          revert with 0, 'Investor is 0'
      require not uint8(mstor5m.field_8)
      uint8(mstor5m.field_8) = 1
      mem[ceil32(m_data.length) + 128] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
      mem[ceil32(m_data.length) + 132] = 11
      mem[ceil32(m_data.length) + 164] = 0
      mem[ceil32(m_data.length) + 196] = m_to
      mem[ceil32(m_data.length) + 228] = m_amount
      mem[ceil32(m_data.length) + 260] = mbalanceOfm[addr(m_to)m]
      mem[ceil32(m_data.length) + 292] = mbalanceOf
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
           gas gas_remaining wei
          args 11, 0, addr(m_to), m_amount, mbalanceOfm[addr(m_to)m], mbalanceOf
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mgranularity
      if m_amount % mgranularity:
          revert with 0, 'Invalid granularity'
      if mtransfersFrozen:
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          uint8(mstor5m.field_8) = 0
          revert with 0, 'Transfer invalid'
      mem[0] = 2
      mem[32] = 19
      [94ms = 0
      [94midx = 0
      [94mt = 0
      [94mt = 0
      [94mu = 0
      mwhile [94midx < mstorB9D2m.lengthm:
          if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = [94mt
              [94mu = [94mu
              mcontinue 
          [94m_126 = mem[64]
          mem[mem[64]] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
          mem[mem[64] + 4] = 0
          mem[mem[64] + 36] = m_to
          mem[mem[64] + 68] = m_amount
          mem[mem[64] + 132] = 1
          mem[mem[64] + 100] = 160
          mem[mem[64] + 164] = mem[96]
          [94ms = 0
          mwhile [94ms < mem[96]m:
              mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms + 32
              mcontinue 
          if not mem[96] % 32:
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len mem[96] + [94m_126 + -mem[64] + 192]
          else:
              mem[floor32(mem[96]) + [94m_126 + 196] = mem[floor32(mem[96]) + [94m_126 + -(mem[96] % 32) + 228 len mem[96] % 32]
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len floor32(mem[96]) + [94m_126 + -mem[64] + 224]
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 3
          if not ext_call.return_data[0]:
              mem[0] = 2
              mem[32] = 19
              [94ms = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = 1
              [94mu = 1
              mcontinue 
          require ext_call.return_data[0] <= 3
          if ext_call.return_data[0] != 2:
              require ext_call.return_data[0] <= 3
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = [94mu
          mcontinue 
  else:
      if addr(mstor20m[callerm]m.field_256) != caller:
          revert with 0, 'Wrong address'
      if uint8(mstor20m[callerm]m.field_672):
          revert with 0, 'Module archived'
      require 0 < uint256(mstor20m[callerm]m.field_768)
      require 0 < uint256(mstor20m[callerm]m.field_768)
      [94ms = 0
      mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor20', 20))) + (0.03125 / s))m[uint8([94ms)m] != 3m:
          require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
          mem[32] = 20
          require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
          mem[0] = sha3(caller, 20) + 3
          [94ms = [94ms + 1
          mcontinue 
      if munknowna284de02:
          revert with 0, 'Minting frozen'
      if not m_to:
          revert with 0, 'Investor is 0'
      require not uint8(mstor5m.field_8)
      uint8(mstor5m.field_8) = 1
      mem[ceil32(m_data.length) + 128] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
      mem[ceil32(m_data.length) + 132] = 11
      mem[ceil32(m_data.length) + 164] = 0
      mem[ceil32(m_data.length) + 196] = m_to
      mem[ceil32(m_data.length) + 228] = m_amount
      mem[ceil32(m_data.length) + 260] = mbalanceOfm[addr(m_to)m]
      mem[ceil32(m_data.length) + 292] = mbalanceOf
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
           gas gas_remaining wei
          args 11, 0, addr(m_to), m_amount, mbalanceOfm[addr(m_to)m], mbalanceOf
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require mgranularity
      if m_amount % mgranularity:
          revert with 0, 'Invalid granularity'
      if mtransfersFrozen:
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
          [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
               gas gas_remaining wei
              args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
          if not delegate.return_code:
              revert with ext_call.return_data[0 len return_data.size]
          uint8(mstor5m.field_8) = 0
          revert with 0, 'Transfer invalid'
      mem[0] = 2
      mem[32] = 19
      [94ms = 0
      [94midx = 0
      [94mt = 0
      [94mt = 0
      [94mu = 0
      mwhile [94midx < mstorB9D2m.lengthm:
          if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = [94mt
              [94mu = [94mu
              mcontinue 
          mem[ceil32(m_data.length) + 128] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
          mem[ceil32(m_data.length) + 132] = 0
          mem[ceil32(m_data.length) + 164] = m_to
          mem[ceil32(m_data.length) + 196] = m_amount
          mem[ceil32(m_data.length) + 260] = 1
          mem[ceil32(m_data.length) + 228] = 160
          mem[ceil32(m_data.length) + 292] = mem[96]
          [94ms = 0
          mwhile [94ms < mem[96]m:
              mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms + 32
              mcontinue 
          if not mem[96] % 32:
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len mem[96] + ceil32(m_data.length) + -mem[64] + 320]
          else:
              mem[floor32(mem[96]) + ceil32(m_data.length) + 324] = mem[floor32(mem[96]) + ceil32(m_data.length) + -(mem[96] % 32) + 356 len mem[96] % 32]
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_data.length) + -mem[64] + 352]
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 3
          if not ext_call.return_data[0]:
              mem[0] = 2
              mem[32] = 19
              [94ms = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = 1
              [94mu = 1
              mcontinue 
          require ext_call.return_data[0] <= 3
          if ext_call.return_data[0] != 2:
              require ext_call.return_data[0] <= 3
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = [94mu
          mcontinue 
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(0, 22), mbalanceOf, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  uint8(mstor5m.field_8) = 0
  if [94mt:
      revert with 0, 'Transfer invalid'
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args 23, mtotalSupply, mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require m_amount + mtotalSupply >= mtotalSupply
  mtotalSupply += m_amount
  require m_amount + mbalanceOfm[addr(m_to)m] >= mbalanceOfm[addr(m_to)m]
  mbalanceOfm[addr(m_to)m] += m_amount
  log Minted(
        address to=_amount,
        uint256 amount=_to)
  log Transfer(
        address from=_amount,
        address to=0,
        uint256 value=_to)
  return 1


# hash = 0x981b24d0
# getter = None
# const = None
# payable = False
def totalSupplyAt(uint256 m_blockNumber): # not payable
  require m_blockNumber <= mcurrentCheckpointId
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0xb58ae1e2 with:
       gas gas_remaining wei
      args 23, m_blockNumber, mtotalSupply
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return delegate.return_data[0]


# hash = 0xa0632461
# getter = None
# const = None
# payable = False
def unknowna0632461(addr m_param1): # not payable
  require caller == mowner
  if not uint8(mstor20m[addr(m_param1)m]m.field_672):
      revert with 0, 'Not archived'
  if not addr(mstor20m[addr(m_param1)m]m.field_256):
      revert with 0, 'Module missing'
  mem[128] = m_param1
  mem[160] = block.timestamp
  mem[192] = uint256(mstor20m[addr(m_param1)m]m.field_768)
  if not uint256(mstor20m[addr(m_param1)m]m.field_768):
      log 0x51b49bea: 96, addr(_param1), block.timestamp, uint256(stor20[addr(_param1)].field_768)
      mem[0] = m_param1
      mem[32] = 20
      mem[64] = (32 * uint256(mstor20m[addr(m_param1)m]m.field_768)) + 128
      mem[96] = uint256(mstor20m[addr(m_param1)m]m.field_768)
      if not uint256(mstor20m[addr(m_param1)m]m.field_768):
          [94midx = 0
          mwhile [94midx < uint256(mstor20m[addr(m_param1)m]m.field_768)m:
              require [94midx < mem[96]
              [94m_320 = mem[(32 * [94midx) + 128]
              require [94midx < uint256(mstor20m[addr(m_param1)m]m.field_1024)
              require uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1 < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
              addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0) = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)m]m.field_0)
              mem[0] = mem[(32 * [94midx) + 159 len 1]
              mem[32] = 19
              uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)--
              if uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) <= uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                  if uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) != uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                      require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
                      mem[0] = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)
                      mem[32] = 20
                      [94m_392 = sha3(addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20)
                      [94m_393 = mem[64]
                      mem[64] = mem[64] + (32 * uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)) + 32
                      mem[[94m_393] = uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)
                      if mnamem[[94m_392m]:
                          mem[0] = [94m_392 + 3
                          mem[[94m_393 + 32] = uint8(mstor[sha3([94m_392 + 3)m])
                          [94ms = [94m_393 + 32
                          [94mt = 0
                          mwhile [94m_393 + (32 * mnamem[[94m_392m]) > [94msm:
                              mem[[94ms + 32] = mstorsha3(_392 + 3)m[-(0.03125 / [94mt + 1) + [94mt + (-1 * 0.03125 / [94mt + 1 * [94mt) + 1m]
                              [94ms = [94ms + 32
                              [94mt = -([94mt + 1 / 32) + [94mt + (-1 * [94mt + 1 / 32 * [94mt) + 1
                              mcontinue 
                      [94ms = 0
                      mwhile [94ms < uint256(mstor20m[addr(mstor19m[[94m_320 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)m:
                          require [94ms < mem[[94m_393]
                          if mem[(32 * [94ms) + [94m_393 + 63 len 1] == uint8([94m_320):
                              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[[94m_320 << 248m]m.field_0)
                              mem[32] = 20
                              require [94ms < uint256(mstor20m[addr(mstor19m[[94m_320 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_1024)
                              mem[0] = sha3(addr(mstor19m[[94m_320 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20) + 4
                              uint256(mstor20m[addr(mstor19m[[94m_320 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m[[94ms + 4m]m.field_0) = uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)
                          [94ms = [94ms + 1
                          mcontinue 
              else:
                  mem[0] = sha3(mem[(32 * [94midx) + 128] << 248, 19)
                  [94ms = uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) + sha3(sha3(mem[(32 * [94midx) + 128] << 248, 19)) - 1
                  mwhile sha3(sha3(mem[(32 * [94midx) + 128] << 248, 19)) + uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) > [94msm:
                      uint256(mstor[[94msm]) = 0
                      [94ms = [94ms + 1
                      mcontinue 
                  if uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) != uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                      require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
                      mem[0] = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)
                      mem[32] = 20
                      [94m_672 = sha3(addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20)
                      [94m_673 = mem[64]
                      mem[64] = mem[64] + (32 * uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)) + 32
                      mem[[94m_673] = uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)
                      if mnamem[[94m_672m]:
                          mem[0] = [94m_672 + 3
                          mem[[94m_673 + 32] = uint8(mstor[sha3([94m_672 + 3)m])
                          [94ms = [94m_673 + 32
                          [94mt = 0
                          mwhile [94m_673 + (32 * mnamem[[94m_672m]) > [94msm:
                              mem[[94ms + 32] = mstorsha3(_672 + 3)m[-(0.03125 / [94mt + 1) + [94mt + (-1 * 0.03125 / [94mt + 1 * [94mt) + 1m]
                              [94ms = [94ms + 32
                              [94mt = -([94mt + 1 / 32) + [94mt + (-1 * [94mt + 1 / 32 * [94mt) + 1
                              mcontinue 
                      [94ms = 0
                      mwhile [94ms < uint256(mstor20m[addr(mstor19m[[94m_320 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)m:
                          require [94ms < mem[[94m_673]
                          if mem[(32 * [94ms) + [94m_673 + 63 len 1] == uint8([94m_320):
                              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[[94m_320 << 248m]m.field_0)
                              mem[32] = 20
                              require [94ms < uint256(mstor20m[addr(mstor19m[[94m_320 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_1024)
                              mem[0] = sha3(addr(mstor19m[[94m_320 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20) + 4
                              uint256(mstor20m[addr(mstor19m[[94m_320 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m[[94ms + 4m]m.field_0) = uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)
                          [94ms = [94ms + 1
                          mcontinue 
              [94midx = [94midx + 1
              mcontinue 
      else:
          mem[0] = sha3(addr(m_param1), 20) + 3
          mem[128] = uint8(mstor20m[addr(m_param1)m]m[3m]m.field_0)
          [94midx = 128
          [94ms = 0
          mwhile (32 * uint256(mstor20m[addr(m_param1)m]m.field_768)) + 96 > [94midxm:
              mem[[94midx + 32] = mstor('array', 3, ('map', ('mask_shl', 160, 0, 96, ('param', '_param1')), ('name', 'stor20', 20)))m[-(0.03125 / [94ms + 1) + [94ms + (-1 * 0.03125 / [94ms + 1 * [94ms) + 1m]
              [94midx = [94midx + 32
              [94ms = -([94ms + 1 / 32) + [94ms + (-1 * [94ms + 1 / 32 * [94ms) + 1
              mcontinue 
          [94midx = 0
          mwhile [94midx < uint256(mstor20m[addr(m_param1)m]m.field_768)m:
              require [94midx < mem[96]
              [94m_627 = mem[(32 * [94midx) + 128]
              require [94midx < uint256(mstor20m[addr(m_param1)m]m.field_1024)
              require uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1 < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
              addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0) = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)m]m.field_0)
              mem[0] = mem[(32 * [94midx) + 159 len 1]
              mem[32] = 19
              uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)--
              if uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) <= uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                  if uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) != uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                      require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
                      mem[0] = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)
                      mem[32] = 20
                      [94m_719 = sha3(addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20)
                      [94m_720 = mem[64]
                      mem[64] = mem[64] + (32 * uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)) + 32
                      mem[[94m_720] = uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)
                      if mnamem[[94m_719m]:
                          mem[0] = [94m_719 + 3
                          mem[[94m_720 + 32] = uint8(mstor[sha3([94m_719 + 3)m])
                          [94ms = [94m_720 + 32
                          [94mt = 0
                          mwhile [94m_720 + (32 * mnamem[[94m_719m]) > [94msm:
                              mem[[94ms + 32] = mstorsha3(_719 + 3)m[-(0.03125 / [94mt + 1) + [94mt + (-1 * 0.03125 / [94mt + 1 * [94mt) + 1m]
                              [94ms = [94ms + 32
                              [94mt = -([94mt + 1 / 32) + [94mt + (-1 * [94mt + 1 / 32 * [94mt) + 1
                              mcontinue 
                      [94ms = 0
                      mwhile [94ms < uint256(mstor20m[addr(mstor19m[[94m_627 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)m:
                          require [94ms < mem[[94m_720]
                          if mem[(32 * [94ms) + [94m_720 + 63 len 1] == uint8([94m_627):
                              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[[94m_627 << 248m]m.field_0)
                              mem[32] = 20
                              require [94ms < uint256(mstor20m[addr(mstor19m[[94m_627 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_1024)
                              mem[0] = sha3(addr(mstor19m[[94m_627 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20) + 4
                              uint256(mstor20m[addr(mstor19m[[94m_627 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m[[94ms + 4m]m.field_0) = uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)
                          [94ms = [94ms + 1
                          mcontinue 
              else:
                  mem[0] = sha3(mem[(32 * [94midx) + 128] << 248, 19)
                  [94ms = uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) + sha3(sha3(mem[(32 * [94midx) + 128] << 248, 19)) - 1
                  mwhile sha3(sha3(mem[(32 * [94midx) + 128] << 248, 19)) + uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) > [94msm:
                      uint256(mstor[[94msm]) = 0
                      [94ms = [94ms + 1
                      mcontinue 
                  if uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) != uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                      require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
                      mem[0] = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)
                      mem[32] = 20
                      [94m_950 = sha3(addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20)
                      [94m_951 = mem[64]
                      mem[64] = mem[64] + (32 * uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)) + 32
                      mem[[94m_951] = uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)
                      if mnamem[[94m_950m]:
                          mem[0] = [94m_950 + 3
                          mem[[94m_951 + 32] = uint8(mstor[sha3([94m_950 + 3)m])
                          [94ms = [94m_951 + 32
                          [94mt = 0
                          mwhile [94m_951 + (32 * mnamem[[94m_950m]) > [94msm:
                              mem[[94ms + 32] = mstorsha3(_950 + 3)m[-(0.03125 / [94mt + 1) + [94mt + (-1 * 0.03125 / [94mt + 1 * [94mt) + 1m]
                              [94ms = [94ms + 32
                              [94mt = -([94mt + 1 / 32) + [94mt + (-1 * [94mt + 1 / 32 * [94mt) + 1
                              mcontinue 
                      [94ms = 0
                      mwhile [94ms < uint256(mstor20m[addr(mstor19m[[94m_627 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)m:
                          require [94ms < mem[[94m_951]
                          if mem[(32 * [94ms) + [94m_951 + 63 len 1] == uint8([94m_627):
                              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[[94m_627 << 248m]m.field_0)
                              mem[32] = 20
                              require [94ms < uint256(mstor20m[addr(mstor19m[[94m_627 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_1024)
                              mem[0] = sha3(addr(mstor19m[[94m_627 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20) + 4
                              uint256(mstor20m[addr(mstor19m[[94m_627 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m[[94ms + 4m]m.field_0) = uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)
                          [94ms = [94ms + 1
                          mcontinue 
              [94midx = [94midx + 1
              mcontinue 
  else:
      mem[224] = uint8(mstor20m[addr(m_param1)m]m[3m]m.field_0)
      [94midx = 224
      [94ms = 0
      mwhile (32 * uint256(mstor20m[addr(m_param1)m]m.field_768)) + 224 > [94midx + 32m:
          mem[[94midx + 32] = mstor('array', 3, ('map', ('mask_shl', 160, 0, 96, ('param', '_param1')), ('name', 'stor20', 20)))m[-(0.03125 / [94ms + 1) + [94ms + (-1 * 0.03125 / [94ms + 1 * [94ms) + 1m]
          [94midx = [94midx + 32
          [94ms = -([94ms + 1 / 32) + [94ms + (-1 * [94ms + 1 / 32 * [94ms) + 1
          mcontinue 
      log 0x51b49bea: Array(len=uint256(stor20[addr(_param1)].field_768), data=mem[224 len 32 * uint256(stor20[addr(_param1)].field_768)]), addr(_param1), block.timestamp
      mem[0] = m_param1
      mem[32] = 20
      mem[64] = (32 * uint256(mstor20m[addr(m_param1)m]m.field_768)) + 128
      mem[96] = uint256(mstor20m[addr(m_param1)m]m.field_768)
      if not uint256(mstor20m[addr(m_param1)m]m.field_768):
          [94midx = 0
          mwhile [94midx < uint256(mstor20m[addr(m_param1)m]m.field_768)m:
              require [94midx < mem[96]
              [94m_631 = mem[(32 * [94midx) + 128]
              require [94midx < uint256(mstor20m[addr(m_param1)m]m.field_1024)
              require uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1 < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
              addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0) = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)m]m.field_0)
              mem[0] = mem[(32 * [94midx) + 159 len 1]
              mem[32] = 19
              uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)--
              if uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) <= uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                  if uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) != uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                      require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
                      mem[0] = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)
                      mem[32] = 20
                      [94m_722 = sha3(addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20)
                      [94m_723 = mem[64]
                      mem[64] = mem[64] + (32 * uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)) + 32
                      mem[[94m_723] = uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)
                      if mnamem[[94m_722m]:
                          mem[0] = [94m_722 + 3
                          mem[[94m_723 + 32] = uint8(mstor[sha3([94m_722 + 3)m])
                          [94ms = [94m_723 + 32
                          [94mt = 0
                          mwhile [94m_723 + (32 * mnamem[[94m_722m]) > [94msm:
                              mem[[94ms + 32] = mstorsha3(_722 + 3)m[-(0.03125 / [94mt + 1) + [94mt + (-1 * 0.03125 / [94mt + 1 * [94mt) + 1m]
                              [94ms = [94ms + 32
                              [94mt = -([94mt + 1 / 32) + [94mt + (-1 * [94mt + 1 / 32 * [94mt) + 1
                              mcontinue 
                      [94ms = 0
                      mwhile [94ms < uint256(mstor20m[addr(mstor19m[[94m_631 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)m:
                          require [94ms < mem[[94m_723]
                          if mem[(32 * [94ms) + [94m_723 + 63 len 1] == uint8([94m_631):
                              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[[94m_631 << 248m]m.field_0)
                              mem[32] = 20
                              require [94ms < uint256(mstor20m[addr(mstor19m[[94m_631 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_1024)
                              mem[0] = sha3(addr(mstor19m[[94m_631 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20) + 4
                              uint256(mstor20m[addr(mstor19m[[94m_631 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m[[94ms + 4m]m.field_0) = uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)
                          [94ms = [94ms + 1
                          mcontinue 
              else:
                  mem[0] = sha3(mem[(32 * [94midx) + 128] << 248, 19)
                  [94ms = uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) + sha3(sha3(mem[(32 * [94midx) + 128] << 248, 19)) - 1
                  mwhile sha3(sha3(mem[(32 * [94midx) + 128] << 248, 19)) + uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) > [94msm:
                      uint256(mstor[[94msm]) = 0
                      [94ms = [94ms + 1
                      mcontinue 
                  if uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) != uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                      require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
                      mem[0] = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)
                      mem[32] = 20
                      [94m_957 = sha3(addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20)
                      [94m_958 = mem[64]
                      mem[64] = mem[64] + (32 * uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)) + 32
                      mem[[94m_958] = uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)
                      if mnamem[[94m_957m]:
                          mem[0] = [94m_957 + 3
                          mem[[94m_958 + 32] = uint8(mstor[sha3([94m_957 + 3)m])
                          [94ms = [94m_958 + 32
                          [94mt = 0
                          mwhile [94m_958 + (32 * mnamem[[94m_957m]) > [94msm:
                              mem[[94ms + 32] = mstorsha3(_957 + 3)m[-(0.03125 / [94mt + 1) + [94mt + (-1 * 0.03125 / [94mt + 1 * [94mt) + 1m]
                              [94ms = [94ms + 32
                              [94mt = -([94mt + 1 / 32) + [94mt + (-1 * [94mt + 1 / 32 * [94mt) + 1
                              mcontinue 
                      [94ms = 0
                      mwhile [94ms < uint256(mstor20m[addr(mstor19m[[94m_631 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)m:
                          require [94ms < mem[[94m_958]
                          if mem[(32 * [94ms) + [94m_958 + 63 len 1] == uint8([94m_631):
                              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[[94m_631 << 248m]m.field_0)
                              mem[32] = 20
                              require [94ms < uint256(mstor20m[addr(mstor19m[[94m_631 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_1024)
                              mem[0] = sha3(addr(mstor19m[[94m_631 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20) + 4
                              uint256(mstor20m[addr(mstor19m[[94m_631 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m[[94ms + 4m]m.field_0) = uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)
                          [94ms = [94ms + 1
                          mcontinue 
              [94midx = [94midx + 1
              mcontinue 
      else:
          mem[0] = sha3(addr(m_param1), 20) + 3
          mem[128] = uint8(mstor20m[addr(m_param1)m]m[3m]m.field_0)
          [94midx = 128
          [94ms = 0
          mwhile (32 * uint256(mstor20m[addr(m_param1)m]m.field_768)) + 96 > [94midxm:
              mem[[94midx + 32] = mstor('array', 3, ('map', ('mask_shl', 160, 0, 96, ('param', '_param1')), ('name', 'stor20', 20)))m[-(0.03125 / [94ms + 1) + [94ms + (-1 * 0.03125 / [94ms + 1 * [94ms) + 1m]
              [94midx = [94midx + 32
              [94ms = -([94ms + 1 / 32) + [94ms + (-1 * [94ms + 1 / 32 * [94ms) + 1
              mcontinue 
          [94midx = 0
          mwhile [94midx < uint256(mstor20m[addr(m_param1)m]m.field_768)m:
              require [94midx < mem[96]
              [94m_898 = mem[(32 * [94midx) + 128]
              require [94midx < uint256(mstor20m[addr(m_param1)m]m.field_1024)
              require uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1 < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
              addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0) = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)m]m.field_0)
              mem[0] = mem[(32 * [94midx) + 159 len 1]
              mem[32] = 19
              uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)--
              if uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) <= uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                  if uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) != uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                      require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
                      mem[0] = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)
                      mem[32] = 20
                      [94m_996 = sha3(addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20)
                      [94m_997 = mem[64]
                      mem[64] = mem[64] + (32 * uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)) + 32
                      mem[[94m_997] = uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)
                      if mnamem[[94m_996m]:
                          mem[0] = [94m_996 + 3
                          mem[[94m_997 + 32] = uint8(mstor[sha3([94m_996 + 3)m])
                          [94ms = [94m_997 + 32
                          [94mt = 0
                          mwhile [94m_997 + (32 * mnamem[[94m_996m]) > [94msm:
                              mem[[94ms + 32] = mstorsha3(_996 + 3)m[-(0.03125 / [94mt + 1) + [94mt + (-1 * 0.03125 / [94mt + 1 * [94mt) + 1m]
                              [94ms = [94ms + 32
                              [94mt = -([94mt + 1 / 32) + [94mt + (-1 * [94mt + 1 / 32 * [94mt) + 1
                              mcontinue 
                      [94ms = 0
                      mwhile [94ms < uint256(mstor20m[addr(mstor19m[[94m_898 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)m:
                          require [94ms < mem[[94m_997]
                          if mem[(32 * [94ms) + [94m_997 + 63 len 1] == uint8([94m_898):
                              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[[94m_898 << 248m]m.field_0)
                              mem[32] = 20
                              require [94ms < uint256(mstor20m[addr(mstor19m[[94m_898 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_1024)
                              mem[0] = sha3(addr(mstor19m[[94m_898 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20) + 4
                              uint256(mstor20m[addr(mstor19m[[94m_898 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m[[94ms + 4m]m.field_0) = uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)
                          [94ms = [94ms + 1
                          mcontinue 
              else:
                  mem[0] = sha3(mem[(32 * [94midx) + 128] << 248, 19)
                  [94ms = uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) + sha3(sha3(mem[(32 * [94midx) + 128] << 248, 19)) - 1
                  mwhile sha3(sha3(mem[(32 * [94midx) + 128] << 248, 19)) + uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) > [94msm:
                      uint256(mstor[[94msm]) = 0
                      [94ms = [94ms + 1
                      mcontinue 
                  if uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) != uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0) - 1:
                      require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[mem[(32 * [94midx) + 128] << 248m]m.field_0)
                      mem[0] = addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)
                      mem[32] = 20
                      [94m_1132 = sha3(addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20)
                      [94m_1133 = mem[64]
                      mem[64] = mem[64] + (32 * uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)) + 32
                      mem[[94m_1133] = uint256(mstor20m[addr(mstor19m[mem[(32 * [94midx) + 128] << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)
                      if mnamem[[94m_1132m]:
                          mem[0] = [94m_1132 + 3
                          mem[[94m_1133 + 32] = uint8(mstor[sha3([94m_1132 + 3)m])
                          [94ms = [94m_1133 + 32
                          [94mt = 0
                          mwhile [94m_1133 + (32 * mnamem[[94m_1132m]) > [94msm:
                              mem[[94ms + 32] = mstorsha3(_1132 + 3)m[-(0.03125 / [94mt + 1) + [94mt + (-1 * 0.03125 / [94mt + 1 * [94mt) + 1m]
                              [94ms = [94ms + 32
                              [94mt = -([94mt + 1 / 32) + [94mt + (-1 * [94mt + 1 / 32 * [94mt) + 1
                              mcontinue 
                      [94ms = 0
                      mwhile [94ms < uint256(mstor20m[addr(mstor19m[[94m_898 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_768)m:
                          require [94ms < mem[[94m_1133]
                          if mem[(32 * [94ms) + [94m_1133 + 63 len 1] == uint8([94m_898):
                              require uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) < uint256(mstor19m[[94m_898 << 248m]m.field_0)
                              mem[32] = 20
                              require [94ms < uint256(mstor20m[addr(mstor19m[[94m_898 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m.field_1024)
                              mem[0] = sha3(addr(mstor19m[[94m_898 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0), 20) + 4
                              uint256(mstor20m[addr(mstor19m[[94m_898 << 248m]m[uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)m]m.field_0)m]m[[94ms + 4m]m.field_0) = uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0)
                          [94ms = [94ms + 1
                          mcontinue 
              [94midx = [94midx + 1
              mcontinue 
  require uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0) - 1 < uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0)
  require uint256(mstor20m[addr(m_param1)m]m.field_1280) < uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0)
  addr(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m[uint256(mstor20m[addr(m_param1)m]m.field_1280)m]m.field_0) = addr(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m[uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0)m]m.field_0)
  uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0)--
  if uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0) > uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0) - 1:
      [94midx = uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0) - 1
      mwhile uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0) > [94midxm:
          uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m[[94midxm]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 
  if uint256(mstor20m[addr(m_param1)m]m.field_1280) != uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0) - 1:
      require uint256(mstor20m[addr(m_param1)m]m.field_1280) < uint256(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m.field_0)
      uint256(mstor20m[addr(mstor21m[uint256(mstor20m[addr(m_param1)m]m.field_0)m]m[uint256(mstor20m[addr(m_param1)m]m.field_1280)m]m.field_0)m]m.field_1280) = uint256(mstor20m[addr(m_param1)m]m.field_1280)
  uint256(mstor20m[addr(m_param1)m]m.field_0) = 0
  addr(mstor20m[addr(m_param1)m]m.field_256) = 0
  Mask(168, 0, mstor20m[addr(m_param1)m]m.field_512) = 0
  uint256(mstor20m[addr(m_param1)m]m.field_768) = 0
  [94midx = 0
  mwhile uint256(mstor20m[addr(m_param1)m]m.field_768) + 31 / 32 > [94midxm:
      uint256(mstor20m[addr(m_param1)m]m[[94midx + 3m]m.field_0) = 0
      [94midx = [94midx + 1
      mcontinue 
  uint256(mstor20m[addr(m_param1)m]m.field_1024) = 0
  [94midx = 0
  mwhile uint256(mstor20m[addr(m_param1)m]m.field_1024) > [94midxm:
      uint256(mstor20m[addr(m_param1)m]m[[94midx + 4m]m.field_0) = 0
      [94midx = [94midx + 1
      mcontinue 
  uint256(mstor20m[addr(m_param1)m]m.field_1280) = 0


# hash = 0xa1db9782
# getter = None
# const = None
# payable = False
def withdrawERC20(address m_contractAddress, uint256 m_amount): # not payable
  require caller == mowner
  require m_contractAddress
  require ext_code.size(m_contractAddress)
  call m_contractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args addr(mstor5m.field_0), m_amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]


# hash = 0xa284de02
# getter = ['bool', ['storage', 8, 8, 18]]
# const = None
# payable = False
def unknowna284de02(): # not payable
  return bool(munknowna284de02)


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_value): # not payable
  mem[64] = 128
  mem[96] = 0
  require not uint8(mstor5m.field_8)
  uint8(mstor5m.field_8) = 1
  mem[128] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
  mem[132] = 11
  mem[164] = caller
  mem[196] = m_to
  mem[228] = m_value
  mem[260] = mbalanceOfm[addr(m_to)m]
  mem[292] = mbalanceOfm[callerm]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
       gas gas_remaining wei
      args 0, 11, caller, addr(m_to), m_value, mbalanceOfm[addr(m_to)m], mbalanceOfm[callerm]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mgranularity
  if m_value % mgranularity:
      revert with 0, 'Invalid granularity'
  if mtransfersFrozen:
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(caller, 22), mbalanceOfm[callerm], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      uint8(mstor5m.field_8) = 0
      revert with 0, 'Transfer invalid'
  mem[0] = 2
  mem[32] = 19
  [94ms = 0
  [94midx = 0
  [94mt = 0
  [94mt = 0
  [94mu = 0
  mwhile [94midx < mstorB9D2m.lengthm:
      if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
          mem[0] = 2
          mem[32] = 19
          [94ms = [94ms
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = [94mt
          [94mu = [94mu
          mcontinue 
      mem[128] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
      mem[132] = caller
      mem[164] = m_to
      mem[196] = m_value
      mem[260] = 1
      mem[228] = 160
      mem[292] = mem[96]
      [94ms = 0
      mwhile [94ms < mem[96]m:
          mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
          mem[0] = 2
          mem[32] = 19
          [94ms = [94ms + 32
          mcontinue 
      if not mem[96] % 32:
          require ext_code.size(mstorB9D2m[[94midxm])
          call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
               gas gas_remaining wei
              args mem[mem[64] + 4 len mem[96] + -mem[64] + 320]
      else:
          mem[floor32(mem[96]) + 324] = mem[floor32(mem[96]) + -(mem[96] % 32) + 356 len mem[96] % 32]
          require ext_code.size(mstorB9D2m[[94midxm])
          call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
               gas gas_remaining wei
              args mem[mem[64] + 4 len floor32(mem[96]) + -mem[64] + 352]
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0] <= 3
      if not ext_call.return_data[0]:
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = 1
          mcontinue 
      require ext_call.return_data[0] <= 3
      if ext_call.return_data[0] != 2:
          require ext_call.return_data[0] <= 3
      mem[0] = 2
      mem[32] = 19
      [94ms = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94mt = mstorB9D2m[[94midxm]
      [94mt = 1
      [94mu = [94mu
      mcontinue 
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(caller, 22), mbalanceOfm[callerm], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  uint8(mstor5m.field_8) = 0
  if [94mt:
      revert with 0, 'Transfer invalid'
  require m_to
  require m_value <= mbalanceOfm[callerm]
  require m_value <= mbalanceOfm[callerm]
  mbalanceOfm[callerm] -= m_value
  require m_value + mbalanceOfm[m_tom] >= mbalanceOfm[m_tom]
  mbalanceOfm[addr(m_to)m] = m_value + mbalanceOfm[m_tom]
  log Transfer(
        address from=_value,
        address to=caller,
        uint256 value=_to)
  return 1


# hash = 0xac90b422
# getter = None
# const = None
# payable = False
def unknownac90b422(uint8 m_param1): # not payable
  if uint256(mstor19m[m_param1 << 248m]m.field_0):
      mem[128] = addr(mstor19m[m_param1 << 248m]m.field_0)
      if (32 * uint256(mstor19m[m_param1 << 248m]m.field_0)) + 32 > 64:
          mem[160] = addr(mstor19m[m_param1 << 248m]m.field_256)
          [94midx = 160
          [94ms = 1
          mwhile (32 * uint256(mstor19m[m_param1 << 248m]m.field_0)) + 96 > [94midxm:
              mem[[94midx + 32] = addr(mstor19m[m_param1 << 248m]m[[94msm]m.field_256)
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
  mem[(32 * uint256(mstor19m[m_param1 << 248m]m.field_0)) + 128] = 32
  mem[(32 * uint256(mstor19m[m_param1 << 248m]m.field_0)) + 160] = uint256(mstor19m[m_param1 << 248m]m.field_0)
  mem[(32 * uint256(mstor19m[m_param1 << 248m]m.field_0)) + 192 len floor32(uint256(mstor19m[m_param1 << 248m]m.field_0))] = mem[128 len floor32(uint256(mstor19m[m_param1 << 248m]m.field_0))]
  return memory
    from (32 * uint256(mstor19m[m_param1 << 248m]m.field_0)) + 128
     [93mlen (96 * uint256(mstor19m[m_param1 << 248m]m.field_0)) + 64


# hash = 0xb2f5a54c
# getter = None
# const = None
# payable = False
def getInvestors(): # not payable
  if not mstor12m.length:
      mem[(32 * mstor12m.length) + 128] = 32
      mem[(32 * mstor12m.length) + 160] = mstor12m.length
      mem[(32 * mstor12m.length) + 192 len floor32(mstor12m.length)] = mem[128 len floor32(mstor12m.length)]
      return memory
        from (32 * mstor12m.length) + 128
         [93mlen (96 * mstor12m.length) + 64
  mem[128] = addr(mstor12m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * mstor12m.length) + 96 > [94midxm:
      mem[[94midx + 32] = addr(mstor12m[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mstor12m.length) + 192 len floor32(mstor12m.length)] = mem[128 len floor32(mstor12m.length)]
  return Array(len=mstor12m.length, data=mem[128 len floor32(mstor12m.length)], mem[(32 * mstor12m.length) + floor32(mstor12m.length) + 192 len (32 * mstor12m.length) - floor32(mstor12m.length)]), 


# hash = 0xb5de8d4c
# getter = None
# const = None
# payable = False
def getModule(address m_acct): # not payable
  if uint256(mstor20m[addr(m_acct)m]m.field_768):
      mem[128] = uint8(mstor20m[addr(m_acct)m]m[3m]m.field_0)
      [94midx = 128
      [94ms = 0
      mwhile (32 * uint256(mstor20m[addr(m_acct)m]m.field_768)) + 96 > [94midxm:
          mem[[94midx + 32] = mstor('array', 3, ('map', ('mask_shl', 160, 0, 96, ('param', '_acct')), ('name', 'stor20', 20)))m[-(0.03125 / [94ms + 1) + [94ms + (-1 * 0.03125 / [94ms + 1 * [94ms) + 1m]
          [94midx = [94midx + 32
          [94ms = -([94ms + 1 / 32) + [94ms + (-1 * [94ms + 1 / 32 * [94ms) + 1
          mcontinue 
  mem[(32 * uint256(mstor20m[addr(m_acct)m]m.field_768)) + 320 len floor32(uint256(mstor20m[addr(m_acct)m]m.field_768))] = mem[128 len floor32(uint256(mstor20m[addr(m_acct)m]m.field_768))]
  return uint256(mstor20m[addr(m_acct)m]m.field_0), 
         addr(mstor20m[addr(m_acct)m]m.field_256),
         addr(mstor20m[addr(m_acct)m]m.field_512),
         bool(uint8(mstor20m[addr(m_acct)m]m.field_672)),
         Array(len=uint256(mstor20m[addr(m_acct)m]m.field_768), data=mem[128 len floor32(uint256(mstor20m[addr(m_acct)m]m.field_768))], mem[(32 * uint256(mstor20m[addr(m_acct)m]m.field_768)) + floor32(uint256(mstor20m[addr(m_acct)m]m.field_768)) + 320 len (32 * uint256(mstor20m[addr(m_acct)m]m.field_768)) - floor32(uint256(mstor20m[addr(m_acct)m]m.field_768))])


# hash = 0xb95459e4
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def moduleRegistry(): # not payable
  return addr(mmoduleRegistryAddress)


# hash = 0xc013f30f
# getter = None
# const = None
# payable = False
def unknownc013f30f(): # not payable
  if munknowna284de02:
      revert with 0, 'Minting frozen'
  require ext_code.size(addr(munknowncaf90dabAddress))
  call addr(munknowncaf90dabAddress).0x2f0019f2 with:
       gas gas_remaining wei
      args 'freezeMintingAllowed'
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require caller == mowner
  munknowna284de02 = 1
  log 0xac303fba: block.timestamp


# hash = 0xcaf90dab
# getter = ['storage', 160, 0, 9]
# const = None
# payable = False
def unknowncaf90dab(): # not payable
  return addr(munknowncaf90dabAddress)


# hash = 0xce4dbdff
# getter = ['storage', 160, 0, 8]
# const = None
# payable = False
def securityTokenRegistry(): # not payable
  return addr(msecurityTokenRegistryAddress)


# hash = 0xd6abe110
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 15]]]], ['loc', 15]]]
# const = None
# payable = False
def tokenDetails(): # not payable
  return uint256(mtokenDetailsm[0 len mtokenDetailsm.lengthm]m.field_0)


# hash = 0xd73dd623
# getter = None
# const = None
# payable = False
def increaseApproval(address m_spender, uint256 m_addedValue): # not payable
  require m_addedValue + mallowancem[callerm]m[addr(m_spender)m] >= mallowancem[callerm]m[addr(m_spender)m]
  mallowancem[callerm]m[addr(m_spender)m] += m_addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]
# const = None
# payable = False
def allowance(address m_owner, address m_spender): # not payable
  return mallowancem[addr(m_owner)m]m[addr(m_spender)m]


# hash = 0xe45b8134
# getter = ['bool', ['storage', 8, 0, 18]]
# const = None
# payable = False
def transfersFrozen(): # not payable
  return bool(mtransfersFrozen)


# hash = 0xee532f31
# getter = None
# const = None
# payable = False
def transferFromWithData(address m_from, address m_to, uint256 m_value, bytes m_data): # not payable
  mem[64] = ceil32(m_data.length) + 128
  mem[96] = m_data.length
  mem[128 len m_data.length] = m_data[allm]
  require not uint8(mstor5m.field_8)
  uint8(mstor5m.field_8) = 1
  mem[ceil32(m_data.length) + 128] = 0x17dd222c00000000000000000000000000000000000000000000000000000000
  mem[ceil32(m_data.length) + 132] = 11
  mem[ceil32(m_data.length) + 164] = m_from
  mem[ceil32(m_data.length) + 196] = m_to
  mem[ceil32(m_data.length) + 228] = m_value
  mem[ceil32(m_data.length) + 260] = mbalanceOfm[addr(m_to)m]
  mem[ceil32(m_data.length) + 292] = mbalanceOfm[addr(m_from)m]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x17dd222c with:
       gas gas_remaining wei
      args 11, addr(m_from), addr(m_to), m_value, mbalanceOfm[addr(m_to)m], mbalanceOfm[addr(m_from)m]
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require mgranularity
  if m_value % mgranularity:
      revert with 0, 'Invalid granularity'
  if mtransfersFrozen:
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_from), 22), mbalanceOfm[addr(m_from)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
      [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
           gas gas_remaining wei
          args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
      if not delegate.return_code:
          revert with ext_call.return_data[0 len return_data.size]
      uint8(mstor5m.field_8) = 0
      revert with 0, 'Transfer invalid'
  mem[0] = 2
  mem[32] = 19
  [94ms = 0
  [94midx = 0
  [94mt = 0
  [94mt = 0
  [94mu = 0
  mwhile [94midx < mstorB9D2m.lengthm:
      if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
          mem[0] = 2
          mem[32] = 19
          [94ms = [94ms
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = [94mt
          [94mu = [94mu
          mcontinue 
      mem[ceil32(m_data.length) + 128] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
      mem[ceil32(m_data.length) + 132] = m_from
      mem[ceil32(m_data.length) + 164] = m_to
      mem[ceil32(m_data.length) + 196] = m_value
      mem[ceil32(m_data.length) + 260] = 1
      mem[ceil32(m_data.length) + 228] = 160
      mem[ceil32(m_data.length) + 292] = mem[96]
      [94ms = 0
      mwhile [94ms < mem[96]m:
          mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
          mem[0] = 2
          mem[32] = 19
          [94ms = [94ms + 32
          mcontinue 
      if not mem[96] % 32:
          require ext_code.size(mstorB9D2m[[94midxm])
          call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
               gas gas_remaining wei
              args mem[mem[64] + 4 len mem[96] + ceil32(m_data.length) + -mem[64] + 320]
      else:
          mem[floor32(mem[96]) + ceil32(m_data.length) + 324] = mem[floor32(mem[96]) + ceil32(m_data.length) + -(mem[96] % 32) + 356 len mem[96] % 32]
          require ext_code.size(mstorB9D2m[[94midxm])
          call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
               gas gas_remaining wei
              args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_data.length) + -mem[64] + 352]
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0] <= 3
      if not ext_call.return_data[0]:
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = 1
          mcontinue 
      require ext_call.return_data[0] <= 3
      if ext_call.return_data[0] != 2:
          require ext_call.return_data[0] <= 3
      mem[0] = 2
      mem[32] = 19
      [94ms = ext_call.return_data[0]
      [94midx = [94midx + 1
      [94mt = mstorB9D2m[[94midxm]
      [94mt = 1
      [94mu = [94mu
      mcontinue 
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(addr(m_from), 22), mbalanceOfm[addr(m_from)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(0x63e87665fab79f301968fabb26d11a606d7bacd2)
  [93mdelegate 0x63e87665fab79f301968fabb26d11a606d7bacd2.0x7c20d97 with:
       gas gas_remaining wei
      args sha3(addr(m_to), 22), mbalanceOfm[addr(m_to)m], mcurrentCheckpointId
  if not delegate.return_code:
      revert with ext_call.return_data[0 len return_data.size]
  uint8(mstor5m.field_8) = 0
  if [94mt:
      revert with 0, 'Transfer invalid'
  require m_to
  require m_value <= mbalanceOfm[addr(m_from)m]
  require m_value <= mallowancem[addr(m_from)m]m[callerm]
  require m_value <= mbalanceOfm[addr(m_from)m]
  mbalanceOfm[addr(m_from)m] -= m_value
  require m_value + mbalanceOfm[m_tom] >= mbalanceOfm[m_tom]
  mbalanceOfm[addr(m_to)m] = m_value + mbalanceOfm[m_tom]
  require m_value <= mallowancem[addr(m_from)m]m[callerm]
  mallowancem[addr(m_from)m]m[callerm] -= m_value
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 value=_to)
  return 1


# hash = 0xf1d74b0f
# getter = None
# const = None
# payable = False
def unknownf1d74b0f(addr m_param1, addr m_param2, uint256 m_param3, array m_param4): # not payable
  mem[64] = ceil32(m_param4.length) + 128
  mem[96] = m_param4.length
  mem[128 len m_param4.length] = m_param4[allm]
  require mgranularity
  if m_param3 % mgranularity:
      revert with 0, 'Invalid granularity'
  if not mtransfersFrozen:
      mem[0] = 2
      mem[32] = 19
      [94ms = 0
      [94midx = 0
      [94mt = 0
      [94mt = 0
      [94mu = 0
      mwhile [94midx < mstorB9D2m.lengthm:
          if uint8(mstor20m[mstorB9D2m[[94midxm]m]m.field_672):
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = [94mt
              [94mu = [94mu
              mcontinue 
          mem[ceil32(m_param4.length) + 128] = 0xde6ee1bc00000000000000000000000000000000000000000000000000000000
          mem[ceil32(m_param4.length) + 132] = m_param1
          mem[ceil32(m_param4.length) + 164] = m_param2
          mem[ceil32(m_param4.length) + 196] = m_param3
          mem[ceil32(m_param4.length) + 260] = 0
          mem[ceil32(m_param4.length) + 228] = 160
          mem[ceil32(m_param4.length) + 292] = mem[96]
          [94ms = 0
          mwhile [94ms < mem[96]m:
              mem[[94ms + mem[64] + 196] = mem[[94ms + 128]
              mem[0] = 2
              mem[32] = 19
              [94ms = [94ms + 32
              mcontinue 
          if not mem[96] % 32:
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len mem[96] + ceil32(m_param4.length) + -mem[64] + 320]
          else:
              mem[floor32(mem[96]) + ceil32(m_param4.length) + 324] = mem[floor32(mem[96]) + ceil32(m_param4.length) + -(mem[96] % 32) + 356 len mem[96] % 32]
              require ext_code.size(mstorB9D2m[[94midxm])
              call mstorB9D2m[[94midxm].mem[mem[64] len 4] with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len floor32(mem[96]) + ceil32(m_param4.length) + -mem[64] + 352]
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 3
          if not ext_call.return_data[0]:
              mem[0] = 2
              mem[32] = 19
              [94ms = ext_call.return_data[0]
              [94midx = [94midx + 1
              [94mt = mstorB9D2m[[94midxm]
              [94mt = 1
              [94mu = 1
              mcontinue 
          require ext_call.return_data[0] <= 3
          if ext_call.return_data[0] != 2:
              require ext_call.return_data[0] <= 3
          mem[0] = 2
          mem[32] = 19
          [94ms = ext_call.return_data[0]
          [94midx = [94midx + 1
          [94mt = mstorB9D2m[[94midxm]
          [94mt = 1
          [94mu = [94mu
          mcontinue 
      if not [94mt:
          return 1
      return 0
  else:
      return 0


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf433262f
# getter = None
# const = None
# payable = False
def updateFromRegistry(): # not payable
  require caller == mowner
  require ext_code.size(munknown5aa14a70Address)
  call munknown5aa14a70Address.getAddress(string channelId) with:
       gas gas_remaining wei
      args Array(len=14, data='ModuleRegistry')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor7) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor7))
  require ext_code.size(munknown5aa14a70Address)
  call munknown5aa14a70Address.getAddress(string channelId) with:
       gas gas_remaining wei
      args Array(len=21, data='SecurityTokenRegistry')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor8) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor8))
  require ext_code.size(munknown5aa14a70Address)
  call munknown5aa14a70Address.getAddress(string channelId) with:
       gas gas_remaining wei
      args Array(len=15, data='FeatureRegistry')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor9) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor9))
  require ext_code.size(munknown5aa14a70Address)
  call munknown5aa14a70Address.getAddress(string channelId) with:
       gas gas_remaining wei
      args Array(len=10, data='ProofToken')
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  uint256(mstor10) = ext_call.return_data[12 len 20] or Mask(96, 160, uint256(mstor10))


# hash = 0xf5efbd2d
# getter = None
# const = None
# payable = False
def addModule(address m_moduleFactory, bytes m_data, uint256 m_maxCost, uint256 m_budget): # not payable
  require caller == mowner
  require not uint8(mstor5m.field_8)
  uint8(mstor5m.field_8) = 1
  mem[100] = m_moduleFactory
  require ext_code.size(addr(mmoduleRegistryAddress))
  call addr(mmoduleRegistryAddress).useModule(address moduleFactory) with:
       gas gas_remaining wei
      args m_moduleFactory
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96] = 0xb4579d6000000000000000000000000000000000000000000000000000000000
  require ext_code.size(m_moduleFactory)
  call m_moduleFactory.getTypes() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 32
  [94m_6 = mem[96]
  require mem[96] <= 4294967296
  require mem[96] + 32 <= return_data.size
  require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
  require ext_code.size(m_moduleFactory)
  call m_moduleFactory.getSetupCost() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] > m_maxCost:
      revert with 0, 'Invalid cost'
  require ext_code.size(addr(mproofTokenAddress))
  call addr(mproofTokenAddress).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args addr(m_moduleFactory), ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[ceil32(return_data.size) + 164 len m_data.length] = m_data[allm]
  require ext_code.size(m_moduleFactory)
  call m_moduleFactory with:
     funct Mask(32, 224, 'wC`') >> 224
       gas gas_remaining wei
      args Array(len=m_data.length, data=m_data[allm])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[0] = ext_call.return_data[12 len 20]
  mem[32] = 20
  if addr(mstor20m[ext_call.return_data[12 len 20]m]m.field_256):
      revert with 0, 'Module exists'
  mem[ceil32(return_data.size) + 100] = addr(ext_call.return_data[0])
  mem[ceil32(return_data.size) + 132] = m_budget
  require ext_code.size(addr(mproofTokenAddress))
  call addr(mproofTokenAddress).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args addr(ext_call.return_data[0]), m_budget
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_moduleFactory)
  call m_moduleFactory.getName() with:
       gas gas_remaining wei
  mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  [94m_31 = mem[[94m_6 + 96]
  mem[ceil32(return_data.size) + 96] = mem[[94m_6 + 96]
  mem[64] = ceil32(return_data.size) + (32 * [94m_31) + 128
  if not [94m_31:
      [94m_153 = mem[[94m_6 + 96]
      [94midx = 0
      mwhile [94midx < [94m_153m:
          require [94midx < mem[[94m_6 + 96]
          require [94midx < mem[ceil32(return_data.size) + 96]
          mem[ceil32(return_data.size) + (32 * [94midx) + 128] = uint256(mstor19m[mem[[94m_6 + (32 * [94midx) + 159 len 1]m]m.field_0)
          require [94midx < mem[[94m_6 + 96]
          mem[32] = 19
          uint256(mstor19m[mem[(32 * [94midx) + [94m_6 + 159 len 1]m]m.field_0)++
          mem[0] = sha3(mem[(32 * [94midx) + [94m_6 + 159 len 1], 19)
          addr(mstor19m[mem[(32 * [94midx) + [94m_6 + 159 len 1]m]m[uint256(mstor19m[mem[(32 * [94midx) + [94m_6 + 159 len 1]m]m.field_0)m]m.field_0) = addr(ext_call.return_data[0])
          [94midx = [94midx + 1
          mcontinue 
      mem[64] = ceil32(return_data.size) + (32 * [94m_31) + 352
      mem[ceil32(return_data.size) + (32 * [94m_31) + 128] = ext_call.return_data[0]
      mem[ceil32(return_data.size) + (32 * [94m_31) + 160] = addr(ext_call.return_data[0])
      mem[ceil32(return_data.size) + (32 * [94m_31) + 192] = m_moduleFactory
      mem[ceil32(return_data.size) + (32 * [94m_31) + 224] = 0
      mem[ceil32(return_data.size) + (32 * [94m_31) + 256] = [94m_6 + 96
      mem[ceil32(return_data.size) + (32 * [94m_31) + 288] = ceil32(return_data.size) + 96
      mem[ceil32(return_data.size) + (32 * [94m_31) + 320] = uint256(mstor21m[ext_call.return_data[0]m]m.field_0)
      uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_0) = ext_call.return_data[0]
      addr(mstor20m[addr(ext_call.return_data[0])m]m.field_256) = addr(ext_call.return_data[0])
      addr(mstor20m[addr(ext_call.return_data[0])m]m.field_512) = m_moduleFactory
      Mask(96, 0, mstor20m[addr(ext_call.return_data[0])m]m.field_672) = 0
      uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_768) = mem[[94m_6 + 96]
      if not mem[[94m_6 + 96]:
          [94midx = 0
          mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_768) + 31 / 32 > [94midxm:
              uint8(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) = mem[ceil32(return_data.size) + 96]
          if not mem[ceil32(return_data.size) + 96]:
              [94midx = 0
              mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
              uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1280) = uint256(mstor21m[ext_call.return_data[0]m]m.field_0)
              uint256(mstor21m[ext_call.return_data[0]m]m.field_0)++
              addr(mstor21m[ext_call.return_data[0]m]m[uint256(mstor21m[ext_call.return_data[0]m]m.field_0)m]m.field_0) = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 384] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 416] = m_moduleFactory
              mem[ceil32(return_data.size) + (32 * [94m_31) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 480] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 512] = m_budget
              mem[ceil32(return_data.size) + (32 * [94m_31) + 544] = block.timestamp
              mem[ceil32(return_data.size) + (32 * [94m_31) + 352] = 224
              mem[ceil32(return_data.size) + (32 * [94m_31) + 576] = mem[[94m_6 + 96]
              [94m_362 = mem[[94m_6 + 96]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 608 len floor32(mem[[94m_6 + 96])] = mem[[94m_6 + 128 len floor32(mem[[94m_6 + 96])]
              [94mvar55001 = floor32([94m_362)
              log 0xa902846e: 224, ext_call.return_data[0], addr(_moduleFactory), addr(ext_call.return_data[0]), ext_call.return_data[0], _budget, block.timestamp, mem[ceil32(return_data.size) + (32 * _31) + 576 len (32 * _362) + 32]
          else:
              [94ms = 0
              [94midx = ceil32(return_data.size) + 128
              mwhile ceil32(return_data.size) + (32 * mem[ceil32(return_data.size) + 96]) + 128 > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0) = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(return_data.size) + 96]) + 31) >> 5
              mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
              uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1280) = uint256(mstor21m[ext_call.return_data[0]m]m.field_0)
              uint256(mstor21m[ext_call.return_data[0]m]m.field_0)++
              addr(mstor21m[ext_call.return_data[0]m]m[uint256(mstor21m[ext_call.return_data[0]m]m.field_0)m]m.field_0) = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 384] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 416] = m_moduleFactory
              mem[ceil32(return_data.size) + (32 * [94m_31) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 480] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 512] = m_budget
              mem[ceil32(return_data.size) + (32 * [94m_31) + 544] = block.timestamp
              mem[ceil32(return_data.size) + (32 * [94m_31) + 352] = 224
              mem[ceil32(return_data.size) + (32 * [94m_31) + 576] = mem[[94m_6 + 96]
              [94m_438 = mem[[94m_6 + 96]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 608 len floor32(mem[[94m_6 + 96])] = mem[[94m_6 + 128 len floor32(mem[[94m_6 + 96])]
              [94mvar58001 = floor32([94m_438)
              log 0xa902846e: 224, ext_call.return_data[0], addr(_moduleFactory), addr(ext_call.return_data[0]), ext_call.return_data[0], _budget, block.timestamp, mem[ceil32(return_data.size) + (32 * _31) + 576 len (32 * _438) + 32]
      else:
          [94ms = 0
          [94midx = [94m_6 + 128
          mwhile [94m_6 + (32 * mem[[94m_6 + 96]) + 128 > [94midxm:
              uint256(mstor20m[addr(ext_call.return_data[0])m]m[3m]m.field_0) = mem[[94midx + 31 len 1] * 256^[94ms or !(255 * 256^[94ms) and uint256(mstor20m[addr(ext_call.return_data[0])m]m[3m]m.field_0)
              [94ms = [94ms + -([94ms + 1 / 32) + (-1 * [94ms * [94ms + 1 / 32) + 1
              [94midx = [94midx + 32
              mcontinue 
          [94midx = Mask(251, 0, (32 * mem[[94m_6 + 96]) + 31) >> 5
          [94ms = sha3(sha3(addr(ext_call.return_data[0]), 20) + 3)
          mwhile [94midxm:
              uint256(mstor[[94msm]) = !(255 * 256^[94midx) and uint256(mstor[[94msm])
              [94midx = [94midx + -([94midx + 1 / 32) + (-1 * [94midx * [94midx + 1 / 32) + 1
              [94ms = ([94midx + 1 / 32) + [94ms
              mcontinue 
          [94midx = (floor32(None + 3) >> 4) + (None * None + 3 / 32) - (Mask(251, 0, (32 * mem[[94m_6 + 96]) + 31) >> 5 * None + 3 / 32)
          mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_768) + 31 / 32 > [94midxm:
              uint8(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) = mem[ceil32(return_data.size) + 96]
          if not mem[ceil32(return_data.size) + 96]:
              [94midx = 0
              mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
              uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1280) = uint256(mstor21m[ext_call.return_data[0]m]m.field_0)
              uint256(mstor21m[ext_call.return_data[0]m]m.field_0)++
              addr(mstor21m[ext_call.return_data[0]m]m[uint256(mstor21m[ext_call.return_data[0]m]m.field_0)m]m.field_0) = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 384] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 416] = m_moduleFactory
              mem[ceil32(return_data.size) + (32 * [94m_31) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 480] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 512] = m_budget
              mem[ceil32(return_data.size) + (32 * [94m_31) + 544] = block.timestamp
              mem[ceil32(return_data.size) + (32 * [94m_31) + 352] = 224
              mem[ceil32(return_data.size) + (32 * [94m_31) + 576] = mem[[94m_6 + 96]
              [94m_500 = mem[[94m_6 + 96]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 608 len floor32(mem[[94m_6 + 96])] = mem[[94m_6 + 128 len floor32(mem[[94m_6 + 96])]
              log 0xa902846e: 224, ext_call.return_data[0], addr(_moduleFactory), addr(ext_call.return_data[0]), ext_call.return_data[0], _budget, block.timestamp, mem[ceil32(return_data.size) + (32 * _31) + 576 len (32 * _500) + 32]
          else:
              [94ms = 0
              [94midx = ceil32(return_data.size) + 128
              mwhile ceil32(return_data.size) + (32 * mem[ceil32(return_data.size) + 96]) + 128 > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0) = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(return_data.size) + 96]) + 31) >> 5
              mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
              uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1280) = uint256(mstor21m[ext_call.return_data[0]m]m.field_0)
              uint256(mstor21m[ext_call.return_data[0]m]m.field_0)++
              addr(mstor21m[ext_call.return_data[0]m]m[uint256(mstor21m[ext_call.return_data[0]m]m.field_0)m]m.field_0) = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 384] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 416] = m_moduleFactory
              mem[ceil32(return_data.size) + (32 * [94m_31) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 480] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 512] = m_budget
              mem[ceil32(return_data.size) + (32 * [94m_31) + 544] = block.timestamp
              mem[ceil32(return_data.size) + (32 * [94m_31) + 352] = 224
              mem[ceil32(return_data.size) + (32 * [94m_31) + 576] = mem[[94m_6 + 96]
              [94m_536 = mem[[94m_6 + 96]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 608 len floor32(mem[[94m_6 + 96])] = mem[[94m_6 + 128 len floor32(mem[[94m_6 + 96])]
              log 0xa902846e: 224, ext_call.return_data[0], addr(_moduleFactory), addr(ext_call.return_data[0]), ext_call.return_data[0], _budget, block.timestamp, mem[ceil32(return_data.size) + (32 * _31) + 576 len (32 * _536) + 32]
  else:
      mem[ceil32(return_data.size) + 128 len 32 * [94m_31] = code.data[22195 len 32 * [94m_31]
      [94m_154 = mem[[94m_6 + 96]
      [94midx = 0
      mwhile [94midx < [94m_154m:
          require [94midx < mem[[94m_6 + 96]
          require [94midx < mem[ceil32(return_data.size) + 96]
          mem[ceil32(return_data.size) + (32 * [94midx) + 128] = uint256(mstor19m[mem[[94m_6 + (32 * [94midx) + 159 len 1]m]m.field_0)
          require [94midx < mem[[94m_6 + 96]
          mem[32] = 19
          uint256(mstor19m[mem[(32 * [94midx) + [94m_6 + 159 len 1]m]m.field_0)++
          mem[0] = sha3(mem[(32 * [94midx) + [94m_6 + 159 len 1], 19)
          addr(mstor19m[mem[(32 * [94midx) + [94m_6 + 159 len 1]m]m[uint256(mstor19m[mem[(32 * [94midx) + [94m_6 + 159 len 1]m]m.field_0)m]m.field_0) = addr(ext_call.return_data[0])
          [94midx = [94midx + 1
          mcontinue 
      mem[64] = ceil32(return_data.size) + (32 * [94m_31) + 352
      mem[ceil32(return_data.size) + (32 * [94m_31) + 128] = ext_call.return_data[0]
      mem[ceil32(return_data.size) + (32 * [94m_31) + 160] = addr(ext_call.return_data[0])
      mem[ceil32(return_data.size) + (32 * [94m_31) + 192] = m_moduleFactory
      mem[ceil32(return_data.size) + (32 * [94m_31) + 224] = 0
      mem[ceil32(return_data.size) + (32 * [94m_31) + 256] = [94m_6 + 96
      mem[ceil32(return_data.size) + (32 * [94m_31) + 288] = ceil32(return_data.size) + 96
      mem[ceil32(return_data.size) + (32 * [94m_31) + 320] = uint256(mstor21m[ext_call.return_data[0]m]m.field_0)
      uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_0) = ext_call.return_data[0]
      addr(mstor20m[addr(ext_call.return_data[0])m]m.field_256) = addr(ext_call.return_data[0])
      addr(mstor20m[addr(ext_call.return_data[0])m]m.field_512) = m_moduleFactory
      Mask(96, 0, mstor20m[addr(ext_call.return_data[0])m]m.field_672) = 0
      uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_768) = mem[[94m_6 + 96]
      if not mem[[94m_6 + 96]:
          [94midx = 0
          mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_768) + 31 / 32 > [94midxm:
              uint8(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) = mem[ceil32(return_data.size) + 96]
          if not mem[ceil32(return_data.size) + 96]:
              [94midx = 0
              mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
              uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1280) = uint256(mstor21m[ext_call.return_data[0]m]m.field_0)
              uint256(mstor21m[ext_call.return_data[0]m]m.field_0)++
              addr(mstor21m[ext_call.return_data[0]m]m[uint256(mstor21m[ext_call.return_data[0]m]m.field_0)m]m.field_0) = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 384] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 416] = m_moduleFactory
              mem[ceil32(return_data.size) + (32 * [94m_31) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 480] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 512] = m_budget
              mem[ceil32(return_data.size) + (32 * [94m_31) + 544] = block.timestamp
              mem[ceil32(return_data.size) + (32 * [94m_31) + 352] = 224
              mem[ceil32(return_data.size) + (32 * [94m_31) + 576] = mem[[94m_6 + 96]
              [94m_368 = mem[[94m_6 + 96]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 608 len floor32(mem[[94m_6 + 96])] = mem[[94m_6 + 128 len floor32(mem[[94m_6 + 96])]
              [94mvar56001 = floor32([94m_368)
              log 0xa902846e: 224, ext_call.return_data[0], addr(_moduleFactory), addr(ext_call.return_data[0]), ext_call.return_data[0], _budget, block.timestamp, mem[ceil32(return_data.size) + (32 * _31) + 576 len (32 * _368) + 32]
          else:
              [94ms = 0
              [94midx = ceil32(return_data.size) + 128
              mwhile ceil32(return_data.size) + (32 * mem[ceil32(return_data.size) + 96]) + 128 > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0) = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(return_data.size) + 96]) + 31) >> 5
              mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
              uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1280) = uint256(mstor21m[ext_call.return_data[0]m]m.field_0)
              uint256(mstor21m[ext_call.return_data[0]m]m.field_0)++
              addr(mstor21m[ext_call.return_data[0]m]m[uint256(mstor21m[ext_call.return_data[0]m]m.field_0)m]m.field_0) = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 384] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 416] = m_moduleFactory
              mem[ceil32(return_data.size) + (32 * [94m_31) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 480] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 512] = m_budget
              mem[ceil32(return_data.size) + (32 * [94m_31) + 544] = block.timestamp
              mem[ceil32(return_data.size) + (32 * [94m_31) + 352] = 224
              mem[ceil32(return_data.size) + (32 * [94m_31) + 576] = mem[[94m_6 + 96]
              [94m_446 = mem[[94m_6 + 96]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 608 len floor32(mem[[94m_6 + 96])] = mem[[94m_6 + 128 len floor32(mem[[94m_6 + 96])]
              [94mvar59001 = floor32([94m_446)
              log 0xa902846e: 224, ext_call.return_data[0], addr(_moduleFactory), addr(ext_call.return_data[0]), ext_call.return_data[0], _budget, block.timestamp, mem[ceil32(return_data.size) + (32 * _31) + 576 len (32 * _446) + 32]
      else:
          [94ms = 0
          [94midx = [94m_6 + 128
          mwhile [94m_6 + (32 * mem[[94m_6 + 96]) + 128 > [94midxm:
              uint256(mstor20m[addr(ext_call.return_data[0])m]m[3m]m.field_0) = mem[[94midx + 31 len 1] * 256^[94ms or !(255 * 256^[94ms) and uint256(mstor20m[addr(ext_call.return_data[0])m]m[3m]m.field_0)
              [94ms = [94ms + -([94ms + 1 / 32) + (-1 * [94ms * [94ms + 1 / 32) + 1
              [94midx = [94midx + 32
              mcontinue 
          [94midx = Mask(251, 0, (32 * mem[[94m_6 + 96]) + 31) >> 5
          [94ms = sha3(sha3(addr(ext_call.return_data[0]), 20) + 3)
          mwhile [94midxm:
              uint256(mstor[[94msm]) = !(255 * 256^[94midx) and uint256(mstor[[94msm])
              [94midx = [94midx + -([94midx + 1 / 32) + (-1 * [94midx * [94midx + 1 / 32) + 1
              [94ms = ([94midx + 1 / 32) + [94ms
              mcontinue 
          [94midx = (floor32(None + 3) >> 4) + (None * None + 3 / 32) - (Mask(251, 0, (32 * mem[[94m_6 + 96]) + 31) >> 5 * None + 3 / 32)
          mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_768) + 31 / 32 > [94midxm:
              uint8(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 3m]m.field_0) = 0
              [94midx = [94midx + 1
              mcontinue 
          uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) = mem[ceil32(return_data.size) + 96]
          if not mem[ceil32(return_data.size) + 96]:
              [94midx = 0
              mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
              uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1280) = uint256(mstor21m[ext_call.return_data[0]m]m.field_0)
              uint256(mstor21m[ext_call.return_data[0]m]m.field_0)++
              addr(mstor21m[ext_call.return_data[0]m]m[uint256(mstor21m[ext_call.return_data[0]m]m.field_0)m]m.field_0) = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 384] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 416] = m_moduleFactory
              mem[ceil32(return_data.size) + (32 * [94m_31) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 480] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 512] = m_budget
              mem[ceil32(return_data.size) + (32 * [94m_31) + 544] = block.timestamp
              mem[ceil32(return_data.size) + (32 * [94m_31) + 352] = 224
              mem[ceil32(return_data.size) + (32 * [94m_31) + 576] = mem[[94m_6 + 96]
              [94m_506 = mem[[94m_6 + 96]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 608 len floor32(mem[[94m_6 + 96])] = mem[[94m_6 + 128 len floor32(mem[[94m_6 + 96])]
              log 0xa902846e: 224, ext_call.return_data[0], addr(_moduleFactory), addr(ext_call.return_data[0]), ext_call.return_data[0], _budget, block.timestamp, mem[ceil32(return_data.size) + (32 * _31) + 576 len (32 * _506) + 32]
          else:
              [94ms = 0
              [94midx = ceil32(return_data.size) + 128
              mwhile ceil32(return_data.size) + (32 * mem[ceil32(return_data.size) + 96]) + 128 > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94ms + 4m]m.field_0) = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = Mask(251, 0, (32 * mem[ceil32(return_data.size) + 96]) + 31) >> 5
              mwhile uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1024) > [94midxm:
                  uint256(mstor20m[addr(ext_call.return_data[0])m]m[[94midx + 4m]m.field_0) = 0
                  [94midx = [94midx + 1
                  mcontinue 
              uint256(mstor20m[addr(ext_call.return_data[0])m]m.field_1280) = uint256(mstor21m[ext_call.return_data[0]m]m.field_0)
              uint256(mstor21m[ext_call.return_data[0]m]m.field_0)++
              addr(mstor21m[ext_call.return_data[0]m]m[uint256(mstor21m[ext_call.return_data[0]m]m.field_0)m]m.field_0) = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 384] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 416] = m_moduleFactory
              mem[ceil32(return_data.size) + (32 * [94m_31) + 448] = addr(ext_call.return_data[0])
              mem[ceil32(return_data.size) + (32 * [94m_31) + 480] = ext_call.return_data[0]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 512] = m_budget
              mem[ceil32(return_data.size) + (32 * [94m_31) + 544] = block.timestamp
              mem[ceil32(return_data.size) + (32 * [94m_31) + 352] = 224
              mem[ceil32(return_data.size) + (32 * [94m_31) + 576] = mem[[94m_6 + 96]
              [94m_542 = mem[[94m_6 + 96]
              mem[ceil32(return_data.size) + (32 * [94m_31) + 608 len floor32(mem[[94m_6 + 96])] = mem[[94m_6 + 128 len floor32(mem[[94m_6 + 96])]
              log 0xa902846e: 224, ext_call.return_data[0], addr(_moduleFactory), addr(ext_call.return_data[0]), ext_call.return_data[0], _budget, block.timestamp, mem[ceil32(return_data.size) + (32 * _31) + 576 len (32 * _542) + 32]
  uint8(mstor5m.field_8) = 0


# hash = 0xf77c4791
# getter = ['storage', 160, 24, 18]
# const = None
# payable = False
def controller(): # not payable
  return mcontrollerAddress


# hash = 0xff0b9c90
# getter = None
# const = None
# payable = False
def createCheckpoint(): # not payable
  if mowner != caller:
      if addr(mstor20m[callerm]m.field_256) != caller:
          revert with 0, 'Wrong address'
      if uint8(mstor20m[callerm]m.field_672):
          revert with 0, 'Module archived'
      require 0 < uint256(mstor20m[callerm]m.field_768)
      require 0 < uint256(mstor20m[callerm]m.field_768)
      [94ms = 0
      mwhile mstor(('array', 3, ('map', ('mask_shl', 160, 0, 96, 'caller'), ('name', 'stor20', 20))) + (0.03125 / s))m[uint8([94ms)m] != 4m:
          require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
          mem[32] = 20
          require [94ms + 1 < uint256(mstor20m[callerm]m.field_768)
          mem[0] = sha3(caller, 20) + 3
          [94ms = [94ms + 1
          mcontinue 
  require -1 > mcurrentCheckpointId
  mcurrentCheckpointId++
  mstor24m.length++
  mstorB13Dm[mstor24m.lengthm] = block.timestamp
  log 0x624ea167: block.timestamp, currentCheckpointId
  return mcurrentCheckpointId


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


