# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x40089B9f4d5Eb36d62548133f32E52B14fa54C52 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x43700afe': 'unknown43700afe(?)', '0x45e965cd': 'unknown45e965cd(?)', '0x95978868': 'unknown95978868(?)', '0x99a2e1ec': 'unknown99a2e1ec(?)'} 

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
# hash = 0x0054438d
# getter = None
# const = None
# payable = False
def unknown0054438d(addr _param1, uint256 _param2, uint256 _param3): # not payable
  mem[96] = 0xdb737c7800000000000000000000000000000000000000000000000000000000
  mem[100] = _param3
  mem[132] = 1
  require ext_code.size(stor6)
  call stor6.0xdb737c78 with:
       gas gas_remaining wei
      args _param3, 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 224
  require mem[256] <= 4294967296
  require mem[256] + 32 <= return_data.size
  require mem[mem[256] + 96] <= 4294967296 and mem[256] + (32 * mem[mem[256] + 96]) + 32 <= return_data.size
  require mem[288] <= 4294967296
  require mem[288] + 32 <= return_data.size
  require mem[mem[288] + 96] <= 4294967296 and mem[288] + (32 * mem[mem[288] + 96]) + 32 <= return_data.size
  if Mask(160, 32, _param3) >> 32 == _param1:
      return 0
  if not mem[192]:
      if _param2 < 0:
          return 0
  else:
      require stor2
      if _param2 < mem[192] * stor1 / stor2:
          return 0
  return 1


