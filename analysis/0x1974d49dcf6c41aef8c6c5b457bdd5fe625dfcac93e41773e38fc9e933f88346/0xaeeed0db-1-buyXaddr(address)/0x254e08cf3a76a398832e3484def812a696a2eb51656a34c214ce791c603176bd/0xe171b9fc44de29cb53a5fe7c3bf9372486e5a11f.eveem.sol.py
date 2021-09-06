# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xe171b9fC44DE29CB53a5fe7c3BF9372486E5A11F 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x8aaad159': 'unknown8aaad159(?)'} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    stor4 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    stor7
    # storage address 8
    stor8
    # storage address 9
    unknown926091d9
    # storage address 48336328051221896682605502114020202344066604147838473745416963879837708750913
    stor6ADD # mask: a s
# hash = 0x151ac13e
# getter = None
# const = None
# payable = False
def unknown151ac13e(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  if mstor2 != caller:
      revert with 0, 'not controller'
  if m_param2 <= 0:
      revert with 0, 'target must > 0'
  if munknown926091d9m[m_param1m]m.field_768:
      revert with 0, 'pharse has been set already'
  munknown926091d9m[m_param1m]m.field_768 = m_param2
  munknown926091d9m[m_param1m]m.field_1792 = m_param3
  munknown926091d9m[m_param1m]m.field_512 = block.timestamp
  if block.timestamp + mstor5 < mstor5:
      revert with 0, 'SafeMath add failed'
  munknown926091d9m[m_param1m]m.field_256 = block.timestamp + mstor5


# hash = 0x4420e486
# getter = None
# const = None
# payable = True
def register(address m_gameAddress) payable: 
  if ext_code.size(caller):
      revert with 0, 'sorry humans only'
  if call.value <= 10^16:
      revert with 0, 'no register fee'
  if not mstor7m[callerm]:
      mstor6++
      mstor7m[callerm] = mstor6 + 1
      mstor8m[mstor6 + 1m]m.field_0 = caller
      if not mstor7m[addr(m_gameAddress)m]:
          mstor8m[mstor6m]m.field_256 = 1
      else:
          if mstor7m[addr(m_gameAddress)m] == mstor6:
              mstor8m[mstor6m]m.field_256 = 1
          else:
              mstor8m[mstor6m]m.field_256 = mstor7m[addr(m_gameAddress)m]
  if not mstor1:
      call mstor6ADD with:
         value call.value wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  else:
      require ext_code.size(mstor1)
      call mstor1.0xe5a0528a with:
           gas gas_remaining wei
          args mstor7m[callerm], mstor8m[mstor7m[callerm]m]m.field_0, mstor8m[mstor7m[callerm]m]m.field_256
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      call mstor6ADD with:
         value call.value wei
           gas 2300 * is_zero(value) wei


# hash = 0x59a51701
# getter = None
# const = None
# payable = False
def unknown59a51701(addr m_param1, addr m_param2): # not payable
  if mstor2 != caller:
      revert with 0, 'not controller'
  if mstor7m[addr(m_param1)m]:
      if mstor1:
          require ext_code.size(mstor1)
          call mstor1.0xe5a0528a with:
               gas gas_remaining wei
              args mstor7m[addr(m_param1)m], mstor8m[mstor7m[addr(m_param1)m]m]m.field_0, mstor8m[mstor7m[addr(m_param1)m]m]m.field_256
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      return mstor7m[addr(m_param1)m], 0
  mstor6++
  mstor7m[addr(m_param1)m] = mstor6 + 1
  mstor8m[mstor6 + 1m]m.field_0 = m_param1
  if not mstor7m[addr(m_param2)m]:
      mstor8m[mstor6m]m.field_256 = 1
  else:
      if mstor7m[addr(m_param2)m] == mstor6:
          mstor8m[mstor6m]m.field_256 = 1
      else:
          mstor8m[mstor6m]m.field_256 = mstor7m[addr(m_param2)m]
  if mstor1:
      require ext_code.size(mstor1)
      call mstor1.0xe5a0528a with:
           gas gas_remaining wei
          args mstor7m[addr(m_param1)m], mstor8m[mstor7m[addr(m_param1)m]m]m.field_0, mstor8m[mstor7m[addr(m_param1)m]m]m.field_256
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  return mstor7m[addr(m_param1)m], 1


# hash = 0x6979ee1b
# getter = None
# const = None
# payable = False
def unknown6979ee1b(addr m_param1): # not payable
  require caller == mstor0
  if not mstor7m[addr(m_param1)m]:
      mstor6++
      mstor7m[addr(m_param1)m] = mstor6 + 1
      mstor8m[mstor6 + 1m]m.field_0 = m_param1
      if not mstor7m[0m]:
          mstor8m[mstor6m]m.field_256 = 1
      else:
          if mstor7m[0m] == mstor6:
              mstor8m[mstor6m]m.field_256 = 1
          else:
              mstor8m[mstor6m]m.field_256 = mstor7m[0m]
  if mstor1:
      require ext_code.size(mstor1)
      call mstor1.0xe5a0528a with:
           gas gas_remaining wei
          args mstor7m[addr(m_param1)m], mstor8m[mstor7m[addr(m_param1)m]m]m.field_0, mstor8m[mstor7m[addr(m_param1)m]m]m.field_256
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0x6eee1c5d
# getter = None
# const = None
# payable = False
def unknown6eee1c5d(addr m_param1, uint256 m_param2): # not payable
  require caller == mstor0
  if m_param2 % 100 == 1:
      mstor2 = m_param1
  else:
      if 2 == m_param2 % 100:
          mstor1 = m_param1
      else:
          if 3 == m_param2 % 100:
              mstor5 = m_param2 / 100
          else:
              if not m_param2 % 100:
                  if m_param2 / 100:
                      mstor3 = m_param1
                  else:
                      mstor3 = 0
                  mstor4 = m_param2 / 100


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address m_newAdmin): # not payable
  require caller == mstor0
  mstor0 = m_newAdmin


