# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xA179584bb011B6C96040E807F4aaC057FEa611aC 
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
    # storage address 10
    stor10
    # storage address 48336328051221896682605502114020202344066604147838473745416963879837708750913
    stor6ADD # mask: a s
# hash = 0x151ac13e
# getter = None
# const = None
# payable = False
def unknown151ac13e(uint256 _param1, uint256 _param2, uint256 _param3): # not payable
  if stor2 != caller:
      revert with 0, 'not controller'
  if _param2 <= 0:
      revert with 0, 'target must > 0'
  if unknown926091d9[_param1].field_256:
      revert with 0, 'pharse has been set already'
  unknown926091d9[_param1].field_256 = _param2
  unknown926091d9[_param1].field_1280 = _param3
  if 1 == _param1 % 1000:
      stor10[_param1 / 1000].field_256 = block.timestamp
      if block.timestamp + stor5 < stor5:
          revert with 0, 'SafeMath add failed'
      stor10[_param1 / 1000].field_0 = block.timestamp + stor5


# hash = 0x4420e486
# getter = None
# const = None
# payable = True
def register(address _gameAddress) payable: 
  if ext_code.size(caller):
      revert with 0, 'sorry humans only'
  if call.value <= 10^16:
      revert with 0, 'no register fee'
  if not stor7[caller]:
      stor6++
      stor7[caller] = stor6 + 1
      stor8[stor6 + 1].field_0 = caller
      if not stor7[addr(_gameAddress)]:
          stor8[stor6].field_256 = 1
      else:
          if stor7[addr(_gameAddress)] == stor6:
              stor8[stor6].field_256 = 1
          else:
              stor8[stor6].field_256 = stor7[addr(_gameAddress)]
  if not stor1:
      call stor6ADD with:
         value call.value wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  else:
      require ext_code.size(stor1)
      call stor1.0xe5a0528a with:
           gas gas_remaining wei
          args stor7[caller], stor8[stor7[caller]].field_0, stor8[stor7[caller]].field_256
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      call stor6ADD with:
         value call.value wei
           gas 2300 * is_zero(value) wei


# hash = 0x59a51701
# getter = None
# const = None
# payable = False
def unknown59a51701(addr _param1, addr _param2): # not payable
  if stor2 != caller:
      revert with 0, 'not controller'
  if stor7[addr(_param1)]:
      if stor1:
          require ext_code.size(stor1)
          call stor1.0xe5a0528a with:
               gas gas_remaining wei
              args stor7[addr(_param1)], stor8[stor7[addr(_param1)]].field_0, stor8[stor7[addr(_param1)]].field_256
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
      return stor7[addr(_param1)], 0
  stor6++
  stor7[addr(_param1)] = stor6 + 1
  stor8[stor6 + 1].field_0 = _param1
  if not stor7[addr(_param2)]:
      stor8[stor6].field_256 = 1
  else:
      if stor7[addr(_param2)] == stor6:
          stor8[stor6].field_256 = 1
      else:
          stor8[stor6].field_256 = stor7[addr(_param2)]
  if stor1:
      require ext_code.size(stor1)
      call stor1.0xe5a0528a with:
           gas gas_remaining wei
          args stor7[addr(_param1)], stor8[stor7[addr(_param1)]].field_0, stor8[stor7[addr(_param1)]].field_256
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  return stor7[addr(_param1)], 1


# hash = 0x6979ee1b
# getter = None
# const = None
# payable = False
def unknown6979ee1b(addr _param1): # not payable
  require caller == stor0
  if not stor7[addr(_param1)]:
      stor6++
      stor7[addr(_param1)] = stor6 + 1
      stor8[stor6 + 1].field_0 = _param1
      if not stor7[0]:
          stor8[stor6].field_256 = 1
      else:
          if stor7[0] == stor6:
              stor8[stor6].field_256 = 1
          else:
              stor8[stor6].field_256 = stor7[0]
  if stor1:
      require ext_code.size(stor1)
      call stor1.0xe5a0528a with:
           gas gas_remaining wei
          args stor7[addr(_param1)], stor8[stor7[addr(_param1)]].field_0, stor8[stor7[addr(_param1)]].field_256
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0x6eee1c5d
# getter = None
# const = None
# payable = False
def unknown6eee1c5d(addr _param1, uint256 _param2): # not payable
  require caller == stor0
  if _param2 % 100 == 1:
      stor2 = _param1
  else:
      if 2 == _param2 % 100:
          stor1 = _param1
      else:
          if 3 == _param2 % 100:
              stor5 = _param2 / 100
          else:
              if not _param2 % 100:
                  if _param2 / 100:
                      stor3 = _param1
                  else:
                      stor3 = 0
                  stor4 = _param2 / 100


# hash = 0x704b6c02
# getter = None
# const = None
# payable = False
def setAdmin(address _newAdmin): # not payable
  require caller == stor0
  stor0 = _newAdmin


# hash = 0x74e7b3a4
# getter = ['struct', ['loc', 9]]
# const = None
# payable = False
def unknown74e7b3a4(uint256 _param1): # not payable
  return unknown926091d9[_param1].field_256, unknown926091d9[_param1].field_512


# hash = 0x926091d9
# getter = ['struct', ['loc', 9]]
# const = None
# payable = False
def unknown926091d9(uint256 _param1, uint256 _param2): # not payable
  return unknown926091d9[_param1].field_256, 
         unknown926091d9[_param1][4][_param2].field_0,
         unknown926091d9[_param1][6][_param2].field_0


# hash = 0xdb4feabd
# getter = None
# const = None
# payable = False
def unknowndb4feabd(uint256 _param1): # not payable
  return unknown926091d9[_param1].field_256, 
         unknown926091d9[_param1].field_512,
         unknown926091d9[_param1].field_768,
         unknown926091d9[_param1].field_1280,
         unknown926091d9[_param1].field_0,
         stor8[stor9[_param1].field_0].field_0


# hash = 0xe8c58763
# getter = None
# const = None
# payable = False
def unknowne8c58763(uint256 _param1): # not payable
  if not stor10[_param1 / 1000].field_256:
      return stor5
  if not stor10[_param1 / 1000].field_0:
      return stor5
  if block.timestamp < stor10[_param1 / 1000].field_0:
      if block.timestamp > stor10[_param1 / 1000].field_256:
          if block.timestamp > stor10[_param1 / 1000].field_0:
              revert with 0, 'SafeMath sub failed'
          return (stor10[_param1 / 1000].field_0 - block.timestamp)
  if not stor3:
      return 0
  if stor8[stor9[_param1].field_0].field_0 == stor3:
      return 0
  return 10


# hash = 0xfb6622dd
# getter = None
# const = None
# payable = False
def unknownfb6622dd(uint256 _param1, uint256 _param2): # not payable
  if not _param1:
      if _param2 < 0:
          revert with 0, 'SafeMath add failed'
      return _param2
  if 1000 * _param1 / _param1 != 1000:
      revert with 0, 'SafeMath mul failed'
  if _param2 + (1000 * _param1) < 1000 * _param1:
      revert with 0, 'SafeMath add failed'
  return (_param2 + (1000 * _param1))


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