# hash = 0x0326c06b
# getter = None
# const = None
# payable = False
def unknown0326c06b(array _param1): # not payable
  mem[64] = ceil32(_param1.length) + 128
  mem[96] = _param1.length
  mem[128 len _param1.length] = _param1[all]
  [94midx = 0
  [94ms = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      if not Mask(1, 255, mem[[94midx + 128]) >> 7:
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      require [94midx < _param1.length
      if Mask(3, 253, mem[[94midx + 128]) >> 5 == 0x600000000000000000000000000000000000000000000000000000000000000:
          [94midx = [94midx + 2
          [94ms = [94ms + 1
          continue 
      require [94midx < _param1.length
      if Mask(4, 252, mem[[94midx + 128]) >> 4 == 0xe00000000000000000000000000000000000000000000000000000000000000:
          [94midx = [94midx + 3
          [94ms = [94ms + 1
          continue 
      require [94midx < _param1.length
      if Mask(5, 251, mem[[94midx + 128]) >> 3 != 0x1e00000000000000000000000000000000000000000000000000000000000000:
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94midx = [94midx + 4
      [94ms = [94ms + 1
      continue 
  return [94ms


# hash = 0x05117e0d
# getter = None
# const = None
# payable = False
def unknown05117e0d(addr _param1, array _param2): # not payable
  require ext_code.size(stor4)
  call stor4.balanceOf(address owner) with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < _param2.length:
      return 0
  return 1


# hash = 0x1dcd9b55
# getter = None
# const = None
# payable = False
def substring(string _str, uint256 _startIndex, uint256 _endIndex): # not payable
  mem[96] = _str.length
  mem[128 len _str.length] = _str[all]
  mem[ceil32(_str.length) + 128] = _endIndex - _startIndex
  mem[64] = ceil32(_str.length) + floor32(_endIndex + -_startIndex + 31) + 160
  if not _endIndex - _startIndex:
      [94midx = _startIndex
      while [94midx < _endIndex:
          require [94midx < mem[96]
          require [94midx - _startIndex < mem[ceil32(_str.length) + 128]
          mem[ceil32(_str.length) + [94midx + -_startIndex + 160 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          continue 
      [94m_25 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[ceil32(_str.length) + 128]
      [94m_27 = mem[ceil32(_str.length) + 128]
      mem[mem[64] + 64 len ceil32(mem[ceil32(_str.length) + 128])] = mem[ceil32(_str.length) + 160 len ceil32(mem[ceil32(_str.length) + 128])]
      if not [94m_27 % 32:
          return 32, mem[mem[64] + 32 len [94m_27 + 32]
      mem[floor32([94m_27) + mem[64] + 64] = mem[floor32([94m_27) + mem[64] + -([94m_27 % 32) + 96 len [94m_27 % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_27) + [94m_25 + -mem[64] + 96
  mem[ceil32(_str.length) + 160 len 32 * _endIndex - _startIndex] = code.data[7650 len 32 * _endIndex - _startIndex]
  [94midx = _startIndex
  while [94midx < _endIndex:
      require [94midx < mem[96]
      require [94midx - _startIndex < mem[ceil32(_str.length) + 128]
      mem[ceil32(_str.length) + [94midx + -_startIndex + 160 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      continue 
  [94m_30 = mem[64]
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[ceil32(_str.length) + 128]
  [94m_32 = mem[ceil32(_str.length) + 128]
  mem[mem[64] + 64 len ceil32(mem[ceil32(_str.length) + 128])] = mem[ceil32(_str.length) + 160 len ceil32(mem[ceil32(_str.length) + 128])]
  if not [94m_32 % 32:
      return 32, mem[mem[64] + 32 len [94m_32 + 32]
  mem[floor32([94m_32) + mem[64] + 64] = mem[floor32([94m_32) + mem[64] + -([94m_32 % 32) + 96 len [94m_32 % 32]
  return memory
    from mem[64]
     [93mlen floor32([94m_32) + [94m_30 + -mem[64] + 96


# hash = 0x4112987c
# getter = None
# const = None
# payable = False
def unknown4112987c(array _param1, array _param2, array _param3): # not payable
  mem[96] = _param1.length
  mem[128 len _param1.length] = _param1[all]
  mem[ceil32(_param1.length) + 128] = _param2.length
  mem[ceil32(_param1.length) + 160 len _param2.length] = _param2[all]
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 160] = _param3.length
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 192 len _param3.length] = _param3[all]
  mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 192] = 0
  mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 224] = 0
  mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256] = _param1.length + _param2.length + _param3.length
  mem[64] = ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + floor32(_param1.length + _param2.length + _param3.length + 31) + 288
  if not _param1.length + _param2.length + _param3.length:
      [94midx = 0
      [94ms = 0
      while [94midx < _param1.length:
          require [94midx < _param1.length
          require [94ms < _param1.length + _param2.length + _param3.length
          mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = _param1.length
      while [94midx < _param2.length:
          require [94midx < _param2.length
          require [94ms < _param1.length + _param2.length + _param3.length
          mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = _param1.length + _param2.length
      while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 160]:
          require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 160]
          require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256]
          mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = _param1.length + _param2.length + _param3.length
      while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 192]:
          require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 192]
          require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256]
          mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = _param1.length + _param2.length + _param3.length + mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 192]
      while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 224]:
          require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 224]
          require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256]
          mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94m_242 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256]
      [94m_244 = mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256]
      mem[mem[64] + 64 len ceil32(mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256])] = mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 288 len ceil32(mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256])]
      if not [94m_244 % 32:
          return 32, mem[mem[64] + 32 len [94m_244 + 32]
      mem[floor32([94m_244) + mem[64] + 64] = mem[floor32([94m_244) + mem[64] + -([94m_244 % 32) + 96 len [94m_244 % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_244) + [94m_242 + -mem[64] + 96
  mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 288 len 32 * _param1.length + _param2.length + _param3.length] = code.data[7650 len 32 * _param1.length + _param2.length + _param3.length]
  [94midx = 0
  [94ms = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      require [94ms < _param1.length + _param2.length + _param3.length
      mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  [94midx = 0
  [94ms = _param1.length
  while [94midx < _param2.length:
      require [94midx < _param2.length
      require [94ms < _param1.length + _param2.length + _param3.length
      mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  [94midx = 0
  [94ms = _param1.length + _param2.length
  while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 160]:
      require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 160]
      require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256]
      mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  [94m_205 = mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 192]
  [94midx = 0
  [94ms = _param1.length + _param2.length + _param3.length
  while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 192]:
      require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 192]
      require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256]
      mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) - 256
      [94m_205 = mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 192]
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  [94midx = 0
  [94ms = _param1.length + _param2.length + _param3.length + [94m_205
  while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 224]:
      require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 224]
      require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256]
      mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256]
  [94m_247 = mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256]
  mem[mem[64] + 64 len ceil32(mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256])] = mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 288 len ceil32(mem[ceil32(_param1.length) + ceil32(_param2.length) + ceil32(_param3.length) + 256])]
  if not [94m_247 % 32:
      return 32, mem[mem[64] + 32 len [94m_247 + 32]
  mem[floor32([94m_247) + mem[64] + 64] = mem[floor32([94m_247) + mem[64] + -([94m_247 % 32) + 96 len [94m_247 % 32]
  return 32, mem[mem[64] + 32 len floor32([94m_247) + 64]


# hash = 0x44525ace
# getter = None
# const = None
# payable = False
def unknown44525ace(uint8 _param1, uint256 _param2): # not payable
  if _param1 != 2:
      if _param1 != 3:
          if _param1 != 4:
              if _param1 != 5:
                  if _param2 <=′ 0:
                      return (-100000 * -_param2 + 99999 /′ 100000)
                  return (100000 * _param2 + 99999 /′ 100000)
          else:
              if _param1 != 5:
                  if _param2 <=′ 0:
                      return (-100 * -_param2 + 99 /′ 100)
                  return (100 * _param2 + 99 /′ 100)
      else:
          if _param1 != 4:
              if _param1 != 5:
                  if _param2 <=′ 0:
                      return (-1000 * -_param2 + 999 /′ 1000)
                  return (1000 * _param2 + 999 /′ 1000)
          else:
              if _param1 != 5:
                  if _param2 <=′ 0:
                      return (-100 * -_param2 + 99 /′ 100)
                  return (100 * _param2 + 99 /′ 100)
  else:
      if _param1 != 3:
          if _param1 != 4:
              if _param1 != 5:
                  if _param2 <=′ 0:
                      return (-10000 * -_param2 + 9999 /′ 10000)
                  return (10000 * _param2 + 9999 /′ 10000)
          else:
              if _param1 != 5:
                  if _param2 <=′ 0:
                      return (-100 * -_param2 + 99 /′ 100)
                  return (100 * _param2 + 99 /′ 100)
      else:
          if _param1 != 4:
              if _param1 != 5:
                  if _param2 <=′ 0:
                      return (-1000 * -_param2 + 999 /′ 1000)
                  return (1000 * _param2 + 999 /′ 1000)
          else:
              if _param1 != 5:
                  if _param2 <=′ 0:
                      return (-100 * -_param2 + 99 /′ 100)
                  return (100 * _param2 + 99 /′ 100)
  ('eq', 5, ('param', '_param1'))
  if _param2 <=′ 0:
      return (-10 * -_param2 + 9 /′ 10)
  return (10 * _param2 + 9 /′ 10)


# hash = 0x4d79874e
# getter = None
# const = ['return', 0]
# payable = False
const unknown4d79874e = 0


# hash = 0x62026229
# getter = None
# const = None
# payable = False
def unknown62026229(array _param1, array _param2): # not payable
  mem[(32 * _param2.length) + (32 * _param1.length) + 292 len floor32(_param1.length)] = call.data[_param1 + 36 len floor32(_param1.length)]
  mem[(64 * _param1.length) + (32 * _param2.length) + 292] = _param2.length
  mem[(64 * _param1.length) + (32 * _param2.length) + 324 len floor32(_param2.length)] = call.data[_param2 + 36 len floor32(_param2.length)]
  require ext_code.size(stor6)
  call stor6.0x3a7b41f with:
       gas gas_remaining wei
      args 0, 96, (32 * _param1.length) + 128, _param1.length, call.data[_param1 + 36 len floor32(_param1.length)], mem[(32 * _param2.length) + (32 * _param1.length) + floor32(_param1.length) + 292 len (32 * _param2.length) + (32 * _param1.length) + -floor32(_param1.length) + 32]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0]:
      return 0
  return 1


# hash = 0x82568a24
# getter = None
# const = None
# payable = False
def unknown82568a24(addr _param1): # not payable
  require caller == stor0
  stor3 = _param1
  if stor3:
      stor4 = stor3


# hash = 0x862c5e16
# getter = None
# const = None
# payable = False
def unknown862c5e16(uint256 _param1, array _param2): # not payable
  require ext_code.size(stor6)
  call stor6.0x3fadc388 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if _param1 < ext_call.return_data[0] * _param2.length:
      return 0
  return 1


# hash = 0x997bc6c9
# getter = None
# const = None
# payable = False
def unknown997bc6c9(uint256 _param1): # not payable
  if not _param1:
      return '0'
  if _param1 <′ 0:
      [94ms = 0
      [94midx = -_param1
      while [94midx:
          [94ms = [94ms + 1
          [94midx = [94midx / 10
          continue 
      if _param1 >=′ 0:
          mem[96] = [94ms
          mem[64] = ceil32([94ms) + 128
          if not [94ms:
              [94mt = [94ms - 1
              [94midx = -_param1
              while [94midx:
                  require [94mt < mem[96]
                  mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
                  [94mt = [94mt - 1
                  [94midx = [94midx / 10
                  continue 
              if _param1 >=′ 0:
                  [94m_229 = mem[64]
                  mem[mem[64]] = 32
                  mem[mem[64] + 32] = mem[96]
                  [94m_231 = mem[96]
                  mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
                  if not mem[96] % 32:
                      return 32, mem[mem[64] + 32 len mem[96] + 32]
                  mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
                  return memory
                    from mem[64]
                     [93mlen floor32([94m_231) + [94m_229 + -mem[64] + 96
              require 0 < mem[96]
              mem[128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, "'-'"), 0) + 256, 0) << (('mask_shl', 8, 248, -3, "'-'"), 0) - 256
              [94m_254 = mem[64]
              mem[mem[64]] = 32
              mem[mem[64] + 32] = mem[96]
              [94m_256 = mem[96]
              mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
              if not mem[96] % 32:
                  return 32, mem[mem[64] + 32 len mem[96] + 32]
              mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
              return memory
                from mem[64]
                 [93mlen floor32([94m_256) + [94m_254 + -mem[64] + 96
          mem[128 len 32 * [94ms] = code.data[7650 len 32 * [94ms]
          [94mt = [94ms - 1
          [94midx = -_param1
          while [94midx:
              require [94mt < mem[96]
              mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
              [94mt = [94mt - 1
              [94midx = [94midx / 10
              continue 
          if _param1 >=′ 0:
              [94m_232 = mem[64]
              mem[mem[64]] = 32
              mem[mem[64] + 32] = mem[96]
              [94m_234 = mem[96]
              mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
              if not mem[96] % 32:
                  return 32, mem[mem[64] + 32 len mem[96] + 32]
              mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
              return memory
                from mem[64]
                 [93mlen floor32([94m_234) + [94m_232 + -mem[64] + 96
          require 0 < mem[96]
          mem[128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, "'-'"), 0) + 256, 0) << (('mask_shl', 8, 248, -3, "'-'"), 0) - 256
          [94m_258 = mem[64]
          mem[mem[64]] = 32
          mem[mem[64] + 32] = mem[96]
          [94m_260 = mem[96]
          mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
          if not mem[96] % 32:
              return 32, mem[mem[64] + 32 len mem[96] + 32]
          mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
          return memory
            from mem[64]
             [93mlen floor32([94m_260) + [94m_258 + -mem[64] + 96
      mem[96] = [94ms + 1
      mem[64] = floor32([94ms + 32) + 128
      if not [94ms + 1:
          [94mt = [94ms
          [94midx = -_param1
          while [94midx:
              require [94mt < mem[96]
              mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
              [94mt = [94mt - 1
              [94midx = [94midx / 10
              continue 
          if _param1 >=′ 0:
              [94m_235 = mem[64]
              mem[mem[64]] = 32
              mem[mem[64] + 32] = mem[96]
              [94m_237 = mem[96]
              mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
              if not mem[96] % 32:
                  return 32, mem[mem[64] + 32 len mem[96] + 32]
              mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
              return memory
                from mem[64]
                 [93mlen floor32([94m_237) + [94m_235 + -mem[64] + 96
          require 0 < mem[96]
          mem[128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, "'-'"), 0) + 256, 0) << (('mask_shl', 8, 248, -3, "'-'"), 0) - 256
          [94m_262 = mem[64]
          mem[mem[64]] = 32
          mem[mem[64] + 32] = mem[96]
          [94m_264 = mem[96]
          mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
          if not mem[96] % 32:
              return 32, mem[mem[64] + 32 len mem[96] + 32]
          mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
          return memory
            from mem[64]
             [93mlen floor32([94m_264) + [94m_262 + -mem[64] + 96
      mem[128 len 32 * [94ms + 1] = code.data[7650 len 32 * [94ms + 1]
      [94mt = [94ms
      [94midx = -_param1
      while [94midx:
          require [94mt < mem[96]
          mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
          [94mt = [94mt - 1
          [94midx = [94midx / 10
          continue 
      if _param1 >=′ 0:
          [94m_238 = mem[64]
          mem[mem[64]] = 32
          mem[mem[64] + 32] = mem[96]
          [94m_240 = mem[96]
          mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
          if not mem[96] % 32:
              return 32, mem[mem[64] + 32 len mem[96] + 32]
          mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
          return memory
            from mem[64]
             [93mlen floor32([94m_240) + [94m_238 + -mem[64] + 96
      require 0 < mem[96]
      mem[128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, "'-'"), 0) + 256, 0) << (('mask_shl', 8, 248, -3, "'-'"), 0) - 256
      [94m_266 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[96]
      [94m_268 = mem[96]
      mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
      if not mem[96] % 32:
          return 32, mem[mem[64] + 32 len mem[96] + 32]
      mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_268) + [94m_266 + -mem[64] + 96
  [94ms = 0
  [94midx = _param1
  while [94midx:
      [94ms = [94ms + 1
      [94midx = [94midx / 10
      continue 
  if _param1 >=′ 0:
      mem[96] = [94ms
      mem[64] = ceil32([94ms) + 128
      if not [94ms:
          [94mt = [94ms - 1
          [94midx = _param1
          while [94midx:
              require [94mt < mem[96]
              mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
              [94mt = [94mt - 1
              [94midx = [94midx / 10
              continue 
          if _param1 >=′ 0:
              [94m_241 = mem[64]
              mem[mem[64]] = 32
              mem[mem[64] + 32] = mem[96]
              [94m_243 = mem[96]
              mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
              if not mem[96] % 32:
                  return 32, mem[mem[64] + 32 len mem[96] + 32]
              mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
              return memory
                from mem[64]
                 [93mlen floor32([94m_243) + [94m_241 + -mem[64] + 96
          require 0 < mem[96]
          mem[128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, "'-'"), 0) + 256, 0) << (('mask_shl', 8, 248, -3, "'-'"), 0) - 256
          [94m_270 = mem[64]
          mem[mem[64]] = 32
          mem[mem[64] + 32] = mem[96]
          [94m_272 = mem[96]
          mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
          if not mem[96] % 32:
              return 32, mem[mem[64] + 32 len mem[96] + 32]
          mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
          return memory
            from mem[64]
             [93mlen floor32([94m_272) + [94m_270 + -mem[64] + 96
      mem[128 len 32 * [94ms] = code.data[7650 len 32 * [94ms]
      [94mt = [94ms - 1
      [94midx = _param1
      while [94midx:
          require [94mt < mem[96]
          mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
          [94mt = [94mt - 1
          [94midx = [94midx / 10
          continue 
      if _param1 >=′ 0:
          [94m_244 = mem[64]
          mem[mem[64]] = 32
          mem[mem[64] + 32] = mem[96]
          [94m_246 = mem[96]
          mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
          if not mem[96] % 32:
              return 32, mem[mem[64] + 32 len mem[96] + 32]
          mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
          return memory
            from mem[64]
             [93mlen floor32([94m_246) + [94m_244 + -mem[64] + 96
      require 0 < mem[96]
      mem[128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, "'-'"), 0) + 256, 0) << (('mask_shl', 8, 248, -3, "'-'"), 0) - 256
      [94m_274 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[96]
      [94m_276 = mem[96]
      mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
      if not mem[96] % 32:
          return 32, mem[mem[64] + 32 len mem[96] + 32]
      mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_276) + [94m_274 + -mem[64] + 96
  mem[96] = [94ms + 1
  mem[64] = floor32([94ms + 32) + 128
  if not [94ms + 1:
      [94mt = [94ms
      [94midx = _param1
      while [94midx:
          require [94mt < mem[96]
          mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
          [94mt = [94mt - 1
          [94midx = [94midx / 10
          continue 
      if _param1 >=′ 0:
          [94m_247 = mem[64]
          mem[mem[64]] = 32
          mem[mem[64] + 32] = mem[96]
          [94m_249 = mem[96]
          mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
          if not mem[96] % 32:
              return 32, mem[mem[64] + 32 len mem[96] + 32]
          mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
          return memory
            from mem[64]
             [93mlen floor32([94m_249) + [94m_247 + -mem[64] + 96
      require 0 < mem[96]
      mem[128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, "'-'"), 0) + 256, 0) << (('mask_shl', 8, 248, -3, "'-'"), 0) - 256
      [94m_278 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[96]
      [94m_280 = mem[96]
      mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
      if not mem[96] % 32:
          return 32, mem[mem[64] + 32 len mem[96] + 32]
      mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_280) + [94m_278 + -mem[64] + 96
  mem[128 len 32 * [94ms + 1] = code.data[7650 len 32 * [94ms + 1]
  [94mt = [94ms
  [94midx = _param1
  while [94midx:
      require [94mt < mem[96]
      mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
      [94mt = [94mt - 1
      [94midx = [94midx / 10
      continue 
  if _param1 >=′ 0:
      [94m_250 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[96]
      [94m_252 = mem[96]
      mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
      if not mem[96] % 32:
          return 32, mem[mem[64] + 32 len mem[96] + 32]
      mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_252) + [94m_250 + -mem[64] + 96
  require 0 < mem[96]
  mem[128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, "'-'"), 0) + 256, 0) << (('mask_shl', 8, 248, -3, "'-'"), 0) - 256
  [94m_282 = mem[64]
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[96]
  [94m_284 = mem[96]
  mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
  if not mem[96] % 32:
      return 32, mem[mem[64] + 32 len mem[96] + 32]
  mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
  return memory
    from mem[64]
     [93mlen floor32([94m_284) + [94m_282 + -mem[64] + 96


# hash = 0xbf4d89b5
# getter = None
# const = None
# payable = False
def parseInt(string _a, uint256 _b): # not payable
  mem[64] = ceil32(_a.length) + 128
  mem[96] = _a.length
  mem[128 len _a.length] = _a[all]
  [94midx = 0
  [94ms = 0
  while [94midx < _a.length:
      require [94midx < _a.length
      require [94midx < _a.length
      if Mask(8, 248, mem[[94midx + 128]) >= '0':
          if Mask(8, 248, mem[[94midx + 128]) <= '9':
              require [94midx < _a.length
              [94midx = [94midx + 1
              [94ms = (10 * [94ms) + mem[[94midx + 128 len 1] - 48
              continue 
      [94midx = [94midx + 1
      [94ms = [94ms
      continue 
  return [94ms


# hash = 0xd239004e
# getter = None
# const = None
# payable = False
def unknownd239004e(addr _param1): # not payable
  require caller == stor0
  stor5 = _param1
  if stor5:
      stor6 = stor5


# hash = 0xd67c7f35
# getter = None
# const = None
# payable = False
def unknownd67c7f35(uint256 _param1): # not payable
  require caller == stor0
  stor1 = _param1
  stor2 = 100


# hash = 0xda1eb542
# getter = None
# const = None
# payable = False
def unknownda1eb542(uint256 _param1, uint256 _param2): # not payable
  require _param2
  return (_param1 + _param2 - 1 /′ _param2 * _param2)


# hash = 0xf34309cd
# getter = None
# const = None
# payable = False
def unknownf34309cd(addr _param1): # not payable
  require caller == stor0
  stor0 = _param1


# hash = 0xf76f950e
# getter = None
# const = None
# payable = False
def unknownf76f950e(uint256 _param1): # not payable
  if not _param1:
      return '0'
  [94ms = 0
  [94midx = _param1
  while [94midx:
      [94ms = [94ms + 1
      [94midx = [94midx / 10
      continue 
  mem[96] = [94ms
  mem[64] = ceil32([94ms) + 128
  if not [94ms:
      [94mt = [94ms - 1
      [94midx = _param1
      while [94midx:
          require [94mt < mem[96]
          mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
          [94mt = [94mt - 1
          [94midx = [94midx / 10
          continue 
      [94m_32 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[96]
      [94m_34 = mem[96]
      mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
      if not mem[96] % 32:
          return 32, mem[mem[64] + 32 len mem[96] + 32]
      mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_34) + [94m_32 + -mem[64] + 96
  mem[128 len 32 * [94ms] = code.data[7650 len 32 * [94ms]
  [94mt = [94ms - 1
  [94midx = _param1
  while [94midx:
      require [94mt < mem[96]
      mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
      [94mt = [94mt - 1
      [94midx = [94midx / 10
      continue 
  [94m_35 = mem[64]
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[96]
  [94m_37 = mem[96]
  mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
  if not mem[96] % 32:
      return 32, mem[mem[64] + 32 len mem[96] + 32]
  mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
  return memory
    from mem[64]
     [93mlen floor32([94m_37) + [94m_35 + -mem[64] + 96


# hash = 0xff74927b
# getter = None
# const = None
# payable = False
def unknownff74927b(array _param1, array _param2): # not payable
  mem[96] = _param1.length
  mem[128 len _param1.length] = _param1[all]
  mem[ceil32(_param1.length) + 128] = _param2.length
  mem[ceil32(_param1.length) + 160 len _param2.length] = _param2[all]
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 160] = 0
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 192] = 0
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 224] = 0
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 256] = _param1.length + _param2.length
  mem[64] = ceil32(_param1.length) + ceil32(_param2.length) + floor32(_param1.length + _param2.length + 31) + 288
  if not _param1.length + _param2.length:
      [94midx = 0
      [94ms = 0
      while [94midx < _param1.length:
          require [94midx < _param1.length
          require [94ms < _param1.length + _param2.length
          mem[ceil32(_param1.length) + ceil32(_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = _param1.length
      while [94midx < _param2.length:
          require [94midx < _param2.length
          require [94ms < _param1.length + _param2.length
          mem[ceil32(_param1.length) + ceil32(_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = _param1.length + mem[ceil32(_param1.length) + 128]
      while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 160]:
          require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 160]
          require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + 256]
          mem[ceil32(_param1.length) + ceil32(_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94m_204 = mem[ceil32(_param1.length) + ceil32(_param2.length) + 192]
      [94midx = 0
      [94ms = _param1.length + mem[ceil32(_param1.length) + 128]
      while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 192]:
          require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 192]
          require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + 256]
          mem[ceil32(_param1.length) + ceil32(_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
          [94m_204 = mem[ceil32(_param1.length) + ceil32(_param2.length) + 192]
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94midx = 0
      [94ms = _param1.length + mem[ceil32(_param1.length) + 128] + [94m_204
      while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 224]:
          require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 224]
          require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + 256]
          mem[ceil32(_param1.length) + ceil32(_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
      [94m_242 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[ceil32(_param1.length) + ceil32(_param2.length) + 256]
      [94m_244 = mem[ceil32(_param1.length) + ceil32(_param2.length) + 256]
      mem[mem[64] + 64 len ceil32(mem[ceil32(_param1.length) + ceil32(_param2.length) + 256])] = mem[ceil32(_param1.length) + ceil32(_param2.length) + 288 len ceil32(mem[ceil32(_param1.length) + ceil32(_param2.length) + 256])]
      if not [94m_244 % 32:
          return 32, mem[mem[64] + 32 len [94m_244 + 32]
      mem[floor32([94m_244) + mem[64] + 64] = mem[floor32([94m_244) + mem[64] + -([94m_244 % 32) + 96 len [94m_244 % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_244) + [94m_242 + -mem[64] + 96
  mem[ceil32(_param1.length) + ceil32(_param2.length) + 288 len 32 * _param1.length + _param2.length] = code.data[7650 len 32 * _param1.length + _param2.length]
  [94midx = 0
  [94ms = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      require [94ms < _param1.length + _param2.length
      mem[ceil32(_param1.length) + ceil32(_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  [94midx = 0
  [94ms = _param1.length
  while [94midx < _param2.length:
      require [94midx < _param2.length
      require [94ms < _param1.length + _param2.length
      mem[ceil32(_param1.length) + ceil32(_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  [94midx = 0
  [94ms = _param1.length + mem[ceil32(_param1.length) + 128]
  while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 160]:
      require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 160]
      require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + 256]
      mem[ceil32(_param1.length) + ceil32(_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  [94m_205 = mem[ceil32(_param1.length) + ceil32(_param2.length) + 192]
  [94midx = 0
  [94ms = _param1.length + mem[ceil32(_param1.length) + 128]
  while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 192]:
      require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 192]
      require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + 256]
      mem[ceil32(_param1.length) + ceil32(_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
      [94m_205 = mem[ceil32(_param1.length) + ceil32(_param2.length) + 192]
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  [94midx = 0
  [94ms = _param1.length + mem[ceil32(_param1.length) + 128] + [94m_205
  while [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 224]:
      require [94midx < mem[ceil32(_param1.length) + ceil32(_param2.length) + 224]
      require [94ms < mem[ceil32(_param1.length) + ceil32(_param2.length) + 256]
      mem[ceil32(_param1.length) + ceil32(_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      continue 
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[ceil32(_param1.length) + ceil32(_param2.length) + 256]
  [94m_247 = mem[ceil32(_param1.length) + ceil32(_param2.length) + 256]
  mem[mem[64] + 64 len ceil32(mem[ceil32(_param1.length) + ceil32(_param2.length) + 256])] = mem[ceil32(_param1.length) + ceil32(_param2.length) + 288 len ceil32(mem[ceil32(_param1.length) + ceil32(_param2.length) + 256])]
  if not [94m_247 % 32:
      return 32, mem[mem[64] + 32 len [94m_247 + 32]
  mem[floor32([94m_247) + mem[64] + 64] = mem[floor32([94m_247) + mem[64] + -([94m_247 % 32) + 96 len [94m_247 % 32]
  return 32, mem[mem[64] + 32 len floor32([94m_247) + 64]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


