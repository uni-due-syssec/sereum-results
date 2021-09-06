# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x7a6c55A84F9F654ccFBb9AC138318e4B2e4cde8e 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    paused # mask: a s
    # storage address 1
    developerAddress # mask: a s
    # storage address 11
    stor11
    # storage address 20
    unknown3db3f75aAddress # mask: a s
# hash = 0x3db3f75a
# getter = ['storage', 160, 0, 20]
# const = None
# payable = True
def unknown3db3f75a() payable: 
  return munknown3db3f75aAddress


# hash = 0x3db4edd2
# getter = None
# const = None
# payable = True
def unknown3db4edd2(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if not munknownb9aaf2d9m[addr(m_param1)m]m.field_256:
      revert with 0, 32, 15, 0xe4bda0e6b292e69c89e4b88be7b79a0000000000000000000000000000000000
  if munknownb9aaf2d9m[addr(m_param1)m]m.field_256:
      mem[128 len 32 * munknownb9aaf2d9m[addr(m_param1)m]m.field_256] = code.data[4288 len 32 * munknownb9aaf2d9m[addr(m_param1)m]m.field_256]
  [94midx = 0
  mwhile [94midx < munknownb9aaf2d9m[addr(m_param1)m]m.field_256m:
      require [94midx < munknownb9aaf2d9m[addr(m_param1)m]m.field_256
      require [94midx < munknownb9aaf2d9m[addr(m_param1)m]m.field_256
      mem[(32 * [94midx) + 128] = munknownb9aaf2d9m[addr(m_param1)m]m[[94midx + 1m]m.field_0
      mem[0] = m_param1
      mem[32] = 21
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * munknownb9aaf2d9m[addr(m_param1)m]m.field_256) + 192 len floor32(munknownb9aaf2d9m[addr(m_param1)m]m.field_256)] = mem[128 len floor32(munknownb9aaf2d9m[addr(m_param1)m]m.field_256)]
  return Array(len=munknownb9aaf2d9m[addr(m_param1)m]m.field_256, data=mem[128 len floor32(munknownb9aaf2d9m[addr(m_param1)m]m.field_256)], mem[(32 * munknownb9aaf2d9m[addr(m_param1)m]m.field_256) + floor32(munknownb9aaf2d9m[addr(m_param1)m]m.field_256) + 192 len (32 * munknownb9aaf2d9m[addr(m_param1)m]m.field_256) - floor32(munknownb9aaf2d9m[addr(m_param1)m]m.field_256)]), 


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = True
def unpause() payable: 
  if mowner != caller:
      revert with 0, 'dOnly Owner Can Do This'
  require mpaused
  mpaused = 0
  log Unpause()


# hash = 0x40a6621c
# getter = None
# const = None
# payable = True
def unknown40a6621c(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if not munknownb9aaf2d9m[addr(m_param1)m]m.field_0:
      revert with 0, 32, 15, 0xe4bda0e698afe7acace4b880e4bba30000000000000000000000000000000000
  if munknownb9aaf2d9m[addr(m_param1)m]m.field_0:
      mem[128 len 32 * munknownb9aaf2d9m[addr(m_param1)m]m.field_0] = code.data[4288 len 32 * munknownb9aaf2d9m[addr(m_param1)m]m.field_0]
  [94midx = 0
  mwhile [94midx < munknownb9aaf2d9m[addr(m_param1)m]m.field_0m:
      require [94midx < munknownb9aaf2d9m[addr(m_param1)m]m.field_0
      require [94midx < munknownb9aaf2d9m[addr(m_param1)m]m.field_0
      mem[(32 * [94midx) + 128] = munknownb9aaf2d9m[addr(m_param1)m]m[[94midxm]m.field_0
      mem[0] = m_param1
      mem[32] = 21
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * munknownb9aaf2d9m[addr(m_param1)m]m.field_0) + 192 len floor32(munknownb9aaf2d9m[addr(m_param1)m]m.field_0)] = mem[128 len floor32(munknownb9aaf2d9m[addr(m_param1)m]m.field_0)]
  return Array(len=munknownb9aaf2d9m[addr(m_param1)m]m.field_0, data=mem[128 len floor32(munknownb9aaf2d9m[addr(m_param1)m]m.field_0)], mem[(32 * munknownb9aaf2d9m[addr(m_param1)m]m.field_0) + floor32(munknownb9aaf2d9m[addr(m_param1)m]m.field_0) + 192 len (32 * munknownb9aaf2d9m[addr(m_param1)m]m.field_0) - floor32(munknownb9aaf2d9m[addr(m_param1)m]m.field_0)]), 


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 1]]
# const = None
# payable = True
def paused() payable: 
  return bool(mpaused)


# hash = 0x715018a6
# getter = None
# const = None
# payable = True
def renounceOwnership() payable: 
  if mowner != caller:
      revert with 0, 'dOnly Owner Can Do This'
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x8456cb59
# getter = None
# const = None
# payable = True
def pause() payable: 
  if mowner != caller:
      revert with 0, 'dOnly Owner Can Do This'
  require not mpaused
  mpaused = 1
  log Pause()


# hash = 0x8bdbcbf5
# getter = None
# const = None
# payable = True
def unknown8bdbcbf5(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 'dOnly Owner Can Do This'
  munknown3db3f75aAddress = m_param1
  log 0x8ea90b43: addr(_param1), block.timestamp


# hash = 0x8cc401d5
# getter = None
# const = None
# payable = True
def unknown8cc401d5() payable: 
  if mdeveloperAddress != caller:
      revert with 0, 'Only Developer Can Do This'
  mdeveloperAddress = 0


# hash = 0x8d5457f0
# getter = None
# const = None
# payable = True
def unknown8d5457f0(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if munknown3db3f75aAddress != caller:
      revert with 0, 'Only for palyerBook contract!'
  log 0xec317adf: addr(_param1), block.timestamp


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def owner() payable: 
  return mowner


# hash = 0x93dae5eb
# getter = None
# const = None
# payable = True
def unknown93dae5eb(addr m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  if munknown3db3f75aAddress != caller:
      revert with 0, 'Only for palyerBook contract!'
  munknownb9aaf2d9m[addr(m_param1)m]m.field_0++
  munknownb9aaf2d9m[addr(m_param1)m]m[munknownb9aaf2d9m[addr(m_param1)m]m.field_0m]m.field_0 = m_param2
  if 10 == munknownb9aaf2d9m[addr(m_param2)m]m.field_0:
      [94midx = 0
      mwhile [94midx < 9m:
          mem[32] = 21
          require [94midx < munknownb9aaf2d9m[m_param2m]m.field_0
          munknownb9aaf2d9m[addr(m_param1)m]m.field_0++
          mem[0] = sha3(addr(m_param1), 21)
          munknownb9aaf2d9m[addr(m_param1)m]m[munknownb9aaf2d9m[addr(m_param1)m]m.field_0m]m.field_0 = munknownb9aaf2d9m[m_param2m]m[[94midxm]m.field_0
          [94midx = [94midx + 1
          mcontinue 
  else:
      if not munknownb9aaf2d9m[addr(m_param2)m]m.field_0:
      else:
          [94midx = 0
          mwhile [94midx < munknownb9aaf2d9m[addr(m_param2)m]m.field_0m:
              require [94midx < munknownb9aaf2d9m[m_param2m]m.field_0
              munknownb9aaf2d9m[addr(m_param1)m]m.field_0++
              munknownb9aaf2d9m[addr(m_param1)m]m[munknownb9aaf2d9m[addr(m_param1)m]m.field_0m]m.field_0 = munknownb9aaf2d9m[m_param2m]m[[94midxm]m.field_0
              mem[0] = m_param2
              mem[32] = 21
              [94midx = [94midx + 1
              mcontinue 
  log 0x744c7bf3: addr(_param1), addr(_param2), block.timestamp


# hash = 0x9bbee240
# getter = None
# const = None
# payable = True
def unknown9bbee240(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if mdeveloperAddress != caller:
      revert with 0, 'Only Developer Can Do This'
  if not m_param1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  35,
                  0xfe4e657720446576656c6f706572277320416464726573732069732052657175697265,
                  mem[199 len 29]
  mdeveloperAddress = m_param1


# hash = 0xb9aaf2d9
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 21]]]]
# const = None
# payable = True
def unknownb9aaf2d9(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknownb9aaf2d9m[addr(m_param1)m]m.field_256


# hash = 0xc90103fc
# getter = None
# const = None
# payable = True
def unknownc90103fc(addr m_param1, uint256 m_param2, addr m_param3, uint256 m_param4) payable: 
  require calldata.size - 4 >= 128
  if munknown3db3f75aAddress != caller:
      revert with 0, 'Only for palyerBook contract!'
  munknownb9aaf2d9m[addr(m_param1)m]m.field_256++
  mstor[('array', 1, ('map', ('mask_shl', 160, 0, 0, ('param', '_param1')), ('name', 'unknownb9aaf2d9', 21))) + munknownb9aaf2d9m[addr(m_param1)m]m.field_256m]m.field_0 = m_param3
  require m_param4 < 9
  require mstor11m[m_param4m] + m_param2 >= m_param2
  return (mstor11m[m_param4m] + m_param2)


# hash = 0xca4b208b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def developer() payable: 
  return mdeveloperAddress


# hash = 0xd193dd2e
# getter = ['storage', 160, 0, ['sha3', ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 21]]]]
# const = None
# payable = True
def unknownd193dd2e(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  if not munknownb9aaf2d9m[addr(m_param1)m]m.field_0:
      revert with 0, 32, 15, 0xe4bda0e698afe7acace4b880e4bba30000000000000000000000000000000000
  require munknownb9aaf2d9m[addr(m_param1)m]m.field_0
  return munknownb9aaf2d9m[addr(m_param1)m]m.field_0


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address m_newOwner) payable: 
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 'dOnly Owner Can Do This'
  if not m_newOwner:
      revert with 0, 'New Owner's Address is Required'
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  mowner = m_newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


