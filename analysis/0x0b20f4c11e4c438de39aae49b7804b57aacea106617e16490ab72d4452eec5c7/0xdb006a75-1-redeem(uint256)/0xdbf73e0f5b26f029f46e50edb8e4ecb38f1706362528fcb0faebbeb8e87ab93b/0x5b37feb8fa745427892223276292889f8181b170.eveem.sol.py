# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x5B37fEB8fa745427892223276292889f8181b170 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x0e752702': 'unknown0e752702(?)', '0x17bfdfbc': 'unknown17bfdfbc(?)', '0x2608f818': 'unknown2608f818(?)', '0x3af9e669': 'unknown3af9e669(?)', '0x601a0bf1': 'unknown601a0bf1(?)', '0x852a12e3': 'unknown852a12e3(?)', '0xa0712d68': 'mint(uint256 _value)', '0xbd6d894d': 'unknownbd6d894d(?)', '0xc5ebeaec': 'unknownc5ebeaec(?)', '0xdb006a75': 'redeem(uint256 _amount)', '0xf2b3abbd': 'unknownf2b3abbd(?)', '0xf5e3c462': 'unknownf5e3c462(?)', '0xfca7820b': 'unknownfca7820b(?)'} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    name
    # storage address 2
    symbol
    # storage address 3
    decimals # mask: a s
    # storage address 4
    adminAddress # mask: a s
    # storage address 5
    pendingAdminAddress # mask: a s
    # storage address 6
    comptrollerAddress # mask: a s
    # storage address 7
    unknownf3fdb15aAddress # mask: a s
    # storage address 8
    unknown675d972c # mask: a s
    # storage address 9
    unknown173b9904 # mask: a s
    # storage address 10
    unknown6c540baf # mask: a s
    # storage address 11
    unknownaa5af0fd # mask: a s
    # storage address 12
    unknown47bd3718 # mask: a s
    # storage address 13
    unknown8f840ddd # mask: a s
    # storage address 14
    totalSupply # mask: a s
    # storage address 15
    balanceOf
    # storage address 16
    allowance
    # storage address 17
    stor17
    # storage address 18
    underlyingAddress # mask: a s
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 1]]]], ['loc', 1]]]
# const = None
# payable = True
def name() payable: 
  return name[0 len name.length]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = True
def approve(address _spender, uint256 _tokens) payable: 
  require calldata.size - 4 >= 64
  allowance[caller][addr(_spender)] = _tokens
  log Approval(
        address owner=_tokens,
        address spender=caller,
        uint256 value=_spender)
  return 1


# hash = 0x09839b52
# getter = None
# const = ['return', 1]
# payable = True
const unknown09839b52 = 1


# hash = 0x173b9904
# getter = ['storage', 256, 0, 9]
# const = None
# payable = True
def unknown173b9904() payable: 
  return unknown173b9904


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 14]
# const = None
# payable = True
def totalSupply() payable: 
  return totalSupply


