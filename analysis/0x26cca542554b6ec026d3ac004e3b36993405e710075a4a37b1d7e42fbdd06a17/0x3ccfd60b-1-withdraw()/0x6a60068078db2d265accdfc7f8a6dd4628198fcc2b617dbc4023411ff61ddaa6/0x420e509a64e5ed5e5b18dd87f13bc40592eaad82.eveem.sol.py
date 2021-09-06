# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x420E509a64E5Ed5E5B18Dd87F13Bc40592eAAD82 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x1809549f': 'updateAllComponents()', '0x3ccfd60b': 'withdraw()', '0xcd6dc687': 'initialize(address _simplyBrand, uint256 _totalSupply)'} 

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
    stor7
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
    paused # mask: a s
    # storage address 13
    stor13 # mask: a s
    # storage address 15
    stor15
    # storage address 16
    stor16
    # storage address 17
    maxTransfers # mask: a s
    # storage address 18
    accumulatedFee # mask: a s
# hash = 0x05f8d55d
# getter = None
# const = None
# payable = True
def addOwnerBalance() payable: 
  require caller == owner
  accumulatedFee += call.value


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 1]]]], ['loc', 1]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x089f7f85
# getter = None
# const = None
# payable = False
def hasRisk(address _sender, address _receiver, address _tokenAddress, uint256 _amount, uint256 _rate): # not payable
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
       gas gas_remaining wei
      args addr(_sender), addr(_receiver), addr(_tokenAddress), _amount, _rate
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  log RiskEvent(
        address sender=addr(_sender),
        address receiver=addr(_receiver),
        address tokenAddress=addr(_tokenAddress),
        uint256 amount=_amount,
        uint256 rate=_rate,
        bool risky=bool(ext_call.return_data[0]))
  return bool(ext_call.return_data[0])


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
# const = ['return', ['data', 32, 16, 151531991519480409511034004871959281664]]
# payable = False
const WITHDRAW = 'r'


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def totalSupply(): # not payable
  return totalSupply


# hash = 0x1bb7cc99
# getter = None
# const = ['return', ['data', 32, 17, 34163080641509995819850397732846667038720]]
# payable = False
const WHITELIST = 'der'


