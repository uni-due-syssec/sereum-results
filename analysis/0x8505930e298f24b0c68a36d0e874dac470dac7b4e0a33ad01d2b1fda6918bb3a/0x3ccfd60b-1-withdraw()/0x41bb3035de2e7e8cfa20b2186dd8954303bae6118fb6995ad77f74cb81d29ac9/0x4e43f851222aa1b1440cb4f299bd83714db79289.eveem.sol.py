# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x4e43f851222Aa1b1440CB4f299bd83714Db79289 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x350bf7c0': 'unknown350bf7c0(?)', '0x3ccfd60b': 'withdraw()', '0x7d7c2a1c': 'rebalance()', '0xd0febe4c': 'buyTokens()'} 

# storage definitions
def storage:
    # storage address 0
    balanceOf
    # storage address 1
    totalSupply # mask: a s
    # storage address 2
    allowance
    # storage address 3
    owner # mask: a s
    # storage address 4
    unknown2156e6c6
    # storage address 5
    description
    # storage address 6
    category
    # storage address 7
    version
    # storage address 8
    status # mask: a s
    # storage address 8
    fundType # mask: a s
    # storage address 9
    tokens
    # storage address 11
    supportRebalance # mask: a s
    # storage address 12
    decimals # mask: a s
    # storage address 13
    name
    # storage address 14
    symbol
    # storage address 15
    unknown5075edbfAddress # mask: a s
    # storage address 15
    paused # mask: a s
    # storage address 16
    pausedTime # mask: a s
    # storage address 17
    unknown44644ef0 # mask: a s
    # storage address 18
    stor18
    # storage address 19
    unknownd92cb69a # mask: a s
    # storage address 20
    weights
    # storage address 21
    accumulatedFee # mask: a s
    # storage address 22
    unknown96733c5c # mask: a s
    # storage address 23
    unknown95074562 # mask: a s
    # storage address 24
    unknownd214a0b3 # mask: a s
    # storage address 64971906060199484650489883867960036121042624035769298300412616658428710730821
    stor8FA4 # mask: a s
    # storage address 69338188928101896310183398435557611686971956871093484960849267644903331084636
    stor994C # mask: a s
    # storage address 96351918824266353149294365124150426862519194503016895848570039310471999023132
    storD505 # mask: a s
# hash = 0x05f8d55d
# getter = None
# const = None
# payable = True
def addOwnerBalance() payable: 
  require call.value + maccumulatedFee >= maccumulatedFee
  maccumulatedFee += call.value


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 13]]]], ['loc', 13]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


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


# hash = 0x093857b2
# getter = ['storage', 8, 0, 19]
# const = None
# payable = False
def unknown093857b2(): # not payable
  require munknownd92cb69a <= 4
  return munknownd92cb69a


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
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def totalSupply(): # not payable
  return mtotalSupply


# hash = 0x1bb7cc99
# getter = None
# const = ['return', 108257207130708801562209681605405335279468377333953338004896192468914205097984]
# payable = False
const WHITELIST = 0xef57686974656c69737450726f76696465720000000000000000000000000000


# hash = 0x1fa98406
# getter = ['storage', 8, 0, 8]
# const = None
# payable = False
def fundType(): # not payable
  require mfundType <= 2
  return mfundType


# hash = 0x200d2ed2
# getter = ['storage', 8, 8, 8]
# const = None
# payable = False
def status(): # not payable
  require mstatus <= 3
  return mstatus


# hash = 0x2156e6c6
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 4]]]
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
      if not mstor18m[m_param1m]:
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
# getter = ['storage', 256, 0, 12]
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
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknown44644ef0(): # not payable
  return munknown44644ef0


