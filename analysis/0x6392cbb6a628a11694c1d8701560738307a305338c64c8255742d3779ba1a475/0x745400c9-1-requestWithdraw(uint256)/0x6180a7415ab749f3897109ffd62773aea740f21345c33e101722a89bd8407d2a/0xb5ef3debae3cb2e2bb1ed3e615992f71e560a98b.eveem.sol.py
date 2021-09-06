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
def adjustFeeMode(uint8 _newMode): # not payable
  require caller == owner
  require _newMode <= 1
  feeMode = _newMode
  return 1


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 9]]]], ['loc', 9]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x0fe8a48e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 18]]]]]]]
# const = None
# payable = False
def unknown0fe8a48e(uint256 _param1, addr _param2, addr _param3): # not payable
  return unknown0fe8a48e[_param1][_param2][_param3]


# hash = 0x12e89062
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 17]]]]]]]
# const = None
# payable = False
def unknown12e89062(uint256 _param1, addr _param2, addr _param3): # not payable
  return unknown12e89062[_param1][_param2][_param3]


# hash = 0x15cdc529
# getter = None
# const = None
# payable = True
def unknown15cdc529() payable: 
  unknown1a5911d7 = 0
  if ('cd', 36).length != ('cd', 4).length:
      revert with 0, 'Arrays are not the same lengths'
  if ('cd', 68).length != ('cd', 36).length:
      revert with 0, 'Arrays are not the same lengths'
  [94midx = 0
  while [94midx < ('cd', 4).length:
      require [94midx < ('cd', 36).length
      if cd[((32 * [94midx) + cd[36] + 36)] != 0:
          if cd[132]:
              mem[100] = cd[132]
              require ext_code.size(stor23)
              call stor23.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args cd[132]
          else:
              require [94midx < ('cd', 4).length
              require [94midx < ('cd', 36).length
              require [94midx < ('cd', 68).length
              mem[132] = cd[((32 * [94midx) + cd[36] + 36)]
              mem[164] = cd[((32 * [94midx) + cd[68] + 36)]
              mem[196] = 1
              require ext_code.size(stor23)
              call stor23.pickExchange(address token, uint256 amount, uint256 rate, bool isBuying) with:
                   gas gas_remaining wei
                  args addr(cd[((32 * [94midx) + cd[4] + 36)]), cd[((32 * [94midx) + cd[36] + 36)], cd[((32 * [94midx) + cd[68] + 36)], 1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[100] = ext_call.return_data[0]
              require ext_code.size(stor23)
              call stor23.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require [94midx < ('cd', 36).length
          if not addr(ext_call.return_data[0]):
              unknown1a5911d7 += cd[((32 * [94midx) + cd[36] + 36)]
              require [94midx < ('cd', 4).length
              require [94midx < ('cd', 36).length
              mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
              require unknownb4b8de74 + stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] >= stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]
              if unknownb4b8de74 + stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] < block.timestamp:
                  if not unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]:
                      stor20[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = block.timestamp
                  unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]++
                  mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                  stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = block.timestamp
              mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              call caller with:
                 value cd[((32 * [94midx) + cd[36] + 36)] wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              require [94midx < ('cd', 4).length
              require [94midx < ('cd', 36).length
              require [94midx < ('cd', 68).length
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
                  require [94midx < ('cd', 4).length
                  mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                  mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 20))
                  if stor20[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]:
                      stor20[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = 0
                      unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = 0
                      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                      mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                      stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = 0
              else:
                  require [94midx < ('cd', 36).length
                  unknown1a5911d7 += cd[((32 * [94midx) + cd[36] + 36)]
                  require [94midx < ('cd', 4).length
                  require [94midx < ('cd', 36).length
                  mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                  require unknownb4b8de74 + stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] >= stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]
                  if unknownb4b8de74 + stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] < block.timestamp:
                      if not unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]:
                          stor20[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = block.timestamp
                      unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]++
                      mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                      stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = block.timestamp
                  mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                  call caller with:
                     value cd[((32 * [94midx) + cd[36] + 36)] wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 
  require ext_code.size(stor23)
  call stor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, MOTAddress, 10^18, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not call.value - unknown1a5911d7:
      require feeMode <= 1
      require feeMode <= 1
      if feeMode:
          if feeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if feeAmount > 0:
              require ext_code.size(MOTAddress)
              call MOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feeAmount
              require ext_code.size(MOTAddress)
              call MOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feeAmount
      if feeMode:
          require feeMode <= 1
          if feeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if feeAmount:
              require ext_code.size(MOTAddress)
              call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, stor8, feeAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
  else:
      require (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / call.value - unknown1a5911d7 == ext_call.return_data[0]
      require feeMode <= 1
      if feeMode:
          require feeMode <= 1
          if feeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if feeAmount > 0:
              require ext_code.size(MOTAddress)
              call MOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feeAmount
              require ext_code.size(MOTAddress)
              call MOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feeAmount
      else:
          if (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18:
              require feePercentage * (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18 / (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18 == feePercentage
              if feePercentage * (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18 / 10000 > 0:
                  require ext_code.size(MOTAddress)
                  call MOTAddress.balanceOf(address owner) with:
                       gas gas_remaining wei
                      args caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= feePercentage * (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18 / 10000
                  require ext_code.size(MOTAddress)
                  call MOTAddress.allowance(address owner, address spender) with:
                       gas gas_remaining wei
                      args caller, this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= feePercentage * (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18 / 10000
      require feeMode <= 1
      if feeMode:
          require feeMode <= 1
          if feeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if feeAmount:
              require ext_code.size(MOTAddress)
              call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, stor8, feeAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
      else:
          if (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18:
              require feePercentage * (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18 / (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18 == feePercentage
              if feePercentage * (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18 / 10000:
                  require ext_code.size(MOTAddress)
                  call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, stor8, feePercentage * (call.value * ext_call.return_data[0]) - (unknown1a5911d7 * ext_call.return_data[0]) / 10^18 / 10000
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
  return unknown1a5911d7


# hash = 0x1ddfd7db
# getter = None
# const = None
# payable = False
def supportsTradingPair(address _srcAddress, address _destAddress, bytes32 _exchangeId): # not payable
  require ext_code.size(stor23)
  call stor23.supportsTradingPair(address srcAddress, address destAddress, bytes32 exchangeId) with:
       gas gas_remaining wei
      args addr(_srcAddress), addr(_destAddress), _exchangeId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  return bool(ext_call.return_data[0])


# hash = 0x280dd460
# getter = None
# const = None
# payable = False
def adjustFeePercentage(uint256 _newPercentage): # not payable
  require caller == owner
  require _newPercentage <= 10000
  feePercentage = _newPercentage
  return 1


# hash = 0x42bff0d0
# getter = None
# const = None
# payable = False
def setExchangeAdapterManager(address _exchangeAdapterManager): # not payable
  require caller == owner
  stor23 = _exchangeAdapterManager


# hash = 0x46479541
# getter = None
# const = None
# payable = False
def setWalletId(address _newWallet): # not payable
  require caller == owner
  require _newWallet
  stor8 = _newWallet
  return 1


# hash = 0x54fd4d50
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 12]]]], ['loc', 12]]]
# const = None
# payable = False
def version(): # not payable
  return version[0 len version.length]


# hash = 0x5fc6b623
# getter = None
# const = None
# payable = False
def getPrice(address _sourceAddress, address _destAddress, uint256 _amount, bytes32 _exchangeId): # not payable
  require ext_code.size(stor23)
  call stor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0, 0, addr(_destAddress), _amount, _exchangeId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[0], ext_call.return_data[32]


# hash = 0x674f23ba
# getter = None
# const = None
# payable = False
def unknown674f23ba(array _param1): # not payable
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = _param1.length
  if _param1.length:
      mem[(32 * _param1.length) + 160 len 32 * _param1.length] = code.data[12923 len 32 * _param1.length]
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      require [94midx < _param1.length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, sha3(caller, 21))
      require [94midx < _param1.length
      mem[(32 * _param1.length) + (32 * [94midx) + 160] = unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee][mem[(32 * [94midx) + 140 len 20]] + unknownb393e88e[caller][mem[(32 * [94midx) + 140 len 20]][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee]
      [94midx = [94midx + 1
      continue 
  mem[(64 * _param1.length) + 160] = 32
  mem[(64 * _param1.length) + 192] = _param1.length
  mem[(64 * _param1.length) + 224 len floor32(_param1.length)] = mem[(32 * _param1.length) + 160 len floor32(_param1.length)]
  return memory
    from (64 * _param1.length) + 160
     [93mlen (161 * _param1.length) + 64


# hash = 0x69e15404
# getter = ['storage', 256, 0, 7]
# const = None
# payable = False
def feeAmount(): # not payable
  return feeAmount


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  require caller == owner
  log OwnershipRenounced(address previousOwner=owner)
  owner = 0


# hash = 0x7284e416
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 10]]]], ['loc', 10]]]
# const = None
# payable = False
def description(): # not payable
  return description[0 len description.length]


# hash = 0x78265e2f
# getter = None
# const = None
# payable = False
def unknown78265e2f(): # not payable
  stor15 = 0
  stor16 = 1
  if ('cd', 36).length != ('cd', 4).length:
      revert with 0, 'Arrays are not the same lengths'
  if ('cd', 68).length != ('cd', 36).length:
      revert with 0, 'Arrays are not the same lengths'
  [94midx = 0
  while [94midx < ('cd', 4).length:
      require [94midx < ('cd', 36).length
      if cd[((32 * [94midx) + cd[36] + 36)] != 0:
          if cd[132]:
              mem[100] = cd[132]
              require ext_code.size(stor23)
              call stor23.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args cd[132]
          else:
              require [94midx < ('cd', 4).length
              require [94midx < ('cd', 36).length
              require [94midx < ('cd', 68).length
              mem[132] = cd[((32 * [94midx) + cd[36] + 36)]
              mem[164] = cd[((32 * [94midx) + cd[68] + 36)]
              mem[196] = 1
              require ext_code.size(stor23)
              call stor23.pickExchange(address token, uint256 amount, uint256 rate, bool isBuying) with:
                   gas gas_remaining wei
                  args addr(cd[((32 * [94midx) + cd[4] + 36)]), cd[((32 * [94midx) + cd[36] + 36)], cd[((32 * [94midx) + cd[68] + 36)], 1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[100] = ext_call.return_data[0]
              require ext_code.size(stor23)
              call stor23.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not addr(ext_call.return_data[0]):
              stor16 = 0
              require [94midx < ('cd', 4).length
              require [94midx < ('cd', 36).length
              mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
              require unknownb4b8de74 + stor22[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] >= stor22[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]
              if unknownb4b8de74 + stor22[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] < block.timestamp:
                  if not unknownb393e88e[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
                      stor20[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
                  unknownb393e88e[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]++
                  mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                  stor22[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
              mem[0] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
              if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == addr(cd[((32 * [94midx) + cd[4] + 36)]):
                  call caller with:
                     value cd[((32 * [94midx) + cd[36] + 36)] wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
          else:
              require [94midx < ('cd', 36).length
              require [94midx < ('cd', 4).length
              require ext_code.size(addr(cd[((32 * [94midx) + cd[4] + 36)]))
              call addr(cd[((32 * [94midx) + cd[4] + 36)]).allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data[0] < cd[((32 * [94midx) + cd[36] + 36)]:
                  revert with 0, 'Not enough tokens approved'
              require [94midx < ('cd', 4).length
              require [94midx < ('cd', 36).length
              require ext_code.size(addr(cd[((32 * [94midx) + cd[4] + 36)]))
              call addr(cd[((32 * [94midx) + cd[4] + 36)]).transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, addr(ext_call.return_data[0]), cd[((32 * [94midx) + cd[36] + 36)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require [94midx < ('cd', 4).length
              require ext_code.size(addr(cd[((32 * [94midx) + cd[4] + 36)]))
              call addr(cd[((32 * [94midx) + cd[4] + 36)]).allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args addr(ext_call.return_data[0]), this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require [94midx < ('cd', 4).length
              if not ext_call.return_data[0]:
                  require ext_code.size(addr(ext_call.return_data[0]))
                  call addr(ext_call.return_data[0]).0x80b2edd8 with:
                       gas gas_remaining wei
                      args addr(cd[((32 * [94midx) + cd[4] + 36)])
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
              require [94midx < ('cd', 36).length
              require [94midx < ('cd', 68).length
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
                  stor16 = 0
                  require [94midx < ('cd', 4).length
                  require [94midx < ('cd', 36).length
                  mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                  require unknownb4b8de74 + stor22[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] >= stor22[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]
                  if unknownb4b8de74 + stor22[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] < block.timestamp:
                      if not unknownb393e88e[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
                          stor20[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
                      unknownb393e88e[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]++
                      mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                      stor22[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
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
                  require [94midx < ('cd', 4).length
                  mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 20))
                  if stor20[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
                      stor20[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
                      unknownb393e88e[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
                      mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                      stor22[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
                  require [94midx < ('cd', 4).length
                  require [94midx < ('cd', 36).length
                  require ext_code.size(stor23)
                  call stor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
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
                  mem[132] = MOTAddress
                  mem[164] = 10^18
                  mem[196] = 0
                  require ext_code.size(stor23)
                  call stor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, MOTAddress, 10^18, 0
                  mem[96 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  if not ext_call.return_data[0]:
                      require 10^ext_call.return_data[0]
                      require (0 / 10^ext_call.return_data[0] / 10^18) + stor15 >= stor15
                      stor15 += 0 / 10^ext_call.return_data[0] / 10^18
                  else:
                      require cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / ext_call.return_data[0] == cd[((32 * [94midx) + cd[36] + 36)]
                      if not cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0]:
                          require 10^ext_call.return_data[0]
                          require (0 / 10^ext_call.return_data[0] / 10^18) + stor15 >= stor15
                          stor15 += 0 / 10^ext_call.return_data[0] / 10^18
                      else:
                          require ext_call.return_data[0] * cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] == ext_call.return_data[0]
                          require 10^ext_call.return_data[0]
                          require (ext_call.return_data[0] * cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18) + stor15 >= stor15
                          stor15 += ext_call.return_data[0] * cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18
      [94midx = [94midx + 1
      continue 
  require feeMode <= 1
  if feeMode:
      require feeMode <= 1
      if feeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      if feeAmount > 0:
          require ext_code.size(MOTAddress)
          call MOTAddress.balanceOf(address owner) with:
               gas gas_remaining wei
              args caller
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] >= feeAmount
          require ext_code.size(MOTAddress)
          call MOTAddress.allowance(address owner, address spender) with:
               gas gas_remaining wei
              args caller, this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0] >= feeAmount
  else:
      if stor15:
          require feePercentage * stor15 / stor15 == feePercentage
          if feePercentage * stor15 / 10000 > 0:
              require ext_code.size(MOTAddress)
              call MOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feePercentage * stor15 / 10000
              require ext_code.size(MOTAddress)
              call MOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feePercentage * stor15 / 10000
  require feeMode <= 1
  if feeMode:
      require feeMode <= 1
      if feeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      if feeAmount:
          require ext_code.size(MOTAddress)
          call MOTAddress.transferFrom(address from, address to, uint256 value) with:
               gas gas_remaining wei
              args caller, stor8, feeAmount
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          require ext_call.return_data[0]
  else:
      if stor15:
          require feePercentage * stor15 / stor15 == feePercentage
          if feePercentage * stor15 / 10000:
              require ext_code.size(MOTAddress)
              call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, stor8, feePercentage * stor15 / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
  return bool(stor16)


# hash = 0x869f0f25
# getter = None
# const = None
# payable = False
def unknown869f0f25(addr _param1, addr _param2, uint256 _param3, uint256 _param4, uint256 _param5): # not payable
  require ext_code.size(stor23)
  call stor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0, 0, addr(_param2), _param3, _param4
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if ext_call.return_data[0] <= 0:
      require _param5 + unknowne00ff4e3[_param4][addr(_param1)][addr(_param2)] >= unknowne00ff4e3[_param4][addr(_param1)][addr(_param2)]
      if _param5 + unknowne00ff4e3[_param4][addr(_param1)][addr(_param2)] >= block.timestamp:
          return unknown12e89062[_param4][addr(_param1)][addr(_param2)], unknown0fe8a48e[_param4][addr(_param1)][addr(_param2)], 1
      else:
          return 0
  unknown12e89062[_param4][addr(_param1)][addr(_param2)] = ext_call.return_data[0]
  unknown0fe8a48e[_param4][addr(_param1)][addr(_param2)] = ext_call.return_data[32]
  unknowne00ff4e3[_param4][addr(_param1)][addr(_param2)] = block.timestamp
  return ext_call.return_data[0], ext_call.return_data[32], 0


# hash = 0x8955053f
# getter = None
# const = None
# payable = False
def unknown8955053f(addr _param1, uint256 _param2, uint256 _param3, addr _param4, uint256 _param5): # not payable
  require ext_code.size(_param1)
  call _param1.allowance(address owner, address spender) with:
       gas gas_remaining wei
      args caller, this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < _param2:
      revert with 0, 'Not enough tokens approved'
  if _param5:
      if not _param5:
          require unknownb4b8de74 + stor22[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] >= stor22[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]
          if unknownb4b8de74 + stor22[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] < block.timestamp:
              if not unknownb393e88e[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
                  stor20[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
              unknownb393e88e[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]++
              stor22[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _param1:
              call caller with:
                 value _param2 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  return 0
          else:
              return 0
      require ext_code.size(stor23)
      call stor23.getExchangeAdapter(bytes32 id) with:
           gas gas_remaining wei
          args _param5
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(_param1)
      call _param1.allowance(address owner, address spender) with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x80b2edd8 with:
               gas gas_remaining wei
              args _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      require ext_code.size(_param1)
      call _param1.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args caller, addr(ext_call.return_data[0]), _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      call addr(ext_call.return_data[0]) with:
         funct Mask(32, 224, sha3('sellToken(address,uint256,uint25', '6,address)')) >> 224
           gas gas_remaining wei
          args addr(_param1), _param2, _param3, _param4
      require ext_code.size(stor23)
      call stor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0, 0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param2, _param5
  else:
      require ext_code.size(stor23)
      call stor23.pickExchange(address token, uint256 amount, uint256 rate, bool isBuying) with:
           gas gas_remaining wei
          args 0, 0, _param2, _param3, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require unknownb4b8de74 + stor22[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] >= stor22[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]
          if unknownb4b8de74 + stor22[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] < block.timestamp:
              if not unknownb393e88e[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
                  stor20[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
              unknownb393e88e[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]++
              stor22[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _param1:
              call caller with:
                 value _param2 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  return 0
          else:
              return 0
      require ext_code.size(stor23)
      call stor23.getExchangeAdapter(bytes32 id) with:
           gas gas_remaining wei
          args ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(_param1)
      call _param1.allowance(address owner, address spender) with:
           gas gas_remaining wei
          args addr(ext_call.return_data[0]), this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require ext_code.size(addr(ext_call.return_data[0]))
          call addr(ext_call.return_data[0]).0x80b2edd8 with:
               gas gas_remaining wei
              args _param1
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
      require ext_code.size(_param1)
      call _param1.transferFrom(address from, address to, uint256 value) with:
           gas gas_remaining wei
          args caller, addr(ext_call.return_data[0]), _param2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      call addr(ext_call.return_data[0]) with:
         funct Mask(32, 224, sha3('sellToken(address,uint256,uint25', '6,address)')) >> 224
           gas gas_remaining wei
          args addr(_param1), _param2, _param3, _param4
      require ext_code.size(stor23)
      call stor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0, 0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param2, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_code.size(_param1)
  call _param1.decimals() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(stor23)
  call stor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0, 4008636142, MOTAddress, 10^18, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not ext_call.return_data[0]:
      require 10^ext_call.return_data[0]
      require feeMode <= 1
      if feeMode:
          require feeMode <= 1
          if feeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if feeAmount > 0:
              require ext_code.size(MOTAddress)
              call MOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feeAmount
              require ext_code.size(MOTAddress)
              call MOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feeAmount
      else:
          if 0 / 10^ext_call.return_data[0] / 10^18:
              require feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 0 / 10^ext_call.return_data[0] / 10^18 == feePercentage
              if feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000 > 0:
                  require ext_code.size(MOTAddress)
                  call MOTAddress.balanceOf(address owner) with:
                       gas gas_remaining wei
                      args caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
                  require ext_code.size(MOTAddress)
                  call MOTAddress.allowance(address owner, address spender) with:
                       gas gas_remaining wei
                      args caller, this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
      require feeMode <= 1
      if feeMode:
          require feeMode <= 1
          if feeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if feeAmount:
              require ext_code.size(MOTAddress)
              call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, stor8, feeAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
      else:
          if 0 / 10^ext_call.return_data[0] / 10^18:
              require feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 0 / 10^ext_call.return_data[0] / 10^18 == feePercentage
              if feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000:
                  require ext_code.size(MOTAddress)
                  call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, stor8, feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0]
  else:
      require _param2 * ext_call.return_data[0] / ext_call.return_data[0] == _param2
      if not _param2 * ext_call.return_data[0]:
          require 10^ext_call.return_data[0]
          require feeMode <= 1
          if feeMode:
              require feeMode <= 1
              if feeMode != 1:
                  revert with 0, 'Unsupported fee mode.'
              if feeAmount > 0:
                  require ext_code.size(MOTAddress)
                  call MOTAddress.balanceOf(address owner) with:
                       gas gas_remaining wei
                      args caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= feeAmount
                  require ext_code.size(MOTAddress)
                  call MOTAddress.allowance(address owner, address spender) with:
                       gas gas_remaining wei
                      args caller, this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= feeAmount
          else:
              if 0 / 10^ext_call.return_data[0] / 10^18:
                  require feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 0 / 10^ext_call.return_data[0] / 10^18 == feePercentage
                  if feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000 > 0:
                      require ext_code.size(MOTAddress)
                      call MOTAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args caller
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] >= feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
                      require ext_code.size(MOTAddress)
                      call MOTAddress.allowance(address owner, address spender) with:
                           gas gas_remaining wei
                          args caller, this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] >= feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
          require feeMode <= 1
          if feeMode:
              require feeMode <= 1
              if feeMode != 1:
                  revert with 0, 'Unsupported fee mode.'
              if feeAmount:
                  require ext_code.size(MOTAddress)
                  call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, stor8, feeAmount
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0]
          else:
              if 0 / 10^ext_call.return_data[0] / 10^18:
                  require feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 0 / 10^ext_call.return_data[0] / 10^18 == feePercentage
                  if feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000:
                      require ext_code.size(MOTAddress)
                      call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, stor8, feePercentage * 0 / 10^ext_call.return_data[0] / 10^18 / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0]
      else:
          require ext_call.return_data[0] * _param2 * ext_call.return_data[0] / _param2 * ext_call.return_data[0] == ext_call.return_data[0]
          require 10^ext_call.return_data[0]
          require feeMode <= 1
          if feeMode:
              require feeMode <= 1
              if feeMode != 1:
                  revert with 0, 'Unsupported fee mode.'
              if feeAmount > 0:
                  require ext_code.size(MOTAddress)
                  call MOTAddress.balanceOf(address owner) with:
                       gas gas_remaining wei
                      args caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= feeAmount
                  require ext_code.size(MOTAddress)
                  call MOTAddress.allowance(address owner, address spender) with:
                       gas gas_remaining wei
                      args caller, this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= feeAmount
          else:
              if ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18:
                  require feePercentage * ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 == feePercentage
                  if feePercentage * ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000 > 0:
                      require ext_code.size(MOTAddress)
                      call MOTAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args caller
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] >= feePercentage * ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000
                      require ext_code.size(MOTAddress)
                      call MOTAddress.allowance(address owner, address spender) with:
                           gas gas_remaining wei
                          args caller, this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] >= feePercentage * ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000
          require feeMode <= 1
          if feeMode:
              require feeMode <= 1
              if feeMode != 1:
                  revert with 0, 'Unsupported fee mode.'
              if feeAmount:
                  require ext_code.size(MOTAddress)
                  call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, stor8, feeAmount
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0]
          else:
              if ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18:
                  require feePercentage * ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 == feePercentage
                  if feePercentage * ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000:
                      require ext_code.size(MOTAddress)
                      call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, stor8, feePercentage * ext_call.return_data[0] * _param2 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0]
  if stor20[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
      stor20[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
      unknownb393e88e[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
      stor22[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
  return 1


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x977919bf
# getter = None
# const = None
# payable = False
def adjustFeeAmount(uint256 _newAmount): # not payable
  require caller == owner
  feeAmount = _newAmount
  return 1


# hash = 0x99a5d747
# getter = None
# const = None
# payable = False
def calculateFee(uint256 _value): # not payable
  require feeMode <= 1
  if feeMode:
      require feeMode <= 1
      if feeMode != 1:
          revert with 0, 'Unsupported fee mode.'
      return feeAmount
  if not _value:
      return 0
  require feePercentage * _value / _value == feePercentage
  return (feePercentage * _value / 10000)


# hash = 0xa001ecdd
# getter = ['storage', 256, 0, 6]
# const = None
# payable = False
def feePercentage(): # not payable
  return feePercentage


# hash = 0xb188c70d
# getter = ['storage', 8, 160, 5]
# const = None
# payable = False
def feeMode(): # not payable
  require feeMode <= 1
  return feeMode


# hash = 0xb393e88e
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], ['sha3', ['data', 5328391386102250222617600952611448509162254062, ['sha3', ['data', 'caller', 21]]]]]]]
# const = None
# payable = False
def unknownb393e88e(addr _param1): # not payable
  return unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee][addr(_param1)]


# hash = 0xb4b8de74
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknownb4b8de74(): # not payable
  return unknownb4b8de74


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
  return MOTAddress


# hash = 0xc892693b
# getter = None
# const = None
# payable = False
def setMotAddress(address _motAddress): # not payable
  require caller == owner
  require _motAddress
  require MOTAddress != _motAddress
  MOTAddress = _motAddress
  mem[128] = 'MOT'
  mem[96] = 3
  mem[131 len 0] = None
  mem[131] = Mask(208, 0, 'MOT'), mem[160 len 3]
  [94m_31 = sha3(mem[131 len 3])
  mem[131] = 0x95d89b4100000000000000000000000000000000000000000000000000000000
  require ext_code.size(MOTAddress)
  call MOTAddress.symbol() with:
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
def unknownd0f07926(uint256 _param1): # not payable
  require caller == owner
  unknownb4b8de74 = _param1
  return 1


# hash = 0xe00ff4e3
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 19]]]]]]]
# const = None
# payable = False
def unknowne00ff4e3(uint256 _param1, addr _param2, addr _param3): # not payable
  return unknowne00ff4e3[_param1][_param2][_param3]


# hash = 0xeb5d3ab5
# getter = None
# const = None
# payable = True
def unknowneb5d3ab5(addr _param1, uint256 _param2, uint256 _param3, addr _param4, uint256 _param5) payable: 
  require _param2 == call.value
  if _param5:
      if not _param5:
          require unknownb4b8de74 + stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] >= stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]
          if unknownb4b8de74 + stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] < block.timestamp:
              if not unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]:
                  stor20[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
              unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]++
              stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
          call caller with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              return 0
      require ext_code.size(stor23)
      call stor23.getExchangeAdapter(bytes32 id) with:
           gas gas_remaining wei
          args _param5
  else:
      require ext_code.size(stor23)
      call stor23.pickExchange(address token, uint256 amount, uint256 rate, bool isBuying) with:
           gas gas_remaining wei
          args 0, 0, _param2, _param3, 1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require unknownb4b8de74 + stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] >= stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]
          if unknownb4b8de74 + stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] < block.timestamp:
              if not unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]:
                  stor20[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
              unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]++
              stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
          call caller with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              return 0
      require ext_code.size(stor23)
      call stor23.getExchangeAdapter(bytes32 id) with:
           gas gas_remaining wei
          args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  call addr(ext_call.return_data[0]) with:
     funct Mask(32, 224, sha3('buyToken(address,uint256,uint256', ',address)')) >> 224
     value call.value wei
       gas gas_remaining wei
      args addr(_param1), _param2, _param3, _param4
  if not ext_call.success:
      require unknownb4b8de74 + stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] >= stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]
      if unknownb4b8de74 + stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] < block.timestamp:
          if not unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]:
              stor20[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
          unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]++
          stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
      call caller with:
         value call.value wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          return 0
  require ext_code.size(stor23)
  call stor23.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0, 4008636142, MOTAddress, 10^18, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  if not call.value:
      require feeMode <= 1
      require feeMode <= 1
      if feeMode:
          if feeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if feeAmount > 0:
              require ext_code.size(MOTAddress)
              call MOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feeAmount
              require ext_code.size(MOTAddress)
              call MOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feeAmount
      if feeMode:
          require feeMode <= 1
          if feeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if feeAmount:
              require ext_code.size(MOTAddress)
              call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, stor8, feeAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
  else:
      require ext_call.return_data[0] * call.value / call.value == ext_call.return_data[0]
      require feeMode <= 1
      if feeMode:
          require feeMode <= 1
          if feeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if feeAmount > 0:
              require ext_code.size(MOTAddress)
              call MOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feeAmount
              require ext_code.size(MOTAddress)
              call MOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feeAmount
      else:
          if ext_call.return_data[0] * call.value / 10^18:
              require feePercentage * ext_call.return_data[0] * call.value / 10^18 / ext_call.return_data[0] * call.value / 10^18 == feePercentage
              if feePercentage * ext_call.return_data[0] * call.value / 10^18 / 10000 > 0:
                  require ext_code.size(MOTAddress)
                  call MOTAddress.balanceOf(address owner) with:
                       gas gas_remaining wei
                      args caller
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= feePercentage * ext_call.return_data[0] * call.value / 10^18 / 10000
                  require ext_code.size(MOTAddress)
                  call MOTAddress.allowance(address owner, address spender) with:
                       gas gas_remaining wei
                      args caller, this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0] >= feePercentage * ext_call.return_data[0] * call.value / 10^18 / 10000
      require feeMode <= 1
      if feeMode:
          require feeMode <= 1
          if feeMode != 1:
              revert with 0, 'Unsupported fee mode.'
          if feeAmount:
              require ext_code.size(MOTAddress)
              call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, stor8, feeAmount
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
      else:
          if ext_call.return_data[0] * call.value / 10^18:
              require feePercentage * ext_call.return_data[0] * call.value / 10^18 / ext_call.return_data[0] * call.value / 10^18 == feePercentage
              if feePercentage * ext_call.return_data[0] * call.value / 10^18 / 10000:
                  require ext_code.size(MOTAddress)
                  call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                       gas gas_remaining wei
                      args caller, stor8, feePercentage * ext_call.return_data[0] * call.value / 10^18 / 10000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_call.return_data[0]
  if stor20[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]:
      stor20[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = 0
      unknownb393e88e[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = 0
      stor22[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = 0
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
  return category[0 len category.length]


# hash = 0xf0103906
# getter = None
# const = ['return', ['mask_shl', 32, 224, 0, ['sha3', ['data', "'buyToken(address,uint256,uint256'", ['mask_shl', 72, 184, -184, "',address)'"]]]]]
# payable = False
const unknownf0103906 = Mask(32, 224, sha3('buyToken(address,uint256,uint256', Mask(72, 184, ',address)') >> 184))


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require caller == owner
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


