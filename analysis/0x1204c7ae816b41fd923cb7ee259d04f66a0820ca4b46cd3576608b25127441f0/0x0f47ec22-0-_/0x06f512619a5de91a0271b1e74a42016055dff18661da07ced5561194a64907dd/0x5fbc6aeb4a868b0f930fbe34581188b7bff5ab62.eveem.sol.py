# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x5FBC6Aeb4a868B0f930fbe34581188b7bFF5aB62 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    ceoAddress # mask: a s
    # storage address 1
    cooAddress # mask: a s
    # storage address 2
    unknowna1045d73Address # mask: a s
    # storage address 2
    paused # mask: a s
    # storage address 3
    cooldowns
    # storage address 5
    secondsPerBlock # mask: a s
    # storage address 6
    unknownc754a0a3
    # storage address 7
    unknown6e037679
    # storage address 8
    balanceOf
    # storage address 9
    unknown5de973a5
    # storage address 10
    sireAllowedTo
    # storage address 11
    saleAuctionAddress # mask: a s
    # storage address 12
    siringAuctionAddress # mask: a s
    # storage address 13
    unknowne86d5083Address # mask: a s
    # storage address 14
    tokenContractAddress # mask: a s
    # storage address 15
    tokenBalanceOf
    # storage address 16
    autoBirthFee # mask: a s
    # storage address 17
    unknownb9b8ea8e # mask: a s
    # storage address 18
    geneScienceAddress # mask: a s
    # storage address 19
    promoCreatedCount # mask: a s
    # storage address 20
    gen0CreatedCount # mask: a s
    # storage address 111414077815863400510004064629973595961579173665589224203503662149373724986688
    stor111414077815863400510004064629973595961579173665589224203503662149373724986688
# hash = 0x01ffc9a7
# getter = None
# const = None
# payable = False
def supportsInterface(bytes4 m_interfaceId): # not payable
  if Mask(32, 224, sha3('supportsInterface(bytes4)')) == Mask(32, 224, m_interfaceId):
      return True
  return (Mask(32, 224, sha3('totalSupply()') xor sha3('symbol()') xor sha3('name()') xor sha3('balanceOf(address)') xor sha3('ownerOf(uint256)') xor sha3('approve(address,uint256)') xor sha3('transfer(address,uint256)') xor sha3('transferFrom(address,address,uin', 't256)') xor sha3('tokensOfOwner(address)') xor sha3('tokenMetadata(uint256,string)')) == Mask(32, 224, m_interfaceId))


# hash = 0x05e45546
# getter = ['storage', 256, 0, 19]
# const = None
# payable = False
def promoCreatedCount(): # not payable
  return mpromoCreatedCount


# hash = 0x06fdde03
# getter = None
# const = ['return', ['data', ['arr', 11, ['mask_shl', 88, 0, 0, "'CryptoFoxes'"]]]]
# payable = False
const name = 'CryptoFoxes'


# hash = 0x095ea7b3
# getter = None
# const = None
# payable = False
def approve(address m_spender, uint256 m_value): # not payable
  require not mpaused
  require munknown6e037679m[m_valuem] == caller
  munknown5de973a5m[m_valuem] = m_spender
  log Approval(
        address owner=caller,
        address spender=addr(_spender),
        uint256 value=_value)


# hash = 0x0a0f8168
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def ceoAddress(): # not payable
  return mceoAddress


# hash = 0x0e583df0
# getter = None
# const = ['return', 100]
# payable = False
const GEN0_STARTING_PRICE = 100


