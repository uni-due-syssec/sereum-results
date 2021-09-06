# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x57053BCf9366d65198992075f43CC5Bf8d714F4f 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    name
    # storage address 1
    description
    # storage address 2
    category
    # storage address 3
    version
    # storage address 4
    unknown998da6af
    # storage address 5
    unknown89a07309
# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 0]]]], ['loc', 0]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 3]]]], ['loc', 3]]]
# const = None
# payable = False
def version(): # not payable
  return version[0 len version.length]


# hash = 0x7284e416
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 1]]]], ['loc', 1]]]
# const = None
# payable = False
def description(): # not payable
  return description[0 len description.length]


# hash = 0x89a07309
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 5]]]]]]]
# const = None
# payable = False
def unknown89a07309(addr _param1, addr _param2, addr _param3): # not payable
  return unknown89a07309[_param1][_param2][_param3]


# hash = 0x8f99506a
# getter = None
# const = None
# payable = False
def unknown8f99506a(): # not payable
  mem[96] = ('cd', 4).length
  if ('cd', 4).length:
      mem[128 len 32 * ('cd', 4).length] = code.data[2722 len 32 * ('cd', 4).length]
  [94midx = 0
  while [94midx < mem[96]:
      require [94midx < ('cd', 4).length
      mem[0] = addr(cd[36])
      mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 5))
      require [94midx < mem[96]
      mem[(32 * [94midx) + 128] = unknown89a07309[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][addr(cd[36])]
      [94midx = [94midx + 1
      continue 
  mem[(32 * ('cd', 4).length) + 128] = 32
  mem[(32 * ('cd', 4).length) + 160] = mem[96]
  mem[(32 * ('cd', 4).length) + 192 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  return 32, mem[(32 * ('cd', 4).length) + 160 len (32 * mem[96]) + 32]


# hash = 0x918f8674
# getter = None
# const = ['return', 10000]
# payable = False
const DENOMINATOR = 10000


# hash = 0x998da6af
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 4]]]]]
# const = None
# payable = False
def unknown998da6af(addr _param1, addr _param2): # not payable
  return unknown998da6af[_param1][_param2]


# hash = 0xb355c55e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 68]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 36]], ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 5]]]]]]]
# const = None
# payable = False
def unknownb355c55e(addr _param1, addr _param2, addr _param3): # not payable
  return unknown89a07309[addr(_param1)][addr(_param2)][addr(_param3)]


# hash = 0xce7b5574
# getter = None
# const = None
# payable = False
def unknownce7b5574(addr _param1): # not payable
  mem[96] = 0x85450abf00000000000000000000000000000000000000000000000000000000
  require ext_code.size(caller)
  call caller.0x85450abf with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[96 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 96
  require return_data.size >= 32
  [94m_4 = mem[96]
  require mem[96] <= 4294967296
  require mem[96] + 32 <= return_data.size
  require mem[mem[96] + 96] <= 4294967296 and mem[96] + (32 * mem[mem[96] + 96]) + 32 <= return_data.size
  [94m_6 = mem[mem[96] + 96]
  mem[ceil32(return_data.size) + 96] = mem[mem[96] + 96]
  mem[64] = ceil32(return_data.size) + (32 * [94m_6) + 128
  if not [94m_6:
      mem[0] = _param1
      mem[32] = sha3(caller, 4)
      require ext_code.size(caller)
      call caller.totalSupply() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[ceil32(return_data.size) + (32 * [94m_6) + 132] = caller
      require ext_code.size(_param1)
      call _param1.balanceOf(address owner) with:
           gas gas_remaining wei
          args caller
      mem[ceil32(return_data.size) + (32 * [94m_6) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_136 = mem[[94m_4 + 96]
      [94midx = 0
      [94ms = unknown998da6af[caller][addr(_param1)]
      while [94midx < [94m_136:
          require [94midx < mem[[94m_4 + 96]
          [94m_147 = mem[(32 * [94midx) + [94m_4 + 128]
          mem[ceil32(return_data.size) + (32 * [94m_6) + 132] = mem[(32 * [94midx) + [94m_4 + 140 len 20]
          require ext_code.size(caller)
          call caller.balanceOf(address owner) with:
               gas gas_remaining wei
              args addr([94m_147)
          mem[ceil32(return_data.size) + (32 * [94m_6) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_call.return_data[0]
              require [94midx < mem[ceil32(return_data.size) + 96]
              mem[ceil32(return_data.size) + (32 * [94midx) + 128] = 0 / ext_call.return_data[0]
              require [94midx < mem[[94m_4 + 96]
              require [94midx < mem[ceil32(return_data.size) + 96]
              require [94midx < mem[[94m_4 + 96]
              mem[0] = mem[[94m_4 + (32 * [94midx) + 140 len 20]
              mem[32] = sha3(addr(_param1), sha3(caller, 5))
              unknown89a07309[caller][addr(_param1)][mem[[94m_4 + (32 * [94midx) + 140 len 20]] += 0 / ext_call.return_data[0]
              if unknown89a07309[caller][addr(_param1)][mem[(32 * [94midx) + [94m_4 + 140 len 20]] != 0:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          else:
              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
              require ext_call.return_data[0]
              require [94midx < mem[ceil32(return_data.size) + 96]
              mem[ceil32(return_data.size) + (32 * [94midx) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0]
              require [94midx < mem[[94m_4 + 96]
              require [94midx < mem[ceil32(return_data.size) + 96]
              require [94midx < mem[[94m_4 + 96]
              mem[0] = mem[[94m_4 + (32 * [94midx) + 140 len 20]
              mem[32] = sha3(addr(_param1), sha3(caller, 5))
              unknown89a07309[caller][addr(_param1)][mem[[94m_4 + (32 * [94midx) + 140 len 20]] += ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0]
              if unknown89a07309[caller][addr(_param1)][mem[(32 * [94midx) + [94m_4 + 140 len 20]] != 0:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
  else:
      mem[ceil32(return_data.size) + 128 len 32 * [94m_6] = code.data[2722 len 32 * [94m_6]
      mem[0] = _param1
      mem[32] = sha3(caller, 4)
      require ext_code.size(caller)
      call caller.totalSupply() with:
           gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      mem[ceil32(return_data.size) + (32 * [94m_6) + 132] = caller
      require ext_code.size(_param1)
      call _param1.balanceOf(address owner) with:
           gas gas_remaining wei
          args caller
      mem[ceil32(return_data.size) + (32 * [94m_6) + 128] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      [94m_137 = mem[[94m_4 + 96]
      [94midx = 0
      [94ms = unknown998da6af[caller][addr(_param1)]
      while [94midx < [94m_137:
          require [94midx < mem[[94m_4 + 96]
          [94m_153 = mem[(32 * [94midx) + [94m_4 + 128]
          mem[ceil32(return_data.size) + (32 * [94m_6) + 132] = mem[(32 * [94midx) + [94m_4 + 140 len 20]
          require ext_code.size(caller)
          call caller.balanceOf(address owner) with:
               gas gas_remaining wei
              args addr([94m_153)
          mem[ceil32(return_data.size) + (32 * [94m_6) + 128] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_call.return_data[0]
              require [94midx < mem[ceil32(return_data.size) + 96]
              mem[ceil32(return_data.size) + (32 * [94midx) + 128] = 0 / ext_call.return_data[0]
              require [94midx < mem[[94m_4 + 96]
              require [94midx < mem[ceil32(return_data.size) + 96]
              require [94midx < mem[[94m_4 + 96]
              mem[0] = mem[[94m_4 + (32 * [94midx) + 140 len 20]
              mem[32] = sha3(addr(_param1), sha3(caller, 5))
              unknown89a07309[caller][addr(_param1)][mem[[94m_4 + (32 * [94midx) + 140 len 20]] += 0 / ext_call.return_data[0]
              if unknown89a07309[caller][addr(_param1)][mem[(32 * [94midx) + [94m_4 + 140 len 20]] != 0:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          else:
              require ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0] == ext_call.return_data[0]
              require ext_call.return_data[0]
              require [94midx < mem[ceil32(return_data.size) + 96]
              mem[ceil32(return_data.size) + (32 * [94midx) + 128] = ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0]
              require [94midx < mem[[94m_4 + 96]
              require [94midx < mem[ceil32(return_data.size) + 96]
              require [94midx < mem[[94m_4 + 96]
              mem[0] = mem[[94m_4 + (32 * [94midx) + 140 len 20]
              mem[32] = sha3(addr(_param1), sha3(caller, 5))
              unknown89a07309[caller][addr(_param1)][mem[[94m_4 + (32 * [94midx) + 140 len 20]] += ext_call.return_data[0] * ext_call.return_data[0] / ext_call.return_data[0]
              if unknown89a07309[caller][addr(_param1)][mem[(32 * [94midx) + [94m_4 + 140 len 20]] != 0:
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
          [94midx = [94midx + 1
          [94ms = [94ms + 1
          continue 
  unknown998da6af[caller][addr(_param1)] = [94ms
  mem[ceil32(return_data.size) + (32 * [94m_6) + 128] = 32
  mem[ceil32(return_data.size) + (32 * [94m_6) + 160] = mem[ceil32(return_data.size) + 96]
  mem[ceil32(return_data.size) + (32 * [94m_6) + 192 len floor32(mem[ceil32(return_data.size) + 96])] = mem[ceil32(return_data.size) + 128 len floor32(mem[ceil32(return_data.size) + 96])]
  return 32, mem[ceil32(return_data.size) + (32 * [94m_6) + 160 len (32 * mem[ceil32(return_data.size) + 96]) + 32]


# hash = 0xef430aa6
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 2]]]], ['loc', 2]]]
# const = None
# payable = False
def category(): # not payable
  return category[0 len category.length]


# hash = 0xf940e385
# getter = None
# const = None
# payable = False
def withdraw(address _receiver, address _token): # not payable
  unknown998da6af[caller][addr(_receiver)]--
  unknown89a07309[caller][addr(_receiver)][addr(_token)] = 0
  return unknown998da6af[caller][addr(_receiver)]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


