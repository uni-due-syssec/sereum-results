# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xaC9b2cf7E023a4D6F4B9D907590C460851aBf0Ba 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    factoryAddress # mask: a s
    # storage address 1
    securityTokenAddress # mask: a s
    # storage address 2
    paused # mask: a s
    # storage address 2
    proofTokenAddress # mask: a s
    # storage address 3
    issuanceAddress # mask: a s
    # storage address 4
    signingAddress # mask: a s
    # storage address 5
    whitelist
    # storage address 6
    stor6
    # storage address 7
    stor7 # mask: a s
    # storage address 7
    allowAllWhitelistIssuances # mask: a s
    # storage address 7
    stor7 # mask: a s
    # storage address 7
    allowAllWhitelistTransfers # mask: a s
    # storage address 7
    allowAllBurnTransfers # mask: a s
    # storage address 7
    allowAllTransfers # mask: a s
    # storage address 7
    stor7 # mask: a s
# hash = 0x0e94a0ee
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def proofToken(): # not payable
  return proofTokenAddress


# hash = 0x0f28937c
# getter = None
# const = None
# payable = False
def modifyWhitelistMulti(address[] _investors, uint256[] _fromTimes, uint256[] _toTimes, uint256[] _expiryTimes, bool[] _canBuyFromSTO): # not payable
  mem[96] = _investors.length
  mem[128 len 32 * _investors.length] = call.data[_investors + 36 len 32 * _investors.length]
  mem[(32 * _investors.length) + 128] = _fromTimes.length
  mem[(32 * _investors.length) + 160 len 32 * _fromTimes.length] = call.data[_fromTimes + 36 len 32 * _fromTimes.length]
  mem[(32 * _fromTimes.length) + (32 * _investors.length) + 160] = _toTimes.length
  mem[(32 * _fromTimes.length) + (32 * _investors.length) + 192 len 32 * _toTimes.length] = call.data[_toTimes + 36 len 32 * _toTimes.length]
  mem[(32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 192] = _expiryTimes.length
  mem[(32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 224 len 32 * _expiryTimes.length] = call.data[_expiryTimes + 36 len 32 * _expiryTimes.length]
  mem[64] = (32 * _canBuyFromSTO.length) + (32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 256
  mem[(32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 224] = _canBuyFromSTO.length
  mem[(32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 256 len 32 * _canBuyFromSTO.length] = call.data[_canBuyFromSTO + 36 len 32 * _canBuyFromSTO.length]
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  mem[(32 * _canBuyFromSTO.length) + (32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 256] = ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if caller == ext_call.return_data[12 len 20]:
      if _investors.length != _fromTimes.length:
          revert with 0, 'Mismatched input lengths'
      if _fromTimes.length != _toTimes.length:
          revert with 0, 'Mismatched input lengths'
      if _toTimes.length != _expiryTimes.length:
          revert with 0, 'Mismatched input lengths'
      if _canBuyFromSTO.length != _toTimes.length:
          revert with 0, 'Mismatched input length'
      [94midx = 0
      while [94midx < _investors.length:
          require [94midx < mem[96]
          [94m_221 = mem[(32 * [94midx) + 128]
          require [94midx < mem[(32 * _investors.length) + 128]
          [94m_227 = mem[(32 * [94midx) + (32 * _investors.length) + 160]
          require [94midx < mem[(32 * _fromTimes.length) + (32 * _investors.length) + 160]
          [94m_233 = mem[(32 * [94midx) + (32 * _fromTimes.length) + (32 * _investors.length) + 192]
          require [94midx < mem[(32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 192]
          [94m_239 = mem[(32 * [94midx) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 224]
          require [94midx < mem[(32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 224]
          [94m_245 = mem[(32 * [94midx) + (32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 256]
          require ext_code.size(securityTokenAddress)
          call securityTokenAddress.owner() with:
               gas gas_remaining wei
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if caller == addr(ext_call.return_data[0]):
              [94m_266 = mem[64]
              mem[64] = mem[64] + 128
              mem[[94m_266] = mem[(32 * [94midx) + (32 * _investors.length) + 160]
              mem[[94m_266 + 32] = [94m_233
              mem[[94m_266 + 64] = [94m_239
              mem[[94m_266 + 96] = bool([94m_245)
          else:
              if factoryAddress == caller:
                  [94m_296 = mem[64]
                  mem[64] = mem[64] + 128
                  mem[[94m_296] = mem[(32 * [94midx) + (32 * _investors.length) + 160]
                  mem[[94m_296 + 32] = [94m_233
                  mem[[94m_296 + 64] = [94m_239
                  mem[[94m_296 + 96] = bool([94m_245)
              else:
                  require ext_code.size(securityTokenAddress)
                  call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                       gas gas_remaining wei
                      args caller, this.address, 0x57484954454c49535400000000000000000000000000000000000000000000
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if not ext_call.return_data[0]:
                      revert with 0, 'Permission check failed'
                  [94m_326 = mem[64]
                  mem[64] = mem[64] + 128
                  mem[[94m_326] = mem[(32 * [94midx) + (32 * _investors.length) + 160]
                  mem[[94m_326 + 32] = [94m_233
                  mem[[94m_326 + 64] = [94m_239
                  mem[[94m_326 + 96] = bool([94m_245)
          mem[0] = addr([94m_221)
          mem[32] = 5
          whitelist[addr([94m_221)].field_0 = [94m_227
          whitelist[addr([94m_221)].field_256 = [94m_233
          whitelist[addr([94m_221)].field_512 = [94m_239
          whitelist[addr([94m_221)].field_768 = uint8(bool([94m_245))
          mem[mem[64]] = addr([94m_221)
          mem[mem[64] + 32] = block.timestamp
          mem[mem[64] + 64] = caller
          mem[mem[64] + 96] = [94m_227
          mem[mem[64] + 128] = [94m_233
          mem[mem[64] + 160] = [94m_239
          mem[mem[64] + 192] = bool([94m_245)
          log ModifyWhitelist(
                address investor=addr(_221),
                uint256 dateAdded=block.timestamp,
                address addedBy=caller,
                uint256 fromTime=_227,
                uint256 toTime=_233,
                uint256 expiryTime=_239,
                bool canBuyFromSTO=bool(_245))
          [94midx = [94midx + 1
          continue 
  else:
      if factoryAddress == caller:
          if _investors.length != _fromTimes.length:
              revert with 0, 'Mismatched input lengths'
          if _fromTimes.length != _toTimes.length:
              revert with 0, 'Mismatched input lengths'
          if _toTimes.length != _expiryTimes.length:
              revert with 0, 'Mismatched input lengths'
          if _canBuyFromSTO.length != _toTimes.length:
              revert with 0, 'Mismatched input length'
          [94midx = 0
          while [94midx < _investors.length:
              require [94midx < mem[96]
              [94m_223 = mem[(32 * [94midx) + 128]
              require [94midx < mem[(32 * _investors.length) + 128]
              [94m_229 = mem[(32 * [94midx) + (32 * _investors.length) + 160]
              require [94midx < mem[(32 * _fromTimes.length) + (32 * _investors.length) + 160]
              [94m_235 = mem[(32 * [94midx) + (32 * _fromTimes.length) + (32 * _investors.length) + 192]
              require [94midx < mem[(32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 192]
              [94m_241 = mem[(32 * [94midx) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 224]
              require [94midx < mem[(32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 224]
              [94m_246 = mem[(32 * [94midx) + (32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 256]
              require ext_code.size(securityTokenAddress)
              call securityTokenAddress.owner() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if caller == addr(ext_call.return_data[0]):
                  [94m_276 = mem[64]
                  mem[64] = mem[64] + 128
                  mem[[94m_276] = mem[(32 * [94midx) + (32 * _investors.length) + 160]
                  mem[[94m_276 + 32] = [94m_235
                  mem[[94m_276 + 64] = [94m_241
                  mem[[94m_276 + 96] = bool([94m_246)
              else:
                  if factoryAddress == caller:
                      [94m_304 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_304] = mem[(32 * [94midx) + (32 * _investors.length) + 160]
                      mem[[94m_304 + 32] = [94m_235
                      mem[[94m_304 + 64] = [94m_241
                      mem[[94m_304 + 96] = bool([94m_246)
                  else:
                      require ext_code.size(securityTokenAddress)
                      call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                           gas gas_remaining wei
                          args caller, this.address, 0x57484954454c49535400000000000000000000000000000000000000000000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'Permission check failed'
                      [94m_338 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_338] = mem[(32 * [94midx) + (32 * _investors.length) + 160]
                      mem[[94m_338 + 32] = [94m_235
                      mem[[94m_338 + 64] = [94m_241
                      mem[[94m_338 + 96] = bool([94m_246)
              mem[0] = addr([94m_223)
              mem[32] = 5
              whitelist[addr([94m_223)].field_0 = [94m_229
              whitelist[addr([94m_223)].field_256 = [94m_235
              whitelist[addr([94m_223)].field_512 = [94m_241
              whitelist[addr([94m_223)].field_768 = uint8(bool([94m_246))
              mem[mem[64]] = addr([94m_223)
              mem[mem[64] + 32] = block.timestamp
              mem[mem[64] + 64] = caller
              mem[mem[64] + 96] = [94m_229
              mem[mem[64] + 128] = [94m_235
              mem[mem[64] + 160] = [94m_241
              mem[mem[64] + 192] = bool([94m_246)
              log ModifyWhitelist(
                    address investor=addr(_223),
                    uint256 dateAdded=block.timestamp,
                    address addedBy=caller,
                    uint256 fromTime=_229,
                    uint256 toTime=_235,
                    uint256 expiryTime=_241,
                    bool canBuyFromSTO=bool(_246))
              [94midx = [94midx + 1
              continue 
      else:
          mem[(32 * _canBuyFromSTO.length) + (32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 260] = caller
          mem[(32 * _canBuyFromSTO.length) + (32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 292] = this.address
          mem[(32 * _canBuyFromSTO.length) + (32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 324] = 0x57484954454c49535400000000000000000000000000000000000000000000
          require ext_code.size(securityTokenAddress)
          call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
               gas gas_remaining wei
              args caller, this.address, 0x57484954454c49535400000000000000000000000000000000000000000000
          mem[(32 * _canBuyFromSTO.length) + (32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 256] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'Permission check failed'
          if _investors.length != _fromTimes.length:
              revert with 0, 'Mismatched input lengths'
          if _fromTimes.length != _toTimes.length:
              revert with 0, 'Mismatched input lengths'
          if _toTimes.length != _expiryTimes.length:
              revert with 0, 'Mismatched input lengths'
          if _canBuyFromSTO.length != _toTimes.length:
              revert with 0, 'Mismatched input length'
          [94midx = 0
          while [94midx < _investors.length:
              require [94midx < mem[96]
              [94m_225 = mem[(32 * [94midx) + 128]
              require [94midx < mem[(32 * _investors.length) + 128]
              [94m_231 = mem[(32 * [94midx) + (32 * _investors.length) + 160]
              require [94midx < mem[(32 * _fromTimes.length) + (32 * _investors.length) + 160]
              [94m_237 = mem[(32 * [94midx) + (32 * _fromTimes.length) + (32 * _investors.length) + 192]
              require [94midx < mem[(32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 192]
              [94m_243 = mem[(32 * [94midx) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 224]
              require [94midx < mem[(32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 224]
              [94m_247 = mem[(32 * [94midx) + (32 * _expiryTimes.length) + (32 * _toTimes.length) + (32 * _fromTimes.length) + (32 * _investors.length) + 256]
              require ext_code.size(securityTokenAddress)
              call securityTokenAddress.owner() with:
                   gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if caller == addr(ext_call.return_data[0]):
                  [94m_286 = mem[64]
                  mem[64] = mem[64] + 128
                  mem[[94m_286] = mem[(32 * [94midx) + (32 * _investors.length) + 160]
                  mem[[94m_286 + 32] = [94m_237
                  mem[[94m_286 + 64] = [94m_243
                  mem[[94m_286 + 96] = bool([94m_247)
              else:
                  if factoryAddress == caller:
                      [94m_312 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_312] = mem[(32 * [94midx) + (32 * _investors.length) + 160]
                      mem[[94m_312 + 32] = [94m_237
                      mem[[94m_312 + 64] = [94m_243
                      mem[[94m_312 + 96] = bool([94m_247)
                  else:
                      require ext_code.size(securityTokenAddress)
                      call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
                           gas gas_remaining wei
                          args caller, this.address, 0x57484954454c49535400000000000000000000000000000000000000000000
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      if not ext_call.return_data[0]:
                          revert with 0, 'Permission check failed'
                      [94m_350 = mem[64]
                      mem[64] = mem[64] + 128
                      mem[[94m_350] = mem[(32 * [94midx) + (32 * _investors.length) + 160]
                      mem[[94m_350 + 32] = [94m_237
                      mem[[94m_350 + 64] = [94m_243
                      mem[[94m_350 + 96] = bool([94m_247)
              mem[0] = addr([94m_225)
              mem[32] = 5
              whitelist[addr([94m_225)].field_0 = [94m_231
              whitelist[addr([94m_225)].field_256 = [94m_237
              whitelist[addr([94m_225)].field_512 = [94m_243
              whitelist[addr([94m_225)].field_768 = uint8(bool([94m_247))
              mem[mem[64]] = addr([94m_225)
              mem[mem[64] + 32] = block.timestamp
              mem[mem[64] + 64] = caller
              mem[mem[64] + 96] = [94m_231
              mem[mem[64] + 128] = [94m_237
              mem[mem[64] + 160] = [94m_243
              mem[mem[64] + 192] = bool([94m_247)
              log ModifyWhitelist(
                    address investor=addr(_225),
                    uint256 dateAdded=block.timestamp,
                    address addedBy=caller,
                    uint256 fromTime=_231,
                    uint256 toTime=_237,
                    uint256 expiryTime=_243,
                    bool canBuyFromSTO=bool(_247))
              [94midx = [94midx + 1
              continue 


# hash = 0x144b8afa
# getter = ['bool', ['storage', 8, 24, 7]]
# const = None
# payable = False
def allowAllBurnTransfers(): # not payable
  return bool(allowAllBurnTransfers)


# hash = 0x1613ec9d
# getter = None
# const = ['return', 0]
# payable = False
const getInitFunction = 0


# hash = 0x1bb7cc99
# getter = None
# const = ['return', 154214597323535100598731728879190022507949361849447951937806032606295228416]
# payable = False
const WHITELIST = 0x57484954454c49535400000000000000000000000000000000000000000000


# hash = 0x2909a80e
# getter = ['bool', ['storage', 8, 8, 7]]
# const = None
# payable = False
def allowAllWhitelistTransfers(): # not payable
  return bool(allowAllWhitelistTransfers)


# hash = 0x3f0547bb
# getter = None
# const = None
# payable = False
def changeAllowAllTransfers(bool _allowAllTransfers): # not payable
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      if factoryAddress != caller:
          require ext_code.size(securityTokenAddress)
          call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
               gas gas_remaining wei
              args caller, this.address, 0x464c414753000000000000000000000000000000000000000000000000000000
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'Permission check failed'
  allowAllTransfers = uint8(_allowAllTransfers)
  log AllowAllTransfers(bool allowAllTransfers=_allowAllTransfers)


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, 'Sender is not owner'
  if not paused:
      revert with 0, 'Contract is not paused'
  paused = 0
  log Unpause(uint256 timestamp=block.timestamp)


# hash = 0x4caaf45f
# getter = None
# const = None
# payable = False
def changeSigningAddress(address _signingAddress): # not payable
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      if factoryAddress != caller:
          require ext_code.size(securityTokenAddress)
          call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
               gas gas_remaining wei
              args caller, this.address, 0x464c414753000000000000000000000000000000000000000000000000000000
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'Permission check failed'
  signingAddress = _signingAddress
  log ChangeSigningAddress(address signingAddress=_signingAddress)


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 2]]
# const = None
# payable = False
def paused(): # not payable
  return bool(paused)


# hash = 0x5f7619a4
# getter = None
# const = None
# payable = False
def takeFee(uint256 _amount): # not payable
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      if factoryAddress != caller:
          require ext_code.size(securityTokenAddress)
          call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
               gas gas_remaining wei
              args caller, this.address, 'FEE_ADMIN'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'Permission check failed'
  require ext_code.size(factoryAddress)
  call factoryAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(proofTokenAddress)
  call proofTokenAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args securityTokenAddress, addr(ext_call.return_data[0]), _amount
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'Unable to take fee'
  return 1


# hash = 0x7ecc866f
# getter = None
# const = None
# payable = False
def changeAllowAllWhitelistIssuances(bool _allowAllWhitelistIssuances): # not payable
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      if factoryAddress != caller:
          require ext_code.size(securityTokenAddress)
          call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
               gas gas_remaining wei
              args caller, this.address, 0x464c414753000000000000000000000000000000000000000000000000000000
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'Permission check failed'
  Mask(240, 0, stor7.field_16) = Mask(240, 0, _allowAllWhitelistIssuances)
  log AllowAllWhitelistIssuances(bool allowAllWhitelistIssuances=_allowAllWhitelistIssuances)


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      revert with 0, 'Sender is not owner'
  if paused:
      revert with 0, 'Contract is paused'
  paused = 1
  log Pause(uint256 timestammp=block.timestamp)


# hash = 0x9332b62c
# getter = None
# const = None
# payable = False
def changeAllowAllWhitelistTransfers(bool _allowAllWhitelistTransfers): # not payable
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      if factoryAddress != caller:
          require ext_code.size(securityTokenAddress)
          call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
               gas gas_remaining wei
              args caller, this.address, 0x464c414753000000000000000000000000000000000000000000000000000000
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'Permission check failed'
  Mask(248, 0, stor7.field_8) = Mask(248, 0, _allowAllWhitelistTransfers)
  log AllowAllWhitelistTransfers(bool allowAllWhitelistTransfers=_allowAllWhitelistTransfers)


# hash = 0x9728538f
# getter = None
# const = ['return', 31796630314161479358012876999785877093624233240962376764108733155000671272960]
# payable = False
const FLAGS = 0x464c414753000000000000000000000000000000000000000000000000000000


# hash = 0x9b19251a
# getter = ['struct', ['loc', 5]]
# const = None
# payable = False
def whitelist(address _param1): # not payable
  return whitelist[_param1].field_0, 
         whitelist[_param1].field_256,
         whitelist[_param1].field_512,
         bool(whitelist[_param1].field_768)


# hash = 0x9ba0b7c0
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 6]]]]]]
# const = None
# payable = False
def nonceMap(address _param1, uint256 _param2): # not payable
  return bool(stor6[_param1][_param2])


# hash = 0xb1dd8111
# getter = ['bool', ['storage', 8, 0, 7]]
# const = None
# payable = False
def allowAllTransfers(): # not payable
  return bool(allowAllTransfers)


# hash = 0xb3e82dc9
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def signingAddress(): # not payable
  return signingAddress


# hash = 0xb3fac8ce
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def issuanceAddress(): # not payable
  return issuanceAddress


# hash = 0xb84dfbd2
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def securityToken(): # not payable
  return securityTokenAddress


# hash = 0xc3a07df6
# getter = None
# const = ['return', ['data', ['arr', 2, ['mem', ['range', 256, 64]]]]]
# payable = False
const getPermissions = Array(len=2, data=mem[256 len 64])


# hash = 0xc45a0155
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def factory(): # not payable
  return factoryAddress


# hash = 0xd70afa96
# getter = None
# const = ['return', "'FEE_ADMIN'"]
# payable = False
const FEE_ADMIN = 'FEE_ADMIN'


# hash = 0xd7604a78
# getter = None
# const = None
# payable = False
def modifyWhitelist(address _investor, uint256 _fromTime, uint256 _toTime, uint256 _expiryTime, bool _canBuyFromSTO): # not payable
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      if factoryAddress != caller:
          require ext_code.size(securityTokenAddress)
          call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
               gas gas_remaining wei
              args caller, this.address, 0x57484954454c49535400000000000000000000000000000000000000000000
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'Permission check failed'
  whitelist[addr(_investor)].field_0 = _fromTime
  whitelist[addr(_investor)].field_256 = _toTime
  whitelist[addr(_investor)].field_512 = _expiryTime
  whitelist[addr(_investor)].field_768 = uint8(_canBuyFromSTO)
  log ModifyWhitelist(
        address investor=addr(_investor),
        uint256 dateAdded=block.timestamp,
        address addedBy=caller,
        uint256 fromTime=_fromTime,
        uint256 toTime=_toTime,
        uint256 expiryTime=_expiryTime,
        bool canBuyFromSTO=_canBuyFromSTO)


# hash = 0xde6ee1bc
# getter = None
# const = None
# payable = False
def verifyTransfer(address _from, address _to, uint256 _param3, bytes _param4, bool _param5): # not payable
  mem[96] = _param4.length
  mem[128 len _param4.length] = _param4[all]
  if not paused:
      if allowAllTransfers:
          return 2
      if allowAllBurnTransfers:
          if not _to:
              return 2
      if allowAllWhitelistTransfers:
          if whitelist[addr(_to)].field_0:
              if block.timestamp <= whitelist[addr(_to)].field_512:
                  if whitelist[addr(_from)].field_0:
                      if block.timestamp <= whitelist[addr(_from)].field_512:
                          return 2
                  else:
                      if whitelist[addr(_from)].field_256:
                          if block.timestamp <= whitelist[addr(_from)].field_512:
                              return 2
          else:
              if whitelist[addr(_to)].field_256:
                  if block.timestamp <= whitelist[addr(_to)].field_512:
                      if whitelist[addr(_from)].field_0:
                          if block.timestamp <= whitelist[addr(_from)].field_512:
                              return 2
                      else:
                          if whitelist[addr(_from)].field_256:
                              if block.timestamp <= whitelist[addr(_from)].field_512:
                                  return 2
      else:
          if not allowAllWhitelistIssuances:
              if whitelist[addr(_from)].field_0:
                  if block.timestamp <= whitelist[addr(_from)].field_512:
                      if block.timestamp >= whitelist[addr(_from)].field_0:
                          if whitelist[addr(_to)].field_0:
                              if block.timestamp <= whitelist[addr(_to)].field_512:
                                  if block.timestamp >= whitelist[addr(_to)].field_256:
                                      return 2
                          else:
                              if whitelist[addr(_to)].field_256:
                                  if block.timestamp <= whitelist[addr(_to)].field_512:
                                      if block.timestamp >= whitelist[addr(_to)].field_256:
                                          return 2
              else:
                  if whitelist[addr(_from)].field_256:
                      if block.timestamp <= whitelist[addr(_from)].field_512:
                          if block.timestamp >= whitelist[addr(_from)].field_0:
                              if whitelist[addr(_to)].field_0:
                                  if block.timestamp <= whitelist[addr(_to)].field_512:
                                      if block.timestamp >= whitelist[addr(_to)].field_256:
                                          return 2
                              else:
                                  if whitelist[addr(_to)].field_256:
                                      if block.timestamp <= whitelist[addr(_to)].field_512:
                                          if block.timestamp >= whitelist[addr(_to)].field_256:
                                              return 2
          else:
              if issuanceAddress != _from:
                  if whitelist[addr(_from)].field_0:
                      if block.timestamp <= whitelist[addr(_from)].field_512:
                          if block.timestamp >= whitelist[addr(_from)].field_0:
                              if whitelist[addr(_to)].field_0:
                                  if block.timestamp <= whitelist[addr(_to)].field_512:
                                      if block.timestamp >= whitelist[addr(_to)].field_256:
                                          return 2
                              else:
                                  if whitelist[addr(_to)].field_256:
                                      if block.timestamp <= whitelist[addr(_to)].field_512:
                                          if block.timestamp >= whitelist[addr(_to)].field_256:
                                              return 2
                  else:
                      if whitelist[addr(_from)].field_256:
                          if block.timestamp <= whitelist[addr(_from)].field_512:
                              if block.timestamp >= whitelist[addr(_from)].field_0:
                                  if whitelist[addr(_to)].field_0:
                                      if block.timestamp <= whitelist[addr(_to)].field_512:
                                          if block.timestamp >= whitelist[addr(_to)].field_256:
                                              return 2
                                  else:
                                      if whitelist[addr(_to)].field_256:
                                          if block.timestamp <= whitelist[addr(_to)].field_512:
                                              if block.timestamp >= whitelist[addr(_to)].field_256:
                                                  return 2
              else:
                  mem[0] = _to
                  mem[32] = 5
                  if whitelist[addr(_to)].field_768:
                      if whitelist[addr(_to)].field_0:
                          if block.timestamp <= whitelist[addr(_to)].field_512:
                              return 2
                      else:
                          if whitelist[addr(_to)].field_256:
                              if block.timestamp <= whitelist[addr(_to)].field_512:
                                  return 2
                  else:
                      mem[ceil32(_param4.length) + 128] = 0xac90b42200000000000000000000000000000000000000000000000000000000
                      mem[ceil32(_param4.length) + 132] = 3
                      require ext_code.size(securityTokenAddress)
                      call securityTokenAddress.0xac90b422 with:
                           gas gas_remaining wei
                          args 3
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      mem[ceil32(_param4.length) + 128 len return_data.size] = ext_call.return_data[0 len return_data.size]
                      mem[64] = ceil32(_param4.length) + ceil32(return_data.size) + 128
                      require return_data.size >= 32
                      require mem[ceil32(_param4.length) + 128 len 4], 0 <= 4294967296
                      require mem[ceil32(_param4.length) + 128 len 4], 0 + 32 <= return_data.size
                      require mem[ceil32(_param4.length) + mem[ceil32(_param4.length) + 128 len 4], 0 + 128] <= 4294967296 and mem[ceil32(_param4.length) + 128 len 4], 0 + (32 * mem[ceil32(_param4.length) + mem[ceil32(_param4.length) + 128 len 4], 0 + 128]) + 32 <= return_data.size
                      if mem[ceil32(_param4.length) + mem[ceil32(_param4.length) + 128 len 4], 0 + 128] <= 0:
                          if whitelist[addr(_to)].field_0:
                              if block.timestamp <= whitelist[addr(_to)].field_512:
                                  return 2
                          else:
                              if whitelist[addr(_to)].field_256:
                                  if block.timestamp <= whitelist[addr(_to)].field_512:
                                      return 2
  return 1


# hash = 0xe0c68158
# getter = None
# const = None
# payable = False
def changeIssuanceAddress(address _issuanceAddress): # not payable
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      if factoryAddress != caller:
          require ext_code.size(securityTokenAddress)
          call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
               gas gas_remaining wei
              args caller, this.address, 0x464c414753000000000000000000000000000000000000000000000000000000
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'Permission check failed'
  issuanceAddress = _issuanceAddress
  log ChangeIssuanceAddress(address issuanceAddress=_issuanceAddress)


# hash = 0xe55d0f8b
# getter = ['bool', ['storage', 8, 16, 7]]
# const = None
# payable = False
def allowAllWhitelistIssuances(): # not payable
  return bool(allowAllWhitelistIssuances)


# hash = 0xe8a28d52
# getter = None
# const = None
# payable = False
def changeAllowAllBurnTransfers(bool _allowAllBurnTransfers): # not payable
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != caller:
      if factoryAddress != caller:
          require ext_code.size(securityTokenAddress)
          call securityTokenAddress.checkPermission(address delegate, address module, bytes32 perm) with:
               gas gas_remaining wei
              args caller, this.address, 0x464c414753000000000000000000000000000000000000000000000000000000
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_call.return_data[0]:
              revert with 0, 'Permission check failed'
  Mask(232, 0, stor7.field_24) = Mask(232, 0, _allowAllBurnTransfers)
  log AllowAllBurnTransfers(bool allowAllBurnTransfers=_allowAllBurnTransfers)


# hash = 0xf5c19231
# getter = None
# const = None
# payable = False
def modifyWhitelistSigned(address _investor, uint256 _fromTime, uint256 _toTime, uint256 _expiryTime, bool _canBuyFromSTO, uint256 _validFrom, uint256 _validTo, uint256 _nonce, uint8 _v, bytes32 _r, bytes32 _s): # not payable
  if _validFrom > block.timestamp:
      revert with 0, 'ValidFrom is too early'
  if _validTo < block.timestamp:
      revert with 0, 'ValidTo is too late'
  if stor6[addr(_investor)][_nonce]:
      revert with 0, 'Already used signature'
  stor6[addr(_investor)][_nonce] = 1
  [94msigner = erecover(sha3(Mask(224, 32, '\x19Ethereum Signed Message:\n32') >> 32, sha3(this.address, _investor, _fromTime, _toTime, _expiryTime, uint8(_canBuyFromSTO), _validFrom, _validTo, Mask(184, 72, _nonce) >> 72, mem[585 len 9])), _v << 248, _r, _s) # precompiled
  if not erecover.result:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(securityTokenAddress)
  call securityTokenAddress.owner() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data[12 len 20] != addr([94msigner):
      if signingAddress != addr([94msigner):
          revert with 0, 'Incorrect signer'
  whitelist[addr(_investor)].field_0 = _fromTime
  whitelist[addr(_investor)].field_256 = _toTime
  whitelist[addr(_investor)].field_512 = _expiryTime
  whitelist[addr(_investor)].field_768 = uint8(_canBuyFromSTO)
  log ModifyWhitelist(
        address investor=addr(_investor),
        uint256 dateAdded=block.timestamp,
        address addedBy=caller,
        uint256 fromTime=_fromTime,
        uint256 toTime=_toTime,
        uint256 expiryTime=_expiryTime,
        bool canBuyFromSTO=_canBuyFromSTO)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