# hash = 0x0f47ec22
# getter = None
# const = None
# payable = False
def unknown0f47ec22(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  require not mpaused
  require munknown6e037679m[m_param2m] == caller
  require m_param2 > 0
  require m_param2 < munknownc754a0a3m.length
  require 0 == munknownc754a0a3m[m_param2m]m.field_448
  require munknownc754a0a3m[m_param2m]m.field_320 <= uint64(block.number)
  require m_param2 < munknownc754a0a3m.length
  require m_param1 < munknownc754a0a3m.length
  require m_param2 != m_param1
  require m_param1 != munknownc754a0a3m[m_param2m]m.field_384
  require m_param1 != munknownc754a0a3m[m_param2m]m.field_416
  require m_param2 != munknownc754a0a3m[m_param1m]m.field_384
  require m_param2 != munknownc754a0a3m[m_param1m]m.field_416
  if munknownc754a0a3m[m_param1m]m.field_384:
      if munknownc754a0a3m[m_param2m]m.field_384:
          require munknownc754a0a3m[m_param1m]m.field_384 != munknownc754a0a3m[m_param2m]m.field_384
          require munknownc754a0a3m[m_param2m]m.field_416 != munknownc754a0a3m[m_param1m]m.field_384
          require munknownc754a0a3m[m_param2m]m.field_384 != munknownc754a0a3m[m_param1m]m.field_416
          require munknownc754a0a3m[m_param1m]m.field_416 != munknownc754a0a3m[m_param2m]m.field_416
  require ext_code.size(msiringAuctionAddress)
  call msiringAuctionAddress.getCurrentPrice(uint256 tokenId) with:
       gas gas_remaining wei
      args m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0] < ext_call.return_data[0] + mautoBirthFee
  require m_param3 >= ext_call.return_data[0] + mautoBirthFee
  require ext_code.size(msiringAuctionAddress)
  call msiringAuctionAddress.bid(uint256 amount, uint256 auctionId) with:
       gas gas_remaining wei
      args m_param1, m_param3 - mautoBirthFee
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require not mpaused
  if mautoBirthFee:
      if caller != caller:
          if msaleAuctionAddress != caller:
              if msiringAuctionAddress != caller:
                  require caller == munknowne86d5083Address
      require this.address
      require mautoBirthFee <= mtokenBalanceOfm[callerm]
      require mtokenBalanceOfm[addr(this.address)m] + mautoBirthFee > mtokenBalanceOfm[addr(this.address)m]
      mtokenBalanceOfm[callerm] -= mautoBirthFee
      mtokenBalanceOfm[addr(this.address)m] += mautoBirthFee
      require mtokenBalanceOfm[addr(this.address)m] + mtokenBalanceOfm[callerm] == mtokenBalanceOfm[callerm] + mautoBirthFee + mtokenBalanceOfm[addr(this.address)m]
      log TransferToken(
            address from=caller,
            address to=addr(this.address),
            uint256 tokenId=autoBirthFee)
  require uint32(m_param1) < munknownc754a0a3m.length
  require uint32(m_param2) < munknownc754a0a3m.length
  munknownc754a0a3m[2 * uint32(m_param2)m]m.field_448 = uint32(m_param1)
  require munknownc754a0a3m[2 * uint32(m_param1)m]m.field_480 < 14
  require msecondsPerBlock
  munknownc754a0a3m[2 * uint32(m_param1)m]m.field_320 = uint64((mcooldownsm[mstor6m[2 * uint32(m_param1)m]m.field_480m] / msecondsPerBlock) + block.number)
  if munknownc754a0a3m[2 * uint32(m_param1)m]m.field_480 < 13:
      munknownc754a0a3m[2 * uint32(m_param1)m]m.field_480 = uint16(munknownc754a0a3m[2 * uint32(m_param1)m]m.field_480 + 1)
  require munknownc754a0a3m[2 * uint32(m_param2)m]m.field_480 < 14
  require msecondsPerBlock
  munknownc754a0a3m[2 * uint32(m_param2)m]m.field_320 = uint64((mcooldownsm[mstor6m[2 * uint32(m_param2)m]m.field_480m] / msecondsPerBlock) + block.number)
  if munknownc754a0a3m[2 * uint32(m_param2)m]m.field_480 < 13:
      munknownc754a0a3m[2 * uint32(m_param2)m]m.field_480 = uint16(munknownc754a0a3m[2 * uint32(m_param2)m]m.field_480 + 1)
  msireAllowedTom[m_param2 << 224m] = 0
  msireAllowedTom[uint32(m_param1)m] = 0
  munknownb9b8ea8e++
  log Pregnant(
        address owner=unknown6e037679[_param2 << 224],
        uint256 mareId=_param2 << 224,
        uint256 stallionId=_param1 << 224,
        uint256 unproductiveEndBlock=unknownc754a0a3[2 * uint32(_param2)].field_320)


# hash = 0x14001f4c
# getter = None
# const = None
# payable = False
def setSiringAuctionAddress(address m_address): # not payable
  require caller == mceoAddress
  require ext_code.size(m_address)
  call m_address.isSiringClockAuction() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  msiringAuctionAddress = m_address


# hash = 0x18160ddd
# getter = None
# const = None
# payable = False
def totalSupply(): # not payable
  return (munknownc754a0a3m.length - 1)


# hash = 0x1940a936
# getter = ['bool', ['storage', 32, 192, ['add', 1, ['mask_shl', 255, 0, 1, ['cd', 4]], ['sha3', 6]]]]
# const = None
# payable = False
def isPregnant(uint256 m_horseId): # not payable
  require m_horseId > 0
  require m_horseId < munknownc754a0a3m.length
  return bool(munknownc754a0a3m[m_horseIdm]m.field_448)


# hash = 0x19c2f201
# getter = None
# const = ['return', 864000]
# payable = False
const GEN0_AUCTION_DURATION = (240 * 24 * 3600)


# hash = 0x1a266a69
# getter = None
# const = None
# payable = False
def unknown1a266a69(addr m_param1): # not payable
  require caller == mceoAddress
  require m_param1
  munknowna1045d73Address = m_param1


# hash = 0x21717ebf
# getter = ['storage', 160, 0, 12]
# const = None
# payable = False
def siringAuction(): # not payable
  return msiringAuctionAddress


# hash = 0x23b872dd
# getter = None
# const = None
# payable = False
def transferFrom(address m_from, address m_to, uint256 m_value): # not payable
  require not mpaused
  require m_to
  require m_to != this.address
  require munknown5de973a5m[m_valuem] == caller
  require munknown6e037679m[m_valuem] == m_from
  mbalanceOfm[addr(m_to)m]++
  munknown6e037679m[m_valuem] = m_to
  if m_from:
      mbalanceOfm[addr(m_from)m]--
      msireAllowedTom[m_valuem] = 0
      munknown5de973a5m[m_valuem] = 0
  log Transfer(
        address from=addr(_from),
        address to=addr(_to),
        uint256 value=_value)


# hash = 0x23e505d7
# getter = None
# const = None
# payable = True
def unknown23e505d7(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4) payable: 
  require not mpaused
  require call.value >= m_param2 / 100
  require munknown6e037679m[m_param1m] == caller
  require m_param1 > 0
  require m_param1 < munknownc754a0a3m.length
  require not munknownc754a0a3m[m_param1m]m.field_448
  call mceoAddress with:
     value call.value wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  munknown5de973a5m[m_param1m] = msaleAuctionAddress
  require ext_code.size(msaleAuctionAddress)
  call msaleAuctionAddress.0xa912873 with:
       gas gas_remaining wei
      args 0, uint32(m_param1), m_param2, m_param3, m_param4, caller, 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x24e7a38a
