# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xf79bcC67B915ba1FA11c77670ED6F2B5Ae1297a2 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    owner # mask: a s
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    nonFungibleContractAddress # mask: a s
    # storage address 2
    ownerCut # mask: a s
    # storage address 3
    auction
    # storage address 4
    unknown13e063d9 # mask: a s
# hash = 0x13e063d9
# getter = ['bool', ['storage', 8, 0, 4]]
# const = None
# payable = False
def unknown13e063d9(): # not payable
  return bool(munknown13e063d9)


# hash = 0x27ebe40a
# getter = None
# const = None
# payable = False
def createAuction(uint256 m_tokenId, uint256 m_startingPrice, uint256 m_endingPrice, uint256 m_duration, address m_seller): # not payable
  require calldata.size - 4 >= 160
  require m_startingPrice == uint128(m_startingPrice)
  require m_endingPrice == uint128(m_endingPrice)
  require m_duration == uint64(m_duration)
  require caller == mnonFungibleContractAddress
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(m_seller), this.address, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require uint64(m_duration) >= 60
  mauctionm[m_tokenIdm]m.field_0 = m_seller
  mauctionm[m_tokenIdm]m.field_256 = uint128(m_startingPrice)
  mauctionm[m_tokenIdm]m.field_384 = uint128(m_endingPrice)
  mauctionm[m_tokenIdm]m.field_512 = uint64(m_duration)
  mauctionm[m_tokenIdm]m.field_576 = uint64(block.timestamp)
  log AuctionCreated(
        address contract=0,
        uint256 tokenId=_endingPrice << 128,
        uint256 startingPrice=uint64(_duration),
        uint256 endingPrice=_seller,
        uint256 duration=_tokenId)


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require mstor0
  mstor0 = 0
  log Unpause()
  return 1


