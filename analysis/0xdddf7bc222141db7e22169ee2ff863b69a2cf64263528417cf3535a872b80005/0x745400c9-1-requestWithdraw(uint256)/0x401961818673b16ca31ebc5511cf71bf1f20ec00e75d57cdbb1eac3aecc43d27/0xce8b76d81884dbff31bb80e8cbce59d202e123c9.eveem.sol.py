# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xce8B76d81884DBFf31bB80e8cBCe59d202e123c9 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x350bf7c0': 'unknown350bf7c0(?)', '0x3ccfd60b': 'withdraw()'} 

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
    category # mask: a s
    # storage address 7
    version # mask: a s
    # storage address 8
    fundType # mask: a s
    # storage address 8
    status # mask: a s
    # storage address 9
    tokens
    # storage address 10
    decimals # mask: a s
    # storage address 11
    name
    # storage address 12
    symbol
    # storage address 13
    paused # mask: a s
    # storage address 13
    unknown5075edbfAddress # mask: a s
    # storage address 14
    pausedTime # mask: a s
    # storage address 15
    unknown44644ef0 # mask: a s
    # storage address 16
    stor16
    # storage address 17
    unknownd92cb69a # mask: a s
    # storage address 19
    stor19
    # storage address 20
    investors
    # storage address 21
    amounts
    # storage address 22
    stor22
    # storage address 23
    stor23
    # storage address 24
    unknown07b08870
    # storage address 25
    accumulatedFee # mask: a s
    # storage address 26
    unknown1c2a0e5c
    # storage address 27
    unknown81d62bf5
    # storage address 28
    unknown36724ef4 # mask: a s
    # storage address 6291654672758609839894286073275205852155809607691735580756437056550348818336
    storDE8F # mask: a s
    # storage address 25315808107304436489073159149816469109778116306248924645674996900934862678329
    stor37F8 # mask: a s
    # storage address 26616959624788145501257665028759500958019551560565664426117466910078421933505
    stor26616959624788145501257665028759500958019551560565664426117466910078421933505
    # storage address 47444862884950761695014885221812414276220458302405847337313290849613399387294
    stor68E4 # mask: a s
    # storage address 51902219266518241557051091243148885716133317790826664023326234995173080825474
    stor72BF # mask: a s
# hash = 0x05f8d55d
# getter = None
# const = None
# payable = True
def addOwnerBalance() payable: 
  require call.value + accumulatedFee >= accumulatedFee
  accumulatedFee += call.value


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 11]]]], ['loc', 11]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x07b08870
# getter = ['storage', 160, 0, ['add', ['sha3', 24], ['cd', 4]]]
# const = None
# payable = False
def unknown07b08870(uint256 _param1): # not payable
  require _param1 < unknown07b08870.length
  return addr(unknown07b08870[_param1].field_0)


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


# hash = 0x1c2a0e5c
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 26]]]
# const = None
# payable = False
def unknown1c2a0e5c(addr _param1): # not payable
  return unknown1c2a0e5c[_param1]


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


# hash = 0x201d83d8
# getter = None
# const = ['return', 149184142682071031466986821281381690014212207952467003834806840160369508352]
# payable = False
const unknown201d83d8 = 0x546f6b656e42726f6b656e0000000000000000000000000000000000000000


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
      if not stor16[_param1]:
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
# getter = ['storage', 256, 0, 10]
# const = None
# payable = False
def decimals(): # not payable
  return decimals


# hash = 0x36724ef4
# getter = ['bool', ['storage', 8, 0, 28]]
# const = None
# payable = False
def unknown36724ef4(): # not payable
  return bool(unknown36724ef4)


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


