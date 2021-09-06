# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x57028E37CE309cefF1D31c77c9384C75883F8c4a 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    paused # mask: a s
    # storage address 0
    isSaleClockAuction # mask: a s
    # storage address 0
    owner # mask: a s
    # storage address 1
    nonFungibleContractAddress # mask: a s
    # storage address 2
    commission # mask: a s
    # storage address 3
    auction
    # storage address 4
    unknown617746d4
# hash = 0x27ebe40a
# getter = None
# const = None
# payable = False
def createAuction(uint256 _tokenId, uint256 _startingPrice, uint256 _endingPrice, uint256 _duration, address _seller): # not payable
  require _startingPrice < 0xffffffffffffffffffffffffffffffff
  require _endingPrice < 0xffffffffffffffffffffffffffffffff
  require _duration <= 18446744073709551615
  require caller == nonFungibleContractAddress
  require ext_code.size(nonFungibleContractAddress)
  call nonFungibleContractAddress.ownerOf(uint256 tokenId) with:
       gas gas_remaining wei
      args _tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_call.return_data[12 len 20] == _seller
  require ext_code.size(nonFungibleContractAddress)
  call nonFungibleContractAddress.transferFrom(address from, address to, uint256 value) with:
       gas gas_remaining wei
      args addr(_seller), this.address, _tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  unknown617746d4[addr(_seller)].field_0++
  unknown617746d4[addr(_seller)][unknown617746d4[addr(_seller)].field_0].field_0 = _tokenId
  require uint64(_duration) >= 60
  auction[_tokenId].field_0 = _seller
  auction[_tokenId].field_256 = uint128(_startingPrice)
  auction[_tokenId].field_384 = uint128(_endingPrice)
  auction[_tokenId].field_512 = uint64(_duration)
  auction[_tokenId].field_576 = uint64(block.timestamp)
  log AuctionCreated(
        uint256 tokenId=_tokenId,
        uint256 startingPrice=_startingPrice << 128,
        uint256 endingPrice=_endingPrice << 128,
        uint256 duration=uint64(_duration))


# hash = 0x3f4ba83a
# getter = None
# const = None
# payable = False
def unpause(): # not payable
  require caller == owner
  require paused
  paused = 0
  log Unpause()
  return 1