# hash = 0x74e7b3a4
# getter = ['struct', ['loc', 9]]
# const = None
# payable = False
def unknown74e7b3a4(uint256 m_param1): # not payable
  return munknown926091d9m[m_param1m]m.field_768, munknown926091d9m[m_param1m]m.field_1024


# hash = 0x926091d9
# getter = ['struct', ['loc', 9]]
# const = None
# payable = False
def unknown926091d9(uint256 m_param1, uint256 m_param2): # not payable
  return munknown926091d9m[m_param1m]m.field_768, 
         munknown926091d9m[m_param1m]m[6m]m[m_param2m]m.field_0,
         munknown926091d9m[m_param1m]m[8m]m[m_param2m]m.field_0


# hash = 0xdb4feabd
# getter = None
# const = None
# payable = False
def unknowndb4feabd(uint256 m_param1): # not payable
  return munknown926091d9m[m_param1m]m.field_768, 
         munknown926091d9m[m_param1m]m.field_1024,
         munknown926091d9m[m_param1m]m.field_1280,
         munknown926091d9m[m_param1m]m.field_1792,
         munknown926091d9m[m_param1m]m.field_0,
         mstor8m[mstor9m[m_param1m]m.field_0m]m.field_0


# hash = 0xe8c58763
# getter = None
# const = None
# payable = False
def unknowne8c58763(uint256 m_param1): # not payable
  if not munknown926091d9m[m_param1m]m.field_512:
      return mstor5
  if not munknown926091d9m[m_param1m]m.field_256:
      return mstor5
  if block.timestamp < munknown926091d9m[m_param1m]m.field_256:
      if block.timestamp > munknown926091d9m[m_param1m]m.field_512:
          if block.timestamp > munknown926091d9m[m_param1m]m.field_256:
              revert with 0, 'SafeMath sub failed'
          return (munknown926091d9m[m_param1m]m.field_256 - block.timestamp)
  if not mstor3:
      return 0
  if mstor8m[mstor9m[m_param1m]m.field_0m]m.field_0 == mstor3:
      return 0
  return 5


# hash = 0xfb6622dd
# getter = None
# const = None
# payable = False
def unknownfb6622dd(uint256 m_param1, uint256 m_param2): # not payable
  if not m_param1:
      if m_param2 < 0:
          revert with 0, 'SafeMath add failed'
      return m_param2
  if 1000 * m_param1 / m_param1 != 1000:
      revert with 0, 'SafeMath mul failed'
  if m_param2 + (1000 * m_param1) < 1000 * m_param1:
      revert with 0, 'SafeMath add failed'
  return (m_param2 + (1000 * m_param1))


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


