# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x6cd067629939290C5aBFf20E1F6fC8bd750508C0 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x43700afe': 'unknown43700afe(?)', '0x45e965cd': 'unknown45e965cd(?)', '0x95978868': 'unknown95978868(?)'} 

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
def unknown0054438d(addr m_param1, uint256 m_param2, uint256 m_param3): # not payable
  mem[96] = 0xdb737c7800000000000000000000000000000000000000000000000000000000
  mem[100] = m_param3
  mem[132] = 1
  require ext_code.size(mstor6)
  call mstor6.0xdb737c78 with:
       gas gas_remaining wei
      args m_param3, 1
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
  if Mask(160, 32, m_param3) >> 32 == m_param1:
      return 0
  if not mem[192]:
      if m_param2 < 0:
          return 0
  else:
      require mstor2
      if m_param2 < mem[192] * mstor1 / mstor2:
          return 0
  return 1


# hash = 0x0326c06b
# getter = None
# const = None
# payable = False
def unknown0326c06b(array m_param1): # not payable
  mem[64] = ceil32(m_param1.length) + 128
  mem[96] = m_param1.length
  mem[128 len m_param1.length] = m_param1[allm]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      if not Mask(1, 255, mem[[94midx + 128]) >> 7:
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      require [94midx < m_param1.length
      if Mask(3, 253, mem[[94midx + 128]) >> 5 == 0x600000000000000000000000000000000000000000000000000000000000000:
          [94midx = [94midx + 2
          [94ms = [94ms + 1
          mcontinue 
      require [94midx < m_param1.length
      if Mask(4, 252, mem[[94midx + 128]) >> 4 == 0xe00000000000000000000000000000000000000000000000000000000000000:
          [94midx = [94midx + 3
          [94ms = [94ms + 1
          mcontinue 
      require [94midx < m_param1.length
      if Mask(5, 251, mem[[94midx + 128]) >> 3 != 0x1e00000000000000000000000000000000000000000000000000000000000000:
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94midx = [94midx + 4
      [94ms = [94ms + 1
      mcontinue 
  return [94ms


# hash = 0x05117e0d
# getter = None
# const = None
# payable = False
def unknown05117e0d(addr m_param1, array m_param2): # not payable
  require ext_code.size(mstor4)
  call mstor4.balanceOf(address owner) with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < m_param2.length:
      return 0
  return 1


# hash = 0x1dcd9b55
# getter = None
# const = None
# payable = False
def substring(string m_str, uint256 m_startIndex, uint256 m_endIndex): # not payable
  mem[96] = m_str.length
  mem[128 len m_str.length] = m_str[allm]
  mem[ceil32(m_str.length) + 128] = m_endIndex - m_startIndex
  mem[64] = ceil32(m_str.length) + floor32(m_endIndex + -m_startIndex + 31) + 160
  if not m_endIndex - m_startIndex:
      [94midx = m_startIndex
      mwhile [94midx < m_endIndexm:
          require [94midx < mem[96]
          require [94midx - m_startIndex < mem[ceil32(m_str.length) + 128]
          mem[ceil32(m_str.length) + [94midx + -m_startIndex + 160 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          mcontinue 
      [94m_25 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[ceil32(m_str.length) + 128]
      [94m_27 = mem[ceil32(m_str.length) + 128]
      mem[mem[64] + 64 len ceil32(mem[ceil32(m_str.length) + 128])] = mem[ceil32(m_str.length) + 160 len ceil32(mem[ceil32(m_str.length) + 128])]
      if not [94m_27 % 32:
          return 32, mem[mem[64] + 32 len [94m_27 + 32]
      mem[floor32([94m_27) + mem[64] + 64] = mem[floor32([94m_27) + mem[64] + -([94m_27 % 32) + 96 len [94m_27 % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_27) + [94m_25 + -mem[64] + 96
  mem[ceil32(m_str.length) + 160 len 32 * m_endIndex - m_startIndex] = code.data[7173 len 32 * m_endIndex - m_startIndex]
  [94midx = m_startIndex
  mwhile [94midx < m_endIndexm:
      require [94midx < mem[96]
      require [94midx - m_startIndex < mem[ceil32(m_str.length) + 128]
      mem[ceil32(m_str.length) + [94midx + -m_startIndex + 160 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      mcontinue 
  [94m_30 = mem[64]
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[ceil32(m_str.length) + 128]
  [94m_32 = mem[ceil32(m_str.length) + 128]
  mem[mem[64] + 64 len ceil32(mem[ceil32(m_str.length) + 128])] = mem[ceil32(m_str.length) + 160 len ceil32(mem[ceil32(m_str.length) + 128])]
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
def unknown4112987c(array m_param1, array m_param2, array m_param3): # not payable
  mem[96] = m_param1.length
  mem[128 len m_param1.length] = m_param1[allm]
  mem[ceil32(m_param1.length) + 128] = m_param2.length
  mem[ceil32(m_param1.length) + 160 len m_param2.length] = m_param2[allm]
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160] = m_param3.length
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 192 len m_param3.length] = m_param3[allm]
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 192] = 0
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 224] = 0
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256] = m_param1.length + m_param2.length + m_param3.length
  mem[64] = ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + floor32(m_param1.length + m_param2.length + m_param3.length + 31) + 288
  if not m_param1.length + m_param2.length + m_param3.length:
      [94midx = 0
      [94ms = 0
      mwhile [94midx < m_param1.lengthm:
          require [94midx < m_param1.length
          require [94ms < m_param1.length + m_param2.length + m_param3.length
          mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94midx = 0
      [94ms = m_param1.length
      mwhile [94midx < m_param2.lengthm:
          require [94midx < m_param2.length
          require [94ms < m_param1.length + m_param2.length + m_param3.length
          mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94midx = 0
      [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128]
      mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160]m:
          require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160]
          require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256]
          mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94m_204 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 192]
      [94midx = 0
      [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128] + m_param3.length
      mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 192]m:
          require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 192]
          require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256]
          mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) - 256
          [94m_204 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 192]
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94m_234 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 224]
      [94midx = 0
      [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128] + m_param3.length + [94m_204
      mwhile [94midx < [94m_234m:
          require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 224]
          require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256]
          mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) - 256
          [94m_234 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 224]
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94m_242 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256]
      [94m_244 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256]
      mem[mem[64] + 64 len ceil32(mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256])] = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 288 len ceil32(mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256])]
      if not [94m_244 % 32:
          return 32, mem[mem[64] + 32 len [94m_244 + 32]
      mem[floor32([94m_244) + mem[64] + 64] = mem[floor32([94m_244) + mem[64] + -([94m_244 % 32) + 96 len [94m_244 % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_244) + [94m_242 + -mem[64] + 96
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 288 len 32 * m_param1.length + m_param2.length + m_param3.length] = code.data[7173 len 32 * m_param1.length + m_param2.length + m_param3.length]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94ms < m_param1.length + m_param2.length + m_param3.length
      mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  [94midx = 0
  [94ms = m_param1.length
  mwhile [94midx < m_param2.lengthm:
      require [94midx < m_param2.length
      require [94ms < m_param1.length + m_param2.length + m_param3.length
      mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  [94midx = 0
  [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128]
  mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160]m:
      require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160]
      require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256]
      mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  [94m_205 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 192]
  [94midx = 0
  [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128] + m_param3.length
  mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 192]m:
      require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 192]
      require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256]
      mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) - 256
      [94m_205 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 192]
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  [94midx = 0
  [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128] + m_param3.length + [94m_205
  mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 224]m:
      require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 224]
      require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256]
      mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param3'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  [94m_245 = mem[64]
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256]
  [94m_247 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256]
  mem[mem[64] + 64 len ceil32(mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256])] = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 288 len ceil32(mem[ceil32(m_param1.length) + ceil32(m_param2.length) + ceil32(m_param3.length) + 256])]
  if not [94m_247 % 32:
      return 32, mem[mem[64] + 32 len [94m_247 + 32]
  mem[floor32([94m_247) + mem[64] + 64] = mem[floor32([94m_247) + mem[64] + -([94m_247 % 32) + 96 len [94m_247 % 32]
  return memory
    from mem[64]
     [93mlen floor32([94m_247) + [94m_245 + -mem[64] + 96


# hash = 0x62026229
# getter = None
# const = None
# payable = False
def unknown62026229(array m_param1, array m_param2): # not payable
  mem[(32 * m_param2.length) + (32 * m_param1.length) + 292 len floor32(m_param1.length)] = call.data[m_param1 + 36 len floor32(m_param1.length)]
  mem[(64 * m_param1.length) + (32 * m_param2.length) + 292] = m_param2.length
  mem[(64 * m_param1.length) + (32 * m_param2.length) + 324 len floor32(m_param2.length)] = call.data[m_param2 + 36 len floor32(m_param2.length)]
  require ext_code.size(mstor6)
  call mstor6.0x3a7b41f with:
       gas gas_remaining wei
      args 0, 96, (32 * m_param1.length) + 128, m_param1.length, call.data[m_param1 + 36 len floor32(m_param1.length)], mem[(32 * m_param2.length) + (32 * m_param1.length) + floor32(m_param1.length) + 292 len (32 * m_param2.length) + (32 * m_param1.length) + -floor32(m_param1.length) + 32]
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
def unknown82568a24(addr m_param1): # not payable
  require caller == mstor0
  mstor3 = m_param1
  if mstor3:
      mstor4 = mstor3


# hash = 0x862c5e16
# getter = None
# const = None
# payable = False
def unknown862c5e16(uint256 m_param1, array m_param2): # not payable
  require ext_code.size(mstor6)
  call mstor6.0x3fadc388 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if m_param1 < ext_call.return_data[0] * m_param2.length:
      return 0
  return 1


# hash = 0x997bc6c9
# getter = None
# const = None
# payable = False
def unknown997bc6c9(uint256 m_param1): # not payable
  if not m_param1:
      return '0'
  if m_param1 <′ 0:
      [94ms = 0
      [94midx = -m_param1
      mwhile [94midxm:
          [94ms = [94ms + 1
          [94midx = [94midx / 10
          mcontinue 
      if m_param1 >=′ 0:
          mem[96] = [94ms
          mem[64] = ceil32([94ms) + 128
          if [94ms:
              mem[128 len 32 * [94ms] = code.data[7173 len 32 * [94ms]
          [94mt = [94ms - 1
          [94midx = -m_param1
          mwhile [94midxm:
              require [94mt < mem[96]
              mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
              [94mt = [94mt - 1
              [94midx = [94midx / 10
              mcontinue 
      else:
          mem[96] = [94ms + 1
          mem[64] = floor32([94ms + 32) + 128
          if [94ms + 1:
              mem[128 len 32 * [94ms + 1] = code.data[7173 len 32 * [94ms + 1]
          [94mt = [94ms
          [94midx = -m_param1
          mwhile [94midxm:
              require [94mt < mem[96]
              mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
              [94mt = [94mt - 1
              [94midx = [94midx / 10
              mcontinue 
  else:
      [94ms = 0
      [94midx = m_param1
      mwhile [94midxm:
          [94ms = [94ms + 1
          [94midx = [94midx / 10
          mcontinue 
      if m_param1 >=′ 0:
          mem[96] = [94ms
          mem[64] = ceil32([94ms) + 128
          if [94ms:
              mem[128 len 32 * [94ms] = code.data[7173 len 32 * [94ms]
          [94mt = [94ms - 1
          [94midx = m_param1
          mwhile [94midxm:
              require [94mt < mem[96]
              mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
              [94mt = [94mt - 1
              [94midx = [94midx / 10
              mcontinue 
      else:
          mem[96] = [94ms + 1
          mem[64] = floor32([94ms + 32) + 128
          if [94ms + 1:
              mem[128 len 32 * [94ms + 1] = code.data[7173 len 32 * [94ms + 1]
          [94mt = [94ms
          [94midx = m_param1
          mwhile [94midxm:
              require [94mt < mem[96]
              mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
              [94mt = [94mt - 1
              [94midx = [94midx / 10
              mcontinue 
  if m_param1 <′ 0:
      require 0 < mem[96]
      mem[128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, "'-'"), 0) + 256, 0) << (('mask_shl', 8, 248, -3, "'-'"), 0) - 256
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[96]
  mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
  if not mem[96] % 32:
      return 32, mem[mem[64] + 32 len mem[96] + 32]
  mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
  return Array(len=mem[96], data=mem[mem[64] + 64 len floor32(mem[96]) + 32])


# hash = 0xbf4d89b5
# getter = None
# const = None
# payable = False
def parseInt(string m_a, uint256 m_b): # not payable
  mem[64] = ceil32(m_a.length) + 128
  mem[96] = m_a.length
  mem[128 len m_a.length] = m_a[allm]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_a.lengthm:
      require [94midx < m_a.length
      require [94midx < m_a.length
      if Mask(8, 248, mem[[94midx + 128]) >= '0':
          if Mask(8, 248, mem[[94midx + 128]) <= '9':
              require [94midx < m_a.length
              [94midx = [94midx + 1
              [94ms = (10 * [94ms) + mem[[94midx + 128 len 1] - 48
              mcontinue 
      [94midx = [94midx + 1
      [94ms = [94ms
      mcontinue 
  return [94ms


# hash = 0xd239004e
# getter = None
# const = None
# payable = False
def unknownd239004e(addr m_param1): # not payable
  require caller == mstor0
  mstor5 = m_param1
  if mstor5:
      mstor6 = mstor5


# hash = 0xd67c7f35
# getter = None
# const = None
# payable = False
def unknownd67c7f35(uint256 m_param1): # not payable
  require caller == mstor0
  mstor1 = m_param1
  mstor2 = 100


# hash = 0xda1eb542
# getter = None
# const = None
# payable = False
def unknownda1eb542(uint256 m_param1, uint256 m_param2): # not payable
  require m_param2
  return (m_param1 + m_param2 - 1 /′ m_param2 * m_param2)


# hash = 0xf34309cd
# getter = None
# const = None
# payable = False
def unknownf34309cd(addr m_param1): # not payable
  require caller == mstor0
  mstor0 = m_param1


# hash = 0xf76f950e
# getter = None
# const = None
# payable = False
def unknownf76f950e(uint256 m_param1): # not payable
  if not m_param1:
      return '0'
  [94ms = 0
  [94midx = m_param1
  mwhile [94midxm:
      [94ms = [94ms + 1
      [94midx = [94midx / 10
      mcontinue 
  mem[96] = [94ms
  mem[64] = ceil32([94ms) + 128
  if [94ms:
      mem[128 len 32 * [94ms] = code.data[7173 len 32 * [94ms]
  [94mt = [94ms - 1
  [94midx = m_param1
  mwhile [94midxm:
      require [94mt < mem[96]
      mem[[94mt + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', 48, ('mod', ('var', 0), 10))), 0) - 256
      [94mt = [94mt - 1
      [94midx = [94midx / 10
      mcontinue 
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[96]
  mem[mem[64] + 64 len ceil32(mem[96])] = mem[128 len ceil32(mem[96])]
  if not mem[96] % 32:
      return 32, mem[mem[64] + 32 len mem[96] + 32]
  mem[floor32(mem[96]) + mem[64] + 64] = mem[floor32(mem[96]) + mem[64] + -(mem[96] % 32) + 96 len mem[96] % 32]
  return Array(len=mem[96], data=mem[mem[64] + 64 len floor32(mem[96]) + 32])


# hash = 0xff74927b
# getter = None
# const = None
# payable = False
def unknownff74927b(array m_param1, array m_param2): # not payable
  mem[96] = m_param1.length
  mem[128 len m_param1.length] = m_param1[allm]
  mem[ceil32(m_param1.length) + 128] = m_param2.length
  mem[ceil32(m_param1.length) + 160 len m_param2.length] = m_param2[allm]
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160] = 0
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 192] = 0
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 224] = 0
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256] = m_param1.length + m_param2.length
  mem[64] = ceil32(m_param1.length) + ceil32(m_param2.length) + floor32(m_param1.length + m_param2.length + 31) + 288
  if not m_param1.length + m_param2.length:
      [94midx = 0
      [94ms = 0
      mwhile [94midx < m_param1.lengthm:
          require [94midx < m_param1.length
          require [94ms < m_param1.length + m_param2.length
          mem[ceil32(m_param1.length) + ceil32(m_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94midx = 0
      [94ms = m_param1.length
      mwhile [94midx < m_param2.lengthm:
          require [94midx < m_param2.length
          require [94ms < m_param1.length + m_param2.length
          mem[ceil32(m_param1.length) + ceil32(m_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94midx = 0
      [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128]
      mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160]m:
          require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160]
          require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256]
          mem[ceil32(m_param1.length) + ceil32(m_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94m_204 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 192]
      [94midx = 0
      [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128]
      mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 192]m:
          require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 192]
          require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256]
          mem[ceil32(m_param1.length) + ceil32(m_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
          [94m_204 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 192]
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94midx = 0
      [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128] + [94m_204
      mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 224]m:
          require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 224]
          require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256]
          mem[ceil32(m_param1.length) + ceil32(m_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          mcontinue 
      [94m_242 = mem[64]
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256]
      [94m_244 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256]
      mem[mem[64] + 64 len ceil32(mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256])] = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 288 len ceil32(mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256])]
      if not [94m_244 % 32:
          return 32, mem[mem[64] + 32 len [94m_244 + 32]
      mem[floor32([94m_244) + mem[64] + 64] = mem[floor32([94m_244) + mem[64] + -([94m_244 % 32) + 96 len [94m_244 % 32]
      return memory
        from mem[64]
         [93mlen floor32([94m_244) + [94m_242 + -mem[64] + 96
  mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 288 len 32 * m_param1.length + m_param2.length] = code.data[7173 len 32 * m_param1.length + m_param2.length]
  [94midx = 0
  [94ms = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94ms < m_param1.length + m_param2.length
      mem[ceil32(m_param1.length) + ceil32(m_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  [94midx = 0
  [94ms = m_param1.length
  mwhile [94midx < m_param2.lengthm:
      require [94midx < m_param2.length
      require [94ms < m_param1.length + m_param2.length
      mem[ceil32(m_param1.length) + ceil32(m_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 160, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  [94midx = 0
  [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128]
  mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160]m:
      require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 160]
      require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256]
      mem[ceil32(m_param1.length) + ceil32(m_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 192, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  [94m_205 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 192]
  [94midx = 0
  [94ms = m_param1.length + mem[ceil32(m_param1.length) + 128]
  mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 192]m:
      require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 192]
      require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256]
      mem[ceil32(m_param1.length) + ceil32(m_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 224, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
      [94m_205 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 192]
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  [94midx = 0
  [94ms = m_param1.length + m_param2.length + [94m_205
  mwhile [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 224]m:
      require [94midx < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 224]
      require [94ms < mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256]
      mem[ceil32(m_param1.length) + ceil32(m_param2.length) + [94ms + 288 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 256, ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param1'))))), ('mask_shl', 251, 5, 0, ('add', 31, ('cd', ('add', 4, ('param', '_param2'))))), ('var', 0)), 32))), 0) - 256
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  [94m_245 = mem[64]
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256]
  [94m_247 = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256]
  mem[mem[64] + 64 len ceil32(mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256])] = mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 288 len ceil32(mem[ceil32(m_param1.length) + ceil32(m_param2.length) + 256])]
  if not [94m_247 % 32:
      return 32, mem[mem[64] + 32 len [94m_247 + 32]
  mem[floor32([94m_247) + mem[64] + 64] = mem[floor32([94m_247) + mem[64] + -([94m_247 % 32) + 96 len [94m_247 % 32]
  return memory
    from mem[64]
     [93mlen floor32([94m_247) + [94m_245 + -mem[64] + 96


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


