# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x0Cf30Af24ae5Ac65Ed12AF5cf3E32Ecf88658295 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0x21c8ad0e': 'unknown21c8ad0e(?)', '0x321dff17': 'unknown321dff17(?)', '0x40398d67': 'unknown40398d67(?)', '0x63808bcb': 'unknown63808bcb(?)', '0x6658076c': 'unknown6658076c(?)', '0x8f9bbf16': 'getSecurityTokenData(address _securityToken)', '0x92042aee': 'unknown92042aee(?)', '0x972b3ab5': 'unknown972b3ab5(?)', '0xc37792b5': 'generateSecurityToken(string _name, string _symbol, string _tokenDetails, bool _divisible)', '0xd0f6fe42': 'unknownd0f6fe42(?)', '0xd2d10162': 'initialize(address _att, address _attController, uint256 _startTime, uint256 _endTime, address _destEthFoundation, address _destTokensAngel)', '0xd3623f98': 'unknownd3623f98(?)', '0xea470758': 'unknownea470758(?)'} 

# storage definitions
def storage:
    # storage address 0
    unknown165e694a
    # storage address 1
    unknown69ba0fe9
    # storage address 2
    owner
    # storage address 3
    unknownc6cb7ab8
    # storage address 4
    stor4
    # storage address 6
    unknownb3447ac9
# hash = 0x165e694a
# getter = ['storage', 256, 0, ['sha3', ['data', 170075661918629844815851105886566911349217843940851048309366337247487439034, 0]]]
# const = None
# payable = False
def unknown165e694a(): # not payable
  return unknown165e694a[0x604268e9a73dfd777dcecb8a614493dd65c638bad2f5e7d709d378bd2fb0ba]


# hash = 0x1d8acf1b
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 4], 4]]]]
# const = None
# payable = False
def unknown1d8acf1b(uint256 _param1): # not payable
  return bool(stor4[_param1])


# hash = 0x208b080f
# getter = None
# const = None
# payable = False
def changeExpiryLimit(uint256 _newExpiry): # not payable
  if owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040] != caller:
      revert with 0, 'sender must be owner'
  if _newExpiry < 24 * 3600:
      revert with 0, 'Expiry should >= 1 day'
  log 0x7e1cc0e6: unknown165e694a[0x604268e9a73dfd777dcecb8a614493dd65c638bad2f5e7d709d378bd2fb0ba], _newExpiry
  unknown165e694a[0x604268e9a73dfd777dcecb8a614493dd65c638bad2f5e7d709d378bd2fb0ba] = _newExpiry


# hash = 0x26839e53
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 0]]]
# const = None
# payable = False
def unknown26839e53(uint256 _param1): # not payable
  return unknown165e694a[_param1]


# hash = 0x33ce93fe
# getter = None
# const = ['return', ['data', ['arr', 3, ['mem', ['range', 397, 96]]]]]
# payable = False
const unknown33ce93fe = Array(len=3, data=mem[397 len 96])


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  if not stor4[0xee35723ac350a69d2a92d3703f17439cbaadf2f093a21ba5bf5f1a53eb2a14]:
      revert with 0, 'Should not be paused'
  if owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040] != caller:
      revert with 0, 'sender must be owner'
  stor4[0xee35723ac350a69d2a92d3703f17439cbaadf2f093a21ba5bf5f1a53eb2a14] = 0
  log Unpause(uint256 timestamp=block.timestamp)


# hash = 0x42c2e551
# getter = None
# const = None
# payable = False
def unknown42c2e551(uint256 _param1): # not payable
  if owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040] != caller:
      revert with 0, 'sender must be owner'
  if unknown165e694a[0xeed677304bb45536bb7fdfa6b9e47a3c58fe413f9e8f01474b0a4b9c6e0275ba] == _param1:
      revert with 0, 'Fee not changed'
  log 0x82ce758a: unknown165e694a[0xeed677304bb45536bb7fdfa6b9e47a3c58fe413f9e8f01474b0a4b9c6e0275ba], _param1
  unknown165e694a[0xeed677304bb45536bb7fdfa6b9e47a3c58fe413f9e8f01474b0a4b9c6e0275ba] = _param1


# hash = 0x69ba0fe9
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 1]]]]], ['sha3', ['data', ['cd', 4], 1]]]]
# const = None
# payable = False
def unknown69ba0fe9(uint256 _param1): # not payable
  return unknown69ba0fe9[_param1][0 len unknown69ba0fe9[_param1].length].field_0


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  if stor4[0xee35723ac350a69d2a92d3703f17439cbaadf2f093a21ba5bf5f1a53eb2a14]:
      revert with 0, 'Already paused'
  if owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040] != caller:
      revert with 0, 'sender must be owner'
  stor4[0xee35723ac350a69d2a92d3703f17439cbaadf2f093a21ba5bf5f1a53eb2a14] = 1
  log Pause(uint256 timestammp=block.timestamp)