# hash = 0x182df0f5
# getter = None
# const = None
# payable = True
def unknown182df0f5() payable: 
  if 0 == totalSupply:
      return unknown675d972c
  require ext_code.size(underlyingAddress)
  static call underlyingAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if unknown47bd3718 + ext_call.return_data[0] < ext_call.return_data[0]:
      revert with 0, 
                  32,
                  53,
                  0x6465786368616e67655261746553746f7265643a2065786368616e67655261746553746f726564496e7465726e616c206661696c65,
                  mem[249 len 11]
  if unknown8f840ddd > unknown47bd3718 + ext_call.return_data[0]:
      revert with 0, 
                  32,
                  53,
                  0x6465786368616e67655261746553746f7265643a2065786368616e67655261746553746f726564496e7465726e616c206661696c65,
                  mem[249 len 11]
  if not unknown47bd3718 + ext_call.return_data[0] - unknown8f840ddd:
      if not totalSupply:
          revert with 0, 
                      32,
                      53,
                      0x6465786368616e67655261746553746f7265643a2065786368616e67655261746553746f726564496e7465726e616c206661696c65,
                      mem[313 len 11]
      return (0 / totalSupply)
  if (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / unknown47bd3718 + ext_call.return_data[0] - unknown8f840ddd != 10^18:
      revert with 0, 
                  32,
                  53,
                  0x6465786368616e67655261746553746f7265643a2065786368616e67655261746553746f726564496e7465726e616c206661696c65,
                  mem[313 len 11]
  if not totalSupply:
      revert with 0, 
                  32,
                  53,
                  0x6465786368616e67655261746553746f7265643a2065786368616e67655261746553746f726564496e7465726e616c206661696c65,
                  mem[313 len 11]
  return ((10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply)


# hash = 0x23b872dd
# getter = None
# const = None
# payable = True
def transferFrom(address _from, address _to, uint256 _tokens) payable: 
  require calldata.size - 4 >= 96
  stor0++
  require ext_code.size(comptrollerAddress)
  call comptrollerAddress.0xbdcdc258 with:
       gas gas_remaining wei
      args 0, uint32(this.address), addr(_from), addr(_to), _tokens
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      log Failure(
            uint256 error=3,
            uint256 info=74,
            uint256 detail=ext_call.return_data[0])
      if stor0 + 1 != stor0:
          revert with 0, 're-entered'
      else:
          return 0
  if _from == _to:
      log Failure(
            uint256 error=2,
            uint256 info=75,
            uint256 detail=0)
      if stor0 + 1 != stor0:
          revert with 0, 're-entered'
      else:
          return 0
  if _from == caller:
      if _tokens > -1:
          log Failure(
                uint256 error=9,
                uint256 info=75,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      if _tokens > balanceOf[addr(_from)]:
          log Failure(
                uint256 error=9,
                uint256 info=76,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      if _tokens + balanceOf[addr(_to)] < balanceOf[addr(_to)]:
          log Failure(
                uint256 error=9,
                uint256 info=77,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      balanceOf[addr(_from)] -= _tokens
      balanceOf[_to] = _tokens + balanceOf[addr(_to)]
  else:
      if _tokens > allowance[addr(_from)][caller]:
          log Failure(
                uint256 error=9,
                uint256 info=75,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      if _tokens > balanceOf[addr(_from)]:
          log Failure(
                uint256 error=9,
                uint256 info=76,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      if _tokens + balanceOf[addr(_to)] < balanceOf[addr(_to)]:
          log Failure(
                uint256 error=9,
                uint256 info=77,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      balanceOf[addr(_from)] -= _tokens
      balanceOf[_to] = _tokens + balanceOf[addr(_to)]
      if allowance[addr(_from)][caller] != -1:
          allowance[addr(_from)][caller] -= _tokens
  log 0x64ddf252: _tokens, _from, _to
  require ext_code.size(comptrollerAddress)
  call comptrollerAddress.0x6a56947e with:
       gas gas_remaining wei
      args 0, uint32(this.address), addr(_from), addr(_to), _tokens
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if stor0 + 1 != stor0:
      revert with 0, 're-entered'
  return 1


# hash = 0x26782247
# getter = ['storage', 160, 0, 5]
# const = None
# payable = True
def pendingAdmin() payable: 
  return pendingAdminAddress


# hash = 0x313ce567
# getter = ['storage', 256, 0, 3]
# const = None
# payable = True
def decimals() payable: 
  return decimals


# hash = 0x3b1d21a2
# getter = None
# const = None
# payable = True
def unknown3b1d21a2() payable: 
  require ext_code.size(underlyingAddress)
  static call underlyingAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x4576b5db
# getter = None
# const = None
# payable = True
def unknown4576b5db(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if adminAddress != caller:
      log Failure(
            uint256 error=1,
            uint256 info=63,
            uint256 detail=0)
      return 1
  require ext_code.size(_param1)
  static call _param1.0x7e3dd2 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'marker method returned false'
  comptrollerAddress = _param1
  log 0x7ac369db: comptrollerAddress, _param1
  return 0


# hash = 0x47bd3718
# getter = ['storage', 256, 0, 12]
# const = None
# payable = True
def unknown47bd3718() payable: 
  return unknown47bd3718


# hash = 0x5fe3b567
# getter = ['storage', 160, 0, 6]
# const = None
# payable = True
def comptroller() payable: 
  return comptrollerAddress


# hash = 0x675d972c
# getter = ['storage', 256, 0, 8]
# const = None
# payable = True
def unknown675d972c() payable: 
  return unknown675d972c


# hash = 0x6c540baf
# getter = ['storage', 256, 0, 10]
# const = None
# payable = True
def unknown6c540baf() payable: 
  return unknown6c540baf


# hash = 0x6f307dc3
# getter = ['storage', 160, 0, 18]
# const = None
# payable = True
def underlying() payable: 
  return underlyingAddress


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 15]]]
# const = None
# payable = True
def balanceOf(address _tokenOwner) payable: 
  require calldata.size - 4 >= 32
  return balanceOf[addr(_tokenOwner)]


# hash = 0x73acee98
# getter = None
# const = None
# payable = True
def unknown73acee98() payable: 
  stor0++
  require ext_code.size(underlyingAddress)
  static call underlyingAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknownf3fdb15aAddress)
  static call unknownf3fdb15aAddress.0x15f24053 with:
          gas gas_remaining wei
         args ext_call.return_data[0], unknown47bd3718, unknown8f840ddd
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if 5 * 10^14 < ext_call.return_data[32]:
      revert with 0, 'borrow rate is absurdly high'
  if ext_call.return_data[0]:
      log Failure(
            uint256 error=5,
            uint256 info=2,
            uint256 detail=ext_call.return_data[0])
      revert with 0, 'accrue interest failed'
  require unknown6c540baf <= block.number
  if not ext_call.return_data[32]:
      if unknown47bd3718 < 0:
          log Failure(
                uint256 error=9,
                uint256 info=4,
                uint256 detail=2)
          revert with 0, 'accrue interest failed'
      if not unknown173b9904:
          if unknown8f840ddd + (0 / 10^18) < 0 / 10^18:
              log Failure(
                    uint256 error=9,
                    uint256 info=5,
                    uint256 detail=2)
              revert with 0, 'accrue interest failed'
          if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
              log Failure(
                    uint256 error=9,
                    uint256 info=3,
                    uint256 detail=2)
              revert with 0, 'accrue interest failed'
          unknown6c540baf = block.number
      else:
          if 0 / unknown173b9904:
              log Failure(
                    uint256 error=9,
                    uint256 info=5,
                    uint256 detail=2)
              revert with 0, 'accrue interest failed'
          if unknown8f840ddd + (0 / 10^18) < 0 / 10^18:
              log Failure(
                    uint256 error=9,
                    uint256 info=5,
                    uint256 detail=2)
              revert with 0, 'accrue interest failed'
          if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
              log Failure(
                    uint256 error=9,
                    uint256 info=3,
                    uint256 detail=2)
              revert with 0, 'accrue interest failed'
          unknown6c540baf = block.number
          unknown8f840ddd += 0 / 10^18
      log 0x4dec04e7: 0, unknownaa5af0fd, unknown47bd3718, unknown8f840ddd
  else:
      if (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) / ext_call.return_data[32] != block.number - unknown6c540baf:
          log Failure(
                uint256 error=9,
                uint256 info=6,
                uint256 detail=2)
          revert with 0, 'accrue interest failed'
      if not (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]):
          if unknown47bd3718 < 0:
              log Failure(
                    uint256 error=9,
                    uint256 info=4,
                    uint256 detail=2)
              revert with 0, 'accrue interest failed'
          if not unknown173b9904:
              if unknown8f840ddd + (0 / 10^18) < 0 / 10^18:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  revert with 0, 'accrue interest failed'
              if not (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]):
                  if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  unknown6c540baf = block.number
                  log 0x4dec04e7: 0, unknownaa5af0fd, unknown47bd3718, unknown8f840ddd
              else:
                  if (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) != unknownaa5af0fd:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  if unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18) < (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  unknown6c540baf = block.number
                  unknownaa5af0fd += (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18
                  log 0x4dec04e7: 0, unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18), unknown47bd3718, unknown8f840ddd
          else:
              if 0 / unknown173b9904:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  revert with 0, 'accrue interest failed'
              if unknown8f840ddd + (0 / 10^18) < 0 / 10^18:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  revert with 0, 'accrue interest failed'
              if not (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]):
                  if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  unknown6c540baf = block.number
                  unknown8f840ddd += 0 / 10^18
                  log 0x4dec04e7: 0, unknownaa5af0fd, unknown47bd3718, unknown8f840ddd
              else:
                  if (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) != unknownaa5af0fd:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  if unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18) < (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  unknown6c540baf = block.number
                  unknownaa5af0fd += (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18
                  unknown8f840ddd += 0 / 10^18
                  log 0x4dec04e7: 0, unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18), unknown47bd3718, unknown8f840ddd
      else:
          if (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) != unknown47bd3718:
              log Failure(
                    uint256 error=9,
                    uint256 info=1,
                    uint256 detail=2)
              revert with 0, 'accrue interest failed'
          if unknown47bd3718 + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18) < (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18:
              log Failure(
                    uint256 error=9,
                    uint256 info=4,
                    uint256 detail=2)
              revert with 0, 'accrue interest failed'
          if not unknown173b9904:
              if unknown8f840ddd + (0 / 10^18) < 0 / 10^18:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  revert with 0, 'accrue interest failed'
              if not (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]):
                  if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  unknown6c540baf = block.number
                  unknown47bd3718 += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18
                  log 0x4dec04e7: (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18, unknownaa5af0fd, unknown47bd3718 + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18), unknown8f840ddd
              else:
                  if (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) != unknownaa5af0fd:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  if unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18) < (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  unknown6c540baf = block.number
                  unknownaa5af0fd += (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18
                  unknown47bd3718 += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18
                  log 0x4dec04e7: (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18, unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18), unknown47bd3718 + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18), unknown8f840ddd
          else:
              if (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / unknown173b9904 != (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  revert with 0, 'accrue interest failed'
              if unknown8f840ddd + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18) < (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  revert with 0, 'accrue interest failed'
              if not (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]):
                  if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  unknown6c540baf = block.number
                  unknown47bd3718 += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18
                  unknown8f840ddd += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18
                  log 0x4dec04e7: (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18, unknownaa5af0fd, unknown47bd3718 + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18), unknown8f840ddd + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18)
              else:
                  if (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) != unknownaa5af0fd:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  if unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18) < (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      revert with 0, 'accrue interest failed'
                  unknown6c540baf = block.number
                  unknownaa5af0fd += (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18
                  unknown47bd3718 += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18
                  unknown8f840ddd += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18
                  log 0x4dec04e7: (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18, unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18), unknown47bd3718 + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18), unknown8f840ddd + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18)
  if stor0 + 1 != stor0:
      revert with 0, 're-entered'
  return unknown47bd3718


