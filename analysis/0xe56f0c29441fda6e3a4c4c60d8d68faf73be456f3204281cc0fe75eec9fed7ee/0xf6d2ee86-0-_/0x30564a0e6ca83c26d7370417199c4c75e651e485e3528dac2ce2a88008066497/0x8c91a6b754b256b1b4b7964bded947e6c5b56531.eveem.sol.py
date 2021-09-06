# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x8C91A6b754B256b1B4B7964BdEd947E6C5b56531 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 2
    allowance
    # storage address 3
    totalSupply # mask: a s
    # storage address 4
    name
    # storage address 5
    symbol
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    decimals # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    owner # mask: a s
    # storage address 8
    stor8
    # storage address 9
    stor9
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = True
def name() payable: 
  return mnamem[0 len mnamem.lengthm]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = True
def approve(address m_spender, uint256 m_value) payable: 
  require calldata.size - 4 >= 64
  require m_spender
  require caller
  mallowancem[callerm]m[addr(m_spender)m] = m_value
  log Approval(
        address owner=caller,
        address spender=addr(_spender),
        uint256 value=_value)
  return 1


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 3]
# const = None
# payable = True
def totalSupply() payable: 
  return mtotalSupply


# hash = 0x23b872dd
# getter = None
# const = None
# payable = True
def transferFrom(address m_from, address m_to, uint256 m_value) payable: 
  require calldata.size - 4 >= 96
  if addr(mstor6m.field_16) != caller:
      log Transfer(
            address from=addr(_from),
            address to=addr(_to),
            uint256 value=_value)
      require ext_code.size(addr(mstor6m.field_16))
      call addr(mstor6m.field_16).transfer(address token, address from, address to, uint256 amount) with:
           gas gas_remaining wei
          args 0, 0, addr(m_to), addr(this.address), m_value
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
  else:
      if uint8(mstor6m.field_8):
          log Transfer(
                address from=addr(_from),
                address to=addr(_to),
                uint256 value=_value)
          require ext_code.size(addr(mstor6m.field_16))
          call addr(mstor6m.field_16).transfer(address token, address from, address to, uint256 amount) with:
               gas gas_remaining wei
              args 0, 0, addr(m_to), addr(this.address), m_value
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
  require m_value <= mallowancem[addr(m_from)m]m[callerm]
  require caller
  require m_from
  mallowancem[addr(m_from)m]m[callerm] -= m_value
  log Approval(
        address owner=addr(_from),
        address spender=caller,
        uint256 value=allowance[addr(_from)][caller] - _value)
  return 1


# hash = 0x313ce567
# getter = ['storage', 8, 0, 6]
# const = None
# payable = True
def decimals() payable: 
  return mdecimals


# hash = 0x39509351
# getter = None
# const = None
# payable = True
def increaseAllowance(address m_spender, uint256 m_addedValue) payable: 
  require calldata.size - 4 >= 64
  require mallowancem[callerm]m[addr(m_spender)m] + m_addedValue >= mallowancem[callerm]m[addr(m_spender)m]
  require m_spender
  require caller
  mallowancem[callerm]m[addr(m_spender)m] += m_addedValue
  log Approval(
        address owner=caller,
        address spender=addr(_spender),
        uint256 value=allowance[caller][addr(_spender)] + _addedValue)
  return 1


# hash = 0x40a141ff
# getter = None
# const = None
# payable = True
def removeValidator(address m_validator) payable: 
  require calldata.size - 4 >= 32
  require caller == mowner
  mstor8m[addr(m_validator)m] = 0
  return 1