# hash = 0x8905fd4f
# getter = None
# const = None
# payable = False
def reclaimERC20(address _tokenContract): # not payable
  if owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040] != caller:
      revert with 0, 'sender must be owner'
  if not _tokenContract:
      revert with 0, 32, 15, 0xf2496e76616c6964206164647265737300000000000000000000000000000000
  require ext_code.size(_tokenContract)
  call _tokenContract.balanceOf(address owner) with:
       gas gas_remaining wei
      args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(_tokenContract)
  call _tokenContract.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040], ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      revert with 0, 'Transfer failed'


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, ['sha3', ['data', 3543405465270413569032054694310270319370463098018662126445904479033000000, 2]]]
# const = None
# payable = False
def owner(): # not payable
  return owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040]


# hash = 0x959346ae
# getter = None
# const = None
# payable = False
def unknown959346ae(uint256 _param1): # not payable
  if owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040] != caller:
      revert with 0, 'sender must be owner'
  if unknown165e694a[0xd92fcc69711628630fb5a42566c68bd1092bc4aa26826736293969fddcd11cb2] == _param1:
      revert with 0, 'Fee not changed'
  log 0x788dceb0: unknown165e694a[0xd92fcc69711628630fb5a42566c68bd1092bc4aa26826736293969fddcd11cb2], _param1
  unknown165e694a[0xd92fcc69711628630fb5a42566c68bd1092bc4aa26826736293969fddcd11cb2] = _param1


# hash = 0xb187bd26
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', 420878473596016290336356389275327783331751575833935589093925673151268334100, 4]]]]
# const = None
# payable = False
def isPaused(): # not payable
  return bool(stor4[0xee35723ac350a69d2a92d3703f17439cbaadf2f093a21ba5bf5f1a53eb2a14])


# hash = 0xb3447ac9
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def unknownb3447ac9(uint256 _param1): # not payable
  return unknownb3447ac9[_param1]


# hash = 0xbaed8bb1
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 2]]]
# const = None
# payable = False
def unknownbaed8bb1(uint256 _param1): # not payable
  return owner[_param1]


# hash = 0xc6cb7ab8
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['sha3', ['data', ['cd', 4], 3]]]]], ['sha3', ['data', ['cd', 4], 3]]]]
# const = None
# payable = False
def unknownc6cb7ab8(uint256 _param1): # not payable
  return unknownc6cb7ab8[_param1][0 len unknownc6cb7ab8[_param1].length]


# hash = 0xc75948f5
# getter = ['storage', 256, 0, ['sha3', ['data', 108029385844545289293219364189185231752374841221023424905644286862225372771770, 0]]]
# const = None
# payable = False
def unknownc75948f5(): # not payable
  return unknown165e694a[0xeed677304bb45536bb7fdfa6b9e47a3c58fe413f9e8f01474b0a4b9c6e0275ba]


# hash = 0xd300a968
# getter = None
# const = None
# payable = False
def isSecurityToken(address _securityToken): # not payable
  mem[192 len 0] = None
  mem[265] = unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].field_0
  [94midx = 265
  [94ms = 0
  while unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length + 233 > [94midx:
      mem[[94midx + 32] = unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[ceil32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length) + 265 len floor32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length)] = mem[265 len floor32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length)]
  mem[ceil32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length) + floor32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length) + 265] = mem[ceil32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length) + floor32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length) + 265] and 256^(-unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length % 32 + 32) - 1 or mem[floor32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length) + 265] and !(256^(-unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length % 32 + 32) - 1)
  mem[ceil32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length) + 265] = sha3(mem[ceil32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length) + 265 len unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length]) != 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470
  return memory
    from ceil32(unknown69ba0fe9[mem[192 len 11]][Mask(80, 88, 'securityTokens_ticker') >> 88][_securityToken].length) + 265
     [93mlen 32


# hash = 0xe1ecae9e
# getter = ['storage', 256, 0, ['sha3', ['data', 98236340753571939799283840466987927730231466894258916889683281976589286448306, 0]]]
# const = None
# payable = False
def unknowne1ecae9e(): # not payable
  return unknown165e694a[0xd92fcc69711628630fb5a42566c68bd1092bc4aa26826736293969fddcd11cb2]


# hash = 0xe6ff950b
# getter = None
# const = None
# payable = False
def unknowne6ff950b(addr _param1): # not payable
  if owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040] != caller:
      revert with 0, 'sender must be owner'
  if not _param1:
      revert with 0, 32, 15, 0xf2496e76616c6964206164647265737300000000000000000000000000000000
  owner[0xacf8fbd51bb4b83ba426cdb12f63be74db97c412515797993d2a385542e311] = _param1


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  if owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040] != caller:
      revert with 0, 'sender must be owner'
  if not _newOwner:
      revert with 0, 32, 15, 0xf2496e76616c6964206164647265737300000000000000000000000000000000
  log OwnershipTransferred(
        address previousOwner=owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040],
        address newOwner=_newOwner)
  owner[0x2016836a56b71f0d02689e69e326f4f4c1b9057164ef592671cf0d37c8040] = _newOwner


