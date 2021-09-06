# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xEF1A212e09b671da1fE0B3ea30b685b9D0EEdd33 
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
    unknown1fa98406 # mask: a s
    # storage address 6
    tokens
    # storage address 7
    unknownb5f163ff
    # storage address 8
    unknown5075edbfAddress # mask: a s
    # storage address 8
    unknownad03261e # mask: a s
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
    unknown96733c5c # mask: a s
    # storage address 19
    stor19 # mask: a s
    # storage address 19
    stor19 # mask: a s
    # storage address 52726400471484607308559743408741729752080477326138179588767413797364341146058
    stor7492 # mask: a s
    # storage address 102400687454666572095736228992249912990314550370552751600037914286015365625288
    storE264 # mask: a s
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 14]]]], ['loc', 14]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x08ecd9a6
# getter = None
# const = ['return', "'LockerProvider'"]
# payable = False
const unknown08ecd9a6 = 'LockerProvider'


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address _spender, uint256 _value): # not payable
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
const unknown16ba7197 = 0x576974686472617750726f7669646572000000000000000000000000000000


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 11]
# const = None
# payable = False
def totalSupply(): # not payable
  return totalSupply


# hash = 0x1fa98406
# getter = ['storage', 8, 0, 5]
# const = None
# payable = False
def unknown1fa98406(): # not payable
  require unknown1fa98406 <= 2
  return unknown1fa98406


# hash = 0x200d2ed2
# getter = ['storage', 8, 8, 5]
# const = None
# payable = False
def status(): # not payable
  require status <= 3
  return status


# hash = 0x2156e6c6
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def unknown2156e6c6(uint256 _param1): # not payable
  return unknown2156e6c6[_param1]


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address _from, address _to, uint256 _value): # not payable
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
      if not stor9[_param1]:
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
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def decimals(): # not payable
  return decimals