# hash = 0x47f1f960
# getter = None
# const = None
# payable = True
def unknown47f1f960(uint256 m_param1, addr m_param2, uint256 m_param3, uint256 m_param4, addr m_param5, addr m_param6, addr m_param7, uint256 m_param8, uint8 m_param9, uint256 m_param10, uint256 m_param11, uint8 m_param12, uint256 m_param13, uint256 m_param14) payable: 
  require calldata.size - 4 >= 448
  require not mstor0
  mstor0 = 1
  require 9 >= m_param9
  require m_param9 <= 9
  require m_param9 <= 9
  if m_param9 == 4:
      revert with 0, 'Settlement operation is invalid'
  require m_param9 <= 9
  if m_param9 == 5:
      revert with 0, 'Settlement operation is invalid'
  if m_param5 != caller:
      revert with 0, 'Source of funds is not sender'
  if not m_param2:
      revert with 0, 'Address is invalid'
  if m_param2 == this.address:
      revert with 0, 'Address is referencing self'
  if block.timestamp >= m_param3:
      revert with 0, 'RFQ after expiration date'
  if block.number >= m_param4:
      revert with 0, 'RFQ after expiration block'
  if not m_param5:
      revert with 0, 'Address is invalid'
  if m_param5 == this.address:
      revert with 0, 'Address is referencing self'
  if not m_param6:
      revert with 0, 'Address is invalid'
  if m_param6 == this.address:
      revert with 0, 'Address is referencing self'
  if not m_param7:
      revert with 0, 'Address is invalid'
  if m_param7 == this.address:
      revert with 0, 'Address is referencing self'
  if m_param8 <= 0:
      revert with 0, 32, 36, 0xfe5175616e74697479206973206e6f742067726561746572207468616e206d696e696d75, mem[552 len 28]
  if m_param10 <= 0:
      revert with 0, 32, 36, 0xfe5175616e74697479206973206e6f742067726561746572207468616e206d696e696d75, mem[552 len 28]
  mem[928 len 0] = None
  if mstor9m[mem[928 len 3]m][0x68657265756d205369676e6564204d6573m][m_param1m][addr(m_param2)m][m_param3m][m_param4m][addr(m_param5)m][addr(m_param6)m][addr(m_param7)m][m_param8m][m_param9 << 248m][m_param10m][m_param11m]:
      revert with 0, 'Attempted transaction replay'
  mstor9m[mem[928 len 3]m][0x68657265756d205369676e6564204d6573m][m_param1m][addr(m_param2)m][m_param3m][m_param4m][addr(m_param5)m][addr(m_param6)m][addr(m_param7)m][m_param8m][m_param9 << 248m][m_param10m][m_param11m] = 1
  [94msigner = erecover(sha3(mem[928 len 3], 0x68657265756d205369676e6564204d6573, m_param1, addr(m_param2), m_param3, m_param4, addr(m_param5), addr(m_param6), addr(m_param7), m_param8, m_param9 << 248, m_param10, m_param11), m_param12 << 248, m_param13, m_param14) # precompiled
  if not erecover.result:
      revert with ext_call.return_data[0 len return_data.size]
  if bool(mstor8m[addr([94msigner)m]) != 1:
      revert with 0, 'Validator signature is invalid'
  require m_param11 <= m_param10
  require uint64(m_param5)
  require m_param10 - m_param11 <= mtotalSupply
  mtotalSupply = mtotalSupply - m_param10 + m_param11
  log Transfer(
        address from=_param5 << 192,
        address to=0,
        uint256 value=_param10 - _param11)
  require ext_code.size(addr(mstor6m.field_16))
  call addr(mstor6m.field_16).transfer(address token, address from, address to, uint256 amount) with:
       gas gas_remaining wei
      args addr(m_param5), addr(this.address), addr(this.address), m_param10 - m_param11
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  require ext_code.size(addr(mstor6m.field_16))
  if uint8(0 % 3):
      call addr(mstor6m.field_16).transfer(address token, address from, address to, uint256 amount) with:
           gas gas_remaining wei
          args addr(this.address), addr(m_param6), addr(m_param7), m_param8
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          revert with 0, 'vault transfer failed'
  else:
      call addr(mstor6m.field_16).withdraw(address owner, address token, uint256 tokens) with:
           gas gas_remaining wei
          args m_param6 << 192, addr(m_param7), m_param8
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
  ('bool', ('ext_call.return_data', 0, 32))
  if m_param11 > 0:
      if addr(mstor6m.field_16) != caller:
          log Transfer(
                address from=_param5 << 192,
                address to=_param2 << 192,
                uint256 value=_param11)
          require ext_code.size(addr(mstor6m.field_16))
          call addr(mstor6m.field_16).transfer(address token, address from, address to, uint256 amount) with:
               gas gas_remaining wei
              args addr(m_param5), addr(m_param2), addr(this.address), m_param11
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
      else:
          if uint8(mstor6m.field_8):
              log Transfer(
                    address from=_param5 << 192,
                    address to=_param2 << 192,
                    uint256 value=_param11)
              require ext_code.size(addr(mstor6m.field_16))
              call addr(mstor6m.field_16).transfer(address token, address from, address to, uint256 amount) with:
                   gas gas_remaining wei
                  args addr(m_param5), addr(m_param2), addr(this.address), m_param11
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
  log 0xcf3de7b9: _param2 << 192, _param8, _param9 << 248, _param10, _param11, _param5, uint64(_param6) << 96, uint64(_param7) << 96
  mstor0 = 0
  return 1


# hash = 0x4d238c8e
# getter = None
# const = None
# payable = True
def addValidator(address m_validator) payable: 
  require calldata.size - 4 >= 32
  require caller == mowner
  mstor8m[addr(m_validator)m] = 1
  return 1


# hash = 0x70a08231
# getter = None
# const = None
# payable = True
def balanceOf(address m_owner) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(addr(mstor6m.field_16))
  static call addr(mstor6m.field_16).0x5d973e47 with:
          gas gas_remaining wei
         args addr(m_owner), this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return ext_call.return_data[0]


# hash = 0x715018a6
# getter = None
# const = None
# payable = True
def renounceOwnership() payable: 
  require caller == mowner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  mowner = 0


# hash = 0x829dd895
# getter = None
# const = ['return', 200]
# payable = True
const unknown829dd895 = 200


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 7]
# const = None
# payable = True
def owner() payable: 
  return mowner


# hash = 0x8f32d59b
# getter = None
# const = None
# payable = True
def isOwner() payable: 
  return (caller == mowner)


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 5]]]], ['loc', 5]]]
# const = None
# payable = True
def symbol() payable: 
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0xa457c2d7
# getter = None
# const = None
# payable = True
def decreaseAllowance(address m_spender, uint256 m_subtractedValue) payable: 
  require calldata.size - 4 >= 64
  require m_subtractedValue <= mallowancem[callerm]m[addr(m_spender)m]
  require m_spender
  require caller
  mallowancem[callerm]m[addr(m_spender)m] -= m_subtractedValue
  log Approval(
        address owner=caller,
        address spender=addr(_spender),
        uint256 value=allowance[caller][addr(_spender)] - _subtractedValue)
  return 1


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = True
def transfer(address m_to, uint256 m_value) payable: 
  require calldata.size - 4 >= 64
  if addr(mstor6m.field_16) != caller:
      log Transfer(
            address from=caller,
            address to=addr(_to),
            uint256 value=_value)
      require ext_code.size(addr(mstor6m.field_16))
      call addr(mstor6m.field_16).transfer(address token, address from, address to, uint256 amount) with:
           gas gas_remaining wei
          args 0, uint32(caller), addr(m_to), addr(this.address), m_value
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_call.return_data[0]
  else:
      if uint8(mstor6m.field_8):
          log Transfer(
                address from=caller,
                address to=addr(_to),
                uint256 value=_value)
          require ext_code.size(addr(mstor6m.field_16))
          call addr(mstor6m.field_16).transfer(address token, address from, address to, uint256 amount) with:
               gas gas_remaining wei
              args 0, uint32(caller), addr(m_to), addr(this.address), m_value
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
  return 1


