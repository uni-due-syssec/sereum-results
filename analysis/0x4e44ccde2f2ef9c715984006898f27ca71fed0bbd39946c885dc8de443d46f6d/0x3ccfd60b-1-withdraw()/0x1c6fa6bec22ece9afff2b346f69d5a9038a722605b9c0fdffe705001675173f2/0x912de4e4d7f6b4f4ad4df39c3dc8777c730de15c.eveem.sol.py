# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x912DE4E4D7f6b4f4Ad4DF39C3DC8777c730de15c 
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
    weights
    # storage address 20
    accumulatedFee # mask: a s
    # storage address 21
    unknown96733c5c # mask: a s
    # storage address 22
    unknown95074562 # mask: a s
    # storage address 23
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
  require call.value + accumulatedFee >= accumulatedFee
  accumulatedFee += call.value


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 13]]]], ['loc', 13]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x089f7f85
# getter = None
# const = None
# payable = False
def hasRisk(address _sender, address _receiver, address _tokenAddress, uint256 _amount, uint256 _rate): # not payable
  require ext_code.size(unknown2156e6c6['RiskProvider'])
  call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
       gas gas_remaining wei
      args 0, 0, addr(_receiver), addr(_tokenAddress), _amount, _rate
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
def approve(address _spender, uint256 _value): # not payable
  require not paused
  allowance[caller][addr(_spender)] = _value
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
  return totalSupply


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
  require fundType <= 2
  return fundType


# hash = 0x200d2ed2
# getter = ['storage', 8, 8, 8]
# const = None
# payable = False
def status(): # not payable
  require status <= 3
  return status


# hash = 0x2156e6c6
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = False
def unknown2156e6c6(uint256 _param1): # not payable
  return unknown2156e6c6[_param1]


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address _from, address _to, uint256 _value): # not payable
  require not paused
  require _value <= balanceOf[addr(_from)]
  require _value <= allowance[addr(_from)][caller]
  require _to
  require _value <= balanceOf[addr(_from)]
  balanceOf[addr(_from)] -= _value
  require _value + balanceOf[_to] >= balanceOf[_to]
  balanceOf[addr(_to)] = _value + balanceOf[_to]
  require _value <= allowance[addr(_from)][caller]
  allowance[addr(_from)][caller] -= _value
  log Transfer(
        address from=_value,
        address to=_from,
        uint256 value=_to)
  return 1


# hash = 0x2feb34d4
# getter = None
# const = None
# payable = False
def unknown2feb34d4(uint256 _param1): # not payable
  require caller == owner
  require ext_code.size(unknown5075edbfAddress)
  call unknown5075edbfAddress.0xf57ce488 with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if unknown2156e6c6[_param1] != addr(ext_call.return_data[0]):
      require ext_code.size(unknown5075edbfAddress)
      call unknown5075edbfAddress.0xf57ce488 with:
           gas gas_remaining wei
          args _param1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[12 len 20]
      unknown2156e6c6[_param1] = addr(ext_call.return_data[0])
      if not stor18[_param1]:
          require ext_code.size(unknown2156e6c6[_param1])
          call unknown2156e6c6[_param1].MOT() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args unknown2156e6c6[_param1], 0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
               gas gas_remaining wei
              args unknown2156e6c6[_param1], -1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
  return unknown2156e6c6[_param1]


# hash = 0x313ce567
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def decimals(): # not payable
  return decimals


# hash = 0x38a1ff63
# getter = None
# const = None
# payable = False
def unknown38a1ff63(array _param1, array _param2): # not payable
  require caller == owner
  require ext_code.size(unknown2156e6c6[0x4c6f636b657250726f76696465720000000000000000000000000000000000])
  call unknown2156e6c6[0x4c6f636b657250726f76696465720000000000000000000000000000000000].0x38a1ff63 with:
       gas gas_remaining wei
      args 0, 64, (32 * _param1.length) + 96, _param1.length, call.data[_param1 + 36 len 32 * _param1.length], _param2.length, call.data[_param2 + 36 len 32 * _param2.length]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == owner
  require paused
  paused = 0
  log Unpause()


# hash = 0x43d726d6
# getter = None
# const = None
# payable = False
def close(): # not payable
  if owner != caller:
      require 1 == bool(paused)
      require pausedTime + unknown44644ef0 <= block.timestamp
  require status <= 3
  require status
  status = 3
  return 1


# hash = 0x44644ef0
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknown44644ef0(): # not payable
  return unknown44644ef0


