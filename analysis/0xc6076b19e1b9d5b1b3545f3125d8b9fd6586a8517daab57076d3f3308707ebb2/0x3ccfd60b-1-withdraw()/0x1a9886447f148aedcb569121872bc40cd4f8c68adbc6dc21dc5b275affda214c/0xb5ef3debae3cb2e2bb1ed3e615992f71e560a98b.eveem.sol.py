# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xb5ef3DEBae3cb2E2BB1ED3e615992f71E560a98B 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 4
    owner # mask: a s
    # storage address 5
    feeMode # mask: a s
    # storage address 5
    MOTAddress # mask: a s
    # storage address 6
    feePercentage # mask: a s
    # storage address 7
    feeAmount # mask: a s
    # storage address 8
    stor8 # mask: a s
    # storage address 9
    name
    # storage address 10
    description
    # storage address 11
    category
    # storage address 12
    version
    # storage address 13
    unknownb4b8de74 # mask: a s
    # storage address 14
    unknown1a5911d7 # mask: a s
    # storage address 15
    stor15 # mask: a s
    # storage address 16
    stor16 # mask: a s
    # storage address 17
    unknown12e89062
    # storage address 18
    unknown0fe8a48e
    # storage address 19
    unknowne00ff4e3
    # storage address 20
    stor20
    # storage address 21
    unknownb393e88e
    # storage address 22
    stor22
    # storage address 23
    stor23 # mask: a s
# hash = 0x061d7db7
# getter = None
# const = None
# payable = False
def adjustFeeMode(uint8 m_newMode): # not payable
  require caller == mowner
  require m_newMode <= 1
  mfeeMode = m_newMode
  return 1


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 9]]]], ['loc', 9]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x0fe8a48e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 18]]]]]]]
# const = None
# payable = False
def unknown0fe8a48e(uint256 m_param1, addr m_param2, addr m_param3): # not payable
  return munknown0fe8a48em[m_param1m]m[m_param2m]m[m_param3m]


# hash = 0x12e89062
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 17]]]]]]]
# const = None
# payable = False
def unknown12e89062(uint256 m_param1, addr m_param2, addr m_param3): # not payable
  return munknown12e89062m[m_param1m]m[m_param2m]m[m_param3m]


