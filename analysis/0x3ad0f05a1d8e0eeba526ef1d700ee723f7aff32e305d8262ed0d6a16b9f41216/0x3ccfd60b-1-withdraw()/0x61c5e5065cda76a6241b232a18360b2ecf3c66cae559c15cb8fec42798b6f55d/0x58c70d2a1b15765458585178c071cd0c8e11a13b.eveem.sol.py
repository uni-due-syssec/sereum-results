# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x58C70D2A1b15765458585178c071CD0C8E11A13B 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x350bf7c0': 'unknown350bf7c0(?)', '0x3ccfd60b': 'withdraw()'} 

# storage definitions
def storage:
    # storage address 0
    decimals # mask: a s
    # storage address 1
    name
    # storage address 2
    symbol
    # storage address 3
    balanceOf
    # storage address 4
    totalSupply # mask: a s
    # storage address 5
    allowance
    # storage address 6
    owner # mask: a s
    # storage address 7
    unknown2156e6c6
    # storage address 8
    description
    # storage address 9
    category
    # storage address 10
    version
    # storage address 11
    fundType # mask: a s
    # storage address 12
    tokens
    # storage address 13
    status # mask: a s
    # storage address 13
    unknown5075edbfAddress # mask: a s
    # storage address 13
    paused # mask: a s
    # storage address 14
    pausedTime # mask: a s
    # storage address 15
    unknown44644ef0 # mask: a s
    # storage address 16
    stor16
    # storage address 18
    investors
    # storage address 19
    amounts
    # storage address 20
    stor20
    # storage address 21
    unknown07b08870
    # storage address 22
    stor22
    # storage address 23
    accumulatedFee # mask: a s
    # storage address 24
    unknown1c2a0e5c
    # storage address 25
    unknown81d62bf5
    # storage address 6291654672758609839894286073275205852155809607691735580756437056550348818336
    storDE8F # mask: a s
    # storage address 25315808107304436489073159149816469109778116306248924645674996900934862678329
    stor37F8 # mask: a s
    # storage address 47444862884950761695014885221812414276220458302405847337313290849613399387294
    stor68E4 # mask: a s
    # storage address 51902219266518241557051091243148885716133317790826664023326234995173080825474
    stor72BF # mask: a s
    # storage address 67072331549493647622825787457569556318728415786901242217649037894484240406165
    stor67072331549493647622825787457569556318728415786901242217649037894484240406165
# hash = 0x05f8d55d
# getter = None
# const = None
# payable = True
def addOwnerBalance() payable: 
  require caller == mowner
  require call.value + maccumulatedFee >= maccumulatedFee
  maccumulatedFee += call.value


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 1]]]], ['loc', 1]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x07b08870
# getter = ['storage', 160, 0, ['add', ['sha3', 21], ['cd', 4]]]
# const = None
# payable = False
def unknown07b08870(uint256 m_param1): # not payable
  require m_param1 < munknown07b08870m.length
  return munknown07b08870m[m_param1m]


# hash = 0x089f7f85
# getter = None
# const = None
# payable = False
def hasRisk(address m_sender, address m_receiver, address m_tokenAddress, uint256 m_amount, uint256 m_rate): # not payable
  require ext_code.size(munknown2156e6c6m['RiskProvider'm])
  call munknown2156e6c6m['RiskProvider'm].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
       gas gas_remaining wei
      args 0, 0, addr(m_receiver), addr(m_tokenAddress), m_amount, m_rate
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return bool(ext_call.return_data[0])


# hash = 0x08ecd9a6
# getter = None
# const = ['return', 135049151112518904061187182485615172934214931208426453056259151606208004096]
# payable = False
const LOCKER = 0x4c6f636b657250726f76696465720000000000000000000000000000000000


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address m_spender, uint256 m_value): # not payable
  require not mpaused
  mallowancem[callerm]m[addr(m_spender)m] = m_value
  log Approval(
        address owner=_value,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x16ba7197
# getter = None
# const = ['return', 154443516349745585550111941220176751601192532474414730758839226871264051200]
# payable = False
const WITHDRAW = 0x576974686472617750726f7669646572000000000000000000000000000000


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def totalSupply(): # not payable
  return mtotalSupply


# hash = 0x1bb7cc99
# getter = None
# const = ['return', 108257207130708801562209681605405335279468377333953338004896192468914205097984]
# payable = False
const WHITELIST = 0xef57686974656c69737450726f76696465720000000000000000000000000000


# hash = 0x1c2a0e5c
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 24]]]
# const = None
# payable = False
def unknown1c2a0e5c(addr m_param1): # not payable
  return munknown1c2a0e5cm[m_param1m]


# hash = 0x1fa98406
# getter = ['storage', 8, 0, 11]
# const = None
# payable = False
def fundType(): # not payable
  require mfundType <= 1
  return mfundType


# hash = 0x200d2ed2
# getter = ['storage', 8, 0, 13]
# const = None
# payable = False
def status(): # not payable
  require mstatus <= 3
  return mstatus


# hash = 0x201d83d8
# getter = None
# const = ['return', 149184142682071031466986821281381690014212207952467003834806840160369508352]
# payable = False
const unknown201d83d8 = 0x546f6b656e42726f6b656e0000000000000000000000000000000000000000


# hash = 0x2156e6c6
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def unknown2156e6c6(uint256 m_param1): # not payable
  return munknown2156e6c6m[m_param1m]


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_value): # not payable
  require not mpaused
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


# hash = 0x2feb34d4
# getter = None
# const = None
# payable = False
def unknown2feb34d4(uint256 m_param1): # not payable
  require caller == mowner
  require ext_code.size(munknown5075edbfAddress)
  call munknown5075edbfAddress.0xf57ce488 with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if munknown2156e6c6m[m_param1m] != addr(ext_call.return_data[0]):
      require ext_code.size(munknown5075edbfAddress)
      call munknown5075edbfAddress.0xf57ce488 with:
           gas gas_remaining wei
          args m_param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[12 len 20]
      munknown2156e6c6m[m_param1m] = addr(ext_call.return_data[0])
      if not mstor16m[m_param1m]:
          require ext_code.size(munknown2156e6c6m[m_param1m])
          call munknown2156e6c6m[m_param1m].MOT() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args munknown2156e6c6m[m_param1m], 0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args munknown2156e6c6m[m_param1m], -1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
  return munknown2156e6c6m[m_param1m]


# hash = 0x313ce567
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def decimals(): # not payable
  return mdecimals


# hash = 0x38a1ff63
# getter = None
# const = None
# payable = False
def unknown38a1ff63(array m_param1, array m_param2): # not payable
  require caller == mowner
  require ext_code.size(munknown2156e6c6m[0x4c6f636b657250726f76696465720000000000000000000000000000000000m])
  call munknown2156e6c6m[0x4c6f636b657250726f76696465720000000000000000000000000000000000m].0x38a1ff63 with:
       gas gas_remaining wei
      args 0, 64, (32 * m_param1.length) + 96, m_param1.length, call.data[m_param1 + 36 len 32 * m_param1.length], m_param2.length, call.data[m_param2 + 36 len 32 * m_param2.length]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x3c98d189