# getter = None
# const = None
# payable = False
def setGeneScienceAddress(address m_address): # not payable
  require caller == mceoAddress
  require ext_code.size(m_address)
  call m_address.isGeneScience() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mgeneScienceAddress = m_address


# hash = 0x26a4e8d2
# getter = None
# const = None
# payable = False
def setTokenAddress(address m_tokenAddress): # not payable
  require caller == mceoAddress
  require ext_code.size(m_tokenAddress)
  call m_tokenAddress.supportsInterface(bytes4 interfaceId) with:
       gas gas_remaining wei
      args 0xa5126e4500000000000000000000000000000000000000000000000000000000
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mtokenContractAddress = m_tokenAddress


# hash = 0x278ecde1
# getter = None
# const = None
# payable = False
def refund(uint256 m_requestId): # not payable
  require m_requestId <= mtokenBalanceOfm[callerm]
  require ext_code.size(mtokenContractAddress)
  call mtokenContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, m_requestId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mtokenBalanceOfm[callerm] -= m_requestId


# hash = 0x2a0ef02e
# getter = None
# const = None
# payable = False
def unknown2a0ef02e(addr m_param1): # not payable
  require caller == mceoAddress
  require ext_code.size(m_param1)
  call m_param1.0xc7b83519 with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  munknowne86d5083Address = m_param1


# hash = 0x2ba73c15
# getter = None
# const = None
# payable = False
def setCOO(address m_newCOO): # not payable
  require caller == mceoAddress
  require m_newCOO
  mcooAddress = m_newCOO


# hash = 0x2bbfd941
# getter = None
# const = None
# payable = False
def unknown2bbfd941(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4): # not payable
  require not mpaused
  require munknown6e037679m[m_param1m] == caller
  require m_param1 > 0
  require m_param1 < munknownc754a0a3m.length
  require not munknownc754a0a3m[m_param1m]m.field_448
  munknown5de973a5m[m_param1m] = munknowne86d5083Address
  require ext_code.size(munknowne86d5083Address)
  call munknowne86d5083Address.0xa912873 with:
       gas gas_remaining wei
      args 0, uint32(m_param1), m_param2, m_param3, m_param4, caller, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x3d7d3f5a
# getter = None
# const = None
# payable = False
def createSaleAuction(uint256 m_artworkId, uint256 m_startingPrice, uint256 m_endingPrice, uint256 m_duration): # not payable
  require not mpaused
  require munknown6e037679m[m_artworkIdm] == caller
  require m_artworkId > 0
  require m_artworkId < munknownc754a0a3m.length
  require not munknownc754a0a3m[m_artworkIdm]m.field_448
  munknown5de973a5m[m_artworkIdm] = msaleAuctionAddress
  require ext_code.size(msaleAuctionAddress)
  call msaleAuctionAddress.0xa912873 with:
       gas gas_remaining wei
      args 0, uint32(m_artworkId), m_startingPrice, m_endingPrice, m_duration, caller, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == mceoAddress
  require mpaused
  require msaleAuctionAddress
  require msiringAuctionAddress
  require munknowne86d5083Address
  require mtokenContractAddress
  require mgeneScienceAddress
  require caller == mceoAddress
  require mpaused
  mpaused = 0


# hash = 0x46116e6f
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 10]]]
# const = None
# payable = False
def sireAllowedToAddress(uint256 m_param1): # not payable
  return msireAllowedTom[m_param1m]


# hash = 0x46d22c70
# getter = None
# const = None
# payable = False
def canBreedWith(uint256 m_matronId, uint256 m_sireId): # not payable
  require m_matronId > 0
  require m_sireId > 0
  require m_matronId < munknownc754a0a3m.length
  require m_sireId < munknownc754a0a3m.length
  if m_matronId == m_sireId:
      return 0
  if m_sireId == munknownc754a0a3m[m_matronIdm]m.field_384:
      return 0
  if m_sireId == munknownc754a0a3m[m_matronIdm]m.field_416:
      return 0
  if m_matronId == munknownc754a0a3m[m_sireIdm]m.field_384:
      return 0
  if m_matronId == munknownc754a0a3m[m_sireIdm]m.field_416:
      return 0
  if munknownc754a0a3m[m_sireIdm]m.field_384:
      if munknownc754a0a3m[m_matronIdm]m.field_384:
          if munknownc754a0a3m[m_sireIdm]m.field_384 == munknownc754a0a3m[m_matronIdm]m.field_384:
              return 0
          if munknownc754a0a3m[m_matronIdm]m.field_416 == munknownc754a0a3m[m_sireIdm]m.field_384:
              return 0
          if munknownc754a0a3m[m_matronIdm]m.field_384 == munknownc754a0a3m[m_sireIdm]m.field_416:
              return 0
          if munknownc754a0a3m[m_sireIdm]m.field_416 == munknownc754a0a3m[m_matronIdm]m.field_416:
              return 0
  if munknown6e037679m[m_matronIdm] == munknown6e037679m[m_sireIdm]:
      return True
  return (munknown6e037679m[m_matronIdm] == msireAllowedTom[m_sireIdm])