# hash = 0x5afb9775
# getter = None
# const = None
# payable = True
def unknown5afb9775(uint256 m_param1, addr m_param2, uint8 m_param3) payable: 
  require calldata.size - 4 >= 96
  require caller == mnonFungibleContractAddress
  require mauctionm[m_param1m]m.field_576
  if block.timestamp <= mauctionm[m_param1m]m.field_576:
      if 0 >= mauctionm[m_param1m]m.field_512:
          require call.value >= (uint8(10 * m_param3) * mauctionm[m_param1m]m.field_384 / 100) + mauctionm[m_param1m]m.field_384
          mauctionm[m_param1m]m.field_0 = 0
          mauctionm[m_param1m]m.field_256 = 0
          mauctionm[m_param1m]m.field_512 = 0
          if not mauctionm[m_param1m]m.field_384:
              call m_param2 with:
                 value call.value - (uint8(10 * m_param3) * mauctionm[m_param1m]m.field_384 / 100) - mauctionm[m_param1m]m.field_384 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_param1m]m.field_0 with:
                 value (uint8(10 * m_param3) * mauctionm[m_param1m]m.field_384 / 100) + mauctionm[m_param1m]m.field_384 - ((uint8(10 * m_param3) * mauctionm[m_param1m]m.field_384 / 100 * mownerCut) + (mauctionm[m_param1m]m.field_384 * mownerCut) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call m_param2 with:
                 value call.value - (uint8(10 * m_param3) * mauctionm[m_param1m]m.field_384 / 100) - mauctionm[m_param1m]m.field_384 wei
                   gas 2300 * is_zero(value) wei
          log 0x9dd6efc4: ((uint8(10 * _param3) * auction[_param1].field_384 / 100) + auction[_param1].field_384), _param1, auction[_param1].field_0, _param2
      else:
          require mauctionm[m_param1m]m.field_512
          require call.value >= ((mauctionm[m_param1m]m.field_256 * uint8(10 * m_param3)) + (0 /′ mauctionm[m_param1m]m.field_512 * uint8(10 * m_param3)) / 100) + mauctionm[m_param1m]m.field_256 + (0 /′ mauctionm[m_param1m]m.field_512)
          mauctionm[m_param1m]m.field_0 = 0
          mauctionm[m_param1m]m.field_256 = 0
          mauctionm[m_param1m]m.field_512 = 0
          if not mauctionm[m_param1m]m.field_256 + (0 /′ mauctionm[m_param1m]m.field_512):
              call m_param2 with:
                 value call.value - ((mauctionm[m_param1m]m.field_256 * uint8(10 * m_param3)) + (0 /′ mauctionm[m_param1m]m.field_512 * uint8(10 * m_param3)) / 100) - mauctionm[m_param1m]m.field_256 - (0 /′ mauctionm[m_param1m]m.field_512) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_param1m]m.field_0 with:
                 value ((mauctionm[m_param1m]m.field_256 * uint8(10 * m_param3)) + (0 /′ mauctionm[m_param1m]m.field_512 * uint8(10 * m_param3)) / 100) + mauctionm[m_param1m]m.field_256 + (0 /′ mauctionm[m_param1m]m.field_512) - (((mauctionm[m_param1m]m.field_256 * uint8(10 * m_param3)) + (0 /′ mauctionm[m_param1m]m.field_512 * uint8(10 * m_param3)) / 100 * mownerCut) + (mauctionm[m_param1m]m.field_256 * mownerCut) + (0 /′ mauctionm[m_param1m]m.field_512 * mownerCut) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call m_param2 with:
                 value call.value - ((mauctionm[m_param1m]m.field_256 * uint8(10 * m_param3)) + (0 /′ mauctionm[m_param1m]m.field_512 * uint8(10 * m_param3)) / 100) - mauctionm[m_param1m]m.field_256 - (0 /′ mauctionm[m_param1m]m.field_512) wei
                   gas 2300 * is_zero(value) wei
          log 0x9dd6efc4: (((auction[_param1].field_256 * uint8(10 * _param3)) + (0 /′ auction[_param1].field_512 * uint8(10 * _param3)) / 100) + auction[_param1].field_256 + (0 /′ auction[_param1].field_512)), _param1, auction[_param1].field_0, _param2
  else:
      if block.timestamp - mauctionm[m_param1m]m.field_576 >= mauctionm[m_param1m]m.field_512:
          require call.value >= (uint8(10 * m_param3) * mauctionm[m_param1m]m.field_384 / 100) + mauctionm[m_param1m]m.field_384
          mauctionm[m_param1m]m.field_0 = 0
          mauctionm[m_param1m]m.field_256 = 0
          mauctionm[m_param1m]m.field_512 = 0
          if not mauctionm[m_param1m]m.field_384:
              call m_param2 with:
                 value call.value - (uint8(10 * m_param3) * mauctionm[m_param1m]m.field_384 / 100) - mauctionm[m_param1m]m.field_384 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_param1m]m.field_0 with:
                 value (uint8(10 * m_param3) * mauctionm[m_param1m]m.field_384 / 100) + mauctionm[m_param1m]m.field_384 - ((uint8(10 * m_param3) * mauctionm[m_param1m]m.field_384 / 100 * mownerCut) + (mauctionm[m_param1m]m.field_384 * mownerCut) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call m_param2 with:
                 value call.value - (uint8(10 * m_param3) * mauctionm[m_param1m]m.field_384 / 100) - mauctionm[m_param1m]m.field_384 wei
                   gas 2300 * is_zero(value) wei
          log 0x9dd6efc4: ((uint8(10 * _param3) * auction[_param1].field_384 / 100) + auction[_param1].field_384), _param1, auction[_param1].field_0, _param2
      else:
          require mauctionm[m_param1m]m.field_512
          require call.value >= ((mauctionm[m_param1m]m.field_256 * uint8(10 * m_param3)) + ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512 * uint8(10 * m_param3)) / 100) + mauctionm[m_param1m]m.field_256 + ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512)
          mauctionm[m_param1m]m.field_0 = 0
          mauctionm[m_param1m]m.field_256 = 0
          mauctionm[m_param1m]m.field_512 = 0
          if not mauctionm[m_param1m]m.field_256 + ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512):
              call m_param2 with:
                 value call.value - ((mauctionm[m_param1m]m.field_256 * uint8(10 * m_param3)) + ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512 * uint8(10 * m_param3)) / 100) - mauctionm[m_param1m]m.field_256 - ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_param1m]m.field_0 with:
                 value ((mauctionm[m_param1m]m.field_256 * uint8(10 * m_param3)) + ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512 * uint8(10 * m_param3)) / 100) + mauctionm[m_param1m]m.field_256 + ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512) - (((mauctionm[m_param1m]m.field_256 * uint8(10 * m_param3)) + ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512 * uint8(10 * m_param3)) / 100 * mownerCut) + (mauctionm[m_param1m]m.field_256 * mownerCut) + ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512 * mownerCut) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call m_param2 with:
                 value call.value - ((mauctionm[m_param1m]m.field_256 * uint8(10 * m_param3)) + ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512 * uint8(10 * m_param3)) / 100) - mauctionm[m_param1m]m.field_256 - ((block.timestamp * mauctionm[m_param1m]m.field_384) - (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_384) - (block.timestamp * mauctionm[m_param1m]m.field_256) + (mauctionm[m_param1m]m.field_576 * mauctionm[m_param1m]m.field_256) /′ mauctionm[m_param1m]m.field_512) wei
                   gas 2300 * is_zero(value) wei
          log 0x9dd6efc4: (((auction[_param1].field_256 * uint8(10 * _param3)) + ((block.timestamp * auction[_param1].field_384) - (auction[_param1].field_576 * auction[_param1].field_384) - (block.timestamp * auction[_param1].field_256) + (auction[_param1].field_576 * auction[_param1].field_256) /′ auction[_param1].field_512 * uint8(10 * _param3)) / 100) + auction[_param1].field_256 + ((block.timestamp * auction[_param1].field_384) - (auction[_param1].field_576 * auction[_param1].field_384) - (block.timestamp * auction[_param1].field_256) + (auction[_param1].field_576 * auction[_param1].field_256) /′ auction[_param1].field_512)), _param1, auction[_param1].field_0, _param2
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mauctionm[m_param1m]m.field_0, m_param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 0]]
# const = None
# payable = False
def paused(): # not payable
  return bool(mstor0)