# getter = None
# const = None
# payable = False
def unknown3c98d189(uint256 m_param1, array m_param2, array m_param3, array m_param4): # not payable
  mem[96] = m_param2.length
  mem[128 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param2.length) + 128] = m_param3.length
  mem[(32 * m_param2.length) + 160 len 32 * m_param3.length] = call.data[m_param3 + 36 len 32 * m_param3.length]
  mem[(32 * m_param3.length) + (32 * m_param2.length) + 160] = m_param4.length
  mem[(32 * m_param3.length) + (32 * m_param2.length) + 192 len 32 * m_param4.length] = call.data[m_param4 + 36 len 32 * m_param4.length]
  if caller == mowner:
      [94midx = 0
      mwhile [94midx < m_param2.lengthm:
          require [94midx < m_param2.length
          mem[0] = mem[(32 * [94midx) + 140 len 20]
          mem[32] = 22
          if mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
              require [94midx < m_param3.length
              mem[(32 * m_param2.length) + (32 * [94midx) + 160] = 0
              [94midx = [94midx + 1
              mcontinue 
          require [94midx < m_param3.length
          [94m_331 = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
          require [94midx < mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]
          [94m_338 = mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param2.length) + 192]
          mem[0] = 'RiskProvider'
          mem[32] = 7
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = this.address
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = [94m_331
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = [94m_338
          require ext_code.size(munknown2156e6c6m['RiskProvider'm])
          call munknown2156e6c6m['RiskProvider'm].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
               gas gas_remaining wei
              args addr(this.address), munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, [94m_331, [94m_338
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require not ext_call.return_data[0]
          require [94midx < m_param3.length
          require mem[(32 * m_param2.length) + (32 * [94midx) + 160] >= 0
          [94midx = [94midx + 1
          mcontinue 
      require maccumulatedFee <= eth.balance(this.address)
      require eth.balance(this.address) - maccumulatedFee >= 0
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = 0x15cdc52900000000000000000000000000000000000000000000000000000000
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = this.address
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = m_param1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = 160
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 356] = m_param2.length
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 388 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = (32 * m_param2.length) + 192
      mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 388] = m_param3.length
      mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 420 len floor32(m_param3.length)] = mem[(32 * m_param2.length) + 160 len floor32(m_param3.length)]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = (32 * m_param3.length) + (32 * m_param2.length) + 224
      mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 420] = mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]
      mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 452 len floor32(mem[(32 * m_param3.length) + (32 * m_param2.length) + 160])] = mem[(32 * m_param3.length) + (32 * m_param2.length) + 192 len floor32(mem[(32 * m_param3.length) + (32 * m_param2.length) + 160])]
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x15cdc529 with:
           gas gas_remaining wei
          args Array(len=m_param2.length, data=call.data[m_param2 + 36 len floor32(m_param2.length)], mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + floor32(m_param2.length) + 388 len (32 * m_param3.length) + (32 * m_param2.length) + (32 * mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]) + -floor32(m_param2.length) + 64]), (32 * m_param2.length) + 192, (32 * m_param3.length) + (32 * m_param2.length) + 224, addr(this.address), m_param1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < m_param2.length
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < m_param2.length
                  [94m_1347 = mem[(32 * [94midx) + 128]
                  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = this.address
                  require ext_code.size(addr([94m_1347))
                  call addr([94m_1347).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1347)
                  mem[32] = 19
                  mamountsm[addr([94m_1347)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1347)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1347)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1347)
                          mem[0] = addr([94m_1347)
                          mem[32] = 20
                          mstor20m[addr([94m_1347)m] = 1
              [94midx = [94midx + 1
              mcontinue 
          return 1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = m_param2.length
      if not m_param2.length:
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 7
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228] = 32
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 260] = m_param2.length
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 292 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228 len (32 * m_param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1350 = mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + (32 * mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1350 + 224]
              if mem[(32 * [94midx) + (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1350 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 22
                  if not mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
                      require [94midx < mem[96]
                      mstor22m[mem[(32 * [94midx) + 140 len 20]m] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 19
                      if mamountsm[mem[(32 * [94midx) + 140 len 20]m] > 0:
                          require [94midx < mem[96]
                          munknown07b08870m.length++
                          mem[0] = 21
                          munknown07b08870m[munknown07b08870m.lengthm] = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1625 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1625)
                          require ext_code.size(munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1625)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_1647 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          require mem[[94m_1647] <= 4294967296
                          require mem[[94m_1647] + 32 <= return_data.size
                          require mem[[94m_1647 + mem[[94m_1647]] <= 4294967296 and mem[[94m_1647] + (32 * mem[[94m_1647 + mem[[94m_1647]]) + 32 <= return_data.size
              [94midx = [94midx + 1
              mcontinue 
          [94m_1663 = mem[96]
          [94midx = 0
          mwhile [94midx < [94m_1663m:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1679 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1679))
                  call addr([94m_1679).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1679)
                  mem[32] = 19
                  mamountsm[addr([94m_1679)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1679)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1679)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1679)
                          mem[0] = addr([94m_1679)
                          mem[32] = 20
                          mstor20m[addr([94m_1679)m] = 1
              [94midx = [94midx + 1
              mcontinue 
      else:
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 224 len 32 * m_param2.length] = code.data[24275 len 32 * m_param2.length]
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 7
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228] = 32
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 260] = m_param2.length
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 292 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228 len (32 * m_param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1351 = mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + (32 * mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1351 + 224]
              if mem[(32 * [94midx) + (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1351 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 22
                  if not mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
                      require [94midx < mem[96]
                      mstor22m[mem[(32 * [94midx) + 140 len 20]m] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 19
                      if mamountsm[mem[(32 * [94midx) + 140 len 20]m] > 0:
                          require [94midx < mem[96]
                          munknown07b08870m.length++
                          mem[0] = 21
                          munknown07b08870m[munknown07b08870m.lengthm] = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1630 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1630)
                          require ext_code.size(munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1630)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_1648 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          require mem[[94m_1648] <= 4294967296
                          require mem[[94m_1648] + 32 <= return_data.size
                          require mem[[94m_1648 + mem[[94m_1648]] <= 4294967296 and mem[[94m_1648] + (32 * mem[[94m_1648 + mem[[94m_1648]]) + 32 <= return_data.size
              [94midx = [94midx + 1
              mcontinue 
          [94m_1664 = mem[96]
          [94midx = 0
          mwhile [94midx < [94m_1664m:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1682 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1682))
                  call addr([94m_1682).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1682)
                  mem[32] = 19
                  mamountsm[addr([94m_1682)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1682)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1682)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1682)
                          mem[0] = addr([94m_1682)
                          mem[32] = 20
                          mstor20m[addr([94m_1682)m] = 1
              [94midx = [94midx + 1
              mcontinue 
  else:
      require ext_code.size(munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m])
      call munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m].0x919253e8 with:
           gas gas_remaining wei
          args addr(this.address), 2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = 2
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = caller
      require ext_code.size(munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m])
      call munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m].0x5faa299a with:
           gas gas_remaining wei
          args 2, caller
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      [94midx = 0
      mwhile [94midx < m_param2.lengthm:
          require [94midx < m_param2.length
          mem[0] = mem[(32 * [94midx) + 140 len 20]
          mem[32] = 22
          if mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
              require [94midx < m_param3.length
              mem[(32 * m_param2.length) + (32 * [94midx) + 160] = 0
              [94midx = [94midx + 1
              mcontinue 
          require [94midx < m_param3.length
          [94m_335 = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
          require [94midx < mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]
          [94m_340 = mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param2.length) + 192]
          mem[0] = 'RiskProvider'
          mem[32] = 7
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = this.address
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = [94m_335
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = [94m_340
          require ext_code.size(munknown2156e6c6m['RiskProvider'm])
          call munknown2156e6c6m['RiskProvider'm].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
               gas gas_remaining wei
              args addr(this.address), munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, [94m_335, [94m_340
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require not ext_call.return_data[0]
          require [94midx < m_param3.length
          require mem[(32 * m_param2.length) + (32 * [94midx) + 160] >= 0
          [94midx = [94midx + 1
          mcontinue 
      require maccumulatedFee <= eth.balance(this.address)
      require eth.balance(this.address) - maccumulatedFee >= 0
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = 0x15cdc52900000000000000000000000000000000000000000000000000000000
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = this.address
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = m_param1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = 160
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 356] = m_param2.length
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 388 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = (32 * m_param2.length) + 192
      mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 388] = m_param3.length
      mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 420 len floor32(m_param3.length)] = mem[(32 * m_param2.length) + 160 len floor32(m_param3.length)]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = (32 * m_param3.length) + (32 * m_param2.length) + 224
      mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 420] = mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]
      mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 452 len floor32(mem[(32 * m_param3.length) + (32 * m_param2.length) + 160])] = mem[(32 * m_param3.length) + (32 * m_param2.length) + 192 len floor32(mem[(32 * m_param3.length) + (32 * m_param2.length) + 160])]
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x15cdc529 with:
           gas gas_remaining wei
          args Array(len=m_param2.length, data=call.data[m_param2 + 36 len floor32(m_param2.length)], mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + floor32(m_param2.length) + 388 len (32 * m_param3.length) + (32 * m_param2.length) + (32 * mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]) + -floor32(m_param2.length) + 64]), (32 * m_param2.length) + 192, (32 * m_param3.length) + (32 * m_param2.length) + 224, addr(this.address), m_param1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < m_param2.length
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < m_param2.length
                  [94m_1352 = mem[(32 * [94midx) + 128]
                  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = this.address
                  require ext_code.size(addr([94m_1352))
                  call addr([94m_1352).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1352)
                  mem[32] = 19
                  mamountsm[addr([94m_1352)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1352)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1352)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1352)
                          mem[0] = addr([94m_1352)
                          mem[32] = 20
                          mstor20m[addr([94m_1352)m] = 1
              [94midx = [94midx + 1
              mcontinue 
          return 1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = m_param2.length
      if not m_param2.length:
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 7
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228] = 32
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 260] = m_param2.length
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 292 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228 len (32 * m_param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1355 = mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + (32 * mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1355 + 224]
              if mem[(32 * [94midx) + (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1355 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 22
                  if not mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
                      require [94midx < mem[96]
                      mstor22m[mem[(32 * [94midx) + 140 len 20]m] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 19
                      if mamountsm[mem[(32 * [94midx) + 140 len 20]m] > 0:
                          require [94midx < mem[96]
                          munknown07b08870m.length++
                          mem[0] = 21
                          munknown07b08870m[munknown07b08870m.lengthm] = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1635 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1635)
                          require ext_code.size(munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1635)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_1649 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          require mem[[94m_1649] <= 4294967296
                          require mem[[94m_1649] + 32 <= return_data.size
                          require mem[[94m_1649 + mem[[94m_1649]] <= 4294967296 and mem[[94m_1649] + (32 * mem[[94m_1649 + mem[[94m_1649]]) + 32 <= return_data.size
              [94midx = [94midx + 1
              mcontinue 
          [94m_1665 = mem[96]
          [94midx = 0
          mwhile [94midx < [94m_1665m:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1685 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1685))
                  call addr([94m_1685).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1685)
                  mem[32] = 19
                  mamountsm[addr([94m_1685)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1685)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1685)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1685)
                          mem[0] = addr([94m_1685)
                          mem[32] = 20
                          mstor20m[addr([94m_1685)m] = 1
              [94midx = [94midx + 1
              mcontinue 
      else:
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 224 len 32 * m_param2.length] = code.data[24275 len 32 * m_param2.length]
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 7
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228] = 32
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 260] = m_param2.length
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 292 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228 len (32 * m_param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1356 = mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + (32 * mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1356 + 224]
              if mem[(32 * [94midx) + (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1356 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 22
                  if not mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
                      require [94midx < mem[96]
                      mstor22m[mem[(32 * [94midx) + 140 len 20]m] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 19
                      if mamountsm[mem[(32 * [94midx) + 140 len 20]m] > 0:
                          require [94midx < mem[96]
                          munknown07b08870m.length++
                          mem[0] = 21
                          munknown07b08870m[munknown07b08870m.lengthm] = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1640 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1640)
                          require ext_code.size(munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1640)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_1650 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          require mem[[94m_1650] <= 4294967296
                          require mem[[94m_1650] + 32 <= return_data.size
                          require mem[[94m_1650 + mem[[94m_1650]] <= 4294967296 and mem[[94m_1650] + (32 * mem[[94m_1650 + mem[[94m_1650]]) + 32 <= return_data.size
              [94midx = [94midx + 1
              mcontinue 
          [94m_1666 = mem[96]
          [94midx = 0
          mwhile [94midx < [94m_1666m:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1688 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1688))
                  call addr([94m_1688).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1688)
                  mem[32] = 19
                  mamountsm[addr([94m_1688)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1688)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1688)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1688)
                          mem[0] = addr([94m_1688)
                          mem[32] = 20
                          mstor20m[addr([94m_1688)m] = 1
              [94midx = [94midx + 1
              mcontinue 
  return 0


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == mowner
  require mpaused
  mpaused = 0
  log Unpause()


# hash = 0x43d726d6
# getter = None
# const = None
# payable = False
def close(): # not payable
  if mowner != caller:
      require 1 == bool(mpaused)
      require mpausedTime + munknown44644ef0 <= block.timestamp
  require mstatus <= 3
  require mstatus
  mstatus = 3
  return 1


# hash = 0x44644ef0
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknown44644ef0(): # not payable
  return munknown44644ef0


# hash = 0x4f64b2be
# getter = ['storage', 160, 0, ['add', ['sha3', 12], ['cd', 4]]]
# const = None
# payable = False
def tokens(uint256 m_param1): # not payable
  require m_param1 < mtokensm.length
  return mtokensm[m_param1m]m.field_0


# hash = 0x5075edbf
# getter = ['storage', 160, 16, 13]
# const = None
# payable = False
def unknown5075edbf(): # not payable
  return munknown5075edbfAddress


# hash = 0x53d0f255
# getter = None
# const = ['return', 147451643735517635592988715279241764045606126128521621587765788107530567680]
# payable = False
const unknown53d0f255 = 0x5374657050726f766964657200000000000000000000000000000000000000


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 10]]]], ['loc', 10]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x55a3b2c1
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 19]]]
# const = None
# payable = False
def amounts(address m_param1): # not payable
  return mamountsm[m_param1m]


# hash = 0x5acf6903
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 20]]]]
# const = None
# payable = False
def activeTokens(address m_param1): # not payable
  return bool(mstor20m[m_param1m])


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 8, 13]]
# const = None
# payable = False
def paused(): # not payable
  return bool(mpaused)


# hash = 0x5f677404
# getter = None
# const = ['return', 1000000000000000000]
# payable = False
const INITIAL_VALUE = 10^18


# hash = 0x659eeabc
# getter = None
# const = None
# payable = False
def tokensWithAmount(): # not payable
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = mtokensm[[94midxm]m.field_0
      mem[32] = 22
      if mstor22m[mstor12m[[94midxm]m.field_0m]:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      require [94midx < mtokensm.length
      mem[0] = mtokensm[[94midxm]m.field_0
      mem[32] = 19
      if mamountsm[mstor12m[[94midxm]m.field_0m] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  if [94ms:
      mem[128 len 32 * [94ms] = code.data[24275 len 32 * [94ms]
  [94midx = 0
  [94mt = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = mtokensm[[94midxm]m.field_0
      mem[32] = 22
      if mstor22m[mstor12m[[94midxm]m.field_0m]:
          [94midx = [94midx + 1
          [94mt = [94mt
          mcontinue 
      require [94midx < mtokensm.length
      mem[0] = mtokensm[[94midxm]m.field_0
      mem[32] = 19
      if mamountsm[mstor12m[[94midxm]m.field_0m] <= 0:
          [94midx = [94midx + 1
          [94mt = [94mt
          mcontinue 
      require [94midx < mtokensm.length
      mem[0] = 12
      require [94mt < [94ms
      mem[(32 * [94mt) + 128] = mtokensm[[94midxm]m.field_0
      [94midx = [94midx + 1
      [94mt = [94mt + 1
      mcontinue 
  mem[(32 * [94ms) + 192 len floor32([94ms)] = mem[128 len floor32([94ms)]
  return Array(len=[94ms, data=mem[128 len floor32([94ms)], mem[(32 * [94ms) + floor32([94ms) + 192 len (32 * [94ms) - floor32([94ms)])


# hash = 0x66188463
# getter = None
# const = None
# payable = False
def decreaseApproval(address m_spender, uint256 m_subtractedValue): # not payable
  require not mpaused
  if m_subtractedValue <= mallowancem[callerm]m[addr(m_spender)m]:
      mallowancem[callerm]m[addr(m_spender)m] -= m_subtractedValue
  else:
      mallowancem[callerm]m[addr(m_spender)m] = 0
  log Approval(
        address owner=allowance[caller][addr(_spender)],
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x679818a1
# getter = None
# const = None
# payable = False
def unknown679818a1(uint256 m_param1, array m_param2, array m_param3, array m_param4): # not payable
  mem[96] = m_param2.length
  mem[128 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param2.length) + 128] = m_param3.length
  mem[(32 * m_param2.length) + 160 len 32 * m_param3.length] = call.data[m_param3 + 36 len 32 * m_param3.length]
  mem[(32 * m_param3.length) + (32 * m_param2.length) + 160] = m_param4.length
  mem[(32 * m_param3.length) + (32 * m_param2.length) + 192 len 32 * m_param4.length] = call.data[m_param4 + 36 len 32 * m_param4.length]
  if caller == mowner:
      [94midx = 0
      mwhile [94midx < m_param2.lengthm:
          require [94midx < m_param2.length
          mem[0] = mem[(32 * [94midx) + 140 len 20]
          mem[32] = 22
          if mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
              require [94midx < m_param3.length
              mem[(32 * m_param2.length) + (32 * [94midx) + 160] = 0
          else:
              require [94midx < m_param2.length
              [94m_351 = mem[(32 * [94midx) + 128]
              require [94midx < m_param3.length
              [94m_358 = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
              require [94midx < mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]
              [94m_365 = mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param2.length) + 192]
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = this.address
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = addr([94m_351)
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = [94m_358
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = [94m_365
              require ext_code.size(munknown2156e6c6m['RiskProvider'm])
              call munknown2156e6c6m['RiskProvider'm].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                   gas gas_remaining wei
                  args addr(this.address), munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], addr([94m_351), [94m_358, [94m_365
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require not ext_call.return_data[0]
              require [94midx < m_param2.length
              [94m_406 = mem[(32 * [94midx) + 128]
              require [94midx < m_param3.length
              [94m_419 = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
              mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[32] = 7
              require ext_code.size(mem[(32 * [94midx) + 140 len 20])
              call mem[(32 * [94midx) + 140 len 20].approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = [94m_419
              require ext_code.size(addr([94m_406))
              call addr([94m_406).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], [94m_419
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          [94midx = [94midx + 1
          mcontinue 
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = this.address
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = m_param1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = 160
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 356] = m_param2.length
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 388 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = (32 * m_param2.length) + 192
      mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 388] = m_param3.length
      mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 420 len floor32(m_param3.length)] = mem[(32 * m_param2.length) + 160 len floor32(m_param3.length)]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = (32 * m_param3.length) + (32 * m_param2.length) + 224
      mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 420] = mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]
      mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 452 len floor32(mem[(32 * m_param3.length) + (32 * m_param2.length) + 160])] = mem[(32 * m_param3.length) + (32 * m_param2.length) + 192 len floor32(mem[(32 * m_param3.length) + (32 * m_param2.length) + 160])]
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x78265e2f with:
           gas gas_remaining wei
          args Array(len=m_param2.length, data=call.data[m_param2 + 36 len floor32(m_param2.length)], mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + floor32(m_param2.length) + 388 len (32 * m_param3.length) + (32 * m_param2.length) + (32 * mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]) + -floor32(m_param2.length) + 64]), (32 * m_param2.length) + 192, (32 * m_param3.length) + (32 * m_param2.length) + 224, addr(this.address), m_param1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < m_param2.length
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < m_param2.length
                  [94m_1373 = mem[(32 * [94midx) + 128]
                  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = this.address
                  require ext_code.size(addr([94m_1373))
                  call addr([94m_1373).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1373)
                  mem[32] = 19
                  mamountsm[addr([94m_1373)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1373)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1373)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1373)
                          mem[0] = addr([94m_1373)
                          mem[32] = 20
                          mstor20m[addr([94m_1373)m] = 1
              [94midx = [94midx + 1
              mcontinue 
          return 1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = m_param2.length
      if not m_param2.length:
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 7
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228] = 32
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 260] = m_param2.length
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 292 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228 len (32 * m_param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1376 = mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + (32 * mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1376 + 224]
              if mem[(32 * [94midx) + (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1376 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 22
                  if not mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
                      require [94midx < mem[96]
                      mstor22m[mem[(32 * [94midx) + 140 len 20]m] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 19
                      if mamountsm[mem[(32 * [94midx) + 140 len 20]m] > 0:
                          require [94midx < mem[96]
                          munknown07b08870m.length++
                          mem[0] = 21
                          munknown07b08870m[munknown07b08870m.lengthm] = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1651 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1651)
                          require ext_code.size(munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1651)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_1673 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          require mem[[94m_1673] <= 4294967296
                          require mem[[94m_1673] + 32 <= return_data.size
                          require mem[[94m_1673 + mem[[94m_1673]] <= 4294967296 and mem[[94m_1673] + (32 * mem[[94m_1673 + mem[[94m_1673]]) + 32 <= return_data.size
              [94midx = [94midx + 1
              mcontinue 
          [94m_1689 = mem[96]
          [94midx = 0
          mwhile [94midx < [94m_1689m:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1705 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1705))
                  call addr([94m_1705).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1705)
                  mem[32] = 19
                  mamountsm[addr([94m_1705)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1705)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1705)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1705)
                          mem[0] = addr([94m_1705)
                          mem[32] = 20
                          mstor20m[addr([94m_1705)m] = 1
              [94midx = [94midx + 1
              mcontinue 
      else:
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 224 len 32 * m_param2.length] = code.data[24275 len 32 * m_param2.length]
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 7
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228] = 32
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 260] = m_param2.length
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 292 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228 len (32 * m_param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1377 = mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + (32 * mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1377 + 224]
              if mem[(32 * [94midx) + (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1377 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 22
                  if not mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
                      require [94midx < mem[96]
                      mstor22m[mem[(32 * [94midx) + 140 len 20]m] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 19
                      if mamountsm[mem[(32 * [94midx) + 140 len 20]m] > 0:
                          require [94midx < mem[96]
                          munknown07b08870m.length++
                          mem[0] = 21
                          munknown07b08870m[munknown07b08870m.lengthm] = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1656 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1656)
                          require ext_code.size(munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1656)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_1674 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          require mem[[94m_1674] <= 4294967296
                          require mem[[94m_1674] + 32 <= return_data.size
                          require mem[[94m_1674 + mem[[94m_1674]] <= 4294967296 and mem[[94m_1674] + (32 * mem[[94m_1674 + mem[[94m_1674]]) + 32 <= return_data.size
              [94midx = [94midx + 1
              mcontinue 
          [94m_1690 = mem[96]
          [94midx = 0
          mwhile [94midx < [94m_1690m:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1708 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1708))
                  call addr([94m_1708).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1708)
                  mem[32] = 19
                  mamountsm[addr([94m_1708)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1708)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1708)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1708)
                          mem[0] = addr([94m_1708)
                          mem[32] = 20
                          mstor20m[addr([94m_1708)m] = 1
              [94midx = [94midx + 1
              mcontinue 
  else:
      require ext_code.size(munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m])
      call munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m].0x919253e8 with:
           gas gas_remaining wei
          args addr(this.address), 2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = 2
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = caller
      require ext_code.size(munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m])
      call munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m].0x5faa299a with:
           gas gas_remaining wei
          args 2, caller
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      [94midx = 0
      mwhile [94midx < m_param2.lengthm:
          require [94midx < m_param2.length
          mem[0] = mem[(32 * [94midx) + 140 len 20]
          mem[32] = 22
          if mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
              require [94midx < m_param3.length
              mem[(32 * m_param2.length) + (32 * [94midx) + 160] = 0
          else:
              require [94midx < m_param2.length
              [94m_353 = mem[(32 * [94midx) + 128]
              require [94midx < m_param3.length
              [94m_363 = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
              require [94midx < mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]
              [94m_366 = mem[(32 * [94midx) + (32 * m_param3.length) + (32 * m_param2.length) + 192]
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = this.address
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = addr([94m_353)
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = [94m_363
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = [94m_366
              require ext_code.size(munknown2156e6c6m['RiskProvider'm])
              call munknown2156e6c6m['RiskProvider'm].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                   gas gas_remaining wei
                  args addr(this.address), munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], addr([94m_353), [94m_363, [94m_366
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require not ext_call.return_data[0]
              require [94midx < m_param2.length
              [94m_411 = mem[(32 * [94midx) + 128]
              require [94midx < m_param3.length
              [94m_426 = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
              mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[32] = 7
              require ext_code.size(mem[(32 * [94midx) + 140 len 20])
              call mem[(32 * [94midx) + 140 len 20].approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = [94m_426
              require ext_code.size(addr([94m_411))
              call addr([94m_411).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], [94m_426
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          [94midx = [94midx + 1
          mcontinue 
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = this.address
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = m_param1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = 160
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 356] = m_param2.length
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 388 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = (32 * m_param2.length) + 192
      mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 388] = m_param3.length
      mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 420 len floor32(m_param3.length)] = mem[(32 * m_param2.length) + 160 len floor32(m_param3.length)]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = (32 * m_param3.length) + (32 * m_param2.length) + 224
      mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 420] = mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]
      mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 452 len floor32(mem[(32 * m_param3.length) + (32 * m_param2.length) + 160])] = mem[(32 * m_param3.length) + (32 * m_param2.length) + 192 len floor32(mem[(32 * m_param3.length) + (32 * m_param2.length) + 160])]
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x78265e2f with:
           gas gas_remaining wei
          args Array(len=m_param2.length, data=call.data[m_param2 + 36 len floor32(m_param2.length)], mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + floor32(m_param2.length) + 388 len (32 * m_param3.length) + (32 * m_param2.length) + (32 * mem[(32 * m_param3.length) + (32 * m_param2.length) + 160]) + -floor32(m_param2.length) + 64]), (32 * m_param2.length) + 192, (32 * m_param3.length) + (32 * m_param2.length) + 224, addr(this.address), m_param1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < m_param2.length
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < m_param2.length
                  [94m_1378 = mem[(32 * [94midx) + 128]
                  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = this.address
                  require ext_code.size(addr([94m_1378))
                  call addr([94m_1378).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1378)
                  mem[32] = 19
                  mamountsm[addr([94m_1378)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1378)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1378)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1378)
                          mem[0] = addr([94m_1378)
                          mem[32] = 20
                          mstor20m[addr([94m_1378)m] = 1
              [94midx = [94midx + 1
              mcontinue 
          return 1
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = m_param2.length
      if not m_param2.length:
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 7
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228] = 32
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 260] = m_param2.length
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 292 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228 len (32 * m_param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1381 = mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + (32 * mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1381 + 224]
              if mem[(32 * [94midx) + (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1381 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 22
                  if not mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
                      require [94midx < mem[96]
                      mstor22m[mem[(32 * [94midx) + 140 len 20]m] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 19
                      if mamountsm[mem[(32 * [94midx) + 140 len 20]m] > 0:
                          require [94midx < mem[96]
                          munknown07b08870m.length++
                          mem[0] = 21
                          munknown07b08870m[munknown07b08870m.lengthm] = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1661 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1661)
                          require ext_code.size(munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1661)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_1675 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          require mem[[94m_1675] <= 4294967296
                          require mem[[94m_1675] + 32 <= return_data.size
                          require mem[[94m_1675 + mem[[94m_1675]] <= 4294967296 and mem[[94m_1675] + (32 * mem[[94m_1675 + mem[[94m_1675]]) + 32 <= return_data.size
              [94midx = [94midx + 1
              mcontinue 
          [94m_1691 = mem[96]
          [94midx = 0
          mwhile [94midx < [94m_1691m:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1711 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1711))
                  call addr([94m_1711).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1711)
                  mem[32] = 19
                  mamountsm[addr([94m_1711)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1711)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1711)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1711)
                          mem[0] = addr([94m_1711)
                          mem[32] = 20
                          mstor20m[addr([94m_1711)m] = 1
              [94midx = [94midx + 1
              mcontinue 
      else:
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 224 len 32 * m_param2.length] = code.data[24275 len 32 * m_param2.length]
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 7
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228] = 32
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 260] = m_param2.length
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 292 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 228 len (32 * m_param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1382 = mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + (32 * mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          mwhile [94midx < m_param2.lengthm:
              require [94midx < mem[(32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1382 + 224]
              if mem[(32 * [94midx) + (32 * m_param4.length) + (32 * m_param3.length) + (64 * m_param2.length) + [94m_1382 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 22
                  if not mstor22m[mem[(32 * [94midx) + 140 len 20]m]:
                      require [94midx < mem[96]
                      mstor22m[mem[(32 * [94midx) + 140 len 20]m] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 19
                      if mamountsm[mem[(32 * [94midx) + 140 len 20]m] > 0:
                          require [94midx < mem[96]
                          munknown07b08870m.length++
                          mem[0] = 21
                          munknown07b08870m[munknown07b08870m.lengthm] = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1666 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1666)
                          require ext_code.size(munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000m].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1666)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_1676 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          require mem[[94m_1676] <= 4294967296
                          require mem[[94m_1676] + 32 <= return_data.size
                          require mem[[94m_1676 + mem[[94m_1676]] <= 4294967296 and mem[[94m_1676] + (32 * mem[[94m_1676 + mem[[94m_1676]]) + 32 <= return_data.size
              [94midx = [94midx + 1
              mcontinue 
          [94m_1692 = mem[96]
          [94midx = 0
          mwhile [94midx < [94m_1692m:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1714 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1714))
                  call addr([94m_1714).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1714)
                  mem[32] = 19
                  mamountsm[addr([94m_1714)m] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1714)
                      mem[32] = 20
                      if not mstor20m[addr([94m_1714)m]:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_1714)
                          mem[0] = addr([94m_1714)
                          mem[32] = 20
                          mstor20m[addr([94m_1714)m] = 1
              [94midx = [94midx + 1
              mcontinue 
  return 0


# hash = 0x6e947298
# getter = None
# const = None
# payable = False
def getETHBalance(): # not payable
  require maccumulatedFee <= eth.balance(this.address)
  return (eth.balance(this.address) - maccumulatedFee)


# hash = 0x6f7bc9be
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 18]]]
# const = None
# payable = False
def investors(address m_param1): # not payable
  return minvestorsm[m_param1m]


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 3]]]
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


# hash = 0x7284e416
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 8]]]], ['loc', 8]]]
# const = None
# payable = False
def description(): # not payable
  return mdescriptionm[0 len mdescriptionm.lengthm]


# hash = 0x745400c9
# getter = None
# const = None
# payable = False
def requestWithdraw(uint256 m_value): # not payable
  require not mpaused
  if 0 == mtotalSupply:
      require ext_code.size(munknown2156e6c6m['RiskProvider'm])
      call munknown2156e6c6m['RiskProvider'm].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
           gas gas_remaining wei
          args 0, uint32(caller), addr(this.address), addr(this.address), m_value, 10^18
  else:
      require maccumulatedFee <= eth.balance(this.address)
      [94midx = 0
      [94ms = 0
      mwhile [94midx < mtokensm.lengthm:
          mem[0] = mtokensm[[94midxm]m.field_0
          mem[32] = 19
          if not mamountsm[mstor12m[[94midxm]m.field_0m]:
              [94midx = [94midx + 1
              [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
              mcontinue 
          require [94midx < mtokensm.length
          mem[0] = 12
          mem[132] = mtokensm[[94midxm]m.field_0
          mem[164] = mamountsm[mstor12m[[94midxm]m.field_0m]
          mem[196] = 0
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, mamountsm[mstor12m[[94midxm]m.field_0m], 0
          mem[96 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
              mcontinue 
          if not mamountsm[mstor12m[[94midxm]m.field_0m]:
              if ext_call.return_data[0]:
                  if 0 / ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                      mcontinue 
          else:
              if 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / mamountsm[mstor12m[[94midxm]m.field_0m] == 10^18:
                  if ext_call.return_data[0]:
                      if 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / ext_call.return_data[0] >= 0:
                          [94midx = [94midx + 1
                          [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                          mcontinue 
          revert
      require eth.balance(this.address) - maccumulatedFee >= 0
      if not eth.balance(this.address) - maccumulatedFee:
          require mtotalSupply
          require ext_code.size(munknown2156e6c6m['RiskProvider'm])
          call munknown2156e6c6m['RiskProvider'm].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
               gas gas_remaining wei
              args caller, addr(this.address), addr(this.address), m_value, 0 / mtotalSupply
      else:
          require (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / eth.balance(this.address) - maccumulatedFee == 10^mdecimals
          require mtotalSupply
          require ext_code.size(munknown2156e6c6m['RiskProvider'm])
          call munknown2156e6c6m['RiskProvider'm].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
               gas gas_remaining wei
              args caller, addr(this.address), addr(this.address), m_value, (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].0xc8c01a55 with:
       gas gas_remaining wei
      args caller, m_value
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = 0x74d16c37
# getter = None
# const = None
# payable = False
def getAssetsValue(): # not payable
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = mtokensm[[94midxm]m.field_0
      mem[32] = 19
      if not mamountsm[mstor12m[[94midxm]m.field_0m]:
          [94midx = [94midx + 1
          [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
          mcontinue 
      require [94midx < mtokensm.length
      mem[0] = 12
      mem[132] = mtokensm[[94midxm]m.field_0
      mem[164] = mamountsm[mstor12m[[94midxm]m.field_0m]
      mem[196] = 0
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, mamountsm[mstor12m[[94midxm]m.field_0m], 0
      mem[96 len 64] = ext_call.return_data[0 len 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
          mcontinue 
      if not mamountsm[mstor12m[[94midxm]m.field_0m]:
          if ext_call.return_data[0]:
              if 0 / ext_call.return_data[0] >= 0:
                  [94midx = [94midx + 1
                  [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                  mcontinue 
      else:
          if 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / mamountsm[mstor12m[[94midxm]m.field_0m] == 10^18:
              if ext_call.return_data[0]:
                  if 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                      mcontinue 
      revert
  return 0


# hash = 0x7a1ac61e
# getter = None
# const = None
# payable = True
def unknown7a1ac61e(addr m_param1, uint256 m_param2, uint256 m_param3) payable: 
  require caller == mowner
  require m_param1
  require mstatus <= 3
  require not mstatus
  require call.value > 0
  munknown44644ef0 = 8760 * 24 * 3600
  require m_param1
  munknown5075edbfAddress = m_param1
  mstor37F8 = 1
  mstor72BF = 1
  mstorDE8F = 1
  mstor68E4 = 1
  mem[416] = 'MarketProvider'
  mem[448] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[480] = 'RiskProvider'
  mem[512] = 0xef57686974656c69737450726f76696465720000000000000000000000000000
  mem[544] = 0x46656550726f76696465720000000000000000000000000000000000000000
  mem[576] = 0x5265696d6275727361626c6500000000000000000000000000000000000000
  mem[608] = 0x576974686472617750726f7669646572000000000000000000000000000000
  mem[640] = 0x4c6f636b657250726f76696465720000000000000000000000000000000000
  mem[672] = 0x5374657050726f766964657200000000000000000000000000000000000000
  mem[704] = 0x546f6b656e42726f6b656e0000000000000000000000000000000000000000
  [94midx = 0
  mwhile [94midx < 10m:
      [94m_46 = mem[(32 * [94midx) + 416]
      require caller == mowner
      mem[740] = mem[(32 * [94midx) + 416]
      require ext_code.size(munknown5075edbfAddress)
      call munknown5075edbfAddress.0xf57ce488 with:
           gas gas_remaining wei
          args [94m_46
      mem[736] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if munknown2156e6c6m[[94m_46m] != addr(ext_call.return_data[0]):
          mem[740] = [94m_46
          require ext_code.size(munknown5075edbfAddress)
          call munknown5075edbfAddress.0xf57ce488 with:
               gas gas_remaining wei
              args [94m_46
          mem[736] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require addr(ext_call.return_data[0])
          munknown2156e6c6m[[94m_46m] = addr(ext_call.return_data[0])
          if not mstor16m[[94m_46m]:
              require ext_code.size(munknown2156e6c6m[[94m_46m])
              call munknown2156e6c6m[[94m_46m].MOT() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknown2156e6c6m[[94m_46m], 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[736] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
              mem[740] = munknown2156e6c6m[[94m_46m]
              mem[772] = -1
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args munknown2156e6c6m[[94m_46m], -1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
      mem[0] = [94m_46
      mem[32] = 7
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(munknown2156e6c6m['MarketProvider'm])
  call munknown2156e6c6m['MarketProvider'm].0xdfd92f8a with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
  call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].setFeePercentage(uint256 newFee) with:
       gas gas_remaining wei
      args m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(munknown2156e6c6m[0x4c6f636b657250726f76696465720000000000000000000000000000000000m])
  call munknown2156e6c6m[0x4c6f636b657250726f76696465720000000000000000000000000000000000m].0x62f0ce85 with:
       gas gas_remaining wei
      args 0x576974686472617750726f7669646572000000000000000000000000000000, m_param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require 0 < 0, 0x576974686472617750726f76696465720000000000000000000000
  require 1 < 0, 0x576974686472617750726f76696465720000000000000000000000
  mem[1028 len 0] = None
  mem[1124 len 0x576974686472617750726f76696465720000000000000000000000] = 10, 5, 2, 0x576974686472617750726f7669646572000000000000000000000000000000, 0x4765744574680000000000000000000000000000000000000000000000000000, 0, 64, 160, 2, mem[1028 len 64], 0, 0x576974686472617750726f76696465720000000000000000000000, mem[1124 len 0x576974686472617750726f7669646571fffffffffffffffffffe9c]
  require ext_code.size(munknown2156e6c6m[0x5374657050726f766964657200000000000000000000000000000000000000m])
  call munknown2156e6c6m[0x5374657050726f766964657200000000000000000000000000000000000000m].0xfdb880b9 with:
       gas gas_remaining wei
      args 64, 160, 2, mem[1028 len 64], 0, 0x576974686472617750726f76696465720000000000000000000000, mem[1124 len 0xaed2e8d0c8e4c2eea0e4deecd2c8cae400000000000000000000000]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mstatus = 1
  require call.value + maccumulatedFee >= maccumulatedFee
  maccumulatedFee += call.value


# hash = 0x81d62bf5
# getter = ['storage', 160, 0, ['add', ['sha3', 25], ['cd', 4]]]
# const = None
# payable = False
def unknown81d62bf5(uint256 m_param1): # not payable
  require m_param1 < munknown81d62bf5m.length
  return munknown81d62bf5m[m_param1m]m.field_0


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  require caller == mowner
  require not mpaused
  mpaused = 1
  mpausedTime = block.timestamp


# hash = 0x85450abf
# getter = None
# const = None
# payable = False
def unknown85450abf(): # not payable
  if not munknown81d62bf5m.length:
      mem[(32 * munknown81d62bf5m.length) + 128] = 32
      mem[(32 * munknown81d62bf5m.length) + 160] = munknown81d62bf5m.length
      mem[(32 * munknown81d62bf5m.length) + 192 len floor32(munknown81d62bf5m.length)] = mem[128 len floor32(munknown81d62bf5m.length)]
      return memory
        from (32 * munknown81d62bf5m.length) + 128
         [93mlen (96 * munknown81d62bf5m.length) + 64
  mem[128] = addr(munknown81d62bf5m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknown81d62bf5m.length) + 96 > [94midxm:
      mem[[94midx + 32] = munknown81d62bf5m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * munknown81d62bf5m.length) + 192 len floor32(munknown81d62bf5m.length)] = mem[128 len floor32(munknown81d62bf5m.length)]
  return Array(len=munknown81d62bf5m.length, data=mem[128 len floor32(munknown81d62bf5m.length)], mem[(32 * munknown81d62bf5m.length) + floor32(munknown81d62bf5m.length) + 192 len (32 * munknown81d62bf5m.length) - floor32(munknown81d62bf5m.length)]), 


# hash = 0x862b2839
# getter = None
# const = ['return', 32293466278026087082630401698836907263138185254920806816698666571931416788992]
# payable = False
const unknown862b2839 = 0x4765744574680000000000000000000000000000000000000000000000000000


# hash = 0x87b8aa6a
# getter = None
# const = None
# payable = False
def unknown87b8aa6a(uint8 m_param1, bool m_param2): # not payable
  require caller == mowner
  require m_param1 <= 2
  require ext_code.size(munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m])
  call munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m].0x8719e8ac with:
       gas gas_remaining wei
      args m_param1 << 248, m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0x8a97d732
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 22]]]]
# const = None
# payable = False
def unknown8a97d732(addr m_param1): # not payable
  return bool(mstor22m[m_param1m])


# hash = 0x8d859f3e
# getter = None
# const = ['return', "'PriceProvider'"]
# payable = False
const PRICE = 'PriceProvider'


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x918f8674
# getter = None
# const = ['return', 10000]
# payable = False
const DENOMINATOR = 10000


# hash = 0x9375206a
# getter = None
# const = None
# payable = False
def setAllowed(address[] m_accounts, uint8 m_key, bool m_allowed): # not payable
  require caller == mowner
  require m_key <= 2
  mem[(32 * m_accounts.length) + 260 len floor32(m_accounts.length)] = call.data[m_accounts + 36 len floor32(m_accounts.length)]
  require ext_code.size(munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m])
  call munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m].0xb65c7c81 with:
       gas gas_remaining wei
      args Array(len=m_accounts.length, data=call.data[m_accounts + 36 len floor32(m_accounts.length)], mem[(32 * m_accounts.length) + floor32(m_accounts.length) + 260 len (32 * m_accounts.length) - floor32(m_accounts.length)]), m_key << 248, m_allowed
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 1


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 2]]]], ['loc', 2]]]
# const = None
# payable = False
def symbol(): # not payable
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0x98d5fdca
# getter = None
# const = None
# payable = False
def getPrice(): # not payable
  if 0 == mtotalSupply:
      return 10^18
  require maccumulatedFee <= eth.balance(this.address)
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = mtokensm[[94midxm]m.field_0
      mem[32] = 19
      if not mamountsm[mstor12m[[94midxm]m.field_0m]:
          [94midx = [94midx + 1
          [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
          mcontinue 
      require [94midx < mtokensm.length
      mem[0] = 12
      mem[132] = mtokensm[[94midxm]m.field_0
      mem[164] = mamountsm[mstor12m[[94midxm]m.field_0m]
      mem[196] = 0
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, mamountsm[mstor12m[[94midxm]m.field_0m], 0
      mem[96 len 64] = ext_call.return_data[0 len 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
          mcontinue 
      if not mamountsm[mstor12m[[94midxm]m.field_0m]:
          if ext_call.return_data[0]:
              if 0 / ext_call.return_data[0] >= 0:
                  [94midx = [94midx + 1
                  [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                  mcontinue 
      else:
          if 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / mamountsm[mstor12m[[94midxm]m.field_0m] == 10^18:
              if ext_call.return_data[0]:
                  if 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                      mcontinue 
      revert
  if eth.balance(this.address) - maccumulatedFee >= 0:
      if not eth.balance(this.address) - maccumulatedFee:
          if mtotalSupply:
              return (0 / mtotalSupply)
      else:
          if (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / eth.balance(this.address) - maccumulatedFee == 10^mdecimals:
              if mtotalSupply:
                  return ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply)
  revert


# hash = 0x9c2062ad
# getter = None
# const = ['return', "'RiskProvider'"]
# payable = False
const RISK = 'RiskProvider'


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_value): # not payable
  require not mpaused
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


# hash = 0xaa6ca808
# getter = None
# const = None
# payable = False
def getTokens(): # not payable
  [94midx = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = mtokensm[[94midxm]m.field_0
      mem[32] = 19
      require [94midx < mtokensm.length
      mem[(32 * [94midx) + 128] = mamountsm[mstor12m[[94midxm]m.field_0m]
      [94midx = [94midx + 1
      mcontinue 
  if mtokensm.length:
      mem[(32 * mtokensm.length) + 160] = addr(mtokensm.field_0)
      [94midx = (32 * mtokensm.length) + 160
      [94ms = 0
      mwhile (64 * mtokensm.length) + 128 > [94midxm:
          mem[[94midx + 32] = mtokensm[[94msm]m.field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
  mem[(64 * mtokensm.length) + 160] = 64
  mem[(64 * mtokensm.length) + 224] = mtokensm.length
  mem[(64 * mtokensm.length) + 256 len floor32(mtokensm.length)] = mem[(32 * mtokensm.length) + 160 len floor32(mtokensm.length)]
  mem[(64 * mtokensm.length) + 192] = (32 * mtokensm.length) + 96
  mem[(98 * mtokensm.length) + 256] = mtokensm.length
  return Array(len=mtokensm.length, data=mem[(32 * mtokensm.length) + 160 len floor32(mtokensm.length)], mem[(64 * mtokensm.length) + floor32(mtokensm.length) + 256 len (64 * mtokensm.length) + -floor32(mtokensm.length) + 32]), 
         (32 * mtokensm.length) + 96


# hash = 0xb2cca39d
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def pausedTime(): # not payable
  return mpausedTime


# hash = 0xb50e44b8
# getter = None
# const = ['return', 122743337058602665564631354263472091436608355031343273141981057876456636416]
# payable = False
const EXCHANGE = 0x45786368616e676550726f7669646572000000000000000000000000000000


# hash = 0xb86ec38f
# getter = None
# const = ['return', 145581378006796796482538153470897892133593206079523589563550605086325473280]
# payable = False
const REIMBURSABLE = 0x5265696d6275727361626c6500000000000000000000000000000000000000


# hash = 0xb8893727
# getter = None
# const = None
# payable = False
def unknownb8893727(uint256 m_param1, uint256 m_param2): # not payable
  require caller == mowner
  require ext_code.size(munknown2156e6c6m[0x5374657050726f766964657200000000000000000000000000000000000000m])
  call munknown2156e6c6m[0x5374657050726f766964657200000000000000000000000000000000000000m].0xd63a81f0 with:
       gas gas_remaining wei
      args m_param1, m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xbe357616
# getter = None
# const = None
# payable = False
def withdrawFee(uint256 m_amount): # not payable
  require caller == mowner
  require not mpaused
  require m_amount <= maccumulatedFee
  maccumulatedFee -= m_amount
  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0, 4008636142, addr(ext_call.return_data[0]), m_amount, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0xeb5d3ab5 with:
     value m_amount wei
       gas gas_remaining wei
      args 0, ext_call.return_data[32], uint32(m_amount), ext_call.return_data[32], mowner, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 1


# hash = 0xc57981b5
# getter = None
# const = ['return', 124379102342185459001336389329018762428788778823516384280262013063067074560]
# payable = False
const FEE = 0x46656550726f76696465720000000000000000000000000000000000000000


# hash = 0xd3c9ad17
# getter = None
# const = ['return', "'RebalanceProvider'"]
# payable = False
const REBALANCE = 'RebalanceProvider'


# hash = 0xd73dd623
# getter = None
# const = None
# payable = False
def increaseApproval(address m_spender, uint256 m_addedValue): # not payable
  require not mpaused
  require m_addedValue + mallowancem[callerm]m[addr(m_spender)m] >= mallowancem[callerm]m[addr(m_spender)m]
  mallowancem[callerm]m[addr(m_spender)m] += m_addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 5]]]]]
# const = None
# payable = False
def allowance(address m_owner, address m_spender): # not payable
  return mallowancem[addr(m_owner)m]m[addr(m_spender)m]


# hash = 0xe8b5e51f
# getter = None
# const = None
# payable = True
def invest() payable: 
  require ext_code.size(munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m])
  call munknown2156e6c6m[0xef57686974656c69737450726f76696465720000000000000000000000000000m].0x5faa299a with:
       gas gas_remaining wei
      args 0, caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(munknown2156e6c6m['RiskProvider'm])
      call munknown2156e6c6m['RiskProvider'm].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
           gas gas_remaining wei
          args 0, uint32(caller), addr(this.address), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, call.value, 1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require not ext_call.return_data[0]
          require not mpaused
          require mstatus <= 3
          require mstatus == 1
          require call.value >= 10^15
          if munknown1c2a0e5cm[callerm]:
              if mtotalSupply <= 0:
                  require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                  call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                       gas gas_remaining wei
                      args caller, call.value
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= call.value
                      if call.value - ext_call.return_data[0]:
                          require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                          require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                          maccumulatedFee += ext_call.return_data[0]
                          require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                          mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / 10^18
                          require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / 10^18) + mtotalSupply >= mtotalSupply
                          mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / 10^18
                          log Transfer(
                                address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / 10^18),
                                address to=0,
                                uint256 value=caller)
                          return 1
                      else:
                          require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                          maccumulatedFee += ext_call.return_data[0]
                          require mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                          require mtotalSupply >= mtotalSupply
                          log Transfer(
                                address from=0,
                                address to=0,
                                uint256 value=caller)
                          return 1
              else:
                  if call.value:
                      require 10^mdecimals * call.value / call.value == 10^mdecimals
                      require mtotalSupply
                      if mtotalSupply != 0:
                          require maccumulatedFee <= eth.balance(this.address)
                          [94midx = 0
                          [94ms = 0
                          mwhile [94midx < mtokensm.lengthm:
                              mem[0] = mtokensm[[94midxm]m.field_0
                              mem[32] = 19
                              if mamountsm[mstor12m[[94midxm]m.field_0m]:
                                  require [94midx < mtokensm.length
                                  mem[0] = 12
                                  mem[132] = mtokensm[[94midxm]m.field_0
                                  mem[164] = mamountsm[mstor12m[[94midxm]m.field_0m]
                                  mem[196] = 0
                                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                       gas gas_remaining wei
                                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, mamountsm[mstor12m[[94midxm]m.field_0m], 0
                                  mem[96 len 64] = ext_call.return_data[0 len 64]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 64
                                      if ext_call.return_data[0]:
                                          if mamountsm[mstor12m[[94midxm]m.field_0m]:
                                              require 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / mamountsm[mstor12m[[94midxm]m.field_0m] == 10^18
                                              require ext_call.return_data[0]
                                              require 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / ext_call.return_data[0] >= 0
                                              [94midx = [94midx + 1
                                              [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                              mcontinue 
                                          else:
                                              require ext_call.return_data[0]
                                              require 0 / ext_call.return_data[0] >= 0
                                              [94midx = [94midx + 1
                                              [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                              mcontinue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                          mcontinue 
                              else:
                                  [94midx = [94midx + 1
                                  [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                  mcontinue 
                          require eth.balance(this.address) - maccumulatedFee >= 0
                          if eth.balance(this.address) - maccumulatedFee:
                              require (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / eth.balance(this.address) - maccumulatedFee == 10^mdecimals
                              require mtotalSupply
                              require 10^mdecimals * call.value / mtotalSupply <= (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply
                              require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                              call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= call.value
                                  if call.value - ext_call.return_data[0]:
                                      require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                      require ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      log Transfer(
                                            address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                                  else:
                                      require ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require (0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += 0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require (0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += 0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      log Transfer(
                                            address from=(0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                          else:
                              require mtotalSupply
                              require 10^mdecimals * call.value / mtotalSupply <= 0 / mtotalSupply
                              require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                              call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= call.value
                                  if call.value - ext_call.return_data[0]:
                                      require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                      require (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      log Transfer(
                                            address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / (0 / totalSupply) - (10^decimals * call.value / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                                  else:
                                      require (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require (0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += 0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require (0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += 0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      log Transfer(
                                            address from=(0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                      else:
                          require 10^mdecimals * call.value / mtotalSupply <= 10^18
                          require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                               gas gas_remaining wei
                              args caller, call.value
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_call.return_data[0] <= call.value
                              if call.value - ext_call.return_data[0]:
                                  require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                  require -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                  maccumulatedFee += ext_call.return_data[0]
                                  require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                  mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                                  mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  log Transfer(
                                        address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(10^decimals * call.value / totalSupply) + 10^18),
                                        address to=0,
                                        uint256 value=caller)
                                  return 1
                              else:
                                  require -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                  maccumulatedFee += ext_call.return_data[0]
                                  require (0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                  mbalanceOfm[callerm] += 0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  require (0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                                  mtotalSupply += 0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  log Transfer(
                                        address from=(0 / -(10^decimals * call.value / totalSupply) + 10^18),
                                        address to=0,
                                        uint256 value=caller)
                                  return 1
                  else:
                      require mtotalSupply
                      if mtotalSupply != 0:
                          require maccumulatedFee <= eth.balance(this.address)
                          [94midx = 0
                          [94ms = 0
                          mwhile [94midx < mtokensm.lengthm:
                              mem[0] = mtokensm[[94midxm]m.field_0
                              mem[32] = 19
                              if mamountsm[mstor12m[[94midxm]m.field_0m]:
                                  require [94midx < mtokensm.length
                                  mem[0] = 12
                                  mem[132] = mtokensm[[94midxm]m.field_0
                                  mem[164] = mamountsm[mstor12m[[94midxm]m.field_0m]
                                  mem[196] = 0
                                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                       gas gas_remaining wei
                                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, mamountsm[mstor12m[[94midxm]m.field_0m], 0
                                  mem[96 len 64] = ext_call.return_data[0 len 64]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 64
                                      if ext_call.return_data[0]:
                                          if mamountsm[mstor12m[[94midxm]m.field_0m]:
                                              require 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / mamountsm[mstor12m[[94midxm]m.field_0m] == 10^18
                                              require ext_call.return_data[0]
                                              require 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / ext_call.return_data[0] >= 0
                                              [94midx = [94midx + 1
                                              [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                              mcontinue 
                                          else:
                                              require ext_call.return_data[0]
                                              require 0 / ext_call.return_data[0] >= 0
                                              [94midx = [94midx + 1
                                              [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                              mcontinue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                          mcontinue 
                              else:
                                  [94midx = [94midx + 1
                                  [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                  mcontinue 
                          require eth.balance(this.address) - maccumulatedFee >= 0
                          if eth.balance(this.address) - maccumulatedFee:
                              require (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / eth.balance(this.address) - maccumulatedFee == 10^mdecimals
                              require mtotalSupply
                              require 0 / mtotalSupply <= (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply
                              require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                              call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= call.value
                                  if call.value - ext_call.return_data[0]:
                                      require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                      require ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      log Transfer(
                                            address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                                  else:
                                      require ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require (0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += 0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      require (0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += 0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      log Transfer(
                                            address from=(0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                          else:
                              require mtotalSupply
                              require 0 / mtotalSupply <= 0 / mtotalSupply
                              require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                              call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= call.value
                                  require call.value - ext_call.return_data[0]
                                  require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                  revert
                      else:
                          require 0 / mtotalSupply <= 10^18
                          require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                               gas gas_remaining wei
                              args caller, call.value
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_call.return_data[0] <= call.value
                              if call.value - ext_call.return_data[0]:
                                  require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                  require -(0 / mtotalSupply) + 10^18
                                  require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                  maccumulatedFee += ext_call.return_data[0]
                                  require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(0 / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                  mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(0 / mtotalSupply) + 10^18
                                  require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(0 / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                                  mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(0 / mtotalSupply) + 10^18
                                  log Transfer(
                                        address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(0 / totalSupply) + 10^18),
                                        address to=0,
                                        uint256 value=caller)
                                  return 1
                              else:
                                  require -(0 / mtotalSupply) + 10^18
                                  require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                  maccumulatedFee += ext_call.return_data[0]
                                  require (0 / -(0 / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                  mbalanceOfm[callerm] += 0 / -(0 / mtotalSupply) + 10^18
                                  require (0 / -(0 / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                                  mtotalSupply += 0 / -(0 / mtotalSupply) + 10^18
                                  log Transfer(
                                        address from=(0 / -(0 / totalSupply) + 10^18),
                                        address to=0,
                                        uint256 value=caller)
                                  return 1
          else:
              munknown81d62bf5m.length++
              mstor9449m[mstor25m.lengthm] = caller
              munknown1c2a0e5cm[callerm] = munknown81d62bf5m.length + 1
              if mtotalSupply <= 0:
                  require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                  call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                       gas gas_remaining wei
                      args caller, call.value
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require return_data.size >= 32
                      require ext_call.return_data[0] <= call.value
                      if call.value - ext_call.return_data[0]:
                          require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                          require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                          maccumulatedFee += ext_call.return_data[0]
                          require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                          mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / 10^18
                          require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / 10^18) + mtotalSupply >= mtotalSupply
                          mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / 10^18
                          log Transfer(
                                address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / 10^18),
                                address to=0,
                                uint256 value=caller)
                          return 1
                      else:
                          require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                          maccumulatedFee += ext_call.return_data[0]
                          require mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                          require mtotalSupply >= mtotalSupply
                          log Transfer(
                                address from=0,
                                address to=0,
                                uint256 value=caller)
                          return 1
              else:
                  if call.value:
                      require 10^mdecimals * call.value / call.value == 10^mdecimals
                      require mtotalSupply
                      if mtotalSupply != 0:
                          require maccumulatedFee <= eth.balance(this.address)
                          [94midx = 0
                          [94ms = 0
                          mwhile [94midx < mtokensm.lengthm:
                              mem[0] = mtokensm[[94midxm]m.field_0
                              mem[32] = 19
                              if mamountsm[mstor12m[[94midxm]m.field_0m]:
                                  require [94midx < mtokensm.length
                                  mem[0] = 12
                                  mem[132] = mtokensm[[94midxm]m.field_0
                                  mem[164] = mamountsm[mstor12m[[94midxm]m.field_0m]
                                  mem[196] = 0
                                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                       gas gas_remaining wei
                                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, mamountsm[mstor12m[[94midxm]m.field_0m], 0
                                  mem[96 len 64] = ext_call.return_data[0 len 64]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 64
                                      if ext_call.return_data[0]:
                                          if mamountsm[mstor12m[[94midxm]m.field_0m]:
                                              require 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / mamountsm[mstor12m[[94midxm]m.field_0m] == 10^18
                                              require ext_call.return_data[0]
                                              require 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / ext_call.return_data[0] >= 0
                                              [94midx = [94midx + 1
                                              [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                              mcontinue 
                                          else:
                                              require ext_call.return_data[0]
                                              require 0 / ext_call.return_data[0] >= 0
                                              [94midx = [94midx + 1
                                              [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                              mcontinue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                          mcontinue 
                              else:
                                  [94midx = [94midx + 1
                                  [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                  mcontinue 
                          require eth.balance(this.address) - maccumulatedFee >= 0
                          if eth.balance(this.address) - maccumulatedFee:
                              require (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / eth.balance(this.address) - maccumulatedFee == 10^mdecimals
                              require mtotalSupply
                              require 10^mdecimals * call.value / mtotalSupply <= (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply
                              require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                              call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= call.value
                                  if call.value - ext_call.return_data[0]:
                                      require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                      require ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      log Transfer(
                                            address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                                  else:
                                      require ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require (0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += 0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require (0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += 0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      log Transfer(
                                            address from=(0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                          else:
                              require mtotalSupply
                              require 10^mdecimals * call.value / mtotalSupply <= 0 / mtotalSupply
                              require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                              call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= call.value
                                  if call.value - ext_call.return_data[0]:
                                      require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                      require (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      log Transfer(
                                            address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / (0 / totalSupply) - (10^decimals * call.value / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                                  else:
                                      require (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require (0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += 0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      require (0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += 0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                                      log Transfer(
                                            address from=(0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                      else:
                          require 10^mdecimals * call.value / mtotalSupply <= 10^18
                          require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                               gas gas_remaining wei
                              args caller, call.value
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_call.return_data[0] <= call.value
                              if call.value - ext_call.return_data[0]:
                                  require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                  require -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                  maccumulatedFee += ext_call.return_data[0]
                                  require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                  mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                                  mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  log Transfer(
                                        address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(10^decimals * call.value / totalSupply) + 10^18),
                                        address to=0,
                                        uint256 value=caller)
                                  return 1
                              else:
                                  require -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                  maccumulatedFee += ext_call.return_data[0]
                                  require (0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                  mbalanceOfm[callerm] += 0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  require (0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                                  mtotalSupply += 0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                                  log Transfer(
                                        address from=(0 / -(10^decimals * call.value / totalSupply) + 10^18),
                                        address to=0,
                                        uint256 value=caller)
                                  return 1
                  else:
                      require mtotalSupply
                      if mtotalSupply != 0:
                          require maccumulatedFee <= eth.balance(this.address)
                          [94midx = 0
                          [94ms = 0
                          mwhile [94midx < mtokensm.lengthm:
                              mem[0] = mtokensm[[94midxm]m.field_0
                              mem[32] = 19
                              if mamountsm[mstor12m[[94midxm]m.field_0m]:
                                  require [94midx < mtokensm.length
                                  mem[0] = 12
                                  mem[132] = mtokensm[[94midxm]m.field_0
                                  mem[164] = mamountsm[mstor12m[[94midxm]m.field_0m]
                                  mem[196] = 0
                                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                       gas gas_remaining wei
                                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, mamountsm[mstor12m[[94midxm]m.field_0m], 0
                                  mem[96 len 64] = ext_call.return_data[0 len 64]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 64
                                      if ext_call.return_data[0]:
                                          if mamountsm[mstor12m[[94midxm]m.field_0m]:
                                              require 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / mamountsm[mstor12m[[94midxm]m.field_0m] == 10^18
                                              require ext_call.return_data[0]
                                              require 10^18 * mamountsm[mstor12m[[94midxm]m.field_0m] / ext_call.return_data[0] >= 0
                                              [94midx = [94midx + 1
                                              [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                              mcontinue 
                                          else:
                                              require ext_call.return_data[0]
                                              require 0 / ext_call.return_data[0] >= 0
                                              [94midx = [94midx + 1
                                              [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                              mcontinue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                          mcontinue 
                              else:
                                  [94midx = [94midx + 1
                                  [94ms = mamountsm[mstor12m[[94midxm]m.field_0m]
                                  mcontinue 
                          require eth.balance(this.address) - maccumulatedFee >= 0
                          if eth.balance(this.address) - maccumulatedFee:
                              require (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / eth.balance(this.address) - maccumulatedFee == 10^mdecimals
                              require mtotalSupply
                              require 0 / mtotalSupply <= (eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply
                              require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                              call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= call.value
                                  if call.value - ext_call.return_data[0]:
                                      require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                      require ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      log Transfer(
                                            address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                                  else:
                                      require ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                      maccumulatedFee += ext_call.return_data[0]
                                      require (0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] += 0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      require (0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)) + mtotalSupply >= mtotalSupply
                                      mtotalSupply += 0 / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (0 / mtotalSupply)
                                      log Transfer(
                                            address from=(0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                          else:
                              require mtotalSupply
                              require 0 / mtotalSupply <= 0 / mtotalSupply
                              require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                              call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= call.value
                                  require call.value - ext_call.return_data[0]
                                  require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                  revert
                      else:
                          require 0 / mtotalSupply <= 10^18
                          require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
                          call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].0x8b28ab1e with:
                               gas gas_remaining wei
                              args caller, call.value
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_call.return_data[0] <= call.value
                              if call.value - ext_call.return_data[0]:
                                  require (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / call.value - ext_call.return_data[0] == 10^mdecimals
                                  require -(0 / mtotalSupply) + 10^18
                                  require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                  maccumulatedFee += ext_call.return_data[0]
                                  require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(0 / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                  mbalanceOfm[callerm] += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(0 / mtotalSupply) + 10^18
                                  require ((call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(0 / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                                  mtotalSupply += (call.value * 10^mdecimals) - (ext_call.return_data[0] * 10^mdecimals) / -(0 / mtotalSupply) + 10^18
                                  log Transfer(
                                        address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(0 / totalSupply) + 10^18),
                                        address to=0,
                                        uint256 value=caller)
                                  return 1
                              else:
                                  require -(0 / mtotalSupply) + 10^18
                                  require ext_call.return_data[0] + maccumulatedFee >= maccumulatedFee
                                  maccumulatedFee += ext_call.return_data[0]
                                  require (0 / -(0 / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                                  mbalanceOfm[callerm] += 0 / -(0 / mtotalSupply) + 10^18
                                  require (0 / -(0 / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                                  mtotalSupply += 0 / -(0 / mtotalSupply) + 10^18
                                  log Transfer(
                                        address from=(0 / -(0 / totalSupply) + 10^18),
                                        address to=0,
                                        uint256 value=caller)
                                  return 1


# hash = 0xef430aa6
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 9]]]], ['loc', 9]]]
# const = None
# payable = False
def category(): # not payable
  return mcategorym[0 len mcategorym.lengthm]


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


# hash = 0xf46f16c2
# getter = None
# const = ['return', "'MarketProvider'"]
# payable = False
const MARKET = 'MarketProvider'


# hash = 0xf8ce3164
# getter = ['storage', 256, 0, 23]
# const = None
# payable = False
def accumulatedFee(): # not payable
  return maccumulatedFee


# hash = 0xfe56e232
# getter = None
# const = None
# payable = False
def setManagementFee(uint256 m_fee): # not payable
  require caller == mowner
  require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
  call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].setFeePercentage(uint256 newFee) with:
       gas gas_remaining wei
      args m_fee
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