# hash = 0x4700d305
# getter = None
# const = None
# payable = False
def panic(): # not payable
  require caller == mowner
  call mowner with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  [94midx = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = 9
      require ext_code.size(mtokensm[[94midxm]m.field_0)
      call mtokensm[[94midxm]m.field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[96] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
      mem[100] = mowner
      mem[132] = ext_call.return_data[0]
      require ext_code.size(mtokensm[[94midxm]m.field_0)
      call mtokensm[[94midxm]m.field_0.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args mowner, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x4f64b2be
# getter = ['storage', 160, 0, ['add', ['sha3', 9], ['cd', 4]]]
# const = None
# payable = False
def tokens(uint256 m_param1): # not payable
  require m_param1 < mtokensm.length
  return mtokensm[m_param1m]m.field_0


# hash = 0x5075edbf
# getter = ['storage', 160, 8, 15]
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
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 7]]]], ['loc', 7]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 0, 15]]
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
  if mtokensm.length:
      mem[128 len 32 * mtokensm.length] = code.data[23501 len 32 * mtokensm.length]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = 9
      mem[(32 * mtokensm.length) + 132] = this.address
      require ext_code.size(mtokensm[[94midxm]m.field_0)
      call mtokensm[[94midxm]m.field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[(32 * mtokensm.length) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require [94midx < mtokensm.length
      mem[(32 * [94midx) + 128] = ext_call.return_data[0]
      require [94midx < mtokensm.length
      if ext_call.return_data[0] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mtokensm.length) + 128] = [94ms
  if [94ms:
      mem[(32 * mtokensm.length) + 160 len 32 * [94ms] = code.data[23501 len 32 * [94ms]
  [94midx = 0
  [94mt = 0
  mwhile [94midx < mtokensm.lengthm:
      require [94midx < mtokensm.length
      if mem[(32 * [94midx) + 128] <= 0:
          [94midx = [94midx + 1
          [94mt = [94mt
          mcontinue 
      require [94midx < mtokensm.length
      mem[0] = 9
      require [94mt < [94ms
      mem[(32 * mtokensm.length) + (32 * [94mt) + 160] = mtokensm[[94midxm]m.field_0
      [94midx = [94midx + 1
      [94mt = [94mt + 1
      mcontinue 
  mem[(32 * mtokensm.length) + (32 * [94ms) + 224 len floor32([94ms)] = mem[(32 * mtokensm.length) + 160 len floor32([94ms)]
  return Array(len=[94ms, data=mem[(32 * mtokensm.length) + 160 len floor32([94ms)], mem[(32 * mtokensm.length) + (32 * [94ms) + floor32([94ms) + 224 len (32 * [94ms) - floor32([94ms)]), 


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


# hash = 0x6e947298
# getter = None
# const = None
# payable = False
def getETHBalance(): # not payable
  require maccumulatedFee <= eth.balance(this.address)
  return (eth.balance(this.address) - maccumulatedFee)


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


# hash = 0x7284e416
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 5]]]], ['loc', 5]]]
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
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mtokensm.lengthm:
          mem[0] = 9
          require ext_code.size(mtokensm[[94midxm]m.field_0)
          call mtokensm[[94midxm]m.field_0.decimals() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[100] = this.address
          require ext_code.size(mtokensm[[94midxm]m.field_0)
          call mtokensm[[94midxm]m.field_0.balanceOf(address owner) with:
               gas gas_remaining wei
              args this.address
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = mtokensm[[94midxm]m.field_0
              [94ms = ext_call.return_data[0]
              [94ms = ext_call.return_data[0]
              mcontinue 
          mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
          mem[164] = 10^ext_call.return_data[0]
          mem[196] = 0
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args mtokensm[[94midxm]m.field_0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
          mem[96 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = mtokensm[[94midxm]m.field_0
              [94ms = ext_call.return_data[0]
              [94ms = ext_call.return_data[0]
              mcontinue 
          if not ext_call.return_data[0]:
              if 10^ext_call.return_data[0]:
                  if 0 / 10^ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = mtokensm[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94ms = ext_call.return_data[0]
                      mcontinue 
          else:
              if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
                  if 10^ext_call.return_data[0]:
                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                          [94midx = [94midx + 1
                          [94ms = mtokensm[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94ms = ext_call.return_data[0]
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
  require mstatus <= 3
  if mstatus == 3:
      [94midx = 0
      [94ms = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mtokensm.lengthm:
          mem[0] = 9
          require ext_code.size(mtokensm[[94midxm]m.field_0)
          call mtokensm[[94midxm]m.field_0.decimals() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[100] = this.address
          require ext_code.size(mtokensm[[94midxm]m.field_0)
          call mtokensm[[94midxm]m.field_0.balanceOf(address owner) with:
               gas gas_remaining wei
              args this.address
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = mtokensm[[94midxm]m.field_0
              [94ms = ext_call.return_data[0]
              [94ms = ext_call.return_data[0]
              mcontinue 
          mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
          mem[164] = 10^ext_call.return_data[0]
          mem[196] = 0
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args mtokensm[[94midxm]m.field_0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
          mem[96 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = mtokensm[[94midxm]m.field_0
              [94ms = ext_call.return_data[0]
              [94ms = ext_call.return_data[0]
              mcontinue 
          if not ext_call.return_data[0]:
              if 10^ext_call.return_data[0]:
                  if 0 / 10^ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = mtokensm[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94ms = ext_call.return_data[0]
                      mcontinue 
          else:
              if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
                  if 10^ext_call.return_data[0]:
                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                          [94midx = [94midx + 1
                          [94ms = mtokensm[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94ms = ext_call.return_data[0]
                          mcontinue 
          revert
      require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].freeze() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].withdraw(address payee) with:
           gas gas_remaining wei
          args caller
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if ext_call.return_data[32]:
          require ext_call.return_data[32] <= mbalanceOfm[callerm]
          mbalanceOfm[callerm] -= ext_call.return_data[32]
          log Transfer(
                address from=ext_call.return_data[32],
                address to=caller,
                uint256 value=0)
          require ext_call.return_data[32] <= mtotalSupply
          mtotalSupply -= ext_call.return_data[32]
          call caller with:
             value ext_call.return_data[0] wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].finalize() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0x74d16c37
# getter = None
# const = None
# payable = False
def getAssetsValue(): # not payable
  [94midx = 0
  [94ms = 0
  [94ms = 0
  [94ms = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = 9
      require ext_code.size(mtokensm[[94midxm]m.field_0)
      call mtokensm[[94midxm]m.field_0.decimals() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = this.address
      require ext_code.size(mtokensm[[94midxm]m.field_0)
      call mtokensm[[94midxm]m.field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = mtokensm[[94midxm]m.field_0
          [94ms = ext_call.return_data[0]
          [94ms = ext_call.return_data[0]
          mcontinue 
      mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      mem[164] = 10^ext_call.return_data[0]
      mem[196] = 0
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args mtokensm[[94midxm]m.field_0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
      mem[96 len 64] = ext_call.return_data[0 len 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = mtokensm[[94midxm]m.field_0
          [94ms = ext_call.return_data[0]
          [94ms = ext_call.return_data[0]
          mcontinue 
      if not ext_call.return_data[0]:
          if 10^ext_call.return_data[0]:
              if 0 / 10^ext_call.return_data[0] >= 0:
                  [94midx = [94midx + 1
                  [94ms = mtokensm[[94midxm]m.field_0
                  [94ms = ext_call.return_data[0]
                  [94ms = ext_call.return_data[0]
                  mcontinue 
      else:
          if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
              if 10^ext_call.return_data[0]:
                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = mtokensm[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94ms = ext_call.return_data[0]
                      mcontinue 
      revert
  return 0


# hash = 0x768c7206
# getter = None
# const = ['return', 100000000000000000]
# payable = False
const unknown768c7206 = 10^17


# hash = 0x7a1ac61e
# getter = None
# const = None
# payable = True
def unknown7a1ac61e(addr m_param1, uint256 m_param2, uint256 m_param3) payable: 
  require caller == mowner
  require mstatus <= 3
  require not mstatus
  require call.value >= 10^17
  require m_param1
  require m_param3 <= 10000
  munknown44644ef0 = 8760 * 24 * 3600
  munknown96733c5c = m_param3
  require m_param1
  munknown5075edbfAddress = m_param1
  mstorD505 = 1
  mstor994C = 1
  mstor8FA4 = 1
  mem[416] = 'MarketProvider'
  mem[448] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[480] = 0x526562616c616e636550726f76696465720000000000000000000000000000
  mem[512] = 'RiskProvider'
  mem[544] = 0xef57686974656c69737450726f76696465720000000000000000000000000000
  mem[576] = 0x46656550726f76696465720000000000000000000000000000000000000000
  mem[608] = 0x5265696d6275727361626c6500000000000000000000000000000000000000
  mem[640] = 0x576974686472617750726f7669646572000000000000000000000000000000
  mem[672] = 0x4c6f636b657250726f76696465720000000000000000000000000000000000
  mem[704] = 0x5374657050726f766964657200000000000000000000000000000000000000
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
          if not mstor18m[[94m_46m]:
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
      mem[32] = 4
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(munknown2156e6c6m['MarketProvider'm])
  call munknown2156e6c6m['MarketProvider'm].0xdfd92f8a with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require caller == mowner
  require ext_code.size(munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m])
  call munknown2156e6c6m[0x46656550726f76696465720000000000000000000000000000000000000000m].setFeePercentage(uint256 newFee) with:
       gas gas_remaining wei
      args m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[896] = 4
  require 0 < ext_call.return_data[0]
  mem[768] = 3
  require 1 < ext_call.return_data[0]
  mem[800] = 10
  require 2 < ext_call.return_data[0]
  mem[832] = 5
  require 3 < ext_call.return_data[0]
  mem[864] = 5
  mem[928] = 0x526562616c616e636550726f76696465720000000000000000000000000000
  mem[960] = 0x576974686472617750726f7669646572000000000000000000000000000000
  mem[992] = 0x427579546f6b656e7300000000000000000000000000000000000000000000
  mem[1024] = 0x4765744574680000000000000000000000000000000000000000000000000000
  mem[1056] = 0xfdb880b900000000000000000000000000000000000000000000000000000000
  mem[1060] = 64
  mem[1124] = 4
  mem[1156 len 0] = None
  mem[1092] = 224
  mem[1284] = ext_call.return_data[0]
  mem[1316 len floor32(ext_call.return_data[0])] = mem[768 len floor32(ext_call.return_data[0])]
  require ext_code.size(munknown2156e6c6m[0x5374657050726f766964657200000000000000000000000000000000000000m])
  call munknown2156e6c6m[0x5374657050726f766964657200000000000000000000000000000000000000m].0xfdb880b9 with:
       gas gas_remaining wei
      args 64, 224, 4, mem[1156 len 128], ext_call.return_data[0], mem[1316 len 32 * ext_call.return_data[0]]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mstatus = 1
  require call.value + maccumulatedFee >= maccumulatedFee
  maccumulatedFee += call.value


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  require caller == mowner
  require not mpaused
  mpaused = 1
  mpausedTime = block.timestamp


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


# hash = 0x8d859f3e
# getter = None
# const = ['return', "'PriceProvider'"]
# payable = False
const PRICE = 'PriceProvider'


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 3]
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


# hash = 0x95074562
# getter = ['storage', 256, 0, 23]
# const = None
# payable = False
def unknown95074562(): # not payable
  return munknown95074562


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 14]]]], ['loc', 14]]]
# const = None
# payable = False
def symbol(): # not payable
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0x96733c5c
# getter = ['storage', 256, 0, 22]
# const = None
# payable = False
def unknown96733c5c(): # not payable
  return munknown96733c5c


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
  [94ms = 0
  [94ms = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = 9
      require ext_code.size(mtokensm[[94midxm]m.field_0)
      call mtokensm[[94midxm]m.field_0.decimals() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = this.address
      require ext_code.size(mtokensm[[94midxm]m.field_0)
      call mtokensm[[94midxm]m.field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = mtokensm[[94midxm]m.field_0
          [94ms = ext_call.return_data[0]
          [94ms = ext_call.return_data[0]
          mcontinue 
      mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      mem[164] = 10^ext_call.return_data[0]
      mem[196] = 0
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args mtokensm[[94midxm]m.field_0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
      mem[96 len 64] = ext_call.return_data[0 len 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = mtokensm[[94midxm]m.field_0
          [94ms = ext_call.return_data[0]
          [94ms = ext_call.return_data[0]
          mcontinue 
      if not ext_call.return_data[0]:
          if 10^ext_call.return_data[0]:
              if 0 / 10^ext_call.return_data[0] >= 0:
                  [94midx = [94midx + 1
                  [94ms = mtokensm[[94midxm]m.field_0
                  [94ms = ext_call.return_data[0]
                  [94ms = ext_call.return_data[0]
                  mcontinue 
      else:
          if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
              if 10^ext_call.return_data[0]:
                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = mtokensm[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94ms = ext_call.return_data[0]
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


# hash = 0x9c5bcf0a
# getter = None
# const = ['return', 117422681643562417633727756126837387880898653753433760274182616911081111552]
# payable = False
const unknown9c5bcf0a = 0x427579546f6b656e7300000000000000000000000000000000000000000000


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
  if mtokensm.length:
      mem[128] = addr(mtokensm.field_0)
      [94midx = 128
      [94ms = 0
      mwhile (32 * mtokensm.length) + 96 > [94midxm:
          mem[[94midx + 32] = mtokensm[[94msm]m.field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
  if mweightsm.length:
      mem[(32 * mtokensm.length) + 160] = uint256(mweightsm.field_0)
      [94midx = (32 * mtokensm.length) + 160
      [94ms = 0
      mwhile (32 * mtokensm.length) + (32 * mweightsm.length) + 128 > [94midxm:
          mem[[94midx + 32] = mweightsm[[94msm]m.field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          mcontinue 
  mem[(32 * mtokensm.length) + (32 * mweightsm.length) + 256 len floor32(mtokensm.length)] = mem[128 len floor32(mtokensm.length)]
  mem[(64 * mtokensm.length) + (32 * mweightsm.length) + 256] = mweightsm.length
  mem[(64 * mtokensm.length) + (32 * mweightsm.length) + 288 len floor32(mweightsm.length)] = mem[(32 * mtokensm.length) + 160 len floor32(mweightsm.length)]
  return Array(len=mtokensm.length, data=mem[128 len floor32(mtokensm.length)], mem[(32 * mtokensm.length) + (32 * mweightsm.length) + floor32(mtokensm.length) + 256 len (32 * mtokensm.length) + (32 * mweightsm.length) + -floor32(mtokensm.length) + 32]), 
         (32 * mtokensm.length) + 96


# hash = 0xad03261e
# getter = ['bool', ['storage', 8, 0, 11]]
# const = None
# payable = False
def supportRebalance(): # not payable
  return bool(msupportRebalance)


# hash = 0xb2cca39d
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def pausedTime(): # not payable
  return mpausedTime


# hash = 0xb50e44b8
# getter = None
# const = ['return', 122743337058602665564631354263472091436608355031343273141981057876456636416]
# payable = False
const EXCHANGE = 0x45786368616e676550726f7669646572000000000000000000000000000000


# hash = 0xb5f163ff
# getter = ['storage', 256, 0, ['add', ['sha3', 20], ['cd', 4]]]
# const = None
# payable = False
def weights(uint256 m_param1): # not payable
  require m_param1 < mweightsm.length
  return mweightsm[m_param1m]m.field_0


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
  require m_amount > 0
  require mstatus <= 3
  if mstatus == 3:
      [94midx = 0
      [94ms = 0
      [94ms = 0
      [94ms = 0
      mwhile [94midx < mtokensm.lengthm:
          mem[0] = 9
          require ext_code.size(mtokensm[[94midxm]m.field_0)
          call mtokensm[[94midxm]m.field_0.decimals() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[100] = this.address
          require ext_code.size(mtokensm[[94midxm]m.field_0)
          call mtokensm[[94midxm]m.field_0.balanceOf(address owner) with:
               gas gas_remaining wei
              args this.address
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = mtokensm[[94midxm]m.field_0
              [94ms = ext_call.return_data[0]
              [94ms = ext_call.return_data[0]
              mcontinue 
          mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
          mem[164] = 10^ext_call.return_data[0]
          mem[196] = 0
          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args mtokensm[[94midxm]m.field_0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
          mem[96 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = mtokensm[[94midxm]m.field_0
              [94ms = ext_call.return_data[0]
              [94ms = ext_call.return_data[0]
              mcontinue 
          if not ext_call.return_data[0]:
              if 10^ext_call.return_data[0]:
                  if 0 / 10^ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = mtokensm[[94midxm]m.field_0
                      [94ms = ext_call.return_data[0]
                      [94ms = ext_call.return_data[0]
                      mcontinue 
          else:
              if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
                  if 10^ext_call.return_data[0]:
                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                          [94midx = [94midx + 1
                          [94ms = mtokensm[[94midxm]m.field_0
                          [94ms = ext_call.return_data[0]
                          [94ms = ext_call.return_data[0]
                          mcontinue 
          revert
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
          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(ext_call.return_data[0]), m_amount, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0xeb5d3ab5 with:
         value m_amount wei
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), m_amount, ext_call.return_data[32], mowner, 0
  else:
      require m_amount + 10^17 >= m_amount
      require m_amount + 10^17 <= maccumulatedFee
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


# hash = 0xd214a0b3
# getter = ['storage', 256, 0, 24]
# const = None
# payable = False
def unknownd214a0b3(): # not payable
  return munknownd214a0b3


# hash = 0xd3c9ad17
# getter = None
# const = ['return', 145581188027504223537441783832673983417913822530146853016789242044036939776]
# payable = False
const REBALANCE = 0x526562616c616e636550726f76696465720000000000000000000000000000


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


# hash = 0xd92cb69a
# getter = ['storage', 8, 0, 19]
# const = None
# payable = False
def unknownd92cb69a(): # not payable
  require munknownd92cb69a <= 4
  return munknownd92cb69a


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]
# const = None
# payable = False
def allowance(address m_owner, address m_spender): # not payable
  return mallowancem[addr(m_owner)m]m[addr(m_spender)m]


# hash = 0xe8b5e51f
# getter = None
# const = None
# payable = True
def invest() payable: 
  require not mpaused
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
          require mstatus <= 3
          if mstatus != 1:
              revert with 0, 'The Fund is not active'
          else:
              if call.value < 10^15:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Minimum value to invest is 0.001 ETH'
              else:
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
                              [94ms = 0
                              [94ms = 0
                              mwhile [94midx < mtokensm.lengthm:
                                  mem[0] = 9
                                  require ext_code.size(mtokensm[[94midxm]m.field_0)
                                  call mtokensm[[94midxm]m.field_0.decimals() with:
                                       gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      mem[100] = this.address
                                      require ext_code.size(mtokensm[[94midxm]m.field_0)
                                      call mtokensm[[94midxm]m.field_0.balanceOf(address owner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      mem[96] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          if ext_call.return_data[0]:
                                              mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                              mem[164] = 10^ext_call.return_data[0]
                                              mem[196] = 0
                                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                                   gas gas_remaining wei
                                                  args mtokensm[[94midxm]m.field_0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
                                              mem[96 len 64] = ext_call.return_data[0 len 64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 64
                                                  if ext_call.return_data[0]:
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          require 10^ext_call.return_data[0]
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = mtokensm[[94midxm]m.field_0
                                                          [94ms = ext_call.return_data[0]
                                                          [94ms = ext_call.return_data[0]
                                                          mcontinue 
                                                      else:
                                                          require 10^ext_call.return_data[0]
                                                          require 0 / 10^ext_call.return_data[0] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = mtokensm[[94midxm]m.field_0
                                                          [94ms = ext_call.return_data[0]
                                                          [94ms = ext_call.return_data[0]
                                                          mcontinue 
                                                  else:
                                                      [94midx = [94midx + 1
                                                      [94ms = mtokensm[[94midxm]m.field_0
                                                      [94ms = ext_call.return_data[0]
                                                      [94ms = ext_call.return_data[0]
                                                      mcontinue 
                                          else:
                                              [94midx = [94midx + 1
                                              [94ms = mtokensm[[94midxm]m.field_0
                                              [94ms = ext_call.return_data[0]
                                              [94ms = ext_call.return_data[0]
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
                              [94ms = 0
                              [94ms = 0
                              mwhile [94midx < mtokensm.lengthm:
                                  mem[0] = 9
                                  require ext_code.size(mtokensm[[94midxm]m.field_0)
                                  call mtokensm[[94midxm]m.field_0.decimals() with:
                                       gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      mem[100] = this.address
                                      require ext_code.size(mtokensm[[94midxm]m.field_0)
                                      call mtokensm[[94midxm]m.field_0.balanceOf(address owner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      mem[96] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require return_data.size >= 32
                                          if ext_call.return_data[0]:
                                              mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                              mem[164] = 10^ext_call.return_data[0]
                                              mem[196] = 0
                                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                                   gas gas_remaining wei
                                                  args mtokensm[[94midxm]m.field_0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
                                              mem[96 len 64] = ext_call.return_data[0 len 64]
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              else:
                                                  require return_data.size >= 64
                                                  if ext_call.return_data[0]:
                                                      if ext_call.return_data[0]:
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
                                                          require 10^ext_call.return_data[0]
                                                          require ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = mtokensm[[94midxm]m.field_0
                                                          [94ms = ext_call.return_data[0]
                                                          [94ms = ext_call.return_data[0]
                                                          mcontinue 
                                                      else:
                                                          require 10^ext_call.return_data[0]
                                                          require 0 / 10^ext_call.return_data[0] >= 0
                                                          [94midx = [94midx + 1
                                                          [94ms = mtokensm[[94midxm]m.field_0
                                                          [94ms = ext_call.return_data[0]
                                                          [94ms = ext_call.return_data[0]
                                                          mcontinue 
                                                  else:
                                                      [94midx = [94midx + 1
                                                      [94ms = mtokensm[[94midxm]m.field_0
                                                      [94ms = ext_call.return_data[0]
                                                      [94ms = ext_call.return_data[0]
                                                      mcontinue 
                                          else:
                                              [94midx = [94midx + 1
                                              [94ms = mtokensm[[94midxm]m.field_0
                                              [94ms = ext_call.return_data[0]
                                              [94ms = ext_call.return_data[0]
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
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 6]]]], ['loc', 6]]]
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
# getter = ['storage', 256, 0, 21]
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