# hash = 0x4700d305
# getter = None
# const = None
# payable = False
def panic(): # not payable
  require caller == owner
  call owner with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  [94midx = 0
  while [94midx < tokens.length:
      mem[0] = 9
      require ext_code.size(tokens[[94midx].field_0)
      call tokens[[94midx].field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[96] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
      mem[100] = owner
      mem[132] = ext_call.return_data[0]
      require ext_code.size(tokens[[94midx].field_0)
      call tokens[[94midx].field_0.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args owner, ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 


# hash = 0x4f64b2be
# getter = ['storage', 160, 0, ['add', ['sha3', 9], ['cd', 4]]]
# const = None
# payable = False
def tokens(uint256 _param1): # not payable
  require _param1 < tokens.length
  return tokens[_param1].field_0


# hash = 0x5075edbf
# getter = ['storage', 160, 8, 15]
# const = None
# payable = False
def unknown5075edbf(): # not payable
  return unknown5075edbfAddress


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
  return version[0 len version.length]


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 0, 15]]
# const = None
# payable = False
def paused(): # not payable
  return bool(paused)


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
  if tokens.length:
      mem[128 len 32 * tokens.length] = code.data[23022 len 32 * tokens.length]
  [94midx = 0
  [94ms = 0
  while [94midx < tokens.length:
      mem[0] = 9
      mem[(32 * tokens.length) + 132] = this.address
      require ext_code.size(tokens[[94midx].field_0)
      call tokens[[94midx].field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[(32 * tokens.length) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require [94midx < tokens.length
      mem[(32 * [94midx) + 128] = ext_call.return_data[0]
      require [94midx < tokens.length
      if ext_call.return_data[0] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  mem[(32 * tokens.length) + 128] = [94ms
  if [94ms:
      mem[(32 * tokens.length) + 160 len 32 * [94ms] = code.data[23022 len 32 * [94ms]
  [94midx = 0
  [94mt = 0
  while [94midx < tokens.length:
      require [94midx < tokens.length
      if mem[(32 * [94midx) + 128] <= 0:
          [94midx = [94midx + 1
          [94mt = [94mt
          continue 
      require [94midx < tokens.length
      mem[0] = 9
      require [94mt < [94ms
      mem[(32 * tokens.length) + (32 * [94mt) + 160] = tokens[[94midx].field_0
      [94midx = [94midx + 1
      [94mt = [94mt + 1
      continue 
  mem[(32 * tokens.length) + (32 * [94ms) + 224 len floor32([94ms)] = mem[(32 * tokens.length) + 160 len floor32([94ms)]
  return Array(len=[94ms, data=mem[(32 * tokens.length) + 160 len floor32([94ms)], mem[(32 * tokens.length) + (32 * [94ms) + floor32([94ms) + 224 len (32 * [94ms) - floor32([94ms)]), 


# hash = 0x66188463
# getter = None
# const = None
# payable = False
def decreaseApproval(address _spender, uint256 _subtractedValue): # not payable
  require not paused
  if _subtractedValue >= allowance[caller][addr(_spender)]:
      allowance[caller][addr(_spender)] = 0
  else:
      require _subtractedValue <= allowance[caller][addr(_spender)]
      allowance[caller][addr(_spender)] -= _subtractedValue
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
  require accumulatedFee <= eth.balance(this.address)
  return (eth.balance(this.address) - accumulatedFee)


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 0]]]
# const = None
# payable = False
def balanceOf(address _owner): # not payable
  return balanceOf[addr(_owner)]


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipRenounced(address previousOwner=owner)
  owner = 0


# hash = 0x7284e416
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 5]]]], ['loc', 5]]]
# const = None
# payable = False
def description(): # not payable
  return description[0 len description.length]


# hash = 0x745400c9
# getter = None
# const = None
# payable = False
def requestWithdraw(uint256 _value): # not payable
  require not paused
  if 0 == totalSupply:
      require ext_code.size(unknown2156e6c6['RiskProvider'])
      call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
           gas gas_remaining wei
          args 0, uint32(caller), addr(this.address), addr(this.address), _value, 10^18
  else:
      require accumulatedFee <= eth.balance(this.address)
      [94midx = 0
      [94ms = 0
      while [94midx < tokens.length:
          mem[0] = 9
          mem[100] = this.address
          require ext_code.size(tokens[[94midx].field_0)
          call tokens[[94midx].field_0.balanceOf(address owner) with:
               gas gas_remaining wei
              args this.address
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              continue 
          require [94midx < tokens.length
          mem[0] = 9
          mem[132] = tokens[[94midx].field_0
          mem[164] = 10^18
          mem[196] = 0
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94midx].field_0, 10^18, 0
          mem[96 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              continue 
          if not ext_call.return_data[0]:
              if ext_call.return_data[0]:
                  if 0 / ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      continue 
          else:
              if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18:
                  if ext_call.return_data[0]:
                      if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] >= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          continue 
          revert
      require eth.balance(this.address) - accumulatedFee >= 0
      if not eth.balance(this.address) - accumulatedFee:
          require totalSupply
          require ext_code.size(unknown2156e6c6['RiskProvider'])
          call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
               gas gas_remaining wei
              args caller, addr(this.address), addr(this.address), _value, 0 / totalSupply
      else:
          require (eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / eth.balance(this.address) - accumulatedFee == 10^decimals
          require totalSupply
          require ext_code.size(unknown2156e6c6['RiskProvider'])
          call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
               gas gas_remaining wei
              args caller, addr(this.address), addr(this.address), _value, (eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require not ext_call.return_data[0]
  require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
  call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].0xc8c01a55 with:
       gas gas_remaining wei
      args caller, _value
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require status <= 3
  if status == 3:
      [94midx = 0
      [94ms = 0
      while [94midx < tokens.length:
          mem[0] = 9
          mem[100] = this.address
          require ext_code.size(tokens[[94midx].field_0)
          call tokens[[94midx].field_0.balanceOf(address owner) with:
               gas gas_remaining wei
              args this.address
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              continue 
          require [94midx < tokens.length
          mem[0] = 9
          mem[132] = tokens[[94midx].field_0
          mem[164] = 10^18
          mem[196] = 0
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94midx].field_0, 10^18, 0
          mem[96 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              continue 
          if not ext_call.return_data[0]:
              if ext_call.return_data[0]:
                  if 0 / ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      continue 
          else:
              if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18:
                  if ext_call.return_data[0]:
                      if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] >= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          continue 
          revert
      require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].freeze() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].withdraw(address payee) with:
           gas gas_remaining wei
          args caller
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if ext_call.return_data[32]:
          require ext_call.return_data[32] <= balanceOf[caller]
          balanceOf[caller] -= ext_call.return_data[32]
          log Transfer(
                address from=ext_call.return_data[32],
                address to=caller,
                uint256 value=0)
          require ext_call.return_data[32] <= totalSupply
          totalSupply -= ext_call.return_data[32]
          call caller with:
             value ext_call.return_data[0] wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].finalize() with:
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
  while [94midx < tokens.length:
      mem[0] = 9
      mem[100] = this.address
      require ext_code.size(tokens[[94midx].field_0)
      call tokens[[94midx].field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
      require [94midx < tokens.length
      mem[0] = 9
      mem[132] = tokens[[94midx].field_0
      mem[164] = 10^18
      mem[196] = 0
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94midx].field_0, 10^18, 0
      mem[96 len 64] = ext_call.return_data[0 len 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
      if not ext_call.return_data[0]:
          if ext_call.return_data[0]:
              if 0 / ext_call.return_data[0] >= 0:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  continue 
      else:
          if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18:
              if ext_call.return_data[0]:
                  if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      continue 
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
def unknown7a1ac61e(addr _param1, uint256 _param2, uint256 _param3) payable: 
  require caller == owner
  require status <= 3
  require not status
  require call.value >= 10^17
  require _param1
  require _param3 <= 10000
  unknown44644ef0 = 8760 * 24 * 3600
  unknown96733c5c = _param3
  require _param1
  unknown5075edbfAddress = _param1
  storD505 = 1
  stor994C = 1
  stor8FA4 = 1
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
  while [94midx < 10:
      [94m_46 = mem[(32 * [94midx) + 416]
      require caller == owner
      mem[740] = mem[(32 * [94midx) + 416]
      require ext_code.size(unknown5075edbfAddress)
      call unknown5075edbfAddress.0xf57ce488 with:
           gas gas_remaining wei
          args [94m_46
      mem[736] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if unknown2156e6c6[[94m_46] != addr(ext_call.return_data[0]):
          mem[740] = [94m_46
          require ext_code.size(unknown5075edbfAddress)
          call unknown5075edbfAddress.0xf57ce488 with:
               gas gas_remaining wei
              args [94m_46
          mem[736] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require addr(ext_call.return_data[0])
          unknown2156e6c6[[94m_46] = addr(ext_call.return_data[0])
          if not stor18[[94m_46]:
              require ext_code.size(unknown2156e6c6[[94m_46])
              call unknown2156e6c6[[94m_46].MOT() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args unknown2156e6c6[[94m_46], 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[736] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
              mem[740] = unknown2156e6c6[[94m_46]
              mem[772] = -1
              require ext_code.size(addr(ext_call.return_data[0]))
              call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args unknown2156e6c6[[94m_46], -1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
      mem[0] = [94m_46
      mem[32] = 4
      [94midx = [94midx + 1
      continue 
  require ext_code.size(unknown2156e6c6['MarketProvider'])
  call unknown2156e6c6['MarketProvider'].0xdfd92f8a with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require caller == owner
  require ext_code.size(unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000])
  call unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000].setFeePercentage(uint256 newFee) with:
       gas gas_remaining wei
      args _param2
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
  require ext_code.size(unknown2156e6c6[0x5374657050726f766964657200000000000000000000000000000000000000])
  call unknown2156e6c6[0x5374657050726f766964657200000000000000000000000000000000000000].0xfdb880b9 with:
       gas gas_remaining wei
      args 64, 224, 4, mem[1156 len 128], ext_call.return_data[0], mem[1316 len 32 * ext_call.return_data[0]]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  status = 1
  require call.value + accumulatedFee >= accumulatedFee
  accumulatedFee += call.value


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  require caller == owner
  require not paused
  paused = 1
  pausedTime = block.timestamp


# hash = 0x862b2839
# getter = None
# const = ['return', 32293466278026087082630401698836907263138185254920806816698666571931416788992]
# payable = False
const unknown862b2839 = 0x4765744574680000000000000000000000000000000000000000000000000000


# hash = 0x87b8aa6a
# getter = None
# const = None
# payable = False
def unknown87b8aa6a(uint8 _param1, bool _param2): # not payable
  require caller == owner
  require _param1 <= 2
  require ext_code.size(unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000])
  call unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000].0x8719e8ac with:
       gas gas_remaining wei
      args _param1 << 248, _param2
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
  return owner


# hash = 0x918f8674
# getter = None
# const = ['return', 10000]
# payable = False
const DENOMINATOR = 10000


# hash = 0x9375206a
# getter = None
# const = None
# payable = False
def setAllowed(address[] _accounts, uint8 _key, bool _allowed): # not payable
  require caller == owner
  require _key <= 2
  mem[(32 * _accounts.length) + 260 len floor32(_accounts.length)] = call.data[_accounts + 36 len floor32(_accounts.length)]
  require ext_code.size(unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000])
  call unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000].0xb65c7c81 with:
       gas gas_remaining wei
      args Array(len=_accounts.length, data=call.data[_accounts + 36 len floor32(_accounts.length)], mem[(32 * _accounts.length) + floor32(_accounts.length) + 260 len (32 * _accounts.length) - floor32(_accounts.length)]), _key << 248, _allowed
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 1


# hash = 0x95074562
# getter = ['storage', 256, 0, 22]
# const = None
# payable = False
def unknown95074562(): # not payable
  return unknown95074562


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 14]]]], ['loc', 14]]]
# const = None
# payable = False
def symbol(): # not payable
  return symbol[0 len symbol.length]


# hash = 0x96733c5c
# getter = ['storage', 256, 0, 21]
# const = None
# payable = False
def unknown96733c5c(): # not payable
  return unknown96733c5c


# hash = 0x98d5fdca
# getter = None
# const = None
# payable = False
def getPrice(): # not payable
  if 0 == totalSupply:
      return 10^18
  require accumulatedFee <= eth.balance(this.address)
  [94midx = 0
  [94ms = 0
  while [94midx < tokens.length:
      mem[0] = 9
      mem[100] = this.address
      require ext_code.size(tokens[[94midx].field_0)
      call tokens[[94midx].field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
      require [94midx < tokens.length
      mem[0] = 9
      mem[132] = tokens[[94midx].field_0
      mem[164] = 10^18
      mem[196] = 0
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94midx].field_0, 10^18, 0
      mem[96 len 64] = ext_call.return_data[0 len 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
      if not ext_call.return_data[0]:
          if ext_call.return_data[0]:
              if 0 / ext_call.return_data[0] >= 0:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  continue 
      else:
          if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18:
              if ext_call.return_data[0]:
                  if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      continue 
      revert
  if eth.balance(this.address) - accumulatedFee >= 0:
      if not eth.balance(this.address) - accumulatedFee:
          if totalSupply:
              return (0 / totalSupply)
      else:
          if (eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / eth.balance(this.address) - accumulatedFee == 10^decimals:
              if totalSupply:
                  return ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply)
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
def transfer(address _to, uint256 _value): # not payable
  require not paused
  require _value <= balanceOf[caller]
  require _to
  require _value <= balanceOf[caller]
  balanceOf[caller] -= _value
  require _value + balanceOf[_to] >= balanceOf[_to]
  balanceOf[addr(_to)] = _value + balanceOf[_to]
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
  if tokens.length:
      mem[128] = addr(tokens.field_0)
      [94midx = 128
      [94ms = 0
      while (32 * tokens.length) + 96 > [94midx:
          mem[[94midx + 32] = tokens[[94ms].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
  if weights.length:
      mem[(32 * tokens.length) + 160] = uint256(weights.field_0)
      [94midx = (32 * tokens.length) + 160
      [94ms = 0
      while (32 * tokens.length) + (32 * weights.length) + 128 > [94midx:
          mem[[94midx + 32] = weights[[94ms].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
  mem[(32 * tokens.length) + (32 * weights.length) + 256 len floor32(tokens.length)] = mem[128 len floor32(tokens.length)]
  mem[(64 * tokens.length) + (32 * weights.length) + 256] = weights.length
  mem[(64 * tokens.length) + (32 * weights.length) + 288 len floor32(weights.length)] = mem[(32 * tokens.length) + 160 len floor32(weights.length)]
  return Array(len=tokens.length, data=mem[128 len floor32(tokens.length)], mem[(32 * tokens.length) + (32 * weights.length) + floor32(tokens.length) + 256 len (32 * tokens.length) + (32 * weights.length) + -floor32(tokens.length) + 32]), 
         (32 * tokens.length) + 96


# hash = 0xad03261e
# getter = ['bool', ['storage', 8, 0, 11]]
# const = None
# payable = False
def supportRebalance(): # not payable
  return bool(supportRebalance)


# hash = 0xb2cca39d
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def pausedTime(): # not payable
  return pausedTime


# hash = 0xb50e44b8
# getter = None
# const = ['return', 122743337058602665564631354263472091436608355031343273141981057876456636416]
# payable = False
const EXCHANGE = 0x45786368616e676550726f7669646572000000000000000000000000000000


# hash = 0xb5f163ff
# getter = ['storage', 256, 0, ['add', ['sha3', 19], ['cd', 4]]]
# const = None
# payable = False
def weights(uint256 _param1): # not payable
  require _param1 < weights.length
  return weights[_param1].field_0


# hash = 0xb86ec38f
# getter = None
# const = ['return', 145581378006796796482538153470897892133593206079523589563550605086325473280]
# payable = False
const REIMBURSABLE = 0x5265696d6275727361626c6500000000000000000000000000000000000000


# hash = 0xb8893727
# getter = None
# const = None
# payable = False
def unknownb8893727(uint256 _param1, uint256 _param2): # not payable
  require caller == owner
  require ext_code.size(unknown2156e6c6[0x5374657050726f766964657200000000000000000000000000000000000000])
  call unknown2156e6c6[0x5374657050726f766964657200000000000000000000000000000000000000].0xd63a81f0 with:
       gas gas_remaining wei
      args _param1, _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xbe357616
# getter = None
# const = None
# payable = False
def withdrawFee(uint256 _amount): # not payable
  require caller == owner
  require not paused
  require _amount > 0
  require status <= 3
  if status == 3:
      [94midx = 0
      [94ms = 0
      while [94midx < tokens.length:
          mem[0] = 9
          mem[100] = this.address
          require ext_code.size(tokens[[94midx].field_0)
          call tokens[[94midx].field_0.balanceOf(address owner) with:
               gas gas_remaining wei
              args this.address
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              continue 
          require [94midx < tokens.length
          mem[0] = 9
          mem[132] = tokens[[94midx].field_0
          mem[164] = 10^18
          mem[196] = 0
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94midx].field_0, 10^18, 0
          mem[96 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              continue 
          if not ext_call.return_data[0]:
              if ext_call.return_data[0]:
                  if 0 / ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      continue 
          else:
              if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18:
                  if ext_call.return_data[0]:
                      if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] >= 0:
                          [94midx = [94midx + 1
                          [94ms = ext_call.return_data[0]
                          continue 
          revert
      require _amount <= accumulatedFee
      accumulatedFee -= _amount
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].MOT() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(ext_call.return_data[0]), _amount, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0xeb5d3ab5 with:
         value _amount wei
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), _amount, ext_call.return_data[32], owner, 0
  else:
      require _amount + 10^17 >= _amount
      require _amount + 10^17 <= accumulatedFee
      require _amount <= accumulatedFee
      accumulatedFee -= _amount
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].MOT() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0, 4008636142, addr(ext_call.return_data[0]), _amount, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0xeb5d3ab5 with:
         value _amount wei
           gas gas_remaining wei
          args 0, ext_call.return_data[32], uint32(_amount), ext_call.return_data[32], owner, 0
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
# getter = ['storage', 256, 0, 23]
# const = None
# payable = False
def unknownd214a0b3(): # not payable
  return unknownd214a0b3


# hash = 0xd3c9ad17
# getter = None
# const = ['return', 145581188027504223537441783832673983417913822530146853016789242044036939776]
# payable = False
const REBALANCE = 0x526562616c616e636550726f76696465720000000000000000000000000000


# hash = 0xd73dd623
# getter = None
# const = None
# payable = False
def increaseApproval(address _spender, uint256 _addedValue): # not payable
  require not paused
  require _addedValue + allowance[caller][addr(_spender)] >= allowance[caller][addr(_spender)]
  allowance[caller][addr(_spender)] += _addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]
# const = None
# payable = False
def allowance(address _owner, address _spender): # not payable
  return allowance[addr(_owner)][addr(_spender)]


# hash = 0xe8b5e51f
# getter = None
# const = None
# payable = True
def invest() payable: 
  require not paused
  require ext_code.size(unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000])
  call unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000].0x5faa299a with:
       gas gas_remaining wei
      args 0, caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  else:
      require return_data.size >= 32
      require ext_call.return_data[0]
      require ext_code.size(unknown2156e6c6['RiskProvider'])
      call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
           gas gas_remaining wei
          args 0, uint32(caller), addr(this.address), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, call.value, 1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require not ext_call.return_data[0]
          require status <= 3
          if status != 1:
              revert with 0, 'The Fund is not active'
          else:
              if call.value < 10^15:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Minimum value to invest is 0.001 ETH'
              else:
                  if totalSupply <= 0:
                      require ext_code.size(unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000])
                      call unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000].0x8b28ab1e with:
                           gas gas_remaining wei
                          args caller, call.value
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      else:
                          require return_data.size >= 32
                          require ext_call.return_data[0] <= call.value
                          if call.value - ext_call.return_data[0]:
                              require (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / call.value - ext_call.return_data[0] == 10^decimals
                              require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                              accumulatedFee += ext_call.return_data[0]
                              require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / 10^18) + balanceOf[caller] >= balanceOf[caller]
                              balanceOf[caller] += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / 10^18
                              require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / 10^18) + totalSupply >= totalSupply
                              totalSupply += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / 10^18
                              log Transfer(
                                    address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / 10^18),
                                    address to=0,
                                    uint256 value=caller)
                              return 1
                          else:
                              require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                              accumulatedFee += ext_call.return_data[0]
                              require balanceOf[caller] >= balanceOf[caller]
                              require totalSupply >= totalSupply
                              log Transfer(
                                    address from=0,
                                    address to=0,
                                    uint256 value=caller)
                              return 1
                  else:
                      if call.value:
                          require 10^decimals * call.value / call.value == 10^decimals
                          require totalSupply
                          if totalSupply != 0:
                              require accumulatedFee <= eth.balance(this.address)
                              [94midx = 0
                              [94ms = 0
                              while [94midx < tokens.length:
                                  mem[0] = 9
                                  mem[100] = this.address
                                  require ext_code.size(tokens[[94midx].field_0)
                                  call tokens[[94midx].field_0.balanceOf(address owner) with:
                                       gas gas_remaining wei
                                      args this.address
                                  mem[96] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if ext_call.return_data[0]:
                                          require [94midx < tokens.length
                                          mem[0] = 9
                                          mem[132] = tokens[[94midx].field_0
                                          mem[164] = 10^18
                                          mem[196] = 0
                                          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                                          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                               gas gas_remaining wei
                                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94midx].field_0, 10^18, 0
                                          mem[96 len 64] = ext_call.return_data[0 len 64]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 64
                                              if ext_call.return_data[0]:
                                                  if ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                                                      require ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  continue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = ext_call.return_data[0]
                                          continue 
                              require eth.balance(this.address) - accumulatedFee >= 0
                              if eth.balance(this.address) - accumulatedFee:
                                  require (eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / eth.balance(this.address) - accumulatedFee == 10^decimals
                                  require totalSupply
                                  require 10^decimals * call.value / totalSupply <= (eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply
                                  require ext_code.size(unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000])
                                  call unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000].0x8b28ab1e with:
                                       gas gas_remaining wei
                                      args caller, call.value
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= call.value
                                      if call.value - ext_call.return_data[0]:
                                          require (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / call.value - ext_call.return_data[0] == 10^decimals
                                          require ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)
                                          require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                                          accumulatedFee += ext_call.return_data[0]
                                          require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                                          balanceOf[caller] += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)
                                          require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)) + totalSupply >= totalSupply
                                          totalSupply += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)
                                          log Transfer(
                                                address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)),
                                                address to=0,
                                                uint256 value=caller)
                                          return 1
                                      else:
                                          require ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)
                                          require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                                          accumulatedFee += ext_call.return_data[0]
                                          require (0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                                          balanceOf[caller] += 0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)
                                          require (0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)) + totalSupply >= totalSupply
                                          totalSupply += 0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)
                                          log Transfer(
                                                address from=(0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (10^decimals * call.value / totalSupply)),
                                                address to=0,
                                                uint256 value=caller)
                                          return 1
                              else:
                                  require totalSupply
                                  require 10^decimals * call.value / totalSupply <= 0 / totalSupply
                                  require ext_code.size(unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000])
                                  call unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000].0x8b28ab1e with:
                                       gas gas_remaining wei
                                      args caller, call.value
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= call.value
                                      if call.value - ext_call.return_data[0]:
                                          require (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / call.value - ext_call.return_data[0] == 10^decimals
                                          require (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                                          require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                                          accumulatedFee += ext_call.return_data[0]
                                          require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / (0 / totalSupply) - (10^decimals * call.value / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                                          balanceOf[caller] += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                                          require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / (0 / totalSupply) - (10^decimals * call.value / totalSupply)) + totalSupply >= totalSupply
                                          totalSupply += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                                          log Transfer(
                                                address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / (0 / totalSupply) - (10^decimals * call.value / totalSupply)),
                                                address to=0,
                                                uint256 value=caller)
                                          return 1
                                      else:
                                          require (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                                          require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                                          accumulatedFee += ext_call.return_data[0]
                                          require (0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                                          balanceOf[caller] += 0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                                          require (0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)) + totalSupply >= totalSupply
                                          totalSupply += 0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                                          log Transfer(
                                                address from=(0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)),
                                                address to=0,
                                                uint256 value=caller)
                                          return 1
                          else:
                              require 10^decimals * call.value / totalSupply <= 10^18
                              require ext_code.size(unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000])
                              call unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000].0x8b28ab1e with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= call.value
                                  if call.value - ext_call.return_data[0]:
                                      require (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / call.value - ext_call.return_data[0] == 10^decimals
                                      require -(10^decimals * call.value / totalSupply) + 10^18
                                      require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                                      accumulatedFee += ext_call.return_data[0]
                                      require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(10^decimals * call.value / totalSupply) + 10^18) + balanceOf[caller] >= balanceOf[caller]
                                      balanceOf[caller] += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(10^decimals * call.value / totalSupply) + 10^18
                                      require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(10^decimals * call.value / totalSupply) + 10^18) + totalSupply >= totalSupply
                                      totalSupply += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(10^decimals * call.value / totalSupply) + 10^18
                                      log Transfer(
                                            address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(10^decimals * call.value / totalSupply) + 10^18),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                                  else:
                                      require -(10^decimals * call.value / totalSupply) + 10^18
                                      require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                                      accumulatedFee += ext_call.return_data[0]
                                      require (0 / -(10^decimals * call.value / totalSupply) + 10^18) + balanceOf[caller] >= balanceOf[caller]
                                      balanceOf[caller] += 0 / -(10^decimals * call.value / totalSupply) + 10^18
                                      require (0 / -(10^decimals * call.value / totalSupply) + 10^18) + totalSupply >= totalSupply
                                      totalSupply += 0 / -(10^decimals * call.value / totalSupply) + 10^18
                                      log Transfer(
                                            address from=(0 / -(10^decimals * call.value / totalSupply) + 10^18),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                      else:
                          require totalSupply
                          if totalSupply != 0:
                              require accumulatedFee <= eth.balance(this.address)
                              [94midx = 0
                              [94ms = 0
                              while [94midx < tokens.length:
                                  mem[0] = 9
                                  mem[100] = this.address
                                  require ext_code.size(tokens[[94midx].field_0)
                                  call tokens[[94midx].field_0.balanceOf(address owner) with:
                                       gas gas_remaining wei
                                      args this.address
                                  mem[96] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      if ext_call.return_data[0]:
                                          require [94midx < tokens.length
                                          mem[0] = 9
                                          mem[132] = tokens[[94midx].field_0
                                          mem[164] = 10^18
                                          mem[196] = 0
                                          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                                          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                               gas gas_remaining wei
                                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94midx].field_0, 10^18, 0
                                          mem[96 len 64] = ext_call.return_data[0 len 64]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              require return_data.size >= 64
                                              if ext_call.return_data[0]:
                                                  if ext_call.return_data[0]:
                                                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                                                      require ext_call.return_data[0]
                                                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      continue 
                                              else:
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  continue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = ext_call.return_data[0]
                                          continue 
                              require eth.balance(this.address) - accumulatedFee >= 0
                              if eth.balance(this.address) - accumulatedFee:
                                  require (eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / eth.balance(this.address) - accumulatedFee == 10^decimals
                                  require totalSupply
                                  require 0 / totalSupply <= (eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply
                                  require ext_code.size(unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000])
                                  call unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000].0x8b28ab1e with:
                                       gas gas_remaining wei
                                      args caller, call.value
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= call.value
                                      if call.value - ext_call.return_data[0]:
                                          require (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / call.value - ext_call.return_data[0] == 10^decimals
                                          require ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)
                                          require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                                          accumulatedFee += ext_call.return_data[0]
                                          require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                                          balanceOf[caller] += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)
                                          require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)) + totalSupply >= totalSupply
                                          totalSupply += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)
                                          log Transfer(
                                                address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)),
                                                address to=0,
                                                uint256 value=caller)
                                          return 1
                                      else:
                                          require ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)
                                          require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                                          accumulatedFee += ext_call.return_data[0]
                                          require (0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                                          balanceOf[caller] += 0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)
                                          require (0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)) + totalSupply >= totalSupply
                                          totalSupply += 0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)
                                          log Transfer(
                                                address from=(0 / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (0 / totalSupply)),
                                                address to=0,
                                                uint256 value=caller)
                                          return 1
                              else:
                                  require totalSupply
                                  require 0 / totalSupply <= 0 / totalSupply
                                  require ext_code.size(unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000])
                                  call unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000].0x8b28ab1e with:
                                       gas gas_remaining wei
                                      args caller, call.value
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      require ext_call.return_data[0] <= call.value
                                      require call.value - ext_call.return_data[0]
                                      require (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / call.value - ext_call.return_data[0] == 10^decimals
                                      revert
                          else:
                              require 0 / totalSupply <= 10^18
                              require ext_code.size(unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000])
                              call unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000].0x8b28ab1e with:
                                   gas gas_remaining wei
                                  args caller, call.value
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_call.return_data[0] <= call.value
                                  if call.value - ext_call.return_data[0]:
                                      require (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / call.value - ext_call.return_data[0] == 10^decimals
                                      require -(0 / totalSupply) + 10^18
                                      require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                                      accumulatedFee += ext_call.return_data[0]
                                      require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(0 / totalSupply) + 10^18) + balanceOf[caller] >= balanceOf[caller]
                                      balanceOf[caller] += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(0 / totalSupply) + 10^18
                                      require ((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(0 / totalSupply) + 10^18) + totalSupply >= totalSupply
                                      totalSupply += (call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(0 / totalSupply) + 10^18
                                      log Transfer(
                                            address from=((call.value * 10^decimals) - (ext_call.return_data[0] * 10^decimals) / -(0 / totalSupply) + 10^18),
                                            address to=0,
                                            uint256 value=caller)
                                      return 1
                                  else:
                                      require -(0 / totalSupply) + 10^18
                                      require ext_call.return_data[0] + accumulatedFee >= accumulatedFee
                                      accumulatedFee += ext_call.return_data[0]
                                      require (0 / -(0 / totalSupply) + 10^18) + balanceOf[caller] >= balanceOf[caller]
                                      balanceOf[caller] += 0 / -(0 / totalSupply) + 10^18
                                      require (0 / -(0 / totalSupply) + 10^18) + totalSupply >= totalSupply
                                      totalSupply += 0 / -(0 / totalSupply) + 10^18
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
  return category[0 len category.length]


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require caller == owner
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = 0xf46f16c2
# getter = None
# const = ['return', "'MarketProvider'"]
# payable = False
const MARKET = 'MarketProvider'


# hash = 0xf8ce3164
# getter = ['storage', 256, 0, 20]
# const = None
# payable = False
def accumulatedFee(): # not payable
  return accumulatedFee


# hash = 0xfe56e232
# getter = None
# const = None
# payable = False
def setManagementFee(uint256 _fee): # not payable
  require caller == owner
  require ext_code.size(unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000])
  call unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000].setFeePercentage(uint256 newFee) with:
       gas gas_remaining wei
      args _fee
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


