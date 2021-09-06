# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x673a06aE4C6ab436B7ceFD2acE23B0f913e9DF54 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x74eb0e4f': 'unknown74eb0e4f(?)', '0x80cbc89a': 'unknown80cbc89a(?)'} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 1
    stor1
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    stor3 # mask: a s
    # storage address 4
    unknownec8732a6 # mask: a s
    # storage address 5
    stor5 # mask: a s
    # storage address 6
    stor6
    # storage address 7
    stor7 # mask: a s
    # storage address 12
    stor12 # mask: a s
    # storage address 13
    stor13 # mask: a s
    # storage address 14
    unknown83fbce3fAddress # mask: a s
    # storage address 15
    stor15
    # storage address 16
    unknownc02e604e
    # storage address 17
    unknownc1f7d04a
    # storage address 18
    unknowncad1dc41
    # storage address 19
    stor19
    # storage address 21
    unknownf247466b # mask: a s
    # storage address 22
    unknown68231acc # mask: a s
    # storage address 23
    unknown015b9f12 # mask: a s
    # storage address 24
    stor24
    # storage address 45483720385226406541623267176334870569841410396899104104055643750338460383346
    stor648E # mask: a s
    # storage address 115146610599997141612367207981218290887837601005015034322912859661087402057312
    storFE92 # mask: a s
# hash = 0x015b9f12
# getter = ['bool', ['storage', 8, 0, 23]]
# const = None
# payable = False
def unknown015b9f12(): # not payable
  return bool(munknown015b9f12)


# hash = 0x2993ed2d
# getter = None
# const = None
# payable = False
def cancelSellOrder(address m_token, uint256 m_price): # not payable
  require calldata.size - 4 >= 64
  require caller == munknown83fbce3fAddress
  if m_price >= munknowncad1dc41m.length:
      revert with 0, 'id error'
  if munknowncad1dc41m[m_pricem]m.field_0 != m_token:
      revert with 0, 'only owner'
  if 275 * 10^11 * 3600 == mstor3:
      require m_price < munknowncad1dc41m.length
      if 5 * 10^16 == munknowncad1dc41m[m_pricem]m.field_512:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      38,
                      0x8a302e303939206e6f7420616c6c6f7765642063616e63656c20302e3120657468206f726465,
                      mem[202 len 26]
  if munknownf247466b:
      revert with 0, 'isFleshUp'
  require m_price < munknowncad1dc41m.length
  require ext_code.size(mstor13)
  static call mstor13.0xe52895b1 with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require munknowncad1dc41m[m_pricem]m.field_768 <= ext_call.return_data[0]
  require m_price < munknowncad1dc41m.length
  if not munknowncad1dc41m[m_pricem]m.field_256:
      require m_price < munknowncad1dc41m.length
      munknowncad1dc41m[m_pricem]m.field_0 = 0
      munknowncad1dc41m[m_pricem]m.field_256 = 0
      munknowncad1dc41m[m_pricem]m.field_512 = 0
      munknowncad1dc41m[m_pricem]m.field_768 = 0
      require ext_code.size(mstor13)
      call mstor13.0x42503695 with:
           gas gas_remaining wei
          args 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require 0 <= mstor15m[mstor18m[m_pricem]m.field_512m]
      munknownc1f7d04am[addr(m_token)m] = 0
      log 0xd870c66b: 0, block.timestamp, _token
  else:
      require 2^(ext_call.return_data[0] - munknowncad1dc41m[m_pricem]m.field_768) * munknowncad1dc41m[m_pricem]m.field_256 / munknowncad1dc41m[m_pricem]m.field_256 == 2^(ext_call.return_data[0] - munknowncad1dc41m[m_pricem]m.field_768)
      require m_price < munknowncad1dc41m.length
      munknowncad1dc41m[m_pricem]m.field_0 = 0
      munknowncad1dc41m[m_pricem]m.field_256 = 0
      munknowncad1dc41m[m_pricem]m.field_512 = 0
      munknowncad1dc41m[m_pricem]m.field_768 = 0
      require ext_code.size(mstor13)
      call mstor13.0x42503695 with:
           gas gas_remaining wei
          args 0, 0, 2^(ext_call.return_data[0] - munknowncad1dc41m[m_pricem]m.field_768) * munknowncad1dc41m[m_pricem]m.field_256, 0, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require 2^(ext_call.return_data[0] - munknowncad1dc41m[m_pricem]m.field_768) * munknowncad1dc41m[m_pricem]m.field_256 <= mstor15m[mstor18m[m_pricem]m.field_512m]
      mstor15m[mstor18m[m_pricem]m.field_512m] += -1 * 2^(ext_call.return_data[0] - munknowncad1dc41m[m_pricem]m.field_768) * munknowncad1dc41m[m_pricem]m.field_256
      munknownc1f7d04am[addr(m_token)m] = 0
      log 0xd870c66b: 2^(ext_call.return_data[0] - unknowncad1dc41[_price].field_768) * unknowncad1dc41[_price].field_256, block.timestamp, _token


