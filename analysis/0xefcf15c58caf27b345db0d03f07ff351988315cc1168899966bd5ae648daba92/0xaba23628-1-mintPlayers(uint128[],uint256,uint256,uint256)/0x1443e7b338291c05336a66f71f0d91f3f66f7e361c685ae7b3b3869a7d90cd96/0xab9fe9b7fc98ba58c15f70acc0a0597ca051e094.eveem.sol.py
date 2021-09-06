# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xAB9Fe9B7Fc98ba58c15f70acc0A0597ca051e094 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {'0xc87b56dd': 'tokenURI(uint256 _tokenId)'} 

# storage definitions
def storage:
    # storage address 12
    remainingMarketingTokens # mask: a s
    # storage address 18
    symbol
    # storage address 3
    ceoAddress # mask: a s
    # storage address 16
    playerToken
    # storage address 9
    balanceOf
    # storage address 10
    stor10
    # storage address 1
    COMMISSIONER_AUCTION_FLOOR_PRICE # mask: a s
    # storage address 1
    stor1 # mask: a s
    # storage address 7
    playerTokenToOwner
    # storage address 17
    name
    # storage address 6
    commissionerAddress # mask: a s
    # storage address 6
    paused # mask: a s
    # storage address 6
    isDevelopment # mask: a s
    # storage address 8
    playerTokenToApproved
    # storage address 11
    stor11
    # storage address 20
    isCoreContract # mask: a s
    # storage address 20
    saleClockAuctionContractAddress # mask: a s
    # storage address 4
    cfoAddress # mask: a s
    # storage address 0
    MAX_MARKETING_TOKENS # mask: a s
    # storage address 2
    COMMISSIONER_AUCTION_DURATION # mask: a s
    # storage address 15
    teamContractAddress # mask: a s
    # storage address 21
    newContractAddress # mask: a s
    # storage address 13
    stor13
    # storage address 5
    cooAddress # mask: a s
    # storage address 14
    leagueRosterContractAddress # mask: a s
# hash = 0x00f86ac7
# getter = None
# const = None
# payable = False
def getKeccak256(string m_stringToHash): # not payable
  mem[128 len m_stringToHash.length] = m_stringToHash[allm]
  mem[ceil32(m_stringToHash.length) + 160 len floor32(m_stringToHash.length)] = call.data[m_stringToHash + 36 len floor32(m_stringToHash.length)]
  mem[ceil32(m_stringToHash.length) + floor32(m_stringToHash.length) + -(m_stringToHash.length % 32) + 192 len m_stringToHash.length % 32] = mem[floor32(m_stringToHash.length) + -(m_stringToHash.length % 32) + 160 len m_stringToHash.length % 32]
  mem[m_stringToHash.length + ceil32(m_stringToHash.length) + 160 len floor32(m_stringToHash.length)] = call.data[m_stringToHash + 36 len floor32(m_stringToHash.length)]
  mem[m_stringToHash.length + ceil32(m_stringToHash.length) + floor32(m_stringToHash.length) + 160] = mem[m_stringToHash.length + ceil32(m_stringToHash.length) + floor32(m_stringToHash.length) + 160] and 256^(-(m_stringToHash.length % 32) + 32) - 1 or mem[ceil32(m_stringToHash.length) + floor32(m_stringToHash.length) + 160] and !(256^(-(m_stringToHash.length % 32) + 32) - 1)
  mem[m_stringToHash.length + ceil32(m_stringToHash.length) + 160] = sha3(call.data[m_stringToHash + 36 len floor32(m_stringToHash.length)], mem[m_stringToHash.length + ceil32(m_stringToHash.length) + floor32(m_stringToHash.length) + 160 len m_stringToHash.length % 32])
  return memory
    from m_stringToHash.length + ceil32(m_stringToHash.length) + 160
     [93mlen 32


# hash = 0x01ffc9a7
# getter = None
# const = None
# payable = False
def supportsInterface(bytes4 m_interfaceId): # not payable
  if 0x1ffc9a700000000000000000000000000000000000000000000000000000000 == Mask(32, 224, m_interfaceId):
      return True
  if Mask(32, 224, m_interfaceId) == 0x5b5e139f00000000000000000000000000000000000000000000000000000000:
      return True
  if Mask(32, 224, m_interfaceId) == 0x80ac58cd00000000000000000000000000000000000000000000000000000000:
      return True
  return (Mask(32, 224, m_interfaceId) == 0x780e9d6300000000000000000000000000000000000000000000000000000000)


# hash = 0x04869083
# getter = None
# const = None
# payable = False
def auctionCreated(uint256 m_param1, address m_param2, uint128 m_param3, uint128 m_param4, uint64 m_param5): # not payable
  require msaleClockAuctionContractAddress
  require caller == msaleClockAuctionContractAddress


# hash = 0x0519ce79
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def cfoAddress(): # not payable
  return mcfoAddress


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 17]]]], ['loc', 17]]]
# const = None
# payable = False
def name(): # not payable
  return mnamem[0 len mnamem.lengthm]


# hash = 0x081812fc
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 8]]]
# const = None
# payable = False
def getApproved(uint256 m_tokenId): # not payable
  require mplayerTokenm.length > m_tokenId
  return mplayerTokenToApprovedm[m_tokenIdm]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address m_spender, uint256 m_value): # not payable
  require not mpaused
  require mplayerTokenToOwnerm[m_valuem]
  require mplayerTokenToOwnerm[m_valuem] != m_spender
  if mplayerTokenToOwnerm[m_valuem] != caller:
      require mplayerTokenToOwnerm[m_valuem]
      require mstor11m[mstor7m[m_valuem]m]m[callerm]
  mplayerTokenToApprovedm[m_valuem] = m_spender
  log Approval(
        address owner=caller,
        address spender=_spender,
        uint256 value=_value)


# hash = 0x0a0f8168
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def ceoAddress(): # not payable
  return mceoAddress


# hash = 0x1051db34
# getter = None
# const = ['return', 1]
# payable = False
const implementsERC721 = 1


# hash = 0x18160ddd
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def totalSupply(): # not payable
  return mplayerTokenm.length


# hash = 0x1ace88a4
# getter = None
# const = None
# payable = False
def realWorldPlayerTokenForPlayerTokenId(uint32 m_playerTokenID): # not payable
  require m_playerTokenID < mplayerTokenm.length
  require ext_code.size(mleagueRosterContractAddress)
  call mleagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
       gas gas_remaining wei
      args uint32(mplayerTokenm[m_playerTokenIDm]m.field_0)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 192
  return uint128(ext_call.return_data[0])


