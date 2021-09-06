# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x83d5dd251c6519A0a6872dcb0754140EFF9635D5 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 6
    bytes
    # storage address 9
    unknowndd779dc0
    # storage address 10
    unknown2fc94ba6
    # storage address 11
    unknown2f392239
    # storage address 8
    unknowneca6cc2e
    # storage address 5
    string
    # storage address 4
    address
    # storage address 2
    unknown33598b00
    # storage address 7
    stor7
    # storage address 3
    bytes32
    # storage address 1
    securityTokenAddress # mask: a s
# hash = 0x079f34e5
# getter = None
# const = None
# payable = True
def unknown079f34e5(uint256 m_param1, uint256 m_param2, uint256 m_param3) payable: 
  require calldata.size - 4 >= 96
  if m_param3 < munknowndd779dc0m[m_param1m]m.field_0:
      mem[96] = m_param3 + -m_param2 + 1
      if m_param3 + -m_param2 + 1:
          mem[128 len 32 * m_param3 + -m_param2 + 1] = code.data[13115 len 32 * m_param3 + -m_param2 + 1]
      [94midx = 0
      mwhile [94midx < m_param3 + -m_param2 + 1m:
          mem[32] = 9
          require m_param2 + [94midx < munknowndd779dc0m[m_param1m]m.field_0
          mem[0] = sha3(m_param1, 9)
          require [94midx < mem[96]
          mem[(32 * [94midx) + 128] = mstor[('map', ('param', '_param1'), ('name', 'unknowndd779dc0', 9)) + m_param2 + [94midxm]m.field_0
          [94midx = [94midx + 1
          mcontinue 
      mem[(32 * m_param3 + -m_param2 + 1) + 128] = 32
      mem[(32 * m_param3 + -m_param2 + 1) + 160] = mem[96]
      mem[(32 * m_param3 + -m_param2 + 1) + 192 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
      return 32, mem[(32 * m_param3 + -m_param2 + 1) + 160 len (32 * mem[96]) + 32]
  mem[96] = munknowndd779dc0m[m_param1m]m.field_0 - m_param2
  if munknowndd779dc0m[m_param1m]m.field_0 - m_param2:
      mem[128 len 32 * munknowndd779dc0m[m_param1m]m.field_0 - m_param2] = code.data[13115 len 32 * munknowndd779dc0m[m_param1m]m.field_0 - m_param2]
  [94midx = 0
  mwhile [94midx < munknowndd779dc0m[m_param1m]m.field_0 - m_param2m:
      mem[32] = 9
      require m_param2 + [94midx < munknowndd779dc0m[m_param1m]m.field_0
      mem[0] = sha3(m_param1, 9)
      require [94midx < mem[96]
      mem[(32 * [94midx) + 128] = mstor[('map', ('param', '_param1'), ('name', 'unknowndd779dc0', 9)) + m_param2 + [94midxm]m.field_0
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * munknowndd779dc0m[m_param1m]m.field_0 - m_param2) + 128] = 32
  mem[(32 * munknowndd779dc0m[m_param1m]m.field_0 - m_param2) + 160] = mem[96]
  mem[(32 * munknowndd779dc0m[m_param1m]m.field_0 - m_param2) + 192 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  return 32, mem[(32 * munknowndd779dc0m[m_param1m]m.field_0 - m_param2) + 160 len (32 * mem[96]) + 32]


# hash = 0x07a7dfee
# getter = None
# const = None
# payable = True
def unknown07a7dfee(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  if not munknowneca6cc2em[m_param1m]m.field_0:
      mem[(32 * munknowneca6cc2em[m_param1m]m.field_0) + 128] = 32
      mem[(32 * munknowneca6cc2em[m_param1m]m.field_0) + 160] = munknowneca6cc2em[m_param1m]m.field_0
      mem[(32 * munknowneca6cc2em[m_param1m]m.field_0) + 192 len floor32(munknowneca6cc2em[m_param1m]m.field_0)] = mem[128 len floor32(munknowneca6cc2em[m_param1m]m.field_0)]
      return memory
        from (32 * munknowneca6cc2em[m_param1m]m.field_0) + 128
         [93mlen (96 * munknowneca6cc2em[m_param1m]m.field_0) + 64
  mem[128] = munknowneca6cc2em[m_param1m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknowneca6cc2em[m_param1m]m.field_0) + 96 > [94midxm:
      mem[[94midx + 32] = munknowneca6cc2em[m_param1m]m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * munknowneca6cc2em[m_param1m]m.field_0) + 192 len floor32(munknowneca6cc2em[m_param1m]m.field_0)] = mem[128 len floor32(munknowneca6cc2em[m_param1m]m.field_0)]
  return Array(len=munknowneca6cc2em[m_param1m]m.field_0, data=mem[128 len floor32(munknowneca6cc2em[m_param1m]m.field_0)], mem[(32 * munknowneca6cc2em[m_param1m]m.field_0) + floor32(munknowneca6cc2em[m_param1m]m.field_0) + 192 len (32 * munknowneca6cc2em[m_param1m]m.field_0) - floor32(munknowneca6cc2em[m_param1m]m.field_0)]), 


# hash = 0x116bb929
# getter = None
# const = None
# payable = True
def unknown116bb929(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  if not munknown2f392239m[m_param1m]m.field_0:
      mem[(32 * munknown2f392239m[m_param1m]m.field_0) + 128] = 32
      mem[(32 * munknown2f392239m[m_param1m]m.field_0) + 160] = munknown2f392239m[m_param1m]m.field_0
      mem[(32 * munknown2f392239m[m_param1m]m.field_0) + 192 len floor32(munknown2f392239m[m_param1m]m.field_0)] = mem[128 len floor32(munknown2f392239m[m_param1m]m.field_0)]
      return memory
        from (32 * munknown2f392239m[m_param1m]m.field_0) + 128
         [93mlen (96 * munknown2f392239m[m_param1m]m.field_0) + 64
  mem[128] = bool(uint8(munknown2f392239m[m_param1m]m.field_0))
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknown2f392239m[m_param1m]m.field_0) + 96 > [94midxm:
      mem[[94midx + 32] = bool(mstor('map', ('param', '_param1'), ('name', 'stor11', 11))m[-(0.03125 / [94ms + 1) + [94ms + (-1 * 0.03125 / [94ms + 1 * [94ms) + 1m])
      [94midx = [94midx + 32
      [94ms = -([94ms + 1 / 32) + [94ms + (-1 * [94ms + 1 / 32 * [94ms) + 1
      mcontinue 
  mem[(32 * munknown2f392239m[m_param1m]m.field_0) + 192 len floor32(munknown2f392239m[m_param1m]m.field_0)] = mem[128 len floor32(munknown2f392239m[m_param1m]m.field_0)]
  return Array(len=munknown2f392239m[m_param1m]m.field_0, data=mem[128 len floor32(munknown2f392239m[m_param1m]m.field_0)], mem[(32 * munknown2f392239m[m_param1m]m.field_0) + floor32(munknown2f392239m[m_param1m]m.field_0) + 192 len (32 * munknown2f392239m[m_param1m]m.field_0) - floor32(munknown2f392239m[m_param1m]m.field_0)]), 


# hash = 0x18e2d128
# getter = None
# const = None
# payable = True
def unknown18e2d128(array m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if m_param1.length != m_param2.length:
      revert with 0, 32, 10, 0xfe626164206c656e677468000000000000000000000000000000000000000000
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = this.address
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94midx < m_param2.length
      if not mem[(32 * [94midx) + 128]:
          revert with 0, 'bad key'
      mem[0] = mem[(32 * [94midx) + 128]
      mem[32] = 3
      mbytes32m[mem[(32 * [94midx) + 128]m] = mem[(32 * [94midx) + (32 * m_param1.length) + 160]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x21f8a721
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 4]]]
# const = None
# payable = True
def getAddress(bytes32 m_key) payable: 
  require calldata.size - 4 >= 32
  return maddressm[m_keym]


# hash = 0x26004846
# getter = None
# const = None
# payable = True
def unknown26004846(uint256 m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[100] = caller
          mem[132] = this.address
          mem[164] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[100] = caller
              mem[132] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  mem[128 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param2.length) + 128] = 0
  if not m_param1:
      revert with 0, 'bad key'
  munknowndd779dc0m[m_param1m]m.field_0 = m_param2.length
  if not m_param2.length:
      [94midx = 0
      mwhile munknowndd779dc0m[m_param1m]m.field_0 > [94midxm:
          munknowndd779dc0m[m_param1m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  else:
      [94ms = 0
      [94midx = 128
      mwhile (32 * m_param2.length) + 128 > [94midxm:
          munknowndd779dc0m[m_param1m]m[[94msm]m.field_0 = mem[[94midx]
          [94ms = [94ms + 1
          [94midx = [94midx + 32
          mcontinue 
      [94midx = Mask(251, 0, (32 * m_param2.length) + 31) >> 5
      mwhile munknowndd779dc0m[m_param1m]m.field_0 > [94midxm:
          munknowndd779dc0m[m_param1m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 


# hash = 0x287a1516
# getter = None
# const = None
# payable = True
def unknown287a1516(uint256 m_param1, uint256 m_param2, uint256 m_param3) payable: 
  require calldata.size - 4 >= 96
  if m_param3 < munknown2f392239m[m_param1m]m.field_0:
      mem[96] = m_param3 + -m_param2 + 1
      if m_param3 + -m_param2 + 1:
          mem[128 len 32 * m_param3 + -m_param2 + 1] = code.data[13115 len 32 * m_param3 + -m_param2 + 1]
      [94midx = 0
      mwhile [94midx < m_param3 + -m_param2 + 1m:
          mem[32] = 11
          require m_param2 + [94midx < munknown2f392239m[m_param1m]m.field_0
          mem[0] = sha3(m_param1, 11)
          require [94midx < mem[96]
          mem[(32 * [94midx) + 128] = bool(mstor('array', ('div', 0.03125, ('add', ('param', '_param2'), ('var', 0))), ('map', ('param', '_param1'), ('name', 'stor11', 11)))m[uint8(m_param2 + [94midx)m])
          [94midx = [94midx + 1
          mcontinue 
      mem[(32 * m_param3 + -m_param2 + 1) + 128] = 32
      mem[(32 * m_param3 + -m_param2 + 1) + 160] = mem[96]
      mem[(32 * m_param3 + -m_param2 + 1) + 192 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
      return 32, mem[(32 * m_param3 + -m_param2 + 1) + 160 len (32 * mem[96]) + 32]
  mem[96] = munknown2f392239m[m_param1m]m.field_0 - m_param2
  if munknown2f392239m[m_param1m]m.field_0 - m_param2:
      mem[128 len 32 * munknown2f392239m[m_param1m]m.field_0 - m_param2] = code.data[13115 len 32 * munknown2f392239m[m_param1m]m.field_0 - m_param2]
  [94midx = 0
  mwhile [94midx < munknown2f392239m[m_param1m]m.field_0 - m_param2m:
      mem[32] = 11
      require m_param2 + [94midx < munknown2f392239m[m_param1m]m.field_0
      mem[0] = sha3(m_param1, 11)
      require [94midx < mem[96]
      mem[(32 * [94midx) + 128] = bool(mstor('array', ('div', 0.03125, ('add', ('param', '_param2'), ('var', 0))), ('map', ('param', '_param1'), ('name', 'stor11', 11)))m[uint8(m_param2 + [94midx)m])
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * munknown2f392239m[m_param1m]m.field_0 - m_param2) + 128] = 32
  mem[(32 * munknown2f392239m[m_param1m]m.field_0 - m_param2) + 160] = mem[96]
  mem[(32 * munknown2f392239m[m_param1m]m.field_0 - m_param2) + 192 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  return 32, mem[(32 * munknown2f392239m[m_param1m]m.field_0 - m_param2) + 160 len (32 * mem[96]) + 32]


# hash = 0x2e28d084
# getter = None
# const = None
# payable = True
def setBytes(bytes32 m_key, bytes m_value) payable: 
  require calldata.size - 4 >= 64
  require m_value <= 4294967296
  require m_value + 36 <= calldata.size
  require m_value.length <= 4294967296 and m_value + m_value.length + 36 <= calldata.size
  if caller == msecurityTokenAddress:
      mem[128 len m_value.length] = m_value[allm]
      mem[m_value.length + 128] = 0
      if not m_key:
          revert with 0, 'bad key'
      mbytesm[m_keym] = (2 * m_value.length) + 1
      if m_value.length <= 0:
          [94midx = 0
          mwhile mbytesm[m_keym]m.length + 31 / 32 > [94midxm:
              mbytesm[m_keym]m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          mbytesm[m_keym] = mem[128]
          [94ms = 1
          [94midx = 160
          mwhile m_value.length + 128 > [94midxm:
              mbytesm[m_keym]m[[94msm] = mem[[94midx]
              [94ms = [94ms + 1
              [94midx = [94midx + 32
              mcontinue 
          [94midx = (Mask(251, 0, m_value.length - 1) >> 5) + 1
          mwhile mbytesm[m_keym]m.length + 31 / 32 > [94midxm:
              mbytesm[m_keym]m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
  else:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if caller == ext_call.return_data[12 len 20]:
          mem[128 len m_value.length] = m_value[allm]
          mem[m_value.length + 128] = 0
          if not m_key:
              revert with 0, 'bad key'
          mbytesm[m_keym] = (2 * m_value.length) + 1
          if m_value.length <= 0:
              [94midx = 0
              mwhile mbytesm[m_keym]m.length + 31 / 32 > [94midxm:
                  mbytesm[m_keym]m[[94midxm] = 0
                  [94midx = [94midx + 1
                  mcontinue 
          else:
              mbytesm[m_keym] = mem[128]
              [94ms = 1
              [94midx = 160
              mwhile m_value.length + 128 > [94midxm:
                  mbytesm[m_keym]m[[94msm] = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = (Mask(251, 0, m_value.length - 1) >> 5) + 1
              mwhile mbytesm[m_keym]m.length + 31 / 32 > [94midxm:
                  mbytesm[m_keym]m[[94midxm] = 0
                  [94midx = [94midx + 1
                  mcontinue 
      else:
          mem[100] = caller
          mem[132] = this.address
          mem[164] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0]:
              mem[128 len m_value.length] = m_value[allm]
              mem[m_value.length + 128] = 0
              if not m_key:
                  revert with 0, 'bad key'
              mbytesm[m_keym] = (2 * m_value.length) + 1
              if m_value.length <= 0:
                  [94midx = 0
                  mwhile mbytesm[m_keym]m.length + 31 / 32 > [94midxm:
                      mbytesm[m_keym]m[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mbytesm[m_keym] = mem[128 len 4], Mask(224, 32, this.address) >> 32
                  [94ms = 1
                  [94midx = 160
                  mwhile m_value.length + 128 > [94midxm:
                      mbytesm[m_keym]m[[94msm] = mem[[94midx]
                      [94ms = [94ms + 1
                      [94midx = [94midx + 32
                      mcontinue 
                  [94midx = (Mask(251, 0, m_value.length - 1) >> 5) + 1
                  mwhile mbytesm[m_keym]m.length + 31 / 32 > [94midxm:
                      mbytesm[m_keym]m[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
          else:
              mem[100] = caller
              mem[132] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
              mem[128 len m_value.length] = m_value[allm]
              mem[m_value.length + 128] = 0
              if not m_key:
                  revert with 0, 'bad key'
              mbytesm[m_keym] = (2 * m_value.length) + 1
              if m_value.length <= 0:
                  [94midx = 0
                  mwhile mbytesm[m_keym]m.length + 31 / 32 > [94midxm:
                      mbytesm[m_keym]m[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mbytesm[m_keym] = mem[128 len 4], 0
                  [94ms = 1
                  [94midx = 160
                  mwhile m_value.length + 128 > [94midxm:
                      mbytesm[m_keym]m[[94msm] = mem[[94midx]
                      [94ms = [94ms + 1
                      [94midx = [94midx + 32
                      mcontinue 
                  [94midx = (Mask(251, 0, m_value.length - 1) >> 5) + 1
                  mwhile mbytesm[m_keym]m.length + 31 / 32 > [94midxm:
                      mbytesm[m_keym]m[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 


# hash = 0x2f392239
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 11]]]
# const = None
# payable = True
def unknown2f392239(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown2f392239m[m_param1m]m.field_0


# hash = 0x2fc94ba6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 10]]]
# const = None
# payable = True
def unknown2fc94ba6(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown2fc94ba6m[m_param1m]m.field_0


# hash = 0x33598b00
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = True
def unknown33598b00(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknown33598b00m[m_param1m]


# hash = 0x35d4d407
# getter = None
# const = None
# payable = True
def unknown35d4d407(uint256 m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[100] = caller
          mem[132] = this.address
          mem[164] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[100] = caller
              mem[132] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  mem[128 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param2.length) + 128] = 0
  if not m_param1:
      revert with 0, 'bad key'
  munknown2f392239m[m_param1m]m.field_0 = m_param2.length
  if not m_param2.length:
      [94midx = 0
      mwhile munknown2f392239m[m_param1m]m.field_0 + 31 / 32 > [94midxm:
          uint8(munknown2f392239m[m_param1m]m[[94midxm]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 
  else:
      [94ms = 0
      [94midx = 128
      mwhile (32 * m_param2.length) + 128 > [94midxm:
          munknown2f392239m[m_param1m]m.field_0 = bool(mem[[94midx]) * 256^[94ms or !(255 * 256^[94ms) and munknown2f392239m[m_param1m]m.field_0
          [94ms = [94ms + -([94ms + 1 / 32) + (-1 * [94ms * [94ms + 1 / 32) + 1
          [94midx = [94midx + 32
          mcontinue 
      [94midx = Mask(251, 0, (32 * m_param2.length) + 31) >> 5
      [94ms = sha3(sha3(m_param1, 11))
      mwhile [94midxm:
          mstor[[94msm] = !(255 * 256^[94midx) and mstor[[94msm]
          [94midx = [94midx + -([94midx + 1 / 32) + (-1 * [94midx * [94midx + 1 / 32) + 1
          [94ms = ([94midx + 1 / 32) + [94ms
          mcontinue 
      [94midx = (floor32(None + 3) >> 4) + (None * None + 3 / 32) - (Mask(251, 0, (32 * m_param2.length) + 31) >> 5 * None + 3 / 32)
      mwhile munknown2f392239m[m_param1m]m.field_0 + 31 / 32 > [94midxm:
          uint8(munknown2f392239m[m_param1m]m[[94midxm]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 


# hash = 0x360ecc82
# getter = None
# const = None
# payable = True
def unknown360ecc82(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_param1:
      revert with 0, 'bad key'
  if m_param2 >= munknown2fc94ba6m[m_param1m]m.field_0:
      revert with 0, 'Invalid Index'
  require munknown2fc94ba6m[m_param1m]m.field_0 - 1 < munknown2fc94ba6m[m_param1m]m.field_0
  require m_param2 < munknown2fc94ba6m[m_param1m]m.field_0
  addr(munknown2fc94ba6m[m_param1m]m[m_param2m]m.field_0) = addr(munknown2fc94ba6m[m_param1m]m[munknown2fc94ba6m[m_param1m]m.field_0m]m.field_0)
  munknown2fc94ba6m[m_param1m]m.field_0--
  if munknown2fc94ba6m[m_param1m]m.field_0 > munknown2fc94ba6m[m_param1m]m.field_0 - 1:
      [94midx = munknown2fc94ba6m[m_param1m]m.field_0 - 1
      mwhile munknown2fc94ba6m[m_param1m]m.field_0 > [94midxm:
          munknown2fc94ba6m[m_param1m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 


# hash = 0x427f76be
# getter = None
# const = None
# payable = True
def unknown427f76be(uint256 m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[100] = caller
          mem[132] = this.address
          mem[164] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[100] = caller
              mem[132] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  mem[128 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param2.length) + 128] = 0
  if not m_param1:
      revert with 0, 'bad key'
  munknowneca6cc2em[m_param1m]m.field_0 = m_param2.length
  if not m_param2.length:
      [94midx = 0
      mwhile munknowneca6cc2em[m_param1m]m.field_0 > [94midxm:
          munknowneca6cc2em[m_param1m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 
  else:
      [94ms = 0
      [94midx = 128
      mwhile (32 * m_param2.length) + 128 > [94midxm:
          munknowneca6cc2em[m_param1m]m[[94msm]m.field_0 = mem[[94midx]
          [94ms = [94ms + 1
          [94midx = [94midx + 32
          mcontinue 
      [94midx = Mask(251, 0, (32 * m_param2.length) + 31) >> 5
      mwhile munknowneca6cc2em[m_param1m]m.field_0 > [94midxm:
          munknowneca6cc2em[m_param1m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 


# hash = 0x48893a04
# getter = None
# const = None
# payable = True
def unknown48893a04(array m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if m_param1.length != m_param2.length:
      revert with 0, 32, 10, 0xfe626164206c656e677468000000000000000000000000000000000000000000
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = this.address
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94midx < m_param2.length
      if not mem[(32 * [94midx) + 128]:
          revert with 0, 'bad key'
      mem[0] = mem[(32 * [94midx) + 128]
      mem[32] = 4
      maddressm[mem[(32 * [94midx) + 128]m] = mem[(32 * [94midx) + (32 * m_param1.length) + 172 len 20]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x4e91db08
# getter = None
# const = None
# payable = True
def setBytes32(bytes32 m_key, bytes32 m_value) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_key:
      revert with 0, 'bad key'
  mbytes32m[m_keym] = m_value


# hash = 0x4f3029c2
# getter = None
# const = None
# payable = True
def unknown4f3029c2(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_param1:
      revert with 0, 'bad key'
  munknown33598b00m[m_param1m] = m_param2


# hash = 0x5948f733
# getter = None
# const = None
# payable = True
def unknown5948f733(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  if not munknown2fc94ba6m[m_param1m]m.field_0:
      mem[(32 * munknown2fc94ba6m[m_param1m]m.field_0) + 128] = 32
      mem[(32 * munknown2fc94ba6m[m_param1m]m.field_0) + 160] = munknown2fc94ba6m[m_param1m]m.field_0
      mem[(32 * munknown2fc94ba6m[m_param1m]m.field_0) + 192 len floor32(munknown2fc94ba6m[m_param1m]m.field_0)] = mem[128 len floor32(munknown2fc94ba6m[m_param1m]m.field_0)]
      return memory
        from (32 * munknown2fc94ba6m[m_param1m]m.field_0) + 128
         [93mlen (96 * munknown2fc94ba6m[m_param1m]m.field_0) + 64
  mem[128] = addr(munknown2fc94ba6m[m_param1m]m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * munknown2fc94ba6m[m_param1m]m.field_0) + 96 > [94midxm:
      mem[[94midx + 32] = addr(munknown2fc94ba6m[m_param1m]m[[94msm]m.field_256)
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * munknown2fc94ba6m[m_param1m]m.field_0) + 192 len floor32(munknown2fc94ba6m[m_param1m]m.field_0)] = mem[128 len floor32(munknown2fc94ba6m[m_param1m]m.field_0)]
  return Array(len=munknown2fc94ba6m[m_param1m]m.field_0, data=mem[128 len floor32(munknown2fc94ba6m[m_param1m]m.field_0)], mem[(32 * munknown2fc94ba6m[m_param1m]m.field_0) + floor32(munknown2fc94ba6m[m_param1m]m.field_0) + 192 len (32 * munknown2fc94ba6m[m_param1m]m.field_0) - floor32(munknown2fc94ba6m[m_param1m]m.field_0)]), 


# hash = 0x5c9f5506
# getter = ['bool', ['storage', 8, ['mask_shl', 5, 0, 3, ['cd', 36]], ['add', ['mask_shl', 251, 5, -5, ['cd', 36]], ['sha3', ['sha3', ['data', ['cd', 4], 11]]]]]]
# const = None
# payable = True
def unknown5c9f5506(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param2 < munknown2f392239m[m_param1m]m.field_0
  return bool(mstor('array', ('div', 0.03125, ('param', '_param2')), ('map', ('param', '_param1'), ('name', 'stor11', 11)))m[uint8(m_param2)m])


# hash = 0x63a93477
# getter = None
# const = None
# payable = True
def unknown63a93477(array m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if m_param1.length != m_param2.length:
      revert with 0, 32, 10, 0xfe626164206c656e677468000000000000000000000000000000000000000000
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = this.address
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94midx < m_param2.length
      if not mem[(32 * [94midx) + 128]:
          revert with 0, 'bad key'
      mem[32] = 11
      munknown2f392239m[mem[(32 * [94midx) + 128]m]m.field_0++
      mem[0] = sha3(mem[(32 * [94midx) + 128], 11)
      munknown2f392239m[mem[(32 * [94midx) + 128]m]m[Mask(251, 0, munknown2f392239m[mem[(32 * [94midx) + 128]m]m.field_5)m]m.field_0 = !(255 * 256^munknown2f392239m[mem[(32 * [94midx) + 128]m]m.field_0 % 32) and munknown2f392239m[mem[(32 * [94midx) + 128]m]m[Mask(251, 0, munknown2f392239m[mem[(32 * [94midx) + 128]m]m.field_5)m]m.field_0 or 256^munknown2f392239m[mem[(32 * [94midx) + 128]m]m.field_0 % 32 * bool(mem[(32 * [94midx) + (32 * m_param1.length) + 160])
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x67ee16a1
# getter = None
# const = None
# payable = True
def unknown67ee16a1(uint256 m_param1, uint256 m_param2, uint256 m_param3) payable: 
  require calldata.size - 4 >= 96
  if m_param3 < munknowneca6cc2em[m_param1m]m.field_0:
      mem[96] = m_param3 + -m_param2 + 1
      if m_param3 + -m_param2 + 1:
          mem[128 len 32 * m_param3 + -m_param2 + 1] = code.data[13115 len 32 * m_param3 + -m_param2 + 1]
      [94midx = 0
      mwhile [94midx < m_param3 + -m_param2 + 1m:
          mem[32] = 8
          require m_param2 + [94midx < munknowneca6cc2em[m_param1m]m.field_0
          mem[0] = sha3(m_param1, 8)
          require [94midx < mem[96]
          mem[(32 * [94midx) + 128] = mstor[('map', ('param', '_param1'), ('name', 'unknowneca6cc2e', 8)) + m_param2 + [94midxm]m.field_0
          [94midx = [94midx + 1
          mcontinue 
      mem[(32 * m_param3 + -m_param2 + 1) + 128] = 32
      mem[(32 * m_param3 + -m_param2 + 1) + 160] = mem[96]
      mem[(32 * m_param3 + -m_param2 + 1) + 192 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
      return 32, mem[(32 * m_param3 + -m_param2 + 1) + 160 len (32 * mem[96]) + 32]
  mem[96] = munknowneca6cc2em[m_param1m]m.field_0 - m_param2
  if munknowneca6cc2em[m_param1m]m.field_0 - m_param2:
      mem[128 len 32 * munknowneca6cc2em[m_param1m]m.field_0 - m_param2] = code.data[13115 len 32 * munknowneca6cc2em[m_param1m]m.field_0 - m_param2]
  [94midx = 0
  mwhile [94midx < munknowneca6cc2em[m_param1m]m.field_0 - m_param2m:
      mem[32] = 8
      require m_param2 + [94midx < munknowneca6cc2em[m_param1m]m.field_0
      mem[0] = sha3(m_param1, 8)
      require [94midx < mem[96]
      mem[(32 * [94midx) + 128] = mstor[('map', ('param', '_param1'), ('name', 'unknowneca6cc2e', 8)) + m_param2 + [94midxm]m.field_0
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * munknowneca6cc2em[m_param1m]m.field_0 - m_param2) + 128] = 32
  mem[(32 * munknowneca6cc2em[m_param1m]m.field_0 - m_param2) + 160] = mem[96]
  mem[(32 * munknowneca6cc2em[m_param1m]m.field_0 - m_param2) + 192 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  return 32, mem[(32 * munknowneca6cc2em[m_param1m]m.field_0 - m_param2) + 160 len (32 * mem[96]) + 32]


# hash = 0x6ddf8174
# getter = None
# const = None
# payable = True
def unknown6ddf8174(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_param1:
      revert with 0, 'bad key'
  munknowneca6cc2em[m_param1m]m.field_0++
  munknowneca6cc2em[m_param1m]m[munknowneca6cc2em[m_param1m]m.field_0m]m.field_0 = m_param2


# hash = 0x6e899550
# getter = None
# const = None
# payable = True
def setString(bytes32 m_key, string m_value) payable: 
  require calldata.size - 4 >= 64
  require m_value <= 4294967296
  require m_value + 36 <= calldata.size
  require m_value.length <= 4294967296 and m_value + m_value.length + 36 <= calldata.size
  if caller == msecurityTokenAddress:
      mem[128 len m_value.length] = m_value[allm]
      mem[m_value.length + 128] = 0
      if not m_key:
          revert with 0, 'bad key'
      mstringm[m_keym] = (2 * m_value.length) + 1
      if m_value.length <= 0:
          [94midx = 0
          mwhile mstringm[m_keym]m.length + 31 / 32 > [94midxm:
              mstringm[m_keym]m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      else:
          mstringm[m_keym] = mem[128]
          [94ms = 1
          [94midx = 160
          mwhile m_value.length + 128 > [94midxm:
              mstringm[m_keym]m[[94msm] = mem[[94midx]
              [94ms = [94ms + 1
              [94midx = [94midx + 32
              mcontinue 
          [94midx = (Mask(251, 0, m_value.length - 1) >> 5) + 1
          mwhile mstringm[m_keym]m.length + 31 / 32 > [94midxm:
              mstringm[m_keym]m[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
  else:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if caller == ext_call.return_data[12 len 20]:
          mem[128 len m_value.length] = m_value[allm]
          mem[m_value.length + 128] = 0
          if not m_key:
              revert with 0, 'bad key'
          mstringm[m_keym] = (2 * m_value.length) + 1
          if m_value.length <= 0:
              [94midx = 0
              mwhile mstringm[m_keym]m.length + 31 / 32 > [94midxm:
                  mstringm[m_keym]m[[94midxm] = 0
                  [94midx = [94midx + 1
                  mcontinue 
          else:
              mstringm[m_keym] = mem[128]
              [94ms = 1
              [94midx = 160
              mwhile m_value.length + 128 > [94midxm:
                  mstringm[m_keym]m[[94msm] = mem[[94midx]
                  [94ms = [94ms + 1
                  [94midx = [94midx + 32
                  mcontinue 
              [94midx = (Mask(251, 0, m_value.length - 1) >> 5) + 1
              mwhile mstringm[m_keym]m.length + 31 / 32 > [94midxm:
                  mstringm[m_keym]m[[94midxm] = 0
                  [94midx = [94midx + 1
                  mcontinue 
      else:
          mem[100] = caller
          mem[132] = this.address
          mem[164] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data[0]:
              mem[128 len m_value.length] = m_value[allm]
              mem[m_value.length + 128] = 0
              if not m_key:
                  revert with 0, 'bad key'
              mstringm[m_keym] = (2 * m_value.length) + 1
              if m_value.length <= 0:
                  [94midx = 0
                  mwhile mstringm[m_keym]m.length + 31 / 32 > [94midxm:
                      mstringm[m_keym]m[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mstringm[m_keym] = mem[128 len 4], Mask(224, 32, this.address) >> 32
                  [94ms = 1
                  [94midx = 160
                  mwhile m_value.length + 128 > [94midxm:
                      mstringm[m_keym]m[[94msm] = mem[[94midx]
                      [94ms = [94ms + 1
                      [94midx = [94midx + 32
                      mcontinue 
                  [94midx = (Mask(251, 0, m_value.length - 1) >> 5) + 1
                  mwhile mstringm[m_keym]m.length + 31 / 32 > [94midxm:
                      mstringm[m_keym]m[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
          else:
              mem[100] = caller
              mem[132] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
              mem[128 len m_value.length] = m_value[allm]
              mem[m_value.length + 128] = 0
              if not m_key:
                  revert with 0, 'bad key'
              mstringm[m_keym] = (2 * m_value.length) + 1
              if m_value.length <= 0:
                  [94midx = 0
                  mwhile mstringm[m_keym]m.length + 31 / 32 > [94midxm:
                      mstringm[m_keym]m[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 
              else:
                  mstringm[m_keym] = mem[128 len 4], 0
                  [94ms = 1
                  [94midx = 160
                  mwhile m_value.length + 128 > [94midxm:
                      mstringm[m_keym]m[[94msm] = mem[[94midx]
                      [94ms = [94ms + 1
                      [94midx = [94midx + 32
                      mcontinue 
                  [94midx = (Mask(251, 0, m_value.length - 1) >> 5) + 1
                  mwhile mstringm[m_keym]m.length + 31 / 32 > [94midxm:
                      mstringm[m_keym]m[[94midxm] = 0
                      [94midx = [94midx + 1
                      mcontinue 


# hash = 0x7ae1cfca
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 7]]]]
# const = None
# payable = True
def getBool(bytes32 m_key) payable: 
  require calldata.size - 4 >= 32
  return bool(mstor7m[m_keym])


# hash = 0x7db8fa5e
# getter = None
# const = None
# payable = True
def unknown7db8fa5e(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_param1:
      revert with 0, 'bad key'
  if m_param2 >= munknown2f392239m[m_param1m]m.field_0:
      revert with 0, 'Invalid Index'
  require munknown2f392239m[m_param1m]m.field_0 - 1 < munknown2f392239m[m_param1m]m.field_0
  require m_param2 < munknown2f392239m[m_param1m]m.field_0
  munknown2f392239m[m_param1m]m[0.03125 / m_param2m]m.field_0 = bool(mstor('array', ('div', 0.03125, ('add', -1, ('stor', 256, 0, ('map', ('param', '_param1'), ('name', 'stor11', 11))))), ('map', ('param', '_param1'), ('name', 'stor11', 11)))m[uint8(mstor11m[m_param1m]m.field_0 - 1)m]) * 256^(m_param2 % 32) or !(255 * 256^(m_param2 % 32)) and munknown2f392239m[m_param1m]m[0.03125 / m_param2m]m.field_0
  munknown2f392239m[m_param1m]m.field_0--
  if munknown2f392239m[m_param1m]m.field_0 > munknown2f392239m[m_param1m]m.field_0 - 1:
      [94midx = munknown2f392239m[m_param1m]m.field_0 + 30 / 32
      mwhile munknown2f392239m[m_param1m]m.field_0 + 31 / 32 > [94midxm:
          munknown2f392239m[m_param1m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 


# hash = 0x81d65b2d
# getter = None
# const = None
# payable = True
def unknown81d65b2d(uint256 m_param1, addr m_param2) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_param1:
      revert with 0, 'bad key'
  munknown2fc94ba6m[m_param1m]m.field_0++
  addr(munknown2fc94ba6m[m_param1m]m[munknown2fc94ba6m[m_param1m]m.field_0m]m.field_0) = m_param2


# hash = 0x88bcd9e5
# getter = None
# const = None
# payable = True
def unknown88bcd9e5(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_param1:
      revert with 0, 'bad key'
  if m_param2 >= munknowneca6cc2em[m_param1m]m.field_0:
      revert with 0, 'Invalid Index'
  require munknowneca6cc2em[m_param1m]m.field_0 - 1 < munknowneca6cc2em[m_param1m]m.field_0
  require m_param2 < munknowneca6cc2em[m_param1m]m.field_0
  munknowneca6cc2em[m_param1m]m[m_param2m]m.field_0 = munknowneca6cc2em[m_param1m]m[munknowneca6cc2em[m_param1m]m.field_0m]m.field_0
  munknowneca6cc2em[m_param1m]m.field_0--
  if munknowneca6cc2em[m_param1m]m.field_0 > munknowneca6cc2em[m_param1m]m.field_0 - 1:
      [94midx = munknowneca6cc2em[m_param1m]m.field_0 - 1
      mwhile munknowneca6cc2em[m_param1m]m.field_0 > [94midxm:
          munknowneca6cc2em[m_param1m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 


# hash = 0x986e791a
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 5]]]]], ['sha3', ['data', ['cd', 4], 5]]]]
# const = None
# payable = True
def getString(bytes32 m_key) payable: 
  return mstringm[m_keym]m[0 len mstringm[m_keym]m.lengthm]


# hash = 0x988f3728
# getter = None
# const = None
# payable = True
def unknown988f3728(array m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if m_param1.length != m_param2.length:
      revert with 0, 32, 10, 0xfe626164206c656e677468000000000000000000000000000000000000000000
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = this.address
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94midx < m_param2.length
      if not mem[(32 * [94midx) + 128]:
          revert with 0, 'bad key'
      mem[32] = 8
      munknowneca6cc2em[mem[(32 * [94midx) + 128]m]m.field_0++
      mem[0] = sha3(mem[(32 * [94midx) + 128], 8)
      munknowneca6cc2em[mem[(32 * [94midx) + 128]m]m[munknowneca6cc2em[mem[(32 * [94midx) + 128]m]m.field_0m]m.field_0 = mem[(32 * [94midx) + (32 * m_param1.length) + 160]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x9920f9c2
# getter = None
# const = None
# payable = True
def unknown9920f9c2(addr m_param1) payable: 
  require calldata.size - 4 >= 32
  require ext_code.size(msecurityTokenAddress)
  static call msecurityTokenAddress.owner() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, 'Unauthorized'
  if not m_param1:
      revert with 0, 'Invalid address'
  log 0xcfafc05b: securityTokenAddress, _param1
  msecurityTokenAddress = m_param1


# hash = 0x9d849203
# getter = ['storage', 160, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 10]]], ['cd', 36]]]
# const = None
# payable = True
def unknown9d849203(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param2 < munknown2fc94ba6m[m_param1m]m.field_0
  return addr(munknown2fc94ba6m[m_param1m]m[m_param2m]m.field_0)


# hash = 0xa444d0fa
# getter = None
# const = None
# payable = True
def unknowna444d0fa(array m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if m_param1.length != m_param2.length:
      revert with 0, 32, 10, 0xfe626164206c656e677468000000000000000000000000000000000000000000
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = this.address
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94midx < m_param2.length
      if not mem[(32 * [94midx) + 128]:
          revert with 0, 'bad key'
      mem[32] = 9
      munknowndd779dc0m[mem[(32 * [94midx) + 128]m]m.field_0++
      mem[0] = sha3(mem[(32 * [94midx) + 128], 9)
      munknowndd779dc0m[mem[(32 * [94midx) + 128]m]m[munknowndd779dc0m[mem[(32 * [94midx) + 128]m]m.field_0m]m.field_0 = mem[(32 * [94midx) + (32 * m_param1.length) + 160]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xa6ed563e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 3]]]
# const = None
# payable = True
def getBytes32(bytes32 m_key) payable: 
  require calldata.size - 4 >= 32
  return mbytes32m[m_keym]


# hash = 0xabfdcced
# getter = None
# const = None
# payable = True
def setBool(bytes32 m_key, bool m_value) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_key:
      revert with 0, 'bad key'
  mstor7m[m_keym] = uint8(m_value)


# hash = 0xb84dfbd2
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def securityToken() payable: 
  return msecurityTokenAddress


# hash = 0xc031a180
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 6]]]]], ['sha3', ['data', ['cd', 4], 6]]]]
# const = None
# payable = True
def getBytes(bytes32 m_key) payable: 
  return mbytesm[m_keym]m[0 len mbytesm[m_keym]m.lengthm]


# hash = 0xc86a1cc6
# getter = None
# const = None
# payable = True
def unknownc86a1cc6(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_param1:
      revert with 0, 'bad key'
  if m_param2 >= munknowndd779dc0m[m_param1m]m.field_0:
      revert with 0, 'Invalid Index'
  require munknowndd779dc0m[m_param1m]m.field_0 - 1 < munknowndd779dc0m[m_param1m]m.field_0
  require m_param2 < munknowndd779dc0m[m_param1m]m.field_0
  munknowndd779dc0m[m_param1m]m[m_param2m]m.field_0 = munknowndd779dc0m[m_param1m]m[munknowndd779dc0m[m_param1m]m.field_0m]m.field_0
  munknowndd779dc0m[m_param1m]m.field_0--
  if munknowndd779dc0m[m_param1m]m.field_0 > munknowndd779dc0m[m_param1m]m.field_0 - 1:
      [94midx = munknowndd779dc0m[m_param1m]m.field_0 - 1
      mwhile munknowndd779dc0m[m_param1m]m.field_0 > [94midxm:
          munknowndd779dc0m[m_param1m]m[[94midxm]m.field_0 = 0
          [94midx = [94midx + 1
          mcontinue 


# hash = 0xca446dd9
# getter = None
# const = None
# payable = True
def setAddress(bytes32 m_key, address m_value) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_key:
      revert with 0, 'bad key'
  maddressm[m_keym] = m_value


# hash = 0xdabc29a9
# getter = None
# const = None
# payable = True
def unknowndabc29a9(uint256 m_param1, bool m_param2) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_param1:
      revert with 0, 'bad key'
  munknown2f392239m[m_param1m]m.field_0++
  munknown2f392239m[m_param1m]m[Mask(251, 0, munknown2f392239m[m_param1m]m.field_5)m]m.field_0 = !(255 * 256^munknown2f392239m[m_param1m]m.field_0 % 32) and munknown2f392239m[m_param1m]m[Mask(251, 0, munknown2f392239m[m_param1m]m.field_5)m]m.field_0 or 256^munknown2f392239m[m_param1m]m.field_0 % 32 * m_param2


# hash = 0xdd031997
# getter = None
# const = None
# payable = True
def unknowndd031997(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  if munknowndd779dc0m[m_param1m]m.field_0:
      mem[128] = munknowndd779dc0m[m_param1m]m.field_0
      if (32 * munknowndd779dc0m[m_param1m]m.field_0) + 32 > 64:
          mem[160] = munknowndd779dc0m[m_param1m]m.field_256
          [94midx = 160
          [94ms = 1
          mwhile (32 * munknowndd779dc0m[m_param1m]m.field_0) + 96 > [94midxm:
              mem[[94midx + 32] = munknowndd779dc0m[m_param1m]m[[94msm]m.field_256
              [94midx = [94midx + 32
              [94ms = [94ms + 1
              mcontinue 
  mem[(32 * munknowndd779dc0m[m_param1m]m.field_0) + 128] = 32
  mem[(32 * munknowndd779dc0m[m_param1m]m.field_0) + 160] = munknowndd779dc0m[m_param1m]m.field_0
  mem[(32 * munknowndd779dc0m[m_param1m]m.field_0) + 192 len floor32(munknowndd779dc0m[m_param1m]m.field_0)] = mem[128 len floor32(munknowndd779dc0m[m_param1m]m.field_0)]
  return memory
    from (32 * munknowndd779dc0m[m_param1m]m.field_0) + 128
     [93mlen (96 * munknowndd779dc0m[m_param1m]m.field_0) + 64


# hash = 0xdd779dc0
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 9]]], ['cd', 36]]]
# const = None
# payable = True
def unknowndd779dc0(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param2 < munknowndd779dc0m[m_param1m]m.field_0
  return munknowndd779dc0m[m_param1m]m[m_param2m]m.field_0


# hash = 0xe0349ba0
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = True
def unknowne0349ba0(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknowndd779dc0m[m_param1m]m.field_0


# hash = 0xe3c652cc
# getter = None
# const = None
# payable = True
def unknowne3c652cc(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  if not m_param1:
      revert with 0, 'bad key'
  munknowndd779dc0m[m_param1m]m.field_0++
  munknowndd779dc0m[m_param1m]m[munknowndd779dc0m[m_param1m]m.field_0m]m.field_0 = m_param2


# hash = 0xe7680259
# getter = None
# const = None
# payable = True
def unknowne7680259(array m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if m_param1.length != m_param2.length:
      revert with 0, 32, 10, 0xfe626164206c656e677468000000000000000000000000000000000000000000
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = this.address
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94midx < m_param2.length
      if not mem[(32 * [94midx) + 128]:
          revert with 0, 'bad key'
      mem[32] = 10
      munknown2fc94ba6m[mem[(32 * [94midx) + 128]m]m.field_0++
      mem[0] = sha3(mem[(32 * [94midx) + 128], 10)
      addr(munknown2fc94ba6m[mem[(32 * [94midx) + 128]m]m[munknown2fc94ba6m[mem[(32 * [94midx) + 128]m]m.field_0m]m.field_0) = mem[(32 * [94midx) + (32 * m_param1.length) + 172 len 20]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xeabebce0
# getter = None
# const = None
# payable = True
def unknowneabebce0(uint256 m_param1, uint256 m_param2, uint256 m_param3) payable: 
  require calldata.size - 4 >= 96
  if m_param3 < munknown2fc94ba6m[m_param1m]m.field_0:
      mem[96] = m_param3 + -m_param2 + 1
      if m_param3 + -m_param2 + 1:
          mem[128 len 32 * m_param3 + -m_param2 + 1] = code.data[13115 len 32 * m_param3 + -m_param2 + 1]
      [94midx = 0
      mwhile [94midx < m_param3 + -m_param2 + 1m:
          mem[32] = 10
          require m_param2 + [94midx < munknown2fc94ba6m[m_param1m]m.field_0
          mem[0] = sha3(m_param1, 10)
          require [94midx < mem[96]
          mem[(32 * [94midx) + 128] = addr(mstor[('map', ('param', '_param1'), ('name', 'unknown2fc94ba6', 10)) + m_param2 + [94midxm]m.field_0)
          [94midx = [94midx + 1
          mcontinue 
      mem[(32 * m_param3 + -m_param2 + 1) + 128] = 32
      mem[(32 * m_param3 + -m_param2 + 1) + 160] = mem[96]
      mem[(32 * m_param3 + -m_param2 + 1) + 192 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
      return 32, mem[(32 * m_param3 + -m_param2 + 1) + 160 len (32 * mem[96]) + 32]
  mem[96] = munknown2fc94ba6m[m_param1m]m.field_0 - m_param2
  if munknown2fc94ba6m[m_param1m]m.field_0 - m_param2:
      mem[128 len 32 * munknown2fc94ba6m[m_param1m]m.field_0 - m_param2] = code.data[13115 len 32 * munknown2fc94ba6m[m_param1m]m.field_0 - m_param2]
  [94midx = 0
  mwhile [94midx < munknown2fc94ba6m[m_param1m]m.field_0 - m_param2m:
      mem[32] = 10
      require m_param2 + [94midx < munknown2fc94ba6m[m_param1m]m.field_0
      mem[0] = sha3(m_param1, 10)
      require [94midx < mem[96]
      mem[(32 * [94midx) + 128] = addr(mstor[('map', ('param', '_param1'), ('name', 'unknown2fc94ba6', 10)) + m_param2 + [94midxm]m.field_0)
      [94midx = [94midx + 1
      mcontinue 
  mem[(32 * munknown2fc94ba6m[m_param1m]m.field_0 - m_param2) + 128] = 32
  mem[(32 * munknown2fc94ba6m[m_param1m]m.field_0 - m_param2) + 160] = mem[96]
  mem[(32 * munknown2fc94ba6m[m_param1m]m.field_0 - m_param2) + 192 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  return 32, mem[(32 * munknown2fc94ba6m[m_param1m]m.field_0 - m_param2) + 160 len (32 * mem[96]) + 32]


# hash = 0xeb5e9b3c
# getter = None
# const = None
# payable = True
def unknowneb5e9b3c(array m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if m_param1.length != m_param2.length:
      revert with 0, 32, 10, 0xfe626164206c656e677468000000000000000000000000000000000000000000
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = this.address
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94midx < m_param2.length
      if not mem[(32 * [94midx) + 128]:
          revert with 0, 'bad key'
      mem[0] = mem[(32 * [94midx) + 128]
      mem[32] = 7
      mstor7m[mem[(32 * [94midx) + 128]m] = uint8(bool(mem[(32 * [94midx) + (32 * m_param1.length) + 160]))
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xec672cf6
# getter = None
# const = None
# payable = True
def unknownec672cf6(uint256 m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[100] = caller
          mem[132] = this.address
          mem[164] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[100] = caller
              mem[132] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  mem[128 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param2.length) + 128] = 0
  if not m_param1:
      revert with 0, 'bad key'
  munknown2fc94ba6m[m_param1m]m.field_0 = m_param2.length
  if not m_param2.length:
      [94midx = 0
      mwhile munknown2fc94ba6m[m_param1m]m.field_0 > [94midxm:
          addr(munknown2fc94ba6m[m_param1m]m[[94midxm]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 
  else:
      [94ms = 0
      [94midx = 128
      mwhile (32 * m_param2.length) + 128 > [94midxm:
          addr(munknown2fc94ba6m[m_param1m]m[[94msm]m.field_0) = mem[[94midx + 12 len 20]
          [94ms = [94ms + 1
          [94midx = [94midx + 32
          mcontinue 
      [94midx = Mask(251, 0, (32 * m_param2.length) + 31) >> 5
      mwhile munknown2fc94ba6m[m_param1m]m.field_0 > [94midxm:
          addr(munknown2fc94ba6m[m_param1m]m[[94midxm]m.field_0) = 0
          [94midx = [94midx + 1
          mcontinue 


# hash = 0xeca6cc2e
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 8]]], ['cd', 36]]]
# const = None
# payable = True
def unknowneca6cc2e(uint256 m_param1, uint256 m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param2 < munknowneca6cc2em[m_param1m]m.field_0
  return munknowneca6cc2em[m_param1m]m[m_param2m]m.field_0


# hash = 0xf0a15434
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 8]]]
# const = None
# payable = True
def unknownf0a15434(uint256 m_param1) payable: 
  require calldata.size - 4 >= 32
  return munknowneca6cc2em[m_param1m]m.field_0


# hash = 0xf83280a9
# getter = None
# const = None
# payable = True
def unknownf83280a9(array m_param1, array m_param2) payable: 
  require calldata.size - 4 >= 64
  require m_param1 <= 4294967296
  require m_param1 + 36 <= calldata.size
  require m_param1.length <= 4294967296 and m_param1 + (32 * m_param1.length) + 36 <= calldata.size
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  require m_param2 <= 4294967296
  require m_param2 + 36 <= calldata.size
  require m_param2.length <= 4294967296 and m_param2 + (32 * m_param2.length) + 36 <= calldata.size
  mem[(32 * m_param1.length) + 128] = m_param2.length
  mem[(32 * m_param1.length) + 160 len 32 * m_param2.length] = call.data[m_param2 + 36 len 32 * m_param2.length]
  mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = 0
  if m_param1.length != m_param2.length:
      revert with 0, 32, 10, 0xfe626164206c656e677468000000000000000000000000000000000000000000
  if msecurityTokenAddress != caller:
      require ext_code.size(msecurityTokenAddress)
      static call msecurityTokenAddress.owner() with:
              gas gas_remaining wei
      mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if ext_call.return_data[12 len 20] != caller:
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = this.address
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 228] = 'MANAGEDATA'
          require ext_code.size(msecurityTokenAddress)
          static call msecurityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                  gas gas_remaining wei
                 args caller, this.address, 'MANAGEDATA'
          mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 164] = caller
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 196] = 6
              require ext_code.size(msecurityTokenAddress)
              static call msecurityTokenAddress.0x52cfe563 with:
                      gas gas_remaining wei
                     args caller, 6
              mem[(32 * m_param1.length) + (32 * m_param2.length) + 160] = ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if not ext_call.return_data[0]:
                  revert with 0, 'Unauthorized'
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94midx < m_param2.length
      if not mem[(32 * [94midx) + 128]:
          revert with 0, 'bad key'
      mem[0] = mem[(32 * [94midx) + 128]
      mem[32] = 2
      munknown33598b00m[mem[(32 * [94midx) + 128]m] = mem[(32 * [94midx) + (32 * m_param1.length) + 160]
      [94midx = [94midx + 1
      mcontinue 


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