# hash = 0x454a2ab3
# getter = None
# const = None
# payable = True
def bid(uint256 _tokenId) payable: 
  require not paused
  require auction[_tokenId].field_576 > 0
  if block.timestamp <= auction[_tokenId].field_576:
      if 0 >= auction[_tokenId].field_512:
          require call.value >= auction[_tokenId].field_384
          auction[_tokenId].field_0 = 0
          auction[_tokenId].field_256 = 0
          auction[_tokenId].field_512 = 0
          if unknown617746d4[stor3[_tokenId].field_0].field_0 > 0:
              [94midx = 0
              [94ms = 0
              while [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                  if [94ms:
                      require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[32] = 4
                      require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[0] = sha3(auction[_tokenId].field_0, 4)
                      unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                  else:
                      mem[32] = 4
                      require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[0] = sha3(auction[_tokenId].field_0, 4)
                      if unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 == _tokenId:
                          require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[32] = 4
                          require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[0] = sha3(auction[_tokenId].field_0, 4)
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                          [94midx = [94midx + 1
                          [94ms = 1
                          continue 
                      if [94ms:
                          require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[32] = 4
                          require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[0] = sha3(auction[_tokenId].field_0, 4)
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
              if [94ms:
                  unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                  unknown617746d4[stor3[_tokenId].field_0].field_0--
                  if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                      [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                      while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                          [94midx = [94midx + 1
                          continue 
              else:
                  if unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 == _tokenId:
                      require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                      unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                      unknown617746d4[stor3[_tokenId].field_0].field_0--
                      if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                          [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                          while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                              unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                  else:
                      if [94ms:
                          require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                          unknown617746d4[stor3[_tokenId].field_0].field_0--
                          if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                              [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                              while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                                  unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
          if auction[_tokenId].field_384 <= 0:
              call caller with:
                 value call.value - auction[_tokenId].field_384 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call auction[_tokenId].field_0 with:
                 value auction[_tokenId].field_384 - (auction[_tokenId].field_384 * commission / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - auction[_tokenId].field_384 wei
                   gas 2300 * is_zero(value) wei
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=auction[_tokenId].field_256,
                address bidder=caller)
      else:
          require auction[_tokenId].field_512
          require call.value >= auction[_tokenId].field_256 + (0 /′ auction[_tokenId].field_512)
          auction[_tokenId].field_0 = 0
          auction[_tokenId].field_256 = 0
          auction[_tokenId].field_512 = 0
          if unknown617746d4[stor3[_tokenId].field_0].field_0 > 0:
              [94midx = 0
              [94ms = 0
              while [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                  if [94ms:
                      require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[32] = 4
                      require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[0] = sha3(auction[_tokenId].field_0, 4)
                      unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                  else:
                      mem[32] = 4
                      require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[0] = sha3(auction[_tokenId].field_0, 4)
                      if unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 == _tokenId:
                          require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[32] = 4
                          require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[0] = sha3(auction[_tokenId].field_0, 4)
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                          [94midx = [94midx + 1
                          [94ms = 1
                          continue 
                      if [94ms:
                          require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[32] = 4
                          require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[0] = sha3(auction[_tokenId].field_0, 4)
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
              if [94ms:
                  unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                  unknown617746d4[stor3[_tokenId].field_0].field_0--
                  if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                      [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                      while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                          [94midx = [94midx + 1
                          continue 
              else:
                  if unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 == _tokenId:
                      require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                      unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                      unknown617746d4[stor3[_tokenId].field_0].field_0--
                      if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                          [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                          while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                              unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                  else:
                      if [94ms:
                          require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                          unknown617746d4[stor3[_tokenId].field_0].field_0--
                          if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                              [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                              while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                                  unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
          if auction[_tokenId].field_256 + (0 /′ auction[_tokenId].field_512) <= 0:
              call caller with:
                 value call.value - auction[_tokenId].field_256 - (0 /′ auction[_tokenId].field_512) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call auction[_tokenId].field_0 with:
                 value auction[_tokenId].field_256 + (0 /′ auction[_tokenId].field_512) - ((auction[_tokenId].field_256 * commission) + (0 /′ auction[_tokenId].field_512 * commission) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - auction[_tokenId].field_256 - (0 /′ auction[_tokenId].field_512) wei
                   gas 2300 * is_zero(value) wei
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=auction[_tokenId].field_256 + (0 /′ auction[_tokenId].field_512),
                address bidder=caller)
  else:
      if block.timestamp - auction[_tokenId].field_576 >= auction[_tokenId].field_512:
          require call.value >= auction[_tokenId].field_384
          auction[_tokenId].field_0 = 0
          auction[_tokenId].field_256 = 0
          auction[_tokenId].field_512 = 0
          if unknown617746d4[stor3[_tokenId].field_0].field_0 > 0:
              [94midx = 0
              [94ms = 0
              while [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                  if [94ms:
                      require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[32] = 4
                      require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[0] = sha3(auction[_tokenId].field_0, 4)
                      unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                  else:
                      mem[32] = 4
                      require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[0] = sha3(auction[_tokenId].field_0, 4)
                      if unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 == _tokenId:
                          require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[32] = 4
                          require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[0] = sha3(auction[_tokenId].field_0, 4)
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                          [94midx = [94midx + 1
                          [94ms = 1
                          continue 
                      if [94ms:
                          require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[32] = 4
                          require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[0] = sha3(auction[_tokenId].field_0, 4)
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
              if [94ms:
                  unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                  unknown617746d4[stor3[_tokenId].field_0].field_0--
                  if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                      [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                      while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                          [94midx = [94midx + 1
                          continue 
              else:
                  if unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 == _tokenId:
                      require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                      unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                      unknown617746d4[stor3[_tokenId].field_0].field_0--
                      if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                          [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                          while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                              unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                  else:
                      if [94ms:
                          require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                          unknown617746d4[stor3[_tokenId].field_0].field_0--
                          if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                              [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                              while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                                  unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
          if auction[_tokenId].field_384 <= 0:
              call caller with:
                 value call.value - auction[_tokenId].field_384 wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call auction[_tokenId].field_0 with:
                 value auction[_tokenId].field_384 - (auction[_tokenId].field_384 * commission / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - auction[_tokenId].field_384 wei
                   gas 2300 * is_zero(value) wei
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=auction[_tokenId].field_256,
                address bidder=caller)
      else:
          require auction[_tokenId].field_512
          require call.value >= auction[_tokenId].field_256 + ((block.timestamp * auction[_tokenId].field_384) - (auction[_tokenId].field_576 * auction[_tokenId].field_384) - (block.timestamp * auction[_tokenId].field_256) + (auction[_tokenId].field_576 * auction[_tokenId].field_256) /′ auction[_tokenId].field_512)
          auction[_tokenId].field_0 = 0
          auction[_tokenId].field_256 = 0
          auction[_tokenId].field_512 = 0
          if unknown617746d4[stor3[_tokenId].field_0].field_0 > 0:
              [94midx = 0
              [94ms = 0
              while [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                  if [94ms:
                      require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[32] = 4
                      require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[0] = sha3(auction[_tokenId].field_0, 4)
                      unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                  else:
                      mem[32] = 4
                      require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                      mem[0] = sha3(auction[_tokenId].field_0, 4)
                      if unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 == _tokenId:
                          require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[32] = 4
                          require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[0] = sha3(auction[_tokenId].field_0, 4)
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                          [94midx = [94midx + 1
                          [94ms = 1
                          continue 
                      if [94ms:
                          require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[32] = 4
                          require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                          mem[0] = sha3(auction[_tokenId].field_0, 4)
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                  [94midx = [94midx + 1
                  [94ms = [94ms
                  continue 
              require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
              if [94ms:
                  unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                  unknown617746d4[stor3[_tokenId].field_0].field_0--
                  if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                      [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                      while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                          [94midx = [94midx + 1
                          continue 
              else:
                  if unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 == _tokenId:
                      require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                      unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                      unknown617746d4[stor3[_tokenId].field_0].field_0--
                      if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                          [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                          while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                              unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                              [94midx = [94midx + 1
                              continue 
                  else:
                      if [94ms:
                          require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                          unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                          unknown617746d4[stor3[_tokenId].field_0].field_0--
                          if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                              [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                              while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                                  unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                                  [94midx = [94midx + 1
                                  continue 
          if auction[_tokenId].field_256 + ((block.timestamp * auction[_tokenId].field_384) - (auction[_tokenId].field_576 * auction[_tokenId].field_384) - (block.timestamp * auction[_tokenId].field_256) + (auction[_tokenId].field_576 * auction[_tokenId].field_256) /′ auction[_tokenId].field_512) <= 0:
              call caller with:
                 value call.value - auction[_tokenId].field_256 - ((block.timestamp * auction[_tokenId].field_384) - (auction[_tokenId].field_576 * auction[_tokenId].field_384) - (block.timestamp * auction[_tokenId].field_256) + (auction[_tokenId].field_576 * auction[_tokenId].field_256) /′ auction[_tokenId].field_512) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
          else:
              call auction[_tokenId].field_0 with:
                 value auction[_tokenId].field_256 + ((block.timestamp * auction[_tokenId].field_384) - (auction[_tokenId].field_576 * auction[_tokenId].field_384) - (block.timestamp * auction[_tokenId].field_256) + (auction[_tokenId].field_576 * auction[_tokenId].field_256) /′ auction[_tokenId].field_512) - ((auction[_tokenId].field_256 * commission) + ((block.timestamp * auction[_tokenId].field_384) - (auction[_tokenId].field_576 * auction[_tokenId].field_384) - (block.timestamp * auction[_tokenId].field_256) + (auction[_tokenId].field_576 * auction[_tokenId].field_256) /′ auction[_tokenId].field_512 * commission) / 10000) wei
                   gas 2300 * is_zero(value) wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              call caller with:
                 value call.value - auction[_tokenId].field_256 - ((block.timestamp * auction[_tokenId].field_384) - (auction[_tokenId].field_576 * auction[_tokenId].field_384) - (block.timestamp * auction[_tokenId].field_256) + (auction[_tokenId].field_576 * auction[_tokenId].field_256) /′ auction[_tokenId].field_512) wei
                   gas 2300 * is_zero(value) wei
          log AuctionSuccessful(
                uint256 tokenId=_tokenId,
                uint256 totalPrice=auction[_tokenId].field_256 + ((block.timestamp * auction[_tokenId].field_384) - (auction[_tokenId].field_576 * auction[_tokenId].field_384) - (block.timestamp * auction[_tokenId].field_256) + (auction[_tokenId].field_576 * auction[_tokenId].field_256) /′ auction[_tokenId].field_512),
                address bidder=caller)
  require ext_code.size(nonFungibleContractAddress)
  call nonFungibleContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args caller, _tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x504bcde7
# getter = None
# const = None
# payable = False
def unknown504bcde7(addr _param1): # not payable
  if not unknown617746d4[addr(_param1)].field_0:
      mem[(32 * unknown617746d4[addr(_param1)].field_0) + 128] = 32
      mem[(32 * unknown617746d4[addr(_param1)].field_0) + 160] = unknown617746d4[addr(_param1)].field_0
      mem[(32 * unknown617746d4[addr(_param1)].field_0) + 192 len floor32(unknown617746d4[addr(_param1)].field_0)] = mem[128 len floor32(unknown617746d4[addr(_param1)].field_0)]
      return memory
        from (32 * unknown617746d4[addr(_param1)].field_0) + 128
         [93mlen (96 * unknown617746d4[addr(_param1)].field_0) + 64
  mem[128] = unknown617746d4[addr(_param1)].field_0
  [94midx = 128
  [94ms = 0
  while (32 * unknown617746d4[addr(_param1)].field_0) + 96 > [94midx:
      mem[[94midx + 32] = unknown617746d4[addr(_param1)][[94ms].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  mem[(32 * unknown617746d4[addr(_param1)].field_0) + 192 len floor32(unknown617746d4[addr(_param1)].field_0)] = mem[128 len floor32(unknown617746d4[addr(_param1)].field_0)]
  return Array(len=unknown617746d4[addr(_param1)].field_0, data=mem[128 len floor32(unknown617746d4[addr(_param1)].field_0)], mem[(32 * unknown617746d4[addr(_param1)].field_0) + floor32(unknown617746d4[addr(_param1)].field_0) + 192 len (32 * unknown617746d4[addr(_param1)].field_0) - floor32(unknown617746d4[addr(_param1)].field_0)]), 


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 160, 0]]
# const = None
# payable = False
def paused(): # not payable
  return bool(paused)


# hash = 0x5fd8c710
# getter = None
# const = None
# payable = False
def withdrawBalance(): # not payable
  if owner != caller:
      require nonFungibleContractAddress == caller
  call nonFungibleContractAddress with:
     value eth.balance(this.address) wei
       gas 2300 * is_zero(value) wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


# hash = 0x617746d4
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 4]]], ['cd', 36]]]
# const = None
# payable = False
def unknown617746d4(addr _param1, uint256 _param2): # not payable
  require _param2 < unknown617746d4[_param1].field_0
  return unknown617746d4[_param1][_param2].field_0


# hash = 0x78bd7935
# getter = ['struct', ['loc', 3]]
# const = None
# payable = False
def getAuction(uint256 _tokenId): # not payable
  require auction[_tokenId].field_576 > 0
  return auction[_tokenId].field_0, 
         auction[_tokenId].field_256,
         auction[_tokenId].field_256,
         auction[_tokenId].field_512,
         auction[_tokenId].field_576


# hash = 0x8456cb59
# getter = None
# const = None
# payable = False
def pause(): # not payable
  require caller == owner
  require not paused
  paused = 1
  log Pause()
  return 1


# hash = 0x85b86188
# getter = ['bool', ['storage', 8, 168, 0]]
# const = None
# payable = False
def isSaleClockAuction(): # not payable
  return bool(isSaleClockAuction)


# hash = 0x878eb368
# getter = None
# const = None
# payable = False
def cancelAuctionWhenPaused(uint256 _tokenId): # not payable
  require caller == owner
  require paused
  require auction[_tokenId].field_576 > 0
  auction[_tokenId].field_0 = 0
  auction[_tokenId].field_256 = 0
  auction[_tokenId].field_512 = 0
  require ext_code.size(nonFungibleContractAddress)
  call nonFungibleContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args auction[_tokenId].field_0, _tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if unknown617746d4[stor3[_tokenId].field_0].field_0 > 0:
      [94midx = 0
      [94ms = 0
      while [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
          if [94ms:
              require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
              mem[32] = 4
              require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
              mem[0] = sha3(auction[_tokenId].field_0, 4)
              unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
          else:
              mem[32] = 4
              require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
              mem[0] = sha3(auction[_tokenId].field_0, 4)
              if unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 == _tokenId:
                  require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                  mem[32] = 4
                  require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                  mem[0] = sha3(auction[_tokenId].field_0, 4)
                  unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                  [94midx = [94midx + 1
                  [94ms = 1
                  continue 
              if [94ms:
                  require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                  mem[32] = 4
                  require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                  mem[0] = sha3(auction[_tokenId].field_0, 4)
                  unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
      if [94ms:
          unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
          unknown617746d4[stor3[_tokenId].field_0].field_0--
          if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
              [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
              while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                  unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                  [94midx = [94midx + 1
                  continue 
      else:
          if unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 == _tokenId:
              require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
              unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
              unknown617746d4[stor3[_tokenId].field_0].field_0--
              if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                  [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                  while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                      unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                      [94midx = [94midx + 1
                      continue 
          else:
              if [94ms:
                  require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                  unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                  unknown617746d4[stor3[_tokenId].field_0].field_0--
                  if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                      [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                      while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                          [94midx = [94midx + 1
                          continue 
  log AuctionCancelled(uint256 tokenId=_tokenId)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 0]
# const = None
# payable = False
def owner(): # not payable
  return owner


# hash = 0x8edd6eb6
# getter = None
# const = ['return', ['balance', 'address']]
# payable = False
const getFund = eth.balance(this.address)


# hash = 0x96b5a755
# getter = None
# const = None
# payable = False
def cancelAuction(uint256 _tokenId): # not payable
  require auction[_tokenId].field_576 > 0
  require auction[_tokenId].field_0 == caller
  auction[_tokenId].field_0 = 0
  auction[_tokenId].field_256 = 0
  auction[_tokenId].field_512 = 0
  require ext_code.size(nonFungibleContractAddress)
  call nonFungibleContractAddress.transfer(address to, uint256 value) with:
       gas gas_remaining wei
      args auction[_tokenId].field_0, _tokenId
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  if unknown617746d4[stor3[_tokenId].field_0].field_0 > 0:
      [94midx = 0
      [94ms = 0
      while [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
          if [94ms:
              require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
              mem[32] = 4
              require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
              mem[0] = sha3(auction[_tokenId].field_0, 4)
              unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
          else:
              mem[32] = 4
              require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
              mem[0] = sha3(auction[_tokenId].field_0, 4)
              if unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 == _tokenId:
                  require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                  mem[32] = 4
                  require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                  mem[0] = sha3(auction[_tokenId].field_0, 4)
                  unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
                  [94midx = [94midx + 1
                  [94ms = 1
                  continue 
              if [94ms:
                  require [94midx + 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                  mem[32] = 4
                  require [94midx < unknown617746d4[stor3[_tokenId].field_0].field_0
                  mem[0] = sha3(auction[_tokenId].field_0, 4)
                  unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = unknown617746d4[stor3[_tokenId].field_0][[94midx].field_256
          [94midx = [94midx + 1
          [94ms = [94ms
          continue 
      require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
      if [94ms:
          unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
          unknown617746d4[stor3[_tokenId].field_0].field_0--
          if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
              [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
              while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                  unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                  [94midx = [94midx + 1
                  continue 
      else:
          if unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 == _tokenId:
              require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
              unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
              unknown617746d4[stor3[_tokenId].field_0].field_0--
              if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                  [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                  while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                      unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                      [94midx = [94midx + 1
                      continue 
          else:
              if [94ms:
                  require unknown617746d4[stor3[_tokenId].field_0].field_0 - 1 < unknown617746d4[stor3[_tokenId].field_0].field_0
                  unknown617746d4[stor3[_tokenId].field_0][unknown617746d4[stor3[_tokenId].field_0].field_0].field_0 = 0
                  unknown617746d4[stor3[_tokenId].field_0].field_0--
                  if unknown617746d4[stor3[_tokenId].field_0].field_0 > unknown617746d4[stor3[_tokenId].field_0].field_0 - 1:
                      [94midx = unknown617746d4[stor3[_tokenId].field_0].field_0 - 1
                      while unknown617746d4[stor3[_tokenId].field_0].field_0 > [94midx:
                          unknown617746d4[stor3[_tokenId].field_0][[94midx].field_0 = 0
                          [94midx = [94midx + 1
                          continue 
  log AuctionCancelled(uint256 tokenId=_tokenId)


# hash = 0xc55d0f56
# getter = None
# const = None
# payable = False
def getCurrentPrice(uint256 _tokenId): # not payable
  require auction[_tokenId].field_576 > 0
  if block.timestamp <= auction[_tokenId].field_576:
      if 0 >= auction[_tokenId].field_512:
          return auction[_tokenId].field_384
      if auction[_tokenId].field_512:
          return (auction[_tokenId].field_256 + (0 /′ auction[_tokenId].field_512))
  else:
      if block.timestamp - auction[_tokenId].field_576 >= auction[_tokenId].field_512:
          return auction[_tokenId].field_384
      if auction[_tokenId].field_512:
          return (auction[_tokenId].field_256 + ((block.timestamp * auction[_tokenId].field_384) - (auction[_tokenId].field_576 * auction[_tokenId].field_384) - (block.timestamp * auction[_tokenId].field_256) + (auction[_tokenId].field_576 * auction[_tokenId].field_256) /′ auction[_tokenId].field_512))
  ('iszero', ('field', 512, ('stor', ('map', ('param', '_tokenId'), ('name', 'auction', 3)))))
  revert


# hash = 0xdd1b7a0f
# getter = ['storage', 160, 0, 1]
# const = None
# payable = False
def nonFungibleContract(): # not payable
  return nonFungibleContractAddress


# hash = 0xe1489191
# getter = ['storage', 256, 0, 2]
# const = None
# payable = False
def commission(): # not payable
  return commission


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = False
def transferOwnership(address _newOwner): # not payable
  require caller == owner
  if _newOwner:
      owner = _newOwner


# hash = _fallback()
# getter = None
# const = None
# payable = False
def _fallback(): # not payable, default function
  stop


