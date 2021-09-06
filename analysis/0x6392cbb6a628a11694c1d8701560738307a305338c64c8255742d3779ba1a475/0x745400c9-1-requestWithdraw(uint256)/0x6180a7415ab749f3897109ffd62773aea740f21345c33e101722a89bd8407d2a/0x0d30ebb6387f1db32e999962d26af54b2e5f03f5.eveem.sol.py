# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x0D30EbB6387F1db32E999962d26aF54b2e5f03f5 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknownc4efc91a # mask: a s
    # storage address 1
    unknown40a73f89 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    supportedTokens
# hash = 0x16ff5798
# getter = None
# const = None
# payable = False
def unknown16ff5798(uint256 m_param1): # not payable
  require m_param1 >= 0
  require m_param1 <= 100
  munknownc4efc91a = m_param1


# hash = 0x40a73f89
# getter = ['bool', ['storage', 8, 0, 1]]
# const = None
# payable = False
def unknown40a73f89(): # not payable
  return bool(munknown40a73f89)


# hash = 0x809a9e55
# getter = None
# const = None
# payable = False
def getExpectedRate(address m_srcToken, address m_destToken, uint256 m_srcTokenValue): # not payable
  if munknown40a73f89:
      return 0
  if mstor3 == m_destToken:
      return 10^15, 10^15
  if mstor3 != m_srcToken:
      if mstor3 != m_destToken:
          [94midx = 0
          mwhile [94midx < msupportedTokensm.lengthm:
              mem[0] = 4
              if msupportedTokensm[[94midxm]m.field_0 != m_destToken:
                  [94midx = [94midx + 1
                  mcontinue 
              return 10^18, 10^18
  else:
      [94midx = 0
      mwhile [94midx < msupportedTokensm.lengthm:
          mem[0] = 4
          if msupportedTokensm[[94midxm]m.field_0 != m_destToken:
              [94midx = [94midx + 1
              mcontinue 
          require [94midx < msupportedTokensm.length
          return msupportedTokensm[[94midxm]m.field_256, msupportedTokensm[[94midxm]m.field_256
      if mstor3 != m_srcToken:
          if mstor3 != m_destToken:
              [94midx = 0
              mwhile [94midx < msupportedTokensm.lengthm:
                  mem[0] = 4
                  if msupportedTokensm[[94midxm]m.field_0 != m_destToken:
                      [94midx = [94midx + 1
                      mcontinue 
                  return 10^18, 10^18
  return 1000 * 10^18, 1000 * 10^18


# hash = 0x9c79c122
# getter = None
# const = None
# payable = False
def unknown9c79c122(bool m_param1): # not payable
  munknown40a73f89 = uint8(m_param1)
  return 1


# hash = 0xb002249d
# getter = None
# const = None
# payable = False
def unknownb002249d(): # not payable
  if msupportedTokensm.length:
      mem[128 len 32 * msupportedTokensm.length] = code.data[2669 len 32 * msupportedTokensm.length]
  [94midx = 0
  mwhile [94midx < msupportedTokensm.lengthm:
      mem[0] = 4
      require [94midx < msupportedTokensm.length
      mem[(32 * [94midx) + 128] = msupportedTokensm[[94midxm]m.field_0
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * msupportedTokensm.length) + 192 len floor32(msupportedTokensm.length)] = mem[128 len floor32(msupportedTokensm.length)]
  return Array(len=msupportedTokensm.length, data=mem[128 len floor32(msupportedTokensm.length)], mem[(32 * msupportedTokensm.length) + floor32(msupportedTokensm.length) + 192 len (32 * msupportedTokensm.length) - floor32(msupportedTokensm.length)]), 


# hash = 0xc4efc91a
# getter = ['storage', 256, 0, 0]
# const = None
# payable = False
def unknownc4efc91a(): # not payable
  return munknownc4efc91a


# hash = 0xc6255626
# getter = ['struct', ['loc', 4]]
# const = None
# payable = False
def supportedTokens(uint256 m_param1): # not payable
  require m_param1 < msupportedTokensm.length
  return msupportedTokensm[m_param1m]m.field_0, msupportedTokensm[m_param1m]m.field_256


# hash = 0xcb3c28c7
# getter = None
# const = None
# payable = True
def trade(address m_src, uint256 m_srcAmount, address m_dest, address m_destAddress, uint256 m_maxDestAmount, uint256 m_minConversionRate, address m_walletId) payable: 
  if munknown40a73f89:
      require 0 >= m_minConversionRate
      if mstor3 == m_src:
          require m_srcAmount == call.value
          require ext_code.size(m_dest)
          call m_dest.decimals() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] >= 18:
              require ext_call.return_data[0] - 18 <= 18
              require ext_code.size(m_dest)
              call m_dest.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(m_destAddress), 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              return 0
          require -ext_call.return_data[0] + 18 <= 18
          require 10^18 * 10^(-ext_call.return_data[0] + 18)
          require ext_code.size(m_dest)
          call m_dest.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(m_destAddress), 0 / 10^18 * 10^(-ext_call.return_data[0] + 18)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          return (0 / 10^18 * 10^(-ext_call.return_data[0] + 18))
      require not call.value
      require ext_code.size(m_src)
      call m_src.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args caller, this.address, m_srcAmount
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(m_src)
      call m_src.decimals() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if mstor3 != m_dest:
          if 18 >= ext_call.return_data[0]:
              require -ext_call.return_data[0] + 18 <= 18
              require ext_code.size(m_dest)
              call m_dest.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(m_destAddress), 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              return 0
          require ext_call.return_data[0] - 18 <= 18
          require 10^18 * 10^(ext_call.return_data[0] - 18)
          require ext_code.size(m_dest)
          call m_dest.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(m_destAddress), 0 / 10^18 * 10^(ext_call.return_data[0] - 18)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      else:
          if 18 >= ext_call.return_data[0]:
              require -ext_call.return_data[0] + 18 <= 18
              call m_destAddress with:
                   gas 2300 wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  return 0
          require ext_call.return_data[0] - 18 <= 18
          require 10^18 * 10^(ext_call.return_data[0] - 18)
          if not 0 / 10^18 * 10^(ext_call.return_data[0] - 18) / 100:
              call m_destAddress with:
                   gas 2300 wei
          else:
              require munknownc4efc91a * 0 / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 / 0 / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 == munknownc4efc91a
              call m_destAddress with:
                 value munknownc4efc91a * 0 / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 wei
                   gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      return (0 / 10^18 * 10^(ext_call.return_data[0] - 18))
  if mstor3 == m_dest:
      require 10^15 >= m_minConversionRate
      if mstor3 == m_src:
          require m_srcAmount == call.value
          require ext_code.size(m_dest)
          call m_dest.decimals() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0] >= 18:
              require ext_call.return_data[0] - 18 <= 18
              require ext_code.size(m_dest)
              call m_dest.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(m_destAddress), 10^15 * 10^(ext_call.return_data[0] - 18) * m_srcAmount / 10^18
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              return (10^15 * 10^(ext_call.return_data[0] - 18) * m_srcAmount / 10^18)
          require -ext_call.return_data[0] + 18 <= 18
          require 10^18 * 10^(-ext_call.return_data[0] + 18)
          require ext_code.size(m_dest)
          call m_dest.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(m_destAddress), 10^15 * m_srcAmount / 10^18 * 10^(-ext_call.return_data[0] + 18)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          return (10^15 * m_srcAmount / 10^18 * 10^(-ext_call.return_data[0] + 18))
      require not call.value
      require ext_code.size(m_src)
      call m_src.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args caller, this.address, m_srcAmount
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(m_src)
      call m_src.decimals() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if mstor3 != m_dest:
          if 18 >= ext_call.return_data[0]:
              require -ext_call.return_data[0] + 18 <= 18
              require ext_code.size(m_dest)
              call m_dest.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(m_destAddress), 10^15 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              return (10^15 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18)
          require ext_call.return_data[0] - 18 <= 18
          require 10^18 * 10^(ext_call.return_data[0] - 18)
          require ext_code.size(m_dest)
          call m_dest.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(m_destAddress), 10^15 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18)
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      else:
          if 18 >= ext_call.return_data[0]:
              require -ext_call.return_data[0] + 18 <= 18
              if not 10^15 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100:
                  call m_destAddress with:
                       gas 2300 wei
              else:
                  require munknownc4efc91a * 10^15 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 / 10^15 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 == munknownc4efc91a
                  call m_destAddress with:
                     value munknownc4efc91a * 10^15 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 wei
                       gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              return (10^15 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18)
          require ext_call.return_data[0] - 18 <= 18
          require 10^18 * 10^(ext_call.return_data[0] - 18)
          if not 10^15 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100:
              call m_destAddress with:
                   gas 2300 wei
          else:
              require munknownc4efc91a * 10^15 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 / 10^15 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 == munknownc4efc91a
              call m_destAddress with:
                 value munknownc4efc91a * 10^15 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 wei
                   gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      return (10^15 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18))
  if mstor3 != m_src:
      if mstor3 != m_dest:
          [94midx = 0
          mwhile [94midx < msupportedTokensm.lengthm:
              mem[0] = 4
              if msupportedTokensm[[94midxm]m.field_0 != m_dest:
                  [94midx = [94midx + 1
                  mcontinue 
              require 10^18 >= m_minConversionRate
              if mstor3 == m_src:
                  require m_srcAmount == call.value
                  require ext_code.size(m_dest)
                  call m_dest.decimals() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data[0] >= 18:
                      require ext_call.return_data[0] - 18 <= 18
                      require ext_code.size(m_dest)
                      call m_dest.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_destAddress), 10^18 * 10^(ext_call.return_data[0] - 18) * m_srcAmount / 10^18
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      return (10^18 * 10^(ext_call.return_data[0] - 18) * m_srcAmount / 10^18)
                  require -ext_call.return_data[0] + 18 <= 18
                  require 10^18 * 10^(-ext_call.return_data[0] + 18)
                  require ext_code.size(m_dest)
                  call m_dest.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args addr(m_destAddress), 10^18 * m_srcAmount / 10^18 * 10^(-ext_call.return_data[0] + 18)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  return (10^18 * m_srcAmount / 10^18 * 10^(-ext_call.return_data[0] + 18))
              require not call.value
              require ext_code.size(m_src)
              call m_src.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, this.address, m_srcAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(m_src)
              call m_src.decimals() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if mstor3 != m_dest:
                  if 18 >= ext_call.return_data[0]:
                      require -ext_call.return_data[0] + 18 <= 18
                      require ext_code.size(m_dest)
                      call m_dest.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_destAddress), 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      return (10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18)
                  require ext_call.return_data[0] - 18 <= 18
                  require 10^18 * 10^(ext_call.return_data[0] - 18)
                  require ext_code.size(m_dest)
                  call m_dest.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args addr(m_destAddress), 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              else:
                  if 18 >= ext_call.return_data[0]:
                      require -ext_call.return_data[0] + 18 <= 18
                      if not 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100:
                          call m_destAddress with:
                               gas 2300 wei
                      else:
                          require munknownc4efc91a * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 / 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 == munknownc4efc91a
                          call m_destAddress with:
                             value munknownc4efc91a * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 wei
                               gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      return (10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18)
                  require ext_call.return_data[0] - 18 <= 18
                  require 10^18 * 10^(ext_call.return_data[0] - 18)
                  if not 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100:
                      call m_destAddress with:
                           gas 2300 wei
                  else:
                      require munknownc4efc91a * 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 / 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 == munknownc4efc91a
                      call m_destAddress with:
                         value munknownc4efc91a * 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 wei
                           gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
              return (10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18))
  else:
      [94midx = 0
      mwhile [94midx < msupportedTokensm.lengthm:
          mem[0] = 4
          if msupportedTokensm[[94midxm]m.field_0 != m_dest:
              [94midx = [94midx + 1
              mcontinue 
          require [94midx < msupportedTokensm.length
          require msupportedTokensm[[94midxm]m.field_256 >= m_minConversionRate
          if mstor3 == m_src:
              require m_srcAmount == call.value
              require ext_code.size(m_dest)
              call m_dest.decimals() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] >= 18:
                  require ext_call.return_data[0] - 18 <= 18
                  require ext_code.size(m_dest)
                  call m_dest.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args addr(m_destAddress), 10^(ext_call.return_data[0] - 18) * msupportedTokensm[[94midxm]m.field_256 * m_srcAmount / 10^18
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  return (10^(ext_call.return_data[0] - 18) * msupportedTokensm[[94midxm]m.field_256 * m_srcAmount / 10^18)
              require -ext_call.return_data[0] + 18 <= 18
              require 10^18 * 10^(-ext_call.return_data[0] + 18)
              require ext_code.size(m_dest)
              call m_dest.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(m_destAddress), m_srcAmount * msupportedTokensm[[94midxm]m.field_256 / 10^18 * 10^(-ext_call.return_data[0] + 18)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              return (m_srcAmount * msupportedTokensm[[94midxm]m.field_256 / 10^18 * 10^(-ext_call.return_data[0] + 18))
          require not call.value
          require ext_code.size(m_src)
          call m_src.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args caller, this.address, m_srcAmount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_code.size(m_src)
          call m_src.decimals() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if mstor3 != m_dest:
              if 18 >= ext_call.return_data[0]:
                  require -ext_call.return_data[0] + 18 <= 18
                  require ext_code.size(m_dest)
                  call m_dest.transfer(address to, uint256 value) with:
                       gas gas_remaining wei
                      args addr(m_destAddress), 10^(-ext_call.return_data[0] + 18) * msupportedTokensm[[94midxm]m.field_256 * m_srcAmount / 10^18
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  return (10^(-ext_call.return_data[0] + 18) * msupportedTokensm[[94midxm]m.field_256 * m_srcAmount / 10^18)
              require ext_call.return_data[0] - 18 <= 18
              require 10^18 * 10^(ext_call.return_data[0] - 18)
              require ext_code.size(m_dest)
              call m_dest.transfer(address to, uint256 value) with:
                   gas gas_remaining wei
                  args addr(m_destAddress), m_srcAmount * msupportedTokensm[[94midxm]m.field_256 / 10^18 * 10^(ext_call.return_data[0] - 18)
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
          else:
              if 18 >= ext_call.return_data[0]:
                  require -ext_call.return_data[0] + 18 <= 18
                  if not 10^(-ext_call.return_data[0] + 18) * msupportedTokensm[[94midxm]m.field_256 * m_srcAmount / 10^18 / 100:
                      call m_destAddress with:
                           gas 2300 wei
                  else:
                      require munknownc4efc91a * 10^(-ext_call.return_data[0] + 18) * msupportedTokensm[[94midxm]m.field_256 * m_srcAmount / 10^18 / 100 / 10^(-ext_call.return_data[0] + 18) * msupportedTokensm[[94midxm]m.field_256 * m_srcAmount / 10^18 / 100 == munknownc4efc91a
                      call m_destAddress with:
                         value munknownc4efc91a * 10^(-ext_call.return_data[0] + 18) * msupportedTokensm[[94midxm]m.field_256 * m_srcAmount / 10^18 / 100 wei
                           gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  return (10^(-ext_call.return_data[0] + 18) * msupportedTokensm[[94midxm]m.field_256 * m_srcAmount / 10^18)
              require ext_call.return_data[0] - 18 <= 18
              require 10^18 * 10^(ext_call.return_data[0] - 18)
              if not m_srcAmount * msupportedTokensm[[94midxm]m.field_256 / 10^18 * 10^(ext_call.return_data[0] - 18) / 100:
                  call m_destAddress with:
                       gas 2300 wei
              else:
                  require munknownc4efc91a * m_srcAmount * msupportedTokensm[[94midxm]m.field_256 / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 / m_srcAmount * msupportedTokensm[[94midxm]m.field_256 / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 == munknownc4efc91a
                  call m_destAddress with:
                     value munknownc4efc91a * m_srcAmount * msupportedTokensm[[94midxm]m.field_256 / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 wei
                       gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          return (m_srcAmount * msupportedTokensm[[94midxm]m.field_256 / 10^18 * 10^(ext_call.return_data[0] - 18))
      if mstor3 != m_src:
          if mstor3 != m_dest:
              [94midx = 0
              mwhile [94midx < msupportedTokensm.lengthm:
                  mem[0] = 4
                  if msupportedTokensm[[94midxm]m.field_0 != m_dest:
                      [94midx = [94midx + 1
                      mcontinue 
                  require 10^18 >= m_minConversionRate
                  if mstor3 == m_src:
                      require m_srcAmount == call.value
                      require ext_code.size(m_dest)
                      call m_dest.decimals() with:
                           gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if ext_call.return_data[0] >= 18:
                          require ext_call.return_data[0] - 18 <= 18
                          require ext_code.size(m_dest)
                          call m_dest.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(m_destAddress), 10^18 * 10^(ext_call.return_data[0] - 18) * m_srcAmount / 10^18
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          return (10^18 * 10^(ext_call.return_data[0] - 18) * m_srcAmount / 10^18)
                      require -ext_call.return_data[0] + 18 <= 18
                      require 10^18 * 10^(-ext_call.return_data[0] + 18)
                      require ext_code.size(m_dest)
                      call m_dest.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_destAddress), 10^18 * m_srcAmount / 10^18 * 10^(-ext_call.return_data[0] + 18)
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      return (10^18 * m_srcAmount / 10^18 * 10^(-ext_call.return_data[0] + 18))
                  require not call.value
                  require ext_code.size(m_src)
                  call m_src.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, this.address, m_srcAmount
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(m_src)
                  call m_src.decimals() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if mstor3 != m_dest:
                      if 18 >= ext_call.return_data[0]:
                          require -ext_call.return_data[0] + 18 <= 18
                          require ext_code.size(m_dest)
                          call m_dest.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args addr(m_destAddress), 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          return (10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18)
                      require ext_call.return_data[0] - 18 <= 18
                      require 10^18 * 10^(ext_call.return_data[0] - 18)
                      require ext_code.size(m_dest)
                      call m_dest.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(m_destAddress), 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18)
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                  else:
                      if 18 >= ext_call.return_data[0]:
                          require -ext_call.return_data[0] + 18 <= 18
                          if not 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100:
                              call m_destAddress with:
                                   gas 2300 wei
                          else:
                              require munknownc4efc91a * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 / 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 == munknownc4efc91a
                              call m_destAddress with:
                                 value munknownc4efc91a * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 wei
                                   gas 2300 * is_zero(value) wei
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          return (10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18)
                      require ext_call.return_data[0] - 18 <= 18
                      require 10^18 * 10^(ext_call.return_data[0] - 18)
                      if not 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100:
                          call m_destAddress with:
                               gas 2300 wei
                      else:
                          require munknownc4efc91a * 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 / 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 == munknownc4efc91a
                          call m_destAddress with:
                             value munknownc4efc91a * 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 wei
                               gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  return (10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18))
  require 1000 * 10^18 >= m_minConversionRate
  if mstor3 == m_src:
      require m_srcAmount == call.value
      require ext_code.size(m_dest)
      call m_dest.decimals() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[0] >= 18:
          require ext_call.return_data[0] - 18 <= 18
          require ext_code.size(m_dest)
          call m_dest.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(m_destAddress), 1000 * 10^18 * 10^(ext_call.return_data[0] - 18) * m_srcAmount / 10^18
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          return (1000 * 10^18 * 10^(ext_call.return_data[0] - 18) * m_srcAmount / 10^18)
      require -ext_call.return_data[0] + 18 <= 18
      require 10^18 * 10^(-ext_call.return_data[0] + 18)
      require ext_code.size(m_dest)
      call m_dest.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(m_destAddress), 1000 * 10^18 * m_srcAmount / 10^18 * 10^(-ext_call.return_data[0] + 18)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      return (1000 * 10^18 * m_srcAmount / 10^18 * 10^(-ext_call.return_data[0] + 18))
  require not call.value
  require ext_code.size(m_src)
  call m_src.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args caller, this.address, m_srcAmount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(m_src)
  call m_src.decimals() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if mstor3 != m_dest:
      if 18 >= ext_call.return_data[0]:
          require -ext_call.return_data[0] + 18 <= 18
          require ext_code.size(m_dest)
          call m_dest.transfer(address to, uint256 value) with:
               gas gas_remaining wei
              args addr(m_destAddress), 1000 * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          return (1000 * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18)
      require ext_call.return_data[0] - 18 <= 18
      require 10^18 * 10^(ext_call.return_data[0] - 18)
      require ext_code.size(m_dest)
      call m_dest.transfer(address to, uint256 value) with:
           gas gas_remaining wei
          args addr(m_destAddress), 1000 * 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
  else:
      if 18 >= ext_call.return_data[0]:
          require -ext_call.return_data[0] + 18 <= 18
          if not 1000 * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100:
              call m_destAddress with:
                   gas 2300 wei
          else:
              require munknownc4efc91a * 1000 * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 / 1000 * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 == munknownc4efc91a
              call m_destAddress with:
                 value munknownc4efc91a * 1000 * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18 / 100 wei
                   gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          return (1000 * 10^18 * 10^(-ext_call.return_data[0] + 18) * m_srcAmount / 10^18)
      require ext_call.return_data[0] - 18 <= 18
      require 10^18 * 10^(ext_call.return_data[0] - 18)
      if not 1000 * 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100:
          call m_destAddress with:
               gas 2300 wei
      else:
          require munknownc4efc91a * 1000 * 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 / 1000 * 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 == munknownc4efc91a
          call m_destAddress with:
             value munknownc4efc91a * 1000 * 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18) / 100 wei
               gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  return (1000 * 10^18 * m_srcAmount / 10^18 * 10^(ext_call.return_data[0] - 18))


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