# hash = 0x4ad8c938
# getter = None
# const = None
# payable = False
def createSiringAuction(uint256 m_tokenId, uint256 m_startingPrice, uint256 m_endingPrice, uint256 m_duration): # not payable
  require not mpaused
  require munknown6e037679m[m_tokenIdm] == caller
  require m_tokenId > 0
  require m_tokenId < munknownc754a0a3m.length
  require 0 == munknownc754a0a3m[m_tokenIdm]m.field_448
  require munknownc754a0a3m[m_tokenIdm]m.field_320 <= uint64(block.number)
  munknown5de973a5m[m_tokenIdm] = msiringAuctionAddress
  require ext_code.size(msiringAuctionAddress)
  call msiringAuctionAddress.0xa912873 with:
       gas gas_remaining wei
      args m_tokenId, m_startingPrice, m_endingPrice, m_duration, caller, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x4b136782
# getter = None
# const = None
# payable = False
def unknown4b136782(uint256 m_param1, uint256 m_param2, uint256 m_param3, uint256 m_param4, addr m_param5): # not payable
  require caller == munknowna1045d73Address
  require 50000 > mpromoCreatedCount
  mpromoCreatedCount++
  require m_param1 == uint32(m_param1)
  require m_param2 == uint32(m_param2)
  require m_param3 == uint16(m_param3)
  munknownc754a0a3m.length++
  munknownc754a0a3m[munknownc754a0a3m.lengthm]m.field_0 = m_param4
  mstorF652m[mstor6m.lengthm]m.field_0 = uint64(block.timestamp)
  mstorF652m[mstor6m.lengthm]m.field_64 = 0
  mstorF652m[mstor6m.lengthm]m.field_128 = uint32(m_param1)
  mstorF652m[mstor6m.lengthm]m.field_160 = uint32(m_param2)
  mstorF652m[mstor6m.lengthm]m.field_192 = 0
  if uint16(m_param3) <= 13:
      mstorF652m[mstor6m.lengthm]m.field_224 = uint16(m_param3)
  else:
      mstorF652m[mstor6m.lengthm]m.field_224 = 13
      mstorF652m[mstor6m.lengthm]m.field_232 = 0
  mstorF652m[mstor6m.lengthm]m.field_240 = uint16(m_param3)
  mstorF652m[mstor6m.lengthm]m.field_256 = 0
  mstorF652m[mstor6m.lengthm]m.field_256 = 0
  require munknownc754a0a3m.length == uint32(munknownc754a0a3m.length)
  if m_param5:
      log Birth(
            address owner=addr(_param5),
            uint256 LinglongCatId=unknownc754a0a3.length,
            uint256 matronId=_param1 << 224,
            uint256 sireId=_param2 << 224,
            uint256 genes=_param3,
            uint256 generation=_param4)
      mbalanceOfm[addr(m_param5)m]++
      munknown6e037679m[mstor6m.lengthm] = m_param5
      log Transfer(
            address from=0,
            address to=addr(_param5),
            uint256 value=unknownc754a0a3.length)
  else:
      log Birth(
            address owner=cooAddress,
            uint256 LinglongCatId=unknownc754a0a3.length,
            uint256 matronId=_param1 << 224,
            uint256 sireId=_param2 << 224,
            uint256 genes=_param3,
            uint256 generation=_param4)
      mbalanceOfm[mstor1m]++
      munknown6e037679m[mstor6m.lengthm] = mcooAddress
      log Transfer(
            address from=0,
            address to=cooAddress,
            uint256 value=unknownc754a0a3.length)


# hash = 0x4b85fd55
# getter = None
# const = None
# payable = False
def setAutoBirthFee(uint256 m_val): # not payable
  require caller == mcooAddress
  mautoBirthFee = m_val


# hash = 0x4dfff04f
# getter = None
# const = None
# payable = False
def approveSiring(address m_addr, uint256 m_sireId): # not payable
  require not mpaused
  require munknown6e037679m[m_sireIdm] == caller
  msireAllowedTom[m_sireIdm] = m_addr


# hash = 0x55a373d6
# getter = ['storage', 160, 0, 14]
# const = None
# payable = False
def tokenContract(): # not payable
  return mtokenContractAddress


# hash = 0x5663896e
# getter = None
# const = None
# payable = False
def setSecondsPerBlock(uint256 m_secs): # not payable
  require caller == mceoAddress
  require m_secs < mcooldownsm.length
  msecondsPerBlock = m_secs


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 2]]
# const = None
# payable = False
def paused(): # not payable
  return bool(mpaused)


# hash = 0x5de973a5
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 9]]]
# const = None
# payable = False
def unknown5de973a5(uint256 m_param1): # not payable
  return munknown5de973a5m[m_param1m]


# hash = 0x6352211e
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def ownerOf(uint256 m_tokenId): # not payable
  require munknown6e037679m[m_tokenIdm]
  return munknown6e037679m[m_tokenIdm]


# hash = 0x680eba27
# getter = None
# const = ['return', 50000]
# payable = False
const GEN0_CREATION_LIMIT = 50000


# hash = 0x6e037679
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def unknown6e037679(uint256 m_param1): # not payable
  return munknown6e037679m[m_param1m]


# hash = 0x6fbde40d
# getter = None
# const = None
# payable = False
def setSaleAuctionAddress(address m_address): # not payable
  require caller == mceoAddress
  require ext_code.size(m_address)
  call m_address.isSaleClockAuction() with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  msaleAuctionAddress = m_address