# hash = 0x67d04e21
# getter = None
# const = None
# payable = False
def unknown67d04e21(): # not payable
  if not mstor24m.length:
      mem[(32 * mstor24m.length) + 128] = 32
      mem[(32 * mstor24m.length) + 160] = mstor24m.length
      mem[(32 * mstor24m.length) + 192 len floor32(mstor24m.length)] = mem[128 len floor32(mstor24m.length)]
      return memory
        from (32 * mstor24m.length) + 128
         [93mlen (96 * mstor24m.length) + 64
  mem[128] = uint256(mstor24m.field_0)
  [94midx = 128
  [94ms = 0
  mwhile (32 * mstor24m.length) + 96 > [94midxm:
      mem[[94midx + 32] = mstor24m[[94msm]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mstor24m.length) + 192 len floor32(mstor24m.length)] = mem[128 len floor32(mstor24m.length)]
  return Array(len=mstor24m.length, data=mem[128 len floor32(mstor24m.length)], mem[(32 * mstor24m.length) + floor32(mstor24m.length) + 192 len (32 * mstor24m.length) - floor32(mstor24m.length)]), 


# hash = 0x68231acc
# getter = ['storage', 256, 0, 22]
# const = None
# payable = False
def unknown68231acc(): # not payable
  return munknown68231acc


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  if mowner != caller:
      revert with 0, 'Only Owner Can Do This'
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x7726e5aa
# getter = None
# const = ['return', 50000000000000000]
# payable = False
const unknown7726e5aa = 5 * 10^16


# hash = 0x83fbce3f
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def unknown83fbce3f(): # not payable
  return munknown83fbce3fAddress


# hash = 0x8cc401d5
# getter = None
# const = None
# payable = False
def unknown8cc401d5(): # not payable
  if addr(mstor1m.length) != caller:
      revert with 0, 'Only Developer Can Do This'
  addr(mstor1m.length) = 0


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x9bbee240
# getter = None
# const = None
# payable = False
def unknown9bbee240(addr m_param1): # not payable
  require calldata.size - 4 >= 32
  if addr(mstor1m.length) != caller:
      revert with 0, 'Only Developer Can Do This'
  if not m_param1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  35,
                  0x724e657720446576656c6f706572277320416464726573732069732052657175697265,
                  mem[199 len 29]
  addr(mstor1m.length) = m_param1


# hash = 0xac78b896
# getter = None
# const = ['return', 10000]
# payable = False
const unknownac78b896 = 10000


# hash = 0xb696ff26
# getter = None
# const = None
# payable = False
def unknownb696ff26(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require caller == munknown83fbce3fAddress
  require m_param1 <= mstor2
  mstor2 -= m_param1


# hash = 0xc02e604e
# getter = ['storage', 256, 0, ['add', 1, ['sha3', ['data', ['cd', 4], 16]]]]
# const = None
# payable = False
def unknownc02e604e(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  return munknownc02e604em[m_param1m]m.field_256


# hash = 0xc1f7d04a
# getter = ['storage', 256, 0, ['sha3', ['data', 'caller', 17]]]
# const = None
# payable = False
def unknownc1f7d04a(): # not payable
  return munknownc1f7d04am[callerm]


# hash = 0xc450a2d8
# getter = None
# const = None
# payable = False
def unknownc450a2d8(): # not payable
  mem[320 len 224] = code.data[13341 len 224]
  [94midx = 0
  mwhile [94midx < 7m:
      require [94midx < 7
      if mstor6m[[94midxm] != 10^17:
          mem[(32 * [94midx) + 320] = mstor15m[mstor6m[[94midxm]m] + mem[(32 * [94midx) + 320]
          mem[0] = mstor6m[[94midxm]
          mem[32] = 19
          mem[(32 * [94midx) + 320] = mstor19m[mstor6m[[94midxm]m] + mem[(32 * [94midx) + 320]
      else:
          mem[(32 * [94midx) + 320] = mstor648E + mem[(32 * [94midx) + 320]
          mem[32] = 19
          mem[0] = 5 * 10^16
          mem[(32 * [94midx) + 320] = mstorFE92 + mem[(32 * [94midx) + 320]
          mem[(32 * [94midx) + 320] = mem[(32 * [94midx) + 320] / 2
      [94midx = [94midx + 1
      mcontinue 
  return memory
    from 320
     [93mlen 224


# hash = 0xca4b208b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def developer(): # not payable
  return addr(mstor1m.length)


# hash = 0xcad1dc41
# getter = ['struct', ['loc', 18]]
# const = None
# payable = False
def unknowncad1dc41(uint256 m_param1): # not payable
  require calldata.size - 4 >= 32
  require m_param1 < munknowncad1dc41m.length
  return munknowncad1dc41m[m_param1m]m.field_0, munknowncad1dc41m[m_param1m]m.field_256, munknowncad1dc41m[m_param1m]m.field_512


# hash = 0xcd11731d
# getter = None
# const = None
# payable = False
def setPlayerBookAddress(address m_newPlayerBookAddress): # not payable
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 'Only Owner Can Do This'
  munknown83fbce3fAddress = m_newPlayerBookAddress
  mstor13 = m_newPlayerBookAddress


# hash = 0xd78caf74
# getter = None
# const = None
# payable = False
def unknownd78caf74(): # not payable
  [94midx = 352
  [94ms = 7
  mwhile 544 > [94midx + 32m:
      mem[[94midx + 32] = uint256(mstor1m[[94msm])
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return mstor6m.length, mstor7, mem[384 len 160]


# hash = 0xe6b74a95
# getter = None
# const = None
# payable = False
def unknowne6b74a95(addr m_param1, uint256 m_param2, uint256 m_param3): # not payable
  require calldata.size - 4 >= 96
  require caller == munknown83fbce3fAddress
  if munknownf247466b:
      revert with 0, 'isFleshUp'
  if m_param3 == mstor3:
      revert with 0, 'out of range'
  if m_param3 < mstor6m.length:
      revert with 0, 'out of range'
  if m_param3 > mstor12:
      if m_param3 != 10^17:
          revert with 0, 'out of range'
  if 275 * 10^11 * 3600 <= mstor3:
      if m_param3 != 10^17:
          revert with 0, '0.099 only allowed 0.1 eth'
  else:
      if m_param3 > 275 * 10^11 * 3600:
          revert with 0, 'out of range'
      if 275 * 10^11 * 3600 <= mstor3:
          if m_param3 != 10^17:
              revert with 0, '0.099 only allowed 0.1 eth'
  require mstor19m[m_param3m] + mstor15m[m_param3m] >= mstor15m[m_param3m]
  require m_param2 >= 0
  if not m_param2 + mstor19m[m_param3m] + mstor15m[m_param3m]:
      if 0 > mstor2:
          revert with 0, 'no more than 2% total fishAmount'
  else:
      require (50 * m_param2) + (50 * mstor19m[m_param3m]) + (50 * mstor15m[m_param3m]) / m_param2 + mstor19m[m_param3m] + mstor15m[m_param3m] == 50
      if (50 * m_param2) + (50 * mstor19m[m_param3m]) + (50 * mstor15m[m_param3m]) > mstor2:
          revert with 0, 'no more than 2% total fishAmount'
  if 275 * 10^11 * 3600 == mstor3:
      require mstorFE92 + mstor648E >= mstor648E
      require m_param2 >= 0
      if not m_param2 + mstorFE92 + mstor648E:
          if 0 > mstor2:
              revert with 0, 'no more than 2% total fishAmount'
      else:
          require (25 * m_param2) + (25 * mstorFE92) + (25 * mstor648E) / m_param2 + mstorFE92 + mstor648E == 25
          if (25 * m_param2) + (25 * mstorFE92) + (25 * mstor648E) > mstor2:
              revert with 0, 'no more than 2% total fishAmount'
  if m_param2 <= 0:
      revert with 0, 'no zero fish'
  if m_param3 % 10^15:
      revert with 0, 'illegal price'
  if munknowncad1dc41m.length:
      require munknownc1f7d04am[addr(m_param1)m] < munknowncad1dc41m.length
      if munknowncad1dc41m[mstor17m[addr(m_param1)m]m]m.field_0 == m_param1:
          revert with 0, 'already exist'
  require ext_code.size(mstor13)
  call mstor13.0x4eba76d9 with:
       gas gas_remaining wei
      args addr(m_param1), m_param2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if m_param3 != 10^17:
      require ext_code.size(mstor13)
      static call mstor13.0xe52895b1 with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      munknowncad1dc41m.length++
      munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_0 = m_param1
      munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_256 = m_param2
      munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_512 = m_param3
      munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_768 = ext_call.return_data[0]
      require m_param2 + mstor15m[m_param3m] >= mstor15m[m_param3m]
      mstor15m[m_param3m] += m_param2
      munknownc1f7d04am[addr(m_param1)m] = munknowncad1dc41m.length
      munknownc02e604em[m_param3m]m.field_0++
      munknownc02e604em[m_param3m]m[munknownc02e604em[m_param3m]m.field_0m]m.field_0 = munknowncad1dc41m.length
      log 0xd870c66b: _param2, block.timestamp, _param1
  else:
      if not m_param2:
          require ext_code.size(mstor13)
          static call mstor13.0xe52895b1 with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] + 1 >= ext_call.return_data[0]
          munknowncad1dc41m.length++
          munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_0 = m_param1
          munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_256 = 0
          munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_512 = 5 * 10^16
          munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_768 = ext_call.return_data[0] + 1
          require mstor15m[5 * 10^16m] >= mstor15m[5 * 10^16m]
          munknownc1f7d04am[addr(m_param1)m] = munknowncad1dc41m.length
          munknownc02e604em[5 * 10^16m]m.field_0++
          munknownc02e604em[5 * 10^16m]m[munknownc02e604em[5 * 10^16m]m.field_0m]m.field_0 = munknowncad1dc41m.length
          log 0xd870c66b: 0, block.timestamp, _param1
      else:
          require 2 * m_param2 / m_param2 == 2
          require ext_code.size(mstor13)
          static call mstor13.0xe52895b1 with:
                  gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] + 1 >= ext_call.return_data[0]
          munknowncad1dc41m.length++
          munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_0 = m_param1
          munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_256 = 0
          munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_257 = uint255(m_param2)
          munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_512 = 5 * 10^16
          munknowncad1dc41m[munknowncad1dc41m.lengthm]m.field_768 = ext_call.return_data[0] + 1
          require (2 * m_param2) + mstor15m[5 * 10^16m] >= mstor15m[5 * 10^16m]
          mstor15m[5 * 10^16m] += 2 * m_param2
          munknownc1f7d04am[addr(m_param1)m] = munknowncad1dc41m.length
          munknownc02e604em[5 * 10^16m]m.field_0++
          munknownc02e604em[5 * 10^16m]m[munknownc02e604em[5 * 10^16m]m.field_0m]m.field_0 = munknowncad1dc41m.length
          log 0xd870c66b: 2 * _param2, block.timestamp, _param1


# hash = 0xec8732a6
# getter = ['storage', 256, 0, 4]
# const = None
# payable = False
def unknownec8732a6(): # not payable
  return munknownec8732a6


# hash = 0xf048ff8e
# getter = None
# const = None
# payable = False
def unknownf048ff8e(): # not payable
  return mstor2, mstor3, mstor5


# hash = 0xf247466b
# getter = ['bool', ['storage', 8, 0, 21]]
# const = None
# payable = False
def unknownf247466b(): # not payable
  return bool(munknownf247466b)


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 'Only Owner Can Do This'
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
  call munknown83fbce3fAddress with:
     value call.value wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


