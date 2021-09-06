# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x5D614C707c5f891B9A21D2394eA13B0DE903664E 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    MAX_MARKETING_TOKENS # mask: a s
    # storage address 1
    stor1
    # storage address 2
    stor2
    # storage address 3
    ceoAddress # mask: a s
    # storage address 4
    cfoAddress # mask: a s
    # storage address 5
    cooAddress # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 6
    commissionerAddress # mask: a s
    # storage address 6
    stor6 # mask: a s
    # storage address 7
    minterContractAddress # mask: a s
    # storage address 9
    md5TokenToRosterIndex
    # storage address 99
    stor99
    # storage address 110349606679412691172957834289542550319383271247755660854362242977991410020068
    stor110349606679412691172957834289542550319383271247755660854362242977991410020068
    # storage address 110349606679412691172957834289542550319383271247755660854362242977991410020069
    stor110349606679412691172957834289542550319383271247755660854362242977991410020069
# hash = 0x0519ce79
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def cfoAddress(): # not payable
  return mcfoAddress


# hash = 0x0a0f8168
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def ceoAddress(): # not payable
  return mceoAddress


# hash = 0x13e8360d
# getter = None
# const = None
# payable = False
def commissionerAuctionComplete(uint32 m_rosterIndex, uint128 m_price): # not payable
  require caller == mminterContractAddress
  require m_rosterIndex < mrealWorldPlayersm.length
  require uint8(mrealWorldPlayersm[m_rosterIndexm]m.field_352)
  if not uint128(mrealWorldPlayersm[m_rosterIndexm]m.field_128):
      uint128(mrealWorldPlayersm[m_rosterIndexm]m.field_128) = m_price
  else:
      Mask(127, 0, mrealWorldPlayersm[m_rosterIndexm]m.field_128) = uint128(m_price + uint128(mrealWorldPlayersm[m_rosterIndexm]m.field_128)) / 2
      bool(mrealWorldPlayersm[m_rosterIndexm]m.field_255) = 0
  uint8(mrealWorldPlayersm[m_rosterIndexm]m.field_352) = 0
  if bool(uint8(mrealWorldPlayersm[m_rosterIndexm]m.field_360)) or False:
      mem[324 len 0] = None
      require ext_code.size(mminterContractAddress)
      call mminterContractAddress.mintPlayers(uint128[] md5Tokens, uint256 startPrice, uint256 endPrice, uint256 duration) with:
           gas gas_remaining wei
          args 128, 0, 0, 0, 1, mem[324]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]


# hash = 0x1567be3e
# getter = None
# const = None
# payable = False
def setCoreContractAddress(address m_address): # not payable
  require caller == mceoAddress
  require ext_code.size(m_address)
  call m_address.isMinter() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mminterContractAddress = m_address


# hash = 0x18a9f29f
# getter = None
# const = None
# payable = False
def setMetadata(uint128 m_md5Token, string m_metadata): # not payable
  require caller == mcommissionerAddress
  if mmd5TokenToRosterIndexm[m_md5Token << 128m] > 0:
      require mmd5TokenToRosterIndexm[m_md5Token << 128m] < mrealWorldPlayersm.length
      mstor[sha3((3 * mstor9m[m_md5Token << 128m]) + ('name', 'realWorldPlayers', 8) + 2)m]m[m]m.field_0 = Array(len=m_metadata.length, data=m_metadata[allm])
  else:
      if 0 < mrealWorldPlayersm.length:
          if uint128(mrealWorldPlayersm.field_0) == m_md5Token:
              require mmd5TokenToRosterIndexm[m_md5Token << 128m] < mrealWorldPlayersm.length
              mstor[sha3((3 * mstor9m[m_md5Token << 128m]) + ('name', 'realWorldPlayers', 8) + 2)m]m[m]m.field_0 = Array(len=m_metadata.length, data=m_metadata[allm])


# hash = 0x19d375f1
# getter = None
# const = ['return', 1]
# payable = False
const isLeagueRosterContract = 1


# hash = 0x1cc14cbc
# getter = ['bool', ['storage', 8, 168, 6]]
# const = None
# payable = False
def isDevelopment(): # not payable
  return bool(uint8(mstor6m.field_168))


# hash = 0x240860f1
# getter = None
# const = None
# payable = False
def setHasCommissionerAuction(uint32 m_rosterIndex): # not payable
  require caller == mminterContractAddress
  require m_rosterIndex < mrealWorldPlayersm.length
  require not uint8(mrealWorldPlayersm[m_rosterIndexm]m.field_352)
  uint8(mrealWorldPlayersm[m_rosterIndexm]m.field_352) = 1


# hash = 0x27d7874c
# getter = None
# const = None
# payable = False
def setCEO(address m_newCEO): # not payable
  require caller == mceoAddress
  require m_newCEO
  mceoAddress = m_newCEO


# hash = 0x2ba73c15
# getter = None
# const = None
# payable = False
def setCOO(address m_newCOO): # not payable
  require caller == mceoAddress
  require m_newCOO
  mcooAddress = m_newCOO


# hash = 0x2e43ec0c
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def commissionerAddress(): # not payable
  return mcommissionerAddress


# hash = 0x302bcc57
# getter = ['storage', 32, 0, 8]
# const = None
# payable = False
def playerCount(): # not payable
  return uint32(mrealWorldPlayersm.length)