# hash = 0x70a08231
# getter = ['storage', 256, 0, ['sha3', ['data', ['mask_shl', 160, 0, 96, ['cd', 4]], 8]]]
# const = None
# payable = False
def balanceOf(address m_owner): # not payable
  return mbalanceOfm[addr(m_owner)m]


# hash = 0x79a9232f
# getter = None
# const = None
# payable = False
def unknown79a9232f(uint256 m_param1, uint256 m_param2): # not payable
  require m_param1 < munknownc754a0a3m.length
  require m_param2 < munknownc754a0a3m.length
  if m_param1 != m_param2:
      if m_param2 != munknownc754a0a3m[m_param1m]m.field_384:
          if m_param2 != munknownc754a0a3m[m_param1m]m.field_416:
              if m_param1 != munknownc754a0a3m[m_param2m]m.field_384:
                  if m_param1 != munknownc754a0a3m[m_param2m]m.field_416:
                      if not munknownc754a0a3m[m_param2m]m.field_384:
                          return 1
                      if not munknownc754a0a3m[m_param1m]m.field_384:
                          return 1
                      if munknownc754a0a3m[m_param2m]m.field_384 != munknownc754a0a3m[m_param1m]m.field_384:
                          if munknownc754a0a3m[m_param1m]m.field_416 != munknownc754a0a3m[m_param2m]m.field_384:
                              if munknownc754a0a3m[m_param1m]m.field_384 != munknownc754a0a3m[m_param2m]m.field_416:
                                  if munknownc754a0a3m[m_param2m]m.field_416 != munknownc754a0a3m[m_param1m]m.field_416:
                                      return 1
                                  else:
                                      return 0
                              else:
                                  return 0
                          else:
                              return 0
                      else:
                          return 0
                  else:
                      return 0
              else:
                  return 0
          else:
              return 0
      else:
          return 0
  else:
      return 0


# hash = 0x7a7d4937
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def secondsPerBlock(): # not payable
  return msecondsPerBlock


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  require caller == mceoAddress
  require not mpaused
  mpaused = 1


