# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xD27797E0ed95Fe57127E15B0F30651A9A8D096B8 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x43d726d6': 'close()'} 

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
    status # mask: a s
    # storage address 5
    fundType # mask: a s
    # storage address 6
    tokens
    # storage address 7
    weights
    # storage address 8
    supportRebalance # mask: a s
    # storage address 8
    unknown5075edbfAddress # mask: a s
    # storage address 9
    stor9
    # storage address 10
    balanceOf
    # storage address 11
    totalSupply # mask: a s
    # storage address 12
    allowance
    # storage address 13
    decimals # mask: a s
    # storage address 14
    name
    # storage address 15
    symbol
    # storage address 16
    investors
    # storage address 17
    amounts
    # storage address 18
    stor18
    # storage address 19
    stor19 # mask: a s
    # storage address 19
    unknown96733c5c # mask: a s
    # storage address 19
    stor19 # mask: a s
    # storage address 52726400471484607308559743408741729752080477326138179588767413797364341146058
    stor7492 # mask: a s
    # storage address 99878207339731269443201174828810409820813871010918775658053253201876726833152
    storDCD1 # mask: a s
    # storage address 102400687454666572095736228992249912990314550370552751600037914286015365625288
    storE264 # mask: a s
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 14]]]], ['loc', 14]]]
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
# const = ['return', 108257214327750412406774586226674903223989967278912285064471193046758912425984]
# payable = False
const WITHDRAW = 0xef576974686472617750726f7669646572000000000000000000000000000000


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 11]
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
      if not mstor9m[m_param1m]:
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
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def decimals(): # not payable
  return mdecimals


# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = False
def withdraw(): # not payable
  if 0 >= mbalanceOfm[callerm]:
      revert with 0, 'Insufficient balance'
  require ext_code.size(munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m].0xc8c01a55 with:
       gas gas_remaining wei
      args caller, mbalanceOfm[callerm]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m].0xc77e7614 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 0 == mtotalSupply:
      if not ext_call.return_data[0]:
          require 10^mdecimals
          if 0 / 10^mdecimals > eth.balance(this.address):
              require eth.balance(this.address) <= 0 / 10^mdecimals
              if not (0 / 10^mdecimals) - eth.balance(this.address):
                  require 0 < mtokensm.length
                  require ext_code.size(addr(mtokensm.field_0))
                  call addr(mtokensm.field_0).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[96] = ext_call.return_data[0]
                  [94ms = 0
                  [94mt = 0
                  mwhile ext_call.successm:
                      require return_data.size >= 32
                      [94m_316 = mem[96]
                      if mem[96]:
                          require [94ms < mtokensm.length
                          mem[132] = mtokensm[[94msm]m.field_0
                          mem[164] = 10^18
                          mem[196] = 0
                          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                               gas gas_remaining wei
                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                          mem[96 len 64] = ext_call.return_data[0 len 64]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if not [94m_316:
                                  require ext_call.return_data[0]
                                  require 0 / ext_call.return_data[0] >= 0
                              else:
                                  require 10^18 * [94m_316 / [94m_316 == 10^18
                                  require ext_call.return_data[0]
                                  require 10^18 * [94m_316 / ext_call.return_data[0] >= 0
                      require [94ms + 1 < mtokensm.length
                      mem[0] = 6
                      mem[100] = this.address
                      require ext_code.size(mtokensm[[94msm]m.field_256)
                      call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = [94ms + 1
                      [94mt = [94m_316
                      mcontinue 
              else:
                  require (10000 * 0 / 10^mdecimals) - (10000 * eth.balance(this.address)) / (0 / 10^mdecimals) - eth.balance(this.address) == 10000
                  require 0 < mtokensm.length
                  require ext_code.size(addr(mtokensm.field_0))
                  call addr(mtokensm.field_0).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[96] = ext_call.return_data[0]
                  [94ms = 0
                  [94mt = 0
                  mwhile ext_call.successm:
                      require return_data.size >= 32
                      [94m_315 = mem[96]
                      if mem[96]:
                          require [94ms < mtokensm.length
                          mem[132] = mtokensm[[94msm]m.field_0
                          mem[164] = 10^18
                          mem[196] = 0
                          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                               gas gas_remaining wei
                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                          mem[96 len 64] = ext_call.return_data[0 len 64]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if not [94m_315:
                                  require ext_call.return_data[0]
                                  require 0 / ext_call.return_data[0] >= 0
                              else:
                                  require 10^18 * [94m_315 / [94m_315 == 10^18
                                  require ext_call.return_data[0]
                                  require 10^18 * [94m_315 / ext_call.return_data[0] >= 0
                      require [94ms + 1 < mtokensm.length
                      mem[0] = 6
                      mem[100] = this.address
                      require ext_code.size(mtokensm[[94msm]m.field_256)
                      call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = [94ms + 1
                      [94mt = [94m_315
                      mcontinue 
              revert with ext_call.return_data[0 len return_data.size]
      else:
          require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
          require 10^mdecimals
          if 10^18 * ext_call.return_data[0] / 10^mdecimals > eth.balance(this.address):
              require eth.balance(this.address) <= 10^18 * ext_call.return_data[0] / 10^mdecimals
              if not (10^18 * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address):
                  require 0 < mtokensm.length
                  require ext_code.size(addr(mtokensm.field_0))
                  call addr(mtokensm.field_0).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[96] = ext_call.return_data[0]
                  [94ms = 0
                  [94mt = 0
                  mwhile ext_call.successm:
                      require return_data.size >= 32
                      [94m_314 = mem[96]
                      if mem[96]:
                          require [94ms < mtokensm.length
                          mem[132] = mtokensm[[94msm]m.field_0
                          mem[164] = 10^18
                          mem[196] = 0
                          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                               gas gas_remaining wei
                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                          mem[96 len 64] = ext_call.return_data[0 len 64]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if not [94m_314:
                                  require ext_call.return_data[0]
                                  require 0 / ext_call.return_data[0] >= 0
                              else:
                                  require 10^18 * [94m_314 / [94m_314 == 10^18
                                  require ext_call.return_data[0]
                                  require 10^18 * [94m_314 / ext_call.return_data[0] >= 0
                      require [94ms + 1 < mtokensm.length
                      mem[0] = 6
                      mem[100] = this.address
                      require ext_code.size(mtokensm[[94msm]m.field_256)
                      call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = [94ms + 1
                      [94mt = [94m_314
                      mcontinue 
              else:
                  require (10000 * 10^18 * ext_call.return_data[0] / 10^mdecimals) - (10000 * eth.balance(this.address)) / (10^18 * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address) == 10000
                  require 0 < mtokensm.length
                  require ext_code.size(addr(mtokensm.field_0))
                  call addr(mtokensm.field_0).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[96] = ext_call.return_data[0]
                  [94ms = 0
                  [94mt = 0
                  mwhile ext_call.successm:
                      require return_data.size >= 32
                      [94m_313 = mem[96]
                      if mem[96]:
                          require [94ms < mtokensm.length
                          mem[132] = mtokensm[[94msm]m.field_0
                          mem[164] = 10^18
                          mem[196] = 0
                          require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                          call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                               gas gas_remaining wei
                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                          mem[96 len 64] = ext_call.return_data[0 len 64]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if not [94m_313:
                                  require ext_call.return_data[0]
                                  require 0 / ext_call.return_data[0] >= 0
                              else:
                                  require 10^18 * [94m_313 / [94m_313 == 10^18
                                  require ext_call.return_data[0]
                                  require 10^18 * [94m_313 / ext_call.return_data[0] >= 0
                      require [94ms + 1 < mtokensm.length
                      mem[0] = 6
                      mem[100] = this.address
                      require ext_code.size(mtokensm[[94msm]m.field_256)
                      call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = [94ms + 1
                      [94mt = [94m_313
                      mcontinue 
              revert with ext_call.return_data[0 len return_data.size]
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
      require eth.balance(this.address) >= 0
      if not eth.balance(this.address):
          require mtotalSupply
          if not ext_call.return_data[0]:
              require 10^mdecimals
              if 0 / 10^mdecimals > eth.balance(this.address):
                  require eth.balance(this.address) <= 0 / 10^mdecimals
                  if not (0 / 10^mdecimals) - eth.balance(this.address):
                      require 0 < mtokensm.length
                      require ext_code.size(addr(mtokensm.field_0))
                      call addr(mtokensm.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      mwhile ext_call.successm:
                          require return_data.size >= 32
                          [94m_557 = mem[96]
                          if mem[96]:
                              require [94ms < mtokensm.length
                              mem[132] = mtokensm[[94msm]m.field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_557:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_557 / [94m_557 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_557 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < mtokensm.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(mtokensm[[94msm]m.field_256)
                          call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_557
                          mcontinue 
                  else:
                      require (10000 * 0 / 10^mdecimals) - (10000 * eth.balance(this.address)) / (0 / 10^mdecimals) - eth.balance(this.address) == 10000
                      require 0 < mtokensm.length
                      require ext_code.size(addr(mtokensm.field_0))
                      call addr(mtokensm.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      mwhile ext_call.successm:
                          require return_data.size >= 32
                          [94m_556 = mem[96]
                          if mem[96]:
                              require [94ms < mtokensm.length
                              mem[132] = mtokensm[[94msm]m.field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_556:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_556 / [94m_556 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_556 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < mtokensm.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(mtokensm[[94msm]m.field_256)
                          call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_556
                          mcontinue 
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              require 0 / mtotalSupply * ext_call.return_data[0] / ext_call.return_data[0] == 0 / mtotalSupply
              require 10^mdecimals
              if 0 / mtotalSupply * ext_call.return_data[0] / 10^mdecimals > eth.balance(this.address):
                  require eth.balance(this.address) <= 0 / mtotalSupply * ext_call.return_data[0] / 10^mdecimals
                  if not (0 / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address):
                      require 0 < mtokensm.length
                      require ext_code.size(addr(mtokensm.field_0))
                      call addr(mtokensm.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      mwhile ext_call.successm:
                          require return_data.size >= 32
                          [94m_555 = mem[96]
                          if mem[96]:
                              require [94ms < mtokensm.length
                              mem[132] = mtokensm[[94msm]m.field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_555:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_555 / [94m_555 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_555 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < mtokensm.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(mtokensm[[94msm]m.field_256)
                          call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_555
                          mcontinue 
                  else:
                      require (10000 * 0 / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - (10000 * eth.balance(this.address)) / (0 / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address) == 10000
                      require 0 < mtokensm.length
                      require ext_code.size(addr(mtokensm.field_0))
                      call addr(mtokensm.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      mwhile ext_call.successm:
                          require return_data.size >= 32
                          [94m_554 = mem[96]
                          if mem[96]:
                              require [94ms < mtokensm.length
                              mem[132] = mtokensm[[94msm]m.field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_554:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_554 / [94m_554 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_554 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < mtokensm.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(mtokensm[[94msm]m.field_256)
                          call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_554
                          mcontinue 
                  revert with ext_call.return_data[0 len return_data.size]
      else:
          require 10^mdecimals * eth.balance(this.address) / eth.balance(this.address) == 10^mdecimals
          require mtotalSupply
          if not ext_call.return_data[0]:
              require 10^mdecimals
              if 0 / 10^mdecimals > eth.balance(this.address):
                  require eth.balance(this.address) <= 0 / 10^mdecimals
                  if not (0 / 10^mdecimals) - eth.balance(this.address):
                      require 0 < mtokensm.length
                      require ext_code.size(addr(mtokensm.field_0))
                      call addr(mtokensm.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      mwhile ext_call.successm:
                          require return_data.size >= 32
                          [94m_553 = mem[96]
                          if mem[96]:
                              require [94ms < mtokensm.length
                              mem[132] = mtokensm[[94msm]m.field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_553:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_553 / [94m_553 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_553 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < mtokensm.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(mtokensm[[94msm]m.field_256)
                          call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_553
                          mcontinue 
                  else:
                      require (10000 * 0 / 10^mdecimals) - (10000 * eth.balance(this.address)) / (0 / 10^mdecimals) - eth.balance(this.address) == 10000
                      require 0 < mtokensm.length
                      require ext_code.size(addr(mtokensm.field_0))
                      call addr(mtokensm.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      mwhile ext_call.successm:
                          require return_data.size >= 32
                          [94m_552 = mem[96]
                          if mem[96]:
                              require [94ms < mtokensm.length
                              mem[132] = mtokensm[[94msm]m.field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_552:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_552 / [94m_552 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_552 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < mtokensm.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(mtokensm[[94msm]m.field_256)
                          call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_552
                          mcontinue 
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              require 10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / ext_call.return_data[0] == 10^mdecimals * eth.balance(this.address) / mtotalSupply
              require 10^mdecimals
              if 10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / 10^mdecimals > eth.balance(this.address):
                  require eth.balance(this.address) <= 10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / 10^mdecimals
                  if not (10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address):
                      require 0 < mtokensm.length
                      require ext_code.size(addr(mtokensm.field_0))
                      call addr(mtokensm.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      mwhile ext_call.successm:
                          require return_data.size >= 32
                          [94m_551 = mem[96]
                          if mem[96]:
                              require [94ms < mtokensm.length
                              mem[132] = mtokensm[[94msm]m.field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_551:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_551 / [94m_551 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_551 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < mtokensm.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(mtokensm[[94msm]m.field_256)
                          call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_551
                          mcontinue 
                  else:
                      require (10000 * 10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - (10000 * eth.balance(this.address)) / (10^mdecimals * eth.balance(this.address) / mtotalSupply * ext_call.return_data[0] / 10^mdecimals) - eth.balance(this.address) == 10000
                      require 0 < mtokensm.length
                      require ext_code.size(addr(mtokensm.field_0))
                      call addr(mtokensm.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      mwhile ext_call.successm:
                          require return_data.size >= 32
                          [94m_550 = mem[96]
                          if mem[96]:
                              require [94ms < mtokensm.length
                              mem[132] = mtokensm[[94msm]m.field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                              call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[[94msm]m.field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_550:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_550 / [94m_550 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_550 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < mtokensm.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(mtokensm[[94msm]m.field_256)
                          call mtokensm[[94msm]m.field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_550
                          mcontinue 
                  revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m].freeze() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m].withdraw(address payee) with:
       gas gas_remaining wei
      args caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
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
  require ext_code.size(munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m].finalize() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log Transfer(
        address from=ext_call.return_data[32],
        address to=caller,
        uint256 value=0)
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
      mem[32] = 17
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
# getter = ['storage', 160, 8, 8]
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
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 17]]]
# const = None
# payable = False
def amounts(address m_param1): # not payable
  return mamountsm[m_param1m]


# hash = 0x5acf6903
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 18]]]]
# const = None
# payable = False
def activeTokens(address m_param1): # not payable
  return bool(mstor18m[m_param1m])


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
      mem[128 len 32 * mtokensm.length] = code.data[15553 len 32 * mtokensm.length]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = 6
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
      mem[(32 * mtokensm.length) + 160 len 32 * [94ms] = code.data[15553 len 32 * [94ms]
  [94midx = 0
  [94mt = 0
  mwhile [94midx < mtokensm.lengthm:
      require [94midx < mtokensm.length
      if mem[(32 * [94midx) + 128] <= 0:
          [94midx = [94midx + 1
          [94mt = [94mt
          mcontinue 
      require [94midx < mtokensm.length
      mem[0] = 6
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
# const = ['return', ['balance', 'address']]
# payable = False
const getETHBalance = eth.balance(this.address)


# hash = 0x6f7bc9be
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 16]]]
# const = None
# payable = False
def investors(address m_param1): # not payable
  return minvestorsm[m_param1m]


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 10]]]
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


# hash = 0x7d7c2a1c
# getter = None
# const = None
# payable = False
def rebalance(): # not payable
  require caller == mowner
  mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[32] = 1
  mem[96] = 0x170a1b0600000000000000000000000000000000000000000000000000000000
  mem[100] = munknown96733c5c
  require ext_code.size(munknown2156e6c6m[0x526562616c616e636550726f76696465720000000000000000000000000000m])
  call munknown2156e6c6m[0x526562616c616e636550726f76696465720000000000000000000000000000m].0x170a1b06 with:
       gas gas_remaining wei
      args munknown96733c5c
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 160
  [94m_10 = mem[96 len 4], Mask(224, 0, mstor19m.field_32)
  require mem[96 len 4], Mask(224, 0, mstor19m.field_32) <= 4294967296
  require mem[96 len 4], Mask(224, 0, mstor19m.field_32) + 32 <= return_data.size
  require mem[mem[96 len 4], Mask(224, 0, mstor19m.field_32) + 96] <= 4294967296 and mem[96 len 4], Mask(224, 0, mstor19m.field_32) + (32 * mem[mem[96 len 4], Mask(224, 0, mstor19m.field_32) + 96]) + 32 <= return_data.size
  [94m_12 = uint32(mstor19m.field_0), mem[132 len 28]
  require uint32(mstor19m.field_0), mem[132 len 28] <= 4294967296
  require uint32(mstor19m.field_0), mem[132 len 28] + 32 <= return_data.size
  require mem[uint32(mstor19m.field_0), mem[132 len 28] + 96] <= 4294967296 and uint32(mstor19m.field_0), mem[132 len 28] + (32 * mem[uint32(mstor19m.field_0), mem[132 len 28] + 96]) + 32 <= return_data.size
  [94m_14 = mem[160]
  require mem[160] <= 4294967296
  require mem[160] + 32 <= return_data.size
  require mem[mem[160] + 96] <= 4294967296 and mem[160] + (32 * mem[mem[160] + 96]) + 32 <= return_data.size
  require mem[192] <= 4294967296
  require mem[192] + 32 <= return_data.size
  require mem[mem[192] + 96] <= 4294967296 and mem[192] + (32 * mem[mem[192] + 96]) + 32 <= return_data.size
  require mem[224] <= 4294967296
  require mem[224] + 32 <= return_data.size
  require mem[mem[224] + 96] <= 4294967296 and mem[224] + (32 * mem[mem[224] + 96]) + 32 <= return_data.size
  [94m_60 = mem[mem[96 len 4], Mask(224, 0, mstor19m.field_32) + 96]
  [94midx = 0
  mwhile uint8([94midx) < [94m_60m:
      require uint8([94midx) < mem[[94m_10 + 96]
      [94m_64 = mem[(32 * uint8([94midx)) + [94m_10 + 128]
      mem[ceil32(return_data.size) + 96] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
      mem[ceil32(return_data.size) + 100] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
      mem[ceil32(return_data.size) + 132] = 0
      require ext_code.size(addr([94m_64))
      call addr([94m_64).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require uint8([94midx) < mem[[94m_10 + 96]
      [94m_70 = mem[(32 * uint8([94midx)) + [94m_10 + 128]
      require uint8([94midx) < mem[[94m_12 + 96]
      [94m_73 = mem[(32 * uint8([94midx)) + [94m_12 + 128]
      mem[ceil32(return_data.size) + 96] = 0x95ea7b300000000000000000000000000000000000000000000000000000000
      mem[ceil32(return_data.size) + 100] = munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m]
      mem[ceil32(return_data.size) + 132] = [94m_73
      require ext_code.size(addr([94m_70))
      call addr([94m_70).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m], [94m_73
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require uint8([94midx) < mem[[94m_10 + 96]
      require uint8([94midx) < mem[[94m_12 + 96]
      [94m_85 = mem[[94m_12 + (32 * uint8([94midx)) + 128]
      mem[ceil32(return_data.size) + 100] = mem[(32 * uint8([94midx)) + [94m_10 + 140 len 20]
      mem[ceil32(return_data.size) + 132] = [94m_85
      mem[ceil32(return_data.size) + 164] = 0
      mem[ceil32(return_data.size) + 196] = this.address
      mem[ceil32(return_data.size) + 228] = 0
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x8955053f with:
           gas gas_remaining wei
          args mem[ceil32(return_data.size) + 100], [94m_85, 0, this.address, 0
      mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      [94midx = [94midx + 1
      mcontinue 
  mem[ceil32(return_data.size) + 96] = 0x3dda288400000000000000000000000000000000000000000000000000000000
  mem[ceil32(return_data.size) + 100] = 0
  require ext_code.size(munknown2156e6c6m[0x526562616c616e636550726f76696465720000000000000000000000000000m])
  call munknown2156e6c6m[0x526562616c616e636550726f76696465720000000000000000000000000000m].0x3dda2884 with:
       gas gas_remaining wei
      args 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(return_data.size) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = (2 * ceil32(return_data.size)) + 96
  require return_data.size >= 32
  [94m_68 = mem[ceil32(return_data.size) + 96 len 4], 0
  require mem[ceil32(return_data.size) + 96 len 4], 0 <= 4294967296
  require mem[ceil32(return_data.size) + 96 len 4], 0 + 32 <= return_data.size
  require mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96 len 4], 0 + 96] <= 4294967296 and mem[ceil32(return_data.size) + 96 len 4], 0 + (32 * mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96 len 4], 0 + 96]) + 32 <= return_data.size
  [94m_100 = mem[[94m_14 + 96]
  [94midx = 0
  mwhile uint8([94midx) < [94m_100m:
      require uint8([94midx) < mem[ceil32(return_data.size) + [94m_68 + 96]
      [94m_104 = mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_68 + 128]
      require uint8([94midx) < mem[[94m_14 + 96]
      require uint8([94midx) < mem[ceil32(return_data.size) + [94m_68 + 96]
      [94m_109 = mem[ceil32(return_data.size) + [94m_68 + (32 * uint8([94midx)) + 128]
      mem[(2 * ceil32(return_data.size)) + 100] = mem[(32 * uint8([94midx)) + [94m_14 + 140 len 20]
      mem[(2 * ceil32(return_data.size)) + 132] = [94m_109
      mem[(2 * ceil32(return_data.size)) + 164] = 0
      mem[(2 * ceil32(return_data.size)) + 196] = this.address
      mem[(2 * ceil32(return_data.size)) + 228] = 0
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0xeb5d3ab5 with:
         value [94m_104 wei
           gas gas_remaining wei
          args mem[(2 * ceil32(return_data.size)) + 100], [94m_109, 0, this.address, 0
      mem[(2 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      [94m_100 = mem[[94m_14 + 96]
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(munknown2156e6c6m[0x526562616c616e636550726f76696465720000000000000000000000000000m])
  call munknown2156e6c6m[0x526562616c616e636550726f76696465720000000000000000000000000000m].finalize() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return 1


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
  log StatusChanged(uint8 newStatus=status)
  return 1


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 15]]]], ['loc', 15]]]
# const = None
# payable = False
def symbol(): # not payable
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0x96733c5c
# getter = ['storage', 256, 0, 19]
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


# hash = 0xa3e2ce24
# getter = None
# const = None
# payable = False
def getTokensAndAmounts(): # not payable
  if mtokensm.length:
      mem[128 len 32 * mtokensm.length] = code.data[15553 len 32 * mtokensm.length]
  [94midx = 0
  mwhile [94midx < mtokensm.lengthm:
      mem[0] = 6
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
      [94midx = [94midx + 1
      mcontinue 
  if not mtokensm.length:
      mem[(64 * mtokensm.length) + 160] = 64
      mem[(64 * mtokensm.length) + 224] = mtokensm.length
      [94ms = 0
      mwhile mtokensm.length < 32 * mtokensm.lengthm:
          mem[(66 * mtokensm.length) + 256] = mem[(34 * mtokensm.length) + 160]
          [94ms = mtokensm.length + 32
          mcontinue 
      mem[(64 * mtokensm.length) + 192] = (32 * mtokensm.length) + 96
      mem[(98 * mtokensm.length) + 256] = mtokensm.length
      mem[(98 * mtokensm.length) + 288 len floor32(mtokensm.length)] = mem[128 len floor32(mtokensm.length)]
      return memory
        from (64 * mtokensm.length) + 160
         [93mlen (194 * mtokensm.length) + 128
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
# getter = ['bool', ['storage', 8, 0, 8]]
# const = None
# payable = False
def supportRebalance(): # not payable
  return bool(msupportRebalance)


# hash = 0xb50e44b8
# getter = None
# const = ['return', 122743337058602665564631354263472091436608355031343273141981057876456636416]
# payable = False
const EXCHANGE = 0x45786368616e676550726f7669646572000000000000000000000000000000


# hash = 0xb5f163ff
# getter = ['storage', 256, 0, ['add', ['sha3', 7], ['cd', 4]]]
# const = None
# payable = False
def weights(uint256 m_param1): # not payable
  require m_param1 < mweightsm.length
  return mweightsm[m_param1m]m.field_0


# hash = 0xb86ec38f
# getter = None
# const = ['return', "'Reimbursable'"]
# payable = False
const REIMBURSABLE = 'Reimbursable'


# hash = 0xcd6dc687
# getter = None
# const = None
# payable = False
def initialize(address m_simplyBrand, uint256 m_totalSupply): # not payable
  require caller == mowner
  require m_simplyBrand
  require mstatus <= 3
  require not mstatus
  require m_totalSupply <= 10000
  require m_simplyBrand
  munknown5075edbfAddress = m_simplyBrand
  mstorE264 = 1
  mstorDCD1 = 1
  mstor7492 = 1
  mem[224] = 'MarketProvider'
  mem[256] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[288] = 0xef576974686472617750726f7669646572000000000000000000000000000000
  mem[320] = 0x526562616c616e636550726f76696465720000000000000000000000000000
  mem[352] = 4
  mem[384 len 128] = code.data[15553 len 128]
  [94midx = 0
  mwhile [94midx < 4m:
      require [94midx < 4
      mem[(32 * [94midx) + 384] = mem[(32 * [94midx) + 224]
      [94midx = [94midx + 1
      mcontinue 
  mem[512] = 0x981f6ab900000000000000000000000000000000000000000000000000000000
  mem[516] = 32
  mem[548] = 4
  mem[580 len 0] = None
  require ext_code.size(munknown5075edbfAddress)
  call munknown5075edbfAddress.0x981f6ab9 with:
       gas gas_remaining wei
      args Array(len=4, data=mem[580 len 128])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[512 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 512
  require return_data.size >= 32
  require mem[512 len 4], 0 <= 4294967296
  require mem[512 len 4], 0 + 32 <= return_data.size
  require mem[mem[512 len 4], 0 + 512] <= 4294967296 and mem[512 len 4], 0 + (32 * mem[mem[512 len 4], 0 + 512]) + 32 <= return_data.size
  require 4 == mem[mem[512 len 4], 0 + 512]
  [94midx = 0
  mwhile [94midx < 4m:
      require [94midx < 4
      require [94midx < mem[mem[512 len 4], 0 + 512]
      require mem[(32 * [94midx) + mem[512 len 4], 0 + 556 len 20]
      mem[0] = mem[(32 * [94midx) + 384]
      mem[32] = 1
      munknown2156e6c6m[mem[(32 * [94midx) + 384]m] = mem[(32 * [94midx) + mem[512 len 4], 0 + 556 len 20]
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
  require ext_code.size(munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m])
  call munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown2156e6c6m[0xef576974686472617750726f7669646572000000000000000000000000000000m], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(munknown2156e6c6m[0x526562616c616e636550726f76696465720000000000000000000000000000m])
  call munknown2156e6c6m[0x526562616c616e636550726f76696465720000000000000000000000000000m].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown2156e6c6m[0x526562616c616e636550726f76696465720000000000000000000000000000m], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args munknown2156e6c6m[0x526562616c616e636550726f76696465720000000000000000000000000000m], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(munknown2156e6c6m['MarketProvider'm])
  call munknown2156e6c6m['MarketProvider'm].0xdfd92f8a with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  munknown96733c5c = m_totalSupply
  mstatus = 1
  require mstatus <= 3
  log StatusChanged(uint8 newStatus=status)


# hash = 0xd0febe4c
# getter = None
# const = None
# payable = False
def buyTokens(): # not payable
  require caller == mowner
  if eth.balance(this.address):
      if not mtokensm.length:
          mem[(32 * mtokensm.length) + 128] = mtokensm.length
          mem[(64 * mtokensm.length) + 160] = mtokensm.length
      else:
          mem[128 len 32 * mtokensm.length] = code.data[15553 len 32 * mtokensm.length]
          mem[(32 * mtokensm.length) + 128] = mtokensm.length
          mem[(32 * mtokensm.length) + 160 len 32 * mtokensm.length] = code.data[15553 len 32 * mtokensm.length]
          mem[(64 * mtokensm.length) + 160] = mtokensm.length
          mem[(64 * mtokensm.length) + 192 len 32 * mtokensm.length] = code.data[15553 len 32 * mtokensm.length]
      [94midx = 0
      [94ms = 0
      mwhile uint8([94midx) < mtokensm.lengthm:
          require uint8([94midx) < mweightsm.length
          if not eth.balance(this.address):
              if uint8([94midx) < mtokensm.length:
                  mem[(32 * uint8([94midx)) + 128] = 0
                  if uint8([94midx) < mtokensm.length:
                      mem[0] = 6
                      if uint8([94midx) < mem[(64 * mtokensm.length) + 160]:
                          mem[(64 * mtokensm.length) + (32 * uint8([94midx)) + 192] = mtokensm[uint8([94midx)m]m.field_0
                          if uint8([94midx) < mem[(64 * mtokensm.length) + 160]:
                              if uint8([94midx) < mtokensm.length:
                                  mem[(98 * mtokensm.length) + 228] = mtokensm[uint8([94midx)m]m.field_0
                                  mem[(98 * mtokensm.length) + 260] = 0
                                  mem[(98 * mtokensm.length) + 292] = 0
                                  require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                  call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                       gas gas_remaining wei
                                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[uint8([94midx)m]m.field_0, 0, 0
                                  mem[(98 * mtokensm.length) + 192 len 64] = ext_call.return_data[0 len 64]
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >= 64
                                  if uint8([94midx) < mem[(32 * mtokensm.length) + 128]:
                                      mem[(32 * mtokensm.length) + (32 * uint8([94midx)) + 160] = ext_call.return_data[32]
                                      if uint8([94midx) < mtokensm.length:
                                          if [94ms >= [94ms:
                                              [94midx = [94midx + 1
                                              [94ms = [94ms
                                              mcontinue 
          else:
              if mweightsm[uint8([94midx)m]m.field_0 * eth.balance(this.address) / eth.balance(this.address) == mweightsm[uint8([94midx)m]m.field_0:
                  if uint8([94midx) < mtokensm.length:
                      mem[(32 * uint8([94midx)) + 128] = mweightsm[uint8([94midx)m]m.field_0 * eth.balance(this.address) / 100
                      if uint8([94midx) < mtokensm.length:
                          mem[0] = 6
                          if uint8([94midx) < mem[(64 * mtokensm.length) + 160]:
                              mem[(64 * mtokensm.length) + (32 * uint8([94midx)) + 192] = mtokensm[uint8([94midx)m]m.field_0
                              if uint8([94midx) < mem[(64 * mtokensm.length) + 160]:
                                  if uint8([94midx) < mtokensm.length:
                                      mem[(98 * mtokensm.length) + 228] = mtokensm[uint8([94midx)m]m.field_0
                                      mem[(98 * mtokensm.length) + 260] = mweightsm[uint8([94midx)m]m.field_0 * eth.balance(this.address) / 100
                                      mem[(98 * mtokensm.length) + 292] = 0
                                      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
                                      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                           gas gas_remaining wei
                                          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mtokensm[uint8([94midx)m]m.field_0, mweightsm[uint8([94midx)m]m.field_0 * eth.balance(this.address) / 100, 0
                                      mem[(98 * mtokensm.length) + 192 len 64] = ext_call.return_data[0 len 64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 64
                                      if uint8([94midx) < mem[(32 * mtokensm.length) + 128]:
                                          mem[(32 * mtokensm.length) + (32 * uint8([94midx)) + 160] = ext_call.return_data[32]
                                          if uint8([94midx) < mtokensm.length:
                                              if (mweightsm[uint8([94midx)m]m.field_0 * eth.balance(this.address) / 100) + [94ms >= [94ms:
                                                  [94midx = [94midx + 1
                                                  [94ms = (mweightsm[uint8([94midx)m]m.field_0 * eth.balance(this.address) / 100) + [94ms
                                                  mcontinue 
          revert
      mem[(98 * mtokensm.length) + 192] = 0x15cdc52900000000000000000000000000000000000000000000000000000000
      mem[(98 * mtokensm.length) + 292] = this.address
      mem[(98 * mtokensm.length) + 324] = 0
      mem[(98 * mtokensm.length) + 196] = 160
      mem[(98 * mtokensm.length) + 356] = mem[(64 * mtokensm.length) + 160]
      mem[(98 * mtokensm.length) + 388 len floor32(mem[(64 * mtokensm.length) + 160])] = mem[(64 * mtokensm.length) + 192 len floor32(mem[(64 * mtokensm.length) + 160])]
      mem[(98 * mtokensm.length) + 228] = (32 * mem[(64 * mtokensm.length) + 160]) + 192
      mem[(32 * mem[(64 * mtokensm.length) + 160]) + (98 * mtokensm.length) + 388] = mtokensm.length
      mem[(32 * mem[(64 * mtokensm.length) + 160]) + (98 * mtokensm.length) + 420 len floor32(mtokensm.length)] = mem[128 len floor32(mtokensm.length)]
      mem[(98 * mtokensm.length) + 260] = (32 * mtokensm.length) + (32 * mem[(64 * mtokensm.length) + 160]) + 224
      mem[(131 * mtokensm.length) + (32 * mem[(64 * mtokensm.length) + 160]) + 420] = mem[(32 * mtokensm.length) + 128]
      mem[(131 * mtokensm.length) + (32 * mem[(64 * mtokensm.length) + 160]) + 452 len floor32(mem[(32 * mtokensm.length) + 128])] = mem[(32 * mtokensm.length) + 160 len floor32(mem[(32 * mtokensm.length) + 128])]
      require ext_code.size(munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m])
      call munknown2156e6c6m[0x45786368616e676550726f7669646572000000000000000000000000000000m].0x15cdc529 with:
         value [94ms wei
           gas gas_remaining wei
          args 160, (32 * mem[(64 * mtokensm.length) + 160]) + 192, (32 * mtokensm.length) + (32 * mem[(64 * mtokensm.length) + 160]) + 224, this.address, 0, mem[(64 * mtokensm.length) + 160], mem[(98 * mtokensm.length) + 388 len (32 * mtokensm.length) + (32 * mem[(64 * mtokensm.length) + 160]) + 32], mem[(32 * mtokensm.length) + 128], mem[(131 * mtokensm.length) + (32 * mem[(64 * mtokensm.length) + 160]) + 452 len 32 * mem[(32 * mtokensm.length) + 128]]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
  return 1


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
  require m_addedValue + mallowancem[callerm]m[addr(m_spender)m] >= mallowancem[callerm]m[addr(m_spender)m]
  mallowancem[callerm]m[addr(m_spender)m] += m_addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 12]]]]]
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
                  log Transfer(
                        address from=(10^decimals * call.value / 10^18),
                        address to=0,
                        uint256 value=caller)
                  return 1
              else:
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
                              log Transfer(
                                    address from=(10^decimals * call.value / (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)),
                                    address to=0,
                                    uint256 value=caller)
                              return 1
                          else:
                              require (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              require (0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                              mbalanceOfm[callerm] += 0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              require (0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)) + mtotalSupply >= mtotalSupply
                              mtotalSupply += 0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
                              log Transfer(
                                    address from=(0 / (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)),
                                    address to=0,
                                    uint256 value=caller)
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
                              log Transfer(
                                    address from=(10^decimals * call.value / (0 / totalSupply) - (10^decimals * call.value / totalSupply)),
                                    address to=0,
                                    uint256 value=caller)
                              return 1
                          else:
                              require (0 / mtotalSupply) - (10^mdecimals * call.value / mtotalSupply)
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
                      if call.value:
                          require 10^mdecimals * call.value / call.value == 10^mdecimals
                          require -(10^mdecimals * call.value / mtotalSupply) + 10^18
                          require (10^mdecimals * call.value / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                          mbalanceOfm[callerm] += 10^mdecimals * call.value / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                          require (10^mdecimals * call.value / -(10^mdecimals * call.value / mtotalSupply) + 10^18) + mtotalSupply >= mtotalSupply
                          mtotalSupply += 10^mdecimals * call.value / -(10^mdecimals * call.value / mtotalSupply) + 10^18
                          log Transfer(
                                address from=(10^decimals * call.value / -(10^decimals * call.value / totalSupply) + 10^18),
                                address to=0,
                                uint256 value=caller)
                          return 1
                      else:
                          require -(10^mdecimals * call.value / mtotalSupply) + 10^18
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
                              log Transfer(
                                    address from=(10^decimals * call.value / (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)),
                                    address to=0,
                                    uint256 value=caller)
                              return 1
                          else:
                              require (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)
                              require (0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)) + mbalanceOfm[callerm] >= mbalanceOfm[callerm]
                              mbalanceOfm[callerm] += 0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)
                              require (0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)) + mtotalSupply >= mtotalSupply
                              mtotalSupply += 0 / (10^mdecimals * eth.balance(this.address) / mtotalSupply) - (0 / mtotalSupply)
                              log Transfer(
                                    address from=(0 / (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)),
                                    address to=0,
                                    uint256 value=caller)
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
                          log Transfer(
                                address from=(10^decimals * call.value / -(0 / totalSupply) + 10^18),
                                address to=0,
                                uint256 value=caller)
                          return 1
                      else:
                          require -(0 / mtotalSupply) + 10^18
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