# hash = 0xfb621f14
# getter = None
# const = None
# payable = False
def getSecurityTokenAddress(string _symbol): # not payable
  mem[64] = ceil32(_symbol.length) + 128
  mem[96] = _symbol.length
  mem[128 len _symbol.length] = _symbol[all]
  [94ms = 0
  [94midx = 0
  while [94midx < _symbol.length:
      require [94midx < _symbol.length
      [94m_44 = mem[[94midx + 128]
      require [94midx < _symbol.length
      if Mask(8, 248, mem[[94midx + 128]) < 'a':
          mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
          [94ms = Mask(8, 248, [94m_44)
          [94midx = [94midx + 1
          continue 
      if Mask(8, 248, mem[[94midx + 128]) > 'z':
          mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) + 256, 0) << (('mask_shl', 8, 248, -3, ('mem', ('range', ('add', 128, ('var', 0)), 32))), 0) - 256
          [94ms = Mask(8, 248, [94m_44)
          [94midx = [94midx + 1
          continue 
      mem[[94midx + 128 len 8] = Mask(8, -(('mask_shl', 8, 0, 245, ('add', -32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) + 256, 0) << (('mask_shl', 8, 0, 245, ('add', -32, ('mem', ('range', ('add', 128, ('var', 0)), 1)))), 0) - 256
      [94ms = (Mask(8, 248, [94m_44) >> 248) - 32 << 248
      [94midx = [94midx + 1
      continue 
  [94m_41 = mem[64]
  mem[64] = mem[64] + 64
  mem[[94m_41] = 21
  mem[[94m_41 + 32] = 0xd77469636b6572546f5365637572697479546f6b656e00000000000000000000
  [94m_45 = mem[64]
  mem[mem[64] + 32 len 0] = None
  mem[mem[64] + 32 len 21] = 0xd77469636b6572546f5365637572697479546f6b65
  [94m_78 = mem[96]
  mem[mem[64] + 53 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  mem[mem[64] + floor32(mem[96]) + -(mem[96] % 32) + 85 len mem[96] % 32] = mem[floor32(mem[96]) + -(mem[96] % 32) + 160 len mem[96] % 32]
  [94m_104 = mem[64]
  mem[mem[64]] = [94m_78 + [94m_45 + -mem[64] + 21
  mem[64] = [94m_78 + [94m_45 + 53
  [94m_106 = mem[[94m_104]
  if mem[[94m_104] < 32:
      mem[[94m_78 + [94m_45 + 53] = mem[[94m_78 + [94m_45 + 53] and 256^(-mem[[94m_104] + 32) - 1 or mem[[94m_104 + 32] and !(256^(-mem[[94m_104] + 32) - 1)
      return owner[mem[[94m_78 + [94m_45 + 53 len [94m_106]]
  mem[[94m_78 + [94m_45 + 53] = mem[[94m_104 + 32]
  mem[[94m_78 + [94m_45 + 85 len floor32([94m_106 - 32)] = mem[[94m_104 + 64 len floor32([94m_106 - 32)]
  mem[[94m_78 + [94m_45 + floor32([94m_106 - 32) + 85] = mem[[94m_78 + [94m_45 + floor32([94m_106 - 32) + 85] and 256^(-[94m_106 + floor32([94m_106 - 32) + 64) - 1 or mem[[94m_104 + floor32([94m_106 - 32) + 64] and !(256^(-[94m_106 + floor32([94m_106 - 32) + 64) - 1)
  mem[[94m_78 + [94m_45 + 53] = owner[mem[[94m_78 + [94m_45 + 53 len [94m_106]]
  return memory
    from [94m_78 + [94m_45 + 53
     [93mlen 32


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


