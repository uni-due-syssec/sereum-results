# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xd39E6C9580B634b39Ec449292bF3a5de6047B98B 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    unknown2156e6c6
    # storage address 2
    description
    # storage address 3
    category
    # storage address 4
    version
    # storage address 5
    fundType # mask: a s
    # storage address 5
    status # mask: a s
    # storage address 6
    tokens
    # storage address 7
    unknown5075edbfAddress # mask: a s
    # storage address 8
    stor8
    # storage address 9
    decimals # mask: a s
    # storage address 10
    name
    # storage address 11
    symbol
    # storage address 12
    balanceOf
    # storage address 13
    totalSupply # mask: a s
    # storage address 14
    allowance
    # storage address 15
    investors
    # storage address 16
    amounts
    # storage address 17
    stor17
    # storage address 26931604393339382447554222862686626729355078465860095111024870121857565877681
    stor3B8A # mask: a s
    # storage address 47913073437043740706018146470263530464821552251613244091397722805850655305248
    stor69ED # mask: a s
    # storage address 51152841008880598100929084884044496815161540061553138591600771862702143843796
    stor7117 # mask: a s
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 10]]]], ['loc', 10]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x08ecd9a6
# getter = None
# const = ['return', "'LockerProvider'"]
# payable = False
const LOCKER = 'LockerProvider'


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
# const = ['return', 154443516349745585550111941220176751601192532474414730758839226871264051200]
# payable = False
const WITHDRAW = 0x576974686472617750726f7669646572000000000000000000000000000000


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def totalSupply(): # not payable
  return mtotalSupply


# hash = 0x1fa98406
# getter = ['storage', 8, 0, 5]
# const = None
# payable = False
def fundType(): # not payable
  require mfundType <= 2
  return mfundType


# hash = 0x200d2ed2
# getter = ['storage', 8, 8, 5]
# const = None
# payable = False
def status(): # not payable
  require mstatus <= 3
  return mstatus


# hash = 0x2156e6c6
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def unknown2156e6c6(uint256 m_param1): # not payable
  return munknown2156e6c6m[m_param1m]


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
      if not mstor8m[m_param1m]:
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
# getter = ['storage', 256, 0, 9]
# const = None
# payable = False
def decimals(): # not payable
  return mdecimals