# hash = 0x8f840ddd
# getter = ['storage', 256, 0, 13]
# const = None
# payable = True
def unknown8f840ddd() payable: 
  return unknown8f840ddd


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 2]]]], ['loc', 2]]]
# const = None
# payable = True
def symbol() payable: 
  return symbol[0 len symbol.length]


# hash = 0x95dd9193
# getter = None
# const = None
# payable = True
def unknown95dd9193(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if not stor17[addr(_param1)].field_0:
      return 0
  if unknownaa5af0fd * stor17[addr(_param1)].field_0 / stor17[addr(_param1)].field_0 != unknownaa5af0fd:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  55,
                  0x64626f72726f7742616c616e636553746f7265643a20626f72726f7742616c616e636553746f726564496e7465726e616c206661696c65,
                  mem[219 len 9]
  if not stor17[addr(_param1)].field_256:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  55,
                  0x64626f72726f7742616c616e636553746f7265643a20626f72726f7742616c616e636553746f726564496e7465726e616c206661696c65,
                  mem[219 len 9]
  return (unknownaa5af0fd * stor17[addr(_param1)].field_0 / stor17[addr(_param1)].field_256)


# hash = 0xa6afed95
# getter = None
# const = None
# payable = True
def unknowna6afed95() payable: 
  require ext_code.size(underlyingAddress)
  static call underlyingAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknownf3fdb15aAddress)
  static call unknownf3fdb15aAddress.0x15f24053 with:
          gas gas_remaining wei
         args ext_call.return_data[0], unknown47bd3718, unknown8f840ddd
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if 5 * 10^14 < ext_call.return_data[32]:
      revert with 0, 'borrow rate is absurdly high'
  if ext_call.return_data[0]:
      log Failure(
            uint256 error=5,
            uint256 info=2,
            uint256 detail=ext_call.return_data[0])
      return 5
  require unknown6c540baf <= block.number
  if not ext_call.return_data[32]:
      if unknown47bd3718 < 0:
          log Failure(
                uint256 error=9,
                uint256 info=4,
                uint256 detail=2)
          return 9
      if not unknown173b9904:
          if unknown8f840ddd + (0 / 10^18) < 0 / 10^18:
              log Failure(
                    uint256 error=9,
                    uint256 info=5,
                    uint256 detail=2)
              return 9
          if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
              log Failure(
                    uint256 error=9,
                    uint256 info=3,
                    uint256 detail=2)
              return 9
          unknown6c540baf = block.number
      else:
          if 0 / unknown173b9904:
              log Failure(
                    uint256 error=9,
                    uint256 info=5,
                    uint256 detail=2)
              return 9
          if unknown8f840ddd + (0 / 10^18) < 0 / 10^18:
              log Failure(
                    uint256 error=9,
                    uint256 info=5,
                    uint256 detail=2)
              return 9
          if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
              log Failure(
                    uint256 error=9,
                    uint256 info=3,
                    uint256 detail=2)
              return 9
          unknown6c540baf = block.number
          unknown8f840ddd += 0 / 10^18
      log 0x4dec04e7: 0, unknownaa5af0fd, unknown47bd3718, unknown8f840ddd
  else:
      if (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) / ext_call.return_data[32] != block.number - unknown6c540baf:
          log Failure(
                uint256 error=9,
                uint256 info=6,
                uint256 detail=2)
          return 9
      if not (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]):
          if unknown47bd3718 < 0:
              log Failure(
                    uint256 error=9,
                    uint256 info=4,
                    uint256 detail=2)
              return 9
          if not unknown173b9904:
              if unknown8f840ddd + (0 / 10^18) < 0 / 10^18:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  return 9
              if not (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]):
                  if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  unknown6c540baf = block.number
                  log 0x4dec04e7: 0, unknownaa5af0fd, unknown47bd3718, unknown8f840ddd
              else:
                  if (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) != unknownaa5af0fd:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  if unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18) < (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  unknown6c540baf = block.number
                  unknownaa5af0fd += (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18
                  log 0x4dec04e7: 0, unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18), unknown47bd3718, unknown8f840ddd
          else:
              if 0 / unknown173b9904:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  return 9
              if unknown8f840ddd + (0 / 10^18) < 0 / 10^18:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  return 9
              if not (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]):
                  if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  unknown6c540baf = block.number
                  unknown8f840ddd += 0 / 10^18
                  log 0x4dec04e7: 0, unknownaa5af0fd, unknown47bd3718, unknown8f840ddd
              else:
                  if (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) != unknownaa5af0fd:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  if unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18) < (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  unknown6c540baf = block.number
                  unknownaa5af0fd += (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18
                  unknown8f840ddd += 0 / 10^18
                  log 0x4dec04e7: 0, unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18), unknown47bd3718, unknown8f840ddd
      else:
          if (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) != unknown47bd3718:
              log Failure(
                    uint256 error=9,
                    uint256 info=1,
                    uint256 detail=2)
              return 9
          if unknown47bd3718 + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18) < (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18:
              log Failure(
                    uint256 error=9,
                    uint256 info=4,
                    uint256 detail=2)
              return 9
          if not unknown173b9904:
              if unknown8f840ddd + (0 / 10^18) < 0 / 10^18:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  return 9
              if not (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]):
                  if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  unknown6c540baf = block.number
                  unknown47bd3718 += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18
                  log 0x4dec04e7: (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18, unknownaa5af0fd, unknown47bd3718 + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18), unknown8f840ddd
              else:
                  if (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) != unknownaa5af0fd:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  if unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18) < (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  unknown6c540baf = block.number
                  unknownaa5af0fd += (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18
                  unknown47bd3718 += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18
                  log 0x4dec04e7: (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18, unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18), unknown47bd3718 + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18), unknown8f840ddd
          else:
              if (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / unknown173b9904 != (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  return 9
              if unknown8f840ddd + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18) < (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18:
                  log Failure(
                        uint256 error=9,
                        uint256 info=5,
                        uint256 detail=2)
                  return 9
              if not (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]):
                  if unknownaa5af0fd + (0 / 10^18) < 0 / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  unknown6c540baf = block.number
                  unknown47bd3718 += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18
                  unknown8f840ddd += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18
                  log 0x4dec04e7: (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18, unknownaa5af0fd, unknown47bd3718 + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18), unknown8f840ddd + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18)
              else:
                  if (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / (block.number * ext_call.return_data[32]) - (unknown6c540baf * ext_call.return_data[32]) != unknownaa5af0fd:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  if unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18) < (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18:
                      log Failure(
                            uint256 error=9,
                            uint256 info=3,
                            uint256 detail=2)
                      return 9
                  unknown6c540baf = block.number
                  unknownaa5af0fd += (block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18
                  unknown47bd3718 += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18
                  unknown8f840ddd += (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18
                  log 0x4dec04e7: (block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18, unknownaa5af0fd + ((block.number * ext_call.return_data[32] * unknownaa5af0fd) - (unknown6c540baf * ext_call.return_data[32] * unknownaa5af0fd) / 10^18), unknown47bd3718 + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18), unknown8f840ddd + ((block.number * ext_call.return_data[32] * unknown47bd3718) - (unknown6c540baf * ext_call.return_data[32] * unknown47bd3718) / 10^18 * unknown173b9904 / 10^18)
  return 0


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = True
def transfer(address _to, uint256 _tokens) payable: 
  require calldata.size - 4 >= 64
  stor0++
  require ext_code.size(comptrollerAddress)
  call comptrollerAddress.0xbdcdc258 with:
       gas gas_remaining wei
      args 0, uint32(this.address), caller, addr(_to), _tokens
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      log Failure(
            uint256 error=3,
            uint256 info=74,
            uint256 detail=ext_call.return_data[0])
      if stor0 + 1 != stor0:
          revert with 0, 're-entered'
      else:
          return 0
  if caller == _to:
      log Failure(
            uint256 error=2,
            uint256 info=75,
            uint256 detail=0)
      if stor0 + 1 != stor0:
          revert with 0, 're-entered'
      else:
          return 0
  if caller == caller:
      if _tokens > -1:
          log Failure(
                uint256 error=9,
                uint256 info=75,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      if _tokens > balanceOf[caller]:
          log Failure(
                uint256 error=9,
                uint256 info=76,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      if _tokens + balanceOf[addr(_to)] < balanceOf[addr(_to)]:
          log Failure(
                uint256 error=9,
                uint256 info=77,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      balanceOf[caller] -= _tokens
      balanceOf[_to] = _tokens + balanceOf[addr(_to)]
  else:
      if _tokens > allowance[caller][caller]:
          log Failure(
                uint256 error=9,
                uint256 info=75,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      if _tokens > balanceOf[caller]:
          log Failure(
                uint256 error=9,
                uint256 info=76,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      if _tokens + balanceOf[addr(_to)] < balanceOf[addr(_to)]:
          log Failure(
                uint256 error=9,
                uint256 info=77,
                uint256 detail=0)
          if stor0 + 1 != stor0:
              revert with 0, 're-entered'
          else:
              return 0
      balanceOf[caller] -= _tokens
      balanceOf[_to] = _tokens + balanceOf[addr(_to)]
      if allowance[caller][caller] != -1:
          allowance[caller][caller] -= _tokens
  log 0x64ddf252: _tokens, caller, _to
  require ext_code.size(comptrollerAddress)
  call comptrollerAddress.0x6a56947e with:
       gas gas_remaining wei
      args 0, uint32(this.address), caller, addr(_to), _tokens
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if stor0 + 1 != stor0:
      revert with 0, 're-entered'
  return 1


# hash = 0xaa5af0fd
# getter = ['storage', 256, 0, 11]
# const = None
# payable = True
def unknownaa5af0fd() payable: 
  return unknownaa5af0fd


# hash = 0xae9d70b0
# getter = None
# const = None
# payable = True
def unknownae9d70b0() payable: 
  if totalSupply != 0:
      require ext_code.size(underlyingAddress)
      static call underlyingAddress.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          if unknown47bd3718 + ext_call.return_data[0] < ext_call.return_data[0]:
              revert with 0, 
                          32,
                          53,
                          0x6465786368616e67655261746553746f7265643a2065786368616e67655261746553746f726564496e7465726e616c206661696c65,
                          mem[249 len 11]
          else:
              if unknown8f840ddd > unknown47bd3718 + ext_call.return_data[0]:
                  revert with 0, 
                              32,
                              53,
                              0x6465786368616e67655261746553746f7265643a2065786368616e67655261746553746f726564496e7465726e616c206661696c65,
                              mem[249 len 11]
              else:
                  if unknown47bd3718 + ext_call.return_data[0] - unknown8f840ddd:
                      if (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / unknown47bd3718 + ext_call.return_data[0] - unknown8f840ddd != 10^18:
                          revert with 0, 
                                      32,
                                      53,
                                      0x6465786368616e67655261746553746f7265643a2065786368616e67655261746553746f726564496e7465726e616c206661696c65,
                                      mem[313 len 11]
                      else:
                          if not totalSupply:
                              revert with 0, 
                                          32,
                                          53,
                                          0x6465786368616e67655261746553746f7265643a2065786368616e67655261746553746f726564496e7465726e616c206661696c65,
                                          mem[313 len 11]
                          else:
                              require ext_code.size(underlyingAddress)
                              static call underlyingAddress.balanceOf(address owner) with:
                                      gas gas_remaining wei
                                     args this.address
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 32
                                  require ext_code.size(unknownf3fdb15aAddress)
                                  static call unknownf3fdb15aAddress.0x15f24053 with:
                                          gas gas_remaining wei
                                         args ext_call.return_data[0], unknown47bd3718, unknown8f840ddd
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  else:
                                      require return_data.size >= 64
                                      if ext_call.return_data[0]:
                                          revert with 0, 
                                                      32,
                                                      49,
                                                      0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7752617465206661696c65,
                                                      mem[309 len 15]
                                      else:
                                          if (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply:
                                              if totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply / (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply != totalSupply:
                                                  revert with 0, 
                                                              32,
                                                              49,
                                                              0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720756e6465726c79696e67206661696c65,
                                                              mem[437 len 15]
                                              else:
                                                  if 10^18 * unknown47bd3718 / 10^18 != unknown47bd3718:
                                                      revert with 0, 
                                                                  32,
                                                                  49,
                                                                  0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                  mem[533 len 15]
                                                  else:
                                                      if 10^18 * unknown47bd3718:
                                                          if 1000000000000000000 * 10^18 * unknown47bd3718 / 10^18 * unknown47bd3718 != 10^18:
                                                              revert with 0, 
                                                                          32,
                                                                          49,
                                                                          0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                          mem[565 len 15]
                                                          else:
                                                              if not totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply:
                                                                  revert with 0, 
                                                                              32,
                                                                              49,
                                                                              0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                              mem[565 len 15]
                                                              else:
                                                                  if unknown173b9904 > 10^18:
                                                                      revert with 0, 
                                                                                  32,
                                                                                  60,
                                                                                  0xef737570706c7952617465506572426c6f636b3a2063616c63756c6174696e67206f6e654d696e757352657365727665466163746f72206661696c65,
                                                                                  mem[736 len 4]
                                                                  else:
                                                                      if ext_call.return_data[32]:
                                                                          if (10^18 * ext_call.return_data[32]) - (unknown173b9904 * ext_call.return_data[32]) / ext_call.return_data[32] != -unknown173b9904 + 10^18:
                                                                              revert with 0, 
                                                                                          32,
                                                                                          49,
                                                                                          0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                          mem[917 len 15]
                                                                          else:
                                                                              if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 < 5 * 10^17:
                                                                                  revert with 0, 
                                                                                              32,
                                                                                              49,
                                                                                              0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                              mem[917 len 15]
                                                                              else:
                                                                                  if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18:
                                                                                      if 1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 / (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 != 1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply:
                                                                                          revert with 0, 
                                                                                                      32,
                                                                                                      49,
                                                                                                      0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                                      mem[981 len 15]
                                                                                      else:
                                                                                          if (1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                                                                                              revert with 0, 
                                                                                                          32,
                                                                                                          49,
                                                                                                          0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                                          mem[981 len 15]
                                                                                          else:
                                                                                              return ((1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18)
                                                                                  else:
                                                                                      return 0
                                                                      else:
                                                                          return 0
                                                      else:
                                                          if not totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply:
                                                              revert with 0, 
                                                                          32,
                                                                          49,
                                                                          0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                          mem[565 len 15]
                                                          else:
                                                              if unknown173b9904 > 10^18:
                                                                  revert with 0, 
                                                                              32,
                                                                              60,
                                                                              0xef737570706c7952617465506572426c6f636b3a2063616c63756c6174696e67206f6e654d696e757352657365727665466163746f72206661696c65,
                                                                              mem[736 len 4]
                                                              else:
                                                                  if ext_call.return_data[32]:
                                                                      if (10^18 * ext_call.return_data[32]) - (unknown173b9904 * ext_call.return_data[32]) / ext_call.return_data[32] != -unknown173b9904 + 10^18:
                                                                          revert with 0, 
                                                                                      32,
                                                                                      49,
                                                                                      0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                      mem[917 len 15]
                                                                      else:
                                                                          if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 < 5 * 10^17:
                                                                              revert with 0, 
                                                                                          32,
                                                                                          49,
                                                                                          0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                          mem[917 len 15]
                                                                          else:
                                                                              if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18:
                                                                                  if 0 / totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 / (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 != 0 / totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply:
                                                                                      revert with 0, 
                                                                                                  32,
                                                                                                  49,
                                                                                                  0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                                  mem[981 len 15]
                                                                                  else:
                                                                                      if (0 / totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                                                                                          revert with 0, 
                                                                                                      32,
                                                                                                      49,
                                                                                                      0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                                      mem[981 len 15]
                                                                                      else:
                                                                                          return ((0 / totalSupply * (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18)
                                                                              else:
                                                                                  return 0
                                                                  else:
                                                                      return 0
                                          else:
                                              if 10^18 * unknown47bd3718 / 10^18 != unknown47bd3718:
                                                  revert with 0, 
                                                              32,
                                                              49,
                                                              0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                              mem[533 len 15]
                                              else:
                                                  if not 10^18 * unknown47bd3718:
                                                      revert with 0, 
                                                                  32,
                                                                  49,
                                                                  0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                  mem[565 len 15]
                                                  else:
                                                      if 1000000000000000000 * 10^18 * unknown47bd3718 / 10^18 * unknown47bd3718 != 10^18:
                                                          revert with 0, 
                                                                      32,
                                                                      49,
                                                                      0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                      mem[565 len 15]
                                                      else:
                                                          revert with 0, 
                                                                      32,
                                                                      49,
                                                                      0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                      mem[565 len 15]
                  else:
                      if not totalSupply:
                          revert with 0, 
                                      32,
                                      53,
                                      0x6465786368616e67655261746553746f7265643a2065786368616e67655261746553746f726564496e7465726e616c206661696c65,
                                      mem[313 len 11]
                      else:
                          require ext_code.size(underlyingAddress)
                          static call underlyingAddress.balanceOf(address owner) with:
                                  gas gas_remaining wei
                                 args this.address
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          else:
                              require return_data.size >= 32
                              require ext_code.size(unknownf3fdb15aAddress)
                              static call unknownf3fdb15aAddress.0x15f24053 with:
                                      gas gas_remaining wei
                                     args ext_call.return_data[0], unknown47bd3718, unknown8f840ddd
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              else:
                                  require return_data.size >= 64
                                  if ext_call.return_data[0]:
                                      revert with 0, 
                                                  32,
                                                  49,
                                                  0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7752617465206661696c65,
                                                  mem[309 len 15]
                                  else:
                                      if 0 / totalSupply:
                                          if totalSupply * 0 / totalSupply / 0 / totalSupply != totalSupply:
                                              revert with 0, 
                                                          32,
                                                          49,
                                                          0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720756e6465726c79696e67206661696c65,
                                                          mem[437 len 15]
                                          else:
                                              if 10^18 * unknown47bd3718 / 10^18 != unknown47bd3718:
                                                  revert with 0, 
                                                              32,
                                                              49,
                                                              0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                              mem[533 len 15]
                                              else:
                                                  if 10^18 * unknown47bd3718:
                                                      if 1000000000000000000 * 10^18 * unknown47bd3718 / 10^18 * unknown47bd3718 != 10^18:
                                                          revert with 0, 
                                                                      32,
                                                                      49,
                                                                      0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                      mem[565 len 15]
                                                      else:
                                                          if not totalSupply * 0 / totalSupply:
                                                              revert with 0, 
                                                                          32,
                                                                          49,
                                                                          0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                          mem[565 len 15]
                                                          else:
                                                              if unknown173b9904 > 10^18:
                                                                  revert with 0, 
                                                                              32,
                                                                              60,
                                                                              0xef737570706c7952617465506572426c6f636b3a2063616c63756c6174696e67206f6e654d696e757352657365727665466163746f72206661696c65,
                                                                              mem[736 len 4]
                                                              else:
                                                                  if ext_call.return_data[32]:
                                                                      if (10^18 * ext_call.return_data[32]) - (unknown173b9904 * ext_call.return_data[32]) / ext_call.return_data[32] != -unknown173b9904 + 10^18:
                                                                          revert with 0, 
                                                                                      32,
                                                                                      49,
                                                                                      0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                      mem[917 len 15]
                                                                      else:
                                                                          if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 < 5 * 10^17:
                                                                              revert with 0, 
                                                                                          32,
                                                                                          49,
                                                                                          0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                          mem[917 len 15]
                                                                          else:
                                                                              if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18:
                                                                                  if 1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * 0 / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 / (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 != 1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * 0 / totalSupply:
                                                                                      revert with 0, 
                                                                                                  32,
                                                                                                  49,
                                                                                                  0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                                  mem[981 len 15]
                                                                                  else:
                                                                                      if (1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * 0 / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                                                                                          revert with 0, 
                                                                                                      32,
                                                                                                      49,
                                                                                                      0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                                      mem[981 len 15]
                                                                                      else:
                                                                                          return ((1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * 0 / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18)
                                                                              else:
                                                                                  return 0
                                                                  else:
                                                                      return 0
                                                  else:
                                                      if not totalSupply * 0 / totalSupply:
                                                          revert with 0, 
                                                                      32,
                                                                      49,
                                                                      0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                      mem[565 len 15]
                                                      else:
                                                          if unknown173b9904 > 10^18:
                                                              revert with 0, 
                                                                          32,
                                                                          60,
                                                                          0xef737570706c7952617465506572426c6f636b3a2063616c63756c6174696e67206f6e654d696e757352657365727665466163746f72206661696c65,
                                                                          mem[736 len 4]
                                                          else:
                                                              if ext_call.return_data[32]:
                                                                  if (10^18 * ext_call.return_data[32]) - (unknown173b9904 * ext_call.return_data[32]) / ext_call.return_data[32] != -unknown173b9904 + 10^18:
                                                                      revert with 0, 
                                                                                  32,
                                                                                  49,
                                                                                  0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                  mem[917 len 15]
                                                                  else:
                                                                      if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 < 5 * 10^17:
                                                                          revert with 0, 
                                                                                      32,
                                                                                      49,
                                                                                      0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                      mem[917 len 15]
                                                                      else:
                                                                          if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18:
                                                                              if 0 / totalSupply * 0 / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 / (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 != 0 / totalSupply * 0 / totalSupply:
                                                                                  revert with 0, 
                                                                                              32,
                                                                                              49,
                                                                                              0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                              mem[981 len 15]
                                                                              else:
                                                                                  if (0 / totalSupply * 0 / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                                                                                      revert with 0, 
                                                                                                  32,
                                                                                                  49,
                                                                                                  0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                                  mem[981 len 15]
                                                                                  else:
                                                                                      return ((0 / totalSupply * 0 / totalSupply * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18)
                                                                          else:
                                                                              return 0
                                                              else:
                                                                  return 0
                                      else:
                                          if 10^18 * unknown47bd3718 / 10^18 != unknown47bd3718:
                                              revert with 0, 
                                                          32,
                                                          49,
                                                          0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                          mem[533 len 15]
                                          else:
                                              if not 10^18 * unknown47bd3718:
                                                  revert with 0, 
                                                              32,
                                                              49,
                                                              0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                              mem[565 len 15]
                                              else:
                                                  if 1000000000000000000 * 10^18 * unknown47bd3718 / 10^18 * unknown47bd3718 != 10^18:
                                                      revert with 0, 
                                                                  32,
                                                                  49,
                                                                  0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                  mem[565 len 15]
                                                  else:
                                                      revert with 0, 
                                                                  32,
                                                                  49,
                                                                  0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                                  mem[565 len 15]
  else:
      require ext_code.size(underlyingAddress)
      static call underlyingAddress.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          require return_data.size >= 32
          require ext_code.size(unknownf3fdb15aAddress)
          static call unknownf3fdb15aAddress.0x15f24053 with:
                  gas gas_remaining wei
                 args ext_call.return_data[0], unknown47bd3718, unknown8f840ddd
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              require return_data.size >= 64
              if ext_call.return_data[0]:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                              32,
                              49,
                              0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7752617465206661696c65,
                              mem[213 len 15]
              else:
                  if unknown675d972c:
                      if totalSupply * unknown675d972c / unknown675d972c != totalSupply:
                          revert with 0, 
                                      32,
                                      49,
                                      0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720756e6465726c79696e67206661696c65,
                                      mem[341 len 15]
                      else:
                          if 10^18 * unknown47bd3718 / 10^18 != unknown47bd3718:
                              revert with 0, 
                                          32,
                                          49,
                                          0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                          mem[437 len 15]
                          else:
                              if 10^18 * unknown47bd3718:
                                  if 1000000000000000000 * 10^18 * unknown47bd3718 / 10^18 * unknown47bd3718 != 10^18:
                                      revert with 0, 
                                                  32,
                                                  49,
                                                  0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                  mem[469 len 15]
                                  else:
                                      if not totalSupply * unknown675d972c:
                                          revert with 0, 
                                                      32,
                                                      49,
                                                      0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                      mem[469 len 15]
                                      else:
                                          if unknown173b9904 > 10^18:
                                              revert with 0, 
                                                          32,
                                                          60,
                                                          0xef737570706c7952617465506572426c6f636b3a2063616c63756c6174696e67206f6e654d696e757352657365727665466163746f72206661696c65,
                                                          mem[640 len 4]
                                          else:
                                              if ext_call.return_data[32]:
                                                  if (10^18 * ext_call.return_data[32]) - (unknown173b9904 * ext_call.return_data[32]) / ext_call.return_data[32] != -unknown173b9904 + 10^18:
                                                      revert with 0, 
                                                                  32,
                                                                  49,
                                                                  0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                  mem[821 len 15]
                                                  else:
                                                      if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 < 5 * 10^17:
                                                          revert with 0, 
                                                                      32,
                                                                      49,
                                                                      0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                      mem[821 len 15]
                                                      else:
                                                          if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18:
                                                              if 1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * unknown675d972c * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 / (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 != 1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * unknown675d972c:
                                                                  revert with 0, 
                                                                              32,
                                                                              49,
                                                                              0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                              mem[885 len 15]
                                                              else:
                                                                  if (1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * unknown675d972c * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                                                                      revert with 0, 
                                                                                  32,
                                                                                  49,
                                                                                  0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                                  mem[885 len 15]
                                                                  else:
                                                                      return ((1000000000000000000 * 10^18 * unknown47bd3718 / totalSupply * unknown675d972c * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18)
                                                          else:
                                                              return 0
                                              else:
                                                  return 0
                              else:
                                  if not totalSupply * unknown675d972c:
                                      revert with 0, 
                                                  32,
                                                  49,
                                                  0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                                  mem[469 len 15]
                                  else:
                                      if unknown173b9904 > 10^18:
                                          revert with 0, 
                                                      32,
                                                      60,
                                                      0xef737570706c7952617465506572426c6f636b3a2063616c63756c6174696e67206f6e654d696e757352657365727665466163746f72206661696c65,
                                                      mem[640 len 4]
                                      else:
                                          if ext_call.return_data[32]:
                                              if (10^18 * ext_call.return_data[32]) - (unknown173b9904 * ext_call.return_data[32]) / ext_call.return_data[32] != -unknown173b9904 + 10^18:
                                                  revert with 0, 
                                                              32,
                                                              49,
                                                              0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                              mem[821 len 15]
                                              else:
                                                  if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 < 5 * 10^17:
                                                      revert with 0, 
                                                                  32,
                                                                  49,
                                                                  0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                  mem[821 len 15]
                                                  else:
                                                      if (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18:
                                                          if 0 / totalSupply * unknown675d972c * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 / (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18 != 0 / totalSupply * unknown675d972c:
                                                              revert with 0, 
                                                                          32,
                                                                          49,
                                                                          0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                          mem[885 len 15]
                                                          else:
                                                              if (0 / totalSupply * unknown675d972c * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 < 5 * 10^17:
                                                                  revert with 0, 
                                                                              32,
                                                                              49,
                                                                              0x64737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720737570706c7952617465206661696c65,
                                                                              mem[885 len 15]
                                                              else:
                                                                  return ((0 / totalSupply * unknown675d972c * (10^18 * ext_call.return_data[32]) + (-1 * unknown173b9904 * ext_call.return_data[32]) + 5 * 10^17 / 10^18) + 5 * 10^17 / 10^18)
                                                      else:
                                                          return 0
                                          else:
                                              return 0
                  else:
                      if 10^18 * unknown47bd3718 / 10^18 != unknown47bd3718:
                          revert with 0, 
                                      32,
                                      49,
                                      0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                      mem[437 len 15]
                      else:
                          if not 10^18 * unknown47bd3718:
                              revert with 0, 
                                          32,
                                          49,
                                          0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                          mem[469 len 15]
                          else:
                              if 1000000000000000000 * 10^18 * unknown47bd3718 / 10^18 * unknown47bd3718 != 10^18:
                                  revert with 0, 
                                              32,
                                              49,
                                              0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                              mem[469 len 15]
                              else:
                                  revert with 0, 
                                              32,
                                              49,
                                              0xfe737570706c7952617465506572426c6f636b3a2063616c63756c6174696e6720626f72726f7773506572206661696c65,
                                              mem[469 len 15]


# hash = 0xb2a02ff1
# getter = None
# const = None
# payable = True
def unknownb2a02ff1(addr _param1, addr _param2, uint256 _param3) payable: 
  require calldata.size - 4 >= 96
  stor0++
  require ext_code.size(comptrollerAddress)
  call comptrollerAddress.0xd02f7351 with:
       gas gas_remaining wei
      args 0, uint32(this.address), caller, addr(_param1), _param2, _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      log Failure(
            uint256 error=3,
            uint256 info=27,
            uint256 detail=ext_call.return_data[0])
      if stor0 + 1 != stor0:
          revert with 0, 're-entered'
      return 3
  if _param2 == _param1:
      log Failure(
            uint256 error=6,
            uint256 info=28,
            uint256 detail=0)
      if stor0 + 1 != stor0:
          revert with 0, 're-entered'
      return 6
  if _param3 > balanceOf[addr(_param2)]:
      log Failure(
            uint256 error=9,
            uint256 info=26,
            uint256 detail=3)
      if stor0 + 1 != stor0:
          revert with 0, 're-entered'
      return 9
  if _param3 + balanceOf[addr(_param1)] < balanceOf[addr(_param1)]:
      log Failure(
            uint256 error=9,
            uint256 info=25,
            uint256 detail=2)
      if stor0 + 1 != stor0:
          revert with 0, 're-entered'
      return 9
  balanceOf[addr(_param2)] -= _param3
  balanceOf[_param1] = _param3 + balanceOf[addr(_param1)]
  log 0x64ddf252: _param3, _param2, _param1
  require ext_code.size(comptrollerAddress)
  call comptrollerAddress.0x6d35bf91 with:
       gas gas_remaining wei
      args 0, uint32(this.address), caller, addr(_param1), _param2, _param3
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if stor0 + 1 != stor0:
      revert with 0, 're-entered'
  else:
      return 0


# hash = 0xb71d1a0c
# getter = None
# const = None
# payable = True
def _setPendingAdmin(address _newPendingAdmin) payable: 
  require calldata.size - 4 >= 32
  if adminAddress != caller:
      log Failure(
            uint256 error=1,
            uint256 info=69,
            uint256 detail=0)
      return 1
  pendingAdminAddress = _newPendingAdmin
  log NewPendingAdmin(
        address oldPendingAdmin=pendingAdminAddress,
        address newPendingAdmin=_newPendingAdmin)
  return 0


# hash = 0xc37f68e2
# getter = None
# const = None
# payable = True
def unknownc37f68e2(addr _param1) payable: 
  require calldata.size - 4 >= 32
  if not stor17[addr(_param1)].field_0:
      if 0 == totalSupply:
          return 0, balanceOf[addr(_param1)], 0, unknown675d972c
      require ext_code.size(underlyingAddress)
      static call underlyingAddress.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if unknown47bd3718 + ext_call.return_data[0] >= ext_call.return_data[0]:
          if unknown8f840ddd <= unknown47bd3718 + ext_call.return_data[0]:
              if not unknown47bd3718 + ext_call.return_data[0] - unknown8f840ddd:
                  if totalSupply:
                      return 0, balanceOf[addr(_param1)], 0, 0 / totalSupply
              else:
                  if (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / unknown47bd3718 + ext_call.return_data[0] - unknown8f840ddd == 10^18:
                      if totalSupply:
                          return 0, 
                                 balanceOf[addr(_param1)],
                                 0,
                                 (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply
  else:
      if unknownaa5af0fd * stor17[addr(_param1)].field_0 / stor17[addr(_param1)].field_0 == unknownaa5af0fd:
          if stor17[addr(_param1)].field_256:
              if 0 == totalSupply:
                  return 0, 
                         balanceOf[addr(_param1)],
                         unknownaa5af0fd * stor17[addr(_param1)].field_0 / stor17[addr(_param1)].field_256,
                         unknown675d972c
              require ext_code.size(underlyingAddress)
              static call underlyingAddress.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if unknown47bd3718 + ext_call.return_data[0] >= ext_call.return_data[0]:
                  if unknown8f840ddd <= unknown47bd3718 + ext_call.return_data[0]:
                      if not unknown47bd3718 + ext_call.return_data[0] - unknown8f840ddd:
                          if totalSupply:
                              return 0, 
                                     balanceOf[addr(_param1)],
                                     unknownaa5af0fd * stor17[addr(_param1)].field_0 / stor17[addr(_param1)].field_256,
                                     0 / totalSupply
                      else:
                          if (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / unknown47bd3718 + ext_call.return_data[0] - unknown8f840ddd == 10^18:
                              if totalSupply:
                                  return 0, 
                                         balanceOf[addr(_param1)],
                                         unknownaa5af0fd * stor17[addr(_param1)].field_0 / stor17[addr(_param1)].field_256,
                                         (10^18 * unknown47bd3718) + (10^18 * ext_call.return_data[0]) - (10^18 * unknown8f840ddd) / totalSupply
  return 9, 0, 0, 0


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 16]]]]]
# const = None
# payable = True
def allowance(address _tokenOwner, address _spender) payable: 
  require calldata.size - 4 >= 64
  return allowance[addr(_tokenOwner)][addr(_spender)]


# hash = 0xe9c714f2
# getter = None
# const = None
# payable = True
def _acceptAdmin() payable: 
  if pendingAdminAddress != caller:
      log Failure(
            uint256 error=1,
            uint256 info=0,
            uint256 detail=0)
      return 1
  if not caller:
      log Failure(
            uint256 error=1,
            uint256 info=0,
            uint256 detail=0)
      return 1
  adminAddress = pendingAdminAddress
  pendingAdminAddress = 0
  log NewAdmin(
        address oldAdmin=adminAddress,
        address newAdmin=pendingAdminAddress)
  log NewPendingAdmin(
        address oldPendingAdmin=pendingAdminAddress,
        address newPendingAdmin=pendingAdminAddress)
  return 0


# hash = 0xf3fdb15a
# getter = ['storage', 160, 0, 7]
# const = None
# payable = True
def unknownf3fdb15a() payable: 
  return unknownf3fdb15aAddress


# hash = 0xf851a440
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def admin() payable: 
  return adminAddress


# hash = 0xf8f9da28
# getter = None
# const = None
# payable = True
def unknownf8f9da28() payable: 
  require ext_code.size(underlyingAddress)
  static call underlyingAddress.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(unknownf3fdb15aAddress)
  static call unknownf3fdb15aAddress.0x15f24053 with:
          gas gas_remaining wei
         args ext_call.return_data[0], unknown47bd3718, unknown8f840ddd
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if ext_call.return_data[0]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  55,
                  0x64626f72726f7752617465506572426c6f636b3a20696e746572657374526174654d6f64656c2e626f72726f7752617465206661696c65,
                  mem[219 len 9]
  return ext_call.return_data[32]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