# hash = 0x3c98d189
# getter = None
# const = None
# payable = False
def unknown3c98d189(uint256 _param1, array _param2, array _param3, array _param4): # not payable
  mem[96] = _param2.length
  mem[128 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  mem[(32 * _param2.length) + 128] = _param3.length
  mem[(32 * _param2.length) + 160 len 32 * _param3.length] = call.data[_param3 + 36 len 32 * _param3.length]
  mem[(32 * _param3.length) + (32 * _param2.length) + 160] = _param4.length
  mem[(32 * _param3.length) + (32 * _param2.length) + 192 len 32 * _param4.length] = call.data[_param4 + 36 len 32 * _param4.length]
  if caller == owner:
      require unknownd92cb69a <= 2
      require not unknownd92cb69a
      [94midx = 0
      while [94midx < _param2.length:
          require [94midx < _param2.length
          mem[0] = mem[(32 * [94midx) + 140 len 20]
          mem[32] = 23
          if stor23[mem[(32 * [94midx) + 140 len 20]]:
              require [94midx < _param3.length
              mem[(32 * _param2.length) + (32 * [94midx) + 160] = 0
              [94midx = [94midx + 1
              continue 
          require [94midx < _param2.length
          require ext_code.size(mem[(32 * [94midx) + 140 len 20])
          call mem[(32 * [94midx) + 140 len 20].decimals() with:
               gas gas_remaining wei
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 18
          require [94midx < _param3.length
          [94m_368 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
          require [94midx < mem[(32 * _param3.length) + (32 * _param2.length) + 160]
          [94m_375 = mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param2.length) + 192]
          mem[0] = 'RiskProvider'
          mem[32] = 4
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = this.address
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000]
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 260] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 292] = [94m_368
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 324] = [94m_375
          require ext_code.size(unknown2156e6c6['RiskProvider'])
          call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
               gas gas_remaining wei
              args addr(this.address), unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, [94m_368, [94m_375
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require not ext_call.return_data[0]
          require [94midx < _param3.length
          require mem[(32 * _param2.length) + (32 * [94midx) + 160] >= 0
          [94midx = [94midx + 1
          continue 
      require accumulatedFee <= eth.balance(this.address)
      require eth.balance(this.address) - accumulatedFee >= 0
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = 0x15cdc52900000000000000000000000000000000000000000000000000000000
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 292] = this.address
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 324] = _param1
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = 160
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 356] = _param2.length
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 388 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = (32 * _param2.length) + 192
      mem[(64 * _param2.length) + (32 * _param4.length) + (32 * _param3.length) + 388] = _param3.length
      mem[(64 * _param2.length) + (32 * _param4.length) + (32 * _param3.length) + 420 len floor32(_param3.length)] = mem[(32 * _param2.length) + 160 len floor32(_param3.length)]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 260] = (32 * _param3.length) + (32 * _param2.length) + 224
      mem[(64 * _param3.length) + (64 * _param2.length) + (32 * _param4.length) + 420] = mem[(32 * _param3.length) + (32 * _param2.length) + 160]
      mem[(64 * _param3.length) + (64 * _param2.length) + (32 * _param4.length) + 452 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])] = mem[(32 * _param3.length) + (32 * _param2.length) + 192 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])]
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x15cdc529 with:
           gas gas_remaining wei
          args mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196 len (32 * mem[(32 * _param3.length) + (32 * _param2.length) + 160]) + (32 * _param3.length) + (32 * _param2.length) + 256]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < _param2.length
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < _param2.length
                  [94m_1371 = mem[(32 * [94midx) + 128]
                  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = this.address
                  require ext_code.size(addr([94m_1371))
                  call addr([94m_1371).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1371)
                  mem[32] = 21
                  amounts[addr([94m_1371)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1371)
                      mem[32] = 22
                      if not stor22[addr([94m_1371)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1371)
                          mem[0] = addr([94m_1371)
                          mem[32] = 22
                          stor22[addr([94m_1371)] = 1
              [94midx = [94midx + 1
              continue 
          return 1
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = _param2.length
      if not _param2.length:
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 4
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228] = 32
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 260] = _param2.length
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 292 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228 len (32 * _param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1374 = mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + (32 * mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1374 + 224]
              if mem[(32 * [94midx) + (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1374 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 23
                  if not stor23[mem[(32 * [94midx) + 140 len 20]]:
                      require [94midx < mem[96]
                      stor23[mem[(32 * [94midx) + 140 len 20]] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 21
                      if amounts[mem[(32 * [94midx) + 140 len 20]] > 0:
                          require [94midx < mem[96]
                          unknown07b08870.length++
                          mem[0] = 24
                          addr(unknown07b08870[unknown07b08870.length].field_0) = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1649 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1649)
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1649)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_1671 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          require mem[[94m_1671] <= 4294967296
                          require mem[[94m_1671] + 32 <= return_data.size
                          require mem[[94m_1671 + mem[[94m_1671]] <= 4294967296 and mem[[94m_1671] + (32 * mem[[94m_1671 + mem[[94m_1671]]) + 32 <= return_data.size
              [94midx = [94midx + 1
              continue 
          [94m_1687 = mem[96]
          [94midx = 0
          while [94midx < [94m_1687:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1703 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1703))
                  call addr([94m_1703).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1703)
                  mem[32] = 21
                  amounts[addr([94m_1703)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1703)
                      mem[32] = 22
                      if not stor22[addr([94m_1703)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1703)
                          mem[0] = addr([94m_1703)
                          mem[32] = 22
                          stor22[addr([94m_1703)] = 1
              [94midx = [94midx + 1
              continue 
      else:
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 224 len 32 * _param2.length] = code.data[24497 len 32 * _param2.length]
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 4
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228] = 32
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 260] = _param2.length
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 292 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228 len (32 * _param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1375 = mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + (32 * mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1375 + 224]
              if mem[(32 * [94midx) + (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1375 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 23
                  if not stor23[mem[(32 * [94midx) + 140 len 20]]:
                      require [94midx < mem[96]
                      stor23[mem[(32 * [94midx) + 140 len 20]] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 21
                      if amounts[mem[(32 * [94midx) + 140 len 20]] > 0:
                          require [94midx < mem[96]
                          unknown07b08870.length++
                          mem[0] = 24
                          addr(unknown07b08870[unknown07b08870.length].field_0) = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1654 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1654)
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1654)
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_1672 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          require mem[[94m_1672] <= 4294967296
                          require mem[[94m_1672] + 32 <= return_data.size
                          require mem[[94m_1672 + mem[[94m_1672]] <= 4294967296 and mem[[94m_1672] + (32 * mem[[94m_1672 + mem[[94m_1672]]) + 32 <= return_data.size
              [94midx = [94midx + 1
              continue 
          [94m_1688 = mem[96]
          [94midx = 0
          while [94midx < [94m_1688:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1706 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1706))
                  call addr([94m_1706).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1706)
                  mem[32] = 21
                  amounts[addr([94m_1706)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1706)
                      mem[32] = 22
                      if not stor22[addr([94m_1706)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1706)
                          mem[0] = addr([94m_1706)
                          mem[32] = 22
                          stor22[addr([94m_1706)] = 1
              [94midx = [94midx + 1
              continue 
  else:
      require ext_code.size(unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000])
      call unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000].0x919253e8 with:
           gas gas_remaining wei
          args addr(this.address), 2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = 2
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = caller
      require ext_code.size(unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000])
      call unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000].0x5faa299a with:
           gas gas_remaining wei
          args 2, caller
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require unknownd92cb69a <= 2
      require not unknownd92cb69a
      [94midx = 0
      while [94midx < _param2.length:
          require [94midx < _param2.length
          mem[0] = mem[(32 * [94midx) + 140 len 20]
          mem[32] = 23
          if stor23[mem[(32 * [94midx) + 140 len 20]]:
              require [94midx < _param3.length
              mem[(32 * _param2.length) + (32 * [94midx) + 160] = 0
              [94midx = [94midx + 1
              continue 
          require [94midx < _param2.length
          require ext_code.size(mem[(32 * [94midx) + 140 len 20])
          call mem[(32 * [94midx) + 140 len 20].decimals() with:
               gas gas_remaining wei
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] <= 18
          require [94midx < _param3.length
          [94m_373 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
          require [94midx < mem[(32 * _param3.length) + (32 * _param2.length) + 160]
          [94m_376 = mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param2.length) + 192]
          mem[0] = 'RiskProvider'
          mem[32] = 4
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = this.address
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000]
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 260] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 292] = [94m_373
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 324] = [94m_376
          require ext_code.size(unknown2156e6c6['RiskProvider'])
          call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
               gas gas_remaining wei
              args addr(this.address), unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, [94m_373, [94m_376
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require not ext_call.return_data[0]
          require [94midx < _param3.length
          require mem[(32 * _param2.length) + (32 * [94midx) + 160] >= 0
          [94midx = [94midx + 1
          continue 
      require accumulatedFee <= eth.balance(this.address)
      require eth.balance(this.address) - accumulatedFee >= 0
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = 0x15cdc52900000000000000000000000000000000000000000000000000000000
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 292] = this.address
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 324] = _param1
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = 160
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 356] = _param2.length
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 388 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = (32 * _param2.length) + 192
      mem[(64 * _param2.length) + (32 * _param4.length) + (32 * _param3.length) + 388] = _param3.length
      mem[(64 * _param2.length) + (32 * _param4.length) + (32 * _param3.length) + 420 len floor32(_param3.length)] = mem[(32 * _param2.length) + 160 len floor32(_param3.length)]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 260] = (32 * _param3.length) + (32 * _param2.length) + 224
      mem[(64 * _param3.length) + (64 * _param2.length) + (32 * _param4.length) + 420] = mem[(32 * _param3.length) + (32 * _param2.length) + 160]
      mem[(64 * _param3.length) + (64 * _param2.length) + (32 * _param4.length) + 452 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])] = mem[(32 * _param3.length) + (32 * _param2.length) + 192 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])]
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x15cdc529 with:
           gas gas_remaining wei
          args mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196 len (32 * mem[(32 * _param3.length) + (32 * _param2.length) + 160]) + (32 * _param3.length) + (32 * _param2.length) + 256]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < _param2.length
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < _param2.length
                  [94m_1376 = mem[(32 * [94midx) + 128]
                  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = this.address
                  require ext_code.size(addr([94m_1376))
                  call addr([94m_1376).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1376)
                  mem[32] = 21
                  amounts[addr([94m_1376)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1376)
                      mem[32] = 22
                      if not stor22[addr([94m_1376)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1376)
                          mem[0] = addr([94m_1376)
                          mem[32] = 22
                          stor22[addr([94m_1376)] = 1
              [94midx = [94midx + 1
              continue 
          return 1
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = _param2.length
      if not _param2.length:
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 4
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228] = 32
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 260] = _param2.length
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 292 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228 len (32 * _param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1379 = mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + (32 * mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1379 + 224]
              if mem[(32 * [94midx) + (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1379 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 23
                  if not stor23[mem[(32 * [94midx) + 140 len 20]]:
                      require [94midx < mem[96]
                      stor23[mem[(32 * [94midx) + 140 len 20]] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 21
                      if amounts[mem[(32 * [94midx) + 140 len 20]] > 0:
                          require [94midx < mem[96]
                          unknown07b08870.length++
                          mem[0] = 24
                          addr(unknown07b08870[unknown07b08870.length].field_0) = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1659 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1659)
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1659)
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
              continue 
          [94m_1689 = mem[96]
          [94midx = 0
          while [94midx < [94m_1689:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1709 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1709))
                  call addr([94m_1709).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1709)
                  mem[32] = 21
                  amounts[addr([94m_1709)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1709)
                      mem[32] = 22
                      if not stor22[addr([94m_1709)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1709)
                          mem[0] = addr([94m_1709)
                          mem[32] = 22
                          stor22[addr([94m_1709)] = 1
              [94midx = [94midx + 1
              continue 
      else:
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 224 len 32 * _param2.length] = code.data[24497 len 32 * _param2.length]
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 4
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228] = 32
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 260] = _param2.length
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 292 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228 len (32 * _param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1380 = mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + (32 * mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1380 + 224]
              if mem[(32 * [94midx) + (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1380 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 23
                  if not stor23[mem[(32 * [94midx) + 140 len 20]]:
                      require [94midx < mem[96]
                      stor23[mem[(32 * [94midx) + 140 len 20]] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 21
                      if amounts[mem[(32 * [94midx) + 140 len 20]] > 0:
                          require [94midx < mem[96]
                          unknown07b08870.length++
                          mem[0] = 24
                          addr(unknown07b08870[unknown07b08870.length].field_0) = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1664 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1664)
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0xce7b5574 with:
                               gas gas_remaining wei
                              args addr([94m_1664)
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
              continue 
          [94m_1690 = mem[96]
          [94midx = 0
          while [94midx < [94m_1690:
              require [94midx < mem[96]
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < mem[96]
                  [94m_1712 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_1712))
                  call addr([94m_1712).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1712)
                  mem[32] = 21
                  amounts[addr([94m_1712)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1712)
                      mem[32] = 22
                      if not stor22[addr([94m_1712)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1712)
                          mem[0] = addr([94m_1712)
                          mem[32] = 22
                          stor22[addr([94m_1712)] = 1
              [94midx = [94midx + 1
              continue 
  return 0


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
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknown44644ef0(): # not payable
  return unknown44644ef0


# hash = 0x4926dc98
# getter = None
# const = ['return', 1000000000000000000]
# payable = False
const unknown4926dc98 = 10^18


# hash = 0x4f64b2be
# getter = ['storage', 160, 0, ['add', ['sha3', 9], ['cd', 4]]]
# const = None
# payable = False
def tokens(uint256 _param1): # not payable
  require _param1 < tokens.length
  return addr(tokens[_param1].field_0)


# hash = 0x5075edbf
# getter = ['storage', 160, 8, 13]
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
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def version(): # not payable
  return version


# hash = 0x55a3b2c1
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 21]]]
# const = None
# payable = False
def amounts(address _param1): # not payable
  return amounts[_param1]


# hash = 0x5acf6903
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 22]]]]
# const = None
# payable = False
def activeTokens(address _param1): # not payable
  return bool(stor22[_param1])


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 0, 13]]
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
  [94midx = 0
  [94ms = 0
  while [94midx < tokens.length:
      mem[0] = addr(tokens[[94midx].field_0)
      mem[32] = 23
      if stor23[addr(stor9[[94midx].field_0)]:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      require [94midx < tokens.length
      mem[0] = addr(tokens[[94midx].field_0)
      mem[32] = 21
      if amounts[addr(stor9[[94midx].field_0)] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  if [94ms:
      mem[128 len 32 * [94ms] = code.data[24497 len 32 * [94ms]
  [94midx = 0
  [94mt = 0
  while [94midx < tokens.length:
      mem[0] = addr(tokens[[94midx].field_0)
      mem[32] = 23
      if stor23[addr(stor9[[94midx].field_0)]:
          [94midx = [94midx + 1
          [94mt = [94mt
          continue 
      require [94midx < tokens.length
      mem[0] = addr(tokens[[94midx].field_0)
      mem[32] = 21
      if amounts[addr(stor9[[94midx].field_0)] <= 0:
          [94midx = [94midx + 1
          [94mt = [94mt
          continue 
      require [94midx < tokens.length
      mem[0] = 9
      require [94mt < [94ms
      mem[(32 * [94mt) + 128] = addr(tokens[[94midx].field_0)
      [94midx = [94midx + 1
      [94mt = [94mt + 1
      continue 
  mem[(32 * [94ms) + 192 len floor32([94ms)] = mem[128 len floor32([94ms)]
  return Array(len=[94ms, data=mem[128 len floor32([94ms)], mem[(32 * [94ms) + floor32([94ms) + 192 len (32 * [94ms) - floor32([94ms)])


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


# hash = 0x679818a1
# getter = None
# const = None
# payable = False
def unknown679818a1(uint256 _param1, array _param2, array _param3, array _param4): # not payable
  mem[96] = _param2.length
  mem[128 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  mem[(32 * _param2.length) + 128] = _param3.length
  mem[(32 * _param2.length) + 160 len 32 * _param3.length] = call.data[_param3 + 36 len 32 * _param3.length]
  mem[(32 * _param3.length) + (32 * _param2.length) + 160] = _param4.length
  mem[(32 * _param3.length) + (32 * _param2.length) + 192 len 32 * _param4.length] = call.data[_param4 + 36 len 32 * _param4.length]
  if caller == owner:
      require unknownd92cb69a <= 2
      require not unknownd92cb69a
      [94midx = 0
      while [94midx < _param2.length:
          require [94midx < _param2.length
          mem[0] = mem[(32 * [94midx) + 140 len 20]
          mem[32] = 23
          if stor23[mem[(32 * [94midx) + 140 len 20]]:
              require [94midx < _param3.length
              mem[(32 * _param2.length) + (32 * [94midx) + 160] = 0
          else:
              require [94midx < _param2.length
              [94m_351 = mem[(32 * [94midx) + 128]
              require [94midx < _param3.length
              [94m_358 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
              require [94midx < mem[(32 * _param3.length) + (32 * _param2.length) + 160]
              [94m_365 = mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param2.length) + 192]
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = this.address
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000]
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 260] = addr([94m_351)
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 292] = [94m_358
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 324] = [94m_365
              require ext_code.size(unknown2156e6c6['RiskProvider'])
              call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                   gas gas_remaining wei
                  args addr(this.address), unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], addr([94m_351), [94m_358, [94m_365
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require not ext_call.return_data[0]
              require [94midx < _param2.length
              [94m_404 = mem[(32 * [94midx) + 128]
              require [94midx < _param3.length
              [94m_414 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
              mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[32] = 4
              require ext_code.size(mem[(32 * [94midx) + 140 len 20])
              call mem[(32 * [94midx) + 140 len 20].approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000]
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = [94m_414
              require ext_code.size(addr([94m_404))
              call addr([94m_404).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], [94m_414
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          [94midx = [94midx + 1
          continue 
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 292] = this.address
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 324] = _param1
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = 160
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 356] = _param2.length
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 388 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = (32 * _param2.length) + 192
      mem[(64 * _param2.length) + (32 * _param4.length) + (32 * _param3.length) + 388] = _param3.length
      mem[(64 * _param2.length) + (32 * _param4.length) + (32 * _param3.length) + 420 len floor32(_param3.length)] = mem[(32 * _param2.length) + 160 len floor32(_param3.length)]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 260] = (32 * _param3.length) + (32 * _param2.length) + 224
      mem[(64 * _param3.length) + (64 * _param2.length) + (32 * _param4.length) + 420] = mem[(32 * _param3.length) + (32 * _param2.length) + 160]
      mem[(64 * _param3.length) + (64 * _param2.length) + (32 * _param4.length) + 452 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])] = mem[(32 * _param3.length) + (32 * _param2.length) + 192 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])]
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x78265e2f with:
           gas gas_remaining wei
          args mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196 len (32 * mem[(32 * _param3.length) + (32 * _param2.length) + 160]) + (32 * _param3.length) + (32 * _param2.length) + 256]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < _param2.length
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < _param2.length
                  [94m_1373 = mem[(32 * [94midx) + 128]
                  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = this.address
                  require ext_code.size(addr([94m_1373))
                  call addr([94m_1373).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1373)
                  mem[32] = 21
                  amounts[addr([94m_1373)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1373)
                      mem[32] = 22
                      if not stor22[addr([94m_1373)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1373)
                          mem[0] = addr([94m_1373)
                          mem[32] = 22
                          stor22[addr([94m_1373)] = 1
              [94midx = [94midx + 1
              continue 
          return 1
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = _param2.length
      if not _param2.length:
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 4
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228] = 32
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 260] = _param2.length
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 292 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228 len (32 * _param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1376 = mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + (32 * mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1376 + 224]
              if mem[(32 * [94midx) + (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1376 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 23
                  if not stor23[mem[(32 * [94midx) + 140 len 20]]:
                      require [94midx < mem[96]
                      stor23[mem[(32 * [94midx) + 140 len 20]] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 21
                      if amounts[mem[(32 * [94midx) + 140 len 20]] > 0:
                          require [94midx < mem[96]
                          unknown07b08870.length++
                          mem[0] = 24
                          addr(unknown07b08870[unknown07b08870.length].field_0) = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1651 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1651)
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0xce7b5574 with:
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
              continue 
          [94m_1689 = mem[96]
          [94midx = 0
          while [94midx < [94m_1689:
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
                  mem[32] = 21
                  amounts[addr([94m_1705)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1705)
                      mem[32] = 22
                      if not stor22[addr([94m_1705)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1705)
                          mem[0] = addr([94m_1705)
                          mem[32] = 22
                          stor22[addr([94m_1705)] = 1
              [94midx = [94midx + 1
              continue 
      else:
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 224 len 32 * _param2.length] = code.data[24497 len 32 * _param2.length]
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 4
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228] = 32
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 260] = _param2.length
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 292 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228 len (32 * _param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1377 = mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + (32 * mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1377 + 224]
              if mem[(32 * [94midx) + (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1377 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 23
                  if not stor23[mem[(32 * [94midx) + 140 len 20]]:
                      require [94midx < mem[96]
                      stor23[mem[(32 * [94midx) + 140 len 20]] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 21
                      if amounts[mem[(32 * [94midx) + 140 len 20]] > 0:
                          require [94midx < mem[96]
                          unknown07b08870.length++
                          mem[0] = 24
                          addr(unknown07b08870[unknown07b08870.length].field_0) = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1656 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1656)
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0xce7b5574 with:
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
              continue 
          [94m_1690 = mem[96]
          [94midx = 0
          while [94midx < [94m_1690:
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
                  mem[32] = 21
                  amounts[addr([94m_1708)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1708)
                      mem[32] = 22
                      if not stor22[addr([94m_1708)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1708)
                          mem[0] = addr([94m_1708)
                          mem[32] = 22
                          stor22[addr([94m_1708)] = 1
              [94midx = [94midx + 1
              continue 
  else:
      require ext_code.size(unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000])
      call unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000].0x919253e8 with:
           gas gas_remaining wei
          args addr(this.address), 2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = 2
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = caller
      require ext_code.size(unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000])
      call unknown2156e6c6[0xef57686974656c69737450726f76696465720000000000000000000000000000].0x5faa299a with:
           gas gas_remaining wei
          args 2, caller
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      require unknownd92cb69a <= 2
      require not unknownd92cb69a
      [94midx = 0
      while [94midx < _param2.length:
          require [94midx < _param2.length
          mem[0] = mem[(32 * [94midx) + 140 len 20]
          mem[32] = 23
          if stor23[mem[(32 * [94midx) + 140 len 20]]:
              require [94midx < _param3.length
              mem[(32 * _param2.length) + (32 * [94midx) + 160] = 0
          else:
              require [94midx < _param2.length
              [94m_353 = mem[(32 * [94midx) + 128]
              require [94midx < _param3.length
              [94m_363 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
              require [94midx < mem[(32 * _param3.length) + (32 * _param2.length) + 160]
              [94m_366 = mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param2.length) + 192]
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = this.address
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000]
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 260] = addr([94m_353)
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 292] = [94m_363
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 324] = [94m_366
              require ext_code.size(unknown2156e6c6['RiskProvider'])
              call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                   gas gas_remaining wei
                  args addr(this.address), unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], addr([94m_353), [94m_363, [94m_366
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require not ext_call.return_data[0]
              require [94midx < _param2.length
              [94m_407 = mem[(32 * [94midx) + 128]
              require [94midx < _param3.length
              [94m_420 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
              mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[32] = 4
              require ext_code.size(mem[(32 * [94midx) + 140 len 20])
              call mem[(32 * [94midx) + 140 len 20].approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000]
              mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = [94m_420
              require ext_code.size(addr([94m_407))
              call addr([94m_407).approve(address spender, uint256 value) with:
                   gas gas_remaining wei
                  args unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], [94m_420
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          [94midx = [94midx + 1
          continue 
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 292] = this.address
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 324] = _param1
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = 160
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 356] = _param2.length
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 388 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 228] = (32 * _param2.length) + 192
      mem[(64 * _param2.length) + (32 * _param4.length) + (32 * _param3.length) + 388] = _param3.length
      mem[(64 * _param2.length) + (32 * _param4.length) + (32 * _param3.length) + 420 len floor32(_param3.length)] = mem[(32 * _param2.length) + 160 len floor32(_param3.length)]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 260] = (32 * _param3.length) + (32 * _param2.length) + 224
      mem[(64 * _param3.length) + (64 * _param2.length) + (32 * _param4.length) + 420] = mem[(32 * _param3.length) + (32 * _param2.length) + 160]
      mem[(64 * _param3.length) + (64 * _param2.length) + (32 * _param4.length) + 452 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])] = mem[(32 * _param3.length) + (32 * _param2.length) + 192 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])]
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x78265e2f with:
           gas gas_remaining wei
          args mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196 len (32 * mem[(32 * _param3.length) + (32 * _param2.length) + 160]) + (32 * _param3.length) + (32 * _param2.length) + 256]
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < _param2.length
              if mem[(32 * [94midx) + 140 len 20]:
                  require [94midx < _param2.length
                  [94m_1378 = mem[(32 * [94midx) + 128]
                  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 196] = this.address
                  require ext_code.size(addr([94m_1378))
                  call addr([94m_1378).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = addr([94m_1378)
                  mem[32] = 21
                  amounts[addr([94m_1378)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1378)
                      mem[32] = 22
                      if not stor22[addr([94m_1378)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1378)
                          mem[0] = addr([94m_1378)
                          mem[32] = 22
                          stor22[addr([94m_1378)] = 1
              [94midx = [94midx + 1
              continue 
          return 1
      mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = _param2.length
      if not _param2.length:
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 4
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228] = 32
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 260] = _param2.length
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 292 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228 len (32 * _param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1381 = mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + (32 * mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1381 + 224]
              if mem[(32 * [94midx) + (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1381 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 23
                  if not stor23[mem[(32 * [94midx) + 140 len 20]]:
                      require [94midx < mem[96]
                      stor23[mem[(32 * [94midx) + 140 len 20]] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 21
                      if amounts[mem[(32 * [94midx) + 140 len 20]] > 0:
                          require [94midx < mem[96]
                          unknown07b08870.length++
                          mem[0] = 24
                          addr(unknown07b08870[unknown07b08870.length].field_0) = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1661 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1661)
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0xce7b5574 with:
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
              continue 
          [94m_1691 = mem[96]
          [94midx = 0
          while [94midx < [94m_1691:
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
                  mem[32] = 21
                  amounts[addr([94m_1711)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1711)
                      mem[32] = 22
                      if not stor22[addr([94m_1711)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1711)
                          mem[0] = addr([94m_1711)
                          mem[32] = 22
                          stor22[addr([94m_1711)] = 1
              [94midx = [94midx + 1
              continue 
      else:
          mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 224 len 32 * _param2.length] = code.data[24497 len 32 * _param2.length]
          mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
          mem[32] = 4
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224] = 0x674f23ba00000000000000000000000000000000000000000000000000000000
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228] = 32
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 260] = _param2.length
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 292 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x674f23ba with:
               gas gas_remaining wei
              args mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 228 len (32 * _param2.length) + 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len return_data.size] = ext_call.return_data[0 len return_data.size]
          mem[64] = (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + ceil32(return_data.size) + 224
          require return_data.size >= 32
          [94m_1382 = mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 <= 4294967296
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 32 <= return_data.size
          require mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224] <= 4294967296 and mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + (32 * mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + 224 len 4], 0 + 224]) + 32 <= return_data.size
          [94midx = 0
          while [94midx < _param2.length:
              require [94midx < mem[(32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1382 + 224]
              if mem[(32 * [94midx) + (32 * _param4.length) + (32 * _param3.length) + (64 * _param2.length) + [94m_1382 + 256] > 0:
                  require [94midx < mem[96]
                  mem[0] = mem[(32 * [94midx) + 140 len 20]
                  mem[32] = 23
                  if not stor23[mem[(32 * [94midx) + 140 len 20]]:
                      require [94midx < mem[96]
                      stor23[mem[(32 * [94midx) + 140 len 20]] = 1
                      require [94midx < mem[96]
                      mem[0] = mem[(32 * [94midx) + 140 len 20]
                      mem[32] = 21
                      if amounts[mem[(32 * [94midx) + 140 len 20]] > 0:
                          require [94midx < mem[96]
                          unknown07b08870.length++
                          mem[0] = 24
                          addr(unknown07b08870[unknown07b08870.length].field_0) = mem[(32 * [94midx) + 140 len 20]
                          require [94midx < mem[96]
                          [94m_1666 = mem[(32 * [94midx) + 128]
                          mem[mem[64]] = 0xce7b557400000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = addr([94m_1666)
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0xce7b5574 with:
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
              continue 
          [94m_1692 = mem[96]
          [94midx = 0
          while [94midx < [94m_1692:
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
                  mem[32] = 21
                  amounts[addr([94m_1714)] = ext_call.return_data[0]
                  if 0 < ext_call.return_data[0]:
                      mem[0] = addr([94m_1714)
                      mem[32] = 22
                      if not stor22[addr([94m_1714)]:
                          tokens.length++
                          addr(tokens[tokens.length].field_0) = addr([94m_1714)
                          mem[0] = addr([94m_1714)
                          mem[32] = 22
                          stor22[addr([94m_1714)] = 1
              [94midx = [94midx + 1
              continue 
  return 0


# hash = 0x6e947298
# getter = None
# const = None
# payable = False
def getETHBalance(): # not payable
  require accumulatedFee <= eth.balance(this.address)
  return (eth.balance(this.address) - accumulatedFee)


# hash = 0x6f7bc9be
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 20]]]
# const = None
# payable = False
def investors(address _param1): # not payable
  return investors[_param1]


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
# payable = True
def requestWithdraw(uint256 _value) payable: 
  mem[64] = 96
  require not call.value
  require not paused
  if 0 == totalSupply:
      mem[196] = _value
      mem[228] = 10^18
      require ext_code.size(unknown2156e6c6['RiskProvider'])
      call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
           gas gas_remaining wei
          args 0, uint32(caller), addr(this.address), addr(this.address), _value, 10^18
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
      if status != 3:
          unknown36724ef4 = 1
      else:
          [94midx = 0
          while [94midx < tokens.length:
              mem[0] = addr(tokens[[94midx].field_0)
              mem[32] = 23
              if stor23[addr(stor9[[94midx].field_0)]:
                  [94midx = [94midx + 1
                  continue 
              require [94midx < tokens.length
              mem[0] = 9
              require ext_code.size(addr(tokens[[94midx].field_0))
              call addr(tokens[[94midx].field_0).decimals() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[100] = this.address
              require ext_code.size(addr(tokens[[94midx].field_0))
              call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              mem[96] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  continue 
              mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
              mem[164] = 10^ext_call.return_data[0]
              mem[196] = 0
              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                   gas gas_remaining wei
                  args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
              mem[96 len 64] = ext_call.return_data[0 len 64]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 64
              if not ext_call.return_data[0]:
                  [94midx = [94midx + 1
                  continue 
              if not ext_call.return_data[0]:
                  if 10^ext_call.return_data[0]:
                      if 0 / 10^ext_call.return_data[0] >= 0:
                          [94midx = [94midx + 1
                          continue 
              else:
                  if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
                      if 10^ext_call.return_data[0]:
                          if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                              [94midx = [94midx + 1
                              continue 
              revert
          require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].0xc77e7614 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] != _value:
              unknown36724ef4 = 1
          else:
              require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
              call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].freeze() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              if unknown07b08870.length != 0:
                  mem[0] = 0x546f6b656e42726f6b656e0000000000000000000000000000000000000000
                  mem[32] = 4
                  mem[96] = 0x8f99506a00000000000000000000000000000000000000000000000000000000
                  mem[132] = caller
                  mem[100] = 64
                  mem[164] = unknown07b08870.length
                  if not unknown07b08870.length:
                      require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                      call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0x8f99506a with:
                           gas gas_remaining wei
                          args 64, caller, unknown07b08870.length
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
                      mem[64] = ceil32(return_data.size) + 96
                      require return_data.size >= 32
                      [94m_762 = mem[96 len 4], 0
                      require mem[96 len 4], 0 <= 4294967296
                      require mem[96 len 4], 0 + 32 <= return_data.size
                      require mem[mem[96 len 4], 0 + 96] <= 4294967296 and mem[96 len 4], 0 + (32 * mem[mem[96 len 4], 0 + 96]) + 32 <= return_data.size
                      [94midx = 0
                      while [94midx < unknown07b08870.length:
                          stor19.length++
                          mem[0] = 19
                          addr(stor19[stor19.length].field_0) = addr(unknown07b08870[[94midx].field_0)
                          require [94midx < mem[[94m_762 + 96]
                          if 0 == mem[(32 * [94midx) + [94m_762 + 128]:
                              [94midx = [94midx + 1
                              continue 
                          require [94midx < unknown07b08870.length
                          mem[ceil32(return_data.size) + 100] = addr(unknown07b08870[[94midx].field_0)
                          mem[ceil32(return_data.size) + 132] = caller
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].withdraw(address receiver, address token) with:
                               gas gas_remaining wei
                              args addr(unknown07b08870[[94midx].field_0), caller
                          mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require [94midx < unknown07b08870.length
                          mem[0] = 24
                          require [94midx < mem[[94m_762 + 96]
                          [94m_1410 = mem[(32 * [94midx) + [94m_762 + 128]
                          mem[ceil32(return_data.size) + 96] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
                          mem[ceil32(return_data.size) + 100] = caller
                          mem[ceil32(return_data.size) + 132] = [94m_1410
                          require ext_code.size(addr(unknown07b08870[[94midx].field_0))
                          call addr(unknown07b08870[[94midx].field_0).transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args caller, [94m_1410
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[0]:
                              [94midx = [94midx + 1
                              continue 
                          require unknown07b08870.length - 1 < unknown07b08870.length
                          require [94midx < unknown07b08870.length
                          addr(unknown07b08870[[94midx].field_0) = addr(unknown07b08870[unknown07b08870.length].field_0)
                          require unknown07b08870.length - 1 < mem[[94m_762 + 96]
                          require [94midx < mem[[94m_762 + 96]
                          mem[[94m_762 + (32 * [94midx) + 128] = mem[(32 * unknown07b08870.length - 1) + [94m_762 + 128]
                          require unknown07b08870.length - 1 < unknown07b08870.length
                          mem[0] = 24
                          addr(unknown07b08870[unknown07b08870.length].field_0) = 0
                          unknown07b08870.length--
                          if unknown07b08870.length > unknown07b08870.length - 1:
                              mem[0] = 24
                              [94ms = unknown07b08870.length + sha3(24) - 1
                              while sha3(24) + unknown07b08870.length > [94ms:
                                  stor[[94ms] = 0
                                  [94ms = [94ms + 1
                                  continue 
                          [94midx = [94midx
                          continue 
                      if not stor19.length:
                          [94midx = 0
                          while [94midx < stor19.length:
                              require [94midx < stor19.length
                              if mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20]:
                                  require [94midx < stor19.length
                                  [94m_1903 = mem[ceil32(return_data.size) + (32 * [94midx) + 128]
                                  mem[ceil32(return_data.size) + (32 * stor19.length) + 132] = this.address
                                  require ext_code.size(addr([94m_1903))
                                  call addr([94m_1903).balanceOf(address owner) with:
                                       gas gas_remaining wei
                                      args this.address
                                  mem[ceil32(return_data.size) + (32 * stor19.length) + 128] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[0] = addr([94m_1903)
                                  mem[32] = 21
                                  amounts[addr([94m_1903)] = ext_call.return_data[0]
                                  if 0 < ext_call.return_data[0]:
                                      mem[0] = addr([94m_1903)
                                      mem[32] = 22
                                      if not stor22[addr([94m_1903)]:
                                          tokens.length++
                                          addr(tokens[tokens.length].field_0) = addr([94m_1903)
                                          mem[0] = addr([94m_1903)
                                          mem[32] = 22
                                          stor22[addr([94m_1903)] = 1
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[ceil32(return_data.size) + 128] = addr(stor19.field_0)
                          [94midx = ceil32(return_data.size) + 128
                          [94ms = 0
                          while ceil32(return_data.size) + (32 * stor19.length) + 96 > [94midx:
                              mem[[94midx + 32] = addr(stor19[[94ms].field_256)
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              continue 
                          [94midx = 0
                          while [94midx < stor19.length:
                              require [94midx < stor19.length
                              if mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20]:
                                  require [94midx < stor19.length
                                  [94m_2949 = mem[ceil32(return_data.size) + (32 * [94midx) + 128]
                                  mem[ceil32(return_data.size) + (32 * stor19.length) + 132] = this.address
                                  require ext_code.size(addr([94m_2949))
                                  call addr([94m_2949).balanceOf(address owner) with:
                                       gas gas_remaining wei
                                      args this.address
                                  mem[ceil32(return_data.size) + (32 * stor19.length) + 128] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[0] = addr([94m_2949)
                                  mem[32] = 21
                                  amounts[addr([94m_2949)] = ext_call.return_data[0]
                                  if 0 < ext_call.return_data[0]:
                                      mem[0] = addr([94m_2949)
                                      mem[32] = 22
                                      if not stor22[addr([94m_2949)]:
                                          tokens.length++
                                          addr(tokens[tokens.length].field_0) = addr([94m_2949)
                                          mem[0] = addr([94m_2949)
                                          mem[32] = 22
                                          stor22[addr([94m_2949)] = 1
                              [94midx = [94midx + 1
                              continue 
                  else:
                      mem[0] = 24
                      mem[196] = addr(unknown07b08870.field_0)
                      [94midx = mem[64] + 100
                      [94ms = 0
                      while mem[64] + (32 * unknown07b08870.length) + 100 > [94midx + 32:
                          mem[[94midx + 32] = addr(unknown07b08870[[94ms].field_256)
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          continue 
                      require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                      call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].mem[mem[64] len 4] with:
                           gas gas_remaining wei
                          args mem[mem[64] + 4 len (32 * unknown07b08870.length) + -mem[64] + 192]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      [94m_1891 = mem[64]
                      mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                      mem[64] = mem[64] + ceil32(return_data.size)
                      require return_data.size >= 32
                      [94m_1895 = mem[[94m_1891]
                      require mem[[94m_1891] <= 4294967296
                      require mem[[94m_1891] + 32 <= return_data.size
                      require mem[[94m_1891 + mem[[94m_1891]] <= 4294967296 and mem[[94m_1891] + (32 * mem[[94m_1891 + mem[[94m_1891]]) + 32 <= return_data.size
                      [94midx = 0
                      while [94midx < unknown07b08870.length:
                          stor19.length++
                          mem[0] = 19
                          addr(stor19[stor19.length].field_0) = addr(unknown07b08870[[94midx].field_0)
                          require [94midx < mem[[94m_1891 + [94m_1895]
                          if 0 == mem[(32 * [94midx) + [94m_1891 + [94m_1895 + 32]:
                              [94midx = [94midx + 1
                              continue 
                          require [94midx < unknown07b08870.length
                          mem[mem[64] + 4] = addr(unknown07b08870[[94midx].field_0)
                          mem[mem[64] + 36] = caller
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].withdraw(address receiver, address token) with:
                               gas gas_remaining wei
                              args addr(unknown07b08870[[94midx].field_0), caller
                          mem[mem[64]] = ext_call.return_data[0]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require [94midx < unknown07b08870.length
                          mem[0] = 24
                          require [94midx < mem[[94m_1891 + [94m_1895]
                          [94m_2380 = mem[(32 * [94midx) + [94m_1891 + [94m_1895 + 32]
                          mem[mem[64]] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
                          mem[mem[64] + 4] = caller
                          mem[mem[64] + 36] = [94m_2380
                          require ext_code.size(addr(unknown07b08870[[94midx].field_0))
                          call addr(unknown07b08870[[94midx].field_0).transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args caller, [94m_2380
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data[0]:
                              [94midx = [94midx + 1
                              continue 
                          require unknown07b08870.length - 1 < unknown07b08870.length
                          require [94midx < unknown07b08870.length
                          mem[0] = 24
                          addr(unknown07b08870[[94midx].field_0) = addr(unknown07b08870[unknown07b08870.length].field_0)
                          require unknown07b08870.length - 1 < mem[[94m_1891 + [94m_1895]
                          require [94midx < mem[[94m_1891 + [94m_1895]
                          mem[[94m_1891 + [94m_1895 + (32 * [94midx) + 32] = mem[(32 * unknown07b08870.length - 1) + [94m_1891 + [94m_1895 + 32]
                          require unknown07b08870.length - 1 < unknown07b08870.length
                          mem[0] = 24
                          addr(unknown07b08870[unknown07b08870.length].field_0) = 0
                          unknown07b08870.length--
                          if unknown07b08870.length > unknown07b08870.length - 1:
                              mem[0] = 24
                              [94ms = unknown07b08870.length + sha3(24) - 1
                              while sha3(24) + unknown07b08870.length > [94ms:
                                  stor[[94ms] = 0
                                  [94ms = [94ms + 1
                                  continue 
                          [94midx = [94midx
                          continue 
                      [94m_2300 = mem[64]
                      mem[64] = mem[64] + (32 * stor19.length) + 32
                      mem[[94m_2300] = stor19.length
                      if not stor19.length:
                          [94midx = 0
                          while [94midx < stor19.length:
                              require [94midx < mem[[94m_2300]
                              if mem[(32 * [94midx) + [94m_2300 + 44 len 20]:
                                  require [94midx < mem[[94m_2300]
                                  [94m_2953 = mem[[94m_2300 + (32 * [94midx) + 32]
                                  mem[mem[64] + 4] = this.address
                                  require ext_code.size(addr([94m_2953))
                                  call addr([94m_2953).balanceOf(address owner) with:
                                       gas gas_remaining wei
                                      args this.address
                                  mem[mem[64]] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[0] = addr([94m_2953)
                                  mem[32] = 21
                                  amounts[addr([94m_2953)] = ext_call.return_data[0]
                                  if 0 < ext_call.return_data[0]:
                                      mem[0] = addr([94m_2953)
                                      mem[32] = 22
                                      if not stor22[addr([94m_2953)]:
                                          tokens.length++
                                          addr(tokens[tokens.length].field_0) = addr([94m_2953)
                                          mem[0] = addr([94m_2953)
                                          mem[32] = 22
                                          stor22[addr([94m_2953)] = 1
                              [94midx = [94midx + 1
                              continue 
                      else:
                          mem[0] = 19
                          mem[[94m_2300 + 32] = addr(stor19.field_0)
                          [94midx = [94m_2300 + 32
                          [94ms = 0
                          while [94m_2300 + (32 * stor19.length) > [94midx:
                              mem[[94midx + 32] = addr(stor19[[94ms].field_256)
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              continue 
                          [94midx = 0
                          while [94midx < stor19.length:
                              require [94midx < mem[[94m_2300]
                              if mem[(32 * [94midx) + [94m_2300 + 44 len 20]:
                                  require [94midx < mem[[94m_2300]
                                  [94m_4163 = mem[[94m_2300 + (32 * [94midx) + 32]
                                  mem[mem[64] + 4] = this.address
                                  require ext_code.size(addr([94m_4163))
                                  call addr([94m_4163).balanceOf(address owner) with:
                                       gas gas_remaining wei
                                      args this.address
                                  mem[mem[64]] = ext_call.return_data[0]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 32
                                  mem[0] = addr([94m_4163)
                                  mem[32] = 21
                                  amounts[addr([94m_4163)] = ext_call.return_data[0]
                                  if 0 < ext_call.return_data[0]:
                                      mem[0] = addr([94m_4163)
                                      mem[32] = 22
                                      if not stor22[addr([94m_4163)]:
                                          tokens.length++
                                          addr(tokens[tokens.length].field_0) = addr([94m_4163)
                                          mem[0] = addr([94m_4163)
                                          mem[32] = 22
                                          stor22[addr([94m_4163)] = 1
                              [94midx = [94midx + 1
                              continue 
                  stor19.length = 0
                  [94midx = 0
                  while stor19.length > [94midx:
                      stor19[[94midx].field_0 = 0
                      [94midx = [94midx + 1
                      continue 
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
                  require ext_call.return_data[32] <= totalSupply
                  totalSupply -= ext_call.return_data[32]
                  log Transfer(
                        address from=ext_call.return_data[32],
                        address to=caller,
                        uint256 value=0)
                  if ext_call.return_data[0] > 0:
                      call caller with:
                         value ext_call.return_data[0] wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  if balanceOf[caller] <= 0:
                      require unknown81d62bf5.length - 1 < unknown81d62bf5.length
                      require unknown1c2a0e5c[caller] - 1 < unknown81d62bf5.length
                      addr(unknown81d62bf5[stor26[caller]].field_0) = addr(unknown81d62bf5[unknown81d62bf5.length].field_0)
                      require unknown81d62bf5.length - 1 < unknown81d62bf5.length
                      unknown1c2a0e5c[addr(stor27[stor27.length].field_0)] = unknown1c2a0e5c[caller]
                      unknown81d62bf5.length--
                      if unknown81d62bf5.length > unknown81d62bf5.length - 1:
                          [94midx = unknown81d62bf5.length - 1
                          while unknown81d62bf5.length > [94midx:
                              unknown81d62bf5[[94midx].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                      unknown1c2a0e5c[caller] = 0
              require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
              call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].finalize() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
  else:
      require accumulatedFee <= eth.balance(this.address)
      [94midx = 0
      while [94midx < tokens.length:
          mem[0] = addr(tokens[[94midx].field_0)
          mem[32] = 23
          if stor23[addr(stor9[[94midx].field_0)]:
              [94midx = [94midx + 1
              continue 
          require [94midx < tokens.length
          mem[0] = 9
          require ext_code.size(addr(tokens[[94midx].field_0))
          call addr(tokens[[94midx].field_0).decimals() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[100] = this.address
          require ext_code.size(addr(tokens[[94midx].field_0))
          call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
               gas gas_remaining wei
              args this.address
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              continue 
          mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
          mem[164] = 10^ext_call.return_data[0]
          mem[196] = 0
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
          mem[96 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              continue 
          if not ext_call.return_data[0]:
              if 10^ext_call.return_data[0]:
                  if 0 / 10^ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      continue 
          else:
              if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
                  if 10^ext_call.return_data[0]:
                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                          [94midx = [94midx + 1
                          continue 
          revert
      require eth.balance(this.address) - accumulatedFee >= 0
      if not eth.balance(this.address) - accumulatedFee:
          require totalSupply
          mem[196] = _value
          mem[228] = 0 / totalSupply
          require ext_code.size(unknown2156e6c6['RiskProvider'])
          call unknown2156e6c6['RiskProvider'].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
               gas gas_remaining wei
              args caller, addr(this.address), addr(this.address), _value, 0 / totalSupply
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
          if status != 3:
              unknown36724ef4 = 1
          else:
              [94midx = 0
              while [94midx < tokens.length:
                  mem[0] = addr(tokens[[94midx].field_0)
                  mem[32] = 23
                  if stor23[addr(stor9[[94midx].field_0)]:
                      [94midx = [94midx + 1
                      continue 
                  require [94midx < tokens.length
                  mem[0] = 9
                  require ext_code.size(addr(tokens[[94midx].field_0))
                  call addr(tokens[[94midx].field_0).decimals() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[100] = this.address
                  require ext_code.size(addr(tokens[[94midx].field_0))
                  call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[96] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      continue 
                  mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[164] = 10^ext_call.return_data[0]
                  mem[196] = 0
                  require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                  call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
                  mem[96 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      continue 
                  if not ext_call.return_data[0]:
                      if 10^ext_call.return_data[0]:
                          if 0 / 10^ext_call.return_data[0] >= 0:
                              [94midx = [94midx + 1
                              continue 
                  else:
                      if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
                          if 10^ext_call.return_data[0]:
                              if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                                  [94midx = [94midx + 1
                                  continue 
                  revert
              require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
              call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].0xc77e7614 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] != _value:
                  unknown36724ef4 = 1
              else:
                  require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
                  call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].freeze() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if unknown07b08870.length != 0:
                      mem[0] = 0x546f6b656e42726f6b656e0000000000000000000000000000000000000000
                      mem[32] = 4
                      mem[96] = 0x8f99506a00000000000000000000000000000000000000000000000000000000
                      mem[132] = caller
                      mem[100] = 64
                      mem[164] = unknown07b08870.length
                      if not unknown07b08870.length:
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0x8f99506a with:
                               gas gas_remaining wei
                              args 64, caller, unknown07b08870.length
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = ceil32(return_data.size) + 96
                          require return_data.size >= 32
                          [94m_1499 = mem[96 len 4], 0
                          require mem[96 len 4], 0 <= 4294967296
                          require mem[96 len 4], 0 + 32 <= return_data.size
                          require mem[mem[96 len 4], 0 + 96] <= 4294967296 and mem[96 len 4], 0 + (32 * mem[mem[96 len 4], 0 + 96]) + 32 <= return_data.size
                          [94midx = 0
                          while [94midx < unknown07b08870.length:
                              stor19.length++
                              mem[0] = 19
                              addr(stor19[stor19.length].field_0) = addr(unknown07b08870[[94midx].field_0)
                              require [94midx < mem[[94m_1499 + 96]
                              if 0 == mem[(32 * [94midx) + [94m_1499 + 128]:
                                  [94midx = [94midx + 1
                                  continue 
                              require [94midx < unknown07b08870.length
                              mem[ceil32(return_data.size) + 100] = addr(unknown07b08870[[94midx].field_0)
                              mem[ceil32(return_data.size) + 132] = caller
                              require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                              call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].withdraw(address receiver, address token) with:
                                   gas gas_remaining wei
                                  args addr(unknown07b08870[[94midx].field_0), caller
                              mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require [94midx < unknown07b08870.length
                              mem[0] = 24
                              require [94midx < mem[[94m_1499 + 96]
                              [94m_1959 = mem[(32 * [94midx) + [94m_1499 + 128]
                              mem[ceil32(return_data.size) + 96] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
                              mem[ceil32(return_data.size) + 100] = caller
                              mem[ceil32(return_data.size) + 132] = [94m_1959
                              require ext_code.size(addr(unknown07b08870[[94midx].field_0))
                              call addr(unknown07b08870[[94midx].field_0).transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args caller, [94m_1959
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  continue 
                              require unknown07b08870.length - 1 < unknown07b08870.length
                              require [94midx < unknown07b08870.length
                              addr(unknown07b08870[[94midx].field_0) = addr(unknown07b08870[unknown07b08870.length].field_0)
                              require unknown07b08870.length - 1 < mem[[94m_1499 + 96]
                              require [94midx < mem[[94m_1499 + 96]
                              mem[[94m_1499 + (32 * [94midx) + 128] = mem[(32 * unknown07b08870.length - 1) + [94m_1499 + 128]
                              require unknown07b08870.length - 1 < unknown07b08870.length
                              mem[0] = 24
                              addr(unknown07b08870[unknown07b08870.length].field_0) = 0
                              unknown07b08870.length--
                              if unknown07b08870.length > unknown07b08870.length - 1:
                                  mem[0] = 24
                                  [94ms = unknown07b08870.length + sha3(24) - 1
                                  while sha3(24) + unknown07b08870.length > [94ms:
                                      stor[[94ms] = 0
                                      [94ms = [94ms + 1
                                      continue 
                              [94midx = [94midx
                              continue 
                          if not stor19.length:
                              [94midx = 0
                              while [94midx < stor19.length:
                                  require [94midx < stor19.length
                                  if mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20]:
                                      require [94midx < stor19.length
                                      [94m_2321 = mem[ceil32(return_data.size) + (32 * [94midx) + 128]
                                      mem[ceil32(return_data.size) + (32 * stor19.length) + 132] = this.address
                                      require ext_code.size(addr([94m_2321))
                                      call addr([94m_2321).balanceOf(address owner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      mem[ceil32(return_data.size) + (32 * stor19.length) + 128] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[0] = addr([94m_2321)
                                      mem[32] = 21
                                      amounts[addr([94m_2321)] = ext_call.return_data[0]
                                      if 0 < ext_call.return_data[0]:
                                          mem[0] = addr([94m_2321)
                                          mem[32] = 22
                                          if not stor22[addr([94m_2321)]:
                                              tokens.length++
                                              addr(tokens[tokens.length].field_0) = addr([94m_2321)
                                              mem[0] = addr([94m_2321)
                                              mem[32] = 22
                                              stor22[addr([94m_2321)] = 1
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[ceil32(return_data.size) + 128] = addr(stor19.field_0)
                              [94midx = ceil32(return_data.size) + 128
                              [94ms = 0
                              while ceil32(return_data.size) + (32 * stor19.length) + 96 > [94midx:
                                  mem[[94midx + 32] = addr(stor19[[94ms].field_256)
                                  [94midx = [94midx + 32
                                  [94ms = [94ms + 1
                                  continue 
                              [94midx = 0
                              while [94midx < stor19.length:
                                  require [94midx < stor19.length
                                  if mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20]:
                                      require [94midx < stor19.length
                                      [94m_3621 = mem[ceil32(return_data.size) + (32 * [94midx) + 128]
                                      mem[ceil32(return_data.size) + (32 * stor19.length) + 132] = this.address
                                      require ext_code.size(addr([94m_3621))
                                      call addr([94m_3621).balanceOf(address owner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      mem[ceil32(return_data.size) + (32 * stor19.length) + 128] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[0] = addr([94m_3621)
                                      mem[32] = 21
                                      amounts[addr([94m_3621)] = ext_call.return_data[0]
                                      if 0 < ext_call.return_data[0]:
                                          mem[0] = addr([94m_3621)
                                          mem[32] = 22
                                          if not stor22[addr([94m_3621)]:
                                              tokens.length++
                                              addr(tokens[tokens.length].field_0) = addr([94m_3621)
                                              mem[0] = addr([94m_3621)
                                              mem[32] = 22
                                              stor22[addr([94m_3621)] = 1
                                  [94midx = [94midx + 1
                                  continue 
                      else:
                          mem[0] = 24
                          mem[196] = addr(unknown07b08870.field_0)
                          [94midx = mem[64] + 100
                          [94ms = 0
                          while mem[64] + (32 * unknown07b08870.length) + 100 > [94midx + 32:
                              mem[[94midx + 32] = addr(unknown07b08870[[94ms].field_256)
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              continue 
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].mem[mem[64] len 4] with:
                               gas gas_remaining wei
                              args mem[mem[64] + 4 len (32 * unknown07b08870.length) + -mem[64] + 192]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_2304 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          [94m_2313 = mem[[94m_2304]
                          require mem[[94m_2304] <= 4294967296
                          require mem[[94m_2304] + 32 <= return_data.size
                          require mem[[94m_2304 + mem[[94m_2304]] <= 4294967296 and mem[[94m_2304] + (32 * mem[[94m_2304 + mem[[94m_2304]]) + 32 <= return_data.size
                          [94midx = 0
                          while [94midx < unknown07b08870.length:
                              stor19.length++
                              mem[0] = 19
                              addr(stor19[stor19.length].field_0) = addr(unknown07b08870[[94midx].field_0)
                              require [94midx < mem[[94m_2304 + [94m_2313]
                              if 0 == mem[(32 * [94midx) + [94m_2304 + [94m_2313 + 32]:
                                  [94midx = [94midx + 1
                                  continue 
                              require [94midx < unknown07b08870.length
                              mem[mem[64] + 4] = addr(unknown07b08870[[94midx].field_0)
                              mem[mem[64] + 36] = caller
                              require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                              call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].withdraw(address receiver, address token) with:
                                   gas gas_remaining wei
                                  args addr(unknown07b08870[[94midx].field_0), caller
                              mem[mem[64]] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require [94midx < unknown07b08870.length
                              mem[0] = 24
                              require [94midx < mem[[94m_2304 + [94m_2313]
                              [94m_3031 = mem[(32 * [94midx) + [94m_2304 + [94m_2313 + 32]
                              mem[mem[64]] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
                              mem[mem[64] + 4] = caller
                              mem[mem[64] + 36] = [94m_3031
                              require ext_code.size(addr(unknown07b08870[[94midx].field_0))
                              call addr(unknown07b08870[[94midx].field_0).transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args caller, [94m_3031
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  continue 
                              require unknown07b08870.length - 1 < unknown07b08870.length
                              require [94midx < unknown07b08870.length
                              mem[0] = 24
                              addr(unknown07b08870[[94midx].field_0) = addr(unknown07b08870[unknown07b08870.length].field_0)
                              require unknown07b08870.length - 1 < mem[[94m_2304 + [94m_2313]
                              require [94midx < mem[[94m_2304 + [94m_2313]
                              mem[[94m_2304 + [94m_2313 + (32 * [94midx) + 32] = mem[(32 * unknown07b08870.length - 1) + [94m_2304 + [94m_2313 + 32]
                              require unknown07b08870.length - 1 < unknown07b08870.length
                              mem[0] = 24
                              addr(unknown07b08870[unknown07b08870.length].field_0) = 0
                              unknown07b08870.length--
                              if unknown07b08870.length > unknown07b08870.length - 1:
                                  mem[0] = 24
                                  [94ms = unknown07b08870.length + sha3(24) - 1
                                  while sha3(24) + unknown07b08870.length > [94ms:
                                      stor[[94ms] = 0
                                      [94ms = [94ms + 1
                                      continue 
                              [94midx = [94midx
                              continue 
                          [94m_2921 = mem[64]
                          mem[64] = mem[64] + (32 * stor19.length) + 32
                          mem[[94m_2921] = stor19.length
                          if not stor19.length:
                              [94midx = 0
                              while [94midx < stor19.length:
                                  require [94midx < mem[[94m_2921]
                                  if mem[(32 * [94midx) + [94m_2921 + 44 len 20]:
                                      require [94midx < mem[[94m_2921]
                                      [94m_3625 = mem[[94m_2921 + (32 * [94midx) + 32]
                                      mem[mem[64] + 4] = this.address
                                      require ext_code.size(addr([94m_3625))
                                      call addr([94m_3625).balanceOf(address owner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      mem[mem[64]] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[0] = addr([94m_3625)
                                      mem[32] = 21
                                      amounts[addr([94m_3625)] = ext_call.return_data[0]
                                      if 0 < ext_call.return_data[0]:
                                          mem[0] = addr([94m_3625)
                                          mem[32] = 22
                                          if not stor22[addr([94m_3625)]:
                                              tokens.length++
                                              addr(tokens[tokens.length].field_0) = addr([94m_3625)
                                              mem[0] = addr([94m_3625)
                                              mem[32] = 22
                                              stor22[addr([94m_3625)] = 1
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = 19
                              mem[[94m_2921 + 32] = addr(stor19.field_0)
                              [94midx = [94m_2921 + 32
                              [94ms = 0
                              while [94m_2921 + (32 * stor19.length) > [94midx:
                                  mem[[94midx + 32] = addr(stor19[[94ms].field_256)
                                  [94midx = [94midx + 32
                                  [94ms = [94ms + 1
                                  continue 
                              [94midx = 0
                              while [94midx < stor19.length:
                                  require [94midx < mem[[94m_2921]
                                  if mem[(32 * [94midx) + [94m_2921 + 44 len 20]:
                                      require [94midx < mem[[94m_2921]
                                      [94m_4701 = mem[[94m_2921 + (32 * [94midx) + 32]
                                      mem[mem[64] + 4] = this.address
                                      require ext_code.size(addr([94m_4701))
                                      call addr([94m_4701).balanceOf(address owner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      mem[mem[64]] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[0] = addr([94m_4701)
                                      mem[32] = 21
                                      amounts[addr([94m_4701)] = ext_call.return_data[0]
                                      if 0 < ext_call.return_data[0]:
                                          mem[0] = addr([94m_4701)
                                          mem[32] = 22
                                          if not stor22[addr([94m_4701)]:
                                              tokens.length++
                                              addr(tokens[tokens.length].field_0) = addr([94m_4701)
                                              mem[0] = addr([94m_4701)
                                              mem[32] = 22
                                              stor22[addr([94m_4701)] = 1
                                  [94midx = [94midx + 1
                                  continue 
                      stor19.length = 0
                      [94midx = 0
                      while stor19.length > [94midx:
                          stor19[[94midx].field_0 = 0
                          [94midx = [94midx + 1
                          continue 
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
                      require ext_call.return_data[32] <= totalSupply
                      totalSupply -= ext_call.return_data[32]
                      log Transfer(
                            address from=ext_call.return_data[32],
                            address to=caller,
                            uint256 value=0)
                      if ext_call.return_data[0] > 0:
                          call caller with:
                             value ext_call.return_data[0] wei
                               gas 2300 * is_zero(value) wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                      if balanceOf[caller] <= 0:
                          require unknown81d62bf5.length - 1 < unknown81d62bf5.length
                          require unknown1c2a0e5c[caller] - 1 < unknown81d62bf5.length
                          addr(unknown81d62bf5[stor26[caller]].field_0) = addr(unknown81d62bf5[unknown81d62bf5.length].field_0)
                          require unknown81d62bf5.length - 1 < unknown81d62bf5.length
                          unknown1c2a0e5c[addr(stor27[stor27.length].field_0)] = unknown1c2a0e5c[caller]
                          unknown81d62bf5.length--
                          if unknown81d62bf5.length > unknown81d62bf5.length - 1:
                              [94midx = unknown81d62bf5.length - 1
                              while unknown81d62bf5.length > [94midx:
                                  unknown81d62bf5[[94midx].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                          unknown1c2a0e5c[caller] = 0
                  require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
                  call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].finalize() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
      else:
          require (eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / eth.balance(this.address) - accumulatedFee == 10^decimals
          require totalSupply
          mem[196] = _value
          mem[228] = (eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply
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
          if status != 3:
              unknown36724ef4 = 1
          else:
              [94midx = 0
              while [94midx < tokens.length:
                  mem[0] = addr(tokens[[94midx].field_0)
                  mem[32] = 23
                  if stor23[addr(stor9[[94midx].field_0)]:
                      [94midx = [94midx + 1
                      continue 
                  require [94midx < tokens.length
                  mem[0] = 9
                  require ext_code.size(addr(tokens[[94midx].field_0))
                  call addr(tokens[[94midx].field_0).decimals() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[100] = this.address
                  require ext_code.size(addr(tokens[[94midx].field_0))
                  call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[96] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      continue 
                  mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[164] = 10^ext_call.return_data[0]
                  mem[196] = 0
                  require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                  call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
                  mem[96 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  if not ext_call.return_data[0]:
                      [94midx = [94midx + 1
                      continue 
                  if not ext_call.return_data[0]:
                      if 10^ext_call.return_data[0]:
                          if 0 / 10^ext_call.return_data[0] >= 0:
                              [94midx = [94midx + 1
                              continue 
                  else:
                      if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
                          if 10^ext_call.return_data[0]:
                              if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                                  [94midx = [94midx + 1
                                  continue 
                  revert
              require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
              call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].0xc77e7614 with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] != _value:
                  unknown36724ef4 = 1
              else:
                  require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
                  call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].freeze() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if unknown07b08870.length != 0:
                      mem[0] = 0x546f6b656e42726f6b656e0000000000000000000000000000000000000000
                      mem[32] = 4
                      mem[96] = 0x8f99506a00000000000000000000000000000000000000000000000000000000
                      mem[132] = caller
                      mem[100] = 64
                      mem[164] = unknown07b08870.length
                      if not unknown07b08870.length:
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].0x8f99506a with:
                               gas gas_remaining wei
                              args 64, caller, unknown07b08870.length
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = ceil32(return_data.size) + 96
                          require return_data.size >= 32
                          [94m_1498 = mem[96 len 4], 0
                          require mem[96 len 4], 0 <= 4294967296
                          require mem[96 len 4], 0 + 32 <= return_data.size
                          require mem[mem[96 len 4], 0 + 96] <= 4294967296 and mem[96 len 4], 0 + (32 * mem[mem[96 len 4], 0 + 96]) + 32 <= return_data.size
                          [94midx = 0
                          while [94midx < unknown07b08870.length:
                              stor19.length++
                              mem[0] = 19
                              addr(stor19[stor19.length].field_0) = addr(unknown07b08870[[94midx].field_0)
                              require [94midx < mem[[94m_1498 + 96]
                              if 0 == mem[(32 * [94midx) + [94m_1498 + 128]:
                                  [94midx = [94midx + 1
                                  continue 
                              require [94midx < unknown07b08870.length
                              mem[ceil32(return_data.size) + 100] = addr(unknown07b08870[[94midx].field_0)
                              mem[ceil32(return_data.size) + 132] = caller
                              require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                              call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].withdraw(address receiver, address token) with:
                                   gas gas_remaining wei
                                  args addr(unknown07b08870[[94midx].field_0), caller
                              mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require [94midx < unknown07b08870.length
                              mem[0] = 24
                              require [94midx < mem[[94m_1498 + 96]
                              [94m_1957 = mem[(32 * [94midx) + [94m_1498 + 128]
                              mem[ceil32(return_data.size) + 96] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
                              mem[ceil32(return_data.size) + 100] = caller
                              mem[ceil32(return_data.size) + 132] = [94m_1957
                              require ext_code.size(addr(unknown07b08870[[94midx].field_0))
                              call addr(unknown07b08870[[94midx].field_0).transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args caller, [94m_1957
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  continue 
                              require unknown07b08870.length - 1 < unknown07b08870.length
                              require [94midx < unknown07b08870.length
                              addr(unknown07b08870[[94midx].field_0) = addr(unknown07b08870[unknown07b08870.length].field_0)
                              require unknown07b08870.length - 1 < mem[[94m_1498 + 96]
                              require [94midx < mem[[94m_1498 + 96]
                              mem[[94m_1498 + (32 * [94midx) + 128] = mem[(32 * unknown07b08870.length - 1) + [94m_1498 + 128]
                              require unknown07b08870.length - 1 < unknown07b08870.length
                              mem[0] = 24
                              addr(unknown07b08870[unknown07b08870.length].field_0) = 0
                              unknown07b08870.length--
                              if unknown07b08870.length > unknown07b08870.length - 1:
                                  mem[0] = 24
                                  [94ms = unknown07b08870.length + sha3(24) - 1
                                  while sha3(24) + unknown07b08870.length > [94ms:
                                      stor[[94ms] = 0
                                      [94ms = [94ms + 1
                                      continue 
                              [94midx = [94midx
                              continue 
                          if not stor19.length:
                              [94midx = 0
                              while [94midx < stor19.length:
                                  require [94midx < stor19.length
                                  if mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20]:
                                      require [94midx < stor19.length
                                      [94m_2317 = mem[ceil32(return_data.size) + (32 * [94midx) + 128]
                                      mem[ceil32(return_data.size) + (32 * stor19.length) + 132] = this.address
                                      require ext_code.size(addr([94m_2317))
                                      call addr([94m_2317).balanceOf(address owner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      mem[ceil32(return_data.size) + (32 * stor19.length) + 128] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[0] = addr([94m_2317)
                                      mem[32] = 21
                                      amounts[addr([94m_2317)] = ext_call.return_data[0]
                                      if 0 < ext_call.return_data[0]:
                                          mem[0] = addr([94m_2317)
                                          mem[32] = 22
                                          if not stor22[addr([94m_2317)]:
                                              tokens.length++
                                              addr(tokens[tokens.length].field_0) = addr([94m_2317)
                                              mem[0] = addr([94m_2317)
                                              mem[32] = 22
                                              stor22[addr([94m_2317)] = 1
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[ceil32(return_data.size) + 128] = addr(stor19.field_0)
                              [94midx = ceil32(return_data.size) + 128
                              [94ms = 0
                              while ceil32(return_data.size) + (32 * stor19.length) + 96 > [94midx:
                                  mem[[94midx + 32] = addr(stor19[[94ms].field_256)
                                  [94midx = [94midx + 32
                                  [94ms = [94ms + 1
                                  continue 
                              [94midx = 0
                              while [94midx < stor19.length:
                                  require [94midx < stor19.length
                                  if mem[(32 * [94midx) + ceil32(return_data.size) + 140 len 20]:
                                      require [94midx < stor19.length
                                      [94m_3611 = mem[ceil32(return_data.size) + (32 * [94midx) + 128]
                                      mem[ceil32(return_data.size) + (32 * stor19.length) + 132] = this.address
                                      require ext_code.size(addr([94m_3611))
                                      call addr([94m_3611).balanceOf(address owner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      mem[ceil32(return_data.size) + (32 * stor19.length) + 128] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[0] = addr([94m_3611)
                                      mem[32] = 21
                                      amounts[addr([94m_3611)] = ext_call.return_data[0]
                                      if 0 < ext_call.return_data[0]:
                                          mem[0] = addr([94m_3611)
                                          mem[32] = 22
                                          if not stor22[addr([94m_3611)]:
                                              tokens.length++
                                              addr(tokens[tokens.length].field_0) = addr([94m_3611)
                                              mem[0] = addr([94m_3611)
                                              mem[32] = 22
                                              stor22[addr([94m_3611)] = 1
                                  [94midx = [94midx + 1
                                  continue 
                      else:
                          mem[0] = 24
                          mem[196] = addr(unknown07b08870.field_0)
                          [94midx = mem[64] + 100
                          [94ms = 0
                          while mem[64] + (32 * unknown07b08870.length) + 100 > [94midx + 32:
                              mem[[94midx + 32] = addr(unknown07b08870[[94ms].field_256)
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              continue 
                          require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                          call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].mem[mem[64] len 4] with:
                               gas gas_remaining wei
                              args mem[mem[64] + 4 len (32 * unknown07b08870.length) + -mem[64] + 192]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          [94m_2302 = mem[64]
                          mem[mem[64] len return_data.size] = ext_call.return_data[0 len return_data.size]
                          mem[64] = mem[64] + ceil32(return_data.size)
                          require return_data.size >= 32
                          [94m_2311 = mem[[94m_2302]
                          require mem[[94m_2302] <= 4294967296
                          require mem[[94m_2302] + 32 <= return_data.size
                          require mem[[94m_2302 + mem[[94m_2302]] <= 4294967296 and mem[[94m_2302] + (32 * mem[[94m_2302 + mem[[94m_2302]]) + 32 <= return_data.size
                          [94midx = 0
                          while [94midx < unknown07b08870.length:
                              stor19.length++
                              mem[0] = 19
                              addr(stor19[stor19.length].field_0) = addr(unknown07b08870[[94midx].field_0)
                              require [94midx < mem[[94m_2302 + [94m_2311]
                              if 0 == mem[(32 * [94midx) + [94m_2302 + [94m_2311 + 32]:
                                  [94midx = [94midx + 1
                                  continue 
                              require [94midx < unknown07b08870.length
                              mem[mem[64] + 4] = addr(unknown07b08870[[94midx].field_0)
                              mem[mem[64] + 36] = caller
                              require ext_code.size(unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000])
                              call unknown2156e6c6[0x546f6b656e42726f6b656e0000000000000000000000000000000000000000].withdraw(address receiver, address token) with:
                                   gas gas_remaining wei
                                  args addr(unknown07b08870[[94midx].field_0), caller
                              mem[mem[64]] = ext_call.return_data[0]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 32
                              require [94midx < unknown07b08870.length
                              mem[0] = 24
                              require [94midx < mem[[94m_2302 + [94m_2311]
                              [94m_3027 = mem[(32 * [94midx) + [94m_2302 + [94m_2311 + 32]
                              mem[mem[64]] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
                              mem[mem[64] + 4] = caller
                              mem[mem[64] + 36] = [94m_3027
                              require ext_code.size(addr(unknown07b08870[[94midx].field_0))
                              call addr(unknown07b08870[[94midx].field_0).transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args caller, [94m_3027
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              if ext_call.return_data[0]:
                                  [94midx = [94midx + 1
                                  continue 
                              require unknown07b08870.length - 1 < unknown07b08870.length
                              require [94midx < unknown07b08870.length
                              mem[0] = 24
                              addr(unknown07b08870[[94midx].field_0) = addr(unknown07b08870[unknown07b08870.length].field_0)
                              require unknown07b08870.length - 1 < mem[[94m_2302 + [94m_2311]
                              require [94midx < mem[[94m_2302 + [94m_2311]
                              mem[[94m_2302 + [94m_2311 + (32 * [94midx) + 32] = mem[(32 * unknown07b08870.length - 1) + [94m_2302 + [94m_2311 + 32]
                              require unknown07b08870.length - 1 < unknown07b08870.length
                              mem[0] = 24
                              addr(unknown07b08870[unknown07b08870.length].field_0) = 0
                              unknown07b08870.length--
                              if unknown07b08870.length > unknown07b08870.length - 1:
                                  mem[0] = 24
                                  [94ms = unknown07b08870.length + sha3(24) - 1
                                  while sha3(24) + unknown07b08870.length > [94ms:
                                      stor[[94ms] = 0
                                      [94ms = [94ms + 1
                                      continue 
                              [94midx = [94midx
                              continue 
                          [94m_2920 = mem[64]
                          mem[64] = mem[64] + (32 * stor19.length) + 32
                          mem[[94m_2920] = stor19.length
                          if not stor19.length:
                              [94midx = 0
                              while [94midx < stor19.length:
                                  require [94midx < mem[[94m_2920]
                                  if mem[(32 * [94midx) + [94m_2920 + 44 len 20]:
                                      require [94midx < mem[[94m_2920]
                                      [94m_3615 = mem[[94m_2920 + (32 * [94midx) + 32]
                                      mem[mem[64] + 4] = this.address
                                      require ext_code.size(addr([94m_3615))
                                      call addr([94m_3615).balanceOf(address owner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      mem[mem[64]] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[0] = addr([94m_3615)
                                      mem[32] = 21
                                      amounts[addr([94m_3615)] = ext_call.return_data[0]
                                      if 0 < ext_call.return_data[0]:
                                          mem[0] = addr([94m_3615)
                                          mem[32] = 22
                                          if not stor22[addr([94m_3615)]:
                                              tokens.length++
                                              addr(tokens[tokens.length].field_0) = addr([94m_3615)
                                              mem[0] = addr([94m_3615)
                                              mem[32] = 22
                                              stor22[addr([94m_3615)] = 1
                                  [94midx = [94midx + 1
                                  continue 
                          else:
                              mem[0] = 19
                              mem[[94m_2920 + 32] = addr(stor19.field_0)
                              [94midx = [94m_2920 + 32
                              [94ms = 0
                              while [94m_2920 + (32 * stor19.length) > [94midx:
                                  mem[[94midx + 32] = addr(stor19[[94ms].field_256)
                                  [94midx = [94midx + 32
                                  [94ms = [94ms + 1
                                  continue 
                              [94midx = 0
                              while [94midx < stor19.length:
                                  require [94midx < mem[[94m_2920]
                                  if mem[(32 * [94midx) + [94m_2920 + 44 len 20]:
                                      require [94midx < mem[[94m_2920]
                                      [94m_4693 = mem[[94m_2920 + (32 * [94midx) + 32]
                                      mem[mem[64] + 4] = this.address
                                      require ext_code.size(addr([94m_4693))
                                      call addr([94m_4693).balanceOf(address owner) with:
                                           gas gas_remaining wei
                                          args this.address
                                      mem[mem[64]] = ext_call.return_data[0]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 32
                                      mem[0] = addr([94m_4693)
                                      mem[32] = 21
                                      amounts[addr([94m_4693)] = ext_call.return_data[0]
                                      if 0 < ext_call.return_data[0]:
                                          mem[0] = addr([94m_4693)
                                          mem[32] = 22
                                          if not stor22[addr([94m_4693)]:
                                              tokens.length++
                                              addr(tokens[tokens.length].field_0) = addr([94m_4693)
                                              mem[0] = addr([94m_4693)
                                              mem[32] = 22
                                              stor22[addr([94m_4693)] = 1
                                  [94midx = [94midx + 1
                                  continue 
                      stor19.length = 0
                      [94midx = 0
                      while stor19.length > [94midx:
                          stor19[[94midx].field_0 = 0
                          [94midx = [94midx + 1
                          continue 
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
                      require ext_call.return_data[32] <= totalSupply
                      totalSupply -= ext_call.return_data[32]
                      log Transfer(
                            address from=ext_call.return_data[32],
                            address to=caller,
                            uint256 value=0)
                      if ext_call.return_data[0] > 0:
                          call caller with:
                             value ext_call.return_data[0] wei
                               gas 2300 * is_zero(value) wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                      if balanceOf[caller] <= 0:
                          require unknown81d62bf5.length - 1 < unknown81d62bf5.length
                          require unknown1c2a0e5c[caller] - 1 < unknown81d62bf5.length
                          addr(unknown81d62bf5[stor26[caller]].field_0) = addr(unknown81d62bf5[unknown81d62bf5.length].field_0)
                          require unknown81d62bf5.length - 1 < unknown81d62bf5.length
                          unknown1c2a0e5c[addr(stor27[stor27.length].field_0)] = unknown1c2a0e5c[caller]
                          unknown81d62bf5.length--
                          if unknown81d62bf5.length > unknown81d62bf5.length - 1:
                              [94midx = unknown81d62bf5.length - 1
                              while unknown81d62bf5.length > [94midx:
                                  unknown81d62bf5[[94midx].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                          unknown1c2a0e5c[caller] = 0
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
  while [94midx < tokens.length:
      mem[0] = addr(tokens[[94midx].field_0)
      mem[32] = 23
      if stor23[addr(stor9[[94midx].field_0)]:
          [94midx = [94midx + 1
          continue 
      require [94midx < tokens.length
      mem[0] = 9
      require ext_code.size(addr(tokens[[94midx].field_0))
      call addr(tokens[[94midx].field_0).decimals() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = this.address
      require ext_code.size(addr(tokens[[94midx].field_0))
      call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          continue 
      mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      mem[164] = 10^ext_call.return_data[0]
      mem[196] = 0
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
      mem[96 len 64] = ext_call.return_data[0 len 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          continue 
      if not ext_call.return_data[0]:
          if 10^ext_call.return_data[0]:
              if 0 / 10^ext_call.return_data[0] >= 0:
                  [94midx = [94midx + 1
                  continue 
      else:
          if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
              if 10^ext_call.return_data[0]:
                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
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
  require _param1
  require status <= 3
  require not status
  require call.value >= 10^17
  unknown44644ef0 = 8760 * 24 * 3600
  require _param1
  unknown5075edbfAddress = _param1
  stor37F8 = 1
  stor72BF = 1
  storDE8F = 1
  stor68E4 = 1
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
          if not stor16[[94m_46]:
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
  require ext_code.size(unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000])
  call unknown2156e6c6[0x46656550726f76696465720000000000000000000000000000000000000000].setFeePercentage(uint256 newFee) with:
       gas gas_remaining wei
      args _param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknown2156e6c6[0x4c6f636b657250726f76696465720000000000000000000000000000000000])
  call unknown2156e6c6[0x4c6f636b657250726f76696465720000000000000000000000000000000000].0x62f0ce85 with:
       gas gas_remaining wei
      args 0x576974686472617750726f7669646572000000000000000000000000000000, _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require 0 < 0, 0x576974686472617750726f76696465720000000000000000000000
  require 1 < 0, 0x576974686472617750726f76696465720000000000000000000000
  mem[1028 len 0] = None
  mem[1124 len 0x576974686472617750726f76696465720000000000000000000000] = 10, 5, 2, 0x576974686472617750726f7669646572000000000000000000000000000000, 0x4765744574680000000000000000000000000000000000000000000000000000, 0, 64, 160, 2, mem[1028 len 64], 0, 0x576974686472617750726f76696465720000000000000000000000, mem[1124 len 0x576974686472617750726f7669646571fffffffffffffffffffe9c]
  require ext_code.size(unknown2156e6c6[0x5374657050726f766964657200000000000000000000000000000000000000])
  call unknown2156e6c6[0x5374657050726f766964657200000000000000000000000000000000000000].0xfdb880b9 with:
       gas gas_remaining wei
      args 64, 160, 2, mem[1028 len 64], 0, 0x576974686472617750726f76696465720000000000000000000000, mem[1124 len 0xaed2e8d0c8e4c2eea0e4deecd2c8cae400000000000000000000000]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  status = 1
  require call.value + accumulatedFee >= accumulatedFee
  accumulatedFee += call.value


# hash = 0x81d62bf5
# getter = ['storage', 160, 0, ['add', ['sha3', 27], ['cd', 4]]]
# const = None
# payable = False
def unknown81d62bf5(uint256 _param1): # not payable
  require _param1 < unknown81d62bf5.length
  return addr(unknown81d62bf5[_param1].field_0)


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  require caller == owner
  require not paused
  paused = 1
  pausedTime = block.timestamp


# hash = 0x85450abf
# getter = None
# const = None
# payable = False
def unknown85450abf(): # not payable
  if not unknown81d62bf5.length:
      mem[(32 * unknown81d62bf5.length) + 128] = 32
      mem[(32 * unknown81d62bf5.length) + 160] = unknown81d62bf5.length
      mem[(32 * unknown81d62bf5.length) + 192 len floor32(unknown81d62bf5.length)] = mem[128 len floor32(unknown81d62bf5.length)]
      return memory
        from (32 * unknown81d62bf5.length) + 128
         [93mlen (96 * unknown81d62bf5.length) + 64
  mem[128] = addr(unknown81d62bf5.field_0)
  [94midx = 128
  [94ms = 0
  while (32 * unknown81d62bf5.length) + 96 > [94midx:
      mem[[94midx + 32] = addr(unknown81d62bf5[[94ms].field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * unknown81d62bf5.length) + 192 len floor32(unknown81d62bf5.length)] = mem[128 len floor32(unknown81d62bf5.length)]
  return Array(len=unknown81d62bf5.length, data=mem[128 len floor32(unknown81d62bf5.length)], mem[(32 * unknown81d62bf5.length) + floor32(unknown81d62bf5.length) + 192 len (32 * unknown81d62bf5.length) - floor32(unknown81d62bf5.length)]), 


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


# hash = 0x8a97d732
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 23]]]]
# const = None
# payable = False
def unknown8a97d732(addr _param1): # not payable
  return bool(stor23[_param1])


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


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 12]]]], ['loc', 12]]]
# const = None
# payable = False
def symbol(): # not payable
  return symbol[0 len symbol.length]


# hash = 0x98d5fdca
# getter = None
# const = None
# payable = False
def getPrice(): # not payable
  if 0 == totalSupply:
      return 10^18
  require accumulatedFee <= eth.balance(this.address)
  [94midx = 0
  while [94midx < tokens.length:
      mem[0] = addr(tokens[[94midx].field_0)
      mem[32] = 23
      if stor23[addr(stor9[[94midx].field_0)]:
          [94midx = [94midx + 1
          continue 
      require [94midx < tokens.length
      mem[0] = 9
      require ext_code.size(addr(tokens[[94midx].field_0))
      call addr(tokens[[94midx].field_0).decimals() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[100] = this.address
      require ext_code.size(addr(tokens[[94midx].field_0))
      call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          continue 
      mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      mem[164] = 10^ext_call.return_data[0]
      mem[196] = 0
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
      mem[96 len 64] = ext_call.return_data[0 len 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          continue 
      if not ext_call.return_data[0]:
          if 10^ext_call.return_data[0]:
              if 0 / 10^ext_call.return_data[0] >= 0:
                  [94midx = [94midx + 1
                  continue 
      else:
          if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
              if 10^ext_call.return_data[0]:
                  if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
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
  [94midx = 0
  while [94midx < tokens.length:
      mem[0] = addr(tokens[[94midx].field_0)
      mem[32] = 21
      require [94midx < tokens.length
      mem[(32 * [94midx) + 128] = amounts[addr(stor9[[94midx].field_0)]
      [94midx = [94midx + 1
      continue 
  if tokens.length:
      mem[(32 * tokens.length) + 160] = addr(tokens.field_0)
      [94midx = (32 * tokens.length) + 160
      [94ms = 0
      while (64 * tokens.length) + 128 > [94midx:
          mem[[94midx + 32] = addr(tokens[[94ms].field_256)
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
  mem[(64 * tokens.length) + 160] = 64
  mem[(64 * tokens.length) + 224] = tokens.length
  mem[(64 * tokens.length) + 256 len floor32(tokens.length)] = mem[(32 * tokens.length) + 160 len floor32(tokens.length)]
  mem[(64 * tokens.length) + 192] = (32 * tokens.length) + 96
  mem[(98 * tokens.length) + 256] = tokens.length
  return Array(len=tokens.length, data=mem[(32 * tokens.length) + 160 len floor32(tokens.length)], mem[(64 * tokens.length) + floor32(tokens.length) + 256 len (64 * tokens.length) + -floor32(tokens.length) + 32]), 
         (32 * tokens.length) + 96


# hash = 0xb2cca39d
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def pausedTime(): # not payable
  return pausedTime


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
  if status != 3:
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
  else:
      [94midx = 0
      while [94midx < tokens.length:
          mem[0] = addr(tokens[[94midx].field_0)
          mem[32] = 23
          if stor23[addr(stor9[[94midx].field_0)]:
              [94midx = [94midx + 1
              continue 
          require [94midx < tokens.length
          mem[0] = 9
          require ext_code.size(addr(tokens[[94midx].field_0))
          call addr(tokens[[94midx].field_0).decimals() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          mem[100] = this.address
          require ext_code.size(addr(tokens[[94midx].field_0))
          call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
               gas gas_remaining wei
              args this.address
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              continue 
          mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
          mem[164] = 10^ext_call.return_data[0]
          mem[196] = 0
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
          mem[96 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
          if not ext_call.return_data[0]:
              [94midx = [94midx + 1
              continue 
          if not ext_call.return_data[0]:
              if 10^ext_call.return_data[0]:
                  if 0 / 10^ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      continue 
          else:
              if ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]:
                  if 10^ext_call.return_data[0]:
                      if ext_call.return_data[0] * ext_call.return_data[0] / 10^ext_call.return_data[0] >= 0:
                          [94midx = [94midx + 1
                          continue 
          revert
      require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].0xc77e7614 with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require _amount <= accumulatedFee
      else:
          require _amount + 10^17 >= _amount
          require _amount + 10^17 <= accumulatedFee
          require _amount <= accumulatedFee
      ('le', ('param', '_amount'), ('stor', ('name', 'accumulatedFee', 25)))
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
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
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
def increaseApproval(address _spender, uint256 _addedValue): # not payable
  require not paused
  require _addedValue + allowance[caller][addr(_spender)] >= allowance[caller][addr(_spender)]
  allowance[caller][addr(_spender)] += _addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xd92cb69a
# getter = ['storage', 8, 0, 17]
# const = None
# payable = False
def unknownd92cb69a(): # not payable
  require unknownd92cb69a <= 2
  return unknownd92cb69a


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
          require not paused
          require status <= 3
          require status == 1
          require call.value >= 10^15
          if unknown1c2a0e5c[caller]:
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
                          while [94midx < tokens.length:
                              mem[0] = addr(tokens[[94midx].field_0)
                              mem[32] = 23
                              if not stor23[addr(stor9[[94midx].field_0)]:
                                  require [94midx < tokens.length
                                  mem[0] = 9
                                  require ext_code.size(addr(tokens[[94midx].field_0))
                                  call addr(tokens[[94midx].field_0).decimals() with:
                                       gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      mem[100] = this.address
                                      require ext_code.size(addr(tokens[[94midx].field_0))
                                      call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
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
                                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                                   gas gas_remaining wei
                                                  args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
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
                                                          continue 
                                                      else:
                                                          require 10^ext_call.return_data[0]
                                                          require 0 / 10^ext_call.return_data[0] >= 0
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      [94midx = [94midx + 1
                                                      continue 
                                          else:
                                              [94midx = [94midx + 1
                                              continue 
                              else:
                                  [94midx = [94midx + 1
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
                          while [94midx < tokens.length:
                              mem[0] = addr(tokens[[94midx].field_0)
                              mem[32] = 23
                              if not stor23[addr(stor9[[94midx].field_0)]:
                                  require [94midx < tokens.length
                                  mem[0] = 9
                                  require ext_code.size(addr(tokens[[94midx].field_0))
                                  call addr(tokens[[94midx].field_0).decimals() with:
                                       gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      mem[100] = this.address
                                      require ext_code.size(addr(tokens[[94midx].field_0))
                                      call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
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
                                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                                   gas gas_remaining wei
                                                  args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
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
                                                          continue 
                                                      else:
                                                          require 10^ext_call.return_data[0]
                                                          require 0 / 10^ext_call.return_data[0] >= 0
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      [94midx = [94midx + 1
                                                      continue 
                                          else:
                                              [94midx = [94midx + 1
                                              continue 
                              else:
                                  [94midx = [94midx + 1
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
          else:
              unknown81d62bf5.length++
              stor3AD8[stor27.length] = caller
              unknown1c2a0e5c[caller] = unknown81d62bf5.length + 1
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
                          while [94midx < tokens.length:
                              mem[0] = addr(tokens[[94midx].field_0)
                              mem[32] = 23
                              if not stor23[addr(stor9[[94midx].field_0)]:
                                  require [94midx < tokens.length
                                  mem[0] = 9
                                  require ext_code.size(addr(tokens[[94midx].field_0))
                                  call addr(tokens[[94midx].field_0).decimals() with:
                                       gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      mem[100] = this.address
                                      require ext_code.size(addr(tokens[[94midx].field_0))
                                      call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
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
                                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                                   gas gas_remaining wei
                                                  args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
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
                                                          continue 
                                                      else:
                                                          require 10^ext_call.return_data[0]
                                                          require 0 / 10^ext_call.return_data[0] >= 0
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      [94midx = [94midx + 1
                                                      continue 
                                          else:
                                              [94midx = [94midx + 1
                                              continue 
                              else:
                                  [94midx = [94midx + 1
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
                          while [94midx < tokens.length:
                              mem[0] = addr(tokens[[94midx].field_0)
                              mem[32] = 23
                              if not stor23[addr(stor9[[94midx].field_0)]:
                                  require [94midx < tokens.length
                                  mem[0] = 9
                                  require ext_code.size(addr(tokens[[94midx].field_0))
                                  call addr(tokens[[94midx].field_0).decimals() with:
                                       gas gas_remaining wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 32
                                      mem[100] = this.address
                                      require ext_code.size(addr(tokens[[94midx].field_0))
                                      call addr(tokens[[94midx].field_0).balanceOf(address owner) with:
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
                                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                                   gas gas_remaining wei
                                                  args addr(tokens[[94midx].field_0), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10^ext_call.return_data[0], 0
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
                                                          continue 
                                                      else:
                                                          require 10^ext_call.return_data[0]
                                                          require 0 / 10^ext_call.return_data[0] >= 0
                                                          [94midx = [94midx + 1
                                                          continue 
                                                  else:
                                                      [94midx = [94midx + 1
                                                      continue 
                                          else:
                                              [94midx = [94midx + 1
                                              continue 
                              else:
                                  [94midx = [94midx + 1
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
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def category(): # not payable
  return category


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
# getter = ['storage', 256, 0, 25]
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

