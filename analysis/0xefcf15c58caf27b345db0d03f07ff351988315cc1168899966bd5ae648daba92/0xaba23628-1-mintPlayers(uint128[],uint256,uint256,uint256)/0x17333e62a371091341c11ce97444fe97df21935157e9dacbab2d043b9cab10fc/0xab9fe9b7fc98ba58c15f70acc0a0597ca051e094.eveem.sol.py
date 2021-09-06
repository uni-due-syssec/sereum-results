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
def getKeccak256(string _stringToHash): # not payable
  mem[128 len _stringToHash.length] = _stringToHash[all]
  mem[ceil32(_stringToHash.length) + 160 len floor32(_stringToHash.length)] = call.data[_stringToHash + 36 len floor32(_stringToHash.length)]
  mem[ceil32(_stringToHash.length) + floor32(_stringToHash.length) + -(_stringToHash.length % 32) + 192 len _stringToHash.length % 32] = mem[floor32(_stringToHash.length) + -(_stringToHash.length % 32) + 160 len _stringToHash.length % 32]
  mem[_stringToHash.length + ceil32(_stringToHash.length) + 160 len floor32(_stringToHash.length)] = call.data[_stringToHash + 36 len floor32(_stringToHash.length)]
  mem[_stringToHash.length + ceil32(_stringToHash.length) + floor32(_stringToHash.length) + 160] = mem[_stringToHash.length + ceil32(_stringToHash.length) + floor32(_stringToHash.length) + 160] and 256^(-(_stringToHash.length % 32) + 32) - 1 or mem[ceil32(_stringToHash.length) + floor32(_stringToHash.length) + 160] and !(256^(-(_stringToHash.length % 32) + 32) - 1)
  mem[_stringToHash.length + ceil32(_stringToHash.length) + 160] = sha3(call.data[_stringToHash + 36 len floor32(_stringToHash.length)], mem[_stringToHash.length + ceil32(_stringToHash.length) + floor32(_stringToHash.length) + 160 len _stringToHash.length % 32])
  return memory
    from _stringToHash.length + ceil32(_stringToHash.length) + 160
     [93mlen 32


# hash = 0x01ffc9a7
# getter = None
# const = None
# payable = False
def supportsInterface(bytes4 _interfaceId): # not payable
  if 0x1ffc9a700000000000000000000000000000000000000000000000000000000 == Mask(32, 224, _interfaceId):
      return True
  if Mask(32, 224, _interfaceId) == 0x5b5e139f00000000000000000000000000000000000000000000000000000000:
      return True
  if Mask(32, 224, _interfaceId) == 0x80ac58cd00000000000000000000000000000000000000000000000000000000:
      return True
  return (Mask(32, 224, _interfaceId) == 0x780e9d6300000000000000000000000000000000000000000000000000000000)


# hash = 0x04869083
# getter = None
# const = None
# payable = False
def auctionCreated(uint256 _param1, address _param2, uint128 _param3, uint128 _param4, uint64 _param5): # not payable
  require saleClockAuctionContractAddress
  require caller == saleClockAuctionContractAddress


# hash = 0x0519ce79
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def cfoAddress(): # not payable
  return cfoAddress


# hash = 0x06fdde03
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 17]]]], ['loc', 17]]]
# const = None
# payable = False
def name(): # not payable
  return name[0 len name.length]


# hash = 0x081812fc
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 8]]]
# const = None
# payable = False
def getApproved(uint256 _tokenId): # not payable
  require playerToken.length > _tokenId
  return playerTokenToApproved[_tokenId]


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address _spender, uint256 _value): # not payable
  require not paused
  require playerTokenToOwner[_value]
  require playerTokenToOwner[_value] != _spender
  if playerTokenToOwner[_value] != caller:
      require playerTokenToOwner[_value]
      require stor11[stor7[_value]][caller]
  playerTokenToApproved[_value] = _spender
  log Approval(
        address owner=caller,
        address spender=_spender,
        uint256 value=_value)


# hash = 0x0a0f8168
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def ceoAddress(): # not payable
  return ceoAddress


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
  return playerToken.length


# hash = 0x1ace88a4
# getter = None
# const = None
# payable = False
def realWorldPlayerTokenForPlayerTokenId(uint32 _playerTokenID): # not payable
  require _playerTokenID < playerToken.length
  require ext_code.size(leagueRosterContractAddress)
  call leagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
       gas gas_remaining wei
      args uint32(playerToken[_playerTokenID].field_0)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 192
  return uint128(ext_call.return_data[0])