# hash = 0x1ca3630a
# getter = None
# const = None
# payable = False
def updateComponent(string _name): # not payable
  mem[128 len _name.length] = _name[all]
  require caller == owner
  mem[ceil32(_name.length) + 128] = 0xd4ba769c00000000000000000000000000000000000000000000000000000000
  mem[ceil32(_name.length) + 132] = 32
  mem[ceil32(_name.length) + 164] = _name.length
  mem[ceil32(_name.length) + 196 len ceil32(_name.length)] = _name[all], mem[_name.length + 128 len ceil32(_name.length) - _name.length]
  require ext_code.size(stor13)
  call stor13.0xd4ba769c with:
       gas gas_remaining wei
      args Array(len=_name.length, data=_name[all])
  mem[ceil32(_name.length) + 128] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mem[ceil32(_name.length) + 128 len floor32(_name.length)] = call.data[_name + 36 len floor32(_name.length)]
  mem[ceil32(_name.length) + floor32(_name.length) + 128] = 256^(-(_name.length % 32) + 32) - 1 and mem[ceil32(_name.length) + floor32(_name.length) + 128] or call.data[_name + floor32(_name.length) + 36 len _name.length % 32], mem[_name.length + 128 len -(_name.length % 32) + 32] and !(256^(-(_name.length % 32) + 32) - 1)
  mem[ceil32(_name.length) + _name.length + 128] = 7
  if stor[mem[ceil32(_name.length) + floor32(_name.length) + 128 len (_name.length % 32) + 32]][call.data[_name + 36 len floor32(_name.length)]] == addr(ext_call.return_data[0]):
      mem[ceil32(_name.length) + 128 len floor32(_name.length)] = call.data[_name + 36 len floor32(_name.length)]
      mem[ceil32(_name.length) + floor32(_name.length) + 128] = 256^(-(_name.length % 32) + 32) - 1 and mem[ceil32(_name.length) + floor32(_name.length) + 128] or call.data[_name + floor32(_name.length) + 36 len _name.length % 32], mem[_name.length + 128 len -(_name.length % 32) + 32] and !(256^(-(_name.length % 32) + 32) - 1)
      mem[ceil32(_name.length) + _name.length + 128] = 7
      mem[ceil32(_name.length) + 128] = stor[mem[ceil32(_name.length) + floor32(_name.length) + 128 len (_name.length % 32) + 32]][call.data[_name + 36 len floor32(_name.length)]]
      return memory
        from ceil32(_name.length) + 128
         [93mlen 32
  mem[ceil32(_name.length) + 128] = 0xd4ba769c00000000000000000000000000000000000000000000000000000000
  mem[ceil32(_name.length) + 132] = 32
  mem[ceil32(_name.length) + 164] = _name.length
  mem[ceil32(_name.length) + 196 len ceil32(_name.length)] = _name[all], mem[_name.length + 128 len ceil32(_name.length) - _name.length]
  require ext_code.size(stor13)
  call stor13.0xd4ba769c with:
       gas gas_remaining wei
      args Array(len=_name.length, data=_name[all])
  mem[ceil32(_name.length) + 128] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require addr(ext_call.return_data[0])
  mem[ceil32(_name.length) + 128 len floor32(_name.length)] = call.data[_name + 36 len floor32(_name.length)]
  mem[ceil32(_name.length) + floor32(_name.length) + 128] = 256^(-(_name.length % 32) + 32) - 1 and mem[ceil32(_name.length) + floor32(_name.length) + 128] or call.data[_name + floor32(_name.length) + 36 len _name.length % 32], mem[_name.length + 128 len -(_name.length % 32) + 32] and !(256^(-(_name.length % 32) + 32) - 1)
  mem[ceil32(_name.length) + _name.length + 128] = 7
  stor[mem[ceil32(_name.length) + floor32(_name.length) + 128 len (_name.length % 32) + 32]][call.data[_name + 36 len floor32(_name.length)]] = addr(ext_call.return_data[0])
  mem[ceil32(_name.length) + 128] = 14
  mem[ceil32(_name.length) + 160] = 0x4d61726b657450726f76696465720000000000000000000000000000000000
  mem[ceil32(_name.length) + 238 len 0] = None
  mem[ceil32(_name.length) + 238] = 0, mem[ceil32(_name.length) + 256 len 14]
  mem[ceil32(_name.length) + 270 len floor32(_name.length)] = call.data[_name + 36 len floor32(_name.length)]
  mem[ceil32(_name.length) + floor32(_name.length) + -(_name.length % 32) + 302 len _name.length % 32] = mem[floor32(_name.length) + -(_name.length % 32) + 160 len _name.length % 32]
  mem[_name.length + ceil32(_name.length) + 270 len floor32(_name.length)] = call.data[_name + 36 len floor32(_name.length)]
  mem[(2 * floor32(_name.length)) + ceil32(_name.length) + 302 len _name.length % 32] = mem[ceil32(_name.length) + -(_name.length % 32) + floor32(_name.length) + 302 len _name.length % 32]
  if sha3(call.data[_name + 36 len floor32(_name.length)], mem[_name.length + ceil32(_name.length) + floor32(_name.length) + 270 len _name.length % 32]) != sha3(mem[ceil32(_name.length) + 238 len 14]):
      mem[_name.length + ceil32(_name.length) + 270 len floor32(_name.length)] = call.data[_name + 36 len floor32(_name.length)]
      mem[_name.length + ceil32(_name.length) + floor32(_name.length) + 270] = 256^(-(_name.length % 32) + 32) - 1 and mem[_name.length + ceil32(_name.length) + floor32(_name.length) + 270] or call.data[_name + floor32(_name.length) + 36 len _name.length % 32], mem[_name.length + 128 len -(_name.length % 32) + 32] and !(256^(-(_name.length % 32) + 32) - 1)
      mem[(2 * _name.length) + ceil32(_name.length) + 270] = 7
      [94m_2893 = sha3(call.data[_name + 36 len floor32(_name.length)], mem[_name.length + ceil32(_name.length) + floor32(_name.length) + 270 len (_name.length % 32) + 32])
      require ext_code.size(stor[mem[_name.length + ceil32(_name.length) + floor32(_name.length) + 270 len (_name.length % 32) + 32]][call.data[_name + 36 len floor32(_name.length)]])
      call stor[mem[_name.length + ceil32(_name.length) + floor32(_name.length) + 270 len (_name.length % 32) + 32]][call.data[_name + 36 len floor32(_name.length)]].MOT() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[_name.length + ceil32(_name.length) + 274] = stor[mem[_name.length + ceil32(_name.length) + floor32(_name.length) + 270 len (_name.length % 32) + 32]][call.data[_name + 36 len floor32(_name.length)]]
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args mem[_name.length + ceil32(_name.length) + 274], 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(stor[[94m_2893])
      call stor[[94m_2893].MOT() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args stor[[94m_2893], -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(stor13)
  call stor13.0xd4ba769c with:
       gas gas_remaining wei
      args Array(len=_name.length, data=_name[all])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return addr(ext_call.return_data[0])


# hash = 0x1ed374c6
# getter = None
# const = None
# payable = False
def disableWhitelist(uint8 _key): # not payable
  require caller == owner
  require _key <= 1
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].0x42340458 with:
       gas gas_remaining wei
      args _key
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0x1fa98406
# getter = ['storage', 8, 0, 11]
# const = None
# payable = False
def fundType(): # not payable
  require fundType <= 1
  return fundType


# hash = 0x200d2ed2
# getter = ['storage', 8, 0, 13]
# const = None
# payable = False
def status(): # not payable
  require status <= 3
  return status


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address _from, address _to, uint256 _value): # not payable
  require not paused
  require _to
  require _value <= balanceOf[addr(_from)]
  require _value <= allowance[addr(_from)][caller]
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


# hash = 0x313ce567
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def decimals(): # not payable
  return decimals


# hash = 0x36642c21
# getter = None
# const = None
# payable = False
def unknown36642c21(): # not payable
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].0xc77e7614 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x3c98d189
# getter = None
# const = None
# payable = False
def unknown3c98d189(uint256 _param1, array _param2, array _param3, array _param4): # not payable
  mem[96] = _param2.length
  mem[128 len 32 * _param2.length] = call.data[_param2 + 36 len 32 * _param2.length]
  mem[(32 * _param2.length) + 128] = _param3.length
  mem[(32 * _param2.length) + 160 len 32 * _param3.length] = call.data[_param3 + 36 len 32 * _param3.length]
  mem[64] = (32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192
  mem[(32 * _param3.length) + (32 * _param2.length) + 160] = _param4.length
  mem[(32 * _param3.length) + (32 * _param2.length) + 192 len 32 * _param4.length] = call.data[_param4 + 36 len 32 * _param4.length]
  require caller == owner
  [94midx = 0
  [94ms = 0
  while [94midx < _param3.length:
      require [94midx < mem[(32 * _param2.length) + 128]
      [94m_70 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
      require [94midx < mem[(32 * _param3.length) + (32 * _param2.length) + 160]
      [94m_72 = mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param2.length) + 192]
      [94m_76 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_76] = 12
      mem[[94m_76 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
      [94m_81 = mem[64]
      [94mu = [94m_76 + 32
      [94mv = mem[64]
      [94mt = mem[[94m_76]
      while [94mt >= 32:
          mem[[94mv] = mem[[94mu]
          [94mu = [94mu + 32
          [94mv = [94mv + 32
          [94mt = [94mt - 32
          continue 
      mem[mem[64] + floor32(mem[[94m_76])] = 256^(-(mem[[94m_76] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_76])] or mem[[94m_76 + floor32(mem[[94m_76]) + 32] and !(256^(-(mem[[94m_76] % 32) + 32) - 1)
      mem[[94m_81 + 12] = 7
      require ext_code.size(stor[sha3(mem[mem[64] len [94m_81 + -mem[64] + 44])])
      call stor[sha3(mem[mem[64] len [94m_81 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
           gas gas_remaining wei
          args addr(this.address), 0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, [94m_70, [94m_72
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[mem[64]] = this.address
      mem[mem[64] + 32] = 0
      mem[mem[64] + 64] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      mem[mem[64] + 96] = [94m_70
      mem[mem[64] + 128] = [94m_72
      mem[mem[64] + 160] = bool(ext_call.return_data[0])
      log RiskEvent(
            address sender=addr(this.address),
            address receiver=0,
            address tokenAddress=0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee,
            uint256 amount=_70,
            uint256 rate=_72,
            bool risky=bool(ext_call.return_data[0]))
      require not ext_call.return_data[0]
      if [94midx < mem[(32 * _param2.length) + 128]:
          [94midx = [94midx + 1
          [94ms = [94ms + mem[(32 * [94midx) + (32 * _param2.length) + 160]
          continue 
      revert
  require eth.balance(this.address) - accumulatedFee >= [94ms
  [94m_73 = mem[64]
  mem[64] = mem[64] + 64
  mem[[94m_73] = 16
  mem[[94m_73 + 32] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[mem[64] len 0] = None
  mem[mem[64] + 16] = 7
  [94m_142 = mem[64]
  mem[mem[64]] = 0xf417793600000000000000000000000000000000000000000000000000000000
  mem[mem[64] + 100] = this.address
  mem[mem[64] + 132] = _param1
  mem[mem[64] + 164] = 0
  mem[mem[64] + 4] = 192
  mem[mem[64] + 196] = mem[96]
  [94m_144 = mem[96]
  mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  mem[mem[64] + 36] = (32 * mem[96]) + 224
  mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * _param2.length) + 128]
  [94m_182 = mem[(32 * _param2.length) + 128]
  mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * _param2.length) + 128])] = mem[(32 * _param2.length) + 160 len floor32(mem[(32 * _param2.length) + 128])]
  mem[mem[64] + 68] = (32 * [94m_182) + (32 * mem[96]) + 256
  mem[(32 * [94m_182) + (32 * [94m_144) + [94m_142 + 260] = mem[(32 * _param3.length) + (32 * _param2.length) + 160]
  [94m_210 = mem[(32 * _param3.length) + (32 * _param2.length) + 160]
  mem[(32 * [94m_182) + (32 * [94m_144) + [94m_142 + 292 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])] = mem[(32 * _param3.length) + (32 * _param2.length) + 192 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])]
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].buyTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
     value [94ms wei
       gas gas_remaining wei
      args mem[mem[64] + 4 len (32 * [94m_210) + (32 * [94m_182) + (32 * [94m_144) + [94m_142 + -mem[64] + 288]
  mem[mem[64]] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  [94m_256 = mem[96]
  [94midx = 0
  [94ms = 0
  while [94midx < [94m_256:
      require [94midx < mem[96]
      [94m_258 = mem[(32 * [94midx) + 128]
      mem[mem[64] + 4] = this.address
      require ext_code.size(addr([94m_258))
      call addr([94m_258).balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      stor15[addr([94m_258)] = ext_call.return_data[0]
      if 0 >= ext_call.return_data[0]:
          mem[0] = addr([94m_258)
          mem[32] = 15
          mem[mem[64]] = addr([94m_258)
          mem[mem[64] + 32] = stor15[addr([94m_258)]
          log 0xd431031d: addr(_258), stor15[addr(_258)]
      else:
          if stor16[addr([94m_258)]:
              mem[0] = addr([94m_258)
              mem[32] = 15
              mem[mem[64]] = addr([94m_258)
              mem[mem[64] + 32] = stor15[addr([94m_258)]
              log 0xd431031d: addr(_258), stor15[addr(_258)]
          else:
              tokens.length++
              tokens[tokens.length].field_0 = addr([94m_258)
              mem[0] = addr([94m_258)
              mem[32] = 16
              stor16[addr([94m_258)] = 1
      [94midx = [94midx + 1
      [94ms = [94m_258
      continue 
  return 1


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
  require caller == owner
  require status <= 3
  require status
  require caller == owner
  [94midx = 0
  [94ms = 0
  while uint8([94midx) < tokens.length:
      mem[0] = tokens[uint8([94midx)].field_0
      mem[32] = 15
      if stor15[stor12[uint8([94midx)].field_0] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  mem[96] = uint8([94ms)
  if not uint8([94ms):
      [94midx = 0
      [94mt = 0
      while uint8([94midx) < tokens.length:
          mem[0] = tokens[uint8([94midx)].field_0
          mem[32] = 15
          if stor15[stor12[uint8([94midx)].field_0] <= 0:
              [94midx = [94midx + 1
              [94mt = [94mt
              continue 
          require uint8([94midx) < tokens.length
          mem[0] = 12
          require uint8([94mt) < uint8([94ms)
          mem[(32 * uint8([94mt)) + 128] = tokens[uint8([94midx)].field_0
          [94midx = [94midx + 1
          [94mt = [94mt + 1
          continue 
      mem[(32 * uint8([94ms)) + 128] = uint8([94ms)
      if not uint8([94ms):
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2633 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2633))
                  call addr([94m_2633).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2850 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2931 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2931] = 12
                  mem[[94m_2931 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_2973 = mem[64]
                  [94mu = [94m_2931 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2931]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2931])] = 256^(-(mem[[94m_2931] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2931])] or mem[[94m_2931 + floor32(mem[[94m_2931]) + 32] and !(256^(-(mem[[94m_2931] % 32) + 32) - 1)
                  mem[[94m_2973 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_2973 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_2973 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2850), 100000 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2850)
                  mem[mem[64] + 96] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2850),
                        uint256 amount=100000 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3418 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3418))
                  call addr([94m_3418).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3458 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3482 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3482
                  require ext_code.size(addr([94m_3458))
                  call addr([94m_3458).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3482
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2601 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2603 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3250 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3250) + (32 * mem[96]) + 256
              mem[(32 * [94m_3250) + (32 * [94m_2603) + [94m_2601 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3658 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3250) + (32 * [94m_2603) + [94m_2601 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3658) + (32 * [94m_3250) + (32 * [94m_2603) + [94m_2601 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_4065 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_4065:
                  require [94midx < mem[96]
                  [94m_4081 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_4081))
                  call addr([94m_4081).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_4081)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_4081)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_4081)
                      mem[mem[64] + 32] = stor15[addr([94m_4081)]
                      log 0xd431031d: addr(_4081), stor15[addr(_4081)]
                  else:
                      if stor16[addr([94m_4081)]:
                          mem[0] = addr([94m_4081)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_4081)
                          mem[mem[64] + 32] = stor15[addr([94m_4081)]
                          log 0xd431031d: addr(_4081), stor15[addr(_4081)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_4081)
                          mem[0] = addr([94m_4081)
                          mem[32] = 16
                          stor16[addr([94m_4081)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_4081
                  continue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2636 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2636))
                  call addr([94m_2636).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2853 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2936 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2936] = 12
                  mem[[94m_2936 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_2979 = mem[64]
                  [94mu = [94m_2936 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2936]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2936])] = 256^(-(mem[[94m_2936] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2936])] or mem[[94m_2936 + floor32(mem[[94m_2936]) + 32] and !(256^(-(mem[[94m_2936] % 32) + 32) - 1)
                  mem[[94m_2979 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_2979 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_2979 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2853), 100000 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2853)
                  mem[mem[64] + 96] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2853),
                        uint256 amount=100000 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3422 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3422))
                  call addr([94m_3422).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3461 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3486 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3486
                  require ext_code.size(addr([94m_3461))
                  call addr([94m_3461).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3486
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2605 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2607 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3258 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3258) + (32 * mem[96]) + 256
              mem[(32 * [94m_3258) + (32 * [94m_2607) + [94m_2605 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3661 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3258) + (32 * [94m_2607) + [94m_2605 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3661) + (32 * [94m_3258) + (32 * [94m_2607) + [94m_2605 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_4066 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_4066:
                  require [94midx < mem[96]
                  [94m_4084 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_4084))
                  call addr([94m_4084).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_4084)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_4084)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_4084)
                      mem[mem[64] + 32] = stor15[addr([94m_4084)]
                      log 0xd431031d: addr(_4084), stor15[addr(_4084)]
                  else:
                      if stor16[addr([94m_4084)]:
                          mem[0] = addr([94m_4084)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_4084)
                          mem[mem[64] + 32] = stor15[addr([94m_4084)]
                          log 0xd431031d: addr(_4084), stor15[addr(_4084)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_4084)
                          mem[0] = addr([94m_4084)
                          mem[32] = 16
                          stor16[addr([94m_4084)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_4084
                  continue 
      else:
          mem[(32 * uint8([94ms)) + 160 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2639 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2639))
                  call addr([94m_2639).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2856 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2941 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2941] = 12
                  mem[[94m_2941 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94mu = [94m_2941 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2941]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2941])] = 256^(-(mem[[94m_2941] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2941])] or mem[[94m_2941 + floor32(mem[[94m_2941]) + 32] and !(256^(-(mem[[94m_2941] % 32) + 32) - 1)
                  require ext_code.size(stor7[mem[mem[64] len 12]])
                  call stor7[mem[mem[64] len 12]].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2856), 100000 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2856)
                  mem[mem[64] + 96] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2856),
                        uint256 amount=100000 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3426 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3426))
                  call addr([94m_3426).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3464 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3490 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3490
                  require ext_code.size(addr([94m_3464))
                  call addr([94m_3464).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3490
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2609 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2611 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3266 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3266) + (32 * mem[96]) + 256
              mem[(32 * [94m_3266) + (32 * [94m_2611) + [94m_2609 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3664 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3266) + (32 * [94m_2611) + [94m_2609 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3664) + (32 * [94m_3266) + (32 * [94m_2611) + [94m_2609 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_4067 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_4067:
                  require [94midx < mem[96]
                  [94m_4087 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_4087))
                  call addr([94m_4087).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_4087)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_4087)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_4087)
                      mem[mem[64] + 32] = stor15[addr([94m_4087)]
                      log 0xd431031d: addr(_4087), stor15[addr(_4087)]
                  else:
                      if stor16[addr([94m_4087)]:
                          mem[0] = addr([94m_4087)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_4087)
                          mem[mem[64] + 32] = stor15[addr([94m_4087)]
                          log 0xd431031d: addr(_4087), stor15[addr(_4087)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_4087)
                          mem[0] = addr([94m_4087)
                          mem[32] = 16
                          stor16[addr([94m_4087)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_4087
                  continue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2642 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2642))
                  call addr([94m_2642).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2859 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2946 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2946] = 12
                  mem[[94m_2946 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_2991 = mem[64]
                  [94mu = [94m_2946 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2946]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2946])] = 256^(-(mem[[94m_2946] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2946])] or mem[[94m_2946 + floor32(mem[[94m_2946]) + 32] and !(256^(-(mem[[94m_2946] % 32) + 32) - 1)
                  mem[[94m_2991 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_2991 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_2991 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2859), 100000 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2859)
                  mem[mem[64] + 96] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2859),
                        uint256 amount=100000 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3430 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3430))
                  call addr([94m_3430).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3467 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3494 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3494
                  require ext_code.size(addr([94m_3467))
                  call addr([94m_3467).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3494
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2613 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2615 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3274 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3274) + (32 * mem[96]) + 256
              mem[(32 * [94m_3274) + (32 * [94m_2615) + [94m_2613 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3667 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3274) + (32 * [94m_2615) + [94m_2613 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3667) + (32 * [94m_3274) + (32 * [94m_2615) + [94m_2613 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_4068 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_4068:
                  require [94midx < mem[96]
                  [94m_4090 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_4090))
                  call addr([94m_4090).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_4090)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_4090)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_4090)
                      mem[mem[64] + 32] = stor15[addr([94m_4090)]
                      log 0xd431031d: addr(_4090), stor15[addr(_4090)]
                  else:
                      if stor16[addr([94m_4090)]:
                          mem[0] = addr([94m_4090)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_4090)
                          mem[mem[64] + 32] = stor15[addr([94m_4090)]
                          log 0xd431031d: addr(_4090), stor15[addr(_4090)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_4090)
                          mem[0] = addr([94m_4090)
                          mem[32] = 16
                          stor16[addr([94m_4090)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_4090
                  continue 
  else:
      mem[128 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
      [94midx = 0
      [94mt = 0
      while uint8([94midx) < tokens.length:
          mem[0] = tokens[uint8([94midx)].field_0
          mem[32] = 15
          if stor15[stor12[uint8([94midx)].field_0] <= 0:
              [94midx = [94midx + 1
              [94mt = [94mt
              continue 
          require uint8([94midx) < tokens.length
          mem[0] = 12
          require uint8([94mt) < uint8([94ms)
          mem[(32 * uint8([94mt)) + 128] = tokens[uint8([94midx)].field_0
          [94midx = [94midx + 1
          [94mt = [94mt + 1
          continue 
      mem[(32 * uint8([94ms)) + 128] = uint8([94ms)
      if not uint8([94ms):
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2645 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2645))
                  call addr([94m_2645).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2862 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2951 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2951] = 12
                  mem[[94m_2951 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_2997 = mem[64]
                  [94mu = [94m_2951 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2951]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2951])] = 256^(-(mem[[94m_2951] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2951])] or mem[[94m_2951 + floor32(mem[[94m_2951]) + 32] and !(256^(-(mem[[94m_2951] % 32) + 32) - 1)
                  mem[[94m_2997 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_2997 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_2997 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2862), 100000 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2862)
                  mem[mem[64] + 96] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2862),
                        uint256 amount=100000 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3434 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3434))
                  call addr([94m_3434).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3470 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3498 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3498
                  require ext_code.size(addr([94m_3470))
                  call addr([94m_3470).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3498
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2617 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2619 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3282 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3282) + (32 * mem[96]) + 256
              mem[(32 * [94m_3282) + (32 * [94m_2619) + [94m_2617 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3670 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3282) + (32 * [94m_2619) + [94m_2617 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3670) + (32 * [94m_3282) + (32 * [94m_2619) + [94m_2617 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_4069 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_4069:
                  require [94midx < mem[96]
                  [94m_4093 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_4093))
                  call addr([94m_4093).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_4093)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_4093)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_4093)
                      mem[mem[64] + 32] = stor15[addr([94m_4093)]
                      log 0xd431031d: addr(_4093), stor15[addr(_4093)]
                  else:
                      if stor16[addr([94m_4093)]:
                          mem[0] = addr([94m_4093)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_4093)
                          mem[mem[64] + 32] = stor15[addr([94m_4093)]
                          log 0xd431031d: addr(_4093), stor15[addr(_4093)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_4093)
                          mem[0] = addr([94m_4093)
                          mem[32] = 16
                          stor16[addr([94m_4093)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_4093
                  continue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2648 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2648))
                  call addr([94m_2648).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2865 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2956 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2956] = 12
                  mem[[94m_2956 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94mu = [94m_2956 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2956]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2956])] = 256^(-(mem[[94m_2956] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2956])] or mem[[94m_2956 + floor32(mem[[94m_2956]) + 32] and !(256^(-(mem[[94m_2956] % 32) + 32) - 1)
                  require ext_code.size(stor7[mem[mem[64] len 12]])
                  call stor7[mem[mem[64] len 12]].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2865), 100000 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2865)
                  mem[mem[64] + 96] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2865),
                        uint256 amount=100000 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3438 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3438))
                  call addr([94m_3438).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3473 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3502 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3502
                  require ext_code.size(addr([94m_3473))
                  call addr([94m_3473).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3502
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2621 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2623 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3290 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3290) + (32 * mem[96]) + 256
              mem[(32 * [94m_3290) + (32 * [94m_2623) + [94m_2621 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3673 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3290) + (32 * [94m_2623) + [94m_2621 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3673) + (32 * [94m_3290) + (32 * [94m_2623) + [94m_2621 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_4070 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_4070:
                  require [94midx < mem[96]
                  [94m_4096 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_4096))
                  call addr([94m_4096).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_4096)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_4096)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_4096)
                      mem[mem[64] + 32] = stor15[addr([94m_4096)]
                      log 0xd431031d: addr(_4096), stor15[addr(_4096)]
                  else:
                      if stor16[addr([94m_4096)]:
                          mem[0] = addr([94m_4096)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_4096)
                          mem[mem[64] + 32] = stor15[addr([94m_4096)]
                          log 0xd431031d: addr(_4096), stor15[addr(_4096)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_4096)
                          mem[0] = addr([94m_4096)
                          mem[32] = 16
                          stor16[addr([94m_4096)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_4096
                  continue 
      else:
          mem[(32 * uint8([94ms)) + 160 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2651 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2651))
                  call addr([94m_2651).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2868 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2961 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2961] = 12
                  mem[[94m_2961 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_3009 = mem[64]
                  [94mu = [94m_2961 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2961]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2961])] = 256^(-(mem[[94m_2961] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2961])] or mem[[94m_2961 + floor32(mem[[94m_2961]) + 32] and !(256^(-(mem[[94m_2961] % 32) + 32) - 1)
                  mem[[94m_3009 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_3009 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_3009 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2868), 100000 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2868)
                  mem[mem[64] + 96] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2868),
                        uint256 amount=100000 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3442 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3442))
                  call addr([94m_3442).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3476 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3506 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3506
                  require ext_code.size(addr([94m_3476))
                  call addr([94m_3476).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3506
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2625 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2627 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3298 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3298) + (32 * mem[96]) + 256
              mem[(32 * [94m_3298) + (32 * [94m_2627) + [94m_2625 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3676 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3298) + (32 * [94m_2627) + [94m_2625 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3676) + (32 * [94m_3298) + (32 * [94m_2627) + [94m_2625 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_4071 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_4071:
                  require [94midx < mem[96]
                  [94m_4099 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_4099))
                  call addr([94m_4099).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_4099)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_4099)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_4099)
                      mem[mem[64] + 32] = stor15[addr([94m_4099)]
                      log 0xd431031d: addr(_4099), stor15[addr(_4099)]
                  else:
                      if stor16[addr([94m_4099)]:
                          mem[0] = addr([94m_4099)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_4099)
                          mem[mem[64] + 32] = stor15[addr([94m_4099)]
                          log 0xd431031d: addr(_4099), stor15[addr(_4099)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_4099)
                          mem[0] = addr([94m_4099)
                          mem[32] = 16
                          stor16[addr([94m_4099)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_4099
                  continue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2654 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2654))
                  call addr([94m_2654).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2871 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2966 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2966] = 12
                  mem[[94m_2966 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_3015 = mem[64]
                  [94mu = [94m_2966 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2966]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2966])] = 256^(-(mem[[94m_2966] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2966])] or mem[[94m_2966 + floor32(mem[[94m_2966]) + 32] and !(256^(-(mem[[94m_2966] % 32) + 32) - 1)
                  mem[[94m_3015 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_3015 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_3015 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2871), 100000 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2871)
                  mem[mem[64] + 96] = 100000 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2871),
                        uint256 amount=100000 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3446 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3446))
                  call addr([94m_3446).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3479 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3510 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3510
                  require ext_code.size(addr([94m_3479))
                  call addr([94m_3479).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3510
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2629 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2631 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3306 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3306) + (32 * mem[96]) + 256
              mem[(32 * [94m_3306) + (32 * [94m_2631) + [94m_2629 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3679 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3306) + (32 * [94m_2631) + [94m_2629 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3679) + (32 * [94m_3306) + (32 * [94m_2631) + [94m_2629 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_4072 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_4072:
                  require [94midx < mem[96]
                  [94m_4102 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_4102))
                  call addr([94m_4102).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_4102)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_4102)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_4102)
                      mem[mem[64] + 32] = stor15[addr([94m_4102)]
                      log 0xd431031d: addr(_4102), stor15[addr(_4102)]
                  else:
                      if stor16[addr([94m_4102)]:
                          mem[0] = addr([94m_4102)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_4102)
                          mem[mem[64] + 32] = stor15[addr([94m_4102)]
                          log 0xd431031d: addr(_4102), stor15[addr(_4102)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_4102)
                          mem[0] = addr([94m_4102)
                          mem[32] = 16
                          stor16[addr([94m_4102)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_4102
                  continue 
  status = 3
  log ChangeStatus(uint8 status=3)
  return 1


# hash = 0x445d1397
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def maxTransfers(): # not payable
  return maxTransfers


# hash = 0x4f64b2be
# getter = ['storage', 160, 0, ['add', ['sha3', 12], ['cd', 4]]]
# const = None
# payable = False
def tokens(uint256 _param1): # not payable
  require _param1 < tokens.length
  return tokens[_param1].field_0


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 10]]]], ['loc', 10]]]
# const = None
# payable = False
def version(): # not payable
  return version[0 len version.length]


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 8, 13]]
# const = None
# payable = False
def paused(): # not payable
  return bool(paused)


# hash = 0x5f677404
# getter = None
# const = ['return', 1000000000000000000]
# payable = False
const INITIAL_VALUE = 10^18


# hash = 0x648aa3b1
# getter = None
# const = None
# payable = False
def getComponentByName(string _name): # not payable
  mem[128 len _name.length] = _name[all]
  mem[ceil32(_name.length) + 128 len floor32(_name.length)] = call.data[_name + 36 len floor32(_name.length)]
  mem[ceil32(_name.length) + floor32(_name.length) + 128] = 256^(-(_name.length % 32) + 32) - 1 and mem[ceil32(_name.length) + floor32(_name.length) + 128] or call.data[_name + floor32(_name.length) + 36 len _name.length % 32], mem[_name.length + 128 len -(_name.length % 32) + 32] and !(256^(-(_name.length % 32) + 32) - 1)
  mem[ceil32(_name.length) + _name.length + 128] = 7
  mem[ceil32(_name.length) + 128] = stor[mem[ceil32(_name.length) + floor32(_name.length) + 128 len (_name.length % 32) + 32]][call.data[_name + 36 len floor32(_name.length)]]
  return memory
    from ceil32(_name.length) + 128
     [93mlen 32


# hash = 0x659eeabc
# getter = None
# const = None
# payable = False
def tokensWithAmount(): # not payable
  [94midx = 0
  [94ms = 0
  while uint8([94midx) < tokens.length:
      mem[0] = tokens[uint8([94midx)].field_0
      mem[32] = 15
      if stor15[stor12[uint8([94midx)].field_0] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  if uint8([94ms):
      mem[128 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
  [94midx = 0
  [94mt = 0
  while uint8([94midx) < tokens.length:
      mem[0] = tokens[uint8([94midx)].field_0
      mem[32] = 15
      if stor15[stor12[uint8([94midx)].field_0] <= 0:
          [94midx = [94midx + 1
          [94mt = [94mt
          continue 
      require uint8([94midx) < tokens.length
      mem[0] = 12
      require uint8([94mt) < uint8([94ms)
      mem[(32 * uint8([94mt)) + 128] = tokens[uint8([94midx)].field_0
      [94midx = [94midx + 1
      [94mt = [94mt + 1
      continue 
  mem[(32 * uint8([94ms)) + 192 len Mask(3, 5, [94ms)] = mem[128 len Mask(3, 5, [94ms)]
  return Array(len=[94ms << 248, data=mem[128 len Mask(3, 5, [94ms)], mem[(32 * uint8([94ms)) + Mask(3, 5, [94ms) + 192 len (32 * uint8([94ms)) - Mask(3, 5, [94ms)]), 


# hash = 0x66188463
# getter = None
# const = None
# payable = False
def decreaseApproval(address _spender, uint256 _subtractedValue): # not payable
  require not paused
  if _subtractedValue <= allowance[caller][addr(_spender)]:
      allowance[caller][addr(_spender)] -= _subtractedValue
  else:
      allowance[caller][addr(_spender)] = 0
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
  require caller == owner
  mem[64] = (32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 256
  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 192] = 16
  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 256 len 0] = None
  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 257 len 15] = 0x45786368616e676550726f76696465
  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 256 len 1] = 0
  mem[(32 * _param4.length) + (32 * _param3.length) + (32 * _param2.length) + 272] = 7
  [94midx = 0
  while [94midx < tokens.length:
      require [94midx < mem[96]
      [94m_149 = mem[(32 * [94midx) + 128]
      require [94midx < mem[(32 * _param2.length) + 128]
      [94m_154 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
      require [94midx < mem[(32 * _param3.length) + (32 * _param2.length) + 160]
      [94m_156 = mem[(32 * [94midx) + (32 * _param3.length) + (32 * _param2.length) + 192]
      [94m_160 = mem[64]
      mem[64] = mem[64] + 64
      mem[[94m_160] = 12
      mem[[94m_160 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
      [94m_163 = mem[64]
      [94mt = [94m_160 + 32
      [94mu = mem[64]
      [94ms = mem[[94m_160]
      while [94ms >= 32:
          mem[[94mu] = mem[[94mt]
          [94mt = [94mt + 32
          [94mu = [94mu + 32
          [94ms = [94ms - 32
          continue 
      mem[mem[64] + floor32(mem[[94m_160])] = 256^(-(mem[[94m_160] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_160])] or mem[[94m_160 + floor32(mem[[94m_160]) + 32] and !(256^(-(mem[[94m_160] % 32) + 32) - 1)
      mem[[94m_163 + 12] = 7
      require ext_code.size(stor[sha3(mem[mem[64] len [94m_163 + -mem[64] + 44])])
      call stor[sha3(mem[mem[64] len [94m_163 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
           gas gas_remaining wei
          args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_149), [94m_154, [94m_156
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[mem[64]] = this.address
      mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
      mem[mem[64] + 64] = addr([94m_149)
      mem[mem[64] + 96] = [94m_154
      mem[mem[64] + 128] = [94m_156
      mem[mem[64] + 160] = bool(ext_call.return_data[0])
      log RiskEvent(
            address sender=addr(this.address),
            address receiver=stor[sha3(0, 0, 7)],
            address tokenAddress=addr(_149),
            uint256 amount=_154,
            uint256 rate=_156,
            bool risky=bool(ext_call.return_data[0]))
      require not ext_call.return_data[0]
      require [94midx < mem[96]
      [94m_230 = mem[(32 * [94midx) + 128]
      mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
      mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
      mem[mem[64] + 36] = 0
      require ext_code.size(addr([94m_230))
      call addr([94m_230).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args stor[sha3(0, 0, 7)], 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require [94midx < mem[96]
      [94m_235 = mem[(32 * [94midx) + 128]
      require [94midx < mem[(32 * _param2.length) + 128]
      [94m_238 = mem[(32 * [94midx) + (32 * _param2.length) + 160]
      mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
      mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
      mem[mem[64] + 36] = [94m_238
      require ext_code.size(addr([94m_235))
      call addr([94m_235).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args stor[sha3(0, 0, 7)], [94m_238
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 
  [94m_145 = mem[64]
  mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
  mem[mem[64] + 100] = this.address
  mem[mem[64] + 132] = _param1
  mem[mem[64] + 164] = 0
  mem[mem[64] + 4] = 192
  mem[mem[64] + 196] = mem[96]
  [94m_147 = mem[96]
  mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  mem[mem[64] + 36] = (32 * mem[96]) + 224
  mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * _param2.length) + 128]
  [94m_209 = mem[(32 * _param2.length) + 128]
  mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * _param2.length) + 128])] = mem[(32 * _param2.length) + 160 len floor32(mem[(32 * _param2.length) + 128])]
  mem[mem[64] + 68] = (32 * [94m_209) + (32 * mem[96]) + 256
  mem[(32 * [94m_209) + (32 * [94m_147) + [94m_145 + 260] = mem[(32 * _param3.length) + (32 * _param2.length) + 160]
  [94m_258 = mem[(32 * _param3.length) + (32 * _param2.length) + 160]
  mem[(32 * [94m_209) + (32 * [94m_147) + [94m_145 + 292 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])] = mem[(32 * _param3.length) + (32 * _param2.length) + 192 len floor32(mem[(32 * _param3.length) + (32 * _param2.length) + 160])]
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
       gas gas_remaining wei
      args mem[mem[64] + 4 len (32 * [94m_258) + (32 * [94m_209) + (32 * [94m_147) + [94m_145 + -mem[64] + 288]
  mem[mem[64]] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  [94m_304 = mem[96]
  [94midx = 0
  [94ms = 0
  while [94midx < [94m_304:
      require [94midx < mem[96]
      [94m_306 = mem[(32 * [94midx) + 128]
      mem[mem[64] + 4] = this.address
      require ext_code.size(addr([94m_306))
      call addr([94m_306).balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[mem[64]] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      stor15[addr([94m_306)] = ext_call.return_data[0]
      if 0 >= ext_call.return_data[0]:
          mem[0] = addr([94m_306)
          mem[32] = 15
          mem[mem[64]] = addr([94m_306)
          mem[mem[64] + 32] = stor15[addr([94m_306)]
          log 0xd431031d: addr(_306), stor15[addr(_306)]
      else:
          if stor16[addr([94m_306)]:
              mem[0] = addr([94m_306)
              mem[32] = 15
              mem[mem[64]] = addr([94m_306)
              mem[mem[64] + 32] = stor15[addr([94m_306)]
              log 0xd431031d: addr(_306), stor15[addr(_306)]
          else:
              tokens.length++
              tokens[tokens.length].field_0 = addr([94m_306)
              mem[0] = addr([94m_306)
              mem[32] = 16
              stor16[addr([94m_306)] = 1
      [94midx = [94midx + 1
      [94ms = [94m_306
      continue 
  return 1


# hash = 0x6e947298
# getter = None
# const = None
# payable = False
def getETHBalance(): # not payable
  return (eth.balance(this.address) - accumulatedFee)


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 3]]]
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
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 8]]]], ['loc', 8]]]
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
      require ext_code.size(stor[sha3(0, 0, 7)])
      call stor[sha3(0, 0, 7)].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
           gas gas_remaining wei
          args caller, addr(this.address), addr(this.address), _value, 10^18
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      log RiskEvent(
            address sender=caller,
            address receiver=addr(this.address),
            address tokenAddress=addr(this.address),
            uint256 amount=_value,
            uint256 rate=10^18,
            bool risky=bool(ext_call.return_data[0]))
  else:
      [94midx = 0
      [94ms = 0
      while uint16([94midx) < tokens.length:
          mem[0] = 12
          mem[164] = this.address
          require ext_code.size(tokens[uint16([94midx)].field_0)
          call tokens[uint16([94midx)].field_0.balanceOf(address owner) with:
               gas gas_remaining wei
              args this.address
          mem[160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0]:
              require uint16([94midx) < tokens.length
              mem[0] = 12
              mem[196] = tokens[uint16([94midx)].field_0
              mem[228] = ext_call.return_data[0]
              mem[260] = 0
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                   gas gas_remaining wei
                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[uint16([94midx)].field_0, ext_call.return_data[0], 0
              mem[160 len 64] = ext_call.return_data[0 len 64]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 64
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          continue 
      require totalSupply
      require ext_code.size(stor[sha3(0, 0, 7)])
      call stor[sha3(0, 0, 7)].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
           gas gas_remaining wei
          args caller, addr(this.address), addr(this.address), _value, (eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      log RiskEvent(
            address sender=caller,
            address receiver=addr(this.address),
            address tokenAddress=addr(this.address),
            uint256 amount=_value,
            uint256 rate=(eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply,
            bool risky=bool(ext_call.return_data[0]))
  require not ext_call.return_data[0]
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].0xc8c01a55 with:
       gas gas_remaining wei
      args caller, _value
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
  while uint16([94midx) < tokens.length:
      mem[0] = 12
      mem[164] = this.address
      require ext_code.size(tokens[uint16([94midx)].field_0)
      call tokens[uint16([94midx)].field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          require uint16([94midx) < tokens.length
          mem[0] = 12
          mem[196] = tokens[uint16([94midx)].field_0
          mem[228] = ext_call.return_data[0]
          mem[260] = 0
          require ext_code.size(stor[sha3(0, 0, 7)])
          call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[uint16([94midx)].field_0, ext_call.return_data[0], 0
          mem[160 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0]
      continue 
  return 0


# hash = 0x7bb25d60
# getter = None
# const = None
# payable = False
def withdrawInProgress(): # not payable
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].isInProgress() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return bool(ext_call.return_data[0])


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  require caller == owner
  require not paused
  paused = 1
  log Pause()


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x918f8674
# getter = None
# const = ['return', 100000]
# payable = False
const DENOMINATOR = 100000


# hash = 0x9375206a
# getter = None
# const = None
# payable = False
def setAllowed(address[] _accounts, uint8 _key, bool _allowed): # not payable
  require caller == owner
  require _key <= 1
  mem[(32 * _accounts.length) + 324 len floor32(_accounts.length)] = call.data[_accounts + 36 len floor32(_accounts.length)]
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].setAllowed(address[] accounts, uint8 key, bool allowed) with:
       gas gas_remaining wei
      args Array(len=_accounts.length, data=call.data[_accounts + 36 len floor32(_accounts.length)], mem[(32 * _accounts.length) + floor32(_accounts.length) + 324 len (32 * _accounts.length) - floor32(_accounts.length)]), _key << 248, _allowed
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 1


# hash = 0x95bc9538
# getter = None
# const = None
# payable = False
def changeStatus(uint8 _status): # not payable
  require caller == owner
  require _status <= 3
  require _status
  require status <= 3
  require status
  require status <= 3
  require status != 3
  require _status <= 3
  require _status != 3
  require _status <= 3
  status = _status
  require status <= 3
  log ChangeStatus(uint8 status=status)
  return 1


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 2]]]], ['loc', 2]]]
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
  [94midx = 0
  [94ms = 0
  while uint16([94midx) < tokens.length:
      mem[0] = 12
      mem[164] = this.address
      require ext_code.size(tokens[uint16([94midx)].field_0)
      call tokens[uint16([94midx)].field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          require uint16([94midx) < tokens.length
          mem[0] = 12
          mem[196] = tokens[uint16([94midx)].field_0
          mem[228] = ext_call.return_data[0]
          mem[260] = 0
          require ext_code.size(stor[sha3(0, 0, 7)])
          call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[uint16([94midx)].field_0, ext_call.return_data[0], 0
          mem[160 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0]
      continue 
  if totalSupply:
      return ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply)
  revert


# hash = 0x9c2062ad
# getter = None
# const = ['return', ['data', 32, 12, 0]]
# payable = False
const RISK = ''


# hash = 0x9c2b1a95
# getter = None
# const = None
# payable = False
def getManagementFee(): # not payable
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].getFeePercentage() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0xa0ffe7bb
# getter = None
# const = None
# payable = False
def registerInNewMarketplace(): # not payable
  require caller == owner
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].0xdfd92f8a with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  return 1


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address _to, uint256 _value): # not payable
  require not paused
  require _to
  require _value <= balanceOf[caller]
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
      mem[0] = tokens[[94midx].field_0
      mem[32] = 15
      require [94midx < tokens.length
      mem[(32 * [94midx) + 128] = stor15[stor12[[94midx].field_0]
      [94midx = [94midx + 1
      continue 
  if tokens.length:
      mem[(32 * tokens.length) + 160] = addr(tokens.field_0)
      [94midx = (32 * tokens.length) + 160
      [94ms = 0
      while (64 * tokens.length) + 128 > [94midx:
          mem[[94midx + 32] = tokens[[94ms].field_256
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


# hash = 0xaf048c37
# getter = None
# const = None
# payable = False
def enableWhitelist(uint8 _key): # not payable
  require caller == owner
  require _key <= 1
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].0x2f038fd5 with:
       gas gas_remaining wei
      args _key
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0xb50e44b8
# getter = None
# const = ['return', ['data', 32, 16, 151531991519480409511034004871959281664]]
# payable = False
const EXCHANGE = 'r'


# hash = 0xb86ec38f
# getter = None
# const = ['return', ['data', 32, 12, 0]]
# payable = False
const REIMBURSABLE = ''


# hash = 0xbe357616
# getter = None
# const = None
# payable = False
def withdrawFee(uint256 _amount): # not payable
  require caller == owner
  require not paused
  require _amount <= accumulatedFee
  accumulatedFee -= _amount
  call caller with:
     value _amount wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0xc57981b5
# getter = None
# const = ['return', ['data', 32, 11, 0]]
# payable = False
const FEE = ''


# hash = 0xcedc2ce1
# getter = None
# const = None
# payable = False
def setMaxTransfers(uint256 _maxTransfers): # not payable
  require caller == owner
  require _maxTransfers > 0
  maxTransfers = _maxTransfers


# hash = 0xd3c9ad17
# getter = None
# const = ['return', ['data', ['arr', 17, ['mask_shl', 136, 0, 0, "'RebalanceProvider'"]]]]
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


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 5]]]]]
# const = None
# payable = False
def allowance(address _owner, address _spender): # not payable
  return allowance[addr(_owner)][addr(_spender)]


# hash = 0xe8b5e51f
# getter = None
# const = None
# payable = True
def invest() payable: 
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].0xcf46db5b with:
       gas gas_remaining wei
      args 0, caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
       gas gas_remaining wei
      args caller, addr(this.address), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, call.value, 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  log RiskEvent(
        address sender=caller,
        address receiver=addr(this.address),
        address tokenAddress=0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee,
        uint256 amount=call.value,
        uint256 rate=1,
        bool risky=bool(ext_call.return_data[0]))
  require not ext_call.return_data[0]
  require not paused
  require status <= 3
  if status != 1:
      revert with 0, 'The Fund is not active'
  if call.value < 10^15:
      revert with 0, 'Minimum value to invest is 0.001 ETH'
  if totalSupply <= 0:
      require ext_code.size(stor[sha3(0, 0, 7)])
      call stor[sha3(0, 0, 7)].0x8b28ab1e with:
           gas gas_remaining wei
          args caller, call.value
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      accumulatedFee += ext_call.return_data[0]
      balanceOf[caller] += (100000 * call.value) - (100000 * ext_call.return_data[0]) / 10^18 * 10^decimals / 100000
      totalSupply += (100000 * call.value) - (100000 * ext_call.return_data[0]) / 10^18 * 10^decimals / 100000
      log Invested(
            address user=caller,
            uint256 amount=(100000 * call.value) - (100000 * ext_call.return_data[0]) / 10^18 * 10^decimals / 100000)
  else:
      require totalSupply
      if 0 == totalSupply:
          require ext_code.size(stor[sha3(0, 0, 7)])
          call stor[sha3(0, 0, 7)].0x8b28ab1e with:
               gas gas_remaining wei
              args caller, call.value
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require -(call.value * 10^decimals / totalSupply) + 10^18
          accumulatedFee += ext_call.return_data[0]
          balanceOf[caller] += (100000 * call.value) - (100000 * ext_call.return_data[0]) / -(call.value * 10^decimals / totalSupply) + 10^18 * 10^decimals / 100000
          totalSupply += (100000 * call.value) - (100000 * ext_call.return_data[0]) / -(call.value * 10^decimals / totalSupply) + 10^18 * 10^decimals / 100000
          log Invested(
                address user=caller,
                uint256 amount=(100000 * call.value) - (100000 * ext_call.return_data[0]) / -(call.value * 10^decimals / totalSupply) + 10^18 * 10^decimals / 100000)
      else:
          [94midx = 0
          [94ms = 0
          while uint16([94midx) < tokens.length:
              mem[0] = 12
              mem[292] = this.address
              require ext_code.size(tokens[uint16([94midx)].field_0)
              call tokens[uint16([94midx)].field_0.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              mem[288] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0]:
                  require uint16([94midx) < tokens.length
                  mem[0] = 12
                  mem[324] = tokens[uint16([94midx)].field_0
                  mem[356] = ext_call.return_data[0]
                  mem[388] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[uint16([94midx)].field_0, ext_call.return_data[0], 0
                  mem[288 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              continue 
          require totalSupply
          require ext_code.size(stor[sha3(0, 0, 7)])
          call stor[sha3(0, 0, 7)].0x8b28ab1e with:
               gas gas_remaining wei
              args caller, call.value
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (call.value * 10^decimals / totalSupply)
          accumulatedFee += ext_call.return_data[0]
          balanceOf[caller] += (100000 * call.value) - (100000 * ext_call.return_data[0]) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (call.value * 10^decimals / totalSupply) * 10^decimals / 100000
          totalSupply += (100000 * call.value) - (100000 * ext_call.return_data[0]) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (call.value * 10^decimals / totalSupply) * 10^decimals / 100000
          log Invested(
                address user=caller,
                uint256 amount=(100000 * call.value) - (100000 * ext_call.return_data[0]) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (call.value * 10^decimals / totalSupply) * 10^decimals / 100000)
  return 1


# hash = 0xe90f84bd
# getter = None
# const = None
# payable = False
def unknowne90f84bd(uint256 _param1): # not payable
  require caller == owner
  [94midx = 0
  [94ms = 0
  while uint8([94midx) < tokens.length:
      mem[0] = tokens[uint8([94midx)].field_0
      mem[32] = 15
      if stor15[stor12[uint8([94midx)].field_0] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  mem[96] = uint8([94ms)
  if not uint8([94ms):
      [94midx = 0
      [94mt = 0
      while uint8([94midx) < tokens.length:
          mem[0] = tokens[uint8([94midx)].field_0
          mem[32] = 15
          if stor15[stor12[uint8([94midx)].field_0] <= 0:
              [94midx = [94midx + 1
              [94mt = [94mt
              continue 
          require uint8([94midx) < tokens.length
          mem[0] = 12
          require uint8([94mt) < uint8([94ms)
          mem[(32 * uint8([94mt)) + 128] = tokens[uint8([94midx)].field_0
          [94midx = [94midx + 1
          [94mt = [94mt + 1
          continue 
      mem[(32 * uint8([94ms)) + 128] = uint8([94ms)
      if not uint8([94ms):
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2521 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2521))
                  call addr([94m_2521).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = _param1 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param1 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2738 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2810 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2810] = 12
                  mem[[94m_2810 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_2843 = mem[64]
                  [94mu = [94m_2810 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2810]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2810])] = 256^(-(mem[[94m_2810] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2810])] or mem[[94m_2810 + floor32(mem[[94m_2810]) + 32] and !(256^(-(mem[[94m_2810] % 32) + 32) - 1)
                  mem[[94m_2843 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_2843 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_2843 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2738), _param1 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2738)
                  mem[mem[64] + 96] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2738),
                        uint256 amount=_param1 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3274 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3274))
                  call addr([94m_3274).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3314 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3338 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3338
                  require ext_code.size(addr([94m_3314))
                  call addr([94m_3314).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3338
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2489 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2491 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3106 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3106) + (32 * mem[96]) + 256
              mem[(32 * [94m_3106) + (32 * [94m_2491) + [94m_2489 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3482 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3106) + (32 * [94m_2491) + [94m_2489 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3482) + (32 * [94m_3106) + (32 * [94m_2491) + [94m_2489 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_3825 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_3825:
                  require [94midx < mem[96]
                  [94m_3841 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_3841))
                  call addr([94m_3841).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_3841)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3841)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_3841)
                      mem[mem[64] + 32] = stor15[addr([94m_3841)]
                      log 0xd431031d: addr(_3841), stor15[addr(_3841)]
                  else:
                      if stor16[addr([94m_3841)]:
                          mem[0] = addr([94m_3841)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_3841)
                          mem[mem[64] + 32] = stor15[addr([94m_3841)]
                          log 0xd431031d: addr(_3841), stor15[addr(_3841)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_3841)
                          mem[0] = addr([94m_3841)
                          mem[32] = 16
                          stor16[addr([94m_3841)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_3841
                  continue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2524 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2524))
                  call addr([94m_2524).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = _param1 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param1 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2741 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2814 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2814] = 12
                  mem[[94m_2814 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_2847 = mem[64]
                  [94mu = [94m_2814 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2814]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2814])] = 256^(-(mem[[94m_2814] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2814])] or mem[[94m_2814 + floor32(mem[[94m_2814]) + 32] and !(256^(-(mem[[94m_2814] % 32) + 32) - 1)
                  mem[[94m_2847 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_2847 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_2847 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2741), _param1 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2741)
                  mem[mem[64] + 96] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2741),
                        uint256 amount=_param1 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3278 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3278))
                  call addr([94m_3278).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3317 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3342 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3342
                  require ext_code.size(addr([94m_3317))
                  call addr([94m_3317).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3342
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2493 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2495 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3114 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3114) + (32 * mem[96]) + 256
              mem[(32 * [94m_3114) + (32 * [94m_2495) + [94m_2493 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3485 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3114) + (32 * [94m_2495) + [94m_2493 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3485) + (32 * [94m_3114) + (32 * [94m_2495) + [94m_2493 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_3826 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_3826:
                  require [94midx < mem[96]
                  [94m_3844 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_3844))
                  call addr([94m_3844).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_3844)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3844)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_3844)
                      mem[mem[64] + 32] = stor15[addr([94m_3844)]
                      log 0xd431031d: addr(_3844), stor15[addr(_3844)]
                  else:
                      if stor16[addr([94m_3844)]:
                          mem[0] = addr([94m_3844)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_3844)
                          mem[mem[64] + 32] = stor15[addr([94m_3844)]
                          log 0xd431031d: addr(_3844), stor15[addr(_3844)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_3844)
                          mem[0] = addr([94m_3844)
                          mem[32] = 16
                          stor16[addr([94m_3844)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_3844
                  continue 
      else:
          mem[(32 * uint8([94ms)) + 160 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2527 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2527))
                  call addr([94m_2527).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = _param1 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param1 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2744 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2818 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2818] = 12
                  mem[[94m_2818 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_2851 = mem[64]
                  [94mu = [94m_2818 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2818]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2818])] = 256^(-(mem[[94m_2818] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2818])] or mem[[94m_2818 + floor32(mem[[94m_2818]) + 32] and !(256^(-(mem[[94m_2818] % 32) + 32) - 1)
                  mem[[94m_2851 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_2851 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_2851 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2744), _param1 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2744)
                  mem[mem[64] + 96] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2744),
                        uint256 amount=_param1 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3282 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3282))
                  call addr([94m_3282).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3320 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3346 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3346
                  require ext_code.size(addr([94m_3320))
                  call addr([94m_3320).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3346
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2497 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2499 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3122 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3122) + (32 * mem[96]) + 256
              mem[(32 * [94m_3122) + (32 * [94m_2499) + [94m_2497 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3488 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3122) + (32 * [94m_2499) + [94m_2497 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3488) + (32 * [94m_3122) + (32 * [94m_2499) + [94m_2497 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_3827 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_3827:
                  require [94midx < mem[96]
                  [94m_3847 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_3847))
                  call addr([94m_3847).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_3847)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3847)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_3847)
                      mem[mem[64] + 32] = stor15[addr([94m_3847)]
                      log 0xd431031d: addr(_3847), stor15[addr(_3847)]
                  else:
                      if stor16[addr([94m_3847)]:
                          mem[0] = addr([94m_3847)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_3847)
                          mem[mem[64] + 32] = stor15[addr([94m_3847)]
                          log 0xd431031d: addr(_3847), stor15[addr(_3847)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_3847)
                          mem[0] = addr([94m_3847)
                          mem[32] = 16
                          stor16[addr([94m_3847)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_3847
                  continue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2530 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2530))
                  call addr([94m_2530).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = _param1 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param1 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2747 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2822 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2822] = 12
                  mem[[94m_2822 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94mu = [94m_2822 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2822]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2822])] = 256^(-(mem[[94m_2822] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2822])] or mem[[94m_2822 + floor32(mem[[94m_2822]) + 32] and !(256^(-(mem[[94m_2822] % 32) + 32) - 1)
                  require ext_code.size(stor7[mem[mem[64] len 12]])
                  call stor7[mem[mem[64] len 12]].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2747), _param1 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2747)
                  mem[mem[64] + 96] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2747),
                        uint256 amount=_param1 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3286 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3286))
                  call addr([94m_3286).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3323 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3350 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3350
                  require ext_code.size(addr([94m_3323))
                  call addr([94m_3323).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3350
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2501 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2503 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3130 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3130) + (32 * mem[96]) + 256
              mem[(32 * [94m_3130) + (32 * [94m_2503) + [94m_2501 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3491 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3130) + (32 * [94m_2503) + [94m_2501 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3491) + (32 * [94m_3130) + (32 * [94m_2503) + [94m_2501 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_3828 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_3828:
                  require [94midx < mem[96]
                  [94m_3850 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_3850))
                  call addr([94m_3850).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_3850)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3850)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_3850)
                      mem[mem[64] + 32] = stor15[addr([94m_3850)]
                      log 0xd431031d: addr(_3850), stor15[addr(_3850)]
                  else:
                      if stor16[addr([94m_3850)]:
                          mem[0] = addr([94m_3850)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_3850)
                          mem[mem[64] + 32] = stor15[addr([94m_3850)]
                          log 0xd431031d: addr(_3850), stor15[addr(_3850)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_3850)
                          mem[0] = addr([94m_3850)
                          mem[32] = 16
                          stor16[addr([94m_3850)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_3850
                  continue 
  else:
      mem[128 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
      [94midx = 0
      [94mt = 0
      while uint8([94midx) < tokens.length:
          mem[0] = tokens[uint8([94midx)].field_0
          mem[32] = 15
          if stor15[stor12[uint8([94midx)].field_0] <= 0:
              [94midx = [94midx + 1
              [94mt = [94mt
              continue 
          require uint8([94midx) < tokens.length
          mem[0] = 12
          require uint8([94mt) < uint8([94ms)
          mem[(32 * uint8([94mt)) + 128] = tokens[uint8([94midx)].field_0
          [94midx = [94midx + 1
          [94mt = [94mt + 1
          continue 
      mem[(32 * uint8([94ms)) + 128] = uint8([94ms)
      if not uint8([94ms):
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2533 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2533))
                  call addr([94m_2533).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = _param1 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param1 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2750 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2826 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2826] = 12
                  mem[[94m_2826 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94mu = [94m_2826 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2826]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2826])] = 256^(-(mem[[94m_2826] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2826])] or mem[[94m_2826 + floor32(mem[[94m_2826]) + 32] and !(256^(-(mem[[94m_2826] % 32) + 32) - 1)
                  require ext_code.size(stor7[mem[mem[64] len 12]])
                  call stor7[mem[mem[64] len 12]].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2750), _param1 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2750)
                  mem[mem[64] + 96] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2750),
                        uint256 amount=_param1 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3290 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3290))
                  call addr([94m_3290).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3326 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3354 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3354
                  require ext_code.size(addr([94m_3326))
                  call addr([94m_3326).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3354
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2505 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2507 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3138 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3138) + (32 * mem[96]) + 256
              mem[(32 * [94m_3138) + (32 * [94m_2507) + [94m_2505 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3494 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3138) + (32 * [94m_2507) + [94m_2505 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3494) + (32 * [94m_3138) + (32 * [94m_2507) + [94m_2505 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_3829 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_3829:
                  require [94midx < mem[96]
                  [94m_3853 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_3853))
                  call addr([94m_3853).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_3853)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3853)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_3853)
                      mem[mem[64] + 32] = stor15[addr([94m_3853)]
                      log 0xd431031d: addr(_3853), stor15[addr(_3853)]
                  else:
                      if stor16[addr([94m_3853)]:
                          mem[0] = addr([94m_3853)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_3853)
                          mem[mem[64] + 32] = stor15[addr([94m_3853)]
                          log 0xd431031d: addr(_3853), stor15[addr(_3853)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_3853)
                          mem[0] = addr([94m_3853)
                          mem[32] = 16
                          stor16[addr([94m_3853)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_3853
                  continue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2536 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2536))
                  call addr([94m_2536).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = _param1 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param1 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2753 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2830 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2830] = 12
                  mem[[94m_2830 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_2863 = mem[64]
                  [94mu = [94m_2830 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2830]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2830])] = 256^(-(mem[[94m_2830] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2830])] or mem[[94m_2830 + floor32(mem[[94m_2830]) + 32] and !(256^(-(mem[[94m_2830] % 32) + 32) - 1)
                  mem[[94m_2863 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_2863 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_2863 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2753), _param1 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2753)
                  mem[mem[64] + 96] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2753),
                        uint256 amount=_param1 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3294 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3294))
                  call addr([94m_3294).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3329 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3358 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3358
                  require ext_code.size(addr([94m_3329))
                  call addr([94m_3329).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3358
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2509 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2511 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3146 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3146) + (32 * mem[96]) + 256
              mem[(32 * [94m_3146) + (32 * [94m_2511) + [94m_2509 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3497 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3146) + (32 * [94m_2511) + [94m_2509 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3497) + (32 * [94m_3146) + (32 * [94m_2511) + [94m_2509 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_3830 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_3830:
                  require [94midx < mem[96]
                  [94m_3856 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_3856))
                  call addr([94m_3856).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_3856)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3856)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_3856)
                      mem[mem[64] + 32] = stor15[addr([94m_3856)]
                      log 0xd431031d: addr(_3856), stor15[addr(_3856)]
                  else:
                      if stor16[addr([94m_3856)]:
                          mem[0] = addr([94m_3856)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_3856)
                          mem[mem[64] + 32] = stor15[addr([94m_3856)]
                          log 0xd431031d: addr(_3856), stor15[addr(_3856)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_3856)
                          mem[0] = addr([94m_3856)
                          mem[32] = 16
                          stor16[addr([94m_3856)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_3856
                  continue 
      else:
          mem[(32 * uint8([94ms)) + 160 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2539 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2539))
                  call addr([94m_2539).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = _param1 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param1 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2756 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2834 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2834] = 12
                  mem[[94m_2834 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_2867 = mem[64]
                  [94mu = [94m_2834 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2834]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2834])] = 256^(-(mem[[94m_2834] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2834])] or mem[[94m_2834 + floor32(mem[[94m_2834]) + 32] and !(256^(-(mem[[94m_2834] % 32) + 32) - 1)
                  mem[[94m_2867 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_2867 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_2867 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2756), _param1 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2756)
                  mem[mem[64] + 96] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2756),
                        uint256 amount=_param1 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3298 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3298))
                  call addr([94m_3298).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3332 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3362 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3362
                  require ext_code.size(addr([94m_3332))
                  call addr([94m_3332).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3362
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2513 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2515 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3154 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3154) + (32 * mem[96]) + 256
              mem[(32 * [94m_3154) + (32 * [94m_2515) + [94m_2513 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3500 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3154) + (32 * [94m_2515) + [94m_2513 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3500) + (32 * [94m_3154) + (32 * [94m_2515) + [94m_2513 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_3831 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_3831:
                  require [94midx < mem[96]
                  [94m_3859 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_3859))
                  call addr([94m_3859).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_3859)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3859)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_3859)
                      mem[mem[64] + 32] = stor15[addr([94m_3859)]
                      log 0xd431031d: addr(_3859), stor15[addr(_3859)]
                  else:
                      if stor16[addr([94m_3859)]:
                          mem[0] = addr([94m_3859)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_3859)
                          mem[mem[64] + 32] = stor15[addr([94m_3859)]
                          log 0xd431031d: addr(_3859), stor15[addr(_3859)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_3859)
                          mem[0] = addr([94m_3859)
                          mem[32] = 16
                          stor16[addr([94m_3859)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_3859
                  continue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[21952 len 32 * uint8([94ms)]
              mem[64] = (3 * 32 * uint8([94ms)) + 256
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 7
              [94mt = 0
              while [94mt < uint8([94ms):
                  require [94mt < mem[96]
                  [94m_2542 = mem[(32 * [94mt) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_2542))
                  call addr([94m_2542).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[(32 * uint8([94ms)) + (32 * [94mt) + 160] = _param1 * ext_call.return_data[0] / 100000
                  require [94mt < mem[96]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  mem[mem[64] + 4] = mem[(32 * [94mt) + 140 len 20]
                  mem[mem[64] + 36] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[mem[64] + 68] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 100] = 0
                  require ext_code.size(stor[sha3(0, 0, 7)])
                  call stor[sha3(0, 0, 7)].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[mem[64] + 4], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param1 * ext_call.return_data[0] / 100000, 0
                  mem[mem[64] len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  mem[(32 * [94mt) + (64 * uint8([94ms)) + 192] = ext_call.return_data[32]
                  require [94mt < mem[96]
                  [94m_2759 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  require [94mt < mem[(64 * uint8([94ms)) + 160]
                  [94m_2838 = mem[64]
                  mem[64] = mem[64] + 64
                  mem[[94m_2838] = 12
                  mem[[94m_2838 + 32] = 0x5269736b50726f766964657200000000000000000000000000000000000000
                  [94m_2871 = mem[64]
                  [94mu = [94m_2838 + 32
                  [94mv = mem[64]
                  [94midx = mem[[94m_2838]
                  while [94midx >= 32:
                      mem[[94mv] = mem[[94mu]
                      [94mu = [94mu + 32
                      [94mv = [94mv + 32
                      [94midx = [94midx - 32
                      continue 
                  mem[mem[64] + floor32(mem[[94m_2838])] = 256^(-(mem[[94m_2838] % 32) + 32) - 1 and mem[mem[64] + floor32(mem[[94m_2838])] or mem[[94m_2838 + floor32(mem[[94m_2838]) + 32] and !(256^(-(mem[[94m_2838] % 32) + 32) - 1)
                  mem[[94m_2871 + 12] = 7
                  require ext_code.size(stor[sha3(mem[mem[64] len [94m_2871 + -mem[64] + 44])])
                  call stor[sha3(mem[mem[64] len [94m_2871 + -mem[64] + 44])].hasRisk(address sender, address receiver, address tokenAddress, uint256 amount, uint256 rate) with:
                       gas gas_remaining wei
                      args addr(this.address), stor[sha3(0, 0, 7)], addr([94m_2759), _param1 * ext_call.return_data[0] / 100000, ext_call.return_data[32]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[mem[64]] = this.address
                  mem[mem[64] + 32] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 64] = addr([94m_2759)
                  mem[mem[64] + 96] = _param1 * ext_call.return_data[0] / 100000
                  mem[mem[64] + 128] = ext_call.return_data[32]
                  mem[mem[64] + 160] = bool(ext_call.return_data[0])
                  log RiskEvent(
                        address sender=addr(this.address),
                        address receiver=stor[sha3(0, 0, 7)],
                        address tokenAddress=addr(_2759),
                        uint256 amount=_param1 * ext_call.return_data[0] / 100000,
                        uint256 rate=ext_call.return_data[32],
                        bool risky=bool(ext_call.return_data[0]))
                  require not ext_call.return_data[0]
                  require [94mt < mem[96]
                  [94m_3302 = mem[(32 * [94mt) + 128]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = 0
                  require ext_code.size(addr([94m_3302))
                  call addr([94m_3302).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < mem[96]
                  [94m_3335 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * uint8([94ms)) + 128]
                  [94m_3366 = mem[(32 * [94mt) + (32 * uint8([94ms)) + 160]
                  mem[mem[64]] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[mem[64] + 4] = stor[sha3(0, 0, 7)]
                  mem[mem[64] + 36] = [94m_3366
                  require ext_code.size(addr([94m_3335))
                  call addr([94m_3335).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args stor[sha3(0, 0, 7)], [94m_3366
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  continue 
              [94m_2517 = mem[64]
              mem[mem[64]] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 100] = this.address
              mem[mem[64] + 132] = 0
              mem[mem[64] + 164] = 0
              mem[mem[64] + 4] = 192
              mem[mem[64] + 196] = mem[96]
              [94m_2519 = mem[96]
              mem[mem[64] + 228 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
              mem[mem[64] + 36] = (32 * mem[96]) + 224
              mem[(32 * mem[96]) + mem[64] + 228] = mem[(32 * uint8([94ms)) + 128]
              [94m_3162 = mem[(32 * uint8([94ms)) + 128]
              mem[(32 * mem[96]) + mem[64] + 260 len floor32(mem[(32 * uint8([94ms)) + 128])] = mem[(32 * uint8([94ms)) + 160 len floor32(mem[(32 * uint8([94ms)) + 128])]
              mem[mem[64] + 68] = (32 * [94m_3162) + (32 * mem[96]) + 256
              mem[(32 * [94m_3162) + (32 * [94m_2519) + [94m_2517 + 260] = mem[(64 * uint8([94ms)) + 160]
              [94m_3503 = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * [94m_3162) + (32 * [94m_2519) + [94m_2517 + 292 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(stor[sha3(0, 0, 7)])
              call stor[sha3(0, 0, 7)].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args mem[mem[64] + 4 len (32 * [94m_3503) + (32 * [94m_3162) + (32 * [94m_2519) + [94m_2517 + -mem[64] + 288]
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94m_3832 = mem[96]
              [94midx = 0
              [94ms = 0
              while [94midx < [94m_3832:
                  require [94midx < mem[96]
                  [94m_3862 = mem[(32 * [94midx) + 128]
                  mem[mem[64] + 4] = this.address
                  require ext_code.size(addr([94m_3862))
                  call addr([94m_3862).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[mem[64]] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  stor15[addr([94m_3862)] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3862)
                      mem[32] = 15
                      mem[mem[64]] = addr([94m_3862)
                      mem[mem[64] + 32] = stor15[addr([94m_3862)]
                      log 0xd431031d: addr(_3862), stor15[addr(_3862)]
                  else:
                      if stor16[addr([94m_3862)]:
                          mem[0] = addr([94m_3862)
                          mem[32] = 15
                          mem[mem[64]] = addr([94m_3862)
                          mem[mem[64] + 32] = stor15[addr([94m_3862)]
                          log 0xd431031d: addr(_3862), stor15[addr(_3862)]
                      else:
                          tokens.length++
                          tokens[tokens.length].field_0 = addr([94m_3862)
                          mem[0] = addr([94m_3862)
                          mem[32] = 16
                          stor16[addr([94m_3862)] = 1
                  [94midx = [94midx + 1
                  [94ms = [94m_3862
                  continue 


# hash = 0xef430aa6
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 9]]]], ['loc', 9]]]
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
# const = ['return', ['data', 32, 14, 0]]
# payable = False
const MARKET = ''


# hash = 0xf8ce3164
# getter = ['storage', 256, 0, 18]
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
  require ext_code.size(stor[sha3(0, 0, 7)])
  call stor[sha3(0, 0, 7)].setFeePercentage(uint256 newFee) with:
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