# hash = 0x334e712f
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def COMMISSIONER_AUCTION_DURATION(): # not payable
  return mstor2m.length


# hash = 0x36e685f5
# getter = None
# const = None
# payable = False
def setCLevelAddresses(address m_ceo, address m_cfo, address m_coo, address m_commish): # not payable
  require caller == mceoAddress
  require m_ceo
  require m_cfo
  require m_coo
  require m_commish
  mceoAddress = m_ceo
  mcfoAddress = m_cfo
  mcooAddress = m_coo
  mcommissionerAddress = m_commish


# hash = 0x390209c1
# getter = None
# const = None
# payable = False
def getMetadata(uint128 m_md5Token): # not payable
  if mmd5TokenToRosterIndexm[m_md5Token << 128m] <= 0:
      if 0 >= mrealWorldPlayersm.length:
          return ''
      if uint128(mrealWorldPlayersm.field_0) != m_md5Token:
          return ''
  require mmd5TokenToRosterIndexm[m_md5Token << 128m] < mrealWorldPlayersm.length
  mem[128] = mstor[sha3((3 * mstor9m[m_md5Token << 128m]) + ('name', 'realWorldPlayers', 8) + 2)m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile mstor[(3 * mstor9m[m_md5Token << 128m]) + ('name', 'realWorldPlayers', 8) + 2m]m.length + 96 > [94midxm:
      mem[[94midx + 32] = mstor[[94ms + sha3((3 * mstor9m[m_md5Token << 128m]) + ('name', 'realWorldPlayers', 8) + 2)m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return Array(len=mstor[(3 * mstor9m[m_md5Token << 128m]) + ('name', 'realWorldPlayers', 8) + 2m]m.length, data=mem[128 len mstor[(3 * mstor9m[m_md5Token << 128m]) + ('name', 'realWorldPlayers', 8) + 2m]m.length]), 


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == mceoAddress
  require uint8(mstor6m.field_160)
  uint8(mstor6m.field_160) = 0


# hash = 0x4e0a3379
# getter = None
# const = None
# payable = False
def setCFO(address m_newCFO): # not payable
  require caller == mceoAddress
  require m_newCFO
  mcfoAddress = m_newCFO


# hash = 0x4e0c4a9c
# getter = None
# const = None
# payable = False
def setCommissioner(address m_newCommissioner): # not payable
  require caller == mceoAddress
  require m_newCommissioner
  mcommissionerAddress = m_newCommissioner


# hash = 0x4edf9785
# getter = ['storage', 32, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = False
def md5TokenToRosterIndex(uint128 m_param1): # not payable
  return mmd5TokenToRosterIndexm[m_param1m]


# hash = 0x54367179
# getter = None
# const = None
# payable = False
def updateRealWorldPlayer(uint32 m_rosterIndex, uint128 m_prevCommissionerSalePrice, uint64 m_lastMintedTime, uint32 m_mintedCount, bool m_hasActiveCommissionerAuction, bool m_mintingEnabled): # not payable
  require caller == mminterContractAddress
  require m_rosterIndex < mrealWorldPlayersm.length
  uint128(mrealWorldPlayersm[m_rosterIndexm]m.field_128) = m_prevCommissionerSalePrice
  uint64(mrealWorldPlayersm[m_rosterIndexm]m.field_256) = m_lastMintedTime
  uint32(mrealWorldPlayersm[m_rosterIndexm]m.field_320) = m_mintedCount
  uint8(mrealWorldPlayersm[m_rosterIndexm]m.field_352) = uint8(m_hasActiveCommissionerAuction)
  Mask(152, 0, mrealWorldPlayersm[m_rosterIndexm]m.field_360) = Mask(152, 0, m_mintingEnabled)
  Mask(144, 0, mrealWorldPlayersm[m_rosterIndexm]m.field_368) = Mask(144, 16, m_hasActiveCommissionerAuction) >> 16


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 6]]
# const = None
# payable = False
def paused(): # not payable
  return bool(uint8(mstor6m.field_160))


# hash = 0x5fd8c710
# getter = None
# const = None
# payable = False
def withdrawBalance(): # not payable
  require caller == mcfoAddress
  call mcfoAddress with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x632f83eb
# getter = ['struct', ['loc', 8]]
# const = None
# payable = False
def realWorldPlayerFromIndex(uint128 m_idx): # not payable
  require m_idx < mrealWorldPlayersm.length
  [94midx = 576
  [94ms = 0
  mwhile mstor[('name', 'realWorldPlayers', 8) + (3 * m_idx) + 2m]m.length + 544 > [94midxm:
      mem[[94midx + 32] = mstor[[94ms + sha3(('name', 'realWorldPlayers', 8) + (3 * m_idx) + 2)m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return uint128(mrealWorldPlayersm[m_idxm]m.field_0), 
         uint128(mrealWorldPlayersm[m_idxm]m.field_0),
         uint64(mrealWorldPlayersm[m_idxm]m.field_256),
         uint32(mrealWorldPlayersm[m_idxm]m.field_256),
         bool(uint8(mrealWorldPlayersm[m_idxm]m.field_352)),
         bool(uint8(mrealWorldPlayersm[m_idxm]m.field_360))


# hash = 0x70ffffec
# getter = ['storage', 16, 0, 0]
# const = None
# payable = False
def MAX_MARKETING_TOKENS(): # not payable
  return mMAX_MARKETING_TOKENS


# hash = 0x778b09ce
# getter = ['struct', ['loc', 8]]
# const = None
# payable = False
def realWorldPlayers(uint256 m_param1): # not payable
  require m_param1 < mrealWorldPlayersm.length
  mem[128] = mstor[sha3((3 * m_param1) + ('name', 'realWorldPlayers', 8) + 2)m]m.field_0
  [94midx = 128
  [94ms = 0
  mwhile mstor[(3 * m_param1) + ('name', 'realWorldPlayers', 8) + 2m]m.length + 96 > [94midxm:
      mem[[94midx + 32] = mstor[[94ms + sha3((3 * m_param1) + ('name', 'realWorldPlayers', 8) + 2)m]m.field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      mcontinue 
  return uint128(mrealWorldPlayersm[m_param1m]m.field_0), 
         uint128(mrealWorldPlayersm[m_param1m]m.field_0),
         uint64(mrealWorldPlayersm[m_param1m]m.field_256),
         uint32(mrealWorldPlayersm[m_param1m]m.field_256),
         bool(uint8(mrealWorldPlayersm[m_param1m]m.field_352)),
         bool(uint8(mrealWorldPlayersm[m_param1m]m.field_360)),
         Array(len=mstor[(3 * m_param1) + ('name', 'realWorldPlayers', 8) + 2m]m.length, data=mem[128 len mstor[(3 * m_param1) + ('name', 'realWorldPlayers', 8) + 2m]m.length])


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  if mcooAddress != caller:
      if mceoAddress != caller:
          if mcfoAddress != caller:
              require caller == mcommissionerAddress
  require not uint8(mstor6m.field_160)
  uint8(mstor6m.field_160) = 1


# hash = 0x886ed2d1
# getter = None
# const = None
# payable = False
def enableRealWorldPlayerMinting(uint128[] m_md5Tokens, bool[] m_mintingEnabled): # not payable
  mem[128 len 32 * m_md5Tokens.length] = call.data[m_md5Tokens + 36 len 32 * m_md5Tokens.length]
  mem[(32 * m_md5Tokens.length) + 128] = m_mintingEnabled.length
  mem[(32 * m_md5Tokens.length) + 160 len 32 * m_mintingEnabled.length] = call.data[m_mintingEnabled + 36 len 32 * m_mintingEnabled.length]
  require caller == mcommissionerAddress
  require m_md5Tokens.length == m_mintingEnabled.length
  [94ms = 0
  [94midx = 0
  mwhile uint32([94midx) < m_md5Tokens.lengthm:
      require uint32([94midx) < m_md5Tokens.length
      mem[32] = 9
      if mmd5TokenToRosterIndexm[mem[(32 * uint32([94midx)) + 144 len 16]m] <= 0:
          require 0 < mrealWorldPlayersm.length
          require uint32([94midx) < m_md5Tokens.length
          require 0 < mrealWorldPlayersm.length
          require uint128(mrealWorldPlayersm.field_0) == mem[(32 * uint32([94midx)) + 144 len 16]
      require uint32([94midx) < m_mintingEnabled.length
      require mmd5TokenToRosterIndexm[mem[(32 * uint32([94midx)) + 144 len 16]m] < mrealWorldPlayersm.length
      mem[0] = 8
      Mask(152, 0, mrealWorldPlayersm[mstor9m[mem[(32 * uint32([94midx)) + 144 len 16]m]m]m.field_360) = Mask(152, 0, bool(mem[(32 * uint32([94midx)) + (32 * m_md5Tokens.length) + 160]))
      [94ms = mmd5TokenToRosterIndexm[mem[(32 * uint32([94midx)) + 144 len 16]m]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x8b52463a
# getter = None
# const = None
# payable = False
def commissionerAuctionCancelled(uint32 m_rosterIndex): # not payable
  require caller == mminterContractAddress
  require m_rosterIndex < mrealWorldPlayersm.length
  require uint8(mrealWorldPlayersm[m_rosterIndexm]m.field_352)


# hash = 0x8f835871
# getter = None
# const = None
# payable = False
def addRealWorldPlayers(uint128[] m_md5Tokens, bool[] m_mintingEnabled): # not payable
  mem[96] = m_md5Tokens.length
  mem[128 len 32 * m_md5Tokens.length] = call.data[m_md5Tokens + 36 len 32 * m_md5Tokens.length]
  mem[(32 * m_md5Tokens.length) + 128] = m_mintingEnabled.length
  mem[(32 * m_md5Tokens.length) + 160 len 32 * m_mintingEnabled.length] = call.data[m_mintingEnabled + 36 len 32 * m_mintingEnabled.length]
  mem[64] = (32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 384
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 160] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 192] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 224] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 256] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 288] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 320] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 352] = 96
  require caller == mcommissionerAddress
  require m_md5Tokens.length == m_mintingEnabled.length
  [94ms = 0
  [94mt = (32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 160
  [94midx = 0
  mwhile uint32([94midx) < m_md5Tokens.lengthm:
      if not mrealWorldPlayersm.length:
          [94m_67 = mem[64]
          mem[64] = mem[64] + 224
          require uint32([94midx) < mem[96]
          mem[[94m_67] = mem[(32 * uint32([94midx)) + 144 len 16]
          mem[[94m_67 + 32] = 0
          mem[[94m_67 + 64] = 0
          mem[[94m_67 + 96] = 0
          mem[[94m_67 + 128] = 0
          require uint32([94midx) < mem[(32 * m_md5Tokens.length) + 128]
          mem[[94m_67 + 160] = bool(mem[(32 * uint32([94midx)) + (32 * m_md5Tokens.length) + 160])
          [94m_75 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_75] = 0
          mem[[94m_67 + 192] = [94m_75
          mrealWorldPlayersm.length++
          mem[0] = 8
          uint128(mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_0) = mem[[94m_67 + 16 len 16]
          uint128(mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_128) = 0
          mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_256 % 1 = 0
          Mask(96, 0, mstorF3F7m[mstor8m.lengthm]m.field_0) = 0
          uint8(mstorF3F7m[mstor8m.lengthm]m.field_96) = 0
          Mask(152, 0, mstorF3F7m[mstor8m.lengthm]m.field_104) = Mask(152, 0, bool(mem[[94m_67 + 160]))
          Mask(144, 0, mstorF3F7m[mstor8m.lengthm]m.field_112) = 0
          mstorF3F7m[mstor8m.lengthm]m.field_256 % 1 = 0
          mstorF3F7m[mstor8m.lengthm]m.field_256 % 1 = 0
          bool(mstorF3F7m[mstor8m.lengthm]m.field_0) = 0
          uint255(mstorF3F7m[mstor8m.lengthm]m.field_1) = 0
          Mask(248, 0, mstorF3F7m[mstor8m.lengthm]m.field_8) = mem[[94m_75 + 32 len 31]
          [94ms = sha3((3 * mrealWorldPlayersm.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911b)
          mwhile sha3((3 * mrealWorldPlayersm.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911b) + (mstor[(3 * mstor8m.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911bm]m.length + 31 / 32) > [94msm:
              mstor[[94msm] = 0
              [94ms = [94ms + 1
              mcontinue 
          require mrealWorldPlayersm.length < 4294967295
          require uint32([94midx) < mem[96]
          mem[0] = mem[(32 * uint32([94midx)) + 144 len 16]
          mem[32] = 9
          mmd5TokenToRosterIndexm[mem[(32 * uint32([94midx)) + 144 len 16]m] = uint32(mrealWorldPlayersm.length)
          [94ms = mrealWorldPlayersm.length
          [94mt = [94m_67
          [94midx = [94midx + 1
          mcontinue 
      require uint32([94midx) < mem[96]
      mem[0] = mem[(32 * uint32([94midx)) + 144 len 16]
      mem[32] = 9
      if mmd5TokenToRosterIndexm[mem[(32 * uint32([94midx)) + 144 len 16]m]:
          [94ms = [94ms
          [94mt = [94mt
          [94midx = [94midx + 1
          mcontinue 
      require uint32([94midx) < mem[96]
      require 0 < mrealWorldPlayersm.length
      mem[0] = 8
      if uint128(mrealWorldPlayersm.field_0) == mem[(32 * uint32([94midx)) + 144 len 16]:
          [94ms = [94ms
          [94mt = [94mt
          [94midx = [94midx + 1
          mcontinue 
      [94m_88 = mem[64]
      mem[64] = mem[64] + 224
      require uint32([94midx) < mem[96]
      mem[[94m_88] = mem[(32 * uint32([94midx)) + 144 len 16]
      mem[[94m_88 + 32] = 0
      mem[[94m_88 + 64] = 0
      mem[[94m_88 + 96] = 0
      mem[[94m_88 + 128] = 0
      require uint32([94midx) < mem[(32 * m_md5Tokens.length) + 128]
      mem[[94m_88 + 160] = bool(mem[(32 * uint32([94midx)) + (32 * m_md5Tokens.length) + 160])
      [94m_94 = mem[64]
      mem[64] = mem[64] + 32
      mem[[94m_94] = 0
      mem[[94m_88 + 192] = [94m_94
      mrealWorldPlayersm.length++
      mem[0] = 8
      uint128(mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_0) = mem[[94m_88 + 16 len 16]
      uint128(mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_128) = 0
      mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_256 % 1 = 0
      Mask(96, 0, mstorF3F7m[mstor8m.lengthm]m.field_0) = 0
      uint8(mstorF3F7m[mstor8m.lengthm]m.field_96) = 0
      Mask(152, 0, mstorF3F7m[mstor8m.lengthm]m.field_104) = Mask(152, 0, bool(mem[[94m_88 + 160]))
      Mask(144, 0, mstorF3F7m[mstor8m.lengthm]m.field_112) = 0
      mstorF3F7m[mstor8m.lengthm]m.field_256 % 1 = 0
      mstorF3F7m[mstor8m.lengthm]m.field_256 % 1 = 0
      bool(mstorF3F7m[mstor8m.lengthm]m.field_0) = 0
      uint255(mstorF3F7m[mstor8m.lengthm]m.field_1) = 0
      Mask(248, 0, mstorF3F7m[mstor8m.lengthm]m.field_8) = mem[[94m_94 + 32 len 31]
      [94ms = sha3((3 * mrealWorldPlayersm.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911b)
      mwhile sha3((3 * mrealWorldPlayersm.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911b) + (mstor[(3 * mstor8m.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911bm]m.length + 31 / 32) > [94msm:
          mstor[[94msm] = 0
          [94ms = [94ms + 1
          mcontinue 
      require mrealWorldPlayersm.length < 4294967295
      require uint32([94midx) < mem[96]
      mem[0] = mem[(32 * uint32([94midx)) + 144 len 16]
      mem[32] = 9
      mmd5TokenToRosterIndexm[mem[(32 * uint32([94midx)) + 144 len 16]m] = uint32(mrealWorldPlayersm.length)
      [94ms = mrealWorldPlayersm.length
      [94mt = [94m_88
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x92f00233
# getter = ['storage', 160, 0, 7]
# const = None
# payable = False
def minterContract(): # not payable
  return mminterContractAddress


# hash = 0x9ea82706
# getter = None
# const = None
# payable = False
def removeRealWorldPlayer(uint128 m_md5Token): # not payable
  mem[64] = 320
  mem[96] = 0
  mem[128] = 0
  mem[160] = 0
  mem[192] = 0
  mem[224] = 0
  mem[256] = 0
  mem[288] = 96
  require caller == mcommissionerAddress
  require 1 == bool(uint8(mstor6m.field_168))
  [94ms = 96
  [94midx = 0
  mwhile uint32([94midx) < uint32(mrealWorldPlayersm.length)m:
      require uint32([94midx) < mrealWorldPlayersm.length
      mem[0] = 8
      [94m_58 = mem[64]
      mem[64] = mem[64] + 224
      mem[[94m_58] = uint128(mrealWorldPlayersm[uint32([94midx)m]m.field_0)
      mem[[94m_58 + 32] = uint128(mrealWorldPlayersm[uint32([94midx)m]m.field_128)
      mem[[94m_58 + 64] = uint64(mrealWorldPlayersm[uint32([94midx)m]m.field_256)
      mem[[94m_58 + 96] = uint32(mrealWorldPlayersm[uint32([94midx)m]m.field_320)
      mem[[94m_58 + 128] = bool(uint8(mrealWorldPlayersm[uint32([94midx)m]m.field_352))
      mem[[94m_58 + 160] = bool(uint8(mrealWorldPlayersm[uint32([94midx)m]m.field_360))
      [94m_59 = mem[64]
      mem[64] = mem[64] + ceil32(mstor[('name', 'realWorldPlayers', 8) + (3 * uint32([94midx)) + 2m]m.length) + 32
      mem[[94m_59] = mstor[('name', 'realWorldPlayers', 8) + (3 * uint32([94midx)) + 2m]m.length
      mem[0] = sha3(8) + (3 * uint32([94midx)) + 2
      mem[[94m_59 + 32] = mstor[sha3(('name', 'realWorldPlayers', 8) + (3 * uint32([94midx)) + 2)m]m.field_0
      [94ms = [94m_59 + 32
      [94mt = sha3(mem[0])
      mwhile [94m_59 + mstor[('name', 'realWorldPlayers', 8) + (3 * uint32([94midx)) + 2m]m.length > [94msm:
          mem[[94ms + 32] = uint256(mstor1m[[94mtm])
          [94ms = [94ms + 32
          [94mt = [94mt + 1
          mcontinue 
      mem[[94m_58 + 192] = [94m_59
      if mem[[94m_58 + 16 len 16] != m_md5Token:
          [94ms = [94m_58
          [94midx = [94midx + 1
          mcontinue 
      [94ms = [94midx
      mwhile uint32([94ms) < uint32(mrealWorldPlayersm.length - 1)m:
          require uint32([94ms + 1) < mrealWorldPlayersm.length
          require uint32([94ms) < mrealWorldPlayersm.length
          uint128(mrealWorldPlayersm[uint32([94ms)m]m.field_0) = uint128(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_0)
          uint128(mrealWorldPlayersm[uint32([94ms)m]m.field_0) = uint128(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_0)
          uint128(mrealWorldPlayersm[uint32([94ms)m]m.field_128) = uint128(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_128)
          uint64(mrealWorldPlayersm[uint32([94ms)m]m.field_256) = uint64(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_256)
          uint64(mrealWorldPlayersm[uint32([94ms)m]m.field_256) = uint64(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_256)
          Mask(192, 0, mrealWorldPlayersm[uint32([94ms)m]m.field_320) = uint32(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_320)
          addr(mrealWorldPlayersm[uint32([94ms)m]m.field_352) = 0
          uint64(mrealWorldPlayersm[uint32([94ms)m]m.field_256) = uint64(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_256)
          uint32(mrealWorldPlayersm[uint32([94ms)m]m.field_320) = uint32(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_320)
          addr(mrealWorldPlayersm[uint32([94ms)m]m.field_352) = addr(bool(uint8(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_352)))
          Mask(152, 0, mrealWorldPlayersm[uint32([94ms)m]m.field_360) = 0
          Mask(152, 0, mrealWorldPlayersm[uint32([94ms)m]m.field_360) = 0
          uint64(mrealWorldPlayersm[uint32([94ms)m]m.field_256) = uint64(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_256)
          uint32(mrealWorldPlayersm[uint32([94ms)m]m.field_320) = uint32(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_320)
          uint8(mrealWorldPlayersm[uint32([94ms)m]m.field_352) = uint8(bool(uint8(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_352)))
          Mask(152, 0, mrealWorldPlayersm[uint32([94ms)m]m.field_360) = Mask(152, 0, bool(uint8(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_360)))
          Mask(144, 0, mrealWorldPlayersm[uint32([94ms)m]m.field_368) = 0
          Mask(144, 0, mrealWorldPlayersm[uint32([94ms)m]m.field_368) = 0
          Mask(144, 0, mrealWorldPlayersm[uint32([94ms)m]m.field_368) = Mask(144, 16, bool(uint8(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_352))) >> 16
          if 31 >= mstor[(3 * uint32([94ms + 1)) + ('name', 'realWorldPlayers', 8) + 2m]m.length:
              mrealWorldPlayersm[uint32([94ms)m]m.field_512 = mrealWorldPlayersm[uint32([94ms + 1)m]m.field_512
              [94mt = sha3((3 * uint32([94ms)) + sha3(8) + 2)
              mwhile sha3((3 * uint32([94ms)) + sha3(8) + 2) + (mstor[(3 * uint32([94ms)) + ('name', 'realWorldPlayers', 8) + 2m]m.length + 31 / 32) > [94mtm:
                  mstor[[94mtm] = 0
                  [94mt = [94mt + 1
                  mcontinue 
              require uint32([94ms) < mrealWorldPlayersm.length
              mem[0] = uint128(mrealWorldPlayersm[uint32([94ms)m]m.field_0)
              mem[32] = 9
              mmd5TokenToRosterIndexm[uint128(mstor8m[uint32([94ms)m]m.field_0)m] = uint32([94ms)
              [94ms = [94ms + 1
              mcontinue 
          mrealWorldPlayersm[uint32([94ms)m]m.field_512 = Mask(255, 1, mrealWorldPlayersm[uint32([94ms + 1)m]m.field_512 and (256 * not bool(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_512)) - 1) + 1
          if not Mask(255, 1, mrealWorldPlayersm[uint32([94ms + 1)m]m.field_512 and (256 * not bool(mrealWorldPlayersm[uint32([94ms + 1)m]m.field_512)) - 1):
              [94mt = sha3((3 * uint32([94ms)) + sha3(8) + 2)
              mwhile sha3((3 * uint32([94ms)) + sha3(8) + 2) + (mstor[(3 * uint32([94ms)) + ('name', 'realWorldPlayers', 8) + 2m]m.length + 31 / 32) > [94mtm:
                  mstor[[94mtm] = 0
                  [94mt = [94mt + 1
                  mcontinue 
              require uint32([94ms) < mrealWorldPlayersm.length
              mem[0] = uint128(mrealWorldPlayersm[uint32([94ms)m]m.field_0)
              mem[32] = 9
              mmd5TokenToRosterIndexm[uint128(mstor8m[uint32([94ms)m]m.field_0)m] = uint32([94ms)
              [94ms = [94ms + 1
              mcontinue 
          [94mt = sha3((3 * uint32([94ms)) + sha3(8) + 2)
          [94mu = sha3((3 * uint32([94ms + 1)) + sha3(8) + 2)
          mwhile sha3((3 * uint32([94ms + 1)) + sha3(8) + 2) + (mstor[(3 * uint32([94ms + 1)) + ('name', 'realWorldPlayers', 8) + 2m]m.length + 31 / 32) > [94mum:
              mstor[[94mtm] = mstor[[94mum]
              [94mt = [94mt + 1
              [94mu = [94mu + 1
              mcontinue 
          [94mu = [94mt
          mwhile sha3((3 * uint32([94mu)) + sha3(8) + 2) + (mstor[(3 * uint32([94mu)) + ('name', 'realWorldPlayers', 8) + 2m]m.length + 31 / 32) > [94mum:
              mstor[[94mum] = 0
              [94mu = [94mu + 1
              mcontinue 
          require uint32([94mu) < mrealWorldPlayersm.length
          mem[0] = uint128(mrealWorldPlayersm[uint32([94mu)m]m.field_0)
          mem[32] = 9
          mmd5TokenToRosterIndexm[uint128(mstor8m[uint32([94mu)m]m.field_0)m] = uint32([94mu)
          [94mu = [94mu + 1
          mcontinue 
      require mrealWorldPlayersm.length - 1 < mrealWorldPlayersm.length
      mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_0 = 0
      Mask(112, 0, mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_0) = 0
      mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_0 = 0
      if 31 < mstor[(3 * mrealWorldPlayersm.length) + ('name', 'realWorldPlayers', 8) - 1m]m.length:
          [94midx = sha3((3 * mrealWorldPlayersm.length) + sha3(8) - 1)
          mwhile sha3((3 * mrealWorldPlayersm.length) + sha3(8) - 1) + (mstor[(3 * mrealWorldPlayersm.length) + ('name', 'realWorldPlayers', 8) - 1m]m.length + 31 / 32) > [94midxm:
              mstor[[94midxm] = 0
              [94midx = [94midx + 1
              mcontinue 
      mrealWorldPlayersm.length--
      if mrealWorldPlayersm.length > mrealWorldPlayersm.length - 1:
          mem[0] = 8
          [94midx = sha3(mem[0]) + (3 * mrealWorldPlayersm.length) - 3
          mwhile sha3(8) + (3 * mrealWorldPlayersm.length) > [94midxm:
              mstor[[94midxm] = 0
              Mask(112, 0, mstor1m[[94midxm]) = 0
              mstor2m[[94midxm] = 0
              if 31 < mstor[[94midx + 2m]m.length:
                  mem[0] = [94midx + 2
                  [94ms = sha3([94midx + 2)
                  mwhile sha3([94midx + 2) + (mstor[[94midx + 2m]m.length + 31 / 32) > [94msm:
                      mstor[[94msm] = 0
                      [94ms = [94ms + 1
                      mcontinue 
              [94midx = [94midx + 3
              mcontinue 
      stop


# hash = 0xa9741394
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def COMMISSIONER_AUCTION_FLOOR_PRICE(): # not payable
  return mstor1m.length


# hash = 0xb047fb50
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def cooAddress(): # not payable
  return mcooAddress


# hash = 0xb326c189
# getter = None
# const = None
# payable = False
def hasOpenCommissionerAuction(uint128 m_md5Token): # not payable
  require caller == mcommissionerAddress
  require ext_code.size(this.address)
  call this.address.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
       gas gas_remaining wei
      args m_md5Token
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[16 len 16] != 0xffffffffffffffffffffffffffffffff
  require ext_call.return_data[16 len 16] < mrealWorldPlayersm.length
  return bool(uint8(mrealWorldPlayersm[uint128(ext_call.return_data[0])m]m.field_352))


# hash = 0xce88a9ce
# getter = None
# const = None
# payable = False
def setProduction(): # not payable
  require caller == mceoAddress
  require 1 == bool(uint8(mstor6m.field_168))
  uint8(mstor6m.field_168) = 0


# hash = 0xdd897767
# getter = None
# const = None
# payable = False
def isRealWorldPlayerMintingEnabled(uint128 m_md5Token): # not payable
  if mmd5TokenToRosterIndexm[m_md5Token << 128m] <= 0:
      require 0 < mrealWorldPlayersm.length
      require uint128(mrealWorldPlayersm.field_0) == m_md5Token
  require mmd5TokenToRosterIndexm[m_md5Token << 128m] < mrealWorldPlayersm.length
  return bool(uint8(mrealWorldPlayersm[mstor9m[m_md5Token << 128m]m]m.field_360))


# hash = 0xea28baee
# getter = None
# const = None
# payable = False
def getRealWorldPlayerRosterIndex(uint128 m_md5Token): # not payable
  if mmd5TokenToRosterIndexm[m_md5Token << 128m]:
      return mmd5TokenToRosterIndexm[m_md5Token << 128m]
  if 0 >= mrealWorldPlayersm.length:
      return 0xffffffffffffffffffffffffffffffff
  if uint128(mrealWorldPlayersm.field_0) != m_md5Token:
      return 0xffffffffffffffffffffffffffffffff
  else:
      return 0


# hash = 0xf4351e15
# getter = None
# const = None
# payable = False
def addAndMintPlayers(uint128[] m_md5Tokens, bool[] m_mintingEnabled, uint256 m_startPrice, uint256 m_endPrice, uint256 m_duration): # not payable
  mem[96] = m_md5Tokens.length
  mem[128 len 32 * m_md5Tokens.length] = call.data[m_md5Tokens + 36 len 32 * m_md5Tokens.length]
  mem[(32 * m_md5Tokens.length) + 128] = m_mintingEnabled.length
  mem[(32 * m_md5Tokens.length) + 160 len 32 * m_mintingEnabled.length] = call.data[m_mintingEnabled + 36 len 32 * m_mintingEnabled.length]
  require caller == mcommissionerAddress
  mem[64] = (32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 384
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 160] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 192] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 224] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 256] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 288] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 320] = 0
  mem[(32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 352] = 96
  require m_md5Tokens.length == m_mintingEnabled.length
  [94ms = 0
  [94mt = (32 * m_mintingEnabled.length) + (32 * m_md5Tokens.length) + 160
  [94midx = 0
  mwhile uint32([94midx) < m_md5Tokens.lengthm:
      if not mrealWorldPlayersm.length:
          [94m_75 = mem[64]
          mem[64] = mem[64] + 224
          require uint32([94midx) < mem[96]
          mem[[94m_75] = mem[(32 * uint32([94midx)) + 144 len 16]
          mem[[94m_75 + 32] = 0
          mem[[94m_75 + 64] = 0
          mem[[94m_75 + 96] = 0
          mem[[94m_75 + 128] = 0
          require uint32([94midx) < mem[(32 * m_md5Tokens.length) + 128]
          mem[[94m_75 + 160] = bool(mem[(32 * uint32([94midx)) + (32 * m_md5Tokens.length) + 160])
          [94m_85 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_85] = 0
          mem[[94m_75 + 192] = [94m_85
          mrealWorldPlayersm.length++
          mem[0] = 8
          uint128(mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_0) = mem[[94m_75 + 16 len 16]
          uint128(mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_128) = 0
          mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_256 % 1 = 0
          Mask(96, 0, mstorF3F7m[mstor8m.lengthm]m.field_0) = 0
          uint8(mstorF3F7m[mstor8m.lengthm]m.field_96) = 0
          Mask(152, 0, mstorF3F7m[mstor8m.lengthm]m.field_104) = Mask(152, 0, bool(mem[[94m_75 + 160]))
          Mask(144, 0, mstorF3F7m[mstor8m.lengthm]m.field_112) = 0
          mstorF3F7m[mstor8m.lengthm]m.field_256 % 1 = 0
          mstorF3F7m[mstor8m.lengthm]m.field_256 % 1 = 0
          bool(mstorF3F7m[mstor8m.lengthm]m.field_0) = 0
          uint255(mstorF3F7m[mstor8m.lengthm]m.field_1) = 0
          Mask(248, 0, mstorF3F7m[mstor8m.lengthm]m.field_8) = mem[[94m_85 + 32 len 31]
          [94ms = sha3((3 * mrealWorldPlayersm.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911b)
          mwhile sha3((3 * mrealWorldPlayersm.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911b) + (mstor[(3 * mstor8m.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911bm]m.length + 31 / 32) > [94msm:
              mstor[[94msm] = 0
              [94ms = [94ms + 1
              mcontinue 
          require mrealWorldPlayersm.length < 4294967295
          require uint32([94midx) < mem[96]
          mem[0] = mem[(32 * uint32([94midx)) + 144 len 16]
          mem[32] = 9
          mmd5TokenToRosterIndexm[mem[(32 * uint32([94midx)) + 144 len 16]m] = uint32(mrealWorldPlayersm.length)
          [94ms = mrealWorldPlayersm.length
          [94mt = [94m_75
          [94midx = [94midx + 1
          mcontinue 
      require uint32([94midx) < mem[96]
      mem[0] = mem[(32 * uint32([94midx)) + 144 len 16]
      mem[32] = 9
      if mmd5TokenToRosterIndexm[mem[(32 * uint32([94midx)) + 144 len 16]m]:
          [94ms = [94ms
          [94mt = [94mt
          [94midx = [94midx + 1
          mcontinue 
      require uint32([94midx) < mem[96]
      require 0 < mrealWorldPlayersm.length
      mem[0] = 8
      if uint128(mrealWorldPlayersm.field_0) == mem[(32 * uint32([94midx)) + 144 len 16]:
          [94ms = [94ms
          [94mt = [94mt
          [94midx = [94midx + 1
          mcontinue 
      [94m_98 = mem[64]
      mem[64] = mem[64] + 224
      require uint32([94midx) < mem[96]
      mem[[94m_98] = mem[(32 * uint32([94midx)) + 144 len 16]
      mem[[94m_98 + 32] = 0
      mem[[94m_98 + 64] = 0
      mem[[94m_98 + 96] = 0
      mem[[94m_98 + 128] = 0
      require uint32([94midx) < mem[(32 * m_md5Tokens.length) + 128]
      mem[[94m_98 + 160] = bool(mem[(32 * uint32([94midx)) + (32 * m_md5Tokens.length) + 160])
      [94m_104 = mem[64]
      mem[64] = mem[64] + 32
      mem[[94m_104] = 0
      mem[[94m_98 + 192] = [94m_104
      mrealWorldPlayersm.length++
      mem[0] = 8
      uint128(mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_0) = mem[[94m_98 + 16 len 16]
      uint128(mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_128) = 0
      mrealWorldPlayersm[mrealWorldPlayersm.lengthm]m.field_256 % 1 = 0
      Mask(96, 0, mstorF3F7m[mstor8m.lengthm]m.field_0) = 0
      uint8(mstorF3F7m[mstor8m.lengthm]m.field_96) = 0
      Mask(152, 0, mstorF3F7m[mstor8m.lengthm]m.field_104) = Mask(152, 0, bool(mem[[94m_98 + 160]))
      Mask(144, 0, mstorF3F7m[mstor8m.lengthm]m.field_112) = 0
      mstorF3F7m[mstor8m.lengthm]m.field_256 % 1 = 0
      mstorF3F7m[mstor8m.lengthm]m.field_256 % 1 = 0
      bool(mstorF3F7m[mstor8m.lengthm]m.field_0) = 0
      uint255(mstorF3F7m[mstor8m.lengthm]m.field_1) = 0
      Mask(248, 0, mstorF3F7m[mstor8m.lengthm]m.field_8) = mem[[94m_104 + 32 len 31]
      [94ms = sha3((3 * mrealWorldPlayersm.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911b)
      mwhile sha3((3 * mrealWorldPlayersm.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911b) + (mstor[(3 * mstor8m.length) - 0xc085601c9b05546c4de925af5cdebeab0dd5f5d4bea4dc57b37e961749c911bm]m.length + 31 / 32) > [94msm:
          mstor[[94msm] = 0
          [94ms = [94ms + 1
          mcontinue 
      require mrealWorldPlayersm.length < 4294967295
      require uint32([94midx) < mem[96]
      mem[0] = mem[(32 * uint32([94midx)) + 144 len 16]
      mem[32] = 9
      mmd5TokenToRosterIndexm[mem[(32 * uint32([94midx)) + 144 len 16]m] = uint32(mrealWorldPlayersm.length)
      [94ms = mrealWorldPlayersm.length
      [94mt = [94m_98
      [94midx = [94midx + 1
      mcontinue 
  mem[mem[64]] = 0xaba2362800000000000000000000000000000000000000000000000000000000
  mem[mem[64] + 36] = m_startPrice
  mem[mem[64] + 68] = m_endPrice
  mem[mem[64] + 100] = m_duration
  mem[mem[64] + 4] = 128
  mem[mem[64] + 132] = mem[96]
  mem[mem[64] + 164 len floor32(mem[96])] = mem[128 len floor32(mem[96])]
  require ext_code.size(mminterContractAddress)
  call mminterContractAddress.mintPlayers(uint128[] md5Tokens, uint256 startPrice, uint256 endPrice, uint256 duration) with:
       gas gas_remaining wei
      args 128, m_startPrice, m_endPrice, m_duration, mem[mem[64] + 132 len (32 * mem[96]) + 32]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