# hash = 0x3ccfd60b
# getter = None
# const = None
# payable = False
def withdraw(): # not payable
  if 0 >= balanceOf[caller]:
      revert with 0, 'Insufficient balance'
  require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
  call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].0xc8c01a55 with:
       gas gas_remaining wei
      args caller, balanceOf[caller]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
  call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].0xc77e7614 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if 0 == totalSupply:
      if not ext_call.return_data[0]:
          require 10^decimals
          if 0 / 10^decimals > eth.balance(this.address):
              require eth.balance(this.address) <= 0 / 10^decimals
              if not (0 / 10^decimals) - eth.balance(this.address):
                  require 0 < tokens.length
                  require ext_code.size(addr(tokens.field_0))
                  call addr(tokens.field_0).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[96] = ext_call.return_data[0]
                  [94ms = 0
                  [94mt = 0
                  while ext_call.success:
                      require return_data.size >= 32
                      [94m_292 = mem[96]
                      if mem[96]:
                          require [94ms < tokens.length
                          mem[132] = tokens[[94ms].field_0
                          mem[164] = 10^18
                          mem[196] = 0
                          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                               gas gas_remaining wei
                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                          mem[96 len 64] = ext_call.return_data[0 len 64]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if not [94m_292:
                                  require ext_call.return_data[0]
                                  require 0 / ext_call.return_data[0] >= 0
                              else:
                                  require 10^18 * [94m_292 / [94m_292 == 10^18
                                  require ext_call.return_data[0]
                                  require 10^18 * [94m_292 / ext_call.return_data[0] >= 0
                      require [94ms + 1 < tokens.length
                      mem[0] = 6
                      mem[100] = this.address
                      require ext_code.size(tokens[[94ms].field_256)
                      call tokens[[94ms].field_256.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = [94ms + 1
                      [94mt = [94m_292
                      continue 
              else:
                  require (10000 * 0 / 10^decimals) - (10000 * eth.balance(this.address)) / (0 / 10^decimals) - eth.balance(this.address) == 10000
                  require 0 < tokens.length
                  require ext_code.size(addr(tokens.field_0))
                  call addr(tokens.field_0).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[96] = ext_call.return_data[0]
                  [94ms = 0
                  [94mt = 0
                  while ext_call.success:
                      require return_data.size >= 32
                      [94m_291 = mem[96]
                      if mem[96]:
                          require [94ms < tokens.length
                          mem[132] = tokens[[94ms].field_0
                          mem[164] = 10^18
                          mem[196] = 0
                          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                               gas gas_remaining wei
                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                          mem[96 len 64] = ext_call.return_data[0 len 64]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if not [94m_291:
                                  require ext_call.return_data[0]
                                  require 0 / ext_call.return_data[0] >= 0
                              else:
                                  require 10^18 * [94m_291 / [94m_291 == 10^18
                                  require ext_call.return_data[0]
                                  require 10^18 * [94m_291 / ext_call.return_data[0] >= 0
                      require [94ms + 1 < tokens.length
                      mem[0] = 6
                      mem[100] = this.address
                      require ext_code.size(tokens[[94ms].field_256)
                      call tokens[[94ms].field_256.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = [94ms + 1
                      [94mt = [94m_291
                      continue 
              revert with ext_call.return_data[0 len return_data.size]
      else:
          require 10^18 * ext_call.return_data[0] / ext_call.return_data[0] == 10^18
          require 10^decimals
          if 10^18 * ext_call.return_data[0] / 10^decimals > eth.balance(this.address):
              require eth.balance(this.address) <= 10^18 * ext_call.return_data[0] / 10^decimals
              if not (10^18 * ext_call.return_data[0] / 10^decimals) - eth.balance(this.address):
                  require 0 < tokens.length
                  require ext_code.size(addr(tokens.field_0))
                  call addr(tokens.field_0).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[96] = ext_call.return_data[0]
                  [94ms = 0
                  [94mt = 0
                  while ext_call.success:
                      require return_data.size >= 32
                      [94m_290 = mem[96]
                      if mem[96]:
                          require [94ms < tokens.length
                          mem[132] = tokens[[94ms].field_0
                          mem[164] = 10^18
                          mem[196] = 0
                          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                               gas gas_remaining wei
                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                          mem[96 len 64] = ext_call.return_data[0 len 64]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if not [94m_290:
                                  require ext_call.return_data[0]
                                  require 0 / ext_call.return_data[0] >= 0
                              else:
                                  require 10^18 * [94m_290 / [94m_290 == 10^18
                                  require ext_call.return_data[0]
                                  require 10^18 * [94m_290 / ext_call.return_data[0] >= 0
                      require [94ms + 1 < tokens.length
                      mem[0] = 6
                      mem[100] = this.address
                      require ext_code.size(tokens[[94ms].field_256)
                      call tokens[[94ms].field_256.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = [94ms + 1
                      [94mt = [94m_290
                      continue 
              else:
                  require (10000 * 10^18 * ext_call.return_data[0] / 10^decimals) - (10000 * eth.balance(this.address)) / (10^18 * ext_call.return_data[0] / 10^decimals) - eth.balance(this.address) == 10000
                  require 0 < tokens.length
                  require ext_code.size(addr(tokens.field_0))
                  call addr(tokens.field_0).balanceOf(address owner) with:
                       gas gas_remaining wei
                      args this.address
                  mem[96] = ext_call.return_data[0]
                  [94ms = 0
                  [94mt = 0
                  while ext_call.success:
                      require return_data.size >= 32
                      [94m_289 = mem[96]
                      if mem[96]:
                          require [94ms < tokens.length
                          mem[132] = tokens[[94ms].field_0
                          mem[164] = 10^18
                          mem[196] = 0
                          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                               gas gas_remaining wei
                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                          mem[96 len 64] = ext_call.return_data[0 len 64]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 64
                          if ext_call.return_data[0]:
                              if not [94m_289:
                                  require ext_call.return_data[0]
                                  require 0 / ext_call.return_data[0] >= 0
                              else:
                                  require 10^18 * [94m_289 / [94m_289 == 10^18
                                  require ext_call.return_data[0]
                                  require 10^18 * [94m_289 / ext_call.return_data[0] >= 0
                      require [94ms + 1 < tokens.length
                      mem[0] = 6
                      mem[100] = this.address
                      require ext_code.size(tokens[[94ms].field_256)
                      call tokens[[94ms].field_256.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = [94ms + 1
                      [94mt = [94m_289
                      continue 
              revert with ext_call.return_data[0 len return_data.size]
  else:
      [94midx = 0
      [94ms = 0
      while [94midx < tokens.length:
          mem[0] = 6
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
          mem[0] = 6
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
      require eth.balance(this.address) >= 0
      if not eth.balance(this.address):
          require totalSupply
          if not ext_call.return_data[0]:
              require 10^decimals
              if 0 / 10^decimals > eth.balance(this.address):
                  require eth.balance(this.address) <= 0 / 10^decimals
                  if not (0 / 10^decimals) - eth.balance(this.address):
                      require 0 < tokens.length
                      require ext_code.size(addr(tokens.field_0))
                      call addr(tokens.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      while ext_call.success:
                          require return_data.size >= 32
                          [94m_517 = mem[96]
                          if mem[96]:
                              require [94ms < tokens.length
                              mem[132] = tokens[[94ms].field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_517:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_517 / [94m_517 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_517 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < tokens.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(tokens[[94ms].field_256)
                          call tokens[[94ms].field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_517
                          continue 
                  else:
                      require (10000 * 0 / 10^decimals) - (10000 * eth.balance(this.address)) / (0 / 10^decimals) - eth.balance(this.address) == 10000
                      require 0 < tokens.length
                      require ext_code.size(addr(tokens.field_0))
                      call addr(tokens.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      while ext_call.success:
                          require return_data.size >= 32
                          [94m_516 = mem[96]
                          if mem[96]:
                              require [94ms < tokens.length
                              mem[132] = tokens[[94ms].field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_516:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_516 / [94m_516 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_516 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < tokens.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(tokens[[94ms].field_256)
                          call tokens[[94ms].field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_516
                          continue 
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              require 0 / totalSupply * ext_call.return_data[0] / ext_call.return_data[0] == 0 / totalSupply
              require 10^decimals
              if 0 / totalSupply * ext_call.return_data[0] / 10^decimals > eth.balance(this.address):
                  require eth.balance(this.address) <= 0 / totalSupply * ext_call.return_data[0] / 10^decimals
                  if not (0 / totalSupply * ext_call.return_data[0] / 10^decimals) - eth.balance(this.address):
                      require 0 < tokens.length
                      require ext_code.size(addr(tokens.field_0))
                      call addr(tokens.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      while ext_call.success:
                          require return_data.size >= 32
                          [94m_515 = mem[96]
                          if mem[96]:
                              require [94ms < tokens.length
                              mem[132] = tokens[[94ms].field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_515:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_515 / [94m_515 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_515 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < tokens.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(tokens[[94ms].field_256)
                          call tokens[[94ms].field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_515
                          continue 
                  else:
                      require (10000 * 0 / totalSupply * ext_call.return_data[0] / 10^decimals) - (10000 * eth.balance(this.address)) / (0 / totalSupply * ext_call.return_data[0] / 10^decimals) - eth.balance(this.address) == 10000
                      require 0 < tokens.length
                      require ext_code.size(addr(tokens.field_0))
                      call addr(tokens.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      while ext_call.success:
                          require return_data.size >= 32
                          [94m_514 = mem[96]
                          if mem[96]:
                              require [94ms < tokens.length
                              mem[132] = tokens[[94ms].field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_514:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_514 / [94m_514 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_514 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < tokens.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(tokens[[94ms].field_256)
                          call tokens[[94ms].field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_514
                          continue 
                  revert with ext_call.return_data[0 len return_data.size]
      else:
          require 10^decimals * eth.balance(this.address) / eth.balance(this.address) == 10^decimals
          require totalSupply
          if not ext_call.return_data[0]:
              require 10^decimals
              if 0 / 10^decimals > eth.balance(this.address):
                  require eth.balance(this.address) <= 0 / 10^decimals
                  if not (0 / 10^decimals) - eth.balance(this.address):
                      require 0 < tokens.length
                      require ext_code.size(addr(tokens.field_0))
                      call addr(tokens.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      while ext_call.success:
                          require return_data.size >= 32
                          [94m_513 = mem[96]
                          if mem[96]:
                              require [94ms < tokens.length
                              mem[132] = tokens[[94ms].field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_513:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_513 / [94m_513 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_513 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < tokens.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(tokens[[94ms].field_256)
                          call tokens[[94ms].field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_513
                          continue 
                  else:
                      require (10000 * 0 / 10^decimals) - (10000 * eth.balance(this.address)) / (0 / 10^decimals) - eth.balance(this.address) == 10000
                      require 0 < tokens.length
                      require ext_code.size(addr(tokens.field_0))
                      call addr(tokens.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      while ext_call.success:
                          require return_data.size >= 32
                          [94m_512 = mem[96]
                          if mem[96]:
                              require [94ms < tokens.length
                              mem[132] = tokens[[94ms].field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_512:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_512 / [94m_512 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_512 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < tokens.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(tokens[[94ms].field_256)
                          call tokens[[94ms].field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_512
                          continue 
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              require 10^decimals * eth.balance(this.address) / totalSupply * ext_call.return_data[0] / ext_call.return_data[0] == 10^decimals * eth.balance(this.address) / totalSupply
              require 10^decimals
              if 10^decimals * eth.balance(this.address) / totalSupply * ext_call.return_data[0] / 10^decimals > eth.balance(this.address):
                  require eth.balance(this.address) <= 10^decimals * eth.balance(this.address) / totalSupply * ext_call.return_data[0] / 10^decimals
                  if not (10^decimals * eth.balance(this.address) / totalSupply * ext_call.return_data[0] / 10^decimals) - eth.balance(this.address):
                      require 0 < tokens.length
                      require ext_code.size(addr(tokens.field_0))
                      call addr(tokens.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      while ext_call.success:
                          require return_data.size >= 32
                          [94m_511 = mem[96]
                          if mem[96]:
                              require [94ms < tokens.length
                              mem[132] = tokens[[94ms].field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_511:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_511 / [94m_511 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_511 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < tokens.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(tokens[[94ms].field_256)
                          call tokens[[94ms].field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_511
                          continue 
                  else:
                      require (10000 * 10^decimals * eth.balance(this.address) / totalSupply * ext_call.return_data[0] / 10^decimals) - (10000 * eth.balance(this.address)) / (10^decimals * eth.balance(this.address) / totalSupply * ext_call.return_data[0] / 10^decimals) - eth.balance(this.address) == 10000
                      require 0 < tokens.length
                      require ext_code.size(addr(tokens.field_0))
                      call addr(tokens.field_0).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args this.address
                      mem[96] = ext_call.return_data[0]
                      [94ms = 0
                      [94mt = 0
                      while ext_call.success:
                          require return_data.size >= 32
                          [94m_510 = mem[96]
                          if mem[96]:
                              require [94ms < tokens.length
                              mem[132] = tokens[[94ms].field_0
                              mem[164] = 10^18
                              mem[196] = 0
                              require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                              call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                   gas gas_remaining wei
                                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[[94ms].field_0, 10^18, 0
                              mem[96 len 64] = ext_call.return_data[0 len 64]
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >= 64
                              if ext_call.return_data[0]:
                                  if not [94m_510:
                                      require ext_call.return_data[0]
                                      require 0 / ext_call.return_data[0] >= 0
                                  else:
                                      require 10^18 * [94m_510 / [94m_510 == 10^18
                                      require ext_call.return_data[0]
                                      require 10^18 * [94m_510 / ext_call.return_data[0] >= 0
                          require [94ms + 1 < tokens.length
                          mem[0] = 6
                          mem[100] = this.address
                          require ext_code.size(tokens[[94ms].field_256)
                          call tokens[[94ms].field_256.balanceOf(address owner) with:
                               gas gas_remaining wei
                              args this.address
                          mem[96] = ext_call.return_data[0]
                          [94ms = [94ms + 1
                          [94mt = [94m_510
                          continue 
                  revert with ext_call.return_data[0 len return_data.size]
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
  require ext_call.return_data[32] <= balanceOf[caller]
  balanceOf[caller] -= ext_call.return_data[32]
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
  return 1


# hash = 0x4f64b2be
# getter = ['storage', 160, 0, ['add', ['sha3', 6], ['cd', 4]]]
# const = None
# payable = False
def tokens(uint256 _param1): # not payable
  require _param1 < tokens.length
  return tokens[_param1].field_0


# hash = 0x5075edbf
# getter = ['storage', 160, 8, 8]
# const = None
# payable = False
def unknown5075edbf(): # not payable
  return unknown5075edbfAddress


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = False
def version(): # not payable
  return version[0 len version.length]


# hash = 0x55a3b2c1
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 17]]]
# const = None
# payable = False
def amounts(address _param1): # not payable
  return amounts[_param1]


# hash = 0x5acf6903
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 18]]]]
# const = None
# payable = False
def unknown5acf6903(addr _param1): # not payable
  return bool(stor18[_param1])


# hash = 0x5f677404
# getter = None
# const = ['return', 1000000000000000000]
# payable = False
const unknown5f677404 = 10^18


# hash = 0x659eeabc
# getter = None
# const = None
# payable = False
def unknown659eeabc(): # not payable
  if tokens.length:
      mem[128 len 32 * tokens.length] = code.data[15038 len 32 * tokens.length]
  [94midx = 0
  [94ms = 0
  while [94midx < tokens.length:
      mem[0] = 6
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
      mem[(32 * tokens.length) + 160 len 32 * [94ms] = code.data[15038 len 32 * [94ms]
  [94midx = 0
  [94mt = 0
  while [94midx < tokens.length:
      require [94midx < tokens.length
      if mem[(32 * [94midx) + 128] <= 0:
          [94midx = [94midx + 1
          [94mt = [94mt
          continue 
      require [94midx < tokens.length
      mem[0] = 6
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
  if _subtractedValue <= allowance[caller][addr(_spender)]:
      allowance[caller][addr(_spender)] -= _subtractedValue
  else:
      allowance[caller][addr(_spender)] = 0
  log Approval(
        address owner=allowance[caller][addr(_spender)],
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x6f7bc9be
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 16]]]
# const = None
# payable = False
def investors(address _param1): # not payable
  return investors[_param1]


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 10]]]
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
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 2]]]], ['loc', 2]]]
# const = None
# payable = False
def description(): # not payable
  return description[0 len description.length]


# hash = 0x74d16c37
# getter = None
# const = None
# payable = False
def unknown74d16c37(): # not payable
  [94midx = 0
  [94ms = 0
  while [94midx < tokens.length:
      mem[0] = 6
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
      mem[0] = 6
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


# hash = 0x7d7c2a1c
# getter = None
# const = None
# payable = False
def unknown7d7c2a1c(): # not payable
  require caller == owner
  mem[0] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[32] = 1
  mem[96] = 0x170a1b0600000000000000000000000000000000000000000000000000000000
  mem[100] = unknown96733c5c
  require ext_code.size(unknown2156e6c6[0x526562616c616e636550726f76696465720000000000000000000000000000])
  call unknown2156e6c6[0x526562616c616e636550726f76696465720000000000000000000000000000].0x170a1b06 with:
       gas gas_remaining wei
      args unknown96733c5c
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 160
  [94m_10 = mem[96 len 4], Mask(224, 0, stor19.field_32)
  require mem[96 len 4], Mask(224, 0, stor19.field_32) <= 4294967296
  require mem[96 len 4], Mask(224, 0, stor19.field_32) + 32 <= return_data.size
  require mem[mem[96 len 4], Mask(224, 0, stor19.field_32) + 96] <= 4294967296 and mem[96 len 4], Mask(224, 0, stor19.field_32) + (32 * mem[mem[96 len 4], Mask(224, 0, stor19.field_32) + 96]) + 32 <= return_data.size
  [94m_12 = uint32(stor19.field_0), mem[132 len 28]
  require uint32(stor19.field_0), mem[132 len 28] <= 4294967296
  require uint32(stor19.field_0), mem[132 len 28] + 32 <= return_data.size
  require mem[uint32(stor19.field_0), mem[132 len 28] + 96] <= 4294967296 and uint32(stor19.field_0), mem[132 len 28] + (32 * mem[uint32(stor19.field_0), mem[132 len 28] + 96]) + 32 <= return_data.size
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
  [94m_62 = mem[mem[96 len 4], Mask(224, 0, stor19.field_32) + 96]
  [94midx = 0
  while uint8([94midx) < [94m_62:
      require uint8([94midx) < mem[[94m_10 + 96]
      [94m_66 = mem[(32 * uint8([94midx)) + [94m_10 + 128]
      mem[ceil32(return_data.size) + 100] = unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000]
      mem[ceil32(return_data.size) + 132] = 0
      require ext_code.size(addr([94m_66))
      call addr([94m_66).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], 0
      mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require uint8([94midx) < mem[[94m_10 + 96]
      [94m_74 = mem[(32 * uint8([94midx)) + [94m_10 + 128]
      require uint8([94midx) < mem[[94m_12 + 96]
      [94m_76 = mem[(32 * uint8([94midx)) + [94m_12 + 128]
      mem[ceil32(return_data.size) + 100] = unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000]
      mem[ceil32(return_data.size) + 132] = [94m_76
      require ext_code.size(addr([94m_74))
      call addr([94m_74).approve(address spender, uint256 value) with:
           gas gas_remaining wei
          args unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], [94m_76
      mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require uint8([94midx) < mem[[94m_10 + 96]
      require uint8([94midx) < mem[[94m_12 + 96]
      [94m_95 = mem[[94m_12 + (32 * uint8([94midx)) + 128]
      mem[ceil32(return_data.size) + 100] = mem[(32 * uint8([94midx)) + [94m_10 + 140 len 20]
      mem[ceil32(return_data.size) + 132] = [94m_95
      mem[ceil32(return_data.size) + 164] = 0
      mem[ceil32(return_data.size) + 196] = this.address
      mem[ceil32(return_data.size) + 228] = 0
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x8955053f with:
           gas gas_remaining wei
          args mem[ceil32(return_data.size) + 100], [94m_95, 0, this.address, 0
      mem[ceil32(return_data.size) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      [94midx = [94midx + 1
      continue 
  mem[ceil32(return_data.size) + 96] = 0x3dda288400000000000000000000000000000000000000000000000000000000
  mem[ceil32(return_data.size) + 100] = 0
  require ext_code.size(unknown2156e6c6[0x526562616c616e636550726f76696465720000000000000000000000000000])
  call unknown2156e6c6[0x526562616c616e636550726f76696465720000000000000000000000000000].0x3dda2884 with:
       gas gas_remaining wei
      args 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[ceil32(return_data.size) + 96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = (2 * ceil32(return_data.size)) + 96
  require return_data.size >= 32
  [94m_70 = mem[ceil32(return_data.size) + 96 len 4], 0
  require mem[ceil32(return_data.size) + 96 len 4], 0 <= 4294967296
  require mem[ceil32(return_data.size) + 96 len 4], 0 + 32 <= return_data.size
  require mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96 len 4], 0 + 96] <= 4294967296 and mem[ceil32(return_data.size) + 96 len 4], 0 + (32 * mem[ceil32(return_data.size) + mem[ceil32(return_data.size) + 96 len 4], 0 + 96]) + 32 <= return_data.size
  [94m_104 = mem[[94m_14 + 96]
  [94midx = 0
  while uint8([94midx) < [94m_104:
      require uint8([94midx) < mem[ceil32(return_data.size) + [94m_70 + 96]
      [94m_108 = mem[(32 * uint8([94midx)) + ceil32(return_data.size) + [94m_70 + 128]
      require uint8([94midx) < mem[[94m_14 + 96]
      require uint8([94midx) < mem[ceil32(return_data.size) + [94m_70 + 96]
      [94m_113 = mem[ceil32(return_data.size) + [94m_70 + (32 * uint8([94midx)) + 128]
      mem[(2 * ceil32(return_data.size)) + 100] = mem[(32 * uint8([94midx)) + [94m_14 + 140 len 20]
      mem[(2 * ceil32(return_data.size)) + 132] = [94m_113
      mem[(2 * ceil32(return_data.size)) + 164] = 0
      mem[(2 * ceil32(return_data.size)) + 196] = this.address
      mem[(2 * ceil32(return_data.size)) + 228] = 0
      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0xeb5d3ab5 with:
         value [94m_108 wei
           gas gas_remaining wei
          args mem[(2 * ceil32(return_data.size)) + 100], [94m_113, 0, this.address, 0
      mem[(2 * ceil32(return_data.size)) + 96] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
      [94m_104 = mem[[94m_14 + 96]
      [94midx = [94midx + 1
      continue 
  require ext_code.size(unknown2156e6c6[0x526562616c616e636550726f76696465720000000000000000000000000000])
  call unknown2156e6c6[0x526562616c616e636550726f76696465720000000000000000000000000000].finalize() with:
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
  return owner


# hash = 0x918f8674
# getter = None
# const = ['return', 10000]
# payable = False
const DENOMINATOR = 10000


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
  log StatusChanged(uint8 newStatus=status)
  return 1


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 15]]]], ['loc', 15]]]
# const = None
# payable = False
def symbol(): # not payable
  return symbol[0 len symbol.length]


# hash = 0x96733c5c
# getter = ['storage', 256, 0, 19]
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
  [94midx = 0
  [94ms = 0
  while [94midx < tokens.length:
      mem[0] = 6
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
      mem[0] = 6
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
  if eth.balance(this.address) >= 0:
      if not eth.balance(this.address):
          if totalSupply:
              return (0 / totalSupply)
      else:
          if 10^decimals * eth.balance(this.address) / eth.balance(this.address) == 10^decimals:
              if totalSupply:
                  return (10^decimals * eth.balance(this.address) / totalSupply)
  revert


# hash = 0xa3e2ce24
# getter = None
# const = None
# payable = False
def unknowna3e2ce24(): # not payable
  if tokens.length:
      mem[128 len 32 * tokens.length] = code.data[15038 len 32 * tokens.length]
  [94midx = 0
  while [94midx < tokens.length:
      mem[0] = 6
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
      [94midx = [94midx + 1
      continue 
  if not tokens.length:
      mem[(64 * tokens.length) + 160] = 64
      mem[(64 * tokens.length) + 224] = tokens.length
      [94ms = 0
      while tokens.length < 32 * tokens.length:
          mem[(66 * tokens.length) + 256] = mem[(34 * tokens.length) + 160]
          [94ms = tokens.length + 32
          continue 
      mem[(64 * tokens.length) + 192] = (32 * tokens.length) + 96
      mem[(98 * tokens.length) + 256] = tokens.length
      mem[(98 * tokens.length) + 288 len floor32(tokens.length)] = mem[128 len floor32(tokens.length)]
      return memory
        from (64 * tokens.length) + 160
         [93mlen (194 * tokens.length) + 128
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


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address _to, uint256 _value): # not payable
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
  if tokens.length:
      mem[128] = addr(tokens.field_0)
      [94midx = 128
      [94ms = 0
      while (32 * tokens.length) + 96 > [94midx:
          mem[[94midx + 32] = tokens[[94ms].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
  if unknownb5f163ff.length:
      mem[(32 * tokens.length) + 160] = uint256(unknownb5f163ff.field_0)
      [94midx = (32 * tokens.length) + 160
      [94ms = 0
      while (32 * tokens.length) + (32 * unknownb5f163ff.length) + 128 > [94midx:
          mem[[94midx + 32] = unknownb5f163ff[[94ms].field_256
          [94midx = [94midx + 32
          [94ms = [94ms + 1
          continue 
  mem[(32 * tokens.length) + (32 * unknownb5f163ff.length) + 256 len floor32(tokens.length)] = mem[128 len floor32(tokens.length)]
  mem[(64 * tokens.length) + (32 * unknownb5f163ff.length) + 256] = unknownb5f163ff.length
  mem[(64 * tokens.length) + (32 * unknownb5f163ff.length) + 288 len floor32(unknownb5f163ff.length)] = mem[(32 * tokens.length) + 160 len floor32(unknownb5f163ff.length)]
  return Array(len=tokens.length, data=mem[128 len floor32(tokens.length)], mem[(32 * tokens.length) + (32 * unknownb5f163ff.length) + floor32(tokens.length) + 256 len (32 * tokens.length) + (32 * unknownb5f163ff.length) + -floor32(tokens.length) + 32]), 
         (32 * tokens.length) + 96


# hash = 0xad03261e
# getter = ['bool', ['storage', 8, 0, 8]]
# const = None
# payable = False
def unknownad03261e(): # not payable
  return bool(unknownad03261e)


# hash = 0xb50e44b8
# getter = None
# const = ['return', 122743337058602665564631354263472091436608355031343273141981057876456636416]
# payable = False
const unknownb50e44b8 = 0x45786368616e676550726f7669646572000000000000000000000000000000


# hash = 0xb5f163ff
# getter = ['storage', 256, 0, ['add', ['sha3', 7], ['cd', 4]]]
# const = None
# payable = False
def unknownb5f163ff(uint256 _param1): # not payable
  require _param1 < unknownb5f163ff.length
  return unknownb5f163ff[_param1].field_0


# hash = 0xb86ec38f
# getter = None
# const = ['return', "'Reimbursable'"]
# payable = False
const unknownb86ec38f = 'Reimbursable'


# hash = 0xcd6dc687
# getter = None
# const = None
# payable = False
def initialize(address _registry, uint256 _validAttributeTypeID): # not payable
  require caller == owner
  require _registry
  require status <= 3
  require not status
  require _validAttributeTypeID <= 10000
  require _registry
  unknown5075edbfAddress = _registry
  storE264 = 1
  stor7492 = 1
  mem[224] = 'MarketProvider'
  mem[256] = 0x45786368616e676550726f7669646572000000000000000000000000000000
  mem[288] = 0x576974686472617750726f7669646572000000000000000000000000000000
  mem[320] = 0x526562616c616e636550726f76696465720000000000000000000000000000
  mem[352] = 4
  mem[384 len 128] = code.data[15038 len 128]
  [94midx = 0
  while [94midx < 4:
      require [94midx < 4
      mem[(32 * [94midx) + 384] = mem[(32 * [94midx) + 224]
      [94midx = [94midx + 1
      continue 
  mem[512] = 0x981f6ab900000000000000000000000000000000000000000000000000000000
  mem[516] = 32
  mem[548] = 4
  mem[580 len 0] = None
  require ext_code.size(unknown5075edbfAddress)
  call unknown5075edbfAddress.0x981f6ab9 with:
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
  while [94midx < 4:
      require [94midx < 4
      require [94midx < mem[mem[512 len 4], 0 + 512]
      require mem[(32 * [94midx) + mem[512 len 4], 0 + 556 len 20]
      mem[0] = mem[(32 * [94midx) + 384]
      mem[32] = 1
      unknown2156e6c6[mem[(32 * [94midx) + 384]] = mem[(32 * [94midx) + mem[512 len 4], 0 + 556 len 20]
      [94midx = [94midx + 1
      continue 
  require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
  call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000])
  call unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args unknown2156e6c6[0x576974686472617750726f7669646572000000000000000000000000000000], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(unknown2156e6c6[0x526562616c616e636550726f76696465720000000000000000000000000000])
  call unknown2156e6c6[0x526562616c616e636550726f76696465720000000000000000000000000000].MOT() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args unknown2156e6c6[0x526562616c616e636550726f76696465720000000000000000000000000000], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(ext_call.return_data[0]))
  call addr(ext_call.return_data[0]).approve(address spender, uint256 value) with:
       gas gas_remaining wei
      args unknown2156e6c6[0x526562616c616e636550726f76696465720000000000000000000000000000], -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(unknown2156e6c6['MarketProvider'])
  call unknown2156e6c6['MarketProvider'].0xdfd92f8a with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  unknown96733c5c = _validAttributeTypeID
  status = 1
  require status <= 3
  log StatusChanged(uint8 newStatus=status)


# hash = 0xd0febe4c
# getter = None
# const = None
# payable = False
def buyTokens(): # not payable
  require caller == owner
  if eth.balance(this.address):
      if not tokens.length:
          mem[(32 * tokens.length) + 128] = tokens.length
          mem[(64 * tokens.length) + 160] = tokens.length
          [94midx = 0
          [94ms = 0
          while uint8([94midx) < tokens.length:
              require uint8([94midx) < unknownb5f163ff.length
              if not eth.balance(this.address):
                  if uint8([94midx) < tokens.length:
                      mem[(32 * uint8([94midx)) + 128] = 0
                      if uint8([94midx) < tokens.length:
                          mem[0] = 6
                          if uint8([94midx) < mem[(64 * tokens.length) + 160]:
                              mem[(64 * tokens.length) + (32 * uint8([94midx)) + 192] = tokens[uint8([94midx)].field_0
                              if uint8([94midx) < mem[(64 * tokens.length) + 160]:
                                  if uint8([94midx) < tokens.length:
                                      mem[(98 * tokens.length) + 228] = tokens[uint8([94midx)].field_0
                                      mem[(98 * tokens.length) + 260] = 0
                                      mem[(98 * tokens.length) + 292] = 0
                                      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                                      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                           gas gas_remaining wei
                                          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[uint8([94midx)].field_0, 0, 0
                                      mem[(98 * tokens.length) + 192 len 64] = ext_call.return_data[0 len 64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 64
                                      if uint8([94midx) < mem[(32 * tokens.length) + 128]:
                                          mem[(32 * tokens.length) + (32 * uint8([94midx)) + 160] = ext_call.return_data[32]
                                          if uint8([94midx) < tokens.length:
                                              if [94ms >= [94ms:
                                                  [94midx = [94midx + 1
                                                  [94ms = [94ms
                                                  continue 
              else:
                  if unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / eth.balance(this.address) == unknownb5f163ff[uint8([94midx)].field_0:
                      if uint8([94midx) < tokens.length:
                          mem[(32 * uint8([94midx)) + 128] = unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / 100
                          if uint8([94midx) < tokens.length:
                              mem[0] = 6
                              if uint8([94midx) < mem[(64 * tokens.length) + 160]:
                                  mem[(64 * tokens.length) + (32 * uint8([94midx)) + 192] = tokens[uint8([94midx)].field_0
                                  if uint8([94midx) < mem[(64 * tokens.length) + 160]:
                                      if uint8([94midx) < tokens.length:
                                          mem[(98 * tokens.length) + 228] = tokens[uint8([94midx)].field_0
                                          mem[(98 * tokens.length) + 260] = unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / 100
                                          mem[(98 * tokens.length) + 292] = 0
                                          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                                          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                               gas gas_remaining wei
                                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[uint8([94midx)].field_0, unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / 100, 0
                                          mem[(98 * tokens.length) + 192 len 64] = ext_call.return_data[0 len 64]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 64
                                          if uint8([94midx) < mem[(32 * tokens.length) + 128]:
                                              mem[(32 * tokens.length) + (32 * uint8([94midx)) + 160] = ext_call.return_data[32]
                                              if uint8([94midx) < tokens.length:
                                                  if (unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / 100) + [94ms >= [94ms:
                                                      [94midx = [94midx + 1
                                                      [94ms = (unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / 100) + [94ms
                                                      continue 
              revert
          mem[(98 * tokens.length) + 192] = 0x15cdc52900000000000000000000000000000000000000000000000000000000
          mem[(98 * tokens.length) + 292] = this.address
          mem[(98 * tokens.length) + 324] = 0
          mem[(98 * tokens.length) + 196] = 160
          mem[(98 * tokens.length) + 356] = mem[(64 * tokens.length) + 160]
          mem[(98 * tokens.length) + 388 len floor32(mem[(64 * tokens.length) + 160])] = mem[(64 * tokens.length) + 192 len floor32(mem[(64 * tokens.length) + 160])]
          mem[(98 * tokens.length) + 228] = (32 * mem[(64 * tokens.length) + 160]) + 192
          mem[(32 * mem[(64 * tokens.length) + 160]) + (98 * tokens.length) + 388] = tokens.length
          mem[(32 * mem[(64 * tokens.length) + 160]) + (98 * tokens.length) + 420 len floor32(tokens.length)] = mem[128 len floor32(tokens.length)]
          mem[(98 * tokens.length) + 260] = (32 * tokens.length) + (32 * mem[(64 * tokens.length) + 160]) + 224
          mem[(131 * tokens.length) + (32 * mem[(64 * tokens.length) + 160]) + 420] = mem[(32 * tokens.length) + 128]
          mem[(131 * tokens.length) + (32 * mem[(64 * tokens.length) + 160]) + 452 len floor32(mem[(32 * tokens.length) + 128])] = mem[(32 * tokens.length) + 160 len floor32(mem[(32 * tokens.length) + 128])]
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x15cdc529 with:
             value [94ms wei
               gas gas_remaining wei
              args mem[(98 * tokens.length) + 196 len (32 * mem[(32 * tokens.length) + 128]) + (32 * tokens.length) + (32 * mem[(64 * tokens.length) + 160]) + 256]
      else:
          mem[128 len 32 * tokens.length] = code.data[15038 len 32 * tokens.length]
          mem[(32 * tokens.length) + 128] = tokens.length
          mem[(32 * tokens.length) + 160 len 32 * tokens.length] = code.data[15038 len 32 * tokens.length]
          mem[(64 * tokens.length) + 160] = tokens.length
          mem[(64 * tokens.length) + 192 len 32 * tokens.length] = code.data[15038 len 32 * tokens.length]
          [94midx = 0
          [94ms = 0
          while uint8([94midx) < tokens.length:
              require uint8([94midx) < unknownb5f163ff.length
              if not eth.balance(this.address):
                  if uint8([94midx) < tokens.length:
                      mem[(32 * uint8([94midx)) + 128] = 0
                      if uint8([94midx) < tokens.length:
                          mem[0] = 6
                          if uint8([94midx) < mem[(64 * tokens.length) + 160]:
                              mem[(64 * tokens.length) + (32 * uint8([94midx)) + 192] = tokens[uint8([94midx)].field_0
                              if uint8([94midx) < mem[(64 * tokens.length) + 160]:
                                  if uint8([94midx) < tokens.length:
                                      mem[(98 * tokens.length) + 228] = tokens[uint8([94midx)].field_0
                                      mem[(98 * tokens.length) + 260] = 0
                                      mem[(98 * tokens.length) + 292] = 0
                                      require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                                      call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                           gas gas_remaining wei
                                          args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[uint8([94midx)].field_0, 0, 0
                                      mem[(98 * tokens.length) + 192 len 64] = ext_call.return_data[0 len 64]
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >= 64
                                      if uint8([94midx) < mem[(32 * tokens.length) + 128]:
                                          mem[(32 * tokens.length) + (32 * uint8([94midx)) + 160] = ext_call.return_data[32]
                                          if uint8([94midx) < tokens.length:
                                              if [94ms >= [94ms:
                                                  [94midx = [94midx + 1
                                                  [94ms = [94ms
                                                  continue 
              else:
                  if unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / eth.balance(this.address) == unknownb5f163ff[uint8([94midx)].field_0:
                      if uint8([94midx) < tokens.length:
                          mem[(32 * uint8([94midx)) + 128] = unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / 100
                          if uint8([94midx) < tokens.length:
                              mem[0] = 6
                              if uint8([94midx) < mem[(64 * tokens.length) + 160]:
                                  mem[(64 * tokens.length) + (32 * uint8([94midx)) + 192] = tokens[uint8([94midx)].field_0
                                  if uint8([94midx) < mem[(64 * tokens.length) + 160]:
                                      if uint8([94midx) < tokens.length:
                                          mem[(98 * tokens.length) + 228] = tokens[uint8([94midx)].field_0
                                          mem[(98 * tokens.length) + 260] = unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / 100
                                          mem[(98 * tokens.length) + 292] = 0
                                          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
                                          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                                               gas gas_remaining wei
                                              args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, tokens[uint8([94midx)].field_0, unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / 100, 0
                                          mem[(98 * tokens.length) + 192 len 64] = ext_call.return_data[0 len 64]
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >= 64
                                          if uint8([94midx) < mem[(32 * tokens.length) + 128]:
                                              mem[(32 * tokens.length) + (32 * uint8([94midx)) + 160] = ext_call.return_data[32]
                                              if uint8([94midx) < tokens.length:
                                                  if (unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / 100) + [94ms >= [94ms:
                                                      [94midx = [94midx + 1
                                                      [94ms = (unknownb5f163ff[uint8([94midx)].field_0 * eth.balance(this.address) / 100) + [94ms
                                                      continue 
              revert
          mem[(98 * tokens.length) + 192] = 0x15cdc52900000000000000000000000000000000000000000000000000000000
          mem[(98 * tokens.length) + 292] = this.address
          mem[(98 * tokens.length) + 324] = 0
          mem[(98 * tokens.length) + 196] = 160
          mem[(98 * tokens.length) + 356] = mem[(64 * tokens.length) + 160]
          mem[(98 * tokens.length) + 388 len floor32(mem[(64 * tokens.length) + 160])] = mem[(64 * tokens.length) + 192 len floor32(mem[(64 * tokens.length) + 160])]
          mem[(98 * tokens.length) + 228] = (32 * mem[(64 * tokens.length) + 160]) + 192
          mem[(32 * mem[(64 * tokens.length) + 160]) + (98 * tokens.length) + 388] = tokens.length
          mem[(32 * mem[(64 * tokens.length) + 160]) + (98 * tokens.length) + 420 len floor32(tokens.length)] = mem[128 len floor32(tokens.length)]
          mem[(98 * tokens.length) + 260] = (32 * tokens.length) + (32 * mem[(64 * tokens.length) + 160]) + 224
          mem[(131 * tokens.length) + (32 * mem[(64 * tokens.length) + 160]) + 420] = mem[(32 * tokens.length) + 128]
          mem[(131 * tokens.length) + (32 * mem[(64 * tokens.length) + 160]) + 452 len floor32(mem[(32 * tokens.length) + 128])] = mem[(32 * tokens.length) + 160 len floor32(mem[(32 * tokens.length) + 128])]
          require ext_code.size(unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000])
          call unknown2156e6c6[0x45786368616e676550726f7669646572000000000000000000000000000000].0x15cdc529 with:
             value [94ms wei
               gas gas_remaining wei
              args 160, (32 * mem[(64 * tokens.length) + 160]) + 192, (32 * tokens.length) + (32 * mem[(64 * tokens.length) + 160]) + 224, this.address, 0, mem[(64 * tokens.length) + 160], mem[(98 * tokens.length) + 388 len (32 * tokens.length) + (32 * mem[(64 * tokens.length) + 160]) + 32], mem[(32 * tokens.length) + 128], mem[(131 * tokens.length) + (32 * mem[(64 * tokens.length) + 160]) + 452 len 32 * mem[(32 * tokens.length) + 128]]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
  return 1


# hash = 0xd3c9ad17
# getter = None
# const = ['return', 145581188027504223537441783832673983417913822530146853016789242044036939776]
# payable = False
const unknownd3c9ad17 = 0x526562616c616e636550726f76696465720000000000000000000000000000


# hash = 0xd73dd623
# getter = None
# const = None
# payable = False
def increaseApproval(address _spender, uint256 _addedValue): # not payable
  require _addedValue + allowance[caller][addr(_spender)] >= allowance[caller][addr(_spender)]
  allowance[caller][addr(_spender)] += _addedValue
  log Approval(
        address owner=(_addedValue + allowance[caller][addr(_spender)]),
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 12]]]]]
# const = None
# payable = False
def allowance(address _owner, address _spender): # not payable
  return allowance[addr(_owner)][addr(_spender)]


# hash = 0xe8b5e51f
# getter = None
# const = None
# payable = True
def invest() payable: 
  require status <= 3
  if status != 1:
      revert with 0, 'The Fund is not active'
  else:
      if call.value < 10^15:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Minimum value to invest is 0.001 ETH'
      else:
          if totalSupply <= 0:
              if call.value:
                  require 10^decimals * call.value / call.value == 10^decimals
                  require (10^decimals * call.value / 10^18) + balanceOf[caller] >= balanceOf[caller]
                  balanceOf[caller] += 10^decimals * call.value / 10^18
                  require (10^decimals * call.value / 10^18) + totalSupply >= totalSupply
                  totalSupply += 10^decimals * call.value / 10^18
                  return 1
              else:
                  require balanceOf[caller] >= balanceOf[caller]
                  require totalSupply >= totalSupply
                  return 1
          else:
              if call.value:
                  require 10^decimals * call.value / call.value == 10^decimals
                  require totalSupply
                  if totalSupply != 0:
                      [94midx = 0
                      [94ms = 0
                      while [94midx < tokens.length:
                          mem[0] = 6
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
                                  mem[0] = 6
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
                      require eth.balance(this.address) >= 0
                      if eth.balance(this.address):
                          require 10^decimals * eth.balance(this.address) / eth.balance(this.address) == 10^decimals
                          require totalSupply
                          require 10^decimals * call.value / totalSupply <= 10^decimals * eth.balance(this.address) / totalSupply
                          if call.value:
                              require 10^decimals * call.value / call.value == 10^decimals
                              require (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)
                              require (10^decimals * call.value / (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                              balanceOf[caller] += 10^decimals * call.value / (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)
                              require (10^decimals * call.value / (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)) + totalSupply >= totalSupply
                              totalSupply += 10^decimals * call.value / (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)
                              return 1
                          else:
                              require (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)
                              require (0 / (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                              balanceOf[caller] += 0 / (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)
                              require (0 / (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)) + totalSupply >= totalSupply
                              totalSupply += 0 / (10^decimals * eth.balance(this.address) / totalSupply) - (10^decimals * call.value / totalSupply)
                              return 1
                      else:
                          require totalSupply
                          require 10^decimals * call.value / totalSupply <= 0 / totalSupply
                          if call.value:
                              require 10^decimals * call.value / call.value == 10^decimals
                              require (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                              require (10^decimals * call.value / (0 / totalSupply) - (10^decimals * call.value / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                              balanceOf[caller] += 10^decimals * call.value / (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                              require (10^decimals * call.value / (0 / totalSupply) - (10^decimals * call.value / totalSupply)) + totalSupply >= totalSupply
                              totalSupply += 10^decimals * call.value / (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                              return 1
                          else:
                              require (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                              require (0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                              balanceOf[caller] += 0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                              require (0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)) + totalSupply >= totalSupply
                              totalSupply += 0 / (0 / totalSupply) - (10^decimals * call.value / totalSupply)
                              return 1
                  else:
                      require 10^decimals * call.value / totalSupply <= 10^18
                      if call.value:
                          require 10^decimals * call.value / call.value == 10^decimals
                          require -(10^decimals * call.value / totalSupply) + 10^18
                          require (10^decimals * call.value / -(10^decimals * call.value / totalSupply) + 10^18) + balanceOf[caller] >= balanceOf[caller]
                          balanceOf[caller] += 10^decimals * call.value / -(10^decimals * call.value / totalSupply) + 10^18
                          require (10^decimals * call.value / -(10^decimals * call.value / totalSupply) + 10^18) + totalSupply >= totalSupply
                          totalSupply += 10^decimals * call.value / -(10^decimals * call.value / totalSupply) + 10^18
                          return 1
                      else:
                          require -(10^decimals * call.value / totalSupply) + 10^18
                          require (0 / -(10^decimals * call.value / totalSupply) + 10^18) + balanceOf[caller] >= balanceOf[caller]
                          balanceOf[caller] += 0 / -(10^decimals * call.value / totalSupply) + 10^18
                          require (0 / -(10^decimals * call.value / totalSupply) + 10^18) + totalSupply >= totalSupply
                          totalSupply += 0 / -(10^decimals * call.value / totalSupply) + 10^18
                          return 1
              else:
                  require totalSupply
                  if totalSupply != 0:
                      [94midx = 0
                      [94ms = 0
                      while [94midx < tokens.length:
                          mem[0] = 6
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
                                  mem[0] = 6
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
                      require eth.balance(this.address) >= 0
                      if eth.balance(this.address):
                          require 10^decimals * eth.balance(this.address) / eth.balance(this.address) == 10^decimals
                          require totalSupply
                          require 0 / totalSupply <= 10^decimals * eth.balance(this.address) / totalSupply
                          if call.value:
                              require 10^decimals * call.value / call.value == 10^decimals
                              require (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)
                              require (10^decimals * call.value / (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                              balanceOf[caller] += 10^decimals * call.value / (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)
                              require (10^decimals * call.value / (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)) + totalSupply >= totalSupply
                              totalSupply += 10^decimals * call.value / (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)
                              return 1
                          else:
                              require (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)
                              require (0 / (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)) + balanceOf[caller] >= balanceOf[caller]
                              balanceOf[caller] += 0 / (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)
                              require (0 / (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)) + totalSupply >= totalSupply
                              totalSupply += 0 / (10^decimals * eth.balance(this.address) / totalSupply) - (0 / totalSupply)
                              return 1
                      else:
                          require totalSupply
                          require 0 / totalSupply <= 0 / totalSupply
                          require call.value
                          require 10^decimals * call.value / call.value == 10^decimals
                          revert
                  else:
                      require 0 / totalSupply <= 10^18
                      if call.value:
                          require 10^decimals * call.value / call.value == 10^decimals
                          require -(0 / totalSupply) + 10^18
                          require (10^decimals * call.value / -(0 / totalSupply) + 10^18) + balanceOf[caller] >= balanceOf[caller]
                          balanceOf[caller] += 10^decimals * call.value / -(0 / totalSupply) + 10^18
                          require (10^decimals * call.value / -(0 / totalSupply) + 10^18) + totalSupply >= totalSupply
                          totalSupply += 10^decimals * call.value / -(0 / totalSupply) + 10^18
                          return 1
                      else:
                          require -(0 / totalSupply) + 10^18
                          require (0 / -(0 / totalSupply) + 10^18) + balanceOf[caller] >= balanceOf[caller]
                          balanceOf[caller] += 0 / -(0 / totalSupply) + 10^18
                          require (0 / -(0 / totalSupply) + 10^18) + totalSupply >= totalSupply
                          totalSupply += 0 / -(0 / totalSupply) + 10^18
                          return 1


# hash = 0xef430aa6
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 3]]]], ['loc', 3]]]
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
const unknownf46f16c2 = 'MarketProvider'


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