# hash = 0xdd62ed3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 2]]]]]
# const = None
# payable = True
def allowance(address m_owner, address m_spender) payable: 
  require calldata.size - 4 >= 64
  return mallowancem[addr(m_owner)m]m[addr(m_spender)m]


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address m_newOwner) payable: 
  require calldata.size - 4 >= 32
  require caller == mowner
  require m_newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = 0xf6d2ee86
# getter = None
# const = None
# payable = True
def unknownf6d2ee86(addr m_param1, array m_param2, array m_param3, uint8 m_param4) payable: 
  require calldata.size - 4 >= 128
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + m_param2.length + 36 <= calldata.size
  require m_param3 <= 4294967296
  require m_param3 + 36 <= calldata.size
  require m_param3.length <= 4294967296 and m_param3 + m_param3.length + 36 <= calldata.size
  require not uint8(mstor6m.field_8)
  require not mstor0
  mstor0 = 1
  addr(mstor6m.field_16) = m_param1
  mnamem[m] = Array(len=m_param2.length, data=m_param2[allm])
  msymbolm[m] = Array(len=m_param3.length, data=m_param3[allm])
  mdecimals = m_param4
  require addr(mstor6m.field_16)
  require this.address
  mallowancem[addr(this.address)m]m[addr(mstor6m.field_0)m] = -1
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 160] = this.address
  mem[ceil32(m_param2.length) + ceil32(m_param3.length) + 192] = addr(mstor6m.field_16)
  log Approval(
        address owner=Mask(8 * -ceil32(_param3.length) + _param3.length + 32, 0, 0),
        address spender=mem[ceil32(_param2.length) + _param3.length + 192 len ceil32(_param3.length) + -_param3.length + 32],
        uint256 value=-1)
  require ext_code.size(addr(mstor6m.field_16))
  call addr(mstor6m.field_16).deposit(address darknode, address token, uint256 value) with:
       gas gas_remaining wei
      args addr(this.address), addr(this.address), -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'Initialzation deposit failed'
  require ext_code.size(addr(mstor6m.field_16))
  call addr(mstor6m.field_16).0xb5f5e722 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'Opt in balance management failed'
  Mask(248, 0, mstor6m.field_8) = 1
  require ext_code.size(addr(mstor6m.field_16))
  static call addr(mstor6m.field_16).0x5d973e47 with:
          gas gas_remaining wei
         args addr(this.address), this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] == -1
  mstor0 = 0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