# hash = 0x5fd8c710
# getter = None
# const = None
# payable = False
def withdrawBalance(): # not payable
  if mowner != caller:
      require mnonFungibleContractAddress == caller
  call mnonFungibleContractAddress with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei


# hash = 0x60c1e048
# getter = None
# const = None
# payable = False
def unknown60c1e048(uint256 m_param1, uint8 m_param2): # not payable
  require calldata.size - 4 >= 64
  return (uint8(10 * m_param2) * m_param1 / 100)


# hash = 0x715018a6
# getter = None
# const = None
# payable = False
def renounceOwnership(): # not payable
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  log OwnershipRenounced(address previousOwner=owner)
  mowner = 0


# hash = 0x78bd7935
# getter = ['struct', ['loc', 3]]
# const = None
# payable = False
def getAuction(uint256 m_tokenId): # not payable
  require calldata.size - 4 >= 32
  if not mauctionm[m_tokenIdm]m.field_576:
      revert with 0, 'not on auction'
  return mauctionm[m_tokenIdm]m.field_0, 
         mauctionm[m_tokenIdm]m.field_256,
         mauctionm[m_tokenIdm]m.field_256,
         mauctionm[m_tokenIdm]m.field_512,
         mauctionm[m_tokenIdm]m.field_576


# hash = 0x83b5ff8b
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def ownerCut(): # not payable
  return mownerCut


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  require not mstor0
  mstor0 = 1
  log Pause()
  return 1


# hash = 0x878eb368
# getter = None
# const = None
# payable = False
def cancelAuctionWhenPaused(uint256 m_tokenId): # not payable
  require calldata.size - 4 >= 32
  require mstor0
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
  if not mauctionm[m_tokenIdm]m.field_576:
      revert with 0, 'not on auction'
  mauctionm[m_tokenIdm]m.field_0 = 0
  mauctionm[m_tokenIdm]m.field_256 = 0
  mauctionm[m_tokenIdm]m.field_512 = 0
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mauctionm[m_tokenIdm]m.field_0, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log AuctionCancelled(uint256 tokenId=_tokenId)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return mowner


# hash = 0x96b5a755
# getter = None
# const = None
# payable = False
def cancelAuction(uint256 m_tokenId): # not payable
  require calldata.size - 4 >= 32
  if not mauctionm[m_tokenIdm]m.field_576:
      revert with 0, 'not on auction'
  if mauctionm[m_tokenIdm]m.field_0 != caller:
      revert with 0, 'not seller'
  mauctionm[m_tokenIdm]m.field_0 = 0
  mauctionm[m_tokenIdm]m.field_256 = 0
  mauctionm[m_tokenIdm]m.field_512 = 0
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mauctionm[m_tokenIdm]m.field_0, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  log AuctionCancelled(uint256 tokenId=_tokenId)


