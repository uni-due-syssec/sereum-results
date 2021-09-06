# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x7B48cC0E7F2bD9F2cA17881758fb2dfCD839BA4c 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 4
    owner # mask: a s
    # storage address 5
    MOTAddress # mask: a s
    # storage address 5
    feeMode # mask: a s
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
    unknown60a90e81 # mask: a s
    # storage address 16
    unknown7e4a9cff # mask: a s
    # storage address 17
    unknown12e89062
    # storage address 18
    unknown0fe8a48e
    # storage address 19
    unknowne00ff4e3
    # storage address 20
    unknownb5eae11b
    # storage address 21
    unknown05558ec7
    # storage address 22
    unknownf1483789
    # storage address 23
    exchangeAdapterManagerAddress # mask: a s
    # storage address 12899467125109667542873028959968672964931742148193715383312412186801137625777
    stor12899467125109667542873028959968672964931742148193715383312412186801137625777
    # storage address 41818820592815202936749920137095441757517247022956301812126849936144786674706
    stor41818820592815202936749920137095441757517247022956301812126849936144786674706
    # storage address 44905755405770339912253796001627216527500107807266478715588041085227740625768
    stor44905755405770339912253796001627216527500107807266478715588041085227740625768
# hash = 0x05558ec7
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 21]]]]]]]
# const = None
# payable = False
def unknown05558ec7(addr _param1, addr _param2, addr _param3): # not payable
  return unknown05558ec7[_param1][_param2][_param3]


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
              mem[100] = 0
              require ext_code.size(exchangeAdapterManagerAddress)
              call exchangeAdapterManagerAddress.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args 0
          else:
              require [94midx < ('cd', 4).length
              require [94midx < ('cd', 36).length
              require [94midx < ('cd', 68).length
              mem[132] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              mem[164] = cd[((32 * [94midx) + cd[36] + 36)]
              mem[196] = cd[((32 * [94midx) + cd[68] + 36)]
              require ext_code.size(exchangeAdapterManagerAddress)
              call exchangeAdapterManagerAddress.0x9ddf8831 with:
                   gas gas_remaining wei
                  args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, addr(cd[((32 * [94midx) + cd[4] + 36)]), cd[((32 * [94midx) + cd[36] + 36)], cd[((32 * [94midx) + cd[68] + 36)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[100] = ext_call.return_data[0]
              require ext_code.size(exchangeAdapterManagerAddress)
              call exchangeAdapterManagerAddress.getExchangeAdapter(bytes32 id) with:
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
              require unknownb4b8de74 + unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] >= unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]
              if unknownb4b8de74 + unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] < block.timestamp:
                  if not unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]:
                      unknownb5eae11b[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = block.timestamp
                  unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]++
                  mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                  unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = block.timestamp
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
                  if unknownb5eae11b[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]:
                      unknownb5eae11b[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = 0
                      unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = 0
                      mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                      mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                      unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = 0
              else:
                  require [94midx < ('cd', 36).length
                  unknown1a5911d7 += cd[((32 * [94midx) + cd[36] + 36)]
                  require [94midx < ('cd', 4).length
                  require [94midx < ('cd', 36).length
                  mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                  require unknownb4b8de74 + unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] >= unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]
                  if unknownb4b8de74 + unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] < block.timestamp:
                      if not unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]:
                          unknownb5eae11b[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = block.timestamp
                      unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])]++
                      mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000, sha3(caller, 22))
                      unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(cd[((32 * [94midx) + cd[4] + 36)])] = block.timestamp
                  mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                  call caller with:
                     value cd[((32 * [94midx) + cd[36] + 36)] wei
                       gas 2300 * is_zero(value) wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
      [94midx = [94midx + 1
      continue 
  require ext_code.size(exchangeAdapterManagerAddress)
  call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
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
  require ext_code.size(exchangeAdapterManagerAddress)
  call exchangeAdapterManagerAddress.supportsTradingPair(address srcAddress, address destAddress, bytes32 exchangeId) with:
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
  exchangeAdapterManagerAddress = _exchangeAdapterManager


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
  require ext_code.size(exchangeAdapterManagerAddress)
  call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
       gas gas_remaining wei
      args 0, 0, addr(_destAddress), _amount, _exchangeId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  return ext_call.return_data[0], ext_call.return_data[32]


# hash = 0x60a90e81
# getter = ['storage', 256, 0, 15]
# const = None
# payable = False
def unknown60a90e81(): # not payable
  return unknown60a90e81


# hash = 0x674f23ba
# getter = None
# const = None
# payable = False
def unknown674f23ba(array _param1): # not payable
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  mem[(32 * _param1.length) + 128] = _param1.length
  if _param1.length:
      mem[(32 * _param1.length) + 160 len 32 * _param1.length] = code.data[16794 len 32 * _param1.length]
  [94midx = 0
  while [94midx < _param1.length:
      require [94midx < _param1.length
      require [94midx < _param1.length
      mem[0] = mem[(32 * [94midx) + 140 len 20]
      mem[32] = sha3(0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, sha3(caller, 21))
      require [94midx < _param1.length
      mem[(32 * _param1.length) + (32 * [94midx) + 160] = unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee][mem[(32 * [94midx) + 140 len 20]] + unknown05558ec7[caller][mem[(32 * [94midx) + 140 len 20]][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee]
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


# hash = 0x6b06d264
# getter = None
# const = ['return', ['mask_shl', 32, 224, 0, ['sha3', ['data', "'tokenExchange(address,address,ui'", ['mask_shl', 176, 80, -80, "'nt256,uint256,address)'"]]]]]
# payable = False
const unknown6b06d264 = Mask(32, 224, sha3('tokenExchange(address,address,ui', Mask(176, 80, 'nt256,uint256,address)') >> 80))


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


# hash = 0x74c6ec74
# getter = None
# const = None
# payable = False
def unknown74c6ec74(addr _param1, addr _param2, uint256 _param3, uint256 _param4, addr _param5, uint256 _param6): # not payable
  require ext_code.size(_param1)
  call _param1.allowance(address owner, address spender) with:
       gas gas_remaining wei
      args caller, this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[0] < _param3:
      revert with 0, 'Not enough tokens approved'
  if _param6:
      if not _param6:
          require unknownb4b8de74 + unknownf1483789[caller][addr(_param1)][addr(_param2)] >= unknownf1483789[caller][addr(_param1)][addr(_param2)]
          if unknownb4b8de74 + unknownf1483789[caller][addr(_param1)][addr(_param2)] < block.timestamp:
              if not unknown05558ec7[caller][addr(_param1)][addr(_param2)]:
                  unknownb5eae11b[caller][addr(_param1)][addr(_param2)] = block.timestamp
              unknown05558ec7[caller][addr(_param1)][addr(_param2)]++
              unknownf1483789[caller][addr(_param1)][addr(_param2)] = block.timestamp
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _param1:
              call caller with:
                 value _param3 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  return 0
          else:
              return 0
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getExchangeAdapter(bytes32 id) with:
           gas gas_remaining wei
          args _param6
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
          args caller, addr(ext_call.return_data[0]), _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      call addr(ext_call.return_data[0]) with:
         funct Mask(32, 224, sha3('tokenExchange(address,address,ui', 'nt256,uint256,address)')) >> 224
           gas gas_remaining wei
          args addr(_param1), addr(_param2), _param3, _param4, addr(_param5)
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0, 0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param3, _param6
  else:
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.0x9ddf8831 with:
           gas gas_remaining wei
          args 0, 0, addr(_param2), _param3, _param4
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require unknownb4b8de74 + unknownf1483789[caller][addr(_param1)][addr(_param2)] >= unknownf1483789[caller][addr(_param1)][addr(_param2)]
          if unknownb4b8de74 + unknownf1483789[caller][addr(_param1)][addr(_param2)] < block.timestamp:
              if not unknown05558ec7[caller][addr(_param1)][addr(_param2)]:
                  unknownb5eae11b[caller][addr(_param1)][addr(_param2)] = block.timestamp
              unknown05558ec7[caller][addr(_param1)][addr(_param2)]++
              unknownf1483789[caller][addr(_param1)][addr(_param2)] = block.timestamp
          if 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee == _param1:
              call caller with:
                 value _param3 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              else:
                  return 0
          else:
              return 0
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getExchangeAdapter(bytes32 id) with:
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
          args caller, addr(ext_call.return_data[0]), _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      call addr(ext_call.return_data[0]) with:
         funct Mask(32, 224, sha3('tokenExchange(address,address,ui', 'nt256,uint256,address)')) >> 224
           gas gas_remaining wei
          args addr(_param1), addr(_param2), _param3, _param4, addr(_param5)
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0, 0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param3, ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 64
  require ext_code.size(_param1)
  call _param1.decimals() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(exchangeAdapterManagerAddress)
  call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
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
      require _param3 * ext_call.return_data[0] / ext_call.return_data[0] == _param3
      if not _param3 * ext_call.return_data[0]:
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
          require ext_call.return_data[0] * _param3 * ext_call.return_data[0] / _param3 * ext_call.return_data[0] == ext_call.return_data[0]
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
              if ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18:
                  require feePercentage * ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 == feePercentage
                  if feePercentage * ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000 > 0:
                      require ext_code.size(MOTAddress)
                      call MOTAddress.balanceOf(address owner) with:
                           gas gas_remaining wei
                          args caller
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] >= feePercentage * ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000
                      require ext_code.size(MOTAddress)
                      call MOTAddress.allowance(address owner, address spender) with:
                           gas gas_remaining wei
                          args caller, this.address
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0] >= feePercentage * ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000
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
              if ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18:
                  require feePercentage * ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 == feePercentage
                  if feePercentage * ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000:
                      require ext_code.size(MOTAddress)
                      call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                           gas gas_remaining wei
                          args caller, stor8, feePercentage * ext_call.return_data[0] * _param3 * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18 / 10000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_call.return_data[0]
  if unknownb5eae11b[caller][addr(_param1)][addr(_param2)]:
      unknownb5eae11b[caller][addr(_param1)][addr(_param2)] = 0
      unknown05558ec7[caller][addr(_param1)][addr(_param2)] = 0
      unknownf1483789[caller][addr(_param1)][addr(_param2)] = 0
  return 1


# hash = 0x78265e2f
# getter = None
# const = None
# payable = False
def unknown78265e2f(): # not payable
  unknown60a90e81 = 0
  unknown7e4a9cff = 1
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
              require ext_code.size(exchangeAdapterManagerAddress)
              call exchangeAdapterManagerAddress.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args cd[132]
          else:
              require [94midx < ('cd', 4).length
              require [94midx < ('cd', 36).length
              require [94midx < ('cd', 68).length
              mem[132] = 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
              mem[164] = cd[((32 * [94midx) + cd[36] + 36)]
              mem[196] = cd[((32 * [94midx) + cd[68] + 36)]
              require ext_code.size(exchangeAdapterManagerAddress)
              call exchangeAdapterManagerAddress.0x9ddf8831 with:
                   gas gas_remaining wei
                  args addr(cd[((32 * [94midx) + cd[4] + 36)]), 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, cd[((32 * [94midx) + cd[36] + 36)], cd[((32 * [94midx) + cd[68] + 36)]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              mem[100] = ext_call.return_data[0]
              require ext_code.size(exchangeAdapterManagerAddress)
              call exchangeAdapterManagerAddress.getExchangeAdapter(bytes32 id) with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
          mem[96] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not addr(ext_call.return_data[0]):
              unknown7e4a9cff = 0
              require [94midx < ('cd', 4).length
              require [94midx < ('cd', 36).length
              mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
              require unknownb4b8de74 + unknownf1483789[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] >= unknownf1483789[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]
              if unknownb4b8de74 + unknownf1483789[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] < block.timestamp:
                  if not unknown05558ec7[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
                      unknownb5eae11b[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
                  unknown05558ec7[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]++
                  mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                  unknownf1483789[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
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
                  unknown7e4a9cff = 0
                  require [94midx < ('cd', 4).length
                  require [94midx < ('cd', 36).length
                  mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                  require unknownb4b8de74 + unknownf1483789[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] >= unknownf1483789[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]
                  if unknownb4b8de74 + unknownf1483789[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] < block.timestamp:
                      if not unknown05558ec7[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
                          unknownb5eae11b[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
                      unknown05558ec7[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]++
                      mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                      unknownf1483789[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
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
                  if unknownb5eae11b[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
                      unknownb5eae11b[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
                      unknown05558ec7[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
                      mem[32] = sha3(addr(cd[((32 * [94midx) + cd[4] + 36)]), sha3(caller, 22))
                      unknownf1483789[caller][addr(cd[((32 * [94midx) + cd[4] + 36)])][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
                  require [94midx < ('cd', 4).length
                  require [94midx < ('cd', 36).length
                  require ext_code.size(exchangeAdapterManagerAddress)
                  call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
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
                  require ext_code.size(exchangeAdapterManagerAddress)
                  call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
                       gas gas_remaining wei
                      args 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, MOTAddress, 10^18, 0
                  mem[96 len 64] = ext_call.return_data[0 len 64]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 64
                  if not ext_call.return_data[0]:
                      require 10^ext_call.return_data[0]
                      require (0 / 10^ext_call.return_data[0] / 10^18) + unknown60a90e81 >= unknown60a90e81
                      unknown60a90e81 += 0 / 10^ext_call.return_data[0] / 10^18
                  else:
                      require cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / ext_call.return_data[0] == cd[((32 * [94midx) + cd[36] + 36)]
                      if not cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0]:
                          require 10^ext_call.return_data[0]
                          require (0 / 10^ext_call.return_data[0] / 10^18) + unknown60a90e81 >= unknown60a90e81
                          unknown60a90e81 += 0 / 10^ext_call.return_data[0] / 10^18
                      else:
                          require ext_call.return_data[0] * cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] == ext_call.return_data[0]
                          require 10^ext_call.return_data[0]
                          require (ext_call.return_data[0] * cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18) + unknown60a90e81 >= unknown60a90e81
                          unknown60a90e81 += ext_call.return_data[0] * cd[((32 * [94midx) + cd[36] + 36)] * ext_call.return_data[0] / 10^ext_call.return_data[0] / 10^18
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
      if unknown60a90e81:
          require feePercentage * unknown60a90e81 / unknown60a90e81 == feePercentage
          if feePercentage * unknown60a90e81 / 10000 > 0:
              require ext_code.size(MOTAddress)
              call MOTAddress.balanceOf(address owner) with:
                   gas gas_remaining wei
                  args caller
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feePercentage * unknown60a90e81 / 10000
              require ext_code.size(MOTAddress)
              call MOTAddress.allowance(address owner, address spender) with:
                   gas gas_remaining wei
                  args caller, this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0] >= feePercentage * unknown60a90e81 / 10000
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
      if unknown60a90e81:
          require feePercentage * unknown60a90e81 / unknown60a90e81 == feePercentage
          if feePercentage * unknown60a90e81 / 10000:
              require ext_code.size(MOTAddress)
              call MOTAddress.transferFrom(address from, address to, uint256 value) with:
                   gas gas_remaining wei
                  args caller, stor8, feePercentage * unknown60a90e81 / 10000
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_call.return_data[0]
  return bool(unknown7e4a9cff)


# hash = 0x7e4a9cff
# getter = ['bool', ['storage', 8, 0, 16]]
# const = None
# payable = False
def unknown7e4a9cff(): # not payable
  return bool(unknown7e4a9cff)


# hash = 0x869f0f25
# getter = None
# const = None
# payable = False
def unknown869f0f25(addr _param1, addr _param2, uint256 _param3, uint256 _param4, uint256 _param5): # not payable
  require ext_code.size(exchangeAdapterManagerAddress)
  call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
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
          require unknownb4b8de74 + unknownf1483789[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] >= unknownf1483789[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]
          if unknownb4b8de74 + unknownf1483789[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] < block.timestamp:
              if not unknown05558ec7[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
                  unknownb5eae11b[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
              unknown05558ec7[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]++
              unknownf1483789[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
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
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getExchangeAdapter(bytes32 id) with:
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
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
           gas gas_remaining wei
          args 0, 0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param2, _param5
  else:
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.0x9ddf8831 with:
           gas gas_remaining wei
          args 0, 0, 0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee, _param2, _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require unknownb4b8de74 + unknownf1483789[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] >= unknownf1483789[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]
          if unknownb4b8de74 + unknownf1483789[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] < block.timestamp:
              if not unknown05558ec7[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
                  unknownb5eae11b[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
              unknown05558ec7[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]++
              unknownf1483789[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = block.timestamp
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
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getExchangeAdapter(bytes32 id) with:
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
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
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
  require ext_code.size(exchangeAdapterManagerAddress)
  call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
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
  if unknownb5eae11b[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000]:
      unknownb5eae11b[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
      unknown05558ec7[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
      unknownf1483789[caller][addr(_param1)][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000] = 0
  return 1


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8fa66921
# getter = None
# const = None
# payable = False
def unknown8fa66921(): # not payable
  mem[96] = ('cd', 4).length
  if not ('cd', 4).length:
      mem[(32 * ('cd', 4).length) + 128] = ('cd', 4).length
      mem[(64 * ('cd', 4).length) + 160] = ('cd', 4).length
      mem[(98 * ('cd', 4).length) + 192] = 0x8fb5a48200000000000000000000000000000000000000000000000000000000
      mem[(98 * ('cd', 4).length) + 196] = 32
      mem[(98 * ('cd', 4).length) + 228] = ('cd', 4).length
      mem[(98 * ('cd', 4).length) + 260 len 32 * ('cd', 4).length] = call.data[cd[4] + 36 len 32 * ('cd', 4).length]
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getPrices(address[] ofAssets) with:
           gas gas_remaining wei
          args Array(len=('cd', 4).length, data=mem[(98 * ('cd', 4).length) + 260 len 161 * ('cd', 4).length])
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      mem[(98 * ('cd', 4).length) + 192 len return_data.size] = ext_call.return_data[0 len return_data.size]
      mem[64] = (98 * ('cd', 4).length) + ceil32(return_data.size) + 192
      require return_data.size >= 64
      [94m_9 = mem[(98 * ('cd', 4).length) + 192 len 4], 0
      require mem[(98 * ('cd', 4).length) + 192 len 4], 0 <= 4294967296
      require mem[(98 * ('cd', 4).length) + 192 len 4], 0 + 32 <= return_data.size
      require mem[(98 * ('cd', 4).length) + mem[(98 * ('cd', 4).length) + 192 len 4], 0 + 192] <= 4294967296 and mem[(98 * ('cd', 4).length) + 192 len 4], 0 + (32 * mem[(98 * ('cd', 4).length) + mem[(98 * ('cd', 4).length) + 192 len 4], 0 + 192]) + 32 <= return_data.size
      require 32, Mask(224, 32, ('cd', 4).length) >> 32 <= 4294967296
      require 32, Mask(224, 32, ('cd', 4).length) >> 32 + 32 <= return_data.size
      require mem[(98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + 192] <= 4294967296 and 32, Mask(224, 32, ('cd', 4).length) >> 32 + (32 * mem[(98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + 192]) + 32 <= return_data.size
      [94m_118 = mem[(98 * ('cd', 4).length) + mem[(98 * ('cd', 4).length) + 192 len 4], 0 + 192]
      [94midx = 0
      while [94midx < [94m_118:
          require [94midx < mem[(98 * ('cd', 4).length) + [94m_9 + 192]
          if mem[(32 * [94midx) + (98 * ('cd', 4).length) + [94m_9 + 224] <= 0:
              require [94midx < ('cd', 4).length
              mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              mem[32] = 0x6347c1c18602f5cf5015075a1ee0f4e57acbbd64a3bb6fa2f607dd6eb58efb68
              require [94midx < ('cd', 4).length
              if stor6347[addr(cd[((32 * [94midx) + cd[4] + 36)])] + cd[36] < block.timestamp:
                  mem[(32 * [94midx) + 128] = 0
                  require [94midx < mem[(32 * ('cd', 4).length) + 128]
                  mem[(32 * ('cd', 4).length) + (32 * [94midx) + 160] = 0
                  require [94midx < mem[(64 * ('cd', 4).length) + 160]
                  mem[(64 * ('cd', 4).length) + (32 * [94midx) + 192] = 0
              else:
                  require [94midx < ('cd', 4).length
                  mem[(32 * [94midx) + 128] = stor5C74[addr(cd[((32 * [94midx) + cd[4] + 36)])]
                  require [94midx < ('cd', 4).length
                  mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
                  mem[32] = 0x1c84d6f402ae240e5cef11f90e285bb7534dc7691fa483e0f9c02ce6dd29aab1
                  require [94midx < mem[(32 * ('cd', 4).length) + 128]
                  mem[(32 * ('cd', 4).length) + (32 * [94midx) + 160] = stor1C84[addr(cd[((32 * [94midx) + cd[4] + 36)])]
                  require [94midx < mem[(64 * ('cd', 4).length) + 160]
                  mem[(64 * ('cd', 4).length) + (32 * [94midx) + 192] = 1
          else:
              require [94midx < mem[(98 * ('cd', 4).length) + [94m_9 + 192]
              require [94midx < ('cd', 4).length
              stor5C74[addr(cd[((32 * [94midx) + cd[4] + 36)])] = mem[(98 * ('cd', 4).length) + [94m_9 + (32 * [94midx) + 224]
              require [94midx < mem[(98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + 192]
              require [94midx < ('cd', 4).length
              stor1C84[addr(cd[((32 * [94midx) + cd[4] + 36)])] = mem[(98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + (32 * [94midx) + 224]
              mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              mem[32] = 0x6347c1c18602f5cf5015075a1ee0f4e57acbbd64a3bb6fa2f607dd6eb58efb68
              stor6347[addr(cd[((32 * [94midx) + cd[4] + 36)])] = block.timestamp
              require [94midx < mem[(98 * ('cd', 4).length) + [94m_9 + 192]
              require [94midx < ('cd', 4).length
              mem[(32 * [94midx) + 128] = mem[(32 * [94midx) + (98 * ('cd', 4).length) + [94m_9 + 224]
              require [94midx < mem[(98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + 192]
              require [94midx < mem[(32 * ('cd', 4).length) + 128]
              mem[(32 * ('cd', 4).length) + (32 * [94midx) + 160] = mem[(32 * [94midx) + (98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + 224]
              require [94midx < mem[(64 * ('cd', 4).length) + 160]
              mem[(64 * ('cd', 4).length) + (32 * [94midx) + 192] = 0
          [94midx = [94midx + 1
          continue 
      mem[(98 * ('cd', 4).length) + ceil32(return_data.size) + 192] = 96
      mem[(98 * ('cd', 4).length) + ceil32(return_data.size) + 288] = ('cd', 4).length
      mem[(98 * ('cd', 4).length) + ceil32(return_data.size) + 320 len floor32(('cd', 4).length)] = mem[128 len floor32(('cd', 4).length)]
      mem[(98 * ('cd', 4).length) + ceil32(return_data.size) + 224] = (32 * ('cd', 4).length) + 128
      mem[(131 * ('cd', 4).length) + ceil32(return_data.size) + 320] = mem[(32 * ('cd', 4).length) + 128]
      mem[(131 * ('cd', 4).length) + ceil32(return_data.size) + 352 len floor32(mem[(32 * ('cd', 4).length) + 128])] = mem[(32 * ('cd', 4).length) + 160 len floor32(mem[(32 * ('cd', 4).length) + 128])]
      mem[(98 * ('cd', 4).length) + ceil32(return_data.size) + 256] = (32 * mem[(32 * ('cd', 4).length) + 128]) + (32 * ('cd', 4).length) + 160
      mem[(32 * mem[(32 * ('cd', 4).length) + 128]) + (131 * ('cd', 4).length) + ceil32(return_data.size) + 352] = mem[(64 * ('cd', 4).length) + 160]
      [94m_233 = mem[(64 * ('cd', 4).length) + 160]
      mem[(32 * mem[(32 * ('cd', 4).length) + 128]) + (131 * ('cd', 4).length) + ceil32(return_data.size) + 384 len floor32(mem[(64 * ('cd', 4).length) + 160])] = mem[(64 * ('cd', 4).length) + 192 len floor32(mem[(64 * ('cd', 4).length) + 160])]
      return memory
        from (98 * ('cd', 4).length) + ceil32(return_data.size) + 192
         [93mlen (32 * [94m_233) + (32 * mem[(32 * ('cd', 4).length) + 128]) + (33 * ('cd', 4).length) + 192
  mem[128 len 32 * ('cd', 4).length] = code.data[16794 len 32 * ('cd', 4).length]
  mem[(32 * ('cd', 4).length) + 128] = ('cd', 4).length
  mem[(32 * ('cd', 4).length) + 160 len 32 * ('cd', 4).length] = code.data[16794 len 32 * ('cd', 4).length]
  mem[(64 * ('cd', 4).length) + 160] = ('cd', 4).length
  mem[(64 * ('cd', 4).length) + 192 len 32 * ('cd', 4).length] = code.data[16794 len 32 * ('cd', 4).length]
  mem[(98 * ('cd', 4).length) + 192] = 0x8fb5a48200000000000000000000000000000000000000000000000000000000
  mem[(98 * ('cd', 4).length) + 196] = 32
  mem[(98 * ('cd', 4).length) + 228] = ('cd', 4).length
  mem[(98 * ('cd', 4).length) + 260 len 32 * ('cd', 4).length] = call.data[cd[4] + 36 len 32 * ('cd', 4).length]
  require ext_code.size(exchangeAdapterManagerAddress)
  call exchangeAdapterManagerAddress.getPrices(address[] ofAssets) with:
       gas gas_remaining wei
      args Array(len=('cd', 4).length, data=mem[(98 * ('cd', 4).length) + 260 len 161 * ('cd', 4).length])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[(98 * ('cd', 4).length) + 192 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = (98 * ('cd', 4).length) + ceil32(return_data.size) + 192
  require return_data.size >= 64
  [94m_15 = mem[(98 * ('cd', 4).length) + 192 len 4], 0
  require mem[(98 * ('cd', 4).length) + 192 len 4], 0 <= 4294967296
  require mem[(98 * ('cd', 4).length) + 192 len 4], 0 + 32 <= return_data.size
  require mem[(98 * ('cd', 4).length) + mem[(98 * ('cd', 4).length) + 192 len 4], 0 + 192] <= 4294967296 and mem[(98 * ('cd', 4).length) + 192 len 4], 0 + (32 * mem[(98 * ('cd', 4).length) + mem[(98 * ('cd', 4).length) + 192 len 4], 0 + 192]) + 32 <= return_data.size
  require 32, Mask(224, 32, ('cd', 4).length) >> 32 <= 4294967296
  require 32, Mask(224, 32, ('cd', 4).length) >> 32 + 32 <= return_data.size
  require mem[(98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + 192] <= 4294967296 and 32, Mask(224, 32, ('cd', 4).length) >> 32 + (32 * mem[(98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + 192]) + 32 <= return_data.size
  [94m_119 = mem[(98 * ('cd', 4).length) + mem[(98 * ('cd', 4).length) + 192 len 4], 0 + 192]
  [94midx = 0
  while [94midx < [94m_119:
      require [94midx < mem[(98 * ('cd', 4).length) + [94m_15 + 192]
      if mem[(32 * [94midx) + (98 * ('cd', 4).length) + [94m_15 + 224] <= 0:
          require [94midx < ('cd', 4).length
          mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
          mem[32] = 0x6347c1c18602f5cf5015075a1ee0f4e57acbbd64a3bb6fa2f607dd6eb58efb68
          require [94midx < ('cd', 4).length
          if stor6347[addr(cd[((32 * [94midx) + cd[4] + 36)])] + cd[36] < block.timestamp:
              mem[(32 * [94midx) + 128] = 0
              require [94midx < mem[(32 * ('cd', 4).length) + 128]
              mem[(32 * ('cd', 4).length) + (32 * [94midx) + 160] = 0
              require [94midx < mem[(64 * ('cd', 4).length) + 160]
              mem[(64 * ('cd', 4).length) + (32 * [94midx) + 192] = 0
          else:
              require [94midx < ('cd', 4).length
              mem[(32 * [94midx) + 128] = stor5C74[addr(cd[((32 * [94midx) + cd[4] + 36)])]
              require [94midx < ('cd', 4).length
              mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
              mem[32] = 0x1c84d6f402ae240e5cef11f90e285bb7534dc7691fa483e0f9c02ce6dd29aab1
              require [94midx < mem[(32 * ('cd', 4).length) + 128]
              mem[(32 * ('cd', 4).length) + (32 * [94midx) + 160] = stor1C84[addr(cd[((32 * [94midx) + cd[4] + 36)])]
              require [94midx < mem[(64 * ('cd', 4).length) + 160]
              mem[(64 * ('cd', 4).length) + (32 * [94midx) + 192] = 1
      else:
          require [94midx < mem[(98 * ('cd', 4).length) + [94m_15 + 192]
          require [94midx < ('cd', 4).length
          stor5C74[addr(cd[((32 * [94midx) + cd[4] + 36)])] = mem[(98 * ('cd', 4).length) + [94m_15 + (32 * [94midx) + 224]
          require [94midx < mem[(98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + 192]
          require [94midx < ('cd', 4).length
          stor1C84[addr(cd[((32 * [94midx) + cd[4] + 36)])] = mem[(98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + (32 * [94midx) + 224]
          mem[0] = addr(cd[((32 * [94midx) + cd[4] + 36)])
          mem[32] = 0x6347c1c18602f5cf5015075a1ee0f4e57acbbd64a3bb6fa2f607dd6eb58efb68
          stor6347[addr(cd[((32 * [94midx) + cd[4] + 36)])] = block.timestamp
          require [94midx < mem[(98 * ('cd', 4).length) + [94m_15 + 192]
          require [94midx < ('cd', 4).length
          mem[(32 * [94midx) + 128] = mem[(32 * [94midx) + (98 * ('cd', 4).length) + [94m_15 + 224]
          require [94midx < mem[(98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + 192]
          require [94midx < mem[(32 * ('cd', 4).length) + 128]
          mem[(32 * ('cd', 4).length) + (32 * [94midx) + 160] = mem[(32 * [94midx) + (98 * ('cd', 4).length) + 32, Mask(224, 32, ('cd', 4).length) >> 32 + 224]
          require [94midx < mem[(64 * ('cd', 4).length) + 160]
          mem[(64 * ('cd', 4).length) + (32 * [94midx) + 192] = 0
      [94midx = [94midx + 1
      continue 
  mem[(98 * ('cd', 4).length) + ceil32(return_data.size) + 192] = 96
  mem[(98 * ('cd', 4).length) + ceil32(return_data.size) + 288] = ('cd', 4).length
  mem[(98 * ('cd', 4).length) + ceil32(return_data.size) + 320 len floor32(('cd', 4).length)] = mem[128 len floor32(('cd', 4).length)]
  mem[(98 * ('cd', 4).length) + ceil32(return_data.size) + 224] = (32 * ('cd', 4).length) + 128
  mem[(131 * ('cd', 4).length) + ceil32(return_data.size) + 320] = mem[(32 * ('cd', 4).length) + 128]
  mem[(131 * ('cd', 4).length) + ceil32(return_data.size) + 352 len floor32(mem[(32 * ('cd', 4).length) + 128])] = mem[(32 * ('cd', 4).length) + 160 len floor32(mem[(32 * ('cd', 4).length) + 128])]
  mem[(98 * ('cd', 4).length) + ceil32(return_data.size) + 256] = (32 * mem[(32 * ('cd', 4).length) + 128]) + (32 * ('cd', 4).length) + 160
  mem[(32 * mem[(32 * ('cd', 4).length) + 128]) + (131 * ('cd', 4).length) + ceil32(return_data.size) + 352] = mem[(64 * ('cd', 4).length) + 160]
  [94m_236 = mem[(64 * ('cd', 4).length) + 160]
  mem[(32 * mem[(32 * ('cd', 4).length) + 128]) + (131 * ('cd', 4).length) + ceil32(return_data.size) + 384 len floor32(mem[(64 * ('cd', 4).length) + 160])] = mem[(64 * ('cd', 4).length) + 192 len floor32(mem[(64 * ('cd', 4).length) + 160])]
  return memory
    from (98 * ('cd', 4).length) + ceil32(return_data.size) + 192
     [93mlen (32 * [94m_236) + (32 * mem[(32 * ('cd', 4).length) + 128]) + (33 * ('cd', 4).length) + 192


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
  return unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee][addr(_param1)]


# hash = 0xb4b8de74
# getter = ['storage', 256, 0, 13]
# const = None
# payable = False
def unknownb4b8de74(): # not payable
  return unknownb4b8de74


# hash = 0xb5eae11b
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 20]]]]]]]
# const = None
# payable = False
def unknownb5eae11b(addr _param1, addr _param2, addr _param3): # not payable
  return unknownb5eae11b[_param1][_param2][_param3]


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


# hash = 0xca626232
# getter = ['storage', 160, 0, 23]
# const = None
# payable = False
def exchangeAdapterManager(): # not payable
  return exchangeAdapterManagerAddress


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
          require unknownb4b8de74 + unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] >= unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]
          if unknownb4b8de74 + unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] < block.timestamp:
              if not unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]:
                  unknownb5eae11b[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
              unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]++
              unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
          call caller with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              return 0
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getExchangeAdapter(bytes32 id) with:
           gas gas_remaining wei
          args _param5
  else:
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.0x9ddf8831 with:
           gas gas_remaining wei
          args 0, 4008636142, addr(_param1), _param2, _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          require unknownb4b8de74 + unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] >= unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]
          if unknownb4b8de74 + unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] < block.timestamp:
              if not unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]:
                  unknownb5eae11b[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
              unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]++
              unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
          call caller with:
             value call.value wei
               gas 2300 * is_zero(value) wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          else:
              return 0
      require ext_code.size(exchangeAdapterManagerAddress)
      call exchangeAdapterManagerAddress.getExchangeAdapter(bytes32 id) with:
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
      require unknownb4b8de74 + unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] >= unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]
      if unknownb4b8de74 + unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] < block.timestamp:
          if not unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]:
              unknownb5eae11b[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
          unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]++
          unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = block.timestamp
      call caller with:
         value call.value wei
           gas 2300 * is_zero(value) wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      else:
          return 0
  require ext_code.size(exchangeAdapterManagerAddress)
  call exchangeAdapterManagerAddress.getPrice(address sourceAddress, address destAddress, uint256 amount, bytes32 exchangeId) with:
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
  if unknownb5eae11b[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)]:
      unknownb5eae11b[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = 0
      unknown05558ec7[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = 0
      unknownf1483789[caller][0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000][addr(_param1)] = 0
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


# hash = 0xf1483789
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 22]]]]]]]
# const = None
# payable = False
def unknownf1483789(addr _param1, addr _param2, addr _param3): # not payable
  return unknownf1483789[_param1][_param2][_param3]


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