# hash = 0x33f245b1
# getter = None
# const = None
# payable = False
def unknown33f245b1(uint256 m_param1, addr m_param2, addr m_param3, uint256 m_param4, uint256 m_param5): # not payable
  require caller == mowner
  require m_param2 != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
  require m_param3 != 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
  require ext_code.size(m_param2)
  call m_param2.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(m_param2)
  call m_param2.approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], m_param4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[164] = m_param4
  mem[196] = m_param5
  mem[228] = this.address
  mem[260] = m_param1
  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x74c6ec74 with:
       gas gas_remaining wei
      args 0, 0, addr(m_param3), m_param4, m_param5, this.address, m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mem[128] = m_param2
  mem[160] = m_param3
  [94midx = 0
  [94ms = 0
  mwhile [94midx < 2m:
      require [94midx < 2
      [94m_35 = mem[(32 * [94midx) + 128]
      mem[196] = this.address
      require ext_code.size(addr([94m_35))
      call addr([94m_35).balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mamountsm[addr([94m_35)m] = ext_call.return_data[0]
      if 0 >= ext_call.return_data[0]:
          mem[0] = addr([94m_35)
          mem[32] = 16
          mem[192] = addr([94m_35)
          mem[224] = mamountsm[addr([94m_35)m]
          log 0xc2d539e6: addr(_35), amounts[addr(_35)]
      else:
          if mstor17m[addr([94m_35)m]:
              mem[0] = addr([94m_35)
              mem[32] = 16
              mem[192] = addr([94m_35)
              mem[224] = mamountsm[addr([94m_35)m]
              log 0xc2d539e6: addr(_35), amounts[addr(_35)]
          else:
              mtokensm.length++
              mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_35)
              mem[0] = addr([94m_35)
              mem[32] = 17
              mstor17m[addr([94m_35)m] = 1
      [94midx = [94midx + 1
      [94ms = [94m_35
      mcontinue 
  return 1


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
      require mem[(32 * m_param2.length) + (32 * [94midx) + 160] + [94ms >= [94ms
      [94midx = [94midx + 1
      [94ms = mem[(32 * m_param2.length) + (32 * [94midx) + 160] + [94ms
      mcontinue 
  require [94m_45 * m_param3.length <= eth.balance(this.address)
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = this.address
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = m_param1
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = 160
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 356] = m_param2.length
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 388 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = (32 * m_param2.length) + 192
  mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 388] = m_param3.length
  mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 420 len floor32(m_param3.length)] = call.data[m_param3 + 36 len floor32(m_param3.length)]
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = (32 * m_param3.length) + (32 * m_param2.length) + 224
  mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 420] = m_param4.length
  mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 452 len floor32(m_param4.length)] = call.data[m_param4 + 36 len floor32(m_param4.length)]
  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x15cdc529 with:
     value [94ms wei
       gas gas_remaining wei
      args Array(len=m_param2.length, data=call.data[m_param2 + 36 len floor32(m_param2.length)], mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + floor32(m_param2.length) + 388 len (32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + -floor32(m_param2.length) + 64]), (32 * m_param2.length) + 192, (32 * m_param3.length) + (32 * m_param2.length) + 224, addr(this.address), m_param1
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_param2.lengthm:
      require [94midx < m_param2.length
      [94m_155 = mem[(32 * [94midx) + 128]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = this.address
      require ext_code.size(addr([94m_155))
      call addr([94m_155).balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mamountsm[addr([94m_155)m] = ext_call.return_data[0]
      if 0 >= ext_call.return_data[0]:
          mem[0] = addr([94m_155)
          mem[32] = 16
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = addr([94m_155)
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 224] = mamountsm[addr([94m_155)m]
          log 0xc2d539e6: addr(_155), amounts[addr(_155)]
      else:
          if mstor17m[addr([94m_155)m]:
              mem[0] = addr([94m_155)
              mem[32] = 16
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = addr([94m_155)
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 224] = mamountsm[addr([94m_155)m]
              log 0xc2d539e6: addr(_155), amounts[addr(_155)]
          else:
              mtokensm.length++
              mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_155)
              mem[0] = addr([94m_155)
              mem[32] = 17
              mstor17m[addr([94m_155)m] = 1
      [94midx = [94midx + 1
      [94ms = [94m_155
      mcontinue 
  return 1


# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = False
def withdraw(): # not payable
  if 0 >= mbalanceOfm[callerm]:
      revert with 0, 'Insufficient balance'
  else:
      require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].0xc8c01a55 with:
           gas gas_remaining wei
          args caller, mbalanceOfm[callerm]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
          call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].0xc77e7614 with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 32
              if mtotalSupply != 0:
                  [94midx = 0
                  [94ms = 0
                  mwhile [94midx < mtokensm.lengthm:
                      mem[0] = 6
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
                              require [94midx < mtokensm.length
                              mem[0] = 6
                              mem[132] = mtokensm[[94midxm]m.field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
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
                                          mcontinue 
                                      else:
                                          require ext_call.return_data[0]
                                          require 0 / ext_call.return_data[0] >= 0
                                          [94midx = [94midx + 1
                                          [94ms = ext_call.return_data[0]
                                          mcontinue 
                                  else:
                                      [94midx = [94midx + 1
                                      [94ms = ext_call.return_data[0]
                                      mcontinue 
                          else:
                              [94midx = [94midx + 1
                              [94ms = ext_call.return_data[0]
                              mcontinue 
                  require eth.balance(this.address) >= 0
                  if eth.balance(this.address):
                      require 10^mdecimals * eth.balance(this.address) / eth.balance(this.address) == 10^mdecimals
                      require mtotalSupply
                      if ext_call.return_data[0]:
                          require 10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / ext_call.return_data[0] == 10^mdecimals * eth.balance(this.address) / mtotalSupply
                          require 10^mdecimals
                          if 10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / 10^mdecimals <= eth.balance(this.address):
                              require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].freeze() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].withdraw(address payee) with:
                                       gas gas_remaining wei
                                      args caller
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 64
                                      require ext_call.return_data[32] <= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] -= ext_call.return_data[32]
                                      require ext_call.return_data[32] <= mtotalSupply
                                      mtotalSupply -= ext_call.return_data[32]
                                      call caller with:
                                         value ext_call.return_data[0] wei
                                           gas 2300 * is_zero(value) wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                                          call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].finalize() with:
                                               gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              return 1
                          else:
                              [94midx = 0
                              [94ms = 0
                              mwhile [94midx < mtokensm.lengthm:
                                  mem[0] = 6
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
                                          require [94midx < mtokensm.length
                                          mem[0] = 6
                                          mem[132] = mtokensm[[94midxm]m.field_0
                                          mem[164] = 10^18
                                          mem[196] = 0
                                          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                               gas gas_remaining wei
                                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
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
                                                      mcontinue 
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      mcontinue 
                                              else:
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  mcontinue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = ext_call.return_data[0]
                                          mcontinue 
                              require eth.balance(this.address) <= 10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / 10^mdecimals
                              require (10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address)
                              require (10000 * 10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - (10000 * eth.balance(this.address)) / (10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address) == 10000
                              revert
                      else:
                          require 10^mdecimals
                          if 0 / 10^mdecimals <= eth.balance(this.address):
                              require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].freeze() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].withdraw(address payee) with:
                                       gas gas_remaining wei
                                      args caller
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 64
                                      require ext_call.return_data[32] <= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] -= ext_call.return_data[32]
                                      require ext_call.return_data[32] <= mtotalSupply
                                      mtotalSupply -= ext_call.return_data[32]
                                      call caller with:
                                         value ext_call.return_data[0] wei
                                           gas 2300 * is_zero(value) wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                                          call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].finalize() with:
                                               gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              return 1
                          else:
                              [94midx = 0
                              [94ms = 0
                              mwhile [94midx < mtokensm.lengthm:
                                  mem[0] = 6
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
                                          require [94midx < mtokensm.length
                                          mem[0] = 6
                                          mem[132] = mtokensm[[94midxm]m.field_0
                                          mem[164] = 10^18
                                          mem[196] = 0
                                          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                               gas gas_remaining wei
                                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
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
                                                      mcontinue 
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      mcontinue 
                                              else:
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  mcontinue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = ext_call.return_data[0]
                                          mcontinue 
                              require eth.balance(this.address) <= 0 / 10^mdecimals
                              require (0 / 10^mdecimals) - eth.balance(this.address)
                              require (10000 * 0 / 10^mdecimals) - (10000 * eth.balance(this.address)) / (0 / 10^mdecimals) - eth.balance(this.address) == 10000
                              revert
                  else:
                      require mtotalSupply
                      if ext_call.return_data[0]:
                          require 0 / mtotalSupply * ext_call.return_data[0] / ext_call.return_data[0] == 0 / mtotalSupply
                          require 10^mdecimals
                          if 0 / mtotalSupply * ext_call.return_data[0] / 10^mdecimals <= eth.balance(this.address):
                              require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].freeze() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].withdraw(address payee) with:
                                       gas gas_remaining wei
                                      args caller
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 64
                                      require ext_call.return_data[32] <= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] -= ext_call.return_data[32]
                                      require ext_call.return_data[32] <= mtotalSupply
                                      mtotalSupply -= ext_call.return_data[32]
                                      call caller with:
                                         value ext_call.return_data[0] wei
                                           gas 2300 * is_zero(value) wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                                          call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].finalize() with:
                                               gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              return 1
                          else:
                              [94midx = 0
                              [94ms = 0
                              mwhile [94midx < mtokensm.lengthm:
                                  mem[0] = 6
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
                                          require [94midx < mtokensm.length
                                          mem[0] = 6
                                          mem[132] = mtokensm[[94midxm]m.field_0
                                          mem[164] = 10^18
                                          mem[196] = 0
                                          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                               gas gas_remaining wei
                                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
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
                                                      mcontinue 
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      mcontinue 
                                              else:
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  mcontinue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = ext_call.return_data[0]
                                          mcontinue 
                              require eth.balance(this.address) <= 0 / mtotalSupply * ext_call.return_data[0] / 10^mdecimals
                              require (0 / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address)
                              require (10000 * 0 / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - (10000 * eth.balance(this.address)) / (0 / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address) == 10000
                              revert
                      else:
                          require 10^mdecimals
                          if 0 / 10^mdecimals <= eth.balance(this.address):
                              require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].freeze() with:
                                   gas gas_remaining wei
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].withdraw(address payee) with:
                                       gas gas_remaining wei
                                      args caller
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 64
                                      require ext_call.return_data[32] <= mbalanceOfm[callerm]
                                      mbalanceOfm[callerm] -= ext_call.return_data[32]
                                      require ext_call.return_data[32] <= mtotalSupply
                                      mtotalSupply -= ext_call.return_data[32]
                                      call caller with:
                                         value ext_call.return_data[0] wei
                                           gas 2300 * is_zero(value) wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                                          call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].finalize() with:
                                               gas gas_remaining wei
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          else:
                                              return 1
                          else:
                              [94midx = 0
                              [94ms = 0
                              mwhile [94midx < mtokensm.lengthm:
                                  mem[0] = 6
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
                                          require [94midx < mtokensm.length
                                          mem[0] = 6
                                          mem[132] = mtokensm[[94midxm]m.field_0
                                          mem[164] = 10^18
                                          mem[196] = 0
                                          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                               gas gas_remaining wei
                                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
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
                                                      mcontinue 
                                                  else:
                                                      require ext_call.return_data[0]
                                                      require 0 / ext_call.return_data[0] >= 0
                                                      [94midx = [94midx + 1
                                                      [94ms = ext_call.return_data[0]
                                                      mcontinue 
                                              else:
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  mcontinue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = ext_call.return_data[0]
                                          mcontinue 
                              require eth.balance(this.address) <= 0 / 10^mdecimals
                              require (0 / 10^mdecimals) - eth.balance(this.address)
                              require (10000 * 0 / 10^mdecimals) - (10000 * eth.balance(this.address)) / (0 / 10^mdecimals) - eth.balance(this.address) == 10000
                              revert
              else:
                  if ext_call.return_data[0]:
                      require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
                      require 10^mdecimals
                      if 10^18 * ext_call.return_data[0] / 10^mdecimals <= eth.balance(this.address):
                          require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                          call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].freeze() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].withdraw(address payee) with:
                                   gas gas_remaining wei
                                  args caller
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 64
                                  require ext_call.return_data[32] <= mbalanceOfm[callerm]
                                  mbalanceOfm[callerm] -= ext_call.return_data[32]
                                  require ext_call.return_data[32] <= mtotalSupply
                                  mtotalSupply -= ext_call.return_data[32]
                                  call caller with:
                                     value ext_call.return_data[0] wei
                                       gas 2300 * is_zero(value) wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                                      call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].finalize() with:
                                           gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          return 1
                      else:
                          [94midx = 0
                          [94ms = 0
                          mwhile [94midx < mtokensm.lengthm:
                              mem[0] = 6
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
                                      require [94midx < mtokensm.length
                                      mem[0] = 6
                                      mem[132] = mtokensm[[94midxm]m.field_0
                                      mem[164] = 10^18
                                      mem[196] = 0
                                      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                           gas gas_remaining wei
                                          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
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
                                                  mcontinue 
                                              else:
                                                  require ext_call.return_data[0]
                                                  require 0 / ext_call.return_data[0] >= 0
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  mcontinue 
                                          else:
                                              [94midx = [94midx + 1
                                              [94ms = ext_call.return_data[0]
                                              mcontinue 
                                  else:
                                      [94midx = [94midx + 1
                                      [94ms = ext_call.return_data[0]
                                      mcontinue 
                          require eth.balance(this.address) <= 10^18 * ext_call.return_data[0] / 10^mdecimals
                          require (10^18 * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address)
                          require (10000 * 10^18 * ext_call.return_data[0] / 10^mdecimals) - (10000 * eth.balance(this.address)) / (10^18 * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address) == 10000
                          revert
                  else:
                      require 10^mdecimals
                      if 0 / 10^mdecimals <= eth.balance(this.address):
                          require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                          call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].freeze() with:
                               gas gas_remaining wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].withdraw(address payee) with:
                                   gas gas_remaining wei
                                  args caller
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 64
                                  require ext_call.return_data[32] <= mbalanceOfm[callerm]
                                  mbalanceOfm[callerm] -= ext_call.return_data[32]
                                  require ext_call.return_data[32] <= mtotalSupply
                                  mtotalSupply -= ext_call.return_data[32]
                                  call caller with:
                                     value ext_call.return_data[0] wei
                                       gas 2300 * is_zero(value) wei
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
                                      call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].finalize() with:
                                           gas gas_remaining wei
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      else:
                                          return 1
                      else:
                          [94midx = 0
                          [94ms = 0
                          mwhile [94midx < mtokensm.lengthm:
                              mem[0] = 6
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
                                      require [94midx < mtokensm.length
                                      mem[0] = 6
                                      mem[132] = mtokensm[[94midxm]m.field_0
                                      mem[164] = 10^18
                                      mem[196] = 0
                                      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                           gas gas_remaining wei
                                          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
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
                                                  mcontinue 
                                              else:
                                                  require ext_call.return_data[0]
                                                  require 0 / ext_call.return_data[0] >= 0
                                                  [94midx = [94midx + 1
                                                  [94ms = ext_call.return_data[0]
                                                  mcontinue 
                                          else:
                                              [94midx = [94midx + 1
                                              [94ms = ext_call.return_data[0]
                                              mcontinue 
                                  else:
                                      [94midx = [94midx + 1
                                      [94ms = ext_call.return_data[0]
                                      mcontinue 
                          require eth.balance(this.address) <= 0 / 10^mdecimals
                          require (0 / 10^mdecimals) - eth.balance(this.address)
                          require (10000 * 0 / 10^mdecimals) - (10000 * eth.balance(this.address)) / (0 / 10^mdecimals) - eth.balance(this.address) == 10000
                          revert


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
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = mtokensm[[94midxm]m.field_0
      mem[32] = 16
      if mamountsm[mstor6m[[94midxm]m.field_0m] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  if not [94ms:
      [94midx = 0
      [94mt = 0
      mwhile [94midx < mtokensm.lengthm:
          mem[0] = mtokensm[[94midxm]m.field_0
          mem[32] = 16
          if mamountsm[mstor6m[[94midxm]m.field_0m] <= 0:
              [94midx = [94midx + 1
              [94mt = [94mt
              mcontinue 
          require [94midx < mtokensm.length
          mem[0] = 6
          require [94mt < [94ms
          mem[(32 * [94mt) + 128] = mtokensm[[94midxm]m.field_0
          [94midx = [94midx + 1
          [94mt = [94mt + 1
          mcontinue 
      mem[(32 * [94ms) + 128] = [94ms
      if not [94ms:
          mem[(64 * [94ms) + 160] = [94ms
          if not [94ms:
              [94mt = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_1357 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_1357))
                  call addr([94m_1357).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 10000 * ext_call.return_data[0] / 10000 == ext_call.return_data[0]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(32 * [94ms) + (32 * [94mt) + 160] = 10000 * ext_call.return_data[0] / 10000
                  require [94mt < [94ms
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 196] = mem[(32 * [94mt) + 140 len 20]
                  mem[(3 * 32 * [94ms) + 228] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * [94ms) + 260] = 10000 * ext_call.return_data[0] / 10000
                  mem[(3 * 32 * [94ms) + 292] = 0
                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * [94ms) + 196], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10000 * ext_call.return_data[0] / 10000, 0
                  mem[(3 * 32 * [94ms) + 192 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * [94ms) + 160]
                  mem[(64 * [94ms) + (32 * [94mt) + 192] = ext_call.return_data[32]
                  require [94mt < [94ms
                  [94m_1697 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 0
                  require ext_code.size(addr([94m_1697))
                  call addr([94m_1697).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < [94ms
                  [94m_1757 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 10000 * ext_call.return_data[0] / 10000
                  require ext_code.size(addr([94m_1757))
                  call addr([94m_1757).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 10000 * ext_call.return_data[0] / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * [94ms) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * [94ms) + 292] = this.address
              mem[(3 * 32 * [94ms) + 324] = 0
              mem[(3 * 32 * [94ms) + 196] = 160
              mem[(3 * 32 * [94ms) + 356] = [94ms
              mem[(3 * 32 * [94ms) + 388 len floor32([94ms)] = mem[128 len floor32([94ms)]
              mem[(3 * 32 * [94ms) + 228] = (32 * [94ms) + 192
              mem[(128 * [94ms) + 388] = mem[(32 * [94ms) + 128]
              mem[(128 * [94ms) + 420 len floor32(mem[(32 * [94ms) + 128])] = mem[(32 * [94ms) + 160 len floor32(mem[(32 * [94ms) + 128])]
              mem[(3 * 32 * [94ms) + 260] = (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 420] = mem[(64 * [94ms) + 160]
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 452 len floor32(mem[(64 * [94ms) + 160])] = mem[(64 * [94ms) + 192 len floor32(mem[(64 * [94ms) + 160])]
              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x78265e2f with:
                   gas gas_remaining wei
                  args 160, (32 * [94ms) + 192, (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224, addr(this.address), 0, [94ms, mem[128 len floor32([94ms)], mem[(3 * 32 * [94ms) + floor32([94ms) + 388 len (32 * [94ms) + (32 * mem[(64 * [94ms) + 160]) + (32 * mem[(32 * [94ms) + 128]) + -floor32([94ms) + 64]
              mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_2461 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_2461))
                  call addr([94m_2461).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mamountsm[addr([94m_2461)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_2461)
                      mem[32] = 16
                      mem[(3 * 32 * [94ms) + 192] = addr([94m_2461)
                      mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2461)m]
                      log 0xc2d539e6: addr(_2461), amounts[addr(_2461)]
                  else:
                      if mstor17m[addr([94m_2461)m]:
                          mem[0] = addr([94m_2461)
                          mem[32] = 16
                          mem[(3 * 32 * [94ms) + 192] = addr([94m_2461)
                          mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2461)m]
                          log 0xc2d539e6: addr(_2461), amounts[addr(_2461)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_2461)
                          mem[0] = addr([94m_2461)
                          mem[32] = 17
                          mstor17m[addr([94m_2461)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_2461
                  mcontinue 
          else:
              mem[(64 * [94ms) + 192 len 32 * [94ms] = code.data[14699 len 32 * [94ms]
              [94mt = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_1360 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_1360))
                  call addr([94m_1360).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 10000 * ext_call.return_data[0] / 10000 == ext_call.return_data[0]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(32 * [94ms) + (32 * [94mt) + 160] = 10000 * ext_call.return_data[0] / 10000
                  require [94mt < [94ms
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 196] = mem[(32 * [94mt) + 140 len 20]
                  mem[(3 * 32 * [94ms) + 228] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * [94ms) + 260] = 10000 * ext_call.return_data[0] / 10000
                  mem[(3 * 32 * [94ms) + 292] = 0
                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * [94ms) + 196], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10000 * ext_call.return_data[0] / 10000, 0
                  mem[(3 * 32 * [94ms) + 192 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * [94ms) + 160]
                  mem[(64 * [94ms) + (32 * [94mt) + 192] = ext_call.return_data[32]
                  require [94mt < [94ms
                  [94m_1704 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 0
                  require ext_code.size(addr([94m_1704))
                  call addr([94m_1704).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < [94ms
                  [94m_1759 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 10000 * ext_call.return_data[0] / 10000
                  require ext_code.size(addr([94m_1759))
                  call addr([94m_1759).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 10000 * ext_call.return_data[0] / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * [94ms) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * [94ms) + 292] = this.address
              mem[(3 * 32 * [94ms) + 324] = 0
              mem[(3 * 32 * [94ms) + 196] = 160
              mem[(3 * 32 * [94ms) + 356] = [94ms
              mem[(3 * 32 * [94ms) + 388 len floor32([94ms)] = mem[128 len floor32([94ms)]
              mem[(3 * 32 * [94ms) + 228] = (32 * [94ms) + 192
              mem[(128 * [94ms) + 388] = mem[(32 * [94ms) + 128]
              mem[(128 * [94ms) + 420 len floor32(mem[(32 * [94ms) + 128])] = mem[(32 * [94ms) + 160 len floor32(mem[(32 * [94ms) + 128])]
              mem[(3 * 32 * [94ms) + 260] = (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 420] = mem[(64 * [94ms) + 160]
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 452 len floor32(mem[(64 * [94ms) + 160])] = mem[(64 * [94ms) + 192 len floor32(mem[(64 * [94ms) + 160])]
              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x78265e2f with:
                   gas gas_remaining wei
                  args 160, (32 * [94ms) + 192, (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224, addr(this.address), 0, [94ms, mem[128 len floor32([94ms)], mem[(3 * 32 * [94ms) + floor32([94ms) + 388 len (32 * [94ms) + (32 * mem[(64 * [94ms) + 160]) + (32 * mem[(32 * [94ms) + 128]) + -floor32([94ms) + 64]
              mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_2464 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_2464))
                  call addr([94m_2464).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mamountsm[addr([94m_2464)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_2464)
                      mem[32] = 16
                      mem[(3 * 32 * [94ms) + 192] = addr([94m_2464)
                      mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2464)m]
                      log 0xc2d539e6: addr(_2464), amounts[addr(_2464)]
                  else:
                      if mstor17m[addr([94m_2464)m]:
                          mem[0] = addr([94m_2464)
                          mem[32] = 16
                          mem[(3 * 32 * [94ms) + 192] = addr([94m_2464)
                          mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2464)m]
                          log 0xc2d539e6: addr(_2464), amounts[addr(_2464)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_2464)
                          mem[0] = addr([94m_2464)
                          mem[32] = 17
                          mstor17m[addr([94m_2464)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_2464
                  mcontinue 
      else:
          mem[(32 * [94ms) + 160 len 32 * [94ms] = code.data[14699 len 32 * [94ms]
          mem[(64 * [94ms) + 160] = [94ms
          if not [94ms:
              [94mt = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_1363 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_1363))
                  call addr([94m_1363).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 10000 * ext_call.return_data[0] / 10000 == ext_call.return_data[0]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(32 * [94ms) + (32 * [94mt) + 160] = 10000 * ext_call.return_data[0] / 10000
                  require [94mt < [94ms
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 196] = mem[(32 * [94mt) + 140 len 20]
                  mem[(3 * 32 * [94ms) + 228] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * [94ms) + 260] = 10000 * ext_call.return_data[0] / 10000
                  mem[(3 * 32 * [94ms) + 292] = 0
                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * [94ms) + 196], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10000 * ext_call.return_data[0] / 10000, 0
                  mem[(3 * 32 * [94ms) + 192 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * [94ms) + 160]
                  mem[(64 * [94ms) + (32 * [94mt) + 192] = ext_call.return_data[32]
                  require [94mt < [94ms
                  [94m_1711 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 0
                  require ext_code.size(addr([94m_1711))
                  call addr([94m_1711).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < [94ms
                  [94m_1761 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 10000 * ext_call.return_data[0] / 10000
                  require ext_code.size(addr([94m_1761))
                  call addr([94m_1761).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 10000 * ext_call.return_data[0] / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * [94ms) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * [94ms) + 292] = this.address
              mem[(3 * 32 * [94ms) + 324] = 0
              mem[(3 * 32 * [94ms) + 196] = 160
              mem[(3 * 32 * [94ms) + 356] = [94ms
              mem[(3 * 32 * [94ms) + 388 len floor32([94ms)] = mem[128 len floor32([94ms)]
              mem[(3 * 32 * [94ms) + 228] = (32 * [94ms) + 192
              mem[(128 * [94ms) + 388] = mem[(32 * [94ms) + 128]
              mem[(128 * [94ms) + 420 len floor32(mem[(32 * [94ms) + 128])] = mem[(32 * [94ms) + 160 len floor32(mem[(32 * [94ms) + 128])]
              mem[(3 * 32 * [94ms) + 260] = (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 420] = mem[(64 * [94ms) + 160]
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 452 len floor32(mem[(64 * [94ms) + 160])] = mem[(64 * [94ms) + 192 len floor32(mem[(64 * [94ms) + 160])]
              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x78265e2f with:
                   gas gas_remaining wei
                  args 160, (32 * [94ms) + 192, (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224, addr(this.address), 0, [94ms, mem[128 len floor32([94ms)], mem[(3 * 32 * [94ms) + floor32([94ms) + 388 len (32 * [94ms) + (32 * mem[(64 * [94ms) + 160]) + (32 * mem[(32 * [94ms) + 128]) + -floor32([94ms) + 64]
              mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_2467 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_2467))
                  call addr([94m_2467).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mamountsm[addr([94m_2467)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_2467)
                      mem[32] = 16
                      mem[(3 * 32 * [94ms) + 192] = addr([94m_2467)
                      mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2467)m]
                      log 0xc2d539e6: addr(_2467), amounts[addr(_2467)]
                  else:
                      if mstor17m[addr([94m_2467)m]:
                          mem[0] = addr([94m_2467)
                          mem[32] = 16
                          mem[(3 * 32 * [94ms) + 192] = addr([94m_2467)
                          mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2467)m]
                          log 0xc2d539e6: addr(_2467), amounts[addr(_2467)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_2467)
                          mem[0] = addr([94m_2467)
                          mem[32] = 17
                          mstor17m[addr([94m_2467)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_2467
                  mcontinue 
          else:
              mem[(64 * [94ms) + 192 len 32 * [94ms] = code.data[14699 len 32 * [94ms]
              [94mt = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_1366 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_1366))
                  call addr([94m_1366).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 10000 * ext_call.return_data[0] / 10000 == ext_call.return_data[0]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(32 * [94ms) + (32 * [94mt) + 160] = 10000 * ext_call.return_data[0] / 10000
                  require [94mt < [94ms
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 196] = mem[(32 * [94mt) + 140 len 20]
                  mem[(3 * 32 * [94ms) + 228] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * [94ms) + 260] = 10000 * ext_call.return_data[0] / 10000
                  mem[(3 * 32 * [94ms) + 292] = 0
                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * [94ms) + 196], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10000 * ext_call.return_data[0] / 10000, 0
                  mem[(3 * 32 * [94ms) + 192 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * [94ms) + 160]
                  mem[(64 * [94ms) + (32 * [94mt) + 192] = ext_call.return_data[32]
                  require [94mt < [94ms
                  [94m_1718 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 0
                  require ext_code.size(addr([94m_1718))
                  call addr([94m_1718).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < [94ms
                  [94m_1763 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 10000 * ext_call.return_data[0] / 10000
                  require ext_code.size(addr([94m_1763))
                  call addr([94m_1763).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 10000 * ext_call.return_data[0] / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * [94ms) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * [94ms) + 292] = this.address
              mem[(3 * 32 * [94ms) + 324] = 0
              mem[(3 * 32 * [94ms) + 196] = 160
              mem[(3 * 32 * [94ms) + 356] = [94ms
              mem[(3 * 32 * [94ms) + 388 len floor32([94ms)] = mem[128 len floor32([94ms)]
              mem[(3 * 32 * [94ms) + 228] = (32 * [94ms) + 192
              mem[(128 * [94ms) + 388] = mem[(32 * [94ms) + 128]
              mem[(128 * [94ms) + 420 len floor32(mem[(32 * [94ms) + 128])] = mem[(32 * [94ms) + 160 len floor32(mem[(32 * [94ms) + 128])]
              mem[(3 * 32 * [94ms) + 260] = (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 420] = mem[(64 * [94ms) + 160]
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 452 len floor32(mem[(64 * [94ms) + 160])] = mem[(64 * [94ms) + 192 len floor32(mem[(64 * [94ms) + 160])]
              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x78265e2f with:
                   gas gas_remaining wei
                  args 160, (32 * [94ms) + 192, (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224, addr(this.address), 0, [94ms, mem[128 len floor32([94ms)], mem[(3 * 32 * [94ms) + floor32([94ms) + 388 len (32 * [94ms) + (32 * mem[(64 * [94ms) + 160]) + (32 * mem[(32 * [94ms) + 128]) + -floor32([94ms) + 64]
              mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_2470 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_2470))
                  call addr([94m_2470).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mamountsm[addr([94m_2470)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_2470)
                      mem[32] = 16
                      mem[(3 * 32 * [94ms) + 192] = addr([94m_2470)
                      mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2470)m]
                      log 0xc2d539e6: addr(_2470), amounts[addr(_2470)]
                  else:
                      if mstor17m[addr([94m_2470)m]:
                          mem[0] = addr([94m_2470)
                          mem[32] = 16
                          mem[(3 * 32 * [94ms) + 192] = addr([94m_2470)
                          mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2470)m]
                          log 0xc2d539e6: addr(_2470), amounts[addr(_2470)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_2470)
                          mem[0] = addr([94m_2470)
                          mem[32] = 17
                          mstor17m[addr([94m_2470)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_2470
                  mcontinue 
  else:
      mem[128 len 32 * [94ms] = code.data[14699 len 32 * [94ms]
      [94midx = 0
      [94mt = 0
      mwhile [94midx < mtokensm.lengthm:
          mem[0] = mtokensm[[94midxm]m.field_0
          mem[32] = 16
          if mamountsm[mstor6m[[94midxm]m.field_0m] <= 0:
              [94midx = [94midx + 1
              [94mt = [94mt
              mcontinue 
          require [94midx < mtokensm.length
          mem[0] = 6
          require [94mt < [94ms
          mem[(32 * [94mt) + 128] = mtokensm[[94midxm]m.field_0
          [94midx = [94midx + 1
          [94mt = [94mt + 1
          mcontinue 
      mem[(32 * [94ms) + 128] = [94ms
      if not [94ms:
          mem[(64 * [94ms) + 160] = [94ms
          if not [94ms:
              [94mt = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_1369 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_1369))
                  call addr([94m_1369).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 10000 * ext_call.return_data[0] / 10000 == ext_call.return_data[0]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(32 * [94ms) + (32 * [94mt) + 160] = 10000 * ext_call.return_data[0] / 10000
                  require [94mt < [94ms
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 196] = mem[(32 * [94mt) + 140 len 20]
                  mem[(3 * 32 * [94ms) + 228] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * [94ms) + 260] = 10000 * ext_call.return_data[0] / 10000
                  mem[(3 * 32 * [94ms) + 292] = 0
                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * [94ms) + 196], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10000 * ext_call.return_data[0] / 10000, 0
                  mem[(3 * 32 * [94ms) + 192 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * [94ms) + 160]
                  mem[(64 * [94ms) + (32 * [94mt) + 192] = ext_call.return_data[32]
                  require [94mt < [94ms
                  [94m_1725 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 0
                  require ext_code.size(addr([94m_1725))
                  call addr([94m_1725).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < [94ms
                  [94m_1765 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 10000 * ext_call.return_data[0] / 10000
                  require ext_code.size(addr([94m_1765))
                  call addr([94m_1765).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 10000 * ext_call.return_data[0] / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * [94ms) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * [94ms) + 292] = this.address
              mem[(3 * 32 * [94ms) + 324] = 0
              mem[(3 * 32 * [94ms) + 196] = 160
              mem[(3 * 32 * [94ms) + 356] = [94ms
              mem[(3 * 32 * [94ms) + 388 len floor32([94ms)] = mem[128 len floor32([94ms)]
              mem[(3 * 32 * [94ms) + 228] = (32 * [94ms) + 192
              mem[(128 * [94ms) + 388] = mem[(32 * [94ms) + 128]
              mem[(128 * [94ms) + 420 len floor32(mem[(32 * [94ms) + 128])] = mem[(32 * [94ms) + 160 len floor32(mem[(32 * [94ms) + 128])]
              mem[(3 * 32 * [94ms) + 260] = (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 420] = mem[(64 * [94ms) + 160]
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 452 len floor32(mem[(64 * [94ms) + 160])] = mem[(64 * [94ms) + 192 len floor32(mem[(64 * [94ms) + 160])]
              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x78265e2f with:
                   gas gas_remaining wei
                  args 160, (32 * [94ms) + 192, (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224, addr(this.address), 0, [94ms, mem[128 len floor32([94ms)], mem[(3 * 32 * [94ms) + floor32([94ms) + 388 len (32 * [94ms) + (32 * mem[(64 * [94ms) + 160]) + (32 * mem[(32 * [94ms) + 128]) + -floor32([94ms) + 64]
              mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_2473 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_2473))
                  call addr([94m_2473).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mamountsm[addr([94m_2473)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_2473)
                      mem[32] = 16
                      mem[(3 * 32 * [94ms) + 192] = addr([94m_2473)
                      mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2473)m]
                      log 0xc2d539e6: addr(_2473), amounts[addr(_2473)]
                  else:
                      if mstor17m[addr([94m_2473)m]:
                          mem[0] = addr([94m_2473)
                          mem[32] = 16
                          mem[(3 * 32 * [94ms) + 192] = addr([94m_2473)
                          mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2473)m]
                          log 0xc2d539e6: addr(_2473), amounts[addr(_2473)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_2473)
                          mem[0] = addr([94m_2473)
                          mem[32] = 17
                          mstor17m[addr([94m_2473)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_2473
                  mcontinue 
          else:
              mem[(64 * [94ms) + 192 len 32 * [94ms] = code.data[14699 len 32 * [94ms]
              [94mt = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_1372 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_1372))
                  call addr([94m_1372).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 10000 * ext_call.return_data[0] / 10000 == ext_call.return_data[0]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(32 * [94ms) + (32 * [94mt) + 160] = 10000 * ext_call.return_data[0] / 10000
                  require [94mt < [94ms
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 196] = mem[(32 * [94mt) + 140 len 20]
                  mem[(3 * 32 * [94ms) + 228] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * [94ms) + 260] = 10000 * ext_call.return_data[0] / 10000
                  mem[(3 * 32 * [94ms) + 292] = 0
                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * [94ms) + 196], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10000 * ext_call.return_data[0] / 10000, 0
                  mem[(3 * 32 * [94ms) + 192 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * [94ms) + 160]
                  mem[(64 * [94ms) + (32 * [94mt) + 192] = ext_call.return_data[32]
                  require [94mt < [94ms
                  [94m_1732 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 0
                  require ext_code.size(addr([94m_1732))
                  call addr([94m_1732).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < [94ms
                  [94m_1767 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 10000 * ext_call.return_data[0] / 10000
                  require ext_code.size(addr([94m_1767))
                  call addr([94m_1767).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 10000 * ext_call.return_data[0] / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * [94ms) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * [94ms) + 292] = this.address
              mem[(3 * 32 * [94ms) + 324] = 0
              mem[(3 * 32 * [94ms) + 196] = 160
              mem[(3 * 32 * [94ms) + 356] = [94ms
              mem[(3 * 32 * [94ms) + 388 len floor32([94ms)] = mem[128 len floor32([94ms)]
              mem[(3 * 32 * [94ms) + 228] = (32 * [94ms) + 192
              mem[(128 * [94ms) + 388] = mem[(32 * [94ms) + 128]
              mem[(128 * [94ms) + 420 len floor32(mem[(32 * [94ms) + 128])] = mem[(32 * [94ms) + 160 len floor32(mem[(32 * [94ms) + 128])]
              mem[(3 * 32 * [94ms) + 260] = (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 420] = mem[(64 * [94ms) + 160]
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 452 len floor32(mem[(64 * [94ms) + 160])] = mem[(64 * [94ms) + 192 len floor32(mem[(64 * [94ms) + 160])]
              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x78265e2f with:
                   gas gas_remaining wei
                  args 160, (32 * [94ms) + 192, (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224, addr(this.address), 0, [94ms, mem[128 len floor32([94ms)], mem[(3 * 32 * [94ms) + floor32([94ms) + 388 len (32 * [94ms) + (32 * mem[(64 * [94ms) + 160]) + (32 * mem[(32 * [94ms) + 128]) + -floor32([94ms) + 64]
              mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_2476 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_2476))
                  call addr([94m_2476).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mamountsm[addr([94m_2476)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_2476)
                      mem[32] = 16
                      mem[(3 * 32 * [94ms) + 192] = addr([94m_2476)
                      mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2476)m]
                      log 0xc2d539e6: addr(_2476), amounts[addr(_2476)]
                  else:
                      if mstor17m[addr([94m_2476)m]:
                          mem[0] = addr([94m_2476)
                          mem[32] = 16
                          mem[(3 * 32 * [94ms) + 192] = addr([94m_2476)
                          mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2476)m]
                          log 0xc2d539e6: addr(_2476), amounts[addr(_2476)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_2476)
                          mem[0] = addr([94m_2476)
                          mem[32] = 17
                          mstor17m[addr([94m_2476)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_2476
                  mcontinue 
      else:
          mem[(32 * [94ms) + 160 len 32 * [94ms] = code.data[14699 len 32 * [94ms]
          mem[(64 * [94ms) + 160] = [94ms
          if not [94ms:
              [94mt = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_1375 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_1375))
                  call addr([94m_1375).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 10000 * ext_call.return_data[0] / 10000 == ext_call.return_data[0]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(32 * [94ms) + (32 * [94mt) + 160] = 10000 * ext_call.return_data[0] / 10000
                  require [94mt < [94ms
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 196] = mem[(32 * [94mt) + 140 len 20]
                  mem[(3 * 32 * [94ms) + 228] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * [94ms) + 260] = 10000 * ext_call.return_data[0] / 10000
                  mem[(3 * 32 * [94ms) + 292] = 0
                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * [94ms) + 196], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10000 * ext_call.return_data[0] / 10000, 0
                  mem[(3 * 32 * [94ms) + 192 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * [94ms) + 160]
                  mem[(64 * [94ms) + (32 * [94mt) + 192] = ext_call.return_data[32]
                  require [94mt < [94ms
                  [94m_1739 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 0
                  require ext_code.size(addr([94m_1739))
                  call addr([94m_1739).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < [94ms
                  [94m_1769 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 10000 * ext_call.return_data[0] / 10000
                  require ext_code.size(addr([94m_1769))
                  call addr([94m_1769).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 10000 * ext_call.return_data[0] / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * [94ms) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * [94ms) + 292] = this.address
              mem[(3 * 32 * [94ms) + 324] = 0
              mem[(3 * 32 * [94ms) + 196] = 160
              mem[(3 * 32 * [94ms) + 356] = [94ms
              mem[(3 * 32 * [94ms) + 388 len floor32([94ms)] = mem[128 len floor32([94ms)]
              mem[(3 * 32 * [94ms) + 228] = (32 * [94ms) + 192
              mem[(128 * [94ms) + 388] = mem[(32 * [94ms) + 128]
              mem[(128 * [94ms) + 420 len floor32(mem[(32 * [94ms) + 128])] = mem[(32 * [94ms) + 160 len floor32(mem[(32 * [94ms) + 128])]
              mem[(3 * 32 * [94ms) + 260] = (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 420] = mem[(64 * [94ms) + 160]
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 452 len floor32(mem[(64 * [94ms) + 160])] = mem[(64 * [94ms) + 192 len floor32(mem[(64 * [94ms) + 160])]
              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x78265e2f with:
                   gas gas_remaining wei
                  args 160, (32 * [94ms) + 192, (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224, addr(this.address), 0, [94ms, mem[128 len floor32([94ms)], mem[(3 * 32 * [94ms) + floor32([94ms) + 388 len (32 * [94ms) + (32 * mem[(64 * [94ms) + 160]) + (32 * mem[(32 * [94ms) + 128]) + -floor32([94ms) + 64]
              mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_2479 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_2479))
                  call addr([94m_2479).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mamountsm[addr([94m_2479)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_2479)
                      mem[32] = 16
                      mem[(3 * 32 * [94ms) + 192] = addr([94m_2479)
                      mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2479)m]
                      log 0xc2d539e6: addr(_2479), amounts[addr(_2479)]
                  else:
                      if mstor17m[addr([94m_2479)m]:
                          mem[0] = addr([94m_2479)
                          mem[32] = 16
                          mem[(3 * 32 * [94ms) + 192] = addr([94m_2479)
                          mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2479)m]
                          log 0xc2d539e6: addr(_2479), amounts[addr(_2479)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_2479)
                          mem[0] = addr([94m_2479)
                          mem[32] = 17
                          mstor17m[addr([94m_2479)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_2479
                  mcontinue 
          else:
              mem[(64 * [94ms) + 192 len 32 * [94ms] = code.data[14699 len 32 * [94ms]
              [94mt = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_1378 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_1378))
                  call addr([94m_1378).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require 10000 * ext_call.return_data[0] / 10000 == ext_call.return_data[0]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(32 * [94ms) + (32 * [94mt) + 160] = 10000 * ext_call.return_data[0] / 10000
                  require [94mt < [94ms
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 196] = mem[(32 * [94mt) + 140 len 20]
                  mem[(3 * 32 * [94ms) + 228] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[(3 * 32 * [94ms) + 260] = 10000 * ext_call.return_data[0] / 10000
                  mem[(3 * 32 * [94ms) + 292] = 0
                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args mem[(3 * 32 * [94ms) + 196], 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, 10000 * ext_call.return_data[0] / 10000, 0
                  mem[(3 * 32 * [94ms) + 192 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require [94mt < mem[(64 * [94ms) + 160]
                  mem[(64 * [94ms) + (32 * [94mt) + 192] = ext_call.return_data[32]
                  require [94mt < [94ms
                  [94m_1746 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 0
                  require ext_code.size(addr([94m_1746))
                  call addr([94m_1746).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require [94mt < [94ms
                  [94m_1771 = mem[(32 * [94mt) + 128]
                  require [94mt < mem[(32 * [94ms) + 128]
                  mem[(3 * 32 * [94ms) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
                  mem[(3 * 32 * [94ms) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
                  mem[(3 * 32 * [94ms) + 228] = 10000 * ext_call.return_data[0] / 10000
                  require ext_code.size(addr([94m_1771))
                  call addr([94m_1771).approve(address spender, uint256 value) with:
                       gas gas_remaining wei
                      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 10000 * ext_call.return_data[0] / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  [94mt = [94mt + 1
                  mcontinue 
              mem[(3 * 32 * [94ms) + 192] = 0x78265e2f00000000000000000000000000000000000000000000000000000000
              mem[(3 * 32 * [94ms) + 292] = this.address
              mem[(3 * 32 * [94ms) + 324] = 0
              mem[(3 * 32 * [94ms) + 196] = 160
              mem[(3 * 32 * [94ms) + 356] = [94ms
              mem[(3 * 32 * [94ms) + 388 len floor32([94ms)] = mem[128 len floor32([94ms)]
              mem[(3 * 32 * [94ms) + 228] = (32 * [94ms) + 192
              mem[(128 * [94ms) + 388] = mem[(32 * [94ms) + 128]
              mem[(128 * [94ms) + 420 len floor32(mem[(32 * [94ms) + 128])] = mem[(32 * [94ms) + 160 len floor32(mem[(32 * [94ms) + 128])]
              mem[(3 * 32 * [94ms) + 260] = (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 420] = mem[(64 * [94ms) + 160]
              mem[(32 * mem[(32 * [94ms) + 128]) + (128 * [94ms) + 452 len floor32(mem[(64 * [94ms) + 160])] = mem[(64 * [94ms) + 192 len floor32(mem[(64 * [94ms) + 160])]
              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x78265e2f with:
                   gas gas_remaining wei
                  args 160, (32 * [94ms) + 192, (32 * mem[(32 * [94ms) + 128]) + (32 * [94ms) + 224, addr(this.address), 0, [94ms, mem[128 len floor32([94ms)], mem[(3 * 32 * [94ms) + floor32([94ms) + 388 len (32 * [94ms) + (32 * mem[(64 * [94ms) + 160]) + (32 * mem[(32 * [94ms) + 128]) + -floor32([94ms) + 64]
              mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
              [94mt = 0
              [94mu = 0
              mwhile [94mt < [94msm:
                  require [94mt < [94ms
                  [94m_2482 = mem[(32 * [94mt) + 128]
                  mem[(3 * 32 * [94ms) + 196] = this.address
                  require ext_code.size(addr([94m_2482))
                  call addr([94m_2482).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[(3 * 32 * [94ms) + 192] = ext_call.return_data[0]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mamountsm[addr([94m_2482)m] = ext_call.return_data[0]
                  if 0 >= ext_call.return_data[0]:
                      mem[0] = addr([94m_2482)
                      mem[32] = 16
                      mem[(3 * 32 * [94ms) + 192] = addr([94m_2482)
                      mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2482)m]
                      log 0xc2d539e6: addr(_2482), amounts[addr(_2482)]
                  else:
                      if mstor17m[addr([94m_2482)m]:
                          mem[0] = addr([94m_2482)
                          mem[32] = 16
                          mem[(3 * 32 * [94ms) + 192] = addr([94m_2482)
                          mem[(3 * 32 * [94ms) + 224] = mamountsm[addr([94m_2482)m]
                          log 0xc2d539e6: addr(_2482), amounts[addr(_2482)]
                      else:
                          mtokensm.length++
                          mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_2482)
                          mem[0] = addr([94m_2482)
                          mem[32] = 17
                          mstor17m[addr([94m_2482)m] = 1
                  [94mt = [94mt + 1
                  [94mu = [94m_2482
                  mcontinue 
  mstatus = 3
  log 0x7ea7eb4c: 3
  return 1


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
      mem[0] = mtokensm[[94midxm]m.field_0
      mem[32] = 16
      mem[96] = 0xa9059cbb00000000000000000000000000000000000000000000000000000000
      mem[100] = mowner
      mem[132] = mamountsm[mstor6m[[94midxm]m.field_0m]
      require ext_code.size(mtokensm[[94midxm]m.field_0)
      call mtokensm[[94midxm]m.field_0.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args mowner, mamountsm[mstor6m[[94midxm]m.field_0m]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x4f64b2be
# getter = ['storage', 160, 0, ['add', ['sha3', 6], ['cd', 4]]]
# const = None
# payable = False
def tokens(uint256 m_param1): # not payable
  require m_param1 < mtokensm.length
  return mtokensm[m_param1m]m.field_0


# hash = 0x5075edbf
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def unknown5075edbf(): # not payable
  return munknown5075edbfAddress


# hash = 0x53d0f255
# getter = None
# const = ['return', "'StepProvider'"]
# payable = False
const unknown53d0f255 = 'StepProvider'


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x55a3b2c1
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 16]]]
# const = None
# payable = False
def amounts(address m_param1): # not payable
  return mamountsm[m_param1m]


# hash = 0x5acf6903
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 17]]]]
# const = None
# payable = False
def activeTokens(address m_param1): # not payable
  return bool(mstor17m[m_param1m])


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
      mem[32] = 16
      if mamountsm[mstor6m[[94midxm]m.field_0m] <= 0:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  if [94ms:
      mem[128 len 32 * [94ms] = code.data[14699 len 32 * [94ms]
  [94midx = 0
  [94mt = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = mtokensm[[94midxm]m.field_0
      mem[32] = 16
      if mamountsm[mstor6m[[94midxm]m.field_0m] <= 0:
          [94midx = [94midx + 1
          [94mt = [94mt
          mcontinue 
      require [94midx < mtokensm.length
      mem[0] = 6
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
  [94midx = 0
  mwhile [94midx < m_param2.lengthm:
      require [94midx < m_param2.length
      [94m_54 = mem[(32 * [94midx) + 128]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = 0
      require ext_code.size(addr([94m_54))
      call addr([94m_54).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require [94midx < m_param2.length
      [94m_64 = mem[(32 * [94midx) + 128]
      require [94midx < m_param3.length
      [94m_66 = mem[(32 * [94midx) + (32 * m_param2.length) + 160]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = [94m_66
      require ext_code.size(addr([94m_64))
      call addr([94m_64).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], [94m_66
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 292] = this.address
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 324] = m_param1
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = 160
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 356] = m_param2.length
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 388 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 228] = (32 * m_param2.length) + 192
  mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 388] = m_param3.length
  mem[(64 * m_param2.length) + (32 * m_param4.length) + (32 * m_param3.length) + 420 len floor32(m_param3.length)] = call.data[m_param3 + 36 len floor32(m_param3.length)]
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 260] = (32 * m_param3.length) + (32 * m_param2.length) + 224
  mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 420] = m_param4.length
  mem[(64 * m_param3.length) + (64 * m_param2.length) + (32 * m_param4.length) + 452 len floor32(m_param4.length)] = call.data[m_param4 + 36 len floor32(m_param4.length)]
  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].'x&^/' with:
       gas gas_remaining wei
      args Array(len=m_param2.length, data=call.data[m_param2 + 36 len floor32(m_param2.length)], mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + floor32(m_param2.length) + 388 len (32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + -floor32(m_param2.length) + 64]), (32 * m_param2.length) + 192, (32 * m_param3.length) + (32 * m_param2.length) + 224, this.address, m_param1
  mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_param2.lengthm:
      require [94midx < m_param2.length
      [94m_168 = mem[(32 * [94midx) + 128]
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 196] = this.address
      require ext_code.size(addr([94m_168))
      call addr([94m_168).balanceOf(address owner) with:
           gas gas_remaining wei
          args this.address
      mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mamountsm[addr([94m_168)m] = ext_call.return_data[0]
      if 0 >= ext_call.return_data[0]:
          mem[0] = addr([94m_168)
          mem[32] = 16
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = addr([94m_168)
          mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 224] = mamountsm[addr([94m_168)m]
          log 0xc2d539e6: addr(_168), amounts[addr(_168)]
      else:
          if mstor17m[addr([94m_168)m]:
              mem[0] = addr([94m_168)
              mem[32] = 16
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 192] = addr([94m_168)
              mem[(32 * m_param4.length) + (32 * m_param3.length) + (32 * m_param2.length) + 224] = mamountsm[addr([94m_168)m]
              log 0xc2d539e6: addr(_168), amounts[addr(_168)]
          else:
              mtokensm.length++
              mtokensm[mtokensm.lengthm]m.field_0 = addr([94m_168)
              mem[0] = addr([94m_168)
              mem[32] = 17
              mstor17m[addr([94m_168)m] = 1
      [94midx = [94midx + 1
      [94ms = [94m_168
      mcontinue 
  return 1


# hash = 0x6f7bc9be
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 15]]]
# const = None
# payable = False
def investors(address m_param1): # not payable
  return minvestorsm[m_param1m]


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 12]]]
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
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 2]]]], ['loc', 2]]]
# const = None
# payable = False
def description(): # not payable
  return mdescriptionm[0 len mdescriptionm.lengthm]


# hash = 0x74d16c37
# getter = None
# const = None
# payable = False
def getAssetsValue(): # not payable
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = 6
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
          [94ms = ext_call.return_data[0]
          mcontinue 
      require [94midx < mtokensm.length
      mem[0] = 6
      mem[132] = mtokensm[[94midxm]m.field_0
      mem[164] = 10^18
      mem[196] = 0
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
      mem[96 len 64] = ext_call.return_data[0 len 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          mcontinue 
      if not ext_call.return_data[0]:
          if ext_call.return_data[0]:
              if 0 / ext_call.return_data[0] >= 0:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  mcontinue 
      else:
          if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18:
              if ext_call.return_data[0]:
                  if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      mcontinue 
      revert
  return 0


# hash = 0x8d859f3e
# getter = None
# const = ['return', "'PriceProvider'"]
# payable = False
const PRICE = 'PriceProvider'


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x918f8674
# getter = None
# const = ['return', 10000]
# payable = False
const DENOMINATOR = 10000


# hash = 0x95bc9538
# getter = None
# const = None
# payable = False
def changeStatus(uint8 m_status): # not payable
  require caller == mowner
  require m_status <= 3
  require m_status
  require mstatus <= 3
  require mstatus
  require mstatus <= 3
  require mstatus != 3
  require m_status <= 3
  require m_status != 3
  require m_status <= 3
  mstatus = m_status
  require mstatus <= 3
  log 0x7ea7eb4c: status
  return 1


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 11]]]], ['loc', 11]]]
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
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = 6
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
          [94ms = ext_call.return_data[0]
          mcontinue 
      require [94midx < mtokensm.length
      mem[0] = 6
      mem[132] = mtokensm[[94midxm]m.field_0
      mem[164] = 10^18
      mem[196] = 0
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
      mem[96 len 64] = ext_call.return_data[0 len 64]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 64
      if not ext_call.return_data[0]:
          [94midx = [94midx + 1
          [94ms = ext_call.return_data[0]
          mcontinue 
      if not ext_call.return_data[0]:
          if ext_call.return_data[0]:
              if 0 / ext_call.return_data[0] >= 0:
                  [94midx = [94midx + 1
                  [94ms = ext_call.return_data[0]
                  mcontinue 
      else:
          if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18:
              if ext_call.return_data[0]:
                  if 10^18 * ext_call.return_data[0] / ext_call.return_data[0] >= 0:
                      [94midx = [94midx + 1
                      [94ms = ext_call.return_data[0]
                      mcontinue 
      revert
  if eth.balance(this.address) >= 0:
      if not eth.balance(this.address):
          if mtotalSupply:
              return (0 / mtotalSupply)
      else:
          if 10^mdecimals * eth.balance(this.address) / eth.balance(this.address) == 10^mdecimals:
              if mtotalSupply:
                  return (10^mdecimals * eth.balance(this.address) / mtotalSupply)
  revert


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
      mem[32] = 16
      require [94midx < mtokensm.length
      mem[(32 * [94midx) + 128] = mamountsm[mstor6m[[94midxm]m.field_0m]
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


# hash = 0xb50e44b8
# getter = None
# const = ['return', 122743337058602665564631354263472091436608355031343273141981057876456636416]
# payable = False
const EXCHANGE = 0x45786368616e676550726f7669646572000000000000000000000000000000


# hash = 0xb86ec38f
# getter = None
# const = ['return', "'Reimbursable'"]
# payable = False
const REIMBURSABLE = 'Reimbursable'


# hash = 0xc4d66de8
# getter = None
# const = None
# payable = False
def initialize(address m_sender): # not payable
  require caller == mowner
  require m_sender
  require mstatus <= 3
  require not mstatus
  require m_sender
  munknown5075edbfAddress = m_sender
  mstor7117 = 1
  mstor69ED = 1
  mstor3B8A = 1
  mem[192] = 'MarketProvider'
  mem[224] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[256] = 0x576974686472617750726f7669646572000000000000000000000000000000
  mem[288] = 3
  mem[320 len 96] = code.data[14699 len 96]
  [94midx = 0
  mwhile [94midx < 3m:
      require [94midx < 3
      mem[(32 * [94midx) + 320] = mem[(32 * [94midx) + 192]
      [94midx = [94midx + 1
      mcontinue 
  mem[416] = 0x981f6ab900000000000000000000000000000000000000000000000000000000
  mem[420] = 32
  mem[452] = 3
  mem[484 len 0] = None
  require ext_code.size(munknown5075edbfAddress)
  call munknown5075edbfAddress.0x981f6ab9 with:
       gas gas_remaining wei
      args Array(len=3, data=mem[484 len 96])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[416 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 416
  require return_data.size >= 32
  require mem[416 len 4], 0 <= 4294967296
  require mem[416 len 4], 0 + 32 <= return_data.size
  require mem[mem[416 len 4], 0 + 416] <= 4294967296 and mem[416 len 4], 0 + (32 * mem[mem[416 len 4], 0 + 416]) + 32 <= return_data.size
  require 3 == mem[mem[416 len 4], 0 + 416]
  [94midx = 0
  mwhile [94midx < 3m:
      require [94midx < 3
      require [94midx < mem[mem[416 len 4], 0 + 416]
      require mem[(32 * [94midx) + mem[416 len 4], 0 + 460 len 20]
      mem[0] = mem[(32 * [94midx) + 320]
      mem[32] = 1
      munknown2156e6c6m[mem[(32 * [94midx) + 320]m] = mem[(32 * [94midx) + mem[416 len 4], 0 + 460 len 20]
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown2156e6c6m[0x576974686472617750726f7669646572000000000000000000000000000000m], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(munknown2156e6c6m['MarketProvider'm])
  call munknown2156e6c6m['MarketProvider'm].0xdfd92f8a with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  mstatus = 1
  require mstatus <= 3
  log 0x7ea7eb4c: status


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
  require m_addedValue + mallowancem[callerm]m[addr(m_spender)m] >= mallowancem[callerm]m[addr(m_spender)m]
  mallowancem[callerm]m[addr(m_spender)m] += m_addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 14]]]]]
# const = None
# payable = False
def allowance(address m_owner, address m_spender): # not payable
  return mallowancem[addr(m_owner)m]m[addr(m_spender)m]


# hash = 0xe8b5e51f
# getter = None
# const = None
# payable = True
def invest() payable: 
  require mstatus <= 3
  if mstatus != 1:
      revert with 0, 'The Fund is not active'
  else:
      if call.value < 10^15:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Minimum value to invest is 0.001 ETH'
      else:
          if mtotalSupply <= 0:
              if call.value:
                  require 10^mdecimals * call.value / call.value == 10^mdecimals
                  require (10^mdecimals * call.value / 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                  mbalanceOfm[callerm] += 10^mdecimals * call.value / 10^18
                  require (10^mdecimals * call.value / 10^18) + mtotalSupply >= mtotalSupply
                  mtotalSupply += 10^mdecimals * call.value / 10^18
                  return 1
              else:
                  require mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                  require mtotalSupply >= mtotalSupply
                  return 1
          else:
              if call.value:
                  require 10^mdecimals * call.value / call.value == 10^mdecimals
                  require mtotalSupply
                  if mtotalSupply != 0:
                      [94midx = 0
                      [94ms = 0
                      mwhile [94midx < mtokensm.lengthm:
                          mem[0] = 6
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
                                  require [94midx < mtokensm.length
                                  mem[0] = 6
                                  mem[132] = mtokensm[[94midxm]m.field_0
                                  mem[164] = 10^18
                                  mem[196] = 0
                                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                       gas gas_remaining wei
                                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
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
                                              mcontinue 
                                          else:
                                              require ext_call.return_data[0]
                                              require 0 / ext_call.return_data[0] >= 0
                                              [94midx = [94midx + 1
                                              [94ms = ext_call.return_data[0]
                                              mcontinue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = ext_call.return_data[0]
                                          mcontinue 
                              else:
                                  [94midx = [94midx + 1
                                  [94ms = ext_call.return_data[0]
                                  mcontinue 
                      require eth.balance(this.address) >= 0
                      if eth.balance(this.address):
                          require 10^mdecimals * eth.balance(this.address) / eth.balance(this.address) == 10^mdecimals
                          require mtotalSupply
                          require 10^mdecimals * call.value / mtotalSupply <= 10^mdecimals * eth.balance(this.address) / mtotalSupply
                          if call.value:
                              require 10^mdecimals * call.value / call.value == 10^mdecimals
                              require (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              require (10^mdecimals * call.value / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                              mbalanceOfm[callerm] += 10^mdecimals * call.value / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              require (10^mdecimals * call.value / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                              mtotalSupply += 10^mdecimals * call.value / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              return 1
                          else:
                              require (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              require (0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                              mbalanceOfm[callerm] += 0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              require (0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                              mtotalSupply += 0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              return 1
                      else:
                          require mtotalSupply
                          require 10^mdecimals * call.value / mtotalSupply <= 0 / mtotalSupply
                          if call.value:
                              require 10^mdecimals * call.value / call.value == 10^mdecimals
                              require (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              require (10^mdecimals * call.value / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                              mbalanceOfm[callerm] += 10^mdecimals * call.value / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              require (10^mdecimals * call.value / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                              mtotalSupply += 10^mdecimals * call.value / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              return 1
                          else:
                              require (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              require (0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                              mbalanceOfm[callerm] += 0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              require (0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                              mtotalSupply += 0 / (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              return 1
                  else:
                      require 10^mdecimals * call.value / mtotalSupply <= 10^18
                      if call.value:
                          require 10^mdecimals * call.value / call.value == 10^mdecimals
                          require -(10^mdecimals * call.value / mtotalSupply) + 10^18
                          require (10^mdecimals * call.value / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                          mbalanceOfm[callerm] += 10^mdecimals * call.value / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                          require (10^mdecimals * call.value / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                          mtotalSupply += 10^mdecimals * call.value / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                          return 1
                      else:
                          require -(10^mdecimals * call.value / mtotalSupply) + 10^18
                          require (0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                          mbalanceOfm[callerm] += 0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                          require (0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                          mtotalSupply += 0 / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                          return 1
              else:
                  require mtotalSupply
                  if mtotalSupply != 0:
                      [94midx = 0
                      [94ms = 0
                      mwhile [94midx < mtokensm.lengthm:
                          mem[0] = 6
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
                                  require [94midx < mtokensm.length
                                  mem[0] = 6
                                  mem[132] = mtokensm[[94midxm]m.field_0
                                  mem[164] = 10^18
                                  mem[196] = 0
                                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                       gas gas_remaining wei
                                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94midxm]m.field_0, 10^18, 0
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
                                              mcontinue 
                                          else:
                                              require ext_call.return_data[0]
                                              require 0 / ext_call.return_data[0] >= 0
                                              [94midx = [94midx + 1
                                              [94ms = ext_call.return_data[0]
                                              mcontinue 
                                      else:
                                          [94midx = [94midx + 1
                                          [94ms = ext_call.return_data[0]
                                          mcontinue 
                              else:
                                  [94midx = [94midx + 1
                                  [94ms = ext_call.return_data[0]
                                  mcontinue 
                      require eth.balance(this.address) >= 0
                      if eth.balance(this.address):
                          require 10^mdecimals * eth.balance(this.address) / eth.balance(this.address) == 10^mdecimals
                          require mtotalSupply
                          require 0 / mtotalSupply <= 10^mdecimals * eth.balance(this.address) / mtotalSupply
                          if call.value:
                              require 10^mdecimals * call.value / call.value == 10^mdecimals
                              require (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)
                              require (10^mdecimals * call.value / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                              mbalanceOfm[callerm] += 10^mdecimals * call.value / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)
                              require (10^mdecimals * call.value / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)) + mtotalSupply >= mtotalSupply
                              mtotalSupply += 10^mdecimals * call.value / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)
                              return 1
                          else:
                              require (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)
                              require (0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                              mbalanceOfm[callerm] += 0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)
                              require (0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)) + mtotalSupply >= mtotalSupply
                              mtotalSupply += 0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)
                              return 1
                      else:
                          require mtotalSupply
                          require 0 / mtotalSupply <= 0 / mtotalSupply
                          require call.value
                          require 10^mdecimals * call.value / call.value == 10^mdecimals
                          revert
                  else:
                      require 0 / mtotalSupply <= 10^18
                      if call.value:
                          require 10^mdecimals * call.value / call.value == 10^mdecimals
                          require -(0 / mtotalSupply) + 10^18
                          require (10^mdecimals * call.value / -(0 / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                          mbalanceOfm[callerm] += 10^mdecimals * call.value / -(0 / mtotalSupply) + 10^18
                          require (10^mdecimals * call.value / -(0 / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                          mtotalSupply += 10^mdecimals * call.value / -(0 / mtotalSupply) + 10^18
                          return 1
                      else:
                          require -(0 / mtotalSupply) + 10^18
                          require (0 / -(0 / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                          mbalanceOfm[callerm] += 0 / -(0 / mtotalSupply) + 10^18
                          require (0 / -(0 / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                          mtotalSupply += 0 / -(0 / mtotalSupply) + 10^18
                          return 1


# hash = 0xef430aa6
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 3]]]], ['loc', 3]]]
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


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


