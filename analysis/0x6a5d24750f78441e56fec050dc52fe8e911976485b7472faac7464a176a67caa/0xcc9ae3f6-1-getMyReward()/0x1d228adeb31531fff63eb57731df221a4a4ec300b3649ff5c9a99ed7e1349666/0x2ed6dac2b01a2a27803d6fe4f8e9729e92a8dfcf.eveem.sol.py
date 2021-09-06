# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x2ED6DAC2b01A2a27803d6FE4f8E9729E92a8Dfcf 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x173825d9': 'removeOwner(address _owner)', '0x7065cb48': 'addOwner(address _owner)'} 

# storage definitions
def storage:
    # storage address 0
    m_required # mask: a s
    # storage address 1
    m_numOwners # mask: a s
    # storage address 2
    stor2
    # storage address 258
    stor258
    # storage address 259
    stor259
    # storage address 260
    stor260
    # storage address 261
    m_dailyLimit # mask: a s
    # storage address 262
    stor262 # mask: a s
    # storage address 263
    stor263 # mask: a s
    # storage address 264
    unknowndd287692Address # mask: a s
    # storage address 265
    unknown458e8a0a # mask: a s
    # storage address 266
    unknown4534e5f6 # mask: a s
    # storage address 267
    stor267
# hash = 0x2f54bf6e
# getter = None
# const = None
# payable = True
def isOwner(address _addr) payable: 
  return (stor258[addr(_addr)] > 0)


# hash = 0x4123cb6b
# getter = ['storage', 256, 0, 1]
# const = None
# payable = True
def m_numOwners() payable: 
  return m_numOwners


# hash = 0x4534e5f6
# getter = ['storage', 8, 0, 266]
# const = None
# payable = True
def unknown4534e5f6() payable: 
  return unknown4534e5f6


# hash = 0x458e8a0a
# getter = ['storage', 256, 0, 265]
# const = None
# payable = True
def unknown458e8a0a() payable: 
  return unknown458e8a0a