# hash = 0x9f04996d
# getter = None
# const = None
# payable = True
def bid(uint256 m_tokenId, address m_bidder) payable: 
  require calldata.size - 4 >= 64
  require caller == mnonFungibleContractAddress
  require mauctionm[m_tokenIdm]m.field_576
  if block.timestamp <= mauctionm[m_tokenIdm]m.field_576:
      if 0 >= mauctionm[m_tokenIdm]m.field_512:
          require call.value >= mauctionm[m_tokenIdm]m.field_384
          mauctionm[m_tokenIdm]m.field_0 = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          mauctionm[m_tokenIdm]m.field_512 = 0
          if not mauctionm[m_tokenIdm]m.field_384:
              call m_bidder with:
                 value call.value - mauctionm[m_tokenIdm]m.field_384 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_tokenIdm]m.field_0 with:
                 value mauctionm[m_tokenIdm]m.field_384 - (mauctionm[m_tokenIdm]m.field_384 * mownerCut / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call m_bidder with:
                 value call.value - mauctionm[m_tokenIdm]m.field_384 wei
                   gas 2300 * is_zero(value) wei
          log 0x9dd6efc4: auction[_tokenId].field_384, _tokenId, auction[_tokenId].field_0, _bidder
      else:
          require mauctionm[m_tokenIdm]m.field_512
          require call.value >= mauctionm[m_tokenIdm]m.field_256 + (0 /′ mauctionm[m_tokenIdm]m.field_512)
          mauctionm[m_tokenIdm]m.field_0 = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          mauctionm[m_tokenIdm]m.field_512 = 0
          if not mauctionm[m_tokenIdm]m.field_256 + (0 /′ mauctionm[m_tokenIdm]m.field_512):
              call m_bidder with:
                 value call.value - mauctionm[m_tokenIdm]m.field_256 - (0 /′ mauctionm[m_tokenIdm]m.field_512) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_tokenIdm]m.field_0 with:
                 value mauctionm[m_tokenIdm]m.field_256 + (0 /′ mauctionm[m_tokenIdm]m.field_512) - ((mauctionm[m_tokenIdm]m.field_256 * mownerCut) + (0 /′ mauctionm[m_tokenIdm]m.field_512 * mownerCut) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call m_bidder with:
                 value call.value - mauctionm[m_tokenIdm]m.field_256 - (0 /′ mauctionm[m_tokenIdm]m.field_512) wei
                   gas 2300 * is_zero(value) wei
          log 0x9dd6efc4: (auction[_tokenId].field_256 + (0 /′ auction[_tokenId].field_512)), _tokenId, auction[_tokenId].field_0, _bidder
  else:
      if block.timestamp - mauctionm[m_tokenIdm]m.field_576 >= mauctionm[m_tokenIdm]m.field_512:
          require call.value >= mauctionm[m_tokenIdm]m.field_384
          mauctionm[m_tokenIdm]m.field_0 = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          mauctionm[m_tokenIdm]m.field_512 = 0
          if not mauctionm[m_tokenIdm]m.field_384:
              call m_bidder with:
                 value call.value - mauctionm[m_tokenIdm]m.field_384 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_tokenIdm]m.field_0 with:
                 value mauctionm[m_tokenIdm]m.field_384 - (mauctionm[m_tokenIdm]m.field_384 * mownerCut / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call m_bidder with:
                 value call.value - mauctionm[m_tokenIdm]m.field_384 wei
                   gas 2300 * is_zero(value) wei
          log 0x9dd6efc4: auction[_tokenId].field_384, _tokenId, auction[_tokenId].field_0, _bidder
      else:
          require mauctionm[m_tokenIdm]m.field_512
          require call.value >= mauctionm[m_tokenIdm]m.field_256 + ((block.timestamp * mauctionm[m_tokenIdm]m.field_384) - (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_384) - (block.timestamp * mauctionm[m_tokenIdm]m.field_256) + (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_256) /′ mauctionm[m_tokenIdm]m.field_512)
          mauctionm[m_tokenIdm]m.field_0 = 0
          mauctionm[m_tokenIdm]m.field_256 = 0
          mauctionm[m_tokenIdm]m.field_512 = 0
          if not mauctionm[m_tokenIdm]m.field_256 + ((block.timestamp * mauctionm[m_tokenIdm]m.field_384) - (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_384) - (block.timestamp * mauctionm[m_tokenIdm]m.field_256) + (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_256) /′ mauctionm[m_tokenIdm]m.field_512):
              call m_bidder with:
                 value call.value - mauctionm[m_tokenIdm]m.field_256 - ((block.timestamp * mauctionm[m_tokenIdm]m.field_384) - (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_384) - (block.timestamp * mauctionm[m_tokenIdm]m.field_256) + (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_256) /′ mauctionm[m_tokenIdm]m.field_512) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call mauctionm[m_tokenIdm]m.field_0 with:
                 value mauctionm[m_tokenIdm]m.field_256 + ((block.timestamp * mauctionm[m_tokenIdm]m.field_384) - (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_384) - (block.timestamp * mauctionm[m_tokenIdm]m.field_256) + (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_256) /′ mauctionm[m_tokenIdm]m.field_512) - ((mauctionm[m_tokenIdm]m.field_256 * mownerCut) + ((block.timestamp * mauctionm[m_tokenIdm]m.field_384) - (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_384) - (block.timestamp * mauctionm[m_tokenIdm]m.field_256) + (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_256) /′ mauctionm[m_tokenIdm]m.field_512 * mownerCut) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call m_bidder with:
                 value call.value - mauctionm[m_tokenIdm]m.field_256 - ((block.timestamp * mauctionm[m_tokenIdm]m.field_384) - (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_384) - (block.timestamp * mauctionm[m_tokenIdm]m.field_256) + (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_256) /′ mauctionm[m_tokenIdm]m.field_512) wei
                   gas 2300 * is_zero(value) wei
          log 0x9dd6efc4: (auction[_tokenId].field_256 + ((block.timestamp * auction[_tokenId].field_384) - (auction[_tokenId].field_576 * auction[_tokenId].field_384) - (block.timestamp * auction[_tokenId].field_256) + (auction[_tokenId].field_576 * auction[_tokenId].field_256) /′ auction[_tokenId].field_512)), _tokenId, auction[_tokenId].field_0, _bidder
  require ext_code.size(mnonFungibleContractAddress)
  call mnonFungibleContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args mauctionm[m_tokenIdm]m.field_0, m_tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0xc55d0f56
# getter = None
# const = None
# payable = False
def getCurrentPrice(uint256 m_tokenId): # not payable
  require calldata.size - 4 >= 32
  if not mauctionm[m_tokenIdm]m.field_576:
      revert with 0, 'not on auction'
  if block.timestamp <= mauctionm[m_tokenIdm]m.field_576:
      if 0 >= mauctionm[m_tokenIdm]m.field_512:
          return mauctionm[m_tokenIdm]m.field_384
      if mauctionm[m_tokenIdm]m.field_512:
          return (mauctionm[m_tokenIdm]m.field_256 + (0 /′ mauctionm[m_tokenIdm]m.field_512))
  else:
      if block.timestamp - mauctionm[m_tokenIdm]m.field_576 >= mauctionm[m_tokenIdm]m.field_512:
          return mauctionm[m_tokenIdm]m.field_384
      if mauctionm[m_tokenIdm]m.field_512:
          return (mauctionm[m_tokenIdm]m.field_256 + ((block.timestamp * mauctionm[m_tokenIdm]m.field_384) - (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_384) - (block.timestamp * mauctionm[m_tokenIdm]m.field_256) + (mauctionm[m_tokenIdm]m.field_576 * mauctionm[m_tokenIdm]m.field_256) /′ mauctionm[m_tokenIdm]m.field_512))
  ('iszero', ('field', 512, ('stor', ('map', ('param', '_tokenId'), ('name', 'auction', 3)))))
  revert


# hash = 0xdd1b7a0f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def nonFungibleContract(): # not payable
  return mnonFungibleContractAddress


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address m_newOwner): # not payable
  require calldata.size - 4 >= 32
  if mowner != caller:
      revert with 0, 32, 21, 0xfe4973206e6f7420636f6e7472616374206f776e657200000000000000000000
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


