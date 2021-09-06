# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xb83894Ea21781f947D8DbF1cA102117DCDDf0d05 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x3ccfd60b': 'withdraw()'} 

# storage definitions
def storage:
    # storage address 0
    decimals # mask: a s
    # storage address 1
    name
    # storage address 2
    symbol
    # storage address 3
    owner # mask: a s
    # storage address 4
    stor4
    # storage address 5
    description
    # storage address 6
    category
    # storage address 7
    version
    # storage address 8
    fundType # mask: a s
    # storage address 9
    tokens
    # storage address 10
    status # mask: a s
    # storage address 11
    balanceOf
    # storage address 12
    totalSupply # mask: a s
    # storage address 13
    allowance
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
  require caller == mowner
  maccumulatedFee += call.value


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 1]]]], ['loc', 1]]]
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


# hash = 0x16ba7197
# getter = None
# const = ['return', ['data', 32, 16, 151531991519480409511034004871959281664]]
# payable = False
const WITHDRAW = 'r'


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 12]
# const = None
# payable = False
def totalSupply(): # not payable
  return mtotalSupply


# hash = 0x1bb7cc99
# getter = None
# const = ['return', ['data', 32, 17, 34163080641509995819850397732846667038720]]
# payable = False
const WHITELIST = 'der'


# hash = 0x1ed374c6
# getter = None
# const = None
# payable = False
def disableWhitelist(uint8 m_key): # not payable
  require caller == mowner
  require m_key <= 1
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].0x42340458 with:
       gas gas_remaining wei
      args m_key
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  return 1


# hash = 0x1fa98406
# getter = ['storage', 8, 0, 8]
# const = None
# payable = False
def fundType(): # not payable
  require mfundType <= 1
  return mfundType


# hash = 0x200d2ed2
# getter = ['storage', 8, 0, 10]
# const = None
# payable = False
def status(): # not payable
  require mstatus <= 3
  return mstatus


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_value): # not payable
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


# hash = 0x313ce567
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def decimals(): # not payable
  return mdecimals