# hash = 0x8462151c
# getter = None
# const = None
# payable = False
def tokensOfOwner(address m_owner): # not payable
  if not mbalanceOfm[addr(m_owner)m]:
      return ''
  mem[128 len 32 * mbalanceOfm[addr(m_owner)m]] = code.data[13020 len 32 * mbalanceOfm[addr(m_owner)m]]
  [94midx = 1
  [94ms = 0
  mwhile [94midx <= munknownc754a0a3m.length - 1m:
      mem[0] = [94midx
      mem[32] = 7
      if munknown6e037679m[[94midxm] != m_owner:
          [94midx = [94midx + 1
          [94ms = [94ms
          mcontinue 
      require [94ms < mbalanceOfm[addr(m_owner)m]
      mem[(32 * [94ms) + 128] = [94midx
      [94midx = [94midx + 1
      [94ms = [94ms + 1
      mcontinue 
  mem[(32 * mbalanceOfm[addr(m_owner)m]) + 192 len floor32(mbalanceOfm[addr(m_owner)m])] = mem[128 len floor32(mbalanceOfm[addr(m_owner)m])]
  return Array(len=mbalanceOfm[addr(m_owner)m], data=mem[128 len floor32(mbalanceOfm[addr(m_owner)m])], mem[(32 * mbalanceOfm[addr(m_owner)m]) + floor32(mbalanceOfm[addr(m_owner)m]) + 192 len (32 * mbalanceOfm[addr(m_owner)m]) - floor32(mbalanceOfm[addr(m_owner)m])]), 


# hash = 0x88c2a0bf
# getter = None
# const = None
# payable = False
def giveBirth(uint256 m_matronId): # not payable
  require not mpaused
  require m_matronId < munknownc754a0a3m.length
  require munknownc754a0a3m[m_matronIdm]m.field_256
  require munknownc754a0a3m[m_matronIdm]m.field_448 != 0
  require munknownc754a0a3m[m_matronIdm]m.field_320 <= uint64(block.number)
  require munknownc754a0a3m[m_matronIdm]m.field_448 < munknownc754a0a3m.length
  require ext_code.size(mgeneScienceAddress)
  call mgeneScienceAddress.mixGenes(uint256 genes1, uint256 genes2, uint256 targetBlock) with:
       gas gas_remaining wei
      args munknownc754a0a3m[m_matronIdm]m.field_0, munknownc754a0a3m[munknownc754a0a3m[m_matronIdm]m.field_448m]m.field_0, uint64(munknownc754a0a3m[m_matronIdm]m.field_320 - 1)
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require m_matronId == uint32(m_matronId)
  require munknownc754a0a3m[m_matronIdm]m.field_448 == munknownc754a0a3m[m_matronIdm]m.field_448
  if munknownc754a0a3m[m_matronIdm]m.field_496 >= munknownc754a0a3m[munknownc754a0a3m[m_matronIdm]m.field_448m]m.field_496:
      require uint16(munknownc754a0a3m[m_matronIdm]m.field_496 + 1) == uint16(munknownc754a0a3m[m_matronIdm]m.field_496 + 1)
      munknownc754a0a3m.length++
      munknownc754a0a3m[munknownc754a0a3m.lengthm]m.field_0 = ext_call.return_data[0]
      mstorF652m[mstor6m.lengthm]m.field_0 = uint64(block.timestamp)
      mstorF652m[mstor6m.lengthm]m.field_64 = 0
      mstorF652m[mstor6m.lengthm]m.field_128 = uint32(m_matronId)
      mstorF652m[mstor6m.lengthm]m.field_160 = munknownc754a0a3m[m_matronIdm]m.field_448
      mstorF652m[mstor6m.lengthm]m.field_192 = 0
      if uint16(munknownc754a0a3m[m_matronIdm]m.field_496 + 1) / 2 <= 13:
          mstorF652m[mstor6m.lengthm]m.field_224 = uint16(munknownc754a0a3m[m_matronIdm]m.field_496 + 1) / 2
          mstorF652m[mstor6m.lengthm]m.field_239 = 0
      else:
          mstorF652m[mstor6m.lengthm]m.field_224 = 13
          mstorF652m[mstor6m.lengthm]m.field_232 = 0
      mstorF652m[mstor6m.lengthm]m.field_240 = uint16(munknownc754a0a3m[m_matronIdm]m.field_496 + 1)
      mstorF652m[mstor6m.lengthm]m.field_256 = 0
      mstorF652m[mstor6m.lengthm]m.field_256 = 0
      require munknownc754a0a3m.length == uint32(munknownc754a0a3m.length)
      log Birth(
            address owner=unknown6e037679[_matronId],
            uint256 LinglongCatId=unknownc754a0a3.length,
            uint256 matronId=_matronId << 224,
            uint256 sireId=unknownc754a0a3[_matronId].field_256,
            uint256 genes=unknownc754a0a3[_matronId].field_496 + 1 << 240,
            uint256 generation=ext_call.return_data[0])
  else:
      require uint16(munknownc754a0a3m[munknownc754a0a3m[m_matronIdm]m.field_448m]m.field_496 + 1) == uint16(munknownc754a0a3m[munknownc754a0a3m[m_matronIdm]m.field_448m]m.field_496 + 1)
      munknownc754a0a3m.length++
      munknownc754a0a3m[munknownc754a0a3m.lengthm]m.field_0 = ext_call.return_data[0]
      mstorF652m[mstor6m.lengthm]m.field_0 = uint64(block.timestamp)
      mstorF652m[mstor6m.lengthm]m.field_64 = 0
      mstorF652m[mstor6m.lengthm]m.field_128 = uint32(m_matronId)
      mstorF652m[mstor6m.lengthm]m.field_160 = munknownc754a0a3m[m_matronIdm]m.field_448
      mstorF652m[mstor6m.lengthm]m.field_192 = 0
      if uint16(munknownc754a0a3m[munknownc754a0a3m[m_matronIdm]m.field_448m]m.field_496 + 1) / 2 <= 13:
          mstorF652m[mstor6m.lengthm]m.field_224 = uint16(munknownc754a0a3m[munknownc754a0a3m[m_matronIdm]m.field_448m]m.field_496 + 1) / 2
          mstorF652m[mstor6m.lengthm]m.field_239 = 0
      else:
          mstorF652m[mstor6m.lengthm]m.field_224 = 13
          mstorF652m[mstor6m.lengthm]m.field_232 = 0
      mstorF652m[mstor6m.lengthm]m.field_240 = uint16(munknownc754a0a3m[munknownc754a0a3m[m_matronIdm]m.field_448m]m.field_496 + 1)
      mstorF652m[mstor6m.lengthm]m.field_256 = 0
      mstorF652m[mstor6m.lengthm]m.field_256 = 0
      require munknownc754a0a3m.length == uint32(munknownc754a0a3m.length)
      log Birth(
            address owner=unknown6e037679[_matronId],
            uint256 LinglongCatId=unknownc754a0a3.length,
            uint256 matronId=_matronId << 224,
            uint256 sireId=unknownc754a0a3[_matronId].field_256,
            uint256 genes=unknownc754a0a3[unknownc754a0a3[_matronId].field_448].field_496 + 1 << 240,
            uint256 generation=ext_call.return_data[0])
  mbalanceOfm[mstor7m[m_matronIdm]m]++
  munknown6e037679m[mstor6m.lengthm] = munknown6e037679m[m_matronIdm]
  log Transfer(
        address from=0,
        address to=unknown6e037679[_matronId],
        uint256 value=unknownc754a0a3.length)
  munknownc754a0a3m[m_matronIdm]m.field_448 = 0
  munknownb9b8ea8e--
  return munknownc754a0a3m.length


# hash = 0x92f64cce
# getter = None
# const = None
# payable = False
def unknown92f64cce(uint256 m_param1, uint256 m_param2, uint256 m_param3): # not payable
  require not mpaused
  require m_param3 >= mautoBirthFee
  require munknown6e037679m[m_param1m] == caller
  if munknown6e037679m[m_param1m] != munknown6e037679m[m_param2m]:
      require munknown6e037679m[m_param1m] == msireAllowedTom[m_param2m]
  require m_param1 < munknownc754a0a3m.length
  require 0 == munknownc754a0a3m[m_param1m]m.field_448
  require munknownc754a0a3m[m_param1m]m.field_320 <= uint64(block.number)
  require m_param2 < munknownc754a0a3m.length
  require 0 == munknownc754a0a3m[m_param2m]m.field_448
  require munknownc754a0a3m[m_param2m]m.field_320 <= uint64(block.number)
  require m_param1 != m_param2
  require m_param2 != munknownc754a0a3m[m_param1m]m.field_384
  require m_param2 != munknownc754a0a3m[m_param1m]m.field_416
  require m_param1 != munknownc754a0a3m[m_param2m]m.field_384
  require m_param1 != munknownc754a0a3m[m_param2m]m.field_416
  if munknownc754a0a3m[m_param2m]m.field_384:
      if munknownc754a0a3m[m_param1m]m.field_384:
          require munknownc754a0a3m[m_param2m]m.field_384 != munknownc754a0a3m[m_param1m]m.field_384
          require munknownc754a0a3m[m_param1m]m.field_416 != munknownc754a0a3m[m_param2m]m.field_384
          require munknownc754a0a3m[m_param1m]m.field_384 != munknownc754a0a3m[m_param2m]m.field_416
          require munknownc754a0a3m[m_param2m]m.field_416 != munknownc754a0a3m[m_param1m]m.field_416
  require not mpaused
  if m_param3:
      if caller != caller:
          if msaleAuctionAddress != caller:
              if msiringAuctionAddress != caller:
                  require caller == munknowne86d5083Address
      require this.address
      require m_param3 <= mtokenBalanceOfm[callerm]
      require mtokenBalanceOfm[addr(this.address)m] + m_param3 > mtokenBalanceOfm[addr(this.address)m]
      mtokenBalanceOfm[callerm] -= m_param3
      mtokenBalanceOfm[addr(this.address)m] += m_param3
      require mtokenBalanceOfm[addr(this.address)m] + mtokenBalanceOfm[callerm] == mtokenBalanceOfm[callerm] + m_param3 + mtokenBalanceOfm[addr(this.address)m]
      log TransferToken(
            address from=caller,
            address to=addr(this.address),
            uint256 tokenId=_param3)
  require m_param2 < munknownc754a0a3m.length
  require m_param1 < munknownc754a0a3m.length
  munknownc754a0a3m[m_param1m]m.field_448 = uint32(m_param2)
  require munknownc754a0a3m[m_param2m]m.field_480 < 14
  require msecondsPerBlock
  munknownc754a0a3m[m_param2m]m.field_320 = uint64((mcooldownsm[mstor6m[m_param2m]m.field_480m] / msecondsPerBlock) + block.number)
  if munknownc754a0a3m[m_param2m]m.field_480 < 13:
      munknownc754a0a3m[m_param2m]m.field_480 = uint16(munknownc754a0a3m[m_param2m]m.field_480 + 1)
  require munknownc754a0a3m[m_param1m]m.field_480 < 14
  require msecondsPerBlock
  munknownc754a0a3m[m_param1m]m.field_320 = uint64((mcooldownsm[mstor6m[m_param1m]m.field_480m] / msecondsPerBlock) + block.number)
  if munknownc754a0a3m[m_param1m]m.field_480 < 13:
      munknownc754a0a3m[m_param1m]m.field_480 = uint16(munknownc754a0a3m[m_param1m]m.field_480 + 1)
  msireAllowedTom[m_param1m] = 0
  msireAllowedTom[m_param2m] = 0
  munknownb9b8ea8e++
  log Pregnant(
        address owner=unknown6e037679[_param1],
        uint256 mareId=_param1,
        uint256 stallionId=_param2,
        uint256 unproductiveEndBlock=unknownc754a0a3[_param1].field_320)


# hash = 0x95d89b41
# getter = None
# const = ['return', ['data', ['arr', 2, ['mask_shl', 16, 0, 0, "'CF'"]]]]
# payable = False
const symbol = 'CF'


# hash = 0x9d6fac6f
# getter = ['storage', 32, ['mask_shl', 3, 0, 5, ['cd', 4]], ['add', 3, ['mask_shl', 253, 3, -3, ['cd', 4]]]]
# const = None
# payable = False
def cooldowns(uint256 m_param1): # not payable
  require m_param1 < 14
  return mcooldownsm[uint8(m_param1)m]


# hash = 0xa1045d73
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def unknowna1045d73(): # not payable
  return munknowna1045d73Address


# hash = 0xa9059cbb
# getter = None
# const = None
# payable = False
def transfer(address m_to, uint256 m_value): # not payable
  require not mpaused
  require m_to
  require m_to != this.address
  require msaleAuctionAddress != m_to
  require msiringAuctionAddress != m_to
  require munknowne86d5083Address != m_to
  require munknown6e037679m[m_valuem] == caller
  mbalanceOfm[addr(m_to)m]++
  munknown6e037679m[m_valuem] = m_to
  if caller:
      mbalanceOfm[callerm]--
      msireAllowedTom[m_valuem] = 0
      munknown5de973a5m[m_valuem] = 0
  log Transfer(
        address from=caller,
        address to=addr(_to),
        uint256 value=_value)


# hash = 0xad221195
# getter = None
# const = None
# payable = False
def transferTokenFrom(address m_from, address m_to, uint256 m_tokenId): # not payable
  require not mpaused
  if m_tokenId:
      if m_from != caller:
          if msaleAuctionAddress != caller:
              if msiringAuctionAddress != caller:
                  require caller == munknowne86d5083Address
      require m_to
      require m_tokenId <= mtokenBalanceOfm[addr(m_from)m]
      require mtokenBalanceOfm[addr(m_to)m] + m_tokenId > mtokenBalanceOfm[addr(m_to)m]
      mtokenBalanceOfm[m_fromm] -= m_tokenId
      mtokenBalanceOfm[addr(m_to)m] += m_tokenId
      require mtokenBalanceOfm[addr(m_to)m] + mtokenBalanceOfm[m_fromm] == mtokenBalanceOfm[m_fromm] + m_tokenId + mtokenBalanceOfm[addr(m_to)m]
      log TransferToken(
            address from=addr(_from),
            address to=addr(_to),
            uint256 tokenId=_tokenId)


# hash = 0xb047fb50
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def cooAddress(): # not payable
  return mcooAddress


# hash = 0xb0c35c05
# getter = ['storage', 256, 0, 16]
# const = None
# payable = False
def autoBirthFee(): # not payable
  return mautoBirthFee


# hash = 0xb9b8ea8e
# getter = ['storage', 256, 0, 17]
# const = None
# payable = False
def unknownb9b8ea8e(): # not payable
  return munknownb9b8ea8e


# hash = 0xc3bea9af
# getter = None
# const = None
# payable = False
def createGen0Auction(uint256 m_pandaId): # not payable
  require caller == mcooAddress
  require 50000 > mgen0CreatedCount
  munknownc754a0a3m.length++
  munknownc754a0a3m[munknownc754a0a3m.lengthm]m.field_0 = m_pandaId
  mstorF652m[mstor6m.lengthm]m.field_0 = uint64(block.timestamp)
  mstorF652m[mstor6m.lengthm]m.field_64 = 0
  mstorF652m[mstor6m.lengthm]m.field_256 = 0
  mstorF652m[mstor6m.lengthm]m.field_256 = 0
  mstorF652m[mstor6m.lengthm]m.field_256 = 0
  mstorF652m[mstor6m.lengthm]m.field_256 = 0
  mstorF652m[mstor6m.lengthm]m.field_256 = 0
  mstorF652m[mstor6m.lengthm]m.field_256 = 0
  require munknownc754a0a3m.length == uint32(munknownc754a0a3m.length)
  log Birth(
        address owner=addr(this.address),
        uint256 LinglongCatId=unknownc754a0a3.length,
        uint256 matronId=0,
        uint256 sireId=0,
        uint256 genes=0,
        uint256 generation=_pandaId)
  mbalanceOfm[addr(this.address)m]++
  munknown6e037679m[mstor6m.lengthm] = this.address
  log Transfer(
        address from=0,
        address to=addr(this.address),
        uint256 value=unknownc754a0a3.length)
  munknown5de973a5m[mstor6m.lengthm] = msaleAuctionAddress
  require ext_code.size(msaleAuctionAddress)
  call msaleAuctionAddress.0xa912873 with:
       gas gas_remaining wei
      args munknownc754a0a3m.length, 500, 500, 240 * 24 * 3600, this.address, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  mgen0CreatedCount++


# hash = 0xc754a0a3
# getter = ['struct', ['loc', 6]]
# const = None
# payable = False
def unknownc754a0a3(uint256 m_param1): # not payable
  require m_param1 < munknownc754a0a3m.length
  return munknownc754a0a3m[m_param1m]m.field_448 != 0, 
         munknownc754a0a3m[m_param1m]m.field_320 <= block.number,
         munknownc754a0a3m[m_param1m]m.field_256,
         munknownc754a0a3m[m_param1m]m.field_256,
         munknownc754a0a3m[m_param1m]m.field_448,
         munknownc754a0a3m[m_param1m]m.field_256,
         munknownc754a0a3m[m_param1m]m.field_256,
         munknownc754a0a3m[m_param1m]m.field_256,
         munknownc754a0a3m[m_param1m]m.field_256,
         munknownc754a0a3m[m_param1m]m.field_0


# hash = 0xd3e6f49f
# getter = None
# const = None
# payable = False
def isReadyToBreed(uint256 m_tokenId): # not payable
  require m_tokenId > 0
  require m_tokenId < munknownc754a0a3m.length
  if munknownc754a0a3m[m_tokenIdm]m.field_448 != 0:
      return (0 == munknownc754a0a3m[m_tokenIdm]m.field_256)
  return munknownc754a0a3m[m_tokenIdm]m.field_256 <= uint64(block.number)


# hash = 0xdefb9584
# getter = None
# const = ['return', 50000]
# payable = False
const PROMO_CREATION_LIMIT = 50000


# hash = 0xe42c08f2
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 15]]]
# const = None
# payable = False
def tokenBalanceOf(address m_param1): # not payable
  return mtokenBalanceOfm[m_param1m]


# hash = 0xe6cbe351
# getter = ['storage', 160, 0, 11]
# const = None
# payable = False
def saleAuction(): # not payable
  return msaleAuctionAddress


# hash = 0xe86d5083
# getter = ['storage', 160, 0, 13]
# const = None
# payable = False
def unknowne86d5083(): # not payable
  return munknowne86d5083Address


# hash = 0xef299b0b
# getter = None
# const = None
# payable = False
def unknownef299b0b(uint256 m_param1): # not payable
  require mtokenBalanceOfm[callerm] + m_param1 > mtokenBalanceOfm[callerm]
  require ext_code.size(mtokenContractAddress)
  call mtokenContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args caller, this.address, m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[0]
  mtokenBalanceOfm[callerm] += m_param1


# hash = 0xf1ca9410
# getter = ['storage', 256, 0, 20]
# const = None
# payable = False
def gen0CreatedCount(): # not payable
  return mgen0CreatedCount


# hash = 0xf2b47d52
# getter = ['storage', 160, 0, 18]
# const = None
# payable = False
def geneScience(): # not payable
  return mgeneScienceAddress


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