# hash = 0x1cc14cbc
# getter = ['bool', ['storage', 8, 168, 6]]
# const = None
# payable = False
def isDevelopment(): # not payable
  return bool(misDevelopment)


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_value): # not payable
  require not mpaused
  require m_to
  require mplayerTokenm.length > m_value
  require mplayerTokenToApprovedm[m_valuem] == m_to
  require mplayerTokenToOwnerm[m_valuem] == m_from
  if mplayerTokenToOwnerm[m_valuem] != caller:
      if mplayerTokenToApprovedm[m_valuem] != caller:
          require mstor11m[addr(m_from)m]m[callerm]
  mplayerTokenToOwnerm[m_valuem] = m_to
  if m_from:
      require mbalanceOfm[addr(m_from)m]m.field_0 - 1 < mbalanceOfm[addr(m_from)m]m.field_0
      require uint32(mstor10m[m_value << 224m]m.field_0) < mbalanceOfm[addr(m_from)m]m.field_0
      mbalanceOfm[addr(m_from)m]m[mstor10m[m_value << 224m]m.field_3 % 536870912m]m.field_0 = mstor('array', ('div', 0.125, ('add', -1, ('stor', 256, 0, ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9))))), ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9)))m[uint8(mstor9m[addr(m_from)m]m.field_0 - 1)m] * 256^(4 * mstor10m[m_value << 224m]m.field_0 % 8) or !(4294967295 * 256^(4 * mstor10m[m_value << 224m]m.field_0 % 8)) and mbalanceOfm[addr(m_from)m]m[mstor10m[m_value << 224m]m.field_3 % 536870912m]m.field_0
      mbalanceOfm[addr(m_from)m]m.field_0--
      if mbalanceOfm[addr(m_from)m]m.field_0 > mbalanceOfm[addr(m_from)m]m.field_0 - 1:
          [94midx = mbalanceOfm[addr(m_from)m]m.field_0 + 6 / 8
          mwhile mbalanceOfm[addr(m_from)m]m.field_0 + 7 / 8 > [94midxm:
              mbalanceOfm[addr(m_from)m]m[[94midxm]m.field_0 = 0
              [94midx = [94midx + 1
              mcontinue 
      uint32(mstor10m[uint32(mstor9m[addr(m_from)m]m[0.125 / mstor9m[addr(m_from)m]m.field_0 - 1m]m.field_(32 * stor9[addr(_from)].field_0 - 1 % 8) - 224)m]m.field_0) = uint32(mstor10m[m_value << 224m]m.field_0)
      uint32(mstor10m[uint32(m_value)m]m.field_0) = 0
      mplayerTokenToApprovedm[m_valuem] = 0
  mbalanceOfm[addr(m_to)m]m.field_0++
  mbalanceOfm[addr(m_to)m]m[Mask(253, 0, mbalanceOfm[addr(m_to)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(m_to)m]m[Mask(253, 0, mbalanceOfm[addr(m_to)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(m_to)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(m_to)m]m.field_0 % 8) * uint32(m_value)
  uint32(mstor10m[m_value << 224m]m.field_0) = uint32(mbalanceOfm[addr(m_to)m]m.field_0)
  log Transfer(
        address from=_from,
        address to=_to,
        uint256 value=_value)


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


# hash = 0x2bfe243f
# getter = None
# const = None
# payable = False
def minStartPriceForCommishAuctions(uint128[] m_md5Tokens): # not payable
  mem[128 len 32 * m_md5Tokens.length] = call.data[m_md5Tokens + 36 len 32 * m_md5Tokens.length]
  mem[(32 * m_md5Tokens.length) + 128 len 1600] = code.data[17799 len 1600]
  mem[(32 * m_md5Tokens.length) + 1728 len 1600] = code.data[17799 len 1600]
  mem[(32 * m_md5Tokens.length) + 3328] = 0
  mem[(32 * m_md5Tokens.length) + 3360] = 0
  mem[(32 * m_md5Tokens.length) + 3392] = 0
  mem[(32 * m_md5Tokens.length) + 3424] = 0
  mem[(32 * m_md5Tokens.length) + 3456] = 0
  mem[(32 * m_md5Tokens.length) + 3488] = 0
  mem[(32 * m_md5Tokens.length) + 3520] = 96
  require caller == mcommissionerAddress
  require 50 >= m_md5Tokens.length
  [94ms = 0
  [94ms = 0
  [94midx = 0
  mwhile uint32([94midx) < m_md5Tokens.lengthm:
      require uint32([94midx) < m_md5Tokens.length
      [94m_28 = mem[(32 * uint32([94midx)) + 128]
      mem[(32 * m_md5Tokens.length) + 3556] = mem[(32 * uint32([94midx)) + 144 len 16]
      require ext_code.size(mleagueRosterContractAddress)
      call mleagueRosterContractAddress.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
           gas gas_remaining wei
          args uint128([94m_28)
      mem[(32 * m_md5Tokens.length) + 3552] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if uint128(ext_call.return_data[0]) != 0xffffffffffffffffffffffffffffffff:
          require ext_code.size(mleagueRosterContractAddress)
          call mleagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
               gas gas_remaining wei
              args uint128(ext_call.return_data[0])
          mem[(32 * m_md5Tokens.length) + 3552 len 192] = ext_call.return_data[0 len 192]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 192
          mem[(32 * m_md5Tokens.length) + 3488] = bool(ext_call.return_data[160])
          mem[(32 * m_md5Tokens.length) + 3456] = bool(ext_call.return_data[128])
          mem[(32 * m_md5Tokens.length) + 3424] = uint32(ext_call.return_data[96])
          mem[(32 * m_md5Tokens.length) + 3392] = uint64(ext_call.return_data[64])
          mem[(32 * m_md5Tokens.length) + 3360] = uint128(ext_call.return_data[32])
          mem[(32 * m_md5Tokens.length) + 3328] = uint128(ext_call.return_data[0])
          if uint128([94m_28) == uint128(ext_call.return_data[0]):
              require uint32([94midx) < 50
              if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) <= 0xffffffffffffffffffffffffffffffff:
                  if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
                      mem[(32 * uint32([94midx)) + (32 * m_md5Tokens.length) + 1728] = uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4))
                  else:
                      mem[(32 * uint32([94midx)) + (32 * m_md5Tokens.length) + 1728] = uint128(mstor1)
              else:
                  if 0xffffffffffffffffffffffffffffffff >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
                      mem[(32 * uint32([94midx)) + (32 * m_md5Tokens.length) + 1728] = 0xffffffffffffffffffffffffffffffff
                  else:
                      mem[(32 * uint32([94midx)) + (32 * m_md5Tokens.length) + 1728] = uint128(mstor1)
      [94ms = ext_call.return_data[0]
      [94ms = [94m_28
      [94midx = [94midx + 1
      mcontinue 
  return memory
    from (32 * m_md5Tokens.length) + 1728
     [93mlen 1600


# hash = 0x2d90dd92
# getter = ['storage', 16, 0, 12]
# const = None
# payable = False
def remainingMarketingTokens(): # not payable
  return mremainingMarketingTokens


# hash = 0x2e43ec0c
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def commissionerAddress(): # not payable
  return mcommissionerAddress


# hash = 0x2f745c59
# getter = ['storage', 32, ['mask_shl', 3, 0, 5, ['cd', 36]], ['add', ['mask_shl', 253, 3, -3, ['cd', 36]], ['sha3', ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 9]]]]]
# const = None
# payable = False
def tokenOfOwnerByIndex(address m_owner, uint256 m_index): # not payable
  require m_owner
  require m_index < mbalanceOfm[addr(m_owner)m]m.field_0
  require m_index < mbalanceOfm[addr(m_owner)m]m.field_0
  return mtokenOfOwnerByIndexm[uint8(m_index)m]


# hash = 0x30d1f3e3
# getter = ['struct', ['loc', 16]]
# const = None
# payable = False
def playerTokens(uint256 m_param1): # not payable
  require m_param1 < mplayerTokenm.length
  return uint32(mplayerTokenm[m_param1m]m.field_0), 
         uint32(mplayerTokenm[m_param1m]m.field_0),
         uint64(mplayerTokenm[m_param1m]m.field_0),
         uint128(mplayerTokenm[m_param1m]m.field_128)


# hash = 0x325ecf99
# getter = None
# const = None
# payable = False
def addMarketingToken(uint256 m_keywordHash, uint128 m_md5Token): # not payable
  require caller == mcommissionerAddress
  require mremainingMarketingTokens > 0
  require not mstor13m[m_keywordHashm]
  require ext_code.size(mleagueRosterContractAddress)
  call mleagueRosterContractAddress.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
       gas gas_remaining wei
      args m_md5Token
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[16 len 16] != 0xffffffffffffffffffffffffffffffff
  mremainingMarketingTokens = uint16(mremainingMarketingTokens - 1)
  mstor13m[m_keywordHashm] = m_md5Token
  log MarketingTokenCreated(
        uint256 hash=_keywordHash,
        uint128 rwpMd5=_md5Token)


# hash = 0x334e712f
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def COMMISSIONER_AUCTION_DURATION(): # not payable
  return mCOMMISSIONER_AUCTION_DURATION


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


# hash = 0x3d7d3f5a
# getter = None
# const = None
# payable = False
def createSaleAuction(uint256 m_artworkId, uint256 m_startingPrice, uint256 m_endingPrice, uint256 m_duration): # not payable
  require not mpaused
  require mplayerTokenToOwnerm[m_artworkIdm] == caller
  mplayerTokenToApprovedm[m_artworkIdm] = msaleClockAuctionContractAddress
  require ext_code.size(msaleClockAuctionContractAddress)
  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
       gas gas_remaining wei
      args 0, uint32(m_artworkId), m_startingPrice, m_endingPrice, m_duration, caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x3d83230f
# getter = None
# const = None
# payable = False
def auctionSuccessful(uint256 m_tokenId, uint128 m_totalPrice, address m_seller, address m_winner): # not payable
  require msaleClockAuctionContractAddress
  require caller == msaleClockAuctionContractAddress
  require m_tokenId < mplayerTokenm.length
  uint128(mplayerTokenm[m_tokenIdm]m.field_128) = m_totalPrice
  if this.address == m_seller:
      require m_tokenId < mplayerTokenm.length
      require ext_code.size(mleagueRosterContractAddress)
      call mleagueRosterContractAddress.commissionerAuctionComplete(uint32 rosterIndex, uint128 price) with:
           gas gas_remaining wei
          args uint32(mplayerTokenm[m_tokenIdm]m.field_0), m_totalPrice
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log CommissionerAuctionSuccessful(
            uint256 tokenId=_tokenId,
            uint256 totalPrice=_totalPrice << 128,
            address winner=_winner)


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == mceoAddress
  require mpaused
  require mleagueRosterContractAddress
  require msaleClockAuctionContractAddress
  require not mnewContractAddress
  require caller == mceoAddress
  require mpaused
  mpaused = 0


# hash = 0x41ba7011
# getter = None
# const = None
# payable = False
def setLeagueRosterContractAddress(address m_address): # not payable
  require caller == mceoAddress
  if not misDevelopment:
      require not mleagueRosterContractAddress
  require ext_code.size(m_address)
  call m_address.isLeagueRosterContract() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mleagueRosterContractAddress = m_address


# hash = 0x42842e0e
# getter = None
# const = None
# payable = True
def safeTransferFrom(address m_from, address m_to, uint256 m_tokenId) payable: 
  require m_to
  require not mpaused
  require m_to
  require mplayerTokenm.length > m_tokenId
  require mplayerTokenToApprovedm[m_tokenIdm] == m_to
  require mplayerTokenToOwnerm[m_tokenIdm] == m_from
  if mplayerTokenToOwnerm[m_tokenIdm] != caller:
      if mplayerTokenToApprovedm[m_tokenIdm] != caller:
          require mstor11m[addr(m_from)m]m[callerm]
  mplayerTokenToOwnerm[m_tokenIdm] = m_to
  if m_from:
      require mbalanceOfm[addr(m_from)m]m.field_0 - 1 < mbalanceOfm[addr(m_from)m]m.field_0
      require uint32(mstor10m[m_tokenId << 224m]m.field_0) < mbalanceOfm[addr(m_from)m]m.field_0
      mbalanceOfm[addr(m_from)m]m[mstor10m[m_tokenId << 224m]m.field_3 % 536870912m]m.field_0 = mstor('array', ('div', 0.125, ('add', -1, ('stor', 256, 0, ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9))))), ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9)))m[uint8(mstor9m[addr(m_from)m]m.field_0 - 1)m] * 256^(4 * mstor10m[m_tokenId << 224m]m.field_0 % 8) or !(4294967295 * 256^(4 * mstor10m[m_tokenId << 224m]m.field_0 % 8)) and mbalanceOfm[addr(m_from)m]m[mstor10m[m_tokenId << 224m]m.field_3 % 536870912m]m.field_0
      mbalanceOfm[addr(m_from)m]m.field_0--
      if mbalanceOfm[addr(m_from)m]m.field_0 > mbalanceOfm[addr(m_from)m]m.field_0 - 1:
          [94midx = mbalanceOfm[addr(m_from)m]m.field_0 + 6 / 8
          mwhile mbalanceOfm[addr(m_from)m]m.field_0 + 7 / 8 > [94midxm:
              mbalanceOfm[addr(m_from)m]m[[94midxm]m.field_0 = 0
              [94midx = [94midx + 1
              mcontinue 
      uint32(mstor10m[uint32(mstor9m[addr(m_from)m]m[0.125 / mstor9m[addr(m_from)m]m.field_0 - 1m]m.field_(32 * stor9[addr(_from)].field_0 - 1 % 8) - 224)m]m.field_0) = uint32(mstor10m[m_tokenId << 224m]m.field_0)
      uint32(mstor10m[uint32(m_tokenId)m]m.field_0) = 0
      mplayerTokenToApprovedm[m_tokenIdm] = 0
  mbalanceOfm[addr(m_to)m]m.field_0++
  mbalanceOfm[addr(m_to)m]m[Mask(253, 0, mbalanceOfm[addr(m_to)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(m_to)m]m[Mask(253, 0, mbalanceOfm[addr(m_to)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(m_to)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(m_to)m]m.field_0 % 8) * uint32(m_tokenId)
  uint32(mstor10m[m_tokenId << 224m]m.field_0) = uint32(mbalanceOfm[addr(m_to)m]m.field_0)
  log Transfer(
        address from=_from,
        address to=_to,
        uint256 value=_tokenId)
  if ext_code.size(m_to) > 0:
      require ext_code.size(m_to)
      call m_to.onERC721Received(address param1, address param2, uint256 param3, bytes param4) with:
           gas 50000 wei
          args 0, uint32(caller), addr(m_from), m_tokenId, 128, 0, mem[260]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require Mask(32, 224, sha3('onERC721Received(address,uint256', ',bytes)')) == Mask(32, 224, ext_call.return_data[0])


# hash = 0x4682ff71
# getter = None
# const = None
# payable = False
def redeemMarketingToken(string m_keyWords): # not payable
  mem[128 len m_keyWords.length] = m_keyWords[allm]
  mem[ceil32(m_keyWords.length) + 128] = 0
  mem[ceil32(m_keyWords.length) + 160] = 0
  mem[ceil32(m_keyWords.length) + 384 len floor32(m_keyWords.length)] = call.data[m_keyWords + 36 len floor32(m_keyWords.length)]
  mem[ceil32(m_keyWords.length) + floor32(m_keyWords.length) + -(m_keyWords.length % 32) + 416 len m_keyWords.length % 32] = mem[floor32(m_keyWords.length) + -(m_keyWords.length % 32) + 160 len m_keyWords.length % 32]
  mem[m_keyWords.length + ceil32(m_keyWords.length) + 384 len floor32(m_keyWords.length)] = call.data[m_keyWords + 36 len floor32(m_keyWords.length)]
  mem[m_keyWords.length + ceil32(m_keyWords.length) + floor32(m_keyWords.length) + 384] = 256^(-(m_keyWords.length % 32) + 32) - 1 and mem[m_keyWords.length + ceil32(m_keyWords.length) + floor32(m_keyWords.length) + 384] or mem[ceil32(m_keyWords.length) + floor32(m_keyWords.length) + 384 len -(m_keyWords.length % 32) + 32], mem[floor32(m_keyWords.length) + -(m_keyWords.length % 32) + 160 len m_keyWords.length % 32] and !(256^(-(m_keyWords.length % 32) + 32) - 1)
  if mstor13m[call.data[m_keyWords + 36 len floor32(m_keyWords.length)]m][mem[m_keyWords.length + ceil32(m_keyWords.length) + floor32(m_keyWords.length) + 384 len m_keyWords.length % 32]m]:
      mstor13m[call.data[m_keyWords + 36 len floor32(m_keyWords.length)]m][mem[m_keyWords.length + ceil32(m_keyWords.length) + floor32(m_keyWords.length) + 384 len m_keyWords.length % 32]m] = 0
      require ext_code.size(mleagueRosterContractAddress)
      call mleagueRosterContractAddress.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
           gas gas_remaining wei
          args mstor13m[call.data[m_keyWords + 36 len floor32(m_keyWords.length)]m][mem[m_keyWords.length + ceil32(m_keyWords.length) + floor32(m_keyWords.length) + 384 len m_keyWords.length % 32]m]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if uint128(ext_call.return_data[0]) != 0xffffffffffffffffffffffffffffffff:
          require ext_code.size(mleagueRosterContractAddress)
          call mleagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
               gas gas_remaining wei
              args uint128(ext_call.return_data[0])
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 192
          require uint32(ext_call.return_data[0]) < 4294967295
          require uint32(ext_call.return_data[96]) < 4294967295
          mplayerTokenm.length++
          uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
          uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
          uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
          uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
          mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
          require mplayerTokenm.length < 4294967295
          mplayerTokenToOwnerm[mstor16m.lengthm] = caller
          mbalanceOfm[callerm]m.field_0++
          mbalanceOfm[callerm]m[Mask(253, 0, mbalanceOfm[callerm]m.field_3)m]m.field_0 = mbalanceOfm[callerm]m[Mask(253, 0, mbalanceOfm[callerm]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[callerm]m.field_0 % 8)) or 256^(4 * mbalanceOfm[callerm]m.field_0 % 8) * uint32(mplayerTokenm.length)
          uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[callerm]m.field_0)
          log Transfer(
                address from=0,
                address to=caller,
                uint256 value=playerToken.length)
          require ext_code.size(mleagueRosterContractAddress)
          call mleagueRosterContractAddress.'T6qy' with:
               gas gas_remaining wei
              args ext_call.return_data[0] << 224, ext_call.return_data[32] << 128, block.timestamp << 192, uint32(ext_call.return_data[96]) + 1 << 224, bool(ext_call.return_data[128]), bool(ext_call.return_data[160])
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          log MarketingTokenRedeemed(
                uint256 hash=sha3(call.data[_keyWords + 36 len floor32(_keyWords.length)], mem[_keyWords.length + ceil32(_keyWords.length) + floor32(_keyWords.length) + 384 len _keyWords.length % 32]),
                uint128 rwpMd5=uint128(ext_call.return_data[0]),
                address recipient=caller)


# hash = 0x4df6d048
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 8]]]
# const = None
# payable = False
def playerTokenToApproved(uint256 m_param1): # not payable
  return mplayerTokenToApprovedm[m_param1m]


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


# hash = 0x4e41ebf6
# getter = None
# const = None
# payable = False
def createCommissionerAuction(uint32 m_playerTokenId, uint256 m_startingPrice, uint256 m_endingPrice, uint256 m_duration): # not payable
  require not mpaused
  require caller == mcommissionerAddress
  require mleagueRosterContractAddress
  require m_playerTokenId < mplayerTokenm.length
  require mplayerTokenToOwnerm[m_playerTokenId << 224m] == this.address
  require m_playerTokenId < mplayerTokenm.length
  require ext_code.size(mleagueRosterContractAddress)
  call mleagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
       gas gas_remaining wei
      args uint32(mplayerTokenm[m_playerTokenIdm]m.field_0)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 192
  mplayerTokenToApprovedm[m_playerTokenId << 224m] = msaleClockAuctionContractAddress
  require ext_code.size(msaleClockAuctionContractAddress)
  if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) <= 0xffffffffffffffffffffffffffffffff:
      if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
          if m_startingPrice >= uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)):
              if m_duration:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, m_startingPrice, m_endingPrice, m_duration, this.address
              else:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, m_startingPrice, m_endingPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
          else:
              if m_duration:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, m_endingPrice, m_duration, this.address
              else:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, m_endingPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
      else:
          if m_startingPrice >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
              if m_duration:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, m_startingPrice, m_endingPrice, m_duration, this.address
              else:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, m_startingPrice, m_endingPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
          else:
              if m_duration:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endingPrice, m_duration, this.address
              else:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endingPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
  else:
      if 0xffffffffffffffffffffffffffffffff >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
          if m_startingPrice >= 0xffffffffffffffffffffffffffffffff:
              if m_duration:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, m_startingPrice, m_endingPrice, m_duration, this.address
              else:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, m_startingPrice, m_endingPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
          else:
              if m_duration:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, 0xffffffffffffffffffffffffffffffff, m_endingPrice, m_duration, this.address
              else:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, 0xffffffffffffffffffffffffffffffff, m_endingPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
      else:
          if m_startingPrice >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
              if m_duration:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, m_startingPrice, m_endingPrice, m_duration, this.address
              else:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, m_startingPrice, m_endingPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
          else:
              if m_duration:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endingPrice, m_duration, this.address
              else:
                  call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args m_playerTokenId << 224, uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endingPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x4f6ccce7
# getter = None
# const = None
# payable = False
def tokenByIndex(uint256 m_index): # not payable
  require mplayerTokenm.length > m_index
  return m_index


# hash = 0x50e59eb3
# getter = None
# const = ['return', 1]
# payable = False
const isMinter = 1


# hash = 0x54367179
# getter = None
# const = None
# payable = False
def updateRealWorldPlayer(uint32 m_rosterIndex, uint128 m_prevCommissionerSalePrice, uint64 m_lastMintedTime, uint32 m_mintedCount, bool m_hasActiveCommissionerAuction, bool m_mintingEnabled): # not payable
  require caller == mceoAddress
  require 1 == bool(misDevelopment)
  require mleagueRosterContractAddress
  require ext_code.size(mleagueRosterContractAddress)
  call mleagueRosterContractAddress.'T6qy' with:
       gas gas_remaining wei
      args Mask(224, 0, 'T6qy'), 0, m_prevCommissionerSalePrice << 128, m_lastMintedTime << 192, m_mintedCount, m_hasActiveCommissionerAuction, m_mintingEnabled
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x555fe48a
# getter = None
# const = None
# payable = False
def batchTransferFrom(address m_from, address m_to, uint32[] m_tokenIds): # not payable
  mem[128 len 32 * m_tokenIds.length] = call.data[m_tokenIds + 36 len 32 * m_tokenIds.length]
  require not mpaused
  [94ms = 0
  [94midx = 0
  mwhile uint32([94midx) < m_tokenIds.lengthm:
      require uint32([94midx) < m_tokenIds.length
      require mplayerTokenToApprovedm[mem[(32 * uint32([94midx)) + 156 len 4]m] == m_to
      require mplayerTokenToOwnerm[mem[(32 * uint32([94midx)) + 128] << 224m] == m_from
      if mplayerTokenToOwnerm[mem[(32 * uint32([94midx)) + 128] << 224m] != caller:
          if mplayerTokenToApprovedm[mem[(32 * uint32([94midx)) + 128] << 224m] != caller:
              require mstor11m[addr(m_from)m]m[callerm]
      mplayerTokenToOwnerm[mem[(32 * uint32([94midx)) + 128] << 224m] = m_to
      if m_from:
          require mbalanceOfm[addr(m_from)m]m.field_0 - 1 < mbalanceOfm[addr(m_from)m]m.field_0
          require uint32(mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_0) < mbalanceOfm[addr(m_from)m]m.field_0
          mbalanceOfm[addr(m_from)m]m[mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_3 % 536870912m]m.field_0 = mstor('array', ('div', 0.125, ('add', -1, ('stor', 256, 0, ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9))))), ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9)))m[uint8(mstor9m[addr(m_from)m]m.field_0 - 1)m] * 256^(4 * mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_0 % 8) or !(4294967295 * 256^(4 * mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_0 % 8)) and mbalanceOfm[addr(m_from)m]m[mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_3 % 536870912m]m.field_0
          mbalanceOfm[addr(m_from)m]m.field_0--
          if mbalanceOfm[addr(m_from)m]m.field_0 > mbalanceOfm[addr(m_from)m]m.field_0 - 1:
              [94ms = (mbalanceOfm[addr(m_from)m]m.field_0 + 6 / 8) + sha3(sha3(addr(m_from), 9))
              mwhile sha3(sha3(addr(m_from), 9)) + (mbalanceOfm[addr(m_from)m]m.field_0 + 7 / 8) > [94msm:
                  mstor[[94msm] = 0
                  [94ms = [94ms + 1
                  mcontinue 
          uint32(mstor10m[uint32(mstor9m[addr(m_from)m]m[0.125 / mstor9m[addr(m_from)m]m.field_0 - 1m]m.field_(32 * stor9[addr(_from)].field_0 - 1 % 8) - 224)m]m.field_0) = uint32(mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_0)
          uint32(mstor10m[mem[(32 * uint32([94midx)) + 156 len 4]m]m.field_0) = 0
          mplayerTokenToApprovedm[mem[(32 * uint32([94midx)) + 128] << 224m] = 0
      mbalanceOfm[addr(m_to)m]m.field_0++
      mbalanceOfm[addr(m_to)m]m[Mask(253, 0, mbalanceOfm[addr(m_to)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(m_to)m]m[Mask(253, 0, mbalanceOfm[addr(m_to)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(m_to)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(m_to)m]m.field_0 % 8) * mem[(32 * uint32([94midx)) + 156 len 4]
      mem[0] = mem[(32 * uint32([94midx)) + 156 len 4]
      mem[32] = 10
      uint32(mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_0) = uint32(mbalanceOfm[addr(m_to)m]m.field_0)
      log Transfer(
            address from=_from,
            address to=_to,
            uint256 value=mem[(32 * uint32(idx)) + 156 len 4])
      [94ms = mem[(32 * uint32([94midx)) + 128]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 6]]
# const = None
# payable = False
def paused(): # not payable
  return bool(mpaused)


# hash = 0x5ecb6594
# getter = ['bool', ['storage', 8, 160, 20]]
# const = None
# payable = False
def isCoreContract(): # not payable
  return bool(misCoreContract)


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


# hash = 0x6275448e
# getter = None
# const = None
# payable = False
def batchApprove(address m_to, uint32[] m_tokenIds): # not payable
  mem[128 len 32 * m_tokenIds.length] = call.data[m_tokenIds + 36 len 32 * m_tokenIds.length]
  require not mpaused
  [94ms = 0
  [94midx = 0
  mwhile uint32([94midx) < m_tokenIds.lengthm:
      require uint32([94midx) < m_tokenIds.length
      if mplayerTokenToOwnerm[mem[(32 * uint32([94midx)) + 156 len 4]m] != caller:
          require mplayerTokenToOwnerm[mem[(32 * uint32([94midx)) + 128] << 224m]
          require mstor11m[mstor7m[mem[(32 * uint32([94midx)) + 128] << 224m]m]m[callerm]
      mem[0] = mem[(32 * uint32([94midx)) + 156 len 4]
      mem[32] = 8
      mplayerTokenToApprovedm[mem[(32 * uint32([94midx)) + 128] << 224m] = m_to
      log Approval(
            address owner=caller,
            address spender=_to,
            uint256 value=mem[(32 * uint32(idx)) + 156 len 4])
      [94ms = mem[(32 * uint32([94midx)) + 128]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0x6352211e
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def ownerOf(uint256 m_tokenId): # not payable
  require mplayerTokenToOwnerm[m_tokenIdm]
  return mplayerTokenToOwnerm[m_tokenIdm]


# hash = 0x6af04a57
# getter = ['storage', 160, 0, 21]
# const = None
# payable = False
def newContractAddress(): # not payable
  return mnewContractAddress


# hash = 0x6bb2374a
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def playerTokenToOwner(uint256 m_param1): # not payable
  return mplayerTokenToOwnerm[m_param1m]


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 9]]]
# const = None
# payable = False
def balanceOf(address m_owner): # not payable
  return mbalanceOfm[addr(m_owner)m]m.field_0


# hash = 0x70ffffec
# getter = ['storage', 16, 0, 0]
# const = None
# payable = False
def MAX_MARKETING_TOKENS(): # not payable
  return mMAX_MARKETING_TOKENS


# hash = 0x7290c21d
# getter = None
# const = None
# payable = False
def auctionCancelled(uint256 m_tokenId, address m_seller): # not payable
  require msaleClockAuctionContractAddress
  require caller == msaleClockAuctionContractAddress
  if this.address == m_seller:
      require m_tokenId < mplayerTokenm.length
      require ext_code.size(mleagueRosterContractAddress)
      call mleagueRosterContractAddress.commissionerAuctionCancelled(uint32 rosterIndex) with:
           gas gas_remaining wei
          args uint32(mplayerTokenm[m_tokenIdm]m.field_0)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log CommissionerAuctionCanceled(uint256 tokenId=_tokenId)


# hash = 0x75d955f7
# getter = None
# const = None
# payable = False
def realWorldPlayerMetadataForPlayerTokenId(uint32 m_playerTokenID): # not payable
  mem[288] = 96
  require m_playerTokenID < mplayerTokenm.length
  require ext_code.size(mleagueRosterContractAddress)
  call mleagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
       gas gas_remaining wei
      args uint32(mplayerTokenm[m_playerTokenIDm]m.field_0)
  mem[320 len 192] = ext_call.return_data[0 len 192]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 192
  mem[256] = bool(ext_call.return_data[160])
  mem[224] = bool(ext_call.return_data[128])
  mem[192] = uint32(ext_call.return_data[96])
  mem[160] = uint64(ext_call.return_data[64])
  mem[128] = uint128(ext_call.return_data[32])
  mem[96] = uint128(ext_call.return_data[0])
  mem[320] = 0x390209c100000000000000000000000000000000000000000000000000000000
  mem[324] = uint128(ext_call.return_data[0])
  require ext_code.size(mleagueRosterContractAddress)
  call mleagueRosterContractAddress.getMetadata(uint128 md5Token) with:
       gas gas_remaining wei
      args uint128(ext_call.return_data[0])
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mem[320 len return_data.size] = ext_call.return_data[0 len return_data.size]
  mem[64] = ceil32(return_data.size) + 320
  require return_data.size >= 32
  [94m_15 = mem[320 len 4], uint128(ext_call.return_data[0]) << 96
  require mem[320 len 4], uint128(ext_call.return_data[0]) << 96 <= 4294967296
  require mem[320 len 4], uint128(ext_call.return_data[0]) << 96 + 32 <= return_data.size
  require return_data.size >= mem[mem[320 len 4], uint128(ext_call.return_data[0]) << 96 + 320] + mem[320 len 4], uint128(ext_call.return_data[0]) << 96 + 32 and mem[mem[320 len 4], uint128(ext_call.return_data[0]) << 96 + 320] <= 4294967296
  mem[ceil32(return_data.size) + 320] = 32
  mem[ceil32(return_data.size) + 352] = mem[[94m_15 + 320]
  [94m_19 = mem[[94m_15 + 320]
  mem[ceil32(return_data.size) + 384 len ceil32(mem[[94m_15 + 320])] = mem[[94m_15 + 352 len ceil32(mem[[94m_15 + 320])]
  if not [94m_19 % 32:
      return 32, mem[ceil32(return_data.size) + 352 len [94m_19 + 32]
  mem[floor32([94m_19) + ceil32(return_data.size) + 384] = mem[floor32([94m_19) + ceil32(return_data.size) + -([94m_19 % 32) + 416 len [94m_19 % 32]
  return 32, mem[ceil32(return_data.size) + 352 len floor32([94m_19) + 64]


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  if mcooAddress != caller:
      if mceoAddress != caller:
          if mcfoAddress != caller:
              require caller == mcommissionerAddress
  require not mpaused
  mpaused = 1


# hash = 0x87800ce2
# getter = None
# const = None
# payable = False
def MD5FromMarketingKeywords(string m_keyWords): # not payable
  mem[128 len m_keyWords.length] = m_keyWords[allm]
  mem[ceil32(m_keyWords.length) + 160 len floor32(m_keyWords.length)] = call.data[m_keyWords + 36 len floor32(m_keyWords.length)]
  mem[ceil32(m_keyWords.length) + floor32(m_keyWords.length) + -(m_keyWords.length % 32) + 192 len m_keyWords.length % 32] = mem[floor32(m_keyWords.length) + -(m_keyWords.length % 32) + 160 len m_keyWords.length % 32]
  mem[m_keyWords.length + ceil32(m_keyWords.length) + 160 len floor32(m_keyWords.length)] = call.data[m_keyWords + 36 len floor32(m_keyWords.length)]
  mem[m_keyWords.length + ceil32(m_keyWords.length) + floor32(m_keyWords.length) + 160] = 256^(-(m_keyWords.length % 32) + 32) - 1 and mem[m_keyWords.length + ceil32(m_keyWords.length) + floor32(m_keyWords.length) + 160] or mem[ceil32(m_keyWords.length) + floor32(m_keyWords.length) + 160] and !(256^(-(m_keyWords.length % 32) + 32) - 1)
  mem[m_keyWords.length + ceil32(m_keyWords.length) + 160] = mstor13m[call.data[m_keyWords + 36 len floor32(m_keyWords.length)]m][mem[m_keyWords.length + ceil32(m_keyWords.length) + floor32(m_keyWords.length) + 160 len m_keyWords.length % 32]m]
  return memory
    from m_keyWords.length + ceil32(m_keyWords.length) + 160
     [93mlen 32


# hash = 0x91876e57
# getter = None
# const = None
# payable = False
def withdrawAuctionBalances(): # not payable
  require caller == mcooAddress
  require ext_code.size(msaleClockAuctionContractAddress)
  call msaleClockAuctionContractAddress.withdrawBalance() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 18]]]], ['loc', 18]]]
# const = None
# payable = False
def symbol(): # not payable
  return msymbolm[0 len msymbolm.lengthm]


# hash = 0x9ca3669d
# getter = None
# const = None
# payable = False
def cancelCommissionerAuction(uint32 m_tokenId): # not payable
  require caller == mcommissionerAddress
  require msaleClockAuctionContractAddress
  require ext_code.size(msaleClockAuctionContractAddress)
  call msaleClockAuctionContractAddress.cancelAuction(uint256 tokenId) with:
       gas gas_remaining wei
      args m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xa22cb465
# getter = None
# const = None
# payable = False
def setApprovalForAll(address m_to, bool m_approved): # not payable
  require m_to != caller
  mstor11m[callerm]m[addr(m_to)m] = uint8(m_approved)
  log ApprovalForAll(
        address owner=_approved,
        address operator=caller,
        bool approved=_to)


# hash = 0xa9741394
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def COMMISSIONER_AUCTION_FLOOR_PRICE(): # not payable
  return uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE)


# hash = 0xaba23628
# getter = None
# const = None
# payable = False
def mintPlayers(uint128[] m_md5Tokens, uint256 m_startPrice, uint256 m_endPrice, uint256 m_duration): # not payable
  mem[96] = m_md5Tokens.length
  mem[128 len 32 * m_md5Tokens.length] = call.data[m_md5Tokens + 36 len 32 * m_md5Tokens.length]
  mem[64] = (32 * m_md5Tokens.length) + 352
  mem[(32 * m_md5Tokens.length) + 128] = 0
  mem[(32 * m_md5Tokens.length) + 160] = 0
  mem[(32 * m_md5Tokens.length) + 192] = 0
  mem[(32 * m_md5Tokens.length) + 224] = 0
  mem[(32 * m_md5Tokens.length) + 256] = 0
  mem[(32 * m_md5Tokens.length) + 288] = 0
  mem[(32 * m_md5Tokens.length) + 320] = 96
  require mleagueRosterContractAddress
  require msaleClockAuctionContractAddress
  if caller == mcommissionerAddress:
      [94ms = 0
      [94ms = 0
      [94midx = 0
      mwhile uint32([94midx) < m_md5Tokens.lengthm:
          require uint32([94midx) < mem[96]
          [94m_493 = mem[(32 * uint32([94midx)) + 128]
          mem[mem[64] + 4] = mem[(32 * uint32([94midx)) + 144 len 16]
          require ext_code.size(mleagueRosterContractAddress)
          call mleagueRosterContractAddress.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
               gas gas_remaining wei
              args ([94m_493 << 128)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if uint128(ext_call.return_data[0]) != 0xffffffffffffffffffffffffffffffff:
              require ext_code.size(mleagueRosterContractAddress)
              call mleagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
                   gas gas_remaining wei
                  args (ext_call.return_data[0] << 128)
              mem[mem[64] len 192] = ext_call.return_data[0 len 192]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 192
              mem[(32 * m_md5Tokens.length) + 288] = bool(ext_call.return_data[160])
              mem[(32 * m_md5Tokens.length) + 256] = bool(ext_call.return_data[128])
              mem[(32 * m_md5Tokens.length) + 224] = uint32(ext_call.return_data[96])
              mem[(32 * m_md5Tokens.length) + 192] = uint64(ext_call.return_data[64])
              mem[(32 * m_md5Tokens.length) + 160] = uint128(ext_call.return_data[32])
              mem[(32 * m_md5Tokens.length) + 128] = uint128(ext_call.return_data[0])
              if uint128([94m_493) == uint128(ext_call.return_data[0]):
                  if ext_call.return_data[160]:
                      if not ext_call.return_data[128]:
                          if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) <= 0xffffffffffffffffffffffffffffffff:
                              if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
                                  if m_startPrice >= uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)):
                                      [94m_539 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_539] = 0
                                      mem[[94m_539 + 32] = 0
                                      mem[[94m_539 + 64] = 0
                                      mem[[94m_539 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_559 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_559] = uint32(ext_call.return_data[0])
                                      mem[[94m_559 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_559 + 64] = uint64(block.timestamp)
                                      mem[[94m_559 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                                  else:
                                      [94m_547 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_547] = 0
                                      mem[[94m_547 + 32] = 0
                                      mem[[94m_547 + 64] = 0
                                      mem[[94m_547 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_579 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_579] = uint32(ext_call.return_data[0])
                                      mem[[94m_579 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_579 + 64] = uint64(block.timestamp)
                                      mem[[94m_579 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                              else:
                                  if m_startPrice >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
                                      [94m_540 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_540] = 0
                                      mem[[94m_540 + 32] = 0
                                      mem[[94m_540 + 64] = 0
                                      mem[[94m_540 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_564 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_564] = uint32(ext_call.return_data[0])
                                      mem[[94m_564 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_564 + 64] = uint64(block.timestamp)
                                      mem[[94m_564 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                                  else:
                                      [94m_548 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_548] = 0
                                      mem[[94m_548 + 32] = 0
                                      mem[[94m_548 + 64] = 0
                                      mem[[94m_548 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_584 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_584] = uint32(ext_call.return_data[0])
                                      mem[[94m_584 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_584 + 64] = uint64(block.timestamp)
                                      mem[[94m_584 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                          else:
                              if 0xffffffffffffffffffffffffffffffff >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
                                  if m_startPrice >= 0xffffffffffffffffffffffffffffffff:
                                      [94m_549 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_549] = 0
                                      mem[[94m_549 + 32] = 0
                                      mem[[94m_549 + 64] = 0
                                      mem[[94m_549 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_589 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_589] = uint32(ext_call.return_data[0])
                                      mem[[94m_589 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_589 + 64] = uint64(block.timestamp)
                                      mem[[94m_589 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                                  else:
                                      [94m_555 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_555] = 0
                                      mem[[94m_555 + 32] = 0
                                      mem[[94m_555 + 64] = 0
                                      mem[[94m_555 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_621 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_621] = uint32(ext_call.return_data[0])
                                      mem[[94m_621 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_621 + 64] = uint64(block.timestamp)
                                      mem[[94m_621 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), 0xffffffffffffffffffffffffffffffff, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), 0xffffffffffffffffffffffffffffffff, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                              else:
                                  if m_startPrice >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
                                      [94m_550 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_550] = 0
                                      mem[[94m_550 + 32] = 0
                                      mem[[94m_550 + 64] = 0
                                      mem[[94m_550 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_594 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_594] = uint32(ext_call.return_data[0])
                                      mem[[94m_594 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_594 + 64] = uint64(block.timestamp)
                                      mem[[94m_594 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                                  else:
                                      [94m_556 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_556] = 0
                                      mem[[94m_556 + 32] = 0
                                      mem[[94m_556 + 64] = 0
                                      mem[[94m_556 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_626 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_626] = uint32(ext_call.return_data[0])
                                      mem[[94m_626 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_626 + 64] = uint64(block.timestamp)
                                      mem[[94m_626 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[mem[64]] = 'T6qy'
                          mem[mem[64] + 4] = uint32(ext_call.return_data[0])
                          mem[mem[64] + 36] = uint128(ext_call.return_data[32])
                          mem[mem[64] + 68] = uint64(block.timestamp)
                          mem[mem[64] + 100] = uint32(uint32(ext_call.return_data[96]) + 1)
                          mem[mem[64] + 132] = 1
                          mem[mem[64] + 164] = bool(ext_call.return_data[160])
                          require ext_code.size(mleagueRosterContractAddress)
                          call mleagueRosterContractAddress.'T6qy' with:
                               gas gas_remaining wei
                              args ext_call.return_data[0] << 224, ext_call.return_data[32] << 128, block.timestamp << 192, uint32(ext_call.return_data[96]) + 1 << 224, 1, bool(ext_call.return_data[160])
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
          [94ms = ext_call.return_data[0]
          [94ms = [94m_493
          [94midx = [94midx + 1
          mcontinue 
  else:
      require caller == mleagueRosterContractAddress
      [94ms = 0
      [94ms = 0
      [94midx = 0
      mwhile uint32([94midx) < m_md5Tokens.lengthm:
          require uint32([94midx) < mem[96]
          [94m_496 = mem[(32 * uint32([94midx)) + 128]
          mem[mem[64] + 4] = mem[(32 * uint32([94midx)) + 144 len 16]
          require ext_code.size(mleagueRosterContractAddress)
          call mleagueRosterContractAddress.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
               gas gas_remaining wei
              args ([94m_496 << 128)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if uint128(ext_call.return_data[0]) != 0xffffffffffffffffffffffffffffffff:
              require ext_code.size(mleagueRosterContractAddress)
              call mleagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
                   gas gas_remaining wei
                  args (ext_call.return_data[0] << 128)
              mem[mem[64] len 192] = ext_call.return_data[0 len 192]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 192
              mem[(32 * m_md5Tokens.length) + 288] = bool(ext_call.return_data[160])
              mem[(32 * m_md5Tokens.length) + 256] = bool(ext_call.return_data[128])
              mem[(32 * m_md5Tokens.length) + 224] = uint32(ext_call.return_data[96])
              mem[(32 * m_md5Tokens.length) + 192] = uint64(ext_call.return_data[64])
              mem[(32 * m_md5Tokens.length) + 160] = uint128(ext_call.return_data[32])
              mem[(32 * m_md5Tokens.length) + 128] = uint128(ext_call.return_data[0])
              if uint128([94m_496) == uint128(ext_call.return_data[0]):
                  if ext_call.return_data[160]:
                      if not ext_call.return_data[128]:
                          if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) <= 0xffffffffffffffffffffffffffffffff:
                              if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
                                  if m_startPrice >= uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)):
                                      [94m_543 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_543] = 0
                                      mem[[94m_543 + 32] = 0
                                      mem[[94m_543 + 64] = 0
                                      mem[[94m_543 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_569 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_569] = uint32(ext_call.return_data[0])
                                      mem[[94m_569 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_569 + 64] = uint64(block.timestamp)
                                      mem[[94m_569 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                                  else:
                                      [94m_551 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_551] = 0
                                      mem[[94m_551 + 32] = 0
                                      mem[[94m_551 + 64] = 0
                                      mem[[94m_551 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_599 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_599] = uint32(ext_call.return_data[0])
                                      mem[[94m_599 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_599 + 64] = uint64(block.timestamp)
                                      mem[[94m_599 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                              else:
                                  if m_startPrice >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
                                      [94m_544 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_544] = 0
                                      mem[[94m_544 + 32] = 0
                                      mem[[94m_544 + 64] = 0
                                      mem[[94m_544 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_574 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_574] = uint32(ext_call.return_data[0])
                                      mem[[94m_574 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_574 + 64] = uint64(block.timestamp)
                                      mem[[94m_574 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                                  else:
                                      [94m_552 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_552] = 0
                                      mem[[94m_552 + 32] = 0
                                      mem[[94m_552 + 64] = 0
                                      mem[[94m_552 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_604 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_604] = uint32(ext_call.return_data[0])
                                      mem[[94m_604 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_604 + 64] = uint64(block.timestamp)
                                      mem[[94m_604 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                          else:
                              if 0xffffffffffffffffffffffffffffffff >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
                                  if m_startPrice >= 0xffffffffffffffffffffffffffffffff:
                                      [94m_553 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_553] = 0
                                      mem[[94m_553 + 32] = 0
                                      mem[[94m_553 + 64] = 0
                                      mem[[94m_553 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_609 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_609] = uint32(ext_call.return_data[0])
                                      mem[[94m_609 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_609 + 64] = uint64(block.timestamp)
                                      mem[[94m_609 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                                  else:
                                      [94m_557 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_557] = 0
                                      mem[[94m_557 + 32] = 0
                                      mem[[94m_557 + 64] = 0
                                      mem[[94m_557 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_633 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_633] = uint32(ext_call.return_data[0])
                                      mem[[94m_633 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_633 + 64] = uint64(block.timestamp)
                                      mem[[94m_633 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), 0xffffffffffffffffffffffffffffffff, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), 0xffffffffffffffffffffffffffffffff, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                              else:
                                  if m_startPrice >= uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE):
                                      [94m_554 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_554] = 0
                                      mem[[94m_554 + 32] = 0
                                      mem[[94m_554 + 64] = 0
                                      mem[[94m_554 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_614 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_614] = uint32(ext_call.return_data[0])
                                      mem[[94m_614 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_614 + 64] = uint64(block.timestamp)
                                      mem[[94m_614 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), m_startPrice, m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                                  else:
                                      [94m_558 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_558] = 0
                                      mem[[94m_558 + 32] = 0
                                      mem[[94m_558 + 64] = 0
                                      mem[[94m_558 + 96] = 0
                                      require uint32(ext_call.return_data[0]) < 4294967295
                                      require uint32(ext_call.return_data[96]) < 4294967295
                                      [94m_638 = mem[64]
                                      mem[64] = mem[64] + 128
                                      mem[[94m_638] = uint32(ext_call.return_data[0])
                                      mem[[94m_638 + 32] = uint32(ext_call.return_data[96])
                                      mem[[94m_638 + 64] = uint64(block.timestamp)
                                      mem[[94m_638 + 96] = 0
                                      mplayerTokenm.length++
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_0) = uint32(ext_call.return_data[0])
                                      uint32(mplayerTokenm[mplayerTokenm.lengthm]m.field_32) = uint32(ext_call.return_data[96])
                                      uint64(mplayerTokenm[mplayerTokenm.lengthm]m.field_64) = uint64(block.timestamp)
                                      uint128(mplayerTokenm[mplayerTokenm.lengthm]m.field_128) = 0
                                      mplayerTokenm[mplayerTokenm.lengthm]m.field_256 % 1 = 0
                                      require mplayerTokenm.length < 4294967295
                                      mplayerTokenToOwnerm[mstor16m.lengthm] = this.address
                                      mbalanceOfm[addr(this.address)m]m.field_0++
                                      mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(this.address)m]m[Mask(253, 0, mbalanceOfm[addr(this.address)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(this.address)m]m.field_0 % 8) * uint32(mplayerTokenm.length)
                                      uint32(mstor10m[uint32(mstor16m.length)m]m.field_0) = uint32(mbalanceOfm[addr(this.address)m]m.field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(mplayerTokenm.length)
                                      mem[32] = 8
                                      mplayerTokenToApprovedm[uint32(mstor16m.length)m] = msaleClockAuctionContractAddress
                                      require ext_code.size(msaleClockAuctionContractAddress)
                                      if m_duration:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endPrice, m_duration, this.address
                                      else:
                                          call msaleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(mplayerTokenm.length), uint256(mCOMMISSIONER_AUCTION_FLOOR_PRICE), m_endPrice, mCOMMISSIONER_AUCTION_DURATION, this.address
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[mem[64]] = 'T6qy'
                          mem[mem[64] + 4] = uint32(ext_call.return_data[0])
                          mem[mem[64] + 36] = uint128(ext_call.return_data[32])
                          mem[mem[64] + 68] = uint64(block.timestamp)
                          mem[mem[64] + 100] = uint32(uint32(ext_call.return_data[96]) + 1)
                          mem[mem[64] + 132] = 1
                          mem[mem[64] + 164] = bool(ext_call.return_data[160])
                          require ext_code.size(mleagueRosterContractAddress)
                          call mleagueRosterContractAddress.'T6qy' with:
                               gas gas_remaining wei
                              args ext_call.return_data[0] << 224, ext_call.return_data[32] << 128, block.timestamp << 192, uint32(ext_call.return_data[96]) + 1 << 224, 1, bool(ext_call.return_data[160])
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
          [94ms = ext_call.return_data[0]
          [94ms = [94m_496
          [94midx = [94midx + 1
          mcontinue 


# hash = 0xb047fb50
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def cooAddress(): # not payable
  return mcooAddress


# hash = 0xb352c562
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def leagueRosterContract(): # not payable
  return mleagueRosterContractAddress


# hash = 0xb42d3b40
# getter = None
# const = None
# payable = False
def setTeamContractAddress(address m_address): # not payable
  require caller == mceoAddress
  require ext_code.size(m_address)
  call m_address.isTeamContract() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mteamContractAddress = m_address


# hash = 0xb5d7d3d8
# getter = ['storage', 160, 0, 15]
# const = None
# payable = False
def teamContract(): # not payable
  return mteamContractAddress


# hash = 0xb88d4fde
# getter = None
# const = None
# payable = True
def safeTransferFrom(address m_from, address m_to, uint256 m_tokenId, bytes m_data) payable: 
  require not mpaused
  require m_to
  require mplayerTokenm.length > m_tokenId
  require mplayerTokenToApprovedm[m_tokenIdm] == m_to
  require mplayerTokenToOwnerm[m_tokenIdm] == m_from
  if mplayerTokenToOwnerm[m_tokenIdm] != caller:
      if mplayerTokenToApprovedm[m_tokenIdm] != caller:
          require mstor11m[addr(m_from)m]m[callerm]
  mplayerTokenToOwnerm[m_tokenIdm] = m_to
  if m_from:
      require mbalanceOfm[addr(m_from)m]m.field_0 - 1 < mbalanceOfm[addr(m_from)m]m.field_0
      require uint32(mstor10m[m_tokenId << 224m]m.field_0) < mbalanceOfm[addr(m_from)m]m.field_0
      mbalanceOfm[addr(m_from)m]m[mstor10m[m_tokenId << 224m]m.field_3 % 536870912m]m.field_0 = mstor('array', ('div', 0.125, ('add', -1, ('stor', 256, 0, ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9))))), ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9)))m[uint8(mstor9m[addr(m_from)m]m.field_0 - 1)m] * 256^(4 * mstor10m[m_tokenId << 224m]m.field_0 % 8) or !(4294967295 * 256^(4 * mstor10m[m_tokenId << 224m]m.field_0 % 8)) and mbalanceOfm[addr(m_from)m]m[mstor10m[m_tokenId << 224m]m.field_3 % 536870912m]m.field_0
      mbalanceOfm[addr(m_from)m]m.field_0--
      if mbalanceOfm[addr(m_from)m]m.field_0 > mbalanceOfm[addr(m_from)m]m.field_0 - 1:
          [94midx = mbalanceOfm[addr(m_from)m]m.field_0 + 6 / 8
          mwhile mbalanceOfm[addr(m_from)m]m.field_0 + 7 / 8 > [94midxm:
              mbalanceOfm[addr(m_from)m]m[[94midxm]m.field_0 = 0
              [94midx = [94midx + 1
              mcontinue 
      uint32(mstor10m[uint32(mstor9m[addr(m_from)m]m[0.125 / mstor9m[addr(m_from)m]m.field_0 - 1m]m.field_(32 * stor9[addr(_from)].field_0 - 1 % 8) - 224)m]m.field_0) = uint32(mstor10m[m_tokenId << 224m]m.field_0)
      uint32(mstor10m[uint32(m_tokenId)m]m.field_0) = 0
      mplayerTokenToApprovedm[m_tokenIdm] = 0
  mbalanceOfm[addr(m_to)m]m.field_0++
  mbalanceOfm[addr(m_to)m]m[Mask(253, 0, mbalanceOfm[addr(m_to)m]m.field_3)m]m.field_0 = mbalanceOfm[addr(m_to)m]m[Mask(253, 0, mbalanceOfm[addr(m_to)m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[addr(m_to)m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[addr(m_to)m]m.field_0 % 8) * uint32(m_tokenId)
  uint32(mstor10m[m_tokenId << 224m]m.field_0) = uint32(mbalanceOfm[addr(m_to)m]m.field_0)
  log Transfer(
        address from=_from,
        address to=_to,
        uint256 value=_tokenId)
  if ext_code.size(m_to) > 0:
      require ext_code.size(m_to)
      call m_to.onERC721Received(address param1, address param2, uint256 param3, bytes param4) with:
           gas 50000 wei
          args 0, uint32(caller), addr(m_from), m_tokenId, 128, m_data.length, m_data[allm]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require Mask(32, 224, sha3('onERC721Received(address,uint256', ',bytes)')) == Mask(32, 224, ext_call.return_data[0])


# hash = 0xb9931d30
# getter = ['struct', ['loc', 16]]
# const = None
# payable = False
def getPlayerToken(uint32 m_playerTokenID): # not payable
  require m_playerTokenID < mplayerTokenm.length
  return uint32(mplayerTokenm[m_playerTokenIDm]m.field_0), 
         uint32(mplayerTokenm[m_playerTokenIDm]m.field_0),
         uint64(mplayerTokenm[m_playerTokenIDm]m.field_0),
         uint128(mplayerTokenm[m_playerTokenIDm]m.field_128)


# hash = 0xc5013863
# getter = ['storage', 160, 0, 20]
# const = None
# payable = False
def saleClockAuctionContract(): # not payable
  return msaleClockAuctionContractAddress


# hash = 0xce88a9ce
# getter = None
# const = None
# payable = False
def setProduction(): # not payable
  require caller == mceoAddress
  require 1 == bool(misDevelopment)
  misDevelopment = 0


# hash = 0xd5bcecab
# getter = None
# const = None
# payable = False
def setLeagueRosterAndSaleAndTeamContractAddress(address m_leagueAddress, address m_saleAddress, address m_teamAddress): # not payable
  require caller == mceoAddress
  if not misDevelopment:
      require not mleagueRosterContractAddress
  require ext_code.size(m_leagueAddress)
  call m_leagueAddress.isLeagueRosterContract() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mleagueRosterContractAddress = m_leagueAddress
  require caller == mceoAddress
  require m_saleAddress
  require ext_code.size(m_saleAddress)
  call m_saleAddress.isSaleClockAuction() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  msaleClockAuctionContractAddress = m_saleAddress
  require caller == mceoAddress
  require ext_code.size(m_teamAddress)
  call m_teamAddress.isTeamContract() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mteamContractAddress = m_teamAddress


# hash = 0xe149f036
# getter = ['storage', 32, ['mask_shl', 3, 0, 5, ['cd', 36]], ['add', ['mask_shl', 253, 3, -3, ['cd', 36]], ['sha3', ['sha3', ['data', ['cd', 4], 9]]]]]
# const = None
# payable = False
def ownedTokens(address m_param1, uint256 m_param2): # not payable
  require m_param2 < mbalanceOfm[m_param1m]m.field_0
  return mownedTokensm[uint8(m_param2)m]


# hash = 0xe3a531a3
# getter = None
# const = None
# payable = False
def setSaleAuctionContractAddress(address m_address): # not payable
  require caller == mceoAddress
  require m_address
  require ext_code.size(m_address)
  call m_address.isSaleClockAuction() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  msaleClockAuctionContractAddress = m_address


# hash = 0xea8037d6
# getter = None
# const = None
# payable = False
def batchEscrowToTeamContract(address m_owner, uint32[] m_tokenIds): # not payable
  mem[128 len 32 * m_tokenIds.length] = call.data[m_tokenIds + 36 len 32 * m_tokenIds.length]
  require not mpaused
  require mteamContractAddress
  require caller == mteamContractAddress
  [94ms = 0
  [94midx = 0
  mwhile uint32([94midx) < m_tokenIds.lengthm:
      require uint32([94midx) < m_tokenIds.length
      require mplayerTokenToOwnerm[mem[(32 * uint32([94midx)) + 156 len 4]m] == m_owner
      mplayerTokenToOwnerm[mem[(32 * uint32([94midx)) + 128] << 224m] = mteamContractAddress
      if m_owner:
          require mbalanceOfm[addr(m_owner)m]m.field_0 - 1 < mbalanceOfm[addr(m_owner)m]m.field_0
          require uint32(mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_0) < mbalanceOfm[addr(m_owner)m]m.field_0
          mbalanceOfm[addr(m_owner)m]m[mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_3 % 536870912m]m.field_0 = mstor('array', ('div', 0.125, ('add', -1, ('stor', 256, 0, ('map', ('mask_shl', 160, 0, 96, ('param', '_owner')), ('name', 'stor9', 9))))), ('map', ('mask_shl', 160, 0, 96, ('param', '_owner')), ('name', 'stor9', 9)))m[uint8(mstor9m[addr(m_owner)m]m.field_0 - 1)m] * 256^(4 * mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_0 % 8) or !(4294967295 * 256^(4 * mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_0 % 8)) and mbalanceOfm[addr(m_owner)m]m[mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_3 % 536870912m]m.field_0
          mbalanceOfm[addr(m_owner)m]m.field_0--
          if mbalanceOfm[addr(m_owner)m]m.field_0 > mbalanceOfm[addr(m_owner)m]m.field_0 - 1:
              [94ms = (mbalanceOfm[addr(m_owner)m]m.field_0 + 6 / 8) + sha3(sha3(addr(m_owner), 9))
              mwhile sha3(sha3(addr(m_owner), 9)) + (mbalanceOfm[addr(m_owner)m]m.field_0 + 7 / 8) > [94msm:
                  mstor[[94msm] = 0
                  [94ms = [94ms + 1
                  mcontinue 
          uint32(mstor10m[uint32(mstor9m[addr(m_owner)m]m[0.125 / mstor9m[addr(m_owner)m]m.field_0 - 1m]m.field_(32 * stor9[addr(_owner)].field_0 - 1 % 8) - 224)m]m.field_0) = uint32(mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_0)
          uint32(mstor10m[mem[(32 * uint32([94midx)) + 156 len 4]m]m.field_0) = 0
          mplayerTokenToApprovedm[mem[(32 * uint32([94midx)) + 128] << 224m] = 0
      mbalanceOfm[mstor15m]m.field_0++
      mbalanceOfm[mstor15m]m[Mask(253, 0, mbalanceOfm[mstor15m]m.field_3)m]m.field_0 = mbalanceOfm[mstor15m]m[Mask(253, 0, mbalanceOfm[mstor15m]m.field_3)m]m.field_0 and !(4294967295 * 256^(4 * mbalanceOfm[mstor15m]m.field_0 % 8)) or 256^(4 * mbalanceOfm[mstor15m]m.field_0 % 8) * mem[(32 * uint32([94midx)) + 156 len 4]
      mem[0] = mem[(32 * uint32([94midx)) + 156 len 4]
      mem[32] = 10
      uint32(mstor10m[mem[(32 * uint32([94midx)) + 128] << 224m]m.field_0) = uint32(mbalanceOfm[mstor15m]m.field_0)
      log Transfer(
            address from=_owner,
            address to=teamContractAddress,
            uint256 value=mem[(32 * uint32(idx)) + 156 len 4])
      [94ms = mem[(32 * uint32([94midx)) + 128]
      [94midx = [94midx + 1
      mcontinue 


# hash = 0xeaf4170c
# getter = None
# const = ['return', 1]
# payable = False
const implementsSaleClockAuctionListener = 1


# hash = 0xeb2c0223
# getter = None
# const = None
# payable = False
def upgradeContract(address m_newContract): # not payable
  require caller == mceoAddress
  require mpaused
  mnewContractAddress = m_newContract
  log ContractUpgrade(address newContract=_newContract)


# hash = 0xf418b153
# getter = None
# const = None
# payable = False
def replaceMarketingToken(uint256 m_oldKeywordHash, uint256 m_newKeywordHash, uint128 m_md5Token): # not payable
  require caller == mcommissionerAddress
  if mstor13m[m_oldKeywordHashm]:
      mstor13m[m_oldKeywordHashm] = 0
      mstor13m[m_newKeywordHashm] = m_md5Token
      log MarketingTokenReplaced(
            uint256 oldHash=_oldKeywordHash,
            uint256 newHash=_newKeywordHash,
            uint128 rwpMd5=_md5Token)


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  stop