# hash = 0x36642c21
# getter = None
# const = None
# payable = False
def unknown36642c21(): # not payable
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].0xc77e7614 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x3c98d189
# getter = None
# const = None
# payable = False
def unknown3c98d189(uint256 m_param1, array m_param2, array m_param3, array m_param4): # not payable
  mem[128 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param2.length) + 128] = m_param3.length
  mem[(32 * m_param2.length) + 160 len 32 * m_param3.length] = call.data[m_param3 + 36 len 32 * m_param3.length]
  mem[(32 * m_param3.length) + (32 * m_param2.length) + 160] = m_param4.length
  mem[(32 * m_param3.length) + (32 * m_param2.length) + 192 len 32 * m_param4.length] = call.data[m_param4 + 36 len 32 * m_param4.length]
  require caller == mowner
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_param3.lengthm:
      require [94midx < m_param3.length
      [94midx = [94midx + 1
      [94ms = [94ms + mem[(32 * [94midx) + (32 * m_param2.length) + 160]
      mcontinue 
  require eth.balance(this.address) - maccumulatedFee >= [94ms * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = 16
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256 len 0] = None
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 356] = this.address
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 388] = m_param1
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 420] = 0
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = 192
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 452] = m_param2.length
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 484 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = (32 * m_param2.length) + 224
  mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 484] = m_param3.length
  mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 516 len floor32(m_param3.length)] = call.data[m_param3 + 36 len floor32(m_param3.length)]
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = (32 * m_param3.length) + (32 * m_param2.length) + 256
  mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 516] = m_param4.length
  mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 548 len floor32(m_param4.length)] = call.data[m_param4 + 36 len floor32(m_param4.length)]
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].buyTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
     value [94ms * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length * m_param3.length wei
       gas gas_remaining wei
      args 192, (32 * m_param2.length) + 224, (32 * m_param3.length) + (32 * m_param2.length) + 256, addr(this.address), m_param1, 0, m_param2.length, call.data[m_param2 + 36 len floor32(m_param2.length)], mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + floor32(m_param2.length) + 484 len (32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + -floor32(m_param2.length) + 64]
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_param2.lengthm:
      require [94midx < m_param2.length
      [94m_205 = mem[(32 * [94midx) + 128]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = this.address
      require ext_code.size(addr([94m_205))
      call addr([94m_205).balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mstor15m[addr([94m_205)m] = ext_call.return_data[0]
      if 0 >= ext_call.return_data[0]:
          mem[0] = addr([94m_205)
          mem[32] = 15
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256] = addr([94m_205)
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 288] = mstor15m[addr([94m_205)m]
          log 0xd431031d: addr(_205), stor15[addr(_205)]
      else:
          if mstor16m[addr([94m_205)m]:
              mem[0] = addr([94m_205)
              mem[32] = 15
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256] = addr([94m_205)
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 288] = mstor15m[addr([94m_205)m]
              log 0xd431031d: addr(_205), stor15[addr(_205)]
          else:
              mtokensm.length++
              mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_205)
              mem[0] = addr([94m_205)
              mem[32] = 16
              mstor16m[addr([94m_205)m] = 1
      [94midx = [94midx + 1
      [94ms = [94m_205
      mcontinue 
  return 1


# hash = 0x43d726d6
# getter = None
# const = None
# payable = False
def close(): # not payable
  require caller == mowner
  require mstatus <= 3
  require mstatus
  [94midx = 0
  [94ms = 0
  mwhile uint8([94midx) < mtokensm.lengthm:
      mem[0] = mtokensm[uint8([94midx)m]m.field_0
      mem[32] = 15
      if mstor15m[mstor9m[uint8([94midx)m]m.field_0m] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  if not uint8([94ms):
      [94midx = 0
      [94mt = 0
      mwhile uint8([94midx) < mtokensm.lengthm:
          mem[0] = mtokensm[uint8([94midx)m]m.field_0
          mem[32] = 15
          if mstor15m[mstor9m[uint8([94midx)m]m.field_0m] <= 0:
              [94midx = [94midx + 1
              [94mt = [94mt
              mcontinue 
          require uint8([94midx) < mtokensm.length
          mem[0] = 9
          require uint8([94mt) < uint8([94ms)
          mem[(32 * uint8([94mt)) + 128] = mtokensm[uint8([94midx)m]m.field_0
          [94midx = [94midx + 1
          [94mt = [94mt + 1
          mcontinue 
      mem[(32 * uint8([94ms)) + 128] = uint8([94ms)
      if not uint8([94ms):
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 4
              [94mt = 0
              mwhile uint8([94mt) < uint8([94ms)m:
                  require uint8([94mt) < uint8([94ms)
                  [94m_1933 = mem[(32 * uint8([94mt)) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_1933))
                  call addr([94m_1933).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require uint8([94mt) < uint8([94ms)
                  mem[(32 * uint8([94ms)) + (32 * uint8([94mt)) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require uint8([94mt) < uint8([94ms)
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mem[(32 * uint8([94mt)) + 140 len 20]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * uint8([94ms)) + 324] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(mstor[sha3(0, 0, 4)m])
                  call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * uint8([94ms)) + 260], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, mem[(3 * 32 * uint8([94ms)) + 356]
                  mem[(3 * 32 * uint8([94ms)) + 256 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require uint8([94mt) < mem[(64 * uint8([94ms)) + 160]
                  mem[(64 * uint8([94ms)) + (32 * uint8([94mt)) + 192] = ext_call.return_data[32]
                  require uint8([94mt) < uint8([94ms)
                  [94m_2150 = mem[(32 * uint8([94mt)) + 128]
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mstor[sha3(0, 0, 4)m]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(addr([94m_2150))
                  call addr([94m_2150).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args mstor[sha3(0, 0, 4)m], 100000 * ext_call.return_data[0] / 100000
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * uint8([94ms)) + 256] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 356] = this.address
              mem[(3 * 32 * uint8([94ms)) + 420] = 0
              mem[(3 * 32 * uint8([94ms)) + 260] = 192
              mem[(3 * 32 * uint8([94ms)) + 452] = uint8([94ms)
              mem[(3 * 32 * uint8([94ms)) + 484 len Mask(3, 5, [94ms)] = mem[128 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 292] = (32 * uint8([94ms)) + 224
              mem[(uint8([94ms) << 7) + 484] = uint8([94ms)
              mem[(uint8([94ms) << 7) + 516 len Mask(3, 5, [94ms)] = mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 324] = (64 * uint8([94ms)) + 256
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 516] = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 548 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(mstor[sha3(0, 0, 4)m])
              call mstor[sha3(0, 0, 4)m].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args 192, (32 * uint8([94ms)) + 224, (64 * uint8([94ms)) + 256, addr(this.address), mem[(3 * 32 * uint8([94ms)) + 388], 0, [94ms << 248, mem[128 len Mask(3, 5, [94ms)], mem[(3 * 32 * uint8([94ms)) + Mask(3, 5, [94ms) + 484 len (uint8([94ms) << 7) + (-3 * 32 * uint8([94ms)) + -Mask(3, 5, [94ms) + 32], mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)], mem[Mask(3, 5, [94ms) + (uint8([94ms) << 7) + 516 len (32 * mem[(64 * uint8([94ms)) + 160]) + (64 * uint8([94ms)) + -Mask(3, 5, [94ms) + -(uint8([94ms) << 7) + (3 * 32 * uint8([94ms)) + 32]
              mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < uint8([94ms)m:
                  require [94mt < uint8([94ms)
                  [94m_3013 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_3013))
                  call addr([94m_3013).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15m[addr([94m_3013)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3013)
                      mem[32] = 15
                      mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3013)
                      mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3013)m]
                      log 0xd431031d: addr(_3013), stor15[addr(_3013)]
                  else:
                      if mstor16m[addr([94m_3013)m]:
                          mem[0] = addr([94m_3013)
                          mem[32] = 15
                          mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3013)
                          mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3013)m]
                          log 0xd431031d: addr(_3013), stor15[addr(_3013)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_3013)
                          mem[0] = addr([94m_3013)
                          mem[32] = 16
                          mstor16m[addr([94m_3013)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_3013
                  mcontinue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[17449 len 32 * uint8([94ms)]
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 4
              [94mt = 0
              mwhile uint8([94mt) < uint8([94ms)m:
                  require uint8([94mt) < uint8([94ms)
                  [94m_1936 = mem[(32 * uint8([94mt)) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_1936))
                  call addr([94m_1936).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require uint8([94mt) < uint8([94ms)
                  mem[(32 * uint8([94ms)) + (32 * uint8([94mt)) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require uint8([94mt) < uint8([94ms)
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mem[(32 * uint8([94mt)) + 140 len 20]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * uint8([94ms)) + 324] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(mstor[sha3(0, 0, 4)m])
                  call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * uint8([94ms)) + 260], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, mem[(3 * 32 * uint8([94ms)) + 356]
                  mem[(3 * 32 * uint8([94ms)) + 256 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require uint8([94mt) < mem[(64 * uint8([94ms)) + 160]
                  mem[(64 * uint8([94ms)) + (32 * uint8([94mt)) + 192] = ext_call.return_data[32]
                  require uint8([94mt) < uint8([94ms)
                  [94m_2153 = mem[(32 * uint8([94mt)) + 128]
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mstor[sha3(0, 0, 4)m]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(addr([94m_2153))
                  call addr([94m_2153).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args mstor[sha3(0, 0, 4)m], 100000 * ext_call.return_data[0] / 100000
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * uint8([94ms)) + 256] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 356] = this.address
              mem[(3 * 32 * uint8([94ms)) + 420] = 0
              mem[(3 * 32 * uint8([94ms)) + 260] = 192
              mem[(3 * 32 * uint8([94ms)) + 452] = uint8([94ms)
              mem[(3 * 32 * uint8([94ms)) + 484 len Mask(3, 5, [94ms)] = mem[128 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 292] = (32 * uint8([94ms)) + 224
              mem[(uint8([94ms) << 7) + 484] = uint8([94ms)
              mem[(uint8([94ms) << 7) + 516 len Mask(3, 5, [94ms)] = mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 324] = (64 * uint8([94ms)) + 256
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 516] = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 548 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(mstor[sha3(0, 0, 4)m])
              call mstor[sha3(0, 0, 4)m].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args 192, (32 * uint8([94ms)) + 224, (64 * uint8([94ms)) + 256, addr(this.address), mem[(3 * 32 * uint8([94ms)) + 388], 0, [94ms << 248, mem[128 len Mask(3, 5, [94ms)], mem[(3 * 32 * uint8([94ms)) + Mask(3, 5, [94ms) + 484 len (uint8([94ms) << 7) + (-3 * 32 * uint8([94ms)) + -Mask(3, 5, [94ms) + 32], mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)], mem[Mask(3, 5, [94ms) + (uint8([94ms) << 7) + 516 len (32 * mem[(64 * uint8([94ms)) + 160]) + (64 * uint8([94ms)) + -Mask(3, 5, [94ms) + -(uint8([94ms) << 7) + (3 * 32 * uint8([94ms)) + 32]
              mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < uint8([94ms)m:
                  require [94mt < uint8([94ms)
                  [94m_3016 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_3016))
                  call addr([94m_3016).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15m[addr([94m_3016)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3016)
                      mem[32] = 15
                      mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3016)
                      mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3016)m]
                      log 0xd431031d: addr(_3016), stor15[addr(_3016)]
                  else:
                      if mstor16m[addr([94m_3016)m]:
                          mem[0] = addr([94m_3016)
                          mem[32] = 15
                          mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3016)
                          mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3016)m]
                          log 0xd431031d: addr(_3016), stor15[addr(_3016)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_3016)
                          mem[0] = addr([94m_3016)
                          mem[32] = 16
                          mstor16m[addr([94m_3016)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_3016
                  mcontinue 
      else:
          mem[(32 * uint8([94ms)) + 160 len 32 * uint8([94ms)] = code.data[17449 len 32 * uint8([94ms)]
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 4
              [94mt = 0
              mwhile uint8([94mt) < uint8([94ms)m:
                  require uint8([94mt) < uint8([94ms)
                  [94m_1939 = mem[(32 * uint8([94mt)) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_1939))
                  call addr([94m_1939).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require uint8([94mt) < uint8([94ms)
                  mem[(32 * uint8([94ms)) + (32 * uint8([94mt)) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require uint8([94mt) < uint8([94ms)
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mem[(32 * uint8([94mt)) + 140 len 20]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * uint8([94ms)) + 324] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(mstor[sha3(0, 0, 4)m])
                  call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * uint8([94ms)) + 260], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, mem[(3 * 32 * uint8([94ms)) + 356]
                  mem[(3 * 32 * uint8([94ms)) + 256 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require uint8([94mt) < mem[(64 * uint8([94ms)) + 160]
                  mem[(64 * uint8([94ms)) + (32 * uint8([94mt)) + 192] = ext_call.return_data[32]
                  require uint8([94mt) < uint8([94ms)
                  [94m_2156 = mem[(32 * uint8([94mt)) + 128]
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mstor[sha3(0, 0, 4)m]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(addr([94m_2156))
                  call addr([94m_2156).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args mstor[sha3(0, 0, 4)m], 100000 * ext_call.return_data[0] / 100000
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * uint8([94ms)) + 256] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 356] = this.address
              mem[(3 * 32 * uint8([94ms)) + 420] = 0
              mem[(3 * 32 * uint8([94ms)) + 260] = 192
              mem[(3 * 32 * uint8([94ms)) + 452] = uint8([94ms)
              mem[(3 * 32 * uint8([94ms)) + 484 len Mask(3, 5, [94ms)] = mem[128 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 292] = (32 * uint8([94ms)) + 224
              mem[(uint8([94ms) << 7) + 484] = uint8([94ms)
              mem[(uint8([94ms) << 7) + 516 len Mask(3, 5, [94ms)] = mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 324] = (64 * uint8([94ms)) + 256
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 516] = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 548 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(mstor[sha3(0, 0, 4)m])
              call mstor[sha3(0, 0, 4)m].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args 192, (32 * uint8([94ms)) + 224, (64 * uint8([94ms)) + 256, addr(this.address), mem[(3 * 32 * uint8([94ms)) + 388], 0, [94ms << 248, mem[128 len Mask(3, 5, [94ms)], mem[(3 * 32 * uint8([94ms)) + Mask(3, 5, [94ms) + 484 len (uint8([94ms) << 7) + (-3 * 32 * uint8([94ms)) + -Mask(3, 5, [94ms) + 32], mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)], mem[Mask(3, 5, [94ms) + (uint8([94ms) << 7) + 516 len (32 * mem[(64 * uint8([94ms)) + 160]) + (64 * uint8([94ms)) + -Mask(3, 5, [94ms) + -(uint8([94ms) << 7) + (3 * 32 * uint8([94ms)) + 32]
              mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < uint8([94ms)m:
                  require [94mt < uint8([94ms)
                  [94m_3019 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_3019))
                  call addr([94m_3019).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15m[addr([94m_3019)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3019)
                      mem[32] = 15
                      mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3019)
                      mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3019)m]
                      log 0xd431031d: addr(_3019), stor15[addr(_3019)]
                  else:
                      if mstor16m[addr([94m_3019)m]:
                          mem[0] = addr([94m_3019)
                          mem[32] = 15
                          mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3019)
                          mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3019)m]
                          log 0xd431031d: addr(_3019), stor15[addr(_3019)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_3019)
                          mem[0] = addr([94m_3019)
                          mem[32] = 16
                          mstor16m[addr([94m_3019)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_3019
                  mcontinue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[17449 len 32 * uint8([94ms)]
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 4
              [94mt = 0
              mwhile uint8([94mt) < uint8([94ms)m:
                  require uint8([94mt) < uint8([94ms)
                  [94m_1942 = mem[(32 * uint8([94mt)) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_1942))
                  call addr([94m_1942).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require uint8([94mt) < uint8([94ms)
                  mem[(32 * uint8([94ms)) + (32 * uint8([94mt)) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require uint8([94mt) < uint8([94ms)
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mem[(32 * uint8([94mt)) + 140 len 20]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * uint8([94ms)) + 324] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(mstor[sha3(0, 0, 4)m])
                  call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * uint8([94ms)) + 260], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, mem[(3 * 32 * uint8([94ms)) + 356]
                  mem[(3 * 32 * uint8([94ms)) + 256 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require uint8([94mt) < mem[(64 * uint8([94ms)) + 160]
                  mem[(64 * uint8([94ms)) + (32 * uint8([94mt)) + 192] = ext_call.return_data[32]
                  require uint8([94mt) < uint8([94ms)
                  [94m_2159 = mem[(32 * uint8([94mt)) + 128]
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mstor[sha3(0, 0, 4)m]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(addr([94m_2159))
                  call addr([94m_2159).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args mstor[sha3(0, 0, 4)m], 100000 * ext_call.return_data[0] / 100000
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * uint8([94ms)) + 256] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 356] = this.address
              mem[(3 * 32 * uint8([94ms)) + 420] = 0
              mem[(3 * 32 * uint8([94ms)) + 260] = 192
              mem[(3 * 32 * uint8([94ms)) + 452] = uint8([94ms)
              mem[(3 * 32 * uint8([94ms)) + 484 len Mask(3, 5, [94ms)] = mem[128 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 292] = (32 * uint8([94ms)) + 224
              mem[(uint8([94ms) << 7) + 484] = uint8([94ms)
              mem[(uint8([94ms) << 7) + 516 len Mask(3, 5, [94ms)] = mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 324] = (64 * uint8([94ms)) + 256
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 516] = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 548 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(mstor[sha3(0, 0, 4)m])
              call mstor[sha3(0, 0, 4)m].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args 192, (32 * uint8([94ms)) + 224, (64 * uint8([94ms)) + 256, addr(this.address), mem[(3 * 32 * uint8([94ms)) + 388], 0, [94ms << 248, mem[128 len Mask(3, 5, [94ms)], mem[(3 * 32 * uint8([94ms)) + Mask(3, 5, [94ms) + 484 len (uint8([94ms) << 7) + (-3 * 32 * uint8([94ms)) + -Mask(3, 5, [94ms) + 32], mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)], mem[Mask(3, 5, [94ms) + (uint8([94ms) << 7) + 516 len (32 * mem[(64 * uint8([94ms)) + 160]) + (64 * uint8([94ms)) + -Mask(3, 5, [94ms) + -(uint8([94ms) << 7) + (3 * 32 * uint8([94ms)) + 32]
              mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < uint8([94ms)m:
                  require [94mt < uint8([94ms)
                  [94m_3022 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_3022))
                  call addr([94m_3022).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15m[addr([94m_3022)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3022)
                      mem[32] = 15
                      mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3022)
                      mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3022)m]
                      log 0xd431031d: addr(_3022), stor15[addr(_3022)]
                  else:
                      if mstor16m[addr([94m_3022)m]:
                          mem[0] = addr([94m_3022)
                          mem[32] = 15
                          mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3022)
                          mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3022)m]
                          log 0xd431031d: addr(_3022), stor15[addr(_3022)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_3022)
                          mem[0] = addr([94m_3022)
                          mem[32] = 16
                          mstor16m[addr([94m_3022)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_3022
                  mcontinue 
  else:
      mem[128 len 32 * uint8([94ms)] = code.data[17449 len 32 * uint8([94ms)]
      [94midx = 0
      [94mt = 0
      mwhile uint8([94midx) < mtokensm.lengthm:
          mem[0] = mtokensm[uint8([94midx)m]m.field_0
          mem[32] = 15
          if mstor15m[mstor9m[uint8([94midx)m]m.field_0m] <= 0:
              [94midx = [94midx + 1
              [94mt = [94mt
              mcontinue 
          require uint8([94midx) < mtokensm.length
          mem[0] = 9
          require uint8([94mt) < uint8([94ms)
          mem[(32 * uint8([94mt)) + 128] = mtokensm[uint8([94midx)m]m.field_0
          [94midx = [94midx + 1
          [94mt = [94mt + 1
          mcontinue 
      mem[(32 * uint8([94ms)) + 128] = uint8([94ms)
      if not uint8([94ms):
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 4
              [94mt = 0
              mwhile uint8([94mt) < uint8([94ms)m:
                  require uint8([94mt) < uint8([94ms)
                  [94m_1945 = mem[(32 * uint8([94mt)) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_1945))
                  call addr([94m_1945).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require uint8([94mt) < uint8([94ms)
                  mem[(32 * uint8([94ms)) + (32 * uint8([94mt)) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require uint8([94mt) < uint8([94ms)
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mem[(32 * uint8([94mt)) + 140 len 20]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * uint8([94ms)) + 324] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(mstor[sha3(0, 0, 4)m])
                  call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * uint8([94ms)) + 260], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, mem[(3 * 32 * uint8([94ms)) + 356]
                  mem[(3 * 32 * uint8([94ms)) + 256 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require uint8([94mt) < mem[(64 * uint8([94ms)) + 160]
                  mem[(64 * uint8([94ms)) + (32 * uint8([94mt)) + 192] = ext_call.return_data[32]
                  require uint8([94mt) < uint8([94ms)
                  [94m_2162 = mem[(32 * uint8([94mt)) + 128]
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mstor[sha3(0, 0, 4)m]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(addr([94m_2162))
                  call addr([94m_2162).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args mstor[sha3(0, 0, 4)m], 100000 * ext_call.return_data[0] / 100000
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * uint8([94ms)) + 256] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 356] = this.address
              mem[(3 * 32 * uint8([94ms)) + 420] = 0
              mem[(3 * 32 * uint8([94ms)) + 260] = 192
              mem[(3 * 32 * uint8([94ms)) + 452] = uint8([94ms)
              mem[(3 * 32 * uint8([94ms)) + 484 len Mask(3, 5, [94ms)] = mem[128 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 292] = (32 * uint8([94ms)) + 224
              mem[(uint8([94ms) << 7) + 484] = uint8([94ms)
              mem[(uint8([94ms) << 7) + 516 len Mask(3, 5, [94ms)] = mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 324] = (64 * uint8([94ms)) + 256
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 516] = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 548 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(mstor[sha3(0, 0, 4)m])
              call mstor[sha3(0, 0, 4)m].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args 192, (32 * uint8([94ms)) + 224, (64 * uint8([94ms)) + 256, addr(this.address), mem[(3 * 32 * uint8([94ms)) + 388], 0, [94ms << 248, mem[128 len Mask(3, 5, [94ms)], mem[(3 * 32 * uint8([94ms)) + Mask(3, 5, [94ms) + 484 len (uint8([94ms) << 7) + (-3 * 32 * uint8([94ms)) + -Mask(3, 5, [94ms) + 32], mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)], mem[Mask(3, 5, [94ms) + (uint8([94ms) << 7) + 516 len (32 * mem[(64 * uint8([94ms)) + 160]) + (64 * uint8([94ms)) + -Mask(3, 5, [94ms) + -(uint8([94ms) << 7) + (3 * 32 * uint8([94ms)) + 32]
              mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < uint8([94ms)m:
                  require [94mt < uint8([94ms)
                  [94m_3025 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_3025))
                  call addr([94m_3025).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15m[addr([94m_3025)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3025)
                      mem[32] = 15
                      mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3025)
                      mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3025)m]
                      log 0xd431031d: addr(_3025), stor15[addr(_3025)]
                  else:
                      if mstor16m[addr([94m_3025)m]:
                          mem[0] = addr([94m_3025)
                          mem[32] = 15
                          mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3025)
                          mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3025)m]
                          log 0xd431031d: addr(_3025), stor15[addr(_3025)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_3025)
                          mem[0] = addr([94m_3025)
                          mem[32] = 16
                          mstor16m[addr([94m_3025)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_3025
                  mcontinue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[17449 len 32 * uint8([94ms)]
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 4
              [94mt = 0
              mwhile uint8([94mt) < uint8([94ms)m:
                  require uint8([94mt) < uint8([94ms)
                  [94m_1948 = mem[(32 * uint8([94mt)) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_1948))
                  call addr([94m_1948).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require uint8([94mt) < uint8([94ms)
                  mem[(32 * uint8([94ms)) + (32 * uint8([94mt)) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require uint8([94mt) < uint8([94ms)
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mem[(32 * uint8([94mt)) + 140 len 20]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * uint8([94ms)) + 324] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(mstor[sha3(0, 0, 4)m])
                  call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * uint8([94ms)) + 260], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, mem[(3 * 32 * uint8([94ms)) + 356]
                  mem[(3 * 32 * uint8([94ms)) + 256 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require uint8([94mt) < mem[(64 * uint8([94ms)) + 160]
                  mem[(64 * uint8([94ms)) + (32 * uint8([94mt)) + 192] = ext_call.return_data[32]
                  require uint8([94mt) < uint8([94ms)
                  [94m_2165 = mem[(32 * uint8([94mt)) + 128]
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mstor[sha3(0, 0, 4)m]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(addr([94m_2165))
                  call addr([94m_2165).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args mstor[sha3(0, 0, 4)m], 100000 * ext_call.return_data[0] / 100000
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * uint8([94ms)) + 256] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 356] = this.address
              mem[(3 * 32 * uint8([94ms)) + 420] = 0
              mem[(3 * 32 * uint8([94ms)) + 260] = 192
              mem[(3 * 32 * uint8([94ms)) + 452] = uint8([94ms)
              mem[(3 * 32 * uint8([94ms)) + 484 len Mask(3, 5, [94ms)] = mem[128 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 292] = (32 * uint8([94ms)) + 224
              mem[(uint8([94ms) << 7) + 484] = uint8([94ms)
              mem[(uint8([94ms) << 7) + 516 len Mask(3, 5, [94ms)] = mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 324] = (64 * uint8([94ms)) + 256
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 516] = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 548 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(mstor[sha3(0, 0, 4)m])
              call mstor[sha3(0, 0, 4)m].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args 192, (32 * uint8([94ms)) + 224, (64 * uint8([94ms)) + 256, addr(this.address), mem[(3 * 32 * uint8([94ms)) + 388], 0, [94ms << 248, mem[128 len Mask(3, 5, [94ms)], mem[(3 * 32 * uint8([94ms)) + Mask(3, 5, [94ms) + 484 len (uint8([94ms) << 7) + (-3 * 32 * uint8([94ms)) + -Mask(3, 5, [94ms) + 32], mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)], mem[Mask(3, 5, [94ms) + (uint8([94ms) << 7) + 516 len (32 * mem[(64 * uint8([94ms)) + 160]) + (64 * uint8([94ms)) + -Mask(3, 5, [94ms) + -(uint8([94ms) << 7) + (3 * 32 * uint8([94ms)) + 32]
              mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < uint8([94ms)m:
                  require [94mt < uint8([94ms)
                  [94m_3028 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_3028))
                  call addr([94m_3028).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15m[addr([94m_3028)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3028)
                      mem[32] = 15
                      mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3028)
                      mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3028)m]
                      log 0xd431031d: addr(_3028), stor15[addr(_3028)]
                  else:
                      if mstor16m[addr([94m_3028)m]:
                          mem[0] = addr([94m_3028)
                          mem[32] = 15
                          mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3028)
                          mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3028)m]
                          log 0xd431031d: addr(_3028), stor15[addr(_3028)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_3028)
                          mem[0] = addr([94m_3028)
                          mem[32] = 16
                          mstor16m[addr([94m_3028)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_3028
                  mcontinue 
      else:
          mem[(32 * uint8([94ms)) + 160 len 32 * uint8([94ms)] = code.data[17449 len 32 * uint8([94ms)]
          mem[(64 * uint8([94ms)) + 160] = uint8([94ms)
          if not uint8([94ms):
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 4
              [94mt = 0
              mwhile uint8([94mt) < uint8([94ms)m:
                  require uint8([94mt) < uint8([94ms)
                  [94m_1951 = mem[(32 * uint8([94mt)) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_1951))
                  call addr([94m_1951).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require uint8([94mt) < uint8([94ms)
                  mem[(32 * uint8([94ms)) + (32 * uint8([94mt)) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require uint8([94mt) < uint8([94ms)
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mem[(32 * uint8([94mt)) + 140 len 20]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * uint8([94ms)) + 324] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(mstor[sha3(0, 0, 4)m])
                  call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * uint8([94ms)) + 260], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, mem[(3 * 32 * uint8([94ms)) + 356]
                  mem[(3 * 32 * uint8([94ms)) + 256 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require uint8([94mt) < mem[(64 * uint8([94ms)) + 160]
                  mem[(64 * uint8([94ms)) + (32 * uint8([94mt)) + 192] = ext_call.return_data[32]
                  require uint8([94mt) < uint8([94ms)
                  [94m_2168 = mem[(32 * uint8([94mt)) + 128]
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mstor[sha3(0, 0, 4)m]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(addr([94m_2168))
                  call addr([94m_2168).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args mstor[sha3(0, 0, 4)m], 100000 * ext_call.return_data[0] / 100000
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * uint8([94ms)) + 256] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 356] = this.address
              mem[(3 * 32 * uint8([94ms)) + 420] = 0
              mem[(3 * 32 * uint8([94ms)) + 260] = 192
              mem[(3 * 32 * uint8([94ms)) + 452] = uint8([94ms)
              mem[(3 * 32 * uint8([94ms)) + 484 len Mask(3, 5, [94ms)] = mem[128 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 292] = (32 * uint8([94ms)) + 224
              mem[(uint8([94ms) << 7) + 484] = uint8([94ms)
              mem[(uint8([94ms) << 7) + 516 len Mask(3, 5, [94ms)] = mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 324] = (64 * uint8([94ms)) + 256
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 516] = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 548 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(mstor[sha3(0, 0, 4)m])
              call mstor[sha3(0, 0, 4)m].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args 192, (32 * uint8([94ms)) + 224, (64 * uint8([94ms)) + 256, addr(this.address), mem[(3 * 32 * uint8([94ms)) + 388], 0, [94ms << 248, mem[128 len Mask(3, 5, [94ms)], mem[(3 * 32 * uint8([94ms)) + Mask(3, 5, [94ms) + 484 len (uint8([94ms) << 7) + (-3 * 32 * uint8([94ms)) + -Mask(3, 5, [94ms) + 32], mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)], mem[Mask(3, 5, [94ms) + (uint8([94ms) << 7) + 516 len (32 * mem[(64 * uint8([94ms)) + 160]) + (64 * uint8([94ms)) + -Mask(3, 5, [94ms) + -(uint8([94ms) << 7) + (3 * 32 * uint8([94ms)) + 32]
              mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < uint8([94ms)m:
                  require [94mt < uint8([94ms)
                  [94m_3031 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_3031))
                  call addr([94m_3031).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15m[addr([94m_3031)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3031)
                      mem[32] = 15
                      mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3031)
                      mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3031)m]
                      log 0xd431031d: addr(_3031), stor15[addr(_3031)]
                  else:
                      if mstor16m[addr([94m_3031)m]:
                          mem[0] = addr([94m_3031)
                          mem[32] = 15
                          mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3031)
                          mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3031)m]
                          log 0xd431031d: addr(_3031), stor15[addr(_3031)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_3031)
                          mem[0] = addr([94m_3031)
                          mem[32] = 16
                          mstor16m[addr([94m_3031)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_3031
                  mcontinue 
          else:
              mem[(64 * uint8([94ms)) + 192 len 32 * uint8([94ms)] = code.data[17449 len 32 * uint8([94ms)]
              mem[(3 * 32 * uint8([94ms)) + 192] = 16
              mem[(3 * 32 * uint8([94ms)) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 256 len 0] = None
              mem[(3 * 32 * uint8([94ms)) + 257 len 15] = 0x45786368616e676550726f76696465
              mem[(3 * 32 * uint8([94ms)) + 256 len 1] = 0
              mem[(3 * 32 * uint8([94ms)) + 272] = 4
              [94mt = 0
              mwhile uint8([94mt) < uint8([94ms)m:
                  require uint8([94mt) < uint8([94ms)
                  [94m_1954 = mem[(32 * uint8([94mt)) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_1954))
                  call addr([94m_1954).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require uint8([94mt) < uint8([94ms)
                  mem[(32 * uint8([94ms)) + (32 * uint8([94mt)) + 160] = 100000 * ext_call.return_data[0] / 100000
                  require uint8([94mt) < uint8([94ms)
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mem[(32 * uint8([94mt)) + 140 len 20]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * uint8([94ms)) + 324] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(mstor[sha3(0, 0, 4)m])
                  call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * uint8([94ms)) + 260], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 100000 * ext_call.return_data[0] / 100000, mem[(3 * 32 * uint8([94ms)) + 356]
                  mem[(3 * 32 * uint8([94ms)) + 256 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require uint8([94mt) < mem[(64 * uint8([94ms)) + 160]
                  mem[(64 * uint8([94ms)) + (32 * uint8([94mt)) + 192] = ext_call.return_data[32]
                  require uint8([94mt) < uint8([94ms)
                  [94m_2171 = mem[(32 * uint8([94mt)) + 128]
                  require uint8([94mt) < uint8([94ms)
                  mem[(3 * 32 * uint8([94ms)) + 260] = mstor[sha3(0, 0, 4)m]
                  mem[(3 * 32 * uint8([94ms)) + 292] = 100000 * ext_call.return_data[0] / 100000
                  require ext_code.size(addr([94m_2171))
                  call addr([94m_2171).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args mstor[sha3(0, 0, 4)m], 100000 * ext_call.return_data[0] / 100000
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * uint8([94ms)) + 256] = 0xc34bdef000000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * uint8([94ms)) + 356] = this.address
              mem[(3 * 32 * uint8([94ms)) + 420] = 0
              mem[(3 * 32 * uint8([94ms)) + 260] = 192
              mem[(3 * 32 * uint8([94ms)) + 452] = uint8([94ms)
              mem[(3 * 32 * uint8([94ms)) + 484 len Mask(3, 5, [94ms)] = mem[128 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 292] = (32 * uint8([94ms)) + 224
              mem[(uint8([94ms) << 7) + 484] = uint8([94ms)
              mem[(uint8([94ms) << 7) + 516 len Mask(3, 5, [94ms)] = mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)]
              mem[(3 * 32 * uint8([94ms)) + 324] = (64 * uint8([94ms)) + 256
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 516] = mem[(64 * uint8([94ms)) + 160]
              mem[(32 * uint8([94ms)) + (uint8([94ms) << 7) + 548 len floor32(mem[(64 * uint8([94ms)) + 160])] = mem[(64 * uint8([94ms)) + 192 len floor32(mem[(64 * uint8([94ms)) + 160])]
              require ext_code.size(mstor[sha3(0, 0, 4)m])
              call mstor[sha3(0, 0, 4)m].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
                   gas gas_remaining wei
                  args 192, (32 * uint8([94ms)) + 224, (64 * uint8([94ms)) + 256, addr(this.address), mem[(3 * 32 * uint8([94ms)) + 388], 0, [94ms << 248, mem[128 len Mask(3, 5, [94ms)], mem[(3 * 32 * uint8([94ms)) + Mask(3, 5, [94ms) + 484 len (uint8([94ms) << 7) + (-3 * 32 * uint8([94ms)) + -Mask(3, 5, [94ms) + 32], mem[(32 * uint8([94ms)) + 160 len Mask(3, 5, [94ms)], mem[Mask(3, 5, [94ms) + (uint8([94ms) << 7) + 516 len (32 * mem[(64 * uint8([94ms)) + 160]) + (64 * uint8([94ms)) + -Mask(3, 5, [94ms) + -(uint8([94ms) << 7) + (3 * 32 * uint8([94ms)) + 32]
              mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < uint8([94ms)m:
                  require [94mt < uint8([94ms)
                  [94m_3034 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * uint8([94ms)) + 260] = this.address
                  require ext_code.size(addr([94m_3034))
                  call addr([94m_3034).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * uint8([94ms)) + 256] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mstor15m[addr([94m_3034)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_3034)
                      mem[32] = 15
                      mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3034)
                      mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3034)m]
                      log 0xd431031d: addr(_3034), stor15[addr(_3034)]
                  else:
                      if mstor16m[addr([94m_3034)m]:
                          mem[0] = addr([94m_3034)
                          mem[32] = 15
                          mem[(3 * 32 * uint8([94ms)) + 256] = addr([94m_3034)
                          mem[(3 * 32 * uint8([94ms)) + 288] = mstor15m[addr([94m_3034)m]
                          log 0xd431031d: addr(_3034), stor15[addr(_3034)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_3034)
                          mem[0] = addr([94m_3034)
                          mem[32] = 16
                          mstor16m[addr([94m_3034)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_3034
                  mcontinue 
  mstatus = 3
  log ChangeStatus(uint8 status=3)
  return 1


# hash = 0x445d1397
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def maxTransfers(): # not payable
  return mmaxTransfers


# hash = 0x4623299a
# getter = None
# const = None
# payable = False
def unknown4623299a(array m_param1, addr m_param2): # not payable
  require caller == mowner
  mem[128 len m_param1.length] = m_param1[allm]
  require m_param2
  mem[ceil32(m_param1.length) + 128 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
  mem[ceil32(m_param1.length) + floor32(m_param1.length) + 128] = 256^(-(m_param1.length % 32) + 32) - 1 and mem[ceil32(m_param1.length) + floor32(m_param1.length) + 128] or call.data[m_param1 + floor32(m_param1.length) + 36 len m_param1.length % 32], mem[m_param1.length + 128 len -(m_param1.length % 32) + 32] and !(256^(-(m_param1.length % 32) + 32) - 1)
  mem[ceil32(m_param1.length) + m_param1.length + 128] = 4
  mstor[mem[ceil32(m_param1.length) + floor32(m_param1.length) + 128 len (m_param1.length % 32) + 32]m]m[call.data[m_param1 + 36 len floor32(m_param1.length)]m] = m_param2
  mem[ceil32(m_param1.length) + 238 len 0] = None
  mem[ceil32(m_param1.length) + 238] = 0, mem[ceil32(m_param1.length) + 256 len 14]
  mem[ceil32(m_param1.length) + 270 len m_param1.length] = m_param1[allm]
  mem[ceil32(m_param1.length) + m_param1.length + 270 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
  mem[ceil32(m_param1.length) + (2 * floor32(m_param1.length)) + 302 len m_param1.length % 32] = mem[ceil32(m_param1.length) + -(m_param1.length % 32) + floor32(m_param1.length) + 302 len m_param1.length % 32]
  if sha3(call.data[m_param1 + 36 len floor32(m_param1.length)], mem[ceil32(m_param1.length) + m_param1.length + floor32(m_param1.length) + 270 len m_param1.length % 32]) != sha3(mem[ceil32(m_param1.length) + 238 len 14]):
      mem[ceil32(m_param1.length) + m_param1.length + 302 len m_param1.length] = m_param1[allm]
      mem[(2 * ceil32(m_param1.length)) + m_param1.length + 302 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
      mem[(2 * ceil32(m_param1.length)) + m_param1.length + floor32(m_param1.length) + 302] = 256^(-(m_param1.length % 32) + 32) - 1 and mem[(2 * ceil32(m_param1.length)) + m_param1.length + floor32(m_param1.length) + 302] or mem[ceil32(m_param1.length) + m_param1.length + floor32(m_param1.length) + 302] and !(256^(-(m_param1.length % 32) + 32) - 1)
      mem[(2 * ceil32(m_param1.length)) + (2 * m_param1.length) + 302] = 4
      [94m_232 = sha3(call.data[m_param1 + 36 len floor32(m_param1.length)], mem[(2 * ceil32(m_param1.length)) + m_param1.length + floor32(m_param1.length) + 302 len (m_param1.length % 32) + 32])
      require ext_code.size(mstor[mem[(2 * ceil32(m_param1.length)) + m_param1.length + floor32(m_param1.length) + 302 len (m_param1.length % 32) + 32]m]m[call.data[m_param1 + 36 len floor32(m_param1.length)]m])
      call mstor[mem[(2 * ceil32(m_param1.length)) + m_param1.length + floor32(m_param1.length) + 302 len (m_param1.length % 32) + 32]m]m[call.data[m_param1 + 36 len floor32(m_param1.length)]m].MOT() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[(2 * ceil32(m_param1.length)) + m_param1.length + 306] = mstor[mem[(2 * ceil32(m_param1.length)) + m_param1.length + floor32(m_param1.length) + 302 len (m_param1.length % 32) + 32]m]m[call.data[m_param1 + 36 len floor32(m_param1.length)]m]
      mem[(2 * ceil32(m_param1.length)) + m_param1.length + 338] = 0
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args mem[(2 * ceil32(m_param1.length)) + m_param1.length + 306 len ceil32(m_param1.length) + 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(mstor[[94m_232m])
      call mstor[[94m_232m].MOT() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[(2 * ceil32(m_param1.length)) + m_param1.length + 306] = mstor[[94m_232m]
      mem[(2 * ceil32(m_param1.length)) + m_param1.length + 338] = -1
      require ext_code.size(addr(ext_call.return_data[0]))
      call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args mem[(2 * ceil32(m_param1.length)) + m_param1.length + 306 len ceil32(m_param1.length) + 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
  return 1


# hash = 0x4f64b2be
# getter = ['storage', 160, 0, ['add', ['sha3', 9], ['cd', 4]]]
# const = None
# payable = False
def tokens(uint256 m_param1): # not payable
  require m_param1 < mtokensm.length
  return mtokensm[m_param1m]m.field_0


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 7]]]], ['loc', 7]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x5f677404
# getter = None
# const = ['return', 1000000000000000000]
# payable = False
const INITIAL_VALUE = 10^18


# hash = 0x648aa3b1
# getter = None
# const = None
# payable = False
def getComponentByName(string m_name): # not payable
  mem[128 len m_name.length] = m_name[allm]
  mem[ceil32(m_name.length) + 128 len floor32(m_name.length)] = call.data[m_name + 36 len floor32(m_name.length)]
  mem[ceil32(m_name.length) + floor32(m_name.length) + 128] = 256^(-(m_name.length % 32) + 32) - 1 and mem[ceil32(m_name.length) + floor32(m_name.length) + 128] or call.data[m_name + floor32(m_name.length) + 36 len m_name.length % 32], mem[m_name.length + 128 len -(m_name.length % 32) + 32] and !(256^(-(m_name.length % 32) + 32) - 1)
  mem[ceil32(m_name.length) + m_name.length + 128] = 4
  mem[ceil32(m_name.length) + 128] = mstor[mem[ceil32(m_name.length) + floor32(m_name.length) + 128 len (m_name.length % 32) + 32]m]m[call.data[m_name + 36 len floor32(m_name.length)]m]
  return memory
    from ceil32(m_name.length) + 128
     [93mlen 32


# hash = 0x659eeabc
# getter = None
# const = None
# payable = False
def tokensWithAmount(): # not payable
  [94midx = 0
  [94ms = 0
  mwhile uint8([94midx) < mtokensm.lengthm:
      mem[0] = mtokensm[uint8([94midx)m]m.field_0
      mem[32] = 15
      if mstor15m[mstor9m[uint8([94midx)m]m.field_0m] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  if uint8([94ms):
      mem[128 len 32 * uint8([94ms)] = code.data[17449 len 32 * uint8([94ms)]
  [94midx = 0
  [94mt = 0
  mwhile uint8([94midx) < mtokensm.lengthm:
      mem[0] = mtokensm[uint8([94midx)m]m.field_0
      mem[32] = 15
      if mstor15m[mstor9m[uint8([94midx)m]m.field_0m] <= 0:
          [94midx = [94midx + 1
          [94mt = [94mt
          mcontinue 
      require uint8([94midx) < mtokensm.length
      mem[0] = 9
      require uint8([94mt) < uint8([94ms)
      mem[(32 * uint8([94mt)) + 128] = mtokensm[uint8([94midx)m]m.field_0
      [94midx = [94midx + 1
      [94mt = [94mt + 1
      mcontinue 
  mem[(32 * uint8([94ms)) + 192 len Mask(3, 5, [94ms)] = mem[128 len Mask(3, 5, [94ms)]
  return Array(len=[94ms << 248, data=mem[128 len Mask(3, 5, [94ms)], mem[(32 * uint8([94ms)) + Mask(3, 5, [94ms) + 192 len (32 * uint8([94ms)) - Mask(3, 5, [94ms)]), 


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


# hash = 0x679818a1
# getter = None
# const = None
# payable = False
def unknown679818a1(uint256 m_param1, array m_param2, array m_param3, array m_param4): # not payable
  mem[128 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param2.length) + 128] = m_param3.length
  mem[(32 * m_param2.length) + 160 len 32 * m_param3.length] = call.data[m_param3 + 36 len 32 * m_param3.length]
  mem[(32 * m_param3.length) + (32 * m_param2.length) + 160] = m_param4.length
  mem[(32 * m_param3.length) + (32 * m_param2.length) + 192 len 32 * m_param4.length] = call.data[m_param4 + 36 len 32 * m_param4.length]
  require caller == mowner
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = 16
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256 len 0] = None
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 257 len 15] = 0x45786368616e676550726f76696465
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256 len 1] = 0
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 272] = 4
  [94midx = 0
  mwhile [94midx < mtokensm.lengthm:
      require [94midx < m_param2.length
      [94m_99 = mem[(32 * [94midx) + 128]
      require [94midx < m_param3.length
      [94m_104 = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = mstor[sha3(0, 0, 4)m]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = [94m_104
      require ext_code.size(addr([94m_99))
      call addr([94m_99).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args mstor[sha3(0, 0, 4)m], [94m_104
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 356] = this.address
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 388] = m_param1
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 420] = 0
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = 192
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 452] = m_param2.length
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 484 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = (32 * m_param2.length) + 224
  mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 484] = m_param3.length
  mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 516 len floor32(m_param3.length)] = call.data[m_param3 + 36 len floor32(m_param3.length)]
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = (32 * m_param3.length) + (32 * m_param2.length) + 256
  mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 516] = m_param4.length
  mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 548 len floor32(m_param4.length)] = call.data[m_param4 + 36 len floor32(m_param4.length)]
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].sellTokens(address[] tokens, uint256[] amounts, uint256[] minimumRates, address depositAddress, bytes32 exchangeId, address param6) with:
       gas gas_remaining wei
      args 192, (32 * m_param2.length) + 224, (32 * m_param3.length) + (32 * m_param2.length) + 256, addr(this.address), m_param1, 0, m_param2.length, call.data[m_param2 + 36 len floor32(m_param2.length)], mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + floor32(m_param2.length) + 484 len (32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + -floor32(m_param2.length) + 64]
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_param2.lengthm:
      require [94midx < m_param2.length
      [94m_210 = mem[(32 * [94midx) + 128]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = this.address
      require ext_code.size(addr([94m_210))
      call addr([94m_210).balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mstor15m[addr([94m_210)m] = ext_call.return_data[0]
      if 0 >= ext_call.return_data[0]:
          mem[0] = addr([94m_210)
          mem[32] = 15
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256] = addr([94m_210)
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 288] = mstor15m[addr([94m_210)m]
          log 0xd431031d: addr(_210), stor15[addr(_210)]
      else:
          if mstor16m[addr([94m_210)m]:
              mem[0] = addr([94m_210)
              mem[32] = 15
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 256] = addr([94m_210)
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 288] = mstor15m[addr([94m_210)m]
              log 0xd431031d: addr(_210), stor15[addr(_210)]
          else:
              mtokensm.length++
              mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_210)
              mem[0] = addr([94m_210)
              mem[32] = 16
              mstor16m[addr([94m_210)m] = 1
      [94midx = [94midx + 1
      [94ms = [94m_210
      mcontinue 
  return 1


# hash = 0x6e947298
# getter = None
# const = None
# payable = False
def getETHBalance(): # not payable
  return (eth.balance(this.address) - maccumulatedFee)


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 11]]]
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
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].0xcf46db5b with:
       gas gas_remaining wei
      args 0, caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].0xc8c01a55 with:
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
  mwhile uint16([94midx) < mtokensm.lengthm:
      mem[0] = 9
      mem[164] = this.address
      require ext_code.size(mtokensm[uint16([94midx)m]m.field_0)
      call mtokensm[uint16([94midx)m]m.field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          require uint16([94midx) < mtokensm.length
          mem[0] = 9
          mem[196] = mtokensm[uint16([94midx)m]m.field_0
          mem[228] = ext_call.return_data[0]
          mem[260] = 0
          require ext_code.size(mstor[sha3(0, 0, 4)m])
          call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[uint16([94midx)m]m.field_0, ext_call.return_data[0], 0
          mem[160 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0]
      mcontinue 
  return 0


# hash = 0x7bb25d60
# getter = None
# const = None
# payable = False
def withdrawInProgress(): # not payable
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].isInProgress() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return bool(ext_call.return_data[0])


# hash = 0x88301911
# getter = None
# const = None
# payable = True
def unknown88301911(addr m_param1, addr m_param2, addr m_param3, addr m_param4, addr m_param5, addr m_param6, addr m_param7, uint256 m_param8) payable: 
  require caller == mowner
  require mstatus <= 3
  require not mstatus
  require call.value > 0
  require m_param1
  mstor[sha3(0, 0, 4)m] = m_param1
  require m_param2
  mstor[sha3(0, 0, 4)m] = m_param2
  require m_param3
  mstor[sha3(0, 0, 4)m] = m_param3
  require m_param4
  mstor4m['RiskProvider'm] = m_param4
  require m_param5
  mstor[sha3(0, 0, 4)m] = m_param5
  require m_param7
  mstor[sha3(0, 0, 4)m] = m_param7
  require m_param6
  mstor[sha3(0, 0, 4)m] = m_param6
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor[sha3(0, 0, 4)m], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor[sha3(0, 0, 4)m], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor[sha3(0, 0, 4)m], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor[sha3(0, 0, 4)m], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4m['RiskProvider'm])
  call mstor4m['RiskProvider'm].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor4m['RiskProvider'm], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor4m['RiskProvider'm])
  call mstor4m['RiskProvider'm].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor4m['RiskProvider'm], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor[sha3(0, 0, 4)m], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor[sha3(0, 0, 4)m], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor[sha3(0, 0, 4)m], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor[sha3(0, 0, 4)m], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor[sha3(0, 0, 4)m], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args mstor[sha3(0, 0, 4)m], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_param1)
  call m_param1.0xdfd92f8a with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_param7)
  call m_param7.setFeePercentage(uint256 newFee) with:
       gas gas_remaining wei
      args m_param8
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mstatus = 1
  log ChangeStatus(uint8 status=1)
  maccumulatedFee += call.value


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x918f8674
# getter = None
# const = ['return', 100000]
# payable = False
const DENOMINATOR = 100000


# hash = 0x9375206a
# getter = None
# const = None
# payable = False
def setAllowed(address[] m_accounts, uint8 m_key, bool m_allowed): # not payable
  require caller == mowner
  require m_key <= 1
  mem[(32 * m_accounts.length) + 324 len floor32(m_accounts.length)] = call.data[m_accounts + 36 len floor32(m_accounts.length)]
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].setAllowed(address[] accounts, uint8 key, bool allowed) with:
       gas gas_remaining wei
      args Array(len=m_accounts.length, data=call.data[m_accounts + 36 len floor32(m_accounts.length)], mem[(32 * m_accounts.length) + floor32(m_accounts.length) + 324 len (32 * m_accounts.length) - floor32(m_accounts.length)]), m_key << 248, m_allowed
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 1


# hash = 0x95bc9538
# getter = None
# const = None
# payable = False
def changeStatus(uint8 m_status): # not payable
  require m_status <= 3
  require m_status
  require mstatus <= 3
  require mstatus
  require m_status <= 3
  require m_status != 3
  require mstatus <= 3
  require mstatus != 3
  require m_status <= 3
  require m_status != 3
  require m_status <= 3
  mstatus = m_status
  require mstatus <= 3
  log ChangeStatus(uint8 status=status)
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
  [94midx = 0
  [94ms = 0
  mwhile uint16([94midx) < mtokensm.lengthm:
      mem[0] = 9
      mem[164] = this.address
      require ext_code.size(mtokensm[uint16([94midx)m]m.field_0)
      call mtokensm[uint16([94midx)m]m.field_0.balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0]:
          require uint16([94midx) < mtokensm.length
          mem[0] = 9
          mem[196] = mtokensm[uint16([94midx)m]m.field_0
          mem[228] = ext_call.return_data[0]
          mem[260] = 0
          require ext_code.size(mstor[sha3(0, 0, 4)m])
          call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
               gas gas_remaining wei
              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[uint16([94midx)m]m.field_0, ext_call.return_data[0], 0
          mem[160 len 64] = ext_call.return_data[0 len 64]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 64
      [94midx = [94midx + 1
      [94ms = ext_call.return_data[0]
      mcontinue 
  if mtotalSupply:
      return ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply)
  revert


# hash = 0x9c2062ad
# getter = None
# const = ['return', ['data', ['arr', 12, ['mask_shl', 96, 0, 0, "'RiskProvider'"]]]]
# payable = False
const RISK = 'RiskProvider'


# hash = 0x9c2b1a95
# getter = None
# const = None
# payable = False
def getManagementFee(): # not payable
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].getFeePercentage() with:
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
  require caller == mowner
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].0xdfd92f8a with:
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
def transfer(address m_to, uint256 m_value): # not payable
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
      mem[32] = 15
      require [94midx < mtokensm.length
      mem[(32 * [94midx) + 128] = mstor15m[mstor9m[[94midxm]m.field_0m]
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


# hash = 0xaf048c37
# getter = None
# const = None
# payable = False
def enableWhitelist(uint8 m_key): # not payable
  require caller == mowner
  require m_key <= 1
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].0x2f038fd5 with:
       gas gas_remaining wei
      args m_key
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
def withdrawFee(uint256 m_amount): # not payable
  require caller == mowner
  require m_amount <= maccumulatedFee
  maccumulatedFee -= m_amount
  call caller with:
     value m_amount wei
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
def setMaxTransfers(uint256 m_maxTransfers): # not payable
  require caller == mowner
  mmaxTransfers = m_maxTransfers


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
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 13]]]]]
# const = None
# payable = False
def allowance(address m_owner, address m_spender): # not payable
  return mallowancem[addr(m_owner)m]m[addr(m_spender)m]


# hash = 0xe8b5e51f
# getter = None
# const = None
# payable = True
def invest() payable: 
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].0xcf46db5b with:
       gas gas_remaining wei
      args 0, caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require mstatus <= 3
  if mstatus != 1:
      revert with 0, 'The Fund is not active'
  if call.value < 10^15:
      revert with 0, 'Minimum value to invest is 0.001 ETH'
  if mtotalSupply <= 0:
      require ext_code.size(mstor[sha3(0, 0, 4)m])
      call mstor[sha3(0, 0, 4)m].0x8b28ab1e with:
           gas gas_remaining wei
          args caller, call.value
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      maccumulatedFee += ext_call.return_data[0]
      mbalanceOfm[callerm] += (100000 * call.value) - (100000 * ext_call.return_data[0]) / 10^18 * 10^mdecimals / 100000
      mtotalSupply += (100000 * call.value) - (100000 * ext_call.return_data[0]) / 10^18 * 10^mdecimals / 100000
      log Invested(
            address user=caller,
            uint256 amount=(100000 * call.value) - (100000 * ext_call.return_data[0]) / 10^18 * 10^decimals / 100000)
  else:
      require mtotalSupply
      if 0 == mtotalSupply:
          require ext_code.size(mstor[sha3(0, 0, 4)m])
          call mstor[sha3(0, 0, 4)m].0x8b28ab1e with:
               gas gas_remaining wei
              args caller, call.value
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require -(call.value * 10^mdecimals / mtotalSupply) + 10^18
          maccumulatedFee += ext_call.return_data[0]
          mbalanceOfm[callerm] += (100000 * call.value) - (100000 * ext_call.return_data[0]) / -(call.value * 10^mdecimals / mtotalSupply) + 10^18 * 10^mdecimals / 100000
          mtotalSupply += (100000 * call.value) - (100000 * ext_call.return_data[0]) / -(call.value * 10^mdecimals / mtotalSupply) + 10^18 * 10^mdecimals / 100000
          log Invested(
                address user=caller,
                uint256 amount=(100000 * call.value) - (100000 * ext_call.return_data[0]) / -(call.value * 10^decimals / totalSupply) + 10^18 * 10^decimals / 100000)
      else:
          [94midx = 0
          [94ms = 0
          mwhile uint16([94midx) < mtokensm.lengthm:
              mem[0] = 9
              mem[228] = this.address
              require ext_code.size(mtokensm[uint16([94midx)m]m.field_0)
              call mtokensm[uint16([94midx)m]m.field_0.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args this.address
              mem[224] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0]:
                  require uint16([94midx) < mtokensm.length
                  mem[0] = 9
                  mem[260] = mtokensm[uint16([94midx)m]m.field_0
                  mem[292] = ext_call.return_data[0]
                  mem[324] = 0
                  require ext_code.size(mstor[sha3(0, 0, 4)m])
                  call mstor[sha3(0, 0, 4)m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[uint16([94midx)m]m.field_0, ext_call.return_data[0], 0
                  mem[224 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
              [94midx = [94midx + 1
              [94ms = ext_call.return_data[0]
              mcontinue 
          require mtotalSupply
          require ext_code.size(mstor[sha3(0, 0, 4)m])
          call mstor[sha3(0, 0, 4)m].0x8b28ab1e with:
               gas gas_remaining wei
              args caller, call.value
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (call.value * 10^mdecimals / mtotalSupply)
          maccumulatedFee += ext_call.return_data[0]
          mbalanceOfm[callerm] += (100000 * call.value) - (100000 * ext_call.return_data[0]) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (call.value * 10^mdecimals / mtotalSupply) * 10^mdecimals / 100000
          mtotalSupply += (100000 * call.value) - (100000 * ext_call.return_data[0]) / ((eth.balance(this.address) * 10^mdecimals) - (maccumulatedFee * 10^mdecimals) / mtotalSupply) - (call.value * 10^mdecimals / mtotalSupply) * 10^mdecimals / 100000
          log Invested(
                address user=caller,
                uint256 amount=(100000 * call.value) - (100000 * ext_call.return_data[0]) / ((eth.balance(this.address) * 10^decimals) - (accumulatedFee * 10^decimals) / totalSupply) - (call.value * 10^decimals / totalSupply) * 10^decimals / 100000)
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
# const = ['return', ['data', 32, 14, 0]]
# payable = False
const MARKET = ''


# hash = 0xf8ce3164
# getter = ['storage', 256, 0, 18]
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
  require ext_code.size(mstor[sha3(0, 0, 4)m])
  call mstor[sha3(0, 0, 4)m].setFeePercentage(uint256 newFee) with:
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