# hash = 0x5c52c2f5
# getter = None
# const = None
# payable = True
def resetSpentToday() payable: 
  if stor258[caller] != 0:
      if stor259[call.data[0 len calldata.size]].field_0:
          if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
              stop
          else:
              log Confirmation(
                    address owner=caller,
                    bytes32 operation=sha3(call.data[0 len calldata.size]))
              if stor259[call.data[0 len calldata.size]].field_0 > 1:
                  stor259[call.data[0 len calldata.size]].field_0--
                  stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                  stop
              else:
                  require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                  stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                  stor259[call.data[0 len calldata.size]].field_0 = 0
                  stor259[call.data[0 len calldata.size]].field_256 = 0
                  stor259[call.data[0 len calldata.size]].field_512 = 0
                  stor262 = 0
                  stop
      else:
          stor259[call.data[0 len calldata.size]].field_0 = m_required
          stor259[call.data[0 len calldata.size]].field_256 = 0
          stor260.length++
          if not stor260.length > stor260.length + 1:
              stor259[call.data[0 len calldata.size]].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size])
              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
                  stop
              else:
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=sha3(call.data[0 len calldata.size]))
                  if stor259[call.data[0 len calldata.size]].field_0 > 1:
                      stor259[call.data[0 len calldata.size]].field_0--
                      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                      stop
                  else:
                      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                      stor259[call.data[0 len calldata.size]].field_0 = 0
                      stor259[call.data[0 len calldata.size]].field_256 = 0
                      stor259[call.data[0 len calldata.size]].field_512 = 0
                      stor262 = 0
                      stop
          else:
              [94midx = stor260.length + 1
              while stor260.length > [94midx:
                  stor260[[94midx] = 0
                  [94midx = [94midx + 1
                  continue 
              stor259[call.data[0 len calldata.size]].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size])
              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
                  stop
              else:
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=sha3(call.data[0 len calldata.size]))
                  if stor259[call.data[0 len calldata.size]].field_0 > 1:
                      stor259[call.data[0 len calldata.size]].field_0--
                      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                      stop
                  else:
                      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                      stor259[call.data[0 len calldata.size]].field_0 = 0
                      stor259[call.data[0 len calldata.size]].field_256 = 0
                      stor259[call.data[0 len calldata.size]].field_512 = 0
                      stor262 = 0
                      stop
  else:
      stop


# hash = 0x632a9a52
# getter = None
# const = None
# payable = True
def vote() payable: 
  call unknowndd287692Address.vote(uint256 proposalNumber, bool supportsProposal) with:
       gas gas_remaining - 25050 wei
      args 98, 1
  require ext_call.success


# hash = 0x746c9171
# getter = ['storage', 256, 0, 0]
# const = None
# payable = True
def m_required() payable: 
  return m_required


# hash = 0x797af627
# getter = None
# const = None
# payable = True
def confirm(bytes32 _h) payable: 
  if stor258[caller] != 0:
      if stor259[_h].field_0:
          if 2^stor258[caller] and stor259[_h].field_256 != 0:
              return 0
          else:
              mem[128] = _h
              log Confirmation(
                    address owner=caller,
                    bytes32 operation=_h)
              if stor259[_h].field_0 > 1:
                  stor259[_h].field_0--
                  stor259[_h].field_256 = 2^stor258[caller] or stor259[_h].field_256
                  return 0
              else:
                  require stor259[_h].field_512 < stor260.length
                  stor[code.data[4948 len 32] + stor259[_h].field_512] = 0
                  stor259[_h].field_0 = 0
                  stor259[_h].field_256 = 0
                  stor259[_h].field_512 = 0
                  if not addr(stor267[_h].field_0):
                      return 0
                  else:
                      mem[96] = stor267[_h][2].field_0
                      [94midx = 96
                      [94ms = 0
                      while stor267[_h][2].length + 96 > [94midx + 32:
                          mem[[94midx + 32] = stor267[_h][[94ms + 2].field_256
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          continue 
                      call addr(stor267[_h].field_0).mem[96 len 4] with:
                         value stor267[_h].field_256 wei
                           gas gas_remaining - 34050 wei
                          args mem[100 len stor267[_h][2].length + (floor32(stor267[_h][2].length - 1) + -stor267[_h][2].length + 32 % 32) - 4]
                      mem[288] = stor267[_h][2].field_0
                      [94midx = 288
                      [94ms = 0
                      while stor267[_h][2].length + 288 > [94midx + 32:
                          mem[[94midx + 32] = stor267[_h][[94ms + 2].field_256
                          [94midx = [94midx + 32
                          [94ms = [94ms + 1
                          continue 
                      log MultiTransact(
                            address owner=caller,
                            bytes32 operation=_h,
                            uint256 value=stor267[_h].field_256,
                            address to=addr(stor267[_h].field_0),
                            bytes data=Array(len=stor267[_h][2].length, data=mem[288 len stor267[_h][2].length + (floor32(stor267[_h][2].length - 1) + -stor267[_h][2].length + 32 % 32)]))
                      addr(stor267[_h].field_0) = 0
                      stor267[_h].field_256 = 0
                      stor267[_h].field_512 = 0
                      if 31 < stor267[_h][2].length:
                          [94midx = 0
                          while stor267[_h][2].length + 31 / 32 > [94midx:
                              stor267[_h][[94midx + 2].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                          return 1
                      else:
                          return 1
      else:
          stor259[_h].field_0 = m_required
          stor259[_h].field_256 = 0
          stor260.length++
          if not stor260.length > stor260.length + 1:
              stor259[_h].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = _h
              if 2^stor258[caller] and stor259[_h].field_256 != 0:
                  return 0
              else:
                  mem[128] = _h
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=_h)
                  if stor259[_h].field_0 > 1:
                      stor259[_h].field_0--
                      stor259[_h].field_256 = 2^stor258[caller] or stor259[_h].field_256
                      return 0
                  else:
                      require stor259[_h].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[_h].field_512] = 0
                      stor259[_h].field_0 = 0
                      stor259[_h].field_256 = 0
                      stor259[_h].field_512 = 0
                      if not addr(stor267[_h].field_0):
                          return 0
                      else:
                          mem[96] = stor267[_h][2].field_0
                          [94midx = 96
                          [94ms = 0
                          while stor267[_h][2].length + 96 > [94midx + 32:
                              mem[[94midx + 32] = stor267[_h][[94ms + 2].field_256
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              continue 
                          call addr(stor267[_h].field_0).mem[96 len 4] with:
                             value stor267[_h].field_256 wei
                               gas gas_remaining - 34050 wei
                              args mem[100 len stor267[_h][2].length + (floor32(stor267[_h][2].length - 1) + -stor267[_h][2].length + 32 % 32) - 4]
                          mem[288] = stor267[_h][2].field_0
                          [94midx = 288
                          [94ms = 0
                          while stor267[_h][2].length + 288 > [94midx + 32:
                              mem[[94midx + 32] = stor267[_h][[94ms + 2].field_256
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              continue 
                          log MultiTransact(
                                address owner=caller,
                                bytes32 operation=_h,
                                uint256 value=stor267[_h].field_256,
                                address to=addr(stor267[_h].field_0),
                                bytes data=Array(len=stor267[_h][2].length, data=mem[288 len stor267[_h][2].length + (floor32(stor267[_h][2].length - 1) + -stor267[_h][2].length + 32 % 32)]))
                          addr(stor267[_h].field_0) = 0
                          stor267[_h].field_256 = 0
                          stor267[_h].field_512 = 0
                          if 31 < stor267[_h][2].length:
                              [94midx = 0
                              while stor267[_h][2].length + 31 / 32 > [94midx:
                                  stor267[_h][[94midx + 2].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                              return 1
                          else:
                              return 1
          else:
              [94midx = stor260.length + 1
              while stor260.length > [94midx:
                  stor260[[94midx] = 0
                  [94midx = [94midx + 1
                  continue 
              stor259[_h].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = _h
              if 2^stor258[caller] and stor259[_h].field_256 != 0:
                  return 0
              else:
                  mem[128] = _h
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=_h)
                  if stor259[_h].field_0 > 1:
                      stor259[_h].field_0--
                      stor259[_h].field_256 = 2^stor258[caller] or stor259[_h].field_256
                      return 0
                  else:
                      require stor259[_h].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[_h].field_512] = 0
                      stor259[_h].field_0 = 0
                      stor259[_h].field_256 = 0
                      stor259[_h].field_512 = 0
                      if not addr(stor267[_h].field_0):
                          return 0
                      else:
                          mem[96] = stor267[_h][2].field_0
                          [94midx = 96
                          [94ms = 0
                          while stor267[_h][2].length + 96 > [94midx + 32:
                              mem[[94midx + 32] = stor267[_h][[94ms + 2].field_256
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              continue 
                          call addr(stor267[_h].field_0).mem[96 len 4] with:
                             value stor267[_h].field_256 wei
                               gas gas_remaining - 34050 wei
                              args mem[100 len stor267[_h][2].length + (floor32(stor267[_h][2].length - 1) + -stor267[_h][2].length + 32 % 32) - 4]
                          mem[288] = stor267[_h][2].field_0
                          [94midx = 288
                          [94ms = 0
                          while stor267[_h][2].length + 288 > [94midx + 32:
                              mem[[94midx + 32] = stor267[_h][[94ms + 2].field_256
                              [94midx = [94midx + 32
                              [94ms = [94ms + 1
                              continue 
                          log MultiTransact(
                                address owner=caller,
                                bytes32 operation=_h,
                                uint256 value=stor267[_h].field_256,
                                address to=addr(stor267[_h].field_0),
                                bytes data=Array(len=stor267[_h][2].length, data=mem[288 len stor267[_h][2].length + (floor32(stor267[_h][2].length - 1) + -stor267[_h][2].length + 32 % 32)]))
                          addr(stor267[_h].field_0) = 0
                          stor267[_h].field_256 = 0
                          stor267[_h].field_512 = 0
                          if 31 < stor267[_h][2].length:
                              [94midx = 0
                              while stor267[_h][2].length + 31 / 32 > [94midx:
                                  stor267[_h][[94midx + 2].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                              return 1
                          else:
                              return 1
  else:
      return 0


# hash = 0xa89a9ffb
# getter = None
# const = None
# payable = True
def unknowna89a9ffb(addr _param1) payable: 
  require caller == 0x6b671106bf4de59243111c0fece9f43da91595f
  call _param1 with:
     value eth.balance(this.address) wei
       gas 0 wei


# hash = 0xb20d30a9
# getter = None
# const = None
# payable = True
def setDailyLimit(uint256 _dailyLimit) payable: 
  if stor258[caller] != 0:
      if stor259[call.data[0 len calldata.size]].field_0:
          if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
              stop
          else:
              log Confirmation(
                    address owner=caller,
                    bytes32 operation=sha3(call.data[0 len calldata.size]))
              if stor259[call.data[0 len calldata.size]].field_0 > 1:
                  stor259[call.data[0 len calldata.size]].field_0--
                  stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                  stop
              else:
                  require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                  stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                  stor259[call.data[0 len calldata.size]].field_0 = 0
                  stor259[call.data[0 len calldata.size]].field_256 = 0
                  stor259[call.data[0 len calldata.size]].field_512 = 0
                  m_dailyLimit = _dailyLimit
                  stop
      else:
          stor259[call.data[0 len calldata.size]].field_0 = m_required
          stor259[call.data[0 len calldata.size]].field_256 = 0
          stor260.length++
          if not stor260.length > stor260.length + 1:
              stor259[call.data[0 len calldata.size]].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size])
              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
                  stop
              else:
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=sha3(call.data[0 len calldata.size]))
                  if stor259[call.data[0 len calldata.size]].field_0 > 1:
                      stor259[call.data[0 len calldata.size]].field_0--
                      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                      stop
                  else:
                      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                      stor259[call.data[0 len calldata.size]].field_0 = 0
                      stor259[call.data[0 len calldata.size]].field_256 = 0
                      stor259[call.data[0 len calldata.size]].field_512 = 0
                      m_dailyLimit = _dailyLimit
                      stop
          else:
              [94midx = stor260.length + 1
              while stor260.length > [94midx:
                  stor260[[94midx] = 0
                  [94midx = [94midx + 1
                  continue 
              stor259[call.data[0 len calldata.size]].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size])
              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
                  stop
              else:
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=sha3(call.data[0 len calldata.size]))
                  if stor259[call.data[0 len calldata.size]].field_0 > 1:
                      stor259[call.data[0 len calldata.size]].field_0--
                      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                      stop
                  else:
                      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                      stor259[call.data[0 len calldata.size]].field_0 = 0
                      stor259[call.data[0 len calldata.size]].field_256 = 0
                      stor259[call.data[0 len calldata.size]].field_512 = 0
                      m_dailyLimit = _dailyLimit
                      stop
  else:
      stop


# hash = 0xb61d27f6
# getter = None
# const = None
# payable = True
def execute(address _to, uint256 _value, bytes _data) payable: 
  if stor258[caller] <= 0:
      return 0
  else:
      if stor258[caller] <= 0:
          mem[96 len calldata.size] = call.data[0 len calldata.size]
          mem[calldata.size + 96] = block.number
          if stor258[caller] != 0:
              if stor259[call.data[0 len calldata.size]][block.number].field_0:
                  if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                          return sha3(call.data[0 len calldata.size], block.number)
                      else:
                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                          [94ms = 0
                          [94midx = _data + 36
                          while _data + _data.length + 36 > [94midx:
                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                              [94ms = [94ms + 1
                              [94midx = [94midx + 32
                              continue 
                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                          log ConfirmationNeeded(
                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                address initiator=caller,
                                uint256 value=_value,
                                address to=addr(_to),
                                bytes data=Array(len=_data.length, data=_data[all]))
                          return sha3(call.data[0 len calldata.size], block.number)
                  else:
                      mem[128] = sha3(call.data[0 len calldata.size], block.number)
                      log Confirmation(
                            address owner=caller,
                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                      if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                          stor259[call.data[0 len calldata.size]][block.number].field_0--
                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                              return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                              [94ms = 0
                              [94midx = _data + 36
                              while _data + _data.length + 36 > [94midx:
                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                  [94ms = [94ms + 1
                                  [94midx = [94midx + 32
                                  continue 
                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                              log ConfirmationNeeded(
                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                    address initiator=caller,
                                    uint256 value=_value,
                                    address to=addr(_to),
                                    bytes data=Array(len=_data.length, data=_data[all]))
                              return sha3(call.data[0 len calldata.size], block.number)
                      else:
                          require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                          stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                          stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                          stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                          if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                              if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                  return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                  [94ms = 0
                                  [94midx = _data + 36
                                  while _data + _data.length + 36 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                      [94ms = [94ms + 1
                                      [94midx = [94midx + 32
                                      continue 
                                  [94midx = Mask(251, 0, _data.length + 31) >> 5
                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                      [94midx = [94midx + 1
                                      continue 
                                  log ConfirmationNeeded(
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                        address initiator=caller,
                                        uint256 value=_value,
                                        address to=addr(_to),
                                        bytes data=Array(len=_data.length, data=_data[all]))
                                  return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                              [94midx = 96
                              [94ms = 0
                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                  mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                  [94midx = [94midx + 32
                                  [94ms = [94ms + 1
                                  continue 
                              call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                 value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                   gas gas_remaining - 34050 wei
                                  args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                              mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                              [94midx = 288
                              [94ms = 0
                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                  mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                  [94midx = [94midx + 32
                                  [94ms = [94ms + 1
                                  continue 
                              log MultiTransact(
                                    address owner=caller,
                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                    uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                    address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                    bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                              addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                              stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                              stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                              if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                  [94midx = 0
                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                      [94midx = [94midx + 1
                                      continue 
                                  return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  return sha3(call.data[0 len calldata.size], block.number)
              else:
                  stor259[call.data[0 len calldata.size]][block.number].field_0 = m_required
                  stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                  stor260.length++
                  if not stor260.length > stor260.length + 1:
                      stor259[call.data[0 len calldata.size]][block.number].field_512 = stor260.length
                      require stor260.length < stor260.length
                      stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size], block.number)
                      if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                              return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                              [94ms = 0
                              [94midx = _data + 36
                              while _data + _data.length + 36 > [94midx:
                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                  [94ms = [94ms + 1
                                  [94midx = [94midx + 32
                                  continue 
                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                              log ConfirmationNeeded(
                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                    address initiator=caller,
                                    uint256 value=_value,
                                    address to=addr(_to),
                                    bytes data=Array(len=_data.length, data=_data[all]))
                              return sha3(call.data[0 len calldata.size], block.number)
                      else:
                          mem[128] = sha3(call.data[0 len calldata.size], block.number)
                          log Confirmation(
                                address owner=caller,
                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                          if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                              stor259[call.data[0 len calldata.size]][block.number].field_0--
                              stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                              if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                  return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                  [94ms = 0
                                  [94midx = _data + 36
                                  while _data + _data.length + 36 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                      [94ms = [94ms + 1
                                      [94midx = [94midx + 32
                                      continue 
                                  [94midx = Mask(251, 0, _data.length + 31) >> 5
                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                      [94midx = [94midx + 1
                                      continue 
                                  log ConfirmationNeeded(
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                        address initiator=caller,
                                        uint256 value=_value,
                                        address to=addr(_to),
                                        bytes data=Array(len=_data.length, data=_data[all]))
                                  return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                              stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                              stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                              stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                              stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                              if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                  if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                      [94ms = 0
                                      [94midx = _data + 36
                                      while _data + _data.length + 36 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                          [94ms = [94ms + 1
                                          [94midx = [94midx + 32
                                          continue 
                                      [94midx = Mask(251, 0, _data.length + 31) >> 5
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      log ConfirmationNeeded(
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            address initiator=caller,
                                            uint256 value=_value,
                                            address to=addr(_to),
                                            bytes data=Array(len=_data.length, data=_data[all]))
                                      return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                  [94midx = 96
                                  [94ms = 0
                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                      mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                      [94midx = [94midx + 32
                                      [94ms = [94ms + 1
                                      continue 
                                  call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                     value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                       gas gas_remaining - 34050 wei
                                      args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                  mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                  [94midx = 288
                                  [94ms = 0
                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                      mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                      [94midx = [94midx + 32
                                      [94ms = [94ms + 1
                                      continue 
                                  log MultiTransact(
                                        address owner=caller,
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                        uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                        address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                        bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                  addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                  if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                      [94midx = 0
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      return sha3(call.data[0 len calldata.size], block.number)
                  else:
                      [94midx = stor260.length + 1
                      while stor260.length > [94midx:
                          stor260[[94midx] = 0
                          [94midx = [94midx + 1
                          continue 
                      stor259[call.data[0 len calldata.size]][block.number].field_512 = stor260.length
                      require stor260.length < stor260.length
                      stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size], block.number)
                      if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                              return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                              [94ms = 0
                              [94midx = _data + 36
                              while _data + _data.length + 36 > [94midx:
                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                  [94ms = [94ms + 1
                                  [94midx = [94midx + 32
                                  continue 
                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                              log ConfirmationNeeded(
                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                    address initiator=caller,
                                    uint256 value=_value,
                                    address to=addr(_to),
                                    bytes data=Array(len=_data.length, data=_data[all]))
                              return sha3(call.data[0 len calldata.size], block.number)
                      else:
                          mem[128] = sha3(call.data[0 len calldata.size], block.number)
                          log Confirmation(
                                address owner=caller,
                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                          if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                              stor259[call.data[0 len calldata.size]][block.number].field_0--
                              stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                              if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                  return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                  [94ms = 0
                                  [94midx = _data + 36
                                  while _data + _data.length + 36 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                      [94ms = [94ms + 1
                                      [94midx = [94midx + 32
                                      continue 
                                  [94midx = Mask(251, 0, _data.length + 31) >> 5
                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                      [94midx = [94midx + 1
                                      continue 
                                  log ConfirmationNeeded(
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                        address initiator=caller,
                                        uint256 value=_value,
                                        address to=addr(_to),
                                        bytes data=Array(len=_data.length, data=_data[all]))
                                  return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                              stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                              stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                              stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                              stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                              if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                  if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                      [94ms = 0
                                      [94midx = _data + 36
                                      while _data + _data.length + 36 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                          [94ms = [94ms + 1
                                          [94midx = [94midx + 32
                                          continue 
                                      [94midx = Mask(251, 0, _data.length + 31) >> 5
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      log ConfirmationNeeded(
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            address initiator=caller,
                                            uint256 value=_value,
                                            address to=addr(_to),
                                            bytes data=Array(len=_data.length, data=_data[all]))
                                      return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                  [94midx = 96
                                  [94ms = 0
                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                      mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                      [94midx = [94midx + 32
                                      [94ms = [94ms + 1
                                      continue 
                                  call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                     value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                       gas gas_remaining - 34050 wei
                                      args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                  mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                  [94midx = 288
                                  [94ms = 0
                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                      mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                      [94midx = [94midx + 32
                                      [94ms = [94ms + 1
                                      continue 
                                  log MultiTransact(
                                        address owner=caller,
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                        uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                        address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                        bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                  addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                  if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                      [94midx = 0
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      return sha3(call.data[0 len calldata.size], block.number)
          else:
              if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                  return sha3(call.data[0 len calldata.size], block.number)
              else:
                  stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                  stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                  stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                  [94ms = 0
                  [94midx = _data + 36
                  while _data + _data.length + 36 > [94midx:
                      stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                      [94ms = [94ms + 1
                      [94midx = [94midx + 32
                      continue 
                  [94midx = Mask(251, 0, _data.length + 31) >> 5
                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                      [94midx = [94midx + 1
                      continue 
                  log ConfirmationNeeded(
                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                        address initiator=caller,
                        uint256 value=_value,
                        address to=addr(_to),
                        bytes data=Array(len=_data.length, data=_data[all]))
                  return sha3(call.data[0 len calldata.size], block.number)
      else:
          if block.timestamp / 24 * 3600 <= stor263:
              if _value + stor262 < stor262:
                  mem[96 len calldata.size] = call.data[0 len calldata.size]
                  mem[calldata.size + 96] = block.number
                  if stor258[caller] != 0:
                      if stor259[call.data[0 len calldata.size]][block.number].field_0:
                          if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                              if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                  return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                  [94ms = 0
                                  [94midx = _data + 36
                                  while _data + _data.length + 36 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                      [94ms = [94ms + 1
                                      [94midx = [94midx + 32
                                      continue 
                                  [94midx = Mask(251, 0, _data.length + 31) >> 5
                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                      [94midx = [94midx + 1
                                      continue 
                                  log ConfirmationNeeded(
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                        address initiator=caller,
                                        uint256 value=_value,
                                        address to=addr(_to),
                                        bytes data=Array(len=_data.length, data=_data[all]))
                                  return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              mem[128] = sha3(call.data[0 len calldata.size], block.number)
                              log Confirmation(
                                    address owner=caller,
                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                              if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                  stor259[call.data[0 len calldata.size]][block.number].field_0--
                                  stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                  if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                      [94ms = 0
                                      [94midx = _data + 36
                                      while _data + _data.length + 36 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                          [94ms = [94ms + 1
                                          [94midx = [94midx + 32
                                          continue 
                                      [94midx = Mask(251, 0, _data.length + 31) >> 5
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      log ConfirmationNeeded(
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            address initiator=caller,
                                            uint256 value=_value,
                                            address to=addr(_to),
                                            bytes data=Array(len=_data.length, data=_data[all]))
                                      return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                  stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                  stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                  stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                  stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                  if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                      [94midx = 96
                                      [94ms = 0
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                          mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                          [94midx = [94midx + 32
                                          [94ms = [94ms + 1
                                          continue 
                                      call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                         value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                           gas gas_remaining - 34050 wei
                                          args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                      mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                      [94midx = 288
                                      [94ms = 0
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                          mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                          [94midx = [94midx + 32
                                          [94ms = [94ms + 1
                                          continue 
                                      log MultiTransact(
                                            address owner=caller,
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                            address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                            bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                      addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                      if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                          [94midx = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          return sha3(call.data[0 len calldata.size], block.number)
                      else:
                          stor259[call.data[0 len calldata.size]][block.number].field_0 = m_required
                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                          stor260.length++
                          if not stor260.length > stor260.length + 1:
                              stor259[call.data[0 len calldata.size]][block.number].field_512 = stor260.length
                              require stor260.length < stor260.length
                              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size], block.number)
                              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                                  if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                      [94ms = 0
                                      [94midx = _data + 36
                                      while _data + _data.length + 36 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                          [94ms = [94ms + 1
                                          [94midx = [94midx + 32
                                          continue 
                                      [94midx = Mask(251, 0, _data.length + 31) >> 5
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      log ConfirmationNeeded(
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            address initiator=caller,
                                            uint256 value=_value,
                                            address to=addr(_to),
                                            bytes data=Array(len=_data.length, data=_data[all]))
                                      return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  mem[128] = sha3(call.data[0 len calldata.size], block.number)
                                  log Confirmation(
                                        address owner=caller,
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                                  if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                      stor259[call.data[0 len calldata.size]][block.number].field_0--
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                      if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                              [94ms = 0
                                              [94midx = _data + 36
                                              while _data + _data.length + 36 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                  [94ms = [94ms + 1
                                                  [94midx = [94midx + 32
                                                  continue 
                                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              log ConfirmationNeeded(
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    address initiator=caller,
                                                    uint256 value=_value,
                                                    address to=addr(_to),
                                                    bytes data=Array(len=_data.length, data=_data[all]))
                                              return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 96
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                             value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                               gas gas_remaining - 34050 wei
                                              args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                          mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 288
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          log MultiTransact(
                                                address owner=caller,
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                                address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                                bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                          addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                          if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                              [94midx = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              [94midx = stor260.length + 1
                              while stor260.length > [94midx:
                                  stor260[[94midx] = 0
                                  [94midx = [94midx + 1
                                  continue 
                              stor259[call.data[0 len calldata.size]][block.number].field_512 = stor260.length
                              require stor260.length < stor260.length
                              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size], block.number)
                              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                                  if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                      [94ms = 0
                                      [94midx = _data + 36
                                      while _data + _data.length + 36 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                          [94ms = [94ms + 1
                                          [94midx = [94midx + 32
                                          continue 
                                      [94midx = Mask(251, 0, _data.length + 31) >> 5
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      log ConfirmationNeeded(
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            address initiator=caller,
                                            uint256 value=_value,
                                            address to=addr(_to),
                                            bytes data=Array(len=_data.length, data=_data[all]))
                                      return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  mem[128] = sha3(call.data[0 len calldata.size], block.number)
                                  log Confirmation(
                                        address owner=caller,
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                                  if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                      stor259[call.data[0 len calldata.size]][block.number].field_0--
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                      if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                              [94ms = 0
                                              [94midx = _data + 36
                                              while _data + _data.length + 36 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                  [94ms = [94ms + 1
                                                  [94midx = [94midx + 32
                                                  continue 
                                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              log ConfirmationNeeded(
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    address initiator=caller,
                                                    uint256 value=_value,
                                                    address to=addr(_to),
                                                    bytes data=Array(len=_data.length, data=_data[all]))
                                              return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 96
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                             value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                               gas gas_remaining - 34050 wei
                                              args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                          mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 288
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          log MultiTransact(
                                                address owner=caller,
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                                address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                                bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                          addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                          if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                              [94midx = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              return sha3(call.data[0 len calldata.size], block.number)
                  else:
                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                          return sha3(call.data[0 len calldata.size], block.number)
                      else:
                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                          [94ms = 0
                          [94midx = _data + 36
                          while _data + _data.length + 36 > [94midx:
                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                              [94ms = [94ms + 1
                              [94midx = [94midx + 32
                              continue 
                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                          log ConfirmationNeeded(
                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                address initiator=caller,
                                uint256 value=_value,
                                address to=addr(_to),
                                bytes data=Array(len=_data.length, data=_data[all]))
                          return sha3(call.data[0 len calldata.size], block.number)
              else:
                  if _value + stor262 > m_dailyLimit:
                      mem[96 len calldata.size] = call.data[0 len calldata.size]
                      mem[calldata.size + 96] = block.number
                      if stor258[caller] != 0:
                          if stor259[call.data[0 len calldata.size]][block.number].field_0:
                              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                                  if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                      [94ms = 0
                                      [94midx = _data + 36
                                      while _data + _data.length + 36 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                          [94ms = [94ms + 1
                                          [94midx = [94midx + 32
                                          continue 
                                      [94midx = Mask(251, 0, _data.length + 31) >> 5
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      log ConfirmationNeeded(
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            address initiator=caller,
                                            uint256 value=_value,
                                            address to=addr(_to),
                                            bytes data=Array(len=_data.length, data=_data[all]))
                                      return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  mem[128] = sha3(call.data[0 len calldata.size], block.number)
                                  log Confirmation(
                                        address owner=caller,
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                                  if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                      stor259[call.data[0 len calldata.size]][block.number].field_0--
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                      if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                              [94ms = 0
                                              [94midx = _data + 36
                                              while _data + _data.length + 36 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                  [94ms = [94ms + 1
                                                  [94midx = [94midx + 32
                                                  continue 
                                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              log ConfirmationNeeded(
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    address initiator=caller,
                                                    uint256 value=_value,
                                                    address to=addr(_to),
                                                    bytes data=Array(len=_data.length, data=_data[all]))
                                              return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 96
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                             value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                               gas gas_remaining - 34050 wei
                                              args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                          mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 288
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          log MultiTransact(
                                                address owner=caller,
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                                address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                                bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                          addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                          if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                              [94midx = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              stor259[call.data[0 len calldata.size]][block.number].field_0 = m_required
                              stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                              stor260.length++
                              if not stor260.length > stor260.length + 1:
                                  stor259[call.data[0 len calldata.size]][block.number].field_512 = stor260.length
                                  require stor260.length < stor260.length
                                  stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size], block.number)
                                  if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      mem[128] = sha3(call.data[0 len calldata.size], block.number)
                                      log Confirmation(
                                            address owner=caller,
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                                      if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                          stor259[call.data[0 len calldata.size]][block.number].field_0--
                                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                              [94ms = 0
                                              [94midx = _data + 36
                                              while _data + _data.length + 36 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                  [94ms = [94ms + 1
                                                  [94midx = [94midx + 32
                                                  continue 
                                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              log ConfirmationNeeded(
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    address initiator=caller,
                                                    uint256 value=_value,
                                                    address to=addr(_to),
                                                    bytes data=Array(len=_data.length, data=_data[all]))
                                              return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                          stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                          if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                              else:
                                                  stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                                  [94ms = 0
                                                  [94midx = _data + 36
                                                  while _data + _data.length + 36 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                      [94ms = [94ms + 1
                                                      [94midx = [94midx + 32
                                                      continue 
                                                  [94midx = Mask(251, 0, _data.length + 31) >> 5
                                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  log ConfirmationNeeded(
                                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                        address initiator=caller,
                                                        uint256 value=_value,
                                                        address to=addr(_to),
                                                        bytes data=Array(len=_data.length, data=_data[all]))
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                              [94midx = 96
                                              [94ms = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                                  mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                                  [94midx = [94midx + 32
                                                  [94ms = [94ms + 1
                                                  continue 
                                              call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                                 value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                                   gas gas_remaining - 34050 wei
                                                  args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                              mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                              [94midx = 288
                                              [94ms = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                                  mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                                  [94midx = [94midx + 32
                                                  [94ms = [94ms + 1
                                                  continue 
                                              log MultiTransact(
                                                    address owner=caller,
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                                    address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                                    bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                              addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                              if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                                  [94midx = 0
                                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                              else:
                                                  return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  [94midx = stor260.length + 1
                                  while stor260.length > [94midx:
                                      stor260[[94midx] = 0
                                      [94midx = [94midx + 1
                                      continue 
                                  stor259[call.data[0 len calldata.size]][block.number].field_512 = stor260.length
                                  require stor260.length < stor260.length
                                  stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size], block.number)
                                  if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      mem[128] = sha3(call.data[0 len calldata.size], block.number)
                                      log Confirmation(
                                            address owner=caller,
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                                      if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                          stor259[call.data[0 len calldata.size]][block.number].field_0--
                                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                              [94ms = 0
                                              [94midx = _data + 36
                                              while _data + _data.length + 36 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                  [94ms = [94ms + 1
                                                  [94midx = [94midx + 32
                                                  continue 
                                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              log ConfirmationNeeded(
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    address initiator=caller,
                                                    uint256 value=_value,
                                                    address to=addr(_to),
                                                    bytes data=Array(len=_data.length, data=_data[all]))
                                              return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                          stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                          if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                              else:
                                                  stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                                  [94ms = 0
                                                  [94midx = _data + 36
                                                  while _data + _data.length + 36 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                      [94ms = [94ms + 1
                                                      [94midx = [94midx + 32
                                                      continue 
                                                  [94midx = Mask(251, 0, _data.length + 31) >> 5
                                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  log ConfirmationNeeded(
                                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                        address initiator=caller,
                                                        uint256 value=_value,
                                                        address to=addr(_to),
                                                        bytes data=Array(len=_data.length, data=_data[all]))
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                              [94midx = 96
                                              [94ms = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                                  mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                                  [94midx = [94midx + 32
                                                  [94ms = [94ms + 1
                                                  continue 
                                              call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                                 value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                                   gas gas_remaining - 34050 wei
                                                  args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                              mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                              [94midx = 288
                                              [94ms = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                                  mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                                  [94midx = [94midx + 32
                                                  [94ms = [94ms + 1
                                                  continue 
                                              log MultiTransact(
                                                    address owner=caller,
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                                    address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                                    bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                              addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                              if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                                  [94midx = 0
                                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                              else:
                                                  return sha3(call.data[0 len calldata.size], block.number)
                      else:
                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                              return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                              [94ms = 0
                              [94midx = _data + 36
                              while _data + _data.length + 36 > [94midx:
                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                  [94ms = [94ms + 1
                                  [94midx = [94midx + 32
                                  continue 
                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                              log ConfirmationNeeded(
                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                    address initiator=caller,
                                    uint256 value=_value,
                                    address to=addr(_to),
                                    bytes data=Array(len=_data.length, data=_data[all]))
                              return sha3(call.data[0 len calldata.size], block.number)
                  else:
                      stor262 += _value
                      log SingleTransact(
                            address owner=caller,
                            uint256 value=_value,
                            address to=addr(_to),
                            bytes data=Array(len=_data.length, data=_data[all]))
                      call _to with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                          args _data[all]
                      return 0
          else:
              stor262 = 0
              stor263 = block.timestamp / 24 * 3600
              if _value + stor262 < stor262:
                  mem[96 len calldata.size] = call.data[0 len calldata.size]
                  mem[calldata.size + 96] = block.number
                  if stor258[caller] != 0:
                      if stor259[call.data[0 len calldata.size]][block.number].field_0:
                          if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                              if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                  return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                  [94ms = 0
                                  [94midx = _data + 36
                                  while _data + _data.length + 36 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                      [94ms = [94ms + 1
                                      [94midx = [94midx + 32
                                      continue 
                                  [94midx = Mask(251, 0, _data.length + 31) >> 5
                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                      [94midx = [94midx + 1
                                      continue 
                                  log ConfirmationNeeded(
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                        address initiator=caller,
                                        uint256 value=_value,
                                        address to=addr(_to),
                                        bytes data=Array(len=_data.length, data=_data[all]))
                                  return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              mem[128] = sha3(call.data[0 len calldata.size], block.number)
                              log Confirmation(
                                    address owner=caller,
                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                              if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                  stor259[call.data[0 len calldata.size]][block.number].field_0--
                                  stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                  if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                      [94ms = 0
                                      [94midx = _data + 36
                                      while _data + _data.length + 36 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                          [94ms = [94ms + 1
                                          [94midx = [94midx + 32
                                          continue 
                                      [94midx = Mask(251, 0, _data.length + 31) >> 5
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      log ConfirmationNeeded(
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            address initiator=caller,
                                            uint256 value=_value,
                                            address to=addr(_to),
                                            bytes data=Array(len=_data.length, data=_data[all]))
                                      return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                  stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                  stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                  stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                  stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                  if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                      [94midx = 96
                                      [94ms = 0
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                          mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                          [94midx = [94midx + 32
                                          [94ms = [94ms + 1
                                          continue 
                                      call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                         value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                           gas gas_remaining - 34050 wei
                                          args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                      mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                      [94midx = 288
                                      [94ms = 0
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                          mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                          [94midx = [94midx + 32
                                          [94ms = [94ms + 1
                                          continue 
                                      log MultiTransact(
                                            address owner=caller,
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                            address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                            bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                      addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                      if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                          [94midx = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          return sha3(call.data[0 len calldata.size], block.number)
                      else:
                          stor259[call.data[0 len calldata.size]][block.number].field_0 = m_required
                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                          stor260.length++
                          if not stor260.length > stor260.length + 1:
                              stor259[call.data[0 len calldata.size]][block.number].field_512 = stor260.length
                              require stor260.length < stor260.length
                              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size], block.number)
                              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                                  if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                      [94ms = 0
                                      [94midx = _data + 36
                                      while _data + _data.length + 36 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                          [94ms = [94ms + 1
                                          [94midx = [94midx + 32
                                          continue 
                                      [94midx = Mask(251, 0, _data.length + 31) >> 5
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      log ConfirmationNeeded(
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            address initiator=caller,
                                            uint256 value=_value,
                                            address to=addr(_to),
                                            bytes data=Array(len=_data.length, data=_data[all]))
                                      return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  mem[128] = sha3(call.data[0 len calldata.size], block.number)
                                  log Confirmation(
                                        address owner=caller,
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                                  if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                      stor259[call.data[0 len calldata.size]][block.number].field_0--
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                      if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                              [94ms = 0
                                              [94midx = _data + 36
                                              while _data + _data.length + 36 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                  [94ms = [94ms + 1
                                                  [94midx = [94midx + 32
                                                  continue 
                                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              log ConfirmationNeeded(
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    address initiator=caller,
                                                    uint256 value=_value,
                                                    address to=addr(_to),
                                                    bytes data=Array(len=_data.length, data=_data[all]))
                                              return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 96
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                             value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                               gas gas_remaining - 34050 wei
                                              args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                          mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 288
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          log MultiTransact(
                                                address owner=caller,
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                                address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                                bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                          addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                          if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                              [94midx = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              [94midx = stor260.length + 1
                              while stor260.length > [94midx:
                                  stor260[[94midx] = 0
                                  [94midx = [94midx + 1
                                  continue 
                              stor259[call.data[0 len calldata.size]][block.number].field_512 = stor260.length
                              require stor260.length < stor260.length
                              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size], block.number)
                              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                                  if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                      [94ms = 0
                                      [94midx = _data + 36
                                      while _data + _data.length + 36 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                          [94ms = [94ms + 1
                                          [94midx = [94midx + 32
                                          continue 
                                      [94midx = Mask(251, 0, _data.length + 31) >> 5
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      log ConfirmationNeeded(
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            address initiator=caller,
                                            uint256 value=_value,
                                            address to=addr(_to),
                                            bytes data=Array(len=_data.length, data=_data[all]))
                                      return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  mem[128] = sha3(call.data[0 len calldata.size], block.number)
                                  log Confirmation(
                                        address owner=caller,
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                                  if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                      stor259[call.data[0 len calldata.size]][block.number].field_0--
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                      if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                              [94ms = 0
                                              [94midx = _data + 36
                                              while _data + _data.length + 36 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                  [94ms = [94ms + 1
                                                  [94midx = [94midx + 32
                                                  continue 
                                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              log ConfirmationNeeded(
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    address initiator=caller,
                                                    uint256 value=_value,
                                                    address to=addr(_to),
                                                    bytes data=Array(len=_data.length, data=_data[all]))
                                              return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 96
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                             value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                               gas gas_remaining - 34050 wei
                                              args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                          mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 288
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          log MultiTransact(
                                                address owner=caller,
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                                address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                                bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                          addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                          if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                              [94midx = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              return sha3(call.data[0 len calldata.size], block.number)
                  else:
                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                          return sha3(call.data[0 len calldata.size], block.number)
                      else:
                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                          [94ms = 0
                          [94midx = _data + 36
                          while _data + _data.length + 36 > [94midx:
                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                              [94ms = [94ms + 1
                              [94midx = [94midx + 32
                              continue 
                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                          log ConfirmationNeeded(
                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                address initiator=caller,
                                uint256 value=_value,
                                address to=addr(_to),
                                bytes data=Array(len=_data.length, data=_data[all]))
                          return sha3(call.data[0 len calldata.size], block.number)
              else:
                  if _value + stor262 > m_dailyLimit:
                      mem[96 len calldata.size] = call.data[0 len calldata.size]
                      mem[calldata.size + 96] = block.number
                      if stor258[caller] != 0:
                          if stor259[call.data[0 len calldata.size]][block.number].field_0:
                              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                                  if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                      return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                      stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                      stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                      [94ms = 0
                                      [94midx = _data + 36
                                      while _data + _data.length + 36 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                          [94ms = [94ms + 1
                                          [94midx = [94midx + 32
                                          continue 
                                      [94midx = Mask(251, 0, _data.length + 31) >> 5
                                      while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                          stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                          [94midx = [94midx + 1
                                          continue 
                                      log ConfirmationNeeded(
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                            address initiator=caller,
                                            uint256 value=_value,
                                            address to=addr(_to),
                                            bytes data=Array(len=_data.length, data=_data[all]))
                                      return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  mem[128] = sha3(call.data[0 len calldata.size], block.number)
                                  log Confirmation(
                                        address owner=caller,
                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                                  if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                      stor259[call.data[0 len calldata.size]][block.number].field_0--
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                      stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                      if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                              [94ms = 0
                                              [94midx = _data + 36
                                              while _data + _data.length + 36 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                  [94ms = [94ms + 1
                                                  [94midx = [94midx + 32
                                                  continue 
                                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              log ConfirmationNeeded(
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    address initiator=caller,
                                                    uint256 value=_value,
                                                    address to=addr(_to),
                                                    bytes data=Array(len=_data.length, data=_data[all]))
                                              return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 96
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                             value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                               gas gas_remaining - 34050 wei
                                              args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                          mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                          [94midx = 288
                                          [94ms = 0
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                              mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                              [94midx = [94midx + 32
                                              [94ms = [94ms + 1
                                              continue 
                                          log MultiTransact(
                                                address owner=caller,
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                                address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                                bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                          addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                          if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                              [94midx = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              stor259[call.data[0 len calldata.size]][block.number].field_0 = m_required
                              stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                              stor260.length++
                              if not stor260.length > stor260.length + 1:
                                  stor259[call.data[0 len calldata.size]][block.number].field_512 = stor260.length
                                  require stor260.length < stor260.length
                                  stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size], block.number)
                                  if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      mem[128] = sha3(call.data[0 len calldata.size], block.number)
                                      log Confirmation(
                                            address owner=caller,
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                                      if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                          stor259[call.data[0 len calldata.size]][block.number].field_0--
                                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                              [94ms = 0
                                              [94midx = _data + 36
                                              while _data + _data.length + 36 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                  [94ms = [94ms + 1
                                                  [94midx = [94midx + 32
                                                  continue 
                                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              log ConfirmationNeeded(
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    address initiator=caller,
                                                    uint256 value=_value,
                                                    address to=addr(_to),
                                                    bytes data=Array(len=_data.length, data=_data[all]))
                                              return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                          stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                          if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                              else:
                                                  stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                                  [94ms = 0
                                                  [94midx = _data + 36
                                                  while _data + _data.length + 36 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                      [94ms = [94ms + 1
                                                      [94midx = [94midx + 32
                                                      continue 
                                                  [94midx = Mask(251, 0, _data.length + 31) >> 5
                                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  log ConfirmationNeeded(
                                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                        address initiator=caller,
                                                        uint256 value=_value,
                                                        address to=addr(_to),
                                                        bytes data=Array(len=_data.length, data=_data[all]))
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                              [94midx = 96
                                              [94ms = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                                  mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                                  [94midx = [94midx + 32
                                                  [94ms = [94ms + 1
                                                  continue 
                                              call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                                 value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                                   gas gas_remaining - 34050 wei
                                                  args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                              mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                              [94midx = 288
                                              [94ms = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                                  mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                                  [94midx = [94midx + 32
                                                  [94ms = [94ms + 1
                                                  continue 
                                              log MultiTransact(
                                                    address owner=caller,
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                                    address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                                    bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                              addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                              if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                                  [94midx = 0
                                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                              else:
                                                  return sha3(call.data[0 len calldata.size], block.number)
                              else:
                                  [94midx = stor260.length + 1
                                  while stor260.length > [94midx:
                                      stor260[[94midx] = 0
                                      [94midx = [94midx + 1
                                      continue 
                                  stor259[call.data[0 len calldata.size]][block.number].field_512 = stor260.length
                                  require stor260.length < stor260.length
                                  stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size], block.number)
                                  if 2^stor258[caller] and stor259[call.data[0 len calldata.size]][block.number].field_256 != 0:
                                      if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                          return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                          stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                          stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                          [94ms = 0
                                          [94midx = _data + 36
                                          while _data + _data.length + 36 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                              [94ms = [94ms + 1
                                              [94midx = [94midx + 32
                                              continue 
                                          [94midx = Mask(251, 0, _data.length + 31) >> 5
                                          while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                              stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                              [94midx = [94midx + 1
                                              continue 
                                          log ConfirmationNeeded(
                                                bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                address initiator=caller,
                                                uint256 value=_value,
                                                address to=addr(_to),
                                                bytes data=Array(len=_data.length, data=_data[all]))
                                          return sha3(call.data[0 len calldata.size], block.number)
                                  else:
                                      mem[128] = sha3(call.data[0 len calldata.size], block.number)
                                      log Confirmation(
                                            address owner=caller,
                                            bytes32 operation=sha3(call.data[0 len calldata.size], block.number))
                                      if stor259[call.data[0 len calldata.size]][block.number].field_0 > 1:
                                          stor259[call.data[0 len calldata.size]][block.number].field_0--
                                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]][block.number].field_256
                                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                              [94ms = 0
                                              [94midx = _data + 36
                                              while _data + _data.length + 36 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                  [94ms = [94ms + 1
                                                  [94midx = [94midx + 32
                                                  continue 
                                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                  [94midx = [94midx + 1
                                                  continue 
                                              log ConfirmationNeeded(
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    address initiator=caller,
                                                    uint256 value=_value,
                                                    address to=addr(_to),
                                                    bytes data=Array(len=_data.length, data=_data[all]))
                                              return sha3(call.data[0 len calldata.size], block.number)
                                      else:
                                          require stor259[call.data[0 len calldata.size]][block.number].field_512 < stor260.length
                                          stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]][block.number].field_512] = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_0 = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_256 = 0
                                          stor259[call.data[0 len calldata.size]][block.number].field_512 = 0
                                          if not addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                              if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                              else:
                                                  stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                                                  stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                                                  stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                                                  [94ms = 0
                                                  [94midx = _data + 36
                                                  while _data + _data.length + 36 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                                      [94ms = [94ms + 1
                                                      [94midx = [94midx + 32
                                                      continue 
                                                  [94midx = Mask(251, 0, _data.length + 31) >> 5
                                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  log ConfirmationNeeded(
                                                        bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                        address initiator=caller,
                                                        uint256 value=_value,
                                                        address to=addr(_to),
                                                        bytes data=Array(len=_data.length, data=_data[all]))
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                          else:
                                              mem[96] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                              [94midx = 96
                                              [94ms = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 96 > [94midx + 32:
                                                  mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                                  [94midx = [94midx + 32
                                                  [94ms = [94ms + 1
                                                  continue 
                                              call addr(stor267[call.data[0 len calldata.size]][block.number].field_0).mem[96 len 4] with:
                                                 value stor267[call.data[0 len calldata.size]][block.number].field_256 wei
                                                   gas gas_remaining - 34050 wei
                                                  args mem[100 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32) - 4]
                                              mem[288] = stor267[call.data[0 len calldata.size]][block.number][2].field_0
                                              [94midx = 288
                                              [94ms = 0
                                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 288 > [94midx + 32:
                                                  mem[[94midx + 32] = stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_256
                                                  [94midx = [94midx + 32
                                                  [94ms = [94ms + 1
                                                  continue 
                                              log MultiTransact(
                                                    address owner=caller,
                                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                                    uint256 value=stor267[call.data[0 len calldata.size]][block.number].field_256,
                                                    address to=addr(stor267[call.data[0 len calldata.size]][block.number].field_0),
                                                    bytes data=Array(len=stor267[call.data[0 len calldata.size]][block.number][2].length, data=mem[288 len stor267[call.data[0 len calldata.size]][block.number][2].length + (floor32(stor267[call.data[0 len calldata.size]][block.number][2].length - 1) + -stor267[call.data[0 len calldata.size]][block.number][2].length + 32 % 32)]))
                                              addr(stor267[call.data[0 len calldata.size]][block.number].field_0) = 0
                                              stor267[call.data[0 len calldata.size]][block.number].field_256 = 0
                                              stor267[call.data[0 len calldata.size]][block.number].field_512 = 0
                                              if 31 < stor267[call.data[0 len calldata.size]][block.number][2].length:
                                                  [94midx = 0
                                                  while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                                      stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                                      [94midx = [94midx + 1
                                                      continue 
                                                  return sha3(call.data[0 len calldata.size], block.number)
                                              else:
                                                  return sha3(call.data[0 len calldata.size], block.number)
                      else:
                          if addr(stor267[call.data[0 len calldata.size]][block.number].field_0):
                              return sha3(call.data[0 len calldata.size], block.number)
                          else:
                              stor267[call.data[0 len calldata.size]][block.number].field_0 = _to or Mask(96, 160, stor267[call.data[0 len calldata.size]][block.number].field_0)
                              stor267[call.data[0 len calldata.size]][block.number].field_256 = _value
                              stor267[call.data[0 len calldata.size]][block.number].field_512 = (2 * _data.length) + 1
                              [94ms = 0
                              [94midx = _data + 36
                              while _data + _data.length + 36 > [94midx:
                                  stor267[call.data[0 len calldata.size]][block.number][[94ms + 2].field_0 = cd[[94midx]
                                  [94ms = [94ms + 1
                                  [94midx = [94midx + 32
                                  continue 
                              [94midx = Mask(251, 0, _data.length + 31) >> 5
                              while stor267[call.data[0 len calldata.size]][block.number][2].length + 31 / 32 > [94midx:
                                  stor267[call.data[0 len calldata.size]][block.number][[94midx + 2].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
                              log ConfirmationNeeded(
                                    bytes32 operation=sha3(call.data[0 len calldata.size], block.number),
                                    address initiator=caller,
                                    uint256 value=_value,
                                    address to=addr(_to),
                                    bytes data=Array(len=_data.length, data=_data[all]))
                              return sha3(call.data[0 len calldata.size], block.number)
                  else:
                      stor262 += _value
                      log SingleTransact(
                            address owner=caller,
                            uint256 value=_value,
                            address to=addr(_to),
                            bytes data=Array(len=_data.length, data=_data[all]))
                      call _to with:
                         value _value wei
                           gas gas_remaining - 34050 wei
                          args _data[all]
                      return 0


# hash = 0xb75c7dc6
# getter = None
# const = None
# payable = True
def revoke(bytes32 _digest) payable: 
  if stor258[caller] != 0:
      if 2^stor258[caller] and stor259[_digest].field_256 > 0:
          stor259[_digest].field_0++
          stor259[_digest].field_256 -= 2^stor258[caller]
          log Revoke(
                address owner=caller,
                bytes32 operation=_digest)


# hash = 0xba51a6df
# getter = None
# const = None
# payable = True
def changeRequirement(uint256 _required) payable: 
  if stor258[caller] != 0:
      if stor259[call.data[0 len calldata.size]].field_0:
          if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
              stop
          else:
              log Confirmation(
                    address owner=caller,
                    bytes32 operation=sha3(call.data[0 len calldata.size]))
              if stor259[call.data[0 len calldata.size]].field_0 > 1:
                  stor259[call.data[0 len calldata.size]].field_0--
                  stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                  stop
              else:
                  require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                  stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                  stor259[call.data[0 len calldata.size]].field_0 = 0
                  stor259[call.data[0 len calldata.size]].field_256 = 0
                  stor259[call.data[0 len calldata.size]].field_512 = 0
                  if _required <= m_numOwners:
                      m_required = _required
                      [94midx = 0
                      while [94midx < stor260.length:
                          mem[0] = stor[code.data[4948 len 32] + [94midx]
                          mem[32] = 267
                          addr(stor267[stor[code.data[4948 len 32] + [94midx]].field_0) = 0
                          stor267[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                          stor267[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                          if 31 < stor267[stor[code.data[4948 len 32] + [94midx]][2].length:
                              mem[0] = sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2
                              [94ms = sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2)
                              while sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2) + (stor267[stor[code.data[4948 len 32] + [94midx]][2].length + 31 / 32) > [94ms:
                                  stor[[94ms] = 0
                                  [94ms = [94ms + 1
                                  continue 
                              [94midx = [94midx + 1
                              continue 
                          else:
                              [94midx = [94midx + 1
                              continue 
                      [94midx = 0
                      while [94midx < stor260.length:
                          mem[0] = 260
                          if not stor[code.data[4948 len 32] + [94midx]:
                              [94midx = [94midx + 1
                              continue 
                          else:
                              require [94midx < stor260.length
                              mem[0] = stor[code.data[4948 len 32] + [94midx]
                              mem[32] = 259
                              stor259[stor[code.data[4948 len 32] + [94midx]].field_0 = 0
                              stor259[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                              stor259[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                              [94midx = [94midx + 1
                              continue 
                      stor260.length = 0
                      [94midx = code.data[4948 len 32]
                      while code.data[4948 len 32] + stor260.length > [94midx:
                          stor[[94midx] = 0
                          [94midx = [94midx + 1
                          continue 
                      log RequirementChanged(uint256 newRequirement=_required)
                      stop
                  else:
                      stop
      else:
          stor259[call.data[0 len calldata.size]].field_0 = m_required
          stor259[call.data[0 len calldata.size]].field_256 = 0
          stor260.length++
          if not stor260.length > stor260.length + 1:
              stor259[call.data[0 len calldata.size]].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size])
              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
                  stop
              else:
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=sha3(call.data[0 len calldata.size]))
                  if stor259[call.data[0 len calldata.size]].field_0 > 1:
                      stor259[call.data[0 len calldata.size]].field_0--
                      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                      stop
                  else:
                      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                      stor259[call.data[0 len calldata.size]].field_0 = 0
                      stor259[call.data[0 len calldata.size]].field_256 = 0
                      stor259[call.data[0 len calldata.size]].field_512 = 0
                      if _required <= m_numOwners:
                          m_required = _required
                          [94midx = 0
                          while [94midx < stor260.length:
                              mem[0] = stor[code.data[4948 len 32] + [94midx]
                              mem[32] = 267
                              addr(stor267[stor[code.data[4948 len 32] + [94midx]].field_0) = 0
                              stor267[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                              stor267[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                              if 31 < stor267[stor[code.data[4948 len 32] + [94midx]][2].length:
                                  mem[0] = sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2
                                  [94ms = sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2)
                                  while sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2) + (stor267[stor[code.data[4948 len 32] + [94midx]][2].length + 31 / 32) > [94ms:
                                      stor[[94ms] = 0
                                      [94ms = [94ms + 1
                                      continue 
                                  [94midx = [94midx + 1
                                  continue 
                              else:
                                  [94midx = [94midx + 1
                                  continue 
                          [94midx = 0
                          while [94midx < stor260.length:
                              mem[0] = 260
                              if not stor[code.data[4948 len 32] + [94midx]:
                                  [94midx = [94midx + 1
                                  continue 
                              else:
                                  require [94midx < stor260.length
                                  mem[0] = stor[code.data[4948 len 32] + [94midx]
                                  mem[32] = 259
                                  stor259[stor[code.data[4948 len 32] + [94midx]].field_0 = 0
                                  stor259[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                                  stor259[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                                  [94midx = [94midx + 1
                                  continue 
                          stor260.length = 0
                          [94midx = code.data[4948 len 32]
                          while code.data[4948 len 32] + stor260.length > [94midx:
                              stor[[94midx] = 0
                              [94midx = [94midx + 1
                              continue 
                          log RequirementChanged(uint256 newRequirement=_required)
                          stop
                      else:
                          stop
          else:
              [94midx = stor260.length + 1
              while stor260.length > [94midx:
                  stor260[[94midx] = 0
                  [94midx = [94midx + 1
                  continue 
              stor259[call.data[0 len calldata.size]].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size])
              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
                  stop
              else:
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=sha3(call.data[0 len calldata.size]))
                  if stor259[call.data[0 len calldata.size]].field_0 > 1:
                      stor259[call.data[0 len calldata.size]].field_0--
                      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                      stop
                  else:
                      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                      stor259[call.data[0 len calldata.size]].field_0 = 0
                      stor259[call.data[0 len calldata.size]].field_256 = 0
                      stor259[call.data[0 len calldata.size]].field_512 = 0
                      if _required <= m_numOwners:
                          m_required = _required
                          [94midx = 0
                          while [94midx < stor260.length:
                              mem[0] = stor[code.data[4948 len 32] + [94midx]
                              mem[32] = 267
                              addr(stor267[stor[code.data[4948 len 32] + [94midx]].field_0) = 0
                              stor267[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                              stor267[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                              if 31 < stor267[stor[code.data[4948 len 32] + [94midx]][2].length:
                                  mem[0] = sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2
                                  [94ms = sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2)
                                  while sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2) + (stor267[stor[code.data[4948 len 32] + [94midx]][2].length + 31 / 32) > [94ms:
                                      stor[[94ms] = 0
                                      [94ms = [94ms + 1
                                      continue 
                                  [94midx = [94midx + 1
                                  continue 
                              else:
                                  [94midx = [94midx + 1
                                  continue 
                          [94midx = 0
                          while [94midx < stor260.length:
                              mem[0] = 260
                              if not stor[code.data[4948 len 32] + [94midx]:
                                  [94midx = [94midx + 1
                                  continue 
                              else:
                                  require [94midx < stor260.length
                                  mem[0] = stor[code.data[4948 len 32] + [94midx]
                                  mem[32] = 259
                                  stor259[stor[code.data[4948 len 32] + [94midx]].field_0 = 0
                                  stor259[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                                  stor259[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                                  [94midx = [94midx + 1
                                  continue 
                          stor260.length = 0
                          [94midx = code.data[4948 len 32]
                          while code.data[4948 len 32] + stor260.length > [94midx:
                              stor[[94midx] = 0
                              [94midx = [94midx + 1
                              continue 
                          log RequirementChanged(uint256 newRequirement=_required)
                          stop
                      else:
                          stop
  else:
      stop


# hash = 0xc2cf7326
# getter = None
# const = None
# payable = True
def hasConfirmed(bytes32 _operation, address _owner) payable: 
  if stor258[addr(_owner)] != 0:
      return 2^stor258[addr(_owner)] and stor259[_operation].field_256 != 0
  else:
      return 0


# hash = 0xcadbb5af
# getter = None
# const = None
# payable = True
def unknowncadbb5af(uint256 _param1) payable: 
  unknown458e8a0a = _param1
  call unknowndd287692Address.splitDAO(uint256 proposalID, address newCurator) with:
       gas gas_remaining - 25050 wei
      args 98, 0x522b59b92a4566440ae3ef8e3426fbfaa2f37a9b
  require ext_call.success


# hash = 0xcbf0b0c0
# getter = None
# const = None
# payable = True
def kill(address _addr) payable: 
  if stor258[caller] != 0:
      if stor259[call.data[0 len calldata.size]].field_0:
          if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
              stop
          else:
              log Confirmation(
                    address owner=caller,
                    bytes32 operation=sha3(call.data[0 len calldata.size]))
              if stor259[call.data[0 len calldata.size]].field_0 > 1:
                  stor259[call.data[0 len calldata.size]].field_0--
                  stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                  stop
              else:
                  require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                  stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                  stor259[call.data[0 len calldata.size]].field_0 = 0
                  stor259[call.data[0 len calldata.size]].field_256 = 0
                  stor259[call.data[0 len calldata.size]].field_512 = 0
                  [93mselfdestruct([91m_addr[93m)
      else:
          stor259[call.data[0 len calldata.size]].field_0 = m_required
          stor259[call.data[0 len calldata.size]].field_256 = 0
          stor260.length++
          if not stor260.length > stor260.length + 1:
              stor259[call.data[0 len calldata.size]].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size])
              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
                  stop
              else:
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=sha3(call.data[0 len calldata.size]))
                  if stor259[call.data[0 len calldata.size]].field_0 > 1:
                      stor259[call.data[0 len calldata.size]].field_0--
                      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                      stop
                  else:
                      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                      stor259[call.data[0 len calldata.size]].field_0 = 0
                      stor259[call.data[0 len calldata.size]].field_256 = 0
                      stor259[call.data[0 len calldata.size]].field_512 = 0
                      [93mselfdestruct([91m_addr[93m)
          else:
              [94midx = stor260.length + 1
              while stor260.length > [94midx:
                  stor260[[94midx] = 0
                  [94midx = [94midx + 1
                  continue 
              stor259[call.data[0 len calldata.size]].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size])
              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
                  stop
              else:
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=sha3(call.data[0 len calldata.size]))
                  if stor259[call.data[0 len calldata.size]].field_0 > 1:
                      stor259[call.data[0 len calldata.size]].field_0--
                      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                      stop
                  else:
                      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                      stor259[call.data[0 len calldata.size]].field_0 = 0
                      stor259[call.data[0 len calldata.size]].field_256 = 0
                      stor259[call.data[0 len calldata.size]].field_512 = 0
                      [93mselfdestruct([91m_addr[93m)
  else:
      stop


# hash = 0xdd287692
# getter = ['storage', 160, 0, 264]
# const = None
# payable = True
def unknowndd287692() payable: 
  return unknowndd287692Address


# hash = 0xf00d4b5d
# getter = None
# const = None
# payable = True
def changeOwner(address _previousOwner, address _newOwner) payable: 
  if stor258[caller] != 0:
      if stor259[call.data[0 len calldata.size]].field_0:
          if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
              stop
          else:
              log Confirmation(
                    address owner=caller,
                    bytes32 operation=sha3(call.data[0 len calldata.size]))
              if stor259[call.data[0 len calldata.size]].field_0 > 1:
                  stor259[call.data[0 len calldata.size]].field_0--
                  stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                  stop
              else:
                  require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                  stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                  stor259[call.data[0 len calldata.size]].field_0 = 0
                  stor259[call.data[0 len calldata.size]].field_256 = 0
                  stor259[call.data[0 len calldata.size]].field_512 = 0
                  if stor258[addr(_newOwner)] <= 0:
                      if stor258[addr(_previousOwner)]:
                          [94midx = 0
                          while [94midx < stor260.length:
                              mem[0] = stor[code.data[4948 len 32] + [94midx]
                              mem[32] = 267
                              addr(stor267[stor[code.data[4948 len 32] + [94midx]].field_0) = 0
                              stor267[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                              stor267[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                              if 31 < stor267[stor[code.data[4948 len 32] + [94midx]][2].length:
                                  mem[0] = sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2
                                  [94ms = sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2)
                                  while sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2) + (stor267[stor[code.data[4948 len 32] + [94midx]][2].length + 31 / 32) > [94ms:
                                      stor[[94ms] = 0
                                      [94ms = [94ms + 1
                                      continue 
                                  [94midx = [94midx + 1
                                  continue 
                              else:
                                  [94midx = [94midx + 1
                                  continue 
                          [94midx = 0
                          while [94midx < stor260.length:
                              mem[0] = 260
                              if not stor[code.data[4948 len 32] + [94midx]:
                                  [94midx = [94midx + 1
                                  continue 
                              else:
                                  require [94midx < stor260.length
                                  mem[0] = stor[code.data[4948 len 32] + [94midx]
                                  mem[32] = 259
                                  stor259[stor[code.data[4948 len 32] + [94midx]].field_0 = 0
                                  stor259[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                                  stor259[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                                  [94midx = [94midx + 1
                                  continue 
                          stor260.length = 0
                          [94midx = code.data[4948 len 32]
                          while code.data[4948 len 32] + stor260.length > [94midx:
                              stor[[94midx] = 0
                              [94midx = [94midx + 1
                              continue 
                          require stor258[addr(_previousOwner)] < 256
                          addr(stor2[stor258[addr(_previousOwner)]].field_0) = _newOwner
                          Mask(96, 0, stor2[stor258[addr(_previousOwner)]].field_160) = 0
                          stor258[addr(_previousOwner)] = 0
                          stor258[_newOwner] = stor258[addr(_previousOwner)]
                          log OwnerChanged(
                                address oldOwner=addr(_previousOwner),
                                address newOwner=_newOwner)
                          stop
                      else:
                          stop
                  else:
                      stop
      else:
          stor259[call.data[0 len calldata.size]].field_0 = m_required
          stor259[call.data[0 len calldata.size]].field_256 = 0
          stor260.length++
          if not stor260.length > stor260.length + 1:
              stor259[call.data[0 len calldata.size]].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size])
              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
                  stop
              else:
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=sha3(call.data[0 len calldata.size]))
                  if stor259[call.data[0 len calldata.size]].field_0 > 1:
                      stor259[call.data[0 len calldata.size]].field_0--
                      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                      stop
                  else:
                      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                      stor259[call.data[0 len calldata.size]].field_0 = 0
                      stor259[call.data[0 len calldata.size]].field_256 = 0
                      stor259[call.data[0 len calldata.size]].field_512 = 0
                      if stor258[addr(_newOwner)] <= 0:
                          if stor258[addr(_previousOwner)]:
                              [94midx = 0
                              while [94midx < stor260.length:
                                  mem[0] = stor[code.data[4948 len 32] + [94midx]
                                  mem[32] = 267
                                  addr(stor267[stor[code.data[4948 len 32] + [94midx]].field_0) = 0
                                  stor267[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                                  stor267[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                                  if 31 < stor267[stor[code.data[4948 len 32] + [94midx]][2].length:
                                      mem[0] = sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2
                                      [94ms = sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2)
                                      while sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2) + (stor267[stor[code.data[4948 len 32] + [94midx]][2].length + 31 / 32) > [94ms:
                                          stor[[94ms] = 0
                                          [94ms = [94ms + 1
                                          continue 
                                      [94midx = [94midx + 1
                                      continue 
                                  else:
                                      [94midx = [94midx + 1
                                      continue 
                              [94midx = 0
                              while [94midx < stor260.length:
                                  mem[0] = 260
                                  if not stor[code.data[4948 len 32] + [94midx]:
                                      [94midx = [94midx + 1
                                      continue 
                                  else:
                                      require [94midx < stor260.length
                                      mem[0] = stor[code.data[4948 len 32] + [94midx]
                                      mem[32] = 259
                                      stor259[stor[code.data[4948 len 32] + [94midx]].field_0 = 0
                                      stor259[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                                      stor259[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                                      [94midx = [94midx + 1
                                      continue 
                              stor260.length = 0
                              [94midx = code.data[4948 len 32]
                              while code.data[4948 len 32] + stor260.length > [94midx:
                                  stor[[94midx] = 0
                                  [94midx = [94midx + 1
                                  continue 
                              require stor258[addr(_previousOwner)] < 256
                              addr(stor2[stor258[addr(_previousOwner)]].field_0) = _newOwner
                              Mask(96, 0, stor2[stor258[addr(_previousOwner)]].field_160) = 0
                              stor258[addr(_previousOwner)] = 0
                              stor258[_newOwner] = stor258[addr(_previousOwner)]
                              log OwnerChanged(
                                    address oldOwner=addr(_previousOwner),
                                    address newOwner=_newOwner)
                              stop
                          else:
                              stop
                      else:
                          stop
          else:
              [94midx = stor260.length + 1
              while stor260.length > [94midx:
                  stor260[[94midx] = 0
                  [94midx = [94midx + 1
                  continue 
              stor259[call.data[0 len calldata.size]].field_512 = stor260.length
              require stor260.length < stor260.length
              stor[code.data[4948 len 32] + stor260.length] = sha3(call.data[0 len calldata.size])
              if 2^stor258[caller] and stor259[call.data[0 len calldata.size]].field_256 != 0:
                  stop
              else:
                  log Confirmation(
                        address owner=caller,
                        bytes32 operation=sha3(call.data[0 len calldata.size]))
                  if stor259[call.data[0 len calldata.size]].field_0 > 1:
                      stor259[call.data[0 len calldata.size]].field_0--
                      stor259[call.data[0 len calldata.size]].field_256 = 2^stor258[caller] or stor259[call.data[0 len calldata.size]].field_256
                      stop
                  else:
                      require stor259[call.data[0 len calldata.size]].field_512 < stor260.length
                      stor[code.data[4948 len 32] + stor259[call.data[0 len calldata.size]].field_512] = 0
                      stor259[call.data[0 len calldata.size]].field_0 = 0
                      stor259[call.data[0 len calldata.size]].field_256 = 0
                      stor259[call.data[0 len calldata.size]].field_512 = 0
                      if stor258[addr(_newOwner)] <= 0:
                          if stor258[addr(_previousOwner)]:
                              [94midx = 0
                              while [94midx < stor260.length:
                                  mem[0] = stor[code.data[4948 len 32] + [94midx]
                                  mem[32] = 267
                                  addr(stor267[stor[code.data[4948 len 32] + [94midx]].field_0) = 0
                                  stor267[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                                  stor267[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                                  if 31 < stor267[stor[code.data[4948 len 32] + [94midx]][2].length:
                                      mem[0] = sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2
                                      [94ms = sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2)
                                      while sha3(sha3(stor[code.data[4948 len 32] + [94midx], 267) + 2) + (stor267[stor[code.data[4948 len 32] + [94midx]][2].length + 31 / 32) > [94ms:
                                          stor[[94ms] = 0
                                          [94ms = [94ms + 1
                                          continue 
                                      [94midx = [94midx + 1
                                      continue 
                                  else:
                                      [94midx = [94midx + 1
                                      continue 
                              [94midx = 0
                              while [94midx < stor260.length:
                                  mem[0] = 260
                                  if not stor[code.data[4948 len 32] + [94midx]:
                                      [94midx = [94midx + 1
                                      continue 
                                  else:
                                      require [94midx < stor260.length
                                      mem[0] = stor[code.data[4948 len 32] + [94midx]
                                      mem[32] = 259
                                      stor259[stor[code.data[4948 len 32] + [94midx]].field_0 = 0
                                      stor259[stor[code.data[4948 len 32] + [94midx]].field_256 = 0
                                      stor259[stor[code.data[4948 len 32] + [94midx]].field_512 = 0
                                      [94midx = [94midx + 1
                                      continue 
                              stor260.length = 0
                              [94midx = code.data[4948 len 32]
                              while code.data[4948 len 32] + stor260.length > [94midx:
                                  stor[[94midx] = 0
                                  [94midx = [94midx + 1
                                  continue 
                              require stor258[addr(_previousOwner)] < 256
                              addr(stor2[stor258[addr(_previousOwner)]].field_0) = _newOwner
                              Mask(96, 0, stor2[stor258[addr(_previousOwner)]].field_160) = 0
                              stor258[addr(_previousOwner)] = 0
                              stor258[_newOwner] = stor258[addr(_previousOwner)]
                              log OwnerChanged(
                                    address oldOwner=addr(_previousOwner),
                                    address newOwner=_newOwner)
                              stop
                          else:
                              stop
                      else:
                          stop
  else:
      stop


# hash = 0xf1736d86
# getter = ['storage', 256, 0, 261]
# const = None
# payable = True
def m_dailyLimit() payable: 
  return m_dailyLimit


# hash = 0xf3fef3a3
# getter = None
# const = None
# payable = True
def withdraw(address _address, uint256 _amount) payable: 
  require caller == 0x6b671106bf4de59243111c0fece9f43da91595f
  call unknowndd287692Address.transfer(address to, uint256 value) with:
       gas gas_remaining - 25050 wei
      args addr(_address), _amount
  require ext_call.success


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  if unknown458e8a0a <= 40:
      unknown458e8a0a++
      call unknowndd287692Address.getMyReward() with:
           gas gas_remaining - 25050 wei
      require ext_call.success
  else:
      unknown458e8a0a = 0
      call unknowndd287692Address.balanceOf(address owner) with:
           gas gas_remaining - 25050 wei
          args this.address
      require ext_call.success
      call unknowndd287692Address.transfer(address to, uint256 value) with:
           gas gas_remaining - 25050 wei
          args 0xabeebb597cd3fec57b6ebd6220beed584b423059, ext_call.return_data[0]