# hash = 0x1cc14cbc
# getter = ['bool', ['storage', 8, 168, 6]]
# const = None
# payable = False
def isDevelopment(): # not payable
  return bool(isDevelopment)


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address _from, address _to, uint256 _value): # not payable
  require not paused
  require _to
  require playerToken.length > _value
  require playerTokenToApproved[_value] == _to
  require playerTokenToOwner[_value] == _from
  if playerTokenToOwner[_value] != caller:
      if playerTokenToApproved[_value] != caller:
          require stor11[addr(_from)][caller]
  playerTokenToOwner[_value] = _to
  if _from:
      require balanceOf[addr(_from)].field_0 - 1 < balanceOf[addr(_from)].field_0
      require uint32(stor10[_value << 224].field_0) < balanceOf[addr(_from)].field_0
      balanceOf[addr(_from)][stor10[_value << 224].field_3 % 536870912].field_0 = stor('array', ('div', 0.125, ('add', -1, ('stor', 256, 0, ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9))))), ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9)))[uint8(stor9[addr(_from)].field_0 - 1)] * 256^(4 * stor10[_value << 224].field_0 % 8) or !(4294967295 * 256^(4 * stor10[_value << 224].field_0 % 8)) and balanceOf[addr(_from)][stor10[_value << 224].field_3 % 536870912].field_0
      balanceOf[addr(_from)].field_0--
      if balanceOf[addr(_from)].field_0 > balanceOf[addr(_from)].field_0 - 1:
          [94midx = balanceOf[addr(_from)].field_0 + 6 / 8
          while balanceOf[addr(_from)].field_0 + 7 / 8 > [94midx:
              balanceOf[addr(_from)][[94midx].field_0 = 0
              [94midx = [94midx + 1
              continue 
      uint32(stor10[uint32(stor9[addr(_from)][0.125 / stor9[addr(_from)].field_0 - 1].field_(32 * stor9[addr(_from)].field_0 - 1 % 8) - 224)].field_0) = uint32(stor10[_value << 224].field_0)
      uint32(stor10[uint32(_value)].field_0) = 0
      playerTokenToApproved[_value] = 0
  balanceOf[addr(_to)].field_0++
  balanceOf[addr(_to)][Mask(253, 0, balanceOf[addr(_to)].field_3)].field_0 = balanceOf[addr(_to)][Mask(253, 0, balanceOf[addr(_to)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(_to)].field_0 % 8)) or 256^(4 * balanceOf[addr(_to)].field_0 % 8) * uint32(_value)
  uint32(stor10[_value << 224].field_0) = uint32(balanceOf[addr(_to)].field_0)
  log Transfer(
        address from=_from,
        address to=_to,
        uint256 value=_value)


# hash = 0x27d7874c
# getter = None
# const = None
# payable = False
def setCEO(address _newCEO): # not payable
  require caller == ceoAddress
  require _newCEO
  ceoAddress = _newCEO


# hash = 0x2ba73c15
# getter = None
# const = None
# payable = False
def setCOO(address _newCOO): # not payable
  require caller == ceoAddress
  require _newCOO
  cooAddress = _newCOO


# hash = 0x2bfe243f
# getter = None
# const = None
# payable = False
def minStartPriceForCommishAuctions(uint128[] _md5Tokens): # not payable
  mem[128 len 32 * _md5Tokens.length] = call.data[_md5Tokens + 36 len 32 * _md5Tokens.length]
  mem[(32 * _md5Tokens.length) + 128 len 1600] = code.data[17799 len 1600]
  mem[(32 * _md5Tokens.length) + 1728 len 1600] = code.data[17799 len 1600]
  mem[(32 * _md5Tokens.length) + 3328] = 0
  mem[(32 * _md5Tokens.length) + 3360] = 0
  mem[(32 * _md5Tokens.length) + 3392] = 0
  mem[(32 * _md5Tokens.length) + 3424] = 0
  mem[(32 * _md5Tokens.length) + 3456] = 0
  mem[(32 * _md5Tokens.length) + 3488] = 0
  mem[(32 * _md5Tokens.length) + 3520] = 96
  require caller == commissionerAddress
  require 50 >= _md5Tokens.length
  [94ms = 0
  [94ms = 0
  [94midx = 0
  while uint32([94midx) < _md5Tokens.length:
      require uint32([94midx) < _md5Tokens.length
      [94m_28 = mem[(32 * uint32([94midx)) + 128]
      mem[(32 * _md5Tokens.length) + 3556] = mem[(32 * uint32([94midx)) + 144 len 16]
      require ext_code.size(leagueRosterContractAddress)
      call leagueRosterContractAddress.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
           gas gas_remaining wei
          args uint128([94m_28)
      mem[(32 * _md5Tokens.length) + 3552] = ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if uint128(ext_call.return_data[0]) != 0xffffffffffffffffffffffffffffffff:
          require ext_code.size(leagueRosterContractAddress)
          call leagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
               gas gas_remaining wei
              args uint128(ext_call.return_data[0])
          mem[(32 * _md5Tokens.length) + 3552 len 192] = ext_call.return_data[0 len 192]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 192
          mem[(32 * _md5Tokens.length) + 3488] = bool(ext_call.return_data[160])
          mem[(32 * _md5Tokens.length) + 3456] = bool(ext_call.return_data[128])
          mem[(32 * _md5Tokens.length) + 3424] = uint32(ext_call.return_data[96])
          mem[(32 * _md5Tokens.length) + 3392] = uint64(ext_call.return_data[64])
          mem[(32 * _md5Tokens.length) + 3360] = uint128(ext_call.return_data[32])
          mem[(32 * _md5Tokens.length) + 3328] = uint128(ext_call.return_data[0])
          if uint128([94m_28) == uint128(ext_call.return_data[0]):
              require uint32([94midx) < 50
              if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) <= 0xffffffffffffffffffffffffffffffff:
                  if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
                      mem[(32 * uint32([94midx)) + (32 * _md5Tokens.length) + 1728] = uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4))
                  else:
                      mem[(32 * uint32([94midx)) + (32 * _md5Tokens.length) + 1728] = uint128(stor1)
              else:
                  if 0xffffffffffffffffffffffffffffffff >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
                      mem[(32 * uint32([94midx)) + (32 * _md5Tokens.length) + 1728] = 0xffffffffffffffffffffffffffffffff
                  else:
                      mem[(32 * uint32([94midx)) + (32 * _md5Tokens.length) + 1728] = uint128(stor1)
      [94ms = ext_call.return_data[0]
      [94ms = [94m_28
      [94midx = [94midx + 1
      continue 
  return memory
    from (32 * _md5Tokens.length) + 1728
     [93mlen 1600


# hash = 0x2d90dd92
# getter = ['storage', 16, 0, 12]
# const = None
# payable = False
def remainingMarketingTokens(): # not payable
  return remainingMarketingTokens


# hash = 0x2e43ec0c
# getter = ['storage', 160, 0, 6]
# const = None
# payable = False
def commissionerAddress(): # not payable
  return commissionerAddress


# hash = 0x2f745c59
# getter = ['storage', 32, ['mask_shl', 3, 0, 5, ['cd', 36]], ['add', ['mask_shl', 253, 3, -3, ['cd', 36]], ['sha3', ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 9]]]]]
# const = None
# payable = False
def tokenOfOwnerByIndex(address _owner, uint256 _index): # not payable
  require _owner
  require _index < balanceOf[addr(_owner)].field_0
  require _index < balanceOf[addr(_owner)].field_0
  return tokenOfOwnerByIndex[uint8(_index)]


# hash = 0x30d1f3e3
# getter = ['struct', ['loc', 16]]
# const = None
# payable = False
def playerTokens(uint256 _param1): # not payable
  require _param1 < playerToken.length
  return uint32(playerToken[_param1].field_0), 
         uint32(playerToken[_param1].field_0),
         uint64(playerToken[_param1].field_0),
         uint128(playerToken[_param1].field_128)


# hash = 0x325ecf99
# getter = None
# const = None
# payable = False
def addMarketingToken(uint256 _keywordHash, uint128 _md5Token): # not payable
  require caller == commissionerAddress
  require remainingMarketingTokens > 0
  require not stor13[_keywordHash]
  require ext_code.size(leagueRosterContractAddress)
  call leagueRosterContractAddress.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
       gas gas_remaining wei
      args _md5Token
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[16 len 16] != 0xffffffffffffffffffffffffffffffff
  remainingMarketingTokens = uint16(remainingMarketingTokens - 1)
  stor13[_keywordHash] = _md5Token
  log MarketingTokenCreated(
        uint256 hash=_keywordHash,
        uint128 rwpMd5=_md5Token)


# hash = 0x334e712f
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def COMMISSIONER_AUCTION_DURATION(): # not payable
  return COMMISSIONER_AUCTION_DURATION


# hash = 0x36e685f5
# getter = None
# const = None
# payable = False
def setCLevelAddresses(address _ceo, address _cfo, address _coo, address _commish): # not payable
  require caller == ceoAddress
  require _ceo
  require _cfo
  require _coo
  require _commish
  ceoAddress = _ceo
  cfoAddress = _cfo
  cooAddress = _coo
  commissionerAddress = _commish


# hash = 0x3d7d3f5a
# getter = None
# const = None
# payable = False
def createSaleAuction(uint256 _artworkId, uint256 _startingPrice, uint256 _endingPrice, uint256 _duration): # not payable
  require not paused
  require playerTokenToOwner[_artworkId] == caller
  playerTokenToApproved[_artworkId] = saleClockAuctionContractAddress
  require ext_code.size(saleClockAuctionContractAddress)
  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
       gas gas_remaining wei
      args 0, uint32(_artworkId), _startingPrice, _endingPrice, _duration, caller
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x3d83230f
# getter = None
# const = None
# payable = False
def auctionSuccessful(uint256 _tokenId, uint128 _totalPrice, address _seller, address _winner): # not payable
  require saleClockAuctionContractAddress
  require caller == saleClockAuctionContractAddress
  require _tokenId < playerToken.length
  uint128(playerToken[_tokenId].field_128) = _totalPrice
  if this.address == _seller:
      require _tokenId < playerToken.length
      require ext_code.size(leagueRosterContractAddress)
      call leagueRosterContractAddress.commissionerAuctionComplete(uint32 rosterIndex, uint128 price) with:
           gas gas_remaining wei
          args uint32(playerToken[_tokenId].field_0), _totalPrice
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
  require caller == ceoAddress
  require paused
  require leagueRosterContractAddress
  require saleClockAuctionContractAddress
  require not newContractAddress
  require caller == ceoAddress
  require paused
  paused = 0


# hash = 0x41ba7011
# getter = None
# const = None
# payable = False
def setLeagueRosterContractAddress(address _address): # not payable
  require caller == ceoAddress
  if not isDevelopment:
      require not leagueRosterContractAddress
  require ext_code.size(_address)
  call _address.isLeagueRosterContract() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  leagueRosterContractAddress = _address


# hash = 0x42842e0e
# getter = None
# const = None
# payable = True
def safeTransferFrom(address _from, address _to, uint256 _tokenId) payable: 
  require _to
  require not paused
  require _to
  require playerToken.length > _tokenId
  require playerTokenToApproved[_tokenId] == _to
  require playerTokenToOwner[_tokenId] == _from
  if playerTokenToOwner[_tokenId] != caller:
      if playerTokenToApproved[_tokenId] != caller:
          require stor11[addr(_from)][caller]
  playerTokenToOwner[_tokenId] = _to
  if _from:
      require balanceOf[addr(_from)].field_0 - 1 < balanceOf[addr(_from)].field_0
      require uint32(stor10[_tokenId << 224].field_0) < balanceOf[addr(_from)].field_0
      balanceOf[addr(_from)][stor10[_tokenId << 224].field_3 % 536870912].field_0 = stor('array', ('div', 0.125, ('add', -1, ('stor', 256, 0, ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9))))), ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9)))[uint8(stor9[addr(_from)].field_0 - 1)] * 256^(4 * stor10[_tokenId << 224].field_0 % 8) or !(4294967295 * 256^(4 * stor10[_tokenId << 224].field_0 % 8)) and balanceOf[addr(_from)][stor10[_tokenId << 224].field_3 % 536870912].field_0
      balanceOf[addr(_from)].field_0--
      if balanceOf[addr(_from)].field_0 > balanceOf[addr(_from)].field_0 - 1:
          [94midx = balanceOf[addr(_from)].field_0 + 6 / 8
          while balanceOf[addr(_from)].field_0 + 7 / 8 > [94midx:
              balanceOf[addr(_from)][[94midx].field_0 = 0
              [94midx = [94midx + 1
              continue 
      uint32(stor10[uint32(stor9[addr(_from)][0.125 / stor9[addr(_from)].field_0 - 1].field_(32 * stor9[addr(_from)].field_0 - 1 % 8) - 224)].field_0) = uint32(stor10[_tokenId << 224].field_0)
      uint32(stor10[uint32(_tokenId)].field_0) = 0
      playerTokenToApproved[_tokenId] = 0
  balanceOf[addr(_to)].field_0++
  balanceOf[addr(_to)][Mask(253, 0, balanceOf[addr(_to)].field_3)].field_0 = balanceOf[addr(_to)][Mask(253, 0, balanceOf[addr(_to)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(_to)].field_0 % 8)) or 256^(4 * balanceOf[addr(_to)].field_0 % 8) * uint32(_tokenId)
  uint32(stor10[_tokenId << 224].field_0) = uint32(balanceOf[addr(_to)].field_0)
  log Transfer(
        address from=_from,
        address to=_to,
        uint256 value=_tokenId)
  if ext_code.size(_to) > 0:
      require ext_code.size(_to)
      call _to.onERC721Received(address param1, address param2, uint256 param3, bytes param4) with:
           gas 50000 wei
          args 0, uint32(caller), addr(_from), _tokenId, 128, 0, mem[260]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require Mask(32, 224, sha3('onERC721Received(address,uint256', ',bytes)')) == Mask(32, 224, ext_call.return_data[0])


# hash = 0x4682ff71
# getter = None
# const = None
# payable = False
def redeemMarketingToken(string _keyWords): # not payable
  mem[128 len _keyWords.length] = _keyWords[all]
  mem[ceil32(_keyWords.length) + 128] = 0
  mem[ceil32(_keyWords.length) + 160] = 0
  mem[ceil32(_keyWords.length) + 384 len floor32(_keyWords.length)] = call.data[_keyWords + 36 len floor32(_keyWords.length)]
  mem[ceil32(_keyWords.length) + floor32(_keyWords.length) + -(_keyWords.length % 32) + 416 len _keyWords.length % 32] = mem[floor32(_keyWords.length) + -(_keyWords.length % 32) + 160 len _keyWords.length % 32]
  mem[_keyWords.length + ceil32(_keyWords.length) + 384 len floor32(_keyWords.length)] = call.data[_keyWords + 36 len floor32(_keyWords.length)]
  mem[_keyWords.length + ceil32(_keyWords.length) + floor32(_keyWords.length) + 384] = 256^(-(_keyWords.length % 32) + 32) - 1 and mem[_keyWords.length + ceil32(_keyWords.length) + floor32(_keyWords.length) + 384] or mem[ceil32(_keyWords.length) + floor32(_keyWords.length) + 384 len -(_keyWords.length % 32) + 32], mem[floor32(_keyWords.length) + -(_keyWords.length % 32) + 160 len _keyWords.length % 32] and !(256^(-(_keyWords.length % 32) + 32) - 1)
  if stor13[call.data[_keyWords + 36 len floor32(_keyWords.length)]][mem[_keyWords.length + ceil32(_keyWords.length) + floor32(_keyWords.length) + 384 len _keyWords.length % 32]]:
      stor13[call.data[_keyWords + 36 len floor32(_keyWords.length)]][mem[_keyWords.length + ceil32(_keyWords.length) + floor32(_keyWords.length) + 384 len _keyWords.length % 32]] = 0
      require ext_code.size(leagueRosterContractAddress)
      call leagueRosterContractAddress.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
           gas gas_remaining wei
          args stor13[call.data[_keyWords + 36 len floor32(_keyWords.length)]][mem[_keyWords.length + ceil32(_keyWords.length) + floor32(_keyWords.length) + 384 len _keyWords.length % 32]]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if uint128(ext_call.return_data[0]) != 0xffffffffffffffffffffffffffffffff:
          require ext_code.size(leagueRosterContractAddress)
          call leagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
               gas gas_remaining wei
              args uint128(ext_call.return_data[0])
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 192
          require uint32(ext_call.return_data[0]) < 4294967295
          require uint32(ext_call.return_data[96]) < 4294967295
          playerToken.length++
          uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
          uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
          uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
          uint128(playerToken[playerToken.length].field_128) = 0
          playerToken[playerToken.length].field_256 % 1 = 0
          require playerToken.length < 4294967295
          playerTokenToOwner[stor16.length] = caller
          balanceOf[caller].field_0++
          balanceOf[caller][Mask(253, 0, balanceOf[caller].field_3)].field_0 = balanceOf[caller][Mask(253, 0, balanceOf[caller].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[caller].field_0 % 8)) or 256^(4 * balanceOf[caller].field_0 % 8) * uint32(playerToken.length)
          uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[caller].field_0)
          log Transfer(
                address from=0,
                address to=caller,
                uint256 value=playerToken.length)
          require ext_code.size(leagueRosterContractAddress)
          call leagueRosterContractAddress.'T6qy' with:
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
def playerTokenToApproved(uint256 _param1): # not payable
  return playerTokenToApproved[_param1]


# hash = 0x4e0a3379
# getter = None
# const = None
# payable = False
def setCFO(address _newCFO): # not payable
  require caller == ceoAddress
  require _newCFO
  cfoAddress = _newCFO


# hash = 0x4e0c4a9c
# getter = None
# const = None
# payable = False
def setCommissioner(address _newCommissioner): # not payable
  require caller == ceoAddress
  require _newCommissioner
  commissionerAddress = _newCommissioner


# hash = 0x4e41ebf6
# getter = None
# const = None
# payable = False
def createCommissionerAuction(uint32 _playerTokenId, uint256 _startingPrice, uint256 _endingPrice, uint256 _duration): # not payable
  require not paused
  require caller == commissionerAddress
  require leagueRosterContractAddress
  require _playerTokenId < playerToken.length
  require playerTokenToOwner[_playerTokenId << 224] == this.address
  require _playerTokenId < playerToken.length
  require ext_code.size(leagueRosterContractAddress)
  call leagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
       gas gas_remaining wei
      args uint32(playerToken[_playerTokenId].field_0)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 192
  playerTokenToApproved[_playerTokenId << 224] = saleClockAuctionContractAddress
  require ext_code.size(saleClockAuctionContractAddress)
  if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) <= 0xffffffffffffffffffffffffffffffff:
      if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
          if _startingPrice >= uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)):
              if _duration:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, _startingPrice, _endingPrice, _duration, this.address
              else:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, _startingPrice, _endingPrice, COMMISSIONER_AUCTION_DURATION, this.address
          else:
              if _duration:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, _endingPrice, _duration, this.address
              else:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, _endingPrice, COMMISSIONER_AUCTION_DURATION, this.address
      else:
          if _startingPrice >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
              if _duration:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, _startingPrice, _endingPrice, _duration, this.address
              else:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, _startingPrice, _endingPrice, COMMISSIONER_AUCTION_DURATION, this.address
          else:
              if _duration:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endingPrice, _duration, this.address
              else:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endingPrice, COMMISSIONER_AUCTION_DURATION, this.address
  else:
      if 0xffffffffffffffffffffffffffffffff >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
          if _startingPrice >= 0xffffffffffffffffffffffffffffffff:
              if _duration:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, _startingPrice, _endingPrice, _duration, this.address
              else:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, _startingPrice, _endingPrice, COMMISSIONER_AUCTION_DURATION, this.address
          else:
              if _duration:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, 0xffffffffffffffffffffffffffffffff, _endingPrice, _duration, this.address
              else:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, 0xffffffffffffffffffffffffffffffff, _endingPrice, COMMISSIONER_AUCTION_DURATION, this.address
      else:
          if _startingPrice >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
              if _duration:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, _startingPrice, _endingPrice, _duration, this.address
              else:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, _startingPrice, _endingPrice, COMMISSIONER_AUCTION_DURATION, this.address
          else:
              if _duration:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endingPrice, _duration, this.address
              else:
                  call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                       gas gas_remaining wei
                      args _playerTokenId << 224, uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endingPrice, COMMISSIONER_AUCTION_DURATION, this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x4f6ccce7
# getter = None
# const = None
# payable = False
def tokenByIndex(uint256 _index): # not payable
  require playerToken.length > _index
  return _index


# hash = 0x50e59eb3
# getter = None
# const = ['return', 1]
# payable = False
const isMinter = 1


# hash = 0x54367179
# getter = None
# const = None
# payable = False
def updateRealWorldPlayer(uint32 _rosterIndex, uint128 _prevCommissionerSalePrice, uint64 _lastMintedTime, uint32 _mintedCount, bool _hasActiveCommissionerAuction, bool _mintingEnabled): # not payable
  require caller == ceoAddress
  require 1 == bool(isDevelopment)
  require leagueRosterContractAddress
  require ext_code.size(leagueRosterContractAddress)
  call leagueRosterContractAddress.'T6qy' with:
       gas gas_remaining wei
      args Mask(224, 0, 'T6qy'), 0, _prevCommissionerSalePrice << 128, _lastMintedTime << 192, _mintedCount, _hasActiveCommissionerAuction, _mintingEnabled
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x555fe48a
# getter = None
# const = None
# payable = False
def batchTransferFrom(address _from, address _to, uint32[] _tokenIds): # not payable
  mem[128 len 32 * _tokenIds.length] = call.data[_tokenIds + 36 len 32 * _tokenIds.length]
  require not paused
  [94ms = 0
  [94midx = 0
  while uint32([94midx) < _tokenIds.length:
      require uint32([94midx) < _tokenIds.length
      require playerTokenToApproved[mem[(32 * uint32([94midx)) + 156 len 4]] == _to
      require playerTokenToOwner[mem[(32 * uint32([94midx)) + 128] << 224] == _from
      if playerTokenToOwner[mem[(32 * uint32([94midx)) + 128] << 224] != caller:
          if playerTokenToApproved[mem[(32 * uint32([94midx)) + 128] << 224] != caller:
              require stor11[addr(_from)][caller]
      playerTokenToOwner[mem[(32 * uint32([94midx)) + 128] << 224] = _to
      if _from:
          require balanceOf[addr(_from)].field_0 - 1 < balanceOf[addr(_from)].field_0
          require uint32(stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_0) < balanceOf[addr(_from)].field_0
          balanceOf[addr(_from)][stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_3 % 536870912].field_0 = stor('array', ('div', 0.125, ('add', -1, ('stor', 256, 0, ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9))))), ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9)))[uint8(stor9[addr(_from)].field_0 - 1)] * 256^(4 * stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_0 % 8) or !(4294967295 * 256^(4 * stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_0 % 8)) and balanceOf[addr(_from)][stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_3 % 536870912].field_0
          balanceOf[addr(_from)].field_0--
          if balanceOf[addr(_from)].field_0 > balanceOf[addr(_from)].field_0 - 1:
              [94ms = (balanceOf[addr(_from)].field_0 + 6 / 8) + sha3(sha3(addr(_from), 9))
              while sha3(sha3(addr(_from), 9)) + (balanceOf[addr(_from)].field_0 + 7 / 8) > [94ms:
                  stor[[94ms] = 0
                  [94ms = [94ms + 1
                  continue 
          uint32(stor10[uint32(stor9[addr(_from)][0.125 / stor9[addr(_from)].field_0 - 1].field_(32 * stor9[addr(_from)].field_0 - 1 % 8) - 224)].field_0) = uint32(stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_0)
          uint32(stor10[mem[(32 * uint32([94midx)) + 156 len 4]].field_0) = 0
          playerTokenToApproved[mem[(32 * uint32([94midx)) + 128] << 224] = 0
      balanceOf[addr(_to)].field_0++
      balanceOf[addr(_to)][Mask(253, 0, balanceOf[addr(_to)].field_3)].field_0 = balanceOf[addr(_to)][Mask(253, 0, balanceOf[addr(_to)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(_to)].field_0 % 8)) or 256^(4 * balanceOf[addr(_to)].field_0 % 8) * mem[(32 * uint32([94midx)) + 156 len 4]
      mem[0] = mem[(32 * uint32([94midx)) + 156 len 4]
      mem[32] = 10
      uint32(stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_0) = uint32(balanceOf[addr(_to)].field_0)
      log Transfer(
            address from=_from,
            address to=_to,
            uint256 value=mem[(32 * uint32(idx)) + 156 len 4])
      [94ms = mem[(32 * uint32([94midx)) + 128]
      [94midx = [94midx + 1
      continue 


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 6]]
# const = None
# payable = False
def paused(): # not payable
  return bool(paused)


# hash = 0x5ecb6594
# getter = ['bool', ['storage', 8, 160, 20]]
# const = None
# payable = False
def isCoreContract(): # not payable
  return bool(isCoreContract)


# hash = 0x5fd8c710
# getter = None
# const = None
# payable = False
def withdrawBalance(): # not payable
  require caller == cfoAddress
  call cfoAddress with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x6275448e
# getter = None
# const = None
# payable = False
def batchApprove(address _to, uint32[] _tokenIds): # not payable
  mem[128 len 32 * _tokenIds.length] = call.data[_tokenIds + 36 len 32 * _tokenIds.length]
  require not paused
  [94ms = 0
  [94midx = 0
  while uint32([94midx) < _tokenIds.length:
      require uint32([94midx) < _tokenIds.length
      if playerTokenToOwner[mem[(32 * uint32([94midx)) + 156 len 4]] != caller:
          require playerTokenToOwner[mem[(32 * uint32([94midx)) + 128] << 224]
          require stor11[stor7[mem[(32 * uint32([94midx)) + 128] << 224]][caller]
      mem[0] = mem[(32 * uint32([94midx)) + 156 len 4]
      mem[32] = 8
      playerTokenToApproved[mem[(32 * uint32([94midx)) + 128] << 224] = _to
      log Approval(
            address owner=caller,
            address spender=_to,
            uint256 value=mem[(32 * uint32(idx)) + 156 len 4])
      [94ms = mem[(32 * uint32([94midx)) + 128]
      [94midx = [94midx + 1
      continue 


# hash = 0x6352211e
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def ownerOf(uint256 _tokenId): # not payable
  require playerTokenToOwner[_tokenId]
  return playerTokenToOwner[_tokenId]


# hash = 0x6af04a57
# getter = ['storage', 160, 0, 21]
# const = None
# payable = False
def newContractAddress(): # not payable
  return newContractAddress


# hash = 0x6bb2374a
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def playerTokenToOwner(uint256 _param1): # not payable
  return playerTokenToOwner[_param1]


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 9]]]
# const = None
# payable = False
def balanceOf(address _owner): # not payable
  return balanceOf[addr(_owner)].field_0


# hash = 0x70ffffec
# getter = ['storage', 16, 0, 0]
# const = None
# payable = False
def MAX_MARKETING_TOKENS(): # not payable
  return MAX_MARKETING_TOKENS


# hash = 0x7290c21d
# getter = None
# const = None
# payable = False
def auctionCancelled(uint256 _tokenId, address _seller): # not payable
  require saleClockAuctionContractAddress
  require caller == saleClockAuctionContractAddress
  if this.address == _seller:
      require _tokenId < playerToken.length
      require ext_code.size(leagueRosterContractAddress)
      call leagueRosterContractAddress.commissionerAuctionCancelled(uint32 rosterIndex) with:
           gas gas_remaining wei
          args uint32(playerToken[_tokenId].field_0)
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      log CommissionerAuctionCanceled(uint256 tokenId=_tokenId)


# hash = 0x75d955f7
# getter = None
# const = None
# payable = False
def realWorldPlayerMetadataForPlayerTokenId(uint32 _playerTokenID): # not payable
  mem[288] = 96
  require _playerTokenID < playerToken.length
  require ext_code.size(leagueRosterContractAddress)
  call leagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
       gas gas_remaining wei
      args uint32(playerToken[_playerTokenID].field_0)
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
  require ext_code.size(leagueRosterContractAddress)
  call leagueRosterContractAddress.getMetadata(uint128 md5Token) with:
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
  if cooAddress != caller:
      if ceoAddress != caller:
          if cfoAddress != caller:
              require caller == commissionerAddress
  require not paused
  paused = 1


# hash = 0x87800ce2
# getter = None
# const = None
# payable = False
def MD5FromMarketingKeywords(string _keyWords): # not payable
  mem[128 len _keyWords.length] = _keyWords[all]
  mem[ceil32(_keyWords.length) + 160 len floor32(_keyWords.length)] = call.data[_keyWords + 36 len floor32(_keyWords.length)]
  mem[ceil32(_keyWords.length) + floor32(_keyWords.length) + -(_keyWords.length % 32) + 192 len _keyWords.length % 32] = mem[floor32(_keyWords.length) + -(_keyWords.length % 32) + 160 len _keyWords.length % 32]
  mem[_keyWords.length + ceil32(_keyWords.length) + 160 len floor32(_keyWords.length)] = call.data[_keyWords + 36 len floor32(_keyWords.length)]
  mem[_keyWords.length + ceil32(_keyWords.length) + floor32(_keyWords.length) + 160] = 256^(-(_keyWords.length % 32) + 32) - 1 and mem[_keyWords.length + ceil32(_keyWords.length) + floor32(_keyWords.length) + 160] or mem[ceil32(_keyWords.length) + floor32(_keyWords.length) + 160] and !(256^(-(_keyWords.length % 32) + 32) - 1)
  mem[_keyWords.length + ceil32(_keyWords.length) + 160] = stor13[call.data[_keyWords + 36 len floor32(_keyWords.length)]][mem[_keyWords.length + ceil32(_keyWords.length) + floor32(_keyWords.length) + 160 len _keyWords.length % 32]]
  return memory
    from _keyWords.length + ceil32(_keyWords.length) + 160
     [93mlen 32


# hash = 0x91876e57
# getter = None
# const = None
# payable = False
def withdrawAuctionBalances(): # not payable
  require caller == cooAddress
  require ext_code.size(saleClockAuctionContractAddress)
  call saleClockAuctionContractAddress.withdrawBalance() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x95d89b41
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 18]]]], ['loc', 18]]]
# const = None
# payable = False
def symbol(): # not payable
  return symbol[0 len symbol.length]


# hash = 0x9ca3669d
# getter = None
# const = None
# payable = False
def cancelCommissionerAuction(uint32 _tokenId): # not payable
  require caller == commissionerAddress
  require saleClockAuctionContractAddress
  require ext_code.size(saleClockAuctionContractAddress)
  call saleClockAuctionContractAddress.cancelAuction(uint256 tokenId) with:
       gas gas_remaining wei
      args _tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xa22cb465
# getter = None
# const = None
# payable = False
def setApprovalForAll(address _to, bool _approved): # not payable
  require _to != caller
  stor11[caller][addr(_to)] = uint8(_approved)
  log ApprovalForAll(
        address owner=_approved,
        address operator=caller,
        bool approved=_to)


# hash = 0xa9741394
# getter = ['storage', 256, 0, 1]
# const = None
# payable = False
def COMMISSIONER_AUCTION_FLOOR_PRICE(): # not payable
  return uint256(COMMISSIONER_AUCTION_FLOOR_PRICE)


# hash = 0xaba23628
# getter = None
# const = None
# payable = False
def mintPlayers(uint128[] _md5Tokens, uint256 _startPrice, uint256 _endPrice, uint256 _duration): # not payable
  mem[96] = _md5Tokens.length
  mem[128 len 32 * _md5Tokens.length] = call.data[_md5Tokens + 36 len 32 * _md5Tokens.length]
  mem[64] = (32 * _md5Tokens.length) + 352
  mem[(32 * _md5Tokens.length) + 128] = 0
  mem[(32 * _md5Tokens.length) + 160] = 0
  mem[(32 * _md5Tokens.length) + 192] = 0
  mem[(32 * _md5Tokens.length) + 224] = 0
  mem[(32 * _md5Tokens.length) + 256] = 0
  mem[(32 * _md5Tokens.length) + 288] = 0
  mem[(32 * _md5Tokens.length) + 320] = 96
  require leagueRosterContractAddress
  require saleClockAuctionContractAddress
  if caller == commissionerAddress:
      [94ms = 0
      [94ms = 0
      [94midx = 0
      while uint32([94midx) < _md5Tokens.length:
          require uint32([94midx) < mem[96]
          [94m_493 = mem[(32 * uint32([94midx)) + 128]
          mem[mem[64] + 4] = mem[(32 * uint32([94midx)) + 144 len 16]
          require ext_code.size(leagueRosterContractAddress)
          call leagueRosterContractAddress.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
               gas gas_remaining wei
              args ([94m_493 << 128)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if uint128(ext_call.return_data[0]) != 0xffffffffffffffffffffffffffffffff:
              require ext_code.size(leagueRosterContractAddress)
              call leagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
                   gas gas_remaining wei
                  args (ext_call.return_data[0] << 128)
              mem[mem[64] len 192] = ext_call.return_data[0 len 192]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 192
              mem[(32 * _md5Tokens.length) + 288] = bool(ext_call.return_data[160])
              mem[(32 * _md5Tokens.length) + 256] = bool(ext_call.return_data[128])
              mem[(32 * _md5Tokens.length) + 224] = uint32(ext_call.return_data[96])
              mem[(32 * _md5Tokens.length) + 192] = uint64(ext_call.return_data[64])
              mem[(32 * _md5Tokens.length) + 160] = uint128(ext_call.return_data[32])
              mem[(32 * _md5Tokens.length) + 128] = uint128(ext_call.return_data[0])
              if uint128([94m_493) == uint128(ext_call.return_data[0]):
                  if ext_call.return_data[160]:
                      if not ext_call.return_data[128]:
                          if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) <= 0xffffffffffffffffffffffffffffffff:
                              if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
                                  if _startPrice >= uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)):
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
                              else:
                                  if _startPrice >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
                          else:
                              if 0xffffffffffffffffffffffffffffffff >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
                                  if _startPrice >= 0xffffffffffffffffffffffffffffffff:
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), 0xffffffffffffffffffffffffffffffff, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), 0xffffffffffffffffffffffffffffffff, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
                              else:
                                  if _startPrice >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[mem[64]] = 'T6qy'
                          mem[mem[64] + 4] = uint32(ext_call.return_data[0])
                          mem[mem[64] + 36] = uint128(ext_call.return_data[32])
                          mem[mem[64] + 68] = uint64(block.timestamp)
                          mem[mem[64] + 100] = uint32(uint32(ext_call.return_data[96]) + 1)
                          mem[mem[64] + 132] = 1
                          mem[mem[64] + 164] = bool(ext_call.return_data[160])
                          require ext_code.size(leagueRosterContractAddress)
                          call leagueRosterContractAddress.'T6qy' with:
                               gas gas_remaining wei
                              args ext_call.return_data[0] << 224, ext_call.return_data[32] << 128, block.timestamp << 192, uint32(ext_call.return_data[96]) + 1 << 224, 1, bool(ext_call.return_data[160])
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
          [94ms = ext_call.return_data[0]
          [94ms = [94m_493
          [94midx = [94midx + 1
          continue 
  else:
      require caller == leagueRosterContractAddress
      [94ms = 0
      [94ms = 0
      [94midx = 0
      while uint32([94midx) < _md5Tokens.length:
          require uint32([94midx) < mem[96]
          [94m_496 = mem[(32 * uint32([94midx)) + 128]
          mem[mem[64] + 4] = mem[(32 * uint32([94midx)) + 144 len 16]
          require ext_code.size(leagueRosterContractAddress)
          call leagueRosterContractAddress.getRealWorldPlayerRosterIndex(uint128 md5Token) with:
               gas gas_remaining wei
              args ([94m_496 << 128)
          mem[mem[64]] = ext_call.return_data[0]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if uint128(ext_call.return_data[0]) != 0xffffffffffffffffffffffffffffffff:
              require ext_code.size(leagueRosterContractAddress)
              call leagueRosterContractAddress.realWorldPlayerFromIndex(uint128 idx) with:
                   gas gas_remaining wei
                  args (ext_call.return_data[0] << 128)
              mem[mem[64] len 192] = ext_call.return_data[0 len 192]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 192
              mem[(32 * _md5Tokens.length) + 288] = bool(ext_call.return_data[160])
              mem[(32 * _md5Tokens.length) + 256] = bool(ext_call.return_data[128])
              mem[(32 * _md5Tokens.length) + 224] = uint32(ext_call.return_data[96])
              mem[(32 * _md5Tokens.length) + 192] = uint64(ext_call.return_data[64])
              mem[(32 * _md5Tokens.length) + 160] = uint128(ext_call.return_data[32])
              mem[(32 * _md5Tokens.length) + 128] = uint128(ext_call.return_data[0])
              if uint128([94m_496) == uint128(ext_call.return_data[0]):
                  if ext_call.return_data[160]:
                      if not ext_call.return_data[128]:
                          if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) <= 0xffffffffffffffffffffffffffffffff:
                              if uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)) >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
                                  if _startPrice >= uint128(uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4)):
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint128(ext_call.return_data[32]) + (uint128(ext_call.return_data[32]) / 4) << 128, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
                              else:
                                  if _startPrice >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
                          else:
                              if 0xffffffffffffffffffffffffffffffff >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
                                  if _startPrice >= 0xffffffffffffffffffffffffffffffff:
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), 0xffffffffffffffffffffffffffffffff, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), 0xffffffffffffffffffffffffffffffff, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
                              else:
                                  if _startPrice >= uint256(COMMISSIONER_AUCTION_FLOOR_PRICE):
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), _startPrice, _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
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
                                      playerToken.length++
                                      uint32(playerToken[playerToken.length].field_0) = uint32(ext_call.return_data[0])
                                      uint32(playerToken[playerToken.length].field_32) = uint32(ext_call.return_data[96])
                                      uint64(playerToken[playerToken.length].field_64) = uint64(block.timestamp)
                                      uint128(playerToken[playerToken.length].field_128) = 0
                                      playerToken[playerToken.length].field_256 % 1 = 0
                                      require playerToken.length < 4294967295
                                      playerTokenToOwner[stor16.length] = this.address
                                      balanceOf[addr(this.address)].field_0++
                                      balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 = balanceOf[addr(this.address)][Mask(253, 0, balanceOf[addr(this.address)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(this.address)].field_0 % 8)) or 256^(4 * balanceOf[addr(this.address)].field_0 % 8) * uint32(playerToken.length)
                                      uint32(stor10[uint32(stor16.length)].field_0) = uint32(balanceOf[addr(this.address)].field_0)
                                      log Transfer(
                                            address from=0,
                                            address to=this.address,
                                            uint256 value=playerToken.length)
                                      mem[0] = uint32(playerToken.length)
                                      mem[32] = 8
                                      playerTokenToApproved[uint32(stor16.length)] = saleClockAuctionContractAddress
                                      require ext_code.size(saleClockAuctionContractAddress)
                                      if _duration:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endPrice, _duration, this.address
                                      else:
                                          call saleClockAuctionContractAddress.createAuction(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration, address seller) with:
                                               gas gas_remaining wei
                                              args uint32(playerToken.length), uint256(COMMISSIONER_AUCTION_FLOOR_PRICE), _endPrice, COMMISSIONER_AUCTION_DURATION, this.address
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          mem[mem[64]] = 'T6qy'
                          mem[mem[64] + 4] = uint32(ext_call.return_data[0])
                          mem[mem[64] + 36] = uint128(ext_call.return_data[32])
                          mem[mem[64] + 68] = uint64(block.timestamp)
                          mem[mem[64] + 100] = uint32(uint32(ext_call.return_data[96]) + 1)
                          mem[mem[64] + 132] = 1
                          mem[mem[64] + 164] = bool(ext_call.return_data[160])
                          require ext_code.size(leagueRosterContractAddress)
                          call leagueRosterContractAddress.'T6qy' with:
                               gas gas_remaining wei
                              args ext_call.return_data[0] << 224, ext_call.return_data[32] << 128, block.timestamp << 192, uint32(ext_call.return_data[96]) + 1 << 224, 1, bool(ext_call.return_data[160])
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
          [94ms = ext_call.return_data[0]
          [94ms = [94m_496
          [94midx = [94midx + 1
          continue 


# hash = 0xb047fb50
# getter = ['storage', 160, 0, 5]
# const = None
# payable = False
def cooAddress(): # not payable
  return cooAddress


# hash = 0xb352c562
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def leagueRosterContract(): # not payable
  return leagueRosterContractAddress


# hash = 0xb42d3b40
# getter = None
# const = None
# payable = False
def setTeamContractAddress(address _address): # not payable
  require caller == ceoAddress
  require ext_code.size(_address)
  call _address.isTeamContract() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  teamContractAddress = _address


# hash = 0xb5d7d3d8
# getter = ['storage', 160, 0, 15]
# const = None
# payable = False
def teamContract(): # not payable
  return teamContractAddress


# hash = 0xb88d4fde
# getter = None
# const = None
# payable = True
def safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes _data) payable: 
  require not paused
  require _to
  require playerToken.length > _tokenId
  require playerTokenToApproved[_tokenId] == _to
  require playerTokenToOwner[_tokenId] == _from
  if playerTokenToOwner[_tokenId] != caller:
      if playerTokenToApproved[_tokenId] != caller:
          require stor11[addr(_from)][caller]
  playerTokenToOwner[_tokenId] = _to
  if _from:
      require balanceOf[addr(_from)].field_0 - 1 < balanceOf[addr(_from)].field_0
      require uint32(stor10[_tokenId << 224].field_0) < balanceOf[addr(_from)].field_0
      balanceOf[addr(_from)][stor10[_tokenId << 224].field_3 % 536870912].field_0 = stor('array', ('div', 0.125, ('add', -1, ('stor', 256, 0, ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9))))), ('map', ('mask_shl', 160, 0, 96, ('param', '_from')), ('name', 'stor9', 9)))[uint8(stor9[addr(_from)].field_0 - 1)] * 256^(4 * stor10[_tokenId << 224].field_0 % 8) or !(4294967295 * 256^(4 * stor10[_tokenId << 224].field_0 % 8)) and balanceOf[addr(_from)][stor10[_tokenId << 224].field_3 % 536870912].field_0
      balanceOf[addr(_from)].field_0--
      if balanceOf[addr(_from)].field_0 > balanceOf[addr(_from)].field_0 - 1:
          [94midx = balanceOf[addr(_from)].field_0 + 6 / 8
          while balanceOf[addr(_from)].field_0 + 7 / 8 > [94midx:
              balanceOf[addr(_from)][[94midx].field_0 = 0
              [94midx = [94midx + 1
              continue 
      uint32(stor10[uint32(stor9[addr(_from)][0.125 / stor9[addr(_from)].field_0 - 1].field_(32 * stor9[addr(_from)].field_0 - 1 % 8) - 224)].field_0) = uint32(stor10[_tokenId << 224].field_0)
      uint32(stor10[uint32(_tokenId)].field_0) = 0
      playerTokenToApproved[_tokenId] = 0
  balanceOf[addr(_to)].field_0++
  balanceOf[addr(_to)][Mask(253, 0, balanceOf[addr(_to)].field_3)].field_0 = balanceOf[addr(_to)][Mask(253, 0, balanceOf[addr(_to)].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[addr(_to)].field_0 % 8)) or 256^(4 * balanceOf[addr(_to)].field_0 % 8) * uint32(_tokenId)
  uint32(stor10[_tokenId << 224].field_0) = uint32(balanceOf[addr(_to)].field_0)
  log Transfer(
        address from=_from,
        address to=_to,
        uint256 value=_tokenId)
  if ext_code.size(_to) > 0:
      require ext_code.size(_to)
      call _to.onERC721Received(address param1, address param2, uint256 param3, bytes param4) with:
           gas 50000 wei
          args 0, uint32(caller), addr(_from), _tokenId, 128, _data.length, _data[all]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require Mask(32, 224, sha3('onERC721Received(address,uint256', ',bytes)')) == Mask(32, 224, ext_call.return_data[0])


# hash = 0xb9931d30
# getter = ['struct', ['loc', 16]]
# const = None
# payable = False
def getPlayerToken(uint32 _playerTokenID): # not payable
  require _playerTokenID < playerToken.length
  return uint32(playerToken[_playerTokenID].field_0), 
         uint32(playerToken[_playerTokenID].field_0),
         uint64(playerToken[_playerTokenID].field_0),
         uint128(playerToken[_playerTokenID].field_128)


# hash = 0xc5013863
# getter = ['storage', 160, 0, 20]
# const = None
# payable = False
def saleClockAuctionContract(): # not payable
  return saleClockAuctionContractAddress


# hash = 0xce88a9ce
# getter = None
# const = None
# payable = False
def setProduction(): # not payable
  require caller == ceoAddress
  require 1 == bool(isDevelopment)
  isDevelopment = 0


# hash = 0xd5bcecab
# getter = None
# const = None
# payable = False
def setLeagueRosterAndSaleAndTeamContractAddress(address _leagueAddress, address _saleAddress, address _teamAddress): # not payable
  require caller == ceoAddress
  if not isDevelopment:
      require not leagueRosterContractAddress
  require ext_code.size(_leagueAddress)
  call _leagueAddress.isLeagueRosterContract() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  leagueRosterContractAddress = _leagueAddress
  require caller == ceoAddress
  require _saleAddress
  require ext_code.size(_saleAddress)
  call _saleAddress.isSaleClockAuction() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  saleClockAuctionContractAddress = _saleAddress
  require caller == ceoAddress
  require ext_code.size(_teamAddress)
  call _teamAddress.isTeamContract() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  teamContractAddress = _teamAddress


# hash = 0xe149f036
# getter = ['storage', 32, ['mask_shl', 3, 0, 5, ['cd', 36]], ['add', ['mask_shl', 253, 3, -3, ['cd', 36]], ['sha3', ['sha3', ['data', ['cd', 4], 9]]]]]
# const = None
# payable = False
def ownedTokens(address _param1, uint256 _param2): # not payable
  require _param2 < balanceOf[_param1].field_0
  return ownedTokens[uint8(_param2)]


# hash = 0xe3a531a3
# getter = None
# const = None
# payable = False
def setSaleAuctionContractAddress(address _address): # not payable
  require caller == ceoAddress
  require _address
  require ext_code.size(_address)
  call _address.isSaleClockAuction() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  saleClockAuctionContractAddress = _address


# hash = 0xea8037d6
# getter = None
# const = None
# payable = False
def batchEscrowToTeamContract(address _owner, uint32[] _tokenIds): # not payable
  mem[128 len 32 * _tokenIds.length] = call.data[_tokenIds + 36 len 32 * _tokenIds.length]
  require not paused
  require teamContractAddress
  require caller == teamContractAddress
  [94ms = 0
  [94midx = 0
  while uint32([94midx) < _tokenIds.length:
      require uint32([94midx) < _tokenIds.length
      require playerTokenToOwner[mem[(32 * uint32([94midx)) + 156 len 4]] == _owner
      playerTokenToOwner[mem[(32 * uint32([94midx)) + 128] << 224] = teamContractAddress
      if _owner:
          require balanceOf[addr(_owner)].field_0 - 1 < balanceOf[addr(_owner)].field_0
          require uint32(stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_0) < balanceOf[addr(_owner)].field_0
          balanceOf[addr(_owner)][stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_3 % 536870912].field_0 = stor('array', ('div', 0.125, ('add', -1, ('stor', 256, 0, ('map', ('mask_shl', 160, 0, 96, ('param', '_owner')), ('name', 'stor9', 9))))), ('map', ('mask_shl', 160, 0, 96, ('param', '_owner')), ('name', 'stor9', 9)))[uint8(stor9[addr(_owner)].field_0 - 1)] * 256^(4 * stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_0 % 8) or !(4294967295 * 256^(4 * stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_0 % 8)) and balanceOf[addr(_owner)][stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_3 % 536870912].field_0
          balanceOf[addr(_owner)].field_0--
          if balanceOf[addr(_owner)].field_0 > balanceOf[addr(_owner)].field_0 - 1:
              [94ms = (balanceOf[addr(_owner)].field_0 + 6 / 8) + sha3(sha3(addr(_owner), 9))
              while sha3(sha3(addr(_owner), 9)) + (balanceOf[addr(_owner)].field_0 + 7 / 8) > [94ms:
                  stor[[94ms] = 0
                  [94ms = [94ms + 1
                  continue 
          uint32(stor10[uint32(stor9[addr(_owner)][0.125 / stor9[addr(_owner)].field_0 - 1].field_(32 * stor9[addr(_owner)].field_0 - 1 % 8) - 224)].field_0) = uint32(stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_0)
          uint32(stor10[mem[(32 * uint32([94midx)) + 156 len 4]].field_0) = 0
          playerTokenToApproved[mem[(32 * uint32([94midx)) + 128] << 224] = 0
      balanceOf[stor15].field_0++
      balanceOf[stor15][Mask(253, 0, balanceOf[stor15].field_3)].field_0 = balanceOf[stor15][Mask(253, 0, balanceOf[stor15].field_3)].field_0 and !(4294967295 * 256^(4 * balanceOf[stor15].field_0 % 8)) or 256^(4 * balanceOf[stor15].field_0 % 8) * mem[(32 * uint32([94midx)) + 156 len 4]
      mem[0] = mem[(32 * uint32([94midx)) + 156 len 4]
      mem[32] = 10
      uint32(stor10[mem[(32 * uint32([94midx)) + 128] << 224].field_0) = uint32(balanceOf[stor15].field_0)
      log Transfer(
            address from=_owner,
            address to=teamContractAddress,
            uint256 value=mem[(32 * uint32(idx)) + 156 len 4])
      [94ms = mem[(32 * uint32([94midx)) + 128]
      [94midx = [94midx + 1
      continue 


# hash = 0xeaf4170c
# getter = None
# const = ['return', 1]
# payable = False
const implementsSaleClockAuctionListener = 1


# hash = 0xeb2c0223
# getter = None
# const = None
# payable = False
def upgradeContract(address _newContract): # not payable
  require caller == ceoAddress
  require paused
  newContractAddress = _newContract
  log ContractUpgrade(address newContract=_newContract)


# hash = 0xf418b153
# getter = None
# const = None
# payable = False
def replaceMarketingToken(uint256 _oldKeywordHash, uint256 _newKeywordHash, uint128 _md5Token): # not payable
  require caller == commissionerAddress
  if stor13[_oldKeywordHash]:
      stor13[_oldKeywordHash] = 0
      stor13[_newKeywordHash] = _md5Token
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