# hash = 0x15cdc529
# getter = None
# const = None
# payable = True
def unknown15cdc529() payable: 
  munknown1a5911d7 = 0
  if m('cd', 36).length != m('cd', 4).length:
      revert with 0, 'Arrays are not the same lengths'
  if m('cd', 68).length != m('cd', 36).length:
      revert with 0, 'Arrays are not the same lengths'
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      require [94midx < m('cd', 36).length
      if cd[((32 * [94midx) + cd[36] + 36)] != 0:
          if cd[132]:
              mem[100] = cd[132]
              require ext_code.size(mstor23)
              call mstor23.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args cd[132]
          else:
              require [94midx < m('cd', 4).length
              require [94midx < m('cd', 36).length
              require [94midx < m('cd', 68).length
              mem[132] = cd[((32 * [94midx) + cd[36] + 36)]
              mem[164] = cd[((32 * [94midx) + cd[68] + 36)]
              mem[196] = 1
              require ext_code.size(mstor23)
              call mstor23.pickExchange(address token, uint256 amount, uint256 rate, bool isBuying) with:
                   gas gas_remaining wei
                  args addr(cd[((32 * [94midx) + cd[4] + 36)]), cd[((32 * [94midx) + cd[36] + 36)], cd[((32 * [94midx) + cd[68] + 36)], 1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[100] = ext_call.return_data[0]
              require ext_code.size(mstor23)
              call mstor23.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require [94midx < m('cd', 36).length
          if not addr(ext_call.return_data[0]):
              munknown1a5911d7 += cd[((32 * [94midx) + cd[36] + 36)]
              require [94midx < m('cd', 4).length
              require [94midx < m('cd', 36).length
              mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
              require munknownb4b8de74 + mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] >= mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]
              if munknownb4b8de74 + mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] < block.timestamp:
                  if not munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]:
                      mstor20m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = block.timestamp
                  munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]++
                  mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                  mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = block.timestamp
              mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              call caller with:
                 value cd[((32 * [94midx) + cd[36] + 36)] wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              require [94midx < m('cd', 4).length
              require [94midx < m('cd', 36).length
              require [94midx < m('cd', 68).length
              mem[96] = Mask(32, 224, sha3('buyToken(address,uint256,uint256', ',address)'))
              mem[100] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              mem[132] = cd[((32 * [94midx) + cd[36] + 36)]
              mem[164] = cd[((32 * [94midx) + cd[68] + 36)]
              mem[196] = addr(cd[100])
              call addr(ext_call.return_data[0]) with:
                 funct Mask(32, 224, sha3('buyToken(address,uint256,uint256', ',address)')) >> 224
                 value cd[((32 * [94midx) + cd[36] + 36)] wei
                   gas gas_remaining wei
                  args addr(cd[((32 * [94midx) + cd[4] + 36)]), cd[((32 * [94midx) + cd[36] + 36)], cd[((32 * [94midx) + cd[68] + 36)], addr(cd[100])
              if ext_call.success:
                  require [94midx < m('cd', 4).length
                  mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                  mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 20))
                  if mstor20m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]:
                      mstor20m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = 0
                      munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = 0
                      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                      mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                      mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = 0
              else:
                  require [94midx < m('cd', 36).length
                  munknown1a5911d7 += cd[((32 * [94midx) + cd[36] + 36)]
                  require [94midx < m('cd', 4).length
                  require [94midx < m('cd', 36).length
                  mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                  require munknownb4b8de74 + mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] >= mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]
                  if munknownb4b8de74 + mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] < block.timestamp:
                      if not munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]:
                          mstor20m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = block.timestamp
                      munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]++
                      mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                      mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m] = block.timestamp
                  mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                  call caller with:
                     value cd[((32 * [94midx) + cd[36] + 36)] wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      mcontinue 
  require ext_code.size(mstor23)
  call mstor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mMOTAddress, 10^18, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not call.value - munknown1a5911d7:
      require mfeeMode <= 1
      require mfeeMode <= 1
      if mfeeMode:
          if mfeeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if mfeeAmount > 0:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeeAmount
              require ext_code.size(mMOTAddress)
              call mMOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeeAmount
      if mfeeMode:
          require mfeeMode <= 1
          if mfeeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if mfeeAmount:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mstor8, mfeeAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
  else:
      require (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / call.value - munknown1a5911d7 == ext_call.return_data[0]
      require mfeeMode <= 1
      if mfeeMode:
          require mfeeMode <= 1
          if mfeeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if mfeeAmount > 0:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeeAmount
              require ext_code.size(mMOTAddress)
              call mMOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeeAmount
      else:
          if (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18:
              require mfeePercentage * (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18 / (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18 == mfeePercentage
              if mfeePercentage * (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18 / 10000 > 0:
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.balanceOf(address owner) with:
                       gas gas_remaining wei
                      args caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= mfeePercentage * (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18 / 10000
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.allowance(address owner, address spender) with:
                       gas gas_remaining wei
                      args caller, this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= mfeePercentage * (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18 / 10000
      require mfeeMode <= 1
      if mfeeMode:
          require mfeeMode <= 1
          if mfeeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if mfeeAmount:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mstor8, mfeeAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
      else:
          if (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18:
              require mfeePercentage * (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18 / (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18 == mfeePercentage
              if mfeePercentage * (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18 / 10000:
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, mstor8, mfeePercentage * (call.value * ext_call.return_data[0]) - (munknown1a5911d7 * ext_call.return_data[0]) / 10^18 / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0]
  return 1


# hash = 0x1a5911d7
# getter = ['storage', 256, 0, 14]
# const = None
# payable = False
def unknown1a5911d7(): # not payable
  return munknown1a5911d7


# hash = 0x1ddfd7db
# getter = None
# const = None
# payable = False
def supportsTradingPair(address m_srcAddress, address m_destAddress, bytes32 m_exchangeId): # not payable
  require ext_code.size(mstor23)
  call mstor23.supportsTradingPair(address srcAddress, address destAddress, bytes32 exchangeId) with:
       gas gas_remaining wei
      args addr(m_srcAddress), addr(m_destAddress), m_exchangeId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return bool(ext_call.return_data[0])


# hash = 0x280dd460
# getter = None
# const = None
# payable = False
def adjustFeePercentage(uint256 m_newPercentage): # not payable
  require caller == mowner
  require m_newPercentage <= 10000
  mfeePercentage = m_newPercentage
  return 1


# hash = 0x42bff0d0
# getter = None
# const = None
# payable = False
def setExchangeAdapterManager(address m_exchangeAdapterManager): # not payable
  require caller == mowner
  mstor23 = m_exchangeAdapterManager


# hash = 0x46479541
# getter = None
# const = None
# payable = False
def setWalletId(address m_newWallet): # not payable
  require caller == mowner
  require m_newWallet
  mstor8 = m_newWallet
  return 1


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 12]]]], ['loc', 12]]]
# const = None
# payable = False
def version(): # not payable
  return mversionm[0 len mversionm.lengthm]


# hash = 0x5fc6b623
# getter = None
# const = None
# payable = False
def getPrice(address m_sourceAddress, address m_destAddress, uint256 m_amount, bytes32 m_exchangeId): # not payable
  require ext_code.size(mstor23)
  call mstor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0, 0, addr(m_destAddress), m_amount, m_exchangeId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[0], ext_call.return_data[32]


# hash = 0x674f23ba
# getter = None
# const = None
# payable = False
def unknown674f23ba(array m_param1): # not payable
  mem[128 len 32 * m_param1.length] = call.data[m_param1 + 36 len 32 * m_param1.length]
  mem[(32 * m_param1.length) + 128] = m_param1.length
  if m_param1.length:
      mem[(32 * m_param1.length) + 160 len 32 * m_param1.length] = code.data[12923 len 32 * m_param1.length]
  [94midx = 0
  mwhile [94midx < m_param1.lengthm:
      require [94midx < m_param1.length
      require [94midx < m_param1.length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, sha3(caller, 21))
      require [94midx < m_param1.length
      mem[(32 * m_param1.length) + (32 * [94midx) + 160] = munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeem]m[mem[(32 * [94midx) + 140 len 20]m] + munknownb393e88em[callerm]m[mem[(32 * [94midx) + 140 len 20]m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeem]
      [94midx = [94midx + 1
      mcontinue 
  mem[(64 * m_param1.length) + 160] = 32
  mem[(64 * m_param1.length) + 192] = m_param1.length
  mem[(64 * m_param1.length) + 224 len floor32(m_param1.length)] = mem[(32 * m_param1.length) + 160 len floor32(m_param1.length)]
  return memory
    from (64 * m_param1.length) + 160
     [93mlen (161 * m_param1.length) + 64


# hash = 0x69e15404
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def feeAmount(): # not payable
  return mfeeAmount


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == mowner
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x7284e416
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 10]]]], ['loc', 10]]]
# const = None
# payable = False
def description(): # not payable
  return mdescriptionm[0 len mdescriptionm.lengthm]


# hash = 0x78265e2f
# getter = None
# const = None
# payable = False
def unknown78265e2f(): # not payable
  mstor15 = 0
  mstor16 = 1
  if m('cd', 36).length != m('cd', 4).length:
      revert with 0, 'Arrays are not the same lengths'
  if m('cd', 68).length != m('cd', 36).length:
      revert with 0, 'Arrays are not the same lengths'
  [94midx = 0
  mwhile [94midx < m('cd', 4).lengthm:
      require [94midx < m('cd', 36).length
      if cd[((32 * [94midx) + cd[36] + 36)] != 0:
          if cd[132]:
              mem[100] = cd[132]
              require ext_code.size(mstor23)
              call mstor23.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args cd[132]
          else:
              require [94midx < m('cd', 4).length
              require [94midx < m('cd', 36).length
              require [94midx < m('cd', 68).length
              mem[132] = cd[((32 * [94midx) + cd[36] + 36)]
              mem[164] = cd[((32 * [94midx) + cd[68] + 36)]
              mem[196] = 1
              require ext_code.size(mstor23)
              call mstor23.pickExchange(address token, uint256 amount, uint256 rate, bool isBuying) with:
                   gas gas_remaining wei
                  args addr(cd[((32 * [94midx) + cd[4] + 36)]), cd[((32 * [94midx) + cd[36] + 36)], cd[((32 * [94midx) + cd[68] + 36)], 1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[100] = ext_call.return_data[0]
              require ext_code.size(mstor23)
              call mstor23.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not addr(ext_call.return_data[0]):
              mstor16 = 0
              require [94midx < m('cd', 4).length
              require [94midx < m('cd', 36).length
              mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
              require munknownb4b8de74 + mstor22m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] >= mstor22m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]
              if munknownb4b8de74 + mstor22m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] < block.timestamp:
                  if not munknownb393e88em[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]:
                      mstor20m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = block.timestamp
                  munknownb393e88em[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]++
                  mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                  mstor22m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = block.timestamp
              mem[0] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(cd[((32 * [94midx) + cd[4] + 36)]):
                  call caller with:
                     value cd[((32 * [94midx) + cd[36] + 36)] wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
          else:
              require [94midx < m('cd', 36).length
              require [94midx < m('cd', 4).length
              require ext_code.size(addr(cd[((32 * [94midx) + cd[4] + 36)]))
              call addr(cd[((32 * [94midx) + cd[4] + 36)]).allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] < cd[((32 * [94midx) + cd[36] + 36)]:
                  revert with 0, 'Not enough tokens approved'
              require [94midx < m('cd', 4).length
              require [94midx < m('cd', 36).length
              require ext_code.size(addr(cd[((32 * [94midx) + cd[4] + 36)]))
              call addr(cd[((32 * [94midx) + cd[4] + 36)]).transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, addr(ext_call.return_data[0]), cd[((32 * [94midx) + cd[36] + 36)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require [94midx < m('cd', 4).length
              require ext_code.size(addr(cd[((32 * [94midx) + cd[4] + 36)]))
              call addr(cd[((32 * [94midx) + cd[4] + 36)]).allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data[0]), this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require [94midx < m('cd', 4).length
              if not ext_call.return_data[0]:
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x80b2edd8 with:
                       gas gas_remaining wei
                      args addr(cd[((32 * [94midx) + cd[4] + 36)])
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              require [94midx < m('cd', 36).length
              require [94midx < m('cd', 68).length
              mem[96] = Mask(32, 224, sha3('sellToken(address,uint256,uint25', '6,address)'))
              mem[100] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              mem[132] = cd[((32 * [94midx) + cd[36] + 36)]
              mem[164] = cd[((32 * [94midx) + cd[68] + 36)]
              mem[196] = addr(cd[100])
              call addr(ext_call.return_data[0]) with:
                 funct Mask(32, 224, sha3('sellToken(address,uint256,uint25', '6,address)')) >> 224
                   gas gas_remaining wei
                  args addr(cd[((32 * [94midx) + cd[4] + 36)]), cd[((32 * [94midx) + cd[36] + 36)], cd[((32 * [94midx) + cd[68] + 36)], addr(cd[100])
              if not ext_call.success:
                  mstor16 = 0
                  require [94midx < m('cd', 4).length
                  require [94midx < m('cd', 36).length
                  mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                  require munknownb4b8de74 + mstor22m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] >= mstor22m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]
                  if munknownb4b8de74 + mstor22m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] < block.timestamp:
                      if not munknownb393e88em[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]:
                          mstor20m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = block.timestamp
                      munknownb393e88em[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]++
                      mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                      mstor22m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = block.timestamp
                  mem[0] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(cd[((32 * [94midx) + cd[4] + 36)]):
                      call caller with:
                         value cd[((32 * [94midx) + cd[36] + 36)] wei
                           gas 2300 * is_zero(value) wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                  else:
                      require ext_code.size(addr(cd[((32 * [94midx) + cd[4] + 36)]))
                      call addr(cd[((32 * [94midx) + cd[4] + 36)]).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args caller
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      mem[132] = caller
                      mem[164] = cd[((32 * [94midx) + cd[36] + 36)]
                      require ext_code.size(addr(cd[((32 * [94midx) + cd[4] + 36)]))
                      call addr(cd[((32 * [94midx) + cd[4] + 36)]).transferFrom(address from, address to, uint256 value) with:
                           gas gas_remaining wei
                          args addr(ext_call.return_data[0]), caller, cd[((32 * [94midx) + cd[36] + 36)]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require cd[((32 * [94midx) + cd[36] + 36)] + ext_call.return_data[0] >= ext_call.return_data[0]
                      mem[100] = caller
                      require ext_code.size(addr(cd[((32 * [94midx) + cd[4] + 36)]))
                      call addr(cd[((32 * [94midx) + cd[4] + 36)]).balanceOf(address owner) with:
                           gas gas_remaining wei
                          args caller
                      mem[96] = ext_call.return_data[0]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] == cd[((32 * [94midx) + cd[36] + 36)] + ext_call.return_data[0]
              else:
                  require [94midx < m('cd', 4).length
                  mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 20))
                  if mstor20m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]:
                      mstor20m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = 0
                      munknownb393e88em[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = 0
                      mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                      mstor22m[callerm]m[addr(cd[((32 * [94midx) + cd[4] + 36)])m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = 0
                  require [94midx < m('cd', 4).length
                  require [94midx < m('cd', 36).length
                  require ext_code.size(mstor23)
                  call mstor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args addr(cd[((32 * [94midx) + cd[4] + 36)]), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, cd[((32 * [94midx) + cd[36] + 36)], cd[132]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  require ext_code.size(addr(cd[((32 * [94midx) + cd[4] + 36)]))
                  call addr(cd[((32 * [94midx) + cd[4] + 36)]).decimals() with:
                       gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  mem[0] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                  mem[132] = mMOTAddress
                  mem[164] = 10^18
                  mem[196] = 0
                  require ext_code.size(mstor23)
                  call mstor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, mMOTAddress, 10^18, 0
                  mem[96 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  if not ext_call.return_data[0]:
                      require 10^ext_call.return_data[0]
                      require (0 / 10^ext_call.return_data[0] / 10^18) + mstor15 >= mstor15
                      mstor15 += 0 / 10^ext_call.return_data[0] / 10^18
                  else:
                      require cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / ext_call.return_data[0] == cd[((32 * [94midx) + cd[36] + 36)]
                      if not cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0]:
                          require 10^ext_call.return_data[0]
                          require (0 / 10^ext_call.return_data[0] / 10^18) + mstor15 >= mstor15
                          mstor15 += 0 / 10^ext_call.return_data[0] / 10^18
                      else:
                          require ext_call.return_data[0] * cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] == ext_call.return_data[0]
                          require 10^ext_call.return_data[0]
                          require (ext_call.return_data[0] * cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18) + mstor15 >= mstor15
                          mstor15 += ext_call.return_data[0] * cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18
      [94midx = [94midx + 1
      mcontinue 
  require mfeeMode <= 1
  if mfeeMode:
      require mfeeMode <= 1
      if mfeeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      if mfeeAmount > 0:
          require ext_code.size(mMOTAddress)
          call mMOTAddress.balanceOf(address owner) with:
               gas gas_remaining wei
              args caller
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] >= mfeeAmount
          require ext_code.size(mMOTAddress)
          call mMOTAddress.allowance(address owner, address spender) with:
               gas gas_remaining wei
              args caller, this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] >= mfeeAmount
  else:
      if mstor15:
          require mfeePercentage * mstor15 / mstor15 == mfeePercentage
          if mfeePercentage * mstor15 / 10000 > 0:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeePercentage * mstor15 / 10000
              require ext_code.size(mMOTAddress)
              call mMOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeePercentage * mstor15 / 10000
  require mfeeMode <= 1
  if mfeeMode:
      require mfeeMode <= 1
      if mfeeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      if mfeeAmount:
          require ext_code.size(mMOTAddress)
          call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args caller, mstor8, mfeeAmount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
  else:
      if mstor15:
          require mfeePercentage * mstor15 / mstor15 == mfeePercentage
          if mfeePercentage * mstor15 / 10000:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mstor8, mfeePercentage * mstor15 / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
  return bool(mstor16)


# hash = 0x869f0f25
# getter = None
# const = None
# payable = False
def unknown869f0f25(addr m_param1, addr m_param2, uint256 m_param3, uint256 m_param4, uint256 m_param5): # not payable
  require ext_code.size(mstor23)
  call mstor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0, 0, addr(m_param2), m_param3, m_param4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if ext_call.return_data[0] <= 0:
      require m_param5 + munknowne00ff4e3m[m_param4m]m[addr(m_param1)m]m[addr(m_param2)m] >= munknowne00ff4e3m[m_param4m]m[addr(m_param1)m]m[addr(m_param2)m]
      if m_param5 + munknowne00ff4e3m[m_param4m]m[addr(m_param1)m]m[addr(m_param2)m] >= block.timestamp:
          return munknown12e89062m[m_param4m]m[addr(m_param1)m]m[addr(m_param2)m], munknown0fe8a48em[m_param4m]m[addr(m_param1)m]m[addr(m_param2)m], 1
      else:
          return 0
  munknown12e89062m[m_param4m]m[addr(m_param1)m]m[addr(m_param2)m] = ext_call.return_data[0]
  munknown0fe8a48em[m_param4m]m[addr(m_param1)m]m[addr(m_param2)m] = ext_call.return_data[32]
  munknowne00ff4e3m[m_param4m]m[addr(m_param1)m]m[addr(m_param2)m] = block.timestamp
  return ext_call.return_data[0], ext_call.return_data[32], 0


# hash = 0x8955053f
# getter = None
# const = None
# payable = False
def unknown8955053f(addr m_param1, uint256 m_param2, uint256 m_param3, addr m_param4, uint256 m_param5): # not payable
  require ext_code.size(m_param1)
  call m_param1.allowance(address owner, address spender) with:
       gas gas_remaining wei
      args caller, this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < m_param2:
      revert with 0, 'Not enough tokens approved'
  if m_param5:
      if not m_param5:
          require munknownb4b8de74 + mstor22m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] >= mstor22m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]
          if munknownb4b8de74 + mstor22m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] < block.timestamp:
              if not munknownb393e88em[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]:
                  mstor20m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = block.timestamp
              munknownb393e88em[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]++
              mstor22m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = block.timestamp
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == m_param1:
              call caller with:
                 value m_param2 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  return 0
          else:
              return 0
      require ext_code.size(mstor23)
      call mstor23.getExchangeAdapter(bytes32 id) with:
           gas gas_remaining wei
          args m_param5
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(m_param1)
      call m_param1.allowance(address owner, address spender) with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x80b2edd8 with:
               gas gas_remaining wei
              args m_param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      require ext_code.size(m_param1)
      call m_param1.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args caller, addr(ext_call.return_data[0]), m_param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      call addr(ext_call.return_data[0]) with:
         funct Mask(32, 224, sha3('sellToken(address,uint256,uint25', '6,address)')) >> 224
           gas gas_remaining wei
          args addr(m_param1), m_param2, m_param3, m_param4
      require ext_code.size(mstor23)
      call mstor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0, 0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, m_param2, m_param5
  else:
      require ext_code.size(mstor23)
      call mstor23.pickExchange(address token, uint256 amount, uint256 rate, bool isBuying) with:
           gas gas_remaining wei
          args 0, 0, m_param2, m_param3, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require munknownb4b8de74 + mstor22m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] >= mstor22m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]
          if munknownb4b8de74 + mstor22m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] < block.timestamp:
              if not munknownb393e88em[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]:
                  mstor20m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = block.timestamp
              munknownb393e88em[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]++
              mstor22m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = block.timestamp
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == m_param1:
              call caller with:
                 value m_param2 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  return 0
          else:
              return 0
      require ext_code.size(mstor23)
      call mstor23.getExchangeAdapter(bytes32 id) with:
           gas gas_remaining wei
          args ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(m_param1)
      call m_param1.allowance(address owner, address spender) with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x80b2edd8 with:
               gas gas_remaining wei
              args m_param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      require ext_code.size(m_param1)
      call m_param1.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args caller, addr(ext_call.return_data[0]), m_param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      call addr(ext_call.return_data[0]) with:
         funct Mask(32, 224, sha3('sellToken(address,uint256,uint25', '6,address)')) >> 224
           gas gas_remaining wei
          args addr(m_param1), m_param2, m_param3, m_param4
      require ext_code.size(mstor23)
      call mstor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0, 0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, m_param2, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_code.size(m_param1)
  call m_param1.decimals() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(mstor23)
  call mstor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0, 4008636142, mMOTAddress, 10^18, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not ext_call.return_data[0]:
      require 10^ext_call.return_data[0]
      require mfeeMode <= 1
      if mfeeMode:
          require mfeeMode <= 1
          if mfeeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if mfeeAmount > 0:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeeAmount
              require ext_code.size(mMOTAddress)
              call mMOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeeAmount
      else:
          if 0 / 10^ext_call.return_data[0] / 10^18:
              require mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 0 / 10^ext_call.return_data[0] / 10^18 == mfeePercentage
              if mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000 > 0:
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.balanceOf(address owner) with:
                       gas gas_remaining wei
                      args caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.allowance(address owner, address spender) with:
                       gas gas_remaining wei
                      args caller, this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
      require mfeeMode <= 1
      if mfeeMode:
          require mfeeMode <= 1
          if mfeeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if mfeeAmount:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mstor8, mfeeAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
      else:
          if 0 / 10^ext_call.return_data[0] / 10^18:
              require mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 0 / 10^ext_call.return_data[0] / 10^18 == mfeePercentage
              if mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000:
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, mstor8, mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0]
  else:
      require m_param2 * ext_call.return_data[0] / ext_call.return_data[0] == m_param2
      if not m_param2 * ext_call.return_data[0]:
          require 10^ext_call.return_data[0]
          require mfeeMode <= 1
          if mfeeMode:
              require mfeeMode <= 1
              if mfeeMode != 1:
                  revert with 0, 'Unsupported fee mode.'
              if mfeeAmount > 0:
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.balanceOf(address owner) with:
                       gas gas_remaining wei
                      args caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= mfeeAmount
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.allowance(address owner, address spender) with:
                       gas gas_remaining wei
                      args caller, this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= mfeeAmount
          else:
              if 0 / 10^ext_call.return_data[0] / 10^18:
                  require mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 0 / 10^ext_call.return_data[0] / 10^18 == mfeePercentage
                  if mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000 > 0:
                      require ext_code.size(mMOTAddress)
                      call mMOTAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args caller
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] >= mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
                      require ext_code.size(mMOTAddress)
                      call mMOTAddress.allowance(address owner, address spender) with:
                           gas gas_remaining wei
                          args caller, this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] >= mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
          require mfeeMode <= 1
          if mfeeMode:
              require mfeeMode <= 1
              if mfeeMode != 1:
                  revert with 0, 'Unsupported fee mode.'
              if mfeeAmount:
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, mstor8, mfeeAmount
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0]
          else:
              if 0 / 10^ext_call.return_data[0] / 10^18:
                  require mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 0 / 10^ext_call.return_data[0] / 10^18 == mfeePercentage
                  if mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000:
                      require ext_code.size(mMOTAddress)
                      call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, mstor8, mfeePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0]
      else:
          require ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / m_param2 * ext_call.return_data[0] == ext_call.return_data[0]
          require 10^ext_call.return_data[0]
          require mfeeMode <= 1
          if mfeeMode:
              require mfeeMode <= 1
              if mfeeMode != 1:
                  revert with 0, 'Unsupported fee mode.'
              if mfeeAmount > 0:
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.balanceOf(address owner) with:
                       gas gas_remaining wei
                      args caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= mfeeAmount
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.allowance(address owner, address spender) with:
                       gas gas_remaining wei
                      args caller, this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= mfeeAmount
          else:
              if ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18:
                  require mfeePercentage * ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 == mfeePercentage
                  if mfeePercentage * ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000 > 0:
                      require ext_code.size(mMOTAddress)
                      call mMOTAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args caller
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] >= mfeePercentage * ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000
                      require ext_code.size(mMOTAddress)
                      call mMOTAddress.allowance(address owner, address spender) with:
                           gas gas_remaining wei
                          args caller, this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] >= mfeePercentage * ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000
          require mfeeMode <= 1
          if mfeeMode:
              require mfeeMode <= 1
              if mfeeMode != 1:
                  revert with 0, 'Unsupported fee mode.'
              if mfeeAmount:
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, mstor8, mfeeAmount
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0]
          else:
              if ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18:
                  require mfeePercentage * ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 == mfeePercentage
                  if mfeePercentage * ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000:
                      require ext_code.size(mMOTAddress)
                      call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, mstor8, mfeePercentage * ext_call.return_data[0] * m_param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0]
  if mstor20m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]:
      mstor20m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = 0
      munknownb393e88em[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = 0
      mstor22m[callerm]m[addr(m_param1)m]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m] = 0
  return 1


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x977919bf
# getter = None
# const = None
# payable = False
def adjustFeeAmount(uint256 m_newAmount): # not payable
  require caller == mowner
  mfeeAmount = m_newAmount
  return 1


# hash = 0x99a5d747
# getter = None
# const = None
# payable = False
def calculateFee(uint256 m_value): # not payable
  require mfeeMode <= 1
  if mfeeMode:
      require mfeeMode <= 1
      if mfeeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      return mfeeAmount
  if not m_value:
      return 0
  require mfeePercentage * m_value / m_value == mfeePercentage
  return (mfeePercentage * m_value / 10000)


# hash = 0xa001ecdd
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def feePercentage(): # not payable
  return mfeePercentage


# hash = 0xb188c70d
# getter = ['storage', 8, 160, 5]
# const = None
# payable = False
def feeMode(): # not payable
  require mfeeMode <= 1
  return mfeeMode


# hash = 0xb393e88e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], ['sha3', ['data', 5328391386102250222617600952611448509162254062, ['sha3', ['data', 'caller', 21]]]]]]]
# const = None
# payable = False
def unknownb393e88e(addr m_param1): # not payable
  return munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeem]m[addr(m_param1)m]


# hash = 0xb4b8de74
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknownb4b8de74(): # not payable
  return munknownb4b8de74


# hash = 0xc55c4115
# getter = None
# const = ['return', 10000]
# payable = False
const FEE_CHARGER_DENOMINATOR = 10000


# hash = 0xc642f094
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def MOT(): # not payable
  return mMOTAddress


# hash = 0xc892693b
# getter = None
# const = None
# payable = False
def setMotAddress(address m_motAddress): # not payable
  require caller == mowner
  require m_motAddress
  require mMOTAddress != m_motAddress
  mMOTAddress = m_motAddress
  mem[128] = 'MOT'
  mem[96] = 3
  mem[131 len 0] = None
  mem[131] = Mask(208, 0, 'MOT'), mem[160 len 3]
  [94m_31 = sha3(mem[131 len 3])
  mem[131] = 0x95d89b4100000000000000000000000000000000000000000000000000000000
  require ext_code.size(mMOTAddress)
  call mMOTAddress.symbol() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[131 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 131
  require return_data.size >= 32
  require mem[131] <= 4294967296
  require mem[131] + 32 <= return_data.size
  require return_data.size >= mem[mem[131] + 131] + mem[131] + 32 and mem[mem[131] + 131] <= 4294967296
  [94m_38 = mem[mem[131] + 131]
  mem[ceil32(return_data.size) + 163 len floor32(mem[mem[131] + 131])] = mem[mem[131] + 163 len floor32(mem[mem[131] + 131])]
  mem[ceil32(return_data.size) + floor32(mem[mem[131] + 131]) + -(mem[mem[131] + 131] % 32) + 195 len mem[mem[131] + 131] % 32] = mem[mem[131] + -(mem[mem[131] + 131] % 32) + floor32(mem[mem[131] + 131]) + 195 len mem[mem[131] + 131] % 32]
  mem[[94m_38 + ceil32(return_data.size) + 163 len floor32([94m_38)] = mem[ceil32(return_data.size) + 163 len floor32([94m_38)]
  mem[(2 * floor32([94m_38)) + ceil32(return_data.size) + 195 len [94m_38 % 32] = mem[ceil32(return_data.size) + -([94m_38 % 32) + floor32([94m_38) + 195 len [94m_38 % 32]
  require sha3(mem[[94m_38 + ceil32(return_data.size) + 163 len [94m_38]) == [94m_31
  return 1


# hash = 0xd0f07926
# getter = None
# const = None
# payable = False
def unknownd0f07926(uint256 m_param1): # not payable
  require caller == mowner
  munknownb4b8de74 = m_param1
  return 1


# hash = 0xe00ff4e3
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 19]]]]]]]
# const = None
# payable = False
def unknowne00ff4e3(uint256 m_param1, addr m_param2, addr m_param3): # not payable
  return munknowne00ff4e3m[m_param1m]m[m_param2m]m[m_param3m]


# hash = 0xeb5d3ab5
# getter = None
# const = None
# payable = True
def unknowneb5d3ab5(addr m_param1, uint256 m_param2, uint256 m_param3, addr m_param4, uint256 m_param5) payable: 
  require m_param2 == call.value
  if m_param5:
      if not m_param5:
          require munknownb4b8de74 + mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] >= mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m]
          if munknownb4b8de74 + mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] < block.timestamp:
              if not munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m]:
                  mstor20m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] = block.timestamp
              munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m]++
              mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] = block.timestamp
          call caller with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              return 0
      require ext_code.size(mstor23)
      call mstor23.getExchangeAdapter(bytes32 id) with:
           gas gas_remaining wei
          args m_param5
  else:
      require ext_code.size(mstor23)
      call mstor23.pickExchange(address token, uint256 amount, uint256 rate, bool isBuying) with:
           gas gas_remaining wei
          args 0, 0, m_param2, m_param3, 1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require munknownb4b8de74 + mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] >= mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m]
          if munknownb4b8de74 + mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] < block.timestamp:
              if not munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m]:
                  mstor20m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] = block.timestamp
              munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m]++
              mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] = block.timestamp
          call caller with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              return 0
      require ext_code.size(mstor23)
      call mstor23.getExchangeAdapter(bytes32 id) with:
           gas gas_remaining wei
          args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  call addr(ext_call.return_data[0]) with:
     funct Mask(32, 224, sha3('buyToken(address,uint256,uint256', ',address)')) >> 224
     value call.value wei
       gas gas_remaining wei
      args addr(m_param1), m_param2, m_param3, m_param4
  if not ext_call.success:
      require munknownb4b8de74 + mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] >= mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m]
      if munknownb4b8de74 + mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] < block.timestamp:
          if not munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m]:
              mstor20m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] = block.timestamp
          munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m]++
          mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] = block.timestamp
      call caller with:
         value call.value wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          return 0
  require ext_code.size(mstor23)
  call mstor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0, 4008636142, mMOTAddress, 10^18, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not call.value:
      require mfeeMode <= 1
      require mfeeMode <= 1
      if mfeeMode:
          if mfeeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if mfeeAmount > 0:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeeAmount
              require ext_code.size(mMOTAddress)
              call mMOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeeAmount
      if mfeeMode:
          require mfeeMode <= 1
          if mfeeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if mfeeAmount:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mstor8, mfeeAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
  else:
      require ext_call.return_data[0] * call.value / call.value == ext_call.return_data[0]
      require mfeeMode <= 1
      if mfeeMode:
          require mfeeMode <= 1
          if mfeeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if mfeeAmount > 0:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeeAmount
              require ext_code.size(mMOTAddress)
              call mMOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= mfeeAmount
      else:
          if ext_call.return_data[0] * call.value / 10^18:
              require mfeePercentage * ext_call.return_data[0] * call.value / 10^18 / ext_call.return_data[0] * call.value / 10^18 == mfeePercentage
              if mfeePercentage * ext_call.return_data[0] * call.value / 10^18 / 10000 > 0:
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.balanceOf(address owner) with:
                       gas gas_remaining wei
                      args caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= mfeePercentage * ext_call.return_data[0] * call.value / 10^18 / 10000
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.allowance(address owner, address spender) with:
                       gas gas_remaining wei
                      args caller, this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= mfeePercentage * ext_call.return_data[0] * call.value / 10^18 / 10000
      require mfeeMode <= 1
      if mfeeMode:
          require mfeeMode <= 1
          if mfeeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if mfeeAmount:
              require ext_code.size(mMOTAddress)
              call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, mstor8, mfeeAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
      else:
          if ext_call.return_data[0] * call.value / 10^18:
              require mfeePercentage * ext_call.return_data[0] * call.value / 10^18 / ext_call.return_data[0] * call.value / 10^18 == mfeePercentage
              if mfeePercentage * ext_call.return_data[0] * call.value / 10^18 / 10000:
                  require ext_code.size(mMOTAddress)
                  call mMOTAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, mstor8, mfeePercentage * ext_call.return_data[0] * call.value / 10^18 / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0]
  if mstor20m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m]:
      mstor20m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] = 0
      munknownb393e88em[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] = 0
      mstor22m[callerm]m[0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000m]m[addr(m_param1)m] = 0
  return 1


# hash = 0xef3d95b9
# getter = None
# const = ['return', ['mask_shl', 32, 224, 0, ['sha3', ['data', "'sellToken(address,uint256,uint25'", ['mask_shl', 80, 176, -176, "'6,address)'"]]]]]
# payable = False
const unknownef3d95b9 = Mask(32, 224, sha3('sellToken(address,uint256,uint25', Mask(80, 176, '6,address)') >> 176))


# hash = 0xef430aa6
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 11]]]], ['loc', 11]]]
# const = None
# payable = False
def category(): # not payable
  return mcategorym[0 len mcategorym.lengthm]


# hash = 0xf0103906
# getter = None
# const = ['return', ['mask_shl', 32, 224, 0, ['sha3', ['data', "'buyToken(address,uint256,uint256'", ['mask_shl', 72, 184, -184, "',address)'"]]]]]
# payable = False
const unknownf0103906 = Mask(32, 224, sha3('buyToken(address,uint256,uint256', Mask(72, 184, ',address)') >> 184))


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require caller == mowner
  require m_newOwner
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


